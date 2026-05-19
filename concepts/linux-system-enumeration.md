---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Linux Target - Linux System Enumeration.md"]
tags: ["security", "pentest", "linux", "post-exploitation", "enumeration", "linpeas", "privilege-escalation"]
---

# Liệt kê hệ thống Linux (Linux System Enumeration)

**Liệt kê hệ thống (System Enumeration)** là quá trình thu thập thông tin chi tiết từ bên trong hệ thống sau khi đã giành được [[my_knowlegde/concepts/linux-initial-access|truy cập ban đầu]]. Đây là bước nền tảng của giai đoạn **Hậu khai thác (Post-Exploitation)**.

## Phân biệt Khai thác và Hậu khai thác

*   **Khai thác (Exploitation)**: Tấn công từ bên ngoài vào các dịch vụ công khai.
*   **Hậu khai thác (Post-Exploitation)**: Khai thác từ bên trong để lấy thông tin nhạy cảm hoặc leo thang đặc quyền.

## Các thông tin cần thu thập

Để hiểu rõ mục tiêu và tìm đường leo thang lên quyền `root`, chuyên gia cần biết:
1.  **Thông tin hệ thống**: Phiên bản OS, phiên bản Kernel, kiến trúc chip.
2.  **Thông tin người dùng**: Người dùng hiện tại có quyền gì? Có bao nhiêu người dùng khác? Có quyền `sudo` không?
3.  **Mạng nội bộ**: Các giao diện mạng, bảng định tuyến, các kết nối đang hoạt động.
4.  **Dịch vụ đang chạy**: Các tiến trình ẩn, các cổng đang lắng nghe nội bộ, các tác vụ lập lịch (cron jobs).
5.  **Hệ thống tệp tin**: Các tệp tin có quyền hạn bất thường (SUID/SGID), các ổ đĩa chưa mount.
6.  **Cơ chế bảo mật**: Trạng thái tường lửa, AppArmor, SELinux hoặc ASLR.

## Công cụ tự động: LinPEAS

**LinPEAS (Linux Privilege Escalation Awesome Script)** là công cụ phổ biến nhất để tự động hóa quá trình liệt kê.

*   **Cách sử dụng**:
    1.  Tải script về máy tấn công.
    2.  Chuyển lên máy mục tiêu qua SSH: `scp -i id_rsa linpeas.sh <user>@<IP>:/tmp`.
    3.  Thực thi: `bash linpeas.sh -a > results.txt`.
*   **Giải thích màu sắc kết quả**:
    *   <span style="color:red">**Màu đỏ (Red)**</span>: Các vector có khả năng leo thang đặc quyền cực cao (99%).
    *   <span style="color:orange">**Màu vàng (Yellow)**</span>: Các điểm yếu cần được phân tích thêm.
    *   **Màu xanh (Green)**: Thông tin chung hữu ích cho việc liệt kê thủ công.

## Liên kết liên quan
- [[my_knowlegde/concepts/linux-initial-access|Truy cập ban đầu (Linux)]]
- [[my_knowlegde/concepts/linux-vulnerability-assessment|Đánh giá lỗ hổng (Linux)]]
- [[my_knowlegde/concepts/linux-privilege-escalation|Leo thang đặc quyền (Linux)]]
- [[my_knowlegde/concepts/penetration-testing|Kiểm thử xâm nhập]]
