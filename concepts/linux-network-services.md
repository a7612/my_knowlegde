---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - Network Services.md"]
tags: ["linux", "administration", "network", "ssh", "nfs", "apache", "vpn"]
---

# Các Dịch vụ Mạng trên Linux (Network Services)

Quản trị dịch vụ mạng là kỹ năng cốt lõi để thiết lập kết nối, truyền tải tệp tin và quản lý hệ thống từ xa.

## 1. Secure Shell (SSH)
**[[ssh|SSH]]** là giao thức tiêu chuẩn để quản lý hệ thống từ xa một cách bảo mật qua kết nối mã hóa.
* **Máy chủ**: Phổ biến nhất là **OpenSSH**. Cài đặt bằng `sudo apt install openssh-server`.
* **Cấu hình**: Tệp `/etc/ssh/sshd_config` cho phép điều chỉnh cổng, phương thức đăng nhập và các giới hạn bảo mật.
* **Ứng dụng trong Pentest**: Dùng để truy cập máy mục tiêu, tạo đường hầm (tunneling) và chuyển tiếp cổng (port forwarding).

## 2. Network File System (NFS)
**[[nfs|NFS]]** cho phép gắn các thư mục từ máy chủ từ xa và sử dụng như thư mục cục bộ.
* **Cài đặt**: `sudo apt install nfs-kernel-server`.
* **Cấu hình**: Tệp `/etc/exports` định nghĩa các thư mục chia sẻ và quyền truy cập (`rw`, `sync`, `no_root_squash`).
* **Gắn kết**: Sử dụng lệnh `mount <IP_Server>:/path/to/share /mnt/local_path`.

## 3. Web Server (Máy chủ Web)
Dùng để phân phối nội dung web qua giao thức HTTP/HTTPS.
* **Apache**: Phổ biến, ổn định, cấu hình tại `/etc/apache2/apache2.conf`.
* **Python SimpleHTTPServer**: Cách nhanh nhất để chia sẻ tệp tin trong mạng nội bộ.
    `python3 -m http.server 8000`
* **Ứng dụng**: Phục vụ việc chuyển tệp tin sang máy mục tiêu hoặc lưu trữ các trang giả mạo (phishing).

## 4. Virtual Private Network (VPN)
Tạo ra một đường hầm bảo mật kết nối với mạng nội bộ từ xa.
* **OpenVPN**: Giải pháp mã nguồn mở phổ biến.
* **Kết nối**: Sử dụng lệnh `sudo openvpn --config client.ovpn`.

Hiểu rõ cách cấu hình và những rủi ro bảo mật của từng dịch vụ (như capture mật khẩu FTP không mã hóa) là điều tối quan trọng đối với cả quản trị viên và chuyên gia an ninh mạng.
