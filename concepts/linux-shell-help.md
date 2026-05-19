---
sources: ["raw/Hack The Box/Linux Fundamentals/The Shell - Getting Help.md", "raw/man7.org/intro(1) - Linux manual page.md", "raw/man7.org/intro(2) - Linux manual page.md", "raw/man7.org/intro(3) - Linux manual page.md", "raw/man7.org/intro(4) - Linux manual page.md", "raw/man7.org/intro(5) - Linux manual page.md", "raw/man7.org/intro(6) - Linux manual page.md", "raw/man7.org/intro(7) - Linux manual page.md", "raw/man7.org/intro(8) - Linux manual page.md"]
tags: ["linux", "shell", "help", "man", "apropos"]
---

# Cách nhận trợ giúp trong Linux (Getting Help)

Khi làm việc với các công cụ trên dòng lệnh Linux, việc làm quen với các tham số và tùy chọn là rất quan trọng. Có nhiều cách để tìm hiểu về một công cụ ngay trong terminal.

## 1. Trang hướng dẫn ([[my_knowlegde/concepts/linux-man-pages|Man pages]])
Đây là nguồn tài liệu chi tiết nhất cho hầu hết các lệnh. Hệ thống được chia thành 8 phần chính phục vụ người dùng và lập trình viên.
* **Cú pháp**: `man <tool>`
* **Ví dụ**: `man ls` sẽ hiển thị hướng dẫn sử dụng chi tiết cho lệnh `ls`.
* **Chi tiết**: Xem thêm tại [[my_knowlegde/concepts/linux-man-pages|Hệ thống trang hướng dẫn Linux]].

## 2. Tùy chọn trợ giúp nhanh (--help)
Hầu hết các công cụ cung cấp bản tóm tắt nhanh về các tham số.
* **Cú pháp**: `<tool> --help` hoặc `<tool> -h` (ví dụ: `ls --help` hoặc `curl -h`).

## 3. Lệnh Apropos
Dùng để tìm kiếm các lệnh dựa trên từ khóa trong mô tả ngắn của chúng.
* **Cú pháp**: `apropos <từ_khóa>`
* **Ví dụ**: `apropos sudo` liệt kê các trang hướng dẫn liên quan đến `sudo`.

## 4. Công cụ hỗ trợ bên ngoài
* **ExplainShell**: Trang web [explainshell.com](https://explainshell.com/) giúp giải thích chi tiết từng thành phần của một dòng lệnh phức tạp.

Việc tự tìm hiểu thông qua các công cụ trợ giúp này giúp bạn nhanh chóng làm chủ các công cụ mới mà không cần phải ghi nhớ mọi tham số.
