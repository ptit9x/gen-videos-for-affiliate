"""ep008 1K preview — STAGE 3 ONLY (rerun after the main script crashed).

Main script build_master_1k.py completed stages 1-2 + the Remotion Boxed render
(exit 0, 269s, ep008-boxed-tmp.mp4 16MB, 28.70s), then crashed in stage 3:
  full = np.zeros((int(28.6*48000), 2))  vs dlg = 1376256 samples (28.672s)
  -> ValueError broadcast (1372800,2) vs (1376256,2).
Fix: total = actual boxed-audio duration (len(dlg)/SR), not the nominal 28.6s.
The extra ~0.07s is AAC priming/frame rounding; shot bounds are unaffected
(segments probed exactly at their trims; caption timings measured on the
assembly audio, same timeline).

This script: laugh mix (numpy) -> mux -> final loudnorm -> QC -> report.
"""
import json, pathlib, subprocess, wave
import numpy as np
from PIL import Image

GEN = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep008-con-nho-do/generated")
EDIT = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep008-con-nho-do/edit")
WORK = EDIT / "build1k"
REMO = pathlib.Path("/home/hatch/workspace/remotion-captions-test")
LAUGH = pathlib.Path("/home/hatch/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3")
SR = 48000

SEGS = [
    ("sh010", "sh010-take005-dub-thaomy-wordalign.mp4", 2.8),
    ("sh020", "sh020-take003.mp4", 3.6),
    ("sh030", "sh030-take002-dub-thaomy-wordalign.mp4", 5.2),
    ("sh040", "sh040-take004.mp4", 5.0),
    ("sh050", "sh050-take002.mp4", 2.0),
    ("sh060", "sh060-take015.mp4", 7.0),
    ("sh070", "sh070-take002.mp4", 3.0),
]
BOUNDS = {}
_t = 0.0
for sh, _, dur in SEGS:
    BOUNDS[sh] = (_t, _t + dur)
    _t += dur
NOMINAL_TOTAL = _t

def run(cmd, check=True, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if check and r.returncode != 0:
        print("FAILED:", " ".join(str(c) for c in cmd))
        print(r.stderr[-3000:])
        raise SystemExit(1)
    return r

def probe(p):
    return json.loads(run(["ffprobe", "-v", "quiet", "-print_format", "json",
                           "-show_format", "-show_streams", str(p)]).stdout)

def wav_read(p):
    w = wave.open(str(p))
    n, sr, ch = w.getnframes(), w.getframerate(), w.getnchannels()
    d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        d = d.reshape(-1, ch)
    return d, sr, ch

def wav_write(p, d, sr):
    d = np.clip(d, -1, 1)
    inter, ch = (d.reshape(-1), d.shape[1]) if d.ndim == 2 else (d, 1)
    w = wave.open(str(p), "wb")
    w.setnchannels(ch); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((inter * 32767).astype(np.int16).tobytes())
    w.close()

boxed_tmp = REMO / "out" / "ep008-boxed-tmp.mp4"
assert boxed_tmp.exists() and boxed_tmp.stat().st_size > 1_000_000, "boxed render missing"
binfo = probe(boxed_tmp)
bvdur = float([s for s in binfo["streams"] if s["codec_type"] == "video"][0]["duration"])
print(f"boxed tmp: {boxed_tmp} size={boxed_tmp.stat().st_size} vdur={bvdur:.2f}s")

# (re)extract audio stems
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_tmp), "-vn", "-ac", "2", "-ar", "48000",
     "-c:a", "pcm_s16le", str(WORK / "boxed-48k.wav")])
dlg, _, _ = wav_read(WORK / "boxed-48k.wav")
run(["ffmpeg", "-v", "error", "-y", "-i", str(LAUGH),
     "-vn", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", str(WORK / "laugh1-48k.wav")])
laugh, _, _ = wav_read(WORK / "laugh1-48k.wav")
if laugh.ndim == 1:
    laugh = np.stack([laugh, laugh], axis=1)
laugh_dur = len(laugh) / SR
print(f"dialogue {len(dlg)/SR:.3f}s peak {np.abs(dlg).max():.3f}; laugh {laugh_dur:.2f}s peak {np.abs(laugh).max():.3f}")
hop100 = SR // 100
m = np.abs(laugh).max(axis=1)
buckets = np.array([m[i*hop100:(i+1)*hop100].max() for i in range(len(m)//hop100)])
onset = float(np.where(buckets > 0.05)[0][0] / 100)
print(f"laugh onset in file: {onset:.2f}s")
LAUGH_AUDIBLE_AT = 25.7  # 0.1s into sh070 (starts 25.6s)
stem_start = round(LAUGH_AUDIBLE_AT - onset, 2)
laugh_end = stem_start + laugh_dur
total = len(dlg) / SR  # ACTUAL duration (28.672s), not nominal 28.6 — the stage-3 crash fix
print(f"stem_start={stem_start}s (audible ~{LAUGH_AUDIBLE_AT:.2f}s), laugh ends {laugh_end:.2f}s, "
      f"total={total:.3f}s (nominal {NOMINAL_TOTAL:.1f}s) -> no freeze tail needed")
assert laugh_end < total, "laugh would overrun the video"

full = np.zeros((len(dlg), 2), dtype=np.float32)
full += dlg
s0 = int(stem_start * SR)
full[s0:s0 + len(laugh)] += laugh
peak = np.abs(full).max()
print(f"mixed peak: {peak:.3f}")
if peak > 0.98:
    gain = 0.98 / peak
    full = np.zeros((len(dlg), 2), dtype=np.float32)
    full += dlg
    full[s0:s0 + len(laugh)] += laugh * gain
    print(f"scaled laugh by {gain:.3f}; new peak {np.abs(full).max():.3f}")
wav_write(WORK / "full-audio.wav", full, SR)

tmp = WORK / "final-tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_tmp),
     "-i", str(WORK / "full-audio.wav"),
     "-map", "0:v", "-map", "1:a",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(total), str(tmp)])
final = EDIT / "ep008-master-1k-preview.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp),
     "-af", "loudnorm=I=-15.5:TP=-1.0:LRA=11,aresample=48000",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(total), str(final)])
finfo = probe(final)
print(f"FINAL: {final} fmt={float(finfo['format']['duration']):.2f}s")
for s in finfo["streams"]:
    print(f"  {s['codec_type']}: {s['codec_name']} dur={float(s.get('duration', 0)):.2f} " +
          (f"{s['width']}x{s['height']} fps={s.get('avg_frame_rate')}" if s["codec_type"] == "video" else
           f"ch={s.get('channels')} sr={s.get('sample_rate')}"))
r = run(["ffmpeg", "-v", "info", "-i", str(final), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        check=False)
js = r.stderr[r.stderr.find("{"):r.stderr.find("}") + 1]
print("final loudnorm measure:", js.replace("\\n", " ").replace("\\t", " "))

# ============ QC: energy per shot on final audio ============
print("== QC: energy per shot (final) ==")
run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vn", "-ac", "2", "-ar", "48000",
     "-c:a", "pcm_s16le", str(WORK / "final-48k.wav")])
d, _, _ = wav_read(WORK / "final-48k.wav")
mm = np.abs(d).max(axis=1)
hop10 = SR // 10
for sh, _, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    seg = mm[int(t0*SR):int(t1*SR)]
    bmax = [float(mm[b*hop10:(b+1)*hop10].max()) for b in range(int(t0*10), int(t1*10))]
    print(f"  {sh} {t0:.1f}-{t1:.1f}s peak={seg.max():.3f} mean={seg.mean():.4f} "
          f"buckets0.1s: {' '.join(f'{x:.2f}' for x in bmax)}")
print("  sh070 detail (laugh zone 25.6-28.6):")
print("   ", " ".join(f"{b/10:.1f}:{mm[b*hop10:(b+1)*hop10].max():.3f}" for b in range(256, 286)))

# ============ QC: contact sheet (mid per shot + around cuts) ============
print("== QC: contact sheet ==")
qcd = WORK / "qc"
qcd.mkdir(exist_ok=True)
def grab(t, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(final), "-frames:v", "1", str(out)])
mids = []
for sh, _, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    fp = qcd / f"final-mid-{sh}.png"
    grab((t0 + t1) / 2, fp)
    mids.append(Image.open(fp).convert("RGB"))
cuts = []
for sh, _, _ in SEGS[1:]:
    t0, _ = BOUNDS[sh]
    for dt, tag in [(-0.06, "pre"), (0.06, "post")]:
        fp = qcd / f"final-cut-{sh}-{tag}.png"
        grab(t0 + dt, fp)
        cuts.append(Image.open(fp).convert("RGB"))
sheet = Image.new("RGB", (270*7, 480 + 480), "white")
for i, im in enumerate(mids):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 0))
for i, im in enumerate(cuts):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 480))
sheet.save(WORK / "qc-contact.png")
print(f"contact sheet: {WORK / 'qc-contact.png'} (row1 mids sh010-sh070, row2 cut frames)")

# ============ QC: Whisper transcript of final (record only) ============
print("== QC: whisper transcript (final, record only) ==")
run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vn", "-ac", "1", "-ar", "16000",
     "-c:a", "pcm_s16le", str(WORK / "final-16k.wav")])
d16f, sr16f, _ = wav_read(WORK / "final-16k.wav")
from faster_whisper import WhisperModel
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base",
                     device="cpu", compute_type="int8", local_files_only=True)
segs_f, _ = model.transcribe(d16f, language="vi", word_timestamps=False, beam_size=5)
for s in segs_f:
    print(f"  {s.start:.2f}-{s.end:.2f} {s.text.strip()!r}")

# ============ build report ============
import hashlib
def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
seg_durs = {}
for sh, _, T in SEGS:
    seg_durs[sh] = round(float(probe(WORK / f"seg-{sh}.mp4")["format"]["duration"]), 2)
report = f"""# ep008 master 1K preview — build report

## Outputs
- Preview: `edit/ep008-master-1k-preview.mp4` sha256 `{sha(final)}`
- SRT: `edit/ep008-master-1k-preview.srt`
- Scripts: `edit/build_master_1k.py` (stages 1-2 + render) + `edit/stage3_only.py`
  (stage 3 rerun — the first run crashed on a shape mismatch, see below)
- Work dir: `edit/build1k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render.log, qc-contact.png)

## Sources (all 1K 720x1280 24fps, from generated/)
- sh010 sh010-take005-dub-thaomy-wordalign.mp4 (clone ThaoMy, word-aligned) trim 0-2.8s
- sh020 sh020-take003.mp4 (native) trim 0-3.6s
- sh030 sh030-take002-dub-thaomy-wordalign.mp4 (clone ThaoMy, word-aligned) trim 0-5.2s
- sh040 sh040-take004.mp4 (native) trim 0-5.0s (sentence 2 cut by design)
- sh050 sh050-take002.mp4 (native) trim 0-2.0s
- sh060 sh060-take015.mp4 (native, NOT the dub-minhquan spare) trim 0-7.0s
- sh070 sh070-take002.mp4 (native, silent) trim 0-3.0s
- Nominal total {NOMINAL_TOTAL:.1f}s; actual final {total:.2f}s (extra ~0.07s is AAC
  priming/frame rounding at the tail — shot bounds unchanged). Bounds: {BOUNDS}

## Stage 1 commands (per segment)
ffmpeg -i <src> -vf "trim=0:<T>,setpts=PTS-STARTPTS,crop=640:1138:40:0,scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[6:v][6:a]concat=n=7:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11 (ep006 pattern), video copy.
  Measured on assembly: input_i -14.95 LUFS (target -15.5, single-pass deviation 0.55 LU).
Segment durations measured: {seg_durs}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on ALL 7 shots (top-right
  corners clean foliage). Icon top edge ranges y~1180-1221 across shots (720x1280 coords).
- Uniform crop crop=640:1138:40:0 (=640x1138 window, x 40..680, y 0..1138, then lanczos to
  1080x1920): removes the icon on every shot with ~40px margin. One uniform crop
  (not per-shot) so framing/scale stays consistent across hard cuts; per-shot crops
  would visibly change zoom shot-to-shot. Faces/hands verified safe on mid frames
  (hands lowest ~y1010 in sh070, well above the 1138 cut line).

## Stage 2 captions (Remotion Boxed)
- Whisper base word timestamps on assembly audio, aligned to script words IN ORDER,
  energy-refined (10ms buckets, thr 0.02), clamped to shot bounds, overlaps clamped.
  Counts clean on all 6 dialogue shots (8/8, 9/9, 12/12, 9/9, 6/6, 14/14 = 58 words).
  Known ASR artifacts ignored by design: "chia tay"->"chi tai", "Giua"->"du", "Lo"->"lua",
  "a?"->"ta". captions-PROBLEMS.txt lists only benign 10-30ms end clamps (refined word
  ends running into the next word's start in continuous speech; clamped back).
- Render: cd remotion-captions-test && npx remotion render Boxed out/ep008-boxed-tmp.mp4
  --props '{{"accent":"#F59E0B"}}' --browser-executable <chrome-headless-shell-131>
  --concurrency=2 --crf=18 (exit 0, 269s, 16MB, vdur 28.70s; log: edit/build1k/render.log;
  temp file verified by exit code + fresh timestamp + probed duration before use;
  no title card, no punch-in zoom)
- Remotion: @remotion/cli ^4.0.0, template remotion-captions, Boxed composition,
  1080x1920, 30fps (meta.json).

## Stage 3 laugh — RERUN (first attempt crashed)
- Crash cause: numpy full-track allocated at nominal 28.6s (1372800 samples) but the
  boxed audio is 28.672s (1376256 samples) -> broadcast ValueError. Fix in stage3_only.py:
  total = len(dlg)/SR (actual boxed-audio duration). No re-render needed (boxed tmp intact).
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix over sh070, audible onset {LAUGH_AUDIBLE_AT:.1f}s (0.1s into the
  reaction shot), stem_start={stem_start:.2f}s, laugh ends {laugh_end:.2f}s < {total:.2f}s.
- NO freeze-frame tail (ep006 stage1 pattern has none; laugh fits inside the video).
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.
- FLAG: laugh-over-sh070 placement is the series pattern but the user has NOT
  explicitly confirmed it for ep008 — he can say remove.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, ~28.67s, AAC 48kHz stereo).
- Energy per shot + sh070 laugh-zone buckets: see script output above.
- Contact sheet: edit/build1k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: see script output above (record only; script words govern captions).
"""
(WORK / "build-report.md").write_text(report)
print(report)
print("STAGE3 DONE")
