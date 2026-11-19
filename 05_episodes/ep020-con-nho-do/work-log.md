# Work log — ep020 Con Nhỏ Đó

## 2026-11-19 22:13 — Lưu tư liệu nguồn + draft kịch bản, chưa gen

- Richard gửi link share Facebook reel Hey Men Comedy ("Yêu khổ quá thôi dẹp nghỉ hết đi", 63s, 352K views).
- facebook-cli báo chưa kết nối nên không đọc qua connector được; kéo trực tiếp bằng yt-dlp từ link share, về đủ file 1080×1920/63,37s/24MB, sha256 `9a71ae6d…0c450`.
- Transcript dựng từ phụ đề burn-in trong video (soi frame 2s/lần) + kiểm chéo faster-whisper base. Câu cuối nam bỏ đi nghe không chắc, đã ghi rõ "không chắc" trong `source-transcript.md`, không bịa.
- Viết `script.md` draft: phỏng theo reel gốc, viết lại giọng Bắc, 5 shot × 8s = 40s. Bỏ tát + bỏ chửi thề của bản gốc (ghi rõ trong script để Richard chốt). Chàng trai chưa chốt là ai trong 13 người; trang phục My chưa chốt; chưa affiliate.
- `episode.yaml` draft: 5 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip. Bước tiếp theo chờ Richard duyệt kịch bản (và chốt: 5 shot hay gộp 4, chàng trai là ai, có giữ độ đanh đá kiểu khác thay cho tát hay không).

## 2026-11-20 00:08 — Richard bảo sẽ cấp chàng trai + trang phục sau

- Cập nhật `script.md`: chàng trai (ảnh nhân vật) và trang phục My đều do Richard gửi sau — chờ cậu ấy cấp rồi mới khóa mặt/đồ, ghi `wardrobe.md` và làm frame. Không tự chọn người hay đồ trước.
- Commit + push riêng ep020 (không đụng các thay đổi ep005 chưa commit của luồng khác).
