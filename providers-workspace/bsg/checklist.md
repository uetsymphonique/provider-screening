## Checklist đánh giá sản phẩm phục vụ Bidirectional Security Gateway (BSG) / Cross Domain Solution

### 1. Architecture & Security (Kiến trúc & Bảo mật hệ thống)
+ Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại
phễu ranh giới, ngắt hoàn toàn IP routing.
+ Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách
biệt kết nối qua FPGA hoặc Shared Memory cách ly.
+ Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm
trong danh mục White-list.
+ Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS /
Microkernel / SELinux Strict Mode).
+ Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu
sạch trước khi cho phép phễu nội khởi tạo phiên mới.

### 2. Inspection & CDR Engine (Kiểm tra nội dung & CDR)
+ Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định
dạng Office (DOCX, XLSX), PDF, Image, CAD.
+ Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript,
DDE Links, Embedded Objects trong file.
+ Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus
quét song song payload thô.
+ Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu
trúc XML, JSON, FIXM, AIXM theo W3C Schema.
+ Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh
(Security Labels) gắn kèm tập tin.
+ Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND,
Tài khoản, Regex tùy biến.
+ Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên
trong file hình ảnh (PNG, JPEG, BMP).

### 3. Protocol Support (Hỗ trợ giao thức)
+ Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có
làm sạch nội dung.
+ Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3,
MQTT Industrial Proxy.
+ Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với
khả năng whitelist câu lệnh Query.
+ Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF
Unidirectional/Bidirectional Relay.

### 4. Performance & High Availability (Hiệu năng & Sẵn sàng cao)
+ Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế
≥ 1Gbps (hoặc theo tải dự án).
+ Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức
realtime ≤ 10ms.
+ Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố
trong thời gian ≤ 100ms không mất session.
+ Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close)
khi phần cứng bị tấn công từ chối dịch vụ DoS.

### 5. Management & Compliance (Quản trị & Tuân thủ)
+ Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin
Policy và Auditor An ninh.
+ Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã
hóa TLS tới SIEM.
+ Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST
SP 800-82, IEC 62443, ISO 27001.
+ Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+),
FIPS 140-3 hoặc Chứng nhận Cơ yếu.
