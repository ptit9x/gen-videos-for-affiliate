"""Wordalign dub for ep013 sh020 take001 (video CAM, 8.00s): clone NamVeo over the
silent Veo clip. No native audio exists (Flow: "Chua tao am thanh nao",
ffprobe: no audio stream) — this build ADDS the clone track to a video-only
file, it does not mute anything.

- Video: take001 clip 4d9a6a9e (26/11 12:07), 8.00s 720x1280 24fps. Nam cuoi
  ha mieng 0-2s (frame 0s mieng mo to, 1s giơ 2 tay nam dam, 2s cuoi), cuoi
  3-5s, ket nhe 7s. Hinh dung (cua go + tu giay, mat khop Nam ep008).
  Take001 bi REJECT vi cam; 10 lan gen lai sau do deu loi audio tren Flow.
- Clone: NamVeo, VieNeu v3 Turbo tren Colab T4, enroll tu audio goc sh040
  take001 (Nam noi that "Um... de thuong!" lap 2 lan — lay ca file lam mau
  giong; tien le ghi san trong work-log 27/11). TTS "Dễ thương!" 0.96s.
- Placement v1: cau "Dễ thương!" dat 0.15-0.85s — SAI: mieng Nam luc 0s van
  KHEP cuoi, toi ~0.3s moi bat dau ha (xem frame 6fps: 0.00s khep, 0.17s khep,
  0.33s bat dau ha, 0.50s ha to). Tieng di truoc mieng ~0.3s nen Richard bao
  chua khop moi. v2: cau moi "Dễ thương nha" (3 am tiet, 0.86s) dat 0.30-1.21s
  (atempo 1.0) — onset tieng ~0.35s, dung luc mieng bat dau ha; "nha" roi
  ~0.86-1.16s, gan luc giơ 2 tay (1.0-1.5s). Silence elsewhere (no bed).
- Output: video copy from take001, audio = clone mono 48kHz AAC 192k.

TTS wav: ~/workspace/colab-t4-test/ep013-dub/nam-ep013-sh020-v2.wav (0.96s, 48kHz mono)
TTS Whisper (base, 16kHz): "Dễ thương" — 2/2 tu dung, 0.00-0.60s. Richard's
ear decides whether the voice sounds like Nam / Northern enough.
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
VIDEO1K = GEN / "sh020-take001.mp4"
TTS = pathlib.Path("/home/hatch/workspace/colab-t4-test/ep013-dub/nam-ep013-sh020-v2.wav")
OUT = GEN / "sh020-take001-dubbed.mp4"
SR = 48000
DUR = 8.00  # take001 duration

# (label, native window start/end, TTS slice start/end, atempo)
# (label, placement window start/end, TTS slice start/end, atempo)
# One phrase only: "Dễ thương!" placed where the mouth is widest open (0-2s).
PHRASES = [
    ("P1 De thuong nha!", 0.30, 1.21, 0.00, 0.86, 1.0),
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
    "# ep013 sh020 take004 wordalign dub — build report\n\n" + "\n".join(report) +
    f"\n\nOutput: {OUT}\nTTS: {TTS}\nVideo source (copy): {VIDEO1K}\n")
print("WORDALIGN SH020 DONE")
