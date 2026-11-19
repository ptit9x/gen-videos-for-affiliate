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
