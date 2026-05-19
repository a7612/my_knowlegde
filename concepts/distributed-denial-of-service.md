---
sources: ["raw/Hack The Box/Introduction to Information Security/Threats - Distributed Denial of Service.md"]
tags: ["security", "threats", "ddos", "network-security"]
---

# Tấn công từ chối dịch vụ phân tán (Distributed Denial of Service - DDoS)

**DDoS attack** là một nỗ lực độc hại nhằm làm gián đoạn hoạt động bình thường của một trang web, máy chủ hoặc dịch vụ trực tuyến bằng cách làm tràn ngập nó với một lượng lớn lưu lượng truy cập internet. Khác với tấn công **Denial of Service (DoS)** truyền thống chỉ đến từ một nguồn duy nhất, tấn công DDoS đến từ nhiều nguồn cùng một lúc.

## Các thành phần chính của cuộc tấn công
1.  **Kẻ tấn công (The Attacker)**: Cá nhân hoặc nhóm điều phối cuộc tấn công.
2.  **Mạng máy tính ma (Botnet)**: Một mạng lưới các thiết bị bị xâm nhập (máy tính, máy chủ, thiết bị [[my_knowlegde/concepts/iot-security|IoT]]) nằm rải rác ở nhiều nơi, được điều khiển từ xa bởi kẻ tấn công.
3.  **Nạn nhân (The Victim)**: Máy chủ, dịch vụ hoặc mạng lưới mục tiêu mà kẻ tấn công muốn làm tê liệt.

## Cách thức hoạt động
Kẻ tấn công gửi lệnh đến Botnet, yêu cầu tất cả các thiết bị trong mạng lưới gửi yêu cầu truy cập đến nạn nhân cùng một lúc. Sự gia tăng đột biến của lưu lượng truy cập này tiêu thụ hết băng thông và khả năng xử lý của mục tiêu, khiến nó chạy chậm lại đáng kể hoặc bị sập hoàn toàn. Người dùng hợp lệ sẽ không thể truy cập dịch vụ trong thời gian này.

## Ví dụ điển hình: Cuộc tấn công vào Dyn (2016)
Vào năm 2016, một cuộc tấn công DDoS lớn đã nhắm vào Dyn, một công ty cung cấp dịch vụ internet quan trọng. Cuộc tấn công đã khiến các trang web lớn như Twitter, Netflix và Reddit không thể truy cập được trong nhiều giờ. Kẻ tấn công đã sử dụng mã độc **Mirai** để tạo ra một botnet khổng lồ từ hàng ngàn thiết bị IoT như camera và bộ định tuyến gia đình.

## Tác động
*   **Tổn thất tài chính**: Ngừng hoạt động dẫn đến mất doanh thu, đặc biệt là với các trang thương mại điện tử và ngân hàng trực tuyến.
*   **Hư hại danh tiếng**: Các sự cố ngừng dịch vụ kéo dài làm xói mòn lòng tin của khách hàng.
*   **Gián đoạn vận hành**: Ảnh hưởng đến các dịch vụ thiết yếu và người dùng phụ thuộc vào chúng.
*   **Bức bình phong (Smokescreen)**: Đôi khi DDoS được sử dụng để làm xao nhãng đội ngũ bảo mật trong khi kẻ tấn công thực hiện các hành vi xâm nhập dữ liệu hoặc cài đặt mã độc khác.

## Liên kết liên quan
- [[my_knowlegde/concepts/cyber-threats|Các mối đe dọa mạng]]
- [[my_knowlegde/concepts/iot-security|An ninh Internet vạn vật]]
- [[my_knowlegde/concepts/network-security|An ninh mạng]]
- [[my_knowlegde/concepts/incident-management|Quản lý sự cố]]
