---
sources: ["raw/Hack The Box/Introduction to Networking/Connection Establishment - Cryptography.md"]
tags: ["cryptography", "security", "encryption", "aes", "rsa", "cipher-modes"]
---

# Kiến thức cơ bản về Mật mã học (Cryptography Basics)

Mật mã học là nền tảng để đảm bảo tính bảo mật, toàn vẹn và xác thực của dữ liệu trên Internet thông qua các thuật toán toán học phức tạp.

## 1. Các loại Mã hóa chính

### Mã hóa Đối xứng (Symmetric Encryption)
*   **Cơ chế**: Sử dụng cùng một khóa (Secret Key) cho cả mã hóa và giải mã.
*   **Đặc điểm**: Nhanh, hiệu quả khi xử lý lượng dữ liệu lớn.
*   **Thách thức**: Khó khăn trong việc phân phối, lưu trữ và trao đổi khóa an toàn.
*   **So sánh thuật toán**:
    *   **DES (Data Encryption Standard)**: Khóa 64-bit (thực tế 56-bit do 8-bit checksum). Hiện đã lỗi thời do khóa ngắn, dễ bị tấn công brute-force.
    *   **3DES (Triple DES)**: Thực hiện 3 vòng mã hóa (mã hóa - giải mã - mã hóa). An toàn hơn DES nhưng chậm và dần bị thay thế.
    *   **AES (Advanced Encryption Standard)**: Tiêu chuẩn hiện đại nhất. Sử dụng khóa 128-bit, 192-bit hoặc 256-bit. Nhanh hơn và an toàn hơn DES do cấu trúc thuật toán hiệu quả hơn.

### Mã hóa Bất đối xứng (Asymmetric / Public-Key Encryption)
*   **Cơ chế**: Sử dụng cặp khóa: **Khóa công khai (Public Key)** để mã hóa và **Khóa bí mật (Private Key)** để giải mã.
*   **Ưu điểm**: Độ bảo mật cao, giải quyết triệt để vấn đề trao đổi khóa (Public Key có thể công khai cho tất cả mọi người).
*   **Ứng dụng**: Chữ ký số, SSL/TLS, SSH, VPN, PKI.
*   **Ví dụ**: **RSA**, **PGP**, **ECC** (Elliptic Curve Cryptography).

## 2. Các chế độ mã hóa khối (Cipher Modes)
Quy định cách thuật toán mã hóa khối (thường là 64 hoặc 128 bit) xử lý và kết hợp các khối dữ liệu:

| Chế độ | Đặc điểm | Ứng dụng/Ghi chú |
| :--- | :--- | :--- |
| **ECB (Electronic Code Book)** | Mỗi khối được mã hóa độc lập. | **Không an toàn**: Không che giấu được mẫu dữ liệu, dễ bị phân tích thống kê. |
| **CBC (Cipher Block Chaining)** | Khối hiện tại phụ thuộc vào khối trước đó. | Chế độ mặc định của AES. Dùng cho mã hóa ổ đĩa (TrueCrypt, VeraCrypt) và email (TLS/SSL). |
| **CFB (Cipher Feedback)** | Thích hợp mã hóa luồng dữ liệu thời gian thực. | Dùng trong mã hóa mạng hoặc các tệp đang truyền (BitLocker, PKCS). |
| **OFB (Output Feedback)** | Tạo luồng khóa độc lập với bản rõ. | Tốt cho truyền thông thời gian thực, có trong giao thức SSH. |
| **CTR (Counter)** | Sử dụng bộ đếm để mã hóa luồng dữ liệu. | Dùng trong IPsec, BitLocker, và các kịch bản thời gian thực cần xử lý song song. |
| **GCM (Galois/Counter Mode)** | Kết hợp bảo mật và kiểm tra tính toàn vẹn. | Phổ biến trong VPN, giao tiếp không dây và các giao thức bảo mật hiện đại. |

## Liên kết liên quan
- [[my_knowlegde/concepts/key-exchange|Cơ chế trao đổi khóa]]
- [[my_knowlegde/concepts/authentication-protocols|Giao thức xác thực]]
- [[my_knowlegde/concepts/network-security|Bảo mật mạng]]
