---
sources: ["raw/Hack The Box/Network Foundations/Networking Fundamentals - Components of a Network.md"]
tags: ["networking", "security", "firewall"]
---

# Tường lửa (Firewall)

[[firewall|Tường lửa]] là một ứng dụng hoặc thiết bị bảo mật dùng để theo dõi và kiểm soát lưu lượng mạng ra vào dựa trên các quy tắc bảo mật đã được thiết lập.

## Các loại tường lửa chi tiết

### 1. Tường lửa lọc gói tin (Packet Filtering Firewall)
* **Tầng hoạt động**: Tầng 3 (Mạng) và Tầng 4 (Giao vận).
* **Cơ chế**: Kiểm tra địa chỉ IP nguồn/đích, cổng nguồn/đích và loại giao thức.
* **Ví dụ**: Một ACL đơn giản trên Router chỉ cho phép cổng 80 (HTTP) và 443 (HTTPS).

### 2. Tường lửa kiểm tra trạng thái (Stateful Inspection Firewall)
* **Cơ chế**: Theo dõi trạng thái của các kết nối mạng. Thông minh hơn vì nó hiểu toàn bộ cuộc hội thoại.
* **Ví dụ**: Chỉ cho phép dữ liệu đi vào nếu nó khớp với một yêu cầu đi ra đã được thiết lập trước đó.

### 3. Tường lửa tầng ứng dụng (Application Layer / Proxy Firewall)
* **Tầng hoạt động**: Lên đến Tầng 7 (Ứng dụng).
* **Cơ chế**: Có thể kiểm tra nội dung thực tế của lưu lượng (ví dụ: các yêu cầu HTTP) và chặn các yêu cầu độc hại.

### 4. Tường lửa thế hệ mới (Next-Generation Firewall - NGFW)
* **Cơ chế**: Kết hợp kiểm tra trạng thái với các tính năng nâng cao như kiểm tra gói tin sâu (DPI), phát hiện/ngăn chặn xâm nhập (IDS/IPS) và kiểm soát ứng dụng.

### 5. Tường lửa Ứng dụng Web (Web Application Firewall - WAF)
* **Cơ chế**: Hoạt động như một **[[proxies|Proxy ngược (Reverse Proxy)]]**, kiểm tra và lọc các yêu cầu HTTP/HTTPS độc hại nhắm vào ứng dụng web.
* **Ví dụ**: Cloudflare, ModSecurity.
* **Tác dụng**: Chống lại các cuộc tấn công như SQL Injection, Cross-Site Scripting (XSS).

## Triển khai trên Linux
Để biết chi tiết về cách cấu hình tường lửa trên hệ điều hành Linux, xem trang [[linux-firewall|Tường lửa Linux (Iptables)]].

## Vị trí đặt tường lửa
* **Mạng gia đình**: Thường tích hợp sẵn trong Router/Modem.
* **Mạng doanh nghiệp**: Thường là một thiết bị riêng biệt đặt sau Modem/Router và trước mạng nội bộ.
