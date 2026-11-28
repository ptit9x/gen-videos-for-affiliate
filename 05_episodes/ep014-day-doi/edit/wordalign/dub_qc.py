import numpy as np, subprocess
from faster_whisper import WhisperModel
EP = "/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep014-day-doi"
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base", device="cpu", compute_type="int8")
audio16 = np.fromfile(f"{EP}/edit/wordalign/sh020-dubbed-16k.wav", dtype=np.int16).astype(np.float32) / 32768.0
segs, _ = model.transcribe(audio16, language="vi", beam_size=5, word_timestamps=True)
print("DUBBED Whisper (unprompted):")
for seg in segs:
    print(f" SEG {seg.start:.2f}-{seg.end:.2f}: {seg.text.strip()}")
    for w in seg.words:
        print(f"   {w.word} {w.start:.2f}-{w.end:.2f}")
pcm = subprocess.run(["ffmpeg","-v","error","-i",f"{EP}/generated/sh020-take001-dubbed.mp4","-vn","-ac","1","-ar","48000","-f","f32le","-"],capture_output=True,check=True).stdout
a = np.frombuffer(pcm, dtype=np.float32)
print("\nDUBBED energy 0.1s buckets:")
for i in range(0, 50):
    seg = a[i*4800:(i+1)*4800]
    if len(seg)==0: break
    v = float(np.sqrt(np.mean(seg**2)))
    print(f"{i/10:.1f}s {v:.4f} " + "#" * int(min(40, v*400)))
