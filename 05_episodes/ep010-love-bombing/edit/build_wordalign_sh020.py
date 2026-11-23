"""Wordalign dub for ep010 sh020: clone ThaoMyVeo over native take001.

Method (proven ep008/ep009, Richard-approved 21/11):
- Native phrase windows measured by ENERGY envelope (48kHz stereo, 0.1s RMS
  buckets, threshold 0.02) on the native take; Whisper word timestamps only
  for word ORDER/count (Whisper smears onsets early — never trust its first
  word timestamp, and its per-word splits inside a phrase are noisy).
- Clone TTS phrase slices (Whisper spans, padded 0.05s) stretched with
  ffmpeg atempo to exactly the native phrase window, placed at the native
  window start. Silence elsewhere (no bed, no leak).
- Output: video copy from the 2K file, audio replaced entirely by the clone
  mono 48kHz AAC 192k track. Native audio is muted completely.

Phrase windows (native, energy):
  P1 "Tuần hai."      0.0-0.7   (TTS slice 0.00-0.52, stretch 1.346x, atempo 0.743)
  P2 "Một tin."      1.6-2.3   (TTS slice 0.90-1.32, stretch 1.667x, atempo 0.600)
  P3 "Dạo này bận quá." 3.2-4.3 (TTS slice 1.80-2.74, stretch 1.170x, atempo 0.855)
  P4 "Rồi im."        5.7-6.4   (TTS slice 3.44-4.24, stretch 0.875x, atempo 1.143)
All stretch factors within the ep009 proven range (0.60x-1.70x).
Native windows record: edit/sh020-native-windows.md
TTS wav: ~/workspace/colab-t4-test/ep010-dub/thaomy-ep010-sh020.wav
"""
import json
import pathlib
import subprocess

import numpy as np

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep010-love-bombing")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "build2k"
WORK.mkdir(parents=True, exist_ok=True)
VIDEO2K = GEN / "sh020-take001-1080p.mp4"
TTS = pathlib.Path("/home/hatch/workspace/colab-t4-test/ep010-dub/thaomy-ep010-sh020.wav")
OUT = GEN / "sh020-take001-dubbed.mp4"
SR = 48000
DUR = 7.85  # 2K video duration

# (label, native window start/end, TTS slice start/end, atempo)
PHRASES = [
    ("P1 Tuan hai.", 0.0, 0.7, 0.00, 0.52, 0.743),
    ("P2 Mot tin.", 1.6, 2.3, 0.90, 1.32, 0.600),
    ("P3 Dao nay ban qua.", 3.2, 4.3, 1.80, 2.74, 0.855),
    ("P4 Roi im.", 5.7, 6.4, 3.44, 4.24, 1.143),
]


def run(cmd, check=True):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        print("FAILED:", " ".join(str(c) for c in cmd))
        print(r.stderr[-3000:])
        raise SystemExit(1)
    return r


def probe(p):
    return json.loads(run(["ffprobe", "-v", "quiet", "-print_format", "json",
                           "-show_format", "-show_streams", str(p)]).stdout)


assert VIDEO2K.exists(), f"missing 2K video {VIDEO2K}"
assert TTS.exists(), f"missing TTS wav {TTS}"
vinfo = probe(VIDEO2K)
print(f"2K video: {vinfo['streams'][0]['width']}x{vinfo['streams'][0]['height']} "
      f"dur={float(vinfo['format']['duration']):.2f}s")

# Build the aligned mono track with numpy.
full = np.zeros(int(DUR * SR), dtype=np.float32)
report = []
for label, ns, ne, ts, te, atempo in PHRASES:
    pad = 0.05
    s0, s1 = max(0.0, ts - pad), te + pad
    raw = WORK / f"tts-{label.split()[0]}-raw.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(TTS),
         "-af", f"atrim={s0:.2f}:{s1:.2f},asetpts=PTS-STARTPTS,atempo={atempo},aresample=48000",
         "-c:a", "pcm_s16le", str(raw)])
    d = np.frombuffer(subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(raw), "-vn", "-ac", "1", "-ar", str(SR),
         "-f", "f32le", "-"], capture_output=True, check=True).stdout, dtype=np.float32)
    target_len = int(round((ne - ns) * SR))
    # atempo output length varies slightly; trim/pad to exactly the window.
    if len(d) > target_len:
        d = d[:target_len]
    elif len(d) < target_len:
        d = np.concatenate([d, np.zeros(target_len - len(d), dtype=np.float32)])
    o0 = int(round(ns * SR))
    full[o0:o0 + target_len] += d
    stretch = (ne - ns) / (te - ts)
    report.append(f"{label}: native {ns:.1f}-{ne:.1f}s ({ne-ns:.2f}s) <- "
                  f"TTS {ts:.2f}-{te:.2f}s ({te-ts:.2f}s) stretch {stretch:.3f}x "
                  f"(atempo {atempo}), placed at {ns:.1f}s")
    print(" ", report[-1])

peak = float(np.abs(full).max())
print(f"aligned track: {len(full)/SR:.2f}s peak={peak:.3f}")
assert peak < 0.99, "aligned track clips"

# Energy check: silence outside the phrase windows (allow 0.1s tails).
buckets = np.array([float(np.sqrt(np.mean(full[i*4800:(i+1)*4800] ** 2)))
                    for i in range(int(len(full) / 4800))])
for i, b in enumerate(buckets):
    t = i / 10
    inside = any(ns - 0.1 <= t < ne + 0.1 for _, ns, ne, _, _, _ in PHRASES)
    if not inside and b > 0.005:
        print(f"WARNING: energy {b:.4f} outside phrase windows at {t:.1f}s")
print("outside-window energy max:",
      max([b for i, b in enumerate(buckets)
           if not any(ns - 0.1 <= i / 10 < ne + 0.1 for _, ns, ne, _, _, _ in PHRASES)],
          default=0.0))

aligned = WORK / "sh020-aligned.wav"
import wave
w = wave.open(str(aligned), "wb")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(SR)
w.writeframes((np.clip(full, -1, 1) * 32767).astype(np.int16).tobytes())
w.close()

run(["ffmpeg", "-v", "error", "-y", "-i", str(VIDEO2K), "-i", str(aligned),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
     str(OUT)])
oinfo = probe(OUT)
print(f"DUBBED: {OUT} fmt={float(oinfo['format']['duration']):.2f}s")
for s in oinfo["streams"]:
    print(f"  {s['codec_type']}: {s['codec_name']} " +
          (f"{s['width']}x{s['height']}" if s["codec_type"] == "video"
           else f"ch={s.get('channels')} sr={s.get('sample_rate')}"))
import hashlib
print(f"  sha256: {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
(WORK / "wordalign-sh020-report.md").write_text(
    "# ep010 sh020 wordalign dub — build report\n\n" + "\n".join(report) +
    f"\n\nOutput: {OUT}\nTTS: {TTS}\nVideo source (copy): {VIDEO2K}\n")
print("WORDALIGN SH020 DONE")
