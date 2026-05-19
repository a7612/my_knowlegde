---
sources: ["raw/Hack The Box/Network Foundations/Network Communication and Addressing - Domain Name System (DNS).md"]
tags: ["networking", "services", "dns", "name-resolution"]
---

# Hệ thống Phân giải Tên miền (DNS - Domain Name System)

[[dns-service|DNS]] đóng vai trò như một "cuốn danh bạ" của Internet, giúp chuyển đổi các tên miền dễ nhớ (như `www.google.com`) thành địa chỉ IP số mà máy tính có thể hiểu được.

## Phân cấp DNS (DNS Hierarchy)
DNS được tổ chức theo cấu trúc hình cây:
* **Root Servers (Máy chủ gốc)**: Đỉnh cao nhất của hệ thống phân cấp.
* **Top-Level Domains (TLDs)**: Các đuôi tên miền như `.com`, `.org`, `.net` hoặc mã quốc gia như `.vn`.
* **Second-Level Domains**: Tên thương hiệu, ví dụ `google` trong `google.com`.
* **Subdomains / Hostname**: Ví dụ `www` hoặc `mail`.

## Quy trình phân giải DNS (DNS Resolution)
Khi bạn nhập một tên miền vào trình duyệt:
1. **Kiểm tra bộ nhớ đệm (Cache)**: Máy tính kiểm tra xem đã biết địa chỉ IP đó chưa.
2. **Truy vấn Recursive DNS Server**: Thường do ISP cung cấp.
3. **Truy vấn Root Server**: Trỏ tới máy chủ TLD tương ứng.
4. **Truy vấn TLD Name Server**: Trỏ tới máy chủ định danh có thẩm quyền (Authoritative Name Server).
5. **Truy vấn Authoritative Name Server**: Trả về địa chỉ IP chính xác của tên miền.
6. **Trả kết quả**: Recursive server trả địa chỉ IP về cho máy tính để thiết lập kết nối.

Quá trình này diễn ra chỉ trong một phần nhỏ của giây, giúp người dùng truy cập tài nguyên mạng một cách liền mạch.
