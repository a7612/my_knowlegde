---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Linux Target - Linux Pillaging.md"]
tags: ["security", "pentest", "linux", "post-exploitation", "pillaging", "data-exfiltration", "credentials"]
---

# Vét cạn thông tin hệ thống Linux (Linux Pillaging)

**Vét cạn thông tin (Pillaging)** là giai đoạn trong đó chuyên gia tận dụng quyền quản trị cao nhất (**root**) để trích xuất tất cả các thông tin giá trị nhất từ hệ thống. Mục tiêu là thu thập thông tin để leo thang đặc quyền trên các hệ thống khác, di chuyển ngang trong mạng hoặc chứng minh mức độ rò rỉ dữ liệu.

## Các thông tin nhạy cảm cần thu thập

Khi đã có quyền root, không có tệp tin nào là giới hạn:

1.  **Thông tin đăng nhập hệ thống**:
    *   `root` SSH Private Key: Tìm thấy tại `/root/.ssh/id_rsa`. Khóa này có thể cho phép truy cập vào các máy chủ khác mà quản trị viên quản lý.
    *   Tệp `.bash_history` của root: Chứa các lệnh quan trọng, có thể lộ mật khẩu hoặc địa chỉ các hệ thống nội bộ khác.
2.  **Thông tin ứng dụng và Cơ sở dữ liệu**:
    *   Tệp cấu hình WordPress: `/var/www/cube-case.htb/wp-config.php` chứa tên người dùng và mật khẩu cơ sở dữ liệu (MySQL).
3.  **Thông tin hệ thống ẩn**:
    *   Các ổ đĩa chưa mount: Chứa dữ liệu sao lưu hoặc dữ liệu cũ.
    *   Cấu hình bảo mật: Chi tiết các profile AppArmor đang hoạt động.
4.  **Bằng chứng mục tiêu (Flags)**:
    *   Tệp `root.txt`: Thường nằm ở `/root/`, là bằng chứng cuối cùng xác nhận đã kiểm soát hoàn toàn hệ thống.

## Công cụ hỗ trợ

Ngoài LinPEAS, chuyên gia có thể sử dụng các script chuyên biệt như **linpill.sh** để nhanh chóng quét:
*   Các tệp tin nhạy cảm.
*   Các thư mục có quyền ghi trong biến môi trường `PATH`.
*   Danh sách 55+ binaries SUID/SGID tiềm năng.
*   Lịch sử các tác vụ hệ thống (Systemd Autoruns).

## Ý nghĩa đối với tổ chức
Việc chứng minh có thể lấy được các thông tin này giúp tổ chức hiểu rõ:
*   Mức độ nguy hiểm của việc tái sử dụng mật khẩu.
*   Rủi ro từ việc lưu trữ khóa SSH không bảo mật.
*   Tầm quan trọng của việc mã hóa dữ liệu nhạy cảm ngay cả khi ở trong máy chủ.

## Liên kết liên quan
- [[my_knowlegde/concepts/linux-privilege-escalation|Leo thang đặc quyền (Linux)]]
- [[my_knowlegde/concepts/linux-system-enumeration|Liệt kê hệ thống (Linux)]]
- [[lateral-movement|Di chuyển ngang]]
- [[my_knowlegde/concepts/penetration-testing|Kiểm thử xâm nhập]]
