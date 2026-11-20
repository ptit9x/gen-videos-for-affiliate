# Work log — ep021 Nợ 800 Triệu

## 2026-11-21 06:38 — Lưu tư liệu nguồn + draft kịch bản, chưa gen

- Richard gửi link share Facebook reel Hoàng Hiếu ("Mới yêu nhau 1 tuần mà anh đã gặp ngay thử thách cuộc đời", 65s, 182 reactions / 17 comments / 8 shares) và dặn: kịch bản ổn, lưu lại ở tập tiếp theo, nhưng chỉ lấy đến đoạn nợ 800tr thôi.
- Trình duyệt mở được reel (id 1426807959536187, caption + counts đầy đủ) nhưng không nghe được audio và không tải được file — lỗi nghe audio xảy ra cả với video YouTube test, tức là lỗi chung của trình duyệt chứ không riêng Facebook.
- Kéo trực tiếp bằng yt-dlp (`python3 -m yt_dlp`) từ link share, về đủ file 720×1280/65,18s/9,0MB, sha256 `6628dfc2…e7757`. Transcript bằng faster-whisper base local; Whisper nghe sai có hệ thống "cưới"→"cửa", "trả"→"chả", "sính lễ"→"xinh lễ" — đã sửa theo ngữ cảnh + chữ trên màn hình "HẸN HÒ 1 TUẦN CƯỚI LUÔN?". Đoạn 56,7–60,8s Whisper lặp câu cuối với độ tin cậy ~0 nên bỏ qua. Soi frame tại 2s/14s/22s/28s để xác nhận bối cảnh quán cà phê sân vườn, váy ren trắng, áo phông trắng.
- Viết `script.md` draft: phỏng theo reel gốc, viết lại giọng Bắc, 6 shot × 8s = 48s, CẮT ĐÚNG ở câu chốt "Trả nợ 800 triệu, là tiền em nợ." (~0:29 reel gốc). Phần sau của reel gốc (có sẵn con gái, đang mang bầu con trai, không biết bố đứa nhỏ là ai) KHÔNG đưa vào, chỉ ghi trong `source-transcript.md` để đối chiếu.
- `episode.yaml` draft: 6 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả.
- Số tập: ep001–020 đều đã có tên (ep009 đã có draft Giỏ hàng) nên tập mới là ep021 — slot trống tiếp theo, Richard đã 👍 xác nhận.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip. Bước tiếp theo chờ Richard duyệt kịch bản (và chốt: giữ 6 shot hay cắt sh040 về 5, sh060 2 người trong 1 shot hay tách 7 shot, chàng trai là ai, trang phục My váy ren trắng hay SANJOLI).

## 2026-11-21 06:51 — Richard chốt tách shot + trang phục (rev2)

- Richard nhắn: sh060 chia thành 2 shot là chuẩn; trang phục mặc áo dài Thanh Nghi tiếp theo.
- script.md rev2: tách sh060 thành sh060 anh hỏi "Trả gì?" + sh070 My đáp "Trả nợ 800 triệu, là tiền em nợ." — giờ 7 shot × 8s = 56s, đúng luật 1 người nói/shot. Trang phục My CHỐT: áo dài Thanh Nghi hồng đậm, quần hồng nhạt, tóc xõa (mặc tiếp sau ep008).
- Tạo `wardrobe.md` mới cho ep021 (ref áo dài + sha như ep008). episode.yaml + manifest lên rev2, target 56s.
- Chưa làm gì thêm: chưa duyệt kịch bản rev2, chưa làm frame, chưa gen clip. Bước tiếp theo chờ Richard duyệt kịch bản rev2 + cấp ảnh chàng trai rồi mới làm frame.
