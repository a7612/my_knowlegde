---
sources:
  - raw/Hack The Box/Network Foundations/Network Security and Data Flow Analysis - Data Flow Example.md
tags:
  - networking
  - data-flow
  - encapsulation
  - nat
  - dns
---

# Phân tích Luồng dữ liệu (Data Flow Analysis)

Để hiểu cách một mạng hoạt động trên thực tế, chúng ta hãy xem xét quy trình chi tiết khi một người dùng truy cập một trang web (ví dụ: `www.example.com`) từ máy tính xách tay.

## 1. Kết nối Mạng không dây (WLAN)
* Máy tính xác định đúng mạng Wi-Fi (SSID).
* Xác thực bằng mật khẩu (WPA2/WPA3).
* Thiết lập kết nối và giao thức [[dhcp-service|DHCP]] bắt đầu cấu hình IP.

## 2. Cấu hình IP và DHCP
* Nếu máy tính chưa có IP, nó yêu cầu một IP từ máy chủ DHCP của Router.
* Máy chủ DHCP cấp một **IP riêng tư** (ví dụ: `192.168.1.10`) cùng với Subnet Mask, Default Gateway và DNS Server.

## 3. Phân giải tên miền (DNS)
* Máy tính gửi truy vấn [[dns-service|DNS]] để tìm địa chỉ IP của `www.example.com`.
* Máy chủ DNS trả về địa chỉ IP đích (ví dụ: `93.184.216.34`).

## 4. Đóng gói dữ liệu (Encapsulation)
Dữ liệu được chuẩn bị qua các tầng của mô hình [[network-models|OSI/TCP-IP]]:
1. **Tầng ứng dụng**: Trình duyệt tạo yêu cầu HTTP/HTTPS.
2. **Tầng giao vận**: Yêu cầu được gói trong đoạn TCP (cổng 80 hoặc 443).
3. **Tầng Internet**: Đoạn TCP được đặt vào gói IP (Nguồn: `192.168.1.10`, Đích: `93.184.216.34`).
4. **Tầng liên kết**: Gói IP được đặt vào khung Ethernet hoặc Wi-Fi (chứa địa chỉ [[mac-address|MAC]]).

Máy tính sử dụng [[addressing-and-routing|ARP]] để tìm địa chỉ MAC của Router (Default Gateway) để gửi khung dữ liệu đi.

## 5. Biên dịch địa chỉ mạng (NAT)
Router nhận khung dữ liệu, thay thế IP riêng (`192.168.1.10`) bằng **IP công cộng** của nó (ví dụ: `203.0.113.45`). Đây là quy trình [[nat-service|NAT]]. Sau đó, gói tin được chuyển tiếp qua Internet qua nhiều Router trung gian.

## 6. Máy chủ tiếp nhận và Phản hồi
* Tường lửa của máy chủ đích kiểm tra xem lưu lượng có được cho phép hay không.
* Phần mềm máy chủ web (Apache, Nginx) xử lý yêu cầu và gửi lại phản hồi.
* Quá trình phản hồi diễn ra ngược lại, NAT tại Router nhà sẽ ánh xạ IP công cộng trở lại IP riêng của máy tính.

## 7. Giải đóng gói và Hiển thị (Decapsulation)
Máy tính nhận phản hồi, bóc tách các lớp tiêu đề (Header) từ Tầng liên kết đến Tầng ứng dụng. Trình duyệt đọc mã HTML/CSS và hiển thị trang web cho người dùng.
