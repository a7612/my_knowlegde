---
sources: ["raw/Hack The Box/Pentest in a Nutshell/Network Infromation Gathering - Network and Service Scanning.md"]
tags: ["security", "pentest", "scanning", "nmap", "reconnaissance"]
---

# Quét mạng và dịch vụ (Network and Service Scanning)

**Quét mạng và dịch vụ** là bước kỹ thuật nền tảng trong [[penetration-testing|kiểm thử xâm nhập]]. Giai đoạn này giúp chuyên gia xác định các máy chủ đang hoạt động, các cổng mở và các dịch vụ đang chạy trong phạm vi được cho phép để lập bản đồ bề mặt tấn công.

## 1. Hiểu về Phạm vi (Scope)
Trước khi bắt đầu quét, việc xác định rõ phạm vi là cực kỳ quan trọng. Phạm vi thường bao gồm một dải địa chỉ IP, tên miền hoặc hệ thống cụ thể mà khách hàng đã ủy quyền. Việc tuân thủ phạm vi đảm bảo các hoạt động kiểm thử luôn nằm trong giới hạn pháp lý và đạo đức.

## 2. Sử dụng Nmap
**Nmap (Network Mapper)** là công cụ phổ biến nhất để quét mạng nhờ tính linh hoạt và độ chính xác cao.

### Ví dụ về lệnh Nmap cơ bản:
```bash
nmap -sV -p- 10.129.12.0/24 -oA network-scan
```
*   `-sV`: Xác định phiên bản dịch vụ đang chạy trên các cổng mở.
*   `-p-`: Quét toàn bộ 65.535 cổng (cả TCP và UDP).
*   `-oA network-scan`: Lưu kết quả dưới mọi định dạng với tên tệp "network-scan".
*   `10.129.12.0/24`: Chỉ định dải mạng mục tiêu.

## 3. Giải thích kết quả quét
Kết quả quét cung cấp cái nhìn chi tiết về mục tiêu. Ví dụ:
*   **Cổng 21 (FTP)**: Có thể chứa các lỗ hổng về xác thực hoặc cấu hình sai.
*   **Cổng 22 (SSH)**: Một giao thức bảo mật nhưng có thể bị tấn công nếu sử dụng phiên bản cũ hoặc mật khẩu yếu.
*   **Cổng 80/443 (HTTP/HTTPS)**: Các vector tấn công phổ biến thông qua ứng dụng web.
*   **Cổng 445 (SMB)**: Mục tiêu quan trọng trong môi trường Windows (từng bị khai thác bởi EternalBlue).
*   **Cổng 3389 (RDP)**: Thường bị tấn công vét cạn (brute-force) nếu không được bảo vệ tốt.

## 4. Tận dụng kết quả
Thông tin từ Nmap được sử dụng để ưu tiên các mục tiêu cho các bước tiếp theo:
*   **Quét lỗ hổng**: Sử dụng các công cụ như Nessus để tìm các lỗ hổng đã biết dựa trên phiên bản phần mềm.
*   **Kiểm tra thông tin đăng nhập**: Thử tấn công vét cạn trên các dịch vụ như FTP, SSH, RDP.
*   **Phân tích cấu hình**: Kiểm tra các cấu hình sai phổ biến như thông tin đăng nhập mặc định.
*   **Thử nghiệm khai thác**: Sử dụng các framework như Metasploit nếu phát hiện lỗ hổng khả thi.

## Liên kết liên quan
- [[information-gathering|Thu thập thông tin]]
- [[penetration-testing|Kiểm thử xâm nhập]]
- [[network-protocols|Giao thức mạng]]
- [[pentest-pre-engagement|Giai đoạn Tiền dự án]]
