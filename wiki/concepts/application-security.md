---
sources: ["raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Application Security.md"]
tags: ["security", "application", "sdlc", "secure-coding", "penetration-testing"]
---

# An ninh ứng dụng (Application Security)

**An ninh ứng dụng** là một thành phần trọng yếu của [[information-security|An ninh thông tin]], tập trung vào việc bảo vệ các ứng dụng phần mềm khỏi các mối đe dọa bên ngoài trong suốt toàn bộ vòng đời của chúng (từ lúc phát triển đến khi triển khai và bảo trì).

## Mục tiêu cốt lõi
Đảm bảo các ứng dụng được phát triển và vận hành theo cách duy trì bộ ba **CIA**:
* **Bảo mật (Confidentiality)**: Bảo vệ dữ liệu nhạy cảm mà ứng dụng xử lý.
* **Toàn vẹn (Integrity)**: Ngăn chặn việc sửa đổi mã nguồn hoặc dữ liệu trái phép.
* **Sẵn sàng (Availability)**: Đảm bảo ứng dụng luôn hoạt động ổn định cho người dùng.

## Phép ẩn dụ: Xây dựng một ngôi nhà an toàn
Để hiểu về an ninh ứng dụng, hãy tưởng tượng bạn đang xây một ngôi nhà:
1. **Xây dựng (Phát triển ứng dụng)**:
    * **Khóa cửa và cửa sổ**: Thiết lập cơ chế **Xác thực** (Authentication) an toàn.
    * **Tường vững chắc**: Viết mã nguồn (Secure Code) không có kẽ hở để tránh bị sụp đổ (tấn công).
    * **Mái nhà chống thấm**: **Mã hóa** dữ liệu để ngăn chặn rò rỉ thông tin (nước mưa).
2. **Kiểm tra (Kiểm thử lỗ hổng)**:
    * **Thử bẻ khóa**: Thực hiện **Kiểm thử xâm nhập** (Penetration Testing) để xem kẻ trộm có thể đột nhập không.
    * **Tìm vết nứt**: Kiểm tra mã nguồn để phát hiện lỗi (bug) hoặc điểm yếu.
3. **Bảo trì (Giám sát liên tục)**:
    * **Lắp camera**: Giám sát ứng dụng để phát hiện hoạt động bất thường.
    * **Vá tường và thay khóa**: Thường xuyên cập nhật và vá lỗi (patch) để đối phó with các mối đe dọa mới.

## Các khái niệm quan trọng

### Bảo mật ngay từ khâu thiết kế (Security by Design)
Security by Design có nghĩa là bảo mật không phải là thứ được thêm vào sau khi ứng dụng đã hoàn thành, mà được tích hợp ngay từ giai đoạn lập kế hoạch.
*   **Mô hình hóa mối đe dọa (Threat Modeling)**: Hình dung mọi cách kẻ xấu có thể tấn công ứng dụng. Xem thêm: [[insecure-design|Thiết kế không an toàn]].
*   **Đánh giá mã nguồn an toàn (Secure Code Reviews)**: Kiểm tra kỹ lưỡng mã nguồn để đảm bảo không có lỗ hổng như SQL Injection, Cross-Site Scripting (XSS), [[os-command-injection|OS Command Injection]] hay [[use-after-free|Use After Free]].

## Các tiêu chuẩn và Khung bảo mật
Để hỗ trợ việc bảo mật ứng dụng, có nhiều tiêu chuẩn và khung (framework) được công nhận rộng rãi:
*   **[[owasp-top-ten-2025|OWASP Top Ten 2025]]**: Danh sách 10 rủi ro bảo mật ứng dụng web quan trọng nhất, cung cấp cái nhìn tổng quan về các mối đe dọa phổ biến nhất hiện nay.
*   **ASVS (Application Security Verification Standard)**: Một khung tiêu chuẩn để kiểm thử các biện pháp kiểm soát an ninh ứng dụng kỹ thuật.
*   **SAMM (Software Assurance Maturity Model)**: Mô hình giúp tổ chức đánh giá và cải thiện vòng đời phát triển phần mềm an toàn.

## Trách nhiệm trong An ninh ứng dụng
* **Lập trình viên (Developers)**: Tuyến đầu trong việc viết mã an toàn và triển khai các tính năng bảo mật.
* **Kiến trúc sư bảo mật (Security Architects)**: Thiết kế cấu trúc bảo mật tổng thể cho ứng dụng.
* **Đội ngũ vận hành IT**: Duy trì môi trường sản xuất an toàn.
* **Chuyên gia kiểm thử bảo mật (Penetration Testers)**: Sử dụng các công cụ phân tích tĩnh/động để tìm và khai thác lỗ hổng một cách có đạo đức.

## Thách thức
Một trong những thách thức lớn nhất là sự cân bằng giữa **tính bảo mật** và **tốc độ ra mắt thị trường**. Việc vội vàng phát hành ứng dụng có thể dẫn đến việc bỏ qua các bước kiểm tra an ninh, để lại những lỗ hổng nguy hiểm.

## Liên kết liên quan
- [[information-security|An ninh thông tin]]
- [[network-security|An ninh mạng]]
- [[linux-web-services|Dịch vụ web trên Linux]]
- [[os-command-injection|Lỗ hổng Tiêm lệnh hệ điều hành (CWE-78)]]
- [[use-after-free|Lỗ hổng Sử dụng sau khi Giải phóng (CWE-416)]]
