# Bộ ảnh Thảo My hiện hành

Người dùng duyệt mặt mới và toàn bộ body v003 ngày 2026-11-15; yêu cầu chỉ dùng bộ này. Không trộn bộ cũ vào ảnh mới.

## Ảnh đã duyệt

- [Mặt chính diện](approved/thao-my-face-front-v001.png): chuẩn khuôn mặt, tóc và thần thái.
- [Body chính diện](approved/thao-my-body-front-v003.png).
- [Body nghiêng trái khung hình](approved/thao-my-body-profile-screen-left-v003.png).
- [Body phía sau](approved/thao-my-body-back-v003.png).

Body mặc áo thun trắng, quần short be, chân trần. Không suy ra số đo chính xác từ ảnh. Chưa kiểm chứng bộ mới trong Flow.

## Sử dụng

Dùng đúng tên PNG; copy ảnh cần dùng vào `input/references/` của tập và ghi SHA-256 trong `episode.yaml`. Chọn ảnh đơn phù hợp, không dùng sheet. Sửa ảnh cảnh từ ảnh tham chiếu; video chỉ nhận một frame cảnh đầu đã duyệt. Không dựng lại mặt bằng chữ. `screen-left` là hướng mặt trên khung hình; không lật ảnh.

Trang phục tham chiếu body không thay trang phục tập: váy maxi satin đen SANJOLI vẫn theo hồ sơ hiện hành. Ảnh trong `wardrobe/` chỉ tham chiếu trang phục. Giọng VieNeu-TTS nữ miền Bắc đang chờ chọn preset; tắt tiếng gốc Veo khi dựng.

## Xuất xứ

- [Prompt mặt](review/face-reference-2026-11-15/README.md).
- [Prompt body](review/body-v003/README.md).
- `references.json`: danh mục hiện hành và SHA-256.
- Bộ ảnh cũ và bản lưu trữ đã xoá hẳn theo yêu cầu người dùng ngày 2026-11-15; chỉ dùng bộ mới.
- Giữ ảnh nguồn trong `source/` để lưu xuất xứ. Không thay tài sản hay hồ sơ tập đã tạo.
