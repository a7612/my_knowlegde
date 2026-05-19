---
sources: ["raw/Hack The Box/Introduction to Networking/Networking Structure - Proxies.md"]
tags: ["networking", "security", "proxy", "waf"]
---

# Máy chủ ủy quyền (Proxies)

Một **Proxy** là một thiết bị hoặc dịch vụ đóng vai trò trung gian (mediator) trong một kết nối. Điểm khác biệt mấu chốt giữa Proxy và Gateway là Proxy có khả năng kiểm tra nội dung thực tế của lưu lượng truy cập. Proxies hầu như luôn hoạt động ở Tầng 7 (Ứng dụng) của mô hình OSI.

## 1. Proxy chuyển tiếp (Forward Proxy)

Đây là loại proxy phổ biến nhất mà người dùng thường hình dung. Client gửi yêu cầu đến Proxy, và Proxy sẽ thay mặt Client thực hiện yêu cầu đó ra Internet.
*   **Công dụng**: Lọc nội dung, kiểm soát malware (đặc biệt hiệu quả nếu malware không có khả năng nhận diện proxy - proxy-aware).
*   **Ví dụ**: Burp Suite (khi dùng để chuyển tiếp các yêu cầu HTTP).

## 2. Proxy ngược (Reverse Proxy)

Trái ngược với Forward Proxy, Reverse Proxy lọc các yêu cầu **đến** từ Internet vào một mạng nội bộ.
*   **Công dụng**: Bảo vệ máy chủ web, lọc lưu lượng truy cập (chống DDoS), ẩn cấu trúc mạng nội bộ.
*   **Web Application Firewall (WAF)**: Một dạng Reverse Proxy (như ModSecurity hoặc Cloudflare) giúp kiểm tra và chặn các yêu cầu web độc hại.

## 3. Proxy trong suốt và Không trong suốt

*   **Proxy trong suốt (Transparent Proxy)**: Client hoàn toàn không biết sự hiện diện của proxy. Nó tự động chặn và xử lý các yêu cầu của Client.
*   **Proxy không trong suốt (Non-Transparent Proxy)**: Client phải được cấu hình (phần mềm/hệ thống) để biết và gửi dữ liệu qua proxy. Nếu không có cấu hình này, giao tiếp ra ngoài thường bị cắt đứt.

## Phân biệt Proxy và VPN
Nhiều người nhầm lẫn Proxy với VPN. Trong khi cả hai đều có thể thay đổi địa chỉ IP hiển thị, VPN hoạt động ở tầng thấp hơn (thường là Tầng 3) và mã hóa toàn bộ lưu lượng, trong khi Proxy thường chỉ hoạt động cho các ứng dụng cụ thể ở Tầng 7.

## Liên kết liên quan
*   [[network-models|Mô hình OSI]]
*   [[my_knowlegde/entities/firewall|Tường lửa]]
*   [[network-security|Bảo mật mạng]]
