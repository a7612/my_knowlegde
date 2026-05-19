---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A07 Authentication Failures.md"]
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

## Cách phòng tránh
1.  **Xác thực đa yếu tố (MFA)**: Đây là biện pháp hiệu quả nhất để ngăn chặn các cuộc tấn công tự động và sử dụng lại thông tin đăng nhập bị đánh cắp.
2.  **Không sử dụng thông tin mặc định**: Đặc biệt là cho các tài khoản quản trị.
3.  **Kiểm tra mật khẩu yếu**: Đối chiếu mật khẩu mới với danh sách các mật khẩu tệ nhất hoặc dữ liệu đã bị rò rỉ (ví dụ qua API Have I Been Pwned).
4.  **Quản lý phiên an toàn**: Sử dụng trình quản lý phiên tích hợp của máy chủ, tạo ID phiên mới sau khi đăng nhập và thu hồi ngay khi đăng xuất.
5.  **Giới hạn đăng nhập**: Áp dụng giới hạn tốc độ và trì hoãn tăng dần sau các lần đăng nhập thất bại.

## Kịch bản tấn công ví dụ
Kẻ tấn công sử dụng kỹ thuật "Password Spraying" (thử các mật khẩu phổ biến như `MùaXuân2025` trên nhiều tài khoản khác nhau) để tránh bị khóa tài khoản đơn lẻ. Nếu ứng dụng không có MFA, kẻ tấn công dễ dàng xâm nhập vào các tài khoản có mật khẩu dễ đoán.

## Liên kết liên quan
- [[authentication-protocols|Giao thức xác thực]]
- [[cryptographic-failures|Thất bại trong mã hóa]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
