"""ep006 sh020 dub: clone ThaoMyVeo, gen 3 cau thoai (giong Nam -> clone Bac)."""
import os
import time

from vieneu import Vieneu

OUT_DIR = "/content/ep006_sh020_dub"
os.makedirs(OUT_DIR, exist_ok=True)

LINES = {
    "q1-hen-voi-ai-vay": "Hẹn với ai vậy?",
    "q2-di-mot-minh-a": "Đi một mình à?",
    "q3-toi-ghe": "Tội ghê.",
}

t0 = time.time()
v = Vieneu()  # default = v3 Turbo, 48 kHz
print(f"[load] ready in {time.time() - t0:.1f}s", flush=True)

t0 = time.time()
name = v.add_voice("ThaoMyVeo", "/content/ref-clip2.wav")
print(f"[clone] enrolled {name!r} in {time.time() - t0:.1f}s", flush=True)

for slug, text in LINES.items():
    t0 = time.time()
    audio = v.infer(text, voice="ThaoMyVeo")
    out = f"{OUT_DIR}/{slug}.wav"
    v.save(audio, out)
    print(f"[{slug}] wall={time.time() - t0:.1f}s audio={len(audio)/48000:.2f}s text={text} -> {out}", flush=True)
print("[done]")
