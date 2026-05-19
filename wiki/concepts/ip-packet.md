---
sources: ["raw/Hack The Box/Introduction to Networking/Connection Establishment - TCP UDP Connections.md", "raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Common Protocols.md"]
tags: ["networking", "layer3", "ip", "header", "packet", "ttl", "traceroute"]
---

# Gói tin IP (IP Packet)

Gói tin IP là đơn vị dữ liệu cơ bản ở **Tầng Mạng (Layer 3)** của mô hình OSI, dùng để truyền tải thông tin giữa các máy tính. Nó bao gồm phần tiêu đề (Header) và phần dữ liệu (Payload).

## 1. Cấu trúc Tiêu đề IP (IP Header)
Tiêu đề IP chứa các trường thông tin quan trọng để định tuyến và xử lý gói tin:

| Trường | Mô tả |
| :--- | :--- |
| **Version** | Phiên bản IP (v4 hoặc v6). |
| **IHL** | Độ dài tiêu đề (Internet Header Length). |
| **Total Length** | Tổng độ dài toàn bộ gói tin (Header + Payload). |
| **Identification (IP ID)** | Số định danh dùng để nhận diện các mảnh của một gói tin bị phân đoạn. |
| **Flags & Fragment Offset** | Kiểm soát và xác định vị trí các mảnh gói tin khi bị phân mảnh. |
| **TTL (Time to Live)** | Giới hạn thời gian tồn tại của gói tin trên mạng để tránh vòng lặp vô hạn. |
| **Protocol** | Xác định giao thức tầng trên (TCP: 6, UDP: 17, ICMP: 1). |
| **Checksum** | Kiểm tra lỗi trong tiêu đề. |
| **Source/Destination IP** | Địa chỉ IP của người gửi và người nhận. |

### Dấu vân tay hệ điều hành qua TTL (OS Fingerprinting)
Dựa vào giá trị TTL mặc định của một gói tin phản hồi (như lệnh `ping`), ta có thể dự đoán hệ điều hành của mục tiêu:
*   **Windows** (2000/XP/Vista/7/10/11): TTL mặc định là **128**.
*   **Linux / macOS**: TTL mặc định là **64**.
*   **Solaris**: TTL mặc định là **255**.
*   *Lưu ý*: Giá trị này sẽ giảm đi 1 đơn vị sau mỗi bước nhảy (hop) qua một Router. Ví dụ: Nếu `ping` thấy TTL là 122, có thể đó là Windows và cách ta 6 hops.

## 2. Các kỹ thuật và tính năng nâng cao
### Trường Record-Route
Trường này cho phép ghi lại lộ trình các thiết bị mà gói tin đi qua. Khi sử dụng lệnh `ping -R`, gói tin ICMP Echo Reply sẽ liệt kê danh sách IP của tất cả các Router trên đường đi.

### Kỹ thuật Traceroute
*   **Phương thức TCP (Windows - tracert)**: Gửi gói tin TCP SYN với TTL tăng dần (bắt đầu từ 1). Mỗi Router sẽ phản hồi lỗi `ICMP Time-Exceeded` cho đến khi gói tin chạm tới đích và nhận được `TCP SYN/ACK` hoặc `TCP RST`.
*   **Phương thức UDP (Linux/Unix - traceroute)**: Gửi các gói tin UDP đến các cổng không phổ biến trên máy đích. Khi tới đích, máy mục tiêu sẽ phản hồi lỗi `ICMP Destination Unreachable` và `Port Unreachable`.

### Phân tích lưu lượng qua IP ID
Trong quá trình **Network Sniffing**, nếu hai địa chỉ IP khác nhau gửi các gói tin có số **IP ID** liên tiếp (ví dụ: 1337, 1338, 1339...), điều đó cho thấy hai địa chỉ này thuộc về cùng một máy chủ vật lý (Multi-homed host).

## 3. Các cuộc tấn công liên quan
*   **Blind Spoofing**: Kẻ tấn công gửi gói tin giả mạo địa chỉ nguồn. Để thành công, kẻ tấn công phải đoán đúng số thứ tự khởi tạo (**Initial Sequence Number - ISN**) trong tiêu đề TCP để thiết lập kết nối giả mà không cần nhận phản hồi thực.
*   **IP Spoofing**: Giả mạo địa chỉ IP nguồn trong Header để vượt qua các bộ lọc bảo mật hoặc thực hiện tấn công từ chối dịch vụ (DoS).

## Liên kết liên quan
- [[ipv4-address|Địa chỉ IPv4]]
- [[network-protocols|Giao thức mạng (TCP/UDP)]]
- [[icmp-protocol|Giao thức ICMP]]
- [[addressing-and-routing|Định danh và Truyền thông]]
