# ep001 rev4 — Manifest dựng (Ubuntu VM, 2026-11-16)

- Master: `delivery/ep001-rev4-master.mp4` — 1080×1920, 30 fps CFR, H.264 yuv420p, AAC-LC 48 kHz stereo, 15.90s (khóa 15.867 = 7.933 + 7.933, hard cut, không overlap). Phụ đề: `delivery/ep001-rev4.srt` (sidecar, 4 cue, canh theo audio lồng tiếng).
- Loudness master: −13.58 LUFS integrated, true peak −1.03 dBTP (loudnorm I=−14/TP=−1 áp khi dựng).

## Nguồn
| Shot | Frame đầu (đã duyệt 16/11) | Clip Flow | File VM | Thoại |
|---|---|---|---|---|
| sh010 | input/frames/sh010-frame-local-v001.png (sha d5fe6a90…) | `726e3f32-bcaf-4128-891f-c5a00d745b03` “Woman tidying desk with notebook” | clips/sh010-take001.mp4 (720×1280, 24fps, 7.93s) | Dọn xong cái bàn này, tôi sẽ tập trung làm việc! |
| sh020 | input/frames/sh020-frame-local-v001.png (sha 47699cd7…) | `bd0d0ba7-cfb2-4164-a47c-361ca581dfc5` “Woman speaking Vietnamese at desk” | clips/sh020-take001.mp4 (720×1280, 24fps, 7.93s) | Bàn gọn rồi. Đầu óc cũng trống luôn. Mai làm vậy. |

- Gen: Cloud Browser, Flow project 2948266f-ba05-481e-b636-4ebe81db52ba, Frames trực tiếp, TẮT Agent, Veo 3.1 Lite, 9:16, 8s, 1 output, prompt nguyên văn từ input/prompts/sh0X0-motion.txt (KHÔNG chèn khối giọng tăng cường — Henry chưa gật). Mỗi shot 1 lượt, 10 credit; số dư 50 → 40 → 30. Sáng 16/11/2026.
- Nhận diện: frame tĩnh local (rung 3 của thang neo: frame đã duyệt) — mặt mới v001 + body v003 qua ảnh frame.

## Âm thanh
- Tắt toàn bộ tiếng Veo. Lồng VieNeu preset **Đoan Trang**: audio/doan-trang-sh010.wav (2.96s) đặt tại 0.400s; audio/doan-trang-sh020.wav (3.52s) đặt tại 8.300s. Vị trí câu con trong sh020 đo bằng silencedetect: 0–0.941 / 1.251–2.347 / 2.866–3.520.

## Lệnh dựng (tóm tắt)
1. Chuẩn hoá: `ffmpeg -i clip -vf "scale=1080:1920:flags=lanczos,fps=30,setsar=1,format=yuv420p" -r 30 -fps_mode cfr -c:v libx264 -crf 18 -an` → build/n1.mp4, n2.mp4.
2. Master: concat filter n=2 (video) + amix 2 dub (adelay 400 / 8300 ms, apad 15.867) + loudnorm I=-14:TP=-1:LRA=11 → AAC 48 kHz.

## QC
- clip_qa.py master: `ok` — onset 0.50s; A/V lệch −0.033s; **sync_r = 0.02 < 0.3 → điểm đồng bộ môi KHÔNG kết luận được** (không được báo là khớp môi; cần tai/người nghe kiểm chứng).
- qc_delivery.py: decode_ok = true; SRT 4 cue, 0 lỗi; đúng canvas/fps/codec.
- Eyes gate (frame giữa mỗi clip + quanh điểm cắt): mặt ổn định đúng mặt mới; bàn bừa cả hai clip; hard cut rơi đúng setup deadpan.
- Lệch đã biết: (1) sh010 — thay vì kéo sổ tại chỗ, nhân vật nhấc sổ đặt lên laptop giữa bàn (vẫn chỉ dọn 1 món, bàn vẫn bừa); (2) sh020 — cuối clip tay rời mép bàn xuống lòng và mắt khép ở ~0.4s cuối (nhịp “buông xuôi”, không dọn thêm gì); (3) sổ ở sh020 nằm lại bên trái (frame sh020 dựng từ frame gốc, không nối tiếp vị trí sổ cuối sh010); (4) watermark “Veo” góc dưới phải trên cả hai clip (Flow ép, đã biết từ trước).
- Đồng bộ về repo Mac: HOÀN TẤT sáng 16/11 khi Mac bật lại — clip vào generated/sh010/take003.mp4 + generated/sh020/take002.mp4, master + .srt vào delivery/, episode.yaml đã cập nhật (approved_for_generation: true, frame_status: approved, 2 take needs_review, editorial_status: qc) và validate KHỚP episode.schema.json; edit/manifest.yaml đã điền (locked 15.9s, selected takes, lip_sync_qc: inconclusive). Bản ghi này nằm tại prep/rev4-production-record.md trong repo.
- KHÔNG đăng ở đâu — chờ Henry QC và ra lệnh.
