---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Introduction - Intro.md"]
tags: ["security", "pentest", "assessment", "offensive-security"]
---

# Kiểm thử xâm nhập (Penetration Testing)

**Kiểm thử xâm nhập (Penetration Testing)** là một quá trình mô phỏng các cuộc tấn công mạng **được ủy quyền** nhằm vào mạng lưới, hệ thống hoặc ứng dụng của một tổ chức. Mục đích chính là xác định các lỗ hổng bảo mật tiềm ẩn và khắc phục chúng trước khi bị tội phạm mạng khai thác.

Kết quả của quá trình này thường được tổng hợp thành một bản báo cáo chi tiết, cung cấp thông tin cho các nhà phát triển phần mềm, đội ngũ bảo mật và quản trị viên về cách xử lý các vấn đề đã được phát hiện.

## Quy trình Kiểm thử xâm nhập (The Pentest Process)

Quy trình chuẩn thường bao gồm 8 giai đoạn chính:

1.  **[[my_knowlegde/concepts/pentest-pre-engagement|Tiền dự án (Pre-Engagement)]]**: Thảo luận, xác định phạm vi, ký kết các văn bản pháp lý và chuẩn bị quyền hạn cần thiết.
2.  **[[my_knowlegde/concepts/information-gathering|Thu thập thông tin (Information Gathering)]]**: Thu thập dữ liệu về mục tiêu để hiểu cấu trúc, chức năng và các nguồn lực kỹ thuật. Quá trình này bao gồm [[my_knowlegde/concepts/osint|OSINT]] và [[my_knowlegde/concepts/network-scanning|Quét mạng]].
3.  **[[my_knowlegde/concepts/vulnerability-assessment|Đánh giá lỗ hổng (Vulnerability Assessment)]]**: Phân tích thông tin đã thu thập để xác định các vector tấn công tiềm năng và các "low-hanging fruits".
4.  **[[exploitation|Khai thác (Exploitation)]]**: Tấn công trực tiếp vào các lỗ hổng và vượt qua các cơ chế phòng thủ (Ví dụ: [[my_knowlegde/concepts/linux-initial-access|Truy cập ban đầu trên Linux]], [[my_knowlegde/concepts/windows-initial-access|Truy cập ban đầu trên Windows]]).
5.  **[[post-exploitation|Sau khai thác (Post-Exploitation)]]**: Kiểm soát hệ thống từ bên trong, thu thập thông tin nội bộ và leo thang đặc quyền (Ví dụ: [[my_knowlegde/concepts/linux-system-enumeration|Liệt kê hệ thống]], [[my_knowlegde/concepts/linux-vulnerability-assessment|đánh giá lỗ hổng nội bộ]], [[my_knowlegde/concepts/linux-privilege-escalation|leo thang đặc quyền]] và [[my_knowlegde/concepts/linux-pillaging|vét cạn dữ liệu]] trên Linux; và các bước tương tự trên [[my_knowlegde/concepts/windows-system-enumeration|Windows]]).
6.  **[[lateral-movement|Di chuyển ngang (Lateral Movement)]]**: Sử dụng hệ thống đã chiếm được để di chuyển sâu hơn vào mạng nội bộ.
7.  **[[my_knowlegde/concepts/proof-of-concept|Bằng chứng khai thác (Proof-of-concept)]]**: Ghi lại các bước thực hiện kỹ thuật để khách hàng có thể tái hiện và xác nhận lỗ hổng.
8.  **[[post-engagement|Hậu dự án (Post-Engagement)]]**: Bao gồm việc lập [[my_knowlegde/concepts/pentest-documentation|báo cáo dự án]], [[my_knowlegde/concepts/pentest-reporting|trình bày kết quả]] và hỗ trợ khách hàng khắc phục lỗ hổng.

## Tại sao cần thực hiện Pentest?
*   **Chủ động phòng thủ**: Tìm và sửa lỗi trước khi bị tấn công thật.
*   **Tuân thủ quy định**: Đáp ứng các tiêu chuẩn bảo mật ngành (như PCI DSS).
*   **Đánh giá hiệu quả**: Kiểm tra xem các biện pháp bảo mật hiện có (tường lửa, IDS/IPS) có hoạt động như mong đợi hay không.
*   **Nâng cao nhận thức**: Giúp nhân viên và ban lãnh đạo hiểu rõ hơn về các rủi ro thực tế.

## Lời khuyên cho Pentester
Để trở thành một chuyên gia giỏi, bạn cần rèn luyện về tư duy, kỹ năng nghiên cứu và tuân thủ kỷ luật làm việc. Xem thêm tại: [[my_knowlegde/summaries/pentest-recommendations|Lời khuyên cho chuyên viên Kiểm thử xâm nhập]].

## Liên kết liên quan
- [[my_knowlegde/concepts/security-roles|Các vai trò trong an ninh mạng]] (Đặc biệt là [[my_knowlegde/concepts/security-roles|Penetration Tester]])
- [[my_knowlegde/concepts/cyber-threats|Các mối đe dọa mạng]]
- [[my_knowlegde/concepts/cybersecurity-teams|Các đội ngũ an ninh mạng]] (Đặc biệt là [[my_knowlegde/concepts/cybersecurity-teams|Red Team]])
- [[my_knowlegde/concepts/information-security|An ninh thông tin]]
