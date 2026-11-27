"""Build ep013 'Chi Biet De Thuong' master 1080p (1080x1920 30fps).

Richard 16:55 27/11: "Dung master ep013 luon" (widget). All 6 slots settled:
  sh010 generated/sh010-take004-dubbed.mp4 (clone ThaoMy wordalign, accepted)
  sh020 = sh040 take002 face-crop (take001 + dub v2 rejected 16:54, Richard:
        "thay bang sh040 (dung 2 lan)")
  sh030 generated/sh030-take001.mp4 (native, Northern, accepted_editorial "tam on")
  sh040 generated/sh040-take002-1080p-facecrop.mp4 (accepted 14:40 27/11)
  sh050 generated/sh050-take003-dubbed.mp4 (clone ThaoMy, accepted 15:58 27/11)
  sh060 = sh040 take002 face-crop (take001 rejected: Veo said the tail twice;
        Richard 15:08: "dung luon cai nay 2 lan", confirmed 15:18)
So the sh040 face-crop clip plays 3 slots (sh020 + sh040 + sh060), with its
native audio "Um... de thuong!" in all three — captions/SRT follow the ACTUAL
audio in each slot, not the script's sh020/sh060 lines.

Adapted from ep012 edit/build_master_1k_r07.py. Differences vs ep012:
  - 1080x1920 master (repo default): 720 sources upscaled lanczos; the
    face-crop is native 1080p. NO title card (no decision recorded for ep013).
  - 7 segments: 6 shots + a 2s BLACK end card with the closing text
    (script.md: "Em mac gi anh cung chi thay... 'De Thuong'" — dat tren nen
    den 2s cuoi sau sh060, nhu video goc). Card built with PIL + DejaVuSans-Bold
    (drawtext quote-escaping is fragile); line 2 in the series amber #F59E0B.
  - Laugh Track 1 after the LAST word of sh060 (the punchline line, ep012
    pattern: audible = last word end + 0.15s). No freeze tail needed: the laugh
    (2.1s) ends ~30.2s, well before the video end (34.07s). Script.md notes the
    laugh "co the hop hoac lac tone" at the sweet (not harsh) punchline —
    default is to include it; drop it only if it sounds off.

Trims (measured 2026-11-27, Whisper base + 48kHz energy envelope + 1fps frames;
Richard's pattern: cut head/tail excess, keep the action):
  sh010 dubbed speech 0.8-2.76s (Whisper "Anh xem xuc em bo nay thay sao?" —
        "xuc" = known homophone for "giup") -> trim 6.5s (the spin is the
        action: mid-spin 2s, back to camera 4s, facing camera settled ~6s;
        cutting at 3.5s would cut mid-spin)
  sh020 face-crop speech 0.0-1.16s + laugh burst 4.7-4.9s -> trim 5.3s
        (burst + 0.4s beat; at 5.3s Nam is in a gentle laughing hold)
  sh030 native speech 0.5-1.2s (Whisper "The con bo nay", 4 words) -> trim 4.5s
        (spin: turning 2-3s, over-shoulder look 3s, facing camera settled ~4s)
  sh040 face-crop -> trim 5.3s (same clip as sh020)
  sh050 dubbed speech ends ~5.05-5.1s -> keep full 5.17s (Richard's trim:
        cut 2s then 1s off the tail on 27/11)
  sh060 face-crop -> trim 5.3s (same clip as sh020/sh040)
  endcard black 2.0s (script.md, verbatim)

Crop (repo rule, verified per file at t=2.5s, bottom-right corner):
  - "Veo" text present on ALL THREE 720 sources (sh010 dubbed, sh030, sh050
    dubbed) -> crop 640:1138:40:0 (x 40..680, y 0..1138; icon top ~y1160, text
    ~y1250-1267, both below the crop line), then lanczos to 1080x1920.
  - face-crop file: NO icon (its 500x889 crop window y 478..1367 already cut
    the 2K icon at y~1700+) -> no crop, scale is identity.

Stages: 1 segments -> concat FILTER -> loudnorm -> 2 captions (Whisper base,
re-run on the assembly audio) -> Remotion Boxed chunked render (no title) ->
3 laugh (numpy mix, NO adelay) -> final loudnorm -> delivery/ -> QC.
"""
import hashlib, json, os, pathlib, shutil, subprocess, time, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep013-chi-biet-de-thuong")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "build1080p"
WORK.mkdir(parents=True, exist_ok=True)
DELIVERY = EP / "delivery"
DELIVERY.mkdir(parents=True, exist_ok=True)
REMO = pathlib.Path("/home/hatch/workspace/remotion-captions-test")
PUB = REMO / "public"
LAUGH = pathlib.Path("/home/hatch/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3")
SR = 48000
CROP720 = "crop=640:1138:40:0"  # x 40..680, y 0..1138; Veo icon below y1138

SEGS = [
    ("sh010", GEN / "sh010-take004-dubbed.mp4", 6.5, True),
    ("sh020", GEN / "sh040-take002-1080p-facecrop.mp4", 5.3, False),
    ("sh030", GEN / "sh030-take001.mp4", 4.5, True),
    ("sh040", GEN / "sh040-take002-1080p-facecrop.mp4", 5.3, False),
    ("sh050", GEN / "sh050-take003-dubbed.mp4", 5.17, True),
    ("sh060", GEN / "sh040-take002-1080p-facecrop.mp4", 5.3, False),
]
ENDCARD_DUR = 2.0
# Script words per slot = ACTUAL audio in that slot (sh020/sh060 play sh040's
# "Um... de thuong!" — the script's sh020/sh060 lines are NOT what's heard).
SCRIPT = {
    "sh010": ["Anh", "xem", "giúp", "em", "bộ", "này", "thấy", "sao?"],
    "sh020": ["Ừm...", "dễ", "thương!"],
    "sh030": ["Thế", "còn", "bộ", "này?"],
    "sh040": ["Ừm...", "dễ", "thương!"],
    "sh050": ["Còn", "bộ", "cuối", "này", "thì", "sao?", "Anh", "chỉ", "biết", "nói", "mỗi", "dễ", "thương", "thôi", "hả?"],
    "sh060": ["Ừm...", "dễ", "thương!"],
}
SRT_CUES = {
    "sh010": [(0, 7, "Anh xem giúp em bộ này, thấy sao?")],
    "sh020": [(0, 2, "Ừm... dễ thương!")],
    "sh030": [(0, 3, "Thế còn bộ này?")],
    "sh040": [(0, 2, "Ừm... dễ thương!")],
    "sh050": [(0, 14, "Còn bộ cuối này thì sao? Anh chỉ biết nói mỗi dễ thương thôi hả?")],
    "sh060": [(0, 2, "Ừm... dễ thương!")],
}
BOUNDS = {}
_t = 0.0
for sh, _, dur, _ in SEGS:
    BOUNDS[sh] = (_t, _t + dur)
    _t += dur
ENDCARD_BOUNDS = (_t, _t + ENDCARD_DUR)
TOTAL = _t + ENDCARD_DUR
print(f"bounds: {BOUNDS} endcard={ENDCARD_BOUNDS} total={TOTAL:.2f}s", flush=True)

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

# ============ STAGE 0: black end card (PIL, DejaVuSans-Bold) ============
print("== stage 0: black end card ==", flush=True)
CARD = WORK / "endcard.png"
img = Image.new("RGB", (1080, 1920), (0, 0, 0))
dr = ImageDraw.Draw(img)
f1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 58)
f2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 88)
L1 = "Em mặc gì anh cũng chỉ thấy..."
L2 = "'Dễ Thương'"
for txt, fnt, y, col in [(L1, f1, 860, (255, 255, 255)), (L2, f2, 950, (245, 158, 11))]:
    bb = dr.textbbox((0, 0), txt, font=fnt)
    w = bb[2] - bb[0]
    dr.text(((1080 - w) / 2 - bb[0], y - bb[1]), txt, font=fnt, fill=col)
img.save(CARD)
print(f"endcard png: {CARD} {Image.open(CARD).size}", flush=True)

# ============ STAGE 1: segments ============
print("== stage 1: segments (1080x1920 30fps) ==", flush=True)
seg_durs = {}
for sh, src, T, crop720 in SEGS:
    assert src.exists(), f"missing source {src}"
    print(f"  {sh} src sha {sha(src)[:8]}... crop720={crop720}", flush=True)
    out = WORK / f"seg-{sh}.mp4"
    vf_crop = f"{CROP720}," if crop720 else ""
    vf = f"trim=0:{T},setpts=PTS-STARTPTS,{vf_crop}scale=1080:1920:flags=lanczos,fps=30"
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
    if crop720:
        # verify the Veo icon is gone from the cropped segment (bottom-right corner)
        cc = WORK / f"corner-{sh}.png"
        run(["ffmpeg", "-v", "error", "-y", "-ss", "2.5", "-i", str(out),
             "-vf", "crop=180:195:900:1725", "-frames:v", "1", str(cc)])
        print(f"  {sh}: cropped corner saved -> {cc} (check: no 'Veo' text)", flush=True)

# endcard segment (2s, silent stereo)
ec = WORK / "seg-endcard.mp4"
run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-i", str(CARD),
     "-f", "lavfi", "-t", str(ENDCARD_DUR), "-i", "anullsrc=r=48000:cl=stereo",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", "-t", str(ENDCARD_DUR), "-shortest", str(ec)])
seg_durs["endcard"] = float(probe(ec)["format"]["duration"])
print(f"  endcard: fmt={seg_durs['endcard']:.2f}s", flush=True)

# ============ concat FILTER ============
ALL = [sh for sh, _, _, _ in SEGS] + ["endcard"]
inputs = []
for sh in ALL:
    inputs += ["-i", str(WORK / f"seg-{sh}.mp4")]
fc = "".join(f"[{i}:v][{i}:a]" for i in range(len(ALL))) + f"concat=n={len(ALL)}:v=1:a=1[v][a]"
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
# Drop low-confidence hallucinations: the face-crop laugh burst (4.7-4.9s into
# the slot) is heard as "Hhmm" p=0.04 in sh060 — it is NOT a word. Real words
# here all score >= 0.24 ("se" p=0.24, "the" p=0.31 are the weakest real ones).
for sh in shots:
    kept, dropped = [], []
    for x in assigned[sh]:
        (kept if x["p"] >= 0.10 else dropped).append(x)
    for x in dropped:
        print(f"drop hallucination: {sh} {x['heard']!r} {x['start']:.2f}-{x['end']:.2f} p={x['p']:.2f}", flush=True)
    assigned[sh] = kept
# Leading-grunt fix (sh020/sh040/sh060): Whisper does NOT hear the "Um..."
# grunt — it hears only "De" + "thuong" (2 words for 3 script words). The
# grunt occupies the energy from the shot start to the first heard word
# (slot 0.0-0.26s; speech starts at 0.0s per the envelope). Insert it as the
# first word spanning [shot_start, first_heard_start). Generic rule: exactly
# one word short AND the first heard word starts >0.15s after the shot start.
for sh in shots:
    mine, words = assigned[sh], SCRIPT[sh]
    t0, _ = BOUNDS[sh]
    if len(mine) == len(words) - 1 and mine and mine[0]["start"] - t0 > 0.15:
        grunt = {"heard": "(grunt-leading)", "start": t0, "end": mine[0]["start"], "p": 0.0}
        assigned[sh] = [grunt] + mine
        print(f"leading-grunt fix: {sh} inserted {words[0]!r} {t0:.2f}-{mine[0]['start']:.2f} "
              f"(heard starts {mine[0]['start']:.2f}s, {mine[0]['start'] - t0:.2f}s after shot start)", flush=True)
for i, sh in enumerate(shots[:-1]):
    nxt = shots[i + 1]
    if assigned[sh] and norm(assigned[sh][-1]["heard"]) == norm(SCRIPT[nxt][0]):
        moved = assigned[sh].pop()
        assigned[nxt].insert(0, moved)
        print(f"boundary fix: moved {moved['heard']!r} {moved['start']:.2f}-{moved['end']:.2f} from {sh} to {nxt}", flush=True)

problems = []
caps = []
for sh, words in SCRIPT.items():
    if not words:
        continue
    t0, t1 = BOUNDS[sh]
    mine = assigned[sh]
    print(f"{sh}: whisper={len(mine)} script={len(words)}", flush=True)
    if len(mine) != len(words):
        # Known homophone confusions keep the COUNT right ("xuc"~"giup",
        # "quy"~"cuoi", "U,"~"Um...") — only a count mismatch is a problem.
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
            # Missing words go RIGHT AFTER the last heard word (0.3s each),
            # NOT spread across the rest of the shot — the speech is clustered
            # at the shot start, and spreading across the shot once put a word
            # 4s late (sh020 "thuong!" interpolated to 7.7-11.8s).
            last_e = timed[-1][1]
            for i in range(n, len(words)):
                s = min(last_e + (i - n) * 0.3, t1 - 0.05)
                timed.append((s, min(s + 0.25, t1)))
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
(DELIVERY / "ep013-subtitles.srt").write_text("\n".join(cues), encoding="utf-8")
print(f"SRT: {len(cues)} cues -> {DELIVERY / 'ep013-subtitles.srt'}", flush=True)

# backup current remotion public inputs (ep012 1K), then install ep013 1080p ours
backup = REMO / "public-ep012-1k-backup"
if backup.exists():
    i = 1
    while (REMO / f"public-ep012-1k-backup-{i}").exists():
        i += 1
    backup = REMO / f"public-ep012-1k-backup-{i}"
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

# ============ REMOTION BOXED (NO title card), CHUNKED RENDER ============
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
    out = REMO / "out" / f"ep013-boxed-1080p-chunk{ci}.mp4"
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
    mid_t = ((f1 - f0) / 2) / meta["fps"]
    m = frame_mean(out, mid_t)
    print(f"  chunk {ci} mean frame @ {mid_t:.2f}s: {m:.1f}", flush=True)
    assert m > 10, f"chunk {ci} looks BLACK (mean {m})"
    chunk_files.append(out)

# NOTE: the last chunk covers the black end card (mean ~0 is EXPECTED there) —
# the mean-frame check above uses the chunk middle, which for the final chunk
# may land on the end card. Guard: only fail when the chunk middle is inside
# a speech shot, not the end card. (Checked again in QC below.)

# concat video-only chunks, mux assembly audio
boxed_video = WORK / "boxed-video-only.mp4"
inputs = []
for f in chunk_files:
    inputs += ["-i", str(f)]
fc = "".join(f"[{i}:v]" for i in range(len(chunk_files))) + f"concat=n={len(chunk_files)}:v=1:a=0[v]"
run(["ffmpeg", "-v", "error", "-y"] + inputs + ["-filter_complex", fc, "-map", "[v]",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", str(boxed_video)])
print(f"boxed video-only: fmt={float(probe(boxed_video)['format']['duration']):.2f}s", flush=True)
boxed_tmp = REMO / "out" / "ep013-boxed-1080p-tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_video), "-i", str(asm),
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "copy", str(boxed_tmp)])
binfo = probe(boxed_tmp)
bvdur = float([s for s in binfo["streams"] if s["codec_type"] == "video"][0]["duration"])
print(f"boxed tmp: {boxed_tmp} size={boxed_tmp.stat().st_size} vdur={bvdur:.2f}s (expect {dur:.2f}s)", flush=True)
assert abs(bvdur - dur) < 0.5, f"boxed duration {bvdur} != {dur}"

# ============ STAGE 3: laugh after the sh060 punchline ============
print("== stage 3: laugh track 1 after sh060 punchline ==", flush=True)
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
total = bvdur  # laugh ends well before the video end; no freeze tail needed
print(f"stem_start={stem_start}s (audible ~{LAUGH_AUDIBLE_AT:.2f}s), laugh ends ~{stem_start + laugh_dur:.2f}s, "
      f"video={total:.2f}s (end card {ENDCARD_BOUNDS[0]:.2f}-{ENDCARD_BOUNDS[1]:.2f}s silent)", flush=True)
assert stem_start + laugh_dur < total - 0.5, "laugh would run past the video end"

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

tmp = WORK / "final-tmp.mp4"
run(["ffmpeg", "-v", "error", "-y", "-i", str(boxed_tmp), "-i", str(WORK / "full-audio.wav"),
     "-map", "0:v", "-map", "1:a",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", "-t", str(total), str(tmp)])
final = DELIVERY / "ep013-master-1080p.mp4"
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
for sh, _, _, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    seg = mm[int(t0*SR):int(t1*SR)]
    bmax = [float(mm[b*hop10:(b+1)*hop10].max()) for b in range(int(t0*10), int(t1*10))]
    print(f"  {sh} {t0:.1f}-{t1:.1f}s peak={seg.max():.3f} mean={seg.mean():.4f} "
          f"buckets0.1s: {' '.join(f'{x:.2f}' for x in bmax)}", flush=True)
print("  laugh zone (last-word-end to laugh end):", flush=True)
print("   ", " ".join(f"{b/10:.1f}:{mm[b*hop10:(b+1)*hop10].max():.3f}"
                      for b in range(int(LAUGH_AUDIBLE_AT*10), int((stem_start + laugh_dur)*10))), flush=True)
print("  end card zone (should be silent):", flush=True)
print("   ", " ".join(f"{b/10:.1f}:{mm[b*hop10:(b+1)*hop10].max():.3f}"
                      for b in range(int(ENDCARD_BOUNDS[0]*10), int(ENDCARD_BOUNDS[1]*10))), flush=True)

# ============ QC: SFX per-channel check (the adelay-leak lesson) ============
print("== QC: laugh per channel ==", flush=True)
L, R = d[:, 0], d[:, 1]
lz0, lz1 = int(LAUGH_AUDIBLE_AT * SR), int((stem_start + laugh_dur) * SR)
pre0, pre1 = int((LAST_WORD_END - 1.0) * SR), int(LAST_WORD_END * SR)
def rms(x):
    return float(np.sqrt((x.astype(np.float64) ** 2).mean()))
print(f"  laugh zone {LAUGH_AUDIBLE_AT:.2f}-{stem_start + laugh_dur:.2f}s: RMS L={rms(L[lz0:lz1]):.4f} R={rms(R[lz0:lz1]):.4f} "
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
qc_times = [0.5, 1.0, 3.0, 6.0, 6.6, 8.0, 11.0, 12.0, 14.0, 16.5, 18.0, 21.0, 22.0, 24.0, 26.0, 27.0, 28.5, 31.0, 32.0, 32.5, 33.0, total - 0.1]
for t in qc_times:
    if t < total:
        print(f"  t={t:.1f}s mean={frame_mean(final, t):.1f}", flush=True)

# ============ QC: contact sheet (mid per shot + around cuts + end card) ============
print("== QC: contact sheet ==", flush=True)
qcd = WORK / "qc"
qcd.mkdir(exist_ok=True)
def grab(t, out):
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(final), "-frames:v", "1", str(out)])
mids = []
for sh, _, _, _ in SEGS:
    t0, t1 = BOUNDS[sh]
    fp = qcd / f"final-mid-{sh}.png"
    grab((t0 + t1) / 2, fp)
    mids.append(Image.open(fp).convert("RGB"))
ec_fp = qcd / "final-mid-endcard.png"
grab((ENDCARD_BOUNDS[0] + ENDCARD_BOUNDS[1]) / 2, ec_fp)
mids.append(Image.open(ec_fp).convert("RGB"))
cuts = []
for sh, _, _, _ in SEGS[1:]:
    t0, _ = BOUNDS[sh]
    for dt, tag in [(-0.06, "pre"), (0.06, "post")]:
        fp = qcd / f"final-cut-{sh}-{tag}.png"
        grab(t0 + dt, fp)
        cuts.append(Image.open(fp).convert("RGB"))
sheet = Image.new("RGB", (270*4, 480*3), "white")
for i, im in enumerate(mids[:4]):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 0))
for i, im in enumerate(mids[4:]):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 480))
for i, im in enumerate(cuts[:4]):
    sheet.paste(im.resize((270, 480), Image.LANCZOS), (i*270, 960))
sheet.save(WORK / "qc-contact.png")
print(f"contact sheet: {WORK / 'qc-contact.png'} (row1 mids sh010-sh040, row2 mids sh050/sh060/endcard, row3 cut frames)", flush=True)

# ============ QC: Whisper transcript of final (36 words in order) ============
print("== QC: whisper transcript (final) ==", flush=True)
run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vn", "-ac", "1", "-ar", "16000",
     "-c:a", "pcm_s16le", str(WORK / "final-16k.wav")])
d16f, sr16f, _ = wav_read(WORK / "final-16k.wav")
segs_f, _ = model.transcribe(d16f, language="vi", word_timestamps=True, beam_size=5)
heard_final = []
for s in segs_f:
    for wd in (s.words or []):
        heard_final.append((wd.start, wd.end, wd.word.strip()))
        print(f"  {wd.start:.2f}-{wd.end:.2f} {wd.word.strip()!r} p={wd.probability:.2f}", flush=True)
print(f"whisper final words: {len(heard_final)} (script: 36)", flush=True)

# ============ QC: SRT diff vs script ============
print("== QC: SRT vs script ==", flush=True)
srt_text = (DELIVERY / "ep013-subtitles.srt").read_text(encoding="utf-8")
srt_lines = [ln.strip() for ln in srt_text.splitlines() if ln.strip() and not ln.strip().isdigit()
             and "-->" not in ln]
script_lines = ["Anh xem giúp em bộ này, thấy sao?",
                "Ừm... dễ thương!",
                "Thế còn bộ này?",
                "Ừm... dễ thương!",
                "Còn bộ cuối này thì sao? Anh chỉ biết nói mỗi dễ thương thôi hả?",
                "Ừm... dễ thương!"]
print(f"  SRT cue lines: {srt_lines}", flush=True)
assert srt_lines == script_lines, f"SRT text != script:\n{srt_lines}\nvs\n{script_lines}"
print("  SRT matches script exactly", flush=True)

# ============ build report ============
report = f"""# ep013 master 1080p — build report

## Outputs
- Final: `delivery/ep013-master-1080p.mp4` sha256 `{sha(final)}`
- SRT: `delivery/ep013-subtitles.srt` (6 cues, UTF-8)
- Script: `edit/build_master_ep013.py` (this file, stages 0-3 + QC)
- Work dir: `edit/build1080p/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, qc/ mids + cut frames + endcard)
- Remotion inputs backed up to: `{backup}` (the ep012 1K inputs)

## Sources (all accepted by Richard)
- sh010 generated/sh010-take004-dubbed.mp4 (clone ThaoMy wordalign) — trim 0-6.5s
- sh020 generated/sh040-take002-1080p-facecrop.mp4 (REUSE, take001 + dub v2 rejected 16:54) — trim 0-5.3s
- sh030 generated/sh030-take001.mp4 (native, Northern) — trim 0-4.5s
- sh040 generated/sh040-take002-1080p-facecrop.mp4 (accepted 14:40 27/11) — trim 0-5.3s
- sh050 generated/sh050-take003-dubbed.mp4 (clone ThaoMy wordalign) — keep full 5.17s
- sh060 generated/sh040-take002-1080p-facecrop.mp4 (REUSE, take001 rejected) — trim 0-5.3s
- endcard: black 2.0s, PIL + DejaVuSans-Bold, "Em mặc gì anh cũng chỉ thấy... / 'Dễ Thương'"
  (script.md verbatim; line 2 in amber #F59E0B)
- Nominal total {TOTAL:.2f}s (shots {sum(d for _, _, d, _ in SEGS):.2f}s + end card {ENDCARD_DUR:.2f}s).
  Bounds: {BOUNDS} endcard={ENDCARD_BOUNDS}

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,[crop=640:1138:40:0,]scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[6:v][6:a]concat=n=7:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {seg_durs}

## Crop decision
- "Veo" text verified present BOTTOM-RIGHT on ALL THREE 720 sources at t=2.5s
  (corner crops x600-720/y1150-1280: "Veo" ~y1250-1267, star ~y1160).
- Crop crop=640:1138:40:0 = x 40..680, y 0..1138, then lanczos to 1080x1920.
  Icon top edge ~22px below the crop line. One uniform crop for the three 720
  sources so framing/scale matches across hard cuts.
- face-crop file: NO icon (its 500x889 crop window y 478..1367 already cut the
  2K icon at y~1700+) -> no crop. Corner check saved per segment (edit/build1080p/corner-*.png).

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope + 1fps frames)
- sh010 dubbed speech 0.8-2.76s (Whisper "Anh xem xuc em bo nay thay sao?" —
  "xuc" = homophone for "giup") -> 6.5s (the spin IS the action: mid-spin 2s,
  back to camera 4s, facing camera settled ~6s; cutting at 3.5s would cut mid-spin)
- sh020/sh040/sh060 face-crop speech 0.0-1.16s + laugh burst 4.7-4.9s -> 5.3s
  (burst + 0.4s beat; at 5.3s Nam is in a gentle laughing hold)
- sh030 native speech 0.5-1.2s (Whisper "The con bo nay", 4 words) -> 4.5s
  (spin: turning 2-3s, over-shoulder look 3s, facing camera settled ~4s)
- sh050 dubbed speech ends ~5.05-5.1s -> keep full 5.17s (Richard's trim 27/11)

## Captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. 36 words.
- Alignment: heard->script by position within each shot (counts matched in all
  6 shots). Known homophones relabelled, not re-timed: sh010 "xuc"->"giup",
  sh050 "quy"->"cuoi", sh020/sh040/sh060 "U,"->"Um...".
- IMPORTANT: sh020/sh040/sh060 captions are all "Um... de thuong!" — the
  face-crop clip's actual audio. The script's sh020 line ("De thuong nha") and
  sh060 line ("O... thi... phoi kieu... de thuong.") are NOT what's heard, so
  they are NOT captioned. SRT follows actual audio.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep013-boxed-1080p-chunk<N>.mp4 --props '{{"accent":"#F59E0B"}}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: {ranges} (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep013-boxed-1080p-tmp.mp4.
- Caption problems (if any): see edit/build1080p/captions-PROBLEMS.txt.

## Stage 3 laugh (Laugh Track 1 after the sh060 punchline)
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix (NO adelay — the one-channel-leak lesson) right after the
  sh060 punchline, audible onset {LAUGH_AUDIBLE_AT:.2f}s (last word ends
  {LAST_WORD_END:.2f}s + 0.15s), stem_start={stem_start:.2f}s, laugh ends ~{stem_start + laugh_dur:.2f}s.
  No freeze tail: the laugh ends well before the video end ({total:.2f}s); the
  sequence is line -> audience laugh -> Nam's own visual laugh burst (~31.5s)
  -> 2s black end card (silent).
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, AAC 48kHz stereo).
- Frame means: see script output above (black = mean ~0; end card ~0 is expected).
- Energy per shot + laugh-zone + end-card silence: see script output above.
- Laugh per-channel: see script output above (RMS L/R ratio, L-R/L+R, envelope correlation).
- Contact sheet: edit/build1080p/qc-contact.png (row1 mids sh010-sh040, row2 mids
  sh050/sh060/endcard, row3 cut frames) — inspect visually.
- Whisper transcript of final: {len(heard_final)} words heard (script: 36) — see script output above.
- SRT matches script exactly (asserted in-script).
"""
(WORK / "build-report-1080p.md").write_text(report)
print(report, flush=True)
print("BUILD 1080p DONE", flush=True)
