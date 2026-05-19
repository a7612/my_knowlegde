---
sources: ["raw/Hack The Box/Linux Fundamentals/The Shell - System Information.md"]
tags: ["linux", "commands", "system-info", "situational-awareness"]
---

# Thu thập Thông tin Hệ thống (System Information)

Việc hiểu rõ cấu trúc và thông tin chi tiết của hệ thống Linux là bước đầu tiên quan trọng trong quản trị và đánh giá an ninh mạng.

## Các lệnh cơ bản

| Lệnh | Mô tả |
| --- | --- |
| `whoami` | Hiển thị tên người dùng hiện tại. |
| `id` | Hiển thị UID, GID và các nhóm mà người dùng tham gia. |
| `hostname` | Hiển thị tên của máy chủ hiện tại. |
| `uname -a` | Hiển thị thông tin tổng quát về hạt nhân (kernel) và phần cứng. |
| `pwd` | Hiển thị đường dẫn thư mục làm việc hiện tại. |
| `env` | Liệt kê các biến môi trường. |

## Thông tin Mạng và Tiến trình
* **Mạng**: `ip a` hoặc `ifconfig` để xem địa chỉ IP; `netstat` hoặc `ss` để kiểm tra các cổng đang mở và kết nối mạng.
* **Tiến trình**: `ps` hiển thị trạng thái các tiến trình đang chạy.

## Thông tin Phần cứng
* `lsblk`: Liệt kê các thiết bị khối (ổ đĩa).
* `lsusb`: Liệt kê các thiết bị USB.
* `lspci`: Liệt kê các thiết bị PCI.
* `lsof`: Liệt kê các tệp tin đang được mở bởi hệ thống.

## Kết nối từ xa qua SSH
**SSH (Secure Shell)** là giao thức tiêu chuẩn để truy cập và thực thi lệnh trên máy tính từ xa một cách bảo mật.
* **Cú pháp**: `ssh user@IP_Address`

Việc nắm vững các lệnh này giúp bạn có cái nhìn tổng quan về hệ thống (**Situational Awareness**), hỗ trợ phát hiện các lỗ hổng hoặc cấu hình sai. Bạn có thể tra cứu chi tiết tham số của từng lệnh bằng cách sử dụng [[linux-man-pages|lệnh man]].
