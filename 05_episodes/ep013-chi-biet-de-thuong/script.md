# ep013 — Chỉ Biết Dễ Thương

Trạng thái: kịch bản ĐÃ DUYỆT 25/11/2026 (Richard gật widget "Duyệt draft, chốt Nam ep008"), chàng trai CHỐT Nam ep008. Chưa làm frame, chưa gen clip. Trang phục My (3 váy SANJOLI) + bối cảnh phòng khách lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.

## Ý tưởng và twist

Phòng khách căn hộ buổi tối. My thay 3 bộ đồ, lần lượt khoe với Nam đang ngồi sofa: "Anh xem giúp em bộ này, thấy sao?" Nam lần nào cũng chỉ đáp đúng một câu: "Dễ thương!" My gắt: "Còn bộ cuối này thì sao? Anh chỉ biết nói mỗi dễ thương thôi hả?" Nam ấp úng: **"Ồ... thì... phối kiểu... dễ thương."** — hóa ra không phải anh khen cho có, mà trong mắt anh cô mặc gì cũng dễ thương; anh chỉ không biết diễn đạt thành lời.

**Nguồn ý tưởng:** video TikTok 35s của @alan.z9 (Thanh Điền - AI Thực Chiến), đăng 19/10, 864 like / 45 comment — xem `input/references/source-tiktok.md`. Cấu trúc gốc: cô gái khoe 3 bộ đồ, chàng trai lặp lại đúng một nhận xét "dễ thương", cô gái bắt giải thích cụ thể (màu sắc, kiểu dáng, phối đồ) thì anh ta không nói được, chốt bằng dòng chữ cuối màn hình đen.

**Cơ chế hài:** lặp lại → leo thang → lật nghĩa. "Dễ thương" lặp 3 lần thành running gag (lần 2 phải ngập ngừng hơn lần 1, không đọc đều nhau). Câu gắt của My ở sh050 tưởng là chê anh vô tâm, hóa ra câu ấp úng của Nam ở sh060 lật lại thành lời khen chân thành nhất: anh không chê được điểm nào vì thấy cô sao cũng dễ thương. Đúng công thức series: leo thang → đối đầu → câu chốt đanh.

**Tone:** ngọt + hài nhẹ, không cà khịa gắt như ep012. Nam không phải khoe khoang hay keo kiệt — anh ngơ thật, thương thật.

## Khóa nhân vật và bối cảnh

### Thảo My (sh010, sh030, sh050)
- Mặt/tóc: `thao-my-face-front-v002.png` (sha256 `8793c0cea8dbb8a2aef02597d76be943a847450263a8a97229c9e2904ed94ed4`); body: `thao-my-body-front-v003-face-v002-review.png`. Nguồn tại `02_characters/thao-my/approved/`.
- Trang phục: **đề xuất — 3 váy SANJOLI khác màu, mỗi shot một màu** (xem `wardrobe.md`): sh010 hồng, sh030 kem, sh050 đen. Ba màu phải khác rõ nhau trên hình để khán giả thấy cô thay đồ thật — frame nào 2 màu nhìn giống nhau thì làm lại frame, không gen clip.
- Son đỏ + móng tự nhiên (quy tắc QC 19/11: ghi rõ trong mọi image prompt, kiểm tra từng frame).
- Diễn xuất: sh010 xoay người khoe váy, cười tươi; sh030 xoay người, chờ đợi; sh050 chống nạnh, gắt nhưng vẫn đáng yêu (không quát tháo), mắt mở to.

### Chàng trai (sh020, sh040, sh060) — CHỐT: Nam ep008 (25/11/2026)
- Mặt: `02_characters/nam/approved/nam-front-v002.jpg` (sha256 `340a246d8119201bc28bd18721fede3cb2a14a44fac1e003efae2ca3b92a0d1f`, đã duyệt 21/11). Nhân vật Flow "Nam" đã tạo xong ở project ep008 (`CNTM · EP008 · Con Nhỏ Đó`, character_id `c759064c-1e4c-4fe7-86ef-54ab519029bc`, reusable) — khi làm frame ep013 thì lấy lại nhân vật Nam từ project ep008 qua picker, không dùng chung asset giữa các project.
- Trang phục trong tập: **đề xuất — áo phông trắng, quần jean đen** (ở nhà, ngồi sofa). Giữ mặt Nam, đổi đồ theo bối cảnh phòng khách buổi tối.
- Diễn xuất: sh020 mắt tròn, cười khoái, gật đầu; sh040 ngập ngừng, gãi đầu, cười trừ; sh060 cúi đầu ấp úng, tay vân vê gối sofa — đây là shot chốt, biểu cảm ngơ + chân thành phải rõ, không được thành mặt vô hồn.

### Bối cảnh
- Phòng khách căn hộ buổi tối, sofa (Nam ngồi), đèn vàng ấm, đủ sáng thấy rõ mặt hai người và màu váy. Location có trong `03_locations/thao-my-apartment/living-room/` (ảnh review `thao-my-living-room-v001.png`, đang chờ duyệt) — dùng làm ref nền khi làm frame, giữ đồng bộ cả 6 shot; sofa là đạo cụ neo: Nam ngồi yên một chỗ cả tập, chỉ My di chuyển/thay đồ.
- Không cần đạo cụ khác. Gương soi toàn thân là điểm cộng nếu frame tự nhiên có, không bắt buộc.

## Storyboard (draft — 6 shot × 8s = 48s)

| Shot | Người nói | Thoại tiếng Việt | Từ | Một hành động chính | Góc máy/biểu cảm | Thời lượng |
|---|---|---|---|---|---|---|
| sh010 | Thảo My | "Anh xem giúp em bộ này, thấy sao?" | 8 | Xoay người khoe váy hồng, cười tươi | Cận vừa My, nhìn Nam ngoài khung | 8s |
| sh020 | Nam | "Đáng yêu" | 2 | Ngồi sofa, mắt tròn, cười khoái, gật đầu | Cận vừa Nam, nhìn My ngoài khung | 8s |
| sh030 | Thảo My | "Thế còn bộ này?" | 4 | Xoay người khoe váy kem, chờ đợi | Cận vừa My, nhìn Nam ngoài khung | 8s |
| sh040 | Nam | "Ừm... dễ thương!" | 3 | Ngập ngừng, gãi đầu, cười trừ | Cận vừa Nam, nhìn My ngoài khung | 8s |
| sh050 | Thảo My | "Còn bộ cuối này thì sao? Anh chỉ biết nói mỗi dễ thương thôi hả?" | 15 | Xoay người khoe váy đen rồi chống nạnh, gắt | Cận vừa My, nhìn Nam ngoài khung | 8s |
| sh060 | Nam | "Ồ... thì... phối kiểu... dễ thương." | 6 | Cúi đầu ấp úng, tay vân vê gối sofa | Cận vừa Nam, giữ mặt Nam 2s cuối | 8s |

**Câu chốt quotable:** "Ồ... thì... phối kiểu... dễ thương."

**Hook 3 giây:** My xoay người khoe váy hồng + "Anh xem giúp em bộ này, thấy sao?" — khán giả ở lại để xem anh chấm bộ này ra sao.

**Chữ cuối (thêm ở hậu kỳ, không đưa vào prompt Veo):** "Em mặc gì anh cũng chỉ thấy... 'Dễ Thương'" — đặt trên nền đen 2s cuối sau sh060, như video gốc.

## Lưu ý khi chuyển thể (cần Richard chốt)

- **Chàng trai là ai (ĐÃ CHỐT 25/11):** Nam ep008 — Richard gật widget "Duyệt draft, chốt Nam ep008". Nam đã đóng ep023/ep024/ep029 liên tiếp, nhưng vai ngơ ngọt này hợp Nam nhất trong dàn đã có mặt (Thảo ep021 hợp vai cà khịa hơn); mỗi tập là một câu chuyện riêng trong chuỗi 13 chàng trai nên không phá continuity.
- **Số tập ep013 (đổi số 25/11):** tập này viết xong lúc đầu là ep030 (ep026–ep028 đã giữ cho 3 draft Ghost, ep029 đã có trong repo). Richard 16:37 chốt đổi thành ep013 để làm sớm hơn, Gym lùi xuống ep030 — xem work-log.
- **sh050 có 2 câu trong 1 shot (15 từ) — cờ vàng theo luật 1 shot = 1 câu:** draft đã duyệt giữ nguyên 2 câu vì câu gắt phải đi liền câu khoe váy trắng ("Còn bộ cuối này thì sao?" là cú mở cho câu gắt). Nếu take 1 Veo đọc vội/cắt câu thì phương án dự phòng đã chuẩn bị, chỉ dùng khi cần và phải báo Richard trước khi đổi thoại: gộp thành 1 câu "Còn bộ cuối này, anh vẫn chỉ biết nói mỗi dễ thương thôi hả?" (14 từ). Không tự sửa thoại khi chưa báo.
- **"Dễ thương!" lặp 3 lần — diễn xuất phải khác nhau:** sh020 hào hứng, sh040 ngập ngừng + "Ừm...", sh060 ấp úng kéo dài "Ồ... thì... phối kiểu...". Nếu 3 take đọc đều nhau như nhau thì gag chết — lúc chọn take phải nghe cả 3 liền nhau, không nghe rời.
- **3 màu váy phải khác rõ:** hồng / kem / đen theo thứ tự sh010 → sh030 → sh050 (Richard chốt 26/11, đổi sh050 trắng → đen; váy xanh ep005 dự phòng). Ba màu tách rõ dưới đèn vàng — khi làm frame vẫn ghi rõ màu từng bộ + kiểm tra 3 frame cạnh nhau trước khi gen clip.
- **Giọng:** thoại viết giọng Bắc. My giữ tiếng Veo gốc nếu đúng giọng Bắc, sai thì tắt native và lồng clone ThaoMy (wordalign, như ep010/ep011). Nam giữ nguyên tiếng gốc Veo, không lồng giọng ThaoMy vào Nam (quy tắc ep012).
- **Trang phục My:** 3 váy SANJOLI hồng/kem/đen — Richard chốt 26/11 (đổi sh050 trắng → đen; váy xanh ep005 dự phòng), xem `wardrobe.md`.
- **Affiliate:** 3 màu váy SANJOLI đều thuộc aff-0001 (link Shopee đã có) — xem `wardrobe.md`. Chưa gắn link vào bài, chưa đăng.
- **Laugh Track:** cú chốt sh060 là ngọt + ngơ, không phải punchline gắt — Laugh Track 1 ở cuối có thể hợp hoặc lạc tone. Quyết lúc dựng master, sau khi nghe take chốt; mặc định để Laugh Track 1, nếu nghe lạc thì bỏ.

## Tài sản và prompt

Khai báo trong `episode.yaml`. Chưa có frame, chưa có prompt ảnh/motion — làm sau khi Richard duyệt kịch bản + chốt chàng trai.

## Hậu kỳ

Chưa tới bước này. Dự kiến: giữ tiếng Veo gốc nếu giọng Bắc (My) / giọng Nam tự nhiên (Nam), lồng clone ThaoMy cho shot My nếu lệch giọng; chữ cuối thêm ở hậu kỳ trên nền đen 2s; Laugh Track 1 ở cú chốt sh060 nếu hợp tone (xem lưu ý trên).

## Thay đổi 26/11 (Richard)
- sh020: câu thoại đổi từ "Dễ thương!" thành "Đáng yêu" (01:02 27/11) — take001 câm hoàn toàn, take002 lỗi Flow "không tạo được âm thanh" với câu "Dễ thương!".
- LƯU Ý: sh040 ("Ừm... dễ thương.") và sh060 (ấp úng chốt "...dễ thương.") vẫn giữ "dễ thương", câu gắt của My ở sh050 ("Anh chỉ biết nói mỗi dễ thương thôi hả?") cũng vẫn vậy — running gag 3 lần "dễ thương" giờ chỉ còn 2 lần + 1 lần "đáng yêu" ở sh020. Chờ Richard chốt có đổi theo sh040/sh060 không.
