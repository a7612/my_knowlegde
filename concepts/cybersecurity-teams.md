---
sources: ["raw/Hack The Box/Introduction to Information Security/Introduction - Structure of InfoSec.md", "raw/Hack The Box/Introduction to Information Security/Cybersecurity Teams - Red Team.md", "raw/Hack The Box/Introduction to Information Security/Cybersecurity Teams - Blue Team.md", "raw/Hack The Box/Introduction to Information Security/Cybersecurity Teams - Purple Team.md"]
tags: ["security", "teams", "blue-team", "red-team", "purple-team", "soc"]
---

# Các đội ngũ an ninh mạng (Cybersecurity Teams)

Trong một tổ chức, an ninh mạng được duy trì thông qua sự phối hợp của các đội ngũ chuyên biệt. Mỗi đội có vai trò và trách nhiệm riêng, cùng nhau tạo nên một hệ thống phòng thủ vững chắc.

## 1. Đội Xanh (Blue Team) - Hệ thống miễn dịch của tổ chức

**Blue Team** đóng vai trò là tuyến phòng thủ đầu tiên, tập trung vào việc bảo vệ cơ sở hạ tầng kỹ thuật số của tổ chức.

### Các vai trò chính:
*   **Chuyên viên phân tích bảo mật (Security Analysts)**: Giám sát mạng và hệ thống 24/7 để phát hiện các dấu hiệu bất thường.
*   **Chuyên viên ứng cứu sự cố (Incident Responders)**: Hành động ngay khi có vi phạm xảy ra để ngăn chặn và giảm thiểu thiệt hại.
*   **Chuyên gia săn tìm mối đe dọa (Threat Hunters)**: Chủ động tìm kiếm các mối đe dọa tiềm ẩn hoặc lỗ hổng chưa bị khai thác.
*   **Kỹ sư bảo mật (Security Engineers)**: Thiết kế và duy trì các biện pháp bảo mật như tường lửa, IDS/IPS.

### Mục tiêu:
*   Phòng ngừa và giám sát liên tục (thông qua [[my_knowlegde/concepts/dns-service|SIEM]], [[my_knowlegde/concepts/distributed-denial-of-service|IDS]], EDR).
*   Triển khai các biện pháp kiểm soát an ninh (Access Control, Patch Management, Encryption).
*   Ứng cứu và khôi phục sau sự cố.

Trung tâm điều hành an ninh (**SOC - Security Operations Center**) là trung tâm chỉ huy của Blue Team, hoạt động 24/7 để đảm bảo sự cảnh giác không ngừng.

## 2. Đội Đỏ (Red Team) - Những "kẻ tấn công" có đạo đức

**Red Team** mô phỏng các cuộc tấn công thực tế để kiểm tra toàn diện khả năng phòng thủ của tổ chức, bao gồm cả yếu tố công nghệ, con người và vật lý.

### Cách thức hoạt động:
*   **Tiếp cận toàn diện**: Không chỉ tìm lỗi kỹ thuật mà còn sử dụng [[my_knowlegde/concepts/social-engineering|tấn công kỹ thuật xã hội]] và kiểm tra an ninh vật lý.
*   **Hoạt động bí mật**: Hầu hết nhân viên trong tổ chức không biết về cuộc thử nghiệm để đảm bảo phản ứng quan sát được là thực tế nhất.
*   **Dài hạn**: Các chiến dịch có thể kéo dài hàng tuần hoặc hàng tháng, bắt đầu từ việc thu thập thông tin tình báo (OSINT).

### Mục tiêu:
*   Xác định các điểm yếu mà các cuộc kiểm tra thông thường bỏ sót.
*   Đánh giá khả năng phát hiện và phản ứng của Blue Team.
*   Nâng cao nhận thức bảo mật của nhân viên.

## 3. Đội Tím (Purple Team) - Sự cộng tác chiến lược

**Purple Teaming** không phải là một đội ngũ cố định, mà là một phương pháp tiếp cận trong đó Đội Xanh và Đội Đỏ cùng hợp tác để tối ưu hóa khả năng bảo mật.

### Lợi ích của sự hợp tác:
*   **Chia sẻ kiến thức**: Đội Đỏ giải thích cách họ xâm nhập, Đội Xanh chia sẻ cách họ phát hiện.
*   **Cải thiện liên tục**: Giúp Đội Xanh phát triển các chiến lược phòng thủ mạnh hơn và Đội Đỏ tinh chỉnh các kịch bản tấn công thực tế hơn.
*   **Ứng cứu sự cố hiệu quả hơn**: Do thường xuyên diễn tập cùng nhau, sự phối hợp khi có sự cố thật sẽ nhanh chóng và nhịp nhàng hơn.

## Liên kết liên quan
- [[my_knowlegde/concepts/information-security|An ninh thông tin]]
- [[my_knowlegde/concepts/threat-actors|Các tác nhân đe dọa]]
- [[my_knowlegde/concepts/security-roles|Các vai trò trong an ninh thông tin]]
- [[my_knowlegde/concepts/network-security|An ninh mạng]]
- [[my_knowlegde/concepts/social-engineering|Tấn công kỹ thuật xã hội]]
