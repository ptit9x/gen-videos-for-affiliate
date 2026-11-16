# Hướng dẫn làm việc trong dự án

## Mục tiêu và giao tiếp

- Đây là workspace sản xuất video sitcom AI ngắn hướng tới affiliate, hiện ở giai đoạn thử nghiệm cho Page “Chuyện Nhà Thảo My”. Quy trình Flow qua UI đã chạy thành công; chưa có runner tự động. Validator hồ sơ tập nằm trong `06_automation/`.
- Trao đổi, viết kịch bản và báo cáo bằng tiếng Việt. Prompt tạo hình/video có thể dùng tiếng Anh; lời thoại giữ tiếng Việt có dấu.
- Ưu tiên hoàn thành đầu việc đã được yêu cầu. Phân biệt rõ đề xuất, nội dung đã chốt và kết quả đã kiểm chứng; không tự biến gợi ý trong tài liệu thành quyết định của chủ dự án.

## Điều phối Muse Spark và đo lường — chốt 2026-11-16

- `00_docs/production-workflow.md` là tài liệu giao việc cho Muse Spark. Chủ dự án dùng nhiều tài khoản Muse Spark, mỗi tài khoản được giao một tập. Không đồng nhất tài khoản Muse với tài khoản Google Flow.
- Trước khi làm, đọc/cập nhật `00_docs/production-tracker.csv`: mã tài khoản, tập, trạng thái, URL Flow, thời điểm và nguồn phân công. Không tự nhận tập khác/ghi đè người phụ trách; mã tài khoản không chứa secret. Ghi tiến độ thực tế trong work-log.md của tập, cập nhật repository sau từng mốc.
- `07_analytics/publications.csv` theo dõi từng bài theo nền tảng, URL, ngày đăng, revision và bằng chứng. Sản xuất xong không đồng nghĩa đã đăng; `unknown` là chưa xác minh. Không tự đăng bài.
- Schedule Muse Spark hằng tuần phải theo `07_analytics/weekly-review-instructions.md`: đo số liệu thật, review nội dung/phản hồi trong phạm vi truy cập, lưu snapshot/báo cáo và đánh dấu lần chạy, cập nhật ngược repository. Chỉ báo đồng bộ remote sau push được kiểm chứng; thiếu quyền phải báo rõ và giữ bản local/patch. Không lưu secret, không force-push/tự merge.
- Việc chốt hướng dẫn chưa có nghĩa đã tạo Schedule hoặc đã biết mã tài khoản, phân công, trạng thái đăng. Giữ trạng thái chưa xác minh cho tới khi có bằng chứng.

## Kênh chính thức

- Tên kênh/Page: **Chuyện Nhà Thảo My**.
- Facebook: https://www.facebook.com/chuyennhathaomy
- TikTok: https://www.tiktok.com/@chuyennhathaomy
- Người dùng xác nhận đã làm video giới thiệu/công bố Thảo My là AI và cung cấp link Facebook: https://www.facebook.com/share/r/18EVd1BLCM/. Không đề xuất làm lại như một đầu việc chưa hoàn thành. Chưa review nội dung video; chưa có thông tin video này đã đăng TikTok.
- Người dùng xác nhận đã tạo hai kênh trên ngày 2026-11-14. Dùng đúng các URL này khi chuẩn bị caption, lịch đăng và tài liệu bàn giao. Nhân vật chính là **Thảo My**, theo xác nhận bổ sung của người dùng cùng ngày.

## Affiliate hiện tại — chốt 2026-11-16

- Người dùng chưa thêm được link Shopee. Chỉ lưu link affiliate được cung cấp trong `04_products/affiliate-links.csv`, đề xuất tập/ngữ cảnh phù hợp trong `04_products/affiliate-suggestions.csv`. Chưa có link thật thì không tự tạo URL.
- Gợi ý chưa phải lựa chọn được duyệt hoặc link đã gắn; không tự sửa kịch bản/gen media. Chưa yêu cầu đo click/đơn/hoa hồng khi chưa triển khai. `affiliate-placements.csv` chỉ dùng khi có kế hoạch gắn cụ thể hoặc bằng chứng vị trí dùng thực tế.

## Pilot đầu tiên đã đăng — ghi nhận 2026-11-16

- `ep000-pilot1`: người dùng xác nhận đã đăng thử Facebook ngày 2026-11-15 (chưa biết giờ), URL https://www.facebook.com/reel/2920996954966253. Hồ sơ hồi tố tại `05_episodes/ep000-pilot1/README.md`; số liệu tại `07_analytics/ep000.md` và `publications.csv`.
- Chưa review video/lấy số liệu, chưa đối soát tài khoản Muse/project Flow/master; TikTok chưa xác minh. Không đồng nhất với video công bố AI hoặc đánh dấu QC đạt. Giữ số ep001 trở đi. Schedule hằng tuần phải đưa bài này vào phạm vi đo.

## Tổ chức workspace và bản đồ tài liệu

Thứ tự thư mục gốc đã chốt: `00_docs` → `01_brand` → `02_characters` → `03_locations` → `04_products` → `05_episodes` → `06_automation` → `07_analytics`. Giữ kịch bản, clip và bản giao trong cùng tập; không tách thành kho scripts/outputs/final chung. Các đường dẫn cũ chưa đánh số trong bản nghiên cứu là lịch sử, không dùng làm đường dẫn vận hành.


- `00_docs/README.md`: mục lục và phân biệt nghiên cứu với kế hoạch hiện hành. `00_docs/production-plan.md` là lộ trình đề xuất mới, chưa phải toàn bộ quyết định đã duyệt.
- `00_docs/research/01-ke-hoach-san-xuat-pilot.md`: production bible đề xuất, hồ sơ Vy/Minh/Quân và ba pilot.
- `00_docs/research/02-toi-uu-thoai-flow-8s.md`: điều chỉnh từ thử nghiệm Flow thực tế; áp dụng khi chuyển kịch bản pilot cũ thành clip sản xuất.
- `00_docs/research/03-tan-suat-dang-video.md`: kế hoạch thử nghiệm lịch đăng và đo lường.
- `00_docs/production-workflow.md`: hướng dẫn vận hành hiện hành, từ tài nguyên dùng chung tới frame cảnh, Flow và hậu kỳ.
- `01_brand/`: avatar/banner đang dùng trên kênh, không phải ảnh master nhân vật.
- `02_characters/thao-my/`: mặt mới và body v003 đã duyệt 2026-11-15; `approved/` giữ 3 ảnh body v003, mặt v001 lịch sử và mặt/tóc v002 hiện hành. `references.json` ghi tên và SHA-256, `character.yaml` ghi tạo hình/giọng. 27 ảnh cũ đã xoá theo yêu cầu, không khôi phục hoặc dùng lại cho sản xuất mới. `source/` giữ nguồn xuất xứ.
- `03_locations/`: phòng khách căn hộ 50 m², sân nội khu và café hẹn hò. Mỗi location có `source/`, `review/`, `approved/`, README và `location.json`; cả ba đang chờ duyệt, chưa có master. 50 m² là tổng diện tích căn hộ, không phải phòng khách.
- `04_products/`: hồ sơ sản phẩm và tư liệu xác thực; `affiliate-links.csv` lưu link sản phẩm/link affiliate thực tế, `affiliate-placements.csv` ánh xạ link với tập/bài/vị trí dùng. Muse và Schedule cập nhật theo README của thư mục, giữ lịch sử, không tự coi lưu link là đã gắn hoặc có doanh thu; `07_analytics/`: kết quả từng tập/nền tảng, chỉ ghi số liệu thật.
- `05_episodes/`: kịch bản, input, generated, edit và delivery theo từng tập. Dùng [skill thao-my-episode](/Users/richard/.codex/skills/thao-my-episode/SKILL.md) để viết kịch bản và lập hồ sơ tập; bộ khung nằm trong assets của skill, không còn thư mục templates tại gốc dự án. `06_automation/README.md` hướng dẫn validator offline; `episode.yaml` là hồ sơ sản xuất duy nhất, ghi take và ID Flow. Không lưu secret.
- `/Users/richard/.codex/skills/sitcom-flow-assembly/SKILL.md`: quy trình hậu kỳ chi tiết; đọc trước khi dựng, xử lý âm thanh hoặc giao video. `SOURCES.md` trong cùng thư mục skill ghi nguồn; `scripts/` chứa công cụ QC. Gọi skill bằng `$sitcom-flow-assembly`.

## Bảo toàn nguồn và quyết định

- Các tài liệu trong `00_docs/research/` là bản lưu hội thoại có nguồn. Giữ nguyên nội dung và thông tin xuất xứ; viết bản biên tập/kịch bản mới thành file riêng, trừ khi người dùng yêu cầu sửa bản lưu.
- Mặt chuẩn hiện hành: `thao-my-face-front-v002.png`; body đã duyệt: `thao-my-body-front-v003.png`, `thao-my-body-profile-screen-left-v003.png`, `thao-my-body-back-v003.png`. Tất cả nằm trong `02_characters/thao-my/approved/`. Mặt mới giữ giống ảnh người dùng đưa; đề xuất trẻ hóa trước đó đã bị bỏ. Lấy khuôn mặt, tóc và thần thái từ ảnh đã duyệt, không dùng mô tả cũ ghi đè.
- Body v003 mặc áo thun trắng/quần short be để xem tỷ lệ, không tự thay trang phục cảnh/tập. Chiều cao khoảng 169 cm là ý đồ thiết kế; không suy ra số đo ba vòng từ ảnh. Không trộn với body cũ. Bộ mới chưa kiểm chứng trong Flow.
- Tên nhân vật hiện hành là **Thảo My**. “Vy”, “Minh”, “Quân” trong nghiên cứu không phải dàn nhân vật đã triển khai; ưu tiên solo. Không suy ra có nhân vật khác chỉ từ tên thư mục.
- Trước khi gen body hoặc thay vóc dáng mới, mô tả theo ảnh tham chiếu để người dùng duyệt rồi mới gen; bộ v003 hiện đã được duyệt, không cần hỏi lại để dùng đúng bộ đó.
- Khi viết nội dung mới, ghi rõ tên đang dùng, phiên bản và các điểm cần chốt. Chỉ hỏi những điểm thực sự chặn công việc; tiếp tục các phần độc lập.
- Lịch đăng, giờ đăng và mục tiêu số lượng trong tài liệu là giả thuyết thử nghiệm. Mốc “14 ngày chưa affiliate” chỉ là gợi ý cũ, không phải ràng buộc đã chốt. Thử nội dung có ngữ cảnh sản phẩm từ sớm; chỉ bật affiliate khi có quyền phù hợp, sản phẩm và tư liệu xác thực. Không tự đăng bài.

## Kịch bản và Google Flow

- Định hướng: người thật điện ảnh, hài đời sống/cà khịa bằng lời thoại và diễn xuất, mỗi tập khoảng 25–40 giây, khung dọc 9:16.
- Thiết kế mỗi clip Flow khoảng 8 giây như một đơn vị độc lập: một người nói, một câu ngắn trọn ý, một hành động chính. Ngân sách khoảng 12–18 từ tiếng Việt; câu có khoảng nghỉ hoặc nhấn hài cần ngắn hơn. Nếu quá dài, tách clip thay vì ép tốc độ nói.
- Cấu trúc tham khảo: Hook → Tình huống → Cà khịa → Chốt hài. Cho phép clip phản ứng không thoại; không bắt buộc kéo dài tập chỉ để đủ cấu trúc.
- Mỗi clip ghi rõ người nói, thoại, hành động, góc máy, ảnh tham chiếu và thời lượng dự kiến. Ảnh nguồn sửa cảnh dùng đúng tên PNG trong `02_characters/thao-my/README.md`/`references.json`; khai báo trong `episode.yaml`. Frame cảnh đã duyệt lưu riêng trong `input/frames/`, không dùng ảnh body thay frame cảnh.
- Giữ nhất quán khuôn mặt, tóc, trang phục, phụ kiện, giọng và bối cảnh trong tập. Dùng ảnh master đã duyệt, tách từng góc phù hợp; không đưa bảng nhiều góc làm ảnh tham chiếu mặc định, không tạo lại nhân vật chỉ bằng mô tả chữ cho từng cảnh.
- Ảnh nguồn sửa cảnh phải là ảnh đơn của cùng Thảo My, không dùng sheet nhiều mặt. Video chỉ nhận một frame cảnh đầu đã duyệt; không đính kèm ảnh nguồn nhân vật.
- Ưu tiên góc đơn và cắt qua lại giữa người nói. Chữ trên điện thoại/đồ họa nên thêm ở hậu kỳ.
- Muse thao tác UI Flow theo quy trình bên dưới; validator chỉ kiểm tra offline. Chỉ gen shot đã được yêu cầu; không lưu cookie, mật khẩu hoặc session. Không đăng bài chỉ vì đã tạo xong clip.

## Hậu kỳ và tổ chức đầu ra

- Giữ nguyên ảnh/clip nguồn. Đặt đầu ra từng tập trong thư mục riêng với tên rõ ràng; không di chuyển, đổi tên hoặc ghi đè hàng loạt tài nguyên hiện có nếu không cần cho yêu cầu.
- Lưu `05_episodes/<episode>/edit/manifest.yaml`: thứ tự cảnh, file nguồn ↔ thoại ↔ prompt, ảnh/giọng tham chiếu, cách xử lý âm thanh, thời lượng đã khóa và thông số xuất. Lưu lệnh dựng trong manifest; lấy clip từ `generated/`, render tạm vào `edit/` và giao bản đạt QC trong `delivery/`.
- Mặc định xuất 1080×1920, 30 fps, H.264, `yuv420p`, âm thanh AAC 48 kHz. Kiểm tra clip bằng `ffprobe` và chuẩn hóa trước khi ghép; xử lý tỷ lệ khung hình có chủ đích để tránh méo hình.
- Ưu tiên hard cut trong hội thoại. Tính lại tổng thời lượng khi thêm chuyển cảnh chồng lấn; xem quy tắc concat/xfade trong skill hậu kỳ.
- Tắt tiếng gốc Veo; lồng VieNeu-TTS bằng một giọng nữ miền Bắc đã được người dùng chốt trước khi render. Kiểm tra khớp môi, nhịp câu và khoảng nghỉ trên bản lồng tiếng; cùng câu chữ không bảo đảm đồng bộ.
- Phụ đề lấy từ kịch bản, đối chiếu lời nói thực tế và canh theo bản dựng cuối. Mặc định giao `.srt` UTF-8 riêng, tối đa hai dòng/cue, không chồng thời gian hoặc vượt độ dài video; chỉ burn-in khi được yêu cầu.
- **Crop icon Veo trước bàn giao — chốt 2026-11-16:** khi có bản dựng video cuối, kiểm tra icon Veo ở góc phải trên toàn bộ các shot. Nếu có, chủ động crop vừa đủ để loại icon; nếu không có thì không crop vì lý do này. Chọn vùng crop theo vị trí icon thực tế, không dùng một tọa độ cố định cho mọi clip. Giữ tỷ lệ 9:16, scale đồng đều về 1080×1920, không kéo méo hoặc để viền đen; ưu tiên giữ mặt, tay, đạo cụ và điểm gây cười. Nếu crop làm mất nội dung quan trọng, báo rõ và trình phương án trước khi chốt bản giao.
- Thực hiện crop trên timeline/bản render tạm trước khi burn-in phụ đề hoặc đồ họa nếu có; giữ nguyên clip nguồn và master tốt. Ghi vùng crop, kích thước trước/sau, bộ lọc/lệnh dựng thật vào manifest. QC lại khung hình từng shot và quanh điểm cắt sau crop, bảo đảm icon không còn, bố cục đúng và thông số xuất đạt; không coi crop là đã đạt QC khi chưa kiểm tra. Giữ công bố nội dung AI phù hợp khi đăng.
- Render ra file tạm, kiểm tra xong mới thay file giao. Không ghi đè bản master tốt duy nhất trước khi bản thay thế đạt QC.

### Remotion sau bước crop — chốt 2026-11-16

- Áp dụng skill [remotion-best-practices](/Users/richard/.codex/skills/remotion-best-practices/SKILL.md), cài từ repo chính thức https://github.com/remotion-dev/skills, để dựng composition/preview và hoàn thiện hậu kỳ sau khi xác định vùng crop icon Veo. Đọc các REFERENCE.md liên quan do skill chỉ dẫn trước triển khai; vẫn áp dụng sitcom-flow-assembly cho âm thanh, phụ đề và QC.
- Mạch xử lý: chọn take → chuẩn hóa/crop nếu có icon → composition Remotion, lồng giọng và phụ đề theo yêu cầu → preview → render khi có yêu cầu xuất/bàn giao → QC → delivery. Có thể áp dụng crop trong composition để tránh mã hóa trung gian nhiều lần, nhưng crop nằm trước lớp chữ/đồ họa.
- Không tự thêm title, hiệu ứng, nhạc, CTA hoặc burn-in phụ đề chỉ vì dùng Remotion; giữ nhịp hài/hard cut và mặc định SRT riêng. Giữ nguồn, lưu code/cấu hình theo từng tập dưới edit/remotion/, ghi phiên bản công cụ, thông số composition và lệnh thực tế trong manifest.
- Cài skill không có nghĩa đã cài runtime Remotion hoặc đã dựng/render video. Kiểm tra môi trường khi bắt đầu hậu kỳ, không báo preview/render/QC đạt nếu chưa thực hiện.

## Kiểm tra và bàn giao

Các lệnh chạy từ thư mục gốc, thay đường dẫn ví dụ bằng file thực tế:

```sh
python3 /Users/richard/.codex/skills/sitcom-flow-assembly/scripts/clip_qa.py path/to/clip.mp4
python3 /Users/richard/.codex/skills/sitcom-flow-assembly/scripts/clip_qa.py path/to/MASTER.mp4
python3 /Users/richard/.codex/skills/sitcom-flow-assembly/scripts/qc_delivery.py path/to/MASTER.mp4 --srt path/to/subs.srt
```

- Cần Python 3, `ffmpeg` và `ffprobe`; kiểm tra công cụ trước khi chạy. Không giả định các dịch vụ TTS, Colab hoặc đường dẫn VM nhắc trong skill có sẵn trên máy này.
- Script `clip_qa.py` còn hạn chế đã review: chế độ QC phụ thuộc tên file `ab01.mp4`, có thể báo `fluid` khi không đo được sync và không trả mã lỗi khi phát hiện drift. Không coi nhãn hoặc exit code là chứng nhận đạt; đọc số đo và xem/nghe trực tiếp cho tới khi sửa công cụ.
- Chạy `clip_qa.py` tuần tự trong cùng thư mục vì script dùng file tạm tên cố định. Điểm đồng bộ môi có `sync_r < 0.3` là không kết luận được; không báo là đạt.
- `qc_delivery.py` hiện kiểm tra probe, giải mã và cấu trúc/thời gian SRT; không tự xác nhận đủ thông số đích, thời lượng khóa hay loudness. Đối chiếu metadata với manifest và đo loudness/true peak riêng theo skill.
- Xem contact sheet gồm ít nhất một frame giữa mỗi clip và frame quanh chuyển cảnh; kiểm tra lệch mặt, tay/mặt lỗi, chữ giả, watermark, khung đen và hình đứng. QC tự động không thay thế việc xem/nghe.
- Khi giao: nêu đường dẫn master, SRT, manifest và lệnh dựng; thời lượng thực tế so với mục tiêu, canvas/fps, xử lý âm thanh, kết quả QC và các phần chưa kiểm chứng. Không báo đã chạy kiểm tra nếu chưa chạy.
- Với thay đổi chỉ ở tài liệu, kiểm tra nội dung, đường dẫn và định dạng; không cần render video.
- Không tự đăng hoặc xuất bản. Chỉ đăng khi người dùng yêu cầu rõ cho bài cụ thể.

## Quy trình gen video bằng Google Flow — CHỐT 2026-11-14

Quy trình UI dưới đây đã chạy thành công ngày 2026-11-14 theo báo cáo sản xuất. Chưa triển khai runner tự động. Giá, quota, watermark và khả năng xuất là quan sát trên tài khoản ngày đó; kiểm tra lại trên UI trước mỗi lần gen, không mặc định còn áp dụng.

### Phân công mới

- **Muse lái giao diện Flow web chính chủ trong Chrome của người dùng** (không dùng gflow CLI hay bất kỳ công cụ reverse-engineered nào) để dựng ảnh cảnh và gen clip, theo từng gói shot được duyệt. Người dùng duyệt hướng/kịch bản và QC bản cuối; đăng bài vẫn chỉ khi người dùng yêu cầu rõ.
- Đơn vị sản xuất của một shot = **1 ảnh tĩnh cảnh (frame đầu) + 1 prompt chuyển động ngắn**. Các “scene lock / prop lock / camera lock” chi tiết thuộc về khâu dựng ẢNH TĨNH, không còn viết thành prompt video dài.

### Tổ chức project Flow — chốt 2026-11-16

- Mỗi tập = một project sản xuất riêng, tên `CNTM · EP001 · Dọn bàn`… Tạo khi bắt đầu chuẩn bị frame; không tạo sẵn cho mọi ý tưởng. Project `CNTM · LAB · Thảo My` dành cho thử nghiệm khi cần, không thay thư viện nguồn local hoặc trạng thái duyệt.
- Nếu UI có Collections, chia `00 · Tham chiếu`, `01 · Frame`, `02 · Takes`, `03 · Chọn dựng`. Gen lại shot/revision vẫn trong project tập; giữ lịch sử take.
- Tải nguồn đã duyệt cần dùng vào đúng project, ghi URL vào `flow_project` hiện có trong `episode.yaml`, tải frame/clip về đúng thư mục tập và giữ ánh xạ/hash. Không thêm trường ngoài schema.
- Giữ nguyên project/tài sản cũ; tập đang làm dở có thể hoàn tất ở project cũ, từ tập tiếp theo dùng project riêng. Không tự di chuyển/xóa tài sản để tổ chức lại. Chi tiết tại `00_docs/production-workflow.md`.
- Đây là quy ước đã duyệt, không phải xác nhận đã tạo project trên UI hay ủy quyền gen video/đăng bài.

### Công thức gen (bắt buộc theo đúng thứ tự)

1. Làm việc trong project Flow riêng của tập theo quy ước trên (ngoại lệ chuyển tiếp cho tập đang làm dở); tài sản Flow **không dùng chung giữa các project** — cần ảnh nào thì tạo/tải ảnh đó ngay trong project.
2. Dựng ảnh master/cảnh **bên trong project** bằng sửa ảnh (Nano Banana): bắt đầu từ ảnh tham chiếu đã duyệt (mặt `thao-my-face-front-v002.png` và tỷ lệ từ `thao-my-body-front-v003.png`, thêm location đã duyệt khi cần), sửa trang phục/bối cảnh/tư thế/biểu cảm theo shot. Sửa ảnh tốn **0 credit**. Kiểm tra cổng: mặt và tóc phải giữ nguyên nhân vật; lệch mặt là dừng, không đốt credit video vào frame đầu hỏng. Tối đa ~3 lượt sửa lấy bản tốt nhất. Flow sửa ảnh tại chỗ: trước khi sửa tiếp, tải và lưu từng frame đã duyệt vào `input/frames/`, ghi SHA-256 và ánh xạ shot trong `episode.yaml`. Không ghi đè frame đã dùng; clip là asset riêng.
3. Gen video bằng **chế độ Frames (Khung hình) trực tiếp, TẮT Agent**: ảnh cảnh làm frame đầu duy nhất, không frame cuối, không đính kèm gì thêm. Đặt: Video, dọc 9:16, 8 giây, đúng 1 output, **Veo 3.1 Lite = 10 credit/clip**.
4. Prompt video NGẮN, chỉ gồm: 1 hành động chính + câu thoại nguyên văn trong dấu “” + hướng giọng (nữ miền Bắc) + các cấm cơ bản (không nhạc, không phụ đề, không chữ, máy tĩnh). Không dùng prompt dài kiểu khóa cảnh.
5. **TUYỆT ĐỐI TRÁNH**: chế độ Ingredients/nhân vật và đường qua Agent trung gian cho ảnh người thật — đã bị từ chối chính sách “video liên quan đến người nổi tiếng” 5/5 lượt tối 2026-11-14 (2 khuôn mặt khác nhau, ảnh tải lên / ảnh sửa trong Flow / nhân vật Flow đều bị). Agent của Flow còn tự đổi model/giá giữa các phiên (Lite 10 ↔ Omni 24) — nếu bị đưa vào bước duyệt plan, hủy và quay lại Frames trực tiếp; không duyệt đường Agent. Mỗi lượt gen chỉ bấm 1 lần theo ủy quyền của người dùng.
6. Credit: tài khoản miễn phí 50 credit/ngày (làm mới hằng ngày; đã dùng hết 50 trong ngày 2026-11-14, làm mới 2026-11-15). Clip tải về ở 720p gốc (720×1280, 24 fps); tùy chọn upscale 1080p/4K bị khóa trên tài khoản này.
7. Flow ở khu vực này ép watermark AI hiển thị trên nội dung — kiểm tra khi xuất bản.

### Nhận diện nhân vật và trang phục theo tập

- Thảo My: mặt/tóc theo `thao-my-face-front-v002.png` mới đã duyệt; tóc nâu tối, mái thưa theo ảnh. Ảnh là chuẩn, không tự đổi sang nâu sáng/mái bằng theo tài liệu cũ. Không tạo lại nhận diện bằng chữ thuần.
- Cập nhật 2026-11-15: trang phục thay đổi theo từng tập, giữ nhất quán trong tập; không mặc định váy đen cho toàn series. ep001–002 đang gen nên giữ bộ hiện tại, không tự đổi take. Từ ep003 xem `wardrobe.md` từng tập; các bộ đề xuất chưa được duyệt. Tập nối cùng buổi/cảnh có thể giữ bộ vì continuity.
- Nơi cung cấp ảnh/link: `02_characters/<nhân-vật>/wardrobe/inbox/` hoặc ngay trong chat. Duyệt bản thử đồ trước gen video. Váy SANJOLI đen giữ là lựa chọn đã dùng của My, không xóa nguồn. Ảnh sản phẩm chỉ tham chiếu trang phục, không tham chiếu người.

### Tự bổ sung bối cảnh bằng Flow — chốt 2026-11-15

- Khi đang chuẩn bị tập/shot được yêu cầu mà thiếu ảnh bối cảnh hoặc frame cảnh, chủ động tạo/sửa ảnh bằng **Google Flow web chính chủ trong Chrome**, ngay trong project của tập (hoặc project cũ theo ngoại lệ chuyển tiếp); không dừng chỉ để hỏi có tạo bối cảnh hay không. Đây là ủy quyền tạo ảnh phục vụ công việc, không phải ủy quyền gen video hoặc đăng bài.
- Dùng sửa ảnh Nano Banana theo quy trình trên; giữ nguồn nhận diện đã duyệt, không tự thay mặt/body, không dùng Agent/Ingredients để gen video. Kiểm tra model/giá trên UI; nếu tạo ảnh phát sinh phí ngoài quy trình 0 credit đã ghi nhận, không tự chấp nhận khoản phí mới.
- Nếu thiếu location trống: tạo ứng viên, lưu bản tải về vào review/ của location, ghi nguồn/project và trạng thái chờ duyệt. Nếu thiếu frame có nhân vật: dựng trong project, tải vào input/frames/ từng tập, giữ phiên bản riêng và ghi SHA-256/ánh xạ shot trong episode.yaml.
- Không tự ghi location/frame approved hoặc bật approved_for_generation chỉ vì đã tạo ảnh. Khi đã có ảnh phù hợp, trình ảnh để duyệt trước gen clip. Không dùng location trống thay frame có nhân vật.
- Nếu không truy cập được Flow, báo rõ trở ngại; không tự chuyển sang công cụ tạo ảnh khác nếu chưa có ủy quyền tương ứng. Hai frame local ep001 tạo bằng imagegen ngày 2026-11-15 theo yêu cầu riêng, không chứng minh đã chạy Flow.

### Cập nhật trang phục ep002 — chốt 2026-11-16

- Người dùng chỉ định ep002 dùng cùng link affiliate ep001 (`aff-0001`, https://s.shopee.vn/5LDVnTeC4f), tham chiếu váy SANJOLI màu kem trong hai ảnh gửi. Xem `05_episodes/ep002-tieu-chuan-co-ban/wardrobe.md`; nguồn giữ tại `02_characters/thao-my/wardrobe/inbox/ep002-sanjoli-kem/`.
- Chỉ định mới áp dụng khi chuẩn bị bản mới ep002, ưu tiên hơn ghi chú giữ bộ cũ. Không ghi đè take cũ; chưa tạo/duyệt ảnh ghép hoặc frame. Ảnh người mẫu chỉ tham chiếu bộ đồ, không thay nhận diện/body Thảo My. Chưa gắn link vào bài.

### Các màu váy cho tập sau ep002 — chốt 2026-11-16

- Người dùng xác nhận các tập sau tiếp tục link `aff-0001` nhưng đổi màu váy; ảnh trắng, xanh dương và hồng giữ tại `02_characters/thao-my/wardrobe/inbox/sanjoli-color-variants/`, README có tên file/hash.
- ep002 vẫn màu kem. Từ ep003 chưa có ánh xạ màu cụ thể; đề xuất trong wardrobe.md rồi phân biệt rõ trạng thái duyệt, không gán thứ tự ảnh thành thứ tự tập. Chỉ định mới ưu tiên hơn đề xuất trang phục cũ khi chuẩn bị bản mới cho Thảo My; giữ lịch sử và continuity tập nối cảnh.
- Ảnh chỉ tham chiếu đồ, không nhận diện/cơ thể/phụ kiện người mẫu. Chưa có frame thử đồ được duyệt hoặc ủy quyền gen video từ việc lưu nguồn.

### Quy tắc tủ đồ — chốt 2026-11-15

- Mỗi tập chọn một bộ riêng phù hợp bối cảnh cho **từng nhân vật**; đa dạng giữa các tập, giữ nguyên bộ/phụ kiện trong các shot cùng tập. Không tự đổi mặt, tóc hoặc vóc dáng khi thay quần áo. Nếu hai tập nối trực tiếp cùng buổi/cảnh, có thể giữ bộ để liền mạch, ví dụ My ở ep004 → ep005.
- Trước khi chuẩn bị frame, đọc `05_episodes/<tập>/wardrobe.md`. Nếu chưa có, lập bản đề xuất trang phục; không tự coi là đã duyệt. Ghi bộ của từng người, nguồn ảnh/link, trạng thái duyệt và ảnh thử đồ/frame tương ứng. ep003–008 đã có bản đề xuất; ep001–002 đang gen giữ bộ hiện tại trừ khi người dùng yêu cầu đổi.
- Người dùng có thể gửi ảnh/link ngay trong chat hoặc bỏ vào `02_characters/thao-my/wardrobe/inbox/` và `02_characters/vy/wardrobe/inbox/`, kèm tập/nhân vật. Lưu nguồn và ánh xạ vào wardrobe.md của tập; không bắt người dùng phải tự thao tác folder. Ảnh người mẫu chỉ tham chiếu bộ đồ, không lấy nhận diện/cơ thể người mẫu thay nhân vật.
- Khi chưa có nguồn người dùng cung cấp, đề xuất bộ bằng mô tả phù hợp nhân vật/bối cảnh. Chỉ tạo ảnh thử đồ/frame khi có yêu cầu tạo ảnh tương ứng; không tự gen chỉ vì đã viết kịch bản hoặc có wardrobe.md. Sửa đồ từ ảnh nhân vật đã duyệt, không tạo lại nhân vật bằng chữ thuần.
- `wardrobe/inbox/` giữ nguồn đầu vào; `wardrobe/review/` giữ ảnh thử đồ chờ duyệt; `wardrobe/approved/` chỉ nhận bản được người dùng duyệt rõ. Gửi ảnh nguồn không đồng nghĩa duyệt frame cuối. Giữ phiên bản riêng, không ghi đè nguồn/master tốt.
- Khi chuyển sang sản xuất, đồng bộ bộ đã chọn vào prompt ảnh, `image_sources` trong episode.yaml và ghi chú manifest theo schema hiện hành; không tự thêm trường ngoài schema. Video vẫn chỉ nhận một frame cảnh đầu đã duyệt. Đổi bộ sau gen phải tăng revision, giữ take cũ và không nhận take cũ là đầu ra bộ mới.

### Âm thanh — quy tắc bắt buộc

- **Giọng native của Veo KHÔNG dùng làm giọng nhân vật**: mỗi lượt gen tự sinh một giọng khác nhau (đã kiểm chứng: 2 shot của ep001 ra 2 giọng, một Bắc một Nam). Prompt chỉ “hướng” giọng, không khóa được.
- Giọng chính thức = **lồng tiếng VieNeu-TTS (nữ, miền Bắc) trên Colab T4**, một giọng duy nhất cho mọi shot/tập; tắt tiếng gốc Veo khi dựng. Hồ sơ `02_characters/thao-my/character.yaml` hiện ghi preset **Đoan Trang**, trạng thái `locked_by_user_2026_11_15`; dùng theo hồ sơ này. Chưa coi là đã có file audio hoặc môi trường Colab sẵn sàng. Khi chuẩn bị dựng, đồng bộ preset vào manifest của tập, không để ghi chú cũ “chưa chốt” ghi đè lựa chọn trong hồ sơ nhân vật.

### Trạng thái ep001 “Dọn bàn”

- Project Flow: https://flow.google.com/u/1/project/2948266f-ba05-481e-b636-4ebe81db52ba
- Lịch sử rev2 (mặt cũ): sh010 bản chốt = bản **bàn bừa thật** (clip `18ecd1fc-0109-48d6-bb72-49808a7a5bfc`): bài học kịch bản đã kiểm chứng — bàn phải bừa nhìn thấy rõ thì thoại “dọn bàn” mới có đất diễn; bản bàn gọn bị người dùng đánh giá là “ảo”. sh020 (clip `9c6adb5e-44d4-4155-9552-c4c1318f869e`): bàn VẪN bừa trong khi nhân vật deadpan nói “Bàn gọn rồi…” — đó là cú chốt thị giác của tập.
- Rev3 ngày 2026-11-15 đã cập nhật mặt mới/body v003; giữ thoại, bàn bừa và váy đen. Chưa gen frame/video mới. Take rev2 giữ ID làm lịch sử, không chọn cho rev3; không tìm thấy hai file clip local tại đường dẫn cũ khi kiểm tra 2026-11-15. Không báo đã có clip local nếu chưa kiểm tra lại.
- Hồ sơ hiện hành: `05_episodes/ep001-don-ban/episode.yaml`; lịch sử rev2 trong `prep/rev2-record/`. Trước gen mới cần duyệt kịch bản/frame và có yêu cầu gen shot cụ thể.

### Ba pilot mới — bản nháp 2026-11-15

- `05_episodes/ep002-tieu-chuan-co-ban/script.md`: phòng khách, tiêu chuẩn người yêu.
- `05_episodes/ep003-sap-toi/script.md`: sân nội khu, chờ tin nhắn “sắp tới”.
- `05_episodes/ep004-hen-ho-dung-gio/script.md`: café hẹn hò, tự tận hưởng cuộc hẹn.
- Mỗi tập 4 shot khoảng 8 giây, dự kiến 32 giây; chỉ có kịch bản để review, chưa duyệt và chưa gen video. Location còn chờ duyệt. Khi chuyển sang sản xuất, dùng `$thao-my-episode` để lập episode.yaml/manifest; không coi bản nháp là hồ sơ đã sẵn sàng generation.

### Quy tắc bối cảnh

- Ảnh location trống là tài nguyên dùng chung; frame có nhân vật thuộc từng shot/tập. Không dùng ảnh location trống thay frame shot có Thảo My.
- Chỉ đưa ảnh location sang `approved/` và cập nhật master trong `location.json` khi người dùng duyệt rõ ảnh. Đồng ý tổ chức folder không phải duyệt location.
- Ảnh/frame mới giữ phiên bản riêng; không ghi đè master tốt. Ảnh source và bối cảnh đã tạo bằng imagegen không tự chứng nhận quy trình Flow. Việc xoá ảnh cũ đã được yêu cầu riêng, không suy rộng thành tự xoá nguồn hoặc tài sản tập khác.

<!-- postman-cli:installation:start -->
Postman CLI is installed on this device, and can be used for API Engineering work.
<!-- postman-cli:installation:end -->

## Cập nhật nhận diện — chốt 2026-11-16

- Người dùng chọn ảnh mới trong chat làm chuẩn cả mặt và tóc v002. Body v003 giữ nguyên vóc dáng; mặt/tóc trong ảnh body gốc không ghi đè chuẩn v002.
- Bản ghép body với mặt/tóc mới ở `02_characters/thao-my/review/body-v003-face-v002/`, chờ duyệt riêng. Giữ bộ gốc và các revision tập cũ. Chưa kiểm chứng tổ hợp mới trong Flow.

- Phản hồi tiếp theo 2026-11-16: giữ thay đổi nhận diện ít vì đã đăng video; ưu tiên tóc dày và đẹp hơn, không tiếp tục chỉnh cấu trúc mặt. Bộ review mới nhất: `02_characters/thao-my/review/body-v003-face-v002/hair-density-r02/`; chưa duyệt.

## Lựa chọn nhận diện cuối 2026-11-16 — ưu tiên hơn ghi chú thử nghiệm trước

- Chuẩn mặt/tóc: `thao-my-face-front-v002.png`; body chính diện: `thao-my-body-front-v003-face-v002-review.png`, đã duyệt rõ trong chat và copy nguyên byte vào approved. Bỏ hướng giữ mặt cũ chỉ làm tóc dày; không chọn hair-density-r02 hoặc face-correction. Hai góc ghép nghiêng/sau chưa duyệt.
- Đã cập nhật kịch bản ep001–008; ep001 chuyển rev5, giữ hồ sơ rev4 tại prep/rev4-record và giữ nguyên nguồn/take/master. Rev5 chưa có frame/clip và chưa duyệt gen.
