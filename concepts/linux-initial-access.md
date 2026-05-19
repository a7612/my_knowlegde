---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Linux Target - Linux Initial Access.md"]
tags: ["security", "pentest", "linux", "initial-access", "exploitation", "metasploit", "ssh"]
---

# Truy cập ban đầu mục tiêu Linux (Linux Initial Access)

**Truy cập ban đầu (Initial Access)** là bước ngoặt trong quy trình [[my_knowlegde/concepts/penetration-testing|kiểm thử xâm nhập]], khi chuyên gia tận dụng các lỗ hổng đã phát hiện để giành được quyền thực thi lệnh trên hệ thống mục tiêu.

## 1. Khai thác qua WordPress (Metasploit)

Nếu một plugin WordPress (ví dụ: `hash-form` v1.1.0) bị hỏa hổng thực thi mã từ xa (**RCE**), ta có thể sử dụng **Metasploit Framework** để khai thác.

*   **Quy trình thực hiện**:
    1.  Tìm kiếm module: `search wordpress hash form`.
    2.  Cấu hình tham số: `RHOSTS` (IP mục tiêu), `RPORT` (443), `LHOST` (IP máy tấn công), và `SSL true`.
    3.  Thực thi: Lệnh `exploit` sẽ tải lên một tệp tin PHP chứa mã độc (**Payload**) và tạo một kết nối ngược (**Reverse Shell**) về máy tấn công.
*   **Kết quả**: Một phiên làm việc **Meterpreter** được mở ra, cho phép điều khiển hệ thống từ xa dưới quyền người dùng web (thường là `www-data`).

## 2. Truy cập qua SSH (Sử dụng thông tin đã thu thập)

Đây là phương thức truy cập trực tiếp và mạnh mẽ nếu chuyên gia thu thập được thông tin đăng nhập trong giai đoạn trước.

*   **Sử dụng Khóa riêng (Private Key)**:
    *   Lệnh: `ssh -i id_rsa <user>@<IP>`.
    *   Lưu ý: Nếu khóa không có passphrase, ta sẽ đăng nhập được ngay lập tức.
*   **Sử dụng Mật khẩu (Credentials)**:
    *   Lệnh: `ssh <user>@<IP>`.
    *   Mật khẩu có thể tìm thấy trong các tệp lịch sử như `.bash_history` (ví dụ: `john:SuperSecurePass123`).

## 3. Xác nhận truy cập

Sau khi truy cập thành công, chuyên gia cần xác nhận tình trạng của mình bằng các lệnh:
*   `sysinfo`: Xem thông tin hệ điều hành và kiến trúc chip.
*   `id`: Kiểm tra tên người dùng và các nhóm mà người dùng đó tham gia.
*   `pwd`: Xác định thư mục đang làm việc hiện tại.
*   `ifconfig`: Xác định các giao diện mạng nội bộ.

## Liên kết liên quan
- [[my_knowlegde/concepts/linux-information-gathering|Thu thập thông tin (Linux)]]
- [[my_knowlegde/concepts/vulnerability-assessment|Đánh giá lỗ hổng]]
- [[my_knowlegde/concepts/linux-system-enumeration|Liệt kê hệ thống (Linux)]]
- [[my_knowlegde/concepts/penetration-testing|Kiểm thử xâm nhập]]
