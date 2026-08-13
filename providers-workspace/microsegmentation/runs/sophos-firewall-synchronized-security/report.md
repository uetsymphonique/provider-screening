# Microsegmentation Product Assessment: Sophos - Sophos Firewall / Synchronized Security (SFOS with Sophos Central, Security Heartbeat, Synchronized Application Control, ZTNA)

**Product ID:** `sophos-firewall-synchronized-security`
**Version reference:** Sophos Firewall OS 20.0 webhelp (docs.sophos.com/nsg/sophos-firewall/20.0) + Sophos Central Admin customer help (current); CC cert covers SFOS 17.0; FIPS 140-2 cert #4100 covers SFOS 18.5; FIPS 140-3 mode in SFOS 20.0 MR1+
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T13:58:47Z
**Total evidence items collected:** 63
**Total distinct sources:** 53

---

## 1. Overview

Sophos Firewall (SFOS) is a next-generation network firewall whose "Synchronized Security" story ties it to microsegmentation: Security Heartbeat lets Intercept X-protected endpoints share a live health status with the firewall every 15 seconds over an encrypted TLS channel, and firewall rules can then allow or block traffic based on that health state to stop lateral movement [1][3]. Sophos Central (cloud) supplies centralized reporting (up to 365 days of log retention with the paid tier), management, configuration backup, Synchronized Application Control for endpoint application visibility, and a Zero Trust Network Access (ZTNA) gateway that is built into every centrally managed firewall [2][30][45]. The product therefore offers segmentation-adjacent capabilities enforced at the network gateway rather than per-workload agents: policy objects are zones, networks, services, users and health states, and ZTNA adds identity- and resource-based access with both agentless and agent-based modes [19][36]. Deployment shapes include hardware XGS appliances, virtual appliances (VMware, Hyper-V, KVM, Xen), and cloud instances (AWS, Azure), in active-passive or active-active HA pairs, and the firewall can be licensed to run fully air-gapped, though Synchronized Security and Central management are unsupported in that mode [14][15][23].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 7     | 2                | 5      | 0   |
| partial          | 18    | 0                | 17     | 1   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 9 items backed by ≥ 2 source_types; 15 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | - | The firewall shows live IPv4/IPv6 connection details per application, user and source IP, ships log data to Sophos Central at least every five minutes, and Security Heartbeat endpoints report health every 15 seconds; flow discovery is limited to traffic traversing the firewall or heartbeat-connected endpoints. [3], [7], [33], [48] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Dashboards, the Central Report Hub and live-connection views organize traffic by application, user, category and policy area with per-connection detail; no connection-map view organized by application, environment, role and process is documented. [7], [25], [32] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 365.0 days | Central Firewall Reporting Advanced retains firewall log data for up to 365 days with first-in-first-out rotation once storage is exhausted; the free tier keeps data only 7 days and the Xstream bundle 30 days. [30], [31] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (No evidence of vulnerability/CVE overlay on any map view.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | - | Unrecognized applications are surfaced in live connections and classified by Synchronized Application Control, and out-of-state packets are logged as invalid traffic events; detection applies to traffic seen at the firewall rather than workload-internal flows. [4], [7], [18] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | - | Firewall rules match on zones, networks, services, users and endpoint health status rather than tags or labels, and ZTNA policies are assigned to resources with identity-based conditions; no tag-based workload segmentation policy is documented. [1], [19], [36] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | - | no evidence found (No evidence of AI/ML-based policy recommendation.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | The Policy tester lets administrators test firewall rules, SSL/TLS inspection rules and web policies for a given URL, user, time, zone and source IP before and after editing, and an independent KB describes the same Policy Tester tool. [28], [52] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No evidence of instant one-click policy rollback.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | - | Firewall rules are evaluated top-down to the first match, with rule groups acting only as organizational containers; no inherited or hierarchical policy semantics are documented. [27] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | Sophos Intercept X agents support Windows (7/10/11), macOS, Linux and Windows Server 2008 R2 through 2022, with command-line installers for Windows documented by Sophos; no AIX or Solaris agent support is documented. [41], [44] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (No evidence of container/Kubernetes-native isolation.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | ZTNA supports both agentless (web apps) and agent-based (device-health-checked) policies, gateways can be on-premises VMs, Sophos Cloud gateways, or built into centrally managed SFOS devices, and endpoint protection runs an installed agent. [36], [37], [45] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | Sophos Firewall can be licensed and operated fully isolated from the internet via air-gap licenses with manual or automated pattern updates, but Synchronized Security and Sophos Central management are explicitly unsupported in air-gap deployments. [15] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | low | n/a (qualitative) | A PeerSpot user review reports that the bulk capacity of a device handles about 300 users and requests higher scalability thresholds; no controller architecture or 50,000-workload scale evidence exists. [48] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | No agent CPU percentage is published; a third-party reference notes user reports of noticeable performance overhead when the full MDR suite is enabled. [44] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | Only minimum host RAM requirements are published (4 GB for Windows endpoints, 2 GB for Intercept X Essentials); no agent memory-footprint figure is documented. [44] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | - | no evidence found (No published latency figures in milliseconds.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | By default endpoints that never sent a heartbeat are allowed access unless blocking options are enabled, while endpoints with a missing heartbeat are allowed or blocked per the configured policy; agent-failure behavior is therefore policy-driven rather than a documented fail-safe guarantee. [1], [19] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found (No evidence on whether agent install/update requires a reboot.) |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | Sophos Central exposes REST APIs, with roles up to a Super Admin service principal with full CRUD over users, endpoints, alerts and security settings, and the firewall itself offers a configuration API for add/update/delete; 100% parity with every admin-console function is not claimed. [21], [38] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Firewall syslog can be sent to up to five external servers (including TLS transport) for a SIEM or SOC, and Central Firewall Reporting supports simultaneous multi-destination forwarding, e.g. a local SIEM plus Sophos Central. [31], [51] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | - | A ServiceNow ITSM integration exists through Sophos Factory for pushing tickets and triggering automation; no CMDB tag-synchronization integration is documented. [46] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No evidence of CI/CD pipeline integrations (Jenkins, GitLab, Terraform).) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | Synchronized Application Control monitors and controls applications running on heartbeat-connected endpoints at the application level; process-level enforcement is not documented. [4] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Sophos X-Ops threat feeds push a SophosLabs-managed database of malicious IPs, domains and URLs to the firewall for blocking, and Active Threat Response automatically isolates and contains compromised devices; no honeypot or deception capability is documented. [29], [45] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | On-box compliance reports cover PCI, NERC CIP v3, HIPAA, GLBA, SOX, FISMA and CIPA; no NIST 800-207, ISO 27001 or IEC 62443 report templates are documented. [8] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | high | - | Endpoints and firewalls exchange Security Heartbeat over an encrypted TLS connection on port 8347 with Central-issued certificates, FIPS mode restricts TLS to 1.2 and 1.3, and CyberRatings independently tested the firewall's TLS/SSL 1.2 and 1.3 cipher handling. [3], [23], [47] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | Sophos Firewall supports HA clusters in active-passive and active-active modes with configuration and session synchronization between primary and auxiliary devices, and HA pairs can be formed and managed from Sophos Central. [11], [14], [34] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | The firewall remains licensed and functional when isolated from external networks (air-gap), indicating enforcement continues without Sophos Central, but no explicit autonomous-mode guarantee for agent-side policy execution is documented and cloud-managed features depend on connectivity. [15], [44] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Configuration backups can be saved to Sophos Central and restored from one firewall to another; no active disaster-recovery site synchronization is documented. [2], [22] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Supported | high | - | Sophos Firewall OS 17.0 holds a BSI Common Criteria certificate at EAL4 augmented by ALC_FLR.3 (BSI-DSZ-CC-1016-2020), the Sophos Cryptographic Module is NIST FIPS 140-2 validated (certificate #4100, now historical), and SFOS 20.0 MR1 and later support FIPS 140-3 Level 1 mode. [23], [42], [43] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (No evidence of industrial-software compatibility certifications from Siemens, Honeywell or ABB.) |

---

## 4. Notable Strengths

- **Health-based lateral-movement control (items 1.1, 2.1, 4.4, 6.4):** Security Heartbeat shares endpoint health with the firewall every 15 seconds over a certificate-authenticated TLS channel (port 8347), and rules can gate access on source/destination heartbeat status, blocking compromised endpoints [1][3][19].
- **Policy simulation before deploy (item 2.3):** the built-in Policy tester evaluates firewall, SSL/TLS inspection, and web policy matches for given URL/user/zone/source criteria before and after editing, corroborated by an independent KB [28][52].
- **Documented HA with both modes (item 7.1):** HA clusters run in active-passive or active-active mode with configuration and session synchronization, and HA pairs are manageable as a unit from Sophos Central [11][14][34].
- **Registry-level certifications (item 8.1):** Sophos Firewall OS 17.0 holds BSI Common Criteria EAL4+ (ALC_FLR.3), the Sophos Cryptographic Module is NIST FIPS 140-2 validated (cert #4100), and SFOS 20.0 MR1+ supports FIPS 140-3 Level 1 mode [42][43][23].
- **Long reporting history (item 1.3):** Central Firewall Reporting Advanced stores firewall log data for up to 365 days with FIFO rotation, meeting forensic-retention needs at the paid tier [30][31].

## 5. Notable Gaps / Risks

- **No tag/label-based workload segmentation (items 2.1, 6.1):** policy is expressed in zones, networks, services, users and health states, not workload tags, and endpoint control stops at the application level (Synchronized Application Control) rather than process level; a tag- or label-based policy engine would be required to meet the checklist's identity-centric model [19][4].
- **East-west visibility limited to the gateway (items 1.1, 1.2, 1.5):** flows are auto-discovered only when they traverse the firewall or involve heartbeat-connected endpoints, and there is no application/environment/role/process topology map; agent-based flow collection on every workload would close this gap [7][1].
- **Scale and agent-resource figures unavailable (items 3.5, 4.1, 4.2):** one PeerSpot review puts per-device capacity around 300 users with no controller architecture to reach 50,000 workloads, and Sophos publishes no agent CPU% or memory-footprint numbers, only host minimums (4 GB RAM) [48][44].
- **Unsupported checklist features are undecidable from public docs (items 2.2, 2.4, 3.2, 4.5, 5.4, 8.2):** no evidence was found for AI rule recommendation, one-click policy rollback, container/Kubernetes-native isolation, reboot-free agent updates, CI/CD integrations, or Siemens/Honeywell/ABB OT certifications; these are rated unknown pending vendor confirmation.
- **Air-gapped operation disables the synchronized features (item 3.4):** the firewall can run fully isolated with air-gap licenses, but Synchronized Security and Sophos Central management are explicitly unsupported there, so segmentation-relevant automation depends on internet connectivity [15].

## 6. Evidence Quality Notes

63 evidence entries were collected across 53 staged sources (41 vendor docs, 6 third-party reviews, 2 certification registries, 2 vendor blogs, 2 vendor datasheets). Nine items (1.1, 2.3, 3.1, 3.3, 5.2, 6.2, 6.4, 7.2, 8.1) cite at least two source types; 8.1 and 6.4 reach high confidence because they are backed by registries (Common Criteria portal, NIST CMVP) or an independent lab (CyberRatings) in addition to vendor docs. Fifteen items (1.2, 1.3, 1.5, 2.1, 2.5, 3.4, 4.4, 5.1, 5.3, 6.1, 6.3, 7.1, 7.3 plus partial items 4.1/4.2 that use InvGate) rest on vendor documentation alone, so their confidence is capped at medium; this matters most for 1.3 (retention tiers), 2.1 (no tag policy) and 7.1 (HA), where the checklist semantics hinge on product-doc wording. 3.5 relies on a single PeerSpot user quote and is therefore low confidence.

One contradiction was reconciled: the heartbeat pages say an endpoint in Missing status has its traffic blocked, while the rule-editor page says endpoints that never sent a heartbeat are allowed by default unless blocking is enabled; because both behaviors are policy-configurable, 4.4 was rated partial (policy-driven rather than a documented fail-safe) rather than supported. For 8.1, the FIPS 140-2 certificate #4100 is flagged "historical" by NIST, which is why the verdict leans on the current FIPS 140-3 mode documentation as well; this caveat is recorded in the item's evidence and gaps.

---

## Bibliography

[1] Sophos. "Security Heartbeat overview - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SophosCentral/SecurityHeartbeatOverview/ (Retrieved: 2026-08-10T13:58:47Z)
[2] Sophos. "Sophos Central services overview - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SophosCentral/CentralSynchronizationSophosCentralServicesOverview/ (Retrieved: 2026-08-10T13:58:47Z)
[3] Sophos. "Security Heartbeat - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SophosCentral/SecurityHeartbeatOverview/SecurityHeartbeat/ (Retrieved: 2026-08-10T13:58:47Z)
[4] Sophos. "Synchronized Application Control - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Applications/SynchronizedApplicationControl/ (Retrieved: 2026-08-10T13:58:47Z)
[5] Sophos. "Turn on security heartbeat - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SophosCentral/SecurityHeartbeatOverview/EnableHeartbeat/ (Retrieved: 2026-08-10T13:58:47Z)
[6] Sophos. "Integrate your firewall with ZTNA - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SophosCentral/CentralZTNAGateway/ (Retrieved: 2026-08-10T13:58:47Z)
[7] Sophos. "Live connections - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/CurrentActivities/LiveConnectionsIPv4IPv6/ (Retrieved: 2026-08-10T13:58:47Z)
[8] Sophos. "Compliance - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Reports/Compliance/ (Retrieved: 2026-08-10T13:58:47Z)
[9] Sophos. "Disk space for logs and reports - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Logs/StorageLogsReports/ (Retrieved: 2026-08-10T13:58:47Z)
[10] Sophos. "Syslog information - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Logs/LogViewer/LogsSyslogInfo/ (Retrieved: 2026-08-10T13:58:47Z)
[11] Sophos. "High availability - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SystemServices/HighAvailability/ (Retrieved: 2026-08-10T13:58:47Z)
[12] Sophos. "Firewall management and deployment (HA) - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/HighAvailablityStartupGuide/HARequirements/HADeploymentModes/ (Retrieved: 2026-08-10T13:58:47Z)
[13] Sophos. "HA traffic flow - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/HighAvailablityStartupGuide/AboutHA/HAArchitecture/ (Retrieved: 2026-08-10T13:58:47Z)
[14] Sophos. "HA modes and device roles - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/HighAvailablityStartupGuide/AboutHA/HAModesRoles/ (Retrieved: 2026-08-10T13:58:47Z)
[15] Sophos. "Air gap licensing info - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Administration/Licensing/AdministrationLicensingAirGap/ (Retrieved: 2026-08-10T13:58:47Z)
[16] Sophos. "Download firmware - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/BackupAndFirmware/Firmware/FirmwareDownloadFirmware/ (Retrieved: 2026-08-10T13:58:47Z)
[17] Sophos. "Netflow - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Administration/NetflowConfiguration/ (Retrieved: 2026-08-10T13:58:47Z)
[18] Sophos. "Invalid traffic events - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Logs/LogViewer/InvalidTrafficEvents/ (Retrieved: 2026-08-10T13:58:47Z)
[19] Sophos. "Add a firewall rule - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/RulesAndPolicies/FirewallRules/FirewallRuleAdd/ (Retrieved: 2026-08-10T13:58:47Z)
[20] Sophos. "Active firewall rules - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/ControlCenter/ControlCenterActiveFirewallRules/ (Retrieved: 2026-08-10T13:58:47Z)
[21] Sophos. "API - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/BackupAndFirmware/API/ (Retrieved: 2026-08-10T13:58:47Z)
[22] Sophos. "Backup and restore - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/BackupAndFirmware/BackupAndRestore/ (Retrieved: 2026-08-10T13:58:47Z)
[23] Sophos. "FIPS 140-3 Level 1 - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Certifications/FIPS/ (Retrieved: 2026-08-10T13:58:47Z)
[24] Sophos. "Reports - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Reports/ (Retrieved: 2026-08-10T13:58:47Z)
[25] Sophos. "Dashboards - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Reports/Dashboards/ (Retrieved: 2026-08-10T13:58:47Z)
[26] Sophos. "Synchronized Application Control overview - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/SophosCentral/CentralSynchronizationSACOverview/ (Retrieved: 2026-08-10T13:58:47Z)
[27] Sophos. "Firewall rules - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/RulesAndPolicies/FirewallRules/ (Retrieved: 2026-08-10T13:58:47Z)
[28] Sophos. "Policy tester - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Diagnostics/Tools/PolicyTest/ (Retrieved: 2026-08-10T13:58:47Z)
[29] Sophos. "Sophos X-Ops threat feeds - Sophos Firewall (SFOS 20.0 webhelp)". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/ActiveThreatResponse/ConfigureFeeds/ActiveThreatResponseSophosXOpsThreatFeeds/ (Retrieved: 2026-08-10T13:58:47Z)
[30] Sophos. "Firewall reporting storage by firewall model - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/FirewallManagement/Firewalls/FirewallReportingStorage/ (Retrieved: 2026-08-10T13:58:47Z)
[31] Sophos. "Firewall reporting FAQs - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/FirewallManagement/FirewallReports/FirewallReportingFAQs/ (Retrieved: 2026-08-10T13:58:47Z)
[32] Sophos. "Report Hub - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/FirewallManagement/FirewallReportDashboard/ (Retrieved: 2026-08-10T13:58:47Z)
[33] Sophos. "Turn on firewall reporting - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/FirewallManagement/Firewalls/TurnOnFirewallReporting/ (Retrieved: 2026-08-10T13:58:47Z)
[34] Sophos. "Manage an HA pair in Sophos Central - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/FirewallManagement/Firewalls/FirewallManageHA/ (Retrieved: 2026-08-10T13:58:47Z)
[35] Sophos. "Zero Trust Network Access dashboard - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/ZeroTrustNetworkAccess/ (Retrieved: 2026-08-10T13:58:47Z)
[36] Sophos. "Policies (ZTNA) - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/ZeroTrustNetworkAccess/ZTNAPolicies/ (Retrieved: 2026-08-10T13:58:47Z)
[37] Sophos. "Gateways (ZTNA) - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/ZeroTrustNetworkAccess/ZTNAGateways/ (Retrieved: 2026-08-10T13:58:47Z)
[38] Sophos. "API Credentials - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/GlobalSettings/AccessControl/APICredentials/ (Retrieved: 2026-08-10T13:58:47Z)
[39] Sophos. "Third-party access via APIs - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/GlobalSettings/AccessControl/APICredentials/ThirdPartyAccess/ (Retrieved: 2026-08-10T13:58:47Z)
[40] Sophos. "Events - Sophos Central Admin help". https://docs.sophos.com/central/customer/help/en-us/ManageYourProducts/LogsReports/Logs/Events/ (Retrieved: 2026-08-10T13:58:47Z)
[41] Sophos. "Installer command-line options for Windows - Sophos Central Partner help". https://docs.sophos.com/central/Partner/help/en-us/Help/MyEnvironment/Installers/WindowsCommandLine/ (Retrieved: 2026-08-10T13:58:47Z)
[42] BSI / Common Criteria Portal. "Certification Report BSI-DSZ-CC-1016-2020 for Sophos Firewall OS Version 17.0". https://www.commoncriteriaportal.org/files/epfiles/1016a_pdf.pdf (Retrieved: 2026-08-10T13:58:47Z)
[43] NIST / CMVP. "NIST CMVP Certificate #4100 - Sophos Cryptographic Module (FIPS 140-2, Level 1, historical)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4100 (Retrieved: 2026-08-10T13:58:47Z)
[44] InvGate. "Sophos Intercept X - specs, reviews and EoL info (InvGate ITDB)". https://invgate.com/itdb/sophos-intercept-x (Retrieved: 2026-08-10T13:58:47Z)
[45] Sophos. "Sophos ZTNA - Zero Trust Network Access (product page)". https://www.sophos.com/en-us/products/zero-trust-network-access (Retrieved: 2026-08-10T13:58:47Z)
[46] Sophos. "ITSM - ServiceNow Integration | Sophos Marketplace". https://www.sophos.com/en-us/marketplace/servicenow-itsm (Retrieved: 2026-08-10T13:58:47Z)
[47] CyberRatings.org. "2024 Q1 Cloud Network Firewall Report - Sophos (CyberRatings)". https://cyberratings.org/resources/2024-q1-cloud-network-firewall-report-sophos/ (Retrieved: 2026-08-10T13:58:47Z)
[48] PeerSpot. "Sophos Firewall Reviews (PeerSpot)". https://www.peerspot.com/products/sophos-firewall-reviews (Retrieved: 2026-08-10T13:58:47Z)
[49] Sophos Community. "Introducing Sophos ZTNA on Sophos Firewall (Sophos Community announcement)". https://community.sophos.com/zero-trust-network-access/b/announcements/posts/introducing-sophos-ztna-on-sophos-firewall (Retrieved: 2026-08-10T13:58:47Z)
[50] Sophos Community. "Generative AI Policy Enforcement with Sophos Firewall (Sophos Community blog)". https://community.sophos.com/sophos-xg-firewall/b/blog/posts/generative-ai-policy-enforcement-with-sophos-firewall (Retrieved: 2026-08-10T13:58:47Z)
[51] Avanet. "Send Sophos Firewall Syslog securely to a SIEM | Avanet KB". https://www.avanet.com/en/kb/sophos-firewall-syslog-siem/ (Retrieved: 2026-08-10T13:58:47Z)
[52] Avanet. "Test Sophos Firewall Rules Cleanly | Avanet KB". https://www.avanet.com/en/kb/sophos-firewall-rule-testing/ (Retrieved: 2026-08-10T13:58:47Z)
[53] Avanet. "Install Sophos Central Intercept X (Windows) | Avanet KB". https://www.avanet.com/en/kb/install-sophos-central-intercept-x-windows/ (Retrieved: 2026-08-10T13:58:47Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 53 (kept: 53, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, third_party_review: 6, vendor_blog: 2, vendor_datasheet: 2, vendor_doc: 41
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
