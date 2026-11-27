# ep013 master 1080p — build report

## Outputs
- Final: `delivery/ep013-master-1080p.mp4` sha256 `5c9568bc5215d28b56689edbbd5a4083ef902c0897c8115c98f2c3f0a33d4044`
- SRT: `delivery/ep013-subtitles.srt` (6 cues, UTF-8)
- Script: `edit/build_master_ep013.py` (this file, stages 0-3 + QC)
- Work dir: `edit/build1080p/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, qc/ mids + cut frames + endcard)
- Remotion inputs backed up to: `/home/hatch/workspace/remotion-captions-test/public-ep012-1k-backup-1` (the ep012 1K inputs)

## Sources (all accepted by Richard)
- sh010 generated/sh010-take004-dubbed.mp4 (clone ThaoMy wordalign) — trim 0-6.5s
- sh020 generated/sh040-take002-1080p-facecrop.mp4 (REUSE, take001 + dub v2 rejected 16:54) — trim 0-5.3s
- sh030 generated/sh030-take001.mp4 (native, Northern) — trim 0-4.5s
- sh040 generated/sh040-take002-1080p-facecrop.mp4 (accepted 14:40 27/11) — trim 0-5.3s
- sh050 generated/sh050-take003-dubbed.mp4 (clone ThaoMy wordalign) — keep full 5.17s
- sh060 generated/sh040-take002-1080p-facecrop.mp4 (REUSE, take001 rejected) — trim 0-5.3s
- endcard: black 2.0s, PIL + DejaVuSans-Bold, "Em mặc gì anh cũng chỉ thấy... / 'Dễ Thương'"
  (script.md verbatim; line 2 in amber #F59E0B)
- Nominal total 34.07s (shots 32.07s + end card 2.00s).
  Bounds: {'sh010': (0.0, 6.5), 'sh020': (6.5, 11.8), 'sh030': (11.8, 16.3), 'sh040': (16.3, 21.6), 'sh050': (21.6, 26.770000000000003), 'sh060': (26.770000000000003, 32.07)} endcard=(32.07, 34.07)

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,[crop=640:1138:40:0,]scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[6:v][6:a]concat=n=7:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {'sh010': 6.5, 'sh020': 5.3, 'sh030': 4.5, 'sh040': 5.3, 'sh050': 5.17, 'sh060': 5.3, 'endcard': 2.0}

## Crop decision
- "Veo" text verified present BOTTOM-RIGHT on ALL THREE 720 sources at t=2.5s
  (corner crops x600-720/y1150-1280: "Veo" ~y1250-1267, star ~y1160).
- Crop crop=640:1138:40:0 = x 40..680, y 0..1138, then lanczos to 1080x1920.
  Icon top edge ~22px below the crop line. One uniform crop for the three 720
  sources so framing/scale matches across hard cuts.
- face-crop file: NO icon (its 500x889 crop window y 478..1367 already cut the
  2K icon at y~1700+) -> no crop. Corner check saved per segment (edit/build1080p/corner-*.png).

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope + 1fps frames)
- sh010 dubbed speech 0.8-2.76s (Whisper "Anh xem xuc em bo nay thay sao?" —
  "xuc" = homophone for "giup") -> 6.5s (the spin IS the action: mid-spin 2s,
  back to camera 4s, facing camera settled ~6s; cutting at 3.5s would cut mid-spin)
- sh020/sh040/sh060 face-crop speech 0.0-1.16s + laugh burst 4.7-4.9s -> 5.3s
  (burst + 0.4s beat; at 5.3s Nam is in a gentle laughing hold)
- sh030 native speech 0.5-1.2s (Whisper "The con bo nay", 4 words) -> 4.5s
  (spin: turning 2-3s, over-shoulder look 3s, facing camera settled ~4s)
- sh050 dubbed speech ends ~5.05-5.1s -> keep full 5.17s (Richard's trim 27/11)

## Captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. 36 words.
- Alignment: heard->script by position within each shot (counts matched in all
  6 shots). Known homophones relabelled, not re-timed: sh010 "xuc"->"giup",
  sh050 "quy"->"cuoi", sh020/sh040/sh060 "U,"->"Um...".
- IMPORTANT: sh020/sh040/sh060 captions are all "Um... de thuong!" — the
  face-crop clip's actual audio. The script's sh020 line ("De thuong nha") and
  sh060 line ("O... thi... phoi kieu... de thuong.") are NOT what's heard, so
  they are NOT captioned. SRT follows actual audio.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep013-boxed-1080p-chunk<N>.mp4 --props '{"accent":"#F59E0B"}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: [(0, 286), (287, 573), (574, 860), (861, 1025)] (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep013-boxed-1080p-tmp.mp4.
- Caption problems (if any): see edit/build1080p/captions-PROBLEMS.txt.

## Stage 3 laugh (Laugh Track 1 after the sh060 punchline)
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix (NO adelay — the one-channel-leak lesson) right after the
  sh060 punchline, audible onset 28.14s (last word ends
  27.99s + 0.15s), stem_start=27.88s, laugh ends ~29.98s.
  No freeze tail: the laugh ends well before the video end (34.20s); the
  sequence is line -> audience laugh -> Nam's own visual laugh burst (~31.5s)
  -> 2s black end card (silent).
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, AAC 48kHz stereo).
- Frame means: see script output above (black = mean ~0; end card ~0 is expected).
- Energy per shot + laugh-zone + end-card silence: see script output above.
- Laugh per-channel: see script output above (RMS L/R ratio, L-R/L+R, envelope correlation).
- Contact sheet: edit/build1080p/qc-contact.png (row1 mids sh010-sh040, row2 mids
  sh050/sh060/endcard, row3 cut frames) — inspect visually.
- Whisper transcript of final: 33 words heard (script: 36) — see script output above.
- SRT matches script exactly (asserted in-script).
