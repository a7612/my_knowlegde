---
sources:
  - "Hack The Box - Network Foundations - Networking Fundamentals - Introduction to Networks.md"
  - "Hack The Box - Network Foundations - Networking Fundamentals - Components of a Network.md"
  - "Hack The Box - Network Foundations - Network Concepts.md"
  - "Hack The Box - Network Foundations - Network Communication and Addressing - Network Communication.md"
  - "Hack The Box - Network Foundations - Network Communication and Addressing - Domain Name System (DNS).md"
  - "Hack The Box - Network Foundations - Network Communication and Addressing - Dynamic Host Configuration Protocol (DHCP).md"
  - "Hack The Box - Network Foundations - Network Communication and Addressing - Network Address Translation (NAT).md"
tags:
  - "networking"
  - "fundamentals"
  - "summary"
---
# Tóm tắt: Cơ bản về Mạng máy tính (Networking Fundamentals)

Tài liệu này tổng hợp toàn bộ kiến thức cơ bản về mạng máy tính, bao gồm cấu trúc, thành phần, mô hình và các cơ chế giao tiếp.

## Nội dung chính

### 1. Khái niệm và Phân loại
- **[[my_knowlegde/concepts/computer-network|Mạng máy tính]]**: Kết nối thiết bị để chia sẻ tài nguyên.
- **[[local-area-network|LAN]] vs [[wide-area-network|WAN]]**: Phân loại theo quy mô địa lý. [[internet-service-provider|ISP]] cung cấp kết nối tới WAN toàn cầu.

### 2. Định danh và Giao tiếp
- **[[my_knowlegde/concepts/mac-address|Địa chỉ MAC]]**: Định danh vật lý duy nhất của [[network-interface-card|Card mạng]].
- **[[ip-address|Địa chỉ IP]]**: Định danh logic (IPv4/IPv6). Có sự phân biệt giữa IP công cộng và IP riêng.
- **[[port|Cổng (Port)]]**: Phân loại lưu lượng cho các ứng dụng (Web: 80/443, FTP: 21, v.v.).

### 3. Các cơ chế tự động và hỗ trợ
- **[[dns|DNS]]**: "Danh bạ" Internet, dịch tên miền sang IP.
- **[[dhcp|DHCP]]**: Tự động cấp phát IP cho thiết bị (quy trình **DORA**).
- **[[nat|NAT]]**: Cho phép nhiều thiết bị dùng chung một IP công cộng để ra Internet.
- **[[arp|ARP]]**: Cầu nối giữa IP và MAC trong mạng nội bộ.

### 4. Thành phần và Mô hình
- **Nút mạng**: Bao gồm thiết bị đầu cuối và thiết bị trung gian ([[my_knowlegde/entities/router|Router]], [[my_knowlegde/entities/switch|Switch]], [[my_knowlegde/entities/modem|Modem]], [[server|Máy chủ]]).
- **Mô hình tham chiếu**: [[osi-model|Mô hình OSI]] (7 tầng) và [[tcp-ip-model|Mô hình TCP/IP]] (4 tầng).
- **[[network-protocol|Giao thức]]**: Quy tắc chung cho giao tiếp mạng.
- **[[transmission-media|Phương tiện truyền dẫn]]**: Cáp, sóng vô tuyến và các chế độ truyền (Simplex, Duplex).

## Kết luận
Mạng máy tính hiện đại là một sự kết hợp phức tạp nhưng tinh vi giữa phần cứng vật lý và các tầng giao thức phần mềm. Việc hiểu rõ cách các thành phần này phối hợp giúp xây dựng, quản lý và bảo mật hệ thống thông tin một cách hiệu quả.
