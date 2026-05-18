---
sources: ["raw/Hack The Box/Introduction to Networking/Addressing - IP Addresses.md"]
tags: ["networking", "addressing", "ipv4", "layer3"]
---

# Địa chỉ IPv4 (Internet Protocol version 4)

**IPv4** là giao thức định danh máy chủ phổ biến nhất trên Internet, hoạt động tại **Tầng 3 (Mạng)** của mô hình OSI.

## 1. Cấu trúc địa chỉ IPv4
Địa chỉ IPv4 gồm 32 bit, được chia thành 4 nhóm 8 bit (octet), biểu diễn dưới dạng số thập phân cách nhau bởi dấu chấm (dotted-decimal notation).
*   **Ví dụ**: `192.168.10.39`
*   **Phạm vi**: Mỗi octet từ 0 đến 255.
*   **Thành phần**: Chia thành phần mạng (Network part) và phần máy chủ (Host part).

## 2. Phân lớp địa chỉ IP (Legacy)
Trong quá khứ, địa chỉ IP được chia thành các lớp từ A đến E:
*   **Lớp A**: `/8`, dành cho mạng cực lớn.
*   **Lớp B**: `/16`, dành cho mạng vừa.
*   **Lớp C**: `/24`, dành cho mạng nhỏ.
*   **Lớp D**: Dùng cho Multicast.
*   **Lớp E**: Dự phòng.

## 3. CIDR (Classless Inter-Domain Routing)
CIDR thay thế việc phân lớp cố định bằng cách sử dụng **Subnet Mask** hoặc hậu tố CIDR (ví dụ: `/24`) để phân định linh hoạt phần mạng và phần máy chủ.
*   **Ví dụ**: `192.168.10.39/24` có nghĩa là 24 bit đầu là phần mạng.

## 4. Các địa chỉ đặc biệt
*   **Địa chỉ mạng (Network Address)**: Địa chỉ đầu tiên của dải IP (tất cả bit phần host là 0).
*   **Địa chỉ Broadcast**: Địa chỉ cuối cùng của dải IP (tất cả bit phần host là 1).
*   **Default Gateway**: Thường là địa chỉ đầu tiên hoặc cuối cùng có thể gán trong mạng, dùng để trỏ đến Router.

## Liên kết liên quan
*   [[addressing-and-routing|Định danh và Truyền thông]]
*   [[ipv6-address|Địa chỉ IPv6]]
*   [[subnetting|Chia mạng con (Subnetting)]]
