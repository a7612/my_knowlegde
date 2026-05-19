---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A03 Software Supply Chain Failures.md"]
tags: ["owasp", "supply-chain", "dependencies", "sbom", "cicd-security"]
---

# Thất bại trong chuỗi cung ứng phần mềm (Software Supply Chain Failures)

**Thất bại trong chuỗi cung ứng phần mềm** (A03:2025) là các sự cố hoặc sự thỏa hiệp trong quy trình xây dựng, phân phối hoặc cập nhật phần mềm. Đây là một sự mở rộng của rủi ro "Sử dụng các thành phần có lỗ hổng đã biết" để bao hàm toàn bộ hệ sinh thái từ mã nguồn bên thứ ba, công cụ xây dựng đến cơ sở hạ tầng phân phối.

## Tại sao bạn dễ bị tấn công?
*   **Thiếu theo dõi phụ thuộc**: Không quản lý được các thư viện bên thứ ba (bao gồm cả các phụ thuộc bắc cầu - transitive dependencies).
*   **Thành phần lỗi thời**: Sử dụng hệ điều hành, máy chủ web, DBMS hoặc thư viện không còn được hỗ trợ hoặc chứa lỗ hổng.
*   **Thiếu quy trình quản lý thay đổi**: Không kiểm soát được các tiện ích mở rộng IDE, các cập nhật trong kho mã nguồn (repository) hoặc các registry chứa image/library.
*   **Chuỗi cung ứng không được bảo vệ**: Không áp dụng nguyên tắc đặc quyền tối thiểu hoặc phân chia nhiệm vụ (separation of duty) cho các hệ thống build.
*   **Pipeline CI/CD yếu**: Hệ thống build có bảo mật kém hơn chính ứng dụng mà nó tạo ra.

## Cách phòng tránh
1.  **Quản lý SBOM (Software Bill of Materials)**: Tạo và quản lý danh sách thành phần phần mềm tập trung để biết chính xác những gì đang có trong hệ thống.
2.  **Quét lỗ hổng liên tục**: Sử dụng các công cụ như OWASP Dependency Check, Dependency Track hoặc Snyk để giám sát các CVE mới nhất liên quan đến thành phần đang dùng.
3.  **Nguồn tin cậy**: Chỉ tải các thành phần từ các nguồn chính thức qua kết nối an toàn, ưu tiên các gói đã được ký số (signed packages).
4.  **Củng cố Pipeline CI/CD**: Bật MFA, khóa chặt quyền truy cập IAM, sử dụng bí mật (secrets) theo phạm vi môi trường và ghi nhật ký chống giả mạo.
5.  **Triển khai theo giai đoạn**: Không cập nhật đồng thời cho toàn bộ hệ thống; sử dụng canary deployment để hạn chế rủi ro nếu một nhà cung cấp bị thỏa hiệp.

## Kịch bản tấn công ví dụ
- **Tấn công SolarWinds (2019)**: Một nhà cung cấp tin cậy bị cài mã độc vào quy trình cập nhật, dẫn đến 18,000 tổ chức bị ảnh hưởng.
- **Sâu npm (2025)**: Worm tự nhân bản trên npm sử dụng script sau khi cài đặt để đánh cắp token và tự động đẩy các phiên bản độc hại của các gói khác lên registry.

## Liên kết liên quan
- [[integrity-failures|Thất bại về tính toàn vẹn]]
- [[security-misconfiguration|Cấu hình sai bảo mật]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
