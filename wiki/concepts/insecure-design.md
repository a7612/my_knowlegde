---
sources: ["raw/OWASP/2025/OWASP Top Ten 2025 - A06 Insecure Design.md"]
tags: ["owasp", "secure-design", "threat-modeling", "sdlc", "architecture"]
---

# Thiết kế không an toàn (Insecure Design)

**Thiết kế không an toàn** (A06:2025) tập trung vào các rủi ro liên quan đến thiếu sót trong thiết kế và kiến trúc. Đây không phải là về việc thực thi mã nguồn sai (implementation), mà là về việc thiếu các biện pháp kiểm soát bảo mật cần thiết ngay từ giai đoạn lập kế hoạch.

## Phân biệt Thiết kế và Thực thi
*   **Thiết kế không an toàn**: Một thiết kế không bao giờ có thể an toàn dù được lập trình hoàn hảo (ví dụ: quy trình khôi phục mật khẩu dựa trên câu hỏi bí mật dễ đoán).
*   **Thực thi không an toàn**: Một thiết kế an toàn nhưng có lỗi trong mã nguồn (ví dụ: quy trình đổi mật khẩu an toàn nhưng bị lỗi SQL Injection).

## Các thành phần của Thiết kế An toàn
1.  **Vòng đời phát triển phần mềm an toàn (S-SDLC)**: Tích hợp bảo mật vào mọi giai đoạn từ yêu cầu đến vận hành.
2.  **Mô hình hóa mối đe dọa (Threat Modeling)**: Phân tích các luồng dữ liệu và xác định các điểm tấn công tiềm năng trước khi viết mã.
3.  **Thư viện thiết kế an toàn**: Sử dụng các mẫu thiết kế (design patterns) đã được kiểm chứng và các thành phần "paved road" (lối đi an toàn sẵn có).

## Cách phòng tránh
- Thiết lập và sử dụng S-SDLC với sự hỗ trợ của các chuyên gia AppSec.
- Sử dụng Threat Modeling cho các phần quan trọng như xác thực, kiểm soát truy cập và logic nghiệp vụ.
- Tích hợp ngôn ngữ bảo mật và các biện pháp kiểm soát vào User Stories.
- Viết các bài kiểm tra đơn vị (unit tests) và tích hợp để xác thực các luồng quan trọng có khả năng chống lại các mối đe dọa đã mô hình hóa.
- Phân đoạn hệ thống ở cả lớp ứng dụng và lớp mạng dựa trên nhu cầu bảo vệ.

## Kịch bản tấn công ví dụ
Một chuỗi rạp chiếu phim cho phép đặt chỗ nhóm với mức giảm giá, tối đa 15 người. Kẻ tấn công phân tích logic này và thực hiện hàng nghìn yêu cầu đặt chỗ 15 người cùng lúc trên toàn hệ thống, gây thiệt hại doanh thu khổng lồ do giữ chỗ ảo mà không cần đặt cọc. Đây là lỗi trong thiết kế logic nghiệp vụ.

## Liên kết liên quan
- [[application-security|An ninh ứng dụng]]
- [[owasp-top-ten-2025|OWASP Top Ten 2025]]
- [[risk-management|Quản lý rủi ro]]
