---
sources: ["raw/Hack The Box/Introduction to Information Security/Threats - Ransomware.md"]
tags: ["security", "threats", "malware", "ransomware"]
---

# Mã độc tống tiền (Ransomware)

**Ransomware** là một loại phần mềm độc hại (malware) xâm nhập vào máy tính, máy chủ và mạng lưới, thực hiện mã hóa các tệp tin quan trọng khiến chúng không thể truy cập được. Kẻ tấn công sau đó yêu cầu một khoản tiền chuộc (ransom), thường bằng tiền điện tử như Bitcoin, để đổi lấy khóa giải mã nhằm khôi phục dữ liệu. Đây giống như một vụ bắt cóc kỹ thuật số, nơi các tệp tin quan trọng của bạn bị giữ làm con tin.

## Cách thức hoạt động

Một cuộc tấn công Ransomware thường diễn ra qua các giai đoạn:
1.  **Xâm nhập**: Kẻ tấn công thường sử dụng [[my_knowlegde/concepts/social-engineering|Phishing]] (email lừa đảo) chứa liên kết hoặc tệp đính kèm độc hại.
2.  **Mã hóa**: Sau khi được cài đặt, ransomware sử dụng các thuật toán phức tạp để mã hóa tài liệu, ảnh, cơ sở dữ liệu, v.v.
3.  **Tống tiền**: Một thông điệp hiện ra thông báo về tình trạng bị mã hóa và hướng dẫn cách trả tiền chuộc để nhận khóa giải mã.

## Ví dụ điển hình: WannaCry (2017)
Vào tháng 5 năm 2017, cuộc tấn công **WannaCry** đã lan rộng toàn cầu, ảnh hưởng đến hơn 200.000 máy tính tại hơn 150 quốc gia. Các bệnh viện thuộc Dịch vụ Y tế Quốc gia (NHS) của Anh bị ảnh hưởng nặng nề, dẫn đến việc hủy bỏ các ca phẫu thuật và chuyển hướng xe cứu thương. WannaCry khai thác một lỗ hổng trên Windows của các máy tính chưa được cập nhật bản vá bảo mật.

## Tác động
*   **Ngừng trệ hoạt động**: Các doanh nghiệp và dịch vụ công cộng bị đình trệ hoàn toàn.
*   **Tổn thất tài chính**: Bao gồm tiền chuộc, chi phí khôi phục hệ thống và thiệt hại do ngừng hoạt động.
*   **Mất dữ liệu vĩnh viễn**: Không có gì đảm bảo kẻ tấn công sẽ cung cấp khóa giải mã sau khi nhận tiền.
*   **Nguy hiểm đến tính mạng**: Trong lĩnh vực y tế, việc không thể truy cập hồ sơ bệnh nhân có thể đe dọa trực tiếp đến tính mạng.
*   **Hư hại danh tiếng**: Làm xói mòn lòng tin của khách hàng đối với khả năng bảo mật của tổ chức.

## Lưu ý quan trọng
Việc trả tiền chuộc không được khuyến khích vì nó khuyến khích tội phạm mạng tiếp tục hoạt động và khiến tổ chức trở thành mục tiêu cho các cuộc tấn công trong tương lai.

## Liên kết liên quan
- [[my_knowlegde/concepts/cyber-threats|Các mối đe dọa mạng]]
- [[my_knowlegde/concepts/social-engineering|Tấn công kỹ thuật xã hội]]
- [[my_knowlegde/concepts/linux-backup-restore|Sao lưu và khôi phục]]
- [[my_knowlegde/concepts/information-security|An ninh thông tin]]
