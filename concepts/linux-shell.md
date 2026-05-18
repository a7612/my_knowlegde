---
sources: ["raw/Hack The Box/Linux Fundamentals/Introduction - Introduction to Shell.md"]
tags: ["linux", "shell", "terminal", "bash"]
---

# Linux Shell

[[linux-shell|Shell]] là một phần thiết yếu của Linux, đóng vai trò là giao diện nhập/xuất văn bản giữa người dùng và hạt nhân (kernel).

## Shell vs Terminal
* **Terminal**: Là phần mềm giả lập (terminal emulator) cung cấp cửa sổ giao diện để người dùng nhập liệu. Nó là "cổng vào" của Shell.
* **Shell**: Là bộ thông dịch ngôn ngữ lệnh, xử lý các lệnh mà người dùng nhập vào để yêu cầu hệ điều hành thực hiện hành động.

## Các loại Shell phổ biến
* **BASH (Bourne-Again Shell)**: Phổ biến nhất, thuộc dự án GNU.
* **Zsh (Z shell)**: Được ưa chuộng vì tính năng tự động hoàn thành mạnh mẽ.
* **Fish (Friendly Interactive Shell)**: Tập trung vào trải nghiệm người dùng.
* Các loại khác: Tcsh/Csh, Ksh.

## Trình giả lập Terminal và Bộ ghép kênh (Multiplexers)
Các công cụ này mở rộng khả năng của terminal:
* **Terminal Emulators**: Cho phép dùng chương trình văn bản trong giao diện đồ họa (GUI).
* **Multiplexers (ví dụ: Tmux)**: Cho phép chia cửa sổ terminal thành nhiều bảng (panes), làm việc trong nhiều thư mục và không gian làm việc khác nhau cùng lúc.

Sử dụng Shell cho phép tự động hóa các quy trình thông qua các tập lệnh (scripts), giúp công việc thủ công trở nên nhanh chóng và hiệu quả hơn.
