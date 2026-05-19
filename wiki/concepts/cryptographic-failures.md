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

## Các nguyên tắc bảo vệ (Implementation)

### 1. Phân loại dữ liệu (Data Classification)
Xác định dữ liệu nào là nhạy cảm (mật khẩu, số thẻ tín dụng, hồ sơ sức khỏe, PII) để áp dụng mức độ bảo vệ tương ứng. Quy tắc tối thiểu là: **Không lưu trữ dữ liệu nhạy cảm nếu không thực sự cần thiết**.

### 2. Sử dụng thư viện đã được kiểm chứng
**Không bao giờ tự tạo giao thức hoặc thuật toán mật mã riêng**. Hãy sử dụng các thư viện chuẩn, mã nguồn mở và đã được cộng đồng kiểm định như:
*   **Google Tink**: Hỗ trợ quản lý khóa và mã hóa đa nền tảng.
*   **Libsodium**: Thư viện mật mã hiện đại, dễ sử dụng và an toàn.
*   Các dịch vụ KMS của đám mây (AWS KMS, Azure Key Vault, Google Cloud KMS).

### 3. Quản lý vòng đời khóa (Key Life Cycle)
*   **Lưu trữ an toàn**: Không bao giờ để khóa trong mã nguồn hoặc file cấu hình. Sử dụng các kho lưu trữ bí mật (Secrets Vault).
*   **Ghi nhật ký**: Theo dõi mọi lượt truy cập vào khóa để phục vụ điều tra.
*   **Luân chuyển khóa (Rotation)**: Thay đổi khóa định kỳ hoặc ngay sau khi nghi ngờ bị lộ.

### 4. Tính linh hoạt trong mật mã (Cryptographic Agility)
Thiết kế hệ thống sao cho có thể thay đổi thuật toán hoặc độ dài khóa một cách cấu hình được, thay vì sửa mã nguồn. Điều này giúp ứng dụng sẵn sàng cho các thay đổi trong tương lai (ví dụ: chuyển sang thuật toán kháng lượng tử).

## Cách phòng tránh
1.  **Mã hóa mọi nơi**:
    *   **Khi truyền đi (In transit)**: Sử dụng TLS >= 1.2 (ưu tiên 1.3), thực thi HSTS và sử dụng cờ `Secure` cho Cookie.
    *   **Khi lưu trữ (At rest)**: Mã hóa dữ liệu trên đĩa và trong cơ sở dữ liệu.
2.  **Thuật toán hiện đại**:
    *   Mật khẩu: Sử dụng Argon2, scrypt hoặc PBKDF2 với salt ngẫu nhiên.
    *   Dữ liệu: Sử dụng AES-GCM (Authenticated Encryption) để đảm bảo cả tính bí mật và toàn vẹn.
3.  **Làm cứng trình duyệt (Hardening)**: Sử dụng tiêu đề CSP để nâng cấp tự động từ HTTP lên HTTPS.

## Kịch bản tấn công ví dụ
Một trang web không thực thi TLS cho tất cả các trang. Kẻ tấn công trong mạng Wi-Fi công cộng thực hiện hạ cấp kết nối từ HTTPS xuống HTTP (SSL Stripping), đánh cắp Cookie phiên của người dùng và chiếm đoạt tài khoản.

## Liên kết liên quan
- [[cryptography-basics|Cơ bản về mật mã học]]
- [[authentication-failures|Thất bại trong xác thực]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
- [[owasp-proactive-controls|OWASP Proactive Controls]]

