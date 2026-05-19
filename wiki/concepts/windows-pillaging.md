---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Windows Target - Windows Pillaging.md"]
tags: ["security", "pentest", "windows", "post-exploitation", "pillaging", "pii", "gdpr"]
---

# Vét cạn thông tin hệ thống Windows (Windows Pillaging)

Sau khi đạt được quyền quản trị (**Administrator**), chuyên gia thực hiện thu thập các thông tin nhạy cảm nhất từ hệ thống để chứng minh rủi ro và hậu quả của một cuộc tấn công thực tế.

## 1. Khai thác dữ liệu người dùng và hệ thống

Với quyền cao nhất, không còn rào cản nào ngăn chặn việc truy cập dữ liệu:

*   **Thông tin cá nhân (PII)**: Tìm kiếm các tệp tin chứa dữ liệu khách hàng.
    *   *Ví dụ*: Tệp `C:\Users\Administrator\customer_database.csv` chứa danh sách khách hàng, số an sinh xã hội (SSN), ngày sinh và **thông tin thẻ tín dụng (Credit Card Number, CVV)**.
*   **Lịch sử hoạt động**: Các tệp `PowerShell_transcript` lưu lại toàn bộ các lệnh mà quản trị viên đã từng chạy, có thể lộ mật khẩu hoặc quy trình nghiệp vụ.
*   **Log hệ thống**: Nhật ký sự kiện bảo mật (Security Event Logs) để hiểu về các hoạt động đăng nhập và truy cập trước đó.

## 2. Công cụ hỗ trợ: WinPill

Sử dụng script **winpill.ps1** để tự động hóa việc tìm kiếm:
*   Thông tin phần cứng và cấu hình mạng.
*   Các tác vụ lập lịch không phải của Microsoft.
*   Các tệp tin "thú vị" (Interesting files) dựa trên phần mở rộng và thời gian sửa đổi gần nhất.

## 3. Rủi ro về Pháp lý và Tài chính

Việc để rò rỉ các tệp tin như `customer_database.csv` dẫn đến những hậu quả khủng khiếp cho doanh nghiệp:
*   **Vi phạm GDPR (Châu Âu)**: Mức phạt có thể lên tới 20 triệu Euro hoặc 4% doanh thu toàn cầu hàng năm.
*   **Vi phạm HIPAA/CCPA**: Các khoản phạt nặng dựa trên mỗi bản ghi dữ liệu bị lộ.
*   **Hư hại danh tiếng**: Mất lòng tin khách hàng và giá trị cổ phiếu sụt giảm.

## 4. Thu thập chứng cứ (Evidence)

Trong các bài kiểm tra Pentest, tệp tin quan trọng nhất thường là:
*   `C:\Users\Administrator\root.txt` hoặc `flag.txt`: Bằng chứng cho thấy hệ thống đã bị kiểm soát hoàn toàn.

## Liên kết liên quan
- [[windows-privilege-escalation|Leo thang đặc quyền (Windows)]]
- [[windows-system-enumeration|Liệt kê hệ thống (Windows)]]
- [[information-security|An ninh thông tin]]
- [[penetration-testing|Kiểm thử xâm nhập]]
