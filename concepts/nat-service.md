---
sources:
  - raw/Hack The Box/Network Foundations/Network Communication and Addressing - Network Address Translation (NAT).md
tags:
  - networking
  - services
  - nat
  - ipv4
---

# Biên dịch Địa chỉ Mạng (NAT - Network Address Translation)

[[nat|NAT]] là một giải pháp được sử dụng để giải quyết tình trạng thiếu hụt địa chỉ IPv4 bằng cách cho phép nhiều thiết bị trong một mạng riêng chia sẻ một địa chỉ IP công cộng duy nhất để truy cập Internet.

## Địa chỉ IP Công cộng và Riêng tư

### 1. Địa chỉ IP Công cộng (Public IP)
* Được cấp bởi ISP, là duy nhất trên toàn cầu.
* Có thể truy cập từ bất kỳ đâu trên Internet.

### 2. Địa chỉ IP Riêng tư (Private IP)
* Dùng trong mạng nội bộ (gia đình, trường học, văn phòng).
* Không thể định tuyến trực tiếp trên Internet toàn cầu.
* Các dải địa chỉ phổ biến (theo RFC 1918):
    * `10.0.0.0` - `10.255.255.255`
    * `172.16.0.0` - `172.31.255.255`
    * `192.168.0.0` - `192.168.255.255`

## Cơ chế hoạt động của NAT
Khi một thiết bị trong mạng nội bộ gửi yêu cầu ra Internet:
1. Router nhận gói tin và thay thế địa chỉ IP riêng tư của thiết bị bằng địa chỉ IP công cộng của Router.
2. Router lưu thông tin này vào **bảng NAT** (NAT table) để biết gói tin phản hồi sau đó sẽ được gửi trả về cho thiết bị nào trong mạng nội bộ.
3. Khi nhận được phản hồi, Router tra bảng NAT và chuyển tiếp gói tin về đúng thiết bị yêu cầu.

## Các loại NAT
* **Static NAT**: Ánh xạ 1-1 cố định giữa IP riêng và IP công cộng.
* **Dynamic NAT**: Gán IP công cộng từ một nhóm (pool) có sẵn khi cần.
* **Port Address Translation (PAT)**: Còn gọi là NAT Overload, là loại phổ biến nhất. Nhiều IP riêng chia sẻ một IP công cộng bằng cách sử dụng các số hiệu [[network-port|cổng]] khác nhau.

## Lợi ích và Hạn chế
* **Lợi ích**: Tiết kiệm địa chỉ IPv4, tăng cường bảo mật (che giấu cấu trúc mạng nội bộ).
* **Hạn chế**: Gây khó khăn cho một số giao thức yêu cầu kết nối đầu-cuối trực tiếp, làm phức tạp quá trình xử lý sự cố.
