# Work log — ep024 Ngủ Không Ngáy

## 2026-11-22 13:30 — Lưu tư liệu nguồn + draft kịch bản, chưa gen

- Richard gửi link share Facebook reel Chuyện đời daily ("Lý do vợ chọn chồng vì ngủ không ngáy", 29,95s) và dặn: kịch bản này nữa.
- Trình duyệt mở được reel (id 1687774499562746, caption + counts đầy đủ) nhưng không phát được video và không tải được file (Getfvid không vào được, FDOWN bị chặn, trình duyệt báo không hỗ trợ download). Bee tải trực tiếp bằng yt-dlp từ link reel Facebook, về đủ file 1440×2560/29,95s/6,99MB, sha256 `fc5caa7b…18dfe`; đối chiếu với bản repost YouTube Shorts https://www.youtube.com/watch?v=43cT_NWE90E (cùng 29,98s). Transcript bằng faster-whisper base local (model tại `~/MoneyPrinterTurbo/models/whisper-base`, đọc audio bằng numpy vì PyAV lỗi `metadata_errors`); đã sửa các lỗi nghe có hệ thống theo ngữ cảnh + chữ phụ đề cháy sẵn trong video + transcript indexed của trình duyệt — cả 3 nguồn khớp từng câu. Soi frame tại 1s/16s/19s/21s/24s/27s để xác nhận người nói từng câu, bối cảnh phòng khách/sofa, váy lụa kem + áo thun be, outro biển hiệu.
- Lưu ý file: bản lưu trong repo là bản hệ thống re-encode (12.890.778 byte, sha256 `a5c04b23…cc16`) — đã kiểm chứng lại bằng Whisper: transcript khớp từng câu với bản gốc, nội dung không đổi. `/tmp` đã bị wipe giữa chừng nên file `/tmp/chuyendoidaily-ngay-fb.mp4` mất; bản repo lấy lại bằng `cp -L` từ symlink `your_files/` → goals dir.
- **15:23 Richard lệnh đổi chiều:** "Đổi thành sao anh lại chọn em" → draft đổi toàn bộ: My hỏi Nam (thay vì chồng hỏi vợ), My nằm gối đầu lên đùi Nam (thay vì chồng nằm lên đùi vợ), "mấy ông kia" → "mấy cô kia".
- **15:23 Richard lệnh kết "Cút.":** "xong đoạn cuối là ThaoMy nói cút" → sh070 My bật dậy, hất đầu anh ra khỏi đùi, nói "Cút.", thay cho reaction câm sốc của reel gốc.
- Viết `script.md` draft: phỏng theo reel gốc, viết lại giọng Bắc, đổi chiều + kết "Cút." theo lệnh, 7 shot × 8s = 56s (bằng ep021 rev2; phương án cắt sh030 → 48s đã ghi trong script). Reel gốc là vợ chồng → draft CHUYỂN thành bạn trai/bạn gái cho khớp chặng 1 hẹn hò của series.
- `episode.yaml` draft: 7 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả.
- Số tập: ep001–023 đều đã có tên nên tập mới là ep024 — slot trống tiếp theo.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip. Bước tiếp theo chờ Richard duyệt kịch bản (và chốt: chàng trai là ai — Nam ep008 (đề xuất) / Thảo ep021 / người mới; giữ đồ theo reel gốc hay đổi đồ; bối cảnh phòng khách lấy location nào).

## 2026-11-22 15:25 — Richard DUYỆT kịch bản, CHỐT Nam ep008

- Richard gật widget "Duyệt, dùng Nam ep008".
- Cập nhật hồ sơ: `script.md` trạng thái → kịch bản đã duyệt 22/11, chàng trai chốt Nam ep008 (mặt `nam-front-v002.jpg`, sha `340a246d…d1f`, nhân vật Flow "Nam" đã tạo ở project ep008, reusable); `episode.yaml` editorial_status `draft` → `script_approved`; `wardrobe.md` cập nhật theo.
- Trang phục My (váy lụa hai dây kem) + bối cảnh phòng khách lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.
- Validator mặc định đạt (exit 0, chỉ thiếu frame/giọng như mọi draft). Commit riêng scope ep024 sau khi validator đạt, không gom file ep009/ep008 đang dở trong repo; push bằng GIT_SSH_COMMAND đã ghi ở AGENTS.md (lỗi host key 22/11).
- Bước tiếp theo: làm 7 frame (project Flow riêng `CNTM · EP024 · Ngủ Không Ngáy`, 0 credit) — chờ Richard gật làm frame, hoặc đổi đồ/location trước.
