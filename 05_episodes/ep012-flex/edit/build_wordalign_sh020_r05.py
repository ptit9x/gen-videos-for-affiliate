"""Wordalign dub for ep012 sh020 r05: clone ThaoMyVeo over native take004.

NEW LINE (script r05, Richard's pick 2026-11-25 20:21, commit b5295b6):
  "May ty thi ke anh, em uong ly ca phe ba muoi ngan, anh dung lo." (16 words)
Replaces the r03 line "Da hay qua anh, ..." (Richard: the old reply did not
answer the car question — it jumped from the car to the coffee with no bridge).

Method (proven ep008/ep009/ep010/ep011 + ep012 r03 dub):
- Native phrase windows measured by ENERGY envelope (48kHz stereo, 0.05s
  max-abs buckets + 0.02s fine buckets at boundaries) on the native take004;
  Whisper word timestamps only for word ORDER/count. Re-measured 2026-11-25
  for r05 — windows CONFIRMED identical to the r03 record:
  P1 1.02-1.90 / P2 2.40-4.05 / P3 4.56-5.18 (Whisper smears P1 "Da" 0.76s
  and P3 "anh" 4.24s early, as before — energy is the authority).
- Clone TTS phrase slices measured by ENERGY on the TTS wav (Whisper smeared
  the P3 onset to 4.34s; energy shows 4.55s — same smear class as native).
- P1 ADAPTATION (documented, not in the ep011 pattern): the clone speaks
  "May ty thi" and "ke anh" as two bursts with a 0.30s pause between
  (0.62-0.90s of the TTS wav). A contiguous slice would be 1.59s into a
  0.88s window = stretch 0.553x, OUTSIDE the proven 0.60x-1.70x range.
  The internal pause is cut (two sub-slices concatenated), leaving 1.36s
  of speech -> stretch 0.647x, inside range. The pause is inside one phrase,
  not between phrases, so no window timing changes.
- Output: video copy from the 1K take004, audio replaced entirely by the
  clone mono 48kHz AAC 192k track. Native audio is muted completely.

Phrase windows (native, energy) and TTS slices (energy, 0.02s pads):
  P1 "May ty thi ke anh"  1.02-1.90 (0.88s) <- TTS [0.04-0.62 + 0.90-1.68]
     (1.36s) stretch 0.647x (atempo 1.545)
  P2 "em uong ly ca phe ba muoi ngan" 2.40-4.05 (1.65s) <- TTS 2.01-4.05
     (2.04s) stretch 0.809x (atempo 1.236)
  P3 "anh dung lo" 4.56-5.18 (0.62s) <- TTS 4.53-5.47
     (0.94s) stretch 0.660x (atempo 1.516)
All stretch factors within the ep009 proven range (0.60x-1.70x).
Native windows record: edit/sh020-native-windows.md (re-confirmed r05).
TTS wav: ~/workspace/colab-t4-test/ep012-dub-r05/thaomy-ep012-sh020-r05.wav
  (5.84s, 48kHz mono, sha a64baf42...)
Colab session: ep012-dub-r05 (T4, VieNeu v3 Turbo, preset ThaoMyVeo).
"""
import hashlib
import json
import pathlib
import subprocess
import wave

import numpy as np

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep012-flex")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "wordalign"
WORK.mkdir(parents=True, exist_ok=True)
VIDEO1K = GEN / "sh020-take004.mp4"
TTS = pathlib.Path("/home/hatch/workspace/colab-t4-test/ep012-dub-r05/thaomy-ep012-sh020-r05.wav")
OUT = GEN / "sh020-take004-dubbed.mp4"
SR = 48000
DUR = 7.93  # 1K video duration

# (label, native window start/end, [(tts slice start, end), ...], atempo)
PHRASES = [
    ("P1 May ty thi ke anh", 1.02, 1.90,
     [(0.04, 0.62), (0.90, 1.68)], 1.545),
    ("P2 em uong ly ca phe ba muoi ngan", 2.40, 4.05,
     [(2.01, 4.05)], 1.236),
    ("P3 anh dung lo", 4.56, 5.18,
     [(4.53, 5.47)], 1.516),
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
for label, ns, ne, parts, atempo in PHRASES:
    tag = label.split()[0]
    # Build one combined slice wav from the parts (concat filter), then atempo.
    if len(parts) == 1:
        ts, te = parts[0]
        filt = f"atrim={ts:.2f}:{te:.2f},asetpts=PTS-STARTPTS,atempo={atempo},aresample=48000"
        run(["ffmpeg", "-v", "error", "-y", "-i", str(TTS),
             "-af", filt, "-c:a", "pcm_s16le", str(WORK / f"tts-r05-{tag}-raw.wav")])
    else:
        ins, joins = [], []
        for i, (ts, te) in enumerate(parts):
            ins.append(f"[0:a]atrim={ts:.2f}:{te:.2f},asetpts=PTS-STARTPTS[a{i}]")
            joins.append(f"[a{i}]")
        filt = (";".join(ins) +
                f";{''.join(joins)}concat=n={len(parts)}:v=0:a=1,atempo={atempo},"
                f"aresample=48000[out]")
        run(["ffmpeg", "-v", "error", "-y", "-i", str(TTS),
             "-filter_complex", filt, "-map", "[out]", "-c:a", "pcm_s16le",
             str(WORK / f"tts-r05-{tag}-raw.wav")])
    d = np.frombuffer(subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(WORK / f"tts-r05-{tag}-raw.wav"),
         "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True).stdout, dtype=np.float32)
    target_len = int(round((ne - ns) * SR))
    # atempo output length varies slightly; trim/pad to exactly the window.
    if len(d) > target_len:
        d = d[:target_len]
    elif len(d) < target_len:
        d = np.concatenate([d, np.zeros(target_len - len(d), dtype=np.float32)])
    o0 = int(round(ns * SR))
    full[o0:o0 + target_len] += d
    tts_len = sum(te - ts for ts, te in parts)
    stretch = (ne - ns) / tts_len
    report.append(f"{label}: native {ns:.2f}-{ne:.2f}s ({ne-ns:.2f}s) <- "
                  f"TTS {parts} ({tts_len:.2f}s) stretch {stretch:.3f}x "
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
    inside = any(ns - 0.1 <= t < ne + 0.1 for _, ns, ne, _, _ in PHRASES)
    if not inside and b > 0.005:
        print(f"WARNING: energy {b:.4f} outside phrase windows at {t:.1f}s")
print("outside-window energy max:",
      max([b for i, b in enumerate(buckets)
           if not any(ns - 0.1 <= i / 10 < ne + 0.1 for _, ns, ne, _, _ in PHRASES)],
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
(EDIT / "wordalign-sh020-r05-report.md").write_text(
    "# ep012 sh020 wordalign dub r05 — build report\n\n" + "\n".join(report) +
    f"\n\nOutput: {OUT}\nTTS: {TTS}\nVideo source (copy): {VIDEO1K}\n")
print("WORDALIGN SH020 R05 DONE")
