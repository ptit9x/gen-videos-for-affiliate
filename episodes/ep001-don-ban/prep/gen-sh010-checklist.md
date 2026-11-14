# Pre-flight ep001 + Checklist gen sh010 — Chuyện Nhà Thảo My

Ngày kiểm tra: 2026-11-14 (giờ Saigon)
Tập: ep001-don-ban — "Dọn bàn xong hết giờ làm", revision 1

## Kết quả pre-flight: ĐẠT — sẵn sàng gen sh010

Chạy thật validator của chính dự án (`automation/validate_episode.py`) trên bản copy nguyên byte từ Mac sang VM của Muse:

- **Validator: `Input valid; no Flow job submitted.` — exit code 0.**
- Hash SHA-256 khớp 5/5 với khai báo trong `input/shots.json`:
  - `prompts/sh010.txt` — 26341c9c…
  - `prompts/sh020.txt` — a038f726…
  - `references/thao-my-body-front-v002.png` — 956b84c2…
  - `references/thao-my-expr-smug-front-v001.png` — 6febe96f…
  - `references/thao-my-expr-caught-out-front-v001.png` — ad9b6727…
- `episode.yaml` khớp `shots.json`: episode_id ep001, revision 1, shot_order [sh010, sh020], canvas 1080×1920, mục tiêu 16s.
- `approved_for_generation: true` — cờ này chỉ nói gói dữ liệu đã đủ, không phải đã chạy Flow.
- Prompt không có placeholder (quét TODO/TBD/DRAFT/{{…}}/[…]: sạch).
- Thoại: sh010 = **11 từ**, sh020 = **11 từ** — dưới trần 12–18 từ/clip 8s, an toàn ở mức ngắn (kịch bản ghi ước lượng ~12, đếm thật là 11).
- Ảnh tham chiếu sh010: đúng 2 ảnh đơn (dưới giới hạn 3 ảnh/shot), không phải sheet nhiều mặt:
  - body-front-v002: 881×1784 (dọc, toàn thân)
  - expr-smug: 1686×933 (ngang, cận mặt — prompt đã ghi rõ chỉ lấy biểu cảm, không copy crop/nền)
- Prompt sh020 trỏ đúng ảnh biểu cảm của nó (caught-out), không lẫn với sh010.

**Chưa kiểm chứng được ở pre-flight (chỉ biết sau khi gen thật):** Flow có giữ đúng mặt/giọng/bối cảnh không, giọng 2 clip có giống nhau không, quyền thương mại của ảnh nguồn (character.yaml vẫn ghi unverified), body v002 được duyệt làm chuẩn sản xuất hay chưa.

---

## Checklist gen sh010 — làm đúng thứ tự này

Nguyên tắc: **chỉ gen sh010 trước, 1 take duy nhất.** Đạt mới gen sh020. Không gen cả hai cùng lúc.

### Trước khi mở Flow
- [ ] Credit: 1 clip 8s ≈ 10 credits (Lite) / 20 (Fast) / 100 (Quality) theo bảng giá đã tính 13/11 — chọn model trước khi bấm, đừng để mặc định ngốn credit.
- [ ] Chuẩn bị sẵn 2 file ảnh trong `episodes/ep001-don-ban/input/references/`:
  `thao-my-body-front-v002.png` (ảnh 1) và `thao-my-expr-smug-front-v001.png` (ảnh 2) — đúng thứ tự này.
- [ ] Chuẩn bị sẵn nội dung `input/prompts/sh010.txt` để paste **toàn bộ 13 dòng**, không paste mỗi câu thoại.

### Trong Flow
- [ ] Chọn chế độ có ảnh tham chiếu nhân vật/ingredients (Frames/Ingredients tuỳ giao diện tài khoản).
- [ ] Chọn khung **dọc 9:16**, thời lượng **8s**. Nếu tài khoản không có đúng 2 lựa chọn này → **dừng**, báo lại Muse để chỉnh kế hoạch, không tự dùng thông số khác.
- [ ] Upload đúng 2 ảnh ở trên. **Không** upload sheet nhiều mặt, không upload bảng `reference-catalog.jpg`, không thêm ảnh thứ 3.
- [ ] Paste toàn bộ prompt sh010.
- [ ] Kiểm tra lại câu thoại trong prompt đúng nguyên văn, có dấu:
  **"Dọn xong cái bàn này, tôi sẽ tập trung làm việc!"**
- [ ] Bấm tạo **1 take**. Không bấm tạo lại khi trạng thái gửi chưa rõ (tránh trùng job/trừ credit 2 lần).

### Sau khi clip ra
- [ ] Tải về, đặt đúng chỗ, **không đổi tên**: `episodes/ep001-don-ban/generated/sh010/take001.mp4`
- [ ] Tự xem/nghe 1 lượt theo 7 điểm soi trong script.md: chỉ 1 Thảo My (không nhân đôi người từ 2 ảnh) / mặt-tóc-áo trắng-quần short beige đúng / thoại đủ câu, không thêm từ, không nuốt chữ chốt / tay phải chỉ kéo sổ, không xuyên bàn / camera tĩnh, không zoom / bàn chưa tự dọn sạch (vẫn còn dây rối) / không chữ giả, nhạc lạ, tiếng cười tự thêm.
- [ ] Báo Muse "sh010 xong" — Muse sẽ lấy file về chạy ffprobe + clip_qa.py + soi contact sheet trước khi quyết định gen sh020.

### Nếu không đạt
- [ ] Ghi đúng 1 lỗi chính gây hỏng (mặt / giọng / tay / đạo cụ / nhân đôi người).
- [ ] Nếu lỗi do 2 ảnh làm Flow nhân đôi người → lần thử sau chỉ dùng 1 ảnh body, giữ mô tả biểu cảm trong prompt (đã ghi sẵn trong script.md).
- [ ] Không sửa prompt tuỳ tiện: báo Muse, Muse sửa đúng phần gây lỗi và tăng revision + cập nhật hash trong shots.json.
