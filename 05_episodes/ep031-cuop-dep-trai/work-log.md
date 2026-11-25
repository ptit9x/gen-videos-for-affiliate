# Work log — ep031 Cướp Đẹp Trai

## 2026-11-25 20:27 — Richard gửi link Facebook, "update kịch bản ... thêm kịch bản này"

- Link: https://www.facebook.com/share/r/1Ctg73UQ9Q/?mibextid=wwXIfr → reel https://www.facebook.com/reel/1655734339670095 (Táo Đen Shop, verified, caption "POV: Bị cướp nhưng cướp đẹp trai cao 1m8 😭", ~53s ước chừng, 13,6K reactions / 101 comment / 97 share lúc xem 25/11).
- Facebook connector chưa kết nối nên không decode được bằng facebook-cli (lỗi "not connected"); mở bằng trình duyệt cloud, không cần đăng nhập, không post/like/comment/share/download gì. Tóm tắt nguồn lưu tại `input/references/source-facebook.md`.
- Transcript gốc KHÔNG chắc từng chữ: reel không có phụ đề, thoại nhanh + chồng lấn + ồn đường phố, trình duyệt nghe lại nhiều lần vẫn đánh dấu nhiều câu "wording uncertain" (nhất là đoạn giữa đưa đồ). Draft không chép nguyên văn — chỉ giữ cấu trúc + ý thoại, viết lại hoàn toàn sang giọng Bắc.

## 2026-11-25 20:35 — Viết draft ep031, 6 shot × 8s = 48s

- Viết `script.md` draft: chuyển thể cấu trúc gốc (hỏi lịch sự → có người yêu chưa → khen trai cao 1m8 → đưa điện thoại + chìa khóa xe → chốt "Còn em nữa, anh lấy em đi!"), giữ nguyên ý thoại gốc, viết lại theo giọng Bắc Thảo My.
- `episode.yaml` draft: 6 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả, `editorial_status: draft`.
- `wardrobe.md` draft: My áo thun xanh nhạt ôm + chân váy sáng màu theo reel gốc, móng đỏ đậm (khác chuẩn móng tự nhiên — cần Richard chốt); đạo cụ túi hồng + iPhone + chìa khóa xe; location đường phố ban ngày là mới, chưa có master.
- `edit/manifest.yaml`: placeholder copy theo ep013 (chưa tới bước dựng) — tới bước edit sẽ rebuild theo plan giọng trong script (My native-nếu-Bắc không thì clone ThaoMy, cướp sh030 giữ native).
- Số tập: ep026–ep028 đã giữ cho 3 draft Ghost (script-only, chưa lưu repo); ep029, ep030 đã có trong repo nên tập mới là ep031.
- Chàng trai CHƯA CHỐT lúc draft: đề xuất A giữ POV không mặt (khuyến nghị — không cần khóa mặt nam mới, đúng góc reel gốc); phương án B dùng Nam ep008 làm cướp (lệch continuity, chỉ khi Richard muốn thấy mặt). Chờ Richard chọn.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip, chưa commit repo.

## 2026-11-25 20:38 — Richard DUYỆT kịch bản, CHỐT cướp POV không mặt

- Richard gật widget "Duyệt draft, giữ POV không mặt".
- Cập nhật hồ sơ: `script.md` trạng thái → kịch bản đã duyệt 25/11, chàng trai chốt POV không lộ mặt (phương án B dùng Nam ep008 đã bỏ); `episode.yaml` editorial_status `draft` → `script_approved`; `wardrobe.md` cập nhật theo (không cần mặt/trang phục nam).
- Trang phục My (áo thun xanh nhạt + chân váy sáng, móng đỏ đậm theo reel gốc) + bối cảnh đường phố lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.
- Đối chiếu script ↔ episode.yaml (profile check): 6 shot, thoại khớp từng chữ, số tiếng đếm tay 14/6/1/13/14/7, mỗi shot đúng 1 câu, đều trong ngân sách 8s. Không có prompt ảnh/motion hay manifest âm thanh để đối chiếu (chưa tới bước đó). Validator đạt (exit 0; chỉ note thiếu frame 6/6 shot + voice pending — đúng trạng thái draft đã duyệt, như ep013/ep029).
- Lưu hồ sơ vào repo: commit riêng scope ep031, chạy validator trước, push lên main.
- Bước tiếp theo: làm 6 frame (project Flow riêng `CNTM · EP031 · Cướp Đẹp Trai`, 0 credit) — cần ảnh nền đường phố ban ngày đồng bộ 6 shot (location mới, chưa có master) + tay cướp POV vào khung từ mép/trên cao. CHỜ Richard gật làm frame — không tự gen, vì ep012 master r05 vẫn đang làm dở ở chat khác và quy tắc không chạy 2 task Flow song song.

## 2026-11-25 20:39 — Richard thêm 2 điểm sau khi duyệt: ốp iPhone + áo dài

- "còn điểm nữa là ốp iphone như mọi khi nhé, sản phẩm ấy" → điện thoại My là iPhone trong ốp lưng trong suốt MagSafe Slimcase aff-0003 (https://s.shopee.vn/AKcGpsTOV8, active, đích đã xác minh 19/11) như ep006/ep009. Ảnh sản phẩm 02 đã copy vào `input/references/slimcase-phone-ref.jpg` (sha `e492d33a…`, byte-identical với `04_products/prd-0003/`, đúng ảnh ep009 đã dùng). Khi làm frame: dùng ảnh này làm ref ốp + ghi dòng ốp Slimcase vào image prompt từng shot như ep009. Link ốp gắn bằng comment Page sau khi đăng (mẫu ep009 plc-0011), không vào mô tả.
- "áo dài nữa" → My mặc áo dài thay áo thun + chân váy của reel gốc. Tao chọn **Vân Linh xanh nhạt** (đã dùng ep008/ep011, có sẵn trong Flow project ep008 asset `9a824890`, lấy lại qua picker — không upload mới) vì đó là áo dài đã chứng minh trong Flow; Mai Linh đỏ đô (aff-0007, ep012) và Thanh Nghi hồng đậm là phương án đổi, đã ghi trong wardrobe.md để Richard đổi trước khi làm frame nếu muốn. Ảnh ref đã copy vào `input/references/aodai-van-linh-xoa-v3.jpg` (sha `2f71722d…`, đúng file ep008). Lưu ý: tay trái ảnh này cầm vật vàng — frame phải để tay trống.
- Cập nhật: `script.md` (trạng thái + trang phục My + đạo cụ + affiliate), `wardrobe.md` (áo dài Vân Linh + ốp Slimcase + cách gắn aff-0003). Thoại 6 shot KHÔNG đổi nên không cần duyệt lại thoại; đối chiếu lại script ↔ episode.yaml vẫn khớp (validator chạy lại trước commit).
- Commit lần này gộp cả duyệt draft 20:38 + 2 điểm thêm 20:39 (chưa commit riêng lúc duyệt vì 2 tin nhắn tới liền nhau) — xem commit message.

## 2026-11-25 20:42 — Richard "ok" = chốt móng đỏ đậm + gật làm frame

- Bee hỏi "móng đỏ đậm hay về tự nhiên?" + "bước tiếp theo là làm 6 frame, đang chờ mày gật"; Richard đáp "ok" → hiểu là: giữ móng đỏ đậm theo draft + bắt đầu làm 6 frame.
- Cập nhật: móng đỏ đậm CHỐT trong `script.md` + `wardrobe.md`.
- Kiểm tra trước khi giao frame: không có task Flow nào khác đang chạy (browser windows chỉ còn task Facebook reel đã completed) — ep012 ở chat khác đang làm master r05 local (dub + dựng), không phải task Flow, nên không vi phạm quy tắc không chạy 2 task Flow song song.
- Giao trình duyệt làm 6 frame (project Flow riêng `CNTM · EP031 · Cướp Đẹp Trai`, sửa ảnh Nano Banana 0 credit): mặt lấy lại ThaoMy002 qua picker (project EP003), áo dài Vân Linh xanh nhạt lấy lại qua picker từ project ep008 (asset `9a824890`), ốp Slimcase + mặt chuẩn local làm ref dự phòng, nền đường phố ban ngày đồng bộ 6 shot, tay cướp POV chỉ tay/cánh tay không mặt.
