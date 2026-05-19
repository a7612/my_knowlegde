---
sources: ["raw/Hack The Box/Introduction to Networking/Protocols & Terminology - Vendor Specific Information.md", "raw/Hack The Box/Introduction to Networking/Networking Structure - Networking Topologies.md"]
tags: ["networking", "switching", "vlan", "segmentation", "802.1Q"]
---

# Mạng cục bộ ảo (Virtual Local Area Network - VLAN)

**VLAN** là một kỹ thuật phân đoạn logic mạng cục bộ (LAN) trên thiết bị chuyển mạch (Switch), cho phép chia một Switch vật lý thành nhiều Switch ảo, tạo ra các miền quảng bá (broadcast domains) riêng biệt.

## 1. Phân loại và Định danh VLAN
Cisco Switch hỗ trợ các ID từ 1 đến 4094:
*   **Normal-range VLANs (1 - 1005)**:
    *   ID 1: VLAN mặc định (Default VLAN), không thể xóa hay sửa đổi.
    *   ID 1002 - 1005: Dành riêng cho Token Ring và FDDI.
    *   Các thông số được lưu trong tệp `vlan.dat`.
*   **Extended-range VLANs (1006 - 4094)**: Dành cho các mạng quy mô lớn, thông số không được lưu trong `vlan.dat`.

## 2. Nhận diện và Gắn thẻ (VLAN Tagging)
Khi gói tin đi qua cổng Trunk, Switch cần cơ chế để nhận biết gói tin thuộc về VLAN nào.
*   **IEEE 802.1Q**: Tiêu chuẩn phổ biến nhất. Nó chèn thêm một header 4-byte vào khung Ethernet. Các trường quan trọng:
    *   **TPID (0x8100)**: Định danh đây là khung được gắn thẻ 802.1Q.
    *   **TCI**: Chứa thông tin ưu tiên (PCP) và quan trọng nhất là **VID (VLAN Identifier)** - ID của VLAN (12-bit).
*   **ISL (Inter-Switch Link)**: Giao thức độc quyền của Cisco, đóng gói toàn bộ khung Ethernet (26-byte header + 4-byte trailer). Hiện đã lỗi thời.

## 3. Cấu hình VLAN cho Card mạng (NIC)
Một số NIC hỗ trợ gắn thẻ VLAN trực tiếp từ hệ điều hành.

### Trên Linux
Sử dụng mô-đun hạt nhân `8021q` và công cụ `ip`:
```bash
# Nạp module
sudo modprobe 8021q
# Tạo giao diện VLAN 20 trên eth0
sudo ip link add link eth0 name eth0.20 type vlan id 20
# Gán IP và khởi chạy
sudo ip addr add 192.168.1.1/24 dev eth0.20
sudo ip link set up eth0.20
```

### Trên Windows
*   **GUI**: Vào `Device Manager` -> `Properties` của NIC -> tab `Advanced` -> chọn `VLAN ID`.
*   **PowerShell**:
```powershell
Set-NetAdapter -Name "Ethernet 2" -VlanID 10
```

## 4. Phân tích lưu lượng VLAN
Có thể sử dụng **Wireshark** hoặc **tshark** để lọc và phân tích:
*   Wireshark filter: `vlan` hoặc `vlan.id == 10`.
*   Tshark (liệt kê các VLAN ID có trong tệp pcap):
```bash
tshark -r capture.pcap -T fields -e vlan.id | sort -n -u
```

## 5. Các kiểu tấn công VLAN
*   **VLAN Hopping**: Lợi dụng giao thức **DTP (Dynamic Trunking Protocol)** để thiết lập đường Trunk trái phép và truy cập tất cả các VLAN.
*   **Double-tagging**: Lồng hai thẻ VLAN. Switch đầu tiên gỡ thẻ ngoài (Native VLAN), Switch thứ hai đọc thẻ trong và chuyển tiếp đến VLAN mục tiêu. Kẻ tấn công phải thuộc về cùng VLAN với `Native VLAN` của cổng Trunk để thực hiện.

## 6. VXLAN (Virtual eXtensible LAN)
Giải pháp cho trung tâm dữ liệu, sử dụng định danh 24-bit (**VNI**) hỗ trợ tới 16 triệu VLAN, hoạt động như một lớp phủ (overlay) Layer 2 trên hạ tầng Layer 3.

## Liên kết liên quan
- [[my_knowlegde/entities/network-hardware|Thiết bị mạng]]
- [[my_knowlegde/entities/cisco-ios|Hệ điều hành Cisco IOS]]
- [[addressing-and-routing|Định danh và Truyền thông]]
- [[mac-address|Địa chỉ MAC]]
