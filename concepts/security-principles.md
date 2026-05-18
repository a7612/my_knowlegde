---
sources: ["raw/Hack The Box/Introduction to Information Security/Introduction - Principles of Information Security.md"]
tags: ["security", "principles", "cia-triad", "privacy"]
---

# Các nguyên tắc an ninh thông tin (Principles of Information Security)

An ninh thông tin hoạt động dựa trên một bộ các nguyên tắc cơ bản, tạo thành nền tảng cho việc quản lý, bảo vệ và xử lý an toàn các tài sản thông tin quan trọng.

## 1. Tính bảo mật (Confidentiality)
Đảm bảo rằng thông tin chỉ có thể được truy cập bởi những người được ủy quyền.
* **Mục tiêu**: Bảo vệ chống lại việc tiết lộ thông tin trái phép.
* **Biện pháp triển khai**: Mã hóa (Encryption), kiểm soát truy cập (Access Controls).

## 2. Tính toàn vẹn (Integrity)
Duy trì và đảm bảo tính chính xác và đầy đủ của dữ liệu trong suốt vòng đời của nó.
* **Mục tiêu**: Bảo vệ chống lại việc sửa đổi thông tin trái phép.
* **Biện pháp triển khai**: Hàm băm (Hashing), chữ ký số (Digital Signatures).

## 3. Tính sẵn sàng (Availability)
Đảm bảo rằng thông tin và hệ thống có thể được truy cập bởi người dùng được ủy quyền khi cần thiết.
* **Mục tiêu**: Bảo vệ chống lại sự gián đoạn truy cập thông tin.
* **Biện pháp triển khai**: Dự phòng (Redundancy), lập kế hoạch phục hồi sau thảm họa (Disaster Recovery).

## 4. Chống chối bỏ (Non-repudiation)
Đảm bảo rằng một bên không thể phủ nhận tính xác thực của chữ ký trên tài liệu hoặc việc gửi một thông điệp mà họ đã tạo ra.
* **Ý nghĩa**: Quan trọng trong thương mại điện tử và bối cảnh pháp lý.
* **Biện pháp triển khai**: Chữ ký số, nhật ký kiểm toán (Audit logs).

## 5. Xác thực (Authentication)
Xác minh danh tính của người dùng, quy trình hoặc thiết bị.
* **Ý nghĩa**: Đảm bảo chỉ các thực thể được ủy quyền mới có thể truy cập tài nguyên.
* **Biện pháp triển khai**: Mật khẩu, sinh trắc học, xác thực đa yếu tố (MFA).

## 6. Tính riêng tư (Privacy)
Tập trung vào việc xử lý đúng cách các thông tin cá nhân nhạy cảm.
* **Ý nghĩa**: Đảm bảo tuân thủ các quy định bảo vệ dữ liệu.
* **Biện pháp triển khai**: Giảm thiểu dữ liệu (Data minimization), quản lý sự đồng ý (Consent management).

## Liên kết liên quan
- [[information-security|An ninh thông tin]]
- [[network-security|An ninh mạng]]
- [[authentication-protocols|Giao thức xác thực]]
