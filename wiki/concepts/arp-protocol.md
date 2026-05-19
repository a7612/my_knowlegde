---
sources: ["raw/Hack The Box/Introduction to Networking/Addressing - MAC Addresses.md"]
tags: ["networking", "protocols", "arp", "security"]
---

# Giao thức phân giải địa chỉ (ARP - Address Resolution Protocol)

**ARP** là giao thức dùng để ánh xạ địa chỉ **Tầng 3 (IP)** sang địa chỉ **Tầng 2 (MAC)**, cho phép các thiết bị trong cùng mạng LAN giao tiếp với nhau.

## 1. Cơ chế hoạt động
*   **ARP Request**: Khi thiết bị A muốn gửi dữ liệu cho thiết bị B nhưng chỉ biết IP, nó sẽ gửi một bản tin **Broadcast** hỏi: "Ai có IP này? Hãy trả lời cho tôi (MAC của A)".
*   **ARP Reply**: Thiết bị B có IP tương ứng sẽ gửi bản tin **Unicast** trả lời thiết bị A kèm theo địa chỉ MAC của mình.
*   **ARP Cache**: Các thiết bị lưu trữ kết quả ánh xạ vào bộ nhớ đệm (cache) để sử dụng cho các lần sau mà không cần hỏi lại.

## 2. Các loại bản tin ARP
*   **Request**: Quảng bá đến toàn mạng.
*   **Reply**: Phản hồi trực tiếp cho người hỏi.

## 3. Lỗ hổng bảo mật: ARP Spoofing
Do ARP được thiết kế mà không có cơ chế xác thực, kẻ tấn công có thể gửi các bản tin ARP Reply giả mạo để lừa thiết bị nạn nhân rằng địa chỉ MAC của kẻ tấn công là địa chỉ MAC của Gateway (Router).
*   **Hậu quả**: Kẻ tấn công có thể thực hiện tấn công **Man-in-the-Middle (MITM)**, nghe lén hoặc sửa đổi dữ liệu.
*   **Phòng chống**: Sử dụng Static ARP, Dynamic ARP Inspection (DAI) trên Switch, hoặc các giao thức bảo mật như IPSec/SSL.

## Liên kết liên quan
*   [[mac-address|Địa chỉ MAC]]
*   [[ipv4-address|Địa chỉ IPv4]]
*   [[addressing-and-routing|Định danh và Truyền thông]]
