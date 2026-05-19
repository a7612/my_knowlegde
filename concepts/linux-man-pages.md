---
sources: ["raw/man7.org/intro(1) - Linux manual page.md", "raw/man7.org/intro(2) - Linux manual page.md", "raw/man7.org/intro(3) - Linux manual page.md", "raw/man7.org/intro(4) - Linux manual page.md", "raw/man7.org/intro(5) - Linux manual page.md", "raw/man7.org/intro(6) - Linux manual page.md", "raw/man7.org/intro(7) - Linux manual page.md", "raw/man7.org/intro(8) - Linux manual page.md"]
tags: ["linux", "fundamentals", "man-pages", "documentation"]
---

# Hệ thống trang hướng dẫn Linux (Linux Man Pages)

Hệ thống **Man Pages** (Manual Pages) là kho tài liệu chính thức và chi tiết nhất được tích hợp sẵn trong các hệ điều hành Unix-like như Linux. Tài liệu này được chia thành 8 phần (sections) chính để giúp người dùng và lập trình viên dễ dàng tra cứu.

## Các phần của Man Pages

Việc hiểu các số phần (section numbers) là rất quan trọng vì một tên có thể xuất hiện ở nhiều phần khác nhau (ví dụ: `printf(1)` là một lệnh shell, trong khi `printf(3)` là một hàm thư viện C).

| Phần | Tên gọi | Mô tả |
| :--- | :--- | :--- |
| **1** | **User Commands** | Các lệnh người dùng thông thường (ví dụ: `ls`, `cat`, `grep`). |
| **2** | **System Calls** | Các điểm nhập vào nhân (kernel), thường được bọc bởi thư viện C (ví dụ: `open`, `read`, `fork`). |
| **3** | **Library Functions** | Các hàm thư viện (không phải system call wrappers) như các hàm trong `libc`, `libm` (ví dụ: `printf`, `malloc`). |
| **4** | **Special Files** | Các tệp thiết bị đặc biệt nằm trong thư mục `/dev` (ví dụ: `null`, `zero`, `tty`). |
| **5** | **File Formats** | Định dạng các tệp cấu hình và hệ thống tệp (ví dụ: `/etc/passwd`, `/etc/shadow`). |
| **6** | **Games** | Các trò chơi và chương trình giải trí nhỏ có sẵn trên hệ thống. |
| **7** | **Miscellaneous** | Các bài viết tổng quan, quy ước, giao thức và tiêu chuẩn (ví dụ: `tcp(7)`, `ascii(7)`). |
| **8** | **Admin Commands** | Các lệnh dành riêng cho quản trị viên hệ thống (superuser/root) (ví dụ: `fdisk`, `ifconfig`, `mount`). |

## Cách sử dụng lệnh `man`

*   **Tra cứu cơ bản**: `man <tên_lệnh>` (mặc định tìm từ phần 1 trở đi).
*   **Tra cứu phần cụ thể**: `man <số_phần> <tên>` (ví dụ: `man 3 printf`).
*   **Tìm kiếm trang**: `man -k <từ_khóa>` (tương đương với lệnh `apropos`).
*   **Điều hướng trong trang**:
    *   `Space bar`: Cuộn xuống một trang.
    *   `b`: Cuộn lên một trang.
    *   `Enter`: Cuộn xuống từng dòng.
    *   `/`: Tìm kiếm một chuỗi văn bản trong trang.
    *   `q`: Thoát khỏi trang hướng dẫn.

## Tầm quan trọng của Man Pages

Hầu hết các lệnh và tệp cấu hình trong Linux đều được tài liệu hóa cực kỳ chi tiết qua hệ thống này. Đối với các chuyên gia an ninh mạng, việc đọc kỹ Man Pages (đặc biệt là phần 5 và 8) là kỹ năng then chốt để hiểu sâu về cách hệ thống vận hành và tìm kiếm các cấu hình sai.

## Liên kết liên quan
- [[my_knowlegde/concepts/linux-shell-help|Cách nhận trợ giúp trong Linux]]
- [[my_knowlegde/concepts/linux-fundamentals|Kiến thức cơ bản về Linux]]
- [[my_knowlegde/concepts/linux-shell|Giao diện dòng lệnh Linux]]
- [[my_knowlegde/concepts/linux-system-info|Thông tin hệ thống Linux]]
