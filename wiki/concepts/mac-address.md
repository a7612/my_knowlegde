---
sources: ["raw/Hack The Box/Introduction to Networking/Addressing - MAC Addresses.md"]
tags: ["networking", "addressing", "mac", "layer2", "security"]
---

# Địa chỉ MAC (Media Access Control)

**Địa chỉ MAC** là địa chỉ vật lý (physical address) duy nhất của giao diện mạng (NIC), hoạt động tại **Tầng 2 (Liên kết dữ liệu)** của mô hình OSI.

## 1. Cấu trúc địa chỉ MAC
Địa chỉ MAC dài 48 bit (6 octet), được biểu diễn dưới dạng thập lục phân (Hexadecimal).
*   **OUI (Organization Unique Identifier)**: 24 bit đầu tiên do IEEE cấp cho nhà sản xuất.
*   **NIC (Network Interface Controller)**: 24 bit cuối do nhà sản xuất tự gán để đảm bảo tính duy nhất.

**Ví dụ**: `DE:AD:BE:EF:13:37`

## 2. Các loại địa chỉ MAC
*   **Unicast**: Gửi đến một máy chủ cụ thể.
*   **Multicast**: Gửi đến một nhóm máy chủ trong mạng LAN.
*   **Broadcast**: Gửi đến tất cả máy chủ trong mạng. Địa chỉ MAC Broadcast là `FF:FF:FF:FF:FF:FF`.

## 3. Các Vector tấn công liên quan đến MAC
Vì địa chỉ MAC có thể bị thay đổi (spoofing) bằng phần mềm, chúng không nên là cơ chế bảo mật duy nhất.
*   **MAC Spoofing**: Giả mạo địa chỉ MAC của một thiết bị hợp lệ để truy cập trái phép.
*   **MAC Flooding**: Gửi hàng loạt gói tin với các địa chỉ MAC khác nhau đến Switch để làm tràn bảng MAC, khiến Switch hoạt động như Hub và phát tán dữ liệu ra mọi cổng.
*   **MAC Filtering Bypass**: Vượt qua bộ lọc MAC của mạng bằng cách giả mạo MAC được cho phép.

## Liên kết liên quan
*   [[addressing-and-routing|Định danh và Truyền thông]]
*   [[arp-protocol|Giao thức ARP]]
*   [[my_knowlegde/entities/network-hardware|Thiết bị mạng]]
