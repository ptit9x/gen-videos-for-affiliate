# ep014 — QC lồng tiếng clone ThaoMyVeo (sh020 take001)

Ngày: 2026-11-28. Phương pháp: wordalign (như ep008/ep009/ep010/ep011/ep012/ep013).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
Script Colab: `~/workspace/colab-t4-test/ep014_dub_thaomy_sh020.py` (session ep014-dub),
v2 phonetic: `~/workspace/colab-t4-test/ep014_dub_thaomy_sh020_phonetic.py`;
wav: `~/workspace/colab-t4-test/ep014-dub/thaomy-ep014-sh020-phonetic.wav` (5.36s, 48kHz mono).
Build: `edit/build_wordalign_sh020.py` (native windows đo bằng energy envelope
48kHz stereo 0.1s + Whisper word timestamps; TTS spans đo bằng Whisper trên wav clone).
Lý do lồng: Richard 10:21 28/11 duyệt take001 nhưng "sh020 cần lồng tiếng"
(giọng native không phải nữ Bắc).

## Vấn đề "Parasite" và cách xử lý

- v1 (text "Parasite"): Whisper base unprompted nghe lộn 6/12 từ
  ("Mà hôm qua M.S.M Film Barocé Thái Lấm, M.S.M.JU"); prompted thì align đủ
  12 từ nhưng xác suất gần 0 ở em/Parasite/hay/chưa — audio mơ hồ thật, không
  chỉ là quirk của Whisper.
- v2 (text "Pa-ra-sai", cách người Việt đọc tên phim): Whisper base unprompted
  nghe đúng 9/12 từ đúng thứ tự ("mà hôm qua em xem phim và giá xài hãy lắm,
  anh xem chưa?") — chỉ tên phim thành 3 âm tiết Việt ("và giá xài"), tai người
  Việt nghe trong ngữ cảnh "xem phim ... hay lắm" sẽ hiểu là "Parasite".
  Script không đổi, chỉ cách viết cho TTS (như tiền lệ Kokoro "sem nye").
- Chốt dùng v2.

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh020 take001 | `generated/sh020-take001-dubbed.mp4` (sha 30c20772…) | "Mà hôm qua, em xin phim và giá xài hãy lắm em xin chưa" — đủ 12 từ đúng thứ tự (xem→xin 2 lần là artifact Whisper trên giọng clone, như ep013 xem→se; Pa-ra-sai→và giá xài; anh→em là bias LM của Whisper trong ngữ cảnh — cùng audio P2 nghe "anh" đúng khi đọc riêng) | P1 0.20-2.95, gap 3.0-3.1, P2 3.20-3.95, khớp cửa sổ native; năng lượng ngoài cửa sổ = 0.000 | ĐẠT (chờ Richard nghe chốt) |

## Chi tiết kỹ thuật

- 2 cụm: P1 atempo 1.425x (ratio 0.70x, trong khoảng ep011 0.60x–1.70x),
  P2 atempo 1.0 (no-stretch, theo A/B ep013). Thử P2 atempo 0.80 trước:
  Whisper vẫn nghe "em xin chưa" như nhau → "anh"→"em" không phải do tempo,
  giữ bản no-stretch.
- Video copy nguyên từ bản 1K take001 (720x1280, 7.93s), audio thay hoàn toàn
  bằng track clone mono 48kHz AAC 192k — tiếng gốc Veo tắt hẳn (track lồng là
  mono 1 kênh trong khi native là stereo; năng lượng ngoài cửa sổ cụm = 0.000
  tuyệt đối; không bed nền, không rò). Không dùng envelope ducking
  (-20dB/-8dB): cách đó để lọt giọng native (giọng bị Richard loại) dưới bản
  lồng; skill dubbing + toàn bộ bản lồng đã duyệt ep008–ep013 đều tắt hẳn.
- Take gốc sh020-take001.mp4 không bị ghi đè.
- Lip-sync: miệng mở rộng ở 0.5s (nguyên âm P1), mím cười ở 3.5s (đuôi "chưa"),
  khớp tiếng; tai Richard là người chốt cuối.
- sha256 bản lồng: 30c2077206f2d56d5b20824b520cfc13068fb03fdd6f1e2451d33bd3330a8e04
