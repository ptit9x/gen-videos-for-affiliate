# Quy trình vận hành hiện hành

Cập nhật 2026-11-16. Tài liệu giao việc cho Muse Spark trên các tài khoản khác nhau, áp dụng cho Chuyện Nhà Thảo My. Bản nghiên cứu 01 được giữ nguyên; hướng dẫn này triển khai cấu trúc phù hợp quy trình ảnh cảnh → Frames hiện hành.

## Cấu trúc

```text
02_characters/<nhan-vat>/     # source, approved, review, wardrobe, hồ sơ và prompt
03_locations/<boi-canh>/      # source, review, approved, README.md, location.json
04_products/                 # hồ sơ SKU và tư liệu xác thực khi có sản phẩm
05_episodes/epNNN-ten-tap/
  script.md
  episode.yaml
  input/references/
  input/frames/
  input/prompts/
  generated/<shot>/
  edit/manifest.yaml
  delivery/
07_analytics/                # kết quả từng tập và từng nền tảng
00_docs/                     # vận hành, kế hoạch và bản nghiên cứu
```

Kịch bản, clip và bản giao ở cùng tập để truy nguồn shot/take. Không chuyển sang các kho scripts/Flow outputs/final videos chung. Không đổi schema hoặc đường dẫn validator chỉ để thêm location. Bản nháp ý tưởng có thể chỉ có script.md; trước sản xuất phải tạo episode.yaml và manifest bằng `$thao-my-episode`.

## Phân công nhiều tài khoản Muse Spark — chốt 2026-11-16

Mỗi tài khoản Muse Spark được chủ dự án giao một tập. Tài khoản Muse Spark là người thực hiện; project Google Flow là nơi chứa tài sản của tập, không đồng nhất hai khái niệm này. Không giả định tài khoản Muse và tài khoản Google là một.

1. Trước khi làm, đọc AGENTS.md, tài liệu này, hồ sơ tập và `00_docs/production-tracker.csv`. Dùng mã tài khoản do chủ dự án cung cấp (ví dụ `muse-01`), không ghi mật khẩu/cookie/token hoặc email đăng nhập. Nếu chưa có mã, hỏi mã; vẫn có thể đọc và kiểm tra hồ sơ độc lập.
2. Chỉ nhận tập được giao. Cập nhật dòng của tập trong tracker: `muse_account_id`, `work_status=assigned`, thời điểm và nguồn phân công. Nếu đã có tài khoản khác nhận tập, không ghi đè; báo chủ dự án để xử lý bàn giao. Không tự nhận tập khác.
3. Khi bắt đầu, đánh dấu `in_progress`; cập nhật project Flow thực tế trong tracker và `flow_project` của episode.yaml. Ghi tiến độ, revision/take và vướng mắc vào `05_episodes/<tập>/work-log.md`, có thời điểm và mã tài khoản. Khi xong việc được giao, ghi rõ phạm vi hoàn tất và chuyển `awaiting_review`; chỉ `completed` sau duyệt/QC tương ứng. Hoàn tất sản xuất không đồng nghĩa đã đăng.
4. Cập nhật repository sau mỗi mốc nhận việc, tạo frame/take, bàn giao, xác nhận đăng hoặc phát hiện vướng mắc. Trước khi ghi, đọc bản mới nhất; chỉ sửa dòng/file thuộc phạm vi được giao, giữ cập nhật của tài khoản khác. Không ghi đè toàn bộ tracker bằng bản cũ; xung đột cùng dòng cần đối chiếu hoặc báo chủ dự án.
5. Khi đã có bằng chứng đăng, cập nhật riêng Facebook/TikTok trong `07_analytics/publications.csv`: URL bài cụ thể, thời điểm đăng nếu biết, master/revision đã đăng nếu biết, nguồn xác nhận và thời điểm xác minh. Dùng `published` khi có bằng chứng; không suy từ việc render/giao video. `unknown` nghĩa chưa xác minh, không có nghĩa chưa đăng. Một tập đăng lại có dòng riêng cho từng bài. Không tự đăng bài.
6. Nếu làm việc qua remote repository, lưu thay đổi bằng commit mô tả tập/tài khoản hoặc kỳ đo và push lên nhánh làm việc được giao; không tự merge hoặc force-push. Nếu chưa có nhánh được giao, dùng nhánh riêng `codex/muse-<ma>-<ep>-<moc>` để bàn giao. Chỉ báo đã đồng bộ khi kiểm tra commit đã có trên remote. Nếu không có quyền ghi/push, giữ bản local hoặc patch, báo đường dẫn/commit và trở ngại; không báo repository đã cập nhật từ xa.

Tracker dùng trạng thái `unverified`, `assigned`, `in_progress`, `awaiting_review`, `completed`, `blocked`. Dòng khởi tạo `unverified` không phủ nhận các công việc đã làm trước đây. Không thay schema episode.yaml để chứa tài khoản hoặc trạng thái đăng; các sổ theo dõi là thông tin điều phối, episode.yaml vẫn là hồ sơ sản xuất của tập.

## Màu váy cho các tập sau ep002 — cập nhật 2026-11-16

Người dùng chọn tiếp link `aff-0001` cho các tập sau, với nguồn váy trắng/xanh dương/hồng tại `02_characters/thao-my/wardrobe/inbox/sanjoli-color-variants/`. ep002 giữ kem. Muse đọc README nguồn và đề xuất màu cụ thể trong wardrobe.md của tập; chưa coi màu từng tập đã chốt. Chỉ định này cập nhật hướng trang phục Thảo My, giữ lịch sử đề xuất cũ, mặt/body và continuity; không tự gen hoặc duyệt frame.

## Link affiliate sản phẩm — chốt 2026-11-16

Hiện người dùng chưa thêm được link Shopee: chỉ lưu link và đề xuất tập/ngữ cảnh phù hợp trong `04_products/affiliate-suggestions.csv`; không tự gắn link, sửa kịch bản hoặc yêu cầu đo chuyển đổi. Gợi ý cần người dùng duyệt. Muse lưu link Shopee affiliate thực tế vào `04_products/affiliate-links.csv`, giữ cả link sản phẩm gốc và link affiliate. Ánh xạ tập/bài/vị trí dùng tại `04_products/affiliate-placements.csv`; giữ lịch sử khi thay link. Đọc `04_products/README.md` trước cập nhật. Chưa có link thì không tự tạo hoặc đánh dấu đã gắn. Schedule đọc các sổ này để đối soát và đo hiệu quả trong phạm vi dữ liệu có được; lưu link không phải ủy quyền đăng/gắn link.

## Schedule hằng tuần: đo lường và ghi ngược repository

Dùng hướng dẫn giao việc tại `07_analytics/weekly-review-instructions.md` cho Schedule của Muse Spark. Schedule phải cập nhật kết quả thật, trạng thái đăng và dấu vết lần chạy trong repository; gửi báo cáo chat đơn thuần chưa hoàn tất công việc. Chưa có lịch/giờ chạy hoặc Schedule được tạo bởi việc cập nhật tài liệu này.

## Nền sản xuất đã duyệt

Mặt và tóc `thao-my-face-front-v002.png` (người dùng chọn 2026-11-16); body chính diện, nghiêng trái và phía sau v003 chỉ khóa vóc dáng. Không lấy mặt/tóc cũ từ body v003. Các bản ghép mới trong `02_characters/thao-my/review/body-v003-face-v002/` phải duyệt riêng. Danh mục/hash ở `02_characters/thao-my/references.json`. Chỉ dùng bộ mới cho sản xuất mới. Ảnh body áo trắng/quần short be khóa tỷ lệ; trang phục từng tập phải ghi riêng. Trang phục chọn theo từng tập trong `wardrobe.md`; nguồn người dùng gửi qua chat hoặc `02_characters/<nhân-vật>/wardrobe/inbox/`. Không mặc định váy SANJOLI đen cho toàn series; giữ nguyên bộ của ep001–002 đang gen. Bộ location mới còn chờ duyệt; My dùng preset Đoan Trang theo character.yaml, Vy chưa chốt giọng.

## Tổ chức project Google Flow — chốt 2026-11-16

- Mỗi tập dùng một project sản xuất riêng, tên `CNTM · EP001 · Dọn bàn`, `CNTM · EP002 · Tiêu chuẩn cơ bản`… Tạo project khi bắt đầu chuẩn bị frame; chưa cần tạo cho ý tưởng chỉ có kịch bản.
- Project `CNTM · LAB · Thảo My` dành cho thử tạo hình, trang phục và bối cảnh. Chỉ tạo khi có công việc thử nghiệm tương ứng; tài nguyên thử không tự trở thành bản đã duyệt.
- Trong project tập, nếu UI tài khoản có Collections, nhóm tài nguyên thành `00 · Tham chiếu`, `01 · Frame`, `02 · Takes`, `03 · Chọn dựng`. Nhóm chọn dựng chỉ chứa các take đã chọn; giữ lịch sử take còn lại. Nếu chưa có Collections, dùng ánh xạ shot/take trong hồ sơ local để truy nguồn.
- Gen lại shot hoặc tăng revision vẫn dùng project của tập; không tạo project mới cho mỗi take. Tải các ảnh nguồn đã duyệt thực sự cần vào đúng project tập; LAB không thay thư viện nguồn local.
- Ghi URL project vào trường `flow_project` hiện có trong `episode.yaml`; không thêm trường ngoài schema. Tải frame/clip về thư mục tập, giữ hash và ánh xạ shot/take. Tên file local rõ ràng, ví dụ `sh010-frame-v001.png`, `sh010-take-001.mp4`.
- Chuyển tiếp: giữ nguyên project cũ và mọi tài sản/lịch sử. Tập đang làm dở có thể hoàn tất ở project cũ; từ tập tiếp theo dùng project riêng. Không tự di chuyển, đổi tên hoặc xóa tài sản cũ để áp dụng quy ước.
- Quy ước này đã được người dùng duyệt; chưa đồng nghĩa đã tạo project hoặc Collections trên Flow. Tạo project không phải ủy quyền gen video hoặc đăng bài.

## Từ kịch bản tới video

1. Viết kịch bản: mỗi clip khoảng 8 giây, một người nói, câu ngắn và một hành động chính. Ghi thoại, góc máy, hành động, nguồn mặt/body/location và trang phục. Người dùng duyệt hướng/kịch bản.
2. Copy các nguồn đã duyệt thực sự cần vào input/references, giữ tên file; khai báo từng file/hash trong episode.yaml. Asset không dùng chung giữa các project Flow.
3. Tạo/chọn project riêng của tập theo quy ước trên (áp dụng ngoại lệ chuyển tiếp cho tập đang làm dở), ghi URL vào `flow_project`. Sửa ảnh cảnh trong project Flow từ ảnh đơn nhân vật và location đã duyệt. Giữ mặt/tóc, bố cục và đạo cụ nhất quán. Tải frame đã duyệt vào input/frames, hash và ánh xạ shot; không ghi đè frame đã dùng. Mặt lệch thì sửa frame trước.
4. Chỉ khi được yêu cầu gen shot: Frames trực tiếp, Agent tắt, một frame đầu, không frame cuối hay ảnh kèm. Video 9:16, 8 giây, một output. Kiểm tra model/credit/quota thực tế trên UI trước mỗi lượt. Prompt chuyển động ngắn, thoại nguyên văn, máy tĩnh, không nhạc/chữ/phụ đề. Ghi take và ID Flow.
5. Đọc skill sitcom-flow-assembly trước hậu kỳ. Giữ clip nguồn; tắt tiếng Veo, lồng cùng preset VieNeu đã chốt; hard cut, SRT riêng, QC hình/âm thanh/khớp môi. Manifest ghi take, lệnh dựng, thông số và kết quả QC. Chỉ bản đạt QC vào delivery.
6. Trước khi giao video cuối, kiểm tra icon Veo góc phải trên mọi shot. Nếu có, crop vừa đủ theo vị trí thực tế, giữ 9:16 và scale đồng đều về 1080×1920; không méo hình/viền đen, không cắt mất mặt, tay hoặc đạo cụ quan trọng. Làm trước burn-in phụ đề/đồ họa nếu có, giữ nguồn/master tốt, ghi crop và lệnh thật vào manifest rồi QC lại. Nếu crop ảnh hưởng nội dung quan trọng, trình phương án trước khi chốt. Không có icon thì bỏ qua bước crop này.
7. Áp dụng skill `/Users/richard/.codex/skills/remotion-best-practices/SKILL.md` cho bước hoàn thiện bằng Remotion sau crop: lưu composition trong edit/remotion/, preview trước, render khi được yêu cầu xuất/bàn giao, rồi QC bản render cuối trước delivery. Crop có thể đặt ngay trong composition trước lớp chữ để tránh encode nhiều lần. Không tự thêm hiệu ứng/nhạc/burn-in; giữ SRT riêng mặc định và quy trình QC của sitcom-flow-assembly. Chưa có clip nguồn thì chưa coi bước này đã thực hiện.
8. Đăng chỉ khi có yêu cầu cụ thể. Ghi số liệu thật vào analytics; lịch và mục tiêu vẫn là giả thuyết thử nghiệm.

Validator chỉ kiểm tra offline, không gen hoặc chứng nhận media. Không lưu secret/session. Đổi mặt/frame/prompt sau gen phải tăng revision và giữ lịch sử take; không gọi take cũ là đầu ra của revision mới.

## Tình trạng ep001

Rev3 dùng mặt mới/body v003; chưa gen frame/video mới. ID clip rev2 giữ để truy nguồn, hai đường dẫn clip local cũ không tìm thấy khi kiểm tra 2026-11-15. Cần duyệt kịch bản/frame và chốt giọng trước các bước tương ứng.

### Nhận diện chốt cuối 2026-11-16

Mặt/tóc hiện hành `thao-my-face-front-v002.png`; body chính diện hiện hành `thao-my-body-front-v003-face-v002-review.png` trong `02_characters/thao-my/approved/`. Hai góc ghép v002 khác chưa duyệt. Chỉ định này thay các hướng thử giữ mặt cũ hoặc hair-density-r02. ep001 rev5 đang chuẩn bị lại với bộ này; không coi media rev4 là media rev5.
