---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Network Infromation Gathering - Publicly Available Data.md"]
tags: ["security", "reconnaissance", "osint", "information-gathering"]
---

# Tình báo nguồn tin công khai (Open Source Intelligence - OSINT)

**OSINT** là quá trình thu thập và phân tích thông tin từ các nguồn công khai có sẵn để hiểu rõ về một tổ chức hoặc cá nhân. Trong [[penetration-testing|kiểm thử xâm nhập]], OSINT giúp chuyên gia xây dựng bức tranh toàn cảnh về hạ tầng kỹ thuật và con người của mục tiêu trước khi thực hiện các kỹ thuật tấn công trực tiếp.

## Các nguồn thông tin chính

Việc thu thập dữ liệu công khai bao gồm nhiều nguồn khác nhau:

1.  **Dữ liệu doanh nghiệp**: Trang web công ty, thông cáo báo chí, báo cáo tài chính hàng năm (đối với các công ty niêm yết). Những tài liệu này cung cấp cái nhìn về quy mô hoạt động, vị trí văn phòng và các đối tác kinh doanh.
2.  **Mạng xã hội**:
    *   **LinkedIn**: Cực kỳ hữu ích để tìm hiểu về đội ngũ nhân sự kỹ thuật. Hồ sơ nhân viên thường liệt kê các kỹ năng, dự án và công nghệ mà họ đang sử dụng.
    *   **Twitter/X**: Cung cấp các cập nhật mới nhất và các mối quan tâm của tổ chức.
3.  **Hồ sơ công khai**: Giấy phép kinh doanh, bằng sáng chế và thông tin đăng ký tên miền.
4.  **Kho lưu trữ mã nguồn (GitHub)**: Các nhà phát triển đôi khi vô tình chia sẻ các công cụ nội bộ hoặc tệp cấu hình chứa thông tin nhạy cảm như mật khẩu, khóa API hoặc địa chỉ máy chủ nội bộ.
5.  **Tin tuyển dụng**: Các yêu cầu về kỹ năng trong tin tuyển dụng (ví dụ: "Cần kinh nghiệm với Apache 2.4.x hoặc MySQL 5.7") là manh mối quan trọng về ngăn xếp công nghệ (tech stack) mà công ty đang sử dụng.

## Mục tiêu của OSINT

*   **Xác định các thành phần phụ thuộc**: Hiểu được công ty sử dụng dịch vụ của bên thứ ba nào (ví dụ: dịch vụ lưu trữ đám mây, dịch vụ email) để kiểm tra các rủi ro liên quan.
*   **Tìm kiếm lỗ hổng gián tiếp**: Phát hiện các lỗ hổng đã biết (CVE) liên quan đến phần mềm mà công ty đang sử dụng dựa trên thông tin thu thập được.
*   **Hỗ trợ tấn công tâm lý**: Sử dụng thông tin về nhân viên và văn hóa công ty để tạo ra các kịch bản [[social-engineering|tấn công kỹ thuật xã hội]] thuyết phục hơn.

## Liên kết liên quan
- [[information-gathering|Thu thập thông tin]]
- [[penetration-testing|Kiểm thử xâm nhập]]
- [[social-engineering|Tấn công kỹ thuật xã hội]]
- [[cyber-threats|Các mối đe dọa mạng]]
