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
