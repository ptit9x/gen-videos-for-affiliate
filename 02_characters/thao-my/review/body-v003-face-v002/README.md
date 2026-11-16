# Body v003 cập nhật mặt và tóc v002 — chờ duyệt

Ngày tạo: 2026-11-16. Công cụ: image_gen tích hợp, mỗi góc một lượt sửa ảnh.

Nguồn: ảnh body tương ứng trong `../../approved/`, cùng `../../approved/thao-my-face-front-v002.png`. Chỉ yêu cầu thay mặt/tóc; giữ vóc dáng, tư thế, áo thun trắng, quần short be, chân trần và nền xám. Giữ nguyên toàn bộ ảnh gốc.

Ba ảnh review có tên `thao-my-body-<góc>-v003-face-v002-review.png`. Prompt đầy đủ, đường dẫn nguồn công cụ, kích thước và hash từng đầu ra nằm trong `generation-record.json`.

## Kiểm tra trực quan

Đã xem cả ba đầu ra: đủ đầu và bàn chân; đúng góc chính diện, nghiêng trái khung hình và sau; tóc đã đổi sang sóng lớn. Không thấy lỗi nối cổ rõ hoặc lỗi tay/chân nổi bật. Vóc dáng và trang phục nhìn gần nguồn, nhưng ảnh sinh lại không bảo đảm giữ từng pixel hay số đo; chưa có chứng nhận cơ thể giống tuyệt đối. Mặt chính diện hơi xoay theo ảnh chân dung mẫu. Góc nghiêng và tóc phía sau là suy diễn từ ảnh mẫu, cần người dùng duyệt độ khớp và độ dài tóc giữa các góc.

Trạng thái: CHỜ DUYỆT, không đưa vào approved hoặc chọn làm ảnh sản xuất. Chưa kiểm chứng trong Flow. Body v003 gốc vẫn là chuẩn vóc dáng; ảnh v002 là chuẩn mặt và tóc.

## Revision tóc dày r02 — hướng hiện hành

Chốt từ phản hồi tiếp theo: thay đổi ít để giữ nhận diện video đã đăng; chủ yếu tăng độ dày, độ bồng và sóng tóc, không tiếp tục sửa cấu trúc mặt. Đã tạo đủ ba góc bằng image_gen, lưu trong `hair-density-r02/`; prompt và hash ở `revision-record.json`. Đã xem trực quan: tóc đầy hơn nhẹ ở sóng/đuôi, giữ trang phục và tư thế; không thấy lỗi hình thể nổi bật. Không khẳng định giữ nguyên từng pixel hoặc đối chiếu được với video đã đăng. Chờ duyệt hình; chưa thử Flow. Hai lượt chỉnh mặt trước khi nhận chỉ đạo mới được giữ riêng tại `face-correction-superseded/`, không chọn dùng.
