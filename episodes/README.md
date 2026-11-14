# Quản lý từng tập

Copy `templates/episode/` thành `episodes/ep001-ten-tap/`. Dùng tên không dấu, không khoảng trắng; ID tập `ep001`, ID shot `sh010`, `sh020` để dễ chèn cảnh. Không quét `templates/` để tạo video.

- `script.md`: ý tưởng, thoại, storyboard và lý do sáng tạo để review.
- `episode.yaml`: ID, revision, trạng thái biên tập, thứ tự shot, canvas và mục tiêu dựng.
- `input/shots.json`: nguồn dữ liệu cho automation; thứ tự mảng shots là thứ tự yêu cầu tạo. Phải khớp storyboard và `episode.yaml`.
- `input/prompts/`: prompt tự đủ nội dung, mỗi shot một file; không yêu cầu runner bóc Markdown.
- `input/references/`: bản sao ảnh đơn đã duyệt, khóa theo revision. Giữ nguyên tên PNG theo `characters/thao-my/references.json`; kịch bản và shots.json dùng cùng tên. Không tham chiếu ngược ra thư viện dùng chung trong gói gửi Flow.
- `generated/<shot-id>/take001.mp4`: clip gốc tải về, không ghi đè. Không coi file tải dở là clip hoàn tất.
- `edit/manifest.yaml`: take đã chọn, trim, audio, thời lượng khóa và lệnh dựng. `edit/subtitles.srt` tạo sau khi khóa bản dựng.
- `delivery/`: master và báo cáo QC thực tế.

Trạng thái biên tập: draft → script_approved → generating → editing → qc → ready_to_publish → published. Trạng thái mỗi job nằm riêng trong `runs/`, không dùng trạng thái tập để suy ra một yêu cầu đã được Flow nhận.

Khi sửa prompt, ảnh hoặc thông số tạo sau lần chạy đầu, tăng revision và cập nhật checksum; giữ snapshot lần chạy cũ. Không sửa input giữa lúc runner đang dùng nó. Dùng lock ở cấp episode/revision để tránh hai runner cùng gửi job.

Chọn take trong manifest; tuyệt đối không đổi tên một take mới thành take cũ để thay ngầm. Chỉ đăng khi có yêu cầu cụ thể của người dùng.
