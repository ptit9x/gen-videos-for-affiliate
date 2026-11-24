"""Wordalign dub for ep011 sh020: clone ThaoMyVeo over native take001.

Method (proven ep008/ep009/ep010, Richard-approved 21/11):
- Native phrase windows measured by ENERGY envelope (48kHz stereo, 0.05s
  max-abs buckets, per-channel) on the native take; Whisper word timestamps
  only for word ORDER/count. Whisper SMEARED the first word of cluster 1
  by 0.4s (said "Thuong" 0.6s; energy shows speech starts ~1.02s) — the
  energy windows below are the authority, NOT the Whisper times.
- Clone TTS phrase slices (Whisper spans on the TTS wav, padded 0.05s)
  stretched with ffmpeg atempo to exactly the native phrase window, placed
  at the native window start. Silence elsewhere (no bed, no leak).
- Output: video copy from the 1K take001, audio replaced entirely by the
  clone mono 48kHz AAC 192k track. Native audio is muted completely.

Phrase windows (native, energy 0.05s buckets):
  P1 "Thuong anh ghe."  1.00-1.90 (TTS slice 0.00-0.91, stretch 0.989x, atempo 1.011)
  P2 "Chac co do khong xung voi anh." 2.80-4.20 (TTS slice 1.43-3.33, stretch 0.737x, atempo 1.357)
  P3 "Roi truoc do?" 5.85-6.65 (TTS slice 3.75-4.59, stretch 0.952x, atempo 1.050)
All stretch factors within the ep009 proven range (0.60x-1.70x).
Native windows record: edit/sh020-native-windows.md
TTS wav: ~/workspace/colab-t4-test/ep011-dub/thaomy-ep011-sh020.wav (5.20s, 48kHz mono)
"""
import hashlib
import json
import pathlib
import subprocess
import wave

import numpy as np

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep011-noi-xau-ex")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "wordalign"
WORK.mkdir(parents=True, exist_ok=True)
VIDEO1K = GEN / "sh020-take001.mp4"
TTS = pathlib.Path("/home/hatch/workspace/colab-t4-test/ep011-dub/thaomy-ep011-sh020.wav")
OUT = GEN / "sh020-take001-dubbed.mp4"
SR = 48000
DUR = 7.93  # 1K video duration

# (label, native window start/end, TTS slice start/end, atempo)
PHRASES = [
    ("P1 Thuong anh ghe.", 1.00, 1.90, 0.00, 0.91, 1.011),
    ("P2 Chac co do khong xung voi anh.", 2.80, 4.20, 1.43, 3.33, 1.357),
    ("P3 Roi truoc do.", 5.85, 6.65, 3.75, 4.59, 1.050),
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


assert VIDEO1K.exists(), f"missing 1K video {VIDEO1K}"
assert TTS.exists(), f"missing TTS wav {TTS}"
vinfo = probe(VIDEO1K)
print(f"1K video: {vinfo['streams'][0]['width']}x{vinfo['streams'][0]['height']} "
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
    report.append(f"{label}: native {ns:.2f}-{ne:.2f}s ({ne-ns:.2f}s) <- "
                  f"TTS {ts:.2f}-{te:.2f}s ({te-ts:.2f}s) stretch {stretch:.3f}x "
                  f"(atempo {atempo}), placed at {ns:.2f}s")
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
w = wave.open(str(aligned), "wb")
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(SR)
w.writeframes((np.clip(full, -1, 1) * 32767).astype(np.int16).tobytes())
w.close()

run(["ffmpeg", "-v", "error", "-y", "-i", str(VIDEO1K), "-i", str(aligned),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
     str(OUT)])
oinfo = probe(OUT)
print(f"DUBBED: {OUT} fmt={float(oinfo['format']['duration']):.2f}s")
for s in oinfo["streams"]:
    print(f"  {s['codec_type']}: {s['codec_name']} " +
          (f"{s['width']}x{s['height']}" if s["codec_type"] == "video"
           else f"ch={s.get('channels')} sr={s.get('sample_rate')}"))
print(f"  sha256: {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
(EDIT / "wordalign-sh020-report.md").write_text(
    "# ep011 sh020 wordalign dub — build report\n\n" + "\n".join(report) +
    f"\n\nOutput: {OUT}\nTTS: {TTS}\nVideo source (copy): {VIDEO1K}\n")
print("WORDALIGN SH020 DONE")
