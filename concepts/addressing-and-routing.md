---
sources:
  - raw/Hack The Box/Network Foundations/Network Communication and Addressing - Network Communication.md
tags:
  - networking
  - addressing
  - mac
  - ip
  - ports
  - arp
---

# Định danh và Truyền thông mạng (Addressing & Communication)

Để dữ liệu được gửi và nhận chính xác giữa các thiết bị, mạng sử dụng ba thành phần định danh cốt lõi hoạt động tại các tầng khác nhau của mô hình OSI.

## 1. Tầng Mạng (Network Layer - Layer 3)
Tầng mạng chịu trách nhiệm định tuyến gói tin từ nguồn đến đích thông qua các nút mạng (router).
*   **Định danh Logic (Logical Addressing)**: Gán địa chỉ IP cho thiết bị.
*   **Định tuyến (Routing)**: Quyết định đường đi tốt nhất cho gói tin dựa trên bảng định tuyến.
*   **Giao thức phổ biến**: IPv4, IPv6, ICMP, IPsec, OSPF, RIP.

## 2. Các thành phần định danh chính

### Địa chỉ MAC (Media Access Control)
*   **Tầng OSI**: Tầng 2 (Liên kết dữ liệu).
*   **Đặc điểm**: Địa chỉ vật lý duy nhất gán cho phần cứng (NIC).
*   **Vai trò**: Giao tiếp trong mạng nội bộ.
*   **Chi tiết**: [[my_knowlegde/concepts/mac-address|Địa chỉ MAC và các vector tấn công]].

### Địa chỉ IP (Internet Protocol)
*   **Tầng OSI**: Tầng 3 (Mạng).
*   **Các phiên bản**:
    *   **[[my_knowlegde/concepts/ipv4-address|IPv4]]**: 32 bit, sử dụng ký hiệu thập phân có dấu chấm.
    *   **[[my_knowlegde/concepts/ipv6-address|IPv6]]**: 128 bit, sử dụng ký hiệu thập lục phân, tích hợp bảo mật tốt hơn.
*   **Vai trò**: Định danh thiết bị trên phạm vi toàn cầu hoặc mạng lớn.
*   **Quản lý**: [[my_knowlegde/concepts/subnetting|Chia mạng con (Subnetting)]] giúp quản lý dải IP hiệu quả.

### Cổng (Network Port)
*   **Tầng OSI**: Tầng 4 (Giao vận).
*   **Khái niệm**: Số hiệu giúp phân loại lưu lượng cho các dịch vụ cụ thể (HTTP: 80, SSH: 22).

## 3. Giao thức phân giải địa chỉ (ARP)
*   **Chức năng**: Ánh xạ địa chỉ IP sang địa chỉ MAC để thiết bị có thể "nói chuyện" trực tiếp trong mạng LAN.
*   **Chi tiết**: [[my_knowlegde/concepts/arp-protocol|Cơ chế ARP và tấn công ARP Spoofing]].

## Ví dụ: Quy trình truyền tin qua các mạng
1.  **Đóng gói**: Dữ liệu từ tầng ứng dụng được đóng gói với Port (Tầng 4), IP (Tầng 3) và MAC (Tầng 2).
2.  **Định tuyến**: Nếu IP đích nằm ở mạng khác, gói tin được gửi đến **Default Gateway** (thông qua địa chỉ MAC của Router).
3.  **Chuyển tiếp**: Router kiểm tra bảng định tuyến và chuyển gói tin qua các nút mạng cho đến khi tới mạng đích.
4.  **Phân giải**: Tại mạng đích, Router sử dụng ARP để tìm địa chỉ MAC của thiết bị đích và chuyển gói tin vào tầng vật lý.
