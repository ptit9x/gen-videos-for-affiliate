# Bộ ảnh Thảo My hiện hành

Cập nhật 2026-11-16: người dùng chọn ảnh mặt/tóc v002 mới. Giữ vóc dáng body v003 đã duyệt 2026-11-15. Mặt và tóc trong ảnh body v003 cũ không còn là chuẩn nhận diện.

## Ảnh đã duyệt

- [Mặt và tóc v002](approved/thao-my-face-front-v002.png): chuẩn khuôn mặt, tóc và thần thái hiện hành.
- [Mặt v001](approved/thao-my-face-front-v001.png): giữ lịch sử, không dùng làm chuẩn hiện hành.
- [Body chính diện](approved/thao-my-body-front-v003.png).
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
- Bản body cập nhật mặt/tóc: `review/body-v003-face-v002/`, chờ người dùng duyệt, không thay bộ body v003 gốc.
- Chưa kiểm chứng mặt/tóc mới hoặc tổ hợp với body v003 trong Flow. Không sửa hồi tố frame/take/hồ sơ revision cũ.

## Tinh chỉnh cuối ngày 2026-11-16

Người dùng yêu cầu giữ thay đổi nhỏ vì đã đăng video; ưu tiên tóc dày và đẹp hơn, không tiếp tục chỉnh mắt/má/nụ cười. Bộ `review/body-v003-face-v002/hair-density-r02/` là bộ mới nhất đề xuất để duyệt. Các lượt chỉnh mặt trước đó giữ trong `face-correction-superseded/`, không chọn làm hướng sản xuất. Ảnh mẫu v002 tiếp tục lưu làm tham chiếu; không diễn giải thành yêu cầu làm lại khuôn mặt.
