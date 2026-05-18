---
sources: ["raw/Hack The Box/Introduction to Networking/Connection Establishment - Key Exchange Mechanisms.md"]
tags: ["cryptography", "security", "key-exchange", "dh", "ike", "ecdh", "rsa"]
---

# Cơ chế trao đổi khóa (Key Exchange Mechanisms)

Trao đổi khóa là quy trình cho phép hai bên thỏa thuận một khóa bí mật chung (**Shared Secret Key**) qua một kênh truyền thông không an toàn. Đây là bước then chốt để thiết lập kênh truyền tin mã hóa.

## 1. Các thuật toán phổ biến

| Thuật toán | Viết tắt | Đặc điểm | Bảo mật |
| :--- | :--- | :--- | :--- |
| **Diffie-Hellman** | DH | Dựa trên bài toán logarit rời rạc. Cho phép tạo khóa mà không cần giao tiếp trước. | Cần thông số mạnh và xác thực để tránh MITM. Chậm hơn ECDH. |
| **RSA** | RSA | Dựa trên việc nhân các số nguyên tố lớn. Dùng cho cả mã hóa khóa và chữ ký số. | Phổ biến, an toàn với kích thước khóa đủ lớn. Nặng về tính toán hơn ECC. |
| **Elliptic Curve Diffie-Hellman** | ECDH | Biến thể của DH sử dụng mật mã đường cong Elliptic (ECC). | Hiệu quả và nhanh hơn DH truyền thống ở cùng mức bảo mật. Cung cấp tính năng Forward Secrecy. |
| **Elliptic Curve Digital Signature** | ECDSA | Sử dụng ECC để tạo chữ ký số phục vụ xác thực. | Hiệu quả và an toàn cao cho việc tạo và xác minh chữ ký. |

## 2. Giao thức IKE (Internet Key Exchange)
IKE là giao thức được dùng để thiết lập và duy trì các phiên giao tiếp bảo mật (chủ yếu trong VPN). Nó kết hợp Diffie-Hellman và các kỹ thuật mật mã khác để đàm phán tham số bảo mật.

### Hai chế độ hoạt động chính:
*   **Main Mode (Chế độ chính)**: 
    *   Thực hiện qua **3 giai đoạn** (6 thông điệp).
    *   **Ưu điểm**: Linh hoạt, bảo mật cao, bảo vệ định danh của các bên tham gia.
    *   **Nhược điểm**: Hiệu suất chậm hơn Aggressive Mode do nhiều vòng trao đổi.
*   **Aggressive Mode (Chế độ tích cực)**: 
    *   Thực hiện qua **2 giai đoạn** (3 thông điệp).
    *   **Ưu điểm**: Tốc độ nhanh hơn, giảm số lượt trao đổi thông tin.
    *   **Nhược điểm**: **Kém an toàn hơn** vì không cung cấp tính năng bảo vệ định danh, dễ bị tấn công thu thập thông tin.

### Khóa chia sẻ trước (Pre-Shared Key - PSK)
Một giá trị bí mật được chia sẻ thủ công giữa hai bên trước khi bắt đầu quy trình trao đổi khóa. PSK giúp xác thực các bên nhưng cần được truyền qua kênh an toàn ngoài băng (out-of-band) để tránh bị lộ.

## 3. Forward Secrecy
Cơ chế đảm bảo rằng ngay cả khi khóa bí mật dài hạn (Private Key) bị lộ trong tương lai, các phiên giao tiếp cũ đã được ghi lại vẫn không thể bị giải mã. ECDH thường được dùng để cung cấp tính năng này.

## Liên kết liên quan
- [[cryptography-basics|Mật mã học cơ bản]]
- [[vpn-technology|Công nghệ VPN]]
- [[authentication-protocols|Giao thức xác thực]]
