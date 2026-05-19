---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - Regular Expressions.md"]
tags: ["linux", "workflow", "regex", "grep"]
---

# Biểu thức chính quy (Regular Expressions - RegEx)

Biểu thức chính quy là một chuỗi các ký tự định nghĩa một mẫu tìm kiếm, giúp bạn tìm, thay thế và thao tác dữ liệu văn bản với độ chính xác cực cao.

## Các toán tử gom nhóm (Grouping Operators)

| Toán tử | Mô tả |
| --- | --- |
| **`(a)`** | Ngoặc tròn dùng để gom nhóm các phần của regex để xử lý cùng nhau. |
| **`[a-z]`** | Ngoặc vuông định nghĩa các lớp ký tự (ví dụ: tìm bất kỳ chữ cái nào từ a đến z). |
| **`{1,10}`** | Ngoặc nhọn xác định số lần lặp lại (quantifiers). |
| **`\|`** | Toán tử HOẶC (OR), trả về kết quả nếu một trong hai biểu thức khớp. |
| **`.*`** | Kết hợp dấu chấm (bất kỳ ký tự nào) và dấu sao (lặp lại 0 hoặc nhiều lần), thường dùng như toán tử VÀ (AND) khi tìm kiếm nhiều mẫu trên cùng một dòng. |

## Sử dụng với `grep`
Để sử dụng các toán tử mở rộng này, bạn cần thêm tùy chọn `-E` (Extended RegEx).
* Ví dụ tìm dòng chứa "user" HOẶC "root": `grep -E "user|root" /etc/passwd`

RegEx là một công cụ đa năng có mặt trong hầu hết các ngôn ngữ lập trình và công cụ dòng lệnh (như `sed`, `grep`, `awk`), giúp bạn xử lý các tác vụ phức tạp một cách nhanh gọn.
