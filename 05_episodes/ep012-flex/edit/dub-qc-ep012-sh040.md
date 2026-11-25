# ep012 — QC lồng tiếng clone ThaoMyVeo (sh040)

Ngày: 2026-11-25. Phương pháp: wordalign (như ep008/ep009/ep010/ep011, Richard duyệt 21/11 + 24/11).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep012_dub_thaomy_sh040.py` (session ep012-dub),
wav gốc: `~/workspace/colab-t4-test/ep012-dub/thaomy-ep012-sh040.wav` (4.16s, 48kHz mono).
Build: `edit/build_wordalign_sh040.py` (native windows đo bằng energy envelope
48kHz stereo 0.05s + 0.02s fine buckets; TTS spans đo bằng Whisper trên wav clone).
Lý do lồng: Richard 17:31 25/11 chốt lồng clone ThaoMy wordalign cho cả 2 shot My;
native take003 "limited"/"bill" nghe không rõ (2/2 round gen).

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh040 | `generated/sh040-take003-dubbed.mp4` | "Đầm hồ lim tế, má chia biểu li cà phê." — 9/9 từ đúng thứ tự, đúng 2 cửa sổ; "Đồng"→"Đầm", "mà"→"má", "ly"→"li" là nhầm thanh điệu của Whisper; "bill"→"biểu" cũng là artifact đã thấy trên wav gốc. **"limited": Whisper nghe thành "lim tế" cả trên wav clone gốc lẫn bản lồng — Whisper base KHÔNG phân biệt được loanword này, nên từ này KHÔNG xác minh được bằng Whisper; tai Richard là người chốt cuối** | 3.14-4.48 / 5.14-6.70, khớp đúng 2 cửa sổ native | ĐẠT (với lưu ý "limited" cần tai Richard) |

## Chi tiết kỹ thuật

- 2 cụm stretch theo cụm (không theo từng từ Whisper — biên từ Whisper trong cụm
  nhiễu): P1 1.288x, P2 0.696x. Tất cả trong khoảng đã chứng minh của ep009 (0.60x–1.70x).
- CHỈNH CỬA SỔ so với đo ban đầu: P1 bắt đầu lấy theo Whisper (3.14s) vì vùng
  3.10-3.48s vẫn cao hơn nền ambient (0.05-0.14 so với 0.02-0.04) — phù hợp
  khởi âm mềm của "Đồng"; P2 bắt đầu lấy theo energy (5.14s, không phải
  5.22s Whisper). Dub đặt theo cửa sổ: 3.14-4.48 / 5.14-6.70.
  Xem `edit/sh040-native-windows.md`.
- Video copy nguyên từ bản 1K take003 (720x1280, 7.93s; framemd5 video
  IDENTICAL với bản gốc), audio thay hoàn toàn bằng track clone mono 48kHz
  AAC 192k — tiếng gốc Veo tắt hẳn (bằng chứng: track lồng là mono 1 kênh
  trong khi native là stereo, và năng lượng ngoài cửa sổ cụm = 0.000 tuyệt
  đối; không bed nền, không rò).
- Take gốc sh040-take003.mp4 không bị ghi đè (sha vẫn 123ae9a2...).
- Lip-sync: đặt theo phương pháp wordalign đã duyệt ở ep008/ep009/ep010/ep011; tai Richard
  là người chốt cuối.
- sha256 bản lồng: c317193c048e7fa80e53e846803643e12ca878a1a883e65630a2bb37b5551fea
