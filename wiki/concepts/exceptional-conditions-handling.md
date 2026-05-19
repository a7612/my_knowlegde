---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A10 Mishandling of Exceptional Conditions.md"]
tags: ["owasp", "exception-handling", "error-handling", "failing-closed", "code-quality"]
---

# Xử lý sai các điều kiện bất thường (Mishandling of Exceptional Conditions)

**Xử lý sai các điều kiện bất thường** (A10:2025) là danh mục mới trong OWASP 2025. Nó xảy ra khi phần mềm không thể ngăn chặn, phát hiện hoặc phản ứng đúng cách với các tình huống bất thường và không dự đoán trước được, dẫn đến treo máy, hành vi ngoài ý muốn hoặc các lỗ hổng bảo mật.

## Tại sao rủi ro này nguy hiểm?
Khi một ứng dụng không chắc chắn về chỉ thị tiếp theo của mình (do gặp lỗi mà không được xử lý), nó có thể rơi vào trạng thái không thể đoán trước. Điều này dẫn đến:
- **Lỗi logic**: Bỏ qua các bước kiểm tra bảo mật quan trọng.
- **Race conditions**: Xung đột tài nguyên do xử lý lỗi không sạch sẽ.
- **Lộ thông tin**: Trả về các thông báo lỗi chi tiết giúp kẻ tấn công trinh sát hệ thống.
- **Từ chối dịch vụ (DoS)**: Không giải phóng tài nguyên (file, bộ nhớ) khi gặp ngoại lệ.

## Nguyên tắc phòng chống cốt lõi
1.  **Dự báo tình huống xấu nhất**: Lập kế hoạch xử lý cho mọi lỗi hệ thống có thể xảy ra ngay tại nơi chúng phát sinh.
2.  **Thất bại an toàn (Fail Closed)**: Nếu một phần của giao dịch (ví dụ: trừ tiền tài khoản) bị lỗi, toàn bộ giao dịch phải được khôi phục (roll back) về trạng thái ban đầu. Tuyệt đối không được "Fail Open" (cho phép tiếp tục dù gặp lỗi).
3.  **Xử lý lỗi tập trung**: Tránh việc mỗi hàm xử lý lỗi một kiểu. Nên có một bộ xử lý ngoại lệ toàn cục để đảm bảo tính thống nhất.
4.  **Giới hạn tài nguyên**: Sử dụng rate limiting, quota và throttling để ngăn chặn các điều kiện bất thường xảy ra ngay từ đầu.

## Cách thực hiện
- Sử dụng xác thực đầu vào nghiêm ngặt.
- Ghi nhật ký và cảnh báo cho các lỗi quan trọng (kết nối với [[logging-alerting-failures|A09]]).
- Thực hiện Code Review và phân tích tĩnh để tìm các điểm xử lý lỗi yếu.
- Chạy stress test và pentest để xem hệ thống phản ứng thế nào dưới áp lực cực lớn hoặc các dữ liệu đầu vào quái dị.

## Kịch bản tấn công ví dụ
- **Cạn kiệt tài nguyên**: Ứng dụng bắt ngoại lệ khi tải file lên nhưng không đóng file handle. Kẻ tấn công liên tục gây lỗi để làm cạn kiệt tài nguyên hệ thống, gây DoS.
- **Lộ dữ liệu nhạy cảm**: Ứng dụng hiển thị lỗi cơ sở dữ liệu chi tiết cho người dùng. Kẻ tấn công sử dụng thông tin này để tinh chỉnh cuộc tấn công SQL Injection.

## Liên kết liên quan
- [[logging-alerting-failures|Thất bại trong ghi nhật ký và cảnh báo]]
- [[application-security|An ninh ứng dụng]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
