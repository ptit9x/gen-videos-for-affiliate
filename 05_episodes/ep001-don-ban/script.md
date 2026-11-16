> **Rev5 — 2026-11-16, bản cập nhật nhận diện để review.** Thay bộ mặt/body theo lựa chọn cuối; giữ thoại, bàn bừa và váy đen. Hồ sơ rev4/frame/take/master cũ được giữ nguyên để truy nguồn, không phải đầu ra rev5. Rev5 chưa có frame hoặc ủy quyền gen mới.

> Nhận diện cập nhật 2026-11-16: mặt/tóc `thao-my-face-front-v002.png`; body chính diện `thao-my-body-front-v003-face-v002-review.png`, đều trong `02_characters/thao-my/approved/`. Hai góc ghép nghiêng/sau chưa duyệt; không dùng các bản thử tóc về sau. Giữ thoại, hành động, góc máy và trang phục theo tập; biểu cảm diễn thay đổi theo shot, không cố định nụ cười ảnh mẫu. Chưa có frame mới từ bộ này.

> Cập nhật rev4 — 2026-11-15: đã có hai frame local tạo bằng imagegen, chờ duyệt; xem `prep/local-frames-v001.md`. Thoại trong YAML vẫn là bản gốc, bản thoại gắt lưu riêng chưa đồng bộ. Giọng hiện hành là Đoan Trang theo character.yaml. Các mô tả rev3 bên dưới giữ để đối chiếu lịch sử.

# ep001 — Dọn bàn xong hết giờ làm

Phiên bản kịch bản hiện hành 5 — 2026-11-16 (diễn xuất kế thừa rev3). Cập nhật mặt/body mới đã được người dùng duyệt. Một nhân vật, một bối cảnh, hai clip 8 giây; dự kiến 16 giây trước trim. Không affiliate trong tập thử này.

**Ghi chú lịch sử rev3: bản cập nhật để review, chưa tạo frame/clip mới và chưa có lệnh gen video.** Hai clip đã có là rev2, dùng mặt cũ, không đại diện cho rev3. Giữ nguyên thoại, cú chốt bàn vẫn bừa và váy đen. Hồ sơ rev2 được giữ trong `prep/rev2-record/` để đối chiếu lịch sử.

## Ý tưởng và câu chốt

Thảo My tin rằng bàn gọn thì sẽ tập trung. Cô “dọn” đúng một cuốn sổ giữa một cái bàn bừa bộn, tuyên bố đã xong; sang cảnh sau, bàn vẫn nguyên bãi chiến trường mà cô phán “bàn gọn rồi”, rồi lấy việc đầu óc “trống” làm lý do nghỉ. Tiếng cười nằm ở độ vênh giữa lời nói và hình ảnh.

| Clip | Thoại chính xác | Diễn | Ảnh tham chiếu mới |
|---|---|---|---|
| sh010 — 8s | “Dọn xong cái bàn này, tôi sẽ tập trung làm việc!” | Tự tin, kéo một cuốn sổ ra khỏi đống giấy và vuốt cho ngay ngắn — chỉ dọn đúng món đó | `thao-my-face-front-v002.png` + `thao-my-body-front-v003-face-v002-review.png` |
| sh020 — 8s | “Bàn gọn rồi. Đầu óc cũng trống luôn. Mai làm vậy.” | Liếc bàn, nụ cười tắt, ngượng một nhịp rồi chốt tỉnh bơ (deadpan) | `thao-my-face-front-v002.png` + `thao-my-body-front-v003-face-v002-review.png` |

Khoảng 11 từ mỗi câu. Không thêm lời chào, giới thiệu tên, CTA, câu dẫn hoặc tiếng cười. Không nói nhanh để lấp khoảng trống.

## Những thứ phải khóa trong cả hai clip

- Một Thảo My trưởng thành; mặt và tóc đúng ảnh `thao-my-face-front-v002.png` đã duyệt (tóc nâu tối, mái thưa theo ảnh), tỷ lệ body v003, **váy maxi lụa satin đen SANJOLI**.
- Ngồi cùng một ghế beige sau cùng bàn gỗ sáng, tường trắng kem trống, sáng từ bên trái khung hình. Không thêm người, cây, đồ trang trí hoặc điện thoại.
- Camera tĩnh ngang tầm mắt khi ngồi, góc thẳng, trung cảnh từ khoảng eo lên. Thấy đủ đầu, hai cẳng tay và mặt bàn; không quay toàn thân hay zoom.
- Căn phòng và laptop bạc đóng ở giữa không đổi. sh010: bàn **bừa thật** — giấy tờ chồng chất, giấy vo viên, 2 cốc, vỏ snack, dây rối, sticky note, sổ cream chôn một nửa dưới giấy ở bên trái. sh020: **bàn vẫn y nguyên như vậy**, không dọn thêm bất cứ thứ gì; hai tay đặt yên trên mép bàn.
- Điểm nối hai clip là một **hard cut**; sự “đã dọn xong” chỉ tồn tại trong lời nói của nhân vật, không có thật trên hình — đó là chủ ý hài được giữ từ rev2.

## Giọng

- Giọng native do Veo sinh trong clip **không dùng**: đã kiểm chứng 2 clip ra 2 giọng khác nhau (một Bắc, một Nam) dù prompt hướng giọng giống hệt. Xem đó là tiếng nháp để kiểm tra nhịp miệng.
- Bản giao: tắt tiếng Veo, lồng cả hai câu bằng **một giọng VieNeu-TTS nữ miền Bắc duy nhất** (chạy Colab T4). Preset Đoan Trang đã được chốt trong `02_characters/thao-my/character.yaml`; rev5 chưa có audio mới.

## Hồ sơ sản xuất

Quy trình chính ở [AGENTS.md](../../AGENTS.md). Dữ liệu shot, prompt ảnh/video tách riêng, hash và ID clip ở [episode.yaml](episode.yaml); diễn biến thực tế ở [ghi chú rev2](prep/rev2-production-notes.md). Hai clip Flow thuộc rev2, giữ ID làm lịch sử; kiểm tra cập nhật không tìm thấy hai file clip tại đường dẫn local đã khai báo. Rev3 cần dựng lại frame từ mặt mới và body v003, duyệt frame rồi mới có thể gen lại; không dùng frame/clip mặt cũ để đại diện bản mới. Biểu cảm mô tả trong prompt, không dùng ảnh biểu cảm cũ. Body mặc áo trắng/quần be chỉ khóa tỷ lệ, khi sửa cảnh phải thay sang váy đen. Preset VieNeu Đoan Trang đã chốt; không coi audio rev4 là audio rev5 đã kiểm chứng.

## Nhịp diễn từng clip

### sh010 — Tuyên bố, 0–8s

- 0–0.4s: nhìn bàn với vẻ tự tin.
- Khoảng 0.4–5.5s: nói nguyên câu, đồng thời tay phải kéo cuốn sổ ra khỏi đống giấy và vuốt thẳng một đoạn ngắn. Tay trái không dọn gì; mọi thứ khác trên bàn đứng yên.
- Khoảng 5.5–8s: dừng tay, vẻ tự hài lòng. Không phát sinh thoại. Bàn vẫn bừa khi hết clip.

### sh020 — Chốt hài, 8–16s

- Bắt đầu với bàn vẫn bừa. Hai tay đặt yên ở mép bàn; không động đạo cụ.
- Khoảng 0.3–1.8s của clip: “Bàn gọn rồi.” (liếc xuống bàn một nhịp)
- Khoảng 2.1–4.5s: “Đầu óc cũng trống luôn.” Nụ cười nhẹ tắt, mắt né thoáng qua.
- Khoảng 5–6.2s: “Mai làm vậy.” Giọng tỉnh bơ.
- Khoảng 6.2–8s: nhìn camera, mặt nghiêm, giữ nhịp. Không tự cười câu đùa.

Các mốc là ý đồ diễn, không phải bảo đảm Flow bám đúng từng phần giây. Sửa take hoặc trim hậu kỳ theo kết quả thật.

## Checklist trước khi chấp nhận take

- Chỉ một Thảo My; tóc, mặt, trang phục (váy đen) đúng; không ghép thêm người.
- Bàn sh010 bừa rõ rệt và **vẫn bừa ở cuối cả hai clip**; laptop/cốc không đổi vị trí; sổ không biến thành điện thoại.
- Hai tay đúng, không xuyên bàn, không dính đạo cụ; sh020 tay không dọn bất cứ thứ gì.
- Camera không zoom/cắt; đầu và hai tay không bị crop bất thường.
- Không chữ giả hoặc tiếng cười tự thêm. (Thoại kiểm chứng ở bản lồng tiếng, không chấm theo giọng Veo.)
- Nếu không đạt: ghi đúng lỗi, chỉ sửa phần gây lỗi, tăng revision khi đổi input; giữ take cũ và ghi số lượt thử.

## Dựng và đăng

- Ghép sh010 → sh020 bằng một hard cut. Có thể trim phần im lặng nếu nhịp chậm nhưng giữ đủ câu và khoảng chốt.
- Dự kiến 16s trước trim; khóa thời lượng cuối theo file thật và ghi vào `edit/manifest.yaml` khi dựng.
- Không thêm title mở đầu dài, cảnh chuyển, laugh track hoặc CTA kéo dài. Mặc định giao SRT riêng; burn-in chỉ khi được yêu cầu.
- Caption đề xuất: “Bàn đã sẵn sàng. Chủ bàn thì chưa. Ai cũng có một kiểu trì hoãn thế này à?”
- Đây là sitcom AI; giữ công bố AI phù hợp khi đăng. Chưa gắn sản phẩm hoặc link affiliate. Chưa có lệnh đăng bài cụ thể.
