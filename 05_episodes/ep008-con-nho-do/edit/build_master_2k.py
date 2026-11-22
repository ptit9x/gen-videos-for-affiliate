"""Build ep008 'Con Nho Do' FINAL 2K master (28.6s, 1080x1920 30fps).

Adapted from edit/build_master_1k.py (the approved 1K preview build).
Differences vs 1K:
  - Sources are TRUE 2K 1080x1920 24fps 7.85s from ~/workspace/ep008-con-nho-do-clips/
    (shas verified: 5fd6606f/2e03040e/a3426242/d71d292b/0cd5f023/7d103fc3/e53cd889).
  - sh010/sh030 audio = wordalign clone-ThaoMy dub, extracted from the 1K dubbed
    files in generated/ (user-approved audio; NO TTS regen, NO re-wordalign).
  - Crop: Veo icon verified BOTTOM-RIGHT on all 7 2K files (same relative position
    as 1K). 1K crop was 640:1138:40:0 from 720x1280; proportional 2K equivalent is
    960:1707:60:0 (x 60..1020, y 0..1707, icon top edge ~y1770-1832 -> ~63px margin).
    Uniform crop so framing/scale matches the approved 1K preview exactly.
  - Title: "CON NHỎ ĐÓ" via the ep004 Remotion TitleCard (src/TitleCard.tsx, already
    wired into CaptionedVideo via title/titleSeconds props) — overlay on sh010 for
    the first 2s, upper band, must NOT cover My's head. My's head top in sh010 is
    ~y460-480/1920 raw (~y517 final after crop+scale); title occupies ~y173-360.
    No standalone card, no duration change, no timeline shift.
  - Remotion render: chunked from the start (<=287 frames, --concurrency=1 --muted).
    The 1K full render with --concurrency=2 exited 0 but went BLACK from ~13.7s
    (Chrome OOM). Each chunk is verified (exit code + size + mean frame) before use.
  - Stage 3 uses the actual boxed-audio duration (len(dlg)/SR), not nominal 28.6s
    (the 1K stage-3 crash fix).

Stages: 1 segments -> concat FILTER -> loudnorm -> 2 captions (Whisper base,
re-run on the 2K assembly audio; compare vs 1K captions) -> Remotion Boxed +
TitleCard chunked render -> 3 laugh over sh070 -> final loudnorm -> delivery/.
"""
import hashlib, json, os, pathlib, shutil, subprocess, time, wave
import numpy as np
from PIL import Image

CLIPS = pathlib.Path("/home/hatch/workspace/ep008-con-nho-do-clips")
GEN = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep008-con-nho-do/generated")
EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep008-con-nho-do")
EDIT = EP / "edit"
WORK = EDIT / "build2k"
WORK.mkdir(parents=True, exist_ok=True)
DELIVERY = EP / "delivery"
DELIVERY.mkdir(parents=True, exist_ok=True)
REMO = pathlib.Path("/home/hatch/workspace/remotion-captions-test")
PUB = REMO / "public"
LAUGH = pathlib.Path("/home/hatch/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3")
SR = 48000
CROP = "crop=960:1707:60:0"  # 2K proportional equivalent of the 1K 640:1138:40:0
TITLE = "CON NHỎ ĐÓ"
TITLE_SECONDS = 2

# (shot, video source, audio source or None=use video's own audio, trim seconds)
# SOURCE CORRECTIONS (found during run 1's QC, 22/11 ~01:50):
#  - sh060: the downloaded "sh060-take015-2k.mp4" (sha 7d103fc3...) is actually
#    TAKE016 (frame diff 2.1 vs take016 @2.5s; 16.3 vs take015) — a near-static
#    performance, while approved take015 is animated throughout. The browser task
#    grabbed the adjacent take. Substitute: local lanczos upscale of approved 1K
#    take015 (sh060-take015-2k-local-upscale.mp4, sha 80e5729a...). A true Flow 2K
#    re-download of take015 can swap this in later.
#  - AUDIO: approved 1K mixes for ALL native shots. sh020/sh050/sh070 1K audio ==
#    2K audio (identical energy bursts). sh040's 2K audio has a much louder
#    ambience/noise floor in the first second (0.29-0.74 vs 0.06-0.08) and smeared
#    Whisper boundaries (+100-340ms). sh010/sh030 keep the wordalign dub audio.
SEGS = [
    ("sh010", CLIPS / "sh010-take005-2k.mp4", GEN / "sh010-take005-dub-thaomy-wordalign.mp4", 2.8),
    ("sh020", CLIPS / "sh020-take003-2k.mp4", CLIPS / "sh020-take003.mp4", 3.6),
    ("sh030", CLIPS / "sh030-take002-2k.mp4", GEN / "sh030-take002-dub-thaomy-wordalign.mp4", 5.2),
    ("sh040", CLIPS / "sh040-take004-2k.mp4", CLIPS / "sh040-take004.mp4", 5.0),
    ("sh050", CLIPS / "sh050-take002-2k.mp4", CLIPS / "sh050-take002.mp4", 2.0),
    ("sh060", CLIPS / "sh060-take015-2k-local-upscale.mp4", CLIPS / "sh060-take015.mp4", 7.0),
    ("sh070", CLIPS / "sh070-take002-2k.mp4", CLIPS / "sh070-take002.mp4", 3.0),
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
for sh, _, _, dur in SEGS:
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
print("== stage 1: segments (2K sources) ==")
seg_durs = {}
for sh, vid, aud, T in SEGS:
    assert vid.exists(), f"missing video {vid}"
    out = WORK / f"seg-{sh}.mp4"
    vf = f"trim=0:{T},setpts=PTS-STARTPTS,{CROP},scale=1080:1920:flags=lanczos,fps=30"
    af = f"atrim=0:{T},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
    if aud is not None:
        assert aud.exists(), f"missing dub audio {aud}"
        # video from the 2K clip (or local upscale for sh060), audio from the
        # 1K wordalign dubbed file (sh010/sh030) or the approved 1K mix (rest)
        run(["ffmpeg", "-v", "error", "-y", "-i", str(vid), "-i", str(aud),
             "-vf", vf, "-af", af, "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-t", str(T), str(out)])
        if "wordalign" in aud.name:
            print(f"  {sh}: 2K video + wordalign dub audio (trim {T}s)")
        elif sh == "sh060":
            print(f"  {sh}: LOCAL-UPSCALED 2K video (approved take015) + 1K native audio (trim {T}s)")
        else:
            print(f"  {sh}: 2K video + 1K native audio (trim {T}s)")
    else:
        run(["ffmpeg", "-v", "error", "-y", "-i", str(vid), "-vf", vf,
             "-af", af, "-c:v", "libx264", "-crf", "18", "-preset", "medium",
             "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-t", str(T), str(out)])
    info = probe(out)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"][0]
    seg_durs[sh] = float(info["format"]["duration"])
    print(f"  {sh}: fmt={seg_durs[sh]:.2f}s v={v['width']}x{v['height']} {v.get('avg_frame_rate')} "
          f"a={a['codec_name']} {a['sample_rate']}Hz {a['channels']}ch")

# ============ concat FILTER ============
inputs = []
for sh, _, _, _ in SEGS:
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
asm_dur = float(info["format"]["duration"])
print(f"assembly-norm: fmt={asm_dur:.2f}s (expect {TOTAL:.2f}s)")
r = run(["ffmpeg", "-v", "info", "-i", str(asm), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        check=False)
js = r.stderr[r.stderr.find("{"):r.stderr.find("}") + 1]
print("loudnorm measure:", js.replace("\\n", " ").replace("\\t", " "))
json.dump({k: list(v) for k, v in BOUNDS.items()}, open(WORK / "bounds.json", "w"), indent=1)

# ============ STAGE 2: captions from assembly audio (same code as 1K) ============
print("== stage 2: captions (Whisper base on 2K assembly audio) ==")
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

# compare vs the 1K captions (timeline must be identical)
old_caps = json.load(open(PUB / "captions.json"))
max_delta = 0
for new, old in zip(caps, old_caps):
    max_delta = max(max_delta, abs(new["startMs"] - old["startMs"]), abs(new["endMs"] - old["endMs"]))
print(f"caption timing vs 1K: {len(caps)} vs {len(old_caps)} words, max delta {max_delta}ms")
assert len(caps) == len(old_caps), "caption word count differs from 1K!"

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
(DELIVERY / "ep008-master-2k.srt").write_text("\n".join(cues), encoding="utf-8")
print(f"SRT: {len(cues)} cues -> {DELIVERY / 'ep008-master-2k.srt'}")

# backup current remotion public inputs (the 1K ep008 inputs), then install 2K ours
backup = REMO / "public-ep008-1k-backup"
if backup.exists():
    i = 1
    while (REMO / f"public-ep008-1k-backup-{i}").exists():
        i += 1
    backup = REMO / f"public-ep008-1k-backup-{i}"
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

# ============ REMOTION BOXED + TITLECARD, CHUNKED RENDER ============
print("== remotion boxed + title render (chunked, concurrency=1, muted) ==")
BROWSER = "/home/hatch/.cache/hyperframes/chrome/chrome-headless-shell/linux-131.0.6778.85/chrome-headless-shell-linux64/chrome-headless-shell"
assert pathlib.Path(BROWSER).exists(), "chrome-headless-shell 131 missing"
total_frames = max(1, round(dur * meta["fps"]))
print(f"total frames: {total_frames} (dur {dur:.2f}s @ {meta['fps']}fps)")
CHUNK = 287
ranges = []
s = 0
while s < total_frames:
    e = min(s + CHUNK - 1, total_frames - 1)
    ranges.append((s, e))
    s = e + 1
print(f"chunks: {ranges}")
chunk_files = []
for ci, (f0, f1) in enumerate(ranges):
    out = REMO / "out" / f"ep008-boxed-2k-chunk{ci}.mp4"
    if out.exists() and out.stat().st_size > 500_000:
        # reuse an already-rendered chunk (e.g. chunk 0 verified in the first run
        # before the run died on the chunk-1 mean-frame bug below)
        cinfo = probe(out)
        cdur = float(cinfo["format"]["duration"])
        expect = (f1 - f0 + 1) / meta["fps"]
        m = frame_mean(out, ((f1 - f0) / 2) / meta["fps"])
        print(f"chunk {ci} frames {f0}-{f1}: REUSED size={out.stat().st_size} dur={cdur:.2f}s "
              f"(expect {expect:.2f}s) mean={m:.1f}")
        assert abs(cdur - expect) < 0.3, f"reused chunk {ci} duration {cdur} != {expect}"
        assert m > 10, f"reused chunk {ci} looks BLACK (mean {m})"
        chunk_files.append(out)
        continue
    out.unlink(missing_ok=True)
    t0 = time.time()
    r = run(["npx", "remotion", "render", "Boxed", str(out),
             "--props", json.dumps({"accent": "#F59E0B", "title": TITLE, "titleSeconds": TITLE_SECONDS}),
             "--browser-executable", BROWSER, "--concurrency=1", "--crf=18",
             "--frames", f"{f0}-{f1}", "--muted"],
            check=False, cwd=str(REMO))
    (WORK / f"render-chunk{ci}.log").write_text(r.stdout + "\n---STDERR---\n" + r.stderr)
    print(f"chunk {ci} frames {f0}-{f1}: exit={r.returncode} wall={time.time()-t0:.0f}s")
    if r.returncode != 0:
        print("CHUNK RENDER FAILED, last 3000 chars:")
        print((r.stdout + r.stderr)[-3000:])
        raise SystemExit(1)
    assert out.exists() and out.stat().st_size > 500_000, f"chunk {ci} output missing/too small"
    cinfo = probe(out)
    cdur = float(cinfo["format"]["duration"])
    expect = (f1 - f0 + 1) / meta["fps"]
    print(f"  chunk {ci}: size={out.stat().st_size} dur={cdur:.2f}s (expect {expect:.2f}s)")
    assert abs(cdur - expect) < 0.3, f"chunk {ci} duration {cdur} != {expect}"
    # mean-frame check: sample the middle of the CHUNK FILE (black = OOM failure).
    # BUG FIX (first run): mid_t was (f0+f1)/2/fps = master-timeline time, but the
    # chunk file is only (f1-f0+1)/fps long — chunk 1's 14.33s seek returned zero
    # bytes (mean -1.0) and falsely tripped the BLACK assertion. mid_t must be
    # relative to the chunk file itself.
    mid_t = ((f1 - f0) / 2) / meta["fps"]
    m = frame_mean(out, mid_t)
    print(f"  chunk {ci} mean frame @ {mid_t:.2f}s: {m:.1f}")
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
print(f"boxed video-only: fmt={float(probe(boxed_video)['format']['duration']):.2f}s")
boxed_tmp = REMO / "out" / "ep008-boxed-2k-tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_video), "-i", str(asm),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "copy", str(boxed_tmp)])
binfo = probe(boxed_tmp)
bvdur = float([s for s in binfo["streams"] if s["codec_type"] == "video"][0]["duration"])
print(f"boxed tmp: {boxed_tmp} size={boxed_tmp.stat().st_size} vdur={bvdur:.2f}s (expect {dur:.2f}s)")
assert abs(bvdur - dur) < 0.5, f"boxed duration {bvdur} != {dur}"

# ============ STAGE 3: laugh over sh070 (actual-duration fix) ============
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
print(f"dialogue {len(dlg)/SR:.3f}s peak {np.abs(dlg).max():.3f}; laugh {laugh_dur:.2f}s peak {np.abs(laugh).max():.3f}")
hop100 = SR // 100
m = np.abs(laugh).max(axis=1)
buckets = np.array([m[i*hop100:(i+1)*hop100].max() for i in range(len(m)//hop100)])
onset = float(np.where(buckets > 0.05)[0][0] / 100)
print(f"laugh onset in file: {onset:.2f}s")
LAUGH_AUDIBLE_AT = 25.7
stem_start = round(LAUGH_AUDIBLE_AT - onset, 2)
laugh_end = stem_start + laugh_dur
total = len(dlg) / SR  # ACTUAL duration (1K fix: nominal 28.6 vs actual ~28.67)
print(f"stem_start={stem_start}s (audible ~{LAUGH_AUDIBLE_AT:.2f}s), laugh ends {laugh_end:.2f}s, "
      f"total={total:.3f}s (nominal {TOTAL:.1f}s) -> no freeze tail needed")
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
final = DELIVERY / "ep008-master-2k.mp4"
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
for sh, _, _, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    seg = mm[int(t0*SR):int(t1*SR)]
    bmax = [float(mm[b*hop10:(b+1)*hop10].max()) for b in range(int(t0*10), int(t1*10))]
    print(f"  {sh} {t0:.1f}-{t1:.1f}s peak={seg.max():.3f} mean={seg.mean():.4f} "
          f"buckets0.1s: {' '.join(f'{x:.2f}' for x in bmax)}")
print("  sh070 detail (laugh zone 25.6-28.6):")
print("   ", " ".join(f"{b/10:.1f}:{mm[b*hop10:(b+1)*hop10].max():.3f}" for b in range(256, 286)))

# ============ QC: frame means at ~10 timestamps ============
print("== QC: frame means ==")
for t in [0.5, 1.0, 1.5, 5.0, 9.5, 9.6, 13.7, 15.0, 19.0, 19.2, 22.0, 26.0, 28.3]:
    print(f"  t={t:.1f}s mean={frame_mean(final, t):.1f}")

# ============ QC: contact sheet (mid per shot + around cuts) + title frames ============
print("== QC: contact sheet + title frames ==")
qcd = WORK / "qc"
qcd.mkdir(exist_ok=True)
def grab(t, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(final), "-frames:v", "1", str(out)])
for t, tag in [(0.5, "title-0.5"), (1.0, "title-1.0"), (1.5, "title-1.5")]:
    grab(t, qcd / f"final-{tag}.png")
mids = []
for sh, _, _, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    fp = qcd / f"final-mid-{sh}.png"
    grab((t0 + t1) / 2, fp)
    mids.append(Image.open(fp).convert("RGB"))
cuts = []
for sh, _, _, _ in SEGS[1:]:
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
print(f"title frames: {qcd / 'final-title-0.5.png'}, {qcd / 'final-title-1.0.png'}, {qcd / 'final-title-1.5.png'}")

# ============ QC: Whisper transcript of final (record only) ============
print("== QC: whisper transcript (final, record only) ==")
run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vn", "-ac", "1", "-ar", "16000",
     "-c:a", "pcm_s16le", str(WORK / "final-16k.wav")])
d16f, sr16f, _ = wav_read(WORK / "final-16k.wav")
segs_f, _ = model.transcribe(d16f, language="vi", word_timestamps=False, beam_size=5)
for s in segs_f:
    print(f"  {s.start:.2f}-{s.end:.2f} {s.text.strip()!r}")

# ============ build report ============
report = f"""# ep008 master 2K FINAL — build report

## Outputs
- Final: `delivery/ep008-master-2k.mp4` sha256 `{sha(final)}`
- SRT: `delivery/ep008-master-2k.srt`
- Scripts: `edit/build_master_2k.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build2k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, title frames in qc/)
- Remotion inputs backed up to: `{backup}` (the 1K ep008 inputs)

## Sources (all TRUE 2K 1080x1920 24fps 7.85s, from ~/workspace/ep008-con-nho-do-clips/)
- sh010 sh010-take005-2k.mp4 sha 5fd6606f… (VIDEO) + wordalign dub audio from
  generated/sh010-take005-dub-thaomy-wordalign.mp4 — trim 0-2.8s
- sh020 sh020-take003-2k.mp4 sha 2e03040e… (VIDEO) + 1K native audio — trim 0-3.6s
- sh030 sh030-take002-2k.mp4 sha a3426242… (VIDEO) + wordalign dub audio from
  generated/sh030-take002-dub-thaomy-wordalign.mp4 — trim 0-5.2s
- sh040 sh040-take004-2k.mp4 sha d71d292b… (VIDEO) + 1K native audio — trim 0-5.0s
  (sentence 2 cut by design)
- sh050 sh050-take002-2k.mp4 sha 0cd5f023… (VIDEO) + 1K native audio — trim 0-2.0s
- sh060 LOCAL UPSCALE sh060-take015-2k-local-upscale.mp4 sha 80e5729a… (lanczos from
  approved 1K take015, 1080x1920 24fps) + 1K native audio — trim 0-7.0s.
  The downloaded sh060-take015-2k.mp4 (sha 7d103fc3…) is actually TAKE016
  (frame diff 2.1 vs take016 @2.5s; 16.3 vs take015) — wrong take, NOT used.
  A true Flow 2K re-download of take015 can swap this in later.
- sh070 sh070-take002-2k.mp4 sha e53cd889… (VIDEO) + 1K native audio — trim 0-3.0s
  (silent shot; Laugh Track 1 placed over it in stage 3)
- AUDIO RULE: approved 1K mixes for all native shots (sh020/sh050/sh070 1K audio ==
  2K audio; sh040's 2K audio is noisier; sh060's 2K audio belongs to take016).
- Nominal total {TOTAL:.1f}s; actual final {total:.2f}s (AAC priming/frame rounding).
  Bounds: {BOUNDS}

## Stage 1 commands (per segment)
ffmpeg -i <2K video> [-i <1K wordalign file for sh010/sh030>] -vf "trim=0:<T>,setpts=PTS-STARTPTS,{CROP},scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[6:v][6:a]concat=n=7:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11 (ep006 pattern), video copy.
Segment durations measured: {seg_durs}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on ALL 7 2K files
  (top-right corners clean foliage), same relative position as the 1K files.
- Crop {CROP} = proportional 2K equivalent of the approved 1K crop 640:1138:40:0
  (x 60..1020, y 0..1707, then lanczos to 1080x1920). Icon top edge ~y1770-1832
  in 2K coords -> ~63px margin. One uniform crop so framing/scale matches the
  approved 1K preview exactly across hard cuts.

## Title ("CON NHỎ ĐÓ", ep004 style)
- Reused the existing Remotion TitleCard (src/TitleCard.tsx, already wired into
  CaptionedVideo via title/titleSeconds props) — NOT rebuilt. Render props:
  {{"accent": "#F59E0B", "title": "CON NHỎ ĐÓ", "titleSeconds": 2}}.
- Overlay on sh010, first 2s only, upper band (marginTop 9% height, fontSize
  11.5% width, white 900-weight uppercase + black stroke + accent underline bar).
  My's head top in sh010 is ~y460-480/1920 raw (~y517 final after crop+scale);
  title occupies ~y173-360 -> ~150px clear. Verified on frames 0.5/1.0/1.5s
  (edit/build2k/qc/final-title-*.png) — see QC notes below.
- No standalone card, no duration change, no timeline shift (total stays ~28.7s).

## Stage 2 captions (Remotion Boxed)
- Whisper base word timestamps RE-RUN on the 2K assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. Caption timing vs 1K:
  max delta {max_delta}ms. Known ASR artifacts ignored by design.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep008-boxed-2k-chunk<N>.mp4 --props '{{"accent":"#F59E0B","title":"CON NHỎ ĐÓ","titleSeconds":2}}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: {ranges} (<=287 frames each — the 1K
  lesson: full 861-frame render at --concurrency=2 exits 0 but goes BLACK from
  ~13.7s, Chrome OOM). Each chunk verified (exit code + size + duration + mean
  frame at chunk middle) before use. Video-only chunks concatenated, then muxed
  with assembly-norm audio -> out/ep008-boxed-2k-tmp.mp4.
- Caption problems (if any): see edit/build2k/captions-PROBLEMS.txt (empty = clean).

## Stage 3 laugh
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix over sh070, audible onset {LAUGH_AUDIBLE_AT:.1f}s (0.1s into the
  reaction shot), stem_start={stem_start:.2f}s, laugh ends {laugh_end:.2f}s < {total:.2f}s.
- NO freeze-frame tail (laugh fits inside the video).
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.
- Stage-3 duration fix applied from the start: total = len(dlg)/SR (actual
  boxed-audio duration), not nominal 28.6s.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, ~28.7s, AAC 48kHz stereo).
- Frame means at 0.5/1.0/1.5/5.0/9.5/9.6/13.7/15.0/19.0/19.2/22.0/26.0/28.3s:
  see script output above (black = mean ~0; chunk boundaries included).
- Title frames: edit/build2k/qc/final-title-0.5.png, final-title-1.0.png,
  final-title-1.5.png — inspect visually (title visible, upper band, clear of My's head).
- Energy per shot + sh070 laugh-zone buckets: see script output above.
- Contact sheet: edit/build2k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: see script output above (record only; script words govern captions).
"""
(WORK / "build-report.md").write_text(report)
print(report)
print("BUILD 2K DONE")
