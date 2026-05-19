---
sources: ["raw/Hack The Box/Network Foundations/Networking Fundamentals - Components of a Network.md"]
tags: ["networking", "hardware", "router"]
---

# Bộ định tuyến (Router)

[[my_knowlegde/entities/router|Router]] là một thiết bị trung gian đóng vai trò cực kỳ quan trọng trong việc chuyển tiếp các gói dữ liệu giữa các mạng khác nhau và điều phối lưu lượng Internet.

## Đặc điểm chính
* **Tầng OSI**: Hoạt động tại **Tầng mạng (Layer 3)**.
* **Địa chỉ sử dụng**: Sử dụng địa chỉ [[ip-address|IP]] để xác định đích đến của dữ liệu.
* **Chức năng**:
    * **Chuyển tiếp gói tin**: Kiểm tra các gói dữ liệu đến và gửi chúng về phía đích.
    * **Kết nối mạng**: Cho phép các thiết bị trên các mạng khác nhau giao tiếp với nhau.
    * **Quản lý lưu lượng**: Lựa chọn đường đi tối ưu để tránh tắc nghẽn.
    * **Bảo mật**: Tích hợp tường lửa và danh sách kiểm soát truy cập (ACL).

## Giao thức định tuyến
Router sử dụng các bảng định tuyến và giao thức như:
* **OSPF (Open Shortest Path First)**
* **BGP (Border Gateway Protocol)**

## Bộ định tuyến không dây (Wireless Router)
Trong môi trường gia đình hoặc văn phòng nhỏ, một bộ định tuyến không dây kết hợp nhiều chức năng:
* **Định tuyến (Routing)**: Chuyển hướng dữ liệu đến đúng đích.
* **Điểm truy cập không dây (Wireless Access Point)**: Cung cấp vùng phủ sóng Wi-Fi.

### Các thành phần chính của Wireless Router
* **Cổng WAN**: Kết nối với nguồn Internet (ví dụ: Modem).
* **Cổng LAN**: Kết nối có dây cho các thiết bị nội bộ (PC, máy in).
* **Anten (Antennae)**: Truyền và nhận tín hiệu không dây.
* **Bộ xử lý & Bộ nhớ**: Xử lý các tác vụ quản lý mạng.
