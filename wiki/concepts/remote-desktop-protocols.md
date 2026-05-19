---
sources:
  - "Hack The Box Academy - Remote Desktop Protocols in Linux"
tags:
  - "linux"
  - "networking"
  - "remote-access"
---

# Giao thức Điều khiển Máy tính Từ xa (Remote Desktop Protocols)

Các giao thức điều khiển máy tính từ xa cung cấp quyền truy cập giao diện đồ họa (GUI) vào hệ thống Windows, Linux và macOS, cho phép quản trị viên quản lý, khắc phục sự cố và cập nhật hệ thống từ xa.

## Các giao thức phổ biến

*   **Remote Desktop Protocol (RDP)**: Chủ yếu dùng trong môi trường Windows.
*   **Virtual Network Computing (VNC)**: Phổ biến trong môi trường Linux, nhưng cũng hỗ trợ đa nền tảng.

## X Window System (X11 / X)

X11 là một tập hợp các giao thức và ứng dụng cho phép hiển thị cửa sổ ứng dụng trên giao diện đồ họa, phổ biến trên các hệ thống Unix.

*   **Tính minh bạch mạng (Network Transparency)**: X11 có thể hiển thị ứng dụng từ máy chủ từ xa lên máy khách cục bộ.
*   **Cổng kết nối**: Thường dùng các cổng `TCP/6000-6010`. Màn hình đầu tiên `:0` dùng cổng `6000`.
*   **X11 Forwarding**: Cho phép truyền ứng dụng X11 qua SSH để bảo mật (mặc định X11 không mã hóa).
    *   Cấu hình trong `/etc/ssh/sshd_config`: `X11Forwarding yes`.
    *   Sử dụng: `ssh -X user@ip application`.
*   **Bảo mật**: X11 không mã hóa theo mặc định, dễ bị tấn công nghe lén (sniffing) hoặc chụp màn hình nếu không được bảo vệ.

## XDMCP (X Display Manager Control Protocol)

Dùng để quản lý các phiên X Window từ xa qua cổng **UDP/177**. Đây là giao thức không an toàn, dễ bị tấn công Man-in-the-Middle (MitM).

## Virtual Network Computing (VNC)

VNC dựa trên giao thức RFB, cho phép điều khiển máy tính từ xa như thể đang ngồi trước máy.

*   **Cơ chế hoạt động**: Thường lắng nghe trên cổng **TCP/5900** (cho display 0). Các display tiếp theo dùng cổng `5901, 5902...`
*   **Phần mềm phổ biến**: TigerVNC, TightVNC, RealVNC, UltraVNC.
*   **Bảo mật**: Nên kết hợp với SSH Tunnel để mã hóa dữ liệu.
*   **Cài đặt (Ubuntu)**: Thường dùng gói `tigervnc-standalone-server` kết hợp với Desktop Manager nhẹ như `XFCE4`.

## Liên kết liên quan
*   [[linux-network-services|Dịch vụ Mạng Linux]]
*   [[network-security|Bảo mật Mạng]]
*   [[linux-web-services|Dịch vụ Web]]
