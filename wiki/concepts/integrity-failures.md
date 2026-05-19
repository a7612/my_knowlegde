---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A08 Software or Data Integrity Failures.md"]
tags: ["owasp", "integrity", "deserialization", "code-signing", "cicd"]
---

# Thất bại về tính toàn vẹn của phần mềm hoặc dữ liệu (Software or Data Integrity Failures)

**Thất bại về tính toàn vẹn** (A08:2025) tập trung vào việc thiếu kiểm tra tính toàn vẹn của mã nguồn, thư viện và dữ liệu. Điều này xảy ra khi ứng dụng tin tưởng vào các thành phần hoặc dữ liệu từ các nguồn không được xác minh, cho phép kẻ tấn công thay thế chúng bằng mã độc hoặc dữ liệu giả mạo.

## Các kịch bản rủi ro
*   **Cập nhật phần mềm không được ký số**: Ứng dụng tự động tải và cài đặt bản cập nhật mà không kiểm tra chữ ký số để xác minh nguồn gốc.
*   **Giải tuần tự hóa không an toàn (Insecure Deserialization)**: Chuyển đổi dữ liệu từ dạng byte (đã bị kẻ tấn công sửa đổi) trở lại thành đối tượng trong bộ nhớ, dẫn đến thực thi mã từ xa (RCE).
*   **Thư viện từ nguồn không tin cậy**: Sử dụng module từ các CDN công cộng hoặc repository không được kiểm soát mà không kiểm tra mã băm (hash).
*   **Thỏa hiệp Pipeline CI/CD**: Kẻ tấn công thay đổi mã trong quá trình build do hệ thống CI/CD không có cơ chế kiểm tra tính toàn vẹn chặt chẽ.

## Cách phòng tránh
1.  **Sử dụng chữ ký số**: Luôn xác minh chữ ký số của các bản cập nhật và dữ liệu quan trọng.
2.  **Repository tin cậy**: Chỉ sử dụng các kho lưu trữ (npm, Maven, v.v.) đã được phê duyệt. Đối với các hệ thống rủi ro cao, nên lưu trữ repository nội bộ đã qua kiểm duyệt.
3.  **Kiểm tra tính toàn vẹn của dữ liệu tuần tự**: Tuyệt đối không chấp nhận dữ liệu tuần tự từ các nguồn không tin cậy mà không có kiểm tra chữ ký hoặc mã hóa để phát hiện thay đổi.
4.  **Bảo vệ Pipeline**: Đảm bảo phân chia quyền hạn và kiểm soát truy cập chặt chẽ cho toàn bộ quy trình từ build đến deploy.

## Kịch bản tấn công ví dụ
Một ứng dụng Java nhận các đối tượng được tuần tự hóa từ client để duy trì trạng thái người dùng. Kẻ tấn công nhận thấy chữ ký đối tượng Java trong dữ liệu và sử dụng công cụ chuyên dụng để tạo ra một đối tượng độc hại. Khi ứng dụng giải tuần tự hóa đối tượng này, nó thực thi mã độc và cho phép kẻ tấn công chiếm quyền điều khiển máy chủ.

## Liên kết liên quan
- [[software-supply-chain|Thất bại trong chuỗi cung ứng phần mềm]]
- [[cryptographic-failures|Thất bại trong mã hóa]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
