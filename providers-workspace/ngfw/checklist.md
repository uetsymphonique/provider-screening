## Checklist đánh giá sản phẩm phục vụ Next-Generation Firewall (NGFW)

### 1. Architecture & Policy (Kiến trúc & Chính sách Firewall)
+ Kiểm soát chính sách theo ứng dụng lớp 7 (App-ID / Application-based Policy
Control), nhận diện độc lập với cổng/giao thức truyền tải.
+ Phân vùng bảo mật (Security Zone) theo interface vật lý/logic, mỗi zone
quản lý chính sách, log và thống kê riêng.
+ Chính sách dựa trên danh tính người dùng (Identity-based Policy): tích hợp
AD/LDAP/RADIUS, hỗ trợ xác thực agentless không cần cài đặt client riêng.
+ Hỗ trợ đa dạng phương thức NAT (SNAT, DNAT, NAT64, ...) và đối tượng địa
chỉ động theo tên miền (FQDN object).
+ Chế độ triển khai linh hoạt: Transparent/Bridge mode không yêu cầu thay
đổi cấu hình mạng hiện có, và Router/L3 mode.

### 2. Threat Prevention (Ngăn chặn Mối đe dọa)
+ IPS phát hiện và chặn tấn công dựa trên signature, phân tích giao thức và
bất thường lưu lượng (protocol/traffic anomaly).
+ Chống tấn công từ chối dịch vụ (Anti-DDoS): phát hiện và chặn
TCP/UDP/ICMP/HTTP/DNS/SIP flooding.
+ Antivirus / Anti-malware tích hợp inline, quét payload thời gian thực.
+ Sandbox nội bộ hoặc tích hợp Cloud Sandbox để phân tích file trong môi
trường cách ly, phát hiện mối đe dọa zero-day (Advanced Threat Protection).
+ Cập nhật signature / threat intelligence tự động, thời gian thực, không
yêu cầu khởi động lại thiết bị.

### 3. Content & Application Inspection (Kiểm tra Nội dung & Ứng dụng)
+ Giải mã SSL/TLS tự động, hỗ trợ loại trừ chọn lọc theo nguồn/đích/dịch vụ
(SSL Inspection with selective bypass).
+ Kiểm soát ứng dụng cho các dịch vụ rủi ro cao: P2P, IM, webmail, proxy
bypass, remote access tools.
+ Lọc Web/URL dựa trên cơ sở dữ liệu phân loại được cập nhật định kỳ.
+ Lọc DNS / chặn truy vấn tới tên miền độc hại đã biết.
+ Chống rò rỉ dữ liệu (DLP): nhận diện và chặn nội dung nhạy cảm theo từ
khóa, mẫu định danh, hoặc regex tùy biến.

### 4. VPN & Secure Connectivity (VPN & Kết nối An toàn)
+ IPsec VPN tuân thủ chuẩn, hỗ trợ cả IKEv1 và IKEv2.
+ SSL VPN cho truy cập từ xa (remote access), qua client hoặc clientless.
+ Sẵn sàng Mật mã Hậu lượng tử (Post-Quantum Cryptography) cho kênh VPN, độc
lập hoặc kết hợp với thuật toán truyền thống (Hybrid PQC).
+ Zero Trust Network Access (ZTNA) tích hợp sẵn trong hệ điều hành firewall,
kiểm soát truy cập theo danh tính mà không phụ thuộc hoàn toàn vào VPN
truyền thống.

### 5. Performance & High Availability (Hiệu năng & Sẵn sàng cao)
+ Băng thông xử lý Firewall (FW Throughput) ở cấu hình entry-level tối
thiểu ≥ 4 Gbps.
+ Băng thông xử lý VPN (VPN Throughput) ở cấu hình entry-level tối thiểu ≥
1.5 Gbps.
+ Cụm dự phòng cao (HA Active-Standby hoặc Active-Active): failover tự động
không làm gián đoạn phiên (session) đang chạy.
+ Hỗ trợ gộp liên kết mạng (Link Aggregation / Line Bonding, ví dụ 802.3ad
LACP) và giao thức dự phòng định tuyến (VRRP hoặc tương đương).

### 6. Management & Compliance (Quản trị & Tuân thủ)
+ Quản trị qua GUI web và CLI (SSH/Telnet), cung cấp REST API đầy đủ cho tự
động hóa.
+ Tích hợp SIEM/SOAR: đẩy log thời gian thực dạng Syslog/CEF qua kênh mã
hóa.
+ Phân quyền quản trị theo vai trò (RBAC): tách biệt admin hệ thống, admin
chính sách và auditor an ninh.
+ Đa miền ảo hóa (Virtual Domain/VDOM) hoặc cơ chế multi-tenancy tương
đương, cho phép cấu hình định tuyến và thống kê độc lập theo miền.
+ Đạt chứng nhận bảo mật quốc tế (Common Criteria EAL4+, FIPS 140-2/140-3
hoặc tương đương) và có sẵn báo cáo tuân thủ theo chuẩn ngành (ISO 27001,
PCI-DSS, NIST).
