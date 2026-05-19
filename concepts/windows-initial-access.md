---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Windows Target - Windows Initial Access.md"]
tags: ["security", "pentest", "windows", "initial-access", "smb", "gitea", "rdp", "metasploit"]
---

# Truy cập ban đầu mục tiêu Windows (Windows Initial Access)

Sau khi thu thập thông tin, chuyên gia thực hiện khai thác các điểm yếu để giành quyền truy cập vào hệ thống Windows.

## 1. Khai thác SMB và Rò rỉ thông tin

Sử dụng các thông tin đã thu thập được từ các hệ thống khác (như Linux) để thử nghiệm trên Windows (tấn công **Password Reuse**).

*   **Kỹ thuật Spidering**: Sử dụng CrackMapExec để duyệt thư mục chia sẻ.
    *   Lệnh: `crackmapexec smb <IP> -u "john" -p "password" --spider Devs --pattern .`
*   **Thu thập tệp tin nhạy cảm**: Tìm thấy các script PowerShell (ví dụ: `tmp.ps1`) chứa mật khẩu bản rõ (hardcoded credentials). Điều này xác nhận sự tồn tại của người dùng cục bộ và thói quen bảo mật kém.

## 2. Kiểm tra thông tin đăng nhập RDP

Sử dụng công cụ **Hydra** để xác nhận tính hợp lệ của thông tin đăng nhập đối với dịch vụ RDP.
*   Lệnh: `hydra -l john -p "password" rdp://<IP>`
*   Nếu thành công, có thể thiết lập phiên điều khiển giao diện đồ họa qua **xfreerdp**.

## 3. Khai thác Gitea (Metasploit)

Các phiên bản Gitea cũ (dưới 1.13.0) thường có lỗ hổng trong tính năng **Git Hooks**, cho phép thực thi mã từ xa.

*   **Quy trình thực hiện**:
    1.  Sử dụng module: `exploit/multi/http/gitea_git_hooks_rce`.
    2.  Cấu hình `USERNAME`, `PASSWORD` (sử dụng tài khoản đã thu thập được).
    3.  Module sẽ tạo một kho lưu trữ (repository) tạm thời, cài đặt một mã độc vào `post-receive hook` và kích hoạt nó bằng cách đẩy một tệp tin giả.
*   **Kết quả**: Giành được một shell **Meterpreter** dưới quyền người dùng đang chạy Gitea.

## 4. Thiết lập phiên làm việc ổn định

Sau khi có truy cập ban đầu, chuyên gia thường sử dụng RDP để có môi trường làm việc thuận tiện hơn:
*   Lệnh: `xfreerdp /u:john /p:"password" /v:<IP> /w:1366 /h:768`

## Liên kết liên quan
- [[my_knowlegde/concepts/windows-information-gathering|Thu thập thông tin (Windows)]]
- [[my_knowlegde/concepts/windows-system-enumeration|Liệt kê hệ thống (Windows)]]
- [[my_knowlegde/concepts/penetration-testing|Kiểm thử xâm nhập]]
