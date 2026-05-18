---
sources: ["raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Vendor Specific Information.md"]
tags: ["networking", "entity", "cisco", "ios", "administration"]
---

# Hệ điều hành Cisco IOS

**Cisco IOS (Internetwork Operating System)** là hệ điều hành độc quyền chạy trên phần lớn các thiết bị mạng của Cisco như Router và Switch. Nó cung cấp các tính năng quản lý, định tuyến và bảo mật cần thiết cho hạ tầng mạng hiện đại.

## 1. Đặc điểm và Tính năng chính
*   **Hỗ trợ đa giao thức**: IPv4, IPv6, OSPF, BGP, RIP, STP, VTP.
*   **Chất lượng dịch vụ (QoS)**: Ưu tiên lưu lượng quan trọng (như Voice, Video).
*   **Bảo mật**: Tích hợp danh sách kiểm soát truy cập (ACL), mã hóa và xác thực.
*   **Quản trị**: Thông qua giao diện dòng lệnh (**CLI**) hoặc giao diện đồ họa (GUI).

## 2. Các chế độ mật khẩu trong IOS
| Loại mật khẩu | Mục đích |
| :--- | :--- |
| **User Password** | Hạn chế truy cập ban đầu khi đăng nhập vào thiết bị. |
| **Enable Password** | Dùng để chuyển sang chế độ đặc quyền (Privileged mode) để xem cấu hình. |
| **Enable Secret** | Mật khẩu cấp cao nhất để vào chế độ đặc quyền, được lưu trữ dưới dạng mã hóa mạnh. |
| **Secret** | Dùng để bảo mật cho các dịch vụ cụ thể hoặc quản trị từ xa. |

## 3. Giao thức khám phá Cisco (CDP)
**CDP (Cisco Discovery Protocol)** là giao thức Tầng 2 giúp các thiết bị Cisco tự động khám phá và thu thập thông tin về các thiết bị Cisco khác đang kết nối trực tiếp với nó.
*   **Thông tin thu thập**: Tên thiết bị, địa chỉ IP, tên cổng kết nối, phiên bản phần mềm, nền tảng phần cứng.
*   **Lưu ý**: Thông tin này rất hữu ích cho quản trị viên nhưng cũng có thể bị kẻ tấn công lợi dụng để thu thập thông tin mạng (reconnaissance).

## 4. Giao thức cây bao trùm (STP)
STP giúp đảm bảo mạng không bị vòng lặp (loops) khi có nhiều kết nối dự phòng giữa các Switch. Nó ngăn chặn tình trạng "bão quảng bá" (broadcast storms) có thể làm tê liệt mạng.

## Dấu hiệu nhận biết (Fingerprinting)
Khi truy cập từ xa qua Telnet hoặc SSH, các thiết bị Cisco IOS thường phản hồi bằng dòng thông báo:
`User Access Verification`
`Password:`

## Liên kết liên quan
- [[vlans|Mạng cục bộ ảo (VLAN)]]
- [[network-hardware|Thiết bị mạng]]
- [[linux-network-configuration|Cấu hình mạng Linux]]
