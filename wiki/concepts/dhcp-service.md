---
sources: ["raw/Hack The Box/Network Foundations/Network Communication and Addressing - Dynamic Host Configuration Protocol (DHCP).md"]
tags: ["networking", "services", "dhcp", "ip-assignment"]
---

# Giao thức Cấu hình Máy chủ Động (DHCP - Dynamic Host Configuration Protocol)

[[dhcp-service|DHCP]] là một giao thức quản lý mạng được sử dụng để tự động hóa quá trình cấu hình các thiết bị trên mạng IP. Thay vì gán địa chỉ IP thủ công, DHCP cho phép các thiết bị tự động nhận địa chỉ IP và các thông số mạng khác.

## Lợi ích của DHCP
* **Tự động hóa**: Giảm bớt khối lượng công việc quản trị.
* **Tránh xung đột**: Đảm bảo mỗi thiết bị có một địa chỉ IP duy nhất.
* **Tối ưu hóa tài nguyên**: Thu hồi và tái sử dụng các địa chỉ IP không còn sử dụng.

## Quy trình DORA
Quá trình cấp phát địa chỉ IP của DHCP diễn ra qua 4 bước chính, được gọi là [[dora-process|DORA]]:

1. **Discover (Khám phá)**: Máy khách gửi một thông điệp quảng bá để tìm máy chủ DHCP.
2. **Offer (Đề nghị)**: Máy chủ DHCP phản hồi với một địa chỉ IP đề nghị.
3. **Request (Yêu cầu)**: Máy khách chấp nhận đề nghị và gửi yêu cầu sử dụng địa chỉ đó.
4. **Acknowledge (Xác nhận)**: Máy chủ xác nhận và gán địa chỉ IP cho máy khách.

## Thời hạn thuê (Lease Time)
Địa chỉ IP cấp qua DHCP không phải là vĩnh viễn mà có một **thời hạn thuê**. Trước khi hết hạn, máy khách phải gửi yêu cầu gia hạn (renewal) để tiếp tục sử dụng địa chỉ IP đó.

## Các thành phần
* **DHCP Server**: Thiết bị (thường là Router hoặc máy chủ chuyên dụng) quản lý kho địa chỉ IP.
* **DHCP Client**: Bất kỳ thiết bị nào kết nối vào mạng và yêu cầu cấu hình.
