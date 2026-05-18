---
sources: ["raw/Hack The Box/Linux Fundamentals/Introduction - Linux Structure.md"]
tags: ["linux", "architecture", "kernel", "shell"]
---

# Kiến trúc Linux (Linux Architecture)

Hệ điều hành Linux có thể được chia thành các lớp trừu tượng, mỗi lớp có vai trò riêng trong việc vận hành hệ thống.

## Các lớp của hệ thống

| Lớp | Mô tả |
| --- | --- |
| **Phần cứng (Hardware)** | Các thiết bị ngoại vi như RAM, ổ cứng, CPU và các linh kiện khác. |
| **Hạt nhân (Kernel)** | Lõi của hệ điều hành, có chức năng ảo hóa và kiểm soát tài nguyên phần cứng. Nó cung cấp tài nguyên ảo cho từng tiến trình và ngăn chặn xung đột giữa chúng. |
| **Vỏ (Shell)** | Giao diện dòng lệnh (**CLI**) nơi người dùng nhập lệnh để thực thi các chức năng của hạt nhân. |
| **Tiện ích hệ thống (System Utility)** | Cung cấp toàn bộ chức năng của hệ điều hành cho người dùng cuối. |

Kiến trúc này đảm bảo sự phân tách rõ ràng giữa phần cứng vật lý và các ứng dụng người dùng, giúp hệ thống ổn định và bảo mật hơn.
