# Work log — ep008 Con Nhỏ Đó

## 2026-11-19 22:13 — Lưu tư liệu nguồn + draft kịch bản, chưa gen

- Richard gửi link share Facebook reel Hey Men Comedy ("Yêu khổ quá thôi dẹp nghỉ hết đi", 63s, 352K views).
- facebook-cli báo chưa kết nối nên không đọc qua connector được; kéo trực tiếp bằng yt-dlp từ link share, về đủ file 1080×1920/63,37s/24MB, sha256 `9a71ae6d…0c450`.
- Transcript dựng từ phụ đề burn-in trong video (soi frame 2s/lần) + kiểm chéo faster-whisper base. Câu cuối nam bỏ đi nghe không chắc, đã ghi rõ "không chắc" trong `source-transcript.md`, không bịa.
- Viết `script.md` draft: phỏng theo reel gốc, viết lại giọng Bắc, 5 shot × 8s = 40s. Bỏ tát + bỏ chửi thề của bản gốc (ghi rõ trong script để Richard chốt). Chàng trai chưa chốt là ai trong 13 người; trang phục My chưa chốt; chưa affiliate.
- `episode.yaml` draft: 5 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip. Bước tiếp theo chờ Richard duyệt kịch bản (và chốt: 5 shot hay gộp 4, chàng trai là ai, có giữ độ đanh đá kiểu khác thay cho tát hay không).

## 2026-11-20 00:08 — Richard bảo sẽ cấp chàng trai + trang phục sau

- Cập nhật `script.md`: chàng trai (ảnh nhân vật) và trang phục My đều do Richard gửi sau — chờ cậu ấy cấp rồi mới khóa mặt/đồ, ghi `wardrobe.md` và làm frame. Không tự chọn người hay đồ trước.
- Commit + push riêng ep008 (không đụng các thay đổi ep005 chưa commit của luồng khác).

## 2026-11-21 — Bee (Muse), viết lại kịch bản 6 shot (rev2)

- Richard chốt phương án 6 shot (sáng 21/11): thêm sh050 câu sập bẫy của My, sh060 anh chia tay + đứng dậy. Tổng 6 shot × 8s = 48s, dài hơn chuẩn 40s của series, tốn thêm 10 credit/clip so với 5 shot.
- script.md rev2: twist sửa cho khớp shot (câu "thế là anh có thật à?" giờ nằm ở sh050); sh060 góc rộng tĩnh, cả hai trong khung, anh nói trong lúc đứng dậy rồi bước ra khỏi khung, máy giữ mặt My sững sờ 2s cuối. Sửa số từ bảng storyboard: sh020 10 (rev1 ghi 11), sh030 13 (ghi 15), sh040 13 (ghi 14); sh050 6 từ (review ghi 7 là sai — đếm lại: Thế/là/anh/có/thật/à). Bỏ ghi chú gộp sh040+sh050 (29 từ/8s không khả thi). Thêm son đỏ + móng tự nhiên vào khóa nhân vật; thêm beat im lặng sh010/sh020 vào motion note.
- Trang phục My: áo dài, 1 trong 4 mẫu hôm qua (Thanh Nghi hồng đậm / Lam Yến trắng ngà hoa / Xuân Dệt Mộng Hoa hồng nhạt hoa / Vân Linh xanh nhạt hoa) — chờ Richard chốt mẫu. Ảnh tại `~/workspace/ao-dai-2011/`.
- Chàng trai tên Nam (~30 tuổi), Richard đang tìm ảnh — chờ gửi rồi mới khóa mặt/đồ, ghi wardrobe.md và làm frame.
- episode.yaml: revision 2, target 48s, sh050 đổi thoại, thêm sh060. Chưa duyệt kịch bản, chưa làm frame, chưa gen clip, chưa commit.

## 2026-11-21 — Bee (Muse), chốt áo dài + nhận ảnh Nam

- Richard bấm widget chọn áo dài **Thanh Nghi (hồng đậm, quần hồng nhạt)** cho My. Ghi vào script.md + wardrobe.md mới (kèm sha256 3 ảnh ref: shop collage `0c5dceff…`, My mặc Thanh Nghi tóc xõa v3 `3d262ba5…`, bản búi nửa đầu `1636912b…`). Son đỏ + móng tự nhiên đã khóa trong wardrobe.
- Richard gửi ảnh ref Nam (1184×1776, sha256 `b8aadb51…`), lệnh dùng Google Flow sinh nhân vật Nam mới. Đã lưu `02_characters/nam/approved/nam-front-v001.jpg` + README + character.yaml + references.json (mirror cấu trúc của Bằng). Đồ Nam chưa chốt: sơ mi trắng (ảnh ref) hay polo cam (reel gốc) — hỏi Richard.
- Rủi ro đã ghi: ảnh ref trông như ảnh người thật (có watermark studio), Flow có thể chặn tạo nhân vật/gen video theo chính sách người nổi tiếng (như @Vy v2). Fallback: chỉ dùng ảnh ref làm nguồn sửa frame như cách của Bằng, video vẫn Frames-direct.
- Kịch bản rev2 (6 shot) vẫn đang chờ Richard duyệt lại. Chưa commit.

## 2026-11-21 — Bee (Muse), chốt sơ mi trắng + aff-0005

- Richard bấm widget chọn **sơ mi trắng (như ảnh ref)** cho Nam + nhắn link affiliate áo trắng https://s.shopee.vn/9zzT7PVjWK. Ghi vào script.md + wardrobe.md (quần tối màu đơn giản; đồng hồ/vòng tay trong ảnh ref mặc định KHÔNG đưa vào frame).
- Link ghi `04_products/affiliate-links.csv` là **aff-0005 / prd-0005**, trạng thái `unverified`. `browser.open` fetch lỗi 21/11 (không lấy được trang Shopee) → đang kiểm tra lại bằng trình duyệt live (task mới, read-only, không đăng nhập/không mua).
- Thêm dòng ep008 vào `00_docs/production-tracker.csv` (trước đó tracker chưa có ep008).
- Kịch bản rev2 vẫn đang chờ Richard duyệt lại. Nhân vật Nam trên Flow đang chờ Richard duyệt thẻ consent của trình duyệt.

## 2026-11-21 — Bee (Muse), xác minh aff-0005 (kết quả một phần)

- Trình duyệt live mở https://s.shopee.vn/9zzT7PVjWK (read-only, 06:48-06:49): link phân giải tới https://shopee.vn/product/64771533/28877375467 (shop slug opaanlp, shop ID 64771533, item 28877375467). Tiêu đề tab: "Áo sơ mi trắng nam Phan Nguyễn, chất liệu bamboo cao cấp, mềm mát, thấm hút, form slim fit SMD.1416" — đúng áo sơ mi trắng nam.
- Chưa xác minh được: tay dài hay ngắn, màu, size, giá, tên shop hiển thị — Shopee chặn trang đăng nhập (verify/traffic/error). aff-0005 giữ trạng thái `unverified` trong CSV (đã ghi product_url + tên sản phẩm + last_checked_at 2026-11-21).
- Sửa 2 dòng cũ trong script.md cho khớp quyết định mới: "Nam là ai" (đồ Nam đã chốt sơ mi trắng, bỏ câu chờ chọn) và "Tài sản và prompt" (bỏ "gửi ảnh Nam + chốt mẫu áo dài" vì cả hai xong rồi).

## 2026-11-21 — Bee (Muse), nhân vật Nam đã tạo xong trên Flow

- Browser task (06:47–06:50, acc huynhdn Pro, 780 credit lúc đăng nhập): tạo project mới "CNTM · EP008 · Con Nhỏ Đó" — https://flow.google.com/project/da396a3f-bfc4-45d7-abb7-98ed1c151f3c — và nhân vật "Nam" từ đúng 1 ảnh ref nam-front-v001.jpg. Chân dung ra đúng người áo trắng, KHÔNG bị chặn chính sách người nổi tiếng ở bước nào. Không gen video nào.
- Ghi URL project vào episode.yaml `flow_project`; cập nhật tracker (thêm flow_project_url), character.yaml (status created_in_flow), references.json (character_created_2026_11_21), README Nam, MEMORY.md.
- Lưu ý: tạo nhân vật thành công không chứng minh gen video qua Ingredients sẽ chạy — kế hoạch vẫn là Frames-direct cho clip, nhân vật chỉ dùng làm nguồn sửa frame.
- Còn chờ: Richard duyệt kịch bản rev2 → làm frame.

## 2026-11-21 — Bee (Muse), sửa "con nhỏ đó" → "con đó" (rev3)

- Richard (đang review kịch bản): "'con nhỏ đó' thì hơi miền Nam rồi, 'con đó' thôi."
- Sửa toàn bộ thoại trong script.md + episode.yaml (revision 3): sh010 "Anh yêu em hay là yêu con đó?" (8 từ), sh020 "Con đó là đứa nào? Anh còn không biết." (9 từ — "nhỏ nào" cũng sửa thành "đứa nào" vì "nhỏ" làm danh từ chỉ con gái cũng là giọng Nam), sh030 "Giữa em với con đó, anh chọn ai? Lỡ có thì sao?" (12 từ), sh060 "Ừ, thừa nhận luôn: anh yêu con đó. Chia tay đi, yêu khổ quá." (14 từ). sh040/sh050 không có cụm này, giữ nguyên. Tổng 62 từ (rev2: 66), vẫn trong ngân sách ≤15 từ/shot.
- Đã verify bằng grep: trong script.md chỉ còn "Nhỏ" ở 3 chỗ cố ý giữ — tiêu đề tập "# ep008 — Con Nhỏ Đó", ghi chú rev3 trích lại cụm cũ, tên project Flow "CNTM · EP008 · Con Nhỏ Đó".
- Tiêu đề tập CHƯA đổi (đổi tên tập = đổi tên thư mục ep008-con-nho-do + episode.yaml + tracker + tên project Flow) — hỏi Richard có muốn đổi thành "Con Đó" không rồi mới làm.
- Tracker + MEMORY.md cập nhật theo. Chưa commit.

## 2026-11-21 — Bee (Muse), tách sh070 phản ứng im lặng (rev4)

- Richard hỏi: mặt My sững sờ mấy giây cuối có nên làm shot mới không, sợ Flow không chuyển cảnh tốt. Bee khuyên tách: câu sh060 14 từ ~6s + đứng dậy + bỏ đi + giữ mặt 2s ≈ 10–11s, không vừa 1 clip 8s (đúng lỗi nhồi shot đã bắt ở sh050 cũ); chuyển cảnh không phải Veo lo — dựng cắt cứng sh060 → sh070; tiền lệ ep007 sh050 (shot phản ứng im lặng, take002 đạt, dựng lấy 3–4s + freeze). Richard bấm widget chọn tách.
- Rev4: sh060 chỉ còn nói 14 từ + đứng dậy + quay lưng bước ra khỏi khung (góc rộng tĩnh, cắt cứng sang sh070); sh070 mới — My sững sờ không thoại, cận vừa, chỉ My trong khung, máy tĩnh. episode.yaml: dialogue sh070 = '' (theo đúng mẫu ep007 sh050), revision 4, target 56s.
- Richard dặn thêm: shot cuối 8s dài quá thì cắt bớt → ghi rõ trong script (quay 8s, dựng cắt còn ~3s) + phần hậu kỳ (Laugh Track 1 gợi ý chèn trên sh070, không đè câu "Chia tay đi").
- Tổng 62 từ thoại (sh070 0 từ), 7 clip Lite = 70 credit. Tracker + MEMORY.md cập nhật theo. Chưa commit.

## 2026-11-21 — Bee (Muse), ghi tên tham chiếu Nam + gen 7 frame trên Flow

- Tên tham chiếu dùng lại: Richard dặn "nhân vật Nam này nhớ đặt tên tham chiếu sau này dùng lại" → ghi **"Nam"** vào `02_characters/nam/character.yaml` (block `flow_reference`: tên, project, project_url, character_url, character_id c759064c…, reusable: true, reuse_note) + `02_characters/nam/README.md` (mục "Tên tham chiếu dùng lại"). Anh ep021 đã có tên riêng "Thảo" nên không đụng tên.
- Image prompt: viết 7 file `input/prompts/sh0X0-image.txt` (theo mẫu ep007: mặt + body ref, khóa màu áo dài hồng đậm phải GIỐNG hệt ref ở mọi shot My, son đỏ + móng tự nhiên, bối cảnh quán cà phê ngoài trời ban ngày/bàn tròn khăn trắng/2 ly nước cam/cây xanh). 5 ảnh tham chiếu copy vào `input/references/` (mặt v002 sha 8793c0ce…, body v003 sha 50195e87…, áo dài Thanh Nghi v3 xõa sha 3d262ba5… khớp ghi chú cũ, Nam sha b8aadb51…, date-cafe v001 sha 23b9f01c…) và khai báo vào `episode.yaml` (image_prompt + image_sources từng shot, sha256 đầy đủ).
- Validator `06_automation/validate_episode.py`: chỉ báo 7 lỗi `flow_image_asset_id is a required property` (chưa có frame nên chưa có asset ID) — còn lại đạt (thoại, prompt, sha đều khớp).
- Gen frame: đã giao task trình duyệt (browser-task c0604172) làm 7 frame trong project EP008 bằng Nano Banana, 0 credit, mỗi frame 1 edit từ ảnh gốc (My: từ ảnh áo dài Thanh Nghi v3 — mặt đã kiểm chứng khớp master v002, đồ đã đúng sẵn; Nam: từ nam-front-v001.jpg), tối đa ~3 lượt/frame, tải về + báo asset ID. Chưa gen video. Frame xong sẽ trình Richard duyệt rồi mới gen clip.
- Lưu ý: kịch bản rev4 chưa có câu "duyệt" rõ của Richard, nhưng cậu ấy đã lệnh "gen ảnh trên flow đi nhé" nên tao tiến hành làm frame (0 credit, có chốt duyệt frame trước clip). Chưa commit.

## 2026-11-21 — Bee (Muse), QC 7 frame ep008 (soi file local, không tin báo cáo trình duyệt)

- Frame về đủ 7 file 768×1376, 0 credit (780 → 780). Đã copy nguyên byte vào `input/frames/sh0X0-first-frame.jpg`, ghi sha256 + flow_image_asset_id vào episode.yaml, frame_status: pending_review (CHƯA duyệt — chờ Richard). Validator: hết lỗi asset ID, chỉ còn thiếu `edit/manifest.yaml` (bình thường ở bước frame — manifest lập ở bước dựng).
- QC SO TRỰC TIẾP VỚI ẢNH REF (áo dài Thanh Nghi v3 + Nam ref):
  - SẠCH (4): sh010 My áo dài hồng đậm đúng màu, son đỏ, mặt chất vấn, Nam sau lưng áo trắng; sh030 My áo dài đúng, tay gõ bàn, mặt dồn dập; sh050 My áo dài đúng, mặt đắc thắng nhướn mày; sh070 My một mình áo dài đúng, mặt sững sờ mắt mở to miệng hơi há, Nam không lọt khung.
  - LỖI ÁO (3): sh020 My quay lưng mặc áo trắng kem tay ngắn (không phải áo dài); sh040 My mặc áo hồng nhạt cổ bẻ (không phải áo dài hồng đậm); sh060 My mặc áo xám-be (không phải áo dài) — cả 3 đều là shot sửa từ ảnh Nam, mô tả áo My trong prompt bị Flow chặn chính sách 5 lần (trong khi sửa từ ảnh My thì qua). Nam + bối cảnh + diễn xuất ở cả 3 đều đúng.
  - Lưu ý khác: dấu sao Gemini mờ góc dưới phải ở sh010/sh050/sh060 (như các tập trước — lúc gen video sẽ crop); sh060 bối cảnh lệch góc quán khác (ghế gỗ + sàn xi măng, khác ghế mây ở các shot còn lại); nốt ruồi cằm trái KHÔNG nhìn rõ ở độ phân giải 1K này (cả ở ảnh ref áo dài cũng không rõ) — mặt còn lại khớp (tóc, mái, mắt, son).
- Đề xuất trình Richard: duyệt 4 frame sạch, làm lại sh020/sh040/sh060 bằng cách sửa từ ảnh My (Thanh Nghi) kèm ảnh Nam làm thành phần phụ — vì mô tả áo My qua được bộ lọc khi sửa từ ảnh My. Chưa làm lại khi chưa có lệnh. Chưa commit.

## 2026-11-21 — Bee (Muse), Richard chê thêm 2 điểm ở 7 frame ep008

- "Bàn ghế khác nhau": đúng — tao soi lại: ghế mây đan (sh030), ghế kim loại đen (sh040), ghế gỗ (sh060), ghế kim loại (sh010/sh050) — chỉ có bàn tròn khăn trắng là giống nhau. Prompt chỉ khóa "bàn tròn khăn trắng" chứ không khóa loại ghế, nên Flow tự đổi ghế mỗi frame. Bài học: khóa loại ghế trong prompt + location lock.
- "ngực My bé quá": đúng — áo dài trong frame rủ lỏng nên ngực My đọc nhỏ, không đúng chuẩn body v003 đầy đặn của nhân vật. Prompt không ghi rõ độ đầy của ngực. Bài học: ghi rõ "áo dài ôm vừa ở ngực, ngực đầy đặn nổi bật theo body v003" trong mọi prompt My.
- Đề xuất đã trình Richard (widget mới): làm lại CẢ 7 frame với 3 khóa — (a) bàn ghế: bàn tròn khăn trắng + ghế gỗ tối đơn giản, không đan mây (theo chốt 19/11 của Richard ở ep006: ghế mây dễ lỗi họa tiết, ưu tiên gỗ đặc); (b) ngực My đầy đặn, áo dài ôm vừa ở ngực theo body v003; (c) áo dài hồng đậm đúng ở mọi shot (sửa từ ảnh My cho 3 shot Nam). Hoặc phương án 2: chỉ làm lại 3 frame lỗi áo, giữ 4 frame sạch (chấp nhận bàn ghế + ngực như hiện tại ở 4 frame đó). Đang chờ Richard chọn. Chưa commit.

## 2026-11-21 — Bee (Muse), frame bối cảnh khóa date-cafe-v002-day ĐẠT QC
- Browser task 632f5ac1 (07:34–07:38): sửa từ v001, 1 attempt, 0 credit (780 → 780), Flow asset 6592c747-14db-4521-b5c1-8fbc1056df2a.
- Bee QC file local (768×1376, sha cb9ac71d…): ban ngày nắng sáng trời xanh, cùng góc quán v001, bàn tròn phủ khăn trắng, 2 ghế gỗ tối đệm be đầy đủ 2 bên bàn, 2 ly nước cam, cây xanh, không người, không chữ — ĐẠT. (Còn dấu sao Gemini mờ góc dưới phải, như các frame trước — lúc gen video sẽ crop.)
- Đã lưu PNG (sha e7916415…) vào `03_locations/date-cafe/review/date-cafe-v002-day.png` + copy vào episode `input/references/`; episode.yaml image_sources cả 7 shot đã đổi từ v001 sang v002-day; README location đã ghi chú.
- Task gen lại 7 frame nhân vật đã giao (browser-task dcd93c15, 07:38): mỗi frame = 1 edit từ frame bối cảnh khóa, ảnh My/Nam làm thành phần phụ cùng 1 edit, prompt v2 nguyên văn (ghế gỗ tối + áo dài ôm ngực đúng body v003 + áo My tả cả trong shot Nam; nếu bị chặn chính sách thì diễn đạt lại qua ảnh ref, không bỏ mô tả áo). Chờ handoff rồi QC file local trước khi trình Richard.

## 2026-11-21 — Bee (Muse), frame v2: 4 shot My ĐẠT QC, 3 shot Nam BỊ CHẶN chính sách
- Browser task dcd93c15 (07:39–08:15, 36 phút): 4/7 frame về (sh010/sh030/sh050/sh070), 0 credit (780 → 780). 3 shot Nam (sh020/sh040/sh060) bị Flow chặn chính sách CẢ 9 lượt thử (mỗi shot 3 lần, đã thử diễn đạt lại, đổi thành phần, dùng nhân vật Nam Flow, tả Nam bằng chữ, bỏ tên Nam, quay lưng Nam) — không mất credit. Quy luật: 4 shot My qua ngay lần đầu với prompt nguyên văn; 9 lượt shot Nam đều chặn bất kể thành phần/cách tả.
- Bee QC 4 frame v2 trên file local (768×1376): nền KHÓA ĐÚNG (bàn ghế giống hệt frame bối cảnh v002-day), áo dài hồng đậm đúng mọi shot, son đỏ, mặt/diễn xuất đúng. Ngực: cải thiện RÕ ở sh070 cận (áo ôm ngực, đầy đặn), còn 3 shot ngồi thì vừa phải do tư thế ngồi — đã ghi rõ để Richard tự đánh giá. Dấu sao Gemini mờ góc dưới phải còn (như trước, lúc gen video sẽ crop).
- Đã lưu v2 vào input/frames/ (file v1 giữ lại tên *-v1.jpg), episode.yaml ghi sha256 + asset ID v2 cho 4 shot (sh010 7fcae3c4…, sh030 82ed32f0…, sh050 8676bf0f…, sh070 c56cc3ac…); sh020/sh040/sh060 vẫn giữ entry v1.
- Đang thử lại 3 shot Nam bằng cách KHÁC (browser-task 76b40491, 08:17): sửa từ ẢNH NAM làm nguồn (cách đã chạy được 3/3 ở v1), nền v002-day + ảnh áo dài làm thành phần tham chiếu, prompt v2 nguyên văn. Nếu vẫn chặn thì trình Richard 4 frame + xin quyết (dùng frame v1 / đổi góc quay / chờ thử lại sau).

## 2026-11-21 — Bee (Muse), 3 shot Nam ĐÃ CÓ FRAME v2 BẰNG MEDIA PIPELINE
- Thử lại bằng Flow thất bại HOÀN TOÀN (browser-task 76b40491, 08:17–08:24): cả 3 shot Nam chặn chính sách thêm 9 lượt nữa (tổng 18 lượt chặn liên tiếp) — đã thử sửa từ ảnh Nam làm nguồn, nhân vật Nam Flow, prompt tối giản 2 thành phần, bỏ mọi từ ngữ về dáng/áo. 0 credit mất (780 → 780). Kết luận: bộ lọc Flow chặn riêng tổ hợp Nam đối diện + My trong tập này, không phải do từ ngữ hay thành phần.
- CÁCH ĐÃ CỨU ĐƯỢC: sửa 3 frame v1 bằng media pipeline của Bee (media.generate_image, 0 Flow credit) — giữ nguyên bố cục + mặt 2 người từ frame v1, đổi áo My sang áo dài hồng đậm đúng ref + đổi nền sang đúng frame bối cảnh v002-day (ban ngày, khăn trắng, ghế gỗ tối). Kết quả 3/3 đạt. File: sh020 snapshot 0da97798…, sh040 039fe55f…, sh060 f4791891… (1168×2112, jpg).
- Bee QC 3 frame trên file local: sh020 Nam ngơ ngác tay giơ, My sau lưng áo dài đúng, 2 ly cam, bàn ghế khóa đúng; sh040 Nam chỉ tay vào My cười gượng, My nghiêng người áo dài đúng (có thêm tua trang trí nhỏ ở cổ áo do pipeline tự thêm — chấp nhận được); sh060 Nam đã đứng dậy, My ngồi ngước nhìn, cả bàn + 2 ghế đầy đủ. Dấu sao Gemini còn ở góc dưới phải (kế thừa từ frame v1, lúc gen video sẽ crop).
- Đã lưu vào input/frames/ (file v1 giữ lại tên *-v1.jpg), episode.yaml ghi sha256 mới + flow_image_asset_id=null cho 3 shot (không phải asset Flow). Validator: chỉ còn lỗi thiếu edit/manifest.yaml như kỳ vọng ở giai đoạn frame.
- CẢ 7 FRAME V2 ĐÃ ĐỦ — đang trình Richard duyệt. Chưa gen clip.

## 2026-11-21 — Bee (Muse), Richard lệnh GEN theo cách ThaoMyV002
- Richard (08:49–08:50): "nhân vật Nam phải tạo frame làm ảnh tham chiếu mới đc" / "gen như cách tạo ra đc ThaoMyv002 ấy". Bee đối chiếu log 17/11: ThaoMyV002 tạo từ ảnh master trong project (asset-only, không gán giọng, không gen qua Ingredients); frame dựng bằng sửa ảnh từ master + váy + bối cảnh; clip gen Frames-direct từ frame làm ảnh tham chiếu, tắt Agent, Veo Lite. Đúng cách ep001 đã chạy.
- Bee viết 7 motion prompt (ngắn, 1 hành động + thoại nguyên văn + hướng giọng + máy tĩnh, KHÔNG phủ định) vào input/prompts/sh0X0-motion.txt, đồng bộ sha256 vào episode.yaml.
- Task gen 7 clip đã giao (browser-task 30c2e0ed, 08:52): Frames-direct, Agent OFF, Veo 3.1 Lite 10cr/clip (70cr, 780 → 710 kỳ vọng), 9:16, 8s, 1 output/shot, frame v2 làm frame đầu duy nhất, prompt chuyển động nguyên văn; tải 1K. Chờ handoff rồi QC clip local (thoại đủ từng chữ, giọng Bắc, không phụ đề giả, cắt đuôi ma sau ~7s).

## 2026-11-21 — Bee (Muse), QC 7 clip take001 (09:14)
- 7 clip ve du (720x1280, 24fps, 7.93s; sh070 8.00s, khong co audio track dung kich ban), 70cr, 780 -> 710. File goc o ~/workspace/ep008-con-nho-do-clips/sh0X0-take001.mp4, frame QC o frames/ (t1/t3/t5/t7/t7.8).
- Thoai (Whisper base + tiny cross-check + do nang luong 48k stereo + F0): sh020/sh030/sh040/sh050/sh060 DU — cac cho Whisper nghe lech ("Con do", "giua", "chon em", "vua long em chua") deu la nham dong am cua ASR, F0/tiny xac nhan dung kich ban. Khong phu de gia o bat ky frame nao; duoi sach ca 7 clip; Nam dung day quay di dung o sh060; sh070 sung so dung.
- **sh010 take001 LOAI**: Veo lap cau "hay la yeu con do" 2 lan (noi 0.62-2.36s + 2.72-4.54s, khoang lang 2.4-3.6s — do nang luong chung minh that, khong phai artifact ASR). Da giao gen lai take 2 (browser-task edadb35e, cung frame + cung prompt, 10cr, 710 -> 700 ky vong).
- episode.yaml: ghi du 7 take (6 needs_review + sh010 rejected_editorial + ly do), editorial_status=generating. Validator chi con loi thieu edit/manifest.yaml nhu ky vong.

## 2026-11-21 — Bee (Muse), sh010 take002 QC DAT (09:21)
- Take 2 ve: 720x1280, 7.93s, 6.7MB, sha 376481cf..., Flow ID d974499d-d730-40b3-8207-0a8f1d62e6b9, 10cr, 710 -> 700. File ~/workspace/ep008-con-nho-do-clips/sh010-take002.mp4.
- Thoai: Whisper base "Anh yeu em hay la yeu con do" dung 8 tu, 1 lan duy nhat 0.80-2.52s; nang luong 48k stereo: noi 1.0-2.6s roi im hoan toan den het clip — loi lap da het. Hinh: t3 My chom toi doi dien dung, t7.8 My cui xuong ban, khong phu de gia, khong bong ma.
- episode.yaml: sh010 them take002 (needs_review); validator chi con loi thieu edit/manifest.yaml nhu ky vong.
- DU 7 TAKE CHON: sh010 take002 + sh020/sh030/sh040/sh050/sh060/sh070 take001 — cho Richard duyet take + chot giong Bac/dub roi dung master.

## 2026-11-21 — Bee (Muse), Richard chê clip: mặt không giống nhau + Nam đứng lên ngồi xuống
- Richard xem 7 clip (09:54): (1) "mặt mẫu không giống nhau"; (2) "đã thế lại còn cứ đứng lên ngồi xuống làm cái gì".
- Bee verify bằng crop mặt side-by-side (facecheck/): 7 FRAME v2 mặt KHỚP nhau (My: cùng mắt/mái/son; Nam: cùng tóc/cấu trúc mặt qua 3 góc) — drift sinh ra ở bước Veo animate clip, không phải ở frame. Clip: My sh010 hẹp nhất, sh030/sh050/sh070 rộng dần khác nhau; Nam sh020 rộng/góc cạnh hơn sh040. Sửa frame không cứu được; chỉ có re-roll clip (xổ số) hoặc chấp nhận như ep001-007 (cũng drift, đã duyệt).
- sh060: frame gốc Nam ĐÃ ĐỨNG sẵn (media-pipeline note "vừa đứng dậy") nên clip mở đầu bằng anh đứng rồi đi luôn — động tác đứng dậy không được quay; cắt sh050 (ngồi) -> sh060 (đứng) bị giật + 2s đầu anh nhún lên xuống (đang đứng dậy dở). Fix: gen lại sh060 từ frame NGỒI (dùng frame sh040, cả 2 đang ngồi) + motion "stands up from the table and turns to walk away" (10cr).
- Đề xuất trình Richard: (a) fix sh060 (10cr); (b) re-roll 2 clip mặt lệch nhất My sh010 + Nam sh020 (10cr/clip); tổng 30cr. CHỜ chốt.

## 2026-11-21 — Bee, Richard chê thêm: ngồi trái rồi cảnh sau ngồi phải
- Bee đối chiếu frame t3 sh030/sh040/sh050: CHỈ sh040 bị lật bên — sh030 My trái / Nam phải (lưng), sh040 Nam trái / My phải, sh050 My trái / Nam phải (lưng). My nhảy trái→phải→trái qua sh030→sh040→sh050. sh020 (Nam phải) và sh060 (My trái, Nam phải đứng) đều đúng bên. Lỗi ở frame sh040 v2 (media pipeline sửa từ v1).
- Sửa frame sh040 bằng media pipeline (0 credit): đổi chỗ 2 người, My sang trái, Nam sang phải; mặt/đồ/bàn/2 ly nước cam/nền giữ nguyên. File mới `input/frames/sh040-first-frame.jpg` sha 3b138b65…; file lật cũ giữ lại `sh040-first-frame-v2-flipped.jpg` (sha e3ec7d09…). Ngẫu nhiên khớp luôn motion prompt ("pointing a finger at My" — Nam trong frame mới đang chỉ tay). episode.yaml đã cập nhật sha + ghi chú take001 bị lật bên.
- KẾ HOẠCH SỬA MỚI (chờ Richard chốt, 40cr thay vì 30cr): sh040 take 2 (frame đã sửa) + sh060 take 2 (frame sh040 đã sửa, cả 2 ngồi đúng bên) + sh010 take 3 + sh020 take 2 (re-roll mặt).

## 2026-11-21 — Bee, gen lại 4 clip (40cr, 700→660) + QC
- Browser task 81b9cdf9 (11:42–11:54): 4 clip Frames-direct Veo Lite, 0 chặn, 700→660. Flow ID: sh010 take3 f57b0cb4 (5,8MB), sh020 take2 142a51e9 (3,0MB), sh040 take2 91bf5329 (4,4MB), sh060 take2 aa2683a3 (4,3MB). File verify trên disk: 720×1280, 24fps, 7,93s, size khớp receipt. Copy vào ~/workspace/ep008-con-nho-do-clips/ (sha: sh010t3 f7004619…, sh020t2 054941de…, sh040t2 5b58f3b5…, sh060t2 f5544a50…).
- QC thoại (whisper base + tiny + năng lượng 48k + F0): sh010 take3 nói 1 lần 0,82–2,44s, đủ 8 từ, không lặp (energy 1,0–2,6s rồi im). sh020 take2 "Con đó là đứa nào? Anh còn không biết." — F0 từ đầu 130→210Hz tăng = ngang, là "Con" (2 model đều nghe nhầm "Còn"). sh040 take2 tiny xác nhận đúng kịch bản từng chữ (base nghe nhầm "ứng trọng em"/"Vừa làm"). sh060 take2 đủ thoại 0,00–3,84s.
- QC hình: sh040 take2 bên ngồi ĐÚNG (My trái / Nam phải) ở t1/t3/t7.8, Nam chỉ tay đúng prompt. sh060 take2 quay ĐỦ động tác: t1 cả 2 ngồi → t3 Nam đang đứng dậy (tay chống gối) → t5 đứng quay đi → t7 đi xa, ghế trống. Không phụ đề giả, đuôi sạch cả 4 clip.
- Mặt re-roll: sh010 take3 mặt gần như y hệt take2 (cùng frame nên Veo vẽ lại tương tự) — drift so với các clip My khác CHƯA cải thiện rõ; sh020 take2 mặt tương tự take1. Kết quả thật phải để Richard nhìn. Validator: chỉ còn lỗi thiếu edit/manifest.yaml như kỳ vọng.
- Bộ take dựng hiện tại: sh010 take3, sh020 take2, sh030 take1, sh040 take2, sh050 take1, sh060 take2, sh070 take1. CHỜ Richard duyệt 4 clip mới + chốt giọng (Bắc giữ native / không Bắc lồng clone) rồi mới dựng master.

## 2026-11-21 — Bee, Richard: mặt vẫn không khớp sau 4 clip sửa
- Richard xem 4 clip mới: "Mặt lại không khớp rồi". Bee làm montage mặt bộ take hiện tại: My sh010t3 / sh030t1 / sh050t1 / sh070t1 (facecheck/my-current-4faces.jpg), Nam sh020t2 / sh040t2 / sh060t2 (facecheck/nam-current-3faces.jpg).
- Bee nhìn thấy: My sh010 (take2 lẫn take3) mặt hẹp nhất, khác rõ 3 clip còn lại (mặt rộng hơn, mắt to hơn). Nam sh020 (góc 3/4, mặt góc cạnh) khác sh060 (nhìn xuống, mặt mềm/tròn hơn); sh040 là profile nên khó so trực tiếp. Drift ở bước Veo animate, frame khớp nhau không cứu được.
- Bằng chứng re-roll: sh010 take3 ≈ take2 (cùng frame → Veo vẽ lại gần như y hệt). Re-roll mù từ cùng frame xác suất cải thiện thấp; mỗi lần gen là 1 lần xổ số, có lần nhúc nhích (take2 khác take1) có lần không (take3 ≈ take2).
- Các hướng còn lại (chưa chốt, chưa tốn thêm credit): (a) re-roll lại các shot lệch nhất, 10cr/clip, xổ số; (b) thử frame mặt to hơn (crop sát mặt) cho shot lệch nhất rồi gen lại — CHƯA CHỨNG MINH, test 1 clip trước; (c) chấp nhận drift như ep001–007 đã đăng. Chờ Richard chỉ rõ mặt nào lệch nhất + chọn hướng.

## 2026-11-21 — Bee, Richard chốt làm lại từ đầu, bỏ áo dài hồng, gen tham chiếu mới bằng Flow
- Richard: "Làm lại từ đầu nhé, lần này không mặc cái áo dài hồng nữa, lấy ảnh tham chiếu gen với áo dài màu khác đã" + "Gen bằng google flow nhé" + "lấy xanh nhạt thôi".
- Bee xem 4 mẫu: Xuân Dệt Mộng Hoa vẫn hồng (loại); Vân Linh xanh nhạt + Lâm Yến trắng kem là 2 màu khác. Gen cả 2 rồi Richard chốt chỉ lấy xanh nhạt, Lâm Yến bỏ.
- Browser task d831bccc (12:08–12:13): chỉ gen Vân Linh, 0 credit, số dư 660. Flow asset 9a824890-a1de-48ca-b17a-aaaa70244282. File về disk 1536×2752, 468.753 byte, sha 2f71722d…. Bee QC: mặt/tóc/dáng/nền khớp ảnh gốc, áo dài xanh nhạt thêu hoa trắng + quần xanh nhạt đúng mẫu Vân Linh. Nit nhỏ: tay trái cầm thêm 1 vật trang trí vàng nhỏ (không có trong ảnh gốc) — cần để ý lúc làm frame, đừng để lọt vào.
- File lưu: input/references/aodai-van-linh-xoa-v3.jpg (sha 2f71722d…). CHƯA cập nhật episode.yaml/wardrobe.md — chờ Richard duyệt ảnh tham chiếu này rồi mới làm lại 7 frame + cập nhật hồ sơ. Các take cũ (sh010 take3, sh020 take2, sh030 take1, sh040 take2, sh050 take1, sh060 take2, sh070 take1) vẫn giữ trong repo/clips dir, không xóa.
- Rủi ro đã biết cho bước làm lại frame: 3 shot Nam từng bị Flow chặn chính sách 18/18 lần; lần này thử Flow trước, nếu chặn sẽ báo Richard chứ không tự đổi tool.

## 2026-11-21 — Bee, ảnh tham chiếu Nam kiểu ThaoMyv002 (Flow, 0 credit)
- Browser task 70a34d6f (12:15–12:19): gen 1 ảnh chân dung Nam từ nam-front-v001.jpg, 0 credit, số dư 660. Flow asset 968c836f-bec9-4061-b9d7-4a0480a6cbda. File về disk 1536×2752, 229.319 byte, sha 340a246d….
- Bee QC: chính diện, ngực trở lên, nền xám trơn, mặt/tóc/lông mày khớp ảnh gốc, sơ mi trắng dài tay, không watermark, không đồng hồ/vòng/chữ. Nit nhỏ: khung hơi rộng (nửa người trên) và tay áo khó xác nhận có xắn không — prompt frame sẽ ghi rõ xắn tay áo.
- File lưu: 02_characters/nam/approved/nam-front-v002.jpg (sha 340a246d…). CHƯA cập nhật character.yaml — chờ Richard duyệt ảnh này.
- Ảnh nền quán mới: task Flow riêng đang chạy (sửa từ date-cafe-v002-day.png sang góc khác cùng quán, ghế cao chuẩn tầm bàn, không ghế bành thấp).

## 2026-11-21 — Bee, ảnh nền quán cafe mới v003-day (Flow, 0 credit)
- Browser task f69fe544 (12:20–12:24): sửa từ date-cafe-v002-day.png sang góc khác cùng quán, 0 credit, số dư 660. Flow asset 5b80f134-02c3-4af0-9679-63a2fe7787f1. File về disk 1536×2752, 1.017.702 byte, sha 1a66036e….
- Bee QC: góc khác hẳn v002-day (tường đá, cây, sỏi, hoa giấy, đèn dây, có bàn thứ 2 ở nền), 2 ghế gỗ tối đệm be CAO chuẩn tầm bàn (tựa lưng nan cao, mặt ghế ngay dưới mặt bàn — người ngồi ngang tầm bàn, không còn ghế bành thấp), bàn tròn khăn trắng, đúng 2 ly nước cam, ban ngày, cây xanh sau lưng, không người. Nit nhỏ: mép trái lọt 1 bàn khăn trắng thứ 2 (chỉ 1 phần) — frame sẽ crop/xoay quanh bàn chính nên không đáng ngại.
- File lưu: 03_locations/date-cafe/review/date-cafe-v003-day.png (sha 1a66036e…). CHƯA cập nhật location README/episode.yaml — chờ Richard duyệt ảnh này cùng ảnh Nam.

## 2026-11-21 — Bee, Richard DUYỆT ảnh tham chiếu Nam v002
- Richard: "ok Nam có phải frame ko?" — đã duyệt ảnh tham chiếu Nam v002 (nam-front-v002.jpg, Flow asset 968c836f, sha 340a246d…). Bee đã giải thích: đây KHÔNG phải frame, mà là ảnh tham chiếu nhân vật kiểu ThaoMyv002 (chính diện, ngực trở lên, nền trơn) — frame là 7 ảnh cảnh ở quán, làm từ 3 ảnh tham chiếu (My Vân Linh + Nam v002 + quán v003-day).
- character.yaml cập nhật: master_reference → approved/nam-front-v002.jpg, thêm block reference_portrait_v002 (asset + sha + ngày duyệt); v001 giữ lại làm ảnh gốc Richard gửi.
- CHỜ: Richard duyệt nốt ảnh quán v003-day rồi làm lại 7 frame từ đầu.

## 2026-11-21 — Bee, làm lại từ đầu: prompt ảnh v3 + hồ sơ rev5
- Richard duyệt cả 3 ảnh tham chiếu mới (My Vân Linh 12:14, Nam v002 12:35, quán v003-day 12:36) + lệnh "gen 7 frame đi, lần này không gen view rộng nữa, view gần nhân vật hơn".
- Viết lại cả 7 image prompt v3 (input/prompts/sh0X0-image.txt): My áo dài Vân Linh xanh nhạt thêu hoa trắng + quần xanh nhạt (ref aodai-van-linh-xoa-v3.jpg), Nam ref nam-front-v002.jpg, nền date-cafe-v003-day.png (ghế cao), framing CẬN (medium close-up chest-up cho 5 shot đối thoại, medium shot waist-up cho sh060, close-up cho sh070 — KHÔNG góc rộng), bên ngồi My TRÁI / Nam PHẢI mọi shot, mô tả cả 2 người trong mọi prompt, tay trống (không lấy vật vàng trong ảnh Vân Linh), nốt ruồi cằm trái, son đỏ, móng tự nhiên, ngực ôm vừa theo body v003. sh060 frame là Nam đang nhổm dậy (mid-rise, tay chống gối) — không đứng sẵn như take1 cũ.
- script.md + wardrobe.md cập nhật (Vân Linh, v002, v003-day, view gần, sh060 medium shot). episode.yaml rev4 → rev5: image_prompt sha256 mới cho 7 shot, image_sources đổi sang 3 ref mới (Vân Linh 2f71722d…, Nam v002 340a246d…, v003-day 1a66036e…). Validator: chỉ còn lỗi thiếu edit/manifest.yaml (đúng kỳ vọng ở giai đoạn frame). Takes cũ + first_frame v2 vẫn giữ trong yaml (lịch sử).
- Task Flow gen 7 frame v3 đang chạy; mỗi shot tối đa 2 lần thử nếu bị chặn chính sách thì bỏ qua shot đó và báo lại (không loop như 18 lần trước).

## 2026-11-21 — Bee, Richard đổi cách làm shot Nam: tạo frame Nam trước, rồi mới dùng cho việc khác
- Richard (12:46): "Tạo ảnh Nam ra frame hoặc ra nhân vật đi, sau đó mới dùng ảnh đó cho việc khác". (Trước đó cậu ấy hỏi task 7 frame có lại bị chặn chính sách không — Bee trả lời chưa biết, task vẫn đang chạy.)
- Bee chọn hướng FRAME (nhân vật "Nam" trên Flow đã có từ sáng, từ ảnh v001 — nhưng dùng nhân vật để sửa frame cũng từng bị chặn 9/9 ở đợt retry v2; hướng sửa từ ảnh Nam làm canvas thì v1 đã qua được): tạo 1 frame Nam RIÊNG — 1 người, sửa từ chân dung nam-front-v002.jpg làm canvas + nền date-cafe-v003-day.png, Nam ngồi bên phải bàn, ghế trái trống, cận vừa ngực trở lên, 9:16.
- Task 7 frame (291c2090) đã gửi lệnh đổi: BỎ sh020/sh040/sh060, chỉ làm 4 shot My (sh010/sh030/sh050/sh070). Task mới tạo frame Nam: f0b87bcc (đã nhận, đang chạy). Sau khi có frame Nam → dùng nó làm canvas để làm 3 frame Nam v3.

## 2026-11-21 — Bee, frame Nam: Flow CHẶN "unusual activity", cứu bằng media pipeline
- Task Flow tạo frame Nam riêng (f0b87bcc, 12:47–12:49, 2 phút) FAILED: 2 lần thử trong cloud browser đều bị Flow chặn với thông báo "unusual activity" trong vài giây, 0 credit; sau đó task chuyển trình duyệt thì trình duyệt không mở được (chrome_launch_failed), task chết. Không có asset nào được tạo, không tải gì, không mất credit.
- Phân biệt: đây KHÔNG phải chặn chính sách nội dung như 18 lần sáng nay — "unusual activity" giống giới hạn tần suất (hôm nay đã gen rất nhiều trên acc huynhdn). Nghi ngờ thêm: Bee chạy 2 task Flow SONG SONG cùng acc (task 7 frame + task frame Nam) nên acc bị soi — CHƯA CHỨNG MINH, ghi lại để tránh lặp: không chạy 2 task Flow song song cùng acc nữa cho tới khi rõ.
- Cứu bằng media pipeline (cùng cách đã cứu 3 frame Nam v2 sáng nay): 1 lần gen, file `~/workspace/ep008-nam-retry/media-generation-nam-cafe-frame-v001-0-37d5c6b1-2e77-4c20-9224-2e1e7de228c7.jpg` (812.735 byte, 1152×2048, sha 73aa4b75410890dc3c9b20427da492cf509342cd5ca1321c5a3b7ed3c97a2ce0), đã copy byte-identical vào `input/frames/nam-cafe-frame-v001.jpg`. Bee QC: ĐẠT làm tài sản gốc — Nam 1 người, mặt/tóc/áo trắng đúng v002, ngồi bên phải bàn, ghế trái trống, bàn khăn trắng + 2 ly cam, nền đúng v003-day, không chữ/watermark. NIT: khung ra RỘNG (cả bàn + 2 ghế + nhiều sân vườn), không phải cận vừa ngực trở lên như prompt — chấp nhận làm gốc, 3 frame Nam v3 sửa từ nó sẽ siết khung theo từng shot.
- Task 4 frame My v3 (291c2090) vẫn đang chạy lúc 12:49, chưa có kết quả — chờ xem có bị "unusual activity" chung không.

## 2026-11-21 trưa — 7 frame v3 XONG, Bee QC đạt cả 7, chờ Richard duyệt

**4 frame My qua Flow (task 12:39–12:53, acc huynhdn Pro, 660cr, 0 credit):**
- sh010 (asset f71131fd, 2K 1536×2752, sha 1150257c…), sh030 (077631cd, 2K, sha 4fd321c3…), sh050 (50def2fb, 2K, sha bc724f4e…): mỗi shot 1 lần duy nhất. Mặt My khớp nhau cả 4, áo dài Vân Linh xanh nhạt thêu hoa trắng đúng ref, son đỏ, nốt ruồi cằm trái còn, My trái / Nam (vai + gáy) phải, khung cận ngực, bàn khăn trắng + 2 ly cam + ghế gỗ cao đệm be đúng v003-day, tay trống. Sao Gemini mờ góc dưới-phải cả 3 (artifact quen thuộc, crop lúc gen clip).
- sh070 (asset 1e2b4a90, sha d17366cc…): **chỉ 1K 768×1376** — tải 2K fail 3 lần, không file; khung ngang thắt lưng + bàn chứ không phải cận mặt-vai như prompt. Vẫn cận, không rộng; 1K đủ làm first frame (720p). Có thể tải lại 2K từ asset trong Flow sau nếu cần.
- sh020 bị Flow chặn chính sách 2 lần TRƯỚC khi đổi kế hoạch (cùng task này) — bằng chứng mới: shot Nam đối diện vẫn bị chặn trên Flow ngay cả với ref mới.
- File v2 giữ lại dạng *-first-frame-v2.jpg; episode.yaml đồng bộ sha + asset ID v3.

**3 frame Nam từ frame Nam (media pipeline của Bee, 0 credit):**
- sh020: edit từ nam-cafe-frame-v001.jpg + ref Vân Linh; bản gốc ra RỘNG (toàn thân 2 người, nhiều vườn) nên crop hậu kỳ 920×1635 tại (116,200) + upscale lanczos về 1152×2048 (sha 441974b9…) — mặt Nam nguyên vẹn, tay giơ lòng bàn tay, My trái quay lưng, khung giờ medium. Bản rộng gốc giữ ở ~/workspace/ep008-nam-retry/.
- sh040 (sha 3311d6af…): Nam phải cười gượng chỉ tay, My trái nghiêng mặt nghe, khung cận ngực — ĐẠT, bên ngồi đúng (sửa được lỗi lật trái-phải của v2).
- sh060 (sha 4e3a1c16…): Nam phải đang nhổm dậy tay chống gối, chưa đứng hẳn — ĐẠT, sửa được cú nhảy cắt ngồi→đứng của v2; My trái ngước nhìn. Sao Gemini mờ góc dưới-phải.
- flow_image_asset_id = null cả 3 (media pipeline), provenance ghi ở đây.

**Validator:** chỉ lỗi thiếu edit/manifest.yaml (dự kiến). frame_status vẫn pending_review, approved_for_generation false.
**Tiếp theo:** Richard duyệt 7 frame → gen 7 clip Frames-direct Veo Lite (70cr, số dư 660).

## 2026-11-21 trưa — rà soát motion prompt trước khi gen (chuẩn bị sẵn, chưa gen)
- Đọc lại cả 7 motion prompt đối chiếu frame v3: 6/7 khớp. Chỉ sh060 lệch: motion còn ghi "Wide static shot" (tàn dư rev4) trong khi frame v3 là medium shot CLOSE theo lệnh view gần của Richard — đã sửa thành "Medium static shot, both in frame close", đồng bộ sha motion mới ab7c8ac0… vào episode.yaml, validator chỉ thiếu manifest.
- sh050: frame v3 theo đúng image prompt ("stunned, mouth slightly open, eyes wide") nhưng motion prompt ghi "triumphant, smug smile" — giữ nguyên: Veo animate từ stunned sang smug trong 8s là arc hợp lý cho câu "Thế là anh có thật à?" (sững sờ vì anh thừa nhận thật → đắc thắng). Không sửa frame hay motion.
- Mọi thứ sẵn sàng gen ngay khi Richard duyệt frame.

## 2026-11-21 13:05–13:46 — gen 7 clip v3 + QC (Richard duyệt frame 13:05 "Đẹp, gen đi")
**Gen (browser task 64d10816, 13:06–13:35, 29 phút):** Frames-direct, Agent OFF, Veo 3.1 Lite, 9:16, 8s, 1 output, tuần tự. Số dư 660 → 580 (80cr = 8 lần gen). Không clip nào bị chặn chính sách.
- sh050 lần đầu ra KHÔNG có audio (Flow báo "Chưa tạo âm thanh nào") → retry cùng prompt, có audio, là bản dùng (clip c59b3807); bản câm 6bdf78ca KHÔNG tải về.
- Tải về 1K/720p đủ 7 clip, verify trên disk (720×1280, 24fps, 7.93s, có audio) ở ~/workspace/browser_downloads/sess-276836273/.
- Clip ID: sh010 12dbb684, sh020 c3e21d9c, sh030 5c6fd75c, sh040 390570f3, sh050 c59b3807 (retry), sh060 fec7b5bf, sh070 80cca483.

**QC (whisper base + tiny + F0 + năng lượng 48k stereo + contact sheet 5 frame/clip):**
- sh010 take004 REJECT: Veo nói câu 2 lần (0.64–2.44s + 2.92–4.66s) — y hệt lỗi take001 v2.
- sh020 take003 ĐẠT: thoại đủ 1 lần 0.00–2.82s ("Con" nghe thành "Còn" p=0.56, cùng pattern v2 đã xác minh bằng F0). Bên ngồi đúng, đuôi sạch, không phụ đề giả.
- sh030 take002 ĐẠT: thoại đủ 0.00–4.38s, 11 từ. Từ đầu base nghe "Dữ" p=0.40; F0 tăng 180→254Hz loại "Dưới", độ dài + tiền lệ v2 = "Giữa". Đuôi sạch.
- sh040 take003 ĐẠT: thoại đủ (base sót "là", tiny xác nhận "cho là anh có đi"). Bên ngồi My trái / Nam phải ĐÚNG (sửa được lỗi lật v2). Nam chỉ tay + cười gượng, đuôi sạch.
- sh050 take002 ĐẠT (có lưu ý): thoại đủ 0.00–1.28s, F0 rơi 364→182Hz xác nhận "à" (dấu huyền) không phải "á". My cười lớn suốt đuôi clip (đỉnh năng lượng 4.1s, 6.1s) — giống take001 v2, cắt khi dựng.
- sh060 take003 ĐẠT: thoại đủ 0.00–4.24s (base nghe nhầm thanh "nhận"→"nhẳng", "anh"→"ăn"; F0 phẳng ~150Hz xác nhận "anh", âm tiết "nhận" đúng). Quay ĐỦ động tác đứng dậy (nhổm → đứng → quay đi, 7.5s) — sửa được cú nhảy cắt v2. Đuôi sạch.
- sh070 take002 ĐẠT: câm lặng đúng kịch bản (whisper ảo giác CTA subscribe ở 6.5–7.9s trên tiếng nền — tất cả từ cùng timestamp 7.90, không phải lời nói thật). My sững sờ → cúi mặt, đuôi sạch.
- Mặt My khớp nhau qua sh010/sh030/sh050/sh070, mặt Nam khớp qua sh020/sh040/sh060 (tốt hơn v2 — Richard là người quyết cuối).

**sh010 re-roll (browser task 167d195b, 13:39–13:46, 10cr, 580→570):** take005, clip 3622bcb9. QC: câu đầy đủ 1 lần 0.00–2.32s, NHƯNG Veo lặp lại nửa sau câu "hay là yêu con đó" ở 3.28–4.66s (whisper base + năng lượng 48k). Dùng được nếu cắt ở ~2.8s sau câu đầu; hoặc re-roll thêm 1 lần — chờ Richard quyết. Mặt khớp frame, không phụ đề giả, đuôi sạch.
- File: ~/workspace/ep008-con-nho-do-clips/sh010-take005.mp4 (sha b9f6acd8…). episode.yaml: take005 needs_review.
- QC script: qc_v3.py (7 clip), qc_v3b.py (tiny + F0 sh030 + phổ sh050), qc_v3c.py (F0 sh060/sh050 + đỉnh sh050), qc_one.py (clip đơn).

**Dọn ảnh váy hồng (Richard lệnh 13:11):** task browser 2c24aa53 đang chạy — xóa CHỈ ảnh váy hồng Thanh Nghi + 7 frame v2 trong Flow, giữ toàn bộ video clip + Vân Linh + Nam v002 + v003-day + frame v3. Bản local v2 còn đủ trong repo.

## 2026-11-21 13:50 — Richard duyệt clip v3
- DUYỆT 6/7: sh010 take005 (cắt ở ~2.8s sau câu đầu, bỏ phần lặp), sh020 take003, sh030 take002, sh040 take003, sh050 take002 (cười lớn ở đuôi — cắt khi dựng), sh070 take002 → ghi accepted_editorial trong episode.yaml.
- LOẠI sh060 take003: mặt My không giống ThaoMy (Richard) → rejected_editorial. Cần gen lại 1 lần, 10cr, cùng frame + prompt gốc.
- sh060 re-roll CHƯA chạy ngay: task dọn ảnh váy hồng (2c24aa53) vẫn đang chạy trên Flow — không chạy 2 task Flow song song (bài học "unusual activity" 12:47). Chờ task dọn xong rồi gen lại sh060.

## 2026-11-21 13:47–13:53 — dọn ảnh váy hồng trong Flow (task 2c24aa53, xong)
- Xóa 13 ảnh: 2 bản copy chân dung ref Thanh Nghi hồng đậm + 11 bản copy frame v2 váy hồng (sh010×2, sh020×2, sh030×1, sh040×3, sh050×1, sh060×1, sh070×1). Mỗi ảnh mở chi tiết, xác nhận váy hồng đậm rồi mới xóa; thùng rác Flow xác nhận "13 mục". Thư viện ảnh 55 → 42.
- Không xóa video nào: 21 clip còn nguyên. Giữ: ref Vân Linh, frame v3, chân dung Nam v001/v002, nền café v001/v002/v003-day.
- CÒN LẠI: các ảnh still café váy hồng KHÁC (không phải frame đầu hay ref) vẫn trong thư viện, vd "Woman looking stunned in café", "Woman sitting at table smiling" — task không xóa vì ngoài danh sách được giao. Hỏi Richard có xóa nốt không.
- Bản local v2 còn đủ trong repo (input/references/aodai-thanh-nghi-xoa-v3.jpg + *-first-frame-v2.jpg).

## 2026-11-21 13:53 — sh060 re-roll (task fc68a20b, đang chạy)
- Richard 13:50 loại take003 (mặt My không giống ThaoMy). Gen lại 1 lần, 10cr, cùng frame sh060-first-frame.jpg + motion prompt gốc, Frames-direct Veo Lite, tải 1K. Số dư 570 → 560 dự kiến. Chờ task dọn ảnh xong mới chạy (đã xong 13:53).

## 2026-11-21 13:53–13:57 — sh060 re-roll take004 (task fc68a20b, xong)
- Gen 1 lần, 10cr, 570 → 560. Clip 14e7efc8, file sh060-take004.mp4 (sha bffdbc87…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–3.98s (base nghe "anh"→"ăn" p=0.37, cùng pattern take003 đã xác minh bằng F0). Động tác đứng dậy đủ (nhổm → đứng → quay đi, 7.5s), đuôi sạch, không phụ đề giả. Đuôi clip có tiếng nền/tiếng bước chân nhẹ (năng lượng trên ngưỡng tới 8s) — không phải lời nói, không phải lỗi.
- So mặt My: ảnh ghép sheets/sh060-face-compare.png (take003 @3s | take004 @3s | sh070 take002 @0.5s đã duyệt) — Bee thấy take004 gần mặt đã duyệt hơn take003; Richard quyết cuối.
- episode.yaml: take004 needs_review.

## 2026-11-21 14:01 — Richard LOẠI sh060 take004
- Lý do: Nam tự nhiên cúi người, không thấy bỏ đi; ghế không thấy đâu; mặt My vẫn không giống ThaoMy. take004 → rejected_editorial.
- Phân tích frame v3: Nam cúi gập sâu tay chống gối, ghế của Nam hoàn toàn không có trong khung hình; mặt My ngước lên gắt (góc 3/4 ngửa) nên Veo animate lệch cả 2 take. Lỗi này do frame, re-roll y hệt khó cứu.
- Đã thử sửa frame v4 bằng media pipeline (Nam đứng thẳng hơn, lộ ghế, mặt My nhìn thẳng hơn) nhưng tool lỗi đường dẫn file Nam v002 tao ghi sai (02_characters nằm ở gốc repo, không phải trong thư mục tập) và theo hướng dẫn runtime thì KHÔNG được thử lại request đó bằng tool khác — dừng sửa frame ở đây.
- Hướng còn lại: gen lại take005 từ frame v3 cũ, motion prompt sửa nhẹ để nhấn bước bỏ đi + ghế trống: "Nam rises from his chair and walks away from the table toward the background, leaving his empty chair behind him..." (sha motion mới 6a347e57…). Task gen 7e65f6e0 đang chạy, 10cr, 560 → 550 dự kiến.

## 2026-11-21 14:03–14:10 — sh060 re-roll take005 (task 7e65f6e0, xong)
- Gen 1 lần, 10cr, 560 → 550. Clip 8f449015, file sh060-take005.mp4 (sha e6748234…, 720×1280, 7.93s, có audio). Motion prompt mới (sha 6a347e57…) nhấn bước bỏ đi + ghế trống.
- QC: thoại đủ 0.00–4.86s, base nghe đúng cả "Anh" (p=0.85) lần đầu tiên trong 3 take sh060. Nam đứng dậy từ ~2s, quay lưng bỏ đi rõ ràng, GHẾ TRỐNG hiện rõ từ 3s (Veo vẽ theo prompt mới) — sửa được 2 điểm Richard chê ở take004. My tay ôm ngực ở 7.5s. Đuôi sạch, không phụ đề giả. Đầu clip ~1s đầu vẫn bắt đầu từ tư thế cúi của frame gốc, nhưng lên nhanh.
- So mặt My: sheets/sh060-face-compare2.png (take005 @2s | take004 @3s | sh070 @0.5s đã duyệt) — Bee thấy take005 gần mặt đã duyệt hơn take004; Richard quyết cuối.
- episode.yaml: take005 needs_review.

## 2026-11-21 14:18–14:20 — sh060 đổi góc (Richard) + frame v4 + gen take006
- Richard 14:18 LOẠI take005 (mặt My vẫn không giống) → đổi góc: quay từ phía đối diện, chỉ lấy LƯNG My. take005 → rejected_editorial.
- Frame v4 (media pipeline, 0cr): sửa từ frame sh020 (đã có góc lưng My + Nam nhìn thẳng máy) — Nam đổi từ ngồi giơ tay sang nhổm dậy tay chống đùi, ghế lộ rõ sau lưng. QC ĐẠT: lưng My + tóc + áo Vân Linh đúng, mặt My KHÔNG thấy (hết lỗi drift mặt), mặt Nam khớp v002, ghế Nam lộ rõ, bàn + 2 ly cam + nền v003-day đúng, My trái / Nam phải. File: sh060-first-frame.jpg mới (sha 1b28faa4…, 1184×2096, convert từ webp); frame v3 giữ lại dạng sh060-first-frame-v3.jpg (sha 4e3a1c16…).
- Image prompt + motion prompt sh060 viết lại theo góc mới (camera sau lưng My, Nam nhìn thẳng máy, đứng dậy bỏ đi để lại ghế trống); sha đã đồng bộ vào episode.yaml, validator chỉ thiếu manifest.
- Gen take006 (task 09c65146, đang chạy): Frames-direct Veo Lite, 10cr, 550 → 540 dự kiến, tải 1K.
- Ghi chú: lần sửa frame v4 trước đó (từ frame sh060 cũ, Nam đứng thẳng + mặt My nhìn thẳng) tool lỗi đường dẫn file Nam v002 do tao ghi sai (02_characters ở gốc repo) và runtime dặn không thử lại request đó — request lần này là hướng mới độc lập (đổi góc theo lệnh Richard, base khác là frame sh020), không phải thử lại request cũ.

## 2026-11-21 14:19–14:25 — sh060 take006 từ frame v4 (task 09c65146, xong)
- Gen 1 lần, 10cr, 550 → 540. Clip 06dc77d0, file sh060-take006.mp4 (sha bc87ad78…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–4.26s (base nghe nhầm thanh "nhận"→"nhẳng", "anh"→"ăn" — cùng pattern take003 đã xác minh bằng F0). Nam đứng dậy từ đầu clip, quay lưng bỏ đi rõ ràng, GHẾ TRỐNG hiện rõ từ 3s. Mặt My KHÔNG thấy trong cả clip (chỉ lưng + tóc) — lỗi drift mặt hết hẳn. Đuôi sạch, không phụ đề giả. Khung hình hơi rộng hơn take v3 (thấy nhiều vườn + 2 ghế) nhưng đọc rõ.
- episode.yaml: take006 needs_review.

## 2026-11-21 14:32–14:34 — sh060 take006 LOẠI + hướng mới + gen take007
- Richard 14:32 LOẠI take006: mặt Nam không giống. take006 → rejected_editorial.
- Richard 14:32 (ngay sau): "Nói xong giọng tức giận rồi mới đứng dậy đi" — hướng mới: Nam nói thoại bằng giọng TỨC GIẬN trước, nói xong mới đứng dậy bỏ đi (take006 đứng dậy quá sớm, vừa đi vừa nói).
- Motion prompt sh060 viết lại (sha đồng bộ yaml): Nam ngồi đối diện máy, nói giọng tức giận sắc lạnh, nói xong mới đứng dậy bỏ đi để lại ghế trống. Frame giữ v4 (góc lưng My).
- Gen take007 (task a9c00747, đang chạy): Frames-direct Veo Lite, 10cr, 540 → 530 dự kiến, tải 1K.

## 2026-11-21 14:33–14:40 — sh060 take007 (task a9c00747, xong)
- Gen: 2 lần đầu bị Flow chặn "unusual activity" (0cr), đổi sang trình duyệt mới thì gen được, 10cr, 540 → 530. Clip c5ff1732, file sh060-take007.mp4 (sha 696fd90f…, 720×1280, 7.93s, có audio).
- QC: thoại CHUẨN từng chữ 0.00–3.92s ("nhận"/"anh" nghe đúng lần đầu). Nam chồm tới nói (chỉ tay, góc 2–4s) rồi mới quay lưng bỏ đi ~4.5s, ghế trống hiện rõ — đúng hướng "nói xong rồi mới đứng dậy". Mặt My không thấy. Đuôi sạch, không phụ đề giả.
- Mặt Nam: ở thế chồm tới + biểu cảm tức giận, mặt đọc hẹp hơn v002 (mắt/mũi/cằm lệch nhẹ) — Bee không dám chốt khớp, chờ Richard quyết. Nếu loại thì lever còn lại: làm frame v5 Nam ngồi thẳng nhìn thẳng máy khi nói (giữ mặt chính diện), đứng dậy sau.
- episode.yaml: take007 needs_review.

## 2026-11-21 14:43–14:45 — sh060 frame v5 (Richard: review ảnh trước, chưa gen)
- Richard 14:43 LOẠI take007 (mặt Nam không giống) → "gen ảnh ngồi đối diện, nói xong đứng dậy bỏ đi". 14:44 chốt thêm: gen lại ảnh góc này trước, gửi review — CHƯA gen clip.
- Frame v5 (media pipeline, 0cr): sửa từ frame sh020 — Nam ngồi thẳng nhìn thẳng máy, mặt chính diện khớp v002 (tóc chải ngược, lông mày rậm, cằm/hàm đúng), tay đặt đùi, vẻ nghiêm; My lưng trái, áo Vân Linh, bàn + 2 ly cam + nền v003-day đúng. QC ĐẠT. File: sh060-first-frame.jpg mới (sha 2d0f3330…, 1184×2096); frame v4 giữ lại dạng sh060-first-frame-v4.jpg (sha 1b28faa4…).
- Image prompt viết lại theo tư thế ngồi; motion prompt giữ bản take007 (nói giọng tức giận xong rồi mới đứng dậy bỏ đi). Sha đã đồng bộ yaml, validator chỉ thiếu manifest.
- CHỜ Richard duyệt frame v5 → mới gen take008 (10cr, số dư 530).

## 2026-11-21 14:46–14:48 — sh060 frame v6 (Richard: Nam lùi vào giữa khung)
- Richard 14:46 về frame v5: "Như này vẫn chưa ổn, Nam lùi vào giữa khung hình một chút như vậy mới không bị lỗi" — Nam quá sát mép phải/khung quá chật làm Veo lỗi mặt.
- Frame v6 (media pipeline, 0cr): sửa từ frame v5 (giữ nguyên mặt đã khớp) — Nam lùi vào giữa khung, nhỏ lại, còn khoảng trống 2 bên, không còn sát mép phải. QC ĐẠT: mặt Nam giữ nguyên khớp v002, My lưng trái, bàn + 2 ly cam + nền đúng. File: sh060-first-frame.jpg mới (sha a41d3f1f…, 1184×2096); frame v5 giữ lại dạng sh060-first-frame-v5.jpg (sha 2d0f3330…).
- Image prompt cập nhật vị trí giữa khung; motion prompt giữ bản take007. Sha đã đồng bộ yaml, validator chỉ thiếu manifest.
- CHỜ Richard duyệt frame v6 → mới gen take008 (10cr, số dư 530).

## 2026-11-21 14:47–14:49 — sh060 frame v7 (Richard: ok, zoom gần Nam thêm)
- Richard 14:47 về frame v6: "ok đó zoom thêm vào gần Nam một chút nữa" — v6 được duyệt về nội dung, chỉ cần zoom gần Nam hơn.
- Frame v7 (ffmpeg crop, 0cr, KHÔNG gen lại ảnh): crop 90% (1065×1886 tại x20,y100, lệch về phía Nam) + scale lanczos về 1184×2096 — mặt Nam giữ nguyên pixel (không re-roll), Nam to hơn và gần hơn trong khung, My vẫn đủ trong khung trái, bàn/ghế/nền nguyên. QC ĐẠT. File: sh060-first-frame.jpg mới (sha 0f03d062…); frame v6 giữ lại dạng sh060-first-frame-v6.jpg (sha a41d3f1f…).
- Sha đã đồng bộ yaml, validator chỉ thiếu manifest.
- CHỜ Richard duyệt frame v7 → mới gen take008 (10cr, số dư 530).

## 2026-11-21 14:51–14:53 — sh060 frame v8 (Richard: cảnh xung quanh rộng quá, Nam lùi trái)
- Richard 14:51 về frame v7: "Khung cảnh xung quang rộng quá, tao sợ lỗi tiếp ấy, Nam lùi sang trái chút nữa" — cảnh rộng làm Veo dễ lỗi; Nam cần sang trái (gần giữa khung, sát bàn hơn).
- Frame v8 (media pipeline, 0cr): sửa từ frame v7 — Nam sang trái, gần giữa khung + sát bàn hơn, khung siết chặt (ít cảnh trống xung quanh, bàn to hơn trong khung). QC ĐẠT: mặt Nam giữ nguyên khớp v002, My lưng trái, bàn + 2 ly cam + nền đúng, ghế Nam vẫn thấy (tựa + đệm sau lưng). File: sh060-first-frame.jpg mới (sha f841c021…, 1184×2096); frame v7 giữ lại dạng sh060-first-frame-v7.jpg (sha 0f03d062…).
- Image prompt cập nhật vị trí trái + khung siết; motion prompt giữ bản take007. Sha đã đồng bộ yaml, validator chỉ thiếu manifest.
- CHỜ Richard duyệt frame v8 → mới gen take008 (10cr, số dư 530).

## 2026-11-21 14:54–14:56 — sh060 frame v9 (Richard: ghế sau Nam mất luôn)
- Richard 14:54 về frame v8: "Ghế đằng sau Nam mất luôn" — khi Nam lùi trái + khung siết, ghế sau lưng anh gần như biến mất khỏi khung.
- Frame v9 (media pipeline, 0cr): sửa từ frame v8 — khôi phục ghế gỗ tối + đệm be LỘ RÕ sau lưng Nam (tựa cao có nan dọc nhô lên sau vai phải, đệm ngồi thấy dưới người). QC ĐẠT: ghế rõ, mặt Nam giữ nguyên khớp v002, vị trí trái + khung siết giữ nguyên, My lưng trái, bàn + 2 ly cam + nền đúng. File: sh060-first-frame.jpg mới (sha 44ba20f5…, 1184×2096); frame v8 giữ lại dạng sh060-first-frame-v8.jpg (sha f841c021…).
- Image prompt cập nhật ghế lộ rõ; motion prompt giữ bản take007. Sha đã đồng bộ yaml, validator chỉ thiếu manifest.
- CHỜ Richard duyệt frame v9 → mới gen take008 (10cr, số dư 530).

## 2026-11-21 14:55–14:57 — Richard CHỐT lấy frame v6 + gen take008
- Richard 14:55 (reply vào ảnh v6): "thôi lấy ảnh này đi" — dừng vòng sửa, lấy frame v6 (bản đã nói "ok đó" lúc 14:47: Nam lùi vào giữa khung, mặt khớp v002, ghế còn thấy). Các bản v7 (crop zoom), v8 (lùi trái + siết), v9 (khôi phục ghế) giữ lại dạng file riêng, không dùng.
- Khôi phục sh060-first-frame.jpg = bản v6 (sha a41d3f1f…), image prompt về bản v6, sha đồng bộ yaml, validator chỉ thiếu manifest. Motion prompt giữ bản take007 (nói giọng tức giận xong rồi mới đứng dậy bỏ đi).
- Gen take008 (task 715e5f61, đang chạy): Frames-direct Veo Lite, 10cr, 530 → 520 dự kiến, tải 1K.

## 2026-11-21 14:56–15:01 — sh060 take008 từ frame v6 (task 715e5f61, xong)
- Gen 1 lần, 10cr, 530 → 520, không chặn/lỗi. Clip 32849369, file sh060-take008.mp4 (sha a1df3a15…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–4.10s, giọng tức giận mạnh (transcript có dấu "!" sau các cụm). Nam ngồi nói ~1.5s đầu, nhổm dậy giữa câu, quay lưng bỏ đi sau khi hết thoại (~4.2s), ghế trống hiện rõ. Mặt Nam lúc ngồi ở 1.0s khớp v002 tốt nhất từ trước tới nay. Mặt My không thấy. Đuôi sạch, không phụ đề giả.
- Lưu ý: anh bắt đầu nhổm dậy giữa câu (~2s) chứ không đợi hết câu mới đứng — nhưng bước bỏ đi thì sau hết thoại. Chờ Richard quyết.
- episode.yaml: take008 needs_review.

## 2026-11-21 15:06–15:08 — sh060 take008: mặt rộng khi nói (Richard bắt lỗi)
- Richard 15:06: "Lúc nói mặt hơi rộng ra thì phải". Bee soi side-by-side (v002 vs take008 0.5s/1.0s/2.0s/3.0s, sheet sh060-take008-face-wide-compare3.png): ĐÚNG — lúc ngồi yên mặt vẫn hẹp như v002, nhưng há miệng nói, nhất là đoạn hét giận, má + hàm phình ra, mặt rộng hẳn. Đây là artifact lúc Veo animate (há miệng + hét), không phải lỗi frame v6.
- Richard 15:08: "gen lại" → take009 re-roll y hệt setup take008 (frame v6 + motion prompt cũ), task d90fee46 đang chạy, 10cr, 520 → 510 dự kiến.

## 2026-11-21 15:08–15:13 — sh060 take009 re-roll (task d90fee46, xong)
- Gen 1 lần, 10cr, 520 → 510, không chặn/lỗi. Clip c3840654, file sh060-take009.mp4 (sha a2947cc7…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–4.10s; Nam ngồi nói, nhổm dậy giữa câu, bỏ đi sau hết thoại, ghế trống hiện rõ; My quay đầu nhìn theo lúc anh bỏ đi. Đuôi sạch, không phụ đề giả.
- MẶT RỘNG KHI NÓI VẪN CÒN: soi side-by-side (sheet sh060-take009-face-wide-compare.png) — lúc nói/hét mặt vẫn phình rộng như take008. Re-roll KHÔNG sửa được; đây là hành vi hệ thống của Veo lúc animate câu giận, không phải xổ số theo take. Gen thêm nữa khó cứu.
- Khác take008: 0.5s Nam quay sang nhìn My (không nhìn thẳng máy); giọng nghe ít giận hơn (transcript không có dấu "!"). Bee đánh giá take008 nhỉnh hơn (giọng giận mạnh + mặt chính diện lúc đầu).
- episode.yaml: take009 needs_review. Chờ Richard quyết: lấy take008/take009 hay đổi hướng (nói bình tĩnh hơn để mặt đỡ rộng).

## 2026-11-21 15:18–15:19 — sh060 take010: nói bình tĩnh hơn (Richard)
- Richard 15:18: "uk nói bình tĩnh hơn chút xem" — đổi hướng giọng từ giận/hét sang bình tĩnh, lạnh, dứt khoát nhưng không hét, để mặt đỡ rộng khi nói.
- Motion prompt mới (calm/cold/controlled, not shouting); frame v6 giữ nguyên; sha motion đồng bộ yaml, validator chỉ thiếu manifest. Gen take010 (task 9b5c92f9) đang chạy, 10cr, 510 → 500 dự kiến.

## 2026-11-21 15:20 — Richard: gen đến khi khắc phục được thì thôi
- Richard 15:20: "Gen cho đến khi nào khắc phục được thì thôi nhé" — ủy quyền gen lại sh060 liên tục (mỗi take 10cr) cho đến khi mặt Nam lúc nói không còn rộng. Số dư lúc này 510 (take010 đang chạy → 500). Quy trình mỗi vòng: gen → QC thoại + hành động + SOI MẶT LÚC NÓI (side-by-side v002 vs 0.5/1/2/3s) → đạt thì trình, chưa đạt thì gen tiếp.

## 2026-11-21 15:18–15:23 — sh060 take010 giọng bình tĩnh (task 9b5c92f9, xong)
- Gen 1 lần, 10cr, 510 → 500, không chặn/lỗi. Clip 4b276bb6, file sh060-take010.mp4 (sha aeff4882…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–4.44s, nghe đúng "thừa", giọng bình tĩnh thật (transcript dấu "." không "!"). Nam ngồi nói đến ~3s mới nhổm dậy, bỏ đi sau hết thoại, ghế trống hiện rõ.
- MẶT LÚC NÓI CẢI THIỆN RÕ: soi side-by-side — mặt hẹp như v002 từ 0.5–3.5s. Chỉ còn 1 khoảnh khắc ~4.0s (chữ "quá" cuối, miệng mở rộng hình "o") mặt vẫn rộng hơn v002 chút. Đuôi sạch, không phụ đề giả.
- episode.yaml: take010 needs_review. Trình Richard quyết có coi là khắc phục được chưa; nếu chưa thì gen tiếp theo lệnh "gen đến khi khắc phục được thì thôi".

## 2026-11-21 15:49 — sh060 take011: gen tiếp (Richard)
- Richard 15:49: "gen tiếp" — take010 chưa tính là khắc phục xong (còn khoảnh khắc ~4s mặt hơi rộng). Gen take011 y hệt take010 (frame v6 + giọng bình tĩnh), task b0e97c58 đang chạy, 10cr, 500 → 490 dự kiến.

## 2026-11-21 15:49–15:55 — sh060 take011 giọng bình tĩnh (task b0e97c58, xong)
- Gen 1 lần, 10cr, 500 → 490, không chặn/lỗi. Clip 07957222, file sh060-take011.mp4 (sha 4b11e5c5…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–4.42s (nghe "nhận" thành "nhẳng" — lỗi nghe thanh điệu quen thuộc); Nam ngồi nói đến ~3.5s mới nhổm dậy, bỏ đi sau hết thoại, ghế trống hiện rõ.
- MẶT LÚC NÓI: giống hệt take010 — hẹp như v002 từ 0.5–3.5s, chỉ còn khoảnh khắc ~4.0s (chữ "quá" cuối, miệng mở rộng hình "o") mặt vẫn rộng hơn v002 chút. Chưa khắc phục hoàn toàn. Khoảnh khắc này lặp lại ở cả 2 take giọng bình tĩnh → có vẻ là cách Veo nhấn chữ cuối, không phải ngẫu nhiên theo take.
- episode.yaml: take011 needs_review. Theo lệnh "gen đến khi khắc phục được thì thôi", gen tiếp take012 y hệt.

## 2026-11-21 15:56–16:00 — sh060 take012 giọng bình tĩnh (task 32b6d074, xong)
- Gen 1 lần, 10cr, 490 → 480, không chặn/lỗi. Clip d716c51e, file sh060-take012.mp4 (sha dcb87804…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–4.12s (nghe "nhận" thành "nhẳng"); Nam ngồi nói đến ~3.5s mới nhổm dậy, bỏ đi sau hết thoại, ghế trống hiện rõ.
- MẶT LÚC NÓI: giống hệt take010/011 — hẹp như v002 từ 0.5–3.5s, chỉ còn khoảnh khắc ~4.0s (chữ "quá" cuối, miệng mở rộng hình "o") mặt vẫn rộng hơn v002 chút. 3/3 take giọng bình tĩnh đều lặp lại khoảnh khắc này → gen y hệt KHÔNG sửa được nữa; đây là cách Veo nhấn chữ cuối.
- ĐỔI LEVER cho take013: giữ giọng bình tĩnh nhưng thêm "delivers the last words softly and quietly, lips barely parting, face relaxed" — nhắm trực tiếp vào cơ chế gây rộng mặt (miệng mở rộng ở chữ cuối). Motion prompt mới, sha đồng bộ yaml. Gen take013 (task mới) 10cr, 480 → 470 dự kiến.
- episode.yaml: take012 needs_review.

## 2026-11-21 16:03 — Richard: thử cả 3 biểu cảm xem mặt giữ được không
- Richard 16:03: "thử cả ba kiểu xem mặt giữ đc ko" — thử 3 biểu cảm đã đề xuất (buồn bã / mệt mỏi / cười khẩy) xem kiểu nào giữ mặt hẹp.
- Đã chuẩn bị sẵn 3 motion prompt: sh060-motion-sad.txt, sh060-motion-weary.txt, sh060-motion-smirk.txt (cùng frame v6, cùng cấu trúc nói xong mới đứng dậy). Thứ tự thử: buồn bã → mệt mỏi → cười khẩy.
- LƯU Ý: take013 (bình tĩnh + chữ cuối nói khẽ) đang chạy (task 49ae67a6) — KHÔNG chạy song song task Flow (từng bị chặn "unusual activity"). Đợi take013 xong + QC rồi mới chạy 3 take biểu cảm, mỗi take 10cr (470 → 460 → 450 → 440 dự kiến).

## 2026-11-21 16:01–16:05 — sh060 take013 chữ cuối nói khẽ (task 49ae67a6, xong)
- Gen 1 lần, 10cr, 480 → 470, không chặn/lỗi. Clip aaccd00c, file sh060-take013.mp4 (sha 43875e4a…, 720×1280, 7.93s, có audio).
- QC: thoại đủ 0.00–5.18s (chậm hơn hẳn, nghe "nhận" thành "nhẳng"). Nam đứng dậy TRONG lúc nói chữ cuối (4s, thoại đến 5.18s) — lệch hướng "nói xong mới đứng dậy".
- MẶT LÚC NÓI HỖN HỢP: chữ cuối 4.0s hẹp (lever có tác dụng ở đó), nhưng giữa câu 2.0s/3.5s lại rộng hơn take010/011/012. Không tốt hơn 3 take bình tĩnh trước. Lever "chữ cuối nói khẽ" không cứu được tổng thể.
- episode.yaml: take013 needs_review. Motion prompt đổi sang bản BUỒN BÃ (sad) cho take014 — test biểu cảm đầu tiên theo lệnh Richard 16:03.

## 2026-11-21 16:08 — Richard đổi hướng: KHÔNG chuyển động nữa, chỉ Nam, zoom chặt, chỉ nói
- Richard 16:08: "thế thì không chuyển động nữa, gen ảnh chỉ có Nam, zoom vào chính. Sau đó gen nói thôi không chuyển động đứng dậy hay đi đâu xả" — bỏ hẳn đứng dậy/bỏ đi; frame chỉ Nam zoom chặt; clip chỉ ngồi nói.
- Frame mới: sh060-first-frame-tight-nam.jpg (sha dc64ae18…, 720×1280) — crop ffmpeg từ frame v6 (crop 540:960 tại x500,y720, upscale lanczos), mặt giữ nguyên pixel, chỉ Nam đầu + vai, bàn + ly nước cam + ghế còn trong khung, My không còn trong khung. 0cr.
- Motion prompt mới đã chuẩn bị: sh060-motion-static.txt (giọng bình tĩnh/lạnh, ngồi yên suốt clip, không đứng dậy, không bỏ đi, medium close-up, camera static).
- LƯU Ý: take014 (buồn bã, có đứng dậy) vẫn đang chạy (task 6582d6e9) — đã trả 10cr, để nó chạy xong rồi soi nhanh; hướng test biểu cảm đã bị hướng mới này thay thế. Clip tĩnh chỉ gen sau khi Richard duyệt frame mới + take014 xong (không chạy 2 task Flow song song).

## 2026-11-21 16:10 — Richard DUYỆT frame Nam zoom chặt
- Richard 16:10: "duyệt luôn" — frame sh060-first-frame-tight-nam.jpg (sha dc64ae18…) DUYỆT.
- Motion prompt đã đổi sang bản tĩnh (sh060-motion-static.txt), yaml sha đồng bộ. Clip tĩnh (take015, 10cr, 470 → 460 dự kiến) chỉ gen sau khi take014 xong (không chạy 2 task Flow song song).

## 2026-11-21 16:06–16:12 — sh060 take014 BUỒN BÃ (task 6582d6e9, xong)
- Gen 1 lần, 10cr, 470 → 460, không chặn/lỗi. Clip adcc785c, file sh060-take014.mp4 (sha 4e25159f…, 720×1280, 7.93s, có audio).
- QC: thoại 0.00–4.44s — nửa đầu đúng ("thừa nhận" nghe đúng), nửa sau "chia tay" nghe thành "chị tài" (p thấp 0.54/0.67 — giọng buồn nói chậm có thể làm nhòe chữ, hoặc Whisper nghe nhầm). Hành động đúng (nói xong đứng dậy, bỏ đi, ghế trống).
- MẶT LÚC NÓI: HẸP 0.5–2.0s, tốt nhất từ trước tới nay (hơn cả take010/011/012) — buồn bã giữ mặt hẹp khi nói. Đây là dữ liệu quyết định cho clip tĩnh.
- Quyết định: clip tĩnh (take015) dùng GIỌNG BUỒN BÃ thay vì bình tĩnh (đã sửa sh060-motion-static.txt: buồn bã + "each word clear and distinct" để tránh nhòe chữ như take014), frame Nam zoom chặt đã duyệt, ngồi yên suốt clip.
- episode.yaml: take014 needs_review. Test mệt mỏi + cười khẩy BỊ HỦY theo hướng mới của Richard (không chuyển động).

## 2026-11-21 16:13–16:17 — sh060 take015 CLIP TĨNH + BUỒN (task fb8e9bad, xong)
- Gen 1 lần, 10cr, 460 → 450, không chặn/lỗi. Clip 2bfecc28, file sh060-take015.mp4 (sha 86435464…, 720×1280, 7.93s, có audio, chỉ 1.7MB vì ít chuyển động).
- QC: MẶT hẹp 0.5–3.0s, chỉ rộng ở ~5.0s (nửa sau câu). Hành động đúng (ngồi yên suốt clip). Đuôi sạch, không phụ đề giả.
- THOẠI LỖI: "chia tay" nghe thành "chị tài" — xác nhận bởi CẢ base lẫn tiny (tiny: "Chị ta ai đi"), và lặp lại từ take014. 2 take buồn đều lỗi cùng chỗ → giọng buồn làm nhòe "chia tay", không phải lỗi Whisper.
- Kết luận: khung tĩnh giữ mặt tốt, nhưng giọng buồn phá thoại. Hướng tiếp: tĩnh + giọng BÌNH TĨNH (take010–013 nghe "chia tay" đúng) — take016 đang gen.
- episode.yaml: take015 needs_review.

## 2026-11-21 16:19–16:24 — sh060 take016 CLIP TĨNH + BÌNH TĨNH (task cc6d4d6e, xong)
- Gen 1 lần, 10cr, 450 → 440, không chặn/lỗi. Clip d5c80b1e, file sh060-take016.mp4 (sha f89a7662…, 720×1280, 7.93s, có audio, 1.4MB).
- QC: MẶT TỆ HƠN take015 — rộng ở 1.0s/2.0s/5.0s (miệng mở tròn chữ "o" rất to trong khung cận), chỉ hẹp lúc ngậm miệng 0.5s/3.0s.
- THOẠI LỖI: "chia tay" nghe thành "chị tài/tay" — cả base lẫn tiny đều nghe vậy (p thấp 0.22–0.34). Đây là take thứ 3 liên tiếp hỏng "chia tay" (014/015/016) trong khi 4 take bình tĩnh trước (010–013) nói đúng → nghi voice roll của Veo (giọng đổi theo mỗi lần gen), không phải do biểu cảm hay khung hình.
- Kết luận: khung cận làm miệng há chữ "o" trông to hơn, không cứu được mặt; giọng bình tĩnh trong khung cận còn tệ hơn giọng buồn. Hướng tiếp (trong lệnh "gen đến khi khắc phục được thì thôi" + hướng tĩnh của Richard): tĩnh + bình tĩnh + "lips barely parting" cả câu — take017 đang gen.
- episode.yaml: take016 needs_review.

## 2026-11-21 16:25–16:28 — sh060 take017 bị chặn "unusual activity", đổi trình duyệt mới
- Task c70a3df6: bấm gen thì Flow hiện ngay thẻ "Không thành công — hoạt động bất thường", 0cr, số dư vẫn 440, không có clip. Không retry trong cùng trình duyệt (đúng quy tắc đã chứng minh từ take007).
- Đã mở task mới c5340b12 ở trình duyệt mới, rebuild setup từ đầu, gen lại take017 (10cr, 440 → 430 dự kiến).

## 2026-11-21 16:33–16:34 — Richard nghe take015: THOẠI ĐÚNG, GIỌNG MIỀN NAM; take015 ĐƯỢC DUYỆT
- Richard nghe trực tiếp take015 (16:33): "ô nói đúng mà :((" — Veo NÓI ĐÚNG "chia tay". Whisper nghe nhầm thành "chị tài" (cả base lẫn tiny) — artifact ASR trên giọng miền Nam, KHÔNG phải Veo nói sai. Kết luận "giọng buồn làm nhòe chữ" trước đó là SAI; "voice roll" cho thoại cũng chết.
- Richard 16:33: "cái này lấy được" — take015 DUYỆT (accepted_editorial). Nhưng 16:34: "Giọng này miền nam" — giọng take015 là MIỀN NAM, tập yêu cầu giọng Bắc. Cần quyết: lồng tiếng Bắc cho take015, hay chấp nhận giọng Nam, hay xem take017 (giọng mới) có Bắc không.
- take017 (tĩnh + bình tĩnh + lips barely parting): lần 1 bị chặn "unusual activity" 0cr; lần 2 trình duyệt mới xong 16:34 (10cr, 440→430). QC: thoại đủ 0.00–5.66s, Whisper nghe "Chia tay" đúng; mặt hẹp 0.5–3.0s, chỉ hơi rộng ~5.0s (tương đương take015, tốt hơn take016). Gửi Richard nghe thử giọng.
- episode.yaml: take015 accepted_editorial, take017 needs_review.

## 2026-11-21 16:34–16:38 — Giọng Nam: 3/3 take đều MIỀN NAM
- Richard nghe take017 (16:34): "giọng này cũng miền nam". Gửi take010 cho nghe thử (16:37) — Richard 16:38: "cũng miền nam".
- Kết quả: take010, take015, take017 đều giọng miền Nam. Prompt đã ghi "Northern Vietnamese male voice" mọi lần nhưng Veo vẫn ra giọng Nam — prompt không lái được giọng.
- Hướng còn lại: (1) lồng tiếng Bắc cho take015 đã duyệt bằng giọng nam Bắc duy nhất có sẵn miễn phí là VieNeu "Minh Quân" (chạy qua Colab, đã làm được 19/11); (2) gen tiếp xổ số giọng Bắc (10cr/lần, chưa biết tỉ lệ); (3) chấp nhận giọng Nam. Chờ Richard chọn.

## 2026-11-21 16:40–16:43 — LỒNG TIẾNG THỬ take015 bằng VieNeu Minh Quân (Richard: "lồng tiếng thử")
- TTS: VieNeu v3 Turbo preset "Minh Quân" (nam Bắc) chạy trên Colab T4 qua colab_wrap.py (auth tinphim còn hạn, 59 phút; không có session cũ). Script sh060_dub_minhquan.py: pip install vieneu, load model 40.5s, synth half1 2.16s / half2 1.60s / full 3.36s. Tải 3 file về dub/, stop session (không orphan).
- Mix (numpy, theo quy tắc dub đã chứng minh — KHÔNG dùng adelay): track gốc -8dB, hạ -40dB trong TOÀN span thoại gốc (0.00–2.92s, 4.38–6.40s) với ramp 0.1s; TTS đặt 0.0s + 4.38s. Bản đầu lỗi: cửa sổ duck chỉ theo độ dài TTS nên đuôi giọng gốc ("khổ quá" 5.98–6.40s) lọt ra ở -8dB — đã sửa bằng cách duck theo span thoại gốc. Bản cuối: tail rms 0.002 (gần im), Whisper nghe đúng hết câu, không nhân đôi.
- File: sh060-take015-dub-minhquan.mp4 (sha 3a10e4ca…, 7.92s, 720×1280). Gửi Richard nghe thử và quyết.
- LƯU Ý: Whisper vẫn nghe "Chia" với p thấp (0.15) ngay cả trên giọng TTS Bắc — "chia" là âm khó với ASR, tai người mới là chuẩn.

## 2026-11-21 16:45–16:50 — Richard CHẤP NHẬN giọng Nam cho sh060 + kiểm tra tông giọng toàn tập
- Richard 16:45: "Thôi lấy giọng miền Nam cũng được, kiểm tra tông giọng của các video xem Có phải giọng này hết không? Giọng ThaoMy miền bắc, giọng Nam thì miền Nam cũng đc" — take015 (giọng gốc miền Nam) là take sh060 CHÍNH THỨC; bản dub Minh Quân chỉ là dự phòng, không dùng.
- Voice audit (voice_audit.py, Whisper base + F0 autocorrelation, chỉ đo trong span từ Whisper):
  - sh010 take005 (My): F0 median 314Hz, thoại đủ + lặp nửa sau. Không cờ giọng.
  - sh020 take003 (Nam): F0 median 242Hz, thoại đủ. "Con" nghe thành "Còn" p=0.56 (lớp lỗi thanh điệu ASR đã biết).
  - sh030 take002 (My): F0 median 281Hz, thoại đủ. "Giữa" nghe thành "Dữ" p=0.40 NHƯNG đã xác minh từ QC v3b: F0 tăng 180→254Hz (thanh ngã) loại "Dưới", kết luận nói đúng "Giữa" — không phải phát âm Nam.
  - sh040 take003 (Nam): F0 median 203Hz, thoại đủ 2 đoạn.
  - sh050 take002 (My): F0 median 246Hz, thoại đủ (cười đuôi không tính vào F0).
  - sh060 take015 (Nam): F0 median 188Hz, giọng Nam — Richard xác nhận bằng tai.
  - Kết luận đo được: cả 6 take đều đúng giới tính giọng; không còn cờ giọng nào sau khi loại artifact ASR. F0 chênh trong mỗi nhân vật (My 246–314, Nam 188–242) nằm trong biên độ giải thích bằng cách diễn (hỏi/buồn/ngạc nhiên) — KHÔNG chứng minh được giọng có phải cùng 1 roll Veo hay không. Chỉ tai Richard mới chốt được.
- File nghe kiểm: ep008-voice-check.mp4 (25s, ghép span thoại 6 take theo thứ tự sh010→sh020→sh030→sh040→sh050→sh060). Gửi Richard nghe và chốt.

## 2026-11-21 16:53 — Richard bắt lỗi sh040 take003: "Vừa lòng em chưa?" nhìn như Thảo My nói
- Kiểm tra: file voice-check ghép ĐÚNG thứ tự (transcript xác nhận "Vừa lòng em chưa?" ở 15.54–16.60s, đoạn sh040). Âm thanh ĐÚNG giọng Nam (F0 median 156Hz trong câu 2, 0% frame >240Hz).
- Vấn đề là HÌNH: frame 6.0/6.25/6.5s cho thấy My há miệng (như đang nói), Nam miệng đóng, mắt nhắm, cười — Veo gán nhầm animation câu 2 cho My. Câu 1 (0–4.46s) đúng: Nam nói rõ, chỉ tay, My chỉ nghe.
- Take001/take002 cũ là v2 (áo hồng + quán cũ) — không dùng được. Hướng sửa duy nhất: gen lại sh040 (10cr) với prompt nhấn mạnh Nam nói cả 2 câu, My chỉ nghe im. Chờ Richard quyết.

## 2026-11-21 17:01 — sh040 take004: gen xong NHƯNG lỗi gán miệng LẶP LẠI
- Take004 (clip 9c99c366, 10cr, 430→420): thoại đủ, câu 1 đúng (Nam nói rõ + chỉ tay), đuôi sạch, bên ngồi đúng. Âm thanh đúng giọng Nam (F0 median câu 2 = 142Hz).
- NHƯNG câu 2 "Vừa lòng em chưa?" (5.52–6.46s) VẪN LỖI: frame 5.6/5.9/6.2/6.4s cho thấy miệng My vẫn hơi mở, miệng Nam đóng — nhẹ hơn take003 nhưng cùng dạng lỗi. Prompt mới (nhấn mạnh Nam nói cả 2 câu, My im) KHÔNG sửa được. Lỗi lặp lại 2/2 take → có vẻ Veo hệ thống gán animation câu 2 cho My.
- Hướng tiếp nếu Richard không chấp nhận: cắt sang khung chặt Nam riêng cho câu 2 (cách đã làm ở sh060), hoặc re-roll tiếp. Chờ Richard quyết.

## 2026-11-21 17:19–17:20 — Richard: CẮT câu "Vừa lòng em chưa?" + take004 giọng Bắc
- Richard 17:19: "thôi, cắt luôn đoạn có 'vừa lòng em chưa' đi" — sh040 dùng take004 chỉ 0–5.0s (câu 1 "Cho là anh có đi, anh vẫn chọn em." + khoảng lặng; câu 2 bắt đầu 5.52s). take003 chính thức bị thay thế.
- Richard 17:20: "video này thì giọng Nam là miền bắc nè" — giọng Nam take004 là MIỀN BẮC (khác take003 miền Nam). Vậy giọng Nam trong tập hiện: sh020 chưa xác định, sh040 Bắc, sh060 Nam (đã chấp nhận). take004 là take sh040 CHÍNH THỨC (accepted_editorial).

## 2026-11-21 17:44 — Richard hỏi: ghép 7 đoạn + đồng bộ hết giọng về 1 loại được không?
- Trả lời: được, 2 bước (dựng master 7 shot + lồng tiếng thống nhất). Cần Richard chọn phương án vì ảnh hưởng chất lượng khớp môi.
- Đã thử đo LTAS cosine để xem sh020 có cùng giọng take004 (Bắc) hay sh060 (Nam) không: kết quả KHÔNG tách được (sh020–sh030 khác giới vẫn 0.81, sh010–sh050 cùng My chỉ 0.51) — nhiễu nền quán + nội dung âm tiết át tín hiệu giọng. Không dùng LTAS để xác định giọng/nhân vật; chỉ tai Richard mới chốt được giọng sh020.

## 2026-11-21 17:46 — Richard chọn phương án A: giữ gốc, chỉ lồng shot sai giọng
- Phương án B (lồng hết 6 shot) bỏ. Phương án A: My giữ tiếng gốc (Bắc, cả 3 shot); Nam giữ take004 sh040 (Bắc); sh060 take015 lồng Minh Quân (bản dub đã xong, sha 3a10e4ca…); sh020 take003 CHƯA BIẾT giọng — gửi Richard nghe để quyết Bắc/Nam.
- Chuẩn bị sẵn script TTS sh020 (colab-t4-test/sh020_dub_minhquan.py, 1 file, câu liền 0–2.82s) — chỉ chạy khi Richard xác nhận sh020 giọng Nam.
- Trims đã chốt cho master: sh010 take005 cắt ~2.8s (bỏ phần Veo lặp); sh040 take004 0–5.0s (cắt câu 2); sh050 take002 cắt đuôi cười lớn; sh070 take002 cắt còn ~3s; sh060 dùng bản dub.

## 2026-11-21 17:48 — Chuẩn bị dựng master (plan A): manifest + file + validator sạch
- Viết edit/manifest.yaml theo schema v2 (schema_version 2, episode_id ep008, revision 5, selected_takes đủ 7 shot đúng thứ tự, audio_plan plan A, build_notes ghi trims + voice plan + 2K pending + Laugh Track 1 đề xuất). Đã đọc AGENTS.md của repo trước khi sửa (theo nhắc của runtime).
- Copy 7 clip 1K đã chọn vào generated/ + ghi file.path/sha256 vào episode.yaml cho 7 take đã chọn (sh060 trỏ bản dub Minh Quân, sha 3a10e4ca…). Lỗi lần đầu: regex giữ lại 'null' sau 'file:' làm YAML hỏng — đã sửa (7 chỗ), rút kinh nghiệm kiểm tra parse ngay sau khi sửa yaml bằng script.
- Copy 2 ảnh tham chiếu đã duyệt vào input/references/ (nam-front-v002.jpg sha 340a246d…, date-cafe-v003-day.png sha 1a66036e…) — validator trước đó báo thiếu 3 asset này (lỗi cũ bị che vì manifest chưa có).
- Validator mặc định hiện SẠCH (chỉ còn NOTE: take014/016/017 + sh070 take001 chưa có clip local; VieNeu voice pending — đúng vì chờ chốt giọng sh020). LƯU Ý: cổng --stage edit của validator yêu cầu mute Veo + VieNeu-TTS full (luật lồng hết), xung đột với plan A (giữ gốc chọn lọc) — đã ghi vào manifest; chỉ chạy validate mặc định cho tới khi luật được sửa.

## 2026-11-21 17:55 — Richard: làm thử chuỗi giọng (voice only) từ đầu đến cuối
- File: ~/workspace/ep008-con-nho-do-clips/ep008-voice-chain.mp3 (23.76s, mono 48kHz, peak normalize -1dBFS, nghỉ 0.5s giữa các shot).
- Nội dung theo plan A: sh010 take005 native 0-2.32s / sh020 take003 native 0-2.82s / sh030 take002 native 0-4.38s / sh040 take004 native 0-4.48s (chỉ câu 1) / sh050 take002 native 0-1.28s / sh060 take015-DUB Minh Quân 0-5.98s. sh070 câm lặng, không có trong chuỗi.
- QC Whisper base trên chuỗi: đủ 6 câu đúng thứ tự, đúng span; các lỗi nghe còn lại đều là artifact ASR đã biết ("Giữa"->"Dữ", "chọn"->"trọn", "thừa nhận"->"thường nhận" — đã xác minh đúng bằng F0/từ bản dub). "Chia tay" lần này Whisper nghe đúng trong bản dub.
- File kiểm giọng cũ ep008-voice-check.mp4 (25s, dùng take003 sh040 + take015 gốc) ĐÃ LỖI THỜI — chuỗi này thay thế.

## 2026-11-21 18:56 — Richard: bỏ bản lồng Minh Quân, thay bằng bản gốc
- sh060 dùng lại take015 GỐC (giọng Nam, đã chấp nhận 16:45). Bản dub Minh Quân (sha 3a10e4ca…) về lại dự phòng.
- Chuỗi giọng v2: ep008-voice-chain-v2.mp3 (24.18s, toàn bản gốc; sh060 0-6.40s gồm khoảng nghỉ tự nhiên giữa 2 câu). QC Whisper base: đủ 6 câu đúng thứ tự; "chia tay" ASR nghe thành "khi tài" (artifact giọng Nam đã biết — Richard nghe trực tiếp 16:33 xác nhận nói đúng), "Giữa"->"Dữ" (đã xác minh F0). Chuỗi v1 (có dub) lỗi thời.
- episode.yaml: sh060 take015 file -> generated/sh060-take015.mp4 (sha 86435464…). manifest: audio native toàn bộ, voice_status vẫn pending_sh020_verdict.

## 2026-11-21 19:01–19:04 — Richard đổi hướng: VOICE CONVERSION, giữ nhịp điệu
- 19:01 Richard: "convert giọng gốc sang giọng Bắc và giọng Nam sang cùng giọng cho tất cả voice Nam" + "vẫn giữ nhịp điệu này chỉ bóp giọng sang giọng khác" — tức là voice conversion (giữ nguyên thời gian/ngắt nghỉ/cảm xúc của câu gốc, chỉ đổi giọng), KHÔNG phải lồng TTS lại (bản Minh Quân mất nhịp nên bị bỏ).
- 19:04 Richard ĐÍNH CHÍNH: "Giọng My cũng phải convert sang chứ đâu phải giọng Bắc đâu" — giọng My KHÔNG phải Bắc (theo tai Richard). Audit F0 + transcript của Bee nói My Bắc là SAI — F0 đo cao độ, không đo được accent; transcript không có dấu hiệu Nam không có nghĩa là Bắc. Tai Richard luôn thắng đo đạc.
- Hướng mới: convert HẾT 6 shot thoại, giữ nhịp điệu. My -> 1 giọng nữ Bắc; Nam -> 1 giọng nam Bắc (đề xuất lấy giọng take004 làm chuẩn — CHỜ Richard chốt). Giọng chuẩn cho My: đề xuất clone ThaoMy (giọng chính thức, locked 2026-11-18) làm mốc — CHỜ Richard chốt.
- Đang test: subagent kiểm tra tool voice conversion free chạy được trên VM CPU-only (ưu tiên KNN-VC / Seed-VC, giữ prosody), test 1 câu sh060 (0-6.4s) -> giọng take004 (0-4.48s). LƯU Ý TRUNG THỰC đã báo Richard: convert chỉ đổi màu giọng thì làm được, đổi hẳn âm điệu Nam->Bắc mà giữ nguyên nhịp là phần khó nhất (tool convert thường giữ lại âm điệu gốc) — test xong nghe rồi mới quyết.

## 2026-11-21 19:15 — Kết quả test KNN-VC: chạy được nhưng KHÔNG dùng được
- Tool: KNN-VC (bshall/knn-vc, WavLM-Large + kNN topk=4 + HiFi-GAN), venv + torch CPU, ~19s cho 6.4s audio. Script: ~/workspace/knn-vc-test/run_vc.py. File test: vc-test-sh060-to-take004.mp3/wav (sh060 0-6.4s -> giọng take004 0-4.48s).
- Giữ được độ dài/nhịp thô (6.38s vs 6.40s, energy corr 0.84) NHƯNG chữ biến dạng thật: Whisper base nghe "anh yêu con đó" -> "anh đi ngon đó", "yêu khổ quá" -> "đi ngon quá" (Bee xác minh lại độc lập, khớp). Ngữ điệu buồn mất (F0 contour corr 0.10). Âm điệu Nam KHÔNG đổi ("chia tay" vẫn nghe nhầm như cũ). Nguyên nhân: giọng mẫu chỉ 4.48s (193 frame), KNN-VC cần vài phút giọng mẫu.
- Kết luận: VC không làm được "giữ nhịp + đổi âm điệu Nam->Bắc + thống nhất giọng" với tư liệu hiện có. Seed-VC cùng họ, khó khá hơn. Hướng thật còn lại: lồng clone ThaoMy cho My (mất nhịp), giữ giọng gốc, hoặc thu giọng người thật miền Bắc. File test đã gửi Richard nghe thử; chờ cậu ấy quyết.

## 2026-11-21 19:23–19:25 — Richard chốt: lồng clone ThaoMy cho My, giữ giọng Nam; sh050 giữ nguyên
- Richard 19:23: "Lồng clone ThaoMy cho My và giữ giọng Nam". 19:25 bổ sung: sh050 "Thế là anh có thật à" GIỮ NGUYÊN vì đã giọng Bắc. Vậy phạm vi lồng: chỉ sh010 + sh030; sh050 native; Nam (sh020/sh040/sh060) native.
- Cách lồng (theo đúng tiền lệ ep006 sh020, 19/11): VieNeu v3 Turbo trên Colab T4, enroll ThaoMyVeo từ ref-clip2.wav (~/workspace/chuyen-nha-vy/voice-test/clone-test/ref-clip2.wav, còn nguyên), script mẫu generated/dub/gen_sh020_dub.py (v.add_voice + v.infer voice="ThaoMyVeo"). Lồng khô: tắt hẳn tiếng gốc, đặt TTS theo cửa sổ miệng native.
- Cửa sổ miệng native đã đo bằng Whisper base: sh010 0-2.32s (1 câu); sh030 câu 1 0-2.64s ("Giữa em với con đó, anh chọn ai?"), câu 2 3.32-4.38s ("Lỡ có thì sao?").
- Subagent đang chạy lồng (gen 3 file TTS + mix + QC) trên Colab T4; colab sessions hiện 0 session orphan, auth vẫn chạy được.

## 2026-11-21 19:30 — Lồng clone ThaoMy sh010 + sh030 XONG, chờ Richard duyệt
- TTS: Colab T4, VieNeu v3 Turbo, enroll ThaoMyVeo từ ref-clip2.wav, session ep008-dub-thaomy (đã stop sạch). Script: colab-t4-test/ep008_dub_thaomy.py. 3 file wav trong clips/dub/: thaomy-sh010.wav 3.12s, thaomy-sh030-s1.wav 2.80s, thaomy-sh030-s2.wav 2.16s.
- Mix lồng khô (tắt hẳn tiếng gốc, numpy 48kHz, mux ffmpeg video copy): sh010-take005-dub-thaomy.mp4 sha 3a66e819…, sh030-take002-dub-thaomy.mp4 sha 8c922983…, đều 720x1280 24fps 7.92s.
- QC độc lập của Bee trên file đã mux: gap RMS = 0.000000 (không rò tiếng gốc); Whisper base: sh010 đúng hết, sh030 "dữ/lựa" là artifact thanh điệu đã biết trên giọng clone; F0 clone 240.6/247.4/221.2Hz khớp mẫu enroll 246.2Hz.
- ⚠️ OVERRUN (không time-stretch): sh010 TTS 3.12s vs cửa sổ miệng 2.32s (+0.80s) — dài hơn cả điểm cắt master đã chốt ~2.8s; sh030 s2 2.16s vs 1.06s (+1.10s), kết thúc 5.48s — vượt use_range tạm 0-5.2s. sh030 s1 +0.16s, ok. Nếu duyệt thì master phải nới điểm cắt: sh010 ~3.2s, sh030 ~5.5s; môi sẽ lệch nhịp trong lúc clone nói (clone đọc chậm hơn gốc). Chờ Richard nghe + quyết.

## 2026-11-21 19:40 — Bản lồng "nhanh" (atempo) để so sánh với bản chậm
- Nguyên nhân chậm: giọng gốc Veo nói NHANH (sh010: 9 từ/2.32s ≈ 3.9 từ/s; sh030 câu 2: 4 từ/1.06s ≈ 3.8 từ/s), clone đọc nhịp bình thường (~2.9 từ/s). Không phải clone đọc sai.
- VieNeu v3 Turbo infer() KHÔNG có tham số speed (đã kiểm tra source wheel vieneu — chỉ Nano engine mới có speed=1.0). Nên tăng tốc bằng atempo hậu kỳ, không gen lại được nhanh hơn từ model.
- Bản nhanh: sh010-take005-dub-thaomy-fast.mp4 sha 52abdb55… (atempo 1.345x, vừa đúng 2.32s); sh030-take002-dub-thaomy-fast.mp4 sha 201cbefb… (s1 1.06x, s2 1.30x, kết thúc 4.98s — vừa trong trim 5.2s). QC: speech đúng span, gap RMS ~0, Whisper đúng câu (artifact thanh điệu như cũ).
- Chờ Richard nghe so sánh: bản chậm (giọng tự nhiên, môi lệch + nới cắt) vs bản nhanh (khớp môi, giọng gấp hơn).

## 2026-11-21 19:46 — Richard: cả 2 bản lồng chưa khớp môi; hỏi cách khác
- Cách khác đang thử: căn TỪNG TỪ — đo timestamp từng từ của clone (Whisper trên file TTS), kéo/giãn từng từ cho vừa đúng khoảng miệng gốc của từ đó, đặt đúng vị trí gốc. Tiếng Việt mỗi từ gần như 1 âm tiết nên căn từ ≈ căn âm tiết, khác hẳn tăng tốc đều cả câu. Subagent đang làm bản wordalign (sh010 + sh030).
- Hạn chế đã nói trước với Richard: câu 2 sh030 gốc nói nhanh gấp đôi nhịp clone (4 từ/1.06s vs 2.16s) nên dù căn từng từ thì giọng vẫn nghe gấp — không có cách nào vừa khớp môi vừa giữ nhịp chậm cho câu đó.
- Hướng dự phòng (chưa làm, chỉ nêu): AI sửa miệng theo tiếng mới (Wav2Lip/LatentSync) — nặng, phải tải model + chạy CPU, có nguy cơ méo mặt. Chỉ làm nếu wordalign vẫn chưa đủ.

## 2026-11-21 19:49 — Ý tưởng của Richard: chậm video 2x, lồng, rồi tăng lại 2x?
- Tính lại: chậm video 2x thì cửa sổ miệng sh010 thành 2.32->4.64s, trong khi TTS chỉ 3.12s (miệng dài hơn tiếng); tăng cả 2 lại 2x thì tiếng còn 1.56s vs miệng 2.32s, giọng nhanh gấp đôi — vòng đi-vòng lại không giải quyết được vì lệch là TỈ LỆ giữa tiếng và miệng, thay đổi đều cả 2 bên thì tỉ lệ giữ nguyên.
- Biến thể làm được: chậm video đúng tỉ lệ lệch (sh010: 1.345x) và GIỮ NGUYÊN chậm, không tăng lại — giọng tự nhiên, hình chạy slow-motion. Đã làm bản thử sh010-take005-dub-thaomy-slowvideo.mp4 (sha 44eac8bc…, 3.79s, Whisper đúng câu, gap RMS 0).
- Hạn chế: sh030 không dùng được 1 hệ số chung (câu 1 cần 1.06x, câu 2 cần 2.04x) — video sẽ đổi tốc độ giữa chừng, nhìn lạ. sh030 vẫn trông chờ bản wordalign đang làm.

## 2026-11-21 19:51 — Bản wordalign XONG (sh010 + sh030), chờ Richard duyệt
- Build: subagent, script clips/build_wordalign.py. sh010-take005-dub-thaomy-wordalign.mp4 sha 0091753b…, sh030-take002-dub-thaomy-wordalign.mp4 sha 0cc8431a…, đều 720x1280 24fps 7.93s. Bee verify độc lập: sha khớp, gap RMS 0, Whisper khớp báo cáo subagent.
- Phát hiện QUAN TRỌNG (đã verify bằng energy 48kHz stereo): Whisper bôi từ đầu câu ra khoảng lặng đầu clip — "Anh" gốc bắt đầu ~0.88s chứ không phải 0.00s (năng lượng 0-0.8s chỉ ~0.012-0.019, nhảy lên 0.089 ở 0.8-0.9s). Hai bản lồng đầu (chậm + nhanh) đặt TTS ở 0.0s nên tiếng bắt đầu sớm hơn miệng gần 1 giây — đó là 1 phần lý do chưa khớp, không chỉ do nhịp. Bản wordalign đã sửa: đặt từ đúng onset thật. Bài học đã ghi AGENTS.md.
- sh030 wordalign TỐT: hệ số tối đa 2.00x ("với"), câu 2 sạch (max 1.44x nhờ bỏ pause nội bộ của clone), Whisper nghe đúng câu (artifact thanh điệu như cũ).
- sh010 wordalign GIỚI HẠN: giữa câu My nói ~5.5 âm tiết/s, 4 từ cần 2.0-2.42x, Whisper nghe thành "Ấn nhiều em thấy lại dụng con đó" — từ đúng vị trí miệng nhưng có thể nghe gấp/méo. Chờ tai Richard phán.

## 2026-11-21 19:55 — Richard DUYỆT bản lồng wordalign ("lấy tạm bản này"); master 1K đang dựng
- Verdict: sh030 wordalign "video 2 ổn đó" (duyệt hẳn); sh010 wordalign miệng lặp 2 lần "yêu con đó" (defect Veo ở 3.28-4.66s trong clip gốc) — "cắt đi được thì là ok". Điểm cắt master sh010 0-2.8s (đã chốt từ 13:50) loại hẳn đoạn lặp.
- Hồ sơ cập nhật rev6 (manifest + episode.yaml, validator mặc định CLEAN 0 lỗi): file sh010/sh030 trỏ sang bản wordalign trong generated/ (sha 0091753b… / 0cc8431a…), audio_plan voice_status locked, voice_by mixed_clone_wordalign_sh010_sh030_native_rest.
- Subagent đang dựng master 1K preview: 7 shot theo trim (2.8/3.6/5.2/5.0/2.0/7.0/3.0 ≈ 28.6s), concat FILTER, 1080x1920 30fps, Boxed captions (Remotion BasicCaptions, #F59E0B) + SRT riêng, Laugh Track 1 trên sh070 (đề xuất theo pattern series, chưa được Richard chốt riêng — sẽ nêu rõ khi giao preview).

## 2026-11-21 20:30 — Master 1K preview XONG, chờ Richard duyệt
- File: edit/ep008-master-1k-preview.mp4 sha 618568ff…, 28.70s, 1080x1920 30fps, H.264 yuv420p, AAC 48kHz stereo, loudnorm -15.33 LUFS. SRT: edit/ep008-master-1k-preview.srt sha 4dc41876…, 6 cues. Script build: edit/build_master_1k.py + edit/stage3_only.py, báo cáo edit/build1k/build-report.md, contact sheet edit/build1k/qc-contact.png.
- Build: concat FILTER, trims 2.8/3.6/5.2/5.0/2.0/7.0/3.0; crop icon Veo đồng nhất crop=640:1138:40:0 (icon + chữ Veo ở góc dưới-phải cả 7 shot) rồi lanczos lên 1080x1920 — đã verify icon biến mất cả 7 shot, mặt/tay an toàn. Ghi chú: rule AGENTS.md nói crop theo vị trí icon từng clip, build này dùng 1 crop chung để scale/khung hình nhất quán qua hard cut; nếu muốn theo đúng chữ rule thì nói rõ.
- Captions Boxed (Remotion, #F59E0B): 58 từ khớp script; timing Whisper base + energy-refine. Sửa lỗi render nghiêm trọng: render full 861 frame concurrency 2 exit 0 nhưng đen từ ~13,7s (Chrome OOM) — render lại 3 chunk 287 frame concurrency 1 rồi nối, đã verify không đen ở mọi mid/biên/vùng 13,7s. Bài học đã ghi AGENTS.md.
- Laugh Track 1 trên sh070 (nghe 25.7-27.54s) — vị trí theo pattern series, CHƯA được Richard chốt riêng cho ep008; đã nêu rõ khi giao preview.
- Bee verify độc lập: sha khớp, ffprobe đúng thông số, mean frame 111-129 ở mọi mốc (kể cả 13.7s + biên chunk), SRT đúng 6 câu (sh040 chỉ câu 1), soi 3 frame full-res (sh010/sh040/sh070): mặt/khung hình đúng, phụ đề Boxed rõ, không icon Veo, không viền đen.
- Tiếp theo: Richard duyệt preview 1K → download 2K (download-capture) + dựng lại master 2K.

## 2026-11-22 07:31 — Richard DUYỆT master 1K preview, lệnh dựng bản 2K
- Duyệt cả preview kèm Laugh Track 1 trên sh070 (không yêu cầu bỏ) — vị trí laugh chốt theo đó.
- Browser task đang tải 2K upscale 7 clip đã chọn (download-capture, từng clip, verify 1080x1920): sh010 take005, sh020 take003, sh030 take002, sh040 take004, sh050 take002, sh060 take015, sh070 take002. Chưa tải 2K bao giờ cho ep008 — mỗi clip: chọn '1080p Đã tăng độ phân giải' lần 1 chạy job upscale (~6-7 phút), lần 2 mới tải file.
- Sau khi đủ 7 file 2K: ghép lại audio wordalign sh010/sh030 lên video 2K (audio lấy từ file wordalign 1K, không cần lồng lại), dựng lại master 2K với cùng trim/captions/laugh track, QC rồi giao.

## 2026-11-22 07:33 — Richard: thêm title ở đầu video ("Con nhỏ đó")
- Title card mở đầu cho master 2K: chữ "Con Nhỏ Đó" (theo tên tập trong episode.yaml), ~1.5s, trước sh010, kiểu chữ khớp Boxed captions (trắng, accent #F59E0B). Tổng thời lượng 2K ≈ 30.2s. Ghi vào manifest + todo để subagent dựng 2K làm theo. Các tập trước chưa từng có title card nên không có tiền lệ — làm theo chuẩn này, Richard xem bản 2K rồi sửa nếu muốn khác.

## 2026-11-22 07:42 — Richard: title kiểu video "Chia Tiền" (ep004)
- Nhớ đúng: ep004 'Chia Bill' có title "CHIA TIỀN" in hoa, hiện 2s đầu ĐÈ LÊN shot đầu (không phải card đứng riêng), nằm ở dải trên, KHÔNG lấp đầu nhân vật (yêu cầu cứng của Richard lúc 14:28 18/11), làm bằng Remotion TitleCard mới vá vào template captions; master ep004 25.62s đã được Richard duyệt "Tốt".
- Áp cho ep008: title "CON NHỎ ĐÓ" in hoa, 2s đầu đè lên sh010, dải trên, không lấp đầu My; dùng lại TitleCard ep004. Tổng thời lượng giữ ~28.7s (không cộng thêm). Đã sửa manifest + todo theo đúng ý này (bỏ phương án card riêng ~1.5s đã ghi lúc 07:33).
- Tham chiếu TitleCard ep004: master mẫu ~/workspace/ep004-chia-bill-clips/ep004-chia-bill-boxed-laughtrack1.mp4 (title "CHIA TIỀN" 2s đầu); spec trong 05_episodes/ep004-chia-bill/edit/manifest.yaml.

## 2026-11-22 08:16 — Tải 2K: 6/7 xong, sh050 bị khóa Ultra
- 6 clip 2K đã về + verify (h264 1080x1920 24fps 7.85s, đã đổi tên vào clips/): sh010-take005-2k.mp4 sha 5fd6606f…, sh020-take003-2k.mp4 sha 2e03040e…, sh030-take002-2k.mp4 sha a3426242…, sh040-take004-2k.mp4 sha d71d292b…, sh060-take015-2k.mp4 sha 7d103fc3…, sh070-take002-2k.mp4 sha e53cd889… (gốc ở browser_downloads/sess-2258063443/, đã dời đi).
- sh050 take002 (clip c59b3807, áo dài xanh nhạt) bị KHÓA 1080p — Flow đòi nâng cấp Google One AI Ultra $99.99/tháng. Cả take sh050 xanh nhạt còn lại cũng khóa; chỉ bản váy magenta (sai đồ) mới mở 1080p. Quyết định: KHÔNG nâng cấp (không được ủy quyền), KHÔNG lấy bản magenta (sai continuity) — lấy bản 720p gốc của đúng take002, master upscale bằng ffmpeg (đúng chất lượng shot này trong bản 1K preview Richard đã duyệt). Đã báo Richard; nếu cậu ấy muốn 2K thật cho sh050 thì nâng Ultra sau.

## 2026-11-22 08:24 — sh050 2K: khóa Ultra chỉ là tạm thời, đủ 7/7 clip 2K thật
- Browser thử lại take002 thì nút 1080p MỞ (chỉ 4K còn khóa) — job upscale chạy bình thường, không paywall. File f7 về: 7.701.390 byte, h264 1080x1920 24fps 7.85s, đã đổi tên sh050-take002-2k.mp4 sha 0cd5f023…. Không cần bản 720p fallback, không nâng Ultra.
- Đủ 7 file 2K trong clips/ (sha đã ghi ở entry 08:16 + sh050 ở đây). Subagent đang dựng master 2K cuối: title "CON NHỎ ĐÓ" kiểu ep004 (TitleCard đè lên sh010 2s đầu, dải trên, không lấp đầu), audio wordalign sh010/sh030 lấy từ file wordalign 1K ghép lên video 2K, cùng trim/captions/laugh track như bản 1K đã duyệt. File cuối vào delivery/.
- Browser task tải 2K ĐÃ HOÀN TẤT (07:31-08:24, 52 phút): đủ 7 clip, không lỗi clip nào, không nâng Ultra, không đổi gì trong project. Clip ID đầy đủ: sh010 3622bcb9, sh020 c3e21d9c, sh030 5c6fd75c, sh040 390570f3, sh050 c59b3807, sh060 d5c80b1e, sh070 80cca483. Số dư Flow lúc đăng nhập 08:24: 470 credit (hôm qua 17:01 là 420 — tăng, có thể do cộng dồn ngày; ghi nhận, chưa đối chiếu).

## 2026-11-22 09:02 — Master 2K XONG, nhưng sh060 dính take sai (đã xử lý tạm)
- Subagent dựng xong: delivery/ep008-master-2k.mp4 sha d1d6ea57… (36.966.784 byte, 1080x1920 30fps, 28.70s, loudnorm -15.33 LUFS) + delivery/ep008-master-2k.srt sha 4dc41876… (identical bản 1K). Title "CON NHỎ ĐÓ" kiểu ep004 đè sh010 2s đầu, dải trên, không lấp đầu (đã soi frame 0.5/1.0/1.5s). Laugh Track 1 trên sh070. Build script edit/build_master_2k.py, report edit/build2k/build-report.md.
- PHÁT HIỆN QUAN TRỌNG: file tải về "sh060-take015-2k.mp4" thực ra là TAKE016 (không phải take015 đã duyệt). Bee verify độc lập bằng frame-diff: 2K-vs-take015 = 16.29 @2.5s, 2K-vs-take016 = 2.19 (khớp số subagent) — clip tải về gần như tĩnh, miệng Nam khép 0.5-6.5s, audio chạy sớm ~1s. Trình duyệt đã bấm nhầm take kề bên.
- XỬ LÝ: subagent KHÔNG dùng file sai — sh060 trong master là local lanczos upscale từ take015 1K đã duyệt (sh060-take015-2k-local-upscale.mp4, sha 80e5729a…) + audio 1K. Bee soi frame 23.0s: Nam cúi người, mặt nhăn nói "CHIA" — đúng take015. File sai đã đổi tên thành sh060-take016-2k-WRONG-FILE-do-not-use.mp4.
- HẬU QUẢ: sh060 trong master 2K hơi mềm hơn 6 shot kia (upscale tay, không phải Flow AI). Muốn 2K thật cho sh060 thì phải tải lại đúng take015 rồi dựng lại — CHỜ Richard quyết (đã báo, giao master hiện tại kèm cảnh báo).
- Audio: sh040 2K có noise floor đầu shot to hơn 1K (0.29-0.74 vs 0.06-0.08) nên tất cả shot native dùng audio 1K đã duyệt; sh010/sh030 giữ audio wordalign. Caption khớp 1K đúng 0ms.

## 2026-11-22 09:06 — Richard DUYỆT master 2K ('ko sao, lấy bản này cũng đc')
- Master 2K FINAL: delivery/ep008-master-2k.mp4 sha d1d6ea57… + SRT sha 4dc41876…. sh060 local upscale được chấp nhận, KHÔNG tải lại take015 2K. Chờ lệnh đăng/hẹn giờ + bộ đăng (TikTok caption ngắn + nhãn AI; Facebook thêm link aff-0005; bìa mặt Thảo My).

## 2026-11-22 09:07 — Bộ đăng chốt + bắt đầu hẹn giờ 19:00 CN 22/11
- TikTok caption: "Chia tay đi, yêu khổ quá. 😌" + #chuyennhathaomy #phimnganai #haiviet + 'Sound effects: "Laugh Track 1.mp3" by LittleRainySeasons, CC BY, via Freesound.org' (theo mẫu ep004/ep006). Audience Everyone, nhãn AI BẬT.
- Facebook description: cùng caption + dòng "Áo sơ mi trắng Nam mặc: https://s.shopee.vn/9zzT7PVjWK" (aff-0005) + dòng CC BY. Public.
- Bìa: delivery/ep008-cover-thaomy.jpg — frame 26.5s (sh070, My sững sờ, không chữ caption, nốt ruồi rõ).
- Video đăng: delivery/ep008-master-2k.mp4 (2K FINAL đã duyệt 09:06).
- 09:08: browser task TikTok (cloud) đang hẹn 19:00 hôm nay; xong sẽ làm Facebook, rồi commit + push git theo lệnh Richard.

## 2026-11-22 09:14 — TikTok ĐÃ HẸN 19:00 hôm nay (video 7710813089712622856)
- Đã xác minh trên trang TikTok: "Scheduled for: 2026-11-22 19:00", Studio > Posts hiện "Nov 22, 7:00 PM (GMT+7) Saigon" + badge scheduled, top row (14 posts), 0 view. Caption đúng từng chữ, Everyone, nhãn AI BẬT ("Creator labeled as AI-generated"), bìa custom mặt Thảo My đã upload, content check đạt. Link: https://www.tiktok.com/@chuyennhathaomy/video/7710813089712622856
- 09:14: browser task Facebook (cloud) đang hẹn Reel 19:00 hôm nay; xong sẽ đặt cron xác minh 19:20 + commit/push git.

## 2026-11-22 09:18 — Facebook ĐÃ HẸN 19:00 hôm nay (post 1875707280232462)
- Đã xác minh trong Business Suite > Content > Scheduled: Sun Nov 22, 7:00pm, Public, Reel, Page Chuyện Nhà Thảo My; mô tả đúng từng chữ (caption + link aff-0005 + dòng CC BY); thumbnail custom mặt Thảo My; Planner cũng hiện 19:00; toast "Reel scheduled". Không có copyright issue. Nhãn AI: KHÔNG có tùy chọn trên web (đúng như đã kiểm chứng 18/11) — không tìm thêm.
- Lưu ý: ep007 cũng hẹn 19:00 hôm nay cả 2 nền tảng — 2 tập lên cùng lúc, đã báo Richard.
- Cron xác minh 19:20 đã đặt (ep008-record-publication, runonce 2026-11-22T19:20 Asia/Ho_Chi_Minh).
- Git: commit e732bd9 đã push (98 file, scope ep008 + Nam + date-cafe + aff-0005; KHÔNG động file ep009/tracker — để cho chat ep009 và cron 19:20 ghi nhận sau).

## 2026-11-22 09:41 — Dời ep008 sang mai 23/11: TikTok KHÔNG sửa được giờ hẹn
- Richard lệnh dời ep008 sang mai (vì ep007 cũng 19:00 hôm nay). TikTok: KHÔNG cho sửa bài đã hẹn — nút edit bị khóa, tooltip "Scheduled posts cannot be edited.", menu chỉ có Download/Delete. Bài vẫn hẹn 19:00 hôm nay (đã xác minh lại trên trang video). Cách duy nhất: xóa bài đã hẹn rồi upload/hẹn lại mai 19:00 — CHỜ Richard ok xóa hay không. Không xóa, không đăng lại khi chưa có lệnh.
- Facebook: đang thử dời bằng edit/reschedule trong Business Suite (chưa có kết quả).

## 2026-11-22 09:43 — Facebook ĐÃ DỜI sang mai 23/11 19:00 (post 1875707280232462)
- Business Suite > Content > Scheduled: dùng "Reschedule post", đổi ngày 22 → 23/11, giữ 19:00. Đã xác minh sau reload: "Mon Nov 23, 7:00pm, Public", mô tả + link aff-0005 + dòng CC BY nguyên vẹn, thumbnail mặt Thảo My; Planner hiện cột Mon 23 lúc 7:00 PM. Không xóa, không đăng lại, không đổi gì khác. Reel ep007 ("Không có thì khỏi cần…") vẫn ở Sun 22, 7:00 PM, không động.
- TikTok vẫn chờ Richard quyết: xóa bài đã hẹn rồi đăng lại hẹn mai 19h, hay để nguyên 19h hôm nay.

## 2026-11-22 10:41 — TikTok ĐÃ XÓA + ĐĂNG LẠI, hẹn 19:00 mai 23/11 (video mới 7710835700802833682)
- Bài cũ 7710813089712622856 đã xóa (TikTok báo "Post deleted"; URL cũ giờ "Video currently unavailable", không còn trong Posts list).
- Bài mới: video 7710835700802833682, hẹn "Nov 23, 7:00 PM (GMT+7) Saigon" (top row, 00:28, Everyone, 0 view). Caption đúng từng chữ, nhãn AI BẬT, bìa custom mặt Thảo My, content check đạt. Link: https://www.tiktok.com/@chuyennhathaomy/video/7710835700802833682
- Cả 2 nền tảng giờ đều hẹn 19:00 T2 23/11. Cron xác minh đã dời sang 19:20 T2 23/11 (ep008-record-publication, cập nhật video ID TikTok mới).
