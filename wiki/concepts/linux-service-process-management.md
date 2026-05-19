---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - Service and Process Management.md"]
tags: ["linux", "administration", "services", "daemons", "processes", "systemd", "signals"]
---

# Quản lý Dịch vụ và Tiến trình (Service and Process Management)

Dịch vụ (còn gọi là **daemons**) là các thành phần chạy ngầm trong Linux mà không cần tương tác trực tiếp của người dùng. Tiến trình (processes) là các chương trình đang thực thi trên hệ thống.

## 1. Quản lý Dịch vụ với Systemd
Hầu hết các bản phân phối Linux hiện đại sử dụng **systemd** làm hệ thống khởi tạo (init system).
* **Lệnh `systemctl`**: Công cụ chính để tương tác với dịch vụ.
    * `sudo systemctl start <dịch_vụ>`: Khởi chạy dịch vụ.
    * `sudo systemctl stop <dịch_vụ>`: Dừng dịch vụ.
    * `sudo systemctl restart <dịch_vụ>`: Khởi động lại dịch vụ.
    * `sudo systemctl status <dịch_vụ>`: Kiểm tra trạng thái hiện tại.
    * `sudo systemctl enable <dịch_vụ>`: Tự động chạy khi khởi động máy.
    * `sudo systemctl disable <dịch_vụ>`: Tắt tự động chạy khi khởi động.
* **Lệnh `journalctl`**: Xem nhật ký (logs) của các dịch vụ (ví dụ: `journalctl -u ssh.service`).

## 2. Quản lý Tiến trình
Mỗi chương trình khi chạy đều có một mã định danh duy nhất gọi là **PID** (Process ID).
* **Xem tiến trình**: Sử dụng lệnh `ps -aux` hoặc `top`/`htop` để theo dõi thời gian thực.
* **Kiểm soát tiến trình**: Gửi tín hiệu (signals) thông qua lệnh `kill`.
    * **Signal 9 (SIGKILL)**: Buộc dừng ngay lập tức (không dọn dẹp).
    * **Signal 15 (SIGTERM)**: Yêu cầu dừng an toàn (mặc định).

## 3. Quản lý luồng công việc (Jobs)
* **Chạy ngầm (Background)**: Thêm ký hiệu `&` vào cuối lệnh (ví dụ: `ping 8.8.8.8 &`).
* **Tạm dừng**: Nhấn `Ctrl + Z` (gửi tín hiệu `SIGTSTP`).
* **Đưa vào nền**: Dùng lệnh `bg` để tiếp tục chạy tiến trình đang tạm dừng trong nền.
* **Đưa ra phía trước**: Dùng lệnh `fg <ID>` để tương tác lại với tiến trình.

## 4. Thực thi nhiều lệnh
* **Semicolon (`;`)**: Chạy tuần tự, bỏ qua lỗi của lệnh trước.
* **Double Ampersand (`&&`)**: Chỉ chạy lệnh sau nếu lệnh trước thành công.
* **Pipes (`|`)**: Chuyển đầu ra của lệnh trước làm đầu vào cho lệnh sau.
