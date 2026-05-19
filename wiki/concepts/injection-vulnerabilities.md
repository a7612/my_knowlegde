---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A05 Injection.md", "raw/Mitre/CWE/CWE-94 Improper Control of Generation of Code ('Code Injection') (4.20).md", "raw/Mitre/CWE/CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') (4.20).md"]
tags: ["owasp", "injection", "sql-injection", "xss", "input-validation"]
---

# Lỗi tiêm (Injection)

**Lỗi tiêm** (A05:2025) xảy ra khi dữ liệu người dùng không tin cậy được gửi đến một trình thông dịch (interpreter) như cơ sở dữ liệu, trình duyệt hoặc dòng lệnh, khiến trình thông dịch đó thực thi các phần của dữ liệu đó như một câu lệnh.

## Các loại lỗi tiêm phổ biến

### 1. Tiêm mã (Code Injection - CWE-94)
Xảy ra khi ứng dụng xây dựng một đoạn mã từ dữ liệu đầu vào của người dùng mà không được làm sạch.
*   **Cơ chế**: Kẻ tấn công gửi các cú pháp mã (ví dụ: lệnh PHP, Python) thông qua các kênh dữ liệu thông thường để thay đổi luồng điều khiển của ứng dụng.
*   **Hệ quả**: Thực thi mã tùy ý (RCE), chiếm quyền điều khiển hệ thống, hoặc truy cập tài nguyên bị hạn chế.
*   **Ví dụ**: Sử dụng hàm `eval()` hoặc `include()` trong PHP/Python với dữ liệu trực tiếp từ người dùng.

### 2. Tiêm chủng chéo trang (Cross-Site Scripting - XSS - CWE-79)
Tiêm mã script độc hại vào các trang web mà người dùng khác sẽ xem.
*   **Các biến thể**:
    *   **Reflected XSS**: Mã độc được phản hồi trực tiếp từ yêu cầu HTTP (ví dụ qua tham số URL).
    *   **Stored XSS**: Mã độc được lưu trữ vĩnh viễn trên máy chủ (ví dụ trong cơ sở dữ liệu, diễn đàn).
    *   **DOM-based XSS**: Mã độc được thực thi do thay đổi cấu trúc DOM tại trình duyệt.
*   **Hệ quả**: Đánh cắp Cookie phiên, giả mạo giao diện đăng nhập để chiếm đoạt tài khoản, hoặc thực hiện hành động thay người dùng.

### 3. Các loại khác
*   **SQL Injection**: Tiêm mã SQL để truy cập hoặc sửa đổi dữ liệu trái phép trong DB.
*   **OS Command Injection**: Thực thi lệnh hệ điều hành trực tiếp thông qua ứng dụng. Xem thêm: [[os-command-injection|Tiêm lệnh hệ điều hành]].
*   **Prompt Injection**: Một dạng lỗi tiêm mới liên quan đến các mô hình ngôn ngữ lớn (LLM).

## Tại sao ứng dụng bị lỗi?
- Dữ liệu người dùng không được xác thực, lọc hoặc làm sạch (sanitizing).
- Sử dụng các truy vấn động hoặc gọi hàm không được tham số hóa (non-parameterized calls).
- Ghép chuỗi (concatenation) dữ liệu nhạy cảm trực tiếp vào các câu lệnh hoặc mã nguồn.

## Cách phòng tránh
1.  **Sử dụng Safe API**: Ưu tiên sử dụng các API có tham số hóa (parameterized interface) hoặc công cụ ORM.
2.  **Xác thực đầu vào nghiêm ngặt**: Sử dụng danh sách trắng (allow-list) để chỉ chấp nhận dữ liệu đúng định dạng và quy tắc nghiệp vụ.
3.  **Mã hóa đầu ra (Output Encoding)**: Mã hóa dữ liệu dựa trên ngữ cảnh (HTML body, attributes, JavaScript, CSS) trước khi hiển thị để trình duyệt không thực thi chúng như mã.
4.  **Củng cố môi trường**:
    *   **Sandbox/Jail**: Chạy mã trong môi trường bị cô lập (như Unix chroot, AppArmor) để hạn chế quyền truy cập hệ điều hành.
    *   **Content Security Policy (CSP)**: Sử dụng tiêu đề CSP để hạn chế nguồn tải script.
5.  **Tránh hàm nguy hiểm**: Không sử dụng `eval()`, `exec()`, `system()`. Trong Python, hạn chế cả `ast.literal_eval()` trên dữ liệu không tin cậy nếu có cấu trúc lồng nhau sâu.
6.  **Sử dụng HttpOnly**: Thiết lập cờ HttpOnly cho Cookie để ngăn script truy cập thông tin phiên.

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
