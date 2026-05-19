---
sources:
  - "Hack The Box Academy - Linux Fundamentals - Firewall Setup"
tags:
  - "linux"
  - "networking"
  - "security"
  - "firewall"
---

# Tường lửa trong Linux (Linux Firewall - Iptables)

Tường lửa trong Linux là cơ chế bảo mật dùng để kiểm soát và giám sát lưu lượng mạng dựa trên các quy tắc được định nghĩa trước.

## Các giải pháp Tường lửa

*   **Iptables**: Tiêu chuẩn truyền thống lâu đời trên Linux.
*   **Nftables**: Phiên bản hiện đại thay thế iptables với hiệu suất tốt hơn và cú pháp mới.
*   **UFW (Uncomplicated Firewall)**: Giao diện đơn giản chạy trên nền iptables/nftables, phổ biến trên Ubuntu.
*   **FirewallD**: Giải pháp linh hoạt hỗ trợ quản lý theo vùng (zones) và dịch vụ.

## Tìm hiểu Iptables

Iptables hoạt động dựa trên cấu trúc: **Tables (Bảng) -> Chains (Chuỗi) -> Rules (Quy tắc)**.

### 1. Tables (Bảng)
Dùng để phân loại quy tắc theo mục đích:
*   **filter**: Bảng mặc định để lọc gói tin (INPUT, OUTPUT, FORWARD).
*   **nat**: Dùng để thay đổi địa chỉ IP nguồn/đích (Network Address Translation).
*   **mangle**: Dùng để thay đổi các trường trong header của gói tin.

### 2. Chains (Chuỗi)
Nhóm các quy tắc áp dụng cho loại lưu lượng cụ thể:
*   **INPUT**: Lưu lượng đi vào máy.
*   **OUTPUT**: Lưu lượng đi ra từ máy.
*   **FORWARD**: Lưu lượng đi qua máy (đến máy khác).

### 3. Targets (Mục tiêu)
Hành động thực hiện khi gói tin khớp với quy tắc:
*   **ACCEPT**: Cho phép gói tin đi qua.
*   **DROP**: Chặn gói tin (không phản hồi).
*   **REJECT**: Chặn gói tin và gửi thông báo lỗi lại cho nguồn.
*   **LOG**: Ghi lại thông tin gói tin vào nhật ký hệ thống.

## Ví dụ sử dụng Iptables

*   **Cho phép kết nối SSH (Cổng 22)**:
    ```bash
    sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
    ```
*   **Cho phép lưu lượng HTTP (Cổng 80)**:
    ```bash
    sudo iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
    ```
*   **Chặn lưu lượng từ một IP cụ thể**:
    ```bash
    sudo iptables -A INPUT -s 10.10.10.10 -j DROP
    ```

## So sánh Matches phổ biến
| Tùy chọn | Mô tả |
| --- | --- |
| `-p` | Giao thức (tcp, udp, icmp) |
| `--dport` | Cổng đích |
| `--sport` | Cổng nguồn |
| `-s` | Địa chỉ IP nguồn |
| `-d` | Địa chỉ IP đích |
| `-m state` | Trạng thái kết nối (NEW, ESTABLISHED, RELATED) |

## Liên kết liên quan
*   [[my_knowlegde/entities/firewall|Thực thể Tường lửa]]
*   [[my_knowlegde/concepts/network-security|Bảo mật Mạng]]
*   [[my_knowlegde/concepts/linux-network-configuration|Cấu hình Mạng Linux]]
