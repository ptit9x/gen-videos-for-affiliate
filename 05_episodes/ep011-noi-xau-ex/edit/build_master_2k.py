"""Build ep011 'Nói Xấu Ex' FINAL 2K master (1080x1920 30fps).

Adapted from ep010 edit/build_master_2k.py (approved 2K master, 2026-11-23).
Differences vs ep010:
  - 4 shots, NO chat insert, NO title card. Remotion props: {"accent": "#F59E0B"} only.
  - Sources (all TRUE 2K 1080x1920, frame-diff verified vs approved 1K takes):
      sh010 generated/sh010-take001-1080p.mp4 (native, Dũng Southern, accepted)
      sh020 generated/sh020-take001-dubbed-1080p.mp4 (clone ThaoMy wordalign, video from
            2K + clone audio, native fully replaced; APPROVED by Richard 12:05 24/11)
      sh030 generated/sh030-take002-1080p.mp4 (native, Dũng Southern, accepted)
      sh040 generated/sh040-take001-1080p.mp4 (native, My Northern, accepted)
  - Trims (measured 2026-11-24, energy envelope 48kHz stereo 0.1s buckets +
    Whisper base word timestamps on the 2K files; speech end + beat):
      sh010 native speech 0.00-5.68s -> trim 6.4s (beat 0.72s; eyes close ~5.8s,
        he settles/bows — the cut lands on the sad settle, before the deep bow ~7.5s)
      sh020 dubbed speech clusters 1.00-1.90 / 2.80-4.20 / 5.85-6.65 -> trim 7.35s
        (beat 0.70s; Whisper smears first word to 0.72s — energy proves onset 1.00s)
      sh030 take002 speech 0.00-5.48s -> trim 6.2s (beat 0.72s; eyes close ~5.8s,
        head bowed ~7.5s — cut before the bow)
      sh040 native speech 0.66-3.58s + 5.16-6.30s (two sentences; Whisper smears
        first word to 0.66s, energy onset ~0.9s) -> trim 7.7s (beat 1.40s — keeps
        the soft eyes-closed smile through 7.5s, ep010 pattern; laugh plays over it)
  - Crop: Veo sparkle + "Veo" text verified BOTTOM-RIGHT on sh010 + sh040 2K files
    (corner crops x900-1080/y1700-1920: star top ~y1735, "Veo" text ~y1855-1885),
    same relative position as ep010. Crop 960:1707:60:0 (x 60..1020, y 0..1707)
    + lanczos to 1080x1920 — same as ep008/ep010.
  - SFX: Laugh Track 1 right after the sh040 punchline (last word ends 26.25s
    master time). Laugh is 2.1s; video ends 27.65s, so a short freeze-frame tail
    (~0.6s, ep004 pattern) carries the laugh.
  - Caption alignment fix (known ASR artifact): Whisper hears sh030 "Bốn mối"
    as THREE words "Vũ / cũng / mỗi" (16 heard vs 15 script). The alignment
    drops the extra heard word "mỗi" (4.02-4.22s) before assigning, so "Bốn"
    gets "Vũ" (3.60-3.88) and "mối" gets "cũng" (3.88-4.02).
  - Remotion render: chunked from the start (<=287 frames, --concurrency=1
    --muted). Full-render-at-concurrency-2 goes BLACK from ~13.7s (Chrome OOM,
    proven 2026-11-21). Each chunk verified (exit + size + duration + mean
    frame) before use.

Stages: 1 segments -> concat FILTER -> loudnorm -> 2 captions (Whisper base,
re-run on the assembly audio) -> Remotion Boxed chunked render -> 3 laugh +
freeze tail -> final loudnorm -> delivery/ -> QC + cover.
"""
import hashlib, json, os, pathlib, shutil, subprocess, time, wave
import numpy as np
from PIL import Image

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep011-noi-xau-ex")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "build2k"
WORK.mkdir(parents=True, exist_ok=True)
DELIVERY = EP / "delivery"
DELIVERY.mkdir(parents=True, exist_ok=True)
REMO = pathlib.Path("/home/hatch/workspace/remotion-captions-test")
PUB = REMO / "public"
LAUGH = pathlib.Path("/home/hatch/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3")
SR = 48000
CROP = "crop=960:1707:60:0"  # x 60..1020, y 0..1707; Veo icon top edge ~y1735

SEGS = [
    ("sh010", GEN / "sh010-take001-1080p.mp4", 6.4),
    ("sh020", GEN / "sh020-take001-dubbed-1080p.mp4", 7.35),
    ("sh030", GEN / "sh030-take002-1080p.mp4", 6.2),
    ("sh040", GEN / "sh040-take001-1080p.mp4", 7.7),
]
SCRIPT = {
    "sh010": ["Người", "yêu", "cũ", "anh", "tệ", "lắm", "em", "ơi.", "Ích", "kỷ,", "kiểm", "soát,", "không", "hiểu", "anh."],
    "sh020": ["Thương", "anh", "ghê.", "Chắc", "cô", "đó", "không", "xứng", "với", "anh.", "Rồi", "trước", "đó?"],
    "sh030": ["Cũng", "tệ.", "Mà", "cô", "trước", "nữa", "cũng", "vậy.", "Bốn", "mối", "rồi,", "lần", "nào", "cũng", "vậy."],
    "sh040": ["Bốn", "mối", "mà", "lần", "nào", "cũng", "lỗi", "người", "ta.", "Hay", "thật", "đấy", "anh."],
}
# SRT cue sentences per shot: (first word idx, last word idx, text)
SRT_CUES = {
    "sh010": [(0, 7, "Người yêu cũ anh tệ lắm em ơi."), (8, 14, "Ích kỷ, kiểm soát, không hiểu anh.")],
    "sh020": [(0, 2, "Thương anh ghê."), (3, 12, "Chắc cô đó không xứng với anh. Rồi trước đó?")],
    "sh030": [(0, 1, "Cũng tệ."), (2, 14, "Mà cô trước nữa cũng vậy. Bốn mối rồi, lần nào cũng vậy.")],
    "sh040": [(0, 8, "Bốn mối mà lần nào cũng lỗi người ta."), (9, 12, "Hay thật đấy anh.")],
}
BOUNDS = {}
_t = 0.0
for sh, _, dur in SEGS:
    BOUNDS[sh] = (_t, _t + dur)
    _t += dur
TOTAL = _t
print(f"bounds: {BOUNDS} total={TOTAL:.2f}s", flush=True)

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

# ============ STAGE 1: segments ============
print("== stage 1: segments (2K sources, single input each) ==", flush=True)
seg_durs = {}
for sh, src, T in SEGS:
    assert src.exists(), f"missing source {src}"
    print(f"  {sh} src sha {sha(src)[:8]}...", flush=True)
    out = WORK / f"seg-{sh}.mp4"
    vf = f"trim=0:{T},setpts=PTS-STARTPTS,{CROP},scale=1080:1920:flags=lanczos,fps=30"
    af = f"atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", vf, "-af", af,
         "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-t", str(T), str(out)])
    info = probe(out)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"][0]
    seg_durs[sh] = float(info["format"]["duration"])
    print(f"  {sh}: fmt={seg_durs[sh]:.2f}s v={v['width']}x{v['height']} {v.get('avg_frame_rate')} "
          f"a={a['codec_name']} {a['sample_rate']}Hz {a['channels']}ch", flush=True)

# ============ concat FILTER ============
inputs = []
for sh, _, _ in SEGS:
    inputs += ["-i", str(WORK / f"seg-{sh}.mp4")]
fc = "".join(f"[{i}:v][{i}:a]" for i in range(len(SEGS))) + f"concat=n={len(SEGS)}:v=1:a=1[v][a]"
raw = WORK / "assembly-raw.mp4"
run(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", str(raw)])
print(f"concat raw: fmt={float(probe(raw)['format']['duration']):.2f}s", flush=True)

# ============ loudnorm -> assembly ============
asm = WORK / "assembly-norm.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(raw),
     "-af", "loudnorm=I=-15.5:TP=-1.0:LRA=11",
     "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", str(asm)])
info = probe(asm)
asm_dur = float(info["format"]["duration"])
print(f"assembly-norm: fmt={asm_dur:.2f}s (expect {TOTAL:.2f}s)", flush=True)
r = run(["ffmpeg", "-v", "info", "-i", str(asm), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        check=False)
js = r.stderr[r.stderr.find("{"):r.stderr.find("}") + 1]
print("loudnorm measure:", js.replace("\\n", " ").replace("\\t", " "), flush=True)
json.dump({k: list(v) for k, v in BOUNDS.items()}, open(WORK / "bounds.json", "w"), indent=1)

# ============ STAGE 2: captions from assembly audio ============
print("== stage 2: captions (Whisper base on assembly audio) ==", flush=True)
run(["ffmpeg", "-v", "error", "-y", "-i", str(asm), "-vn", "-ac", "1", "-ar", "16000",
     "-c:a", "pcm_s16le", str(WORK / "assembly-16k.wav")])
d16, sr16, _ = wav_read(WORK / "assembly-16k.wav")
print(f"audio: {len(d16)/sr16:.2f}s @ {sr16}Hz", flush=True)
from faster_whisper import WhisperModel
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base",
                     device="cpu", compute_type="int8", local_files_only=True)
segments_w, _ = model.transcribe(d16, language="vi", word_timestamps=True, beam_size=5)
raw_w = []
for s in segments_w:
    for wd in (s.words or []):
        raw_w.append({"heard": wd.word.strip(), "start": wd.start, "end": wd.end, "p": wd.probability})
print(f"whisper words: {len(raw_w)}", flush=True)
for x in raw_w:
    print(f"  {x['start']:.2f}-{x['end']:.2f} {x['heard']!r} p={x['p']:.2f}", flush=True)

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
        print(f"boundary fix: moved {moved['heard']!r} {moved['start']:.2f}-{moved['end']:.2f} from {sh} to {nxt}", flush=True)

# sh030 fix: Whisper hears "Bốn mối" as THREE words "Vũ / cũng / mỗi" (16 heard vs
# 15 script). Drop the extra heard word "mỗi" (~4.02-4.22s) so "Bốn" <- "Vũ",
# "mối" <- "cũng", and the rest re-aligns to the true words.
problems = []
if len(assigned["sh030"]) == 16:
    drop = [x for x in assigned["sh030"] if x["heard"] == "mỗi" and 3.9 <= x["start"] <= 4.3]
    if drop:
        assigned["sh030"].remove(drop[0])
        problems.append(f"sh030: dropped extra ASR word {drop[0]['heard']!r} "
                        f"{drop[0]['start']:.2f}-{drop[0]['end']:.2f} ('Bốn mối' heard as 'Vũ cũng mỗi')")
        print("sh030 fix:", problems[-1], flush=True)

caps = []
for sh, words in SCRIPT.items():
    if not words:
        continue
    t0, t1 = BOUNDS[sh]
    mine = assigned[sh]
    print(f"{sh}: whisper={len(mine)} script={len(words)}", flush=True)
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

print(f"caps: {len(caps)} (expect {sum(len(v) for v in SCRIPT.values())})", flush=True)
for c in caps:
    print(f"  {c['_shot']} {c['startMs']/1000:.2f}-{c['endMs']/1000:.2f} {c['text']!r} (heard {c['_heard']!r})", flush=True)
if problems:
    print("PROBLEMS:", flush=True)
    for p in problems:
        print("  -", p, flush=True)
    (WORK / "captions-PROBLEMS.txt").write_text("\n".join(problems))
else:
    print("alignment clean", flush=True)

def srt_time(ms):
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
cues = []
ci = 1
for sh, sentences in SRT_CUES.items():
    mine = [c for c in caps if c["_shot"] == sh]
    for (wi0, wi1, text) in sentences:
        w0, w1 = mine[wi0], mine[wi1]
        cues.append(f"{ci}\n{srt_time(w0['startMs'])} --> {srt_time(w1['endMs'])}\n{text}\n")
        ci += 1
(DELIVERY / "ep011-master-2k.srt").write_text("\n".join(cues), encoding="utf-8")
print(f"SRT: {len(cues)} cues -> {DELIVERY / 'ep011-master-2k.srt'}", flush=True)

# backup current remotion public inputs (ep010 2K), then install ep011 ours
backup = REMO / "public-ep010-2k-backup"
if backup.exists():
    i = 1
    while (REMO / f"public-ep010-2k-backup-{i}").exists():
        i += 1
    backup = REMO / f"public-ep010-2k-backup-{i}"
backup.mkdir(exist_ok=True)
for f in ["captions.json", "cut.mp4", "meta.json"]:
    if (PUB / f).exists():
        shutil.copy2(PUB / f, backup / f)
print(f"backed up previous remotion inputs to {backup}", flush=True)
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
print("meta:", meta, flush=True)
print("CAPTIONS DONE", flush=True)

# ============ REMOTION BOXED (NO TITLE), CHUNKED RENDER ============
print("== remotion boxed render (chunked, concurrency=1, muted) ==", flush=True)
BROWSER = "/home/hatch/.cache/hyperframes/chrome/chrome-headless-shell/linux-131.0.6778.85/chrome-headless-shell-linux64/chrome-headless-shell"
assert pathlib.Path(BROWSER).exists(), "chrome-headless-shell 131 missing"
total_frames = max(1, round(dur * meta["fps"]))
print(f"total frames: {total_frames} (dur {dur:.2f}s @ {meta['fps']}fps)", flush=True)
CHUNK = 287
ranges = []
s = 0
while s < total_frames:
    e = min(s + CHUNK - 1, total_frames - 1)
    ranges.append((s, e))
    s = e + 1
print(f"chunks: {ranges}", flush=True)
chunk_files = []
for ci, (f0, f1) in enumerate(ranges):
    out = REMO / "out" / f"ep011-boxed-2k-chunk{ci}.mp4"
    out.unlink(missing_ok=True)
    t0 = time.time()
    r = run(["npx", "remotion", "render", "Boxed", str(out),
             "--props", json.dumps({"accent": "#F59E0B"}),
             "--browser-executable", BROWSER, "--concurrency=1", "--crf=18",
             "--frames", f"{f0}-{f1}", "--muted"],
            check=False, cwd=str(REMO))
    (WORK / f"render-chunk{ci}.log").write_text(r.stdout + "\n---STDERR---\n" + r.stderr)
    print(f"chunk {ci} frames {f0}-{f1}: exit={r.returncode} wall={time.time()-t0:.0f}s", flush=True)
    if r.returncode != 0:
        print("CHUNK RENDER FAILED, last 3000 chars:")
        print((r.stdout + r.stderr)[-3000:])
        raise SystemExit(1)
    assert out.exists() and out.stat().st_size > 500_000, f"chunk {ci} output missing/too small"
    cinfo = probe(out)
    cdur = float(cinfo["format"]["duration"])
    expect = (f1 - f0 + 1) / meta["fps"]
    print(f"  chunk {ci}: size={out.stat().st_size} dur={cdur:.2f}s (expect {expect:.2f}s)", flush=True)
    assert abs(cdur - expect) < 0.3, f"chunk {ci} duration {cdur} != {expect}"
    mid_t = ((f1 - f0) / 2) / meta["fps"]  # relative to the CHUNK file, not master
    m = frame_mean(out, mid_t)
    print(f"  chunk {ci} mean frame @ {mid_t:.2f}s: {m:.1f}", flush=True)
    assert m > 10, f"chunk {ci} looks BLACK (mean {m})"
    chunk_files.append(out)

# concat video-only chunks, mux assembly audio
boxed_video = WORK / "boxed-video-only.mp4"
inputs = []
for f in chunk_files:
    inputs += ["-i", str(f)]
fc = "".join(f"[{i}:v]" for i in range(len(chunk_files))) + f"concat=n={len(chunk_files)}:v=1:a=0[v]"
run(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", fc, "-map", "[v]",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", str(boxed_video)])
print(f"boxed video-only: fmt={float(probe(boxed_video)['format']['duration']):.2f}s", flush=True)
boxed_tmp = REMO / "out" / "ep011-boxed-2k-tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_video), "-i", str(asm),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "copy", str(boxed_tmp)])
binfo = probe(boxed_tmp)
bvdur = float([s for s in binfo["streams"] if s["codec_type"] == "video"][0]["duration"])
print(f"boxed tmp: {boxed_tmp} size={boxed_tmp.stat().st_size} vdur={bvdur:.2f}s (expect {dur:.2f}s)", flush=True)
assert abs(bvdur - dur) < 0.5, f"boxed duration {bvdur} != {dur}"

# ============ STAGE 3: laugh after punchline + freeze tail (ep004 pattern) ============
print("== stage 3: laugh track 1 after sh040 punchline ==", flush=True)
LAST_WORD_END = caps[-1]["endMs"] / 1000
print(f"last word '{caps[-1]['text']}' ends {LAST_WORD_END:.2f}s", flush=True)
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
m = np.abs(laugh).max(axis=1)
buckets = np.array([m[i*hop100:(i+1)*hop100].max() for i in range(len(m)//hop100)])
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

# numpy mix (NO adelay — the one-channel-leak lesson; both channels get the stem)
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
for sh, _, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    seg = mm[int(t0*SR):int(t1*SR)]
    bmax = [float(mm[b*hop10:(b+1)*hop10].max()) for b in range(int(t0*10), int(t1*10))]
    print(f"  {sh} {t0:.1f}-{t1:.1f}s peak={seg.max():.3f} mean={seg.mean():.4f} "
          f"buckets0.1s: {' '.join(f'{x:.2f}' for x in bmax)}", flush=True)
print("  laugh zone (last-word-end to total):", flush=True)
print("   ", " ".join(f"{b/10:.1f}:{mm[b*hop10:(b+1)*hop10].max():.3f}"
                      for b in range(int(LAST_WORD_END*10), int(total*10))), flush=True)

# ============ QC: SFX per-channel check (the adelay-leak lesson) ============
print("== QC: laugh per channel ==", flush=True)
L, R = d[:, 0], d[:, 1]
lz0, lz1 = int(LAUGH_AUDIBLE_AT * SR), int(total * SR)
pre0, pre1 = int((LAST_WORD_END - 1.0) * SR), int(LAST_WORD_END * SR)
def rms(x):
    return float(np.sqrt((x.astype(np.float64) ** 2).mean()))
print(f"  laugh zone {LAUGH_AUDIBLE_AT:.2f}-{total:.2f}s: RMS L={rms(L[lz0:lz1]):.4f} R={rms(R[lz0:lz1]):.4f} "
      f"ratio={rms(L[lz0:lz1])/max(rms(R[lz0:lz1]), 1e-6):.2f}", flush=True)
print(f"  pre-laugh 1s ({LAST_WORD_END-1.0:.2f}-{LAST_WORD_END:.2f}s): RMS L={rms(L[pre0:pre1]):.4f} "
      f"R={rms(R[pre0:pre1]):.4f} (dialogue tail, should be low after word end)", flush=True)
diff = L[lz0:lz1].astype(np.float64) - R[lz0:lz1].astype(np.float64)
summ = L[lz0:lz1].astype(np.float64) + R[lz0:lz1].astype(np.float64)
print(f"  laugh zone L-R RMS / L+R RMS = {rms(diff)/max(rms(summ), 1e-6):.3f} (small = both channels carry the laugh)", flush=True)
# correlation of per-channel 10ms envelopes in the laugh zone
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

# ============ QC: contact sheet (mid per shot + around cuts) ============
print("== QC: contact sheet ==", flush=True)
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
sheet = Image.new("RGB", (270*4, 480 + 480), "white")
for i, im in enumerate(mids):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 0))
for i, im in enumerate(cuts):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 480))
sheet.save(WORK / "qc-contact.png")
print(f"contact sheet: {WORK / 'qc-contact.png'} (row1 mids, row2 cut frames)", flush=True)

# ============ QC: Whisper transcript of final (record only) ============
print("== QC: whisper transcript (final, record only) ==", flush=True)
run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vn", "-ac", "1", "-ar", "16000",
     "-c:a", "pcm_s16le", str(WORK / "final-16k.wav")])
d16f, sr16f, _ = wav_read(WORK / "final-16k.wav")
segs_f, _ = model.transcribe(d16f, language="vi", word_timestamps=True, beam_size=5)
for s in segs_f:
    for wd in (s.words or []):
        print(f"  {wd.start:.2f}-{wd.end:.2f} {wd.word.strip()!r} p={wd.probability:.2f}", flush=True)

# ============ cover candidate (sh040 6.5s, eyes open slight smile, looking at camera) ============
COVER_T = BOUNDS["sh040"][0] + 6.5
cover = DELIVERY / "ep011-cover-thaomy.jpg"
run(["ffmpeg", "-v", "error", "-y", "-ss", f"{COVER_T:.2f}", "-i", str(final),
     "-frames:v", "1", "-q:v", "2", str(cover)])
print(f"cover candidate: {cover} (master t={COVER_T:.2f}s = sh040 6.5s)", flush=True)

# ============ build report ============
report = f"""# ep011 master 2K FINAL — build report

## Outputs
- Final: `delivery/ep011-master-2k.mp4` sha256 `{sha(final)}`
- SRT: `delivery/ep011-master-2k.srt`
- Cover candidate: `delivery/ep011-cover-thaomy.jpg` (sh040 6.5s, master t={COVER_T:.2f}s)
- Script: `edit/build_master_2k.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build2k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, mid/cut frames in qc/, measure_2k.py + .log)
- Remotion inputs backed up to: `{backup}` (the ep010 2K inputs)

## Sources (all TRUE 2K 1080x1920, frame-diff verified vs the approved 1K takes)
- sh010 generated/sh010-take001-1080p.mp4 (native, Dũng Southern, accepted) — trim 0-6.4s
- sh020 generated/sh020-take001-dubbed-1080p.mp4 (clone ThaoMy wordalign, video from 2K + clone audio) — trim 0-7.35s
- sh030 generated/sh030-take002-1080p.mp4 (native, Dũng Southern, accepted) — trim 0-6.2s
- sh040 generated/sh040-take001-1080p.mp4 (native, My Northern, accepted) — trim 0-7.7s
- Nominal total {TOTAL:.2f}s; actual final {total:.2f}s (laugh + freeze tail).
  Bounds: {BOUNDS}

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,{CROP},scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[3:v][3:a]concat=n=4:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {seg_durs}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on sh010 + sh040 2K files
  (corner crops x900-1080/y1700-1920 at t=2.5s: star top ~y1735, "Veo" text
  ~y1855-1885), same relative position as ep010.
- Crop {CROP} = x 60..1020, y 0..1707, then lanczos to 1080x1920. Icon top edge
  ~28px below the crop line. One uniform crop so framing/scale matches across
  hard cuts.

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope on the 2K files)
- sh010 native speech 0.00-5.68s -> 6.4s (beat 0.72s; eyes close ~5.8s, settle/bow)
- sh020 dubbed speech clusters 1.00-1.90 / 2.80-4.20 / 5.85-6.65 -> 7.35s (beat 0.70s)
- sh030 take002 speech 0.00-5.48s -> 6.2s (beat 0.72s; eyes close ~5.8s, bow ~7.5s)
- sh040 native speech 0.66-3.58s + 5.16-6.30s -> 7.7s (beat 1.40s — keeps the
  soft eyes-closed smile through 7.5s, ep010 pattern; laugh plays over it)

## Stage 2 captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds.
- sh030 fix: dropped extra ASR word "mỗi" (see PROBLEMS / script) — "Bốn mối"
  is heard by Whisper as three words "Vũ / cũng / mỗi".
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep011-boxed-2k-chunk<N>.mp4 --props '{{"accent":"#F59E0B"}}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: {ranges} (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep011-boxed-2k-tmp.mp4.
- Caption problems (if any): see edit/build2k/captions-PROBLEMS.txt.

## Stage 3 laugh (Laugh Track 1 after the sh040 punchline)
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix (NO adelay — the one-channel-leak lesson) right after the
  sh040 punchline, audible onset {LAUGH_AUDIBLE_AT:.2f}s (last word ends
  {LAST_WORD_END:.2f}s + 0.15s), stem_start={stem_start:.2f}s, laugh ends {total:.2f}s.
- Freeze-frame tail {freeze:.2f}s (still of the last frame, ep004 pattern) so
  the laugh fits; video itself ends at {vdur:.2f}s.
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, AAC 48kHz stereo).
- Frame means: see script output above (black = mean ~0; joins + tail included).
- Energy per shot + laugh-zone buckets: see script output above.
- Laugh per-channel: see script output above (RMS L/R ratio, L-R/L+R, envelope correlation).
- Contact sheet: edit/build2k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: see script output above (record only; script words govern captions).
- Cover: delivery/ep011-cover-thaomy.jpg — CANDIDATE for Richard to confirm, not a decision.
"""
(WORK / "build-report.md").write_text(report)
print(report, flush=True)
print("BUILD 2K DONE", flush=True)
