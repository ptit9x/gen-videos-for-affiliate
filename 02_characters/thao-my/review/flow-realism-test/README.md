# Thử độ tự nhiên và thay váy — 2026-11-16

## Kết quả thực tế

- Đã xem file mặt v002 hiện tại: ảnh dọc 720×1280, selfie hơi cao, tóc dài gợn và ánh sáng ngoài trời. Đề xuất dùng làm nguồn nhận diện, không lấy phối cảnh selfie làm tỷ lệ toàn thân.
- Người dùng nhận xét body chính diện ghép v002 “khá là ảo”, yêu cầu làm lại cho tự nhiên; không yêu cầu đổi vóc dáng. Giữ bản cũ để đối chiếu, không lấy độ mịn/kiểu dựng cũ làm mục tiêu.
- Đã tạo project Flow thử nghiệm: https://flow.google.com/project/b8892ffa-8616-4c50-af95-431b77e67968. Tên UI lưu bị lặp: `CNTM LAB Thao MCNTM LAB Thao My`; chưa sửa được tên cuối.
- UI cho thấy chế độ ảnh, Nano Banana 2.1, giá 0 credit. Chưa hoàn tất tải ảnh, chưa bấm gen. Không có đầu ra mới và không có bản được đánh dấu tốt.
- Điều khiển Chrome không đáng tin cậy trong lần chạy: ảnh chụp không khớp AX, nút tải chưa hoàn tất, thao tác tọa độ lỗi `noWindowsAvailable`. Không coi thao tác nhập/chọn chưa xác minh là đã thành công.

## Nguồn tải lên

File approved `thao-my-face-front-v002.png` thực tế chứa dữ liệu JPEG. `thao-my-face-front-v002-upload.jpg` là bản sao nguyên byte, chỉ đặt đuôi đúng cho việc upload, không chỉnh hình hoặc đổi master. Chưa chứng minh đây là nguyên nhân nút Open bị vô hiệu; bản JPG cũng chưa tải thành công.

Hash nguồn và trạng thái lần thử tại trial-log.json. Chưa cập nhật approved/references hoặc hồ sơ tập; chưa gen video.

## Tiếp tục

Theo `00_docs/flow-wardrobe-identity.md`. Cần khôi phục điều khiển Chrome trước, thử upload và xác minh thumbnail nguồn, rồi mới gen. Chỉ đánh dấu recommended sau khi nhìn trực tiếp ảnh kết quả; đó là đề xuất của người thực hiện, không phải user-approved.

## Tiếp tục sau khi người dùng tải nguồn

Đã xác nhận hai asset `thao-my-face-front-v002-upload.jpg` và `thao-my-body-front-v003.png` trong LAB; thumbnail mặt đúng ảnh selfie hiện tại. Asset mặt: `77ea1282-9046-4306-8010-6542ff2e339d`. Đã thử thêm tham chiếu nhưng chưa xác nhận được attachment; UI điều khiển tiếp tục lỗi/ảnh chụp đen, chưa gen. Prompt chuẩn bị sẵn tại `body-natural-trial-01-prompt.txt`, chưa gửi.
