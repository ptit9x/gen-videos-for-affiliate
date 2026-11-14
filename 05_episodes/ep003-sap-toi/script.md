# ep003 — Anh sắp tới

Phiên bản 1 — 2026-11-15. **Bản nháp để người dùng review; chưa duyệt kịch bản, chưa gen frame/video.** Một Thảo My, bốn shot độc lập khoảng 8 giây, dự kiến 32 giây trước trim; khung dọc 9:16. Không affiliate, không tự đăng.

## Ý tưởng

Một tin nhắn trấn an bị Thảo My bóc ra bằng đúng trải nghiệm chờ đợi.

## Khóa nhân vật và bối cảnh

- Mặt/tóc: `thao-my-face-front-v001.png` đã duyệt; body: `thao-my-body-front-v003.png` đã duyệt. Nguồn tại `02_characters/thao-my/approved/`, không dùng ảnh cũ.
- Trang phục đề xuất: váy maxi satin đen SANJOLI hiện hành, giữ nguyên cả tập; phụ kiện tối giản, không tự thêm logo.
- Bối cảnh: Sân nội khu chung cư. Ảnh ứng viên: `03_locations/apartment-courtyard/review/apartment-courtyard-v001.png`. **Location chưa duyệt**; chỉ dùng để lên kịch bản, chưa coi là nguồn đã được phép gen shot.
- Một nhân vật trên hình; người được nhắc trong thoại không xuất hiện, không có tiếng đáp ngoài hình. Không cần tạo nam chính.
- Máy tĩnh, từng shot chỉ một hành động chính. Biểu cảm lấy từ diễn xuất; không dùng ảnh biểu cảm cũ làm nguồn.

## Shot và lời thoại nguyên văn

### sh010 — 0–8 giây

- Người nói: Thảo My.
- Thoại (12 từ theo khoảng trắng): “Anh nhắn “sắp tới” rồi. Tôi thích đàn ông biết thông báo.”
- Hành động/diễn: Cầm điện thoại, nhìn camera với nụ cười nhẹ.
- Máy: Trung cảnh ngồi ghế gỗ, hàng cây và lối đi phía sau.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

### sh020 — 8–16 giây

- Người nói: Thảo My.
- Thoại (11 từ theo khoảng trắng): “Mười phút trước cũng sắp tới. Anh này nhất quán thật.”
- Hành động/diễn: Liếc xuống điện thoại rồi ngẩng lên, nụ cười nhạt đi.
- Máy: Cận vừa cùng phía ghế.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

### sh030 — 16–24 giây

- Người nói: Thảo My.
- Thoại (12 từ theo khoảng trắng): “Chắc anh đang đi chậm. Tình cảm mà, cần gì phải vội.”
- Hành động/diễn: Nhìn về lối đi trống một nhịp rồi quay lại camera.
- Máy: Trung cảnh, máy tĩnh.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

### sh040 — 24–32 giây

- Người nói: Thảo My.
- Thoại (12 từ theo khoảng trắng): “Tôi về trước đây. Cho anh thêm không gian để sắp tới.”
- Hành động/diễn: Cất điện thoại vào túi, mắt vẫn nhìn camera; chưa đứng dậy trong câu.
- Máy: Trung cảnh như sh010, giữ một nhịp sau câu.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

## Chuẩn bị frame và dựng

Duyệt location và kịch bản trước, rồi lập `episode.yaml` cùng `edit/manifest.yaml` theo template. Đây mới là kịch bản, chưa có hồ sơ sản xuất/ID Flow. Mỗi shot cần frame có Thảo My đã duyệt, không dùng ảnh location trống thay frame. Prompt ảnh khóa bố cục/trang phục/đạo cụ; prompt video chỉ hành động + câu thoại + hướng giọng và các cấm cơ bản. Không tự gen video từ bản nháp này.

Bản giao tắt tiếng gốc Veo, lồng một preset VieNeu nữ miền Bắc đã chốt (hiện chưa chốt). Ghép hard cut, cắt gọn khoảng im nếu cần nhưng giữ nhịp chốt; SRT riêng canh theo audio cuối. Không chữ điện thoại do AI sinh, nhạc cười hay CTA. Chưa có audio/frame/clip để xác nhận nhịp và khớp môi.

Giữ cùng ghế gỗ bên phải, hướng cây/tòa nhà và nắng; không để ghế/lối đi đảo bên. Không hiện đồng hồ hay tin nhắn phải đọc được, không làm time-lapse. Sau câu cuối có thể cắt ngay ở động tác cất điện thoại.
