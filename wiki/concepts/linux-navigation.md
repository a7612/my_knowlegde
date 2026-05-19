---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - Navigation.md"]
tags: ["linux", "workflow", "navigation", "ls", "cd", "pwd"]
---

# Điều hướng trong Linux (Navigation)

Điều hướng là kỹ năng cơ bản để di chuyển và làm việc với các thư mục và tệp tin trong hệ điều hành Linux.

## Các lệnh cơ bản

| Lệnh | Mô tả |
| --- | --- |
| `pwd` | (Print Working Directory) Hiển thị đường dẫn thư mục hiện tại. |
| `ls` | Liệt kê nội dung trong thư mục. |
| `cd` | (Change Directory) Thay đổi thư mục làm việc. |

## Chi tiết lệnh `ls` (List)
Lệnh `ls` có nhiều tùy chọn để tùy biến đầu ra:
* `ls -l`: Hiển thị danh sách chi tiết (quyền hạn, chủ sở hữu, kích thước, thời gian).
* `ls -a`: Hiển thị tất cả các tệp, bao gồm cả tệp ẩn (bắt đầu bằng dấu chấm `.`).
* `ls -la`: Kết hợp hiển thị chi tiết và tệp ẩn.

### Giải thích đầu ra `ls -l`
Ví dụ: `drwxr-xr-x 2 user group 4096 Nov 13 17:37 Desktop`
* `d`: Loại tệp (d = thư mục, - = tệp tin).
* `rwxr-xr-x`: Quyền hạn truy cập.
* `2`: Số lượng liên kết cứng (hard links).
* `user`: Chủ sở hữu tệp.
* `group`: Nhóm sở hữu.
* `4096`: Kích thước (tính theo byte).
* `Nov 13 17:37`: Thời gian sửa đổi lần cuối.

## Di chuyển với `cd` (Change Directory)
* `cd /path/to/dir`: Di chuyển đến một đường dẫn tuyệt đối hoặc tương đối.
* `cd ..`: Quay lại thư mục cha.
* `cd -`: Quay lại thư mục làm việc trước đó.
* `cd ~` hoặc chỉ `cd`: Trở về thư mục nhà (Home directory).

## Phím tắt hữu ích
* **Tab**: Tự động hoàn thành tên tệp/thư mục. Nhấn Tab hai lần để liệt kê các gợi ý.
* **Ctrl + L**: Xóa sạch màn hình terminal (tương đương lệnh `clear`).
* **Ctrl + R**: Tìm kiếm lại các lệnh đã thực hiện trong lịch sử (history).
* **Mũi tên Lên/Xuống**: Duyệt qua lịch sử các lệnh đã dùng.
