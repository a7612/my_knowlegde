---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - File Descriptors and Redirections.md"]
tags: ["linux", "workflow", "redirection", "file-descriptors", "pipes"]
---

# Điều hướng và Chuyển hướng Dữ liệu (Redirections & Pipes)

Bộ mô tả tệp (File Descriptor - FD) là một tham chiếu giúp hạt nhân quản lý các hoạt động Nhập/Xuất (I/O).

## 3 Bộ mô tả tệp mặc định
1. **STDIN (0)**: Luồng dữ liệu đầu vào chuẩn (thường từ bàn phím).
2. **STDOUT (1)**: Luồng dữ liệu đầu ra chuẩn (thường hiển thị trên màn hình).
3. **STDERR (2)**: Luồng dữ liệu báo lỗi chuẩn.

## Chuyển hướng (Redirection)
Sử dụng các ký tự đặc biệt để hướng luồng dữ liệu:

| Ký tự | Mô tả |
| --- | --- |
| `>` | Ghi đè STDOUT vào một tệp (tạo mới hoặc xóa nội dung cũ). |
| `>>` | Thêm tiếp STDOUT vào cuối tệp hiện có. |
| `2>` | Chuyển hướng luồng lỗi STDERR (ví dụ: `2>/dev/null` để bỏ qua lỗi). |
| `<` | Sử dụng nội dung tệp làm STDIN cho một lệnh. |
| `<< EOF` | Chuyển hướng luồng nhập văn bản trực tiếp (stream) cho đến khi gặp từ khóa EOF. |

## Đường ống (Pipes)
Ký tự **`|`** (pipe) được dùng để lấy đầu ra (STDOUT) của chương trình này làm đầu vào (STDIN) cho chương trình kia.
* Ví dụ: `ls /etc | grep "net"` (liệt kê các tệp trong `/etc` và lọc ra những tệp chứa từ "net").

Việc kết hợp chuyển hướng và đường ống cho phép bạn xây dựng các dòng lệnh phức tạp để xử lý dữ liệu một cách cực kỳ mạnh mẽ.
