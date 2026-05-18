---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - User Management.md"]
tags: ["linux", "administration", "users", "groups", "sudo"]
---

# Quản lý Người dùng (User Management)

Quản lý người dùng hiệu quả là khía cạnh nền tảng của quản trị hệ thống Linux. Quản trị viên cần tạo tài khoản, gán người dùng vào nhóm để thực thi các kiểm soát truy cập phù hợp.

## 1. Các lệnh quản lý cơ bản

| Lệnh | Mô tả |
| --- | --- |
| **`sudo`** | Thực thi lệnh với quyền của người dùng khác (mặc định là root). |
| **`su`** | Chuyển sang danh tính người dùng khác (mặc định là root) và thực thi shell mới. |
| **`useradd`** | Tạo người dùng mới. Dùng `-m` để tự động tạo thư mục nhà (home). |
| **`userdel`** | Xóa người dùng. Dùng `-r` để xóa cả thư mục nhà. |
| **`usermod`** | Chỉnh sửa thông tin người dùng (ví dụ: `-L` để khóa tài khoản, `-aG` để thêm vào nhóm). |
| **`addgroup`** | Tạo một nhóm mới trên hệ thống. |
| **`delgroup`** | Xóa một nhóm khỏi hệ thống. |
| **`passwd`** | Thay đổi mật khẩu người dùng. |

## 2. Đặc quyền Sudo (Superuser Do)
Lệnh **[[sudo|sudo]]** cho phép người dùng thực thi các lệnh quản trị mà không cần đăng nhập trực tiếp bằng tài khoản `root`. Đây là một biện pháp bảo mật tốt nhất.
* Các quyền sudo được cấu hình trong tệp `/etc/sudoers`.
* Tệp `/etc/shadow` chứa các bản băm mật khẩu được mã hóa và chỉ có thể truy cập bởi root hoặc qua sudo.

## 3. Quản lý nhóm (Groups)
Nhóm được sử dụng để gán quyền cho nhiều người dùng cùng lúc. Một người dùng có thể thuộc nhiều nhóm khác nhau.
* Việc kiểm tra quyền hạn của một người dùng có thể thực hiện qua lệnh **`id`**.

Nắm vững cách vận hành tài khoản người dùng, quyền hạn và cơ chế xác thực giúp xác định các lỗ hổng bảo mật và đánh giá tình trạng an ninh của hệ thống.
