---
sources: ["raw/Hack The Box/Network Foundations/Networking Fundamentals - Introduction to Networks.md", "raw/Hack The Box/Introduction to Networking/Introduction - Networking Overview.md"]
tags: ["networking", "fundamentals", "segmentation", "fqdn", "url"]
---

# Mạng máy tính (Computer Network)

## Khái niệm cơ bản
Một **[[computer-network|mạng máy tính]]** là một tập hợp các thiết bị được kết nối với nhau để có thể giao tiếp - gửi và nhận dữ liệu, cũng như chia sẻ tài nguyên.

Các thành phần chính bao gồm:
* **[[network-node|Nút mạng (Node)]]**: Các thiết bị đầu cuối như máy tính, điện thoại thông minh, máy in và máy chủ.
* **[[communication-link|Liên kết (Link)]]**: Các đường dẫn truyền thông kết nối các nút thông qua các phương tiện truyền dẫn (cáp đồng, cáp quang, sóng vô tuyến).
* **[[network-topologies|Sơ đồ mạng (Topologies)]]**: Cách sắp xếp vật lý hoặc logic của các thiết bị.
* **[[network-protocols|Giao thức (Protocols)]]**: Các quy tắc giao tiếp (TCP, UDP, IPX).

## Các phép ẩn dụ dễ hiểu

### 1. FQDN và URL (Tòa nhà và Địa chỉ chi tiết)
* **FQDN** (ví dụ: `www.hackthebox.com`): Giống như địa chỉ của một tòa nhà cụ thể.
* **URL** (ví dụ: `https://www.hackthebox.com/example?floor=2&office=dev`): Không chỉ cho biết địa chỉ tòa nhà mà còn chỉ rõ "số tầng", "văn phòng", "hộp thư" và "nhân viên" cụ thể mà gói hàng cần chuyển đến.

### 2. Router và ISP (Bưu điện địa phương và Bưu điện chính)
* **[[router|Router]]**: Đóng vai trò như bưu điện địa phương tại nhà hoặc công ty của bạn. Khi bạn gửi một "gói tin", router sẽ chuyển nó đến bưu điện lớn hơn.
* **[[isp|ISP (Nhà cung cấp dịch vụ Internet)]]**: Đóng vai trò như bưu điện chính. Nó tra cứu "danh bạ điện thoại" (**[[dns-service|DNS]]**) để tìm tọa độ địa lý (Địa chỉ IP) của đích đến và chuyển gói tin đi.

## Tầm quan trọng và Bảo mật mạng

### Phòng thủ theo chiều sâu (Defense in Depth)
Một mạng "phẳng" (flat network) giống như một ngôi nhà chỉ có một ổ khóa cửa chính; nếu kẻ tấn công vượt qua được, họ sẽ có quyền truy cập toàn bộ bên trong. Một mạng lưới an toàn nên được chia nhỏ và bảo vệ theo nhiều lớp:

1. **Phân đoạn mạng (Segmentation)**: Chia mạng lớn thành nhiều mạng nhỏ hơn để hạn chế phạm vi tấn công. Một công ty nên có ít nhất 5 mạng riêng biệt:
    * **Vùng DMZ (Demilitarized Zone)**: Dành cho các máy chủ công khai như Web Server.
    * **Mạng Trạm làm việc (Workstations)**: Dành cho nhân viên, nên có các quy tắc chặn giao tiếp trực tiếp giữa các máy tính cá nhân.
    * **Mạng Quản trị (Administration Network)**: Dành cho các thiết bị như Switch và Router để ngăn chặn việc nghe lén (snooping).
    * **Mạng Điện thoại IP (IP Phones)**: Để ưu tiên băng thông và tránh nghe lén cuộc gọi.
    * **Mạng Máy in (Printers)**: Đây là những thiết bị rất khó bảo mật và thường bị bỏ quên, nên cần được cô lập hoàn toàn.
2. **Danh sách kiểm soát truy cập (ACL)**: Thiết lập các điểm vào/ra cụ thể và kiểm soát luồng giao tiếp giữa các phân đoạn mạng.
3. **Hệ thống phát hiện xâm nhập (IDS)**: Sử dụng các công cụ như Suricata hoặc Snort để phát hiện sớm các hành vi đáng ngờ (ví dụ: quét cổng).

## Phân loại mạng
Mạng có thể được phân loại theo phạm vi địa lý và mục đích sử dụng. Chi tiết xem tại: [[network-types|Các loại mạng máy tính]].

## Sự kết hợp giữa LAN và WAN
Các mạng LAN kết nối với WAN để truy cập các mạng rộng lớn hơn thông qua thiết bị gọi là **[[modem|Modem]]**. Modem đóng vai trò là cầu nối, chuyển đổi tín hiệu số từ router thành định dạng phù hợp để truyền tải qua các phương tiện như đường dây điện thoại hoặc cáp quang.

