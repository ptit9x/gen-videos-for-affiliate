# Quản lý từng tập

Dùng [skill thao-my-episode](/Users/richard/.codex/skills/thao-my-episode/SKILL.md) để tạo `05_episodes/epNNN-ten-tap/`; nếu đã có script thì chỉ thêm file thiếu, không copy đè. Quy trình chính ở [AGENTS.md](../AGENTS.md), lệnh kiểm tra ở [validator](../06_automation/README.md).

- `script.md`: ý tưởng, thoại, diễn xuất và storyboard để review.
- `episode.yaml`: hồ sơ sản xuất duy nhất, schema v2; thứ tự `shots` là thứ tự cảnh. Revision nội dung độc lập với phiên bản schema.
- `input/prompts/<shot>-image.txt`: hướng dẫn sửa ảnh; `<shot>-motion.txt`: chỉ prompt video cần paste. Ghi chú/lịch sử nằm ngoài prompt video.
- `input/references/`: ảnh nguồn sửa cảnh, giữ basename gốc. Không đưa trực tiếp vào payload video.
- `input/frames/`: mỗi shot một frame cảnh đã duyệt, lưu riêng/hash trước khi sửa asset Flow tiếp; không thay bằng ảnh body hay tự dựng lại ảnh lịch sử bị thiếu.
- `generated/<shot>/takeNNN.mp4`: clip nguồn không ghi đè. Hồ sơ tập ghi mọi take, ID Flow và lý do loại; thiếu file local thì `file: null` cùng ghi chú trung thực.
- `edit/manifest.yaml`: chỉ take được chọn theo thứ tự dựng, trim nếu có, âm thanh, thời lượng khóa, lệnh dựng và QC; tham chiếu take trong hồ sơ tập.
- `delivery/`: master đạt QC, SRT riêng và báo cáo. Render tạm trong `edit/` trước khi giao.

Mọi đường dẫn tài sản trong hồ sơ tính từ thư mục tập, đi kèm SHA-256 byte file. Chưa có tài sản thì dùng null; draft được kiểm tra cấu trúc nhưng không được vượt cổng generation. Không đặt đường dẫn giả cho file chưa tải.

Khi đổi nội dung/prompt/frame sau gen, tăng revision, giữ tài sản nguồn và lịch sử take; không sửa hồ sơ đang dùng để gửi. Chỉ bấm một lần cho mỗi lượt được yêu cầu; nếu không rõ đã gửi chưa, đối chiếu Flow trước, không tự gửi lại. Không lưu session/cookie/password.

ep001 rev3 dùng mặt mới/body v003, chưa gen frame/clip mới; ID take rev2 được giữ, hai file clip local cũ không tìm thấy khi kiểm tra ngày 2026-11-15. Giọng còn chờ chọn preset. Tồn tại/hash file không chứng nhận hình, âm thanh hay khớp môi. Không tự đăng bài.

---

## Lineup — 20 tập (cập nhật 2026-11-19)

### Solo (giữ nguyên)

| Tập | Tên | Trạng thái |
|---|---|---|
| ep000-pilot1 | Pilot | Đã đăng |
| ep002-ly-do | Lý do | Draft |
| ep003-co-hoi-cuoi | Cơ hội cuối | Draft |
| ep009-gio-hang | Giỏ hàng | Draft |
| ep016-last-christmas | Last Christmas | Draft |
| ep017-bao-gio-lay-chong | Bao giờ lấy chồng | Draft |

### Ngoài series

| Tập | Tên | Câu chốt | Trend |
|---|---|---|---|
| ep007-kham-benh | Khám Bệnh | "Không có thì khỏi cần." | Châm biếm bảo hiểm y tế |

### Series hẹn hò — Thảo My vs 13 chàng trai

| Tập | Chàng | Câu chốt | Trend |
|---|---|---|---|
| ep001-sap-toi | Anh "2 Phút" | "Cút." | Speed date |
| ep004-chia-bill | Anh Chia Bill | "Lập bảng Excel cho bữa ăn" | Chia bill first date |
| ep005-me-anh-bao | Anh "Mẹ Anh Bảo" | "Hẹn hò với anh, không phải với mẹ anh" | Mama's boy |
| ep006-ban-lam | Anh "Bận Lắm" | "Tổng thống cũng tweet hằng ngày" | Situationship |
| ep010-love-bombing | Anh Love Bombing | "Dội bom xong rút quân" | Love bombing → ghost |
| ep011-noi-xau-ex | Anh "Nói Xấu Ex" | "Bốn mối. Lần nào cũng lỗi người ta" | Toxic ex talk |
| ep012-flex | Anh "Flex" | "Đồng hồ limited mà chia bill cà phê" | Thùng rỗng kêu to |
| ep013-gym | Anh Gym | "Em là người yêu hay là client?" | Gym bro date |
| ep014-day-doi | Anh "Dạy Đời" | "Em không cần thầy giáo" | Mansplaining |
| ep015-lo-het | Anh "Lo Hết" | "Anh lo hết — trừ việc hỏi em muốn gì?" | Ga-lăng toxic |
| ep018-cam-dien-thoai | Anh "Cắm Điện Thoại" | "Hẹn hò với wifi thôi, wifi còn kết nối" | Phone addict |
| ep019-chup-anh | Anh Chụp Ảnh | "Hẹn hò hay casting?" | Date for content |
| ep020-nice-guy | Anh "Nice Guy" | "Ba phút. Từ tử tế sang toxic. Nhanh hơn Grab" | Nice guy syndrome |
