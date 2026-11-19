# Thư viện bối cảnh

Bốn bối cảnh hiện có; ba bối cảnh chờ người dùng duyệt, riêng nhà hàng buổi tối đã có master (duyệt 2026-11-19):

- [Phòng khách](thao-my-apartment/living-room/README.md): căn hộ tổng diện tích 50 m², diện tích riêng phòng khách chưa chốt.
- [Sân nội khu](apartment-courtyard/README.md).
- [Café hẹn hò](date-cafe/README.md): không gian hư cấu tự thiết kế.
- [Nhà hàng buổi tối](restaurant-evening/README.md): bối cảnh chuẩn ep006 'Hẹn Hò Với Ai', đã duyệt làm master.

Mỗi location có `source/` (ảnh nguồn), `review/` (ứng viên), `approved/` (chỉ ảnh được duyệt), `README.md` (bố cục, ánh sáng, prompt) và `location.json` (trạng thái, file, hash). `master_reference: null` khi chưa duyệt. Không coi yêu cầu tạo ảnh hoặc đồng ý tổ chức folder là duyệt ảnh.

Khi duyệt: copy đúng ảnh vào `approved/`, ghi ngày duyệt, cập nhật master và hash. Không tự sinh thêm góc nếu chưa được yêu cầu. Ảnh location trống dùng để dựng frame có nhân vật; frame theo shot lưu trong tập, không đưa location trống thẳng vào video khi shot cần nhân vật.
