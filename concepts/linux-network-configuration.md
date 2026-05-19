---
sources:
  - "Hack The Box Academy - Linux Fundamentals - Network Configuration"
tags:
  - "linux"
  - "networking"
  - "administration"
---

# Cấu hình Mạng trong Linux (Linux Network Configuration)

Cấu hình mạng là kỹ năng thiết yếu để quản lý hệ thống, thiết lập môi trường thử nghiệm và xử lý sự cố kết nối.

## Quản lý Giao diện Mạng (Network Interfaces)

Sử dụng các lệnh `ifconfig` (cũ) hoặc `ip` (hiện đại) để xem và cấu hình giao diện mạng.

*   **Xem thông tin**: `ifconfig` hoặc `ip addr`.
*   **Kích hoạt giao diện**: 
    *   `sudo ifconfig eth0 up`
    *   `sudo ip link set eth0 up`
*   **Gán địa chỉ IP**: `sudo ifconfig eth0 192.168.1.2`.
*   **Gán Netmask**: `sudo ifconfig eth0 netmask 255.255.255.0`.

## Cấu hình Định tuyến và DNS

*   **Gán Gateway mặc định**: `sudo route add default gw 192.168.1.1 eth0`.
*   **Cấu hình DNS tạm thời**: Chỉnh sửa file `/etc/resolv.conf`.
    ```txt
    nameserver 8.8.8.8
    nameserver 8.8.4.4
    ```

## Cấu hình Cố định (Persistent Configuration)

Các thay đổi bằng lệnh trên sẽ mất khi khởi động lại. Để lưu cấu hình cố định:
1.  Chỉnh sửa file `/etc/network/interfaces` (trên Debian/Ubuntu).
    ```txt
    auto eth0
    iface eth0 inet static
      address 192.168.1.2
      netmask 255.255.255.0
      gateway 192.168.1.1
      dns-nameservers 8.8.8.8 8.8.4.4
    ```
2.  Khởi động lại dịch vụ mạng: `sudo systemctl restart networking`.

## Kiểm soát Truy cập Mạng (Network Access Control - NAC)

NAC đảm bảo chỉ các thiết bị được ủy quyền và tuân thủ mới được truy cập mạng.

### Các mô hình kiểm soát truy cập
*   **Discretionary Access Control (DAC)**: Chủ sở hữu tài nguyên tự quyết định quyền truy cập.
*   **Mandatory Access Control (MAC)**: Hệ điều hành thực thi quyền truy cập dựa trên chính sách bảo mật (ví dụ: SELinux, AppArmor).
*   **Role-Based Access Control (RBAC)**: Quyền hạn dựa trên vai trò trong tổ chức.

## Giám sát và Xử lý sự cố

### Công cụ giám sát
*   `ss` / `netstat`: Thống kê socket và kết nối đang hoạt động.
*   `lsof`: Liệt kê các tệp (bao gồm socket) đang mở bởi tiến trình.
*   `tcpdump` / `Wireshark`: Bắt và phân tích gói tin.

### Công cụ xử lý sự cố
1.  **Ping**: Kiểm tra kết nối cơ bản.
2.  **Traceroute**: Truy vết lộ trình của gói tin.
3.  **Nslookup / Dig**: Kiểm tra phân giải DNS.
4.  **Nmap**: Quét cổng và phát hiện dịch vụ.

## Liên kết liên quan
*   [[my_knowlegde/concepts/linux-network-services|Dịch vụ Mạng Linux]]
*   [[my_knowlegde/concepts/linux-firewall|Tường lửa Linux]]
*   [[my_knowlegde/concepts/dns-service|Dịch vụ DNS]]
*   [[my_knowlegde/concepts/dhcp-service|Dịch vụ DHCP]]
