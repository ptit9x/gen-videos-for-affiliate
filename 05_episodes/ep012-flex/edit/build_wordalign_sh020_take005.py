"""Wordalign dub for ep012 sh020 take005: clone ThaoMyVeo over native take005.

LINE (script r05, Richard 2026-11-25 20:21, commit b5295b6):
  "May ty thi ke anh, em uong ly ca phe ba muoi ngan, anh dung lo." (16 words)
take005 was generated natively WITH this line (Flow clip 6b1f178f, 2026-11-26)
to fix the lip-sync problem of take004 (generated for the old line, dubbed).
Richard 2026-11-26 06:56: "ok do, long giong ThaoMy la dc" — dub the clone
over take005 (do NOT keep the native voice).

Method (proven ep008/ep009/ep010/ep011 + ep012 r03/r05 dubs):
- Native phrase windows measured by ENERGY envelope (48kHz stereo, 0.05s
  max-abs buckets + 0.02s fine buckets at boundaries) on take005;
  Whisper word timestamps only for word ORDER/count. Whisper smears onsets
  ~0.3s early (P1 "May" 0.62s vs energy 0.91s) — energy is the authority.
- Clone TTS phrase slices measured by ENERGY on the SAME r05 TTS wav
  (reused, sha a64baf42... — no new Colab run needed).
- P1 ADAPTATION (same as r05): the clone speaks "May ty thi" and "ke anh"
  as two bursts with a 0.30s pause between (0.62-0.90s of the TTS wav).
  The internal pause is cut (two sub-slices concatenated). The pause is
  inside one phrase, so no window timing changes.

Native windows (take005, energy, measured 2026-11-26) and TTS slices:
  P1 "May ty thi ke anh"  0.91-1.99 (1.08s) <- TTS [0.04-0.62 + 0.90-1.68]
     (1.36s) stretch 0.794x (atempo 1.259)
  P2 "em uong ly ca phe ba muoi ngan" 2.41-3.99 (1.58s) <- TTS 2.04-4.05
     (2.01s) stretch 0.786x (atempo 1.272)
  P3 "anh dung lo" 4.29-4.91 (0.62s) <- TTS 4.55-5.47
     (0.92s) stretch 0.674x (atempo 1.484)
All stretch factors within the ep009 proven range (0.60x-1.70x).
Native windows record: edit/sh020-take005-native-windows.md.
TTS wav: ~/workspace/colab-t4-test/ep012-dub-r05/thaomy-ep012-sh020-r05.wav
  (5.84s, 48kHz mono, sha a64baf42...; Colab session ep012-dub-r05,
  T4, VieNeu v3 Turbo, preset ThaoMyVeo).
Output: video copy from the 1K take005, audio replaced entirely by the
clone mono 48kHz AAC 192k track. Native audio is muted completely.
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
VIDEO1K = GEN / "sh020-take005.mp4"
TTS = pathlib.Path("/home/hatch/workspace/colab-t4-test/ep012-dub-r05/thaomy-ep012-sh020-r05.wav")
OUT = GEN / "sh020-take005-dubbed.mp4"
SR = 48000
DUR = 7.93  # 1K video duration

# (label, native window start/end, [(tts slice start, end), ...], atempo)
PHRASES = [
    ("P1 May ty thi ke anh", 0.91, 1.99,
     [(0.04, 0.62), (0.90, 1.68)], 1.259),
    ("P2 em uong ly ca phe ba muoi ngan", 2.41, 3.99,
     [(2.04, 4.05)], 1.272),
    ("P3 anh dung lo", 4.29, 4.91,
     [(4.55, 5.47)], 1.484),
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
             "-af", filt, "-c:a", "pcm_s16le", str(WORK / f"tts-t005-{tag}-raw.wav")])
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
             str(WORK / f"tts-t005-{tag}-raw.wav")])
    d = np.frombuffer(subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(WORK / f"tts-t005-{tag}-raw.wav"),
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

aligned = WORK / "sh020-take005-aligned.wav"
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
(EDIT / "wordalign-sh020-take005-report.md").write_text(
    "# ep012 sh020 wordalign dub take005 — build report\n\n" + "\n".join(report) +
    f"\n\nOutput: {OUT}\nTTS: {TTS}\nVideo source (copy): {VIDEO1K}\n")
print("WORDALIGN SH020 TAKE005 DONE")
