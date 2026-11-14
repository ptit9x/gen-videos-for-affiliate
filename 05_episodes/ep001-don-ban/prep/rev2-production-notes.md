# ep001 — Ghi chú sản xuất rev2 (2026-11-14)

Nhật ký sản xuất revision nội dung 2. Hồ sơ dữ liệu hiện hành dùng schema v2 tại `../episode.yaml`; quy trình thao tác chính nằm trong AGENTS.md ở gốc dự án.

## Thay đổi so với rev 1

- **Trang phục**: váy maxi lụa satin đen SANJOLI là trang phục chốt cho cả hai shot — THAY áo thun trắng + quần short be trong prompt rev 1. Tóc/mặt giữ nguyên mẫu gốc (nâu sáng, mái bằng).
- **Đơn vị gen**: mỗi shot = 1 ảnh tĩnh cảnh dựng trong project Flow + 1 prompt chuyển động ngắn (không dùng prompt dài rev 1 để gen video; các khóa cảnh của rev 1 được dùng làm đặc tả dựng ảnh tĩnh).
- **sh010 bản chốt là bản BÀN BỪA THẬT** (không phải bản bàn gọn đã gen trước): người dùng QC bản bàn gọn ngày 2026-11-14 và nhận xét bàn không bừa nên thoại “dọn bàn” nghe “ảo”. Ảnh tĩnh được sửa tại chỗ trong Flow thành bàn bừa rõ rệt (giấy tờ chồng chất, giấy vo viên, 2 cốc, vỏ snack, dây rối, sticky note, sổ kem chôn một nửa dưới giấy); hành động duy nhất vẫn là tay phải kéo/vuốt thẳng cuốn sổ, mọi thứ còn lại giữ nguyên bừa.
- **sh020**: bàn VẪN bừa (không dọn) trong khi nhân vật deadpan nói “Bàn gọn rồi. Đầu óc cũng trống luôn. Mai làm vậy.” — lệch hình/thoại này là cú chốt thị giác đã được người dùng duyệt. Tay đặt yên trên mép bàn, không dọn gì.

## Tài sản đã tạo (project Flow `2948266f-ba05-481e-b636-4ebe81db52ba`)

- Ảnh tĩnh cảnh (asset sửa tại chỗ, ID `40e80eb3-eee1-47ce-86bb-bd0b22be4c13`): phiên bản hiện tại là bản sh020 (bàn bừa + deadpan); các bản trước nằm trong log sửa của cùng asset.
- sh010 bản bàn gọn (bản bị loại về mặt kịch bản, giữ để đối chiếu): clip `8cc9a421-0f47-43ad-a94d-13b9913e474d`.
- **sh010 bản chốt (bàn bừa): clip `18ecd1fc-0109-48d6-bb72-49808a7a5bfc`** — 8s, 720×1280, Veo 3.1 Lite.
- **sh020 bản chốt: clip `9c6adb5e-44d4-4155-9552-c4c1318f869e`** — 8s, 720×1280, Veo 3.1 Lite.
- Hai clip chốt hiện có tại workspace: `../generated/sh010/take002.mp4` và `../generated/sh020/take001.mp4`. Đã kiểm tra tồn tại/hash khi chuyển hồ sơ; chưa QC media. Frame ảnh riêng của từng shot chưa có tại workspace; không tái dựng giả để thay bản gốc.
- Credit: 5 clip đạt × 10 = 50 credit ngày 2026-11-14 (2 clip test + sh010 gọn + sh010 bừa + sh020), số dư cuối ngày 0; lịch làm mới cần kiểm tra lại trên UI.

- Manifest trước khi chuyển cấu trúc ghi mỗi clip chốt dài 7,93s, 720×1280/24 fps. Đây là số liệu đã ghi nhận trước đó, không phải kết quả probe/QC mới của đợt này; thời lượng dựng cuối chưa khóa.

## Âm thanh

- Giọng native Veo của 2 clip chốt KHÔNG khớp nhau (một Bắc, một Nam — người dùng nghe và xác nhận 2026-11-14). Không dùng tiếng gốc khi dựng bản giao.
- Kế hoạch: tắt tiếng Veo, lồng 2 câu thoại bằng **một giọng VieNeu-TTS nữ miền Bắc duy nhất** (chạy Colab T4). Giọng ĐÃ CHỐT ngày 2026-11-15: **VieNeu preset “Đoan Trang”** (nữ, miền Bắc, phong cách tự nhiên) — đã ghi vào `02_characters/thao-my/character.yaml`. Mẫu nghe thử lưu ở máy Muse: `~/workspace/your_files/thaomy-voice-samples/doan-trang-sh010.wav` và `doan-trang-sh020.wav`.

## Chưa làm

- Lồng tiếng + nối hard cut sh010 → sh020 + phụ đề `.srt` + QC theo skill `sitcom-flow-assembly` → bản giao trong `delivery/`.
- Chưa đăng ở bất kỳ kênh nào.
