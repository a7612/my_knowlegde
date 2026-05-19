---
sources: ["raw/Hack The Box/Introduction to Information Security/Threats - Advanced Persistent Threats.md"]
tags: ["security", "threats", "apt", "cyber-espionage"]
---

# Mối đe dọa thường trực nâng cao (Advanced Persistent Threat - APT)

**Advanced Persistent Threat (APT)** là một cuộc tấn công mạng tinh vi và liên tục, trong đó kẻ xâm nhập giành được quyền truy cập trái phép vào mạng của một tổ chức và duy trì sự hiện diện mà không bị phát hiện trong một thời gian dài. Không giống như các cuộc tấn công thông thường nhằm mục tiêu kiếm lời nhanh chóng, APT là các chiến dịch dài hạn, đòi hỏi nguồn lực lớn và lập kế hoạch tỉ mỉ, thường được thực hiện bởi các nhóm có sự hậu thuẫn của quốc gia hoặc các tổ chức tội phạm có tổ chức.

## Đặc điểm chính
*   **Nâng cao (Advanced)**: Sử dụng các kỹ thuật tấn công phức tạp, mã độc tùy chỉnh và các lỗ hổng chưa được công bố (Zero-day).
*   **Thường trực (Persistent)**: Mục tiêu là duy trì quyền truy cập lâu dài thay vì tấn công rồi rút lui ngay.
*   **Mối đe dọa (Threat)**: Được thực hiện bởi các thực thể có khả năng và ý đồ gây hại cao.

## Các giai đoạn của một cuộc tấn công APT
1.  **Thăm dò (Reconnaissance)**: Thu thập thông tin chi tiết về mục tiêu (cấu trúc mạng, nhân viên, bảo mật).
2.  **Xâm nhập ban đầu (Initial Infiltration)**: Thường thông qua [[social-engineering|Spear-phishing]] hoặc khai thác lỗ hổng phần mềm.
3.  **Thiết lập chỗ đứng (Establish Foothold)**: Cài đặt mã độc và tạo cửa sau (backdoors).
4.  **Di chuyển ngang (Lateral Movement)**: Leo thang đặc quyền và xâm nhập thêm vào các hệ thống khác trong mạng.
5.  **Trích xuất dữ liệu (Data Exfiltration)**: Lén lút chuyển thông tin giá trị ra bên ngoài.
6.  **Duy trì sự hiện diện (Persistence)**: Đảm bảo có thể quay lại hệ thống ngay cả khi một số thành phần bị phát hiện.

## Ví dụ điển hình: Cuộc tấn công SolarWinds (2020)
Kẻ tấn công đã xâm nhập vào quy trình cập nhật phần mềm của SolarWinds để chèn mã độc vào các bản cập nhật hợp lệ. Điều này cho phép chúng gián điệp hàng ngàn tổ chức, bao gồm các cơ quan chính phủ Hoa Kỳ và các công ty Fortune 500, mà không bị phát hiện trong nhiều tháng.

## Tác động
*   **Mất mát tài sản trí tuệ**: Đánh cắp bí mật thương mại, nghiên cứu và công nghệ độc quyền.
*   **An ninh quốc gia**: Xâm nhập vào các tài liệu mật và báo cáo tình báo.
*   **Phá hoại hạ tầng**: Có khả năng gây gián đoạn lưới điện, mạng viễn thông hoặc hệ thống tài chính.
*   **Hệ quả kinh tế**: Gây thiệt hại tài chính khổng lồ và làm xói mòn lợi thế cạnh tranh của doanh nghiệp.

## Liên kết liên quan
- [[cyber-threats|Các mối đe dọa mạng]]
- [[information-security|An ninh thông tin]]
- [[social-engineering|Tấn công kỹ thuật xã hội]]
- [[network-security|An ninh mạng]]
