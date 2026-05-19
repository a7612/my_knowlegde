---
sources: ["raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Cloud Security.md"]
tags: ["security", "cloud", "shared-responsibility", "iam", "compliance"]
---

# An ninh đám mây (Cloud Security)

**An ninh đám mây** là tập hợp các biện pháp được thiết kế để bảo vệ dữ liệu, ứng dụng và hạ tầng được lưu trữ trên các nền tảng đám mây.

## Phép ẩn dụ: Cơ sở lưu trữ công nghệ cao
Hãy tưởng tượng bạn gửi đồ quý giá vào một kho lưu trữ chung hiện đại thay vì để ở nhà:
* **Kho lưu trữ (Đám mây)**: Nơi bạn cất giữ tài sản và truy cập khi cần.
* **Bảo vệ chung**: Chủ kho cung cấp camera, bảo vệ cổng (hạ tầng đám mây).
* **Khóa riêng**: Bạn chịu trách nhiệm khóa ngăn tủ cá nhân của mình (dữ liệu và ứng dụng).

## Mô hình Trách nhiệm Chia sẻ (Shared Responsibility Model)
Đây là khái niệm cốt lõi trong an ninh đám mây:
* **Nhà cung cấp dịch vụ (CSP)**: Bảo vệ "tòa nhà" - tức là hạ tầng vật lý, mạng lưới và các dịch vụ cơ bản.
* **Khách hàng (Bạn)**: Bảo vệ "ngăn tủ" - tức là cấu hình quyền truy cập, bảo mật dữ liệu và ứng dụng bên trong đám mây.

## Các mối đe dọa chính trên Đám mây
1. **Vi phạm dữ liệu (Data Breaches)**: Truy cập trái phép vào thông tin nhạy cảm do lỗi cấu hình hoặc tấn công.
2. **API không an toàn**: Các giao diện lập trình ứng dụng có lỗ hổng bị tin tặc khai thác để xâm nhập hệ thống.
3. **Cấu hình sai (Misconfiguration)**: Ví dụ như để hở các kho lưu trữ dữ liệu (storage buckets) cho công chúng truy cập.
4. **Chiếm đoạt tài khoản (Account Hijacking)**: Kẻ tấn công đánh cắp thông tin đăng nhập để kiểm soát tài khoản đám mây.

## Các lĩnh vực then chốt của An ninh đám mây
* **Bảo vệ dữ liệu**: Mã hóa dữ liệu khi đang lưu trữ (at rest) và khi đang truyền tải (in transit).
* **Quản lý Danh tính và Truy cập (IAM)**: Đảm bảo chỉ những người được ủy quyền mới có thể truy cập tài nguyên (như sử dụng mã khóa cá nhân, xác thực đa yếu tố).
* **Bảo mật mạng**: Sử dụng tường lửa và VPN trên đám mây để giám sát và bảo vệ các luồng dữ liệu.
* **Tuân thủ và Quản trị (Compliance & Governance)**: Đảm bảo các hoạt động trên đám mây tuân thủ luật pháp và các tiêu chuẩn ngành.

## Trách nhiệm và Kiểm thử
* **Nhà cung cấp đám mây**: Đảm bảo hạ tầng luôn an toàn và sẵn sàng.
* **Quản trị viên/Khách hàng**: Thực hiện các chính sách mật khẩu mạnh, quản lý quyền hạn người dùng.
* **Đội ngũ an ninh/Penetration Testers**: Thường xuyên kiểm tra để tìm ra các điểm yếu trong cấu hình đám mây trước khi tin tặc tìm thấy.

## Liên kết liên quan
- [[information-security|An ninh thông tin]]
- [[network-security|An ninh mạng]]
- [[virtualization-and-containers|Ảo hóa và Container]]
