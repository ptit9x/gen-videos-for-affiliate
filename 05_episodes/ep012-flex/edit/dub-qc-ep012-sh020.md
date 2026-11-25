# ep012 — QC lồng tiếng clone ThaoMyVeo (sh020)

Ngày: 2026-11-25. Phương pháp: wordalign (như ep008/ep009/ep010/ep011, Richard duyệt 21/11 + 24/11).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep012_dub_thaomy_sh020.py` (session ep012-dub),
wav gốc: `~/workspace/colab-t4-test/ep012-dub/thaomy-ep012-sh020.wav` (5.36s, 48kHz mono).
Build: `edit/build_wordalign_sh020.py` (native windows đo bằng energy envelope
48kHz stereo 0.05s + 0.02s fine buckets; TTS spans đo bằng Whisper trên wav clone).
Lý do lồng: Richard 17:31 25/11 chốt lồng clone ThaoMy wordalign cho cả 2 shot My.

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh020 | `generated/sh020-take004-dubbed.mp4` | "Dạ hay quá anh, em muốn đi cả phê 30 ngựa, anh đừng lắm" — 14/15 từ đúng thứ tự, đúng 3 cửa sổ; "uống"→"muốn", "lo"→"lắm" là nhầm đồng âm/thanh điệu của Whisper trên audio đã stretch (wav clone gốc nghe đúng "uống" và "lo"); "ly"→"đi", "ngàn"→"ngựa" cũng là artifact ASR đã thấy trên wav gốc | 1.02-1.90 / 2.40-4.05 / 4.56-5.18, khớp đúng 3 cửa sổ native | ĐẠT |

## Chi tiết kỹ thuật

- 3 cụm stretch theo cụm (không theo từng từ Whisper — biên từ Whisper trong cụm
  nhiễu): P1 0.746x, P2 0.809x, P3 1.069x. Tất cả trong khoảng đã chứng minh của ep009 (0.60x–1.70x).
- CHỈNH CỬA SỔ so với đo ban đầu: Whisper smear từ đầu cụm 1 sớm ~0.3s
  ("Dạ" 0.76s) và cụm 3 sớm 0.32s ("anh" 4.24s) — energy 0.02s cho thấy thoại
  bắt đầu 1.02s và 4.56s; dub đặt theo cửa sổ energy: 1.02-1.90 / 2.40-4.05 /
  4.56-5.18. Xem `edit/sh020-native-windows.md`.
- Video copy nguyên từ bản 1K take004 (720x1280, 7.93s; framemd5 video
  IDENTICAL với bản gốc), audio thay hoàn toàn bằng track clone mono 48kHz
  AAC 192k — tiếng gốc Veo tắt hẳn (bằng chứng: track lồng là mono 1 kênh
  trong khi native là stereo, và năng lượng ngoài cửa sổ cụm = 0.000 tuyệt
  đối; không bed nền, không rò).
- Take gốc sh020-take004.mp4 không bị ghi đè (sha vẫn 34cd488a...).
- Lip-sync: đặt theo phương pháp wordalign đã duyệt ở ep008/ep009/ep010/ep011; tai Richard
  là người chốt cuối.
- sha256 bản lồng: 82f3da86dd10d9a867a77eeb6f27249f6023988f864e4d79612252494584e24b
