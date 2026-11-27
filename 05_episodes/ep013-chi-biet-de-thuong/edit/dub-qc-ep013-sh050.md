# ep013 — QC lồng tiếng clone ThaoMyVeo (sh050 take003, bản cắt 5.17s)

Ngày: 2026-11-27. Phương pháp: wordalign (như ep008/ep009/ep010/ep011, sh010 ep013).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep013_dub_thaomy_sh050.py` (session ep013-dub, T4),
wav gốc: `~/workspace/colab-t4-test/ep013-dub/thaomy-ep013-sh050.wav` (5.04s, 48kHz mono).
Build: `edit/build_wordalign_sh050.py` (native windows đo bằng energy envelope
100ms + Whisper word timestamps; TTS spans đo bằng Whisper trên wav clone 16kHz).
Lý do lồng: Richard 15:34 27/11: "ok lồng tiếng ThaoMy vào" (sh050 take003).

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh050 take003 (cắt 5.17s) | `generated/sh050-take003-dubbed.mp4` | "Còn bộ quý này thì sao? Anh chỉ biết nói mỗi dễ thương thôi hả?" — 15/15 từ, đúng thứ tự, đúng 2 cửa sổ; "quý"≈cuối là nhầm đồng âm của Whisper trên giọng clone (wav clone gốc cũng nghe "quý" — cần tai Richard chốt "cuối" có rõ không) | P1 0.65-2.01, P2 2.85-5.15, khớp cửa sổ native (P1 0.65-2.05, P2 2.95-5.10, mở rộng 0.10s đầu + 0.05s đuôi); khoảng lặng 2.1-2.8s sạch | ĐẠT (chờ Richard nghe chốt) |

## Chi tiết kỹ thuật

- P1 atempo 1.0 (TTS 1.36s vừa khít cửa sổ native 1.40s); P2 atempo 1.06
  (TTS 2.44s vs cửa sổ native 2.15s — dài hơn nên tăng tốc nhẹ 6% + mở rộng
  cửa sổ 2.85-5.15). Cả hai đều trong vùng stretch đã chứng minh của ep011
  (0.60x-1.70x). LƯU Ý: lần đầu đo Whisper trên wav clone 48kHz đã cho
  timestamp sai (tới 12.96s) vì faster-whisper đọc mảng numpy như 16kHz —
  phải decode về 16kHz trước khi đo; đã đo lại đúng.
- Video copy nguyên từ bản cắt 1K take003 (720x1280, 5.17s), audio thay hoàn
  toàn bằng track clone mono 48kHz AAC 192k — tiếng gốc Veo tắt hẳn (bằng
  chứng: track lồng là mono 1 kênh trong khi native là stereo, và năng lượng
  ngoài cửa sổ cụm = 0.000 tuyệt đối; không bed nền, không rò).
- Take gốc sh050-take003.mp4 (bản cắt) không bị ghi đè.
- Lip-sync: đặt theo phương pháp wordalign đã duyệt ở ep008/ep009/ep010/ep011
  và sh010 ep013; tai Richard là người chốt cuối.
- sha256 bản lồng: 836ef244f894dc8098bb6f14bdce7528ce5a50e65faa56b3466e2ca2988921fc
