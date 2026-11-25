# ep012 master 1K PREVIEW r05 — build report

## Change vs v1
- Script r05 (commit b5295b6): sh020 line changed to "Mấy tỷ thì kệ anh, em uống
  ly cà phê ba mươi ngàn, anh đừng lo." (16 words, was 15) — Richard 20:21 25/11.
  sh020 re-dubbed with clone ThaoMy wordalign (edit/build_wordalign_sh020_r05.py,
  QC passed, sha 963882b5…). All other shots, trims, crop, captions style, laugh
  placement unchanged. Total script words 47 (was 46).

## Outputs
- Final: `delivery/ep012-master-1k.mp4` sha256 `12c9b33e334b41a2b4cb12993e8ba7f60f045403ce1e00e82dda711df2cea3f6`
- SRT: `delivery/ep012-subtitles.srt` (4 cues, UTF-8)
- Script: `edit/build_master_1k.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build1k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, qc/ mids + cut frames)
- Remotion inputs backed up to: `/home/hatch/workspace/remotion-captions-test/public-ep011-2k-backup-3` (the ep011 2K inputs)

## Sources (all 720x1280 1K, accepted by Richard 2026-11-25 17:31)
- sh010 generated/sh010-take001.mp4 (native, Hùng, accepted, no dub) — trim 0-3.4s
- sh020 generated/sh020-take004-dubbed.mp4 (clone ThaoMy wordalign, r05 line, sha 963882b5…) — trim 0-5.5s
- sh030 generated/sh030-take002.mp4 (native, Hùng, accepted, no dub) — trim 0-4.7s
- sh040 generated/sh040-take003-dubbed.mp4 (clone ThaoMy wordalign) — trim 0-7.0s
- Nominal total 20.60s; actual final 22.51s (laugh + freeze tail).
  Bounds: {'sh010': (0.0, 3.4), 'sh020': (3.4, 8.9), 'sh030': (8.9, 13.600000000000001), 'sh040': (13.600000000000001, 20.6)}

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,crop=640:1138:40:0,scale=720:1280:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[3:v][3:a]concat=n=4:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {'sh010': 3.4, 'sh020': 5.5, 'sh030': 4.7, 'sh040': 7.0}

## Crop decision
- Veo sparkle + "Veo" text verified present BOTTOM-RIGHT on ALL FOUR 1K files
  (corner crops x600-720/y1150-1280 at t=2.5s: star top ~y1160, "Veo" text
  ~y1250-1267).
- Crop crop=640:1138:40:0 = x 40..680, y 0..1138, then lanczos to 720x1280. Icon top edge
  ~22px below the crop line. One uniform crop so framing/scale matches across
  hard cuts. (The 2K crop 960:1707:60:0 scaled by 2/3.)

## Trims (measured, not guessed — Whisper base + 48kHz energy envelope + 1fps frames)
- sh010 native speech 1.08-2.62s (energy loud 1.4-2.6s) -> 3.4s (beat 0.78s;
  watch-point gesture completes as his hand lowers to the table ~3.4s; the
  glass-drink at ~6-7s is Veo tail motion, cut)
- sh020 dubbed speech clusters 1.02-1.90 / 2.40-4.05 / 4.56-5.18 -> 5.5s
  (beat 0.32s; polite smile hold; cup-lowering at ~6-7s is tail, cut)
- sh030 native speech 0.90-4.34s -> 4.7s (beat 0.36s; bill push done ~3s,
  settled hand-on-folder; remaining 3.2s is static hold, cut)
- sh040 dubbed speech clusters 3.14-4.48 / 5.14-6.70 -> 7.0s (beat 0.30s;
  deadpan hold; HEAD 0-3.14s cup-down + smile-fade action untouched)

## Stage 2 captions (Remotion Boxed, NO title card)
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. 47 words.
- Alignment fixes (same pattern as ep011's sh030 fix):
  - sh020 r05: "ba mươi ngàn" heard as "30" + ".000" (15 heard vs 16 script) —
    split the "30" span into "ba"/"mươi", map ".000" to "ngàn". Fallback: "30.000"
    as one token (14 heard) is split into "ba"/"mươi"/"ngàn".
  - sh040: "limited" heard as "lim" + "tế" — merged into "limited" spanning both.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep012-boxed-1k-chunk<N>.mp4 --props '{"accent":"#F59E0B"}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: [(0, 286), (287, 573), (574, 620)] (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep012-boxed-1k-tmp.mp4.
- Caption problems (if any): see edit/build1k/captions-PROBLEMS.txt.

## Stage 3 laugh (Laugh Track 1 after the sh040 punchline)
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix (NO adelay — the one-channel-leak lesson) right after the
  sh040 punchline, audible onset 20.67s (last word ends
  20.52s + 0.15s), stem_start=20.41s, laugh ends 22.51s.
- Freeze-frame tail 1.81s (still of the last frame, ep004 pattern) so
  the laugh fits; video itself ends at 20.70s.
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.

## QC
- ffprobe final: see script output above (720x1280, 30fps, AAC 48kHz stereo).
- Frame means: see script output above (black = mean ~0).
- Energy per shot + laugh-zone buckets: see script output above.
- Laugh per-channel: see script output above (RMS L/R ratio, L-R/L+R, envelope correlation).
- Contact sheet: edit/build1k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Whisper transcript of final: 46 words heard (script: 47) — see script output above.
- SRT matches script exactly (asserted in-script).
