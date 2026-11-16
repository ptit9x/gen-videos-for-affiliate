# Muse Spark — giữ mặt khi thay váy trên Flow

Cập nhật 2026-11-16 theo yêu cầu thử nghiệm và viết lại hướng dẫn. **Chưa kiểm chứng quy trình thay váy trong lần thử này:** bị chặn ở tải ảnh, chưa có đầu ra. Xem `02_characters/thao-my/review/flow-realism-test/README.md`. Không mô tả các bước đề xuất dưới đây là công thức đã thành công.

## Nguồn và mục tiêu

- Nguồn nhận diện: file hiện hành `02_characters/thao-my/approved/thao-my-face-front-v002.png`; xem ảnh thật trước khi dùng và tính lại hash từ byte hiện tại. Không mặc định thumbnail Flow cũ là bản mới chỉ vì cùng tên file. File được xem trong lần thử là selfie ngoài trời, không phải chân dung studio.
- Body ghép `thao-my-body-front-v003-face-v002-review.png` bị người dùng đánh giá thiếu tự nhiên và yêu cầu thử làm lại. Không dùng bản đó làm chuẩn chất da hoặc độ chân thực; không thay master khi chưa có bản mới được duyệt.
- Giữ ý đồ tỷ lệ body v003 đã duyệt; không tự đổi vóc dáng hoặc sao chép cơ thể người mẫu váy. Tách vai trò: mặt/tóc từ v002, tỷ lệ từ body, trang phục từ ảnh váy.
- ep003 dùng váy kem theo wardrobe.md hiện hành; các tập khác đọc hồ sơ riêng. Bộ/màu váy đã được người dùng chọn không cần duyệt lại. Ảnh ghép/frame mới là đầu ra cần đánh giá riêng.

## Thử lại ảnh chính diện tự nhiên — đề xuất chưa kiểm chứng

1. Trong LAB, tải bản mặt hiện hành và ảnh tỷ lệ body đã duyệt. Xác minh đúng thumbnail và giá 0 credit trước gen; nếu có phí mới thì dừng báo chủ dự án.
2. Tạo một ảnh đơn chính diện, góc máy trung tính, cùng tỷ lệ/body và trang phục kiểm tra áo trắng/quần short be. Giữ nhận diện, tóc theo v002, ánh sáng mềm tự nhiên, chất da có chi tiết vừa phải; tránh yêu cầu da hoàn hảo hoặc làm đẹp thêm. Không thay váy/bối cảnh/hành động cùng lượt này.
3. So với mặt v002: mắt, mũi, môi, cằm, đường viền mặt, mái và đường tóc. Kiểm tra ánh sáng mặt/cổ thống nhất, đầu không như dán vào thân, tỷ lệ đầu/thân, vai/tay/chân không biến dạng. Đây là đánh giá thị giác, không khẳng định độ giống bằng điểm số tự động.
4. Nếu lệch mặt, quay về nguồn gốc để thử lại; không sửa tiếp trên bản lệch. Mỗi hướng thử tối đa khoảng 3 lượt rồi đổi cách có lý do hoặc báo hạn chế, không lặp vô hạn cùng prompt. Người dùng đã cho phép tự thử và chọn bản tốt để đề xuất; không tự nâng thành approved.

Prompt khởi đầu (cần điều chỉnh sau khi xem kết quả):

> Use the face photograph as the sole identity and hair reference. Use the approved full-body reference only for body proportions, stance and the white T-shirt with beige shorts. Make a single full-length front-facing photograph of the same adult woman, photographed by another person from a neutral camera angle. Preserve her facial structure and natural hair. Use coherent soft daylight across face, neck and body, subtle natural skin texture and realistic fabric. Keep the approved body proportions. Do not copy the old face from the body reference. No beautification, no reshaping, no collage, no text.

## Thay váy — đề xuất chưa kiểm chứng

1. Dùng ảnh Thảo My đạt kiểm tra nhận diện làm ảnh nền để chỉnh. Nếu là bản review chưa được người dùng duyệt, chỉ dùng trong thử nghiệm riêng, không dùng để gen video sản xuất.
2. Chuẩn bị bản tham chiếu váy riêng từ ảnh sản phẩm: tránh mặt người mẫu, bảng size/logo/nền thừa. Giữ nguyên nguồn, lưu bản dẫn xuất riêng và mô tả cách tạo; chưa tạo bản tách váy trong lần thử bị chặn này.
3. Nếu UI có chọn vùng, chỉ chọn quần áo, tránh mặt/tóc. Nếu không có, dùng prompt giới hạn thay đồ nhưng không coi đó là khóa tuyệt đối. Giữ tư thế/góc máy/nền/ánh sáng, chưa thêm cảnh diễn cùng lượt.
4. Chỉ khi bản mặc váy giữ mặt tốt mới thử thay màu trên chính bản đó; không cần nạp lại toàn bộ ảnh người mẫu mỗi màu. Mỗi lần đều so mặt với nguồn gốc.
5. Dựng bối cảnh/pose thành bước riêng sau đó. Kiểm tra lại nhận diện vì mọi lượt sửa đều có thể lệch mặt. Frame cho video phải được người dùng duyệt; video vẫn Frames trực tiếp, Agent tắt, chỉ một frame đầu.

Prompt thay đồ:

> Edit Image A only. Replace only her clothing with the cream spaghetti-strap maxi dress shown in Image B. Image A is the sole reference for her identity and body proportions. Image B is a garment reference only. Preserve her facial features, hair, expression, pose, camera angle, lighting and background. Do not copy the model's face, body shape, accessories or background from Image B.

## Lưu bản thử và đánh dấu tốt

- Giữ nguồn; tải từng đầu ra về review/ với tên riêng. Lưu model, project, prompt thật, nguồn/hash, số lượt và nhận xét. Không tạo thư mục prep chỉ để giữ phiên bản trong công việc này.
- Dùng các mức `rejected`, `candidate`, `recommended`; ghi lý do cụ thể và hạn chế. Recommended nghĩa người thực hiện đề xuất sau khi xem ảnh, khác với user-approved.
- Tiêu chí bản tốt: giống nhận diện gốc, mặt/cổ/thân thống nhất ánh sáng, tỷ lệ đúng, vải và tay/chân tự nhiên, không trộn mặt/body người mẫu. Đẹp nhưng thành người khác thì loại.
- Tạo README chỉ rõ file recommended và trình ảnh cho chủ dự án. Chỉ cập nhật approved và tham chiếu sản xuất sau duyệt rõ. Lần thử hiện tại chưa có file recommended.
- Nếu tải ảnh/quan sát UI không tin cậy, dừng gen và ghi blocker; không tự đổi sang công cụ tạo ảnh khác hoặc báo thành công.

## Lưu ý định dạng nguồn đã kiểm tra

Trong lần kiểm tra, file mặt v002 đuôi .png nhưng nội dung JPEG. Bản sao .jpg nguyên byte đã lưu trong review/flow-realism-test để upload, không đổi master. Hộp tải vẫn chưa hoàn tất; chưa kết luận lỗi định dạng là nguyên nhân. Luôn kiểm tra định dạng thực và hash khi file nguồn được cập nhật bên ngoài.
