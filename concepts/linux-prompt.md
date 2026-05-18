---
sources: ["raw/Hack The Box/Linux Fundamentals/The Shell - Prompt Description.md"]
tags: ["linux", "shell", "bash", "prompt", "ps1"]
---

# Mô tả Dòng nhắc Lệnh (Prompt Description)

Dòng nhắc lệnh (prompt) là dòng văn bản hiển thị trên terminal để cho biết hệ thống đã sẵn sàng nhận lệnh.

## Cấu trúc mặc định
Định dạng phổ biến của dòng nhắc Bash thường là:
`user@hostname:directory$`

* **`~` (Tilde)**: Đại diện cho thư mục nhà (Home directory) của người dùng.
* **`$` (Dollar sign)**: Biểu thị người dùng thông thường.
* **`#` (Hash sign)**: Biểu thị người dùng có quyền quản trị tối cao (**root**).

## Biến môi trường PS1
Biến `PS1` kiểm soát giao diện của dòng nhắc lệnh. Bạn có thể tùy chỉnh nó trong tệp `.bashrc`.

### Các ký tự đặc biệt phổ biến:
| Ký tự | Mô tả |
| --- | --- |
| `\u` | Tên người dùng hiện tại |
| `\h` | Tên máy chủ (hostname) |
| `\w` | Đường dẫn đầy đủ của thư mục làm việc hiện tại |
| `\d` | Ngày tháng (ví dụ: Mon Feb 6) |
| `\t` | Thời gian hiện tại (24 giờ) |
| `\n` | Dòng mới (newline) |

Việc tùy chỉnh dòng nhắc lệnh giúp terminal trở nên sinh động và cung cấp nhiều thông tin hữu ích ngay lập tức (như địa chỉ IP, thời gian, trạng thái lệnh trước đó).
