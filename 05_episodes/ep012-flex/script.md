# ep012 — Flex

Bản sửa r03 ngày 2026-11-25: thoại 1 câu/shot đã duyệt (Richard 25/11), trang phục áo dài Mai Linh đỏ đô, bối cảnh nhà hàng buổi tối. Hồ sơ rebuild từ script r02 (episode.yaml + 8 prompt cũ là tập khác hẳn sót sau renumber — đã thay toàn bộ). Draft chờ review lại hồ sơ rebuild, chưa duyệt gen. Bốn shot khoảng 8 giây, 32 giây nguồn trước trim; dọc 9:16.

## Ý tưởng và twist

Mới gặp đã khoe xe mấy tỷ, lương ba chục, đồng hồ limited. Bill đến — "em chuyển khoản phần em nhé." **Twist:** "Đồng hồ limited mà chia bill ly cà phê."

**Trend khai thác:** "Thùng rỗng kêu to" — meme VN kinh điển. Khoe giàu + keo kiệt = combo viral. Callback Anh Chia Bill (cùng universe tiền bạc, twist khác).

## Tình huống

Hẹn nhà hàng buổi tối. Hùng khoe xe, đồng hồ limited edition. My lịch sự đáp. Bill đến, Hùng chia bill. My chốt bằng câu đáp trực tiếp. Không lời dẫn, không nhìn camera kể chuyện.

## Nhân vật, trang phục và nguồn

- Thảo My: mặt/tóc thao-my-face-front-v002.png, body thao-my-body-front-v003-face-v002-review.png trong 02_characters/thao-my/approved/.
- Trang phục: **áo dài Mai Linh đỏ đô** (thêu hạc, cúc tàu tua rua, tay lỡ; aff-0007, link https://s.shopee.vn/30ppBKBi6L — UNVERIFIED, Richard dặn không xác minh). Tóc xõa, son đỏ, móng tự nhiên. Ảnh ref: `05_episodes/ep012-flex/input/references/aodai-mai-linh-flatlay-do.jpg`, `aodai-mai-linh-mac-do-ngoai-troi.jpg`, `aodai-mai-linh-mac-do-trong-nha.jpg`.
- Hùng: quay lưng hoặc chỉ thấy tay (đeo đồng hồ limited, cầm ly). Không mặt. Trang phục Hùng chưa chốt — chỉ thấy lưng/tay, chốt trước khi làm frame sh010/sh030.
- Nhà hàng buổi tối. Ảnh nền đã duyệt 19/11: `03_locations/restaurant-evening/approved/restaurant-bg-wood.jpg` (copy trong `05_episodes/ep012-flex/input/references/restaurant-bg-wood.jpg`, sha c035ab8e…).

## Storyboard

Mỗi shot một người nói, quay đơn và cắt qua lại; người nghe ngoài khung. Hai người nhìn nhau, giữ trục đối thoại.

| Shot | Người nói | Thoại tiếng Việt | Số tiếng | Một hành động chính | Góc máy | Thời lượng nguồn |
|---|---|---|---|---|---|---|
| sh010 | Hùng | Em biết xe anh mấy tỷ không? | 7 | Giơ cổ tay khoe đồng hồ, chìa khóa xe trên bàn | Cận vừa Hùng (lưng/tay), nhìn My ngoài khung | 8s |
| sh020 | Thảo My | Dạ hay quá anh, em uống ly cà phê ba mươi ngàn, anh đừng lo. | 15 | Nâng ly cà phê, lịch sự | Cận vừa My, nhìn Hùng ngoài khung | 8s |
| sh030 | Hùng | Bill đây rồi nè, em chuyển khoản phần em nhé, anh gửi số tài khoản. | 15 | Đẩy hóa đơn về phía My, giọng bình thường | Cận vừa Hùng (lưng/tay) | 8s |
| sh040 | Thảo My | Đồng hồ limited mà chia bill ly cà phê. | 9 | Rút điện thoại ra, deadpan, không nói thêm | Cận vừa My, bình thản | 8s |

Hùng khoe giọng tự hào thật sự, không diễn ác. My lịch sự ở sh020, đến sh040 mới lạnh giọng, chỉ nói đúng câu chốt. Trim phần chờ thừa khi dựng.

**Câu chốt quotable:** "Đồng hồ limited mà chia bill ly cà phê."

**Hook 3 giây:** "Em biết xe anh mấy tỷ không?"

## Sản xuất và âm thanh

Prompt và thoại đồng bộ trong episode.yaml. My dùng hướng giọng nữ miền Bắc; giữ native nếu đúng, sai thì tắt native và lồng clone ThaoMy (wordalign, như ep010/ep011). Hùng giữ nguyên tiếng gốc Veo, không preset, không bao giờ lồng giọng ThaoMy vào Hùng (Richard chốt 25/11).

Hard cut, phụ đề Remotion BasicCaptions boxed và SRT. Một SFX Freesound tại cú chốt cuối, chọn nguồn/license khi hậu kỳ; không nhạc nền. Chưa có frame/take, chưa gen hoặc render.

## Lịch sử

Bản r01 monologue Thảo My tường thuật giữ tại prep/before-dialogue-r02/. r02 sửa thành đối thoại trực tiếp (18/11). r03 (25/11): thoại 1 câu/shot đã duyệt, sửa số tiếng, thêm chìa khóa xe trên bàn sh010, đổi trang phục sang Mai Linh đỏ đô, đổi bối cảnh sang nhà hàng buổi tối, sửa plan âm thanh (My native-nếu-Bắc, Hùng giữ native).
