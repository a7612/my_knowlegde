# GEMINI.md - Quy tắc Quản thủ LLM Wiki (Cấu trúc English - Nội dung Tiếng Việt)

## Mục đích (Purpose)
Xây dựng và duy trì một artifact kiến thức tích lũy bền vững. Hệ thống này không chỉ tìm kiếm tài liệu thô mà thực hiện biên dịch (compilation) thông tin thành một mạng lưới tri thức có cấu trúc bằng tiếng Việt, giúp tri thức tự kết nối và giàu lên theo thời gian.
## Cấu trúc Ba Lớp (Architecture)
* **raw/**: Tài liệu nguồn (PDF, MD, v.v.). Đây là lớp bất biến (immutable).
* **wiki/**: Nơi chứa các file Markdown kiến thức.
* **GEMINI.md**: File cấu hình định nghĩa quy tắc vận hành.
## Quy tắc Ngôn ngữ & Bản địa hóa (Localization)
* **Nội dung 100% Tiếng Việt**: Tất cả các tóm tắt, nội dung chi tiết và phân tích bên trong file phải được viết bằng tiếng Việt chuẩn mực, rõ ràng.
* **Biên dịch tri thức**: Khi đọc nguồn tiếng Anh, AI phải tự động tổng hợp và diễn đạt lại bằng thuật ngữ tiếng Việt tương đương thay vì dịch máy.
## Quy trình Thu nạp (Ingest) - Tối ưu Token
Để tiết kiệm chi phí, AI phải tuân thủ nghiêm ngặt:
* **SHA256 Cache**: Tạo một file .wiki-cache.json để lưu trữ mã băm. Kiểm tra mã băm của file nguồn xem có khớp không; nếu không đổi, tự động bỏ qua để tiết kiệm 100% token.
* **Two-Step Ingest**:
    * *Phân tích*: Đọc nguồn để xác định các thực thể/khái niệm cần cập nhật.
    * *Cập nhật*: Chỉ sửa đổi những trang wiki thực sự bị ảnh hưởng thay vì viết lại toàn bộ thư mục.
* **Manual Batching**: Ưu tiên nạp từng tài liệu một dưới sự giám sát của người dùng để tập trung vào kiến thức quan trọng.
## Quản lý Ngân sách Ngữ cảnh (Query Budget)
Phân bổ token theo tỷ lệ 60/20/5/15:
* **60%**: Ưu tiên nạp thông tin từ các trang wiki liên quan nhất.
* **20%**: Chỉ gửi tối đa 10 tin nhắn gần nhất để duy trì mạch hội thoại.
* **5%**: Luôn đọc index.md trước để điều hướng thay vì nạp toàn bộ wiki.
* **15%**: Dành cho chỉ thị từ file GEMINI.md này.
## Quy tắc Đặt tên & Liên kết (Naming & Wikilinks)
* **Cấu trúc thư mục (English)**: Sử dụng tiếng Anh cho các thư mục cấp cao để đảm bảo tính hệ thống: `wiki/concepts/`, `wiki/entities/`, `wiki/papers/`, `wiki/summaries/`, `wiki/people/`, `wiki/history/`, `wiki/music/`.
* **Tên file (English Slugs)**: Tất cả tên file vật lý phải dùng tiếng Anh, viết thường, không dấu, cách nhau bằng dấu gạch ngang (kebab-case) (ví dụ: `attention-mechanism.md`).
* **Một khái niệm - Một trang**: Đảm bảo mỗi thực thể duy nhất chỉ có một trang. Nếu có tên đồng nghĩa (ví dụ: "AI" và "Trí tuệ nhân tạo"), AI chọn một tên chính và dùng liên kết hoặc chuyển hướng.
* **Liên kết Mask `[[wikilink|mask]]`**:
    * Định dạng: `[[english-slug|Tên hiển thị tiếng Việt]]`
    * Ví dụ: `[[neural-networks|Mạng thần kinh]]`
    * Mục đích: Giúp tên file tương thích tốt với hệ thống nhưng khi hiển thị trong Obsidian vẫn rõ ràng và dễ đọc bằng tiếng Việt.
## Bảo trì (Linting)
Định kỳ quét Wiki để phát hiện:
* **YAML Frontmatter**: Mọi trang phải có metadata chứa sources: [] để truy vết nguồn gốc và tags để lọc.
* Các liên kết bị hỏng (Broken links).
* Các trang "mồ côi" (Orphan pages) không có liên kết trỏ đến.
* Mâu thuẫn kiến thức giữa tài liệu cũ và mới.