---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Concluding Report - Proof-of-Concept.md"]
tags: ["security", "pentest", "poc", "evidence", "documentation"]
---

# Bằng chứng khai thác (Proof-of-Concept - PoC)

**Proof-of-Concept (PoC)** là một bản trình diễn kỹ thuật (thường là script, danh sách các lệnh hoặc hướng dẫn từng bước) nhằm minh chứng cho sự tồn tại thực tế của một lỗ hổng bảo mật. Trong [[penetration-testing|kiểm thử xâm nhập]], PoC đóng vai trò là bằng chứng không thể chối cãi để khách hàng hoặc đội ngũ quản trị hệ thống có thể tái hiện và xác nhận lỗ hổng.

## Mục đích của PoC

1.  **Xác nhận lỗ hổng**: Chứng minh rằng một lỗi bảo mật không chỉ là lý thuyết mà có thể bị khai thác thật sự.
2.  **Hỗ trợ tái hiện**: Giúp đội ngũ IT của khách hàng hiểu chính xác cách thức tấn công để kiểm tra lại sau khi đã vá lỗi.
3.  **Đánh giá mức độ nghiêm trọng**: Một PoC thực tế (ví dụ: lấy được quyền root) giúp ban lãnh đạo thấy rõ tác động của lỗ hổng.

## Cấu trúc của một PoC chuyên nghiệp

Một PoC tốt nên được tổ chức theo các giai đoạn của quy trình kiểm thử để dễ theo dõi:

1.  **Tóm tắt (Summary)**: Liệt kê các phát hiện chính (ví dụ: truy cập FTP ẩn danh, mật khẩu bản rõ trong lịch sử lệnh).
2.  **Thông tin mục tiêu**: IP, tên miền, các cổng và dịch vụ phát hiện được ([[network-scanning|Nmap results]]).
3.  **Các bước thực hiện**:
    *   **Lệnh sử dụng**: Các câu lệnh chính xác đã chạy trên máy tấn công hoặc máy mục tiêu.
    *   **Hình ảnh minh họa**: Ảnh chụp màn hình kết quả lệnh, nội dung tệp nhạy cảm lấy được.
    *   **Mô tả ngắn gọn**: Giải thích ý nghĩa của từng bước.
4.  **Kết quả cuối cùng**: Chứng minh mức độ xâm nhập thành công (ví dụ: nội dung tệp `root.txt` hoặc shell điều khiển từ xa).

## Sự khác biệt giữa PoC và Báo cáo (Documentation)

*   **PoC**: Tập trung hoàn toàn vào kỹ thuật, trả lời câu hỏi "Làm thế nào để tấn công?".
*   **[[pentest-documentation|Báo cáo dự án]]**: Cung cấp bức tranh toàn cảnh cho nhiều đối tượng (quản lý, kiểm toán), trả lời câu hỏi "Hệ thống bảo mật như thế nào và cần cải thiện gì?".

## Liên kết liên quan
- [[penetration-testing|Kiểm thử xâm nhập]]
- [[pentest-documentation|Báo cáo dự án Pentest]]
- [[vulnerability-assessment|Đánh giá lỗ hổng]]
- [[linux-pillaging|Vét cạn dữ liệu Linux]]
