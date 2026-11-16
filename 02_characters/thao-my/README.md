# Bộ ảnh Thảo My hiện hành

Cập nhật 2026-11-16: người dùng chọn ảnh mặt/tóc v002 mới. Giữ vóc dáng body v003 đã duyệt 2026-11-15. Mặt và tóc trong ảnh body v003 cũ không còn là chuẩn nhận diện.

## Ảnh đã duyệt

- [Mặt và tóc v002](approved/thao-my-face-front-v002.png): chuẩn khuôn mặt, tóc và thần thái hiện hành.
- [Mặt v001](approved/thao-my-face-front-v001.png): giữ lịch sử, không dùng làm chuẩn hiện hành.
- [Body chính diện hiện hành](approved/thao-my-body-front-v003-face-v002-review.png): người dùng chọn 2026-11-16; giữ nguyên tên file đã chỉ định.
- [Body chính diện v003 gốc](approved/thao-my-body-front-v003.png): lịch sử.
- [Body nghiêng trái khung hình](approved/thao-my-body-profile-screen-left-v003.png).
- [Body phía sau](approved/thao-my-body-back-v003.png).

Body mặc áo thun trắng, quần short be, chân trần. Không suy ra số đo chính xác từ ảnh. Chưa kiểm chứng bộ mới trong Flow.

## Sử dụng

Dùng đúng tên PNG; copy ảnh cần dùng vào `input/references/` của tập và ghi SHA-256 trong `episode.yaml`. Chọn ảnh đơn phù hợp, không dùng sheet. Sửa ảnh cảnh từ ảnh tham chiếu; video chỉ nhận một frame cảnh đầu đã duyệt. Không dựng lại mặt bằng chữ. `screen-left` là hướng mặt trên khung hình; không lật ảnh.

Trang phục tham chiếu body không thay trang phục tập: váy maxi satin đen SANJOLI vẫn theo hồ sơ hiện hành. Ảnh trong `wardrobe/` chỉ tham chiếu trang phục. Giọng VieNeu-TTS nữ miền Bắc đã chốt preset Đoan Trang; tắt tiếng gốc Veo khi dựng.

## Xuất xứ

- [Prompt mặt](review/face-reference-2026-11-15/README.md).
- [Prompt body](review/body-v003/README.md).
- `references.json`: danh mục hiện hành và SHA-256.
- Bộ ảnh cũ và bản lưu trữ đã xoá hẳn theo yêu cầu người dùng ngày 2026-11-15; chỉ dùng bộ mới.
- Giữ ảnh nguồn trong `source/` để lưu xuất xứ. Không thay tài sản hay hồ sơ tập đã tạo.

## Nhận diện theo ảnh mẫu 2026-11-16

Mặt trái xoan mềm, cằm gọn không nhọn; mắt nâu sẫm dáng hạnh nhân, mày khá ngang và cong nhẹ ở đuôi. Sống mũi thanh, đầu mũi tròn; môi hồng san hô, môi dưới đầy hơn, cười nhẹ khép môi. Có nốt nhỏ dưới môi lệch phải ảnh, không tự lật vị trí. Tóc nâu sẫm, rẽ gần giữa, mái thưa tách lọn mảnh, tóc dài uốn sóng lớn. Ảnh là chuẩn; mô tả chỉ hỗ trợ, không thay ảnh.

Ánh sáng cửa sổ ấm không quyết định màu da/tóc cố định. Váy trắng ngà cổ V, tay phồng và trang sức trong ảnh không phải trang phục mặc định. Ảnh bán thân không dùng để suy ra chiều cao hoặc số đo.

- Nguồn nguyên bản: `source/face-hair-reference-2026-11-16.jpg`, người dùng gửi và chọn trong chat ngày 2026-11-16. PNG v002 chuyển định dạng từ nguồn, không chỉnh sửa nhận diện.
- Body chính diện bản ghép đầu tiên đã được duyệt; hai góc nghiêng/sau ghép v002 chưa duyệt. Các góc body v003 gốc chỉ lưu lịch sử, không dùng mặt/tóc cũ thay chuẩn mới.
- Chưa kiểm chứng mặt/tóc mới hoặc tổ hợp với body v003 trong Flow. Không sửa hồi tố frame/take/hồ sơ revision cũ.


## Lựa chọn cuối 2026-11-16

Người dùng chốt mặt `thao-my-face-front-v002.png` và body `thao-my-body-front-v003-face-v002-review.png` từ bộ ghép đầu tiên. Bản body đã copy nguyên byte sang approved, giữ nguồn review. Bỏ hướng giữ mặt cũ chỉ tăng độ dày tóc; các bản hair-density-r02 và face-correction không được chọn. Không tự suy rộng duyệt sang hai góc còn lại. Không tự gen video.
