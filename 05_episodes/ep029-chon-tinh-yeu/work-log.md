# Work log — ep029 Chôn Tình Yêu

## 2026-11-24 09:10 — Richard gửi ảnh truyện 4 khung, hỏi "Thêm kịch bản này đc ko? Nghe hơi kinh dị kaka"

- Ảnh truyện: 4 khung, đêm trăng sân vườn, My đào hố, anh hỏi "Em đang đào gì vậy??", My "Em đang đào hố chôn tình yêu", anh "Nhưng tình yêu này đã chết đâu?", My "Tình yêu này đã chết..." + close-up cười lạnh "...vào cái khoảnh khắc mày cưới vợ con bé pha chế nước rồi."
- File gốc lưu tại `input/references/source-comic-chon-tinh-yeu.jpg` (1024×1024, sha256 `e0bf88b1f0cc53b8eb5b1da22757b8f837b0698cd019f1f382ee877011d37560`). Transcript gốc lưu tại `input/references/source-transcript.md` (tóm tắt, không chép nguyên văn toàn bộ chữ trong ảnh).

## 2026-11-24 09:10 — Viết draft ep029, 5 shot × 8s = 40s

- Viết `script.md` draft: giữ nguyên 5 câu thoại gốc, tách thành 5 shot (khung 3 và khung 4 của truyện tách riêng để câu chốt có trọn 8s).
- `episode.yaml` draft: 5 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả, `editorial_status: draft`.
- `wardrobe.md` draft: My hoodie kem/be + quần đen theo truyện gốc; chàng trai áo thun xám + jean đen.
- Số tập: ep026–ep028 đã giữ cho 3 draft Ghost (script-only, chưa lưu repo) nên tập mới là ep029.
- Chàng trai CHƯA CHỐT: draft đề xuất người yêu cũ mới, mặt mới — vì anh đã cưới vợ khác, dùng Nam/Dũng/Thảo sẽ phá continuity chặng hẹn hò. Chờ Richard chọn.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip, chưa commit repo.

## 2026-11-24 09:16 — Richard DUYỆT kịch bản, CHỐT Nam ep008

- Richard gật widget "Duyệt, dùng Nam ep008" (sau khi nghe cảnh báo continuity trong draft).
- Cập nhật hồ sơ: `script.md` trạng thái → kịch bản đã duyệt 24/11, chàng trai chốt Nam ep008; `episode.yaml` editorial_status `draft` → `script_approved`; `wardrobe.md` cập nhật theo (Nam áo thun xám + jean đen theo truyện gốc).
- Ghi rõ trong script + wardrobe: trong tập này Nam là người yêu cũ đã cưới vợ khác → câu chuyện là quá khứ / ngoại truyện, không phải dòng hẹn hò hiện tại của Nam với My.
- Trang phục My (hoodie kem/be + quần đen) + bối cảnh sân vườn ban đêm lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.
- Lưu hồ sơ vào repo: commit riêng scope ep029, chạy validator trước, push lên main.
- Bước tiếp theo: làm 5 frame (project Flow riêng `CNTM · EP029 · Chôn Tình Yêu`, 0 credit) — lấy lại nhân vật Nam từ project ep008 qua picker, tạo location sân vườn ban đêm mới — chờ Richard gật làm frame, hoặc đổi đồ/location trước.
