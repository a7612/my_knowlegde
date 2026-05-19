---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - File System Management.md"]
tags: ["linux", "administration", "file-system", "inodes", "fdisk", "mounting"]
---

# Quản lý Hệ thống Tệp tin Nâng cao (File System Management)

Quản lý hệ thống tệp tin trên Linux bao gồm việc tổ chức, lưu trữ và bảo trì dữ liệu trên đĩa cứng hoặc các thiết bị lưu trữ khác.

## 1. Các loại Hệ thống Tệp tin (File Systems)
Linux hỗ trợ nhiều định dạng tệp tin khác nhau, phù hợp cho từng mục đích:
* **ext4**: Mặc định cho hầu hết distro hiện đại, cân bằng giữa hiệu suất và độ tin cậy. Có tính năng journaling (ghi nhật ký) giúp phục hồi sau sự cố.
* **Btrfs**: Hỗ trợ các tính năng nâng cao như snapshot và kiểm tra toàn vẹn dữ liệu.
* **XFS**: Hiệu suất cao, tối ưu cho các tệp tin lớn và tải I/O nặng.
* **NTFS**: Dùng để tương thích với Windows.

## 2. Khái niệm Inodes
**[[inode|Inode]]** là cấu trúc dữ liệu lưu trữ metadata của mỗi tệp tin/thư mục (quyền hạn, chủ sở hữu, kích thước, mốc thời gian).
* Inode không chứa tên tệp hoặc dữ liệu thực tế mà chứa các con trỏ trỏ tới các khối (blocks) dữ liệu trên đĩa.
* Bảng inode giúp nhân Linux theo dõi và quản lý mọi tài nguyên trên hệ thống.

## 3. Quản lý Đĩa và Phân vùng
* **Lệnh `fdisk`**: Công cụ chính để tạo, xóa và quản lý phân vùng đĩa.
    * `sudo fdisk -l`: Liệt kê các đĩa và phân vùng hiện có.
* **Phân vùng SWAP**: Không gian đĩa được dùng làm bộ nhớ ảo khi RAM vật lý bị đầy. Nó cũng dùng cho tính năng ngủ đông (hibernation).

## 4. Gắn kết Hệ thống Tệp tin (Mounting)
Gắn kết (Mounting) là quá trình liên kết một phân vùng đĩa với một thư mục trong cây hệ thống.
* **Gắn thủ công**: `sudo mount /dev/sdb1 /mnt/usb`
* **Gỡ gắn**: `sudo umount /mnt/usb` (Lưu ý: Không thể gỡ nếu có tiến trình đang dùng tệp trong đó; dùng `lsof` để kiểm tra).
* **Gắn tự động**: Cấu hình trong tệp **`/etc/fstab`**. Tệp này định nghĩa các phân vùng sẽ được tự động gắn khi khởi động máy.
    * Tùy chọn `noauto` trong fstab sẽ ngăn việc tự động gắn khi boot.

Việc quản lý tốt hệ thống tệp tin đảm bảo dữ liệu luôn sẵn sàng, bảo mật và hệ thống hoạt động ổn định.
