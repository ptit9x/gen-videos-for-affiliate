import numpy as np, subprocess
from faster_whisper import WhisperModel
TTS = "/home/hatch/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020.wav"
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base", device="cpu", compute_type="int8")
pcm16 = subprocess.run(["ffmpeg","-v","error","-i",TTS,"-vn","-ac","1","-ar","16000","-f","s16le","-"],capture_output=True,check=True).stdout
audio16 = np.frombuffer(pcm16, dtype=np.int16).astype(np.float32) / 32768.0
prompt = "Mà hôm qua em xem phim Parasite hay lắm, anh xem chưa?"
segs, info = model.transcribe(audio16, language="vi", beam_size=5, word_timestamps=True, initial_prompt=prompt)
print("PROMPTED:")
for seg in segs:
    print(f"SEG {seg.start:.2f}-{seg.end:.2f}: {seg.text.strip()}")
    for w in seg.words:
        print(f"  {w.word} {w.start:.2f}-{w.end:.2f} p={w.probability:.2f}")
# also unprompted beam1 for comparison
segs2, _ = model.transcribe(audio16, language="vi", beam_size=1, word_timestamps=True)
print("\nBEAM1:")
for seg in segs2:
    print(f"SEG {seg.start:.2f}-{seg.end:.2f}: {seg.text.strip()}")
