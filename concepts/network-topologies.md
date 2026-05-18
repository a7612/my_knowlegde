---
sources: ["raw/Hack The Box/Introduction to Networking/Networking Structure - Networking Topologies.md"]
tags: ["networking", "topologies", "architecture"]
---

# Sơ đồ mạng (Network Topologies)

**Sơ đồ mạng (Topology)** là cách sắp xếp các thiết bị vật lý hoặc logic và các kết nối của chúng trong một mạng. Nó xác định các thành phần cần sử dụng và phương thức truy cập vào phương tiện truyền dẫn.

## 1. Phân loại Topology

*   **Sơ đồ Vật lý (Physical Topology)**: Cách sắp xếp thực tế của các thiết bị, cáp truyền dẫn (bố cục cáp, vị trí các nút).
*   **Sơ đồ Logic (Logical Topology)**: Cách các tín hiệu hoặc dữ liệu thực sự được truyền tải qua mạng giữa các thiết bị, bất kể kết nối vật lý như thế nào.

## 2. Các thành phần kết nối

*   **Kết nối có dây**: Cáp đồng trục (Coaxial), Cáp quang (Fiber optic), Cáp xoắn đôi (Twisted-pair).
*   **Kết nối không dây**: Wi-Fi, Di động (Cellular), Vệ tinh.
*   **Các nút mạng (Nodes)**: Điểm kết nối của phương tiện truyền dẫn với các thiết bị thu/phát (Repeaters, Hubs, Bridges, Switches, Routers, Modems, Gateways, Firewalls).

## 3. Các loại Sơ đồ mạng cơ bản

| Loại Topology | Đặc điểm chính |
| :--- | :--- |
| **Điểm-đến-Điểm (Point-to-Point)** | Kết nối trực tiếp giữa hai máy chủ (host). |
| **Bus** | Tất cả các máy chủ kết nối qua một đường truyền chung. Chỉ một máy có thể gửi dữ liệu tại một thời điểm. |
| **Ngôi sao (Star)** | Tất cả các máy chủ kết nối với một thiết bị trung tâm (Router/Switch). |
| **Vòng (Ring)** | Mỗi máy chủ kết nối với hai máy khác tạo thành vòng khép kín. Dữ liệu truyền theo một hướng nhất định. |
| **Lưới (Mesh)** | Các nút kết nối với nhau theo nhiều đường. Có hai loại: Toàn phần (Fully meshed) và Một phần (Partially meshed). |
| **Cây (Tree)** | Một cấu trúc hình sao mở rộng, thường được sử dụng trong các tòa nhà lớn hoặc mạng đô thị (MAN). |
| **Hỗn hợp (Hybrid)** | Kết hợp hai hoặc nhiều loại sơ đồ cơ bản lại với nhau. |
| **Daisy Chain** | Các máy chủ được kết nối nối tiếp nhau thành một chuỗi. |

## Liên kết liên quan
*   [[computer-network|Mạng máy tính]]
*   [[network-hardware|Thiết bị mạng]]
*   [[network-types|Các loại mạng]]
