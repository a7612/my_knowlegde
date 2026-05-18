---
sources: ["raw/Hack The Box/Linux Fundamentals/Workflow - Permission Management.md"]
tags: ["linux", "workflow", "permissions", "chmod", "chown", "suid", "sgid"]
---

# Quản lý Quyền hạn (Permission Management)

Hệ thống quyền hạn trong Linux kiểm soát ai có thể truy cập và thực hiện các hành động trên tệp tin và thư mục.

## Các loại quyền hạn
Có 3 loại quyền cơ bản:
* **Read (r)**: Đọc nội dung tệp hoặc liệt kê nội dung thư mục.
* **Write (w)**: Sửa đổi nội dung tệp hoặc tạo/xóa tệp trong thư mục.
* **Execute (x)**: Thực thi tệp (như script) hoặc truy cập (traverse) vào thư mục.

## Đối tượng áp dụng
Quyền được thiết lập cho 3 nhóm đối tượng:
1. **Owner (u)**: Chủ sở hữu tệp.
2. **Group (g)**: Nhóm sở hữu tệp.
3. **Others (o)**: Tất cả những người dùng khác.

## Hệ thập bát phân (Octal Notation)
Quyền hạn thường được đại diện bằng các con số:
* 4 = Read (r)
* 2 = Write (w)
* 1 = Execute (x)
* 0 = Không có quyền (-)

Ví dụ: `chmod 755 file` tương đương với:
* Owner: 7 (4+2+1 = rwx)
* Group: 5 (4+0+1 = r-x)
* Others: 5 (4+0+1 = r-x)

## Thay đổi Quyền và Chủ sở hữu
* **`chmod`**: Thay đổi quyền hạn (ví dụ: `chmod +x script.sh`).
* **`chown`**: Thay đổi chủ sở hữu và nhóm (ví dụ: `chown root:root file`).

## Quyền đặc biệt
* **SUID (Set User ID)**: Cho phép thực thi tệp với quyền của chủ sở hữu tệp.
* **SGID (Set Group ID)**: Cho phép thực thi tệp với quyền của nhóm sở hữu.
* **Sticky Bit**: Khi được thiết lập trên một thư mục, chỉ chủ sở hữu tệp (hoặc root) mới có thể xóa hoặc đổi tên tệp trong đó (ví dụ thư mục `/tmp`).

Lưu ý: Việc lạm dụng các quyền đặc biệt như SUID trên các chương trình như `journalctl` có thể dẫn đến rủi ro leo thang đặc quyền (privilege escalation).
