---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - Editing Files.md"]
tags: ["linux", "workflow", "editing", "nano", "vim"]
---

# Chỉnh sửa Tệp tin (Editing Files)

Trong Linux, việc chỉnh sửa tệp tin trực tiếp từ terminal là kỹ năng cực kỳ quan trọng và hiệu quả.

## 1. Nano
Đây là trình soạn thảo văn bản đơn giản, dễ học cho người mới bắt đầu.
* **Mở tệp**: `nano filename.txt`
* **Lưu tệp**: `Ctrl + O` sau đó nhấn `Enter`.
* **Thoát**: `Ctrl + X`.
* **Tìm kiếm**: `Ctrl + W`.

## 2. Vim (Vi Improved)
Vim là một trình soạn thảo cực kỳ mạnh mẽ nhưng có lộ trình học tập dốc hơn. Nó hoạt động dựa trên các **chế độ (modes)**:

| Chế độ | Mô tả |
| --- | --- |
| **Normal** | Chế độ mặc định khi mở Vim, dùng để nhập lệnh điều hướng, xóa, sao chép. |
| **Insert** | Dùng để nhập văn bản (nhấn `i` từ chế độ Normal để vào). |
| **Visual** | Dùng để bôi đen/chọn văn bản. |
| **Command** | Dùng để nhập các lệnh ở dòng cuối (nhấn `:` từ chế độ Normal). |
| **Replace** | Dùng để ghi đè văn bản. |

* **Lưu và Thoát**: Nhấn `Esc` để về chế độ Normal, sau đó gõ `:wq` và nhấn `Enter`.
* **Thoát không lưu**: Gõ `:q!`.
* **Luyện tập**: Sử dụng lệnh `vimtutor` để học cách dùng Vim cơ bản.

## 3. Xem nội dung nhanh
* **`cat`**: Hiển thị toàn bộ nội dung tệp.
* **`less` / `more`**: Xem nội dung theo từng trang.

Việc thành thạo ít nhất một trình soạn thảo dòng lệnh sẽ giúp bạn làm việc nhanh chóng trên các hệ thống không có giao diện đồ họa (như máy chủ).
