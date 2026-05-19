---
sources: ["raw/Hack The Box/Introduction to Information Security/InfoSec Domains - Operational Security.md"]
tags: ["security", "opsec", "operations", "access-control", "risk-assessment"]
---

# An ninh vận hành (Operational Security - OpSec)

**An ninh vận hành (OpSec)** là một thành phần thiết yếu trong chiến lược bảo mật tổng thể của tổ chức. Nó bao gồm các quy trình, thực hành và quyết định liên quan đến việc xử lý và bảo vệ tài sản dữ liệu trong suốt vòng đời của chúng.

## Mục tiêu cốt lõi
Duy trì môi trường an toàn cho các hoạt động hàng ngày của tổ chức, đảm bảo thông tin nhạy cảm luôn được bảo mật, nguyên vẹn và chỉ những người có thẩm quyền mới có thể tiếp cận.

## Phép ẩn dụ: Tổ chức một bữa tiệc sinh nhật
Hãy tưởng tượng bạn đang lên kế hoạch cho một bữa tiệc lớn tại nhà. Bạn có những món đồ quý giá (như máy chơi game, đồ gia bảo) không muốn bị hỏng hoặc mất. OpSec giống như kế hoạch bảo vệ những món đồ đó trong khi bữa tiệc vẫn diễn ra:

1. **Xác định tài sản (Assets Identification)**: Xác định món đồ nào quan trọng nhất cần bảo vệ (ví dụ: sợi dây chuyền gia bảo).
2. **Xác định mối đe dọa (Threat Identification)**: Suy nghĩ về những gì có thể xảy ra (ví dụ: một vị khách vô tình làm vỡ đồ, hoặc ai đó lẻn vào phòng riêng).
3. **Xác định lỗ hổng (Vulnerability Identification)**: Tìm điểm yếu (ví dụ: cửa phòng không khóa, hoặc khách có thể dễ dàng tiếp cận tủ kính).
4. **Kiểm soát truy cập (Access Control)**: Quyết định ai được vào phòng nào (ví dụ: chỉ bạn thân mới có chìa khóa phòng riêng).
5. **Giám sát (Monitoring)**: Luôn để mắt tới khách mời trong suốt bữa tiệc và điều chỉnh kế hoạch nếu thấy ai đó đi vào khu vực cấm.

## Quy trình OpSec trong thực tế
OpSec là một quy trình liên tục và năng động, bao gồm:

### 1. Kiểm soát truy cập (Access Control)
Xác định ai có quyền truy cập vào thông tin và hệ thống nào.
* **Xác thực**: Sử dụng các cơ chế như xác thực đa yếu tố (MFA).
* **Ủy quyền**: Đảm bảo người dùng chỉ có quyền hạn cần thiết cho vai trò của họ.
* **Kiểm toán (Auditing)**: Thường xuyên rà soát lại quyền truy cập để thu hồi khi không còn cần thiết (ví dụ: khi nhân viên nghỉ việc).

### 2. Quản lý tài sản (Asset Management)
Duy trì danh mục cập nhật về tất cả tài sản thông tin (phần cứng, phần mềm, dữ liệu). Việc hiểu rõ mình có gì và chúng nằm ở đâu là điều kiện tiên quyết để bảo vệ chúng.

### 3. Quản lý thay đổi (Change Management)
Đảm bảo các thay đổi đối với hệ thống và quy trình được thực hiện một cách có kiểm soát, có thử nghiệm và phê duyệt đúng quy trình để tránh vô tình tạo ra lỗ hổng bảo mật mới.

### 4. Đào tạo nhận thức bảo mật
Đảm bảo tất cả nhân viên hiểu vai trò của mình trong việc giữ an toàn cho tổ chức (ví dụ: nhận biết tấn công giả mạo - phishing, tầm quan trọng của mật khẩu mạnh).

## Trách nhiệm trong OpSec
* **Đội ngũ An ninh thông tin**: Dưới sự dẫn dắt của **CISO**, phối hợp với các phòng ban (IT, HR, Pháp lý) để đảm bảo các biện pháp bảo mật phù hợp với nhu cầu kinh doanh.
* **Tất cả nhân viên**: Mọi người đều có trách nhiệm tuân thủ các giao thức bảo mật (ví dụ: không chia sẻ thẻ ra vào, không mở cửa cho người lạ vào khu vực hạn chế).

## Kiểm thử OpSec
Các đội ngũ an ninh nội bộ hoặc tư vấn bên ngoài thường thực hiện các bài kiểm tra OpSec thông qua:
* **Kiểm thử xâm nhập (Penetration Testing)**.
* **Tấn công kỹ thuật xã hội (Social Engineering)**: Thử nghiệm xem nhân viên có dễ bị lừa để cung cấp thông tin nhạy cảm hay không.

## Liên kết liên quan
- [[my_knowlegde/concepts/information-security|An ninh thông tin]]
- [[my_knowlegde/concepts/risk-management|Quản lý rủi ro]]
- [[my_knowlegde/concepts/security-roles|Các vai trò trong an ninh thông tin]]
