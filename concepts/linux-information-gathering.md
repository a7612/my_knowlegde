---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Linux Target - Linux Information Gathering.md"]
tags: ["security", "pentest", "linux", "information-gathering", "ftp", "wordpress", "wpscan"]
---

# Thu thập thông tin mục tiêu Linux (Linux Information Gathering)

Sau bước quét mạng ban đầu, chuyên gia cần đi sâu vào việc thu thập thông tin chi tiết về các dịch vụ đang chạy trên mục tiêu Linux để xác định các lỗ hổng cụ thể.

## 1. Khai thác dịch vụ FTP (Cổng 21)

Dịch vụ FTP nếu cấu hình sai (cho phép truy cập ẩn danh) có thể là một mỏ vàng thông tin.

*   **Truy cập ẩn danh**: Sử dụng lệnh `ftp <IP>` với tên người dùng `anonymous` và mật khẩu bất kỳ.
*   **Các tệp tin nhạy cảm thường tìm thấy**:
    *   `WordPress_Blog_Setup_Update.txt`: Có thể chứa tên nhân viên (ví dụ: John Doe), thông tin dự án hoặc thông báo về các thiết lập tạm thời.
    *   `.bash_history`: Lịch sử câu lệnh của người dùng, có thể lộ mật khẩu hoặc các tệp tin cấu hình quan trọng.
    *   `.ssh/id_rsa`: Khóa riêng SSH (Private Key), cho phép đăng nhập từ xa mà không cần mật khẩu nếu không được bảo vệ bằng passphrase.
*   **Lệnh hữu ích**:
    *   `ls -al`: Liệt kê tất cả tệp tin, bao gồm cả tệp ẩn (bắt đầu bằng dấu chấm).
    *   `get <filename>`: Tải tệp tin về máy tấn công.

## 2. Kiểm tra WordPress (Cổng 80/443)

WordPress là hệ quản trị nội dung (CMS) phổ biến và thường là mục tiêu tấn công thông qua các plugin lỗi thời.

*   **Công cụ sử dụng**: **WPScan**
    *   Lệnh quét cơ bản: `wpscan --url https://<IP> -e p` (liệt kê các plugin).
*   **Các thông tin quan trọng thu thập được**:
    *   Phiên bản WordPress (ví dụ: 6.7.2).
    *   Các plugin đang sử dụng (ví dụ: `hash-form` phiên bản 1.1.0).
    *   Người dùng hệ thống (Username enumeration).
    *   Tệp `xmlrpc.php` có được bật hay không (có thể dùng để brute-force hoặc tấn công DDoS).

## 3. Phân tích dữ liệu thu thập

Việc thu thập thông tin và đánh giá lỗ hổng thường diễn ra song song:
*   Nếu tìm thấy khóa SSH -> Kiểm tra xem có thể dùng để đăng nhập hay không.
*   Nếu tìm thấy phiên bản plugin lỗi thời -> Tìm kiếm mã khai thác (Exploit) trên Metasploit hoặc Exploit-DB.

## Liên kết liên quan
- [[my_knowlegde/concepts/information-gathering|Thu thập thông tin (Tổng quan)]]
- [[my_knowlegde/concepts/network-scanning|Quét mạng và dịch vụ]]
- [[my_knowlegde/concepts/linux-initial-access|Truy cập ban đầu (Linux)]]
- [[my_knowlegde/concepts/penetration-testing|Kiểm thử xâm nhập]]
