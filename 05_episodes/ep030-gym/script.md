# ep030 — Gym

Bản sửa r02 ngày 2026-11-18: đối thoại trực tiếp Thảo My ↔ Tuấn theo yêu cầu người dùng. Draft chờ review, chưa duyệt gen. Bốn shot khoảng 8 giây, 32 giây nguồn trước trim; dọc 9:16.

## Ý tưởng và twist

Hẹn ăn tối. Anh ta gọi ức gà luộc, không sốt. Nói về macro, protein, calo. **Twist:** "Em là người yêu hay là client?"

**Trend khai thác:** Gym bro date — meme toàn cầu, VN chưa bão hòa. Thuật ngữ (protein, macro, cutting) quen thuộc Gen Z. Hài thuần, nam cũng xem vì thấy mình.

## Tình huống

Hẹn ăn tối. Tuấn gọi ức gà cho cả hai không hỏi. My muốn gọi phở, Tuấn tính calo hộ. My chốt bằng câu hỏi trực tiếp. Không lời dẫn, không nhìn camera kể chuyện.

## Nhân vật, trang phục và nguồn

- Thảo My: mặt/tóc thao-my-face-front-v002.png, body thao-my-body-front-v003-face-v002-review.png trong 02_characters/thao-my/approved/.
- Trang phục theo tập, chưa chốt.
- Tuấn: quay lưng, áo ôm sát. Không mặt.
- Quán ăn / nhà hàng. Ảnh ứng viên: 03_locations/date-cafe/. Location chưa duyệt.

## Storyboard

Mỗi shot một người nói, quay đơn và cắt qua lại; người nghe ngoài khung. Hai người nhìn nhau, giữ trục đối thoại.

| Shot | Người nói | Thoại tiếng Việt | Số tiếng | Một hành động chính | Góc máy | Thời lượng nguồn |
|---|---|---|---|---|---|---|
| sh010 | Tuấn | Ức gà luộc, trứng luộc, không sốt. Anh gọi cho em luôn nhé. | 13 | Gọi món cho cả hai, giọng quyết đoán | Cận vừa Tuấn, nhìn My ngoài khung | 8s |
| sh020 | Thảo My | Dạ. Mà em thèm phở bò lắm anh. Em gọi phở được không? | 13 | Giơ menu, hỏi nhẹ nhàng | Cận vừa My, nhìn Tuấn ngoài khung | 8s |
| sh030 | Tuấn | Phở nhiều carb lắm em. Để anh tính calo cho, ăn gì cũng phải tính. | 15 | Lấy điện thoại ra bấm, nghiêm túc | Cận vừa Tuấn, nghiêm túc | 8s |
| sh040 | Thảo My | Anh ơi, em là người yêu anh hay là client của anh vậy? | 13 | Đặt menu xuống, nhìn thẳng Tuấn | Cận vừa My, deadpan | 8s |

Tuấn gọi đồ với giọng quyết đoán như huấn luyện viên, không diễn ác. My hỏi nhẹ ở sh020, đến sh040 mới lạnh giọng. Trim phần chờ thừa khi dựng.

**Câu chốt quotable:** "Em là người yêu hay là client?"

**Hook 3 giây:** "Ức gà luộc. Trứng luộc. Không sốt."

## Sản xuất và âm thanh

Prompt và thoại đồng bộ trong episode.yaml. My dùng hướng giọng nữ miền Bắc; giữ native nếu đúng, sai thì tắt native và lồng clone ThaoMy. Tuấn dùng hướng giọng nam miền Bắc, chưa có preset; không lồng giọng ThaoMy vào Tuấn.

Hard cut, phụ đề Remotion BasicCaptions boxed và SRT. Một SFX Freesound tại cú chốt cuối, chọn nguồn/license khi hậu kỳ; không nhạc nền. Chưa có frame/take, chưa gen hoặc render.

## Lịch sử

Bản r01 monologue Thảo My tường thuật giữ tại prep/before-dialogue-r02/. r02 sửa thành đối thoại trực tiếp.

**Đổi số 25/11/2026:** tập này lúc viết là ep013. Richard chốt 'Chỉ Biết Dễ Thương' làm sớm hơn nên Gym lùi xuống ep030 (đổi bằng `git mv`, xem work-log). Nhân tiện đợt đổi số này mới phát hiện `episode.yaml` + 8 prompt cũ trong thư mục vẫn thuộc tập "Đêm Noel" (mồ côi từ đợt đổi số 20/11, không còn tập nào dùng) — đã rebuild yaml theo đúng script Gym r02, prompt Noel cũ chuyển nguyên vào prep/noel-stale-2026-11-20/ làm lịch sử, không xóa. Số tiếng sh020 sửa 12 → 13 (đếm lại tay, "Dạ." cũng tính 1 tiếng).
