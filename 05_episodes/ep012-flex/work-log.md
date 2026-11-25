# Work log — ep012 'Flex'

## 2026-11-25 — Rebuild hồ sơ r03 (review 06:30 → chốt → rebuild)

### Vấn đề (review 06:30 25/11, verdict CHƯA ĐỦ)
- script.md r02 (18/11) là tập Flex (Hùng ↔ My, café, chốt "Đồng hồ limited mà chia bill ly cà phê") nhưng episode.yaml rev 1 + cả 8 prompt trong input/prompts/ lại là một tập khác hẳn — My độc thoại solo ở phòng khách trang trí lễ hội, chốt "Là tôi." Lỗi cùng loại ep011 hôm qua; gần như chắc là file sót sau lần renumber. Theme lễ hội đã có nhà ở ep016 Last Christmas.
- Số từ trong script.md sai 3/4 shot (đếm lại: sh020 16 không phải 15, sh030 15 không phải 14, sh040 14 không phải 13).
- Cả 4 shot đều 2 câu — phạm luật "1 shot, 1 câu trọn ý".
- "Xe mấy tỷ" vô hình (cảnh café, không thấy xe).
- edit/manifest.yaml còn plan âm thanh của concept cũ (mute_veo_native true, VieNeu-TTS).

### Quyết định của Richard (25/11, chat review ep012)
- 06:57: chốt concept Flex; trang phục "áo dài Thanh Nghi tiếp".
- 07:06: đổi trang phục sang áo dài Mai Linh, link aff https://s.shopee.vn/30ppBKBi6L + 10 ảnh (9 tấm riêng, 1 tấm trùng).
- 07:07: "4 câu thoại sửa ok"; "Location kiếm nơi khác đi" (không dùng date-cafe).
- 07:07: "Xe mấy tỉ từ sh010 ok" (giữ câu khoe xe).
- 07:07: "Giọng Hùng giữ nguyên native ok".
- 07:11: "không phải xác minh" (dừng xác minh link Shopee aff-0007); hỏi nhà hàng tối nên mặc màu gì.
- 07:11: Bee đề xuất đỏ đô cho nhà hàng tối; Richard "Duyệt" (07:12) → màu đỏ đô chốt.

### Rebuild r03 (25/11, subagent)
- script.md → r03: thoại 1 câu/shot đã duyệt (7/15/15/9 từ), sửa số tiếng, thêm chìa khóa xe trên bàn sh010, đổi trang phục Mai Linh đỏ đô + aff-0007, đổi bối cảnh nhà hàng buổi tối (đã duyệt 19/11), sửa plan âm thanh.
- episode.yaml → revision 2, title "Flex", editorial_status draft, 4 shot với thoại đã duyệt; approved_for_generation false, first_frame null, takes [].
- input/prompts/ (8 file): viết lại toàn bộ theo Flex; không còn tên tập cũ hay cụm "Không phụ đề"/"Không chữ trên màn hình" trong bất kỳ prompt nào; son đỏ + móng tự nhiên ghi trong mọi image prompt của My; sh010 có chìa khóa xe trên bàn.
- edit/manifest.yaml → revision 2: audio_plan mới (mute_veo_native false; My native-nếu-Bắc else clone ThaoMy wordalign; Hùng giữ native, không preset, không lồng ThaoMy); bỏ plan VieNeu-TTS/mute-all cũ.
- wardrobe.md (mới): Mai Linh đỏ đô + 3 ref đỏ + sha, aff-0007, son đỏ, móng tự nhiên, tóc xõa.
- input/references/restaurant-bg-wood.jpg: copy byte-identical từ 03_locations/restaurant-evening/approved/ (sha c035ab8e…, duyệt 19/11).
- 04_products/affiliate-links.csv: hàng aff-0007 đã có từ trước (kiểm tra: chỉ 1 hàng, không trùng).
- 02_characters/thao-my/wardrobe/REGISTRY.md: hàng Mai Linh đã có từ trước; cập nhật màu thành đỏ đô (chốt 25/11).
- 00_docs/production-tracker.csv: hàng ep012 cập nhật sang Flex r03 (tên + nội dung cũ xem git history).
- Validator: `python3 06_automation/validate_episode.py 05_episodes/ep012-flex` — ĐẠT, exit 0 ("Episode structure valid"). Ghi chú kèm: 4 first frame missing (chưa làm frame — đúng giai đoạn này); "VieNeu voice pending user choice" là ghi chú chung của validator khi voice_status != locked, không phải lỗi (voice_status ở đây là decided_by_user theo quyết định của Richard).
- Commit: `8b1a80a` "rebuild ep012 Flex profile (r03): approved dialogue, Mai Linh red, restaurant-evening, fix Noel leftover" — 26 files, pushed, verified on origin/main (97848cd..8b1a80a).

### Còn chờ (sau rebuild)
- Richard review lại hồ sơ rebuild rồi mới làm frame Nano Banana (0 credit) → duyệt frame → gen clip Veo 3 Lite.
- Trang phục Hùng chưa chốt (chỉ thấy lưng/tay) — chốt trước khi làm frame sh010/sh030.
- aff-0007 UNVERIFIED theo lệnh Richard (không xác minh, không thử lại) — chỉ gắn vào bài khi Richard xác nhận màu/link trên điện thoại của cậu ấy, nếu cậu ấy yêu cầu.

## 2026-11-25 11:02 — Frames v1 (Nano Banana, 0 credit)

- Project Flow mới: CNTM · EP012 · Flex — https://flow.google.com/project/1cc7499d-86b9-44a0-b084-306ff4856f81 (acc huynhdn Pro; không cần xác minh thiết bị).
- Mỗi frame 1 edit trực tiếp từ master, không nối tiếp. Mặt ThaoMy002 lấy lại qua picker từ project EP003; nền nhà hàng lấy lại qua picker từ EP006; chỉ upload 3 ref áo dài đỏ mới; body ref đã có sẵn trong EP006 nên không upload.
- 4 frame về đủ, đã verify file trên disk (768×1376) + xem trực tiếp, map byte-identical vào input/frames/ (sha trong episode.yaml), frame_status pending_review, approved_for_generation vẫn false — chờ Richard duyệt frame.
  - sh010-frame-v1.jpg (ffb31434…, 132.233 B): Hùng lưng/tay, sơ mi trắng, đồng hồ trên cổ tay giơ cao, ly trong tay, chìa khóa xe trên bàn gỗ. Nit: sao Gemini nhỏ góc phải dưới (như ep011 đã duyệt).
  - sh020-frame-v1.jpg (f5673908…, 172.048 B): My áo dài đỏ đô thêu hạc + cúc tàu tua rua, son đỏ, nốt ruồi cằm trái (đã kiểm bằng crop zoom), móng tự nhiên, nâng ly cà phê. Nit: sao Gemini nhỏ góc phải dưới.
  - sh030-frame-v1.jpg (89d2bb5e…, 120.413 B): Hùng lưng/tay, sơ mi trắng, đồng hồ, đẩy bìa hóa đơn đen có hóa đơn trắng qua bàn. Nit: chữ trên hóa đơn mờ, khó đọc (chữ giả nhỏ); sao Gemini nhỏ góc phải dưới.
  - sh040-frame-v1.jpg (bd12340f…, 172.200 B): My deadpan, điện thoại cầm 2 tay trên bàn, áo dài đỏ đô. Nit: son đỏ nhạt hơn sh020 rõ (hồng đất thay vì đỏ tươi); nốt ruồi cằm trái không rõ ở khung này; sao Gemini nhỏ góc phải dưới.
- Validator sau khi map frame: đạt (exit 0).

## 2026-11-25 ~11:15 — Kiểm tra áo dài đỏ vs mẫu Mai Linh (Richard hỏi)

- So sánh trực tiếp frame v1 với 3 ảnh mẫu đỏ (flatlay + mặc ngoài trời + mặc trong nhà) + đo màu HLS.
- ĐÚNG: màu đỏ cùng họ (đỏ đô), cổ trụ, cúc tàu trắng + tua rua, thêu hạc tone-on-tone.
- SAI — TAY ÁO: mẫu thật tay lỡ RỘNG, vải ĐỤC không xuyên thấu, kết thúc ở khuỷu, cẳng tay để trần. Frame v1 tay áo là VOAN XUYÊN THẤU (thấy rõ da tay), ôm tay, kéo dài tới cổ tay. Ảnh đối chiếu: workspace/ep012-sleeve-check-frame-sh020.png vs workspace/ep012-sleeve-check-sample-mai-linh.png.
- MÀU: đo HLS vùng ngực đủ sáng — mẫu L39 S32 H354; sh020 L22 S49 H13, sh040 L24 S53 H2. Frame đỏ tối/đậm hơn mẫu; một phần do đèn vàng nhà hàng tối, nhưng tay áo mới là lỗi cấu trúc rõ ràng.
- Hướng sửa (chờ Richard gật): làm lại sh020/sh040 từ master với prompt ghi rõ "tay lỡ rộng, vải đục không xuyên thấu, tay áo kết thúc ở khuỷu, cẳng tay để trần" + lấy ảnh mặc trong nhà làm ref chính (thấy rõ tay áo nhất). Giữ v1 làm lịch sử, chỉ thay khi v2 được duyệt.

## 2026-11-25 11:31 — Frames v2 cho sh020/sh040 (sửa tay áo + son)

- Prompt sửa (đã cập nhật file + sha trong episode.yaml, validator đạt): tay lỡ RỘNG, vải đục không xuyên thấu, tay áo kết thúc ở khuỷu tay, cẳng tay để trần; ref chính ảnh mặc trong nhà; son đỏ đậm.
- Làm mới 1 edit từ master trong project EP012 (không sửa nối tiếp từ v1), 0 credit, mỗi shot 1 lượt.
- sh020-frame-v2.jpg (56ab98a3…, 175.109 B): tay áo SỬA ĐÚNG — rộng, vải đục, hết ở khuỷu, cẳng tay trần; son đỏ đậm; mặt khớp v002; thêu hạc cùng màu đỏ chìm; cúc tàu + tua rua. Nit: sao Gemini nhỏ góc phải dưới; trên bàn có 2 ly cà phê (cảnh hẹn hò 2 người nên hợp lý).
- sh040-frame-v2.jpg (f5a6995d…, 181.422 B): tay áo SỬA ĐÚNG; son đỏ đậm (đỏ hơn v1 rõ); mặt khớp v002, deadpan, nốt ruồi cằm trái thấy rõ khi crop zoom; điện thoại cầm 2 tay. Nit: thêu hạc bằng chỉ TRẮNG/bạc nổi bật — mẫu thật thêu cùng màu đỏ chìm (sh020 v2 thì đúng); sao Gemini nhỏ góc phải dưới.
- v1 giữ lại làm lịch sử trong input/frames/. episode.yaml đã trỏ sh020/sh040 sang v2, frame_status vẫn pending_review — chờ Richard duyệt.

## 2026-11-25 11:43 — Frame v3 cho sh040 (thêu hạc trắng → cùng màu đỏ)

- Prompt sửa (đã cập nhật file + sha trong episode.yaml, validator đạt): thêu hạc cùng màu đỏ chìm, không dùng chỉ trắng hay bạc.
- Làm mới 1 edit từ master trong project EP012 (không sửa nối tiếp từ v2), 0 credit, 1 lượt.
- sh040-frame-v3.jpg (0cb787c1…, 162.230 B): thêu hạc SỬA ĐÚNG — cùng màu đỏ chìm, không còn chỉ trắng/bạc; tay áo vẫn đúng (rộng, vải đục, hết ở khuỷu, cẳng tay trần); son đỏ đậm; mặt khớp v002, deadpan, nốt ruồi cằm trái thấy rõ khi crop zoom; điện thoại cầm 2 tay.
- Nit mới: cúc tàu ở v3 thành màu ĐỎ ĐẬM thay vì trắng như mẫu (v2 thì cúc trắng đúng) — tua rua vẫn đỏ đậm như mẫu; nền có thêm 2 khách bàn bên, người phụ nữ bàn bên nhìn về phía máy (hơi phân tâm). v2 giữ lại làm lịch sử.
- episode.yaml đã trỏ sh040 sang v3, frame_status vẫn pending_review — chờ Richard duyệt cả 4 frame.
