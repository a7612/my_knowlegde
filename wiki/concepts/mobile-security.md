---
sources: ["raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Mobile Security.md"]
tags: ["security", "mobile", "encryption", "biometrics", "vpn", "application-security"]
---

# An ninh di động (Mobile Security)

**An ninh di động** tập trung vào việc bảo vệ các thiết bị di động (smartphone, máy tính bảng), dữ liệu chúng lưu trữ và các mạng lưới mà chúng kết nối.

## Tầm quan trọng
Thiết bị di động ngày nay giống như một "rương kho báu" di động, chứa đựng thông tin cá nhân, tài chính, danh bạ và cả các dữ liệu công việc nhạy cảm. Vì chúng ta mang theo chúng khắp nơi, rủi ro bị mất cắp vật lý hoặc bị tấn công qua mạng không dây là rất lớn.

## Các lớp bảo vệ di động

| Lớp bảo vệ | Biện pháp chính |
| --- | --- |
| **An ninh thiết bị** | Mật khẩu (Passcode), xác thực sinh trắc học (vân tay, khuôn mặt), khả năng xóa dữ liệu từ xa (Remote Wipe). |
| **An ninh dữ liệu** | **Mã hóa** dữ liệu để kẻ trộm không đọc được, sao lưu an toàn (Secure Backup), chiến lược chống thất thoát dữ liệu (DLP). |
| **An ninh mạng** | Sử dụng **VPN** khi dùng Wi-Fi công cộng, các giao thức truyền tải bảo mật (HTTPS). |
| **An ninh ứng dụng** | Kiểm duyệt ứng dụng (Vetting), quản lý quyền hạn (Permission management), quy trình phát triển ứng dụng an toàn. |

## Phép ẩn dụ: Rương kho báu di động
* **Ổ khóa rương**: Chính là **An ninh thiết bị** (mật khẩu, vân tay).
* **Két sắt bên trong rương**: Chính là **An ninh dữ liệu** (mã hóa). Dù ai đó mở được rương, họ vẫn không mở được két sắt bên trong.
* **Đường vận chuyển an toàn**: Khi mang rương đi trên đường (mạng internet), bạn cần đi qua các đường hầm riêng biệt (**VPN**) để tránh bị cướp.
* **Công cụ trong rương**: Các ứng dụng bạn cài vào rương phải được kiểm tra kỹ lưỡng (**An ninh ứng dụng**) để đảm bảo chúng không phải là công cụ giả mạo nhằm đánh cắp kho báu.

## Trách nhiệm trong tổ chức
Bảo vệ thiết bị di động là nỗ lực chung của nhiều vai trò:
* **Bộ phận IT**: Triển khai các giải pháp như MDM (Mobile Device Management) để quản lý thiết bị và mã hóa.
* **Giám đốc An ninh thông tin (CISO)**: Phát triển chiến lược tổng thể và đảm bảo tuân thủ các quy định pháp lý.
* **Đội ngũ an ninh**: Thực hiện kiểm thử xâm nhập để tìm lỗ hổng trên ứng dụng và thiết bị di động.
* **Người dùng**: Có trách nhiệm cập nhật phần mềm thường xuyên và không cài đặt các ứng dụng không rõ nguồn gốc.

## Liên kết liên quan
- [[information-security|An ninh thông tin]]
- [[network-security|An ninh mạng]]
- [[application-security|An ninh ứng dụng]]
- [[encryption-basics|Cơ bản về mã hóa]]
