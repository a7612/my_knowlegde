---
sources: ["raw/Hack The Box/Network Foundations/Internet Architecture and Wireless Technologies - Internet Architecture.md"]
tags: ["networking", "architecture", "p2p", "client-server", "cloud", "sdn"]
---

# Kiến trúc Internet (Internet Architecture)

Kiến trúc Internet mô tả cách dữ liệu được tổ chức, truyền tải và quản lý qua các mạng. Các mô hình kiến trúc khác nhau giải quyết các vấn đề khác nhau về khả năng mở rộng, hiệu suất và bảo mật.

## 1. Mô hình Khách - Chủ (Client-Server Architecture)
Đây là mô hình phổ biến nhất trên Internet.
* **[[client|Máy khách (Client)]]**: Các thiết bị của người dùng gửi yêu cầu (ví dụ: trình duyệt web).
* **[[server|Máy chủ (Server)]]**: Các máy tính mạnh mẽ phản hồi yêu cầu (ví dụ: web server).

### Các phân lớp kiến trúc (Tiered Architecture)
* **Kiến trúc 1 tầng (Single-Tier)**: Client, server và database nằm trên cùng một máy.
* **Kiến trúc 2 tầng (Two-Tier)**: Chia thành Client (giao diện) và Server (dữ liệu).
* **Kiến trúc 3 tầng (Three-Tier)**: Thêm một tầng trung gian là **Application Server** để xử lý logic nghiệp vụ.
* **Kiến trúc N tầng (N-Tier)**: Sử dụng nhiều tầng máy chủ ứng dụng cho các hệ thống phức tạp.

## 2. Mô hình Ngang hàng (P2P - Peer-to-Peer Architecture)
Mỗi nút trong mạng vừa đóng vai trò là máy khách, vừa là máy chủ.
* **Đặc điểm**: Các thiết bị giao tiếp trực tiếp với nhau để chia sẻ tài nguyên (tệp tin, băng thông) mà không cần máy chủ trung tâm.
* **Ví dụ**: Torrent (BitTorrent), blockchain.
* **Ưu điểm**: Khả năng phục hồi cao, phân phối chi phí tài nguyên.

## 3. Mô hình Hy-brid (Hybrid Architecture)
Kết hợp giữa Client-Server và P2P.
* **Cơ chế**: Sử dụng máy chủ trung tâm để điều phối và xác thực, nhưng việc truyền dữ liệu thực tế diễn ra trực tiếp giữa các thiết bị ngang hàng.
* **Ví dụ**: Các ứng dụng gọi video (như Zoom, Skype).

## 4. Kiến trúc Đám mây (Cloud Architecture)
Cung cấp tài nguyên máy tính (server, lưu trữ, ứng dụng) theo nhu cầu qua Internet thông qua các nhà cung cấp bên thứ ba (AWS, Azure, Google Cloud).
* **Đặc điểm cốt lõi**:
    * Tự phục vụ theo nhu cầu.
    * Truy cập mạng rộng rãi.
    * Nhóm tài nguyên (Resource pooling).
    * Khả năng co giãn nhanh chóng (Elasticity).
    * Dịch vụ được đo lường (trả phí theo mức sử dụng).
* **Mô hình phổ biến**: **SaaS** (Software as a Service) - ví dụ: Google Drive, Dropbox.

## 5. Mạng điều khiển bằng phần mềm (SDN - Software-Defined Networking)
Tách biệt **Mặt phẳng điều khiển (Control Plane)** - nơi đưa ra quyết định định tuyến - khỏi **Mặt phẳng dữ liệu (Data Plane)** - nơi thực hiện chuyển tiếp lưu lượng.
* **Cơ chế**: Quản lý tập trung thông qua một bộ điều khiển phần mềm (SDN Controller), giúp mạng linh hoạt và dễ lập trình hơn.

## 6. Định danh trên Internet (Naming on the Internet)

Khi truy cập tài nguyên trên Internet, chúng ta sử dụng các địa chỉ định danh.

*   **FQDN (Fully Qualified Domain Name)**: Chỉ định địa chỉ chính xác của một "tòa nhà" (máy chủ). 
    *   Ví dụ: `www.hackthebox.com`
*   **URL (Uniform Resource Locator)**: Không chỉ chỉ định "tòa nhà" mà còn chỉ rõ "tầng", "phòng", "người nhận" bên trong đó.
    *   Ví dụ: `https://www.hackthebox.com/example?id=123`
    *   Thành phần của URL bao gồm giao thức (`https`), FQDN (`www.hackthebox.com`), đường dẫn tài nguyên (`/example`) và các tham số (`?id=123`).

Khi gửi một gói tin, **[[dns-service|Dịch vụ tên miền (DNS)]]** sẽ đóng vai trò như danh bạ điện thoại, giúp chuyển đổi các tên miền dễ nhớ này thành địa chỉ IP vật lý để các thiết bị có thể tìm thấy nhau.
