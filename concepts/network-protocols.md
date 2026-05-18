---
sources: ["raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Common Protocols.md", "raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Networking Key Terminology.md", "raw/Hack The Box/Introduction to Networking/Connection Establishment - TCP UDP Connections.md"]
tags: ["networking", "protocols", "tcp", "udp", "icmp", "voip", "cdp", "stp"]
---

# Giao thức mạng (Network Protocols)

Giao thức mạng là tập hợp các quy tắc chuẩn hóa (được định nghĩa trong các RFC) quy định cách các thiết bị trên mạng giao tiếp với nhau, đảm bảo tính nhất quán và tin cậy.

## 1. Hai loại kết nối chính

### TCP (Transmission Control Protocol)
*   **Đặc điểm**: Hướng kết nối (connection-oriented). Thiết lập kết nối qua quy trình **Bắt tay ba bước (Three-Way Handshake)**.
*   **Ưu điểm**: Tin cậy cao, đảm bảo dữ liệu đến đúng thứ tự và không lỗi.
*   **Ứng dụng**: Các dịch vụ cần độ chính xác tuyệt đối như Web, Email, Truyền tệp.

### UDP (User Datagram Protocol)
*   **Đặc điểm**: Không hướng kết nối (connectionless). Gửi các gói tin (**Datagrams**) trực tiếp mà không cần thiết lập trước.
*   **Ưu điểm**: Tốc độ rất nhanh, độ trễ thấp.
*   **Ứng dụng**: Truyền phát thời gian thực (Video, Game), VoIP, DNS.

## 2. Danh mục các giao thức phổ biến

| Giao thức | Cổng | Loại | Mô tả |
| :--- | :--- | :--- | :--- |
| **SSH** | 22 | TCP | Đăng nhập và thực thi lệnh từ xa bảo mật. |
| **Telnet** | 23 | TCP | Đăng nhập từ xa (không mã hóa - không an toàn). |
| **DNS** | 53 | TCP/UDP | Phân giải tên miền sang địa chỉ IP. |
| **HTTP / HTTPS** | 80 / 443 | TCP | Truyền tải nội dung trang web (HTTPS có mã hóa). |
| **FTP** | 20, 21 | TCP | Giao thức truyền tệp tin. |
| **SMB** | 445 | TCP | Chia sẻ tệp và máy in trong mạng Windows. |
| **NFS** | 111, 2049 | TCP/UDP | Chia sẻ tệp qua mạng trong môi trường Linux/Unix. |
| **DHCP** | 67, 68 | UDP | Cấp phát địa chỉ IP động cho thiết bị. |
| **SNMP** | 161, 162 | UDP | Giám sát và quản lý các thiết bị mạng. |
| **RDP** | 3389 | TCP/UDP | Điều khiển máy tính từ xa (Windows). |
| **SIP** | 5060, 5061 | TCP/UDP | Thiết lập cuộc gọi VoIP. |
| **BGP / OSPF** | 179 / 89 | TCP | Các giao thức định tuyến mạng. |
| **VNC** | 5900 | TCP | Chia sẻ màn hình đồ họa. |

## 3. Thoại qua IP (VoIP)
Sử dụng các giao thức báo hiệu để quản lý cuộc gọi qua mạng IP.
*   **SIP (Session Initiation Protocol)**: Phổ biến nhất. Sử dụng các phương thức như:
    *   `INVITE`: Khởi tạo phiên làm việc.
    *   `ACK`: Xác nhận đã nhận được INVITE.
    *   `BYE`: Kết thúc phiên làm việc.
    *   `OPTIONS`: Truy vấn khả năng của máy chủ/người dùng (có thể dùng để liệt kê người dùng hợp lệ).
*   **H.323**: Bộ tiêu chuẩn cũ hơn cho truyền thông đa phương tiện.

## 4. Các giao thức tầng liên kết dữ liệu (Layer 2)
### Cisco Discovery Protocol (CDP)
Giao thức độc quyền của Cisco dùng để thu thập thông tin về các thiết bị Cisco kết nối trực tiếp.
*   **Thông tin thu thập**: Tên thiết bị, địa chỉ IP, cổng kết nối, phiên bản hệ điều hành (IOS), nền tảng phần cứng.
*   **Ghi chú**: Có thể bị kẻ tấn công lợi dụng để thu thập thông tin hạ tầng mạng.

### Spanning Tree Protocol (STP)
Ngăn chặn vòng lặp (loops) trong mạng có nhiều kết nối dư thừa giữa các Switch.
*   **Cơ chế**: Tự động vô hiệu hóa các đường liên kết dư thừa để tạo ra một cấu trúc cây không vòng lặp.
*   **Biến thể**: **Rapid STP (802.1w)** giúp mạng hội tụ nhanh hơn khi có sự cố.

## 5. Giao thức ICMP
Dùng để báo lỗi và chẩn đoán mạng (Ping, Traceroute).
*   **Thông điệp quan trọng**:
    *   `Destination Unreachable`: Không thể tới đích.
    *   `Time Exceeded`: Gói tin hết hạn (TTL = 0).
    *   `Redirect`: Router thông báo nên đi theo đường khác tối ưu hơn.

## Liên kết liên quan
- [[network-models|Mô hình mạng (OSI & TCP/IP)]]
- [[ip-packet|Gói tin IP]]
- [[wireless-networks|Mạng không dây]]
- [[vlans|Mạng cục bộ ảo (VLAN)]]

