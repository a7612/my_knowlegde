---
sources: ["raw/Mitre/CWE/CWE-78 Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection') (4.20).md"]
tags: ["security", "vulnerability", "injection", "os-command-injection", "cwe-78"]
---

# Tấn công Tiêm lệnh Hệ điều hành (OS Command Injection)

**OS Command Injection** (CWE-78) là một lỗ hổng bảo mật nghiêm trọng xảy ra khi một ứng dụng tạo ra các câu lệnh hệ điều hành (OS commands) bằng cách sử dụng dữ liệu không đáng tin cậy từ người dùng mà không có các biện pháp làm sạch (neutralization) đúng cách. Điều này cho phép kẻ tấn công thay đổi logic của câu lệnh và thực thi các lệnh trái phép trực tiếp trên máy chủ.

## Các biến thể chính

Có hai dạng chính của tấn công tiêm lệnh:

1.  **Tiêm tham số (Argument Injection)**: Ứng dụng dự định chạy một chương trình cố định nhưng nhận tham số từ người dùng. Kẻ tấn công sử dụng các ký tự phân tách lệnh (như `;`, `&&`, `|`) để chạy thêm lệnh của riêng họ.
    *   *Ví dụ*: `system("nslookup " + user_input)`. Nếu người dùng nhập `google.com; rm -rf /`, hệ thống sẽ chạy nslookup rồi xóa toàn bộ dữ liệu.
2.  **Kiểm soát hoàn toàn câu lệnh**: Ứng dụng nhận toàn bộ hoặc phần lớn câu lệnh từ người dùng.
    *   *Ví dụ*: `exec(user_input)`. Kẻ tấn công có thể chạy bất kỳ chương trình nào có sẵn trên hệ thống.

## Tác động và Hệ quả

Lỗ hổng này thường dẫn đến sự thỏa hiệp hoàn toàn của hệ thống:
*   **Mất tính Bảo mật**: Kẻ tấn công có thể đọc các tệp nhạy cảm (như `/etc/passwd` hoặc tệp cấu hình chứa mật khẩu).
*   **Mất tính Toàn vẹn**: Kẻ tấn công có thể sửa đổi hoặc xóa dữ liệu, mã nguồn hoặc tệp hệ thống.
*   **Mất tính Sẵn sàng**: Kẻ tấn công có thể làm sập hệ thống hoặc xóa các dịch vụ quan trọng.
*   **Leo thang đặc quyền**: Nếu ứng dụng chạy với quyền cao (như root hoặc Administrator), mọi lệnh tiêm vào cũng sẽ chạy với quyền đó.

## Các ví dụ điển hình

### 1. PHP (Tiêm tham số)
```php
$userName = $_POST["user"];
$command = 'ls -l /home/' . $userName;
system($command);
```
Kẻ tấn công nhập: `; rm -rf /` -> Lệnh thực thi: `ls -l /home/; rm -rf /`

### 2. Java (Thiếu kiểm tra đầu vào)
```java
String latlonCoords = request.getParameter("coords");
Runtime.getRuntime().exec("cmd.exe /C latlon2utm.exe -" + latlonCoords);
```
Kẻ tấn công nhập: `123 & del C:\*.*` -> Lệnh thực thi sẽ xóa các tệp trên ổ C.

## Biện pháp khắc phục (Mitigation)

Cách tốt nhất là **tránh hoàn toàn** việc gọi các lệnh hệ điều hành từ mã nguồn. Nếu bắt buộc phải dùng, hãy tuân thủ các nguyên tắc sau:

1.  **Sử dụng thư viện thay thế**: Ưu tiên sử dụng các hàm có sẵn trong ngôn ngữ lập trình (ví dụ: dùng `unlink()` trong PHP thay vì gọi lệnh `rm` qua shell).
2.  **Tham số hóa (Parameterization)**: Sử dụng các hàm thực thi nhận mảng tham số thay vì một chuỗi lệnh duy nhất. Các hàm này sẽ tự động xử lý việc trích dẫn (quoting) để ngăn chặn tiêm lệnh.
    *   *Ví dụ*: Trong C, dùng `execve()` thay vì `system()`.
3.  **Kiểm tra đầu vào (Input Validation)**: Sử dụng chiến lược "Allowlist" (danh sách trắng). Chỉ chấp nhận các ký tự an toàn (ví dụ: chỉ cho phép chữ cái và số).
4.  **Hạn chế quyền hạn (Least Privilege)**: Chạy ứng dụng dưới quyền một người dùng bị hạn chế để giảm thiểu thiệt hại nếu bị tấn công thành công.
5.  **Môi trường Sandbox**: Chạy mã trong các môi trường cô lập như Docker, `chroot` jail, AppArmor hoặc SELinux.

## Liên kết liên quan
- [[my_knowlegde/concepts/vulnerability-assessment|Đánh giá lỗ hổng]]
- [[my_knowlegde/concepts/application-security|An ninh ứng dụng]]
- [[my_knowlegde/concepts/penetration-testing|Kiểm thử xâm nhập]]
- [[web-security|An ninh Web]]
