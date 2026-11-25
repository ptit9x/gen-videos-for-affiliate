# sh040 take003 — native word windows (measured 2026-11-25, for wordalign dub)
# Source: generated/sh040-take003.mp4 (1K).
# Whisper base (vi) + energy envelope 48kHz stereo, 0.05s max-abs buckets
# per-channel + 0.02s fine buckets at boundaries. Whisper SMEARED the first
# word of P1 ("Đồng" 3.14s) vs energy-strong from 3.48s, but the 3.10-3.48s
# region stays elevated (0.05-0.14, vs 0.02-0.04 ambient floor) — consistent
# with a soft speech onset, so P1 starts at the Whisper time 3.14s. Energy
# is the authority on offset and on P2 onset (5.14s vs Whisper 5.22s).
# Phrase energy windows: "Đồng hồ limited" 3.14-4.48s,
# "mà chia bill ly cà phê" 5.14-6.70s.
# Silence gaps: 0.0-3.14s, 4.48-5.14s, 6.70-7.93s.
# (Ambient transients in native: cup clinks at ~2.58s/2.64s (0.32/0.36,
# single 0.02s buckets) and ~7.35-7.85s — all muted in the dub.)
# Script words (9): Đồng hồ limited mà chia bill ly cà phê.
# Whisper words (9, in order; homophone artifacts only):
#   Đồng 3.14-3.70 | hồ 3.70-3.98 | limited->lim ít thích 3.98-4.62 |
#   mà 5.22-5.28 | chia 5.28-5.58 | bill->biêu 5.58-5.90 |
#   ly->lây 5.90-6.08 | cà 6.08-6.30 | phê 6.30-6.68
# Dub: clone ThaoMyVeo (VieNeu v3 Turbo, Colab T4, session ep012-dub).
# TTS wav: ~/workspace/colab-t4-test/ep012-dub/thaomy-ep012-sh040.wav
# Wordalign build: edit/build_wordalign_sh040.py (stretch factors <= 1.8x).
