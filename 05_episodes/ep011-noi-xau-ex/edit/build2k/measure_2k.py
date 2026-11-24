"""Measure ep011 2K sources: ffprobe + 48kHz stereo 0.1s energy buckets + Whisper base words."""
import json, pathlib, subprocess, sys
import numpy as np
sys.path.insert(0, '/home/hatch/.local/lib/python3.12/site-packages')
from faster_whisper import WhisperModel

EP = pathlib.Path("/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep011-noi-xau-ex")
GEN = EP / "generated"
SRCS = [
    ("sh010", GEN / "sh010-take001-1080p.mp4"),
    ("sh020", GEN / "sh020-take001-dubbed-1080p.mp4"),
    ("sh030", GEN / "sh030-take002-1080p.mp4"),
    ("sh040", GEN / "sh040-take001-1080p.mp4"),
]

def probe(p):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json",
                        "-show_format", "-show_streams", str(p)], capture_output=True, text=True)
    return json.loads(r.stdout)

def decode(p, rate, channels):
    cmd = ["ffmpeg", "-v", "error", "-i", str(p), "-ac", str(channels), "-ar", str(rate),
           "-f", "s16le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base",
                     device="cpu", compute_type="int8", local_files_only=True)
for sh, src in SRCS:
    info = probe(src)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    a = [s for s in info["streams"] if s["codec_type"] == "audio"][0]
    print(f"== {sh} {src.name}: {v['width']}x{v['height']} v={float(v['duration']):.2f}s "
          f"a={float(a['duration']):.2f}s {a['codec_name']} {a['sample_rate']}Hz {a['channels']}ch")
    audio48 = decode(src, 48000, 2).reshape(-1, 2)
    m = np.abs(audio48).max(axis=1)
    hop = 4800
    buckets = [float(m[i*hop:(i+1)*hop].max()) for i in range(len(m)//hop + 1)]
    print("  buckets 0.1s:", " ".join(f"{b:.2f}" for b in buckets))
    audio16 = decode(src, 16000, 1)
    segs, _ = model.transcribe(audio16, language="vi", word_timestamps=True, beam_size=5)
    for s in segs:
        for w in (s.words or []):
            print(f"  word {w.start:.2f}-{w.end:.2f} {w.word.strip()!r} p={w.probability:.2f}")
    print(f"  text: {' '.join(s.text.strip() for s in segs)}")
print("MEASURE DONE")
