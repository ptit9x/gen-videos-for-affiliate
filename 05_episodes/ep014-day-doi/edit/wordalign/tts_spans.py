import numpy as np, subprocess
from faster_whisper import WhisperModel
TTS = "/home/hatch/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020.wav"
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base", device="cpu", compute_type="int8")
pcm16 = subprocess.run(["ffmpeg","-v","error","-i",TTS,"-vn","-ac","1","-ar","16000","-f","s16le","-"],capture_output=True,check=True).stdout
audio16 = np.frombuffer(pcm16, dtype=np.int16).astype(np.float32) / 32768.0
segs, info = model.transcribe(audio16, language="vi", beam_size=5, word_timestamps=True)
for seg in segs:
    print(f"SEG {seg.start:.2f}-{seg.end:.2f}: {seg.text.strip()}")
    for w in seg.words:
        print(f"  {w.word} {w.start:.2f}-{w.end:.2f}")
pcm = subprocess.run(["ffmpeg","-v","error","-i",TTS,"-vn","-ac","1","-ar","48000","-f","f32le","-"],capture_output=True,check=True).stdout
a = np.frombuffer(pcm, dtype=np.float32)
print("\nTTS ENERGY 0.1s buckets (rms):")
for i in range(0, 56):
    seg = a[i*4800:(i+1)*4800]
    if len(seg)==0: break
    v = float(np.sqrt(np.mean(seg**2)))
    print(f"{i/10:.1f}s {v:.4f} " + "#" * int(min(40, v*400)))
