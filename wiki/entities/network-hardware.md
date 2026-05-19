---
sources: ["raw/Hack The Box/Network Foundations/Networking Fundamentals - Components of a Network.md"]
tags: ["networking", "hardware", "devices"]
---

# Thiết bị và Phần cứng Mạng (Network Hardware)

Một mạng máy tính được cấu thành từ nhiều thành phần phần cứng khác nhau, mỗi thành phần đóng một vai trò cụ thể trong việc truyền tải và quản lý dữ liệu.

## 1. Thiết bị đầu cuối (End Devices / Hosts)
Là các thiết bị mà người dùng tương tác trực tiếp để gửi hoặc nhận dữ liệu.
* **Ví dụ**: Máy tính cá nhân, điện thoại thông minh, máy tính bảng, thiết bị IoT (TV thông minh, camera).
* **Vai trò**: Điểm bắt đầu và điểm kết thúc của luồng dữ liệu.

## 2. Thiết bị trung gian (Intermediary Devices)
Đóng vai trò điều phối luồng dữ liệu giữa các thiết bị đầu cuối hoặc giữa các mạng khác nhau.

### [[router|Bộ định tuyến (Router)]]
* **Tầng OSI**: Tầng 3 (Mạng).
* **Chức năng**: Chuyển tiếp gói tin giữa các mạng khác nhau, xác định đường đi tốt nhất bằng bảng định tuyến và các giao thức như OSPF, BGP. Kết nối mạng LAN với Internet.
* **Tính năng**: Thường tích hợp tường lửa và quản lý lưu lượng.

### [[switch|Bộ chuyển mạch (Switch)]]
* **Tầng OSI**: Tầng 2 (Liên kết dữ liệu).
* **Chức năng**: Kết nối các thiết bị trong cùng một mạng LAN. Sử dụng địa chỉ [[mac-address|MAC]] để chuyển dữ liệu đến đúng cổng của thiết bị nhận, giúp giảm tắc nghẽn.

### [[hub|Bộ tập trung (Hub)]]
* **Tầng OSI**: Tầng 1 (Vật lý).
* **Chức năng**: Thiết bị cơ bản kết nối nhiều thiết bị. Nó phát sóng (broadcast) mọi dữ liệu nhận được tới tất cả các cổng, gây ra sự kém hiệu quả và dễ va chạm dữ liệu. Hiện nay đã lỗi thời và được thay thế bởi Switch.

### [[network-interface-card|Thẻ giao tiếp mạng (NIC)]]
* Thành phần phần cứng được cài đặt trong thiết bị để cho phép kết nối mạng.
* Mỗi NIC có một địa chỉ [[mac-address|MAC]] duy nhất. Có thể là NIC có dây (Ethernet) hoặc không dây (Wi-Fi).

## 3. Máy chủ (Servers)
Là các máy tính mạnh mẽ cung cấp dịch vụ cho các máy tính khác (máy khách - clients).
* **Các loại máy chủ**: Web Server, File Server, Mail Server, Database Server.
* **Mô hình Client-Server**: Máy chủ đợi yêu cầu từ máy khách và phản hồi dữ liệu tương ứng.

### [[ids|IDS]] / [[ips|IPS]] (Thiết bị phát hiện/ngăn chặn xâm nhập)
* **NIDS/NIPS**: Thiết bị phần cứng chuyên dụng đặt tại các điểm chiến lược trong mạng để kiểm tra lưu lượng đi qua.
* **HIDS/HIPS**: Giải pháp phần mềm chạy trên từng máy chủ hoặc thiết bị đầu cuối.

### [[cell-tower|Trạm phát sóng di động (Cell Tower)]]
* Cấu trúc chứa anten và thiết bị truyền thông để tạo ra các ô (cell) trong mạng di động.
* Bao gồm các loại: Macro cells (vùng rộng) và Micro/Small cells (vùng mật độ cao).

## 4. Phương tiện và Phần mềm mạng
* **Cáp và đầu nối**: Cáp Ethernet, đầu nối RJ-45, cáp quang.
* **[[firewall|Tường lửa phần mềm (Software Firewall)]]**: Ứng dụng bảo mật kiểm soát lưu lượng mạng dựa trên các quy tắc (ví dụ: IPTables trên Linux).
* **Phần mềm quản lý mạng**: Công cụ theo dõi hiệu suất, cấu hình và phân tích lỗi.
