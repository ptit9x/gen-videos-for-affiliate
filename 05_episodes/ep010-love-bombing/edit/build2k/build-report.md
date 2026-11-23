# ep010 master 2K FINAL — build report

> CORRECTION 2026-11-23 11:30: the script that generated this report was adapted
> from ep009 and its template text still named ep009 sources (sh040, dubbed
> takes, "PROPOSED" laugh). The ACTUAL build used ep010 sources below — verified
> from the stage-1 log lines (sh020 src sha 526e7080 = dubbed file, sh030 src
> sha c542b146 = take002 2K, sh010 with chat overlay). Sections Sources / Crop /
> Trims / Stage 3 header / QC have been corrected by hand; the file itself was
> NOT rebuilt.

## Outputs
- Final: `delivery/ep010-master-2k.mp4` sha256 `780df2bf9fcd57bd008f8f0e5978ca2512ccca20aed32954a037e4a8dfc2378f`
- SRT: `delivery/ep010-master-2k.srt`
- Script: `edit/build_master_2k.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build2k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, mid/cut frames in qc/)
- Remotion inputs backed up to: `/home/hatch/workspace/remotion-captions-test/public-ep009-2k-backup` (the ep009 2K inputs)

## Sources (all TRUE 2K 1080x1920, 7.85s, frame-diff verified vs the approved 1K takes)
- sh010 generated/sh010-take003-1080p.mp4 (native Northern, untouched) — trim 0-6.3s; chat insert edit/chat-insert-sh010.png overlaid 0-2.5s, audio untouched
- sh020 generated/sh020-take001-dubbed.mp4 (clone ThaoMyVeo wordalign, video from 2K + clone audio, native fully replaced) — trim 0-7.1s
- sh030 generated/sh030-take002-1080p.mp4 (native Northern, untouched) — trim 0-7.7s
- Nominal total 21.1s; actual final 21.44s (laugh + freeze tail).
  Bounds: {'sh010': (0.0, 6.3), 'sh020': (6.3, 13.399999999999999), 'sh030': (13.399999999999999, 21.099999999999998)}

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,crop=960:1707:60:0,scale=1080:1920:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[2:v][2:a]concat=n=3:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {'sh010': 6.3, 'sh020': 7.1, 'sh030': 7.7}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on sh010 + sh020 2K
  files (top edge ~y1770, "Veo" text ~y1870-1900, x1020+); sh030 has NO icon
  in that region (full frames at t=2.5/6 also clean).
- Crop crop=960:1707:60:0 = x 60..1020, y 0..1707, then lanczos to 1080x1920. Icon top edge
  ~63px below the crop line. One uniform crop so framing/scale matches across
  hard cuts.

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope)
- sh010 take003 speech 0.0-2.4s + 3.0-5.6s -> 6.3s (chat insert covers 0-2.5s; cut back to her face in the 2.4-3.0s pause)
- sh020 take001 (dubbed) speech 0.0-6.4s -> 7.1s
- sh030 take002 speech 0.0-1.84s + 2.72-6.04s -> 7.7s (keeps the soft eyes-closed smile beat ~7.5s)

## Stage 2 captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep010-boxed-2k-chunk<N>.mp4 --props '{"accent":"#F59E0B"}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: [(0, 286), (287, 573), (574, 635)] (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep010-boxed-2k-tmp.mp4.
- Caption problems: see edit/build2k/captions-PROBLEMS.txt — NOT empty, but only
  alignment notes: Whisper heard 12/13 sh010 words ("em." interpolated,
  5670-6174ms, confidence 0.0) and routine end-time clamps. All 37 script words
  (13+10+14) are in captions.json with sane timing; caption TEXT is the script,
  never Whisper's text.

## Stage 3 laugh (per the approved plan — Laugh Track 1 after the sh030 punchline)
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix right after the sh030 punchline, audible onset
  19.60s (last word ends 19.45s + 0.15s),
  stem_start=19.34s, laugh ends 21.44s.
- Freeze-frame tail 0.24s (still of the last frame, ep004 pattern) so
  the laugh fits; video itself ends at 21.20s.
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.

## QC (verified 2026-11-23 ~11:25, after the rebuild)
- ffprobe final: 1080x1920, 30fps, H.264, AAC 48kHz stereo, 21.44s, 20,865,243 bytes, sha256 780df2bf... (matches Outputs above).
- Loudness: final measures -14.99 LUFS integrated (TP -1.00, LRA 5.80) — in line with ep009 (-14.80).
- Frame means: no black anywhere (t=0.5/2.0 mean ~238 = chat insert; face frames ~108-115; t=21.3 mean 105.5; t>=22.3 no frame, past end).
- Energy per shot: speech in all 3 windows; sh020 shows the wordalign phrase gaps (0.00 outside phrase windows); laugh zone 19.4-21.3s peaks ~0.65 at 19.9-20.5s.
- Whisper transcript of final (record only; homophone artifacts): all 3 dialogues complete in the right windows (0-6.28s, 6.28-11.08s, 12.28-19.76s).
- Visual check (qc-contact.png + frames at 1.0/3.0/6.5/13.6/21.3s): captions Boxed/amber render correctly; cuts clean at 6.3s and 13.4s; chat insert legible; tail freeze holds her soft smile.
- KNOWN WART (flagged to Richard with the master): during the 0-2.5s chat insert the Boxed caption ("TUẦN ĐẦU, NĂM...") sits ON TOP of the chat bubbles and partly covers one bubble. Fix if he wants it: suppress captions 0-2.5s and re-render chunk 0 only.
- First build attempt died ~09:53 (VM replacement killed the background job mid-write; assembly-raw.mp4 corrupt, moov missing). Rebuilt from scratch 11:13-11:24 with `python3 -u` (unbuffered log) via the exec session; exit 0.
