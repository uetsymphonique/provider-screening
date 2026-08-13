# Microsegmentation Product Assessment: Versa Networks - Versa Secure SD-WAN / SASE (VersaONE Universal SASE Platform)

**Product ID:** `versa-secure-sd-wan-sase`
**Version reference:** VOS Release 23.1.x docs era (docs.versa-networks.com, retrieved 2026-08-10)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T16:30:00Z
**Total evidence items collected:** 78
**Total distinct sources:** 48

---

## 1. Overview

Versa Networks delivers microsegmentation as a software-defined, network-centric capability of the Versa Operating System (VOS) that runs across its Secure SD-WAN edge, Secure SD-LAN switching, and VersaONE Universal SASE (Versa SASE client / Secure Access ZTNA) deployments [1][2]. Administrators create microsegments by defining policies whose match criteria place users and devices into segments using users/groups, endpoint information profiles (EIPs), IoT device fingerprints, MAC addresses, and scalable group tags (SGTs); enforcement happens in the NPU and NGFW data plane, and microsegments can be associated with NPU ACL and NGFW security rules [1]. Clientless IoT/OT devices are handled agentlessly through automated device fingerprinting, while endpoints run the Versa SASE client, so both agent-based and agentless shapes are supported [2][25]. The platform is orchestrated by Versa Director/Concerto, with Versa Analytics clusters providing per-tenant dashboards, maps, flow retention, and reporting [14][30]. The GigaOm Radar for SASE classifies Versa as a Leader and Outperformer in the SASE market [44].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 14    | 1                | 13     | 0   |
| partial          | 11    | 0                | 11     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 3 items backed by ≥ 2 source_types; 23 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | Versa automatically identifies endpoints via SASE client, MDM/UEM and gateway telemetry fingerprinting, and VOS IoT security discovers and identifies devices as they enter network traffic. [1], [6], [25] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Analytics dashboards render charts, maps and tables per tenant, site and time period, including a Sites Map dashboard; views are organized by site, application and security category rather than by App/Environment/Role/Process taxonomy. [14], [30] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 90 days | Versa Analytics NoSQL datastores retain daily performance and fault data for three months (90 days) by default, retention is configurable per log type, and archived logs can be restored for forensics. [22], [23] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (Security dashboards show vulnerability statistics but not CVE context overlaid on the connection map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Analytics traffic dashboards report unknown TCP/UDP/SSL traffic and unknown traffic summaries, IoT devices with threats are tracked, and unrecognized endpoints are fingerprinted via gateway telemetry. [6], [30], [41] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Microsegmentation policy rules match on users and groups, endpoint information profiles (EIPs), IoT device fingerprints and MAC addresses and assign scalable group tags (SGTs), making policy identity- and tag-based rather than IP/VLAN-dependent. [1], [2] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | - | Versa Advanced Networking Insights provides AI-powered signal prediction, anomaly detection and UEBA, and VersaAI embeds ML and LLM workflows, but no automatic security-policy rule recommendation feature is documented. [32], [34] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | - | no evidence found |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | Versa Director auto-creates up to 10 template snapshots per deploy that can be compared and restored, and Director node snapshots support rollback of software and configuration; this is version rollback rather than an instant one-click policy rollback. [18], [20] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | VOS multitenancy builds parent-organization to tenant hierarchies with unique device groups and templates per service definition, and SD-LAN microsegmentation applies a uniform policy language across LAN, WAN and cloud edges. [2], [43] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The Versa SASE client supports Windows Server 2012 R2/2016/2019, Windows 10/11, Linux (Debian 10+/Ubuntu 18.04+, Fedora 34+/RHEL8+/CentOS8+), macOS, Android and iOS; no AIX/Solaris or Windows Server 2003/2008/2022 support is documented. [36] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | Microsegmentation supports agent-based Versa SASE clients via EIP data and agentless clientless IoT/OT devices via automated device fingerprinting, with 802.1X and MAC-bypass placement on SD-LAN. [1], [2], [25] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | Versa offline ATP and offline CASB/DLP profiles provide AI/ML, sandbox, reputation and signature-based detection without cloud submission of every file, but full air-gapped operation of Director, Controller and Analytics nodes is not documented. [16] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Sources describe the solution scaling to many thousands of CPE devices with up to 1024 tenants per Director and call the platform highly scalable, but no workload-count capacity figure is published against the 50,000-workload threshold. [35], [43], [45] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | - | no evidence found |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | - | no evidence found |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Versa states microsegmentation runs at wire rate on SD-LAN ASICs with traffic on the switched path at line rate, but no numeric forwarding-latency figure is published to verify the 0.1 ms threshold. [2], [27] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | Enforcement is network-resident: the VOS forwarding plane stays up for up to 8 hours when Controller nodes are unreachable via graceful restart, and the SASE client monitors underlay changes and reconnects on keepalive failure; no explicit agent fail-open guarantee is documented. [35], [36], [37] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | - | Versa Director exposes REST API categories covering VNMS workflows, dashboards, device-level and template-level VOS configuration and request commands, protected by username/password or OAuth tokens. [11] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Versa Analytics can stream alarm, event and threat logs to Splunk in syslog key-value pair format, providing SIEM integration; log-exporter rules also support remote collectors. [7] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | The terraform-provider-versa plugin provides CRUD control over Versa resources via Director and Concerto APIs, and the integration supports terraform apply --auto-approve for CI/CD deployment of security policies. [15] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | The SASE client's application-based split tunnel includes or excludes traffic from specific Windows processes or applications, providing per-process traffic policy on endpoints, but deep process-level enforcement across servers is not documented. [36] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | A threat intelligence microservice consumes external IP/port/domain/URL feeds per tenant, and offline ATP adds AI/ML, sandbox and dynamic-analysis detection; no deception or honeypot capability is documented. [16], [17] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Versa documents PCI DSS, ISO/IEC 27001:2022, SOC 2 Type 2, HIPAA, FIPS 140-2 and CC EAL4+ certifications and DISA Thunderdome zero-trust alignment; explicit NIST 800-207 and IEC 62443 compliance reports are not evidenced. [24], [28], [29] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | - | SASE client-to-gateway registration uses TLS with server-certificate validation followed by client authentication, and Versa Director supports mutual TLS (mTLS) with X.509 client certificates. [12], [48] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | Multiple SD-WAN Controller nodes can be deployed for high availability, VOS Elastic Services Clusters scale service and IO planes across nodes, and interchassis active/standby pairs provide stateful HA at branches and hubs. [9], [10], [35] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | With graceful restart enabled by default, the Controller retains MP-BGP routes for up to 8 hours, keeping the forwarding plane up even when Controller nodes are unreachable, and redundant Controllers further mitigate control-plane failure. [35] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | - | Secondary Analytics clusters operate in active-backup or active-active mode with automatic log failover and archived-log transfer between sites, and Director HA synchronizes backups and snapshots to the standby node. [18], [21] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Supported | high | - | NIST CMVP lists Versa modules validated under FIPS 140-2 (Versa Networks Controller certificate #4380, Branch #4379) and FIPS 140-3 (VOS OpenSSL FIPS Provider module #5161, Level 1), and Versa announced Common Criteria EAL4+ certification of VOS. [24], [46], [47] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found |

---

## 4. Notable Strengths

- **Identity- and tag-based policy (items 2.1, 3.3):** microsegmentation rules match users, EIP security-posture data, device fingerprints, and SGTs rather than IP/VLAN constructs, with both agent-based (SASE client) and agentless (fingerprinting, 802.1X, MAC-bypass) placement [1][2].
- **Auto-discovery and flow retention (items 1.1, 1.3, 1.5):** endpoints are continuously fingerprinted across SASE client, MDM/UEM, and gateway telemetry, unknown TCP/UDP/SSL traffic is surfaced in Analytics dashboards, and NoSQL datastores retain daily data for 90 days by default with configurable per-log-type retention [6][23][30].
- **Controller and data-plane resilience (items 7.1, 7.2, 7.3):** multiple Controller nodes provide HA, graceful restart keeps the forwarding plane up for up to 8 hours when Controllers are unreachable, interchassis active/standby pairs provide stateful HA, and secondary Analytics clusters add active-backup/active-active log collection [21][35].
- **Automation and integration breadth (items 5.1, 5.2, 5.4):** Versa Director exposes REST API categories for workflows, dashboards, and device/template configuration; Analytics streams alarm/event/threat logs to Splunk in syslog key-value format; and terraform-provider-versa supports CI/CD policy deployment [7][11][15].
- **Security certifications (item 8.1):** NIST CMVP lists VOS modules under FIPS 140-2 (Controller #4380, Branch #4379) and FIPS 140-3 (module #5161, Level 1), and Versa announced Common Criteria EAL4+ certification of VOS [24][46][47].

## 5. Notable Gaps / Risks

- **No measured agent-overhead numbers (items 4.1, 4.2, 4.3):** no CPU%, RAM MB, or forwarding-latency figures are published for the SASE client or VOS enforcement path; only qualitative wire-rate/line-rate claims exist, so the sub-1% CPU, sub-100 MB RAM, and sub-0.1 ms latency thresholds cannot be verified.
- **Workload-scale claim not quantified (item 3.5):** sources describe scaling to "many thousands of CPE devices" and 1024 tenants per Director, but no per-controller workload-count capacity is published, leaving the 50,000-workload requirement unconfirmed.
- **Policy management ergonomics missing (items 2.3, 2.4):** no policy simulation/dry-run mode is documented, and rollback is limited to template/Director snapshots rather than an instant one-click policy rollback.
- **Operational integration gaps (items 1.4, 5.3, 3.2):** no CVE context is shown directly on the map, no ServiceNow/CMDB tag sync is documented, and no native Kubernetes/OpenShift isolation is evidenced.
- **Server and OT coverage limits (items 3.1, 6.1, 6.2, 6.3, 8.2):** the client's server-OS coverage stops at Windows Server 2019 (no 2003/2008/2022, AIX, Solaris), process-level enforcement is limited to client split-tunnel rules, no deception capability is documented, NIST 800-207/IEC 62443 reports are not evidenced, and no Siemens/Honeywell/ABB OT certifications were found.

## 6. Evidence Quality Notes

78 evidence entries across 48 staged sources support the 33 items (14 supported, 11 partial, 8 unknown, 0 not_supported). Only item 8.1 reaches high confidence, triangulated through independent NIST CMVP registry pages [46][47] plus a vendor press release [24]; everything else is capped at medium because 43 of 48 sources are vendor documentation. Item 3.5 is the only item using a non-vendor human source (PeerSpot community reviews [45]) in addition to vendor docs, and item 4.3 leans on a vendor blog [27]; both remain partial because the evidence is qualitative. No source contradictions were found; conservative verdicts (partial rather than supported) were chosen wherever the only evidence was qualitative or where a feature (CVE-on-map, policy simulation, ServiceNow sync, deception, OT certifications) had no documentation at all.

Independent corroboration was limited by network conditions: general search engines, the Common Criteria portal, and Reddit were bot-blocked from this environment, so discovery relied on the Versa docs sitemap, the Versa corporate sitemap, the NIST CMVP search/registry, and PeerSpot. The Common Criteria EAL4+ claim therefore rests on Versa's own press release [24] rather than the CCRA registry, and several certification-registry and analyst-report checks (GigaOm full report [44] is vendor-hosted) could not be performed directly; re-validation against the Common Criteria portal and the GigaOm/Frost & Sullivan originals is recommended before procurement decisions.

---

## Bibliography

[1] Versa Networks. "Configure Microsegmentation (Versa Secure SD-WAN docs)". https://docs.versa-networks.com/Secure_SD-WAN/01_Configuration_from_Director/Security_Configuration/Configure_Microsegmentation (Retrieved: 2026-08-10T16:30:00Z)
[2] Versa Networks. "Configure Microsegmentation for SD-LAN (Versa docs)". https://docs.versa-networks.com/Secure_SD-LAN/Configuration_from_Director/Configure_Microsegmentation_for_SD-LAN (Retrieved: 2026-08-10T16:30:00Z)
[3] Versa Networks. "FIPS Compliance (Versa Secure SD-WAN docs)". https://docs.versa-networks.com/Secure_SD-WAN/01_Configuration_from_Director/Security_Configuration/FIPS_Compliance (Retrieved: 2026-08-10T16:30:00Z)
[4] Versa Networks. "Configure EIP-Based Microsegmentation for SD-LAN (Versa docs)". https://docs.versa-networks.com/Secure_SD-LAN/Configuration_from_Director/Configure_EIP-Based_Microsegmentation_for_SD-LAN (Retrieved: 2026-08-10T16:30:00Z)
[5] Versa Networks. "Manage Versa Analytics Log Archives (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Configuration/Manage_Versa_Analytics_Log_Archives (Retrieved: 2026-08-10T16:30:00Z)
[6] Versa Networks. "Device Fingerprinting for Zero Trust Access (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Director/Versa_SASE_Client/Device_Fingerprinting_for_Zero_Trust_Access (Retrieved: 2026-08-10T16:30:00Z)
[7] Versa Networks. "Integrate Splunk with Versa Analytics (Versa docs)". https://docs.versa-networks.com/Integrations_and_Solutions/Integrations/SIEM/Integrate_Splunk_with_Versa_Analytics (Retrieved: 2026-08-10T16:30:00Z)
[8] Versa Networks. "Configure Vulnerability Rules (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Director/Configuration/Configure_Vulnerability_Rules (Retrieved: 2026-08-10T16:30:00Z)
[9] Versa Networks. "Configure Stateful Interchassis HA (Versa docs)". https://docs.versa-networks.com/Secure_SD-WAN/01_Configuration_from_Director/Common_Configuration/Configure_Stateful_Interchassis_HA (Retrieved: 2026-08-10T16:30:00Z)
[10] Versa Networks. "Versa Networks Elastic Services Cluster (Versa docs)". https://docs.versa-networks.com/Reference/Architecture/Versa_Networks_Elastic_Services_Cluster (Retrieved: 2026-08-10T16:30:00Z)
[11] Versa Networks. "Versa Director REST API Overview (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Director/Director_REST_APIs/Versa_Director_REST_API_Overview (Retrieved: 2026-08-10T16:30:00Z)
[12] Versa Networks. "Secure Communication for SD-WAN Devices and SASE Clients (Versa docs)". https://docs.versa-networks.com/Reference/Architecture/Secure_Communication_for_SD-WAN_Devices_and_SASE_Clients (Retrieved: 2026-08-10T16:30:00Z)
[13] Versa Networks. "Install and Configure Versa SASE Clients (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Director/Versa_SASE_Client/Install_and_Configure_Versa_SASE_Clients (Retrieved: 2026-08-10T16:30:00Z)
[14] Versa Networks. "SD-WAN Dashboards (Versa Analytics docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Monitoring_with_Versa_Analytics/SD-WAN_Dashboards (Retrieved: 2026-08-10T16:30:00Z)
[15] Versa Networks. "Terraform Integration (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Concerto/Terraform_Integration (Retrieved: 2026-08-10T16:30:00Z)
[16] Versa Networks. "Configure Offline Advanced Threat Protection (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Concerto/Configure_Offline_Advanced_Threat_Protection (Retrieved: 2026-08-10T16:30:00Z)
[17] Versa Networks. "Configure Threat Intelligence from VMS (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Messaging_Service_(VMS)/Installation_and_Initial_Configuration/Configure_Threat_Intelligence_from_VMS (Retrieved: 2026-08-10T16:30:00Z)
[18] Versa Networks. "Back Up and Restore a Director Node (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Director/Configuration/Back_Up_and_Restore_a_Director_Node (Retrieved: 2026-08-10T16:30:00Z)
[19] Versa Networks. "Configure the Analytics Storage Resource Handler (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Configuration/Configure_the_Analytics_Storage_Resource_Handler (Retrieved: 2026-08-10T16:30:00Z)
[20] Versa Networks. "Manage Template Snapshots (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Director/Configuration/manage_template_snapshots (Retrieved: 2026-08-10T16:30:00Z)
[21] Versa Networks. "Configure a Secondary Cluster for Log Collection (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Configuration/Configure_a_Secondary_Cluster_for_Log_Collection (Retrieved: 2026-08-10T16:30:00Z)
[22] Versa Networks. "Versa Analytics Configuration Concepts (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Configuration/01_Versa_Analytics_Configuration_Concepts (Retrieved: 2026-08-10T16:30:00Z)
[23] Versa Networks. "Versa Analytics Scaling Recommendations (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Configuration/Versa_Analytics_Scaling_Recommendations (Retrieved: 2026-08-10T16:30:00Z)
[24] Versa Networks. "Versa Achieves Common Criteria EAL4+ Certification (press release)". https://versa-networks.com/news/2023/versa-networks-achieves-common-criteria-eal4-certification-further-validating-the-security-and-controls-of-its-sase-and-secure-sd-wan-operating-system/ (Retrieved: 2026-08-10T16:30:00Z)
[25] Versa Networks. "Microsegmentation (Versa Networks solution page)". https://versa-networks.com/solutions/microsegmentation/ (Retrieved: 2026-08-10T16:30:00Z)
[26] Versa Networks. "Versa Networks Achieves FIPS 140-2 Security Certification (press release)". https://versa-networks.com/news/2023/versa-networks-achieves-fips-140-2-security-certification/ (Retrieved: 2026-08-10T16:30:00Z)
[27] Versa Networks. "The Need for Software Defined Adaptive Micro-Segmentation (Versa blog)". https://versa-networks.com/blog/the-need-for-software-defined-adaptive-micro-segmentation/ (Retrieved: 2026-08-10T16:30:00Z)
[28] Versa Networks. "Versa Networks Certifications and Compliance". https://versa-networks.com/certificates/ (Retrieved: 2026-08-10T16:30:00Z)
[29] Versa Networks. "Versa Selected for DISA Thunderdome (press release)". https://versa-networks.com/news/versa-networks-selected-to-provide-sd-wan-zero-trust-access-and-customer-edge-security-stack-cess-for-disas-thunderdome-program/ (Retrieved: 2026-08-10T16:30:00Z)
[30] Versa Networks. "Overview of Analytics Dashboards, Log Screens, and Reports (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Monitoring_with_Versa_Analytics/01Overview_of_Analytics_Dashboards%2C_Log_Screens%2C_and_Reports (Retrieved: 2026-08-10T16:30:00Z)
[31] Versa Networks. "Configure Firewalls (NGFW) (Versa docs)". https://docs.versa-networks.com/Next_Gen_Firewall/SD_Security/Configuration_from_Director/Configure_Firewalls_(NGFW) (Retrieved: 2026-08-10T16:30:00Z)
[32] Versa Networks. "VersaAI: AI Driven Security and Networking (Versa product page)". https://versa-networks.com/products/versaai/ (Retrieved: 2026-08-10T16:30:00Z)
[33] Versa Networks. "View Analytics Insights (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Monitoring_with_Versa_Analytics/View_Analytics_Insights (Retrieved: 2026-08-10T16:30:00Z)
[34] Versa Networks. "Versa Advanced Networking Insights Overview (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Configuration/Versa_Advanced_Networking_Insights_Overview (Retrieved: 2026-08-10T16:30:00Z)
[35] Versa Networks. "SD-WAN Solution Architecture (Versa docs)". https://docs.versa-networks.com/Reference/Architecture/02_SD-WAN_Solution_Architecture (Retrieved: 2026-08-10T16:30:00Z)
[36] Versa Networks. "Use the Versa SASE Client Application (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Director/Versa_SASE_Client/Use_the_Versa_SASE_Client_Application (Retrieved: 2026-08-10T16:30:00Z)
[37] Versa Networks. "Configure the Versa SASE Client To Select the Best Gateway (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Director/Versa_SASE_Client/Configure_Versa_SASE_Client_To_Select_the_Best_Gateway (Retrieved: 2026-08-10T16:30:00Z)
[38] Versa Networks. "Secure Control and Data Overlay Tunnel Solution (Versa docs)". https://docs.versa-networks.com/Reference/Architecture/Secure_Control_and_Data_Overlay_Tunnel_Solution (Retrieved: 2026-08-10T16:30:00Z)
[39] Versa Networks. "Troubleshoot the SASE Client (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Director/Versa_SASE_Client/Troubleshoot_the_SASE_Client (Retrieved: 2026-08-10T16:30:00Z)
[40] Versa Networks. "Configure Pre-Logon for the Versa SASE Client (Versa docs)". https://docs.versa-networks.com/Security_Service_Edge_(SSE)/Configuration_from_Director/Versa_SASE_Client/Configure_Pre-Logon_for_the_Versa_SASE_Client (Retrieved: 2026-08-10T16:30:00Z)
[41] Versa Networks. "Security Dashboards (Versa Analytics docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Analytics/Monitoring_with_Versa_Analytics/Security_Dashboards (Retrieved: 2026-08-10T16:30:00Z)
[42] Versa Networks. "View Security Analytics Data (Versa docs)". https://docs.versa-networks.com/Secure_SD-WAN/01_Configuration_from_Director/Security_Configuration/View_Security_Analytics_Data (Retrieved: 2026-08-10T16:30:00Z)
[43] Versa Networks. "Configure Multitenancy (Versa docs)". https://docs.versa-networks.com/Management_and_Orchestration/Versa_Director/Configuration/Configure_Multitenancy (Retrieved: 2026-08-10T16:30:00Z)
[44] GigaOm (hosted by Versa Networks). "GigaOm Radar for Secure Access Service Edge (SASE) - Versa report page". https://versa-networks.com/resources/reports/gigaom-radar-for-security-access-security-edge-sase/ (Retrieved: 2026-08-10T16:30:00Z)
[45] PeerSpot. "Versa Unified SASE Platform Reviews (PeerSpot)". https://www.peerspot.com/products/versa-unified-secure-access-service-edge-sase-platform-reviews (Retrieved: 2026-08-10T16:30:00Z)
[46] NIST. "NIST CMVP Certificate #5161 - Versa Operating System (VOS) Cryptographic Module". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5161 (Retrieved: 2026-08-10T16:30:00Z)
[47] NIST. "NIST CMVP Certificate #4380 - Versa Networks Controller". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4380 (Retrieved: 2026-08-10T16:30:00Z)
[48] Versa Networks. "Configure MTLS Certificate-Based Authentication (Versa docs)". https://docs.versa-networks.com/Secure_SD-WAN/01_Configuration_from_Director/Security_Configuration/Configure_MTLS_Certificate-Based_Authentication (Retrieved: 2026-08-10T16:30:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 48 (kept: 48, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 1, certification_registry: 2, community: 1, vendor_blog: 1, vendor_doc: 43
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
