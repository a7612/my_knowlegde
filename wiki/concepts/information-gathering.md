---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Network Infromation Gathering - Publicly Available Data.md", "raw/Hack The Box/Pentest in a Nutshell/Network Infromation Gathering - Network and Service Scanning.md"]
tags: ["security", "pentest", "information-gathering", "reconnaissance", "osint", "scanning"]
---

# Thu thập thông tin (Information Gathering)

**Thu thập thông tin (Information Gathering)** là giai đoạn thứ hai trong quy trình [[penetration-testing|kiểm thử xâm nhập]]. Mục tiêu của giai đoạn này là thu thập càng nhiều dữ liệu càng tốt về tổ chức mục tiêu để hiểu cấu trúc, cách thức hoạt động và các tài nguyên kỹ thuật của họ. Thông tin này là nền tảng để xác định các vector tấn công hiệu quả.

Quá trình này thường được chia thành hai phương pháp chính:

## 1. Thu thập dữ liệu công khai ([[osint|OSINT]])
Sử dụng các nguồn thông tin công khai để xây dựng bức tranh toàn cảnh về mục tiêu mà không cần tương tác trực tiếp với hệ thống của họ.
*   **Nguồn**: Trang web công ty, mạng xã hội (LinkedIn, Twitter), hồ sơ tài chính, kho lưu trữ mã nguồn (GitHub).
*   **Lợi ích**: Giúp hiểu về công nghệ đang sử dụng, nhân sự kỹ thuật, và đôi khi là các thông tin nhạy cảm bị rò rỉ (mật khẩu, khóa bí mật).

## 2. Quét mạng và dịch vụ ([[network-scanning|Scanning]])
Sử dụng các công cụ kỹ thuật để xác định các thành phần đang hoạt động trong mạng lưới của khách hàng.
*   **Mục tiêu**: Xác định các máy chủ đang hoạt động (active hosts), các cổng mở (open ports) và các dịch vụ đang chạy (services).
*   **Công cụ**: [[network-scanning|Nmap]] là công cụ phổ biến nhất cho nhiệm vụ này.

## Ghi chú và Lưu trữ thông tin (Note Taking)
Việc ghi chép tỉ mỉ là yếu tố then chốt dẫn đến thành công của một dự án Pentest:
*   **Lý do**: Giúp các thành viên trong đội ngũ kiểm tra lại công việc, theo dõi tiến độ và cung cấp bằng chứng cho báo cáo cuối cùng.
*   **Nội dung cần ghi**: Các lệnh đã chạy, kết quả thu được (kể cả lỗi), ảnh chụp màn hình và các phát hiện "low-hanging fruits" (lỗ hổng dễ khai thác).
*   **Định dạng**: Nên sử dụng định dạng `Markdown` để dễ dàng trình bày và chuyển đổi.

## Liên kết liên quan
- [[penetration-testing|Kiểm thử xâm nhập]]
- [[osint|Tình báo nguồn tin công khai (OSINT)]]
- [[network-scanning|Quét mạng và dịch vụ]]
- [[pentest-pre-engagement|Giai đoạn Tiền dự án]]
