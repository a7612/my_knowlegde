---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - Working with Files and Directories.md"]
tags: ["linux", "workflow", "file-management", "mkdir", "touch", "mv", "cp"]
---

# Quản lý Tệp tin và Thư mục (File and Directory Management)

Trong Linux, việc quản lý tệp tin và thư mục thông qua dòng lệnh mang lại sự hiệu quả và linh hoạt cao hơn so với giao diện đồ họa.

## Tạo mới
* **`touch <tên_file>`**: Tạo một tệp tin trống.
* **`mkdir <tên_thư_mục>`**: Tạo một thư mục mới.
    * `mkdir -p path/to/dir`: Tạo nhiều cấp thư mục cùng lúc (tạo cả các thư mục cha nếu chưa có).

## Di chuyển và Đổi tên
Lệnh **`mv`** (move) được dùng cho cả hai mục đích:
* **Đổi tên**: `mv old_name new_name`
* **Di chuyển**: `mv file_name path/to/destination/`

## Sao chép
Lệnh **`cp`** (copy) dùng để tạo bản sao:
* `cp source_file destination`: Sao chép tệp tin.
* `cp -r source_dir destination`: Sao chép thư mục (cần thêm tùy chọn `-r` để sao chép đệ quy).

## Xóa (Lưu ý quan trọng)
* **`rm <file>`**: Xóa tệp tin.
* **`rm -r <dir>`**: Xóa thư mục và toàn bộ nội dung bên trong.
* **`rmdir <dir>`**: Chỉ xóa được thư mục rỗng.

## Xem cấu trúc cây
* **`tree`**: Hiển thị cấu trúc thư mục và tệp tin dưới dạng sơ đồ cây trực quan.

Việc kết hợp các lệnh này giúp bạn tổ chức hệ thống tệp tin một cách khoa học và nhanh chóng.
