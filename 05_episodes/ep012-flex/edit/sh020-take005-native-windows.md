# ep012 sh020 take005 — native speech windows (energy, measured 2026-11-26)

Source: `generated/sh020-take005.mp4` (Flow clip 6b1f178f, 7.93s, 720x1280).
Method: ffmpeg decode to 48kHz stereo f32le; max-abs buckets 0.05s, refined
with 0.02s fine buckets at boundaries. Ambient floor ~0.02-0.04; speech
buckets 0.1-0.99. Whisper base word timestamps shown only for comparison —
Whisper smears phrase onsets ~0.3s early (known artifact); ENERGY is the
authority.

## Clusters (energy)

- P1 "Mấy tỷ thì kệ anh" (5 words): **0.91 – 1.99**
  - Onset: fine buckets 0.90:0.027, 0.92:0.207 → speech starts ~0.91.
  - End: fine buckets 1.98:0.148, 2.00:0.074, 2.02:0.013 → ends ~1.99.
  - Note: brief inter-word dip at 1.10 (0.026) between "Mấy" and "tỷ" —
    normal gap inside the cluster, not a boundary.
  - Whisper (smeared): words 0.62-1.96.
- P2 "em uống ly cà phê ba mươi ngàn" (8 words): **2.41 – 3.99**
  - Onset: fine buckets 2.40:0.011, 2.42:0.949 → starts ~2.41.
  - End: 0.05s buckets 3.95:0.200, 4.00:0.079 → ends ~3.99.
  - Whisper (smeared): words 2.44-3.80 (end truncated ~0.2s early).
- P3 "anh đừng lo" (3 words): **4.29 – 4.91**
  - Onset: 0.05s bucket 4.30:0.724, fine 4.26:0.010 → starts ~4.29.
  - End: fine buckets 4.88:0.181, 4.90:0.087, 4.92:0.066, 4.94:0.027 →
    sustained speech ends ~4.91 (isolated 4.96 blip 0.117 is a transient,
    not speech).
  - Whisper (smeared): words 4.12-4.78.

Silence between clusters: 2.00-2.41 and 4.00-4.29 (energy at floor).
After P3: 5.00+ ambient only (0.02-0.09, cup/breath noise, no speech).

## Comparison with take004 (r03/r05 record)
- take004: P1 1.02-1.90 / P2 2.40-4.05 / P3 4.56-5.18 (speech ends 5.18s).
- take005: P1 0.91-1.99 / P2 2.41-3.99 / P3 4.29-4.91 (speech ends 4.91s).
- take005 speaks the same line ~0.3s faster overall; P1 starts 0.11s earlier,
  P3 starts 0.27s earlier. Windows were re-measured, NOT copied from take004.

## TTS slices (energy on the r05 clone wav, same file as r05)
- P1: [0.04-0.62 + 0.90-1.68] = 1.36s (pause 0.62-0.90 cut, as in r05).
- P2: 2.04-4.05 = 2.01s (onset re-measured 2.04 vs r05's 2.01).
- P3: 4.55-5.47 = 0.92s (onset re-measured 4.55 vs r05's 4.53).
