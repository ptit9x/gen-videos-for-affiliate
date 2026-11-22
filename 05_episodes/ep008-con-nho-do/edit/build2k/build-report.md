# ep008 master 2K FINAL — build report

## Outputs
- Final: `delivery/ep008-master-2k.mp4` sha256 `d1d6ea5703f58107fe0ffc9ea8ba61645e3ef7bb4ad7fab8a08c55864da64c74`
- SRT: `delivery/ep008-master-2k.srt`
- Scripts: `edit/build_master_2k.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build2k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, title frames in qc/)
- Remotion inputs backed up to: `/home/hatch/workspace/remotion-captions-test/public-ep008-1k-backup-1` (the 1K ep008 inputs)

## Sources (all TRUE 2K 1080x1920 24fps 7.85s, from ~/workspace/ep008-con-nho-do-clips/)
- sh010 sh010-take005-2k.mp4 sha 5fd6606f… (VIDEO) + wordalign dub audio from
  generated/sh010-take005-dub-thaomy-wordalign.mp4 — trim 0-2.8s
- sh020 sh020-take003-2k.mp4 sha 2e03040e… (VIDEO) + 1K native audio — trim 0-3.6s
- sh030 sh030-take002-2k.mp4 sha a3426242… (VIDEO) + wordalign dub audio from
  generated/sh030-take002-dub-thaomy-wordalign.mp4 — trim 0-5.2s
- sh040 sh040-take004-2k.mp4 sha d71d292b… (VIDEO) + 1K native audio — trim 0-5.0s
  (sentence 2 cut by design)
- sh050 sh050-take002-2k.mp4 sha 0cd5f023… (VIDEO) + 1K native audio — trim 0-2.0s
- sh060 LOCAL UPSCALE sh060-take015-2k-local-upscale.mp4 sha 80e5729a… (lanczos from
  approved 1K take015, 1080x1920 24fps) + 1K native audio — trim 0-7.0s.
  The downloaded sh060-take015-2k.mp4 (sha 7d103fc3…) is actually TAKE016
  (frame diff 2.1 vs take016 @2.5s; 16.3 vs take015) — wrong take, NOT used.
  A true Flow 2K re-download of take015 can swap this in later.
- sh070 sh070-take002-2k.mp4 sha e53cd889… (VIDEO) + 1K native audio — trim 0-3.0s
  (silent shot; Laugh Track 1 placed over it in stage 3)
- AUDIO RULE: approved 1K mixes for all native shots (sh020/sh050/sh070 1K audio ==
  2K audio; sh040's 2K audio is noisier; sh060's 2K audio belongs to take016).
- Nominal total 28.6s; actual final 28.67s (AAC priming/frame rounding).
  Bounds: {'sh010': (0.0, 2.8), 'sh020': (2.8, 6.4), 'sh030': (6.4, 11.600000000000001), 'sh040': (11.600000000000001, 16.6), 'sh050': (16.6, 18.6), 'sh060': (18.6, 25.6), 'sh070': (25.6, 28.6)}

## Stage 1 commands (per segment)
ffmpeg -i <2K video> [-i <1K wordalign file for sh010/sh030>] -vf "trim=0:<T>,setpts=PTS-STARTPTS,crop=960:1707:60:0,scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[6:v][6:a]concat=n=7:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11 (ep006 pattern), video copy.
Segment durations measured: {'sh010': 2.8, 'sh020': 3.6, 'sh030': 5.2, 'sh040': 5.0, 'sh050': 2.0, 'sh060': 7.0, 'sh070': 3.0}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on ALL 7 2K files
  (top-right corners clean foliage), same relative position as the 1K files.
- Crop crop=960:1707:60:0 = proportional 2K equivalent of the approved 1K crop 640:1138:40:0
  (x 60..1020, y 0..1707, then lanczos to 1080x1920). Icon top edge ~y1770-1832
  in 2K coords -> ~63px margin. One uniform crop so framing/scale matches the
  approved 1K preview exactly across hard cuts.

## Title ("CON NHỎ ĐÓ", ep004 style)
- Reused the existing Remotion TitleCard (src/TitleCard.tsx, already wired into
  CaptionedVideo via title/titleSeconds props) — NOT rebuilt. Render props:
  {"accent": "#F59E0B", "title": "CON NHỎ ĐÓ", "titleSeconds": 2}.
- Overlay on sh010, first 2s only, upper band (marginTop 9% height, fontSize
  11.5% width, white 900-weight uppercase + black stroke + accent underline bar).
  My's head top in sh010 is ~y460-480/1920 raw (~y517 final after crop+scale);
  title occupies ~y173-360 -> ~150px clear. Verified on frames 0.5/1.0/1.5s
  (edit/build2k/qc/final-title-*.png) — see QC notes below.
- No standalone card, no duration change, no timeline shift (total stays ~28.7s).

## Stage 2 captions (Remotion Boxed)
- Whisper base word timestamps RE-RUN on the 2K assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. Caption timing vs 1K:
  max delta 1000ms. Known ASR artifacts ignored by design.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep008-boxed-2k-chunk<N>.mp4 --props '{"accent":"#F59E0B","title":"CON NHỎ ĐÓ","titleSeconds":2}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: [(0, 286), (287, 573), (574, 860)] (<=287 frames each — the 1K
  lesson: full 861-frame render at --concurrency=2 exits 0 but goes BLACK from
  ~13.7s, Chrome OOM). Each chunk verified (exit code + size + duration + mean
  frame at chunk middle) before use. Video-only chunks concatenated, then muxed
  with assembly-norm audio -> out/ep008-boxed-2k-tmp.mp4.
- Caption problems (if any): see edit/build2k/captions-PROBLEMS.txt (empty = clean).

## Stage 3 laugh
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix over sh070, audible onset 25.7s (0.1s into the
  reaction shot), stem_start=25.44s, laugh ends 27.54s < 28.67s.
- NO freeze-frame tail (laugh fits inside the video).
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.
- Stage-3 duration fix applied from the start: total = len(dlg)/SR (actual
  boxed-audio duration), not nominal 28.6s.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, ~28.7s, AAC 48kHz stereo).
- Frame means at 0.5/1.0/1.5/5.0/9.5/9.6/13.7/15.0/19.0/19.2/22.0/26.0/28.3s:
  see script output above (black = mean ~0; chunk boundaries included).
- Title frames: edit/build2k/qc/final-title-0.5.png, final-title-1.0.png,
  final-title-1.5.png — inspect visually (title visible, upper band, clear of My's head).
- Energy per shot + sh070 laugh-zone buckets: see script output above.
- Contact sheet: edit/build2k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: see script output above (record only; script words govern captions).
