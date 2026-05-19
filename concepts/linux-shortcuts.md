---
sources:
  - "Hack The Box Academy - Linux Fundamentals - Shortcuts"
tags:
  - "linux"
  - "workflow"
  - "cli"
---

# Phím tắt trong Linux (Linux Shortcuts)

Các phím tắt giúp làm việc với dòng lệnh Linux nhanh chóng và hiệu quả hơn, giảm thiểu việc gõ phím và sử dụng chuột trong terminal.

## Tự động hoàn thành (Auto-Complete)

*   `[TAB]`: Kích hoạt tính năng tự động hoàn thành. Dựa trên các ký tự đã nhập, shell sẽ gợi ý các thư mục, lệnh hoặc tùy chọn tương ứng.

## Di chuyển con trỏ (Cursor Movement)

*   `[CTRL] + A`: Di chuyển con trỏ về **đầu** dòng hiện tại.
*   `[CTRL] + E`: Di chuyển con trỏ về **cuối** dòng hiện tại.
*   `[CTRL] + [←]` / `[→]`: Nhảy về đầu từ hiện tại hoặc từ trước đó.
*   `[ALT] + B` / `F`: Nhảy lùi/tiến một từ.

## Xóa nội dung (Erase)

*   `[CTRL] + U`: Xóa mọi thứ từ vị trí con trỏ về **đầu** dòng.
*   `[CTRL] + K`: Xóa mọi thứ từ vị trí con trỏ về **cuối** dòng.
*   `[CTRL] + W`: Xóa từ đứng trước con trỏ.

## Dán nội dung đã xóa (Paste)

*   `[CTRL] + Y`: Dán văn bản hoặc từ vừa bị xóa bằng các lệnh trên.

## Quản lý Tác vụ và Tiến trình

*   `[CTRL] + C`: Kết thúc tác vụ/tiến trình hiện tại bằng cách gửi tín hiệu `SIGINT`. Thường dùng để dừng các lệnh đang chạy như scan.
*   `[CTRL] + Z`: Tạm dừng tiến trình hiện tại và đẩy vào nền (background) bằng cách gửi tín hiệu `SIGTSTP`.
*   `[CTRL] + D`: Đóng luồng `STDIN`, còn gọi là **End-of-File (EOF)** hoặc kết thúc truyền dữ liệu.

## Quản lý Terminal và Lịch sử

*   `[CTRL] + L`: Xóa sạch màn hình terminal (tương đương lệnh `clear`).
*   `[CTRL] + R`: Tìm kiếm trong lịch sử lệnh (command history) theo mẫu.
*   `[↑]` / `[↓]`: Di chuyển qua lại các lệnh đã thực hiện trước đó trong lịch sử.

## Tiện ích khác

*   `[ALT] + [TAB]`: Chuyển đổi giữa các ứng dụng đang mở.
*   `[CTRL] + [+]`: Phóng to (Zoom in).
*   `[CTRL] + [-]`: Thu nhỏ (Zoom out).

## Liên kết liên quan
*   [[my_knowlegde/concepts/linux-shell|Linux Shell]]
*   [[my_knowlegde/concepts/linux-service-process-management|Quản lý Dịch vụ và Tiến trình]]
