---
sources: ["raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Disaster Recovery and Business Continuity.md"]
tags: ["security", "disaster-recovery", "dr", "availability", "resilience"]
---

# Khôi phục sau thảm họa (Disaster Recovery - DR)

**Khôi phục sau thảm họa (DR)** là một tập hợp các quy trình và chính sách tập trung vào việc khôi phục các hệ thống CNTT và dữ liệu quan trọng sau một sự kiện thảm khốc.

## Mục tiêu
* Giảm thiểu thời gian ngừng hoạt động (downtime).
* Hạn chế mất mát dữ liệu.
* Đảm bảo tổ chức có thể nhanh chóng tiếp tục các chức năng thiết yếu.

## Phép ẩn dụ: Buổi hòa nhạc ngoài trời
Hãy tưởng tượng bạn tổ chức một buổi hòa nhạc lớn trong công viên.
* **Thảm họa**: Một cơn mưa xối xả bất ngờ hoặc mất điện.
* **Kế hoạch DR**: Giống như việc bạn mang theo ô (dù) và máy phát điện. Nếu mưa rơi, bạn dùng ô che thiết bị; nếu mất điện, bạn bật máy phát để giữ ánh sáng và âm thanh. DR tập trung vào việc sửa chữa/khôi phục các phần bị hỏng để buổi diễn có thể tiếp tục với sự gián đoạn ít nhất.

## Các yếu tố của một kế hoạch DR
* **Sao lưu dữ liệu (Backup)**: Duy trì các bản sao dữ liệu an toàn.
* **Nhân bản hệ thống (Replication)**: Tạo các bản sao của hệ thống ở các địa điểm khác nhau.
* **Chuyển vùng dự phòng (Failover)**: Tự động chuyển đổi sang các máy chủ hoặc môi trường đám mây dự phòng khi hệ thống chính gặp sự cố.
* **Chỉ số phục hồi**:
    * **RTO (Recovery Time Objective)**: Thời gian tối đa cho phép để khôi phục hệ thống sau sự cố.
    * **RPO (Recovery Point Objective)**: Lượng dữ liệu tối đa có thể chấp nhận bị mất (tính theo thời gian từ bản sao lưu gần nhất).

## Trách nhiệm
* **Đội ngũ Quản lý liên tục kinh doanh**: Thiết kế và bảo trì các kế hoạch.
* **Đội ngũ IT và Vận hành**: Thực thi các biện pháp kỹ thuật.
* **Kiểm thử xâm nhập (Penetration Testers)**: Giúp xác định các lỗ hổng có thể làm hỏng nỗ lực khôi phục và kiểm tra tính hiệu quả của các quy trình khôi phục.

## Liên kết liên quan
- [[business-continuity|Liên tục kinh doanh]]
- [[information-security|An ninh thông tin]]
- [[cloud-security|An ninh đám mây]]
