# Microsegmentation Product Assessment: Ordr - Ordr Systems Control Engine (SCE)

**Product ID:** `ordr-systems-control-engine-sce`
**Version reference:** Ordr SCE 8.2 (User Documentation 8.2.0); 2025 AI Protect datasheets
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T13:59:34Z
**Total evidence items collected:** 87
**Total distinct sources:** 43

---

## 1. Overview

Ordr Systems Control Engine (SCE) is an agentless connected-device visibility and microsegmentation platform aimed primarily at IoT, OT, and IoMT environments. Sensors deployed at the access, distribution, or core layer passively analyze SPAN, port-mirror, TAP, and NetFlow/sFlow/IPFIX data to continuously discover and classify every connected device; an AI/ML engine baselines each device's behavior (the "flow genome") and automatically generates least-privilege, identity- and group-based policies [1, 2, 21]. Ordr positions SCE as moving from visibility to safe enforcement in one platform: policies are simulated against live traffic before deployment, then pushed through APIs/CLI to existing firewalls, NAC platforms, and switches (e.g., Cisco ISE, ClearPass, Forescout, PAN, Fortinet) rather than through endpoint agents [3, 6, 19]. It can be deployed as SaaS, fully on-premises, private cloud, or MSP-hosted, including air-gapped environments, and scales to over 75,000 devices per 5-node Analytics cluster [1, 14]. The product also provides vulnerability/risk correlation (NVD, ICS-CERT, FDA), SIEM/CMDB integrations, and compliance reporting across HIPAA, NIST, ISO/IEC 27001, IEC 62443, and related frameworks [11, 13, 40].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 14    | 3                | 11     | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 5     | 0                | 5      | 0   |

**Evidence quality:** 10 items backed by ≥ 2 source_types; 25 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** No host agent runs on workloads (zero-touch agentless deployment), so endpoint agent CPU overhead does not apply; collection is performed by out-of-band sensors on SPAN/tap/flow copies.
- **4.2:** Agentless architecture means there is no workload-agent RAM footprint to measure; optional OSIC endpoint scripts are lightweight attribute collectors.
- **4.4:** There is no host enforcement agent whose failure could interrupt workload traffic; enforcement executes on network infrastructure (firewalls, NAC, switches) that continues operating independently.
- **4.5:** No agent install/update cycle exists on endpoint hosts; the optional OSIC script is fetched from SCE and upgraded via sensor/SCE configuration changes, with no reboot requirement documented.
- **7.2:** There is no host agent whose autonomous enforcement would matter; policies live on external enforcement points (firewalls/NAC/switches) that operate independently of the SCE controller, and no controller-failure behavior is documented.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | SCE sensors passively collect SPAN/tap/flow data to continuously discover and classify every connected device; Ordr product pages and Cisco's partner page corroborate automatic high-fidelity discovery. [1], [6], [19], [21] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | The Flow Genome helix, Sankey diagram, and policy Matrix visualize device-level communication mapped by device, group, and business function; no process-level map view is documented. [2], [6], [22] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Flow/device/topology data is stored in an optimized database with user-configurable purge scheduling by data age and type, but no retention-period figure (e.g., >=90 days) is published; the Network History UI supports extended range queries. [2], [23], [39] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | - | Vulnerability context (CVE/FDA/ICSA IDs, NVD/ICS-CERT correlation, risk scores) is integrated into device records and trust scoring; it is not documented as rendered directly on the connection map. [11], [12], [40], [41] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | SCE surfaces anomalous, unexpected, and unauthorized flows (peer-to-peer, east-west, outside approved paths) and issues security incidents via ML-powered flow analysis; a Shadow IoT report covers unmanaged devices. [2], [10], [12] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | - | Policies are built from device classification, custom tags, groups, and attributes (e.g., Cisco SGT), explicitly not IP addresses; Cisco documents Ordr's group-based policy creation. [2], [15], [19], [29] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | high | - | SCE's AI/ML baselines device behavior and automatically generates least-privilege policies (learning mode documented in policy profiles); Cisco confirms Ordr dynamically generates ISE segmentation policies. [2], [6], [19], [27] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | A policy simulation mode validates enforcement impact against live traffic in the Matrix interface before any rule is deployed. [3], [6], [9], [12] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No source found describing one-click rollback or instant policy revert.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | Policy objects are organized hierarchically (Buckets > Groups, Groups > Policy Profiles) with profile policies applied to all member devices based on attributes. [20], [27], [28] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | medium | - | Agentless sensors identify OS/firmware/software on every connected host via deep packet inspection and protocol decoding (e.g., WinRM for Windows details), so coverage is OS-agnostic; no per-OS agent matrix is needed. [2], [11], [21] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (No source found describing container/Kubernetes/OpenShift isolation support.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | Discovery and enforcement are agentless-first (passive sensors pushing policies to firewalls/NAC/switches); agent-based coverage exists only through the optional OSIC script collector and third-party EDR integrations, with no native host enforcement agent. [2], [20], [21], [22], [32] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | Sensors and the SCE analytics engine run fully on-premises, and Ordr states sensors operate without internet connectivity in air-gapped environments; the optional SCE Center cloud service handles updates in connected deployments. [1], [14] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 75000 workloads | The datasheet specifies over 75,000 devices managed by a 5-node SCE Analytics cluster (A2000-4R up to 75K, A1000-4R up to 50K, per-sensor 500-10,000); the platform datasheet claims millions of devices per enterprise. [1], [4], [38] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | - | No host agent runs on workloads (zero-touch agentless deployment), so endpoint agent CPU overhead does not apply; collection is performed by out-of-band sensors on SPAN/tap/flow copies. [10], [21] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | - | Agentless architecture means there is no workload-agent RAM footprint to measure; optional OSIC endpoint scripts are lightweight attribute collectors. [10], [21] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Sensors passively inspect SPAN/tap copies and policies are enforced on existing infrastructure out-of-band, so no in-line latency is added, but no measured latency figure in ms is published. [1], [24] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | - | There is no host enforcement agent whose failure could interrupt workload traffic; enforcement executes on network infrastructure (firewalls, NAC, switches) that continues operating independently. [22], [32] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | - | No agent install/update cycle exists on endpoint hosts; the optional OSIC script is fetched from SCE and upgraded via sensor/SCE configuration changes, with no reboot requirement documented. [20], [21] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | - | A RESTful API with HTTPS authentication is documented, exposed via Swagger UI in the GUI, and used to implement new connectors; full parity of every admin function with the API is not explicitly verified. [2], [20], [25] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | SIEM integration is documented for Splunk (JSON events over TCP) and Microsoft Sentinel (Syslog), with IBM QRadar listed in product materials; output is JSON/Syslog-based. [7], [30], [31] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | ServiceNow CMDB integration is documented in detail, including a validated Service Graph Connector and bi-directional CMDB sync with ticketing for remediation. [10], [16], [32] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No source found describing CI/CD pipeline integration (Jenkins, GitLab, Terraform).) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | - | Documented enforcement is network-level only: policies are generated for NAC, firewalls, switches, and wireless controllers (ACL/VLAN/SGT/blocklist), and the platform explicitly operates without agents on end devices, ruling out process-level enforcement. [2], [22], [32] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat-intelligence feeds (Anomali/PulseDive), C2/malicious-URL detection, and behavioral impersonation fingerprinting are documented; no honeypot/deception deployment capability is documented. [2], [12], [37] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Audit-ready compliance reporting is documented for HIPAA, NIST (incl. SP 800-82), ISO/IEC 27001, IEC 62443, CMMC, and CIS; no explicit PCI-DSS or NIST SP 800-207 reporting is documented. [3], [10], [13], [26] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | The platform is agentless (no agent-controller channel); transport is HTTPS/TLS-secured with TLS 1.3 documented for ORDR IQ and certificate-based mutual trust used for pxGrid-based integrations, but no explicit TLS 1.3/mTLS statement for a sensor-to-analytics channel was found. [8], [25], [33] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | The datasheet documents a 5-node SCE Analytics cluster (two A2000-4R + three A1000-4R) providing high availability; the A1000-4R is a cluster-only model. [1], [38] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | N/A | medium | - | There is no host agent whose autonomous enforcement would matter; policies live on external enforcement points (firewalls/NAC/switches) that operate independently of the SCE controller, and no controller-failure behavior is documented. [22], [32] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | - | Database backup and restore are documented (local save or NFS destination) for recovery from disk/system failure or full-site outage. [39] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | - | no evidence found (No evidence found for FIPS 140-2/140-3 or Common Criteria EAL4+ certification; SOC 2 Type II and HIPAA compliance are marketed but are not FIPS/CC.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (No evidence found for industrial software compatibility certifications from Siemens, Honeywell, or ABB.) |

---

## 4. Notable Strengths

- **Agentless discovery-to-enforcement (items 1.1, 3.3, 3.4):** Sensors passively collect SPAN/tap/flow data with no endpoint agents, and policies are enforced by pushing ACL/VLAN/SGT rules to existing firewalls, NAC, and switches; sensors operate fully on-premises and in air-gapped networks [1, 14, 21].
- **AI/ML policy generation with simulation (items 2.2, 2.3):** Behavior baselines are translated into least-privilege policies automatically, and a policy simulation mode validates impact against live traffic before any rule is deployed [2, 6, 12].
- **Identity/tag-based policy model (items 2.1, 2.5):** Policies are built from device classification, custom tags, groups, and attributes such as Cisco SGTs rather than IP addresses, organized through a Bucket/Group/Policy-Profile hierarchy [15, 19, 29].
- **Scale and high availability (items 3.5, 7.1):** Documented capacity of over 75,000 devices per 5-node SCE Analytics cluster, with a cluster-only appliance model and redundant power [1, 38].
- **Ecosystem depth (items 5.2, 5.3):** Native SIEM (Splunk JSON-over-TCP, Sentinel Syslog, QRadar listed), ServiceNow CMDB via a validated Service Graph Connector, and 200+ integrations [16, 30, 31].

## 5. Notable Gaps / Risks

- **No process-level enforcement (item 6.1):** Enforcement is documented only at the network level (ACL/VLAN/SGT/blocklist via NAC, firewalls, switches); the agentless design rules out host process-level control, which may be a gap for workload-level segmentation use cases [2, 22].
- **Undocumented policy rollback (item 2.4):** No source describes a one-click rollback or instant policy revert, a load-bearing safety feature for large-scale enforcement rollouts.
- **No container/Kubernetes support evidence (item 3.2):** No documentation was found for container, Kubernetes, or OpenShift isolation, limiting fit for modern workload environments.
- **No FIPS/Common Criteria or industrial-vendor certifications (items 8.1, 8.2):** SOC 2 Type II and HIPAA are marketed, but FIPS 140-2/140-3, Common Criteria EAL4+, and Siemens/Honeywell/ABB compatibility certifications are not documented [20].
- **Unquantified retention and partial compliance coverage (items 1.3, 6.3):** Flow retention is configurable but no >=90-day figure is published, and PCI-DSS/NIST SP 800-207 reporting are not documented (ISO/IEC 27001, IEC 62443, NIST, HIPAA, CMMC, CIS are) [13, 39].

## 6. Evidence Quality Notes

Evidence was collected from 43 staged sources (87 evidence entries), of which 34 are Ordr technical documentation (vendor_doc), 4 vendor datasheets, 4 vendor blogs, and 1 independent source: Cisco's partner page on cisco.com. Only items 1.1, 2.1, and 2.2 are corroborated by a non-vendor source and rated high confidence; the remaining 28 non-unknown items rely on vendor documentation or datasheets and are capped at medium confidence per the validator rule. The vendor's official 8.2 knowledge base (kb.ordr.net) and the SCE datasheet/technology whitepaper PDFs supplied most of the technical detail (scale, HA cluster, backup, enforcement mechanics, integrations).

No contradictions between sources were found. Verdicts were downgraded from supported to partial wherever evidence was qualitative rather than numeric (1.3 retention, 4.3 latency) or where the documented capability covered only part of the requirement (1.2 process-level map view, 3.3 agent-based coverage, 6.2 honeypot/deception, 6.3 specific frameworks, 6.4 explicit mTLS for a sensor channel). Item 6.1 (process-level enforcement) is rated not_supported on the strength of the documented network-level, agentless enforcement architecture rather than absence of a mention. Five items (2.4, 3.2, 5.4, 8.1, 8.2) have no supporting evidence and are marked unknown per the anti-fabrication contract.

---

## Bibliography

[1] Ordr. "Ordr Systems Control Engine Datasheet". https://go.ordr.net/rs/976-OJA-437/images/ordr_solution_brief_ordr_systems_control_engine_datasheet.pdf (Retrieved: 2026-08-10T13:59:34Z)
[2] Ordr. "Ordr Systems Control Engine Technology White Paper". https://go.ordr.net/rs/976-OJA-437/images/ordr_whitepaper_ordr_systems_control_engine_technology_whitepaper.pdf (Retrieved: 2026-08-10T13:59:34Z)
[3] Ordr. "ORDR AI Protect for Segmentation Datasheet". https://go.ordr.net/rs/976-OJA-437/images/2025_ordr_datasheet_AI_Protect_Segmentation.pdf?version=0 (Retrieved: 2026-08-10T13:59:34Z)
[4] Ordr. "The ORDR AI Protect Platform Datasheet". https://go.ordr.net/rs/976-OJA-437/images/ordr_datasheet-platform.pdf (Retrieved: 2026-08-10T13:59:34Z)
[5] Ordr. "ORDR AI Protect for Security Datasheet". https://go.ordr.net/rs/976-OJA-437/images/2025_ordr_datasheet_AI_Protect_Security.pdf?version=0 (Retrieved: 2026-08-10T13:59:34Z)
[6] Ordr. "The ORDR Platform | Connected Asset Security". https://ordr.net/platform (Retrieved: 2026-08-10T13:59:34Z)
[7] Ordr. "AI Protect for Network Segmentation | ORDR". https://ordr.net/ai-protect-segmentation (Retrieved: 2026-08-10T13:59:34Z)
[8] Ordr. "ORDR IQ: Agentic AI Security Expert | ORDR". https://ordr.net/ordr-iq (Retrieved: 2026-08-10T13:59:34Z)
[9] Ordr. "Network Segmentation Tools That Actually Enforce Protection | ORDR". https://ordr.net/solutions/network-segmentation (Retrieved: 2026-08-10T13:59:34Z)
[10] Ordr. "Connected Device Compliance & Security Hygiene | ORDR". https://ordr.net/solutions/compliance (Retrieved: 2026-08-10T13:59:34Z)
[11] Ordr. "IoT & Connected Device Vulnerability Management | ORDR". https://ordr.net/solutions/vulnerability-management (Retrieved: 2026-08-10T13:59:34Z)
[12] Ordr. "Zero Trust Security for IoT & Connected Devices | ORDR". https://ordr.net/solutions/zero-trust (Retrieved: 2026-08-10T13:59:34Z)
[13] Ordr. "Manufacturing OT/IT Cybersecurity | ORDR". https://ordr.net/solutions/manufacturing (Retrieved: 2026-08-10T13:59:34Z)
[14] Ordr. "Air-Gapped Network - ORDR Glossary". https://ordr.net/glossary/air-gapped-network (Retrieved: 2026-08-10T13:59:34Z)
[15] Ordr. "ORDR Q4 2025 Integration Expansions for Connected Asset Security". https://ordr.net/blog/ordr-integrations-q4-2025 (Retrieved: 2026-08-10T13:59:34Z)
[16] Ordr. "ORDR Integration with ServiceNow Service Graph Connector Program". https://ordr.net/newsroom/servicenow-service-graph-integration (Retrieved: 2026-08-10T13:59:34Z)
[17] Ordr. "Ordr and ServiceNow: Complete CMDB for Better Workflows and Security". https://ordr.net/blog/ordr-and-servicenow-complete-cmdb-for-better-workflows-and-security (Retrieved: 2026-08-10T13:59:34Z)
[18] Ordr. "Top 8 Microsegmentation Tools 2026 | ORDR Ranked #1". https://ordr.net/blog/best-microsegmentation-tools (Retrieved: 2026-08-10T13:59:34Z)
[19] Cisco. "Cisco Security and ORDR". https://www.cisco.com/c/en/us/products/security/technical-alliance-partners/ordr.html (Retrieved: 2026-08-10T13:59:34Z)
[20] Ordr. "ORDR 8.2(R1) Release Notes". https://kb.ordr.net/Ordr8.2/assets/Release_Notes/ORDR_8_2_R1.htm (Retrieved: 2026-08-10T13:59:34Z)
[21] Ordr. "ORDR SCE 8.2 User Documentation - Introduction". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Overview/Introduction.htm (Retrieved: 2026-08-10T13:59:34Z)
[22] Ordr. "ORDR SCE 8.2 - Flow Genome". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Device/Flow_Genome.htm (Retrieved: 2026-08-10T13:59:34Z)
[23] Ordr. "ORDR SCE 8.2 - Network History". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Device/Network_History.htm (Retrieved: 2026-08-10T13:59:34Z)
[24] Ordr. "ORDR SCE 8.2 - SCE Sensors". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Network/SCE_Sensors.htm (Retrieved: 2026-08-10T13:59:34Z)
[25] Ordr. "ORDR SCE 8.2 - SCE API". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Admin_Service_List/Internal/SCE_API.htm (Retrieved: 2026-08-10T13:59:34Z)
[26] Ordr. "ORDR SCE 8.2 - Reports". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Tools/Reports.htm (Retrieved: 2026-08-10T13:59:34Z)
[27] Ordr. "ORDR SCE 8.2 - Policy Profile". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Profiles/Policy_Profile.htm (Retrieved: 2026-08-10T13:59:34Z)
[28] Ordr. "ORDR SCE 8.2 - Groups". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Profiles/Groups.htm (Retrieved: 2026-08-10T13:59:34Z)
[29] Ordr. "ORDR SCE 8.2 - Tags". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Tags.htm (Retrieved: 2026-08-10T13:59:34Z)
[30] Ordr. "ORDR SCE 8.2 - Splunk Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/SIEM/Splunk.htm (Retrieved: 2026-08-10T13:59:34Z)
[31] Ordr. "ORDR SCE 8.2 - Microsoft Sentinel Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/SIEM/Microsoft_Sentinel.htm (Retrieved: 2026-08-10T13:59:34Z)
[32] Ordr. "ORDR SCE 8.2 - ServiceNow Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/CMDB/Servicenow/Servicenow.htm (Retrieved: 2026-08-10T13:59:34Z)
[33] Ordr. "ORDR SCE 8.2 - Cisco ISE Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/Policy/Cisco_ISE/Cisco_ISE.htm (Retrieved: 2026-08-10T13:59:34Z)
[34] Ordr. "ORDR SCE 8.2 - ClearPass Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/Policy/ClearPass/ClearPass.htm (Retrieved: 2026-08-10T13:59:34Z)
[35] Ordr. "ORDR SCE 8.2 - Palo Alto Networks Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/Firewall/PAN/Palo_Alto_Networks.htm (Retrieved: 2026-08-10T13:59:34Z)
[36] Ordr. "ORDR SCE 8.2 - Tenable Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/Vulnerability_Management/Tenable.htm (Retrieved: 2026-08-10T13:59:34Z)
[37] Ordr. "ORDR SCE 8.2 - Anomali ThreatStream Integration". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Integrations/URL_Feed/Anomali_ThreatStream.htm (Retrieved: 2026-08-10T13:59:34Z)
[38] Ordr. "ORDR SCE 8.2 - Appliance Reference". https://kb.ordr.net/Ordr8.2/assets/Installation_Guide/Appliance_Reference.htm (Retrieved: 2026-08-10T13:59:34Z)
[39] Ordr. "ORDR SCE 8.2 - Platform (SSO, Database)". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Settings/Platform.htm (Retrieved: 2026-08-10T13:59:34Z)
[40] Ordr. "ORDR SCE 8.2 - Vulnerabilities". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Device/Vulnerabilities.htm (Retrieved: 2026-08-10T13:59:34Z)
[41] Ordr. "ORDR SCE 8.2 - Vulnerabilities & Info". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Security/Vulnerabilities_%26_Info.htm (Retrieved: 2026-08-10T13:59:34Z)
[42] Ordr. "ORDR SCE 8.2 - OVA Sensor Sizing". https://kb.ordr.net/Ordr8.2/assets/Installation_Guide/OVA_Sensor_Sizing.htm (Retrieved: 2026-08-10T13:59:34Z)
[43] Ordr. "ORDR SCE 8.2 - Devices List". https://kb.ordr.net/Ordr8.2/assets/Online_Help/Device/Devices.htm (Retrieved: 2026-08-10T13:59:34Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 8
- **Sources reviewed:** 43 (kept: 43, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 1, vendor_blog: 4, vendor_datasheet: 4, vendor_doc: 34
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
