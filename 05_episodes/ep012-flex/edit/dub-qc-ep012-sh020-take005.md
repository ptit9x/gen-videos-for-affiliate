# ep012 — QC lồng tiếng clone ThaoMyVeo (sh020) — take005

Ngày: 2026-11-26. Phương pháp: wordalign (như ep008/ep009/ep010/ep011 + ep012 r03/r05).
Clone: ThaoMyVeo, VieNeu v3 Turbo trên Colab T4, enroll từ ref-clip2.wav
(`/home/hatch/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav`).
TTS wav TÁI DÙNG từ r05: `~/workspace/colab-t4-test/ep012-dub-r05/thaomy-ep012-sh020-r05.wav`
(5.84s, 48kHz mono, sha a64baf42… — đã kiểm tra sha trước khi dùng, KHÔNG chạy Colab mới).
Build: `edit/build_wordalign_sh020_take005.py` (native windows đo bằng energy envelope
48kHz stereo 0.05s + 0.02s fine buckets; TTS spans đo bằng energy trên wav clone).
Lý do lồng: Richard 06:56 26/11 "ok đó, lồng giọng ThaoMy là đc" — take005 gen native
với câu mới r05 nhưng giữ giọng native; chốt lồng clone ThaoMy.

## Kết quả

| Shot | File lồng | Whisper base nghe bản lồng | Onset năng lượng | Kết luận |
|---|---|---|---|---|
| sh020 | `generated/sh020-take005-dubbed.mp4` | "Mấy bỉ thì kể anh, em quống lý cả xe 30.000 anh đừng lâu." — 15 token cho 16 từ đúng thứ tự, đúng 3 cửa sổ; "ba mươi ngàn" nghe thành "30" + ".000" (2 token cho 3 từ, artifact đã thấy ở bản r05); "tỷ"→"bỉ", "kệ"→"kể", "uống"→"quống", "ly"→"lý", "cà"→"cả", "phê"→"xe", "lo"→"lâu" là nhầm đồng âm/thanh điệu của Whisper trên audio đã stretch (wav clone gốc r05 nghe đúng cả 16 từ) | 0.91-1.99 / 2.41-3.99 / 4.29-4.91, khớp đúng 3 cửa sổ native | ĐẠT |

## Chi tiết kỹ thuật

- 3 cụm stretch theo cụm (không theo từng từ Whisper — biên từ Whisper trong cụm
  nhiễu): P1 0.794x, P2 0.786x, P3 0.674x. Tất cả trong khoảng đã chứng minh của ep009 (0.60x–1.70x).
- CỬA SỔ NATIVE ĐO LẠI cho take005 (khác take004 — take005 nói nhanh hơn, thoại
  kết thúc 4.91s thay vì 5.18s): P1 0.91-1.99 / P2 2.41-3.99 / P3 4.29-4.91
  (energy 0.05s + 0.02s fine; Whisper smear đầu cụm như cũ: "Mấy" 0.60s,
  "anh" P3 3.88s — energy là chuẩn). Xem `edit/sh020-take005-native-windows.md`.
- TTS spans đo bằng ENERGY (không dùng Whisper): P1 [0.04-0.62 + 0.90-1.68],
  P2 2.04-4.05, P3 4.55-5.47. Cùng wav và cùng slice như r05 (P2/P3 onset đo lại
  2.04/4.55 thay vì 2.01/4.53 — 0.03s silence đầu slice, không ảnh hưởng).
- ĐIỀU CHỈNH P1 (như r05): clone nói "Mấy tỷ thì" và "kệ anh" thành 2 burst,
  giữa có pause 0.30s (0.62-0.90s trên wav TTS). Đã cắt pause nội cụm
  (2 sub-slice 0.04-0.62 + 0.90-1.68, nối lại = 1.36s) → stretch 0.794x,
  trong khoảng. Pause nằm TRONG một cụm, không đổi thời điểm cửa sổ.
- Video copy nguyên từ bản 1K take005 (720x1280, 7.93s; framemd5 video
  IDENTICAL với bản gốc, 4af9ba31…), audio thay hoàn toàn bằng track clone mono
  48kHz AAC 192k — tiếng gốc Veo tắt hẳn (bằng chứng: track lồng là mono 1 kênh
  trong khi native là stereo, và năng lượng ngoài cửa sổ cụm = 0.000 tuyệt
  đối).
- Peak bản lồng: 0.430, không clip. File: sha 60f66835…

## So với take004-dubbed (r05)
- Cùng wav clone, cùng câu, cùng phương pháp. Khác: cửa sổ native của take005
  (thoại nhanh hơn ~0.3s, kết thúc 4.91s vs 5.18s) nên stretch nhanh hơn
  (0.79/0.79/0.67 vs 0.65/0.81/0.66) — vẫn trong khoảng đã chứng minh.
- Take004-dubbed KHÔNG bị động vào (giữ nguyên trong generated/).
