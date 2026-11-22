# ep008 master 1K preview — build report

## Outputs
- Preview: `edit/ep008-master-1k-preview.mp4` sha256 `618568ff2f1b65ba36da018059b4ce46f645264423be1bfcdfd86241c074a13c`
- SRT: `edit/ep008-master-1k-preview.srt`
- Scripts: `edit/build_master_1k.py` (stages 1-2 + render) + `edit/stage3_only.py`
  (stage 3 rerun — the first run crashed on a shape mismatch, see below)
- Work dir: `edit/build1k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render.log, qc-contact.png)

## Sources (all 1K 720x1280 24fps, from generated/)
- sh010 sh010-take005-dub-thaomy-wordalign.mp4 (clone ThaoMy, word-aligned) trim 0-2.8s
- sh020 sh020-take003.mp4 (native) trim 0-3.6s
- sh030 sh030-take002-dub-thaomy-wordalign.mp4 (clone ThaoMy, word-aligned) trim 0-5.2s
- sh040 sh040-take004.mp4 (native) trim 0-5.0s (sentence 2 cut by design)
- sh050 sh050-take002.mp4 (native) trim 0-2.0s
- sh060 sh060-take015.mp4 (native, NOT the dub-minhquan spare) trim 0-7.0s
- sh070 sh070-take002.mp4 (native, silent) trim 0-3.0s
- Nominal total 28.6s; actual final 28.67s (extra ~0.07s is AAC
  priming/frame rounding at the tail — shot bounds unchanged). Bounds: {'sh010': (0.0, 2.8), 'sh020': (2.8, 6.4), 'sh030': (6.4, 11.600000000000001), 'sh040': (11.600000000000001, 16.6), 'sh050': (16.6, 18.6), 'sh060': (18.6, 25.6), 'sh070': (25.6, 28.6)}

## Stage 1 commands (per segment)
ffmpeg -i <src> -vf "trim=0:<T>,setpts=PTS-STARTPTS,crop=640:1138:40:0,scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[6:v][6:a]concat=n=7:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11 (ep006 pattern), video copy.
  Measured on assembly: input_i -14.95 LUFS (target -15.5, single-pass deviation 0.55 LU).
Segment durations measured: {'sh010': 2.8, 'sh020': 3.6, 'sh030': 5.2, 'sh040': 5.0, 'sh050': 2.0, 'sh060': 7.0, 'sh070': 3.0}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on ALL 7 shots (top-right
  corners clean foliage). Icon top edge ranges y~1180-1221 across shots (720x1280 coords).
- Uniform crop crop=640:1138:40:0 (=640x1138 window, x 40..680, y 0..1138, then lanczos to
  1080x1920): removes the icon on every shot with ~40px margin. One uniform crop
  (not per-shot) so framing/scale stays consistent across hard cuts; per-shot crops
  would visibly change zoom shot-to-shot. Faces/hands verified safe on mid frames
  (hands lowest ~y1010 in sh070, well above the 1138 cut line).

## Stage 2 captions (Remotion Boxed)
- Whisper base word timestamps on assembly audio, aligned to script words IN ORDER,
  energy-refined (10ms buckets, thr 0.02), clamped to shot bounds, overlaps clamped.
  Counts clean on all 6 dialogue shots (8/8, 9/9, 12/12, 9/9, 6/6, 14/14 = 58 words).
  Known ASR artifacts ignored by design: "chia tay"->"chi tai", "Giua"->"du", "Lo"->"lua",
  "a?"->"ta". captions-PROBLEMS.txt lists only benign 10-30ms end clamps (refined word
  ends running into the next word's start in continuous speech; clamped back).
- Render: cd remotion-captions-test && npx remotion render Boxed out/ep008-boxed-tmp.mp4
  --props '{"accent":"#F59E0B"}' --browser-executable <chrome-headless-shell-131>
  --concurrency=2 --crf=18 (exit 0, 269s, 16MB, vdur 28.70s; log: edit/build1k/render.log;
  temp file verified by exit code + fresh timestamp + probed duration before use;
  no title card, no punch-in zoom)
- !!! RENDER DEFECT FOUND + FIXED (2026-11-21): the full concurrency-2 render above
  went BLACK from ~13.7s (frame ~413) to the end — exit 0, 861/861 frames encoded,
  no error in its log. Frame-mean probes: assembly fine everywhere (111-125),
  boxed 0.0 from 13.8s on. A retry of frames 287-573 at concurrency 2 ABORTED at
  frame 341 with the smoking gun in its log: "Browser failed to load blob:...
  (Image): net::ERR_OUT_OF_MEMORY" / "EncodingError: The source image cannot be
  decoded" — headless Chrome ran out of memory loading video frames (OffthreadVideo
  blob). A 31-frame test render (400-430) at concurrency 2 was fine, proving the
  failure is stateful (memory accumulates over a long session), not a bad frame.
  ep006's 840-frame concurrency-2 render did NOT hit this (memory conditions vary).
- FIX (applied, verified): re-rendered in 3 chunks with --concurrency=1 --muted:
  out/ep008-boxed-A.mp4 frames 0-286, out/ep008-boxed-B.mp4 frames 287-573,
  out/ep008-boxed-C.mp4 frames 574-860 (287 frames each, ~2 min each, all exit 0).
  Chunk B verified non-black at comp 13.7/14.0s (mean 111.6) before proceeding.
  Concatenated video-only (concat filter, crf 18) + muxed with assembly-norm audio
  -> replaced out/ep008-boxed-tmp.mp4 (26MB, 28.70s). Verified non-black at all 7
  mids, both chunk boundaries (9.5/9.6s, 19.0/19.2s) and the 13.7s region.
  Chunk logs: /tmp/ep008-master/chunkA.log, chunkB1.log, chunkC.log.
  LESSON for future renders on this VM: use --concurrency=1 for 1080x1920 caption
  renders; if a full render goes black mid-way, check frame means (exit 0 proves
  nothing) and re-render in <=287-frame chunks at concurrency 1.
- Remotion: @remotion/cli ^4.0.0, template remotion-captions, Boxed composition,
  1080x1920, 30fps (meta.json).

## Stage 3 laugh — RERUN (first attempt crashed)
- Crash cause: numpy full-track allocated at nominal 28.6s (1372800 samples) but the
  boxed audio is 28.672s (1376256 samples) -> broadcast ValueError. Fix in stage3_only.py:
  total = len(dlg)/SR (actual boxed-audio duration). No re-render needed (boxed tmp intact).
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix over sh070, audible onset 25.7s (0.1s into the
  reaction shot), stem_start=25.44s, laugh ends 27.54s < 28.67s.
- NO freeze-frame tail (ep006 stage1 pattern has none; laugh fits inside the video).
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.
- FLAG: laugh-over-sh070 placement is the series pattern but the user has NOT
  explicitly confirmed it for ep008 — he can say remove.

## QC
- ffprobe final: see script output above (1080x1920, 30fps, ~28.67s, AAC 48kHz stereo).
- Energy per shot + sh070 laugh-zone buckets: see script output above.
- Contact sheet: edit/build1k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: see script output above (record only; script words govern captions).
