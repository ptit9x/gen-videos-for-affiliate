# ep013 — QC lồng tiếng clone NamVeo (sh020 take001, video CÂM 8.00s)

Ngày: 2026-11-27. Phương pháp: wordalign (như ep008/ep009/ep010/ep011, sh010/sh050 ep013).
Clone: NamVeo, VieNeu v3 Turbo trên Colab T4, enroll từ audio gốc sh040 take001
(Nam nói thật "Ừm... dễ thương!" lặp 2 lần — lấy cả file làm mẫu giọng; tiền lệ
ghi sẵn trong work-log 27/11).
Script Colab: `~/workspace/colab-t4-test/ep013_dub_nam_sh020.py` (session ep013-dub-nam, T4),
wav gốc: `~/workspace/colab-t4-test/ep013-dub/nam-ep013-sh020.wav` (0.96s, 48kHz mono).
Build: `edit/build_wordalign_sh020.py`.
Lý do lồng: take001 là video Veo thật nhưng CÂM (không có audio stream); 10 lần
gen lại sau đó đều lỗi audio trên Flow + hết credit. Richard 16:36 27/11 hỏi
pipeline của Bee có gen được video không + "làm nốt cho tao" → cứu take001
bằng dub (video Flow sẵn có, chỉ thêm tiếng), KHÔNG phải gen video mới bằng
pipeline (video AI của Bee bị chặn 403 từ 23/10, không gen được clip người thật).

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Cửa sổ đặt tiếng | Kết luận |
|---|---|---|---|---|
| sh020 take001 (câm, 8.00s) | `generated/sh020-take001-dubbed.mp4` | "dễ thương" — 2/2 từ, đúng 1 lần, đúng cửa sổ | 0.15-0.85s, khớp lúc miệng há to nhất (frame 0s/1s há to, 1s giơ 2 tay nắm đấm); sau đó Nam cười không tiếng 7s còn lại | ĐẠT (chờ Richard nghe chốt giọng Nam) |

## Chi tiết kỹ thuật

- 1 cụm duy nhất, atempo 1.0 (TTS span 0.00-0.65s vừa khít cửa sổ 0.70s).
  Không stretch, không bed nền, không rò (năng lượng ngoài cửa sổ = 0.000
  tuyệt đối; video gốc vốn không có audio stream nên không có gì để tắt).
- Video copy nguyên từ take001 (720x1280, 8.00s, 24fps), audio = track clone
  mono 48kHz AAC 192k.
- Take gốc sh020-take001.mp4 không bị ghi đè.
- Lip-sync: đặt theo miệng há to 0-2s (xem frame 0s/1s/2s); tai Richard là
  người chốt cuối — cả giọng (có giống Nam/giọng Bắc không) lẫn khớp môi.
- sha256 bản lồng: 51810b3bcc61672d565b7393d185bcfa095113f6cd21435324ac4f4da39df88b
