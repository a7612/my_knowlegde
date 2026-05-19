---
sources: ["raw/Hack The Box/Network Foundations/Internet Architecture and Wireless Technologies - Wireless Networks.md", "raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Wireless Networks.md"]
tags: ["networking", "wireless", "wifi", "security", "wpa", "wep", "peap"]
---

# Mạng không dây (Wireless Networks)

Mạng không dây sử dụng sóng vô tuyến (Radio Frequency - RF) để truyền dữ liệu giữa các nút mạng mà không cần cáp vật lý, phổ biến nhất là qua công nghệ WiFi (IEEE 802.11).

## 1. Kết nối WiFi
Để tham gia mạng, thiết bị gửi một **Association Request** (Yêu cầu hiệp hội) tới Wireless Access Point (WAP). Gói tin này chứa:
*   **Địa chỉ MAC**: Định danh duy nhất của adapter không dây.
*   **SSID (Service Set Identifier)**: Tên mạng WiFi.
*   **Data rates**: Các tốc độ truyền dữ liệu mà thiết bị hỗ trợ.
*   **Channels**: Các kênh tần số thiết bị có thể liên lạc.
*   **Security protocols**: Các giao thức bảo mật hỗ trợ (WPA2, WPA3...).

## 2. Các giao thức mã hóa và Lỗ hổng

### WEP (Wired Equivalent Privacy)
*   **Đặc điểm**: Sử dụng thuật toán **RC4**. Có hai phiên bản chính:
    *   **WEP-40 (64)**: IV 24-bit + Khóa bí mật 40-bit.
    *   **WEP-104 (128)**: IV 24-bit + Khóa bí mật 80-bit.
*   **Lỗ hổng CRC**: Cơ chế kiểm tra lỗi CRC được tính toán trên **văn bản thuần (plaintext)** thay vì dữ liệu đã mã hóa. Điều này cho phép kẻ tấn công giải mã gói tin mà không cần biết khóa.
*   **Brute-force IV**: Do IV (Vector khởi tạo) nhỏ (24-bit), kẻ tấn công có thể thu thập đủ gói tin để bẻ khóa trong thời gian ngắn.

### WPA / WPA2 / WPA3
*   **WPA2/WPA3**: Sử dụng mã hóa mạnh **AES (128-bit)**. 
*   **Xác thực**: Hỗ trợ Pre-Shared Key (PSK) cho gia đình hoặc máy chủ 802.1X cho doanh nghiệp.

## 3. Các giao thức xác thực (Authentication)
*   **LEAP (Cisco)**: Sử dụng khóa chia sẻ (shared key) cho cả mã hóa và xác thực. Dễ bị tấn công từ điển.
*   **PEAP (Protected EAP)**: Sử dụng đường hầm **TLS** và chứng chỉ số để bảo vệ quá trình xác thực. An toàn hơn nhiều so với LEAP.

## 4. Các kiểu tấn công mạng không dây
*   **Disassociation Attack**: Gửi các khung hình "ngắt kết nối" giả mạo để buộc người dùng văng khỏi mạng. Có thể dùng để thu thập gói tin bắt tay (handshake) hoặc tiền đề cho tấn công MITM.
*   **Bẻ khóa WEP**: Khai thác yếu điểm của RC4 và IV.
*   **MAC Spoofing**: Giả mạo địa chỉ MAC để vượt qua bộ lọc truy cập.

## 5. Các biện pháp tăng cường bảo mật (Hardening)
1.  **Vô hiệu hóa quảng bá SSID**: Làm mạng ẩn đi (tuy vẫn có thể tìm thấy trong gói tin xác thực).
2.  **Sử dụng WPA3**: Tiêu chuẩn bảo mật mới nhất và mạnh nhất hiện nay.
3.  **Lọc địa chỉ MAC**: Chỉ cho phép thiết bị trong danh sách trắng kết nối.
4.  **Triển khai EAP-TLS**: Sử dụng chứng chỉ số cho từng thiết bị, cung cấp mức độ an toàn cao nhất cho doanh nghiệp.

## Liên kết liên quan
- [[network-security|Bảo mật mạng]]
- [[authentication-protocols|Giao thức xác thực]]
- [[my_knowlegde/entities/network-hardware|Thiết bị mạng]]
