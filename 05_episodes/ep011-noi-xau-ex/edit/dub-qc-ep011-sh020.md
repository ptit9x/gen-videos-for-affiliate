# ep011 — QC lồng tiếng clone ThaoMyVeo (sh020)

Ngày: 2026-11-24. Phương pháp: wordalign (như ep008/ep009/ep010, Richard duyệt 21/11).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep011_dub_thaomy.py` (session ep011-dub),
wav gốc: `~/workspace/colab-t4-test/ep011-dub/thaomy-ep011-sh020.wav` (5.20s, 48kHz mono).
Build: `edit/build_wordalign_sh020.py` (native windows đo bằng energy envelope
48kHz stereo 0.05s + Whisper word timestamps; TTS spans đo bằng Whisper trên wav clone).
Lý do lồng: giọng native sh020 take001 KHÔNG phải Bắc (tai Richard, 09:24 24/11).

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh020 | `generated/sh020-take001-dubbed.mp4` | "Thường anh ghê, chắc của đó không sướng với anh. Rồi trước đó." — 13/13 từ, đúng thứ tự, đúng 3 cửa sổ; "của"≈cô, "sướng"≈xứng là nhầm đồng âm của Whisper trên audio đã stretch (wav clone gốc nghe "cô đó không sửng" — cũng chỉ lệch mỗi "xứng") | 1.0-1.9 / 2.8-4.2 / 5.85-6.65, khớp đúng 3 cửa sổ native | ĐẠT |

## Chi tiết kỹ thuật

- 3 cụm stretch theo cụm (không theo từng từ Whisper — biên từ Whisper trong cụm
  nhiễu): P1 0.989x, P2 0.737x, P3 0.952x. Tất cả trong khoảng đã chứng minh của ep009 (0.60x–1.70x).
- CHỈNH CỬA SỔ so với đo ban đầu: Whisper smear từ đầu cụm 1 sớm 0.4s
  ("Thương" 0.6s) — energy 0.05s từng kênh cho thấy ambient tới 1.00s, thoại bắt
  đầu ~1.02s; tương tự cụm 2 bắt đầu 2.80s (không phải 2.64s), cụm 3 bắt đầu
  5.85s (không phải 5.72s). Dub đặt theo cửa sổ energy: 1.00-1.90 / 2.80-4.20 /
  5.85-6.65. Xem `edit/sh020-native-windows.md`.
- Video copy nguyên từ bản 1K take001 (720x1280, 7.93s), audio thay hoàn toàn bằng
  track clone mono 48kHz AAC 192k — tiếng gốc Veo tắt hẳn (bằng chứng: track
  lồng là mono 1 kênh trong khi native là stereo, và năng lượng ngoài cửa sổ
  cụm = 0.000 tuyệt đối với đuôi 0.1s; không đuôi 0.1s thì chỉ còn 2 bucket biên
  — 5.8s RMS 0.0017 do onset 5.85 nằm giữa bucket, 4.2s RMS 0.0001 dư AAC — không
  bed nền, không rò).
- sh040 GIỮ NGUYÊN tiếng gốc Bắc, không đụng vào. Take gốc sh020-take001.mp4
  không bị ghi đè (sha vẫn 3bb1a1b8...).
- Lip-sync: đặt theo phương pháp wordalign đã duyệt ở ep008/ep009/ep010; tai Richard
  là người chốt cuối.
- sha256 bản lồng: ab4cd7f3e3a5729f152bae6d9c6dccb21e80517b25c71f4902b914ed58824220
