---
sources: 
  - "raw/Mitre/CWE/CWE-59 Improper Link Resolution Before File Access ('Link Following') (4.20).md"
  - "raw/Mitre/CWE/CWE-61 UNIX Symbolic Link (Symlink) Following (4.20).md"
  - "raw/Mitre/CWE/CWE-65 Windows Hard Link (4.20).md"
tags: ["security", "link-following", "symlink", "hard-link", "file-handling"]
---

# Theo dõi liên kết (Link Following)

**Lỗ hổng Theo dõi liên kết (Link Following)** xảy ra khi một ứng dụng truy cập một tệp dựa trên tên tệp, nhưng không ngăn chặn tên tệp đó xác định một liên kết (link) hoặc lối tắt (shortcut) dẫn đến một tài nguyên không mong muốn.

## Các loại liên kết chính

### 1. Liên kết tượng trưng (Symbolic Link / Symlink - CWE-61)
Phổ biến trên hệ điều hành UNIX/Linux. Nếu một chương trình (đặc biệt là chương trình chạy với quyền cao như root) mở một tệp trong thư mục mà người dùng bình thường có quyền ghi, kẻ tấn công có thể thay thế tệp đó bằng một symlink trỏ đến tệp nhạy cảm (ví dụ: `/etc/shadow`).
*   **Hệ quả**: Chương trình sẽ hoạt động trên tệp đích của symlink, dẫn đến việc đọc hoặc ghi đè trái phép dữ liệu nhạy cảm.

### 2. Liên kết cứng (Hard Link - CWE-65)
Chủ yếu đề cập đến các cuộc tấn công trên Windows. Kẻ tấn công có thể thay thế một tệp mà chương trình đặc quyền sử dụng bằng một liên kết cứng trỏ đến tệp hệ thống quan trọng (ví dụ: `AUTOEXEC.BAT`).
*   **Hệ quả**: Kẻ tấn công có thể leo thang đặc quyền hoặc làm hỏng hệ thống khi chương trình đặc quyền thực hiện các thao tác trên liên kết đó.

### 3. Lối tắt Windows (.LNK)
Các tệp .LNK có thể bị lợi dụng để thực thi mã từ xa nếu người dùng bị lừa tải lên hoặc mở một tệp lối tắt độc hại.

## Hệ quả nghiêm trọng
*   **Truy cập trái phép**: Đọc hoặc ghi đè các tệp nằm ngoài phạm vi kiểm soát của ứng dụng.
*   **Leo thang đặc quyền**: Lợi dụng các tiến trình chạy với quyền cao để thay đổi cấu hình hệ thống.
*   **Bỏ qua cơ chế bảo mật**: Nếu tệp liên kết được sử dụng cho một cơ chế bảo mật, kẻ tấn công có thể vượt qua cơ chế đó.

## Cách phòng tránh

### 1. Nguyên tắc đặc quyền tối thiểu
Chạy ứng dụng với quyền hạn thấp nhất cần thiết để giảm thiểu tác động nếu bị khai thác.

### 2. Kiểm tra loại tệp trước khi truy cập
Sử dụng các hàm hệ thống để kiểm tra xem một tệp có phải là liên kết hay không trước khi mở nó (ví dụ: sử dụng `lstat()` thay vì `stat()` trong C).

### 3. Hạn chế quyền ghi trên các thư mục tạm
Các cuộc tấn công link following thường nhắm vào các thư mục tạm (như `/tmp`). Cần đảm bảo quyền truy cập vào các thư mục này được cấu hình an toàn (ví dụ: sử dụng Sticky Bit trên Linux).

### 4. Chuẩn hóa đường dẫn
Sử dụng các hàm chuẩn hóa đường dẫn để giải quyết các liên kết trước khi thực hiện các kiểm tra bảo mật khác.

## Liên kết liên quan
- [[path-traversal|Duyệt đường dẫn (Path Traversal)]]
- [[linux-permissions|Quyền hạn Linux]]
- [[security-misconfiguration|Cấu hình sai bảo mật]]
