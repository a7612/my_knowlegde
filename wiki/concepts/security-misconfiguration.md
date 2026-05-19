---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A02 Security Misconfiguration.md"]
tags: ["owasp", "configuration", "hardening", "xxe", "security-misconfiguration"]
---

# Cấu hình sai bảo mật (Security Misconfiguration)

**Cấu hình sai bảo mật** (A02:2025) là tình trạng một hệ thống, ứng dụng hoặc dịch vụ đám mây được thiết lập không chính xác từ góc độ bảo mật, tạo ra các lỗ hổng dễ bị khai thác. Với xu hướng phần mềm ngày càng phụ thuộc vào cấu hình, rủi ro này đã tăng vọt lên vị trí số 2 trong danh sách OWASP.

## Các dấu hiệu dễ bị tấn công
*   **Thiếu quy trình Hardening**: Không có quy trình làm cứng bảo mật cho các lớp của ứng dụng hoặc dịch vụ đám mây.
*   **Tính năng không cần thiết**: Các cổng (port), dịch vụ, trang web hoặc tài khoản mẫu vẫn được bật/cài đặt.
*   **Tài khoản mặc định**: Tên đăng nhập và mật khẩu mặc định (ví dụ: `admin/admin`) chưa được thay đổi.
*   **Xử lý lỗi quá chi tiết**: Hiển thị thông báo lỗi chứa dấu vết ngăn xếp (stack traces) hoặc thông tin hệ thống nhạy cảm cho người dùng.
*   **XXE (XML External Entity)**: Cấu hình bộ xử lý XML yếu cho phép kẻ tấn công đọc file nội bộ hoặc tấn công SSRF.
*   **Thiếu tiêu đề bảo mật (Security Headers)**: Máy chủ không gửi hoặc thiết lập sai các tiêu đề như HSTS, CSP.

## Cách phòng tránh
1.  **Quy trình Hardening tự động**: Thiết lập các môi trường (Dev, QA, Production) giống hệt nhau về cấu hình bảo mật thông qua tự động hóa.
2.  **Nguyên tắc tối giản**: Chỉ cài đặt và bật những gì thực sự cần thiết. Gỡ bỏ các mẫu (samples) và tài liệu đi kèm phần mềm gốc.
3.  **Quản lý bản vá tập trung**: Thường xuyên cập nhật và đánh giá cấu hình dựa trên các ghi chú bảo mật.
4.  **Phân đoạn kiến trúc**: Sử dụng container hóa, ACL hoặc nhóm bảo mật đám mây để ngăn cách các thành phần.
5.  **Xử lý lỗi tập trung**: Chặn các thông báo lỗi quá chi tiết, chỉ hiển thị thông báo chung cho người dùng cuối.
6.  **Kiểm tra tự động**: Sử dụng các công cụ để định kỳ kiểm tra hiệu quả của các thiết lập bảo mật.

## Kịch bản tấn công ví dụ
Một máy chủ ứng dụng đi kèm với các ứng dụng mẫu không được gỡ bỏ. Kẻ tấn công khai thác lỗ hổng đã biết trong ứng dụng mẫu đó để chiếm quyền điều khiển toàn bộ máy chủ. Hoặc, một S3 bucket trên đám mây được để ở chế độ công khai, cho phép bất kỳ ai cũng có thể tải về dữ liệu nhạy cảm.

## Liên kết liên quan
- [[broken-access-control|Kiểm soát truy cập bị hỏng]]
- [[software-supply-chain|Thất bại trong chuỗi cung ứng phần mềm]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
