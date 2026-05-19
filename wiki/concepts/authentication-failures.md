---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A07 Authentication Failures.md", "raw/Mitre/CWE/CWE-306 Missing Authentication for Critical Function (4.20).md", "raw/Mitre/CWE/CWE-288 Authentication Bypass Using an Alternate Path or Channel (4.20).md"]
tags: ["owasp", "authentication", "passwords", "mfa", "session-management"]
---

# Thất bại trong xác thực (Authentication Failures)

**Thất bại trong xác thực** (A07:2025) xảy ra khi ứng dụng cho phép kẻ tấn công thỏa hiệp mật khẩu, khóa hoặc token phiên, hoặc giả mạo danh tính của người dùng khác một cách tạm thời hoặc vĩnh viễn.

## Các lỗ hổng thường gặp
*   **Credential Stuffing**: Kẻ tấn công sử dụng danh sách tên người dùng và mật khẩu bị rò rỉ từ các vụ hack khác để thử đăng nhập tự động.
*   **Brute Force**: Tấn công vét cạn mật khẩu khi ứng dụng không có cơ chế chặn hoặc làm chậm.
*   **Mật khẩu yếu/Mặc định**: Cho phép mật khẩu như "admin/admin" hoặc các mật khẩu phổ biến trong top 10,000.
*   **Quản lý phiên (Session) kém**: Để lộ ID phiên trên URL, không thu hồi session sau khi đăng xuất hoặc khi hết thời gian chờ (timeout).
*   **Thiếu MFA**: Không yêu cầu xác thực đa yếu tố cho các tài khoản quan trọng.
*   **Account Enumeration**: Thông báo lỗi cho biết tên người dùng có tồn tại hay không, giúp kẻ tấn công thu thập danh sách tài khoản.

*   **Thiếu xác thực cho chức năng quan trọng (CWE-306)**: Ứng dụng không yêu cầu xác thực cho các chức năng nhạy cảm hoặc tiêu tốn nhiều tài nguyên.
*   **Hệ quả**: Kẻ tấn công có thể thực hiện các hành động quản trị, truy cập dữ liệu nhạy cảm hoặc gây lỗi DoS mà không cần đăng nhập.
*   **Ví dụ**: Một API chuyển tiền hoặc đổi mật khẩu có thể được truy cập trực tiếp qua URL mà không kiểm tra danh tính người dùng.

*   **Vượt qua xác thực qua đường dẫn hoặc kênh thay thế (CWE-288)**: Ứng dụng yêu cầu xác thực ở giao diện chính nhưng lại tồn tại các đường dẫn hoặc kênh phụ không được bảo vệ.
    *   **Cơ chế**: Kẻ tấn công truy cập trực tiếp vào các file hỗ trợ, API ẩn, hoặc sử dụng các phím tắt hệ thống (như ESC, CMD-PWR) để bỏ qua màn hình đăng nhập.
    *   **Ví dụ**: Một ứng dụng web yêu cầu đăng nhập tại `index.php` nhưng lại cho phép truy cập trực tiếp vào `admin_panel.php` hoặc các file cài đặt mà không kiểm tra phiên làm việc.

## Cách phòng tránh
1.  **Chiến lược Điểm kiểm soát duy nhất (Choke Point)**: Tập trung tất cả các yêu cầu truy cập tài nguyên qua một cổng kiểm soát duy nhất để đơn giản hóa việc thực thi chính sách bảo mật. Mọi truy cập phải được kiểm tra quyền hạn tại điểm này.
2.  **Phân vùng phần mềm**: Chia ứng dụng thành các vùng: ẩn danh (anonymous), người dùng thông thường, người dùng có đặc quyền và quản trị viên. Xác định rõ ràng vùng nào cần xác thực tập trung.
3.  **Xác thực đa kênh**: Đảm bảo tất cả các kênh liên lạc (bao gồm cả API, giao diện dòng lệnh, và các cổng assumed là riêng tư) đều được bảo vệ đồng bộ.
4.  **Xác thực phía máy chủ (Server-side)**: Tuyệt đối không tin tưởng vào các kiểm tra thực hiện tại trình duyệt (client-side). Kẻ tấn công có thể dễ dàng sửa đổi hoặc gỡ bỏ các kiểm tra này.
5.  **Xác thực đa yếu tố (MFA)**: Đây là biện pháp hiệu quả nhất để ngăn chặn các cuộc tấn công tự động và sử dụng lại thông tin đăng nhập bị đánh cắp.
6.  **Sử dụng Framework chuẩn**: Tránh tự viết cơ chế xác thực. Hãy sử dụng các thư viện đã được kiểm chứng (như ESAPI, OpenSSL).
7.  **Quản lý phiên an toàn**: Sử dụng trình quản lý phiên tích hợp của máy chủ, tạo ID phiên mới sau khi đăng nhập và thu hồi ngay khi đăng xuất.
8.  **Bảo vệ tài nguyên đám mây**: Cấu hình các bucket (S3, Azure Blob) yêu cầu xác thực mạnh mẽ, không để ở chế độ công khai mặc định.
9.  **Vô hiệu hóa các đường dẫn gỡ lỗi/cài đặt**: Xóa bỏ hoặc khóa các file cài đặt (`install.php`), các trang gỡ lỗi (`debug.php`) sau khi triển khai lên môi trường thực tế.

## Kịch bản tấn công ví dụ
Kẻ tấn công sử dụng kỹ thuật "Password Spraying" (thử các mật khẩu phổ biến như `MùaXuân2025` trên nhiều tài khoản khác nhau) để tránh bị khóa tài khoản đơn lẻ. Nếu ứng dụng không có MFA, kẻ tấn công dễ dàng xâm nhập vào các tài khoản có mật khẩu dễ đoán.

## Liên kết liên quan
- [[authentication-protocols|Giao thức xác thực]]
- [[cryptographic-failures|Thất bại trong mã hóa]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
