# Tủ đồ — thao-my

**Sổ đăng ký trang phục đã gen (đường dẫn local + project Flow từng món): `REGISTRY.md` — kiểm tra ở đó trước khi gen/sửa ảnh trang phục mới, đừng gen lại món đã có.**

Cập nhật 2026-11-15. Trang phục chọn theo từng tập, không khóa một bộ cho toàn series.

- `inbox/`: người dùng bỏ ảnh sản phẩm/ảnh bộ đồ vào đây. Có thể thêm file `.md` chứa link sản phẩm và ghi chú; đặt tên gợi nhớ, ví dụ `ep006-ao-xanh.jpg` hoặc `ep006-goi-y.md`.
- `review/`: ảnh thử đồ trên nhân vật, chờ duyệt; giữ phiên bản riêng.
- `approved/`: chỉ lưu bản phối/ảnh thử đồ đã được người dùng duyệt rõ; việc cung cấp ảnh nguồn chưa có nghĩa duyệt frame cuối.

Có thể gửi ảnh hoặc link ngay trong chat, kèm tập và nhân vật; không bắt buộc tự thao tác folder. Ghi nguồn/link thật, không tự khẳng định quyền sử dụng. Ảnh người mẫu chỉ tham chiếu quần áo, không lấy mặt/tóc/vóc dáng người mẫu thay nhân vật.

Nếu chưa có ảnh, đề xuất một bộ bằng mô tả trong `05_episodes/<tập>/wardrobe.md`; khi được yêu cầu tạo frame thì sửa trang phục trên nguồn nhân vật đã duyệt. Không cần gen nhân vật mới mỗi lần thay đồ. Không tự gen từ việc tạo thư mục này.

Mỗi tập một bộ nhất quán cho mỗi nhân vật. Khi nối trực tiếp cùng thời điểm/cảnh giữa hai tập, có thể giữ bộ cũ vì continuity; không ép đổi đồ giữa cảnh. Trang phục riêng được ghi trong wardrobe.md của tập; khi sản xuất đồng bộ vào prompt ảnh, image_sources trong episode.yaml và ghi chú manifest. Không thêm trường ngoài schema. Video chỉ dùng frame cảnh đầu đã duyệt.
