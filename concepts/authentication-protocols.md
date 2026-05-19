---
sources: ["raw/Hack The Box/Introduction to Networking/Connection Establishment - Authentication Protocols.md", "raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Wireless Networks.md"]
tags: ["security", "authentication", "protocols", "oauth", "kerberos", "mfa", "tacacs"]
---

# Giao thức Xác thực (Authentication Protocols)

Xác thực là quy trình xác minh danh tính của người dùng, thiết bị hoặc thực thể trong mạng trước khi cho phép truy cập tài nguyên. Các giao thức này đảm bảo trao đổi thông tin an toàn, duy trì tính bảo mật và toàn vẹn của dữ liệu nhạy cảm.

## 1. Các giao thức xác thực phổ biến

| Giao thức | Mô tả | Ứng dụng |
| :--- | :--- | :--- |
| **Kerberos** | Dựa trên vé (tickets) và KDC (Key Distribution Center). | Môi trường Windows AD (Active Directory). |
| **SRP** | Giao thức dựa trên mật khẩu, chống nghe lén và tấn công MITM. | Xác thực an toàn qua kênh không tin cậy. |
| **SSL / TLS** | Giao thức mật mã đảm bảo liên lạc an toàn qua mạng máy tính. | HTTPS, FTPS, bảo mật email. |
| **OAuth** | Tiêu chuẩn mở cho phép ủy quyền mà không cần chia sẻ mật khẩu. | Đăng nhập bằng Google/Facebook vào ứng dụng khác. |
| **OpenID** | Giao thức xác thực phi tập trung (Single Sign-On). | Một danh tính cho nhiều website. |
| **SAML** | Dựa trên XML để trao đổi dữ liệu xác thực và ủy quyền. | Đăng nhập một lần (SSO) doanh nghiệp. |
| **SSO** | Cho phép dùng một bộ thông tin đăng nhập cho nhiều ứng dụng. | Hệ thống quản lý doanh nghiệp. |
| **PKI** | Hệ thống sử dụng cặp khóa và chứng chỉ số để xác thực. | Xác thực máy chủ, chữ ký số. |
| **PAP** | Gửi mật khẩu dạng văn bản thuần (Rất không an toàn). | Các hệ thống cũ, đơn giản. |
| **CHAP** | Sử dụng bắt tay ba bước để xác thực. | PPP, kết nối mạng diện rộng. |
| **EAP** | Khung hỗ trợ nhiều phương thức xác thực khác nhau. | Mạng không dây, VPN. |
| **SSH / HTTPS** | Các giao thức mặc định sử dụng mã hóa mạnh (SSL/TLS). | Quản trị từ xa, duyệt web an toàn. |

## 2. Xác thực đa yếu tố (MFA / 2FA)
MFA sử dụng kết hợp hai hoặc nhiều yếu tố khác nhau để xác minh danh tính:
*   **Kiến thức (Something you know)**: Mật khẩu, mã PIN.
*   **Sở hữu (Something you have)**: Điện thoại (mã OTP), thẻ cứng, token bảo mật.
*   **Sinh trắc (Something you are)**: Vân tay, khuôn mặt, mống mắt.
*   **FIDO (Fast IDentity Online)**: Liên minh các công ty phát triển tiêu chuẩn mở cho xác thực mạnh, giảm phụ thuộc vào mật khẩu.

## 3. Xác thực trong mạng không dây (Cisco)
*   **LEAP (Lightweight EAP)**: Do Cisco phát triển, dựa trên thuật toán RC4. Dễ bị tấn công từ điển và hiện đã bị thay thế.
*   **PEAP (Protected EAP)**: 
    *   Sử dụng đường hầm **TLS** để bảo vệ quá trình xác thực.
    *   Sử dụng chứng chỉ phía máy chủ (server-side certificate) để xác thực máy chủ.
    *   Mã hóa mã băm **MSCHAPv2**.
    *   Hỗ trợ các thuật toán mã hóa mạnh như **AES** và **3DES**.
*   **EAP-TLS**: Sử dụng chứng chỉ số cho cả máy khách và máy chủ, được coi là an toàn nhất.

## 4. TACACS+
**Terminal Access Controller Access-Control System Plus (TACACS+)** là giao thức dùng để xác thực và phân quyền cho người dùng truy cập thiết bị mạng (Router, Switch).
*   **Đặc điểm**: Mã hóa **toàn bộ gói tin yêu cầu**, bảo vệ thông tin đăng nhập và dữ liệu phiên làm việc khỏi sự can thiệp của bên thứ ba.
*   **Bảo mật**: Thường sử dụng kết hợp với SSL/TLS hoặc IPsec để tăng cường an toàn.

## Liên kết liên quan
- [[my_knowlegde/concepts/cryptography-basics|Mật mã học cơ bản]]
- [[my_knowlegde/concepts/key-exchange|Cơ chế trao đổi khóa]]
- [[my_knowlegde/concepts/network-security|Bảo mật mạng]]
- [[my_knowlegde/concepts/wireless-networks|Mạng không dây]]
