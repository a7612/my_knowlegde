---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Linux Target - Linux Privilege Escalation.md"]
tags: ["security", "pentest", "linux", "privilege-escalation", "sudo", "gtfobins", "nano"]
---

# Leo thang đặc quyền Linux (Linux Privilege Escalation)

**Leo thang đặc quyền (Privilege Escalation)** là mục tiêu cuối cùng của việc khai thác cục bộ, nhằm biến quyền người dùng bị hạn chế thành quyền quản trị cao nhất (**root**).

## 1. Khai thác Sudo và GTFObins

Dự án **GTFObins** liệt kê các tệp tin thực thi (binaries) có thể bị lợi dụng để vượt qua các hạn chế bảo mật. Một ví dụ điển hình là trình chỉnh sửa văn bản `nano`.

*   **Tình huống**: Người dùng được phép chạy `sudo nano` mà không cần mật khẩu.
*   **Kỹ thuật khai thác**:
    1.  Mở trình chỉnh sửa: `sudo /usr/bin/nano`.
    2.  Bấm tổ hợp phím `^R` (Read File) rồi `^X` (Execute Command).
    3.  Nhập lệnh để mở shell: `reset; /bin/bash 1>&0 2>&0`.
*   **Kết quả**: Hệ thống sẽ mở một shell mới dưới quyền **root**.

## 2. Sử dụng quyền Sudo trực tiếp

Nếu chuyên gia đã thu thập được mật khẩu của người dùng (ví dụ: qua `.bash_history` hoặc tấn công vét cạn), việc leo thang có thể thực hiện đơn giản bằng lệnh:

```bash
sudo su
# Nhập mật khẩu người dùng
```

## 3. Các vector leo thang khác (Tóm tắt)

*   **Kernel Exploits**: Khai thác các lỗi trong nhân hệ điều hành (ví dụ: DirtyPipe).
*   **SUID/SGID Binaries**: Các tệp tin chạy với quyền của chủ sở hữu tệp thay vì người dùng thực thi.
*   **Cron Jobs**: Các tác vụ lập lịch chạy dưới quyền root nhưng có tệp tin thực thi mà người dùng thường có thể sửa đổi.
*   **Lưu trữ mật khẩu**: Tìm kiếm mật khẩu trong các tệp cấu hình ứng dụng hoặc biến môi trường.

## Liên kết liên quan
- [[linux-vulnerability-assessment|Đánh giá lỗ hổng (Linux)]]
- [[linux-pillaging|Vét cạn thông tin (Linux)]]
- [[penetration-testing|Kiểm thử xâm nhập]]
