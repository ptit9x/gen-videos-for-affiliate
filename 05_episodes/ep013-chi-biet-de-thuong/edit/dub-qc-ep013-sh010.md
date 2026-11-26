# ep013 — QC lồng tiếng clone ThaoMyVeo (sh010 take004)

Ngày: 2026-11-26. Phương pháp: wordalign (như ep008/ep009/ep010/ep011, Richard duyệt 21/11).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep013_dub_thaomy_sh010.py` (session ep013-dub),
wav gốc: `~/workspace/colab-t4-test/ep013-dub/thaomy-ep013-sh010.wav` (2.96s, 48kHz mono).
Build: `edit/build_wordalign_sh010.py` (native windows đo bằng energy envelope
48kHz stereo 0.05s + Whisper word timestamps; TTS spans đo bằng Whisper trên wav clone).
Lý do lồng: giọng native take004 KHÔNG đủ Bắc (tai Richard, 20:19 26/11: "giọng thì phải lồng rồi", "lồng ThaoMy ấy").

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh010 take004 | `generated/sh010-take004-dubbed.mp4` | "Anh xem xúc em bộ này thấy sao?" — 8/8 từ, đúng thứ tự, đúng 2 cửa sổ; "xúc"≈giúp là nhầm đồng âm của Whisper trên giọng clone (wav clone gốc nghe "giúp" đúng); "xem" + "thấy sao?" nghe đúng | 0.80-2.24 / 2.25-2.77, khớp cửa sổ native mở rộng (onset Whisper 0.80, đuôi P1 0.09s vào khoảng lặng 2.15-2.25) | ĐẠT (chờ Richard nghe chốt) |

## Chi tiết kỹ thuật

- 2 cụm KHÔNG stretch (atempo 1.0 cả hai — khác ep011 dùng atempo tới 1.357x).
  A/B test 26/11: bản stretch (P1 atempo 1.108, P2 1.04, cửa sổ energy chặt
  0.85-2.15 / 2.25-2.75) bị Whisper nghe sai 4 từ ("Anh sẽ xuống em bộ này
  thứ 3"); bản no-stretch chỉ sai 1 từ đồng âm. Giữ bản no-stretch.
- Video copy nguyên từ bản 1K take004 (720x1280, 7.93s), audio thay hoàn toàn bằng
  track clone mono 48kHz AAC 192k — tiếng gốc Veo tắt hẳn (bằng chứng: track
  lồng là mono 1 kênh trong khi native là stereo, và năng lượng ngoài cửa sổ
  cụm = 0.000 tuyệt đối; không bed nền, không rò).
- Take gốc sh010-take004.mp4 không bị ghi đè.
- Lip-sync: đặt theo phương pháp wordalign đã duyệt ở ep008/ep009/ep010/ep011;
  tai Richard là người chốt cuối.
- sha256 bản lồng: c22890965e437a697a7302078acd7d88d0689536f9461aef6394efb2647fbb00
