# ep009 — Giỏ hàng — Work log

## 2026-11-22 — Bee (Muse), sửa hồ sơ theo review kịch bản 22/11 (verdict CẦN SỬA)

- Người dùng duyệt các sửa trong review 06:30 22/11 (widget) + chốt trang phục chọn 1 trong 5 váy SANJOLI có sẵn trong Flow (chưa chọn màu cụ thể — xem dưới).
- Motion prompt (cả 4): xóa "Không phụ đề. Không chữ trên màn hình." — ghi tên chữ vào prompt Veo khiến Veo vẽ phụ đề giả nhiều hơn (luật đã chứng minh 14/11, 16/11).
- Image prompt: tuổi 25 → 26 (theo bible); "ánh sáng tự nhiên" → "Ánh sáng xanh lạnh từ màn hình điện thoại, phòng tối."; sh010 thêm đồng hồ 00:00, sh020 thêm đồng hồ 00:30 + giỏ hàng 7 món trên màn hình, sh040 thêm tổng tiền 2.000.000đ trên màn hình (chữ/số trên điện thoại thêm ở hậu kỳ nếu Veo vẽ sai).
- sh020: CU mặt → "Medium CU, mặt + điện thoại trong tay đều thấy rõ" (khớp hành động ngón tay lướt). sh030: 3 động tác → "Thở dài, mắt nhắm lại, tay vẫn bấm tiếp" (image + motion + storyboard).
- Hậu kỳ (script.md + manifest.yaml): bỏ luật cũ "tắt tiếng Veo"; luật hiện hành: kiểm tra giọng native từng shot, giữ gốc nếu nữ miền Bắc, chỉ lồng clone ThaoMy cho shot không phải Bắc. Manifest chuyển sang cấu trúc speakers như ep003/ep004 (preset ThaoMyVeo, locked). SFX cuối tập đề xuất: Laugh Track 1 sau câu chốt sh040 (chờ chốt vị trí).
- SHA-256 8 prompt đồng bộ lại trong episode.yaml (revision giữ 1). Validator mặc định: đạt. Generation gate: chặn đúng (chưa frame/duyệt gen). Edit gate: chặn đúng (chưa take). Lưu ý: cổng edit của validator vẫn đòi mute_veo_native: true (luật cũ) — mâu thuẫn luật 18/11 và manifest ep003/ep004/ep005 đã đăng; cần cập nhật validator sau, không chặn bước hiện tại.
- Chờ: chọn 1 trong 5 váy SANJOLI (Đen/Kem/Trắng/Hồng/Xanh dương) + son/móng; có gắn affiliate không. Chưa làm frame (chưa wardrobe.md), chưa gen.

## 2026-11-22 — Trang phục chốt: váy trắng

- Richard chọn váy trắng (widget, 07:46). Đã ghi vào cả 4 image prompt: "Trang phục: váy hai dây maxi suông SANJOLI màu trắng. Son đỏ. Móng tự nhiên." + lập wardrobe.md (nguồn váy trắng: sanjoli-color-variants/vn-11134207-81ztc-mthrovmm4g02e7.webp, sha b16dae2e…).
- Lưu ý affiliate: aff-0001 đã xác minh chỉ có Đen + Be, không có Trắng — gắn link vào tập này thì không đúng màu váy (y hệt ep003, khi đó Richard chốt BỎ link). Chờ Richard quyết có gắn affiliate không.
- SHA-256 4 image prompt đồng bộ lại; validator mặc định vẫn đạt (exit 0).
- Tiếp theo: làm 4 frame trong Flow (1 edit từ master v002 mỗi shot, 0 credit) để Richard duyệt, rồi gen 4 clip Lite (40 credit).

## 2026-11-22 — Đổi váy trắng → be + commit

- Richard đổi sang váy be (07:51). Đã sửa cả 4 image prompt ("màu trắng" → "màu be") + viết lại wardrobe.md (nguồn váy be: ep002-sanjoli-kem/vn-11134207-81ztc-mthrovoch3ibe2.webp, sha 214c8c45…). Màu Be CÓ bán thật trong listing aff-0001 (chỉ Đen + Be) nên gắn link sẽ đúng màu váy.
- SHA-256 4 image prompt đồng bộ lại; validator mặc định vẫn đạt (exit 0).
- Richard lệnh "update git luôn" (07:51) → commit + push scope ep009 + tracker (không động ep008/locations/affiliate-links đang dở dang).
