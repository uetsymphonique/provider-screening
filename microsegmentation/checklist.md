## Checklist đánh giá sản phẩm phục vụ microsegmentation

### 1. Visibility & Mapping
+ Tự động khám phá luồng dữ liệu thời gian thực (Real-time
Auto-discovery).
+ Hiển thị sơ đồ kết nối trực quan theo App, Environment,
Role, Process.
+ Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết
forensic.
+ Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context)
trực tiếp trên map.
+ Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn
(Unrecognized Traffic).

### 2. Policy Management
+ Tạo chính sách dựa trên Tag/Label/Identity (không phụ
thuộc IP/VLAN).
+ Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning
(Rule Recommendation).
+ Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation /
Dry-run).
+ Khả năng khôi phục chính sách tức thì (Instant 1-Click
Rollback).
+ Hỗ trợ chính sách phân cấp (Inherited & Hierarchical
Rules).

### 3. Architecture & Support
+ Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux
RHEL/CentOS/Ubuntu, AIX, Solaris.
+ Hỗ trợ Container / Kubernetes / OpenShift native isolation.
+ Hỗ trợ cả giải pháp Agent-based và Agentless/Network
Integration.
+ Tương thích môi trường cách ly hoàn toàn không có
Internet (Air-gapped Network).
+ Khả năng mở rộng (Scalability) lên tới trên 50,000
Workloads tập trung.

### 4. Performance & Impact
+ Mức độ tiêu tốn tài nguyên Agent: CPU < 1%, RAM <
100MB.
+ Không làm tăng độ trễ mạng (< 0.1ms network latency).
+ Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng
giữ nguyên không bị gián đoạn.
+ Cài đặt và cập nhật Agent không yêu cầu Reboot Server.

### 5. Integration & Automation
+ Full RESTful API hỗ trợ 100% chức năng quản trị.
+ Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel)
qua Syslog/CEF/API.
+ Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin
nhãn (Tags).
+ Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho
DevSecOps.

### 6. Security & Compliance
+ Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level
enforcement).
+ Tích hợp Threat Intelligence & Mánh dối (Honeypot/
Deception detection).
+ Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST
800-207, ISO 27001, IEC 62443.
+ Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 /
Mutual Auth).

### 7. High Availability
+ Kiến trúc Cụm Controller hỗ trợ High Availability (ActiveActive / Active-Passive).
+ Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn
tiếp tục thực thi Policy (Autonomous Mode).
+ Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery
site sync).

### 8. Standards Certification
+ Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3,
Common Criteria EAL4+.
+ Chứng nhận tương thích phần mềm công nghiệp từ
Siemens, Honeywell, ABB (cho OT).
