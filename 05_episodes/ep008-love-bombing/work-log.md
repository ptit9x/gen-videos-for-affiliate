# ep008-love-bombing — work log

## 2026-11-19 — Áo linen chuyển sang ep008 (Bee)
- Richard chốt: áo linen LAHSTORE (aff-0002) bỏ khỏi ep006, để vào ep008 Love Bombing — solo ở nhà, sofa ban ngày, đúng bối cảnh áo.
- Ghi vào `script.md` (khóa trang phục + bảng sản phẩm lồng ghép) và `wardrobe.md` mới; sug-0007 chuyển episode ep006 → ep008; ghi chú aff-0002 cập nhật.
- Màu áo chưa chốt; ảnh mẫu màu Tím — dùng Tím khi làm frame nếu Richard không đổi.
- Chưa làm: episode.yaml + prompts ep008 vẫn là bản "Mở hộp" cũ (4 shot unboxing), chưa đồng bộ với kịch bản Love Bombing 3 shot — cần đồng bộ trước khi làm frame/gen clip. Script còn cụm "không nhạc/chữ/phụ đề" ở mục Tài sản và prompt, cần bỏ trước khi gen (bài học phụ đề giả 14/11).

## 2026-11-19 — Đồng bộ episode.yaml + prompts sang Love Bombing (Bee)
- Viết lại 6 prompt theo kịch bản Love Bombing 3 shot (sofa phòng khách ban ngày, áo linen tím); xóa prompt sh040 cũ (unboxing). Bỏ cụm nêu tên phụ đề/chữ khỏi mọi prompt + script; hậu kỳ sửa theo quy tắc giữ tiếng Veo nếu giọng Bắc.
- Viết lại `episode.yaml`: title "Love Bombing", target 24s, 3 shot, dialogue + sha256 prompt mới, image_sources giữ nguyên (hash khớp). Revision giữ 1, manifest khớp.
- Validator default chạy sau bước này; generation gate chặn đúng như kỳ vọng (chưa có frame duyệt / flow_project).
- Kết quả validator 19/11: default exit 0 ("Episode structure valid", chỉ note frame thiếu + giọng VieNeu pending); generation exit 1 đúng kỳ vọng (shot chưa duyệt, chưa có frame, chưa có Flow project, draft).
