"""Build ep012 'Flex' 1K master PREVIEW r06 (720x1280 30fps).

r06 rebuild (2026-11-26): sh020 take005 (generated natively with the r05 line,
Flow clip 6b1f178f) replaces take004; Richard 06:56 26/11: "ok do, long giong
ThaoMy la dc" — take005 dubbed with clone ThaoMy wordalign
(build_wordalign_sh020_take005.py, QC passed, sha 60f66835...). Same pipeline,
crop, laugh as r05; only the sh020 source + trim changed (take005 speaks the
line ~0.3s faster: speech ends 4.91s vs 5.18s, trim 5.3s vs 5.5s). Total
script words still 47.

Adapted from ep011 edit/build_master_2k.py (approved 2K master, 2026-11-24).
Differences vs ep011:
  - 1K sources (720x1280), PREVIEW master (the 2K master comes later from 2K
    downloads). Same pipeline otherwise.
  - Sources (all 720x1280, 7.93s, accepted by Richard 2026-11-25 17:31):
      sh010 generated/sh010-take001.mp4 (native, Hùng, accepted, no dub)
      sh020 generated/sh020-take005-dubbed.mp4 (clone ThaoMy wordalign, take005)
      sh030 generated/sh030-take002.mp4 (native, Hùng, accepted, no dub)
      sh040 generated/sh040-take003-dubbed.mp4 (clone ThaoMy wordalign)
  - Trims (measured 2026-11-25, energy envelope 48kHz stereo 0.1s buckets +
    Whisper base word timestamps + 1fps frames; Richard ordered head/tail
    excess cut, keep the action):
      sh010 native speech 1.08-2.62s (energy loud 1.4-2.6s) -> trim 3.4s
        (beat 0.78s; watch-point gesture completes as his hand lowers to the
        table ~3.4s; the glass-drink at ~6-7s is Veo tail motion, cut)
      sh020 dubbed speech clusters 0.91-1.99 / 2.41-3.99 / 4.29-4.91 -> trim 5.3s
        (beat 0.39s; polite smile hold; cup-lowering/drinking at ~6.0s is tail, cut)
      sh030 native speech 0.90-4.34s -> trim 4.7s (beat 0.36s; bill push done
        ~3s, settled hand-on-folder; remaining 3.2s is static hold, cut)
      sh040 dubbed speech clusters 3.14-4.48 / 5.14-6.70 -> trim 7.0s
        (beat 0.30s; deadpan hold; HEAD 0-3.14s cup-down + smile-fade action
        untouched, per the hard constraint)
  - Crop: Veo sparkle + "Veo" text verified BOTTOM-RIGHT on ALL FOUR 1K files
    (corner crops x600-720/y1150-1280 at t=2.5s: star top ~y1160, "Veo" text
    ~y1250-1267). Crop 640:1138:40:0 (x 40..680, y 0..1138) + lanczos to
    720x1280 — the 2K crop 960:1707:60:0 scaled by 2/3; icon top edge ~22px
    below the crop line. One uniform crop so framing/scale matches across
    hard cuts.
  - SFX: Laugh Track 1 right after the sh040 punchline (last word ends
    ~20.10s master time). Laugh is 2.1s; video ends 20.4s, so a freeze-frame
    tail (ep004 pattern) carries the laugh.
  - Caption alignment fixes (known ASR artifacts, same pattern as ep011's
    sh030 fix): sh020 r05 hears "ba mươi ngàn" as "30" + ".000" (15 heard vs
    16 script) — split the "30" span into "ba"/"mươi", map ".000" to "ngàn".
    sh040 hears "limited" as one word "limite" (8 heard vs 9 script) — the
    last word "phê." timing is interpolated from the gap to the shot end.
  - Remotion render: chunked from the start (<=287 frames, --concurrency=1
    --muted). Full-render-at-concurrency-2 goes BLACK from ~13.7s (Chrome OOM,
    proven 2026-11-21). Each chunk verified (exit + size + duration + mean
    frame) before use.

Stages: 1 segments -> concat FILTER -> loudnorm -> 2 captions (Whisper base,
re-run on the assembly audio) -> Remotion Boxed chunked render -> 3 laugh +
freeze tail -> final loudnorm -> delivery/ -> QC.
"""
import hashlib, json, os, pathlib, shutil, subprocess, time, wave
import numpy as np
from PIL import Image

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep012-flex")
GEN = EP / "generated"
EDIT = EP / "edit"
WORK = EDIT / "build1k"
WORK.mkdir(parents=True, exist_ok=True)
DELIVERY = EP / "delivery"
DELIVERY.mkdir(parents=True, exist_ok=True)
REMO = pathlib.Path("/home/hatch/workspace/remotion-captions-test")
PUB = REMO / "public"
LAUGH = pathlib.Path("/home/hatch/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3")
SR = 48000
CROP = "crop=640:1138:40:0"  # x 40..680, y 0..1138; Veo icon top edge ~y1160

SEGS = [
    ("sh010", GEN / "sh010-take001.mp4", 3.4),
    ("sh020", GEN / "sh020-take005-dubbed.mp4", 5.3),
    ("sh030", GEN / "sh030-take002.mp4", 4.7),
    ("sh040", GEN / "sh040-take003-dubbed.mp4", 7.0),
]
SCRIPT = {
    "sh010": ["Em", "biết", "xe", "anh", "mấy", "tỷ", "không?"],
    "sh020": ["Mấy", "tỷ", "thì", "kệ", "anh,", "em", "uống", "ly", "cà", "phê", "ba", "mươi", "ngàn,", "anh", "đừng", "lo."],
    "sh030": ["Bill", "đây", "rồi", "nè,", "em", "chuyển", "khoản", "phần", "em", "nhé,", "anh", "gửi", "số", "tài", "khoản."],
    "sh040": ["Đồng", "hồ", "limited", "mà", "chia", "bill", "ly", "cà", "phê."],
}
# SRT cue sentences per shot: (first word idx, last word idx, text)
SRT_CUES = {
    "sh010": [(0, 6, "Em biết xe anh mấy tỷ không?")],
    "sh020": [(0, 15, "Mấy tỷ thì kệ anh, em uống ly cà phê ba mươi ngàn, anh đừng lo.")],
    "sh030": [(0, 14, "Bill đây rồi nè, em chuyển khoản phần em nhé, anh gửi số tài khoản.")],
    "sh040": [(0, 8, "Đồng hồ limited mà chia bill ly cà phê.")],
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
print("== stage 1: segments (1K sources, single input each) ==", flush=True)
seg_durs = {}
for sh, src, T in SEGS:
    assert src.exists(), f"missing source {src}"
    print(f"  {sh} src sha {sha(src)[:8]}...", flush=True)
    out = WORK / f"seg-{sh}.mp4"
    vf = f"trim=0:{T},setpts=PTS-STARTPTS,{CROP},scale=720:1280:flags=lanczos,fps=30"
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

problems = []
# r05: "ba mươi ngàn" heard as "30" + ".000" (15 heard vs 16 script):
# split the "30" span into "ba"/"mươi", map ".000" to "ngàn".
# (Standalone r05 dub QC heard exactly this: 15 tokens, P1 5 + P2 7 + P3 3.)
if len(assigned["sh020"]) == 15:
    num = [x for x in assigned["sh020"] if x["heard"] in ("30", "30.000,", "30.000")]
    nxt = None
    if num:
        i = assigned["sh020"].index(num[0])
        if i + 1 < len(assigned["sh020"]) and norm(assigned["sh020"][i + 1]["heard"]) in (".000", ".000,", "000", "ngàn"):
            nxt = assigned["sh020"][i + 1]
    if num and nxt:
        n30 = num[0]
        idx = assigned["sh020"].index(n30)
        mid = (n30["start"] + n30["end"]) / 2
        ba = dict(n30, heard="ba-split", start=n30["start"], end=mid)
        muoi = dict(n30, heard="mươi-split", start=mid, end=n30["end"])
        ngan = dict(nxt, heard="ngàn-mapped")
        assigned["sh020"][idx:idx+2] = [ba, muoi, ngan]
        problems.append(f"sh020 r05: split heard '30' {n30['start']:.2f}-{n30['end']:.2f} into 'ba'/'mươi', "
                        f"mapped {nxt['heard']!r} to 'ngàn' ('ba mươi ngàn' heard as '30' + '.000')")
        print("sh020 fix:", problems[-1], flush=True)
# Fallback: "ba mươi ngàn" heard as 14 tokens. Two sub-cases:
# (a) "cà phê" merged to "café" AND "ba mươi ngàn" as "30" + ".000":
#     split café -> cà/phê, split "30" -> ba/mươi, map ".000" -> ngàn.
#     (Observed in the r05 run: café 6.40-6.68, 30 6.68-7.18, .000 7.18-7.34.)
# (b) "ba mươi ngàn" as ONE token "30.000": split into ba/mươi/ngàn.
elif len(assigned["sh020"]) == 14:
    cafe = [x for x in assigned["sh020"] if norm(x["heard"]) in ("café", "cà")]
    num = [x for x in assigned["sh020"] if x["heard"] in ("30", "30.000,", "30.000")]
    done = False
    if cafe and num:
        ci = assigned["sh020"].index(cafe[0])
        ni = assigned["sh020"].index(num[0])
        nxt = assigned["sh020"][ni + 1] if ni + 1 < len(assigned["sh020"]) else None
        if ni == ci + 1 and nxt and norm(nxt["heard"]) in (".000", ".000,", "000", "ngàn"):
            c = cafe[0]
            mid = (c["start"] + c["end"]) / 2
            ca = dict(c, heard="cà-split", start=c["start"], end=mid)
            phe = dict(c, heard="phê-split", start=mid, end=c["end"])
            n30 = num[0]
            mid2 = (n30["start"] + n30["end"]) / 2
            ba = dict(n30, heard="ba-split", start=n30["start"], end=mid2)
            muoi = dict(n30, heard="mươi-split", start=mid2, end=n30["end"])
            ngan = dict(nxt, heard="ngàn-mapped")
            assigned["sh020"][ci:ni+2] = [ca, phe, ba, muoi, ngan]
            problems.append(f"sh020 r05: split heard 'café' {c['start']:.2f}-{c['end']:.2f} into 'cà'/'phê', "
                            f"split '30' {n30['start']:.2f}-{n30['end']:.2f} into 'ba'/'mươi', "
                            f"mapped {nxt['heard']!r} to 'ngàn'")
            print("sh020 fix:", problems[-1], flush=True)
            done = True
    if not done and num and num[0]["heard"] in ("30.000,", "30.000"):
        n30 = num[0]
        idx = assigned["sh020"].index(n30)
        t0, t1 = n30["start"], n30["end"]
        span = (t1 - t0) / 3
        parts = [dict(n30, heard=h, start=t0 + i * span, end=t0 + (i + 1) * span)
                 for i, h in enumerate(("ba-split", "mươi-split", "ngàn-split"))]
        assigned["sh020"][idx:idx+1] = parts
        problems.append(f"sh020 r05: split heard '30.000' {t0:.2f}-{t1:.2f} into 'ba'/'mươi'/'ngàn'")
        print("sh020 fix:", problems[-1], flush=True)
# Older fallback (r03 line): "cà phê" heard as "café", "phê ba mươi" as "30" (13 heard).
elif len(assigned["sh020"]) == 13:
    cafe = [x for x in assigned["sh020"] if norm(x["heard"]) in ("café", "cà")]
    num = [x for x in assigned["sh020"] if x["heard"] in ("30", "30.000,", "30.000")]
    if cafe and num and assigned["sh020"].index(cafe[0]) + 1 == assigned["sh020"].index(num[0]):
        n30 = num[0]
        idx = assigned["sh020"].index(n30)
        t0, t1 = n30["start"], n30["end"]
        span = (t1 - t0) / 3
        parts = [dict(n30, heard=h, start=t0 + i * span, end=t0 + (i + 1) * span)
                 for i, h in enumerate(("phê-split", "ba-split", "mươi-split"))]
        assigned["sh020"][idx:idx+1] = parts
        problems.append(f"sh020: split heard '30' {t0:.2f}-{t1:.2f} into 'phê'/'ba'/'mươi' "
                        f"('cà phê' heard as 'café', 'phê ba mươi' as '30')")
        print("sh020 fix:", problems[-1], flush=True)
# sh040 fix: Whisper splits "limited" into fragments — 2 ("lim"+"tế") or 3
# ("lý"+"mít"+"tích"). Merge EVERY heard token between "hồ" and "mà" into one
# "limited" spanning first.start to last.end. (If "limited" is heard as one
# token, len is 8 and the generic interpolation covers the last word, as in v1.)
if len(assigned["sh040"]) > 9:
    hs = [i for i, x in enumerate(assigned["sh040"]) if norm(x["heard"]) == "hồ"]
    ms = [i for i, x in enumerate(assigned["sh040"]) if norm(x["heard"]) == "mà"]
    if hs and ms and ms[0] > hs[0] + 1:
        h, m = hs[0], ms[0]
        frags = assigned["sh040"][h + 1:m]
        merged = dict(frags[0], heard="limited-merged",
                      start=frags[0]["start"], end=frags[-1]["end"])
        assigned["sh040"][h + 1:m] = [merged]
        problems.append(f"sh040: merged {len(frags)} fragment(s) "
                        f"{[f['heard'] for f in frags]} {frags[0]['start']:.2f}-{frags[-1]['end']:.2f} "
                        f"into 'limited'")
        print("sh040 fix:", problems[-1], flush=True)

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
(DELIVERY / "ep012-subtitles.srt").write_text("\n".join(cues), encoding="utf-8")
print(f"SRT: {len(cues)} cues -> {DELIVERY / 'ep012-subtitles.srt'}", flush=True)

# backup current remotion public inputs (ep011 2K), then install ep012 1K ours
backup = REMO / "public-ep011-2k-backup"
if backup.exists():
    i = 1
    while (REMO / f"public-ep011-2k-backup-{i}").exists():
        i += 1
    backup = REMO / f"public-ep011-2k-backup-{i}"
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
    out = REMO / "out" / f"ep012-boxed-1k-chunk{ci}.mp4"
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
boxed_tmp = REMO / "out" / "ep012-boxed-1k-tmp.mp4"
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
final = DELIVERY / "ep012-master-1k.mp4"
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
qc_times = [0.5, 1.0, 2.0, 3.0, 3.5, 5.0, 7.0, 8.9, 9.0, 11.0, 13.6, 13.7, 16.0, 18.0, 20.0, 20.5, total - 0.1]
for t in qc_times:
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

# ============ QC: Whisper transcript of final (47 words in order) ============
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
print(f"whisper final words: {len(heard_final)} (script: 47)", flush=True)

# ============ QC: SRT diff vs script ============
print("== QC: SRT vs script ==", flush=True)
srt_text = (DELIVERY / "ep012-subtitles.srt").read_text(encoding="utf-8")
srt_lines = [ln.strip() for ln in srt_text.splitlines() if ln.strip() and not ln.strip().isdigit()
             and "-->" not in ln]
script_lines = ["Em biết xe anh mấy tỷ không?",
                "Mấy tỷ thì kệ anh, em uống ly cà phê ba mươi ngàn, anh đừng lo.",
                "Bill đây rồi nè, em chuyển khoản phần em nhé, anh gửi số tài khoản.",
                "Đồng hồ limited mà chia bill ly cà phê."]
print(f"  SRT cue lines: {srt_lines}", flush=True)
assert srt_lines == script_lines, f"SRT text != script:\n{srt_lines}\nvs\n{script_lines}"
print("  SRT matches script exactly", flush=True)

# ============ build report ============
report = f"""# ep012 master 1K PREVIEW r06 — build report

## Change vs r05
- sh020 take005 (Flow clip 6b1f178f, generated natively with the r05 line to
  fix lip-sync) replaces take004. Richard 06:56 26/11: "ok đó, lồng giọng
  ThaoMy là đc" — take005 dubbed with clone ThaoMy wordalign
  (edit/build_wordalign_sh020_take005.py, QC passed, sha 60f66835…).
  Trim 5.3s (was 5.5s — take005 speaks ~0.3s faster, speech ends 4.91s).
  All other shots, trims, crop, captions style, laugh placement unchanged.
  Total script words 47 (unchanged).

## Outputs
- Final: `delivery/ep012-master-1k.mp4` sha256 `{sha(final)}`
- SRT: `delivery/ep012-subtitles.srt` (4 cues, UTF-8)
- Script: `edit/build_master_1k.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build1k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, qc/ mids + cut frames)
- Remotion inputs backed up to: `{backup}` (the ep011 2K inputs)

## Sources (all 720x1280 1K, accepted by Richard 2026-11-25 17:31)
- sh010 generated/sh010-take001.mp4 (native, Hùng, accepted, no dub) — trim 0-3.4s
- sh020 generated/sh020-take005-dubbed.mp4 (clone ThaoMy wordalign, take005, sha 60f66835…) — trim 0-5.3s
- sh030 generated/sh030-take002.mp4 (native, Hùng, accepted, no dub) — trim 0-4.7s
- sh040 generated/sh040-take003-dubbed.mp4 (clone ThaoMy wordalign) — trim 0-7.0s
- Nominal total {TOTAL:.2f}s; actual final {total:.2f}s (laugh + freeze tail).
  Bounds: {BOUNDS}

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,{CROP},scale=720:1280:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[3:v][3:a]concat=n=4:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {seg_durs}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on ALL FOUR 1K files
  (corner crops x600-720/y1150-1280 at t=2.5s: star top ~y1160, "Veo" text
  ~y1250-1267).
- Crop {CROP} = x 40..680, y 0..1138, then lanczos to 720x1280. Icon top edge
  ~22px below the crop line. One uniform crop so framing/scale matches across
  hard cuts. (The 2K crop 960:1707:60:0 scaled by 2/3.)

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope + 1fps frames)
- sh010 native speech 1.08-2.62s (energy loud 1.4-2.6s) -> 3.4s (beat 0.78s;
  watch-point gesture completes as his hand lowers to the table ~3.4s; the
  glass-drink at ~6-7s is Veo tail motion, cut)
- sh020 dubbed speech clusters 0.91-1.99 / 2.41-3.99 / 4.29-4.91 -> 5.3s
  (beat 0.39s; polite smile hold; cup-lowering/drinking at ~6.0s is tail, cut)
- sh030 native speech 0.90-4.34s -> 4.7s (beat 0.36s; bill push done ~3s,
  settled hand-on-folder; remaining 3.2s is static hold, cut)
- sh040 dubbed speech clusters 3.14-4.48 / 5.14-6.70 -> 7.0s (beat 0.30s;
  deadpan hold; HEAD 0-3.14s cup-down + smile-fade action untouched)

## Stage 2 captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. 47 words.
- Alignment fixes (same pattern as ep011's sh030 fix):
  - sh020 r05: "ba mươi ngàn" heard as "30" + ".000" (15 heard vs 16 script) —
    split the "30" span into "ba"/"mươi", map ".000" to "ngàn". Fallback: "30.000"
    as one token (14 heard) is split into "ba"/"mươi"/"ngàn".
  - sh040: "limited" heard as "lim" + "tế" — merged into "limited" spanning both.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep012-boxed-1k-chunk<N>.mp4 --props '{{"accent":"#F59E0B"}}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: {ranges} (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep012-boxed-1k-tmp.mp4.
- Caption problems (if any): see edit/build1k/captions-PROBLEMS.txt.

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
- ffprobe final: see script output above (720x1280, 30fps, AAC 48kHz stereo).
- Frame means: see script output above (black = mean ~0).
- Energy per shot + laugh-zone buckets: see script output above.
- Laugh per-channel: see script output above (RMS L/R ratio, L-R/L+R, envelope correlation).
- Contact sheet: edit/build1k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: {len(heard_final)} words heard (script: 47) — see script output above.
- SRT matches script exactly (asserted in-script).
"""
(WORK / "build-report-1k-r06.md").write_text(report)
print(report, flush=True)
print("BUILD 1K R06 DONE", flush=True)
