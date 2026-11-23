# ep010 — QC lồng tiếng clone ThaoMyVeo (sh020)

Ngày: 2026-11-23. Phương pháp: wordalign (như ep008/ep009, Richard duyệt 21/11).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep010_dub_thaomy.py`,
wav gốc: `~/workspace/colab-t4-test/ep010-dub/thaomy-ep010-sh020.wav` (4.48s, 48kHz mono).
Build: `edit/build_wordalign_sh020.py` (native windows đo bằng energy envelope
48kHz stereo 0.1s + Whisper word timestamps; TTS spans đo bằng Whisper trên wav clone).
Lý do lồng: giọng native sh020 take001 KHÔNG phải Bắc (tai Richard, 09:33 23/11).

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh020 | `generated/sh020-take001-dubbed.mp4` | "Cần 2, 1 tý, giọt này bệnh quá, dũ ín" — "Cần"≈Tuần, "2"≈hai, "1"≈Một, "tý"≈tin, "giọt"≈Dạo, "bệnh"≈bận, "dũ"≈Rồi, "ín"≈im (nhầm đồng âm/số của Whisper trên audio đã stretch; wav clone gốc nghe đúng cả 10 từ) | 0.0-0.7 / 1.6-2.3 / 3.2-4.3 / 5.7-6.4, khớp đúng 4 cửa sổ native | ĐẠT |

## Chi tiết kỹ thuật

- 4 cụm stretch theo cụm (không theo từng từ Whisper — biên từ Whisper trong cụm
  nhiễu, vd "một" native 0.44s nhưng TTS chỉ 0.10s): P1 1.346x, P2 1.667x,
  P3 1.170x, P4 0.875x. Tất cả trong khoảng đã chứng minh của ep009 (0.60x–1.70x).
- Video copy nguyên từ bản 2K (1080x1920, 7.85s), audio thay hoàn toàn bằng
  track clone mono 48kHz AAC 192k — tiếng gốc Veo tắt hẳn (bằng chứng: track
  lồng là mono 1 kênh trong khi native là stereo, và năng lượng ngoài cửa sổ
  cụm = 0.000 tuyệt đối, không bed nền, không rò).
- sh010 + sh030 GIỮ NGUYÊN tiếng gốc Bắc, không đụng vào. Take gốc không bị ghi đè.
- Lip-sync: đặt theo phương pháp wordalign đã duyệt ở ep008/ep009; tai Richard
  là người chốt cuối.
