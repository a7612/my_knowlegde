---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - Package Management.md"]
tags: ["linux", "administration", "apt", "dpkg", "git"]
---

# Quản lý Gói phần mềm (Package Management)

Hệ thống quản lý gói giúp cài đặt, cập nhật, gỡ bỏ và duy trì phần mềm trên Linux một cách tự động và nhất quán. Các gói phần mềm là các kho lưu trữ chứa tệp thực thi, cấu hình và thông tin về sự phụ thuộc (dependencies).

## 1. Các công cụ quản lý phổ biến

| Công cụ | Mô tả |
| --- | --- |
| **`apt`** | Giao diện dòng lệnh cấp cao cho Debian/Ubuntu, tự động xử lý các gói phụ thuộc. |
| **`dpkg`** | Công cụ cấp thấp để quản lý trực tiếp các tệp `.deb`. |
| **`aptitude`** | Một lựa chọn thay thế cho `apt` với giao diện tương tác hơn. |
| **`snap`** | Hệ thống cài đặt gói đóng gói sẵn (containerized), hỗ trợ nhiều distro. |
| **`pip`** | Trình cài đặt gói cho ngôn ngữ Python. |
| **`git`** | Hệ thống quản lý phiên bản, thường dùng để tải mã nguồn trực tiếp từ GitHub. |

## 2. Advanced Package Tool (APT)
Đây là công cụ phổ biến nhất trên các hệ thống dựa trên Debian (như Ubuntu, Parrot OS).
* **Kho lưu trữ (Repositories)**: Danh sách các máy chủ chứa phần mềm được lưu tại `/etc/apt/sources.list`.
* **Cập nhật danh sách gói**: `sudo apt update`
* **Cài đặt gói**: `sudo apt install <tên_gói> -y`
* **Tìm kiếm trong bộ nhớ đệm**: `apt-cache search <từ_khóa>`
* **Hiển thị thông tin gói**: `apt-cache show <tên_gói>`

## 3. Quy trình làm việc thực tế
1. **Cập nhật hệ thống**: Luôn chạy `sudo apt update` để lấy thông tin mới nhất từ kho lưu trữ.
2. **Cài đặt**: Dùng `apt install` để tự động tải và cài các gói phụ thuộc.
3. **Cài đặt thủ công**: Nếu có tệp `.deb` riêng lẻ, dùng `sudo dpkg -i <tên_file>.deb`. Nếu thiếu phụ thuộc, có thể dùng `sudo apt install -f` để sửa lỗi.
4. **Tải từ mã nguồn**: Sử dụng `git clone <url_github>` để tải mã nguồn các công cụ từ GitHub về máy.

Việc hiểu rõ cách quản lý gói giúp bạn duy trì hệ thống luôn được cập nhật, bảo mật và trang bị đầy đủ các công cụ cần thiết cho công việc (đặc biệt là trong pentest).
