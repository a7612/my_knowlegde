---
sources: ["raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Virtual Private Networks.md"]
tags: ["networking", "security", "vpn", "ipsec", "encryption", "pptp"]
---

# Công nghệ VPN (Virtual Private Network)

**VPN** là công nghệ tạo ra một kết nối bảo mật và được mã hóa giữa một mạng riêng và một thiết bị từ xa (hoặc giữa hai mạng với nhau) qua môi trường Internet công cộng không an toàn.

## 1. Thành phần và Yêu cầu hệ thống
Để một hệ thống VPN hoạt động, cần có các thành phần sau:
*   **VPN Client**: Phần mềm cài trên thiết bị từ xa để thiết lập và duy trì kết nối (ví dụ: OpenVPN, AnyConnect).
*   **VPN Server**: Thiết bị hoặc máy chủ tiếp nhận kết nối, xác thực người dùng và định tuyến lưu lượng vào mạng nội bộ.
*   **Mã hóa (Encryption)**: Sử dụng các thuật toán mạnh như **AES** để đảm bảo tính bảo mật.
*   **Xác thực (Authentication)**: Đảm bảo chỉ thực thể hợp lệ mới có thể truy cập (dùng mật khẩu, chứng chỉ số, hoặc khóa chia sẻ PSK).

## 2. Giao thức bảo mật IP (IPsec)
IPsec là bộ giao thức mạnh mẽ nhất được dùng trong VPN, hoạt động ở tầng Mạng.

### Các giao thức thành phần:
*   **AH (Authentication Header)**: Đảm bảo tính toàn vẹn và xác thực, nhưng **không mã hóa dữ liệu**.
*   **ESP (Encapsulating Security Payload)**: Mã hóa dữ liệu payload và có thể xác thực tùy chọn.
    *   Sử dụng cổng **UDP/4500** khi cần vượt qua các thiết bị NAT (NAT Traversal).
*   **IKE (Internet Key Exchange)**: Thỏa thuận và duy trì các khóa bảo mật qua cổng **UDP/500**.

### Chế độ hoạt động:
*   **Transport Mode**: Chỉ mã hóa payload, giữ nguyên IP Header gốc. Dùng cho giao tiếp Host-to-Host.
*   **Tunnel Mode**: Mã hóa **toàn bộ gói tin IP gốc**, bao gồm cả IP Header. Dùng để tạo đường hầm VPN giữa hai mạng (Site-to-Site).

## 3. Giao thức PPTP (Lỗi thời)
**Point-to-Point Tunneling Protocol (PPTP)** là một trong những giao thức VPN đời đầu (Cổng TCP/1723).
*   **Tình trạng**: Hiện nay được coi là **không an toàn**.
*   **Lỗ hổng**: 
    *   Cơ chế xác thực **MSCHAPv2** có điểm yếu nghiêm trọng.
    *   Sử dụng mã hóa **DES** lỗi thời, có thể bị bẻ khóa dễ dàng bằng phần cứng chuyên dụng.
*   **Thay thế**: Nên sử dụng L2TP/IPsec, OpenVPN hoặc IKEv2/IPsec để đảm bảo an toàn.

## 4. Lợi ích của VPN
1.  **Bảo mật**: Mã hóa dữ liệu giúp chống lại việc nghe lén trên mạng công cộng.
2.  **Truy cập từ xa**: Nhân viên có thể truy cập tài nguyên công ty (email, file server) từ bất cứ đâu.
3.  **Hợp nhất mạng**: Kết nối các chi nhánh văn phòng ở xa thành một mạng logic duy nhất.
4.  **Tiết kiệm chi phí**: Tận dụng hạ tầng Internet thay vì thuê đường truyền riêng đắt đỏ.

## Liên kết liên quan
- [[network-security|Bảo mật mạng]]
- [[internet-architecture|Kiến trúc Internet]]
- [[cryptography-basics|Mật mã học cơ bản]]
- [[key-exchange|Cơ chế trao đổi khóa]]
