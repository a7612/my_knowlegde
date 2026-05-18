---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - Working with Web Services.md"]
tags: ["linux", "administration", "web-server", "apache", "curl", "wget", "http"]
---

# Làm việc với Dịch vụ Web (Working with Web Services)

Dịch vụ web là thành phần cốt lõi trong giao tiếp giữa trình duyệt và máy chủ. Linux cung cấp nhiều lựa chọn máy chủ web mạnh mẽ như Apache, Nginx và các công cụ dòng lệnh để tương tác với chúng.

## 1. Máy chủ Web Apache
Apache là một trong những máy chủ web phổ biến nhất nhờ tính mô-đun và khả năng mở rộng.
* **Cài đặt**: `sudo apt install apache2 -y`
* **Quản lý**: `sudo systemctl start apache2`
* **Cấu hình cổng**: Mặc định chạy ở cổng 80. Có thể đổi tại `/etc/apache2/ports.conf`.
* **Thư mục mặc định**: `/var/www/html`.
* **Mô-đun quan trọng**:
    * `mod_ssl`: Mã hóa giao tiếp.
    * `mod_proxy`: Điều phối lưu lượng (proxy).
    * `mod_rewrite`: Thay đổi URL linh hoạt.

## 2. Công cụ tương tác dòng lệnh
Các công cụ này cho phép phân tích nội dung web mà không cần trình duyệt GUI.
* **cURL**: Công cụ đa năng để truyền tải dữ liệu qua nhiều giao thức (HTTP, FTP, SFTP).
    * `curl http://localhost`: Trả về mã nguồn HTML của trang web.
    * `curl -I http://localhost`: Chỉ xem thông tin tiêu đề (headers) phản hồi.
* **Wget**: Trình quản lý tải xuống mạnh mẽ.
    * `wget http://url/file`: Tải tệp tin về máy cục bộ.

## 3. Máy chủ Web Python nhanh
Dùng để chia sẻ tệp nhanh chóng trong quá trình kiểm thử hoặc phát triển:
`python3 -m http.server 8000`
Lệnh này sẽ biến thư mục hiện tại thành gốc của một máy chủ web chạy tại cổng 8000.

Trong an ninh mạng, việc thành thạo các công cụ này giúp bạn thực hiện chuyển tệp (file transfer), quét lỗ hổng ứng dụng web và thiết lập các trang giả mạo (phishing) hiệu quả.
