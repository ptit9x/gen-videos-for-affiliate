# Ảnh tham chiếu Thảo My

Đã tách 21 ảnh từ hai sheet người dùng chọn. Chỉ crop pixel gốc và lưu PNG; không sinh lại khuôn mặt, không upscale, không làm đẹp. Bỏ 4 pixel mỗi mép ô để tránh đường ghép. Thông tin nguồn, tọa độ và SHA-256 nằm trong `references.json`.

**Trạng thái:** đã tách và kiểm tra hình ảnh; chưa thử tạo video Flow bằng các ảnh đơn. `approved/` ở đây ghi nhận tạo hình đã chọn, không có nghĩa Flow đã chấp nhận tất cả ảnh.

## Quy tắc gọi tên trong kịch bản

- Dùng đúng tên file dưới đây, có đuôi `.png`, không gọi chung “ảnh số 1”.
- Khi đóng gói một tập, copy ảnh vào `input/references/` và giữ nguyên tên file. `reference_files` trong `shots.json` ghi `references/<tên-file>.png`.
- Kịch bản ghi tên file và mục đích (khóa mặt/góc máy/biểu cảm); prompt nhắc đúng thứ tự ảnh đính kèm. Upload ảnh thật, không chỉ viết tên ảnh trong prompt.
- `screen-left/right` chỉ hướng mũi/mặt trên khung hình, không phải bên trái/phải giải phẫu nhân vật. Không lật ảnh.
- Tối đa 3 ảnh/shot theo giới hạn đang gặp; thử 1 ảnh trước. Ảnh quay lưng không thay thế ảnh nhìn rõ mặt để khóa danh tính.

## Body v002

Người dùng đã đồng ý hướng vóc dáng: cao định hướng 169 cm, đồng hồ cát nhẹ, eo rõ hơn, ngực/hông đầy đặn vừa phải, chân dài cân đối; giữ nhận diện khuôn mặt và tóc. Số đo này là ý đồ thiết kế, không đo từ ảnh. Bản v002 được chỉnh bằng imagegen, không phải crop nguyên pixel như v001. Giữ toàn bộ v001 để so sánh; chưa trộn body v001 và v002 trong cùng tập.

- `thao-my-body-front-v002.png`: chính diện.
- `thao-my-body-profile-screen-left-v002.png`: nghiêng, mặt hướng trái khung hình.
- `thao-my-body-back-v002.png`: phía sau.

Ba ảnh này cần người dùng xem và thử Flow trước khi khóa làm bộ body sản xuất. Prompt chỉnh nằm trong [06-body-v002.md](prompts/06-body-v002.md).

## Bộ khởi đầu gợi ý

- Trung cảnh chính diện: `thao-my-angle-front-v001.png`.
- Góc 3/4: `thao-my-angle-threequarter-screen-left-01-v001.png`.
- Cận mặt trung tính: `thao-my-expr-neutral-front-v001.png`.

Chọn theo shot, không mặc định gửi cả ba; ảnh biểu cảm cười/ngạc nhiên thay cho ảnh trung tính khi cảnh cần.

## Biểu cảm sitcom bổ sung

Ba bản chỉnh bằng imagegen từ ảnh mặt trung tính: nghi ngờ (`skeptical`), đắc ý (`smug`) và ngượng khi bị bắt bài (`caught-out`). Tên file ở bảng dưới; chưa thử Flow. Prompt nằm trong `prompts/07-sitcom-expressions.md`.

Năm prompt tạo sheet cũ đã được xoá theo yêu cầu người dùng. `prompts/` chỉ giữ prompt body v002 và biểu cảm sitcom mới.

## Danh mục

| File | Nội dung | Kích thước |
|---|---|---|
| [thao-my-expr-neutral-front-v001.png](approved/thao-my-expr-neutral-front-v001.png) | Chính diện, trung tính | 1827×1012 |
| [thao-my-expr-smile-front-v001.png](approved/thao-my-expr-smile-front-v001.png) | Chính diện, cười nhẹ | 1826×1012 |
| [thao-my-expr-happy-front-v001.png](approved/thao-my-expr-happy-front-v001.png) | Chính diện, cười thấy răng | 1827×1012 |
| [thao-my-expr-surprised-front-v001.png](approved/thao-my-expr-surprised-front-v001.png) | Chính diện, ngạc nhiên | 1827×1024 |
| [thao-my-expr-curious-head-tilt-v001.png](approved/thao-my-expr-curious-head-tilt-v001.png) | Tò mò, nghiêng đầu | 1826×1024 |
| [thao-my-expr-thoughtful-glance-v001.png](approved/thao-my-expr-thoughtful-glance-v001.png) | Suy nghĩ, liếc sang bên | 1827×1024 |
| [thao-my-expr-shy-smile-front-v001.png](approved/thao-my-expr-shy-smile-front-v001.png) | Chính diện, cười ngượng | 1827×1012 |
| [thao-my-expr-talking-front-v001.png](approved/thao-my-expr-talking-front-v001.png) | Chính diện, miệng đang nói | 1826×1012 |
| [thao-my-expr-laughing-front-v001.png](approved/thao-my-expr-laughing-front-v001.png) | Chính diện, cười lớn | 1827×1012 |
| [thao-my-angle-front-v001.png](approved/thao-my-angle-front-v001.png) | Trung cảnh, chính diện | 909×1213 |
| [thao-my-angle-threequarter-screen-left-01-v001.png](approved/thao-my-angle-threequarter-screen-left-01-v001.png) | Trung cảnh, mặt hướng trái khung hình, góc 3/4, bản 1 | 910×1213 |
| [thao-my-angle-threequarter-screen-left-02-v001.png](approved/thao-my-angle-threequarter-screen-left-02-v001.png) | Trung cảnh, mặt hướng trái khung hình, góc 3/4, bản 2 | 909×1213 |
| [thao-my-angle-profile-screen-left-01-v001.png](approved/thao-my-angle-profile-screen-left-01-v001.png) | Trung cảnh, nghiêng hướng trái khung hình, bản 1 | 910×1213 |
| [thao-my-angle-profile-screen-left-02-v001.png](approved/thao-my-angle-profile-screen-left-02-v001.png) | Trung cảnh, nghiêng hướng trái khung hình, bản 2 | 910×1213 |
| [thao-my-angle-back-head-v001.png](approved/thao-my-angle-back-head-v001.png) | Phía sau đầu/vai, không thấy mặt | 908×1213 |
| [thao-my-angle-profile-screen-right-v001.png](approved/thao-my-angle-profile-screen-right-v001.png) | Nửa người, nghiêng hướng phải khung hình | 909×1843 |
| [thao-my-angle-profile-screen-left-03-v001.png](approved/thao-my-angle-profile-screen-left-03-v001.png) | Nửa người, nghiêng hướng trái khung hình, bản 3 | 910×1843 |
| [thao-my-angle-back-upperbody-v001.png](approved/thao-my-angle-back-upperbody-v001.png) | Phía sau thân trên, không thấy mặt | 909×1843 |
| [thao-my-body-front-v001.png](approved/thao-my-body-front-v001.png) | Toàn thân, chính diện | 910×1843 |
| [thao-my-body-profile-screen-left-v001.png](approved/thao-my-body-profile-screen-left-v001.png) | Toàn thân, nghiêng hướng trái khung hình | 910×1843 |
| [thao-my-body-back-v001.png](approved/thao-my-body-back-v001.png) | Toàn thân, phía sau, không thấy mặt | 908×1843 |
| [thao-my-body-front-v002.png](approved/thao-my-body-front-v002.png) | Toàn thân chính diện, vóc dáng v002: đồng hồ cát nhẹ, định hướng 169 cm | 881×1784 |
| [thao-my-body-profile-screen-left-v002.png](approved/thao-my-body-profile-screen-left-v002.png) | Toàn thân nghiêng hướng trái khung hình, body v002 | 881×1784 |
| [thao-my-body-back-v002.png](approved/thao-my-body-back-v002.png) | Toàn thân phía sau, body v002 | 882×1784 |
| [thao-my-expr-skeptical-front-v001.png](approved/thao-my-expr-skeptical-front-v001.png) | Nghi ngờ, nhướng mày và liếc nhẹ | 1685×933 |
| [thao-my-expr-smug-front-v001.png](approved/thao-my-expr-smug-front-v001.png) | Đắc ý, cười nhếch nhẹ | 1686×933 |
| [thao-my-expr-caught-out-front-v001.png](approved/thao-my-expr-caught-out-front-v001.png) | Ngượng khi bị bắt bài, mắt né nhẹ | 1686×933 |

[Bảng xem nhanh 21 ảnh crop gốc](previews/reference-catalog.jpg) chỉ để chọn ảnh, không upload bảng này vào Flow.
