# ep004 — Buổi hẹn đúng giờ

Phiên bản 1 — 2026-11-15. **Bản nháp để người dùng review; chưa duyệt kịch bản, chưa gen frame/video.** Một Thảo My, bốn shot độc lập khoảng 8 giây, dự kiến 32 giây trước trim; khung dọc 9:16. Không affiliate, không tự đăng.

## Ý tưởng

Thảo My tưởng cuộc hẹn đã thành công vì đủ lãng mạn, cuối cùng người đúng giờ duy nhất là cô.

## Khóa nhân vật và bối cảnh

- Mặt/tóc: `thao-my-face-front-v001.png` đã duyệt; body: `thao-my-body-front-v003.png` đã duyệt. Nguồn tại `02_characters/thao-my/approved/`, không dùng ảnh cũ.
- Trang phục đề xuất: váy maxi satin đen SANJOLI hiện hành, giữ nguyên cả tập; phụ kiện tối giản, không tự thêm logo.
- Bối cảnh: Café sân vườn lúc chạng vạng. Ảnh ứng viên: `03_locations/date-cafe/review/date-cafe-v001.png`. **Location chưa duyệt**; chỉ dùng để lên kịch bản, chưa coi là nguồn đã được phép gen shot.
- Một nhân vật trên hình; người được nhắc trong thoại không xuất hiện, không có tiếng đáp ngoài hình. Không cần tạo nam chính.
- Máy tĩnh, từng shot chỉ một hành động chính. Biểu cảm lấy từ diễn xuất; không dùng ảnh biểu cảm cũ làm nguồn.

## Shot và lời thoại nguyên văn

### sh010 — 0–8 giây

- Người nói: Thảo My.
- Thoại (15 từ theo khoảng trắng): “Buổi hẹn đầu tiên, tôi đến sớm. Phải để người ta thấy mình nghiêm túc.”
- Hành động/diễn: Ngồi ngay ngắn, nhìn camera, chỉnh nhẹ tay áo hoặc dây túi đặt bên cạnh.
- Máy: Trung cảnh ngang tầm mắt, ghế đối diện trống thấy một phần.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

### sh020 — 8–16 giây

- Người nói: Thảo My.
- Thoại (14 từ theo khoảng trắng): “Bàn đẹp, đèn đẹp, nước cũng ngon. Thiếu mỗi người trả lời tin nhắn.”
- Hành động/diễn: Nhìn ghế trống rồi trở lại camera.
- Máy: Cận vừa, không quay màn hình điện thoại.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

### sh030 — 16–24 giây

- Người nói: Thảo My.
- Thoại (14 từ theo khoảng trắng): “Anh bảo chọn chỗ lãng mạn. Tôi chọn rồi, giờ tự tận hưởng luôn.”
- Hành động/diễn: Nhấc ly nước của mình một đoạn ngắn, chưa uống khi nói.
- Máy: Trung cảnh cùng trục máy, ghế kia vẫn trống.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

### sh040 — 24–32 giây

- Người nói: Thảo My.
- Thoại (14 từ theo khoảng trắng): “Buổi hẹn này có tương lai đấy. Lần sau tôi vẫn đến, một mình.”
- Hành động/diễn: Đặt ly xuống rồi nhìn camera với vẻ bình thản.
- Máy: Cận vừa, giữ nét mặt sau câu.
- Tham chiếu sửa frame: mặt chính diện mới + body v003 + location nêu trên sau khi được duyệt; shot sau bám frame đầu đã duyệt để giữ bố cục.
- Nhịp dự kiến: mở 0–0,5s; nói trong khoảng 0,5–6,5s; giữ phản ứng cuối. Đọc thử trước khi khóa; nếu câu không đủ thời gian thì rút/tách, không tăng tốc thoại.

## Chuẩn bị frame và dựng

Duyệt location và kịch bản trước, rồi lập `episode.yaml` cùng `edit/manifest.yaml` theo template. Đây mới là kịch bản, chưa có hồ sơ sản xuất/ID Flow. Mỗi shot cần frame có Thảo My đã duyệt, không dùng ảnh location trống thay frame. Prompt ảnh khóa bố cục/trang phục/đạo cụ; prompt video chỉ hành động + câu thoại + hướng giọng và các cấm cơ bản. Không tự gen video từ bản nháp này.

Bản giao tắt tiếng gốc Veo, lồng một preset VieNeu nữ miền Bắc đã chốt (hiện chưa chốt). Ghép hard cut, cắt gọn khoảng im nếu cần nhưng giữ nhịp chốt; SRT riêng canh theo audio cuối. Không chữ điện thoại do AI sinh, nhạc cười hay CTA. Chưa có audio/frame/clip để xác nhận nhịp và khớp môi.

Giữ ghế đối diện trống suốt tập, hai ly không đổi vị trí giữa shot; chỉ ly của Thảo My được nhấc. Đặt đèn/vase thấp hoặc lệch đường nhìn để không che mặt; đây là yêu cầu dựng frame, không tự sửa location đang chờ duyệt. Giữ độ sáng chạng vạng, không chuyển hẳn sang đêm.
