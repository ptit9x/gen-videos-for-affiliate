"""Build ep008 'Con Nho Do' 1K preview master (28.6s, 1080x1920 30fps).

Stages (mirrors ep006 build_stage1/2/3):
  1. segments: trim to use_range, crop 640:1138:40:0 (removes bottom-right
     Veo sparkle + "Veo" text, verified present on ALL 7 shots; ep006-equivalent
     crop, faces/hands verified safe), scale 1080x1920 lanczos, fps=30
     -> concat FILTER (never demuxer+copy) -> loudnorm I=-15.5 -> assembly
  2. captions: Whisper base word timestamps on assembly audio, align to
     script words IN ORDER (Whisper mishears tones: "chia tay"->"chi tai",
     "Giua"->"du", "Lo"->"lua"), energy-refined, clamped to shot bounds
     -> captions.json + cut.mp4 + meta.json -> Remotion Boxed render
     (accent #F59E0B, no title card) to a TEMP file, verified, then used
  3. laugh: Laugh Track 1 (CC BY LittleRainySeasons) mixed over sh070
     (audible onset 25.7s, 0.1s into the reaction shot), numpy mix,
     NO freeze tail (laugh ends ~27.8s < 28.6s video) -> final loudnorm
     -> edit/ep008-master-1k-preview.mp4 + .srt
QC prints: per-shot durations, energy per shot, Whisper transcript.
"""
import json, os, pathlib, shutil, subprocess, wave
import numpy as np
from PIL import Image

GEN = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep008-con-nho-do/generated")
EDIT = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep008-con-nho-do/edit")
WORK = EDIT / "build1k"
WORK.mkdir(parents=True, exist_ok=True)
REMO = pathlib.Path("/home/hatch/workspace/remotion-captions-test")
PUB = REMO / "public"
LAUGH = pathlib.Path("/home/hatch/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3")
SR = 48000
CROP = "crop=640:1138:40:0"

SEGS = [
    ("sh010", "sh010-take005-dub-thaomy-wordalign.mp4", 2.8),
    ("sh020", "sh020-take003.mp4", 3.6),
    ("sh030", "sh030-take002-dub-thaomy-wordalign.mp4", 5.2),
    ("sh040", "sh040-take004.mp4", 5.0),
    ("sh050", "sh050-take002.mp4", 2.0),
    ("sh060", "sh060-take015.mp4", 7.0),
    ("sh070", "sh070-take002.mp4", 3.0),
]
SCRIPT = {
    "sh010": ["Anh", "yêu", "em", "hay", "là", "yêu", "con", "đó?"],
    "sh020": ["Con", "đó", "là", "đứa", "nào?", "Anh", "còn", "không", "biết."],
    "sh030": ["Giữa", "em", "với", "con", "đó,", "anh", "chọn", "ai?", "Lỡ", "có", "thì", "sao?"],
    "sh040": ["Cho", "là", "anh", "có", "đi,", "anh", "vẫn", "chọn", "em."],
    "sh050": ["Thế", "là", "anh", "có", "thật", "à?"],
    "sh060": ["Ừ,", "thừa", "nhận", "luôn:", "anh", "yêu", "con", "đó.", "Chia", "tay", "đi,", "yêu", "khổ", "quá."],
    "sh070": [],
}
SRT_LINES = {
    "sh010": ["Anh yêu em hay là yêu con đó?"],
    "sh020": ["Con đó là đứa nào?", "Anh còn không biết."],
    "sh030": ["Giữa em với con đó, anh chọn ai?", "Lỡ có thì sao?"],
    "sh040": ["Cho là anh có đi, anh vẫn chọn em."],
    "sh050": ["Thế là anh có thật à?"],
    "sh060": ["Ừ, thừa nhận luôn: anh yêu con đó.", "Chia tay đi, yêu khổ quá."],
}
BOUNDS = {}
_t = 0.0
for sh, _, dur in SEGS:
    BOUNDS[sh] = (_t, _t + dur)
    _t += dur
TOTAL = _t
print(f"bounds: {BOUNDS} total={TOTAL:.1f}s")

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

# ============ STAGE 1: segments ============
print("== stage 1: segments ==")
seg_durs = {}
for sh, src, T in SEGS:
    srcp = GEN / src
    assert srcp.exists(), f"missing source {srcp}"
    out = WORK / f"seg-{sh}.mp4"
    vf = f"trim=0:{T},setpts=PTS-STARTPTS,{CROP},scale=1080:1920:flags=lanczos,fps=30"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(srcp), "-vf", vf,
         "-af", f"atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo",
         "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-t", str(T), str(out)])
    info = probe(out)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"][0]
    seg_durs[sh] = float(info["format"]["duration"])
    print(f"  {sh}: fmt={seg_durs[sh]:.2f}s v={v['width']}x{v['height']} {v.get('avg_frame_rate')} "
          f"a={a['codec_name']} {a['sample_rate']}Hz {a['channels']}ch (trim {T}s)")

# ============ concat FILTER ============
inputs = []
for sh, _, _ in SEGS:
    inputs += ["-i", str(WORK / f"seg-{sh}.mp4")]
fc = "".join(f"[{i}:v][{i}:a]" for i in range(len(SEGS))) + f"concat=n={len(SEGS)}:v=1:a=1[v][a]"
raw = WORK / "assembly-raw.mp4"
run(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", str(raw)])
print(f"concat raw: fmt={float(probe(raw)['format']['duration']):.2f}s")

# ============ loudnorm -> assembly ============
asm = WORK / "assembly-norm.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(raw),
     "-af", "loudnorm=I=-15.5:TP=-1.0:LRA=11",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", str(asm)])
info = probe(asm)
print(f"assembly-norm: fmt={float(info['format']['duration']):.2f}s (expect {TOTAL:.2f}s)")
for s in info["streams"]:
    print(f"  {s['codec_type']}: {s['codec_name']} dur={float(s.get('duration', 0)):.2f} " +
          (f"{s['width']}x{s['height']}" if s["codec_type"] == "video" else
           f"ch={s.get('channels')} sr={s.get('sample_rate')}"))
r = run(["ffmpeg", "-v", "info", "-i", str(asm), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        check=False)
js = r.stderr[r.stderr.find("{"):r.stderr.find("}") + 1]
print("loudnorm measure:", js.replace("\\n", " ").replace("\\t", " "))
json.dump({k: list(v) for k, v in BOUNDS.items()}, open(WORK / "bounds.json", "w"), indent=1)

# ============ STAGE 2: captions from assembly audio ============
print("== stage 2: captions ==")
run(["ffmpeg", "-v", "error", "-y", "-i", str(asm), "-vn", "-ac", "1", "-ar", "16000",
     "-c:a", "pcm_s16le", str(WORK / "assembly-16k.wav")])
d16, sr16, _ = wav_read(WORK / "assembly-16k.wav")
print(f"audio: {len(d16)/sr16:.2f}s @ {sr16}Hz")
from faster_whisper import WhisperModel
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base",
                     device="cpu", compute_type="int8", local_files_only=True)
segments_w, _ = model.transcribe(d16, language="vi", word_timestamps=True, beam_size=5)
raw_w = []
for s in segments_w:
    for wd in (s.words or []):
        raw_w.append({"heard": wd.word.strip(), "start": wd.start, "end": wd.end, "p": wd.probability})
print(f"whisper words: {len(raw_w)}")
for x in raw_w:
    print(f"  {x['start']:.2f}-{x['end']:.2f} {x['heard']!r} p={x['p']:.2f}")

hop = sr16 // 100
buckets = np.array([np.abs(d16[i*hop:(i+1)*hop]).max() if (i+1)*hop <= len(d16) else 0.0
                    for i in range(len(d16)//hop + 1)])
def refine(start, end):
    i0, i1 = int(start*100), int(end*100)
    act = np.where(buckets[max(0, i0):i1+1] > 0.02)[0]
    if len(act) == 0:
        return start, end
    return max(0.0, (i0 + act[0]) / 100), min(len(d16)/sr16, (i0 + act[-1] + 1) / 100)

def norm(w):
    return w.strip().strip("'\".,?!:").lower()

shots = [sh for sh, _ in SCRIPT.items() if SCRIPT[sh]]
assigned = {}
for sh in shots:
    t0, t1 = BOUNDS[sh]
    assigned[sh] = [x for x in raw_w if t0 <= (x["start"] + x["end"]) / 2 < t1]
for i, sh in enumerate(shots[:-1]):
    nxt = shots[i + 1]
    if assigned[sh] and norm(assigned[sh][-1]["heard"]) == norm(SCRIPT[nxt][0]):
        moved = assigned[sh].pop()
        assigned[nxt].insert(0, moved)
        print(f"boundary fix: moved {moved['heard']!r} {moved['start']:.2f}-{moved['end']:.2f} from {sh} to {nxt}")

caps = []
problems = []
for sh, words in SCRIPT.items():
    if not words:
        continue
    t0, t1 = BOUNDS[sh]
    mine = assigned[sh]
    print(f"{sh}: whisper={len(mine)} script={len(words)}")
    if len(mine) != len(words):
        problems.append(f"{sh}: whisper {len(mine)} != script {len(words)}")
    n = min(len(mine), len(words))
    timed = []
    for i in range(n):
        s, e = refine(mine[i]["start"], mine[i]["end"])
        s = max(s, t0); e = min(e, t1)
        if e <= s:
            e = s + 0.05
        timed.append((s, e))
    # fallback interpolation for script words without whisper timing
    if n < len(words):
        if timed:
            last_e = timed[-1][1]
            gap = max(0.05, (t1 - last_e) / (len(words) - n))
            for i in range(n, len(words)):
                s = min(last_e + (i - n) * gap, t1 - 0.05)
                timed.append((s, min(s + gap * 0.8, t1)))
                problems.append(f"{sh}: interpolated timing for {words[i]!r} (no whisper word)")
        else:
            gap = (t1 - t0) / len(words)
            for i in range(len(words)):
                timed.append((t0 + i * gap, min(t0 + (i + 1) * gap, t1)))
            problems.append(f"{sh}: ALL timings interpolated (whisper heard nothing)")
    for i, wtext in enumerate(words):
        s, e = timed[i]
        caps.append({"text": wtext, "startMs": round(s*1000), "endMs": round(e*1000),
                     "timestampMs": round(s*1000), "confidence": round(mine[i]["p"], 2) if i < len(mine) else 0.0,
                     "_heard": mine[i]["heard"] if i < len(mine) else "(interp)", "_shot": sh})

for a, b in zip(caps, caps[1:]):
    if a["endMs"] > b["startMs"] + 1:
        a["endMs"] = b["startMs"]
        problems.append(f"clamped overlap: {a['text']} end -> {a['endMs']}")

print(f"caps: {len(caps)} (expect {sum(len(v) for v in SCRIPT.values())})")
for c in caps:
    print(f"  {c['_shot']} {c['startMs']/1000:.2f}-{c['endMs']/1000:.2f} {c['text']!r} (heard {c['_heard']!r})")
if problems:
    print("PROBLEMS:")
    for p in problems:
        print("  -", p)
    (WORK / "captions-PROBLEMS.txt").write_text("\n".join(problems))
else:
    print("alignment clean")

# SRT sidecar: one cue per shot
def srt_time(ms):
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
cues = []
for i, (sh, words) in enumerate(SCRIPT.items(), 1):
    if not words:
        continue
    mine = [c for c in caps if c["_shot"] == sh]
    if not mine:
        continue
    cues.append(f"{i}\n{srt_time(mine[0]['startMs'])} --> {srt_time(mine[-1]['endMs'])}\n" +
                "\n".join(SRT_LINES[sh]) + "\n")
(EDIT / "ep008-master-1k-preview.srt").write_text("\n".join(cues), encoding="utf-8")
print(f"SRT: {len(cues)} cues -> {EDIT / 'ep008-master-1k-preview.srt'}")

# backup current remotion public inputs, then install ours
i = 0
while True:
    name = "public-ep006-backup" if i == 0 else f"public-ep006-backup-{i}"
    backup = REMO / name
    if not backup.exists():
        break
    i += 1
backup.mkdir(exist_ok=True)
for f in ["captions.json", "cut.mp4", "meta.json"]:
    if (PUB / f).exists():
        shutil.copy2(PUB / f, backup / f)
print(f"backed up previous remotion inputs to {backup}")
shutil.copy2(asm, PUB / "cut.mp4")
for c in caps:
    c.pop("_heard", None); c.pop("_shot", None)
json.dump(caps, open(PUB / "captions.json", "w"), ensure_ascii=False, indent=1)
pj = json.loads(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-show_entries", "stream=width,height,avg_frame_rate", "-of", "json",
                     str(PUB / "cut.mp4")]).stdout)
dur = float(pj["format"]["duration"])
st = pj["streams"][0]
num, den = st["avg_frame_rate"].split("/")
meta = {"width": st["width"], "height": st["height"], "fps": round(int(num)/int(den)),
        "duration": dur, "src": "cut.mp4"}
json.dump(meta, open(PUB / "meta.json", "w"), indent=1)
print("meta:", meta)
print("CAPTIONS DONE")

# ============ REMOTION BOXED RENDER ============
print("== remotion boxed render ==")
BROWSER = "/home/hatch/.cache/hyperframes/chrome/chrome-headless-shell/linux-131.0.6778.85/chrome-headless-shell-linux64/chrome-headless-shell"
assert pathlib.Path(BROWSER).exists(), "chrome-headless-shell 131 missing"
boxed_tmp = REMO / "out" / "ep008-boxed-tmp.mp4"
boxed_tmp.unlink(missing_ok=True)
import time
t_render = time.time()
r = run(["npx", "remotion", "render", "Boxed", str(boxed_tmp),
         "--props", '{"accent":"#F59E0B"}',
         "--browser-executable", BROWSER, "--concurrency=2", "--crf=18"],
        check=False, cwd=str(REMO))
open(WORK / "render.log", "w").write(r.stdout + "\n---STDERR---\n" + r.stderr)
print(f"remotion exit={r.returncode} wall={time.time()-t_render:.0f}s")
if r.returncode != 0:
    print("RENDER FAILED, last 3000 chars of log:")
    print((r.stdout + r.stderr)[-3000:])
    raise SystemExit(1)
assert boxed_tmp.exists() and boxed_tmp.stat().st_size > 1_000_000, "render output missing/too small"
binfo = probe(boxed_tmp)
bvdur = float([s for s in binfo["streams"] if s["codec_type"] == "video"][0]["duration"])
print(f"boxed tmp: {boxed_tmp} size={boxed_tmp.stat().st_size} vdur={bvdur:.2f}s (expect {TOTAL:.2f}s)")
assert abs(bvdur - TOTAL) < 0.5, f"boxed duration {bvdur} != {TOTAL}"

# ============ STAGE 3: laugh over sh070 (no freeze tail) ============
print("== stage 3: laugh track 1 over sh070 ==")
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_tmp), "-vn", "-ac", "2", "-ar", "48000",
     "-c:a", "pcm_s16le", str(WORK / "boxed-48k.wav")])
dlg, _, _ = wav_read(WORK / "boxed-48k.wav")
run(["ffmpeg", "-v", "error", "-y", "-i", str(LAUGH),
     "-vn", "-ac", "2", "-ar", "48000", "-c:a", "pcm_s16le", str(WORK / "laugh1-48k.wav")])
laugh, _, _ = wav_read(WORK / "laugh1-48k.wav")
if laugh.ndim == 1:
    laugh = np.stack([laugh, laugh], axis=1)
laugh_dur = len(laugh) / SR
print(f"dialogue {len(dlg)/SR:.2f}s peak {np.abs(dlg).max():.3f}; laugh {laugh_dur:.2f}s peak {np.abs(laugh).max():.3f}")
hop100 = SR // 100
m = np.abs(laugh).max(axis=1)
buckets = np.array([m[i*hop100:(i+1)*hop100].max() for i in range(len(m)//hop100)])
onset = float(np.where(buckets > 0.05)[0][0] / 100)
print(f"laugh onset in file: {onset:.2f}s")
# sh070 starts at 25.6s; audible laugh 0.1s into the reaction shot
LAUGH_AUDIBLE_AT = 25.7
stem_start = round(LAUGH_AUDIBLE_AT - onset, 2)
laugh_end = stem_start + laugh_dur
print(f"stem_start={stem_start}s (audible ~{LAUGH_AUDIBLE_AT:.2f}s), laugh ends {laugh_end:.2f}s, "
      f"video ends {TOTAL:.2f}s -> no freeze tail needed")
assert laugh_end < TOTAL, "laugh would overrun the video"

total = TOTAL
full = np.zeros((int(total * SR), 2), dtype=np.float32)
full[:len(dlg)] += dlg
s0 = int(stem_start * SR)
full[s0:s0 + len(laugh)] += laugh
peak = np.abs(full).max()
print(f"mixed peak: {peak:.3f}")
if peak > 0.98:
    gain = 0.98 / peak
    full = np.zeros((int(total * SR), 2), dtype=np.float32)
    full[:len(dlg)] += dlg
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
segs_f, _ = model.transcribe(d16f, language="vi", word_timestamps=False, beam_size=5)
for s in segs_f:
    print(f"  {s.start:.2f}-{s.end:.2f} {s.text.strip()!r}")

# ============ build report ============
import hashlib
def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
report = f"""# ep008 master 1K preview — build report

## Outputs
- Preview: `edit/ep008-master-1k-preview.mp4` sha256 `{sha(final)}`
- SRT: `edit/ep008-master-1k-preview.srt`
- Script: `edit/build_master_1k.py` (stages 1-3 + QC, this file)
- Work dir: `edit/build1k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render.log, boxed tmp inputs in remotion public/, qc-contact.png)

## Sources (all 1K 720x1280 24fps, from generated/)
- sh010 sh010-take005-dub-thaomy-wordalign.mp4 (clone ThaoMy, word-aligned) trim 0-2.8s
- sh020 sh020-take003.mp4 (native) trim 0-3.6s
- sh030 sh030-take002-dub-thaomy-wordalign.mp4 (clone ThaoMy, word-aligned) trim 0-5.2s
- sh040 sh040-take004.mp4 (native) trim 0-5.0s (sentence 2 cut by design)
- sh050 sh050-take002.mp4 (native) trim 0-2.0s
- sh060 sh060-take015.mp4 (native, NOT the dub-minhquan spare) trim 0-7.0s
- sh070 sh070-take002.mp4 (native, silent) trim 0-3.0s
- Total {TOTAL:.1f}s. Bounds: {BOUNDS}

## Stage 1 commands (per segment)
ffmpeg -i <src> -vf "trim=0:<T>,setpts=PTS-STARTPTS,{CROP},scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[6:v][6:a]concat=n=7:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11 (ep006 pattern), video copy

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on ALL 7 shots (top-right
  corners clean foliage). Icon top edge ranges y~1180-1221 across shots (720x1280 coords).
- Uniform crop {CROP} (=640x1138 window, x 40..680, y 0..1138, then lanczos to
  1080x1920): removes the icon on every shot with ~40px margin. One uniform crop
  (not per-shot) so framing/scale stays consistent across hard cuts; per-shot crops
  would visibly change zoom shot-to-shot. Faces/hands verified safe on mid frames
  (hands lowest ~y1010 in sh070, well above the 1138 cut line).
- Segment durations measured: {seg_durs}

## Stage 2 captions (Remotion Boxed)
- Whisper base word timestamps on assembly audio, aligned to script words IN ORDER,
  energy-refined (10ms buckets, thr 0.02), clamped to shot bounds, overlaps clamped.
  Known ASR artifacts ignored by design: "chia tay"->"chi tai", "Giua"->"du", "Lo"->"lua".
- Render: cd remotion-captions-test && npx remotion render Boxed out/ep008-boxed-tmp.mp4
  --props '{{"accent":"#F59E0B"}}' --browser-executable <chrome-headless-shell-131>
  --concurrency=2 --crf=18  (log: edit/build1k/render.log; temp file verified by
  exit code + fresh timestamp + probed duration before use; no title card)
- Remotion version: @remotion/cli ^4.0.0 (package.json), template remotion-captions,
  Boxed composition, 1080x1920, fps from meta.json (30).
- Caption problems (if any): see edit/build1k/captions-PROBLEMS.txt (empty = clean).

## Stage 3 laugh
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix over sh070, audible onset {LAUGH_AUDIBLE_AT:.1f}s (0.1s into the
  reaction shot), stem_start={stem_start:.2f}s, laugh ends {laugh_end:.2f}s < {TOTAL:.1f}s.
- NO freeze-frame tail (ep006 stage1 pattern has none; laugh fits inside the video).
- Final loudnorm I=-15.5:TP=-1.0:LRA=11 after the mix, video copy.
- FLAG: laugh-over-sh070 placement is the series pattern but the user has NOT
  explicitly confirmed it for ep008 — he can say remove.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, 28.6s, AAC 48kHz stereo).
- Energy per shot + sh070 laugh-zone buckets: see script output above.
- Contact sheet: edit/build1k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: see script output above (record only; script words govern captions).
"""
(WORK / "build-report.md").write_text(report)
print(report)
print("STAGE 1K DONE")
