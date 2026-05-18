---
sources:
  - Hack The Box Academy - Linux Fundamentals - Solaris
tags:
  - operating-system
  - unix
  - enterprise
---

# Solaris (Hệ điều hành)

Solaris là một hệ điều hành dựa trên Unix được phát triển bởi Sun Microsystems (sau này được Oracle Corporation mua lại) vào những năm 1990. Nó nổi tiếng với sự mạnh mẽ, khả năng mở rộng và hỗ trợ cho các hệ thống phần cứng/phần mềm cao cấp.

## Đặc điểm nổi bật

*   **Tính ổn định và Bảo mật**: Được thiết kế cho các ứng dụng quan trọng trong doanh nghiệp (ngân hàng, chính phủ, viễn thông).
*   **ZFS (Zettabyte File System)**: Hệ thống tệp tin tiên tiến với khả năng nén dữ liệu, snapshot và khả năng mở rộng cực cao.
*   **RBAC (Role-Based Access Control)**: Quản lý quyền hạn dựa trên vai trò rất chi tiết.
*   **SMF (Service Management Facility)**: Khung quản lý dịch vụ tiên tiến giúp tăng độ tin cậy.
*   **Hỗ trợ phần cứng**: Thiết kế để hoạt động tốt với các máy chủ SPARC và x86.

## So sánh Solaris và Linux

| Đặc điểm | Linux (ví dụ: Ubuntu) | Solaris |
| --- | --- | --- |
| **Mã nguồn** | Mở (Open Source) | Đóng (Proprietary - Oracle) |
| **Quản lý gói** | APT, DPKG | IPS (Image Packaging System) |
| **Thông tin hệ thống** | `uname -a` | `showrev -a` |
| **Cài đặt phần mềm** | `apt install` | `pkgadd` |
| **Truy vết hệ thống** | `strace` | `truss` |
| **Liệt kê file mở** | `lsof` | `pfiles` |

## Cấu trúc thư mục đặc trưng
Ngoài các thư mục giống Linux, Solaris có một số thư mục đáng chú ý:
*   `/kernel`: Chứa các module nhân.
*   `/usr/kernel`: Chứa các thành phần nhân bổ sung.
*   `/etc/dfs/dfstab`: File cấu hình chia sẻ tài nguyên (như NFS).

## Liên kết liên quan
*   [[linux-distributions|Các bản phân phối Linux]]
*   [[linux-file-system|Hệ thống tệp tin Linux]]
*   [[unix|Unix (Tổng quan)]]
