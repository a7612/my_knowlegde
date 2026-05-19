---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Windows Target - Windows Information Gathering.md"]
tags: ["security", "pentest", "windows", "information-gathering", "smb", "gitea", "nmap"]
---

# Thu thập thông tin mục tiêu Windows (Windows Information Gathering)

Quy trình thu thập thông tin trên Windows có nhiều điểm tương đồng với Linux nhưng tập trung vào các dịch vụ đặc thù của hệ sinh thái Microsoft như SMB và RDP.

## 1. Quét mạng với Nmap

Sử dụng Nmap để xác định bề mặt tấn công của máy chủ Windows (ví dụ: Windows Server 2019 - WIN01).

*   **Lệnh quét**: `sudo nmap -p- -sV -sC <IP> -T5 -Pn`
*   **Các dịch vụ phổ biến tìm thấy**:
    *   **SSH (Cổng 22)**: Đôi khi được cài đặt thêm trên Windows.
    *   **RPC (Cổng 135)**: Dịch vụ gọi hàm từ xa.
    *   **SMB (Cổng 445)**: Dịch vụ chia sẻ tệp tin và máy in.
    *   **Gitea (Cổng 3000)**: Dịch vụ Git tự lưu trữ (self-hosted).
    *   **RDP (Cổng 3389)**: Giao thức điều khiển máy tính từ xa.

## 2. Kiểm tra Gitea (Cổng 3000)

Gitea là một giải pháp thay thế nhẹ cho GitHub. Việc xác định phiên bản là cực kỳ quan trọng.
*   **Thông tin phát hiện**: Phiên bản Gitea 1.12.4 và Go 1.14.8.
*   **Rủi ro**: Các phiên bản cũ thường chứa các lỗ hổng thực thi mã từ xa (RCE) thông qua Git Hooks.

## 3. Thăm dò SMB (Cổng 445)

SMB là vector tấn công quan trọng trong mạng Windows.

*   **Công cụ sử dụng**: **CrackMapExec**
*   **Các phát hiện quan trọng**:
    *   **SMBv1**: Nếu còn bật, đây là dấu hiệu của hệ thống cũ, dễ bị tấn công bởi các lỗ hổng như EternalBlue.
    *   **NULL Session**: Truy cập ẩn danh (không cần username/password) để liệt kê thông tin.
    *   **Guest Account**: Nếu được bật, có thể liệt kê các thư mục chia sẻ (Shares).
*   **Các thư mục chia sẻ mặc định**:
    *   `ADMIN$`: Quản trị từ xa.
    *   `C$`: Ổ đĩa hệ thống.
    *   `IPC$`: Giao tiếp giữa các tiến trình.
    *   `Devs`: Thư mục chia sẻ tùy chỉnh (thường chứa tệp tin của nhà phát triển).

## Liên kết liên quan
- [[my_knowlegde/concepts/information-gathering|Thu thập thông tin (Tổng quan)]]
- [[my_knowlegde/concepts/network-scanning|Quét mạng và dịch vụ]]
- [[my_knowlegde/concepts/windows-initial-access|Truy cập ban đầu (Windows)]]
- [[my_knowlegde/concepts/penetration-testing|Kiểm thử xâm nhập]]
