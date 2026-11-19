# ep006-hen-ho-voi-ai — work log

## 2026-11-19 — Sửa 3 lỗi review + frame sh010 (Bee)
- Pull remote mới nhất: HEAD `5d66365`, không có commit mới sau 14:44. Bản review là bản viết lại `bd77109`.
- Sửa lỗi 1 — thiếu motion prompt: tạo mới `sh010-motion.txt`, `sh030-motion.txt`, `sh040-motion.txt` (hành động + thoại nguyên văn + giọng nữ miền Bắc + camera tĩnh + không nhạc).
- Sửa lỗi 2 — cụm gây phụ đề giả: bỏ "không phụ đề, không chữ trên hình" khỏi `sh020-motion.txt` và khỏi `script.md` (giữ "không nhạc, camera tĩnh"). Lý do: đã chứng minh cụm nêu tên phụ đề khiến Veo vẽ phụ đề giả nhiều hơn (14/11, 16/11).
- Sửa lỗi 3 — "son đỏ" thoại nhắc mà frame không ghi: thêm "son đỏ" vào `sh010-image.txt`.
- Màu áo linen: Tím nhạt — tạm chốt theo ảnh mẫu để làm frame sh010, chưa chốt chính thức; đã ghi rõ "tạm chốt" trong `script.md` + `wardrobe.md`, và thêm "màu tím nhạt" vào cả 4 image prompt để khớp màu xuyên shot.
- Giọng (Richard 14:55): giữ tiếng Veo gốc nếu giọng Bắc; chỉ lồng clone ThaoMy khi giọng Veo không phải Bắc hoặc Richard chỉ định. Đã sửa mục Hậu kỳ trong `script.md` theo đúng quy tắc này.
- Frame sh010: `input/frames/sh010-first-frame.jpg` (1152×2048, sha256 `d48b7b8d2187b3995984268dfdf84722c8eb0ee37b7e18b0b2c223cd39055899`), gen bằng pipeline ảnh của Bee từ master v002 (`thao-my-body-front-v003-face-v002-review.png`, 1 lần sửa trực tiếp từ master gốc, 0 Flow credit) — KHÔNG phải Flow Nano Banana. Chờ Richard duyệt frame trước khi gen clip.
- Chưa làm: frame sh020/sh030/sh040, episode.yaml, manifest, gen clip.

## 2026-11-19 — Đổi sang váy đen, bỏ áo linen, frame sh010 v2 (Bee)
- Richard: áo linen không hợp bối cảnh nhà hàng tối; hỏi còn màu váy cũ nào chưa lên video. Kiểm kê: kem ep001/ep002, trắng ep003, hồng ep004, xanh dương ep005 đều đã lên video; chỉ còn Đen chưa có clip nào (từng định cho ep001, chỉ có frame tĩnh).
- Đổi ep006: váy hai dây maxi suông SANJOLI màu đen, không áo khoác ngoài — Richard chốt. Bỏ áo linen khỏi script/wardrobe/cả 4 image prompt; aff-0002 giữ trong `affiliate-links.csv` cho tập sau, không còn placement trong ep006.
- Frame sh010 v1 tím (commit `4dcc74d`) đổi tên thành `sh010-first-frame-v1-linen.jpg`, giữ lại làm lịch sử. Frame v2 váy đen làm MỚI 1 lần từ master v002 gốc (không sửa nối từ frame v1), pipeline ảnh Bee, 0 Flow credit: `sh010-first-frame.jpg` (1152×2048, sha256 `cc02928254f59aa10e4d99ce30eac52e99ba39bfdb5fbd28f97d95f1e4a039f5`). Chờ Richard duyệt frame v2 trước khi gen clip.

## 2026-11-19 — Frame sh010 v3: váy lụa đen cổ đổ đúng mẫu (Bee)
- Richard: váy đen v2 chưa giống váy mẫu. Soi ảnh mẫu: váy lụa 2 dây maxi suông, cổ đổ, dây mảnh, suông dài 111cm, vải lụa bóng; v2 cổ tròn, vải mờ như camisole, khung cắt ngang eo nên không thấy độ dài maxi.
- Sửa prompt cả 4 shot + script + wardrobe: "váy lụa ... màu đen, cổ đổ, dây mảnh, dáng suông dài, vải lụa bóng"; ghi nguồn mẫu kem vào wardrobe.md.
- Frame v2 đổi tên thành `sh010-first-frame-v2-black.jpg`, giữ lại. Frame v3 làm MỚI 1 lần từ master v002 gốc + ảnh mẫu kem ngồi làm tham chiếu váy (cùng mẫu đổi sang đen), pipeline ảnh Bee, 0 Flow credit: `sh010-first-frame.jpg` (1152×2048, sha256 `ce0387b144b35b8c778558ab3921828dd682b8b7c6c54e92c58eb008aeef32b4`). Cổ đổ + lụa bóng + tà dài thấy rõ tới gần sàn. Chờ Richard duyệt frame v3.

## 2026-11-19 — Frame sh020/sh030/sh040 (Bee)
- Richard 👍 duyệt frame sh010 v3 → làm tiếp 3 frame còn lại, mỗi frame 1 lần sửa từ master v002 gốc (+ ảnh mẫu kem làm tham chiếu váy khi váy thấy rõ), pipeline ảnh Bee, 0 Flow credit, 1152×2048.
- sh020 v1 lỗi: đeo kính (không có trong prompt), điện thoại đen không thấy ốp, bối cảnh phòng khách — giữ lại `sh020-first-frame-v1-glasses.jpg`. v2 đạt: nhà hàng tối, không kính, ốp trong suốt + vòng MagSafe thấy rõ, cười khẩy. `sh020-first-frame.jpg` sha256 `afc1dc96…`.
- sh030 v1 lỗi: sân thượng ban ngày, áo dài tay có nhãn SANJOLI — giữ lại `sh030-first-frame-v1-outdoor.jpg`. v2 đạt: nhà hàng tối, váy hai dây cổ đổ vai trần, son đỏ, nhìn thẳng camera ánh mắt ấm. `sh030-first-frame.jpg` sha256 `d69c2263…`.
- sh040 v1 đạt ngay: váy lụa đen cổ đổ, cắn bánh cười thoải mái, bàn nhà hàng ấm. `sh040-first-frame.jpg` sha256 `284938b0…`.
- Cả 4 frame ep006 đã đủ, chờ Richard duyệt sh020/sh030/sh040 trước khi gen clip. Chưa làm: episode.yaml ep006, manifest, gen clip.

## 2026-11-19 — episode.yaml + duyệt gen (Bee)
- Richard duyệt sh020/sh030/sh040 → lập `episode.yaml` (4 shot, dialogue khớp script, prompt + frame hash đã tính, frame_status approved, approved_for_generation true) và `edit/manifest.yaml` (audio_plan: giữ tiếng Veo nếu giọng Bắc).
- Validator default exit 0; generation gate chặn đúng kỳ vọng (chưa có Flow project, draft).
- Cập nhật production-tracker.csv: váy đen (không còn kem), 4 frame duyệt, đang gen.

## 2026-11-19 — Gen 4 clip take001 + QC (Bee)
- Project Flow mới: "CNTM · EP006 · Hẹn Hò Với Ai" (https://flow.google.com/project/c9fd3958-630c-47e1-8020-6d1db947a4b1), acc huynhdn Pro. 4 clip Frames-direct Veo 3.1 Lite, 10cr/clip, tổng 40cr, số dư 870 → 830 (reset 16/12). Tải bản 720p về `generated/sh0X0-take001.mp4`, đã kiểm tra file trên disk + ffprobe (7.93s, 720×1280, 24fps, có tiếng).
- QC Whisper base: sh010 đủ thoại 0.00–6.90s; sh020 đủ 3 câu (0.58–1.56, 2.24–3.00, 4.50–5.22 — "à" trong span 2.4–3.0 theo năng lượng 48kHz, đuôi lặng); sh030 đủ từng chữ 0.00–5.96s; sh040 "Là tôi" 4.68–6.90s + tiếng "mmm" 3.28–4.68s trước câu (đang nhai bánh). Cả 4: không phụ đề giả, không bóng ma đuôi (soi frame 4s + 7.5s). Veo watermark góc phải dưới còn nguyên — crop ở khâu dựng.
- Lưu ý: preview Flow của sh020 từng báo "Không tải được video" nhưng file tải về decode bình thường.
- episode.yaml: flow_project + 4 take take001 (status needs_review, file + sha256), editorial_status generating. Validator default exit 0. Chờ Richard duyệt take + nghe giọng từng shot.

## 2026-11-19 16:06–17:07 — sửa continuity ghế + sáng (take002)
- Richard phát hiện: ghế sau lưng 4 clip take001 không giống nhau (sh020 ghế gỗ tối, 3 clip còn lại ghế mây) + sáng sh010/sh040 hơn sh020/sh030. Đo độ sáng trung bình: sh010 63,4 / sh020 51,7 / sh030 65,2 / sh040 71,6.
- Richard chốt: ghế mây đan dễ lỗi, lấy bàn ghế kiểu sh020 (ghế gỗ tối + bàn tròn gỗ) làm chuẩn nền.
- Nền trống v1 (ghế mây, theo sh010) gen xong nhưng BỎ. Nền trống v2 theo sh020 (`input/restaurant-bg-wood.jpg`, 1184×2096, sha c035ab8e…, sáng 55,8) làm chuẩn.
- Frame sh020 v3 pipeline Bee bị Richard chê sai váy đen (dây to + chữ SANJOLI in trên váy). Frame sh010 v4 / sh030 v3 / sh040 v2 pipeline Bee không tạo được (3/4 lỗi) — không thử lại.
- Làm lại cả 4 frame trong Flow (Nano Banana 2.1, 1 edit từ master, 0 credit, 1536×2752) với master + nền gỗ + ảnh mẫu váy SANJOLI: sh010 v4-flow (5b12a656…), sh020 v4-flow (e7eee66f…), sh030 v3-flow (4e8bdbe0…), sh040 v2-flow (ae581a32…). Váy đen đúng mẫu (dây mảnh, cổ đổ, lụa bóng, không logo). Lưu ý: dấu sao Flow góc dưới phải cả 4; sh040 có 2 khách mờ phía sau.
- Richard duyệt cả 4 frame 17:07 → frame cũ đổi tên v3/v2/v2/v1 giữ lại, frame Flow lên tên chuẩn; episode.yaml cập nhật frame + image_prompt sha + flow_image_asset_id + image_sources (nền gỗ, mẫu váy); validator exit 0.
- Đang gen lại 4 clip take002 (Frames-direct, Veo 3.1 Lite, 40cr, số dư 830 → dự kiến 790).

## 2026-11-19 17:07–17:16 — take002 đã gen + QC
- 4 clip take002 gen xong 17:16 (Frames-direct, Veo 3.1 Lite, 40cr, số dư 830 → 790): sh010 d09e4bfd…, sh020 7db77728…, sh030 3846e48c…, sh040 4d889094…. File 720p 7.93s 720×1280 24fps AAC đã về đủ, sha ghi trong episode.yaml.
- QC Whisper base: đủ thoại cả 4 (sh010 0.00-6.32; sh020 3 câu, "à" xác minh bằng năng lượng 48kHz nói liền 3.0-3.3s; sh030 0.00-6.24; sh040 "Là tôi" 4.66-5.38 + cười "Hahaha" 0.00-0.34 đầu clip + "mmm" 3.32-4.08). Không phụ đề giả, không bóng ma đuôi.
- Ghế: gỗ tối cả 4 (soi t=4 + t=7.5). Sáng: 55.7 / 56.0 / 55.1 / 54.9 — chênh ~1 điểm (take001 chênh 20 điểm). Váy đen đúng mẫu cả 4.
- Lưu ý: sh010 đĩa bị khăn ăn phủ giữa clip (do động tác chỉnh khăn); sh040 còn 2 khách mờ phía sau (từ frame); watermark Veo góc dưới phải (crop lúc dựng).
- CHỜ Richard duyệt take002 + nghe giọng từng shot (giữ tiếng Veo nếu Bắc).

## 2026-11-19 18:12–19:29 — sửa son + cổ váy + vòng tay, duyệt frame mới
- Richard phát hiện son lệch (sh010/sh030 đỏ, sh020/sh040 hồng nhạt) + móng lệch (móng đỏ chỉ ở take001 sh010, take002 đều tự nhiên). Nguyên nhân: prompt ảnh sh020/sh040 thiếu "son đỏ đậm"; QC frame sót son + móng.
- Richard chốt móng TỰ NHIÊN cho cả tập. Cổ V ở sh040 v3 KHÔNG đúng mẫu (mẫu thật cổ đổ nhẹ, cong mềm, nếp rủ giữa ngực — đã đối chiếu ảnh mẫu) nên phải sửa lại cổ đổ.
- Frame mới (Flow Nano Banana, 1 edit từ master, 0cr): sh020 v5 (son đỏ) → v6 (bỏ vòng tay; lần 1 bị chặn chính sách, thử lại với prompt tả cổ tay trống thì qua), sh040 v3 (son đỏ, cổ V sai) → v4 (cổ đổ đúng mẫu). Cả 2: son đỏ đậm, móng tự nhiên, mặt/váy/nền khớp.
- 19:29 Richard DUYỆT cả 2 frame. Đã đổi tên chuẩn: sh020-first-frame.jpg = v6 (sha 08323f4f…, Flow 870638e7…), sh040-first-frame.jpg = v4 (sha 554fda21…, Flow a465e73c…). Frame cũ giữ lại tên versioned. episode.yaml cập nhật frame + prompt shas, validator đạt.
- Đang gen lại 2 clip sh020/sh040 take003 (20cr, số dư 790 → 770).

## 2026-11-19 19:29–19:35 — take003 đã gen + QC
- 2 clip take003 gen xong 19:35 (Frames-direct, Veo 3.1 Lite, 20cr, số dư 790 → 770): sh020 7952ed40…, sh040 426dae2e…. File 720p 7.93s 720×1280 24fps AAC đã về đủ, sha ghi trong episode.yaml.
- QC Whisper base + năng lượng 48kHz: sh020 đủ 3 câu (2.24-3.24, 4.1-4.8, 5.7-6.3), "à" xác minh nói liền 4.6-4.8s (Whisper gộp vào từ "tội"); sh040 "Là tôi" 0.00-0.60s (nói ngay đầu clip) + tiếng cười/nhai 4.6-6.0s. Không phụ đề giả, không bóng ma đuôi.
- Son đỏ giữ nguyên trong chuyển động cả 2; sh020 không vòng tay, cổ đổ đúng mẫu; sh040 cổ đổ giữ nguyên. Sáng: sh020 53.5 (hơi tối hơn 3 shot còn lại ~2 điểm, cân bằng lúc dựng), sh040 56.0.
- Bộ take hiện tại: sh010 take002 + sh020 take003 + sh030 take002 + sh040 take003.
- CHỜ Richard duyệt take003 + nghe giọng từng shot (giữ tiếng Veo nếu Bắc); sh010/sh030 take002 vẫn chờ nghe giọng.

## 2026-11-19 20:08–20:10 — phán giọng take003 + lỗi khăn sh010
- Richard nghe 2 clip take003: sh040 giọng Bắc -> giữ tiếng Veo gốc; sh020 giọng Nam -> lồng clone ThaoMy (VieNeu Turbo, clone ThaoMyVeo). Đã ghi vào episode.yaml.
- Richard bắt lỗi sh010 take002: khăn ăn trùm lên đĩa ăn. Lỗi từ frame đầu (prompt ảnh ghi "chỉnh khăn ăn" nên frame vẽ tay + khăn ngay trên đĩa; motion chỉ nối tiếp). take002 REJECTED. Sửa: sh010-image.txt mới (khăn gấp gọn bên trái đĩa, không che đĩa, hai tay đặt trên đùi) + sh010-motion.txt mới (ngồi thẳng, vuốt nhẹ váy, nhìn quanh, không chạm khăn). Làm frame mới từ master (Flow, 0cr) rồi gen lại take003 (10cr).
- Ref clone ThaoMyVeo còn nguyên: ~/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav. Lồng sh020: 3 câu đặt theo cửa sổ miệng native (Q1 2.24s, Q2 4.1s, Q3 5.7s), tắt hẳn tiếng gốc.
- Còn chờ Richard nghe giọng sh030 take002.

## 2026-11-19 20:16 — Richard duyệt sh030 take002
- sh030 take002: giọng Bắc, DUYỆT luôn (giữ tiếng Veo gốc). status accepted_editorial.
- Bộ take hiện tại: sh010 take002 rejected (đang làm frame mới), sh020 take003 chờ lồng clone ThaoMy, sh030 take002 DUYỆT, sh040 take003 giọng Bắc (giữ tiếng gốc, chờ duyệt take).

## 2026-11-19 20:18–20:19 — frame sh010 v5 BỊ LOẠI, gen lại từ frame cũ
- Richard loại frame v5: son đỏ ĐẬM hơn 3 shot kia, nốt ruồi cằm trái MẤT, bàn ghế không đúng. Bee QC frame v5 sót cả 3 điểm (chỉ check "có son đỏ" chứ không so sắc son; không check nốt ruồi; không so đồ đạc với 3 shot kia). Bài học: QC frame phải so son (màu + độ đậm), nốt ruồi, đồ đạc TRỰC TIẾP với các frame đã duyệt của tập, không check lẻ từng ảnh.
- Richard quyết: KHÔNG cần frame mới, gen lại từ ảnh cũ (sh010 v4-flow đã duyệt) với motion prompt mới (không chạm khăn). Đang gen sh010 take003 (10cr, số dư 770 → 760). Frame v5 giữ lại làm lịch sử, không dùng.

## 2026-11-19 20:23 — sh010 take003 vẫn lỗi khăn
- Gen từ frame cũ v4 + motion mới (không chạm khăn), 10cr, số dư 770 → 760, clip f54cfebd….
- QC: đủ thoại 0.00-6.72s, son + cổ đổ + sáng (56.2) đều khớp, không phụ đề giả/bóng ma. NHƯNG khăn vẫn trùm lên đĩa ở t=4 và t=7.5 — motion mới không cứu được vì frame đầu đã vẽ tay + khăn ngay trên đĩa, Veo chỉ đặt khăn xuống đĩa. Kết luận: lỗi nằm ở frame, không sửa được bằng motion. Đề xuất: làm frame mới từ master, khóa chặt theo đúng frame v4 (trung cảnh, bàn tròn gỗ + ghế gỗ tối như cũ, son đỏ sáng, nốt ruồi cằm trái còn) chỉ khác khăn gấp gọn bên trái đĩa + tay trên đùi, rồi gen lại take004. Chờ Richard gật.

## 2026-11-19 20:25 — lồng xong sh020 take003 (clone ThaoMyVeo)
- Clone ThaoMyVeo trên Colab T4 (VieNeu v3 Turbo, enroll ref-clip2.wav; gói pip tên `vieneu`, VM mới phải pip install). 3 câu đặt theo cửa sổ miệng native (Q1 2.24s, Q2 4.10s, Q3 5.70s), chuẩn hoá RMS từng câu, tắt hẳn tiếng gốc Nam.
- File: generated/sh020-take003-dub-thaomy.mp4 (sha fceab9b8…, 7.93s 720p). Bee kiểm chứng độc lập: Whisper nghe đủ 3 câu đúng cửa sổ (sai thanh điệu trên giọng clone — lỗi đã biết của base); năng lượng 0-2.2s và 6.3-7.9s = 0.0000 (không rò tiếng gốc); F0 clone 229-246Hz khớp mẫu enroll 247Hz.
- Lưu ý: Q1 dài hơn miệng gốc 0.33s (tới 3.63s), Q2 dài hơn 0.24s (tới 5.04s) — chưa time-stretch (kéo 1.3×+ sẽ vội giọng; ep004 sh040 từng duyệt với lệch 0.3s tương tự). Chờ Richard nghe tai thật.

## 2026-11-19 20:27 — Richard duyệt bản lồng sh020
- Bản lồng sh020 take003 (clone ThaoMyVeo) DUYỆT — giọng clone ok, không cần kéo nhanh Q1/Q2. take003 status accepted_editorial; bản được duyệt là file lồng (generated/sh020-take003-dub-thaomy.mp4), không phải file gốc.
- Bộ take hiện tại: sh010 chờ frame v6 + take004, sh020 take003 DUYỆT (bản lồng), sh030 take002 DUYỆT (tiếng gốc), sh040 take003 giọng Bắc giữ tiếng gốc (chờ duyệt take).

## 2026-11-19 20:31 — frame v6: 2 lần đều lệch khung hình
- Flow Nano Banana làm frame v6 từ master (prompt khóa theo v4), 0cr, 2 lần đều ra khung RỘNG toàn thân (đầu tới chân, ghế trống nổi bật góc phải, thấy sàn) thay vì trung cảnh như v4 — dù prompt ghi rõ "Trung cảnh, khung hình vừa như ảnh tham chiếu". Cả 2 lần: khăn bên trái đĩa ✓, son đỏ sáng ✓, bàn ghế như cũ ✓; lần 1 nốt ruồi còn rõ, lần 2 nốt ruồi mờ.
- Không đốt thêm lượt sửa (đã 0/3 lần về khung hình: v5 + v6 x2). Cách khác: tải bản lần 1 (05ae1bd2…, nốt ruồi rõ) về crop hậu kỳ đúng khung v4 (cắt đáy + 2 bên, giữ mặt/váy/bàn ghế nguyên — crop là phép biến đổi xác định, không gen lại mặt nên không drift), rồi trình Richard duyệt trước khi gen take004.

## 2026-11-19 20:34 — crop frame v6 về trung cảnh (không gen lại)
- Tải bản v6 lần 1 (05ae1bd2…, 2K, sha 1601f509…) về: khăn ✓, son đỏ sáng ✓, nốt ruồi ✓, bàn ghế ✓ — chỉ khung rộng. Crop hậu kỳ (PIL lanczos): box (150, 0, 1387, 2200) trên ảnh 1536×2752 → resize 1080×1920, file sh010-first-frame-v6-crop.jpg (sha 7ed61229…). Kết quả: trung cảnh đầu tới gối, bàn lớn phía trước, không sàn/chân/ghế nổi bật; vai ~51% bề rộng (khớp sh020/sh040 hơn cả v4 39%). Trình Richard duyệt trước khi gen take004.

## 2026-11-19 20:40 — Richard DUYỆT frame sh010 v6 đã crop
- Frame v6 crop (box 150,0,1387,2200 → 1080×1920, sha 7ed61229…) DUYỆT, thay canonical sh010-first-frame.jpg (v4 giữ nguyên ở sh010-first-frame-v4-flow.jpg). Flow ID 05ae1bd2-913e-45f8-a79c-d5f04867c194. Luminance crop 59.7 (sáng hơn ~4 điểm so với các shot, cân bằng lúc dựng).
- Gen sh010 take004 (Veo 3.1 Lite, 10cr, số dư 760 → 750) với motion prompt đã viết lại (không chạm khăn).

## 2026-11-19 20:44 — sh010 take004 xong, QC đạt (chờ Richard duyệt take + giọng)
- Gen 20:40-20:44, clip fee00309-41d6-4a6a-813c-8cadd19f2852, 10cr, số dư 750. Frame v6 crop (upload thẳng, Frames-direct, Agent OFF, prompt verbatim không chạm khăn).
- QC trên file đã tải về (sha de18da76…): 7.93s 720×1280 24fps; Whisper base nghe đủ 4 cụm 0.00-6.74s; khăn gấp gọn bên trái đĩa ở cả 3 mốc t=1/4/7.5, đĩa nhìn rõ — lỗi khăn ĐÃ HẾT; son/nốt ruồi/cổ đổ khớp; không phụ đề giả, không bóng ma đuôi (sau 7.0s chỉ còn ambience). Sáng 60.0, cao hơn các shot ~4-6 điểm — cân bằng lúc dựng.
- Bộ take: sh010 take004 chờ duyệt, sh020 take003 DUYỆT (bản lồng), sh030 take002 DUYỆT (tiếng gốc), sh040 take003 giọng Bắc giữ tiếng gốc (chờ duyệt take).

## 2026-11-19 21:43 — Richard DUYỆT sh010 take004, giữ tiếng gốc
- take004 status accepted_editorial; giữ tiếng Veo gốc, KHÔNG lồng clone.
- Bộ take hiện tại: sh010 take004 DUYỆT (tiếng gốc), sh020 take003 DUYỆT (bản lồng clone), sh030 take002 DUYỆT (tiếng gốc), sh040 take003 giọng Bắc giữ tiếng gốc (chờ duyệt take) — chỉ còn sh040 là chưa chốt.

## 2026-11-19 22:12 — Richard DUYỆT sh040 take003 — ĐỦ 4 TAKE
- take003 status accepted_editorial; giữ tiếng Veo gốc.
- Bộ take CHỐT: sh010 take004 DUYỆT (tiếng gốc), sh020 take003 DUYỆT (bản lồng clone), sh030 take002 DUYỆT (tiếng gốc), sh040 take003 DUYỆT (tiếng gốc). Bắt đầu dựng master: tải 2K upscale cả 4 take → trim → crop watermark Veo → hard cut → Boxed captions + SRT → Laugh Track 1 cuối twist → loudness ~-14 LUFS → trình Richard duyệt master.

## 2026-11-19 22:45 — 2K upscale cả 4 take đã về + kiểm chứng
- Tải 22:13-22:44 (Flow, 0cr), xác minh trên disk (không tin toast): 4 file 1080×1920 24fps, AAC 48kHz stereo, 7.85s mỗi clip (ngắn hơn bản 1K 7.93s đúng như đã biết). Soi frame t=4 từng file: đúng shot (sh010 khăn bên đĩa, sh020 cầm điện thoại, sh030 nói vào camera, sh040 ăn/nhai).
- File: generated/2k/sh010-take004-2k.mp4 (sha f7c19e4d…), sh020-take003-2k.mp4 (sha adee589c…), sh030-take002-2k.mp4 (sha 94ec3d2e…), sh040-take003-2k.mp4 (sha 23d29cf7…).
- Lưu ý dựng: sh020 bản 2K là tiếng gốc Nam — phải lồng lại bằng dub track đã có (generated/dub/sh020-take003-dub-track.wav), kiểm tra lại cửa sổ miệng trên bản 2K vì thời lượng lệch 0.08s so với bản 1K. sh010 sáng hơn các shot ~4-6 điểm — cân bằng lúc dựng. Watermark Veo góc dưới phải còn trên cả 4 bản 2K — crop theo quy tắc repo trước khi burn phụ đề.

## 2026-11-19 22:47 — sh020 lồng lại trên bản 2K (dub track đã duyệt)
- Audio 1K và 2K của sh020 giống hệt nhau từng bucket năng lượng 48kHz (cửa sổ miệng Q1 2.24 / Q2 4.10 / Q3 5.70s giữ nguyên; lệch 0.08s chỉ ở đuôi container). Whisper đặt từ "Tội" (Q3) ở 4.90s là SAI — năng lượng cho thấy Q3 bắt đầu 5.70s; không tin Whisper cho thời điểm trên file 2K.
- Dub: cắt dub track 1K đã duyệt (generated/dub/sh020-take003-dub-track.wav, 7.93s, lặng 6.3-7.9s) còn 7.85s, mux lên video 2K → generated/2k/sh020-take003-2k-dub.mp4 (sha 939b526b…). Kiểm chứng trên file đã mux: Whisper nghe đủ 3 câu, lặng tuyệt đối 0-2.0s và 6.5-7.85s (không lọt tiếng gốc), audio giống hệt bản 1K đã duyệt (corr 1.00000, max diff 0.0026), môi mở đúng 2.5/4.1/5.7s.
- Đo thoại + sáng trên 4 bản 2K (Whisper base): sh010 0.00-6.74s, sh020 (gốc) 2.20-6.22s, sh030 0.00-6.26s, sh040 "Là tôi" 0.00-0.60s + nhai 4.6-5.9s. Sáng full-frame: sh010 60.3 / sh020 53.0 / sh030 54.4 / sh040 55.6.

## 2026-11-19 23:09 — MASTER XONG (30.00s, chờ Richard duyệt)
- Stage 1 (build_stage1.py): trim sh010 7.5 / sh020 7.0 / sh030 7.0 / sh040 6.5s (assembly 28.0s), crop 960:1707:60:0 + lanczos 1080x1920, concat filter, loudnorm -15.79 LUFS. BÀI HỌC: đo sáng phải theo vùng crop (post-crop sh010 65.2 / sh020 57.7 / sh030 59.5 / sh040 61.2, đích 60.9) vì crop cắt vùng tối dưới đáy; eq brightness -0.023 đo được -10.0 điểm (hệ số ~435), không phải -5.9. Chạy lại lần 2 với eq sh010 -0.010 / sh020 +0.007 / sh030 +0.003 → 60.6 / 56.6 / 58.4 / 61.2 (eq dương không sáng lên như kỳ vọng, dư 4.6 điểm, nhìn trên QC sheet đều nên chấp nhận). QC sheet: 4 góc dưới-phải sạch watermark Veo + sparkle, frame quanh 3 điểm cắt đúng shot.
- Stage 2 (build_captions.py): 37 từ, Boxed #F59E0B, SRT 4 cue (ep006-hen-ho-voi-ai-subtitles.srt). Fix biên: từ "Là" của sh040 bị Whisper đặt sang sh030 (chuyển lại + clamp về 21.50s); tiếng nhai nghe thành "Mhmmm" (bỏ qua). Backup input ep005 vào public-ep005-backup.
- Remotion render: lần 1 fail OOM ở frame 448/674 (concurrency 2, RAM máy còn 2.5GB trống, swap đã dùng); lần 2 concurrency 1 OK 674/674 (32.1MB). Từ nay render Remotion trên máy này dùng concurrency 1 khi file ~28s trở lên.
- Stage 3 (build_stage3.py): KHÔNG cắt assembly (giữ trọn tiếng nhai). Nhai chính kết thúc 27.4s; Laugh Track 1 nghe 28.15-29.8s, freeze 1.91s (28.08-30.00s, MSE mid-vs-end 0.0, seam 28.05-vs-29.0 MSE 0.1). Master: ep006-hen-ho-voi-ai-boxed-laughtrack1.mp4 (30.00s, 1080x1920, 24fps, -15.39 LUFS / TP -1.00, sha a3a422b1…), tại ~/workspace/ep006-hen-ho-voi-ai-clips/. Bản Boxed chưa Laugh giữ riêng: ep006-assembly-v1-boxed.mp4. Manifest edit/manifest.yaml (revision 1) đã ghi đầy đủ.
- CHƯA ĐĂNG — chỉ đăng/hẹn giờ khi Richard bảo. Bìa: mặt Thảo My.
