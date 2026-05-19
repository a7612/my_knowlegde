---
sources: ["raw/Hack The Box/Network Foundations/Networking Fundamentals - Network Concepts.md"]
tags: ["networking", "models", "osi", "tcp-ip"]
---

# Mô hình mạng (Network Models)

Để chuẩn hóa việc giao tiếp giữa các thiết bị và phần mềm từ các nhà cung cấp khác nhau, các mô hình tham chiếu như **ISO/OSI** và **TCP/IP** đã được xây dựng. Chúng biểu diễn các bit dữ liệu được truyền đi dưới dạng nội dung mà con người có thể hiểu được.

## Quá trình truyền gói tin (Packet Transfers)

### Đơn vị dữ liệu giao thức (PDU)
Trong hệ thống phân tầng, mỗi tầng trao đổi dữ liệu ở một định dạng khác nhau gọi là **PDU**.
*   **Tầng Ứng dụng**: Data (Dữ liệu).
*   **Tầng Giao vận**: Segment (Đoạn - TCP) hoặc Datagram (Gói dữ liệu - UDP).
*   **Tầng Internet/Mạng**: Packet (Gói tin).
*   **Tầng Liên kết**: Frame (Khung).
*   **Tầng Vật lý**: Bit (Nhị phân).

### Sự đóng gói (Encapsulation)
Trong quá trình truyền, mỗi tầng sẽ thêm một **Header** (tiêu đề) vào PDU từ tầng trên để kiểm soát và nhận diện gói tin. Quá trình này gọi là **Đóng gói (Encapsulation)**. Khi bên nhận nhận được dữ liệu, họ sẽ thực hiện quy trình ngược lại để mở gói dữ liệu ở từng tầng.

## Mô hình OSI (Open Systems Interconnection)
Mô hình **OSI** (hay **ISO/OSI**) là khung khái niệm gồm 7 tầng:

| Tầng | Chức năng chính |
| :--- | :--- |
| **7. Ứng dụng** | Kiểm soát nhập/xuất dữ liệu và cung cấp chức năng cho ứng dụng (HTTP, FTP). |
| **6. Trình diễn** | Chuyển đổi dữ liệu hệ thống sang định dạng chung (Mã hóa, nén). |
| **5. Phiên** | Kiểm soát kết nối logic, ngăn chặn đứt gãy kết nối. |
| **4. Giao vận** | Kiểm soát luồng đầu-cuối, phân đoạn dữ liệu và tránh tắc nghẽn (TCP, UDP). |
| **3. Mạng** | Thiết lập kết nối và định tuyến gói tin qua toàn bộ mạng (IP, ICMP). |
| **2. Liên kết dữ liệu** | Truyền tải tin cậy trên môi trường vật lý, chia luồng bit thành các Frame (MAC). |
| **1. Vật lý** | Truyền tín hiệu điện, quang hoặc sóng điện từ qua dây dẫn hoặc không dây. |

*Lưu ý: Tầng 1-4 là tầng hướng truyền tải (transport-oriented), tầng 5-7 là tầng hướng ứng dụng (application-oriented).*

## Mô hình TCP/IP (Internet Protocol Suite)
Đây là mô hình thực tế của Internet, gồm 4 tầng:

*   **4. Tầng Ứng dụng (Application)**: Cho phép ứng dụng truy cập dịch vụ của các tầng khác (DNS, HTTP).
*   **3. Tầng Giao vận (Transport)**: Cung cấp dịch vụ phiên (TCP) và datagram (UDP).
*   **2. Tầng Internet**: Chịu trách nhiệm định danh máy chủ, đóng gói và định tuyến (IP).
*   **1. Tầng Liên kết (Link)**: Đưa các gói tin lên môi trường mạng vật lý.

## So sánh OSI và TCP/IP
*   **Tính nghiêm ngặt**: OSI có các quy tắc và ranh giới tầng rất nghiêm ngặt, trong khi TCP/IP linh hoạt hơn.
*   **Tính phổ biến**: TCP/IP là xương sống thực tế của Internet, trong khi OSI thường được dùng làm mô hình tham chiếu lý thuyết.

## Tầm quan trọng đối với Chuyên gia Bảo mật (Pentesters)
Cả hai mô hình đều cực kỳ hữu ích:
*   **TCP/IP**: Giúp hiểu nhanh cách toàn bộ kết nối được thiết lập.
*   **OSI**: Giúp chia nhỏ và phân tích chi tiết từng phần của luồng dữ liệu, đặc biệt hữu ích khi thực hiện **Phân tích lưu lượng mạng (Network Traffic Analysis)** để can thiệp hoặc nghe lén.

## Liên kết liên quan
*   [[my_knowlegde/concepts/computer-network|Mạng máy tính]]
*   [[my_knowlegde/concepts/network-protocols|Giao thức mạng]]
*   [[my_knowlegde/concepts/network-security|Bảo mật mạng]]
