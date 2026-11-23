# Quán cà phê hẹn hò — v001

Ngày tạo 2026-11-15, image_gen tích hợp. Bối cảnh tự thiết kế theo yêu cầu người dùng: lãng mạn cho kịch bản hẹn hò. Chờ duyệt, chưa phải master.

Đầu ra: `review/date-cafe-v001.png` (1536×1024). Quán sân vườn lúc chạng vạng, hai ghế đối diện, bàn tròn gỗ và đèn vàng. Ảnh ngang để duyệt không gian; góc quay dọc có nhân vật sẽ dựng riêng theo shot. Đèn bàn hiện ở giữa: khi dựng đối thoại cần kiểm tra không che mặt và đường nhìn.

## Prompt

Use case: photorealistic-natural. Create ONE photorealistic location reference photograph of a cozy romantic garden café in a contemporary Vietnamese city at blue-hour dusk, intended as a recurring dating-dialogue sitcom location. No people. A single small round warm wooden table for two in the foreground, two comfortable wooden chairs with cream cushions opposite one another, one chair left and one right, seen obliquely so both seats and future actors' faces could be framed. On table only two simple iced drinks in clear glasses with subtle condensation, one tiny vase with a few white flowers and one small warm shaded rechargeable table lamp. Table not overloaded, future actors' faces unobstructed. Mature potted trees and climbing greenery around a low cream plaster wall, discreet warm string lights overhead, café glass doors in background softly lit, a few distant empty tables with plausible spacing. Quiet intimate everyday café, romantic but understated, affordable and believable, no heart decorations, no wedding decor, no rose petals, no luxury resort. Warm amber practical lighting mixed with cool twilight, enough gentle fill light for natural facial visibility in later shots. Film still realism, natural textures, grounded spatial geometry, eye-level 35mm perspective, straight verticals. Landscape 3:2 composition showing whole main table and both chairs with room for shot reverse shot camera setups, moderate depth of field so layout remains legible. No text, signage, logos, watermarks, collage or people.

## 2026-11-21 — date-cafe-v002-day.png (bản khóa ban ngày, CHỜ DUYỆT)
- Nguồn: sửa từ date-cafe-v001.png (ảnh tối) bằng Nano Banana trên Flow, project ep008, 0 credit (780 → 780), Flow asset 6592c747-14db-4521-b5c1-8fbc1056df2a. Bee QC file local 07:38: ban ngày nắng sáng, cùng góc quán v001, bàn tròn phủ khăn trắng, 2 ghế gỗ tối đệm be đầy đủ 2 bên bàn, 2 ly nước cam, cây xanh, không người, không chữ — ĐẠT làm frame bối cảnh khóa cho ep008 (cả 7 frame nhân vật sửa từ ảnh này). sha256 e7916415…
- v001 là ảnh tối nên không dùng làm ref bối cảnh cho tập ban ngày nữa.

## 2026-11-21 — date-cafe-v003-day.png (MASTER BAN NGÀY, ĐÃ DUYỆT)
- Nguồn: sửa từ date-cafe-v002-day.png bằng Nano Banana trên Flow, project ep008, 0 credit (Flow asset 5b80f134-02c3-4af0-9679-63a2fe7787f1). Góc KHÁC cùng quán v002-day: tường đá, cây, sỏi, hoa giấy, đèn dây, bàn thứ 2 ở nền; 2 ghế gỗ tối đệm be CAO chuẩn tầm bàn, bàn tròn khăn trắng, đúng 2 ly nước cam, ban ngày, không người.
- Richard duyệt 21/11 (ghi trong script.md ep008). File 1536×2752, sha 1a66036ea6abda7cf5a09dab6a7b5ae2f1b676f3db1cfb3e885be64dd7778fbb.
- location.json cập nhật 23/11: status approved, master_reference = review/date-cafe-v003-day.png (file giữ ở review/ để khỏi vỡ ref ep008). v002-day bỏ (ghế thấp), giữ làm candidate. Dùng làm bối cảnh khóa cho ep010 từ 23/11.
