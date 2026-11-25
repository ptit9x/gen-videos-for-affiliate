# sh020 take004 — native word windows (measured 2026-11-25, for wordalign dub)
# Source: generated/sh020-take004.mp4 (1K).
# Whisper base (vi) + energy envelope 48kHz stereo, 0.05s max-abs buckets
# per-channel + 0.02s fine buckets at boundaries. Whisper SMEARED the first
# word of P1 ("Dạ" 0.76s) and P3 ("anh" 4.24s) early by ~0.3s — energy is
# the authority on onset/offset, Whisper only for word ORDER/count.
# Phrase energy windows: "Dạ hay quá anh," 1.02-1.90s,
# "em uống ly cà phê ba mươi ngàn," 2.40-4.05s, "anh đừng lo" 4.56-5.18s.
# Silence gaps: 0.0-1.02s, 1.90-2.40s, 4.05-4.56s, 5.18-7.93s.
# (Ambient transients in native: ~0.25-0.35s up to 0.09, ~2.25-2.35s 0.07,
# ~5.38-5.46s 0.18 — all muted in the dub.)
# Script words (15): Dạ hay quá anh, em uống ly cà phê ba mươi ngàn, anh đừng lo.
# Whisper words (14, in order; homophone artifacts only):
#   Dạ->Giữa 0.76-1.22 | hay 1.22-1.42 | quá 1.42-1.62 | anh 1.62-1.88 |
#   em 2.42-2.54 | uống 2.54-2.76 | ly->lý 2.76-2.86 | cả 2.86-3.02 |
#   phê 3.02-3.32 | 30 3.32-3.62 | .000 3.62-3.86 | anh 4.24-4.66 |
#   đừng 4.66-4.86 | lo 4.86-5.04
# Dub: clone ThaoMyVeo (VieNeu v3 Turbo, Colab T4, session ep012-dub).
# TTS wav: ~/workspace/colab-t4-test/ep012-dub/thaomy-ep012-sh020.wav
# Wordalign build: edit/build_wordalign_sh020.py (stretch factors <= 1.8x).
