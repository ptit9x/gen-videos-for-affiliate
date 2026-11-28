# ep014 master 1080p — build report

## Outputs
- Final: `delivery/ep014-master-1080p.mp4` sha256 `a724a463005e82e2162a4b9a0bdc016d091b2e376a9d03702e626dfed15fa336`
- SRT: `delivery/ep014-subtitles.srt` (4 cues, UTF-8)
- Script: `edit/build_master_ep014.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build1080p/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, qc/ mids + cut frames)
- Remotion inputs backed up to: `/home/hatch/workspace/remotion-captions-test/public-ep013-1080p-backup-1` (the ep013 1080p inputs)

## Sources (all accepted by Richard 10:21 28/11)
- sh010 generated/sh010-take001.mp4 (native, Northern male) — trim 0-5.5s
- sh020 generated/sh020-take001-dubbed.mp4 (clone ThaoMy wordalign, QC DAT) — trim 0-5.5s
- sh030 generated/sh030-take001.mp4 (native, Northern male) — trim 0-4.5s
- sh040 generated/sh040-take001.mp4 (native, Northern female) — FULL 0-7.93s
- No end card, no title card (not ordered).
- Nominal total 23.43s. Bounds: {'sh010': (0.0, 5.5), 'sh020': (5.5, 11.0), 'sh030': (11.0, 15.5), 'sh040': (15.5, 23.43)}

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,<crop>,scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[3:v][3:a]concat=n=4:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {'sh010': 5.5, 'sh020': 5.5, 'sh030': 4.5, 'sh040': 7.933333}

## Crop decision
- "AI" pill + "Veo" text verified present BOTTOM-RIGHT on all four 720 sources
  at t=2.5s (pill ~y1190-1230, text ~y1250-1267; sh040: "Veo" text confirmed
  at bottom-right corner 28/11) — see edit/qc-frames/icon-*.png.
- Crop crop=640:1138:40:0 = x 40..680, y 0..1138, then lanczos to 1080x1920.
  Icon top edge ~52px below the crop line. One uniform crop for all four 720
  sources so framing/scale matches across hard cuts.
- sh040: crop=640:1138:40:0 (watermark chuan) — KHONG crop vai: Richard 11:16
  chot dung ban goc (crop v1 mat 75-82% + v2 mat 71% deu REJECT); vai Nam sai
  mau ao chap nhan. Corner check saved per segment (edit/build1080p/corner-*.png).

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope + 1fps frames)
- sh010 native speech 0.4-4.4s (P1 0.4-2.6, P2 3.1-4.4) -> 5.5s (speech end + 1.1s smile beat)
- sh020 dubbed speech 0.20-3.95s (P1 0.20-2.95, P2 3.20-3.95) -> 5.5s (speech end + 1.5s smile beat;
  cut before the 7s tail action of putting the cup down)
- sh030 native speech 0.2-2.55s (P1 0.2-1.56, P2 1.8-2.54) -> 4.5s (speech end + ~2s gesture/settle;
  cut before the 6-7s reach for the orange juice glass)
- sh040 native speech 1.6-5.44s (P1 1.6-2.0, P2 2.5-3.6, P3 4.0-5.44) -> FULL 7.93s
  (1.6s listening beat at the head; 5.44-7.93 smile reaction + room for the laugh)

## Captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. 56 words.
- Merges (1 script word heard as several): sh010 "latte" <- "lat"+"te";
  sh020 "Parasite" <- "va"+"gia"+"xai" (phonetic dub "Pa-ra-sai").
  Known homophones relabelled, not re-timed: sh010 "Ca phia"->"Ca phe",
  sh020 "xin"->"xem" x2, "em"->"anh" (P2, Whisper LM bias — proven on the dub QC),
  sh030 "vi"->"y", "Me anh day thiet"->"de anh giai thich".
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep014-boxed-1080p-chunk<N>.mp4 --props '{"accent":"#F59E0B"}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: [(0, 286), (287, 573), (574, 704)] (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep014-boxed-1080p-tmp.mp4.
- Caption problems (if any): see edit/build1080p/captions-PROBLEMS.txt.

## Stage 3 laugh (Laugh Track 1 after the sh040 punchline)
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Last word 'thôi.' ends 20.99s; laugh audible at
  21.14s (stem_start 20.88s, onset 0.26s),
  laugh file ends ~22.98s, video 23.50s.
- numpy mix, NO adelay (both channels get the stem). Per-channel QC below.
