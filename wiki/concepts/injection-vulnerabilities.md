---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A05 Injection.md"]
tags: ["owasp", "injection", "sql-injection", "xss", "input-validation"]
---

# Lỗi tiêm (Injection)

**Lỗi tiêm** (A05:2025) xảy ra khi dữ liệu người dùng không tin cậy được gửi đến một trình thông dịch (interpreter) như cơ sở dữ liệu, trình duyệt hoặc dòng lệnh, khiến trình thông dịch đó thực thi các phần của dữ liệu đó như một câu lệnh.

## Các loại lỗi tiêm phổ biến
*   **SQL Injection**: Tiêm mã SQL để truy cập hoặc sửa đổi dữ liệu trái phép trong DB.
*   **Cross-Site Scripting (XSS)**: Tiêm mã script (thường là JavaScript) vào trình duyệt của người dùng khác.
*   **OS Command Injection**: Thực thi lệnh hệ điều hành trực tiếp thông qua ứng dụng.
*   **NoSQL Injection**: Tấn công các DB không phải SQL như MongoDB.
*   **Prompt Injection**: Một dạng lỗi tiêm mới liên quan đến các mô hình ngôn ngữ lớn (LLM).

## Tại sao ứng dụng bị lỗi?
- Dữ liệu người dùng không được xác thực, lọc hoặc làm sạch (sanitizing).
- Sử dụng các truy vấn động hoặc gọi hàm không được tham số hóa (non-parameterized calls).
- Ghép chuỗi (concatenation) dữ liệu nhạy cảm trực tiếp vào các câu lệnh.

## Cách phòng tránh
1.  **Sử dụng Safe API**: Ưu tiên sử dụng các API có tham số hóa (parameterized interface) hoặc công cụ ORM để tách biệt hoàn toàn dữ liệu và câu lệnh.
2.  **Xác thực đầu vào phía máy chủ**: Sử dụng danh sách trắng (allow-list) để chỉ chấp nhận dữ liệu đúng định dạng.
3.  **Thoát (Escape) ký tự đặc biệt**: Sử dụng cú pháp thoát cụ thể cho từng loại trình thông dịch nếu không thể dùng tham số hóa.
4.  **Kiểm tra bảo mật tự động**: Tích hợp SAST, DAST và IAST vào pipeline CI/CD để phát hiện lỗi sớm.

## Kịch bản tấn công ví dụ
Ứng dụng xây dựng câu lệnh SQL bằng cách ghép chuỗi:
`"SELECT * FROM accounts WHERE id='" + request.getParameter("id") + "'"`
Kẻ tấn công nhập vào `id` giá trị: `' OR '1'='1`. Câu lệnh trở thành:
`SELECT * FROM accounts WHERE id='' OR '1'='1'`
Kết quả là ứng dụng trả về toàn bộ tài khoản trong cơ sở dữ liệu.

## Liên kết liên quan
- [[os-command-injection|Lỗ hổng Tiêm lệnh hệ điều hành]]
- [[application-security|An ninh ứng dụng]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
