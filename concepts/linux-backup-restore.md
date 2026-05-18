---
sources: ["raw/Hack The Box/Linux Fundamentals/System Management - Backup and Restore.md"]
tags: ["linux", "administration", "backup", "restore", "rsync", "ssh"]
---

# Sao lưu và Phục hồi (Backup and Restore)

Việc sao lưu dữ liệu thường xuyên là biện pháp thiết yếu để bảo vệ thông tin khỏi mất mát hoặc hư hỏng. Linux cung cấp nhiều công cụ mạnh mẽ để thực hiện việc này một cách hiệu quả và bảo mật.

## 1. Công cụ Rsync (Remote Sync)
**[[rsync|Rsync]]** là công cụ mã nguồn mở phổ biến nhất cho việc sao lưu nhanh và bảo mật. Ưu điểm lớn nhất là nó chỉ truyền các phần thay đổi của tệp tin (incremental backup).
* **Cài đặt**: `sudo apt install rsync -y`
* **Sao lưu cục bộ sang máy chủ**:
    `rsync -av /path/to/source user@remote:/path/to/destination`
    * `-a` (archive): Giữ nguyên các thuộc tính tệp (quyền, mốc thời gian).
    * `-v` (verbose): Hiển thị chi tiết quá trình.
    * `-z` (compress): Nén dữ liệu khi truyền để tăng tốc độ.
* **Phục hồi**: Đảo ngược vị trí nguồn và đích trong lệnh rsync.

## 2. Sao lưu Bảo mật qua SSH
Để đảm bảo an toàn dữ liệu khi truyền qua mạng, rsync có thể kết hợp với SSH:
`rsync -avz -e ssh /source/ user@backup_server:/destination/`
Dữ liệu sẽ được mã hóa trong suốt quá trình truyền tải, đảm bảo tính bảo mật và toàn vẹn.

## 3. Tự động hóa Sao lưu
Sử dụng kết hợp **[[linux-task-scheduling|Cron]]** và **Rsync** để tự động hóa quy trình:
1. Tạo một script (ví dụ: `backup.sh`) chứa lệnh rsync.
2. Thiết lập xác thực bằng khóa SSH (`ssh-keygen` và `ssh-copy-id`) để không cần nhập mật khẩu thủ công.
3. Thêm script vào crontab để chạy theo định kỳ (ví dụ: hàng giờ).

## 4. Các công cụ khác
* **Duplicity**: Xây dựng dựa trên rsync nhưng bổ sung tính năng mã hóa mạnh mẽ cho bản lưu trữ.
* **Deja Dup**: Giao diện đồ họa (GUI) đơn giản cho người dùng không muốn dùng dòng lệnh, hỗ trợ sao lưu lên đám mây.

Duy trì các bản sao lưu được mã hóa và lưu trữ tại nhiều vị trí khác nhau là chiến lược an toàn nhất cho dữ liệu của bạn.
