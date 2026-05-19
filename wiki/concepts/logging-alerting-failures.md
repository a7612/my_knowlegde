---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A09 Security Logging and Alerting Failures.md"]
tags: ["owasp", "logging", "alerting", "monitoring", "incident-response"]
---

# Thất bại trong ghi nhật ký và cảnh báo bảo mật (Security Logging & Alerting Failures)

**Thất bại trong ghi nhật ký và cảnh báo** (A09:2025) xảy ra khi ứng dụng không ghi lại đủ thông tin về các sự kiện bảo mật hoặc không có cơ chế cảnh báo hiệu quả, dẫn đến việc không thể phát hiện và phản ứng kịp thời với các cuộc tấn công đang diễn ra.

## Các thiếu sót phổ biến
*   **Ghi nhật ký không nhất quán**: Chỉ ghi lại lần đăng nhập thành công mà bỏ qua các lần thất bại, hoặc không ghi lại các giao dịch quan trọng.
*   **Thông báo lỗi không rõ ràng**: Log tạo ra không chứa đủ ngữ cảnh để điều tra sự cố.
*   **Thiếu giám sát liên tục**: Nhật ký ứng dụng và API không được theo dõi thường xuyên.
*   **Thiếu cảnh báo thời gian thực**: Ứng dụng không thể phát hiện hoặc leo thang cảnh báo khi có tấn công tích cực diễn ra.
*   **Lộ lọt thông tin qua Log**: Ghi lại các thông tin nhạy cảm như mật khẩu, dữ liệu cá nhân (PII) vào file nhật ký.
*   **Tấn công vào hệ thống Log**: Log không được bảo vệ chống lại việc xóa hoặc sửa đổi từ kẻ tấn công.

## Cách phòng tránh
1.  **Ghi nhật ký đầy đủ ngữ cảnh**: Đảm bảo tất cả các thất bại trong xác thực, kiểm soát truy cập và xác thực đầu vào đều được ghi lại với đủ thông tin người dùng.
2.  **Định dạng chuẩn**: Sử dụng các định dạng log (như JSON) mà các giải pháp quản lý log (SIEM) có thể dễ dàng tiêu thụ.
3.  **Bảo vệ tính toàn vẹn của Log**: Sử dụng các bảng cơ sở dữ liệu chỉ cho phép thêm (append-only) hoặc các giải pháp lưu trữ tập trung an toàn.
4.  **Thiết lập quy trình phản ứng sự cố**: Xây dựng các kịch bản (playbooks) cho đội ngũ SOC để xử lý các cảnh báo một cách chính xác và nhanh chóng.
5.  **Sử dụng Honeytokens**: Đặt các "bẫy" (dữ liệu giả, tài khoản giả) trong ứng dụng. Bất kỳ sự truy cập nào vào các thành phần này đều là tín hiệu của một cuộc tấn công.

## Kịch bản tấn công ví dụ
Một nhà cung cấp dịch vụ y tế bị tấn công vào năm 2013 nhưng mãi đến hơn 7 năm sau mới phát hiện ra. Nguyên nhân là do các lập trình viên không triển khai ghi nhật ký và giám sát hệ thống, cho phép kẻ tấn công thoải mái truy cập và sửa đổi hàng triệu hồ sơ sức khỏe mà không ai hay biết.

## Liên kết liên quan
- [[incident-management|Quản lý sự cố]]
- [[security-operations-center|Trung tâm vận hành bảo mật (SOC)]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
