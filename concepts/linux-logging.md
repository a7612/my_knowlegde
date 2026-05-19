---
sources:
  - "Hack The Box Academy - Linux Fundamentals - System Logs and Monitoring"
tags:
  - "linux"
  - "administration"
  - "security"
  - "logging"
---

# Nhật ký Hệ thống và Giám sát (System Logs and Monitoring)

Nhật ký hệ thống (Logs) là nguồn thông tin vô giá để theo dõi hoạt động, khắc phục sự cố và phát hiện các mối đe dọa bảo mật trên Linux.

## Các loại nhật ký phổ biến

Hầu hết các file nhật ký được lưu trữ trong thư mục `/var/log/`.

*   **Kernel Logs (`/var/log/kern.log`)**: Chứa thông tin về nhân hệ thống, trình điều khiển thiết bị, lỗi phần cứng và các sự kiện cấp thấp.
*   **System Logs (`/var/log/syslog`)**: Ghi lại các sự kiện cấp hệ thống như khởi động/dừng dịch vụ, thông báo lỗi chung.
*   **Authentication Logs (`/var/log/auth.log`)**: Theo dõi các lần thử đăng nhập (thành công và thất bại), sử dụng `sudo` và các sự kiện liên quan đến xác thực.
*   **Application Logs**: Nhật ký riêng của từng ứng dụng (ví dụ: `/var/log/apache2/error.log`, `/var/log/mysql/error.log`).
*   **Security Logs**: Các công cụ bảo mật có nhật ký riêng (ví dụ: `/var/log/fail2ban.log`, `/var/log/ufw.log`).

## Phân tích Nhật ký cho Penetration Testing

*   **Phát hiện xâm nhập**: Tìm kiếm các nỗ lực đăng nhập thất bại liên tục (brute force) trong `auth.log`.
*   **Theo dõi đặc quyền**: Xem người dùng nào đã sử dụng `sudo` và chạy lệnh gì.
*   **Tìm kiếm thông tin nhạy cảm**: Đôi khi nhật ký ứng dụng có thể vô tình ghi lại thông tin đăng nhập hoặc dữ liệu nhạy cảm ở dạng văn bản thuần túy.

## Các công cụ xem và phân tích

*   `tail -f /var/log/syslog`: Xem nhật ký trong thời gian thực.
*   `grep "Failed" /var/log/auth.log`: Tìm kiếm các lần đăng nhập thất bại.
*   `journalctl`: Công cụ truy vấn nhật ký từ `systemd`.

## Quản lý Nhật ký

*   **Log Rotation**: Sử dụng `logrotate` để ngăn các file nhật ký chiếm quá nhiều dung lượng đĩa bằng cách nén và lưu trữ các phiên bản cũ.
*   **Log Levels**: Cấu hình mức độ chi tiết của nhật ký (từ debug đến emergency).

## Liên kết liên quan
*   [[my_knowlegde/concepts/linux-hardening|Tăng cường Bảo mật Linux]]
*   [[my_knowlegde/concepts/linux-service-process-management|Quản lý Dịch vụ và Tiến trình]]
*   [[my_knowlegde/concepts/linux-filtering|Lọc nội dung]]
