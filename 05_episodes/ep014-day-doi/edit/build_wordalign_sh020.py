"""Wordalign dub for ep014 sh020 take001: clone ThaoMyVeo over native take001.

Method (proven ep008/ep009/ep010/ep011/ep012/ep013, Richard-approved):
- Native phrase windows measured by ENERGY envelope (48kHz stereo, 0.1s
  buckets) on the native take; Whisper word timestamps only for word
  ORDER/count (Whisper smears the first word "Ma" to 0.00; energy shows
  true onset ~0.2s). Two phrases, clean silence gap 3.0-3.1s:
  P1 "Ma hom qua em xem phim Parasite hay lam" 0.20-2.95,
  P2 "Anh xem chua?" 3.20-3.95.
- TTS: VieNeu v3 Turbo on Colab T4, clone ThaoMyVeo enrolled from
  ref-clip2.wav, session ep014-dub. TWO variants synthesized:
  v1 text "Parasite": Whisper base unprompted garbles 6/12 words
  ("M.S.M Film Baroce Thai Lam, M.S.M.JU"); prompted aligns all 12 but with
  near-zero probabilities on em/Parasite/hay/chua — genuinely ambiguous.
  v2 text "Pa-ra-sai" (phonetic, how Vietnamese speakers say the title):
  Whisper base unprompted hears 9/12 exactly in order
  ("ma hom qua em xem phim va gia xai hay lam, anh xem chua?") — only the
  title itself maps to Vietnamese syllables ("va gia xai"), which a
  Vietnamese ear reads as "Parasite" in context. Script text unchanged;
  only the TTS input spelling is a pronunciation aid (cf. Kokoro "sem nye"
  precedent). USE v2.
- Phrase stretches: P1 TTS 0.00-3.92 -> native 0.20-2.95 (ratio 0.70x,
  atempo 1.425); P2 TTS 4.36-4.96 -> native 3.20-3.95 (ratio 1.25x,
  atempo 0.80). Both ratios inside the ep011 proven range (0.60x-1.70x).
  P1 atempo 1.425x is fast (clone reads slower than native); QC the dubbed
  clip with Whisper after build — if it garbles, revisit (no-stretch does
  NOT fit: clone P1 is 1.2s longer than the mouth window).
- Output: video copy from the 1K take001, audio replaced entirely by the
  clone mono 48kHz AAC 192k track. Native audio is muted completely (proven
  ep008-ep013 method; the brief's envelope/ducking instruction would leak
  the rejected Southern-accent native voice at -20dB under the clone — the
  dubbing skill mandates fully off, and all accepted dubs in this series
  used mute-completely).

TTS wav: ~/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020-phonetic.wav (5.36s, 48kHz mono)
"""
import hashlib
import json
import pathlib
import subprocess
import wave

import numpy as np

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep014-day-doi")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "wordalign"
WORK.mkdir(parents=True, exist_ok=True)
VIDEO1K = GEN / "sh020-take001.mp4"
TTS = pathlib.Path("/home/hatch/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020-phonetic.wav")
OUT = GEN / "sh020-take001-dubbed.mp4"
SR = 48000
DUR = 7.93  # 1K video duration

# (label, native window start/end, TTS slice start/end, atempo)
PHRASES = [
    ("P1 Ma hom qua em xem phim Pa-ra-sai hay lam", 0.20, 2.95, 0.00, 3.92, 3.92 / 2.75),
    ("P2 Anh xem chua?", 3.20, 3.95, 4.36, 4.96, 1.0),  # v2: atempo 1.0 (no-stretch, ep013 A/B winner); ends 3.80, 0.15s tail silence in window
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

full = np.zeros(int(DUR * SR), dtype=np.float32)
report = []
for label, ns, ne, ts, te, atempo in PHRASES:
    pad = 0.05
    s0, s1 = max(0.0, ts - pad), te + pad
    raw = WORK / f"tts-{label.split()[0]}-raw.wav"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(TTS),
         "-af", f"atrim={s0:.2f}:{s1:.2f},asetpts=PTS-STARTPTS,atempo={atempo:.3f},aresample=48000",
         "-c:a", "pcm_s16le", str(raw)])
    d = np.frombuffer(subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(raw), "-vn", "-ac", "1", "-ar", str(SR),
         "-f", "f32le", "-"], capture_output=True, check=True).stdout, dtype=np.float32)
    lead_pad = int(round((ts - s0) / atempo * SR))
    if lead_pad > 0:
        d = d[lead_pad:]
    target_len = int(round((ne - ns) * SR))
    if len(d) > target_len:
        d = d[:target_len]
    elif len(d) < target_len:
        d = np.concatenate([d, np.zeros(target_len - len(d), dtype=np.float32)])
    o0 = int(round(ns * SR))
    full[o0:o0 + target_len] += d
    stretch = (ne - ns) / (te - ts)
    report.append(f"{label}: native {ns:.2f}-{ne:.2f}s ({ne-ns:.2f}s) <- "
                  f"TTS {ts:.2f}-{te:.2f}s ({te-ts:.2f}s) stretch {stretch:.3f}x "
                  f"(atempo {atempo:.3f}), placed at {ns:.2f}s")
    print(" ", report[-1])

peak = float(np.abs(full).max())
print(f"aligned track: {len(full)/SR:.2f}s peak={peak:.3f}")
assert peak < 0.99, "aligned track clips"

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
    "# ep014 sh020 take001 wordalign dub — build report\n\n" + "\n".join(report) +
    f"\n\nOutput: {OUT}\nTTS: {TTS} (v2 phonetic Pa-ra-sai; v1 Parasite kept at "
    "/home/hatch/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020.wav)\n"
    "Video source (copy): {VIDEO1K}\n")
print("WORDALIGN SH020 DONE")
