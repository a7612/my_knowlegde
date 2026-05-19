---
sources: ["raw/Hack The Box/Introduction to Information Security/Introduction - Principles of Information Security.md", "raw/Hack The Box/Introduction to Information Security/Introduction - Structure of InfoSec.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Network Security.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Application Security.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Operational Security.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Disaster Recovery and Business Continuity.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Cloud Security.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Physical Security.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Mobile Security.md", "raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Internet of Things Security.md", "raw/NIST/NIST.CSWP.29.pdf"]
tags: ["security", "infosec", "cybersecurity", "fundamentals"]
---

# An ninh thông tin (Information Security)

**An ninh thông tin (InfoSec)** là lĩnh vực tập trung vào việc bảo vệ thông tin và các hệ thống thông tin khỏi việc truy cập, sử dụng, tiết lộ, gián đoạn, sửa đổi hoặc phá hoại trái phép. Mục tiêu cốt lõi là duy trì bộ ba **CIA**: Tính bảo mật (Confidentiality), Tính toàn vẹn (Integrity) và Tính sẵn sàng (Availability) của dữ liệu.

## Tầm quan trọng của An ninh thông tin
Trong thời đại chuyển đổi số, dữ liệu trở thành tài sản vô cùng quý giá, tương tự như kho báu trong một tòa lâu đài. Việc bảo vệ an ninh thông tin giúp:
* **Bảo vệ dữ liệu nhạy cảm**: Ngăn chặn rò rỉ thông tin cá nhân, tài chính và bí mật thương mại.
* **Đảm bảo tính liên tục của kinh doanh**: Duy trì hoạt động của các hệ thống quan trọng ngay cả khi gặp sự cố.
* **Tuân thủ quy định**: Đáp ứng các tiêu chuẩn pháp lý (như GDPR, HIPAA) và ngành về bảo vệ dữ liệu.
* **Bảo vệ uy tín thương hiệu**: Duy trì lòng tin của khách hàng và đối tác sau các sự cố an ninh.
* **Bảo vệ sở hữu trí tuệ**: Ngăn chặn mất mát lợi thế cạnh tranh do mất cắp ý tưởng, phát minh.
* **Thúc đẩy chuyển đổi số an toàn**: Cho phép tổ chức áp dụng công nghệ mới một cách tự tin.

## Các lĩnh vực của An ninh thông tin (InfoSec Domains)
InfoSec là một lĩnh vực rộng lớn với nhiều chuyên môn đặc thù:
1. [[network-security|An ninh mạng (Network Security)]]: Bảo vệ hạ tầng mạng và dữ liệu đang truyền tải bằng tường lửa, VPN, IDS/IPS.
2. [[application-security|An ninh ứng dụng (Application Security)]]: Bảo vệ phần mềm suốt vòng đời phát triển (SDLC), chống lại các lỗ hổng như SQL Injection, XSS.
3. [[operational-security|An ninh vận hành (Operational Security - OpSec)]]: Quản lý các quy trình bảo mật hàng ngày, kiểm soát truy cập và quản lý tài sản.
4. [[disaster-recovery|Khôi phục sau thảm họa (Disaster Recovery)]] và [[business-continuity|Liên tục kinh doanh (Business Continuity)]]: Kế hoạch phục hồi hệ thống và duy trì hoạt động sau sự cố lớn.
5. [[cloud-security|An ninh đám mây (Cloud Security)]]: Bảo vệ dữ liệu và ứng dụng trên các nền tảng đám mây theo mô hình trách nhiệm chia sẻ.
6. [[physical-security|An ninh vật lý (Physical Security)]]: Bảo vệ phần cứng, trung tâm dữ liệu và cơ sở hạ tầng khỏi sự truy cập vật lý trái phép.
7. [[mobile-security|An ninh di động (Mobile Security)]]: Bảo vệ thiết bị di động, ứng dụng và mạng mà chúng kết nối.
8. [[iot-security|An ninh Internet vạn vật (IoT Security)]]: Bảo vệ mạng lưới các thiết bị thông minh kết nối internet.

## Các khung quản lý an ninh (Security Frameworks)
Để quản trị an ninh một cách hệ thống, các tổ chức thường áp dụng các khung tiêu chuẩn toàn cầu:
*   **[[nist-csf|Khung An ninh mạng NIST (CSF) 2.0]]**: Cung cấp cấu trúc 6 chức năng (Quản trị, Xác định, Bảo vệ, Phát hiện, Phản ứng, Khôi phục) để quản lý rủi ro hiệu quả.
*   **ISO/IEC 27001**: Tiêu chuẩn quốc tế về Hệ thống Quản lý An toàn Thông tin (ISMS).
*   **CIS Controls**: Danh sách các hành động phòng thủ ưu tiên để ngăn chặn các cuộc tấn công mạng phổ biến.

## Các quy trình chính trong InfoSec
Một chiến lược an ninh mạnh mẽ dựa trên các quy trình cốt lõi sau:
1. [[risk-assessment|Đánh giá rủi ro (Risk Assessment)]]: Xác định và đánh giá các mối đe dọa (threats) và lỗ hổng (vulnerabilities).
2. **Lập kế hoạch an ninh (Security Planning)**: Phát triển chiến lược, chính sách và phân bổ nguồn lực.
3. **Triển khai kiểm soát an ninh (Implementation)**: Thực thi các giải pháp kỹ thuật (tường lửa, mã hóa) và chính sách.
4. **Giám sát và Phát hiện (Monitoring & Detection)**: Theo dõi liên tục các sự kiện thông qua các hệ thống như SIEM.
5. [[incident-response|Ứng cứu sự cố (Incident Response)]]: Phản ứng nhanh chóng để cô lập và giảm thiểu thiệt hại khi có sự cố.
6. [[disaster-recovery|Khôi phục sau thảm họa (Disaster Recovery)]]: Khôi phục hệ thống và dữ liệu về trạng thái hoạt động bình thường.
7. **Cải tiến liên tục (Continuous Improvement)**: Học hỏi từ các sự cố, thực hiện kiểm toán và cập nhật biện pháp bảo mật.

## Liên kết liên quan
- [[security-principles|Các nguyên tắc an ninh thông tin]]
- [[risk-management|Quản lý rủi ro]]
- [[cybersecurity-teams|Các đội ngũ an ninh mạng]]
- [[security-roles|Các vai trò trong an ninh thông tin]]
