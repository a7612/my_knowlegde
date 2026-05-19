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

## Các mô hình Kiểm soát truy cập (Design Patterns)
Việc thiết kế hệ thống kiểm soát truy cập cần được thực hiện kỹ lưỡng ngay từ đầu (Up Front):
*   **Kiểm soát truy cập dựa trên vai trò (RBAC - Role-Based Access Control)**: Gán quyền cho các vai trò thay vì từng người dùng cá nhân. Hạn chế việc "Hard-code" các vai trò trong mã nguồn (ví dụ: tránh dùng `if(user.hasRole("ADMIN"))`).
*   **Kiểm soát truy cập dựa trên thuộc tính (ABAC - Attribute-Based Access Control)**: Cấp quyền dựa trên các thuộc tính của người dùng, đối tượng và môi trường (ví dụ: `if(user.hasPermission("DELETE_ACCOUNT"))`). Đây là mô hình linh hoạt và dễ mở rộng hơn.

## Các nguyên tắc thực thi (Implementation)
1.  **Mặc định là từ chối (Deny by Default)**: Chỉ cho phép truy cập khi có quy tắc cụ thể. Nếu gặp lỗi trong quá trình xử lý quyền, ứng dụng phải từ chối truy cập ngay lập tức.
2.  **Điểm thực thi chính sách (Policy Enforcement Point)**: Đảm bảo mọi yêu cầu truy cập (bao gồm cả API và Webhooks) đều phải đi qua một lớp xác minh tập trung. Tránh việc rải rác các kiểm tra quyền ở nhiều nơi.
3.  **Nguyên tắc đặc quyền tối thiểu (Least Privilege)**: Cấp quyền "vừa đủ" và "đúng lúc" (Just-in-Time - JIT). Tránh sử dụng tài khoản quản trị cho các tác vụ hàng ngày.
4.  **Thực thi tại phía máy chủ (Server-side)**: Tuyệt đối không tin tưởng vào kiểm tra quyền tại trình duyệt (Client-side).
5.  **Củng cố chống SSRF (C10)**:
    *   **Danh sách trắng (Allow-list)**: Chỉ cho phép máy chủ gửi yêu cầu đến các tên miền hoặc IP tin cậy.
    *   **Xác thực đầu vào**: Kiểm tra kỹ các URL do người dùng cung cấp.
    *   **Vô hiệu hóa chuyển hướng**: Ngăn chặn kẻ tấn công lợi dụng việc chuyển hướng HTTP để vượt qua các bộ lọc.

## Server-Side Request Forgery (SSRF)
Trong phiên bản 2025, SSRF đã được gộp vào danh mục này. Đây là lỗi mà kẻ tấn công có thể ép ứng dụng phía máy chủ gửi các yêu cầu HTTP đến các địa chỉ nội bộ hoặc bên ngoài mà máy chủ đó có quyền truy cập, thường dùng để quét cổng hoặc truy cập các dịch vụ nội bộ (như `localhost` hoặc dịch vụ siêu dữ liệu đám mây).

## Cách phòng tránh
- Sử dụng các thư viện hoặc API kiểm soát truy cập tập trung và đã được kiểm chứng.
- Ghi nhật ký tất cả các lần kiểm tra quyền thất bại để phát hiện hành vi dò quét của kẻ tấn công.
- Sử dụng các cờ bảo mật cho Cookie (Secure, HttpOnly, SameSite) để bảo vệ mã định danh phiên.

## Kịch bản tấn công ví dụ
Kẻ tấn công thay đổi tham số trên URL từ `https://example.com/app/accountInfo?acct=myacct` thành `https://example.com/app/accountInfo?acct=otheracct`. Nếu ứng dụng không kiểm tra quyền sở hữu, kẻ tấn công có thể xem thông tin của bất kỳ ai. Đây là lỗi **IDOR** (Insecure Direct Object Reference).

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
- [[owasp-proactive-controls|OWASP Proactive Controls]]

