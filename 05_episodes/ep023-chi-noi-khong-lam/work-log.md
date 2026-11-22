# Work log — ep023 Chỉ Nói Không Làm

## 2026-11-22 11:10 — Lưu tư liệu nguồn + draft kịch bản, chưa gen

- Richard gửi link Facebook reel Hồ Hùng ("Sao anh nói mà không thấy làm?", 21s, 495K views) và dặn: download kịch bản này. Sau khi tải xong + gửi transcript, Richard gật "có" khi Bee hỏi có viết lại thành draft Thảo My luôn không.
- Trình duyệt mở được reel (id 1503833614936068, caption + counts đầy đủ) nhưng facebook-cli báo chưa kết nối nên không decode/download được bằng connector. Facebook không có nút tải; FDOWN bị Cloudflare Turnstile chặn 3 lần; Getfvid tải được file HD, đã verify trên disk bằng ffprobe (720×1280, 21,076s, 2.245.078 byte, sha256 `0e047e8690418d28dea40a1333ce76e0d49c94632a392c4f173fa0af48d562b7`).
- Transcript: nghe toàn bộ 3 lần trên reel + 1 lần trên file tải về, đối chiếu phụ đề tự động Facebook ở ~3s/~7s/~13s — 5 câu thoại, khớp nhau. Ghi trong `input/references/source-transcript.md`.
- Viết `script.md` draft: phỏng theo reel gốc, giữ nguyên 5 câu thoại (chỉ đổi 1 đại từ ở sh040: "tôi" → "anh" cho nhất quán), 5 shot × 8s = 40s đúng chuẩn series. My im lặng 3 shot đầu (chỉ cười trừ/cúi mặt), chàng trai hỏi 3 lần leo thang rồi gắt, My lật lại ở sh050. Freeze sepia ~5s cuối của reel gốc KHÔNG tách thành shot riêng — giữ trong sh050 + hậu kỳ, để tổng vẫn 40s.
- `episode.yaml` draft: 5 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả.
- Số tập: ep001–022 đều đã có tên nên tập mới là ep023 — slot trống tiếp theo.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip. Bước tiếp theo chờ Richard duyệt kịch bản (và chốt: chàng trai là ai — Nam ep008 (đề xuất) / Thảo ep021 / người mới; giữ đồ theo reel gốc hay đổi đồ; bối cảnh công viên lấy location nào).

## 2026-11-22 12:05 — Richard DUYỆT kịch bản, CHỐT Nam ep008

- Richard gật widget "Duyệt, dùng Nam ep008".
- Cập nhật hồ sơ: `script.md` trạng thái → kịch bản đã duyệt 22/11, chàng trai chốt Nam ep008 (mặt `nam-front-v002.jpg`, sha `340a246d…d1f`, nhân vật Flow "Nam" đã tạo ở project ep008, reusable); `episode.yaml` editorial_status `draft` → `script_approved`; `wardrobe.md` cập nhật theo.
- Trang phục My (áo hai dây hoa + short denim) + bối cảnh công viên lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.
- Validator mặc định đạt (exit 0, chỉ thiếu frame/giọng như mọi draft). Commit riêng scope ep023: `43b4def` (7 file), đã push lên main — chỉ add đúng thư mục ep023, không gom file ep009/ep008 đang dở trong repo.
- Push lần đầu lỗi `Host key verification failed` (2 lần): ssh tìm `~/.ssh` theo getpwuid (root → `/root/.ssh`, trống sau VM replacement) thay vì `$HOME=/home/hatch`, nên không đọc được config + known_hosts đã lưu 17/11. Đẩy được bằng `GIT_SSH_COMMAND="ssh -i /home/hatch/.ssh/id_ed25519_github_bee -o IdentitiesOnly=yes -o UserKnownHostsFile=/home/hatch/.ssh/known_hosts" git push`. Ghi vào `AGENTS.md` để lần sau dùng luôn lệnh này.
- Bước tiếp theo: làm 5 frame (project Flow riêng `CNTM · EP023 · Chỉ Nói Không Làm`, 0 credit) — chờ Richard gật làm frame, hoặc đổi đồ/location trước.
