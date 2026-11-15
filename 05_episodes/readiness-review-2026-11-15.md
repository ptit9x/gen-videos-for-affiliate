# Rà soát sẵn sàng sản xuất — 2026-11-15

Kiểm tra file thực tế trong thư mục ep001–008; chưa mở Flow để xác minh asset trên web. Người dùng báo ep001–002 đang gen, nhưng chưa có frame/clip/audio local ở các thư mục tập được kiểm tra. Không kết luận chưa từng gen trên Flow.

| Tập | Hồ sơ local | Trở ngại trước gen video |
|---|---|---|
| ep001 | Có episode.yaml rev3, manifest, prompt ảnh/video và nguồn mặt/body mới; không có frame cảnh local | Hai shot đều approved_for_generation=false, first_frame=null, frame_status=missing_local. YAML/prompt vẫn thoại cũ; thoại gắt nằm trong file đề xuất riêng, chưa đồng bộ. |
| ep002 | Kịch bản gốc và bản thoại gắt; chưa có episode.yaml/manifest/prompt/frame | Chốt bản thoại đang dùng; lập hồ sơ, ghi bộ đang gen, duyệt location/frame và shot. |
| ep003–004 | Kịch bản gốc, bản thoại gắt, wardrobe.md đề xuất | Chốt thoại/bộ đồ; duyệt location; lập episode.yaml/manifest/prompt; dựng và duyệt từng frame. |
| ep005–008 | Kịch bản có My/Vy, wardrobe.md đề xuất | Ngoài hồ sơ/prompt/frame/location/trang phục, Vy chưa có ảnh master hoặc giọng đã duyệt. |

## Ep001: phân biệt prompt với ảnh

`input/prompts/sh010-image.txt` và `sh020-image.txt` là chỉ dẫn sửa ảnh, không phải file ảnh cảnh. Nguồn trong input/references là ảnh nhân vật, không được dùng thay first_frame. Hai shot cần frame riêng được lưu vào input/frames, SHA-256 và ánh xạ trong episode.yaml. Không tìm thấy ảnh cảnh của tập trong lần quét local này.

Có ảnh body v002 và biểu cảm cũ trong input/references; không thuộc nguồn hiện hành và không dùng cho sản xuất mới. Không xóa hoặc khôi phục tài sản trong lần rà soát này.

## Cờ duyệt

approved_for_generation là cờ theo shot trong episode.yaml, không phải cờ chung của script.md. Ep001 có sẵn cả hai cờ false; ep002–008 chưa có YAML nên chưa có cờ. Không tự bật true để hết lỗi. Chỉ ghi true khi shot được người dùng duyệt gen; frame phải được duyệt riêng, tồn tại local và có hash đúng. Trạng thái đã bắt đầu gen trên Flow cần đối chiếu shot/take thực tế, không suy ra từ thông báo chung.

## Kiểm tra và chỉnh lệch đã thực hiện

Đã chạy validator mặc định cho ep001: cấu trúc hợp lệ, không chứng nhận sẵn sàng generation/edit hoặc QC. Lần đầu báo thiếu hai frame local và giọng chưa chốt trong manifest. Đã đồng bộ manifest sang preset Đoan Trang / voice_status locked theo character.yaml, vì người dùng đã chốt giọng; không tạo audio. Kịch bản cũ còn ghi chú lịch sử giọng chưa chốt, lấy character.yaml làm nguồn chuẩn.

Cả ba location.json đang pending_user_review, master_reference=null. Ảnh location trống không phải frame cảnh có nhân vật. Các bộ mới trong wardrobe.md chưa được duyệt.

Kết luận: chưa tập nào đủ hồ sơ local để xác nhận ready gen video. Bước gần nhất là xác minh/lưu frame đang có trên Flow của ep001–002 và xác định thoại đang dùng, rồi đồng bộ hồ sơ; không cần gen lại mù nếu trên Flow đã có tài sản đúng.
