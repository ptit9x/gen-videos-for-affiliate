# Frame local ep001 — rev4, 2026-11-15

Tạo theo yêu cầu người dùng bằng built-in imagegen, không phải asset Flow. Hai ảnh đã được xem: một người, váy đen, trung cảnh, bàn bừa, shot đầu cười nhẹ và shot sau deadpan. Chưa có phê duyệt người dùng về nhận diện/frame; chưa kiểm chứng trong Flow. Ảnh gần tỷ lệ 9:16 (941×1672), chưa crop hoặc kéo méo.

- sh010: `input/frames/sh010-frame-local-v001.png`, 941×1672, SHA-256 `d5fe6a9040901e2e780dd36f6948628a5a8cc7c90bf337e5073d8339c1888f96`.
- sh020: `input/frames/sh020-frame-local-v001.png`, 941×1672, SHA-256 `47699cd78454ea41d31fc3963d753478f3823bf6c794e608b7ee42e7200e4fc4`.

Nguồn shot đầu: mặt chính diện v001, tỷ lệ body v003 đã duyệt và ảnh váy SANJOLI (chỉ lấy trang phục). Shot sau sửa trực tiếp từ frame shot đầu. Prompt thật lưu trong input/prompts/sh010-local-imagegen-v001.txt và sh020-local-imagegen-v001.txt. Giữ prompt Flow cũ, giữ bản rev3 trong prep/rev3-record; không xóa ảnh nguồn.

YAML và manifest tăng rev4; first_frame có file/hash thật, frame_status=pending_review, approved_for_generation=false. ID take rev2 vẫn là lịch sử, không chọn cho rev4. Chưa tạo clip hoặc audio. Trước gen video cần duyệt frame và xác định dùng thoại gốc hay bản gắt rồi đồng bộ motion prompt/thoại nếu đổi.
