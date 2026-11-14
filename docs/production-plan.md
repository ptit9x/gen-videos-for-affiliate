# Lộ trình đề xuất — Chuyện Nhà Thảo My → affiliate

Ngày review: 2026-11-12. Đây là đề xuất triển khai; tuổi/nghề/tính cách, ngành hàng, lịch và ngân sách bên dưới chưa phải quyết định của chủ dự án. Không hứa doanh thu hay thời điểm ra đơn.

## Tiến độ đã xác nhận

- Người dùng đã làm video giới thiệu/công bố Thảo My là AI: [video Facebook](https://www.facebook.com/share/r/18EVd1BLCM/). Không cần làm lại chỉ để hoàn thành bước giới thiệu.
- Chưa review nội dung video, số liệu hoặc xác nhận bản đăng TikTok. Video giới thiệu là tài nguyên có thể tham khảo khi review giọng, mặt và phong cách; chưa mặc định mọi tài nguyên xuất hiện trong video đã được chốt cho các tập sau.
- Bước tiếp theo: xác nhận có tiếp tục dùng tạo hình/giọng trong video này không, rồi viết pilot sitcom đầu tiên. Nếu giữ bộ hiện có, chỉ thử thêm khi có lỗi cụ thể cần giải quyết.

## 1. Review những gì đang có

| Tài nguyên | Đánh giá | Cách dùng tiếp |
|---|---|---|
| `characters/thao-my/source/` | Đã chọn tạo hình trong hai sheet facial-expressions và multi-angle; Flow từ chối sheet nhiều mặt | Đã tách 21 PNG trong approved/, có tên tham chiếu cố định; thử một ảnh trước, tối đa 3 input theo thử nghiệm người dùng |
| Prompt reference 3×3 | Hữu ích để xem các góc và kiểm tra mặt; không phù hợp để mặc định đưa nguyên bảng vào Flow | Xuất/crop từng ảnh đơn đã kiểm tra, không sinh lại khuôn mặt độc lập bằng chữ |
| Prompt product-review poses | Hộp/chai trắng chỉ là vật mẫu cho tư thế; không đại diện SKU sẽ bán | Khi affiliate phải dùng đúng sản phẩm và biến thể; ưu tiên footage thật tự quay hoặc được phép dùng |
| `brand/avatar.png`, `brand/banner.png` | Nhận diện hiện tại nhất quán màu đỏ/kem, nêu rõ sitcom đời thường | Giữ ở giai đoạn test. Chưa cần làm lại chỉ vì chưa có mặt nhân vật trên avatar |
| Docs 01: production bible/pilot | Có khung hài nhưng tạo hình Vy khác bộ tham chiếu Thảo My; pilot 02/03 cần hai nhân vật chưa có | Giữ nguồn; không dùng ngoại hình Vy ghi đè ảnh hiện tại. Khởi đầu bằng Thảo My solo |
| Docs 02: Flow 8s | Gần nhu cầu thực tế nhất: ngắn, một người nói, một hành động, ảnh đơn | Dùng làm nguyên tắc thử. 12–18 từ là ngân sách tham khảo, đọc và nghe thử từng câu |
| Docs 03: lịch đăng | Đề xuất 1/ngày, kho 7–10 tập, chờ 14 ngày mới affiliate có thể tốn vốn trước khi biết format hiệu quả | Làm 3 pilot trước, chọn format rồi mới tăng kho. Mốc chuyển dựa trên chất lượng, dữ liệu và quyền affiliate |
| Skill hậu kỳ | Có khung ghép/âm thanh/phụ đề tốt; công cụ QC còn lỗi đã review | Chưa coi nhãn `ok`/`fluid` hoặc exit code là đạt. Đọc số đo và kiểm tra nghe/nhìn; sửa QC trước khi chạy hàng loạt |

Các prompt hiện mô tả tóc nâu dài, mái bằng, phong cách trang điểm nhẹ. Ảnh `reference-original.jpg` là ảnh chụp nghiêng, có bối cảnh và tay gần mặt; phù hợp làm nguồn tham khảo hơn là mặc định ảnh chính diện chuẩn. Chưa xác minh tính nhất quán của toàn bộ ảnh hoặc nguồn/quyền thương mại của ảnh gốc. Trước khi chọn master dùng thương mại, xác nhận quyền dùng nguồn; nếu nguồn là người thật và chưa có quyền phù hợp, xây tạo hình hư cấu riêng thay vì khóa bản sao nhận diện của người đó.

## 2. Hướng nội dung nên thử

**Đề xuất định vị:** Thảo My — cô gái hay đặt mục tiêu sống ngăn nắp, mua sắm thông minh nhưng thường tự mâu thuẫn, kể chuyện nhà bằng giọng cà khịa. Chưa cần chốt tuổi, nghề hay thêm người yêu để làm pilot.

Lý do: chủ đề hẹn hò có thể thu hút lượt xem nhưng chưa chứng minh được ý định mua. Chuyện sinh hoạt, góc bàn và mua sắm nối tự nhiên hơn tới các đồ dùng có thể minh họa bằng hình thật.

Ba trụ nội dung thử:

1. **Nhà gọn, chủ nhà chưa gọn:** đồ thất lạc, bàn bừa, dây sạc rối.
2. **Mua để tiết kiệm rồi mua thêm:** giỏ hàng, mua trùng đồ, cám dỗ sale.
3. **Đi làm về chỉ muốn nhàn:** sinh hoạt nhỏ trong nhà, mẹo và đồ dùng có công dụng quan sát được.

Khởi đầu bằng **đồ sắp xếp góc bàn/nhà nhỏ** như nhóm giả thuyết, chưa chọn SKU. Chưa cần mở đồng thời mỹ phẩm, sức khỏe, thời trang và điện tử. Chọn theo khả năng tự kiểm tra sản phẩm, tư liệu thật, người bán, mức hoàn trả và hoa hồng thực nhận; không chọn chỉ vì phần trăm hoa hồng cao.

Mỗi câu chuyện cần có tiếng cười ngay cả khi bỏ link. Khi có link, sản phẩm phải thực sự xuất hiện và có vai trò rõ trong câu chuyện; tránh gắn giỏ hàng vào clip chỉ nói chuyện yêu đương không liên quan.

## 3. Đi từng bước, có đầu ra và điều kiện chuyển

### Bước 1 — Chốt nền sản xuất (1–3 buổi là ước lượng)

- Xác nhận master Thảo My và quyền dùng nguồn hình; chọn một trang phục, một bối cảnh trong nhà và giọng cho pilot.
- Chỉ cần ảnh đơn chính diện và góc 45° thực sự dùng. Chưa cần bộ ảnh mọi trang phục/biểu cảm.
- Dùng cùng câu thoại thử 2–3 clip: nghe giọng, kiểm tra mặt và khả năng nói hết câu, ghi số lần tạo lại/chi phí.
- Giữ avatar/banner đang dùng; bio đề xuất: “Sitcom AI chuyện đời thường cùng Thảo My.” Việc cập nhật kênh do người dùng quyết định.
- Kiểm tra số follower và các quyền đang có trong TikTok Shop cho nhà sáng tạo. Chưa nhập giấy tờ hay dữ liệu thuế vào repo.

**Chuyển bước khi:** có một bộ mặt/giọng/bối cảnh đủ ổn định để sản xuất tiếp, hoặc đã chọn giải pháp TTS nếu âm thanh gốc không ổn. Không tiếp tục mua nhiều lượt tạo khi chưa biết lỗi nằm ở đâu.

### Bước 2 — Viết và làm 3 pilot solo

- Pilot A: “Dọn bàn để làm việc — dọn xong hết giờ” (tình huống thuần hài).
- Pilot B: “Cất kỹ quá, chính chủ cũng không tìm thấy” (nhu cầu sắp xếp).
- Pilot C: “Mua thêm để tiết kiệm phí ship” (mâu thuẫn mua sắm).
- Mỗi tập dự kiến 24–32 giây, 3–4 clip nguồn khoảng 8 giây; cho phép cắt gọn theo nhịp thoại. Không bắt buộc clip nào cũng có lời.
- Ghi đầy đủ prompt trong `episodes/ep001-ten-tap/script.md`; dùng `templates/episode/script.md`. Ba ý tưởng trên chưa phải kịch bản sản xuất đã duyệt.
- Làm xong một tập, xem chất lượng và chi phí trước khi làm tiếp hai tập. Không tạo cùng lúc 10 tập khi pipeline chưa ổn.

**Chuyển bước khi:** có 3 video hoàn chỉnh, không lỗi lời thoại/nhân vật nghiêm trọng và chi phí mỗi tập nằm trong mức chủ dự án chấp nhận.

### Bước 3 — Đăng thử, chọn format (khoảng 7–14 ngày nếu đủ sức sản xuất)

- Đề xuất 3–5 video/tuần ban đầu trên mỗi kênh, dùng cùng master sạch watermark. Có thể lên 1/ngày nếu chất lượng và ngân sách cho phép; đây không phải quy tắc thuật toán.
- Đăng 3 pilot rồi làm biến thể của format có tín hiệu tốt; mỗi biến thể ưu tiên đổi một yếu tố như hook hoặc câu chốt.
- Giờ 19:30 TikTok / 20:30 Facebook từ tài liệu cũ chỉ là giờ thử theo Việt Nam. Không kết luận sau một bài.
- Đo ở mốc 24h và 72h: thời lượng xem trung bình, tỷ lệ xem hết, lượt chia sẻ/bình luận, follow mới, thời gian và chi phí sản xuất. So trong từng nền tảng, với video có thời lượng gần nhau.
- Đọc bình luận tìm nhu cầu về món đồ/tình huống. Không lấy nhiều view làm bằng chứng chắc chắn bán được hàng.

**Chuyển bước khi:** một kiểu nội dung lặp lại được tín hiệu tốt qua vài video, có nhu cầu sản phẩm phù hợp và có đường affiliate được tài khoản cho phép. Không bắt buộc đợi đúng 14 ngày; có thể thử thương mại sớm nếu đã đáp ứng các điều kiện này.

### Bước 4 — Mở đường nhận hoa hồng

Thông tin công khai kiểm tra ngày 2026-11-14:

- Hướng dẫn đăng ký TikTok Shop Việt Nam nêu điều kiện affiliate tiêu chuẩn gồm từ **1.000 follower**, chủ tài khoản **từ 18 tuổi**, cùng điều kiện tài khoản và xác minh. Xác minh bằng thông tin thật của người vận hành, không dùng danh tính Thảo My. Xem [hướng dẫn đăng ký chính thức](https://seller-vn.tiktok.com/university/essay?knowledge_id=6837838528808705&lang=vi-VN).
- TikTok cũng công bố [chương trình hỗ trợ nhà sáng tạo 200–999 follower](https://seller-vn.tiktok.com/university/essay?identity=1&knowledge_id=2356948167771905&role=1). Đây không phải cam kết tài khoản nào cũng có sẵn; kiểm tra lời mời/điều kiện/quyền trong ứng dụng.
- [Chương trình chỉ chia sẻ link](https://seller-vn.tiktok.com/university/essay?knowledge_id=8659790494680849&lang=vi-VN) khác quyền gắn sản phẩm trong video/LIVE. Nếu được duyệt chương trình phù hợp, có thể dùng link theo các kênh được chương trình chấp nhận, gồm Facebook khi được phép. Không mặc định có link nghĩa là đã có giỏ hàng trong video.
- Hoàn thành xác minh, thông tin thanh toán/thuế theo màn hình chính thức của tài khoản. Điều kiện có thể đổi; xác nhận lại trước đăng ký và trước triển khai. Chưa truy cập tài khoản nên chưa xác nhận được quyền của hai kênh hiện tại.

**Đầu ra:** ghi rõ chương trình đã duyệt, loại quyền, nơi được đặt link và cách lấy báo cáo hoa hồng. Nếu chưa có quyền, tiếp tục test nội dung thay vì giả lập giỏ hàng.

### Bước 5 — Test 1–3 sản phẩm, mỗi sản phẩm 2–3 góc kể

Trước khi quay, ghi một hồ sơ ngắn cho từng SKU:

- Link listing, SKU/biến thể, người bán, tồn kho và thông tin sản phẩm kiểm tra ngày nào.
- Giá và hoa hồng hiện hành; chi phí mẫu/ship/clip/tư liệu.
- Công dụng nào tự quan sát được, công dụng nào chỉ do người bán công bố; nguồn chứng minh từng claim.
- Footage tự quay hoặc quyền dùng footage/ảnh người bán; không mặc định tải lại video shop là được phép.

Định dạng đề xuất: **hook hài của Thảo My → tình huống → cảnh thật minh họa đúng sản phẩm → phản ứng/câu chốt → CTA ngắn**. Không tự tạo cảnh sản phẩm AI “hoạt động thần kỳ”. Không cho nhân vật hư cấu kể trải nghiệm cá nhân như một khách hàng thật khi không có cơ sở.

Chỉ một sản phẩm chính/video trong đợt test. Thử tỷ lệ khoảng 3 tập giải trí : 1 tập có affiliate để quan sát phản ứng, điều chỉnh theo dữ liệu; không coi tỷ lệ này là công thức cố định.

Khi có đường mua được kích hoạt, CTA phải khớp nơi mua thực tế. TikTok có giỏ hàng thì chỉ đúng giỏ hàng; Facebook dùng link đã được chương trình chấp nhận. Tạo tracking riêng từng video/nền tảng nếu chương trình hỗ trợ; không thay cấu trúc link làm mất attribution.

### Bước 6 — Đọc doanh thu thực, rồi mới tăng sản lượng

- Views → click sản phẩm → đơn tạo → đơn hoàn tất → hoa hồng thực nhận. Đơn hủy/hoàn không phải doanh thu đã kiếm được; xem [quy định chương trình chia sẻ link](https://seller-vn.tiktok.com/university/essay?knowledge_id=8659790494680849&lang=vi-VN).
- Lưu số liệu khi có báo cáo và cập nhật sau thời hạn hoàn/đối soát. Phân biệt hoa hồng ước tính với đã thanh toán.
- Nhiều view ít click: xem lại nhu cầu, mức liên quan sản phẩm và CTA. Có click ít đơn: xem giá, listing, biến thể và người bán. Có đơn nhưng hoàn nhiều: kiểm tra sản phẩm và kỳ vọng do video tạo ra.
- Lãi đóng góp = hoa hồng thực nhận − chi phí sản xuất − chi phí mẫu/ship phân bổ − chi phí phân phối trực tiếp. Ghi công sức riêng để biết format có đáng tiếp tục.
- Điểm hòa vốn theo số đơn = chi phí phân bổ / hoa hồng thực nhận trung bình mỗi đơn hoàn tất. Chưa có dữ liệu thì không dự báo thu nhập.
- Chỉ tăng số tập hoặc thêm nhân vật khi format lặp lại được và kinh tế sản xuất hợp lý. Sau 6–9 video bán hàng thử mà chưa có tín hiệu click/đơn, review sản phẩm và góc kể trước khi tiếp tục chi tiền render.

## 4. Những điểm trực tiếp ảnh hưởng video AI bán hàng

- TikTok yêu cầu gắn nhãn nội dung AI có hình/âm thanh/video chân thực: [trợ giúp AIGC](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content).
- Video quảng bá thương hiệu/sản phẩm có lợi ích thương mại cần bật công bố nội dung thương mại theo [hướng dẫn TikTok](https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/promoting-a-brand-product-or-service). Nhãn AI và công bố thương mại phục vụ hai mục đích khác nhau.
- TikTok Shop Việt Nam cho phép AIGC theo điều kiện, nhưng hình và claim phải phản ánh đúng sản phẩm: [hướng dẫn AIGC](https://seller-vn.tiktok.com/university/essay?knowledge_id=6832782790018833&lang=vi-VN), [sản phẩm phải nhất quán](https://seller-vn.tiktok.com/university/essay?from=policy&identity=1&knowledge_id=6388742173902593&lang=vi-VN).
- Dùng nhạc có quyền thương mại phù hợp, giọng và hình có quyền sử dụng. Mặc định clip thương mại không cần nhạc nếu chưa xác định quyền.
- Minh bạch với người xem, ví dụ “Thảo My là nhân vật AI. Bài có liên kết tiếp thị, kênh có thể nhận hoa hồng từ đơn đủ điều kiện.” Câu này không thay thế nút công bố của nền tảng.

## 5. Việc làm trước mắt

1. Đã tách 21 ảnh đơn từ hai sheet đã chọn. Dùng tên trong `characters/thao-my/references.json`; chọn master và thử một clip với một ảnh. Chốt giọng muốn thử.
2. Ghi số follower hiện tại, trạng thái TikTok Shop và mức tiền/công chấp nhận cho một tập.
3. Viết hoàn chỉnh pilot A từ mẫu, tạo thử một clip trước khi sản xuất cả tập.
4. Chốt một nhóm sản phẩm dự kiến và nguồn footage thật; chưa cần mua nhiều mẫu.
5. Sau 3 pilot, cập nhật kế hoạch từ kết quả thực tế thay vì tiếp tục mở rộng tài liệu.
