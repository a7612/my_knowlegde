# The Shadow Wiki Project
Chào mừng bạn. Đây là nơi được tổng hợp từ các tài liệu chuyên sâu.

## Các Khái niệm Cơ bản (Core Concepts)
* [[computer-network|Mạng máy tính]]: Tổng quan về mạng, LAN và WAN, các lớp phòng thủ.
* [[network-types|Các loại mạng]]: WAN, LAN, WLAN, VPN và các thuật ngữ GAN, MAN, PAN.
* [[network-topologies|Sơ đồ mạng]]: Point-to-Point, Star, Mesh và các cấu trúc vật lý/logic.
* [[internet-architecture|Kiến trúc Internet]]: Các mô hình Client-Server, P2P, Hybrid, Cloud, SDN và định danh FQDN/URL.
* [[network-models|Mô hình mạng]]: Chi tiết về mô hình OSI và TCP/IP.
* [[network-protocols|Giao thức mạng]]: Các quy tắc giao tiếp trên mạng.
* [[data-transmission|Truyền dẫn dữ liệu]]: Các phương thức và phương tiện truyền dẫn.
* [[wireless-networks|Mạng không dây]]: Wi-Fi, mạng di động và tần số vô tuyến.
* [[network-security|Bảo mật mạng]]: Bộ ba CIA, tường lửa và IDS/IPS.
* [[data-flow-analysis|Phân tích luồng dữ liệu]]: Quy trình chi tiết một yêu cầu mạng.
* [[proxies|Máy chủ ủy quyền (Proxies)]]: Forward Proxy, Reverse Proxy và WAF.

## An ninh thông tin (Information Security)
* [[information-security|An ninh thông tin]]: Tổng quan, tầm quan trọng và quy trình InfoSec.
* [[nist-csf|Khung An ninh mạng NIST (CSF) 2.0]]: Tiêu chuẩn quản trị rủi ro hiện đại.
* [[application-security|An ninh ứng dụng]]: Bảo vệ phần mềm trong suốt vòng đời phát triển.

## Tiêu chuẩn và Khung bảo mật (Standards & Frameworks)
* [[owasp-top-ten-2025|OWASP Top Ten 2025]]: Tóm tắt 10 rủi ro bảo mật ứng dụng web hàng đầu.
* [[owasp-proactive-controls|OWASP Proactive Controls]]: 10 biện pháp kiểm soát bảo mật chủ động cho nhà phát triển.
    * [[broken-access-control|A01: Kiểm soát truy cập bị hỏng]]
    * [[security-misconfiguration|A02: Cấu hình sai bảo mật]]
    * [[software-supply-chain|A03: Thất bại trong chuỗi cung ứng phần mềm]]
    * [[cryptographic-failures|A04: Thất bại trong mã hóa]]
    * [[injection-vulnerabilities|A05: Lỗi tiêm]]
    * [[insecure-design|A06: Thiết kế không an toàn]]
    * [[authentication-failures|A07: Thất bại trong xác thực]]
    * [[integrity-failures|A08: Thất bại về tính toàn vẹn]]
    * [[logging-alerting-failures|A09: Thất bại trong ghi nhật ký và cảnh báo]]
    * [[exceptional-conditions-handling|A10: Xử lý sai các điều kiện bất thường]]
* [[browser-security-features|Các tính năng bảo mật trình duyệt]]: Hardening phía client (CSP, HSTS).

## Các nguyên tắc an ninh thông tin (Information Security Principles)
* [[risk-management|Quản lý rủi ro]]: Rủi ro, mối đe dọa, lỗ hổng và đánh giá rủi ro.
* [[cyber-threats|Các mối đe dọa mạng]]: Tổng quan về các loại mối đe dọa và rủi ro.
* [[cybersecurity-teams|Các đội ngũ an ninh mạng]]: Blue Team, Red Team và Purple Team.
* [[threat-actors|Các tác nhân đe dọa]]: Các cá nhân hoặc nhóm thực hiện tấn công mạng.
* [[security-roles|Các vai trò trong an ninh mạng]]: CISO, Security Architect, Pen Tester.
* [[incident-management|Quản lý sự cố và Khôi phục]]: Ứng cứu sự cố và khôi phục sau thảm họa.
* [[security-operations-center|Trung tâm Điều hành An ninh (SOC)]]: Giám sát, phát hiện và phản ứng sự cố 24/7.

## Các mối đe dọa phổ biến (Common Threats)
* [[distributed-denial-of-service|Tấn công từ chối dịch vụ phân tán (DDoS)]]: Làm tràn ngập mục tiêu bằng lưu lượng từ botnet.
* [[ransomware|Mã độc tống tiền (Ransomware)]]: Mã hóa dữ liệu để tống tiền.
* [[advanced-persistent-threat|Mối đe dọa thường trực nâng cao (APT)]]: Các chiến dịch tấn công dài hạn và tinh vi.
* [[insider-threat|Mối đe dọa từ nội bộ (Insider Threat)]]: Nguy cơ đến từ những người có quyền truy cập hợp lệ.
* [[social-engineering|Tấn công kỹ thuật xã hội (Social Engineering)]]: Thao túng tâm lý để đánh lừa nạn nhân.
* [[server-side-request-forgery|Giả mạo yêu cầu phía máy chủ (SSRF)]]: Coi máy chủ là bàn đạp tấn công.
* [[link-following|Theo dõi liên kết (Link Following)]]: Khai thác symlinks và hard links.

## Kiểm thử xâm nhập (Penetration Testing)
* [[penetration-testing|Kiểm thử xâm nhập]]: Tổng quan về khái niệm và quy trình 8 giai đoạn.
* [[pentest-pre-engagement|Giai đoạn Tiền dự án]]: Các yêu cầu về pháp lý, phạm vi và quy tắc thực thi.
* [[information-gathering|Thu thập thông tin]]: Giai đoạn thu thập dữ liệu về mục tiêu và lập bản đồ bề mặt tấn công.
* [[vulnerability-assessment|Đánh giá lỗ hổng]]: Phân tích dữ liệu thu thập để xác định các điểm yếu và "low-hanging fruits".
* [[memory-safety-vulnerabilities|Lỗ hổng an toàn bộ nhớ]]: Tổng quan về các lỗi quản lý bộ nhớ (CWE-787, CWE-416).
* [[path-traversal|Duyệt đường dẫn (Path Traversal)]]: Lỗ hổng truy cập file trái phép (CWE-22).
* [[os-command-injection|Tiêm lệnh hệ điều hành (OS Command Injection)]]: Lỗ hổng thực thi lệnh trái phép (CWE-78).
* [[use-after-free|Sử dụng sau khi giải phóng (Use After Free)]]: Lỗ hổng quản lý bộ nhớ (CWE-416).
* [[osint|OSINT]]: Thu thập thông tin từ các nguồn công khai (Social Media, GitHub, v.v.).
* [[network-scanning|Quét mạng và dịch vụ]]: Sử dụng Nmap để xác định các cổng mở và dịch vụ đang chạy.

### Kiểm thử mục tiêu Linux (Linux Pentesting)
* [[linux-information-gathering|Thu thập thông tin Linux]]: Khai thác FTP ẩn danh và quét WordPress.
* [[linux-initial-access|Truy cập ban đầu Linux]]: Khai thác RCE qua plugin và sử dụng khóa SSH.
* [[linux-system-enumeration|Liệt kê hệ thống Linux]]: Sử dụng LinPEAS để khám phá nội bộ.
* [[linux-vulnerability-assessment|Đánh giá lỗ hổng Linux]]: Phân tích Kernel và quyền Sudo.
* [[linux-privilege-escalation|Leo thang đặc quyền Linux]]: Kỹ thuật GTFObins và sudo su.
* [[linux-pillaging|Vét cạn dữ liệu Linux]]: Trích xuất khóa SSH root và thông tin nhạy cảm.

### Kiểm thử mục tiêu Windows (Windows Pentesting)
* [[windows-information-gathering|Thu thập thông tin Windows]]: Thăm dò SMB, RDP và xác định phiên bản Gitea.
* [[windows-initial-access|Truy cập ban đầu Windows]]: Khai thác Gitea RCE và Password Reuse.
* [[windows-system-enumeration|Liệt kê hệ thống Windows]]: Kiểm tra quyền hạn (SeImpersonate) và WinPEAS.
* [[windows-vulnerability-assessment|Đánh giá lỗ hổng Windows]]: Phân tích cấu hình sai và tác vụ lập lịch.
* [[windows-privilege-escalation|Leo thang đặc quyền Windows]]: Hijacking script và thêm người dùng vào Administrators.
* [[windows-pillaging|Vét cạn dữ liệu Windows]]: Trích xuất dữ liệu khách hàng (PII) và tuân thủ GDPR.

### Tài liệu và Báo cáo (Reporting)
* [[proof-of-concept|Bằng chứng khai thác (PoC)]]: Cách ghi chép và tái hiện lỗ hổng kỹ thuật.
* [[pentest-documentation|Báo cáo dự án (Documentation)]]: Cấu trúc báo cáo chuẩn và các thành phần chính.
* [[pentest-reporting|Trình bày kết quả (Reporting)]]: Quy trình họp báo cáo và lập kế hoạch khắc phục.
* [[pentest-recommendations|Lời khuyên cho Pentester]]: Tư duy, kỷ luật và phương pháp rèn luyện nghề nghiệp.

## Thành phần và Giao tiếp (Components & Communication)
* [[network-hardware|Thiết bị và Phần cứng]]: Các thiết bị đầu cuối, trung gian và máy chủ.
* [[addressing-and-routing|Định danh và Truyền thông]]: Tổng quan về Tầng Mạng, IP, MAC và Cổng.
* [[mac-address|Địa chỉ MAC]]: Cấu trúc địa chỉ vật lý và các vector tấn công.
* [[ipv4-address|Địa chỉ IPv4]]: Cấu trúc 32 bit, CIDR và các địa chỉ đặc biệt.
* [[ipv6-address|Địa chỉ IPv6]]: Thế hệ IP mới 128 bit, quy tắc rút gọn và SLAAC.
* [[subnetting|Chia mạng con (Subnetting)]]: Kỹ thuật chia dải mạng và tính toán host.
* [[arp-protocol|Giao thức ARP]]: Cơ chế phân giải địa chỉ và tấn công ARP Spoofing.

## Dịch vụ và Địa chỉ (Services & Addressing)
* [[dhcp-service|Dịch vụ DHCP]]: Tự động cấu hình địa chỉ IP.
* [[dns-service|Hệ thống DNS]]: Phân giải tên miền thành địa chỉ IP.
* [[nat-service|Dịch vụ NAT]]: Biên dịch địa chỉ mạng và chia sẻ IP công cộng.

## Kiến thức Linux (Linux Fundamentals)
* [[linux-fundamentals|Kiến thức cơ bản]]: Lịch sử, triết lý và thành phần hệ thống.
* [[linux-architecture|Kiến trúc Linux]]: Các lớp phần cứng, hạt nhân và vỏ.
* [[linux-file-system|Hệ thống tệp tin]]: Cấu trúc thư mục FHS.
* [[linux-shell|Linux Shell]]: Giao diện dòng lệnh và trình giả lập.
* [[linux-shortcuts|Phím tắt Linux]]: Các phím tắt tăng tốc làm việc trên dòng lệnh.
* [[linux-shell-help|Nhận trợ giúp]]: Cách dùng man, help và apropos.
* [[linux-man-pages|Trang hướng dẫn (Man Pages)]]: Cấu trúc 8 phần của hệ thống tài liệu Linux.
* [[linux-prompt|Dòng nhắc lệnh]]: Tìm hiểu về cấu trúc prompt và biến PS1.
* [[linux-system-info|Thông tin hệ thống]]: Các lệnh thu thập thông tin cơ bản.
* [[linux-distributions|Các bản phân phối]]: Debian, Ubuntu, Parrot OS và hơn thế nữa.
* [[solaris|Hệ điều hành Solaris]]: Hệ điều hành Unix doanh nghiệp từ Sun/Oracle.

## Luồng công việc Linux (Linux Workflow)
* [[linux-navigation|Điều hướng]]: Di chuyển và liệt kê với cd, ls, pwd.
* [[linux-file-management|Quản lý tệp tin]]: Tạo, xóa, sao chép và di chuyển.
* [[linux-permissions|Quyền hạn]]: chmod, chown, SUID/SGID và Sticky Bit.
* [[linux-editing-files|Chỉnh sửa tệp]]: Sử dụng Nano và Vim.
* [[linux-redirections|Chuyển hướng và Đường ống]]: FD, >, <, | và xử lý luồng I/O.
* [[linux-filtering|Lọc nội dung]]: grep, awk, sed, cut và xử lý văn bản.
* [[linux-searching|Tìm kiếm]]: find, locate và định vị tài nguyên.
* [[linux-regex|Biểu thức chính quy]]: Kỹ thuật RegEx trong dòng lệnh.

## Quản trị Hệ thống Linux (System Management)
* [[linux-user-management|Quản lý Người dùng]]: Tạo user, nhóm và quyền sudo.
* [[linux-package-management|Quản lý Gói]]: Cài đặt và duy trì phần mềm với APT, DPKG và Git.
* [[linux-service-process-management|Dịch vụ và Tiến trình]]: Quản lý daemons, PID và tín hiệu kill.
* [[linux-task-scheduling|Lập lịch Tác vụ]]: Tự động hóa công việc với Cron và Systemd Timers.
* [[linux-file-system-management|Lưu trữ và Hệ thống tệp]]: Quản lý đĩa, inodes và mounting.
* [[linux-backup-restore|Sao lưu và Phục hồi]]: Sử dụng Rsync, SSH và tự động hóa sao lưu.
* [[linux-network-configuration|Cấu hình Mạng]]: Quản lý giao diện, địa chỉ IP và định tuyến.
* [[linux-network-services|Dịch vụ Mạng]]: Cấu hình SSH, NFS, Web Server và VPN.
* [[remote-desktop-protocols|Giao thức Điều khiển Từ xa]]: RDP, VNC và X11 Forwarding.
* [[linux-web-services|Dịch vụ Web Nâng cao]]: Quản trị Apache và các công cụ cURL/Wget.
* [[linux-containerization|Đóng gói (Containers)]]: Công nghệ Docker và LXC.
* [[linux-hardening|Tăng cường Bảo mật]]: Các biện pháp và cơ chế MAC (SELinux, AppArmor).
* [[linux-firewall|Tường lửa Linux]]: Cấu hình Iptables và các giải pháp firewall.
* [[linux-logging|Ghi nhật ký hệ thống]]: Theo dõi và phân tích log trong /var/log.
