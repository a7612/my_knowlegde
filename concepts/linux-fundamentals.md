---
sources:
  - raw/Hack The Box/Linux Fundamentals/Introduction - Linux Structure.md
tags:
  - linux
  - fundamentals
  - philosophy
---

# Kiến thức cơ bản về Linux (Linux Fundamentals)

Linux là một hệ điều hành (OS) tương tự như Windows hoặc macOS, quản lý tài nguyên phần cứng của máy tính và tạo điều kiện giao tiếp giữa phần mềm và phần cứng. Trong lĩnh vực an ninh mạng, Linux là một cột trụ cơ bản nhờ tính mạnh mẽ, linh hoạt và bản chất mã nguồn mở.

## Lịch sử lược khảo
* **1970**: Unix được phát hành bởi Ken Thompson và Dennis Ritchie tại AT&T.
* **1983**: Richard Stallman khởi xướng dự án GNU với mục tiêu tạo ra một hệ điều hành tự do giống Unix.
* **1991**: Linus Torvalds, một sinh viên người Phần Lan, bắt đầu dự án cá nhân tạo ra hạt nhân (kernel) Linux tự do.
* Hiện nay, hạt nhân Linux đã phát triển từ một vài tệp tin đơn giản lên hơn 23 triệu dòng mã nguồn, được cấp phép theo GNU GPL v2.

## Triết lý Linux
Triết lý Linux tập trung vào sự đơn giản, tính mô-đun và sự cởi mở. Có 5 nguyên tắc cốt lõi:

| Nguyên tắc                                 | Mô tả                                                                                                          |                                               |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Mọi thứ đều là tệp tin**                 | Tất cả tài nguyên hệ thống (thiết bị phần cứng, tiến trình, kết nối mạng) đều được đại diện dưới dạng tệp tin. |                                               |
| **Chương trình nhỏ, đơn mục tiêu**         | Cung cấp nhiều công cụ chuyên biệt làm tốt một nhiệm vụ duy nhất.                                              |                                               |
| **Khả năng chuỗi các chương trình**        | Kết hợp nhiều công cụ nhỏ để thực hiện các tác vụ lớn và phức tạp (ví dụ: lọc dữ liệu).                        |                                               |
| **Tránh giao diện người dùng gò bó**       | Ưu tiên làm việc với [[linux-shell                                                                             | Shell]] (terminal) để có sự kiểm soát tối đa. |
| **Dữ liệu cấu hình lưu trong tệp văn bản** | Ví dụ: tệp `/etc/passwd` lưu trữ thông tin người dùng.                                                         |                                               |

## Các thành phần chính của hệ thống
* **Bootloader**: Đoạn mã hướng dẫn quá trình khởi động (ví dụ: GRUB).
* **OS Kernel**: Thành phần chính quản lý tài nguyên phần cứng và I/O.
* **Daemons**: Các dịch vụ chạy ngầm (lập lịch, in ấn, đa phương tiện).
* **[[linux-shell|OS Shell]]**: Giao diện thông dịch lệnh giữa người dùng và hệ điều hành.
* **Graphics server**: Hệ thống con đồ họa (X-server) cho phép chạy các chương trình đồ họa.
* **Window Manager (GUI)**: Giao diện đồ họa người dùng (GNOME, KDE, MATE, v.v.).
* **Utilities**: Các ứng dụng thực hiện chức năng cụ thể cho người dùng.
