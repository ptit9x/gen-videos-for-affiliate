# Hướng dẫn làm việc trong dự án

## Mục tiêu và giao tiếp

- Đây là workspace sản xuất video sitcom AI ngắn hướng tới affiliate, hiện ở giai đoạn thử nghiệm cho Page “Chuyện Nhà Thảo My”. Chưa có runner tạo video; validator gói đầu vào nằm trong `automation/`.
- Trao đổi, viết kịch bản và báo cáo bằng tiếng Việt. Prompt tạo hình/video có thể dùng tiếng Anh; lời thoại giữ tiếng Việt có dấu.
- Ưu tiên hoàn thành đầu việc đã được yêu cầu. Phân biệt rõ đề xuất, nội dung đã chốt và kết quả đã kiểm chứng; không tự biến gợi ý trong tài liệu thành quyết định của chủ dự án.

## Kênh chính thức

- Tên kênh/Page: **Chuyện Nhà Thảo My**.
- Facebook: https://www.facebook.com/chuyennhathaomy
- TikTok: https://www.tiktok.com/@chuyennhathaomy
- Người dùng xác nhận đã làm video giới thiệu/công bố Thảo My là AI và cung cấp link Facebook: https://www.facebook.com/share/r/18EVd1BLCM/. Không đề xuất làm lại như một đầu việc chưa hoàn thành. Chưa review nội dung video; chưa có thông tin video này đã đăng TikTok.
- Người dùng xác nhận đã tạo hai kênh trên ngày 2026-11-14. Dùng đúng các URL này khi chuẩn bị caption, lịch đăng và tài liệu bàn giao. Nhân vật chính là **Thảo My**, theo xác nhận bổ sung của người dùng cùng ngày.

## Bản đồ tài liệu

- `docs/README.md`: mục lục và phân biệt nghiên cứu với kế hoạch hiện hành. `docs/production-plan.md` là lộ trình đề xuất mới, chưa phải toàn bộ quyết định đã duyệt.
- `docs/research/01-ke-hoach-san-xuat-pilot.md`: production bible đề xuất, hồ sơ Vy/Minh/Quân và ba pilot.
- `docs/research/02-toi-uu-thoai-flow-8s.md`: điều chỉnh từ thử nghiệm Flow thực tế; áp dụng khi chuyển kịch bản pilot cũ thành clip sản xuất.
- `docs/research/03-tan-suat-dang-video.md`: kế hoạch thử nghiệm lịch đăng và đo lường.
- `characters/thao-my/`: `source/` chứa ảnh nguồn, `prompts/` chứa prompt tham chiếu và `approved/` dành cho ảnh đơn đã duyệt của Thảo My; chưa có bộ nhân vật khác. Đã chọn tạo hình từ `facial-expressions-38847112.jpg` và `multi-angle-reference-75f1ee34.jpg`; đã tách 21 ảnh đơn, chưa chốt master/kiểm chứng Flow. `brand/avatar.png` và `brand/banner.png` đang dùng trên kênh, là nhận diện tạm và không phải ảnh master nhân vật.
- `episodes/`: kịch bản, input, generated, edit và delivery theo từng tập. `templates/episode/` là mẫu nháp. `automation/README.md` quy định gói đưa vào Flow; `runs/` giữ nhật ký và trạng thái, không chứa secret.
- `/Users/richard/.codex/skills/sitcom-flow-assembly/SKILL.md`: quy trình hậu kỳ chi tiết; đọc trước khi dựng, xử lý âm thanh hoặc giao video. `SOURCES.md` trong cùng thư mục skill ghi nguồn; `scripts/` chứa công cụ QC. Gọi skill bằng `$sitcom-flow-assembly`.

## Bảo toàn nguồn và quyết định

- Các tài liệu trong `docs/research/` là bản lưu hội thoại có nguồn. Giữ nguyên nội dung và thông tin xuất xứ; viết bản biên tập/kịch bản mới thành file riêng, trừ khi người dùng yêu cầu sửa bản lưu.
- Vóc dáng định hướng đã được người dùng đồng ý: nữ trưởng thành, cao khoảng 169 cm, đồng hồ cát nhẹ, eo rõ hơn, ngực/hông đầy đặn vừa phải, chân dài cân đối; giữ khuôn mặt và tóc. Bộ ảnh body v002 là bản chỉnh để review, chưa mặc định đã duyệt đầu ra; không trộn v001/v002 trong cùng tập.
- Tên nhân vật hiện hành là **Thảo My**. “Vy”, “Minh”, “Quân” trong bản nghiên cứu cũ không phải dàn nhân vật đã triển khai; nội dung mới dùng Thảo My, ưu tiên solo cho giai đoạn thử nghiệm. Tạo hình trong hai sheet đã được người dùng chọn; đã tách 21 ảnh đơn trong `approved/`, chưa chốt master hoặc thử Flow, giọng chưa chốt.
- Khi viết nội dung mới, ghi rõ tên đang dùng, phiên bản và các điểm cần chốt. Chỉ hỏi những điểm thực sự chặn công việc; tiếp tục các phần độc lập.
- Lịch đăng, giờ đăng và mục tiêu số lượng trong tài liệu là giả thuyết thử nghiệm. Mốc “14 ngày chưa affiliate” chỉ là gợi ý cũ, không phải ràng buộc đã chốt. Thử nội dung có ngữ cảnh sản phẩm từ sớm; chỉ bật affiliate khi có quyền phù hợp, sản phẩm và tư liệu xác thực. Không tự đăng bài.

## Kịch bản và Google Flow

- Định hướng: người thật điện ảnh, hài đời sống/cà khịa bằng lời thoại và diễn xuất, mỗi tập khoảng 25–40 giây, khung dọc 9:16.
- Thiết kế mỗi clip Flow khoảng 8 giây như một đơn vị độc lập: một người nói, một câu ngắn trọn ý, một hành động chính. Ngân sách khoảng 12–18 từ tiếng Việt; câu có khoảng nghỉ hoặc nhấn hài cần ngắn hơn. Nếu quá dài, tách clip thay vì ép tốc độ nói.
- Cấu trúc tham khảo: Hook → Tình huống → Cà khịa → Chốt hài. Cho phép clip phản ứng không thoại; không bắt buộc kéo dài tập chỉ để đủ cấu trúc.
- Mỗi clip ghi rõ người nói, thoại, hành động, góc máy, ảnh tham chiếu và thời lượng dự kiến. Dùng đúng tên file PNG trong `characters/thao-my/README.md`/`references.json`; giữ nguyên basename khi copy vào `input/references/` và khai báo trong `shots.json`.
- Giữ nhất quán khuôn mặt, tóc, trang phục, phụ kiện, giọng và bối cảnh trong tập. Dùng ảnh master đã duyệt, tách từng góc phù hợp; không đưa bảng nhiều góc làm ảnh tham chiếu mặc định, không tạo lại nhân vật chỉ bằng mô tả chữ cho từng cảnh.
- Theo thử nghiệm người dùng ngày 2026-11-14, Flow từ chối hai sheet nhiều mặt và chỉ nhận tối đa 3 ảnh input. Mỗi ảnh đưa vào phải là một khung ảnh đơn của cùng Thảo My; chọn ảnh theo từng shot, không bắt buộc dùng đủ 3. Không tạo nhân vật khác để thay thế tạo hình đã chọn.
- Ưu tiên góc đơn và cắt qua lại giữa người nói. Chữ trên điện thoại/đồ họa nên thêm ở hậu kỳ.
- Người dùng đã chọn hướng chuẩn bị dữ liệu cho automation Google Flow. Tuân theo `automation/README.md`; runner chưa được tích hợp. Không suy diễn rằng công cụ cụ thể đã hoạt động. Chỉ gửi tập/revision đã sẵn sàng theo yêu cầu chạy; không lưu cookie, mật khẩu hoặc session trong workspace. Không đăng bài chỉ vì đã tạo xong clip.

## Hậu kỳ và tổ chức đầu ra

- Giữ nguyên ảnh/clip nguồn. Đặt đầu ra từng tập trong thư mục riêng với tên rõ ràng; không di chuyển, đổi tên hoặc ghi đè hàng loạt tài nguyên hiện có nếu không cần cho yêu cầu.
- Lưu `episodes/<episode>/edit/manifest.yaml`: thứ tự cảnh, file nguồn ↔ thoại ↔ prompt, ảnh/giọng tham chiếu, cách xử lý âm thanh, thời lượng đã khóa và thông số xuất. Lưu lệnh dựng trong manifest; lấy clip từ `generated/`, render tạm vào `edit/` và giao bản đạt QC trong `delivery/`.
- Mặc định xuất 1080×1920, 30 fps, H.264, `yuv420p`, âm thanh AAC 48 kHz. Kiểm tra clip bằng `ffprobe` và chuẩn hóa trước khi ghép; xử lý tỷ lệ khung hình có chủ đích để tránh méo hình.
- Ưu tiên hard cut trong hội thoại. Tính lại tổng thời lượng khi thêm chuyển cảnh chồng lấn; xem quy tắc concat/xfade trong skill hậu kỳ.
- Nghe kiểm tra âm thanh từng clip, quyết định phần giữ/bỏ/thay. Nếu cần TTS mà chưa có giọng được chốt, lấy lựa chọn của người dùng trước khi render bản có giọng đó.
- Phụ đề lấy từ kịch bản, đối chiếu lời nói thực tế và canh theo bản dựng cuối. Mặc định giao `.srt` UTF-8 riêng, tối đa hai dòng/cue, không chồng thời gian hoặc vượt độ dài video; chỉ burn-in khi được yêu cầu.
- Render ra file tạm, kiểm tra xong mới thay file giao. Không ghi đè bản master tốt duy nhất trước khi bản thay thế đạt QC.

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

<!-- postman-cli:installation:start -->
Postman CLI is installed on this device, and can be used for API Engineering work.
<!-- postman-cli:installation:end -->
