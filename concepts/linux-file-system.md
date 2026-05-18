---
sources: ["raw/Hack The Box/Linux Fundamentals/Introduction - Linux Structure.md"]
tags: ["linux", "file-system", "fhs"]
---

# Hệ thống Tệp tin Linux (Linux File System)

Hệ điều hành Linux được cấu trúc theo một phân cấp hình cây, tuân theo tiêu chuẩn **Filesystem Hierarchy Standard (FHS)**.

## Cấu trúc thư mục tiêu chuẩn

| Đường dẫn | Mô tả |
| --- | --- |
| **`/`** | Thư mục gốc (Root), chứa toàn bộ các tệp tin cần thiết để khởi động hệ thống. |
| **`/bin`** | Chứa các tệp thực thi (binaries) của các lệnh thiết yếu. |
| **`/boot`** | Chứa bootloader, hạt nhân và các tệp cần thiết để khởi động OS. |
| **`/dev`** | Chứa các tệp thiết bị (device files) đại diện cho phần cứng đính kèm. |
| **`/etc`** | Chứa các tệp cấu hình hệ thống và ứng dụng. |
| **`/home`** | Thư mục lưu trữ riêng cho mỗi người dùng thông thường. |
| **`/lib`** | Chứa các thư viện dùng chung cần thiết cho quá trình khởi động. |
| **`/media`** | Điểm gắn (mount) cho các thiết bị lưu trữ ngoài như USB. |
| **`/mnt`** | Điểm gắn tạm thời cho các hệ thống tệp tin thông thường. |
| **`/opt`** | Chứa các tệp tin tùy chọn như công cụ của bên thứ ba. |
| **`/root`** | Thư mục nhà của người dùng quản trị tối cao (root user). |
| **`/sbin`** | Chứa các tệp thực thi dùng cho quản trị hệ thống (system binaries). |
| **`/tmp`** | Thư mục lưu trữ các tệp tạm thời, thường bị xóa khi khởi động lại. |
| **`/usr`** | Chứa các tệp thực thi, thư viện, tài liệu hướng dẫn (man files). |
| **`/var`** | Chứa các dữ liệu biến đổi như tệp nhật ký (log), hòm thư, tệp web. |
