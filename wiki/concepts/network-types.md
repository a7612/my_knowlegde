---
sources: ["raw/Hack The Box/Introduction to Networking/Networking Structure - Network Types.md"]
tags: ["networking", "wan", "lan", "vpn"]
---

# Các loại mạng máy tính (Network Types)

Mạng máy tính có thể được phân loại dựa trên phạm vi địa lý, công nghệ kết nối và mục đích sử dụng.

## 1. Các thuật ngữ phổ biến (Common Terminology)

| Loại mạng | Viết tắt | Định nghĩa |
| :--- | :--- | :--- |
| **Mạng diện rộng** | WAN | Internet hoặc tập hợp nhiều mạng LAN liên kết lại. Sử dụng các giao thức định tuyến như BGP. |
| **Mạng cục bộ** | LAN | Mạng nội bộ trong phạm vi nhỏ (nhà ở, văn phòng). Sử dụng dải IP nội bộ (RFC 1918). |
| **Mạng cục bộ không dây** | WLAN | Mạng LAN sử dụng Wi-Fi để kết nối không cần cáp. |
| **Mạng riêng ảo** | VPN | Kết nối người dùng hoặc các địa điểm mạng vào một mạng LAN duy nhất thông qua Internet. |

## 2. Tìm hiểu sâu về VPN

VPN có mục tiêu chung là làm cho người dùng cảm thấy như họ đang được cắm trực tiếp vào một mạng khác.
*   **Site-To-Site VPN**: Kết nối toàn bộ dải mạng của hai địa điểm khác nhau (thường dùng Router hoặc Firewall).
*   **Remote Access VPN**: Máy khách tạo giao diện ảo để truy cập mạng công ty (ví dụ: OpenVPN). 
    *   *Split-Tunnel VPN*: Chỉ lưu lượng truy cập các mạng cụ thể mới đi qua VPN, còn lại đi trực tiếp ra Internet.
*   **SSL VPN**: Thực hiện trực tiếp qua trình duyệt web, thường để truyền phát ứng dụng hoặc phiên desktop (ví dụ: Pwnbox).

## 3. Các thuật ngữ học thuật (Book Terms)

Các thuật ngữ này thường được dùng trong các kỳ thi hoặc tài liệu lý thuyết:
*   **GAN (Global Area Network)**: Mạng toàn cầu (Internet), kết nối qua cáp quang biển hoặc vệ tinh.
*   **MAN (Metropolitan Area Network)**: Mạng đô thị, kết nối các LAN trong cùng một thành phố với tốc độ cao.
*   **PAN / WPAN (Personal Area Network)**: Mạng cá nhân trong phạm vi vài mét (ví dụ: Bluetooth kết nối điện thoại và tai nghe).

## Liên kết liên quan
*   [[computer-network|Mạng máy tính]]
*   [[internet-architecture|Kiến trúc Internet]]
*   [[proxies|Máy chủ ủy quyền (Proxies)]]
