# ep012 — QC lồng tiếng clone ThaoMyVeo (sh020) — r05

Ngày: 2026-11-25. Phương pháp: wordalign (như ep008/ep009/ep010/ep011 + ep012 r03).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep012_dub_thaomy_sh020_r05.py` (session ep012-dub-r05),
wav gốc: `~/workspace/colab-t4-test/ep012-dub-r05/thaomy-ep012-sh020-r05.wav` (5.84s, 48kHz mono, sha a64baf42…).
Build: `edit/build_wordalign_sh020_r05.py` (native windows đo bằng energy envelope
48kHz stereo 0.05s + 0.02s fine buckets; TTS spans đo bằng energy trên wav clone).
Lý do lồng lại: Richard 20:21 25/11 chốt câu mới sh020 (script r05, commit b5295b6)
"Mấy tỷ thì kệ anh, em uống ly cà phê ba mươi ngàn, anh đừng lo." (16 từ) —
câu cũ "Dạ hay quá anh..." bị bắt lỗi ở master 1K: không trả lời câu hỏi về xe,
nhảy từ xe sang cà phê không cầu nối.

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh020 | `generated/sh020-take004-dubbed.mp4` | "Mấy tỷ thì kệ anh, em quống ly cả phê 30.000 anh đừng lâu." — 16/16 từ đúng thứ tự, đúng 3 cửa sổ; "ba mươi ngàn" nghe thành "30" + ".000" (2 token cho 3 từ, artifact đã thấy ở bản r03); "uống"→"quống", "lo"→"lâu" là nhầm đồng âm/thanh điệu của Whisper trên audio đã stretch (wav clone gốc nghe đúng "uống" và "lo") | 1.00-1.85 / 2.40-4.00 / 4.55-5.15, khớp đúng 3 cửa sổ native | ĐẠT |

## Chi tiết kỹ thuật

- 3 cụm stretch theo cụm (không theo từng từ Whisper — biên từ Whisper trong cụm
  nhiễu): P1 0.647x, P2 0.809x, P3 0.660x. Tất cả trong khoảng đã chứng minh của ep009 (0.60x–1.70x).
- CỬA SỔ NATIVE ĐO LẠI cho r05: khớp y hệt bản r03 — P1 1.02-1.90 / P2 2.40-4.05 /
  P3 4.56-5.18 (energy 0.05s + 0.02s fine; Whisper smear đầu cụm như cũ:
  "Dạ" 0.76s, "anh" P3 4.24s — energy là chuẩn). Xem `edit/sh020-native-windows.md`.
- ĐIỀU CHỈNH P1 (ghi rõ, không có trong pattern ep011): clone nói "Mấy tỷ thì" và
  "kệ anh" thành 2 burst, giữa có pause 0.30s (0.62-0.90s trên wav TTS). Lấy slice
  liền mạch 0.06-1.65s (1.59s) vào cửa sổ 0.88s sẽ cho stretch 0.553x — NGOÀI
  khoảng đã chứng minh. Đã cắt pause nội cụm (2 sub-slice 0.04-0.62 + 0.90-1.68,
  nối lại = 1.36s) → stretch 0.647x, trong khoảng. Pause nằm TRONG một cụm, không
  đổi thời điểm cửa sổ.
- TTS spans đo bằng ENERGY (không dùng Whisper): P1 [0.04-0.62 + 0.90-1.68],
  P2 2.01-4.05, P3 4.53-5.47. Whisper smear onset P3 về 4.34s trong khi energy
  cho 4.55s — cùng lỗi smear đã biết, lấy energy làm chuẩn.
- Video copy nguyên từ bản 1K take004 (720x1280, 7.93s; framemd5 video
  IDENTICAL với bản gốc, bc2fb56c…), audio thay hoàn toàn bằng track clone mono
  48kHz AAC 192k — tiếng gốc Veo tắt hẳn (bằng chứng: track lồng là mono 1 kênh
  trong khi native là stereo, và năng lượng ngoài cửa sổ cụm = 0.000 tuyệt
  đối; không bed nền, không rò).
- Take gốc sh020-take004.mp4 không bị ghi đè (sha vẫn 34cd488a...).
- Lip-sync: đặt theo phương pháp wordalign đã duyệt ở ep008/ep009/ep010/ep011; tai Richard
  là người chốt cuối.
- sha256 bản lồng r05: 963882b52f7835c17d1de725f5ff50aef172ef67b008f095282e3ede4a2d6ca5
  (bản r03 cũ: 82f3da86…, giữ trong git history).
