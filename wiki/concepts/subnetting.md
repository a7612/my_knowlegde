---
sources: ["raw/Hack The Box/Introduction to Networking/Addressing - Subnetting.md"]
tags: ["networking", "addressing", "subnetting", "ipv4"]
---

# Chia mạng con (Subnetting)

**Subnetting** là quá trình chia một dải địa chỉ IPv4 lớn thành các dải mạng nhỏ hơn (mạng con). Điều này giúp tối ưu hóa việc sử dụng địa chỉ, tăng cường bảo mật và hiệu suất mạng.

## 1. Thành phần của một mạng con
Để xác định một mạng con, ta cần các thông số:
*   **Địa chỉ mạng (Network Address)**: Địa chỉ định danh toàn bộ mạng con.
*   **Địa chỉ Broadcast**: Địa chỉ dùng để gửi tin cho tất cả thiết bị trong mạng con.
*   **Dải Host (Usable IP range)**: Các địa chỉ có thể gán cho thiết bị (nằm giữa địa chỉ mạng và broadcast).
*   **Số lượng Host**: Tổng số địa chỉ gán được (thường là $2^{(32-n)} - 2$).

## 2. Cách thức hoạt động
Sử dụng **Subnet Mask** làm khuôn mẫu (template) để chia địa chỉ IP thành 2 phần:
*   **Phần Mạng (Network Part)**: Cố định, được xác định bởi các bit `1` trong Subnet Mask.
*   **Phần Host (Host Part)**: Có thể thay đổi, được xác định bởi các bit `0` trong Subnet Mask.

## 3. Ví dụ chia mạng con
Giả sử có mạng `192.168.12.128/26`:
*   **Subnet Mask**: `255.255.255.192` (26 bit `1`).
*   **Bước nhảy**: 64 địa chỉ.
*   **Địa chỉ mạng**: `192.168.12.128`
*   **Địa chỉ Broadcast**: `192.168.12.191`
*   **Dải Host**: `192.168.12.129` đến `192.168.12.190`.

## 4. Chia nhỏ tiếp (Sub-subnetting)
Nếu muốn chia mạng `/26` trên thành 4 mạng con nhỏ hơn:
*   Cần thêm 2 bit ($2^2 = 4$).
*   Subnet mask mới sẽ là `/28` (`255.255.255.240`).
*   Mỗi mạng con mới sẽ có 16 địa chỉ ($64 / 4 = 16$).

## Liên kết liên quan
*   [[ipv4-address|Địa chỉ IPv4]]
*   [[addressing-and-routing|Định danh và Truyền thông]]
*   [[network-types|Các loại mạng]]
