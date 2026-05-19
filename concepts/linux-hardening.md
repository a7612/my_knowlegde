---
sources:
  - "Hack The Box Academy - Linux Fundamentals - Linux Security"
tags:
  - "linux"
  - "security"
  - "hardening"
---

# Tăng cường Bảo mật Linux (Linux Hardening)

Bảo mật Linux là một quá trình liên tục nhằm giảm thiểu bề mặt tấn công và bảo vệ dữ liệu khỏi các truy cập trái phép.

## Các biện pháp cơ bản

*   **Cập nhật hệ thống**: Luôn giữ hệ điều hành và các gói phần mềm ở phiên bản mới nhất.
    *   `sudo apt update && sudo apt dist-upgrade`
*   **Quản lý SSH**: 
    *   Vô hiệu hóa đăng nhập bằng mật khẩu (chỉ dùng key).
    *   Vô hiệu hóa đăng nhập trực tiếp bằng tài khoản `root`.
*   **Nguyên tắc đặc quyền tối thiểu (Least Privilege)**: Chỉ cấp quyền `sudo` cho các lệnh cụ thể thay vì toàn quyền.
*   **Kiểm toán định kỳ**: Kiểm tra phiên bản kernel, quyền hạn tệp tin (world-writable), cron jobs và các dịch vụ cấu hình sai.

## Cơ chế Kiểm soát Truy cập Nâng cao (MAC)

Các hệ thống Mandatory Access Control (MAC) cung cấp khả năng kiểm soát chi tiết hơn so với quyền hạn tệp tin truyền thống.

*   **SELinux (Security-Enhanced Linux)**: Tích hợp sâu vào kernel, gán nhãn cho mọi tiến trình và đối tượng. Rất mạnh mẽ nhưng phức tạp khi cấu hình.
*   **AppArmor**: Sử dụng các "profile" ứng dụng để giới hạn tài nguyên. Dễ cấu hình và thân thiện hơn SELinux.

## TCP Wrappers

Một công cụ kiểm soát truy cập dựa trên máy chủ, hạn chế dịch vụ dựa trên địa chỉ IP hoặc hostname của kết nối đến.

*   **File cấu hình**:
    *   `/etc/hosts.allow`: Danh sách các dịch vụ và máy được phép truy cập.
    *   `/etc/hosts.deny`: Danh sách các dịch vụ và máy bị cấm truy cập.
*   **Ví dụ `/etc/hosts.allow`**:
    ```txt
    sshd : 10.129.14.0/24
    ftpd : 10.129.14.10
    ```

## Các công cụ hỗ trợ khác

*   **fail2ban**: Theo dõi các lần đăng nhập thất bại và chặn IP tạm thời.
*   **Snort**: Hệ thống phát hiện xâm nhập (IDS).
*   **Lynis**: Công cụ kiểm tra bảo mật hệ thống.
*   **chkrootkit / rkhunter**: Tìm kiếm rootkit trên hệ thống.

## Checklist bảo mật nhanh

1. Gỡ bỏ các dịch vụ và phần mềm không cần thiết.
2. Vô hiệu hóa các dịch vụ dùng cơ chế xác thực không mã hóa.
3. Đảm bảo NTP hoạt động và Syslog đang chạy.
4. Ép buộc sử dụng mật khẩu mạnh và giới hạn lịch sử mật khẩu.
5. Khóa tài khoản sau một số lần đăng nhập thất bại.
6. Vô hiệu hóa các file SUID/SGID không mong muốn.

## Liên kết liên quan
*   [[my_knowlegde/concepts/network-security|Bảo mật Mạng]]
*   [[my_knowlegde/concepts/linux-firewall|Tường lửa Linux]]
*   [[my_knowlegde/concepts/linux-permissions|Quyền hạn Linux]]
*   [[my_knowlegde/concepts/linux-logging|Ghi nhật ký hệ thống]]
