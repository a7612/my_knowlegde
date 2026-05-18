---
sources: ["raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Internet of Things Security.md"]
tags: ["security", "iot", "network-segmentation", "embedded-systems"]
---

# An ninh Internet vạn vật (IoT Security)

**An ninh Internet vạn vật (IoT Security)** là việc bảo vệ mạng lưới các vật dụng hàng ngày được kết nối internet (như máy điều hòa thông minh, đồng hồ theo dõi sức khỏe, xe kết nối, cảm biến công nghiệp) khỏi các truy cập trái phép và tấn công mạng.

## Thách thức của An ninh IoT
Khác với máy tính truyền thống, các thiết bị IoT thường có:
* **Năng lượng xử lý và bộ nhớ hạn chế**: Khó cài đặt các phần mềm bảo mật phức tạp.
* **Số lượng triển khai lớn**: Khó quản lý và cập nhật đồng bộ cho hàng ngàn thiết bị.
* **Môi trường đa dạng**: Có thể nằm ở những nơi dễ bị tiếp cận vật lý hoặc điều kiện khắc nghiệt.

## Phép ẩn dụ: Những cánh cửa kỹ thuật số vô hình
Hãy tưởng tượng ngôi nhà của bạn đầy các thiết bị thông minh: đèn tự bật, khóa cửa điều khiển qua điện thoại, tủ lạnh thông minh. Những thiết bị này mang lại sự tiện lợi, nhưng chúng cũng tạo ra những "cánh cửa vô hình" để kẻ trộm đột nhập vào mạng nội bộ của bạn. Một chiếc máy điều hòa thông minh bị hack có thể là bàn đạp để tin tặc truy cập vào máy tính cá nhân chứa các tệp quan trọng.

## Trách nhiệm chia sẻ (Shared Responsibility)
Việc bảo mật hệ sinh thái IoT là trách nhiệm của nhiều bên:

| Bên liên quan | Trách nhiệm |
| --- | --- |
| **Nhà sản xuất thiết bị** | Thiết kế bảo mật ngay từ đầu, giảm thiểu các tính năng không cần thiết và cung cấp các bản cập nhật vá lỗi kịp thời. |
| **Quản trị viên mạng** | Bảo mật hạ tầng kết nối, thực hiện **phân đoạn mạng (network segmentation)** để cô lập các thiết bị IoT nếu chúng bị xâm nhập. |
| **Lập trình viên ứng dụng** | Đảm bảo phần mềm tương tác với thiết bị IoT có phương thức xác thực mạnh và mã hóa dữ liệu. |

## Một ví dụ thực tế
Một chuỗi bán lẻ lớn đã lắp đặt hệ thống điều hòa thông minh (HVAC) trên toàn bộ các cửa hàng để tiết kiệm năng lượng. Do hệ thống này thiếu các biện pháp bảo mật cơ bản, tin tặc đã khai thác lỗ hổng để xâm nhập vào mạng lưới của công ty và đánh cắp thông tin thẻ tín dụng của hàng triệu khách hàng.

## Các biện pháp bảo vệ
1. **Phân đoạn mạng**: Đặt các thiết bị IoT vào một mạng riêng biệt, cách ly với các máy chủ chứa dữ liệu quan trọng.
2. **Thay đổi mật khẩu mặc định**: Luôn đổi mật khẩu ngay khi lắp đặt thiết bị mới.
3. **Cập nhật Firmware**: Thường xuyên kiểm tra và cài đặt các bản vá lỗi từ nhà sản xuất.
4. **Tắt các dịch vụ không cần thiết**: Giảm thiểu diện tích tấn công (attack surface).

## Liên kết liên quan
- [[information-security|An ninh thông tin]]
- [[network-security|An ninh mạng]]
- [[cloud-security|An ninh đám mây]]
