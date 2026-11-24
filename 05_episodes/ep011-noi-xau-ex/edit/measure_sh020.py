"""Measure native speech windows for ep011 sh020 take001 (1K).
Whisper base (vi, word timestamps) + energy envelope 48kHz stereo,
0.1s max-abs buckets (threshold 0.02) and RMS buckets.
Whisper smears onsets early; energy is the authority on onset/offset.
"""
import subprocess
import sys

import numpy as np

sys.path.insert(0, "/home/hatch/.local/lib/python3.12/site-packages")
from faster_whisper import WhisperModel

CLIP = "/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep011-noi-xau-ex/generated/sh020-take001.mp4"


def decode(path, rate, channels):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", str(channels),
           "-ar", str(rate), "-f", "s16le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0


model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base",
                     device="cpu", compute_type="int8")
audio16 = decode(CLIP, 16000, 1)
segments, _ = model.transcribe(audio16, language="vi", word_timestamps=True)
words = []
text = []
for seg in segments:
    text.append(seg.text)
    for w in (seg.words or []):
        words.append((round(w.start, 2), round(w.end, 2), w.word))
print("TEXT:", "".join(text).strip())
print("WORDS:", words)

audio48 = decode(CLIP, 48000, 2).reshape(-1, 2)
mono = audio48.mean(axis=1)
n = len(mono) // 4800
maxb = [float(np.abs(mono[i * 4800:(i + 1) * 4800]).max()) for i in range(n)]
rmsb = [float(np.sqrt(np.mean(mono[i * 4800:(i + 1) * 4800] ** 2))) for i in range(n)]
print("MAX buckets:", [round(b, 3) for b in maxb])
print("RMS buckets:", [round(b, 3) for b in rmsb])
active = [i for i, b in enumerate(maxb) if b > 0.02]
print("MAX>0.02 buckets:", active)
