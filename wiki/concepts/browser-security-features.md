---
sources: ["raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C8 Leverage Browser Security Features.md"]
tags: ["security", "browser", "hardening", "csp", "hsts", "security-headers"]
---

# Các tính năng bảo mật trình duyệt (Browser Security Features)

Trình duyệt là cổng vào thế giới web của hầu hết người dùng. Việc tận dụng các tính năng bảo mật tích hợp sẵn trong trình duyệt là một biện pháp **Làm cứng (Hardening)** quan trọng để bảo vệ người dùng khỏi các cuộc tấn công phía client.

## Các tiêu đề bảo mật HTTP (Security Headers)

### 1. Chính sách Bảo mật Nội dung (CSP - Content Security Policy)
CSP là một công cụ mạnh mẽ giúp ngăn chặn XSS và tiêm dữ liệu bằng cách giới hạn các nguồn mà trình duyệt được phép tải nội dung (script, style, hình ảnh).
*   **Strict CSP**: Sử dụng `nonces` hoặc `hashes` để chỉ thực thi các đoạn mã script được chỉ định rõ ràng.
*   **Trusted Types**: Một API trình duyệt giúp ngăn chặn DOM XSS bằng cách đảm bảo chỉ các loại dữ liệu an toàn mới được chèn vào DOM.

### 2. HTTP Strict Transport Security (HSTS)
Buộc trình duyệt luôn kết nối với trang web qua HTTPS. Điều này ngăn chặn các cuộc tấn công **SSL Stripping** (hạ cấp từ HTTPS xuống HTTP).

### 3. X-Frame-Options (XFO)
Ngăn chặn các cuộc tấn công **Clickjacking** (UI-redress) bằng cách không cho phép trang web của bạn bị nhúng vào `<iframe>` của các trang web khác.
*   Lưu ý: CSP với chỉ thị `frame-ancestors` là phương pháp hiện đại và linh hoạt hơn để thay thế XFO.

### 4. X-Content-Type-Options
Sử dụng giá trị `nosniff` để buộc trình duyệt tuân thủ đúng loại MIME được máy chủ trả về, ngăn chặn các cuộc tấn công **MIME sniffing** (thực thi file script giả dạng file ảnh).

### 5. Referrer-Policy
Kiểm soát lượng thông tin được gửi đi trong tiêu đề `Referer` khi người dùng chuyển hướng sang trang web khác, giúp ngăn chặn rò rỉ các thông tin nhạy cảm có trong URL.

## Kiểm soát khả năng nâng cao

### 1. Chính sách Quyền (Permission Policy)
Cho phép trang web thông báo với trình duyệt về các tính năng phần cứng không được sử dụng (ví dụ: camera, micro, USB). Ngay cả khi kẻ tấn công tiêm được mã độc, chúng cũng không thể kích hoạt các thiết bị này.

### 2. Bảo vệ Cookie
*   **Secure**: Chỉ gửi cookie qua kết nối mã hóa (HTTPS).
*   **HttpOnly**: Ngăn chặn JavaScript truy cập cookie, giảm thiểu rủi ro bị đánh cắp phiên qua XSS.
*   **SameSite**: Kiểm soát việc gửi cookie trong các yêu cầu chéo trang (Cross-site), giúp chống lại **CSRF**.

## Tầm quan trọng của Cơ chế phòng thủ theo chiều sâu
Các tính năng trình duyệt thường là lớp phòng thủ cuối cùng. Mặc dù chúng phụ thuộc vào sự hỗ trợ của trình duyệt người dùng, việc triển khai chúng giúp tăng đáng kể "chi phí" và độ khó cho kẻ tấn công.

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[injection-vulnerabilities|Lỗi tiêm]]
- [[owasp-proactive-controls|OWASP Proactive Controls]]
