"""Resume ep011 master build after the first run was killed (SIGTERM) mid-write
while concatenating the video-only Remotion chunks.

State verified before resume (2026-11-24):
  - Segments, concat FILTER, loudnorm assembly: done (assembly-norm.mp4 27.70s).
  - Captions: done — 56 words aligned (SRT written to delivery/, captions.json in
    remotion public/). Problems file holds only routine end-time clamps.
  - Remotion chunks: ALL 3 verified complete (chunk0 287f/9.57s, chunk1 287f/9.57s,
    chunk2 257f/8.57s = 831 frames = 27.7s). The ep010 inputs backup exists.
  - boxed-video-only.mp4 was CORRUPT (moov atom missing — killed mid-write).
    This script deletes it and rebuilds it from the 3 verified chunks, then
    continues with the mux + stage 3 (laugh + freeze) + final loudnorm + QC.
"""
import hashlib, json, pathlib, subprocess, wave
import numpy as np
from PIL import Image

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep011-noi-xau-ex")
EDIT = EP / "edit"
WORK = EDIT / "build2k"
DELIVERY = EP / "delivery"
REMO = pathlib.Path("/home/hatch/workspace/remotion-captions-test")
PUB = REMO / "public"
LAUGH = pathlib.Path("/home/hatch/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3")
SR = 48000

SEGS = [("sh010", 6.4), ("sh020", 7.35), ("sh030", 6.2), ("sh040", 7.7)]
BOUNDS = {}
_t = 0.0
for sh, dur in SEGS:
    BOUNDS[sh] = (_t, _t + dur)
    _t += dur
TOTAL = _t
print(f"bounds: {BOUNDS} total={TOTAL:.2f}s", flush=True)

caps = json.load(open(PUB / "captions.json"))
assert len(caps) == 56, f"expected 56 caps, got {len(caps)}"
LAST_WORD_END = caps[-1]["endMs"] / 1000
print(f"last word '{caps[-1]['text']}' ends {LAST_WORD_END:.2f}s", flush=True)

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

def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

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

def frame_mean(p, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(p),
                        "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                       capture_output=True)
    a = np.frombuffer(r.stdout, dtype=np.uint8)
    return float(a.mean()) if len(a) else -1.0

# ============ rebuild boxed-video-only from the 3 verified chunks ============
print("== rebuild boxed-video-only (chunks were verified; old file was corrupt) ==", flush=True)
chunk_files = [REMO / "out" / f"ep011-boxed-2k-chunk{i}.mp4" for i in range(3)]
for f in chunk_files:
    info = probe(f)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    print(f"  {f.name}: {float(info['format']['duration']):.2f}s {v['width']}x{v['height']}", flush=True)
boxed_video = WORK / "boxed-video-only.mp4"
boxed_video.unlink(missing_ok=True)
inputs = []
for f in chunk_files:
    inputs += ["-i", str(f)]
fc = "".join(f"[{i}:v]" for i in range(len(chunk_files))) + f"concat=n={len(chunk_files)}:v=1:a=0[v]"
run(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", fc, "-map", "[v]",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", str(boxed_video)])
bv = probe(boxed_video)
bv_dur = float(bv["format"]["duration"])
print(f"boxed video-only: fmt={bv_dur:.2f}s (expect ~27.7s)", flush=True)
assert abs(bv_dur - 27.7) < 0.5, f"boxed video duration {bv_dur} wrong"
m = frame_mean(boxed_video, 13.8)
print(f"boxed video-only mean frame @ 13.8s: {m:.1f}", flush=True)
assert m > 10, "boxed video looks BLACK"

asm = WORK / "assembly-norm.mp4"
boxed_tmp = REMO / "out" / "ep011-boxed-2k-tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_video), "-i", str(asm),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "copy", str(boxed_tmp)])
binfo = probe(boxed_tmp)
bvdur = float([s for s in binfo["streams"] if s["codec_type"] == "video"][0]["duration"])
print(f"boxed tmp: {boxed_tmp} size={boxed_tmp.stat().st_size} vdur={bvdur:.2f}s (expect 27.70s)", flush=True)
assert abs(bvdur - 27.70) < 0.5, f"boxed duration {bvdur} != 27.70"

# ============ STAGE 3: laugh after punchline + freeze tail ============
print("== stage 3: laugh track 1 after sh040 punchline ==", flush=True)
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_tmp), "-vn", "-ac", "2", "-ar", "48000",
     "-c:a", "pcm_s16le", str(WORK / "boxed-48k.wav")])
dlg, _, _ = wav_read(WORK / "boxed-48k.wav")
run(["ffmpeg", "-v", "error", "-y", "-i", str(LAUGH),
     "-vn", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", str(WORK / "laugh1-48k.wav")])
laugh, _, _ = wav_read(WORK / "laugh1-48k.wav")
if laugh.ndim == 1:
    laugh = np.stack([laugh, laugh], axis=1)
laugh_dur = len(laugh) / SR
print(f"dialogue {len(dlg)/SR:.3f}s peak {np.abs(dlg).max():.3f}; laugh {laugh_dur:.2f}s peak {np.abs(laugh).max():.3f}", flush=True)
hop100 = SR // 100
mm = np.abs(laugh).max(axis=1)
buckets = np.array([mm[i*hop100:(i+1)*hop100].max() for i in range(len(mm)//hop100)])
onset = float(np.where(buckets > 0.05)[0][0] / 100)
print(f"laugh onset in file: {onset:.2f}s", flush=True)
LAUGH_AUDIBLE_AT = round(LAST_WORD_END + 0.15, 2)
stem_start = round(LAUGH_AUDIBLE_AT - onset, 2)
total = round(stem_start + laugh_dur, 2)
vdur = bvdur
freeze = total - vdur
print(f"stem_start={stem_start}s (audible ~{LAUGH_AUDIBLE_AT:.2f}s), total={total}s, "
      f"video={vdur:.2f}s, freeze={freeze:.2f}s", flush=True)
assert 0.2 < freeze < 2.0, f"freeze {freeze:.2f}s out of range — check trims/laugh placement"

full = np.zeros((int(total * SR), 2), dtype=np.float32)
full[:len(dlg)] += dlg
s0 = int(stem_start * SR)
full[s0:s0 + len(laugh)] += laugh
peak = np.abs(full).max()
print(f"mixed peak: {peak:.3f}", flush=True)
if peak > 0.98:
    gain = 0.98 / peak
    full = np.zeros((int(total * SR), 2), dtype=np.float32)
    full[:len(dlg)] += dlg
    full[s0:s0 + len(laugh)] += laugh * gain
    print(f"scaled laugh by {gain:.3f}; new peak {np.abs(full).max():.3f}", flush=True)
wav_write(WORK / "full-audio.wav", full, SR)

still = WORK / "lastframe.png"
run(["ffmpeg", "-v", "error", "-y", "-ss", f"{vdur - 0.05:.2f}", "-i", str(boxed_tmp),
     "-frames:v", "1", str(still)])
print("still:", Image.open(still).size, flush=True)

tmp = WORK / "final-tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_tmp),
     "-loop", "1", "-framerate", "30", "-t", f"{freeze:.2f}", "-i", str(still),
     "-i", str(WORK / "full-audio.wav"),
     "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[v]",
     "-map", "[v]", "-map", "2:a",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", "-t", str(total), str(tmp)])
final = DELIVERY / "ep011-master-2k.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp),
     "-af", "loudnorm=I=-15.5:TP=-1.0:LRA=11,aresample=48000",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", str(total), str(final)])
finfo = probe(final)
print(f"FINAL: {final} fmt={float(finfo['format']['duration']):.2f}s", flush=True)
for s in finfo["streams"]:
    print(f"  {s['codec_type']}: {s['codec_name']} dur={float(s.get('duration', 0)):.2f} " +
          (f"{s['width']}x{s['height']} fps={s.get('avg_frame_rate')}" if s["codec_type"] == "video" else
           f"ch={s.get('channels')} sr={s.get('sample_rate')}"), flush=True)
r = run(["ffmpeg", "-v", "info", "-i", str(final), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        check=False)
js = r.stderr[r.stderr.find("{"):r.stderr.find("}") + 1]
print("final loudnorm measure:", js.replace("\\n", " ").replace("\\t", " "), flush=True)

# ============ QC: energy per shot on final audio ============
print("== QC: energy per shot (final) ==", flush=True)
run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vn", "-ac", "2", "-ar", "48000",
     "-c:a", "pcm_s16le", str(WORK / "final-48k.wav")])
d, _, _ = wav_read(WORK / "final-48k.wav")
mm = np.abs(d).max(axis=1)
hop10 = SR // 10
for sh, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    seg = mm[int(t0*SR):int(t1*SR)]
    bmax = [float(mm[b*hop10:(b+1)*hop10].max()) for b in range(int(t0*10), int(t1*10))]
    print(f"  {sh} {t0:.1f}-{t1:.1f}s peak={seg.max():.3f} mean={seg.mean():.4f} "
          f"buckets0.1s: {' '.join(f'{x:.2f}' for x in bmax)}", flush=True)
print("  laugh zone (last-word-end to total):", flush=True)
print("   ", " ".join(f"{b/10:.1f}:{mm[b*hop10:(b+1)*hop10].max():.3f}"
                      for b in range(int(LAST_WORD_END*10), int(total*10))), flush=True)

# ============ QC: SFX per-channel check ============
print("== QC: laugh per channel ==", flush=True)
L, R = d[:, 0], d[:, 1]
lz0, lz1 = int(LAUGH_AUDIBLE_AT * SR), int(total * SR)
pre0, pre1 = int((LAST_WORD_END - 1.0) * SR), int(LAST_WORD_END * SR)
def rms(x):
    return float(np.sqrt((x.astype(np.float64) ** 2).mean()))
print(f"  laugh zone {LAUGH_AUDIBLE_AT:.2f}-{total:.2f}s: RMS L={rms(L[lz0:lz1]):.4f} R={rms(R[lz0:lz1]):.4f} "
      f"ratio={rms(L[lz0:lz1])/max(rms(R[lz0:lz1]), 1e-6):.2f}", flush=True)
print(f"  pre-laugh 1s ({LAST_WORD_END-1.0:.2f}-{LAST_WORD_END:.2f}s): RMS L={rms(L[pre0:pre1]):.4f} "
      f"R={rms(R[pre0:pre1]):.4f}", flush=True)
diff = L[lz0:lz1].astype(np.float64) - R[lz0:lz1].astype(np.float64)
summ = L[lz0:lz1].astype(np.float64) + R[lz0:lz1].astype(np.float64)
print(f"  laugh zone L-R RMS / L+R RMS = {rms(diff)/max(rms(summ), 1e-6):.3f} (small = both channels carry the laugh)", flush=True)
def env(x):
    h = SR // 100
    return np.array([np.abs(x[i*h:(i+1)*h]).max() for i in range(len(x)//h)])
eL, eR = env(L[lz0:lz1]), env(R[lz0:lz1])
cc = float(np.corrcoef(eL, eR)[0, 1])
print(f"  laugh-zone L/R envelope correlation = {cc:.3f} (near 1 = same laugh both channels)", flush=True)
assert 0.7 < rms(L[lz0:lz1])/max(rms(R[lz0:lz1]), 1e-6) < 1.4, "laugh L/R imbalance — one-channel leak?"
assert cc > 0.9, "laugh L/R envelopes uncorrelated — check the mix"

# ============ QC: frame means ============
print("== QC: frame means ==", flush=True)
for t in [0.5, 1.0, 3.0, 6.5, 7.0, 10.0, 13.6, 13.9, 16.0, 20.0, 22.0, 26.0, 26.5, 27.5, total - 0.1]:
    if t < total:
        print(f"  t={t:.1f}s mean={frame_mean(final, t):.1f}", flush=True)

# ============ QC: contact sheet ============
print("== QC: contact sheet ==", flush=True)
qcd = WORK / "qc"
qcd.mkdir(exist_ok=True)
def grab(t, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(final), "-frames:v", "1", str(out)])
mids = []
for sh, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    fp = qcd / f"final-mid-{sh}.png"
    grab((t0 + t1) / 2, fp)
    mids.append(Image.open(fp).convert("RGB"))
cuts = []
for sh, _ in SEGS[1:]:
    t0, _ = BOUNDS[sh]
    for dt, tag in [(-0.06, "pre"), (0.06, "post")]:
        fp = qcd / f"final-cut-{sh}-{tag}.png"
        grab(t0 + dt, fp)
        cuts.append(Image.open(fp).convert("RGB"))
sheet = Image.new("RGB", (270*4, 480 + 480), "white")
for i, im in enumerate(mids):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 0))
for i, im in enumerate(cuts):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 480))
sheet.save(WORK / "qc-contact.png")
print(f"contact sheet: {WORK / 'qc-contact.png'} (row1 mids, row2 cut frames)", flush=True)

# ============ QC: Whisper transcript of final ============
print("== QC: whisper transcript (final) ==", flush=True)
run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vn", "-ac", "1", "-ar", "16000",
     "-c:a", "pcm_s16le", str(WORK / "final-16k.wav")])
d16f, sr16f, _ = wav_read(WORK / "final-16k.wav")
from faster_whisper import WhisperModel
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base",
                     device="cpu", compute_type="int8", local_files_only=True)
segs_f, _ = model.transcribe(d16f, language="vi", word_timestamps=True, beam_size=5)
n_words = 0
for s in segs_f:
    for wd in (s.words or []):
        n_words += 1
        print(f"  {wd.start:.2f}-{wd.end:.2f} {wd.word.strip()!r} p={wd.probability:.2f}", flush=True)
print(f"final whisper words: {n_words}", flush=True)

# ============ cover candidate (sh040 6.5s) ============
COVER_T = BOUNDS["sh040"][0] + 6.5
cover = DELIVERY / "ep011-cover-thaomy.jpg"
run(["ffmpeg", "-v", "error", "-y", "-ss", f"{COVER_T:.2f}", "-i", str(final),
     "-frames:v", "1", "-q:v", "2", str(cover)])
print(f"cover candidate: {cover} (master t={COVER_T:.2f}s = sh040 6.5s)", flush=True)
print(f"FINAL SHA: {sha(final)}", flush=True)
print("RESUME BUILD DONE", flush=True)
