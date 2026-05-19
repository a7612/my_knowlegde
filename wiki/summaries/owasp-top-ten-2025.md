---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - Home.md", "raw/OWASP/2025/OWASP Top Ten 2025 - Introduction.md"]
tags: ["owasp", "security-risks", "web-application", "application-security", "vulnerabilities"]
---

# OWASP Top Ten 2025

**OWASP Top Ten 2025** là phiên bản mới nhất của tài liệu nhận thức tiêu chuẩn dành cho các nhà phát triển và chuyên gia bảo mật ứng dụng web. Nó đại diện cho sự đồng thuận rộng rãi về các rủi ro bảo mật quan trọng nhất đối với các ứng dụng web hiện nay.

## Danh sách 10 rủi ro hàng đầu năm 2025

1.  **[[broken-access-control|A01:2025 - Kiểm soát truy cập bị hỏng (Broken Access Control)]]**: Duy trì vị trí số 1. Bao gồm cả rủi ro Server-Side Request Forgery (SSRF).
2.  **[[security-misconfiguration|A02:2025 - Cấu hình sai bảo mật (Security Misconfiguration)]]**: Tăng từ hạng 5 lên hạng 2 do sự phổ biến của phần mềm có khả năng cấu hình cao.
3.  **[[software-supply-chain|A03:2025 - Thất bại trong chuỗi cung ứng phần mềm (Software Supply Chain Failures)]]**: Mở rộng từ "Thành phần dễ bị tổn thương và lỗi thời" để bao quát toàn bộ hệ sinh thái phụ thuộc.
4.  **[[cryptographic-failures|A04:2025 - Thất bại trong mã hóa (Cryptographic Failures)]]**: Giảm xuống hạng 4, tập trung vào các lỗi liên quan đến bảo vệ dữ liệu nhạy cảm.
5.  **[[injection-vulnerabilities|A05:2025 - Lỗi tiêm (Injection)]]**: Bao gồm SQL Injection, XSS và các lỗi tiêm vào trình thông dịch khác.
6.  **[[insecure-design|A06:2025 - Thiết kế không an toàn (Insecure Design)]]**: Tập trung vào các thiếu sót trong thiết kế và kiến trúc thay vì các lỗi thực thi.
7.  **[[authentication-failures|A07:2025 - Thất bại trong xác thực (Authentication Failures)]]**: Tên mới cho "Thất bại trong nhận dạng và xác thực", phản ánh chính xác hơn các CWE liên quan.
8.  **[[integrity-failures|A08:2025 - Thất bại về tính toàn vẹn của phần mềm hoặc dữ liệu (Software or Data Integrity Failures)]]**: Tập trung vào việc không xác minh tính toàn vẹn của mã và dữ liệu.
9.  **[[logging-alerting-failures|A09:2025 - Thất bại trong ghi nhật ký và cảnh báo bảo mật (Security Logging & Alerting Failures)]]**: Nhấn mạnh tầm quan trọng của chức năng cảnh báo để thúc đẩy hành động kịp thời.
10. **[[exceptional-conditions-handling|A10:2025 - Xử lý sai các điều kiện bất thường (Mishandling of Exceptional Conditions)]]**: **DANH MỤC MỚI**, tập trung vào xử lý lỗi kém, lỗi logic và thất bại trong việc đảm bảo an toàn khi gặp sự cố.

## Các thay đổi chính so với phiên bản 2021
- **SSRF** hiện đã được tích hợp vào danh mục **Kiểm soát truy cập bị hỏng (A01)**.
- **Thất bại trong chuỗi cung ứng phần mềm (A03)** được mở rộng đáng kể để phản ánh các mối đe dọa hiện đại như tấn công SolarWinds hoặc các worm tự nhân bản trên npm.
- **Xử lý sai các điều kiện bất thường (A10)** là một danh mục hoàn toàn mới, thay thế cho các khái niệm chung chung về chất lượng mã nguồn bằng các hướng dẫn cụ thể về xử lý lỗi an toàn.

## Tầm quan trọng
Việc tuân thủ OWASP Top Ten giúp các tổ chức giảm thiểu đáng kể các lỗ hổng phổ biến nhất, từ đó bảo vệ dữ liệu người dùng và duy trì uy tín của doanh nghiệp trong môi trường số ngày càng phức tạp.

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[penetration-testing|Kiểm thử xâm nhập]]
- [[vulnerability-assessment|Đánh giá lỗ hổng]]
