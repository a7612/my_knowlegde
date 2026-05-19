---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - Find Files and Directories.md"]
tags: ["linux", "workflow", "searching", "find", "locate"]
---

# Tìm kiếm Tệp tin và Thư mục (Searching)

Việc tìm kiếm nhanh chóng các tệp cấu hình, script hoặc tệp nhạy cảm là kỹ năng quan trọng trong quản trị hệ thống và an ninh mạng.

## 1. Lệnh `which`
Dùng để tìm đường dẫn của một chương trình thực thi. Giúp kiểm tra xem một công cụ (như python, nc, curl) có được cài đặt hay không.
* Ví dụ: `which python`

## 2. Lệnh `find`
Công cụ tìm kiếm mạnh mẽ và linh hoạt nhất, cho phép lọc theo nhiều tiêu chí.
* **Cú pháp**: `find <vị_trí> <tùy_chọn>`
* **Các tùy chọn phổ biến**:
    * `-type f` (tệp) hoặc `-type d` (thư mục).
    * `-name "*.conf"`: Tìm theo tên (sử dụng wildcard).
    * `-user root`: Tìm theo chủ sở hữu.
    * `-size +20k`: Tìm theo kích thước (lớn hơn 20KB).
    * `-newermt 2024-01-01`: Tìm tệp mới hơn ngày chỉ định.
    * `-exec <lệnh> {} \;`: Thực thi một lệnh lên từng kết quả tìm thấy.

## 3. Lệnh `locate`
Tìm kiếm nhanh hơn `find` vì nó tra cứu trong một cơ sở dữ liệu địa phương (`updatedb`).
* **Lưu ý**: Cần chạy `sudo updatedb` để cập nhật dữ liệu mới nhất.
* Mặc dù nhanh nhưng `locate` không có nhiều tùy chọn lọc chi tiết như `find`.

Việc nắm vững các công cụ tìm kiếm giúp bạn nhanh chóng định vị các tài nguyên quan trọng trên một hệ thống xa lạ.
