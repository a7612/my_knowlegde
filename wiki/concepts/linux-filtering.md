---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - Filter Contents.md"]
tags: ["linux", "workflow", "filtering", "grep", "sed", "awk"]
---

# Lọc và Xử lý nội dung (Filtering Content)

Linux cung cấp bộ công cụ phong phú để lọc và biến đổi dữ liệu văn bản từ dòng lệnh mà không cần mở trình soạn thảo.

## Công cụ xem và phân tách
* **`head` / `tail`**: Xem vài dòng đầu hoặc cuối của tệp (mặc định 10 dòng).
* **`sort`**: Sắp xếp các dòng theo thứ tự bảng chữ cái hoặc số.
* **`cut`**: Cắt bỏ các phần của mỗi dòng (dùng `-d` cho ký tự phân cách và `-f` cho vị trí trường).
* **`tr`**: Thay thế hoặc xóa các ký tự cụ thể.

## Công cụ tìm kiếm và lọc mạnh mẽ
* **`grep`**: Tìm kiếm các dòng khớp với một mẫu (pattern).
    * `grep -v`: Loại trừ các dòng khớp với mẫu.
* **`column -t`**: Hiển thị dữ liệu dưới dạng bảng cột ngay ngắn.

## Công cụ xử lý nâng cao (Stream Editors)
* **`awk`**: Ngôn ngữ lập trình xử lý văn bản mạnh mẽ, thường dùng để trích xuất các cột cụ thể (ví dụ: `awk '{print $1}'`).
* **`sed`**: Bộ soạn thảo luồng, dùng để thay thế văn bản theo mẫu (ví dụ: `sed 's/old/new/g'`).

## Thống kê
* **`wc -l`**: Đếm số dòng trong đầu ra hoặc tệp tin.

Sử dụng kết hợp các công cụ này thông qua [[linux-redirections|đường ống (pipes)]] cho phép bạn trích xuất chính xác thông tin cần thiết từ các tệp nhật ký (logs) hoặc cấu hình hệ thống khổng lồ.
