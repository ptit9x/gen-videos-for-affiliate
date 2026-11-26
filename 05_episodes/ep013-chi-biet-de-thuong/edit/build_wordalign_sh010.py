"""Wordalign dub for ep013 sh010 take004: clone ThaoMyVeo over native take004.

Method (proven ep008/ep009/ep010/ep011, Richard-approved):
- Native phrase windows measured by ENERGY envelope (48kHz stereo, 0.05s
  max-abs buckets, per-channel) on the native take; Whisper word timestamps
  only for word ORDER/count. Energy shows TWO clean bursts separated by a
  real silence gap at 2.20s (the comma pause), so phrase-level alignment:
  P1 "Anh xem giup em bo nay," 0.85-2.15, P2 "thay sao?" 2.25-2.75.
- Word-by-word was NOT used: native Whisper boundaries inside the burst are
  unreliable (it gives "thay" only 0.08s before "sao" starts), which would
  force a 0.35x stretch. Phrase stretches below are both inside the ep011
  proven range (0.60x-1.70x).
- Clone TTS phrase slices (Whisper spans on the TTS wav, padded 0.05s)
  placed at the native window start at NATURAL speed (atempo 1.0); the
  windows were widened to fit the clone (see PHRASES note). Silence
  elsewhere (no bed, no leak).
- Output: video copy from the 1K take004, audio replaced entirely by the
  clone mono 48kHz AAC 192k track. Native audio is muted completely.

TTS wav: ~/workspace/colab-t4-test/ep013-dub/thaomy-ep013-sh010.wav (2.96s, 48kHz mono)
TTS Whisper (base): "Anh se giup em bo nay. The sao?" — word 2 heard "se"
(prompt "xem") and word 7 heard "The" (prompt "thay"); same "thay"->"The"
mishearing Whisper made on native take002/take004, so Whisper alone cannot
settle whether the clone really says "se"/"The". Richard's ear decides;
flagged in the report and in the present message.
"""
import hashlib
import json
import pathlib
import subprocess
import wave

import numpy as np

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep013-chi-biet-de-thuong")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "wordalign"
WORK.mkdir(parents=True, exist_ok=True)
VIDEO1K = GEN / "sh010-take004.mp4"
TTS = pathlib.Path("/home/hatch/workspace/colab-t4-test/ep013-dub/thaomy-ep013-sh010.wav")
OUT = GEN / "sh010-take004-dubbed.mp4"
SR = 48000
DUR = 7.93  # 1K video duration

# (label, native window start/end, TTS slice start/end, atempo)
# NO-STRETCH build (chot 26/11): TTS clone doc cham hon native 0.14s o P1
# nhung dat nguyen toc do vua khit cua so mo rong (P1 0.80-2.24 theo
# Whisper onset 0.80 + duoi 0.09s vao khoang lang; P2 2.25-2.77, duoi 0.02s).
# A/B test: ban stretch (atempo 1.108/1.04, cua so energy chat 0.85-2.15 /
# 2.25-2.75) bi Whisper nghe sai 4 tu ("se/xuong/thu/3"); ban no-stretch
# nghe dung 7/8 tu ("xem" + "thay sao?" dung, chi "giup"->"xuc" la nham
# dong am cua Whisper — wav clone goc nghe "giup" dung). Giu ban no-stretch.
PHRASES = [
    ("P1 Anh xem giup em bo nay,", 0.80, 2.24, 0.00, 1.44, 1.0),
    ("P2 thay sao?", 2.25, 2.77, 1.92, 2.44, 1.0),
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
    # Drop the leading pad (it shrank by atempo too) BEFORE trimming, or the
    # trim cuts speech from the tail: the P2 slice's leading 0.05s pad would
    # otherwise eat the last ~0.05s of "sao?".
    lead_pad = int(round((ts - s0) / atempo * SR))
    if lead_pad > 0:
        d = d[lead_pad:]
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

aligned = WORK / "sh010-aligned.wav"
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
(EDIT / "wordalign-sh010-report.md").write_text(
    "# ep013 sh010 take004 wordalign dub — build report\n\n" + "\n".join(report) +
    f"\n\nOutput: {OUT}\nTTS: {TTS}\nVideo source (copy): {VIDEO1K}\n")
print("WORDALIGN SH010 DONE")
