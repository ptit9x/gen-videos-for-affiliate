# Work log — ep022 Hoa Tự Mua

## 2026-11-21 19:10 — Lưu tư liệu nguồn + draft kịch bản, chưa gen

- Richard gửi link share Facebook reel Thiện Dịu Dàng ("Hoa ai tặng em đấy?", 16,8s, 12.200 likes / 430 comments) và dặn: thêm kịch bản này vào git.
- Trình duyệt mở được reel (id 39251138994529710, caption + counts đầy đủ) nhưng facebook-cli báo chưa kết nối nên không decode được link share bằng connector.
- Kéo trực tiếp bằng yt-dlp (`python3 -m yt_dlp`) từ link reel, về đủ file 1440×2560/16,77s/3,8MB, sha256 `8266376c…533d3`. Transcript bằng faster-whisper base local; Whisper nghe sai có hệ thống "Hoa"→"Hòa" ở 2 câu (p=0,63–0,87) — đã sửa theo ngữ cảnh + chữ trên màn hình giây 1 "Hoa ai tặng em đấy?". Soi frame tại 1s/6,5s/9,5s/12,5s để xác nhận người nói từng câu, bối cảnh phòng ngủ/bàn trang điểm, đồ ngủ kem + sơ mi tối.
- Viết `script.md` draft: phỏng theo reel gốc, viết lại giọng Bắc, 4 shot × 8s = 32s, giữ nguyên 4 câu thoại gốc. Reel gốc là vợ chồng dịp 20/10 — draft CHUYỂN thành bạn trai/bạn gái cho khớp chặng 1 hẹn hò của series, bỏ mốc 20/10 cụ thể (đã qua hơn 1 tháng, nay 21/11) để đăng lúc nào cũng được; cả 2 điểm này ghi rõ trong script.md chờ Richard chốt.
- `episode.yaml` draft: 4 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả.
- Số tập: ep001–021 đều đã có tên nên tập mới là ep022 — slot trống tiếp theo.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip. Bước tiếp theo chờ Richard duyệt kịch bản (và chốt: chàng trai là ai — Nam ep008 / Thảo ep021 / người mới; giữ đồ ngủ hay đổi đồ; có thêm sh050 phản ứng câm của chàng trai để kết tập thành 40s không).
