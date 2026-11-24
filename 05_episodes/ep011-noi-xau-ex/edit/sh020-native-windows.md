# sh020 take001 — native word windows (measured 2026-11-24, for wordalign dub)
# Source: generated/sh020-take001.mp4 (1K).
# Whisper base (vi) + energy envelope 48kHz stereo, 0.05s max-abs buckets,
# per-channel. Whisper SMEARED the first word of cluster 1 early by 0.4s
# (said "Thuong" 0.6-1.2; energy shows ambient until 1.00s, speech from
# 1.05s) — energy is the authority on onset/offset, Whisper only for
# word ORDER/count.
# Phrase energy windows: "Thuong anh ghe." 1.00-1.90s,
# "Chac co do khong xung voi anh." 2.80-4.20s, "Roi truoc do?" 5.85-6.65s.
# Silence gaps: 0.0-1.0s, 1.9-2.8s, 4.2-5.85s, 6.65-7.93s.
# (Ambient transients in native: ~0.2-0.4s up to 0.19, ~2.25s 0.14,
# ~4.25-4.3s 0.18, ~6.9s 0.24 — all muted in the dub.)
# Script words (13): Thuong anh ghe. Chac co do khong xung voi anh. Roi truoc do?
# Whisper words (13, in order; homophone artifacts only):
#   Thuong 0.6-1.2 | anh 1.2-1.4 | ghe 1.4-1.8 | chac 2.64-2.98 |
#   co 2.98-3.18 | do 3.18-3.26 | khong 3.26-3.5 | xung 3.5-3.76 |
#   voi 3.76-3.86 | anh 3.86-4.16 | Roi 5.72-6.02 | truoc 6.02-6.32 |
#   do 6.32-6.56
# (Whisper heard "Thuong anh ghe, chac cau do hong suong nhu anh, roi truoc do"
# — "khong xung" -> "hong suong": nghieng Nam, ly do long tieng.)
# Dub: clone ThaoMyVeo (VieNeu v3 Turbo, Colab T4, session ep011-dub).
# TTS wav: ~/workspace/colab-t4-test/ep011-dub/thaomy-ep011-sh020.wav (5.20s)
# Wordalign build: edit/build_wordalign_sh020.py (stretch factors <= 1.8x).
