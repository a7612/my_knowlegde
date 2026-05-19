---
sources: ["raw/Hack The Box/Network Foundations/Network Security and Data Flow Analysis - Network Security.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Network Security.md"]
tags: ["networking", "security", "cia-triad", "ids", "ips", "firewall", "vpn"]
---

# Bảo mật mạng (Network Security)

**Bảo mật mạng** là một thành phần quan trọng của [[my_knowlegde/concepts/information-security|An ninh thông tin]], tập trung vào việc bảo vệ hạ tầng mạng và dữ liệu truyền tải bên trong nó. Hãy tưởng tượng bảo mật mạng giống như hệ thống an ninh của một ngôi nhà: tường lửa là cửa ra vào, IDS/IPS là camera giám sát và báo động, còn VPN là một đường hầm riêng biệt và an toàn để bạn đi vào nhà.

## Các yếu tố cốt lõi của Bảo mật mạng

| Yếu tố | Mô tả |
| --- | --- |
| **[[firewall|Tường lửa (Firewall)]]** | Đóng vai trò là rào cản giữa mạng nội bộ tin cậy và mạng bên ngoài không tin cậy, lọc lưu lượng dựa trên các quy tắc bảo mật. |
| **[[ids|IDS]] / [[ips|IPS]]** | Giám sát lưu lượng mạng để phát hiện các hoạt động đáng ngờ và thực hiện hành động tự động để chặn các mối đe dọa. |
| **[[vpn-technology|Mạng riêng ảo (VPN)]]** | Cung cấp các kết nối an toàn, mã hóa qua mạng công cộng, đảm bảo tính riêng tư và toàn vẹn của dữ liệu khi truyền tải. |
| **Cơ chế kiểm soát truy cập** | Bao gồm các giao thức [[authentication-protocols|Xác thực]] và Ủy quyền để đảm bảo chỉ người dùng hợp lệ mới có thể truy cập tài nguyên mạng. |
| **Công nghệ mã hóa** | Bảo vệ dữ liệu nhạy cảm cả khi đang truyền tải (in transit) và khi đang lưu trữ (at rest), khiến nó không thể đọc được đối với các bên không được ủy quyền. |

## Phép ẩn dụ: Người đưa thư tận tụy
Để dễ hình dung, hãy xem bảo mật mạng như một người đưa thư có trách nhiệm:
* **Đồng phục và thẻ tên**: Đại diện cho cơ chế **xác thực**, đảm bảo chỉ người có thẩm quyền mới được xử lý thư.
* **Túi thư có khóa**: Đóng vai trò như một **tường lửa**, ngăn cách thư tin cậy với các mối đe dọa bên ngoài.
* **Sự cảnh giác của người đưa thư**: Giống như **IDS/IPS**, luôn tìm kiếm các gói hàng khả nghi.
* **Dịch vụ chuyển phát bảo mật**: Tương đương với **VPN**, cung cấp thêm lớp bảo vệ cho các tài liệu tối mật.
* **Niêm phong chống giả mạo**: Đại diện cho **công nghệ mã hóa**, đảm bảo nội dung bên trong không bị đọc trộm.

## Hệ thống Phát hiện và Ngăn chặn Xâm nhập (IDS/IPS)
IDS/IPS là các giải pháp giám sát và phản ứng với các hoạt động đáng ngờ trên mạng.

| Loại | Chức năng | Hành động |
| --- | --- | --- |
| **[[ids|IDS]] (Intrusion Detection System)** | Giám sát lưu lượng để xác định hành vi độc hại. | Tạo cảnh báo, không chặn lưu lượng. |
| **[[ips|IPS]] (Intrusion Prevention System)** | Giám sát và ngăn chặn lưu lượng độc hại. | Chặn hoặc từ chối lưu lượng trong thời gian thực. |

### Kỹ thuật phát hiện
* **Phát hiện dựa trên chữ ký (Signature-based)**: So khớp lưu lượng với cơ sở dữ liệu về các cuộc tấn công đã biết.
* **Phát hiện dựa trên bất thường (Anomaly-based)**: Phát hiện bất kỳ điều gì khác thường so với hoạt động bình thường.

## Trách nhiệm trong Bảo mật mạng
* **Đội ngũ Quản trị mạng/An ninh**: Thiết kế, triển khai và bảo trì hạ tầng bảo mật mạng.
* **Kiểm thử xâm nhập (Penetration Testers)**: Mô phỏng các cuộc tấn công thực tế để tìm ra lỗ hổng trong các biện pháp bảo vệ hiện có.
* **Giám đốc An ninh thông tin (CISO)**: Thiết lập chiến lược tổng thể và đảm bảo bảo mật mạng phù hợp với mục tiêu kinh doanh.

## Các biện pháp thực hành tốt nhất (Best Practices)
1. **Chính sách Quyền hạn tối thiểu ([[least-privilege|Least Privilege]])**: Chỉ cho phép những truy cập thực sự cần thiết.
2. **Bảo mật đa lớp ([[defense-in-depth|Defense in Depth]])**: Kết hợp nhiều lớp phòng thủ (Tường lửa, VPN, IDS/IPS, v.v.).
3. **Giám sát liên tục**: Theo dõi nhật ký hệ thống để phát hiện sớm các dấu hiệu bất thường.
4. **Cập nhật và Vá lỗi thường xuyên**: Đảm bảo tất cả thiết bị mạng và phần mềm bảo mật luôn ở phiên bản mới nhất.
