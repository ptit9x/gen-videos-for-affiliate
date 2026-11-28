import numpy as np, subprocess, json
from faster_whisper import WhisperModel
EP = "/home/hatch/workspace/gen-videos-for-affiliate-git/05_episodes/ep014-day-doi"
model = WhisperModel("/home/hatch/MoneyPrinterTurbo/models/whisper-base", device="cpu", compute_type="int8")
SHOTS = {
 "sh010": "generated/sh010-take001.mp4",
 "sh030": "generated/sh030-take001.mp4",
 "sh040": "generated/sh040-take001.mp4",
}
for sh, path in SHOTS.items():
    # 16k wav for whisper
    subprocess.run(["ffmpeg","-v","error","-y","-i",f"{EP}/{path}","-vn","-ac","1","-ar","16000",
                    f"{EP}/edit/wordalign/{sh}-native-16k.wav"], check=True)
    d16 = np.fromfile(f"{EP}/edit/wordalign/{sh}-native-16k.wav", dtype=np.int16).astype(np.float32)/32768.0
    segs,_ = model.transcribe(d16, language="vi", beam_size=5, word_timestamps=True)
    print(f"\n== {sh} Whisper base ==")
    for seg in segs:
        print(f" SEG {seg.start:.2f}-{seg.end:.2f}: {seg.text.strip()}")
        for w in seg.words:
            print(f"   {w.word} {w.start:.2f}-{w.end:.2f} p={w.probability:.2f}")
    # 48k stereo energy envelope, 0.1s buckets (per-channel RMS)
    pcm = subprocess.run(["ffmpeg","-v","error","-i",f"{EP}/{path}","-vn","-ac","2","-ar","48000","-f","f32le","-"],capture_output=True,check=True).stdout
    a = np.frombuffer(pcm, dtype=np.float32).reshape(-1,2)
    print(f"== {sh} energy 0.1s buckets (L/R RMS) ==")
    for i in range(0, 80):
        seg = a[i*4800:(i+1)*4800]
        if len(seg)==0: break
        l = float(np.sqrt(np.mean(seg[:,0]**2))); r = float(np.sqrt(np.mean(seg[:,1]**2)))
        print(f"{i/10:.1f}s L={l:.4f} R={r:.4f}")
    # 1fps frames
    subprocess.run(["ffmpeg","-v","error","-y","-i",f"{EP}/{path}","-vf","fps=1,scale=360:640",
                    f"{EP}/edit/qc-frames/trim-{sh}-f%02d.png"], check=True)
    print(f"  frames: edit/qc-frames/trim-{sh}-f*.png")
