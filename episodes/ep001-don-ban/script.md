# ep001 — Dọn bàn xong hết giờ làm

Phiên bản 1 — 2026-11-14. Kịch bản đã soạn theo yêu cầu: **ít cảnh, thoại ngắn**. Chưa tạo ảnh bối cảnh hoặc video. Một bối cảnh, một nhân vật, hai clip nguồn 8 giây; tổng dự kiến 16 giây trước trim. Không affiliate trong tập thử này.

## Ý tưởng và câu chốt

Thảo My tin rằng bàn gọn thì sẽ tập trung. Dọn xong, cô lấy ngay việc đầu óc “trống” làm lý do nghỉ.

| Clip | Thoại chính xác | Diễn | Ảnh biểu cảm |
|---|---|---|---|
| sh010 — 8s | “Dọn xong cái bàn này, tôi sẽ tập trung làm việc!” | Tự tin, kéo một cuốn sổ cho ngay ngắn | `thao-my-expr-smug-front-v001.png` |
| sh020 — 8s | “Bàn gọn rồi. Đầu óc cũng trống luôn. Mai làm vậy.” | Nụ cười tắt, ngượng một nhịp rồi chốt tỉnh bơ | `thao-my-expr-caught-out-front-v001.png` |

Khoảng 12 đơn vị tách bằng khoảng trắng mỗi câu; chỉ là ước lượng. Không thêm lời chào, giới thiệu tên, CTA, câu dẫn hoặc tiếng cười. Không nói nhanh để lấp khoảng trống. Nếu take nuốt chữ, rút câu thay vì tăng tốc.

## Những thứ phải khóa trong cả hai clip

- Một Thảo My trưởng thành; mặt/tóc theo ảnh đã chọn, body v002, áo trắng cổ tròn kín và quần short beige cạp cao.
- Ngồi cùng một ghế beige sau cùng bàn gỗ sáng, tường trắng kem trống, sáng từ bên trái khung hình. Không thêm người, cây, đồ trang trí hoặc điện thoại.
- Camera tĩnh ngang tầm mắt khi ngồi, góc thẳng, trung cảnh từ khoảng eo lên. Thấy đủ đầu, hai cẳng tay và mặt bàn; không quay toàn thân hay zoom.
- Đúng 5 đạo cụ: laptop bạc đóng ở giữa; cốc trắng bên phải; sổ cream và bút đen bên trái; dây sạc đen ở phía xa bên phải. Cả hai clip đều laptop đóng, không cần chữ trên màn hình.
- Clip 1: sổ hơi xéo, bút lệch, dây rối nhẹ. Clip 2: sổ/bút thẳng hàng, dây cuộn gọn. Laptop/cốc không đổi vị trí. Dọn bàn xảy ra **ngoài khung thời gian, qua một hard cut**, không bắt Flow biến đổi cả bàn trong một clip.
- Giọng thử nghiệm: nữ trưởng thành, Bắc tự nhiên, cao độ vừa, rõ chữ, hơi cà khịa, không hét. Chưa có giọng cố định; chỉ tạo clip 1 trước, nghe rồi mới quyết định tạo tiếp. Mô tả giọng giống nhau không bảo đảm giọng hai lần sinh giống hệt.

## Ảnh cho từng clip — giữ đúng tên và đúng vai trò

### sh010

1. `input/references/thao-my-body-front-v002.png`: mặt/tóc, trang phục và tỷ lệ người.
2. `input/references/thao-my-expr-smug-front-v001.png`: biểu cảm tự tin/đắc ý nhẹ; không sao chép nền chân dung hoặc crop cận mặt.

### sh020

1. `input/references/thao-my-body-front-v002.png`: cùng nhân vật, cùng trang phục/tỷ lệ.
2. `input/references/thao-my-expr-caught-out-front-v001.png`: phản ứng bị bắt bài, không buồn hay sợ.

Mỗi clip dùng 2 ảnh đơn, dưới giới hạn 3 ảnh người dùng đang gặp. Ảnh cận mặt là tham chiếu biểu cảm của **cùng người**, không phải nhân vật thứ hai. Nếu Flow vẫn nhân đôi người, giảm xuống chỉ ảnh body và giữ mô tả biểu cảm trong prompt. Không tự gửi lại cùng job qua automation khi trạng thái gửi chưa rõ.

## Cách đưa vào Flow — đường A: dùng ảnh tham chiếu trực tiếp

Hướng dẫn theo chức năng; tên nút/chế độ và lựa chọn thực tế cần đối chiếu trên tài khoản, không giả định mọi model có cùng khả năng.

1. Mở chế độ có hỗ trợ ảnh tham chiếu nhân vật/ingredients. Chọn dọc 9:16 và thời lượng 8s nếu tài khoản có các lựa chọn đó. Nếu không có đúng lựa chọn, dừng để điều chỉnh kế hoạch, không âm thầm dùng thông số khác.
2. Làm **sh010 trước**. Upload đúng 2 ảnh ở mục sh010, không upload sheet nhiều mặt hoặc bảng catalog.
3. Copy toàn bộ [input/prompts/sh010.txt](input/prompts/sh010.txt). Không chỉ copy câu thoại. Tạo một take, tải về `generated/sh010/take001.mp4` sau khi xác nhận video hoàn tất.
4. Nghe/xem clip 1 theo checklist bên dưới. Nếu bối cảnh đúng và giọng chấp nhận được, mới làm clip 2.
5. Upload đúng 2 ảnh ở mục sh020, dùng toàn bộ [input/prompts/sh020.txt](input/prompts/sh020.txt). Tải về `generated/sh020/take001.mp4`.
6. Nếu bối cảnh hai clip khác nhau, chuyển sang đường B; không tiêu thêm nhiều lượt chỉ bằng cách thêm hàng loạt câu cấm.

`input/shots.json` đang đóng gói **đường A**, revision 1. Cờ sẵn sàng chỉ nói dữ liệu đã điền đủ cho lần thử; không xác nhận chất lượng Flow và không có nghĩa một runner đã chạy.

## Đường B — nên dùng khi cần khóa căn phòng chặt hơn

Hai ảnh chân dung/body hiện tại không chứa căn phòng. Prompt chữ giúp chỉ định nhưng không khóa được bố cục giống một ảnh cảnh đã chọn. Chuẩn bị ảnh cảnh trước nếu đường A bị lệch; **chưa có hai ảnh cảnh thật trong gói này**.

1. Dùng ảnh body v002 + ảnh smug để tạo một ảnh cảnh duy nhất theo [prep/scene-prompts/sh010-scene.txt](prep/scene-prompts/sh010-scene.txt). Đây là prompt tạo **ảnh tĩnh**, không phải prompt tạo video 8s. Lưu bản chọn thành `input/references/ep001-sh010-start-v001.png`.
2. Từ chính ảnh cảnh sh010 đã chọn, tạo bản chỉnh bàn đã gọn cho sh020 bằng [prep/scene-prompts/sh020-scene.txt](prep/scene-prompts/sh020-scene.txt). Giữ nguyên phòng, camera, nhân vật, laptop và cốc. Lưu `input/references/ep001-sh020-start-v001.png`. Không sinh căn phòng thứ hai chỉ từ văn bản.
3. Với chế độ video nhận ảnh đầu/start frame, dùng ảnh cảnh tương ứng làm ảnh mở đầu. **Không dùng trực tiếp ảnh cận mặt làm start frame** nếu muốn trung cảnh ngồi bàn.
4. Dùng nội dung video prompt tương ứng, nhưng thay đoạn REFERENCE ROLES bằng: “The attached start frame defines the exact woman, room, camera, wardrobe and desk layout. Animate this same scene. Preserve the starting composition and all fixed props.” Bỏ dòng EXPRESSION REFERENCE FILE nếu không đính kèm ảnh đó. Giữ nguyên thoại, diễn xuất, camera, trạng thái bàn và ràng buộc còn lại.
5. Sau khi có file cảnh thật và chọn đường B, tăng revision, sửa `reference_files`, prompt và checksum trong shots.json. Không chạy nguyên JSON đường A rồi kỳ vọng nó tự sử dụng ảnh cảnh mới.

## Nhịp diễn từng clip

### sh010 — Quyết tâm, 0–8s

- 0–0.4s: nhìn bàn với vẻ tự tin.
- Khoảng 0.4–5.5s: nói nguyên câu, đồng thời tay phải chỉ kéo cuốn sổ một đoạn ngắn cho thẳng. Tay trái giữ yên; không cầm laptop/cốc/dây.
- Khoảng 5.5–8s: dừng tay, vẻ tự hài lòng. Không phát sinh thoại.
- Điểm cuối cần giữ: bàn vẫn còn dây rối; chỉ sổ đã ngay hơn. Không yêu cầu hoàn tất dọn toàn bàn trong 8s.

### sh020 — Chốt hài, 8–16s

- Bắt đầu với bàn đã gọn. Hai tay đặt tự nhiên ở mép bàn; không động đạo cụ.
- Khoảng 0.3–1.8s của clip: “Bàn gọn rồi.”
- Khoảng 2.1–4.5s: “Đầu óc cũng trống luôn.” Nụ cười nhẹ tắt, mắt né thoáng qua.
- Khoảng 5–6.2s: “Mai làm vậy.” Giọng tỉnh bơ.
- Khoảng 6.2–8s: nhìn camera, mặt nghiêm, giữ nhịp. Không tự cười câu đùa.

Các mốc là ý đồ diễn, không phải bảo đảm Flow sẽ bám đúng từng phần giây. Chỉ một hành động và một lượt nói mỗi clip; sửa take hoặc trim hậu kỳ theo kết quả thật.

## Checklist trước khi chấp nhận take

- Chỉ một Thảo My; tóc, mặt, trang phục đúng; không ghép thêm người từ hai ảnh input.
- Nghe hết câu, đúng tiếng Việt, không thêm từ; tốc độ tự nhiên, không nuốt câu chốt.
- Hai tay đúng, không xuyên bàn, không dính đạo cụ; sổ không biến thành điện thoại.
- Camera không zoom/cắt; đầu và hai tay không bị crop bất thường.
- sh010 không tự làm sạch toàn bàn; sh020 dùng bàn gọn, giữ nguyên vị trí laptop/cốc.
- Không chữ giả, nhạc/lời khác hoặc tiếng cười tự thêm.
- So giọng clip 2 với clip 1. Nếu lệch rõ, đánh dấu review; chưa tự thay TTS bằng một giọng bất kỳ.

Nếu không đạt: ghi đúng lỗi, chỉ sửa phần gây lỗi, tăng revision khi đổi input; giữ take cũ và ghi số lượt thử. Không giả định thêm ảnh lúc nào cũng cải thiện nhận diện.

## Dựng và đăng

- Ghép sh010 → sh020 bằng một hard cut. Cắt ở lúc tay clip 1 đã dừng; có thể trim phần im lặng nếu nhịp chậm nhưng giữ đủ câu và khoảng chốt.
- Dự kiến 16s trước trim; khóa thời lượng cuối theo file thật. Chưa có clip nên manifest chưa có take, thời lượng khóa hoặc QC đã đạt.
- Không thêm title mở đầu dài, cảnh chuyển, laugh track hoặc CTA kéo dài. Mặc định giao SRT riêng; nếu muốn chữ luôn hiện trên video cần bản burn-in theo yêu cầu.
- Caption đề xuất: “Bàn đã sẵn sàng. Chủ bàn thì chưa. Ai cũng có một kiểu trì hoãn thế này à?”
- Đây là sitcom AI; giữ công bố AI phù hợp khi đăng. Chưa gắn sản phẩm hoặc link affiliate. Chưa có lệnh đăng bài cụ thể.
