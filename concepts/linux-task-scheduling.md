---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - Task Scheduling.md"]
tags: ["linux", "administration", "automation", "cron", "systemd-timer"]
---

# Lập lịch Tác vụ (Task Scheduling)

Lập lịch tác vụ cho phép tự động hóa việc thực thi các kịch bản (scripts) hoặc lệnh vào những thời điểm cụ thể hoặc theo định kỳ.

## 1. Cron (Phương pháp truyền thống)
Cron sử dụng một tiến trình ngầm (**crond**) để kiểm tra các tệp cấu hình gọi là **crontab**.
* **Cấu trúc Crontab**: `phút giờ ngày_tháng tháng ngày_tuần <lệnh>`
    * Ví dụ: `0 0 * * 0 /path/to/backup.sh` (Chạy backup vào 0:00 Chủ Nhật hàng tuần).
* **Quản lý**: Dùng lệnh `crontab -e` để chỉnh sửa lịch trình của người dùng hiện tại.

## 2. Systemd Timers (Phương pháp hiện đại)
Systemd cung cấp cơ chế lập lịch linh hoạt hơn, cho phép kích hoạt tác vụ dựa trên sự kiện hệ thống (như sau khi boot).
* **Quy trình thiết lập**:
    1. Tạo tệp **Timer** (`.timer`): Định nghĩa thời gian hoặc khoảng cách thực thi.
    2. Tạo tệp **Service** (`.service`): Định nghĩa lệnh hoặc script cần chạy.
    3. Kích hoạt: `sudo systemctl enable --now mytimer.timer`.

## 3. So sánh Cron và Systemd Timers

| Đặc điểm | Cron | Systemd Timers |
| --- | --- | --- |
| Cấu hình | Tệp crontab đơn giản | Phức tạp hơn (cần 2 tệp) |
| Tính năng | Đơn thuần theo thời gian | Hỗ trợ sự kiện, phụ thuộc dịch vụ |
| Nhật ký | Lưu trong `/var/log/syslog` | Quản lý tập trung qua `journalctl` |

Việc hiểu rõ lập lịch tác vụ không chỉ giúp quản trị hệ thống hiệu quả mà còn là kiến thức quan trọng trong an ninh mạng để phát hiện các cơ chế duy trì sự hiện diện (persistence) của mã độc.
