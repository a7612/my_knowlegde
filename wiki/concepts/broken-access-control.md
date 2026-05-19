---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A01 Broken Access Control.md"]
tags: ["owasp", "access-control", "authorization", "ssrf", "security-vulnerability"]
---

# Kiểm soát truy cập bị hỏng (Broken Access Control)

**Kiểm soát truy cập bị hỏng** (A01:2025) là rủi ro bảo mật ứng dụng web nghiêm trọng nhất theo OWASP 2025. Nó xảy ra khi các hạn chế đối với những gì người dùng được phép làm không được thực thi đúng cách, cho phép kẻ tấn công truy cập trái phép vào dữ liệu hoặc thực hiện các chức năng nằm ngoài quyền hạn của họ.

## Các lỗi phổ biến
*   **Vi phạm nguyên tắc đặc quyền tối thiểu**: Cấp quyền truy cập cho tất cả mọi người thay vì chỉ những người cần thiết.
*   **Vượt qua kiểm tra kiểm soát truy cập**: Thay đổi URL (tham số, điều hướng trực tiếp), trạng thái ứng dụng nội bộ hoặc sử dụng công cụ tấn công API.
*   **IDOR (Insecure Direct Object References)**: Cho phép xem hoặc chỉnh sửa tài khoản của người khác bằng cách cung cấp định danh duy nhất (ví dụ: `?acct=123`).
*   **Thiếu kiểm soát truy cập API**: Các phương thức POST, PUT, DELETE không được bảo vệ.
*   **Leo thang đặc quyền**: Hành động với tư cách quản trị viên khi chỉ là người dùng thông thường hoặc không cần đăng nhập.
*   **Thao túng siêu dữ liệu**: Giả mạo hoặc thay đổi Token (JWT), Cookie để chiếm quyền.
*   **Cấu hình sai CORS**: Cho phép truy cập API từ các nguồn (origin) không tin cậy.

## Server-Side Request Forgery (SSRF)
Trong phiên bản 2025, SSRF đã được gộp vào danh mục này. Đây là lỗi mà kẻ tấn công có thể ép ứng dụng phía máy chủ gửi các yêu cầu HTTP đến các địa chỉ nội bộ hoặc bên ngoài mà máy chủ đó có quyền truy cập, thường dùng để quét cổng hoặc truy cập các dịch vụ nội bộ không công khai.

## Cách phòng tránh
1.  **Mặc định là từ chối (Deny by Default)**: Chỉ cho phép truy cập khi có quyền cụ thể.
2.  **Thực thi tại phía máy chủ (Server-side)**: Tuyệt đối không tin tưởng vào kiểm tra quyền tại trình duyệt (Client-side).
3.  **Sử dụng cơ chế kiểm soát truy cập tập trung**: Tái sử dụng một cơ chế duy nhất cho toàn bộ ứng dụng.
4.  **Vô hiệu hóa liệt kê thư mục**: Đảm bảo các file nhạy cảm như `.git` không thể truy cập công khai.
5.  **Ghi nhật ký và cảnh báo**: Theo dõi các thất bại trong kiểm soát truy cập để phát hiện tấn công.
6.  **Giới hạn tốc độ (Rate Limiting)**: Ngăn chặn các công cụ tấn công tự động.

## Kịch bản tấn công ví dụ
Kẻ tấn công thay đổi tham số trên URL từ `https://example.com/app/accountInfo?acct=myacct` thành `https://example.com/app/accountInfo?acct=otheracct`. Nếu ứng dụng không kiểm tra quyền sở hữu, kẻ tấn công có thể xem thông tin của bất kỳ ai.

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
- [[network-security|An ninh mạng]]
