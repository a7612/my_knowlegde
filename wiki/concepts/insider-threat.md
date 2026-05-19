---
sources: ["raw/Hack The Box/Introduction to Information Security/Threats - Insider Threat.md"]
tags: ["security", "threats", "insider-threat"]
---

# Mối đe dọa từ nội bộ (Insider Threat)

**Mối đe dọa từ nội bộ** đề cập đến nguy cơ đến từ những cá nhân có quyền truy cập hợp lệ vào tài nguyên của một tổ chức, chẳng hạn như nhân viên, nhà thầu hoặc đối tác kinh doanh. Khác với những kẻ tấn công bên ngoài phải vượt qua các lớp phòng thủ, mối đe dọa nội bộ xuất phát từ chính bên trong tổ chức. Những cá nhân này lạm dụng đặc quyền truy cập của mình để gây hại cho tổ chức, dù là cố ý hay vô tình.

## Phân loại mối đe dọa nội bộ

Có ba loại chính:

1.  **Kẻ nội bộ có ý đồ xấu (Malicious Insiders)**: Những cá nhân cố tình gây hại. Họ có thể đánh cắp thông tin nhạy cảm, phá hoại hệ thống hoặc thực hiện gian lận vì lợi ích cá nhân, trả thù hoặc để mang lại lợi ích cho một tổ chức khác.
2.  **Kẻ nội bộ sơ suất (Negligent Insiders)**: Những cá nhân không có ý định gây hại nhưng lại làm vậy do bất cẩn hoặc thiếu hiểu biết. Ví dụ: gửi nhầm email chứa thông tin mật hoặc rơi vào bẫy [[social-engineering|tấn công kỹ thuật xã hội]].
3.  **Kẻ nội bộ bị xâm nhập (Compromised Insiders)**: Trường hợp kẻ tấn công bên ngoài chiếm được thông tin đăng nhập của một người trong tổ chức. Kẻ tấn công sau đó hoạt động bên trong hệ thống với tư cách là người dùng hợp lệ.

## Chuỗi tấn công nội bộ (Insider Threat Kill Chain)

Quá trình này thường diễn ra qua các giai đoạn:
1.  **Động lực (Motivation)**: Phát triển lý do để hành động chống lại tổ chức (bất mãn, tiền bạc, bị ép buộc).
2.  **Lập kế hoạch (Planning)**: Đánh giá đặc quyền truy cập và xác định các tài sản có giá trị.
3.  **Chuẩn bị (Preparation)**: Thu thập công cụ hoặc thông tin cần thiết.
4.  **Thực thi (Execution)**: Thực hiện hành vi độc hại (trộm dữ liệu, phá hoại).
5.  **Che giấu (Concealment)**: Xóa dấu vết để tránh bị phát hiện.

## Tác động và Hệ quả

*   **Tổn thất tài chính**: Trộm cắp tiền, chi phí ứng cứu sự cố, thiệt hại do gián đoạn hoạt động.
*   **Hư hại danh tiếng**: Làm xói mòn lòng tin của khách hàng và giảm giá trị thị trường.
*   **Hệ quả pháp lý**: Vi phạm các quy định như [[information-security|GDPR, HIPAA]] dẫn đến các khoản phạt nặng và kiện tụng.
*   **Văn hóa tổ chức**: Gây mất lòng tin lẫn nhau giữa các nhân viên.

## Liên kết liên quan
- [[cyber-threats|Các mối đe dọa mạng]]
- [[social-engineering|Tấn công kỹ thuật xã hội]]
- [[operational-security|An ninh vận hành]]
- [[risk-management|Quản lý rủi ro]]
