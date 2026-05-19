---
sources: ["raw/Mitre/CWE/CWE-22 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') (4.20).md"]
tags: ["security", "path-traversal", "directory-traversal", "file-handling", "lfi"]
---

# Lỗ hổng Duyệt đường dẫn (Path Traversal)

**Lỗ hổng Duyệt đường dẫn** (còn gọi là Directory Traversal - CWE-22) xảy ra khi ứng dụng sử dụng dữ liệu đầu vào của người dùng để xây dựng đường dẫn đến một tệp hoặc thư mục mà không làm sạch các ký tự đặc biệt, cho phép kẻ tấn công truy cập vào các tệp nằm ngoài thư mục dự kiến.

## Các biến thể chính

### 1. Duyệt đường dẫn tương đối (Relative Path Traversal)
Kẻ tấn công sử dụng các chuỗi ký tự như `../` (đại diện cho thư mục cha) để thoát ra khỏi thư mục hiện tại.
*   **Ví dụ**: Một ứng dụng yêu cầu tệp hồ sơ tại `/users/profiles/alice`. Kẻ tấn công nhập `../../etc/passwd` để yêu cầu tệp mật khẩu hệ thống. Ứng dụng xây dựng đường dẫn `/users/profiles/../../etc/passwd`, hệ điều hành sẽ giải quyết thành `/etc/passwd`.

### 2. Duyệt đường dẫn tuyệt đối (Absolute Path Traversal)
Kẻ tấn công cung cấp một đường dẫn đầy đủ từ gốc (root) của hệ thống.
*   **Ví dụ**: Thay vì cung cấp tên tệp, kẻ tấn công nhập trực tiếp `/var/www/config.php`.

## Hệ quả nghiêm trọng
*   **Mất tính bảo mật**: Đọc các tệp cấu hình chứa thông tin nhạy cảm, mật khẩu hoặc mã nguồn ứng dụng.
*   **Mất tính toàn vẹn**: Ghi đè lên các tệp quan trọng (thư viện, file thực thi) để thực thi mã độc hoặc thay đổi hành vi hệ thống.
*   **Mất tính sẵn sàng**: Xóa hoặc làm hỏng các tệp thiết yếu khiến hệ thống ngừng hoạt động (DoS).

## Cách phòng tránh

### 1. Chuẩn hóa đường dẫn (Path Canonicalization)
Trước khi sử dụng đường dẫn, hãy chuyển đổi nó về dạng chuẩn mực (canonical form) để loại bỏ các chuỗi `../` hoặc liên kết tượng trưng (symlinks).
*   Sử dụng hàm tích hợp: `realpath()` (C/PHP), `getCanonicalPath()` (Java), `os.path.normpath()` (Python).

### 2. Xác thực đầu vào (Input Validation)
*   **Danh sách trắng (Allow-list)**: Chỉ chấp nhận các tên tệp hoặc đường dẫn đã được định nghĩa trước.
*   **Bản đồ định danh (Mapping)**: Thay vì nhận tên file trực tiếp, hãy nhận một ID số (ví dụ: ID 1 tương ứng với `profile.txt`) và tra cứu trong cơ sở dữ liệu.
*   **Chỉ cho phép ký tự an toàn**: Chỉ chấp nhận chữ cái và số, từ chối bất kỳ dữ liệu nào chứa `/`, `\` hoặc `..`.

### 3. Làm cứng môi trường
*   **Nguyên tắc đặc quyền tối thiểu**: Chạy ứng dụng với tài khoản có quyền hạn thấp nhất, chỉ được phép đọc/ghi trong các thư mục cụ thể.
*   **Chroot Jail / Sandbox**: Sử dụng các cơ chế cô lập của hệ điều hành (như chroot trên Unix, AppArmor, SELinux) để giới hạn phạm vi truy cập file của tiến trình.

### 4. Xử lý lỗi an toàn
Đảm bảo thông báo lỗi không tiết lộ đường dẫn thực tế của hệ thống, điều này giúp kẻ tấn công khó khăn hơn trong việc trinh sát sơ đồ thư mục.

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[broken-access-control|Kiểm soát truy cập bị hỏng]]
- [[memory-safety-vulnerabilities|Lỗ hổng an toàn bộ nhớ]]
