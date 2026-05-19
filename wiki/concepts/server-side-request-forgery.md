---
sources: 
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C10 Stop Server Side Request Forgery.md"
tags: ["security", "ssrf", "web-security", "owasp"]
---

# Giả mạo yêu cầu phía máy chủ (Server-Side Request Forgery - SSRF)

**Giả mạo yêu cầu phía máy chủ (SSRF)** là một lỗ hổng bảo mật cho phép kẻ tấn công ép buộc máy chủ thực hiện các yêu cầu HTTP không mong muốn thay mặt cho kẻ tấn công. 

## Cơ chế hoạt động
SSRF xảy ra khi máy chủ nhận một URL hoặc đường dẫn từ người dùng và cố gắng truy xuất nội dung từ URL đó mà không có sự kiểm tra đầy đủ. Kẻ tấn công có thể lừa máy chủ thực hiện các yêu cầu đến:
*   **Dịch vụ nội bộ**: Truy cập các máy chủ trong mạng nội bộ (DMZ) vốn được bảo vệ bởi tường lửa.
*   **Dịch vụ localhost**: Truy cập các dịch vụ đang chạy trên chính máy chủ đó (ví dụ: bảng điều khiển quản trị, API nội bộ không cần xác thực).
*   **Trích xuất siêu dữ liệu (Metadata)**: Trên môi trường đám mây (như AWS, Azure, GCP), SSRF thường được dùng để truy cập dịch vụ siêu dữ liệu của instance (ví dụ: `http://169.254.169.254/`) để lấy mã thông báo (tokens) hoặc thông tin cấu hình nhạy cảm.

## Hệ quả nghiêm trọng
*   **Quét mạng nội bộ**: Kẻ tấn công có thể sử dụng máy chủ bị lỗi để quét các cổng và dịch vụ đang chạy trong mạng nội bộ.
*   **Bỏ qua cơ chế xác thực**: Nhiều dịch vụ nội bộ tin tưởng máy chủ thực hiện yêu cầu mà không yêu cầu thêm bước xác thực nào.
*   **Trích xuất dữ liệu nhạy cảm**: Lấy được các thông tin bí mật, khóa API hoặc mã nguồn.

## Cách phòng tránh

### 1. Xác thực đầu vào (Input Validation)
*   **Danh sách trắng (Allow-list)**: Chỉ cho phép các yêu cầu đến các tên miền hoặc địa chỉ IP đã được định nghĩa trước.
*   **Vô hiệu hóa các giao thức không cần thiết**: Chỉ cho phép `http` và `https`, ngăn chặn các giao thức như `file://`, `gopher://`, `ftp://`.

### 2. Kiểm tra đích đến của yêu cầu
*   Đảm bảo yêu cầu không trỏ đến các địa chỉ IP nội bộ hoặc loopback (như `127.0.0.1`, `192.168.x.x`, `10.x.x.x`).
*   Lưu ý các kỹ thuật vượt qua như sử dụng DNS Rebinding hoặc các định dạng IP khác nhau.

### 3. Phân mảnh mạng (Network Segmentation)
*   Cấu hình tường lửa để giới hạn lưu lượng truy cập ra ngoài từ các máy chủ ứng dụng.
*   Ngăn chặn máy chủ ứng dụng truy cập trực tiếp vào các tài nguyên nội bộ nhạy cảm không liên quan.

### 4. Cấu hình bảo mật trình phân tích (Parser)
Nếu sử dụng XML hoặc các định dạng dữ liệu có khả năng xử lý thực thể bên ngoài, hãy cấu hình trình phân tích an toàn để ngăn chặn XEE (XML External Entity), một biến thể của SSRF.

## Liên kết liên quan
- [[broken-access-control|Kiểm soát truy cập bị hỏng]]
- [[injection-vulnerabilities|Lỗi tiêm (Injection)]]
- [[owasp-proactive-controls|OWASP Proactive Controls]]
