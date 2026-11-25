# Work log — ep030 Gym (lúc viết là ep013, đổi số 25/11)

## 2026-11-18 — Draft Gym r02, chưa duyệt

- Script r02: đối thoại trực tiếp Thảo My ↔ Tuấn (Gym bro date), 4 shot × 8s = 32s. Ảnh tạo hình Tuấn đã duyệt trong bộ casting-2026-11-18 ("ok ổn").
- Trạng thái: draft chờ review, chưa duyệt gen. Trang phục theo tập chưa chốt, location quán ăn/nhà hàng chưa duyệt.

## 2026-11-25 16:37 — Đổi số ep013 → ep030 + rebuild yaml (phát hiện yaml lệch)

- Richard chốt: 'Chỉ Biết Dễ Thương' (lúc đó là ep030) làm sớm hơn, đổi thành ep013; Gym lùi xuống ep030.
- Khi kiểm kê để đổi số mới phát hiện `episode.yaml` + 8 prompt trong thư mục vẫn thuộc tập "Đêm Noel" (mồ côi từ đợt đổi số 20/11, không còn tập nào dùng) — title, thoại, prompt đều là Noel, lệch hoàn toàn với script Gym r02.
- Xử lý (theo skill profile-check: rebuild toàn bộ khi lệch chạm 3 file trở lên):
  - `git mv` thư mục ep013-gym → ep030-gym.
  - Rebuild `episode.yaml` theo đúng script Gym r02: episode_id ep030, title Gym, 4 shot với đúng thoại r02, prompt null, image_sources mặt + body (sha đã verify bằng shasum).
  - `edit/manifest.yaml`: episode_id ep013 → ep030.
  - 8 prompt Noel cũ chuyển nguyên vào `prep/noel-stale-2026-11-20/` + README giải thích, không xóa.
  - `script.md`: header ep013 → ep030; số tiếng sh020 sửa 12 → 13 (đếm lại tay); thêm ghi chú đổi số vào mục Lịch sử.
  - `prep/before-dialogue-r02/script.md` (bản r01): header ghi rõ lúc viết là ep013.
  - File casting Tuấn (`02_characters/casting-2026-11-18.*`, `02_characters/tuan/*`): episode ep013 → ep030. Tracker + README tập cập nhật theo (xem commit đổi số).
- Validator chạy sau rebuild — xem entry dưới.
- Trạng thái sau đổi số: vẫn draft, chưa duyệt, chưa làm frame, chưa gen clip. Không có gì khác thay đổi về nội dung Gym.

## 2026-11-25 — Profile check sau đổi số (theo skill sitcom_episode_profile_check)

- Đối chiếu script r02 ↔ episode.yaml rebuild: 4/4 thoại khớp từng chữ, số tiếng 13/13/15/13 (trong ngân sách 8s), validator đạt (exit 0; chỉ note thiếu frame 4/4 shot + voice pending — đúng trạng thái draft).
- Cờ vàng (có từ draft r02 gốc 18/11, KHÔNG tự sửa thoại vì draft chưa duyệt): sh010 2 câu, sh020 3 câu, sh030 2 câu — vi phạm luật 1 shot = 1 câu. Khi nào Richard duyệt/review lại kịch bản Gym thì đề xuất tách/cắt ở bước đó; hiện tại giữ nguyên thoại r02.
- Manifest vẫn là placeholder (voice pending) — tới bước edit mới rebuild theo plan giọng trong script (My native-nếu-Bắc không thì clone ThaoMy, Tuấn giọng nam miền Bắc, không lồng ThaoMy vào Tuấn).
