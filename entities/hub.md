---
sources: ["raw/Hack The Box/Network Foundations/Networking Fundamentals - Components of a Network.md"]
tags: ["networking", "hardware", "hub"]
---

# Bộ tập trung (Hub)

[[hub|Hub]] là một thiết bị mạng cơ bản và hiện nay đã trở nên lỗi thời trong các mạng hiện đại.

## Đặc điểm chính
* **Tầng OSI**: Hoạt động tại **Tầng vật lý (Layer 1)**.
* **Chức năng**: Kết nối nhiều thiết bị trong một phân đoạn mạng.
* **Hạn chế**:
    * **Phát sóng (Broadcast)**: Hub không có khả năng quản lý lưu lượng thông minh; nó gửi mọi dữ liệu nhận được tới tất cả các cổng, bất kể đích đến là đâu.
    * **Kém hiệu quả**: Dễ gây ra va chạm dữ liệu (collisions) và lãng phí băng thông.

## Tình trạng hiện tại
Hiện nay, Hub đã được thay thế hoàn toàn bởi [[switch|Switch]] do Switch có hiệu suất và tính thông minh cao hơn nhiều.
