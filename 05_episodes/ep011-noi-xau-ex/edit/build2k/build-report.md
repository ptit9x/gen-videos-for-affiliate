# ep011 master 2K FINAL — build report

## Outputs
- Final: `delivery/ep011-master-2k.mp4` sha256 `ebfdb8573e28e332b2f6a98c7e1c82f641380aed5c7554c81fe944d5e80d314b`
  (43.463.754 bytes, 28.30s, 1080×1920, 30fps, H.264 yuv420p, AAC 48kHz stereo)
- SRT: `delivery/ep011-master-2k.srt` (8 cues, UTF-8, 595 bytes)
- Cover candidate: `delivery/ep011-cover-thaomy.jpg` sha256
  `011f463dc00f22c47fdace79dd2233563df8fe3c200641cb5b5a9aea210c7c24`
  (1080×1920; sh040 6.5s, master t=26.45s — My eyes open, slight smile, looking at
  camera. Extracted from the UNCUTIONED assembly so no caption text is burned in;
  the first extraction from the captioned master carried the word "ANH." and was
  replaced. CANDIDATE for Richard to confirm, not a decision.)
- Scripts: `edit/build_master_2k.py` (stages 1–3 + QC, adapted from ep010) and
  `edit/build2k/resume_build.py` (resume after the first run was killed — see below)
- Work dir: `edit/build2k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, qc/ mids + cut frames + caption frames,
  measure_2k.py + .log, build_master_2k.log, resume_build.log)
- Remotion inputs backed up to: `~/workspace/remotion-captions-test/public-ep010-2k-backup`
  (the ep010 2K inputs)

## Build incident (recorded, not hidden)
- The first run of `build_master_2k.py` was killed by SIGTERM ~10 min in, while
  concatenating the video-only Remotion chunks — AFTER all 3 chunks had rendered
  and passed verification (exit + size + duration + mean frame). The partially
  written `boxed-video-only.mp4` was corrupt (moov atom missing).
- Resume: `resume_build.py` deleted the corrupt file and rebuilt it from the 3
  VERIFIED chunks (chunk0 287f/9.57s, chunk1 287f/9.57s, chunk2 257f/8.57s =
  831 frames = 27.70s), then continued with mux + stage 3 + final loudnorm + QC.
  No re-render, no re-gen, no re-dub, no new credits.

## Sources (all TRUE 2K 1080×1920, frame-diff verified vs the approved 1K takes)
- sh010 `generated/sh010-take001-1080p.mp4` (native, Dũng Southern, accepted) — trim 0–6.4s
- sh020 `generated/sh020-take001-dubbed-1080p.mp4` (clone ThaoMy wordalign, video from 2K
  + clone audio, native fully replaced; APPROVED by Richard 12:05 24/11) — trim 0–7.35s
- sh030 `generated/sh030-take002-1080p.mp4` (native, Dũng Southern, accepted) — trim 0–6.2s
- sh040 `generated/sh040-take001-1080p.mp4` (native, My Northern, accepted) — trim 0–7.7s
- Nominal video total 27.65s; actual final 28.30s (laugh + freeze tail).
  Bounds: sh010 0.00–6.40, sh020 6.40–13.75, sh030 13.75–19.95, sh040 19.95–27.65.

## Stage 1 commands (per segment)
```
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,crop=960:1707:60:0,scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
```
Concat: filter_complex `"[0:v][0:a]...[3:v][3:a]concat=n=4:v=1:a=1[v][a]"` (FILTER, never demuxer+copy).
Loudnorm: `loudnorm=I=-15.5:TP=-1.0:LRA=11`, video copy. Assembly-norm: 27.70s
(input_i −14.60, output_i −23.21 — the loudnorm measure's "output_i" is the
pre-normalisation measurement; the final loudnorm pass is measured separately below).

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on the sh010 + sh040 2K files
  (corner crops x900–1080/y1700–1920 at t=2.5s: star top ~y1735, "Veo" text
  ~y1855–1885), same relative position as ep010.
- Crop `crop=960:1707:60:0` = x 60..1020, y 0..1707, then lanczos to 1080×1920. Icon top
  edge ~28px below the crop line. One uniform crop so framing/scale matches across
  hard cuts. Verified on the final: no Veo icon / Gemini star visible in any checked
  frame (contact sheet, caption frames 1.5/8.0/15.0/22.0s, cut frames, cover).

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope on the 2K files)
- sh010 native speech 0.00–5.68s → 6.4s (beat 0.72s; eyes close ~5.8s, he settles/bows —
  the cut lands on the sad settle, before the deep bow ~7.5s)
- sh020 dubbed speech clusters 1.00–1.90 / 2.80–4.20 / 5.85–6.65 → 7.35s (beat 0.70s;
  Whisper smears first word to 0.72s — energy proves onset 1.00s)
- sh030 take002 speech 0.00–5.48s → 6.2s (beat 0.72s; eyes close ~5.8s, bow ~7.5s)
- sh040 native speech 0.66–3.58s + 5.16–6.30s (two sentences; Whisper smears first word
  to 0.66s, energy onset ~0.9s) → 7.7s (beat 1.40s — keeps the soft eyes-closed
  smile through 7.5s, ep010 pattern; the laugh plays over it)

## Stage 2 captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script words
  IN ORDER, energy-refined, clamped to shot bounds. 56 words, counts match exactly
  per shot (15/13/15/13).
- Boundary fix: Whisper put sh030's first word "Cũng" (13.20–13.92s, midpoint 13.56s)
  in sh020's window — moved to sh030 by the first-word match rule.
- sh030 note: this run heard "Bốn mối" as TWO words ("Bộ" + "mỗi"), so the
  3-for-2 fix prepared in the script (drop the extra "mỗi") did NOT fire and was
  not needed. The alignment is clean.
- `captions-PROBLEMS.txt` holds only routine end-time clamps (a word's energy-refined
  end ran 1 frame past the next word's start; clamped to the next start — the
  caption for each word ends exactly when the next begins).
- Render: `cd remotion-captions-test && npx remotion render Boxed
  out/ep011-boxed-2k-chunk<N>.mp4 --props '{"accent":"#F59E0B"}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted`. Chunks: (0–286), (287–573), (574–830)
  (≤287 frames each — the full-render-at-concurrency-2 lesson: exits 0 but goes
  BLACK from ~13.7s, Chrome OOM). Each chunk verified (exit code + size +
  duration + mean frame at chunk middle) before use. Video-only chunks
  concatenated, then muxed with assembly-norm audio → out/ep011-boxed-2k-tmp.mp4
  (27.70s, mean frame 100.3 @ 13.8s).
- SRT cues (8, from the caption word timings):
  1. 00:00:00,020–00:00:02,240 "Người yêu cũ anh tệ lắm em ơi."
  2. 00:00:02,240–00:00:05,850 "Ích kỷ, kiểm soát, không hiểu anh."
  3. 00:00:07,500–00:00:08,270 "Thương anh ghê."
  4. 00:00:09,300–00:00:13,050 "Chắc cô đó không xứng với anh. Rồi trước đó?"
  5. 00:00:13,770–00:00:14,310 "Cũng tệ."
  6. 00:00:15,150–00:00:19,330 "Mà cô trước nữa cũng vậy. Bốn mối rồi, lần nào cũng vậy."
  7. 00:00:20,580–00:00:23,710 "Bốn mối mà lần nào cũng lỗi người ta."
  8. 00:00:25,150–00:00:26,310 "Hay thật đấy anh."

## Stage 3 laugh (Laugh Track 1 after the sh040 punchline)
- Laugh Track 1: `~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3` (2.10s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix (NO adelay — the one-channel-leak lesson) right after the
  sh040 punchline. Last word "anh." ends 26.31s (caption timing); audible onset
  26.46s (last word + 0.15s); laugh onset in file 0.26s → stem_start 26.20s;
  laugh ends 28.30s.
- Freeze-frame tail 0.60s (still of the last frame, ep004 pattern) so the laugh
  fits; video itself ends at 27.70s.
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.
  Final loudnorm measure: input_i −14.92 LUFS, input_tp −0.97, input_lra 5.60
  (ep010's master was −14.99 LUFS — same ballpark).

## QC — all passed
- ffprobe final: 1080×1920, 30fps, H.264 yuv420p; AAC 48kHz 2ch; video 28.30s,
  audio 28.30s. No stream-duration mismatch.
- Frame means (final): t=0.5/1.0/3.0 → 107.4/107.2/107.4; 6.5/7.0 → 118.7/119.1;
  10.0 → 120.0; 13.6/13.9 → 118.6/100.6; 16.0 → 101.4; 20.0/22.0 → 114.1/116.4;
  26.0/26.5/27.5/28.2 → 115.4/115.5/114.4/113.9. No black segment anywhere
  (black ≈ 0; lowest 100.6).
- Energy per shot (48kHz stereo, 0.1s buckets, final audio): speech in all 4
  windows; sh010 0.5–5.9s; sh020 three clusters 7.4–8.3 / 9.3–10.6 / 12.3–13.1s
  with true silence between phrases (dub, wordalign); sh030 13.8–14.6 / 15.1–16.6 /
  17.1–19.3s; sh040 two sentences 20.9–23.7s + 25.1–26.3s with the pause between.
- Laugh zone buckets (26.3–28.2s): 0.16 → 0.57 peak → 0.065 tail. Laugh present
  ONLY at the end.
- Laugh per-channel (the adelay-leak check, measured on the BUILT file):
  laugh zone 26.46–28.30s RMS L=0.1291 R=0.1292, ratio 1.00; L−R RMS / L+R RMS
  = 0.062; L/R envelope correlation = 0.995. Both channels carry the same laugh —
  NO one-channel leak.
- Whisper base transcript of the final (56 words, all 4 lines in order, correct
  words modulo the KNOWN homophone artifacts): sh010 15 words ("cũ"→"cố",
  "tệ"→"tài", "em"→"mê", "ơi"→"mới", "Ích"→"Ý", "kiểm"→"kìm", "soát"→"sóc");
  sh020 13 words ("Thương"→"Thường", "cô"→"của", "xứng"→"sướng"); sh030 15 words
  ("tệ"→"tài", "nữa"→"nó", "Bốn mối"→"Bộ mỗi"); sh040 13 words ("Bốn mối"→"Bộ mỗi",
  "đấy"→"để"). Same artifacts as the per-take QC — the audio is the approved takes.
- Captions rendered (viewed directly on the final): t=1.5s "ANH TỆ LẮM" (amber on
  "TỆ"); t=8.0s "THƯƠNG ANH GHÊ." (amber on "GHÊ."); t=15.0s sh030 mid; t=22.0s
  "LẦN NÀO CŨNG" (amber on "LẦN"). Boxed style, amber #F59E0B highlight, correct
  text, correct timing. Contact sheet: `edit/build2k/qc-contact.png` (row 1 mids,
  row 2 cut frames — note: the sheet is 4 wide but 6 cut frames were pasted, so
  the 2 sh040 cut frames fell off the sheet; they were viewed individually at
  `edit/build2k/qc/final-cut-sh040-pre.png` and `final-cut-sh040-post.png`).
- Cuts viewed: sh010→sh020 (Dũng settle → My chin-on-hand), sh020→sh030 (My →
  Dũng, "CŨNG TỆ." caption on), sh030→sh040 (Dũng bowed/eyes closed, caption
  cleared → My looking at camera, no caption yet). All hard cuts clean, framing
  consistent, no Veo icon, no fake text.
- The master is NOT a buggy variant of anything: built fresh from the 4 verified
  2K takes + approved dub; the ep001 adelay bug pattern does not apply (numpy mix,
  per-channel verified).
