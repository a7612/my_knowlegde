---
sources: ["raw/Hack The Box/Introduction to Networking/Addressing - IPv6 Addresses.md"]
tags: ["networking", "addressing", "ipv6", "layer3"]
---

# Địa chỉ IPv6 (Internet Protocol version 4)

**IPv6** là thế hệ kế tiếp của IPv4, được thiết kế để giải quyết sự cạn kiệt địa chỉ và cung cấp các tính năng hiện đại hơn.

## 1. Đặc điểm nổi bật
*   **Độ dài**: 128 bit (so với 32 bit của IPv4).
*   **Không gian địa chỉ**: ~ 340 undecillion địa chỉ (gần như vô hạn).
*   **Biểu diễn**: Hệ thập lục phân (Hexadecimal), chia thành 8 khối, ngăn cách bởi dấu hai chấm (`:`).
*   **Tự cấu hình (SLAAC)**: Thiết bị có thể tự gán địa chỉ mà không cần DHCP.
*   **Bảo mật**: Tích hợp sẵn IPsec (Bắt buộc).
*   **Không có Broadcast**: IPv6 sử dụng Multicast để thay thế Broadcast.

## 2. Quy tắc viết rút gọn IPv6
Theo RFC 5952:
*   Bỏ qua các số 0 dẫn đầu trong mỗi khối.
*   Thay thế các khối chứa toàn số 0 liên tiếp bằng dấu `::` (chỉ được dùng một lần duy nhất).
*   Ví dụ: `fe80:0000:0000:0000:dd80:b1a9:6687:2d3b` rút gọn thành `fe80::dd80:b1a9:6687:2d3b`.

## 3. Cấu trúc địa chỉ IPv6
Gồm hai phần chính:
*   **Network Prefix**: Định danh mạng hoặc mạng con.
*   **Interface Identifier (Suffix)**: Định danh giao diện thiết bị (thường được tạo từ địa chỉ MAC 48 bit chuyển đổi sang 64 bit).

## 4. Các loại địa chỉ IPv6
*   **Unicast**: Định danh một giao diện duy nhất.
*   **Anycast**: Định danh một nhóm giao diện, gói tin được gửi đến giao diện "gần nhất".
*   **Multicast**: Định danh một nhóm giao diện, tất cả đều nhận được gói tin.

## Liên kết liên quan
*   [[my_knowlegde/concepts/addressing-and-routing|Định danh và Truyền thông]]
*   [[my_knowlegde/concepts/ipv4-address|Địa chỉ IPv4]]
*   [[my_knowlegde/concepts/mac-address|Địa chỉ MAC]]
