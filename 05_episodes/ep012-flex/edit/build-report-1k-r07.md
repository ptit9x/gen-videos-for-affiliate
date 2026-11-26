# ep012 master 1K PREVIEW r07 — build report

## Change vs r06
- ONLY change: title card "FLEX" added (Richard 07:25 26/11 approved the r06
  master and chose "FLEX" over "XE MẤY TỶ"). Remotion TitleCard, ep004/ep008
  style (src/TitleCard.tsx, wired into CaptionedVideo via title/titleSeconds
  props), props {"accent": "#F59E0B", "title": "FLEX", "titleSeconds": 2} —
  overlay on sh010 for the first 2s (master time 0–2s), top band. All takes,
  trims, crop, captions, laugh, loudnorm identical to r06. Total script words
  47 (unchanged). Title card is a graphic overlay, NOT a caption — not in SRT,
  no dialogue change.

## Outputs
- Final: `delivery/ep012-master-1k.mp4` sha256 `c2b0abec4da100b1c39516b919391d80f70a1bef0de0264e17aedb22172129e8`
- SRT: `delivery/ep012-subtitles.srt` (4 cues, UTF-8)
- Script: `edit/build_master_1k_r07.py` (this file, stages 1-3 + QC)
- Work dir: `edit/build1k/` (segments, assembly, bounds.json, captions-PROBLEMS.txt,
  render-chunk*.log, qc-contact.png, qc/ mids + cut frames)
- Remotion inputs backed up to: `/home/hatch/workspace/remotion-captions-test/public-ep011-2k-backup-5` (the ep011 2K inputs)

## Sources (all 720x1280 1K, accepted by Richard 2026-11-25 17:31)
- sh010 generated/sh010-take001.mp4 (native, Hùng, accepted, no dub) — trim 0-3.4s
- sh020 generated/sh020-take005-dubbed.mp4 (clone ThaoMy wordalign, take005, sha 60f66835…) — trim 0-5.3s
- sh030 generated/sh030-take002.mp4 (native, Hùng, accepted, no dub) — trim 0-4.7s
- sh040 generated/sh040-take003-dubbed.mp4 (clone ThaoMy wordalign) — trim 0-7.0s
- Nominal total 20.40s; actual final 22.14s (laugh + freeze tail).
  Bounds: {'sh010': (0.0, 3.4), 'sh020': (3.4, 8.7), 'sh030': (8.7, 13.399999999999999), 'sh040': (13.399999999999999, 20.4)}

## Stage 1 commands (per segment)
ffmpeg -i <source> -vf "trim=0:<T>,setpts=PTS-STARTPTS,crop=640:1138:40:0,scale=720:1280:flags=lanczos,fps=30"
  -af "atrim=0:<T>,asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
  -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a aac -b:a 192k -t <T> seg-<sh>.mp4
Concat: filter_complex "[0:v][0:a]...[3:v][3:a]concat=n=4:v=1:a=1[v][a]" (FILTER, never demuxer+copy)
Loudnorm: loudnorm=I=-15.5:TP=-1.0:LRA=11, video copy.
Segment durations measured: {'sh010': 3.4, 'sh020': 5.3, 'sh030': 4.7, 'sh040': 7.0}

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
- sh020 dubbed speech clusters 0.91-1.99 / 2.41-3.99 / 4.29-4.91 -> 5.3s
  (beat 0.39s; polite smile hold; cup-lowering/drinking at ~6.0s is tail, cut)
- sh030 native speech 0.90-4.34s -> 4.7s (beat 0.36s; bill push done ~3s,
  settled hand-on-folder; remaining 3.2s is static hold, cut)
- sh040 dubbed speech clusters 3.14-4.48 / 5.14-6.70 -> 7.0s (beat 0.30s;
  deadpan hold; HEAD 0-3.14s cup-down + smile-fade action untouched)

## Title card ("FLEX", ep004/ep008 style)
- Reused the existing Remotion TitleCard (src/TitleCard.tsx, already wired into
  CaptionedVideo via title/titleSeconds props) — NOT rebuilt. Render props:
  {"accent": "#F59E0B", "title": "FLEX", "titleSeconds": 2}.
- Style (from TitleCard.tsx): Inter 900, fontSize width*0.115 (~83px at 720w),
  white fill + black stroke (max 4px) + textShadow, uppercase, centered,
  marginTop height*0.09 (~115px at 1280h), accent underline bar (width*0.22,
  accent #F59E0B) below the text; spring enter + fade-out in last 8 frames.
  Title occupies roughly y115–260 at 720x1280 (top band, clear of the Boxed
  captions lower down). Verified on frames 0.5/1.5s (edit/build1k/qc/final-title-*.png)
  — see QC notes below.

## Stage 2 captions (Remotion Boxed + TitleCard "FLEX")
- Whisper base word timestamps RE-RUN on the assembly audio, aligned to script
  words IN ORDER, energy-refined, clamped to shot bounds. 47 words.
- Alignment fixes (same pattern as ep011's sh030 fix):
  - sh020 r05: "ba mươi ngàn" heard as "30" + ".000" (15 heard vs 16 script) —
    split the "30" span into "ba"/"mươi", map ".000" to "ngàn". Fallback: "30.000"
    as one token (14 heard) is split into "ba"/"mươi"/"ngàn".
  - sh040: "limited" heard as "lim" + "tế" — merged into "limited" spanning both.
- Render: cd remotion-captions-test && npx remotion render Boxed
  out/ep012-boxed-1k-chunk<N>.mp4 --props '{"accent":"#F59E0B","title":"FLEX","titleSeconds":2}'
  --browser-executable <chrome-headless-shell-131> --concurrency=1 --crf=18
  --frames <chunk range> --muted. Chunks: [(0, 286), (287, 573), (574, 614)] (<=287 frames each — the
  full-render-at-concurrency-2 lesson: exits 0 but goes BLACK from ~13.7s,
  Chrome OOM). Each chunk verified (exit code + size + duration + mean frame
  at chunk middle) before use. Video-only chunks concatenated, then muxed with
  assembly-norm audio -> out/ep012-boxed-1k-tmp.mp4.
- Caption problems (if any): see edit/build1k/captions-PROBLEMS.txt.

## Stage 3 laugh (Laugh Track 1 after the sh040 punchline)
- Laugh Track 1: ~/workspace/laugh-sfx/final/laugh-track-1-ccby.mp3 (2.1s,
  Freesound LittleRainySeasons, CC BY — attribution required in descriptions).
- Placement: numpy mix (NO adelay — the one-channel-leak lesson) right after the
  sh040 punchline, audible onset 20.30s (last word ends
  20.15s + 0.15s), stem_start=20.04s, laugh ends 22.14s.
- Freeze-frame tail 1.64s (still of the last frame, ep004 pattern) so
  the laugh fits; video itself ends at 20.50s.
- Final loudnorm I=-15.5:TP=-1.0:LRA=11, aresample=48000, video copy.

## QC
- ffprobe final: see script output above (720x1280, 30fps, AAC 48kHz stereo).
- Frame means: see script output above (black = mean ~0).
- Energy per shot + laugh-zone buckets: see script output above.
- Laugh per-channel: see script output above (RMS L/R ratio, L-R/L+R, envelope correlation).
- Contact sheet: edit/build1k/qc-contact.png (row1 mids, row2 cut frames) — inspect visually.
- Title frames: edit/build1k/qc/final-title-0.5.png, final-title-1.5.png — "FLEX" visible,
  upper band, clear of the character's head; check what it covers in sh010 (face/watch/keys).
- Whisper transcript of final: 46 words heard (script: 47) — see script output above.
- SRT matches script exactly (asserted in-script).
