---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - Containerization.md"]
tags: ["linux", "administration", "containers", "docker", "lxc", "virtualization"]
---

# Công nghệ Đóng gói (Containerization)

Đóng gói (Containerization) là quá trình đóng gói ứng dụng và các thành phần phụ thuộc vào một môi trường cô lập gọi là **container**. So với máy ảo (VM), container nhẹ hơn vì chia sẻ chung nhân (kernel) của hệ điều hành máy chủ.

## 1. Docker
Docker là nền tảng phổ biến nhất để tự động hóa việc triển khai ứng dụng dưới dạng container.
* **Hình ảnh (Images)**: Các mẫu chỉ đọc dùng để tạo container. Định nghĩa qua **Dockerfile**.
* **Kho lưu trữ (Docker Hub)**: Thư viện trực tuyến chứa hàng triệu hình ảnh đóng gói sẵn.
* **Các lệnh cơ bản**:
    * `docker ps`: Liệt kê các container đang chạy.
    * `docker run -p 8080:80 image_name`: Chạy container và ánh xạ cổng máy chủ (8080) vào cổng container (80).
    * `docker logs <ID>`: Xem nhật ký của container.

## 2. Linux Containers (LXC)
LXC là công nghệ ảo hóa cấp hệ điều hành truyền thống hơn Docker.
* **Đặc điểm**: Tập trung vào việc tạo ra các môi trường Linux đầy đủ (giống máy ảo nhẹ) thay vì chỉ chạy một ứng dụng duy nhất như Docker.
* **Cơ chế**: Sử dụng `cgroups` (giới hạn tài nguyên) và `namespaces` (cô lập tiến trình, mạng, tệp tin).
* **Quản lý**: Dùng các lệnh như `lxc-ls`, `lxc-start`, `lxc-attach`.

## 3. So sánh Docker và LXC

| Đặc điểm | Docker | LXC |
| --- | --- | --- |
| Tập trung | Ứng dụng/Microservices | Hệ điều hành đầy đủ |
| Tính di động | Cực cao (Docker Hub) | Thấp hơn (phụ thuộc cấu hình máy chủ) |
| Bảo mật | Tốt (mặc định cô lập mạnh) | Cần cấu hình thêm để đạt mức tương đương |

## 4. Ứng dụng trong An ninh mạng
* **Môi trường thử nghiệm**: Chạy các ứng dụng dễ tổn thương để thực hành tấn công mà không làm hại máy thật.
* **Cô lập mã độc**: Chạy mã nghi ngờ trong container để quan sát hành vi.
* **Leo thang đặc quyền**: Container cấu hình sai (như Docker socket gắn kết vào container) có thể là vector để chiếm quyền máy chủ.

Containerization là kỹ năng không thể thiếu trong kỷ nguyên DevOps và Cloud Security hiện nay.
