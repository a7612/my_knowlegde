---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A04 Cryptographic Failures.md"]
tags: ["owasp", "cryptography", "encryption", "data-protection", "pqc"]
---

# Thất bại trong mã hóa (Cryptographic Failures)

**Thất bại trong mã hóa** (A04:2025) tập trung vào các lỗi liên quan đến việc thiếu mã hóa, sử dụng mã hóa yếu, rò rỉ khóa mã hóa và các lỗi logic liên quan. Rủi ro này thường dẫn đến việc lộ lọt dữ liệu nhạy cảm hoặc chiếm quyền điều khiển hệ thống.

## Các lỗi thường gặp
*   **Dữ liệu truyền đi không được mã hóa**: Sử dụng giao thức HTTP, FTP, SMTP không bảo mật.
*   **Thuật toán yếu hoặc lỗi thời**: Sử dụng MD5, SHA1, RC4, DES hoặc các chế độ mã hóa không an toàn như ECB.
*   **Quản lý khóa kém**: Lưu trữ khóa trong mã nguồn, không thay đổi khóa định kỳ (rotation) hoặc sử dụng khóa mặc định.
*   **Sử dụng số ngẫu nhiên dự đoán được**: Sử dụng bộ tạo số ngẫu nhiên không đủ độ hỗn loạn (entropy) cho các mục đích bảo mật.
*   **Thiếu xác thực khi mã hóa**: Chỉ mã hóa mà không có cơ chế kiểm tra tính toàn vẹn (Authenticated Encryption).
*   **Lỗ hổng Padding Oracle**: Cho phép kẻ tấn công giải mã dữ liệu dựa trên các phản hồi lỗi từ phía máy chủ.

## Cách phòng tránh
1.  **Phân loại dữ liệu**: Xác định dữ liệu nào là nhạy cảm (PII, thẻ tín dụng, hồ sơ sức khỏe) để áp dụng mức độ bảo vệ tương ứng.
2.  **Mã hóa mọi nơi**:
    *   **Khi truyền đi (In transit)**: Sử dụng TLS >= 1.2, thực thi HSTS.
    *   **Khi lưu trữ (At rest)**: Mã hóa dữ liệu trên đĩa, sử dụng HSM hoặc dịch vụ quản lý khóa đám mây.
3.  **Thuật toán hiện đại**: Sử dụng Argon2, scrypt hoặc PBKDF2 cho mật khẩu; AES-GCM cho mã hóa dữ liệu.
4.  **Lưu trữ mật khẩu an toàn**: Luôn sử dụng salt và hàm băm thích ứng (adaptive hashing).
5.  **Chuẩn bị cho Kỷ nguyên Hậu lượng tử (PQC)**: Bắt đầu lộ trình chuyển đổi sang các thuật toán kháng lượng tử trước năm 2030 cho các hệ thống rủi ro cao.

## Kịch bản tấn công ví dụ
Một trang web không thực thi TLS cho tất cả các trang. Kẻ tấn công trong mạng Wi-Fi công cộng thực hiện hạ cấp kết nối từ HTTPS xuống HTTP, đánh cắp Cookie phiên của người dùng và chiếm đoạt tài khoản.

## Liên kết liên quan
- [[cryptography-basics|Cơ bản về mật mã học]]
- [[authentication-failures|Thất bại trong xác thực]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
