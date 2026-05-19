---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Windows Target - Windows Privilege Escalation.md"]
tags: ["security", "pentest", "windows", "privilege-escalation", "scheduled-tasks", "powershell"]
---

# Leo thang đặc quyền Windows (Windows Privilege Escalation)

Mục tiêu của giai đoạn này là giành được quyền **Administrator** hoặc **SYSTEM** trên máy chủ Windows.

## 1. Khai thác Tác vụ lập lịch (Scheduled Task Hijacking)

Đây là kỹ thuật tận dụng một tác vụ hệ thống đang chạy một script mà chúng ta có quyền sửa đổi.

*   **Tình huống**: Tác vụ `CorpBackupAgent` chạy script `backupprep.ps1` dưới quyền Administrator mỗi 2 phút. Chúng ta có quyền **Read/Write** trên script này.
*   **Kỹ thuật thực hiện**:
    1.  Mở script bằng NotePad hoặc lệnh echo.
    2.  Chèn thêm lệnh PowerShell để thêm người dùng của chúng ta vào nhóm quản trị:
        ```powershell
        Add-LocalGroupMember -Group "Administrators" -Member "WIN01\john"
        ```
    3.  Lưu script và đợi tối đa 2 phút.
*   **Kết quả**: Người dùng `john` hiện đã là thành viên của nhóm `Administrators`.

## 2. Duy trì sự hiện diện (Persistence)

Kỹ thuật trên cũng là một cách để duy trì quyền truy cập. Nếu quản trị viên xóa người dùng khỏi nhóm `Administrators`, tác vụ lập lịch sẽ tự động thêm lại người dùng đó sau mỗi 2 phút.

## 3. Kiểm tra kết quả

Sau khi leo thang, chuyên gia cần xác nhận bằng cách:
*   Chạy lệnh: `net user john` để xem danh sách nhóm mới.
*   Thử truy cập vào thư mục của quản trị viên: `ls C:\Users\Administrator`. Nếu truy cập được, việc leo thang đã thành công.

## 4. Các phương pháp leo thang khác (Tóm tắt)

*   **Token Impersonation**: Lợi dụng `SeImpersonatePrivilege` để giả mạo người dùng cấp cao.
*   **Service Binary Overwrite**: Thay thế tệp thực thi của một dịch vụ hệ thống bằng mã độc của mình.
*   **Unquoted Service Path**: Khai thác đường dẫn dịch vụ không có dấu ngoặc kép và chứa dấu cách.
*   **Kernel Exploits**: Khai thác các lỗi sâu trong hệ điều hành Windows.

## Liên kết liên quan
- [[windows-vulnerability-assessment|Đánh giá lỗ hổng (Windows)]]
- [[windows-pillaging|Vét cạn thông tin (Windows)]]
- [[penetration-testing|Kiểm thử xâm nhập]]
