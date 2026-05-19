---
sources: ["raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Physical Security.md"]
tags: ["security", "physical-security", "defense-in-depth", "hardware", "facility"]
---

# An ninh vật lý (Physical Security)

**An ninh vật lý** là việc bảo vệ các thiết bị phần cứng, cơ sở hạ tầng và dữ liệu thực tế khỏi sự truy cập, lấy cắp hoặc phá hoại trực tiếp.

## Tầm quan trọng
Dù các biện pháp bảo mật phần mềm có tinh vi đến đâu, chúng sẽ trở nên vô nghĩa nếu kẻ tấn công có thể tiếp cận trực tiếp vào máy chủ hoặc thiết bị lưu trữ. An ninh vật lý bảo vệ:
* Thiết bị đắt tiền (máy chủ, thiết bị mạng).
* Dữ liệu nhạy cảm được lưu trữ trên phần cứng hoặc tài liệu in ấn.
* Sự an toàn của nhân viên và khách thăm quan.

## Phép ẩn dụ: Cửa hàng kẹo
Hãy tưởng tượng bạn sở hữu một cửa hàng kẹo luôn tấp nập khách:
* Bạn có thể khóa ngăn kéo đựng tiền, nhưng nếu ai đó đột nhập vào cửa hàng sau giờ làm việc, họ có thể lấy đi tất cả kẹo và tiền.
* **An ninh vật lý**: Là việc lắp ổ khóa chắc chắn cho cửa chính, cài đặt hệ thống báo động và thuê bảo vệ để đảm bảo "kẹo" (dữ liệu) của bạn luôn an toàn.

## Chiến lược Phòng thủ đa lớp (Defense in Depth)
An ninh vật lý không chỉ là ổ khóa và lính canh, mà là sự kết hợp của con người, quy trình và công nghệ:
1. **Ngăn chặn (Deter)**: Rào chắn, biển cảnh báo để kẻ xấu từ bỏ ý định.
2. **Phát hiện (Detect)**: Camera giám sát (CCTV), cảm biến chuyển động.
3. **Trì hoãn (Delay)**: Cửa gia cố, khóa chất lượng cao để kéo dài thời gian đột nhập.
4. **Phản ứng (Respond)**: Lực lượng bảo vệ tại chỗ phản ứng khi có sự cố.

## Các lỗ hổng vật lý phổ biến

| Lỗ hổng | Mô tả |
| --- | --- |
| **Điểm truy cập không an toàn** | Cửa sổ, cửa ra vào không khóa hoặc dễ dàng bị vượt qua. |
| **Khóa yếu** | Ổ khóa lỗi thời hoặc kém chất lượng. |
| **Quản lý chìa khóa kém** | Để lộ chìa khóa, thẻ từ hoặc chia sẻ thông tin truy cập trái phép. |
| **Thiếu ánh sáng** | Khu vực tối giúp kẻ trộm dễ dàng ẩn nấp. |
| **Hạ tầng IT bị lộ** | Máy chủ, dây cáp mạng nằm ở nơi người lạ có thể tiếp cận. |
| **Trạm làm việc không được giám sát** | Máy tính để ở nơi công cộng mà không khóa màn hình. |

## Trách nhiệm
* **Đội ngũ quản lý cơ sở vật chất**: Bảo trì tòa nhà và các thiết bị bảo mật vật lý.
* **Đội ngũ An ninh IT**: Bảo vệ phần cứng và thiết bị mạng.
* **Toàn thể nhân viên**: Tuân thủ các quy tắc (ví dụ: không giữ cửa cho người lạ vào, không để lộ thẻ tên).

## Kiểm thử An ninh vật lý
Được thực hiện bởi các chuyên gia (thường gọi là **Red Teamers**). Họ mô phỏng các cuộc tấn công thực tế như:
* Thử vượt qua hệ thống kiểm soát cửa.
* Tấn công kỹ thuật xã hội để nhân viên cho phép vào khu vực hạn chế.
* Kiểm tra thời gian phản ứng của lực lượng bảo vệ.

## Liên kết liên quan
- [[information-security|An ninh thông tin]]
- [[operational-security|An ninh vận hành]]
- [[cybersecurity-teams|Các đội ngũ an ninh mạng]]
