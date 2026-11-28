# sh040 — phân tích crop v2 (sau khi Richard REJECT crop v1)

Ngày: 2026-11-28. Lệnh: làm lại crop sh040, mặt My 45–55% chiều rộng output,
vai Trí biến mất hoàn toàn, giữ 9:16, giữ ly + bàn; đo bằng số trước khi chốt.

## Kết quả đo (take001 720x1280, frame t=1/2/4/5.5/7s)

Phương pháp: skin mask YCrCb (Cr 133–173, Cb 77–127, Y>90) + connected component
lớn nhất trong hộp mặt; mép vai = dark mass (lum<70) chạm mép phải khung;
đọc chéo bằng ảnh lưới 5% (edit/qc-frames/sh040-m4-grid.png).
Script đo: edit/wordalign/measure_sh040_v2.py, v3.py, v4.py, v5.py.

| Đại lượng | Số đo |
|---|---|
| Mặt My — tâm (centroid skin blob) | x = 331–360 theo frame (t=1: 360, t=4: 348, t=7: 332); trung bình ~347 |
| Mặt My — tâm bbox | x = 332–360 (cùng khoảng) |
| Mặt My trong crop v1 (x0–440) | 75–82% chiều rộng (t=7: 75%, t=4: 79%, t=1: 82%) → **khớp nhận xét của Richard (~76%)** |
| Vai Trí — mép trái (đoạn dưới y720–1080) | x = 476–491 (y720–760: 481–484; y1000: 490–492; y1040: 476–478) |
| Vai Trí — mép trái (đoạn trên, đầu Trí y280–320) | x ≈ 520–686 (đầu, xa hơn) |
| Tóc My — đỉnh đầu | y ≈ 340 (đọc lưới) |
| Ly + đĩa — đáy đĩa | y ≈ 1010 (ly y890–975; đọc lưới) |
| Nhịp đứng cần giữ (đỉnh tóc → đáy đĩa) | H ≥ 670px (chưa tính headroom / bàn dưới đĩa) |

## Chứng minh: KHÔNG có vùng crop 9:16 nào đạt cả 4 ràng buộc

Đặt cửa sổ crop [L, R], rộng W = R − L, cao H = W×16/9.
- Giữ đủ nhịp đứng ⇒ H ≥ 670 ⇒ **W ≥ 377**.
- Mặt trong 45–55% ở MỌI frame: mặt dao động x 332→360 (biên độ 28px).
  Frame xấu nhất (t=1, mặt x=360) ở ≤55% ⇒ L ≥ 360 − 0.55W.
- Vai biến mất ⇒ R = L + W ≤ 476 (mép vai nhỏ nhất).

Với W = 377: L ≥ 360 − 0.55×377 = 153 ⇒ R ≥ 530 > 476. **Mâu thuẫn.**
Ngược lại, để R ≤ 476 với mặt t=1 ở ≤55% thì W ≤ (476−360)/0.45 = 258,
suy ra H = 458 < 670. **Mâu thuẫn.**

Ngay cả trường hợp thuận lợi nhất (mặt x=332, mép vai x=491, mặt ở đúng 55%,
không headroom, không bàn dưới đĩa): W ≤ 353 ⇒ H = 627 < 670, và mặt ở t=1
lại rơi ra 63%. **Vùng khả thi là tập rỗng — thiếu ~11px trong trường hợp
thuận lợi nhất, thường thiếu 25–50px.** Nguyên nhân gốc: khoảng cách
mặt→vai chỉ 116–159px, quá nhỏ so với nhịp đứng 670px mà khung 9:16 đòi hỏi.

## Kết luận

**Không làm candidate crop mới — không có vùng crop 9:16 nào thỏa cả 4 điều kiện.**
Không tự chốt bản lệch (đã thử 2 cách đo tự động trước khi đo lưới; cả 2 đều
bắt nhầm blob — ghi lại để khỏi lặp: skin mask rộng bắt cả tay áo/tay, đo
mép vai bằng dark-run bắt cả tóc My; chỉ tin số đo sau khi đọc chéo bằng lưới).

## Phương án trình Richard (chưa làm, chờ duyệt)

1. **Giữ vệt vai mờ (khuyên dùng nếu muốn giữ take này):** crop 9:16 lấy mặt
   My về 50% (vd cửa sổ ~420 rộng, L≈137, R≈557), phần vai Trí lọt vào
   ~80px mép phải được blur mạnh + tối đi trong hậu kỳ (vai vốn đã out-focus;
   blur sẽ đọc như foreground bokeh chủ ý). Mặt đúng giữa ✓, ly + bàn đủ ✓,
   9:16 ✓ — chỉ vi phạm "vai biến mất hoàn toàn" ở mức vệt mờ.
2. **Crop nhẹ hơn + dịch khung:** crop x0–460 (vai hết hẳn) — mặt vẫn ở
   ~75%, chỉ đỡ lệch hơn v1 một chút. Không đạt 45–55%, chỉ là thỏa hiệp.
3. **Re-frame shot (sạch nhất):** làm frame đầu mới chỉ có My (cận vừa,
   mặt giữa khung, không có vai Trí tiền cảnh) → Richard duyệt ảnh trước
   (luật frame-first) → gen lại sh040 take mới (10 credit Flow). Take001
   giữ làm backup.
4. **Xóa vai bằng AI inpainting video:** không có tool local làm được
   (cần inpainting theo từng frame, vai/head Trí chuyển động nhẹ); không
   khả thi trên VM này — chỉ ghi nhận, không đề xuất làm.
