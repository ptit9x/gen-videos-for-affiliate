# ep019 — Khám Bệnh

Trạng thái: draft, chưa duyệt gen. Thảo My + bác sĩ nam (nhân vật một lần, không thuộc series 13 chàng trai).

## Ý tưởng và twist

Thảo My đi khám vì tức ngực, khó thở. Bác sĩ hỏi có bảo hiểm không. Có thì chỉ định làm đủ thứ: chụp chiếu, điện tim, siêu âm, xét nghiệm, nằm viện theo dõi. Cô hỏi thế không có thì sao. **Twist:** không có thì khỏi cần làm gì hết — chỉ cần đổi sang bộ đồ rộng, vì bộ đang mặc chật quá nên thở không nổi.

**Nguồn ý tưởng:** reel của Nàng Yến, đăng 18/11/2026, phòng khám, cùng cấu trúc hỏi bảo hiểm rồi lật kèo: https://www.facebook.com/reel/1603380111091308/ — kịch bản này viết lại hoàn toàn sang giọng Bắc, rút gọn thành 4 shot, mỗi shot một người nói. Không copy thoại gốc.

**Trend khai thác:** châm biếm chi phí khám chữa bệnh theo bảo hiểm — chủ đề ai cũng từng gặp, dễ bình luận và share. Cú chốt nằm ở vật lý nhìn thấy được (bộ đồ chật), không nằm ở lời giải thích.

## Khóa nhân vật và bối cảnh

### Thảo My (sh010, sh030)
- Mặt/tóc: `thao-my-face-front-v002.png`; body: `thao-my-body-front-v003-face-v002-review.png`. Nguồn tại `02_characters/thao-my/approved/`.
- Trang phục: áo len hồng ôm sát, ngắn tay, cổ tròn — **phải nhìn rõ là đang chật** thì cú chốt mới có đất diễn (quy tắc: chi tiết thoại nhắc tới thì hình phải cho thấy). Quần dài tối màu đơn giản. Son đỏ nhẹ, tóc nâu dài buông tự nhiên.
- Diễn xuất: sh010 tay ôm ngực, mặt lo lắng thật; sh030 nghiêng người về trước, tò mò; cuối sh040 sững sờ, mắt mở to, im lặng.

### Bác sĩ (sh020, sh040) — nhân vật một lần
- Nam khoảng 35 tuổi, tóc đen ngắn, đeo kính, cạo râu sạch. Áo blouse trắng khoác ngoài đồ scrub xanh navy cổ V, ống nghe quanh cổ, thẻ nhân viên bệnh viện.
- Mặt bác sĩ **chưa khóa**: không có ảnh tham chiếu đã duyệt, prompt ảnh tả bằng chữ và giữ cùng một người ở sh020 + sh040. Duyệt mặt bác sĩ ở khâu frame trước khi gen clip.
- Diễn xuất: điềm nhiên, matter-of-fact xuyên suốt — càng bình thản thì cú chốt càng hài. sh020 vừa ghi clipboard vừa nói; sh040 nói xong thì cắt sang phản ứng của My.

### Bối cảnh
- Phòng khám/bệnh viện: bàn khám, biển xanh-trắng có chữ thập, poster tim giải phẫu, giường khám phủ ga xanh nhạt ở góc khung, tủ hồ sơ xanh, chậu cây nhỏ trên bàn. Ánh sáng trắng sáng, rõ.
- Location mới, **chưa có master trong `03_locations/`**. Quay shot-reverse-shot tĩnh, dọc 9:16, giống cấu trúc reel gốc: My đối diện bác sĩ qua bàn.

## Storyboard

| Shot | Người nói | Thoại tiếng Việt | Từ | Một hành động chính | Góc máy/biểu cảm | Thời lượng |
|---|---|---|---|---|---|---|
| sh010 | Thảo My | "Bác sĩ ơi, ngực em cứ tức tức, thở không ra hơi." | 12 | Tay ôm ngực, lo lắng | Trung cảnh, ngồi đối diện bác sĩ | 8s |
| sh020 | Bác sĩ | "Có bảo hiểm thì làm đủ: chụp chiếu, điện tim, siêu âm, xét nghiệm, nằm viện theo dõi." | 18 | Vừa ghi clipboard vừa liệt kê | Trung cảnh, sau bàn khám, điềm nhiên | 8s |
| sh030 | Thảo My | "Thế còn không có bảo hiểm thì sao ạ?" | 9 | Nghiêng người về trước, tò mò | Cận vừa | 8s |
| sh040 | Bác sĩ | "Không có thì khỏi cần. Đổi sang bộ đồ rộng đi, mặc chật thế thở làm sao được." | 18 | Nói bình thản, rồi cắt sang My sững sờ im lặng | Trung cảnh, rồi cắt sang cận mặt My | 8s |

**Câu chốt quotable:** "Không có thì khỏi cần."

**Hook 3 giây:** "Bác sĩ ơi, ngực em cứ tức tức, thở không ra hơi."

**Lưu ý khung hình:** không quay cận ngực, không nhấn vào cơ thể. Góc trung cảnh là đủ để thấy áo ôm sát; cú chốt nói về bộ đồ chật, không nói về cơ thể.

## Sản phẩm lồng ghép

Mặc định không affiliate. Phòng khám không hợp sản phẩm hiện có; chưa gắn link, chưa đăng.

## Tài sản và prompt

Khai báo trong `episode.yaml`. Prompt video: hành động + thoại + giọng miền Bắc + camera tĩnh, không nhạc.

## Hậu kỳ

Chọn take trong manifest; hard cut. Giữ tiếng Veo gốc nếu giọng Bắc (cả giọng nữ My và giọng nam bác sĩ); chỉ lồng lại shot nào giọng Veo không phải Bắc hoặc Richard chỉ định lồng shot đó (My lồng giọng clone ThaoMy). Phụ đề burn-in bằng Remotion BasicCaptions (boxed) + giao thêm file .srt riêng. Tại cú twist cuối (sh040) chèn 1 sound effect từ Freesound, ghi nguồn URL + license + tên file vào manifest lúc dựng; không thêm nhạc nền hay SFX ở chỗ khác.
