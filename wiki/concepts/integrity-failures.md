---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A08 Software or Data Integrity Failures.md"]
tags: ["owasp", "integrity", "deserialization", "code-signing", "cicd"]
---

# Thất bại về tính toàn vẹn của phần mềm hoặc dữ liệu (Software or Data Integrity Failures)

**Thất bại về tính toàn vẹn** (A08:2025) tập trung vào việc thiếu kiểm tra tính toàn vẹn của mã nguồn, thư viện và dữ liệu. Điều này xảy ra khi ứng dụng tin tưởng vào các thành phần hoặc dữ liệu từ các nguồn không được xác minh, cho phép kẻ tấn công thay thế chúng bằng mã độc hoặc dữ liệu giả mạo.

## Các kịch bản rủi ro
*   **Cập nhật phần mềm không được ký số**: Ứng dụng tự động tải và cài đặt bản cập nhật mà không kiểm tra chữ ký số để xác minh nguồn gốc.
*   **Giải tuần tự hóa không an toàn (Insecure Deserialization - CWE-502)**: Chuyển đổi dữ liệu từ dạng byte (đã bị kẻ tấn công sửa đổi) trở lại thành đối tượng trong bộ nhớ.
    *   **Hệ quả**: Kẻ tấn công có thể thay đổi các đối tượng không mong muốn, thực thi mã từ xa (RCE) thông qua các "gadget chains" (chuỗi phương thức tự thực thi) hoặc gây lỗi treo ứng dụng (DoS).
    *   **Ví dụ**: Trong Java (Pickle trong Python hoặc unserialize trong PHP), việc không kiểm tra nguồn gốc dữ liệu trước khi đọc đối tượng có thể cho phép thực thi `/bin/sh`.

## Cách phòng tránh
1.  **Sử dụng chữ ký số**: Luôn xác minh chữ ký số (ví dụ: sử dụng HMAC) của các bản cập nhật và dữ liệu quan trọng để đảm bảo dữ liệu không bị sửa đổi.
2.  **Repository tin cậy**: Chỉ sử dụng các kho lưu trữ (npm, Maven, v.v.) đã được phê duyệt. Đối với các hệ thống rủi ro cao, nên lưu trữ repository nội bộ đã qua kiểm duyệt.
3.  **Bảo vệ quá trình Giải tuần tự hóa**:
    *   **Chỉ chấp nhận danh sách trắng (Allow-list)**: Chỉ cho phép giải tuần tự hóa các lớp (classes) cụ thể và an toàn.
    *   **Sử dụng định dạng dữ liệu thuần túy**: Ưu tiên JSON hoặc XML thay vì các định dạng nhị phân của ngôn ngữ để tránh tự động thực thi mã.
    *   **Đánh dấu trường transient**: Sử dụng từ khóa `transient` (trong Java) cho các trường nhạy cảm để chúng không bị tuần tự hóa/giải tuần tự hóa.
4.  **Bảo vệ Pipeline**: Đảm bảo phân chia quyền hạn và kiểm soát truy cập chặt chẽ cho toàn bộ quy trình từ build đến deploy.

## Kịch bản tấn công ví dụ
Một ứng dụng Java nhận các đối tượng được tuần tự hóa từ client để duy trì trạng thái người dùng. Kẻ tấn công nhận thấy chữ ký đối tượng Java trong dữ liệu và sử dụng công cụ chuyên dụng để tạo ra một đối tượng độc hại. Khi ứng dụng giải tuần tự hóa đối tượng này, nó thực thi mã độc và cho phép kẻ tấn công chiếm quyền điều khiển máy chủ.

## Liên kết liên quan
- [[software-supply-chain|Thất bại trong chuỗi cung ứng phần mềm]]
- [[cryptographic-failures|Thất bại trong mã hóa]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
