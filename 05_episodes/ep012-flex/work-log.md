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
- Commit: (ghi hash sau khi push).

### Còn chờ (sau rebuild)
- Richard review lại hồ sơ rebuild rồi mới làm frame Nano Banana (0 credit) → duyệt frame → gen clip Veo 3 Lite.
- Trang phục Hùng chưa chốt (chỉ thấy lưng/tay) — chốt trước khi làm frame sh010/sh030.
- aff-0007 UNVERIFIED theo lệnh Richard (không xác minh, không thử lại) — chỉ gắn vào bài khi Richard xác nhận màu/link trên điện thoại của cậu ấy, nếu cậu ấy yêu cầu.
