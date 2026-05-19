---
sources: 
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C1 Implement Access Control.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C2 Use Cryptography to Protect Data.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C3 Validate all Input & Handle Exceptions.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C4 Address Security from the Start.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C5 Secure By Default Configurations.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C6 Keep your Components Secure.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C7 Secure Digital Identities.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C8 Leverage Browser Security Features.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C9 Implement Security Logging and Monitoring.md"
  - "raw/OWASP/Top Ten - 2024 - Proactive Controls/OWASP Top 10 Proactive Controls - C10 Stop Server Side Request Forgery.md"
tags: ["owasp", "proactive-controls", "secure-coding", "development", "mitigation"]
---

# OWASP Top 10 Proactive Controls

**OWASP Top 10 Proactive Controls** là danh sách các kỹ thuật kiểm soát bảo mật quan trọng nhất mà mọi dự án phát triển phần mềm nên áp dụng ngay từ đầu. Khác với "Top Ten Project" tập trung vào các rủi ro, danh sách này tập trung vào các **giải pháp thực thi** cho nhà phát triển.

## Danh sách 10 biện pháp kiểm soát chủ động

1.  **[[broken-access-control|C1: Triển khai Kiểm soát truy cập (Implement Access Control)]]**: Đảm bảo người dùng chỉ có thể thực hiện các hành động được phép.
2.  **[[cryptographic-failures|C2: Sử dụng Mật mã để Bảo vệ dữ liệu (Use Cryptography to Protect Data)]]**: Mã hóa dữ liệu nhạy cảm khi lưu trữ và truyền tải.
3.  **[[injection-vulnerabilities|C3: Xác thực mọi đầu vào & Xử lý ngoại lệ (Validate all Input & Handle Exceptions)]]**: Ngăn chặn dữ liệu độc hại và xử lý lỗi an toàn.
4.  **[[insecure-design|C4: Giải quyết Bảo mật ngay từ đầu (Address Security from the Start)]]**: Tích hợp bảo mật vào kiến trúc và thiết kế.
5.  **[[security-misconfiguration|C5: Cấu hình mặc định An toàn (Secure By Default Configurations)]]**: Phần mềm phải an toàn ngay khi xuất xưởng mà không cần cấu hình thêm.
6.  **[[software-supply-chain|C6: Giữ cho các Thành phần an toàn (Keep your Components Secure)]]**: Quản lý thư viện và phụ thuộc bên thứ ba.
7.  **[[authentication-failures|C7: Bảo mật Định danh kỹ thuật số (Secure Digital Identities)]]**: Triển khai xác thực mạnh (MFA) và quản lý phiên an toàn.
8.  **[[browser-security-features|C8: Tận dụng các tính năng Bảo mật trình duyệt (Leverage Browser Security Features)]]**: Sử dụng CSP, HSTS và các tiêu đề bảo mật khác.
9.  **[[logging-alerting-failures|C9: Triển khai Ghi nhật ký và Giám sát bảo mật (Implement Security Logging and Monitoring)]]**: Phát hiện và phản ứng với sự cố kịp thời.
10. **[[server-side-request-forgery|C10: Ngăn chặn Giả mạo yêu cầu phía máy chủ (Stop Server Side Request Forgery - SSRF)]]**: Bảo vệ các yêu cầu HTTP nội bộ.


## Tầm quan trọng
Việc áp dụng các biện pháp này giúp giảm thiểu đáng kể chi phí sửa chữa lỗ hổng ở các giai đoạn sau của vòng đời phát triển (SDLC) và xây dựng niềm tin cho người dùng cuối.

## Liên kết liên quan
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
- [[application-security|An ninh ứng dụng]]
- [[memory-safety-vulnerabilities|Lỗ hổng an toàn bộ nhớ]]
