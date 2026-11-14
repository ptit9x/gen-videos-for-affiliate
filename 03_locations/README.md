# Thư viện bối cảnh

Ba bối cảnh hiện có đều chờ người dùng duyệt, chưa có location master:

- [Phòng khách](thao-my-apartment/living-room/README.md): căn hộ tổng diện tích 50 m², diện tích riêng phòng khách chưa chốt.
- [Sân nội khu](apartment-courtyard/README.md).
- [Café hẹn hò](date-cafe/README.md): không gian hư cấu tự thiết kế.

Mỗi location có `source/` (ảnh nguồn), `review/` (ứng viên), `approved/` (chỉ ảnh được duyệt), `README.md` (bố cục, ánh sáng, prompt) và `location.json` (trạng thái, file, hash). `master_reference: null` khi chưa duyệt. Không coi yêu cầu tạo ảnh hoặc đồng ý tổ chức folder là duyệt ảnh.

Khi duyệt: copy đúng ảnh vào `approved/`, ghi ngày duyệt, cập nhật master và hash. Không tự sinh thêm góc nếu chưa được yêu cầu. Ảnh location trống dùng để dựng frame có nhân vật; frame theo shot lưu trong tập, không đưa location trống thẳng vào video khi shot cần nhân vật.
