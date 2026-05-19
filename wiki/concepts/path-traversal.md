---
sources: 
  - "raw/Mitre/CWE/CWE-22 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') (4.20).md"
  - "raw/Mitre/CWE/CWE-23 Relative Path Traversal (4.20).md"
  - "raw/Mitre/CWE/CWE-36 Absolute Path Traversal (4.20).md"
tags: ["security", "path-traversal", "directory-traversal", "file-handling", "lfi"]
---

# Lỗ hổng Duyệt đường dẫn (Path Traversal)

**Lỗ hổng Duyệt đường dẫn** (còn gọi là Directory Traversal) xảy ra khi ứng dụng sử dụng dữ liệu đầu vào của người dùng để xây dựng đường dẫn đến một tệp hoặc thư mục mà không làm sạch các ký tự đặc biệt, cho phép kẻ tấn công truy cập vào các tệp nằm ngoài thư mục dự kiến.

## Các biến thể chính

### 1. Duyệt đường dẫn tương đối (Relative Path Traversal - CWE-23)
Kẻ tấn công sử dụng các chuỗi ký tự như `../` (đại diện cho thư mục cha) để thoát ra khỏi thư mục hiện tại. Lỗ hổng này còn được gọi là "Zip Slip" khi xảy ra trong quá trình giải nén các tệp lưu trữ (ZIP, tar, rar) có chứa tên tệp độc hại.
*   **Ví dụ**: Một ứng dụng yêu cầu tệp hồ sơ tại `/users/profiles/alice`. Kẻ tấn công nhập `../../etc/passwd` để yêu cầu tệp mật khẩu hệ thống. Ứng dụng xây dựng đường dẫn `/users/profiles/../../etc/passwd`, hệ điều hành sẽ giải quyết thành `/etc/passwd`.

### 2. Duyệt đường dẫn tuyệt đối (Absolute Path Traversal - CWE-36)
Kẻ tấn công cung cấp một đường dẫn đầy đủ từ gốc (root) của hệ thống hoặc sử dụng ký tự đặc biệt để bỏ qua thư mục hạn chế.
*   **Ví dụ**: Thay vì cung cấp tên tệp, kẻ tấn công nhập trực tiếp `/etc/passwd` hoặc sử dụng định dạng UNC (như `\\computername\sharename` trên Windows) để truy cập tài nguyên mạng.

## Hệ quả nghiêm trọng
*   **Mất tính bảo mật**: Đọc các tệp cấu hình chứa thông tin nhạy cảm, mật khẩu hoặc mã nguồn ứng dụng.
*   **Mất tính toàn vẹn**: Ghi đè hoặc tạo mới các tệp quan trọng (thư viện, file thực thi) để thực thi mã độc hoặc thay đổi hành vi hệ thống.
*   **Mất tính sẵn sàng**: Xóa hoặc làm hỏng các tệp thiết yếu khiến hệ thống ngừng hoạt động (DoS).

## Cách phòng tránh

### 1. Chuẩn hóa đường dẫn (Path Canonicalization)
Trước khi sử dụng đường dẫn, hãy chuyển đổi nó về dạng chuẩn mực (canonical form) để loại bỏ các chuỗi `../`, `..\\` hoặc các liên kết tượng trưng (symlinks).
*   Sử dụng hàm tích hợp: `realpath()` (C/PHP), `getCanonicalPath()` (Java), `os.path.normpath()` (Python).

### 2. Xác thực đầu vào (Input Validation)
*   **Danh sách trắng (Allow-list)**: Chỉ chấp nhận các tên tệp hoặc đường dẫn đã được định nghĩa trước.
*   **Bản đồ định danh (Mapping)**: Thay vì nhận tên file trực tiếp, hãy nhận một ID số và tra cứu trong cơ sở dữ liệu.
*   **Chỉ cho phép ký tự an toàn**: Chỉ chấp nhận chữ cái và số, từ chối bất kỳ dữ liệu nào chứa `/`, `\` hoặc `..`.

### 3. Làm cứng môi trường
*   **Nguyên tắc đặc quyền tối thiểu**: Chạy ứng dụng với tài khoản có quyền hạn thấp nhất.
*   **Chroot Jail / Sandbox**: Sử dụng các cơ chế cô lập của hệ điều hành để giới hạn phạm vi truy cập file.

### 4. Tường lửa ứng dụng (WAF)
Sử dụng WAF có khả năng phát hiện các mẫu tấn công duyệt đường dẫn phổ biến.

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[broken-access-control|Kiểm soát truy cập bị hỏng]]
- [[link-following|Theo dõi liên kết (Link Following)]]

