import numpy as np, subprocess
from faster_whisper import WhisperModel
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base", device="cpu", compute_type="int8")
for tag, path in [("v1-Parasite", "/home/hatch/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020.wav"),
                  ("v2-Pa-ra-sai", "/home/hatch/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020-phonetic.wav")]:
    pcm16 = subprocess.run(["ffmpeg","-v","error","-i",path,"-vn","-ac","1","-ar","16000","-f","s16le","-"],capture_output=True,check=True).stdout
    audio16 = np.frombuffer(pcm16, dtype=np.int16).astype(np.float32) / 32768.0
    segs, _ = model.transcribe(audio16, language="vi", beam_size=5, word_timestamps=True)
    print(f"== {tag} (unprompted) ==")
    for seg in segs:
        print(f" SEG {seg.start:.2f}-{seg.end:.2f}: {seg.text.strip()}")
        for w in seg.words:
            print(f"   {w.word} {w.start:.2f}-{w.end:.2f}")
    # energy: first/last speech (rms>0.02)
    pcm = subprocess.run(["ffmpeg","-v","error","-i",path,"-vn","-ac","1","-ar","48000","-f","f32le","-"],capture_output=True,check=True).stdout
    a = np.frombuffer(pcm, dtype=np.float32)
    buckets = [float(np.sqrt(np.mean(a[i*4800:(i+1)*4800]**2))) for i in range(len(a)//4800)]
    speech = [i/10 for i,b in enumerate(buckets) if b > 0.02]
    print(f" speech buckets>0.02: {speech[0]:.1f}-{speech[-1]:.1f}s" if speech else " no speech")
