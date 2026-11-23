# sh020 take001 — native word windows (measured 2026-11-23, for wordalign dub)
# Source: generated/sh020-take001.mp4 (1K; timing identical in 2K, same clip).
# Whisper base (vi, prob 1.00) + energy envelope 48kHz stereo, 0.1s RMS buckets.
# Whisper smears onsets early (first word to 0.00); energy is the authority on
# actual onset/offset. Phrase energy windows: "Tuần hai." ~0.0-0.7s,
# "Một tin." ~1.6-2.3s, "Dạo này bận quá." ~3.2-4.3s, "Rồi im." ~5.7-6.4s.
# Silence gaps: ~0.7-1.6s, ~2.3-3.2s, ~4.3-5.7s.
# Script words (10): Tuần hai. Một tin. Dạo này bận quá. Rồi im.
# Whisper words (10, in order; homophone artifacts only):
#   Tuần 0.00-0.24 | hai, 0.24-0.54 | một 1.32-1.76 | tin, 1.76-2.14 |
#   Dạo 2.92-3.40 | này 3.40-3.52 | bận 3.52-3.84 | quá 3.84-4.02 |
#   Rồi 5.34-6.08 | im 6.08-6.44
# (Whisper heard "Tụng hai, một tinh, giáo này bộn quá / Rồi em" — đồng âm.)
# Energy RMS 0.1s buckets (index = 0.1s): see measure_sh020.py output.
# Dub: clone ThaoMyVeo (VieNeu v3 Turbo, Colab T4, session ep010-dub).
# TTS wav: ~/workspace/colab-t4-test/ep010-dub/thaomy-ep010-sh020.wav
# Wordalign build: edit/build_wordalign_sh020.py (rebuild of the lost
# /tmp/ep009_build_wordalign.py; stretch factors must stay <= 1.8x).
