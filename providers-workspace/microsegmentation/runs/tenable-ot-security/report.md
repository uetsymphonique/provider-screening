# Microsegmentation Product Assessment: Tenable - Tenable OT Security (Tenable One OT Exposure)

**Product ID:** `tenable-ot-security`
**Version reference:** Tenable One OT Exposure 4.7.x (current line, docs July 2026); assessment anchored to 4.5-4.7 user guides, product page and 2023-2024 datasheets
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T16:55:20Z
**Total evidence items collected:** 71
**Total distinct sources:** 26

---

## 1. Overview

Tenable OT Security (rebranded Tenable One OT Exposure) is Tenable's operational-technology security platform for converged IT/OT environments, positioned as an ICS visibility, vulnerability-management and threat-detection solution rather than an inline zero-trust enforcement product. Deployment is passive-first: an ICP appliance analyzes traffic collected from SPAN/tap segments, optional sensors capture traffic per managed switch, and Windows OT Agents run active queries where sensors are impractical; an Enterprise Manager option consolidates multiple ICPs [4][8]. The platform auto-discovers and inventories assets, maps their connections, folds CVEs into per-asset risk scores, and detects policy violations and anomalies [2][5]. It integrates with SIEMs via syslog/CEF, with ServiceNow CMDB, and with Tenable Security Center / Vulnerability Management [10][16][17]. Against the 33-item microsegmentation checklist the product scores 8 supported, 17 partial, 1 not supported and 7 unknown: discovery, mapping, dual agent/agentless collection, SIEM/CMDB integration and compliance reporting are strengths, while tag-based policy enforcement, policy simulation/rollback, Kubernetes support, controller-cluster HA and numeric agent-resource/latency figures are absent or unquantified.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 4                | 4      | 0   |
| partial          | 17    | 0                | 17     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 7     | 0                | 0      | 7   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 16 items backed by ≥ 2 source_types; 15 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | The platform auto-discovers and continuously tracks OT/IT assets via passive sensors plus active queries; the product page, user-guide System Elements, Solution Architecture, datasheet and PeerSpot reviews all document automated asset discovery. [1], [2], [4], [5], [14] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | The Network Map visualizes assets and connections with drill-down grouping by asset type, vendor, family, Purdue level and risk level, and color-codes IT vs OT traffic; no app/environment/role/process grouping is documented. [7], [24] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Storage sizing guidance uses a 30-day packet-capture example and states oldest PCAP data is overwritten once storage fills; the Network Map defaults to a 30-day timeframe, and no 90-day connection-history retention figure is documented. [7], [12] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | - | CVE data feeds asset risk scoring and syncs with Tenable Security Center / Tenable One Vulnerability Management; the Network Map itself conveys risk levels (which incorporate CVEs) but does not list CVEs directly on the map. [5], [10] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Unauthorized-communication and network-baseline-deviation policies detect connections between assets that never communicated before, and the solution surfaces unknown communications for investigation. [5], [6], [24] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | - | Detection policies are defined using Asset Groups, Tag Groups and Network Segments rather than raw IPs, and asset inventory can be shared with NGFWs (e.g. Palo Alto) for segmentation; native enforcement of tag-based access policies is not documented. [1], [6], [10] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | - | no evidence found (No AI/ML policy-rule recommendation feature documented; anomaly detection is baseline/statistical and Tenable One AI remediation guidance is separate from policy rule generation.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | - | no evidence found (No policy simulation or dry-run mode documented; the PCAP Player is for traffic analysis, not policy dry-run.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (Device configuration snapshots can be restored to a last known good state, but no instant one-click policy rollback feature is documented.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found (Policies are flat detection rules configured with groups; no inherited or hierarchical policy structure is documented.) |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | OT Agents install on Windows machines (HMI, workstation, jump box) while the ICP/sensors run on Linux (Tenable Core, built on Oracle Linux 8); no explicit AIX or Solaris coverage is documented for OT Security. [8], [9], [25] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (No Kubernetes/container support documented for Tenable OT Security; container security is covered by other Tenable products, not OT Security.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | - | Collection is dual-mode: passive sensors capture all traffic (SPAN/TAP) while Windows OT Agents perform active queries, and Safe Active Query plus active scanning are documented. [2], [4], [8], [9], [15] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | Offline plugin/ruleset updates are documented for devices without internet, and a third-party review confirms sensors operate fully offline in air-gapped networks using only SPAN/TAP access. [3], [15] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scaling guidance is throughput-based per ICP (50 Mbps to 1 Gbps SPAN/TAP) with sensors deployed per managed switch and an Enterprise Manager consolidating multiple ICPs; no workload-count figure is published and PeerSpot cites thousands of assets. [4], [12], [14] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | The vendor comparison table describes the OT Agent as lightweight and bulk-deployable with no dedicated hardware; no CPU-percent figure is published. [9] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | The OT Agent is documented to run on existing Windows machines with no dedicated hardware, but no RAM footprint figure is published. [9] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Monitoring is passive and out-of-band via SPAN/tap, so no inline latency is introduced, but Tenable publishes no numeric latency figure. [4], [15] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | - | Components capture traffic passively out-of-band (SPAN/tap) so there is no inline data path whose failure could interrupt traffic; docs and a CIS directory describe the platform as non-disruptive. [4], [15], [23] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | - | Passive discovery is documented as requiring no reboots and the OT Agent installs via an MSI wizard; the docs do not explicitly state whether a server reboot is required for agent install/update. [8], [15] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | The developer portal documents a GraphQL API (single /graphql endpoint) while the datasheet and Solution Architecture reference a RESTful API for data extraction; no evidence the API covers 100% of administration functions. [2], [4], [22] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | - | Event logs are sent to SIEMs via syslog/CEF and the product page and third-party review document Splunk/SOAR and other SIEM integrations. [1], [4], [15], [16] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | The Tenable Connector for Assets pulls OT Security assets into ServiceNow CMDB tables, and the datasheet describes sharing with CMDB/asset inventory platforms. [2], [17] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No Jenkins/GitLab/Terraform or DevSecOps pipeline integration documented for OT Security; Tenable CI/CD tooling covers container/cloud products.) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | - | Policies are detection rules that log events and send notifications (no enforcement actions), and a PeerSpot reviewer states the product should expand beyond detection to prevention; no process-level access enforcement is documented. [5], [6], [14] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Multi-feed threat intelligence (ICS-CERT, NVD, IoCs) and Suricata signature-based detection are documented; no honeypot/deception capability is mentioned. [5], [13] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Supported | high | - | Out-of-the-box dashboards and reporting map findings to NERC CIP, NIST, ISO 27001, PCI DSS and IEC 62443, with framework-to-requirement mapping described by a third-party review. [1], [15] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | Agent/ICP pairing is certificate-authenticated (certificate fingerprint + API key) and management console access is HTTPS; TLS version and mutual-TLS between agent and controller are not specified. [4], [8], [9] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | - | no evidence found (No active-active/active-passive controller clustering documented; the Enterprise Manager aggregates multiple ICPs (central hub) but no cluster failover is described.) |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | The vendor comparison table states OT Agents can operate independently of the ICP to collect data (with support+scripts), while Sensors are fully ICP-dependent; no policy-execution autonomy is documented. [9] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Backup and restore are documented via the Tenable Core utility (service is stopped during backup/restore); no site-to-site DR replication or sync is documented. [18] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | XL ICP storage uses FIPS-140 compliant self-encrypting drives per the hardware specifications; no FIPS 140-2/140-3 software validation or Common Criteria EAL4+ certification for OT Security was found. [11] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | Protocol-level compatibility with Siemens (SICAM/PROFINET, SIMATIC), Honeywell (Experion PKS FTE/CEE) and ABB (800xA over MMS) is documented, with 40+ industrial protocols per a third-party review; no formal vendor compatibility certificates are cited. [3], [6], [15] |

---

## 4. Notable Strengths

- **Automated real-time asset discovery (items 1.1, 3.3):** passive sensors on SPAN/tap segments plus Windows OT Agents with active queries deliver continuous IT/OT/IoT asset inventory [4][8].
- **Interactive network mapping (items 1.2, 1.5):** the Network Map visualizes connections with grouping by asset type, vendor, family, Purdue level and risk level, and flags unauthorized or never-before-seen conversations [6][7].
- **Dual agent/agentless collection (item 3.3):** full passive traffic capture on sensors is complemented by active scanning and active queries via the OT Agent [2][9].
- **SIEM/SOAR and CMDB integration (items 5.2, 5.3):** syslog/CEF event streaming to SIEMs and ServiceNow CMDB asset sync are documented end to end [16][17].
- **Compliance reporting (item 6.3):** out-of-the-box dashboards map posture to NERC CIP, NIST, ISO 27001, PCI DSS and IEC 62443 [1].

## 5. Notable Gaps / Risks

- **No native policy enforcement (items 2.1, 6.1):** policies are detection rules that log events and send notifications, and a PeerSpot reviewer notes the product should expand beyond detection to prevention; segmentation enforcement depends on sharing inventory with NGFWs such as Palo Alto [6][14].
- **Connection-history retention below the 90-day requirement (item 1.3):** storage guidance uses a 30-day packet-capture example and oldest PCAP data is overwritten when storage fills, so no 90-day forensic window is documented [12].
- **Policy-management features absent (items 2.2-2.5):** no AI/ML rule recommendation, policy simulation/dry-run, instant rollback, or hierarchical/inherited policy structure is documented.
- **Controller HA and autonomy limited (items 7.1, 7.2):** no active-active/active-passive controller clustering is documented (the Enterprise Manager only aggregates ICPs), and sensors are fully ICP-dependent [9].
- **Numeric thresholds unmet (items 3.5, 4.1-4.3):** no workload-count, agent CPU/RAM or latency figures are published; scaling guidance is throughput-based per ICP (50 Mbps to 1 Gbps SPAN/TAP) [12].

## 6. Evidence Quality Notes

16 of 33 items are backed by 2+ source types and 15 rely only on vendor documentation (confidence capped at medium). Non-vendor triangulation came from PeerSpot community reviews, the Security Scientist technical blog and the CIS CyberMarket directory, used for items 1.1, 3.3, 3.4, 4.3, 4.4, 5.2, 6.1 and 6.3; the remaining items are single- or vendor-doc-sourced, which matters most for items 4.1, 4.2, 7.2, 7.3 and 8.1 whose verdicts rest entirely on vendor tables or guides. The Security Scientist page is machine-assisted content, so it was only used where it corroborates vendor documentation.

One direct contradiction surfaced on 5.1: the 2024 datasheet describes a "RESTful API" while the current developer portal states the platform uses a GraphQL API instead of REST; the partial verdict follows the newer developer documentation. All 26 cited sources were staged in artifacts/ with hash-anchored text; industrialcyber.co could not be staged (Cloudflare challenge) and was excluded, and several numeric-threshold items (3.5, 4.1, 4.2, 4.3) have no published figures in any source.

---

## Bibliography

[1] Tenable. "Tenable One OT Exposure (product page)". https://www.tenable.com/products/ot-security (Retrieved: 2026-08-10T16:55:20Z)
[2] Tenable (via Arrow ECS). "Tenable OT Security Data Sheet (Feb 2024)". https://www.arrow.com/globalecs-media/kemkykjc/datasheet-tenable-ot.pdf (Retrieved: 2026-08-10T16:55:20Z)
[3] Tenable. "Tenable One OT Exposure 4.5 User Guide (PDF)". https://docs.tenable.com/OT-security/Content/PDF/Tenable_OT_Security-User_Guide.pdf (Retrieved: 2026-08-10T16:55:20Z)
[4] Tenable. "Solution Architecture (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/Introduction/SolutionArchitecture.htm (Retrieved: 2026-08-10T16:55:20Z)
[5] Tenable. "System Elements (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/Introduction/SystemElements.htm (Retrieved: 2026-08-10T16:55:20Z)
[6] Tenable. "Policies (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/Policies/Policies.htm (Retrieved: 2026-08-10T16:55:20Z)
[7] Tenable. "Network Map (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/Network/NetworkMap.htm (Retrieved: 2026-08-10T16:55:20Z)
[8] Tenable. "OT Agents (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/DataSources/Agents.htm (Retrieved: 2026-08-10T16:55:20Z)
[9] Tenable. "Comparing OT Agent and Sensor (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/DataSources/ComparingOTAgentandSensor.htm (Retrieved: 2026-08-10T16:55:20Z)
[10] Tenable. "Integrations (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/Settings/Integrations.htm (Retrieved: 2026-08-10T16:55:20Z)
[11] Tenable. "Tenable One OT Exposure Hardware Specifications". https://docs.tenable.com/general-requirements/Content/OTSecurityHardwareSpecifications.htm (Retrieved: 2026-08-10T16:55:20Z)
[12] Tenable. "System Requirements (Tenable One OT Exposure 4.7 User Guide)". https://docs.tenable.com/OT-security/Content/GettingStarted/SystemRequirements.htm (Retrieved: 2026-08-10T16:55:20Z)
[13] Tenable (via InNetworkTech). "Tenable OT Security Threat Intelligence Data Sheet (Jul 2023)". https://innetworktech.com/wp-content/uploads/2024/09/Datasheet-Tenable-ot_Threat_Intelligence.pdf (Retrieved: 2026-08-10T16:55:20Z)
[14] PeerSpot. "Tenable OT Security Reviews (PeerSpot)". https://www.peerspot.com/products/tenable-ot-security-reviews (Retrieved: 2026-08-10T16:55:20Z)
[15] Security Scientist. "11 Questions and Answers About Tenable OT Security". https://www.securityscientist.net/blog/12-questions-and-answers-about-tenable-ot-security/ (Retrieved: 2026-08-10T16:55:20Z)
[16] Tenable. "Tenable One OT Exposure Syslog Integration Guide (PDF)". https://docs.tenable.com/quick-reference/ot-security-syslog-integration-guide/Content/PDF/Tenable_OT_Security_Syslog_Integration_Guide.pdf (Retrieved: 2026-08-10T16:55:20Z)
[17] Tenable. "Configure Tenable OT Security (Tenable and ServiceNow Integration Guide)". https://docs.tenable.com/integrations/ServiceNow/Content/snow6/config-tot.htm (Retrieved: 2026-08-10T16:55:20Z)
[18] Tenable. "Upload and Restore an Application Backup (Tenable Core + OT Security)". https://docs.tenable.com/tenable-core/OT-security/Content/Backup_Restore.htm (Retrieved: 2026-08-10T16:55:20Z)
[19] Tenable. "Welcome to Tenable One OT Exposure Enterprise Manager". https://docs.tenable.com/OT-security/enterprise-manager/Content/EnterpriseManager/EMWelcome.htm (Retrieved: 2026-08-10T16:55:20Z)
[20] Tenable. "Welcome to Tenable Core + Tenable OT Security Enterprise Management". https://docs.tenable.com/tenable-core/OT-security-EM/Content/Introduction_OT_EM.htm (Retrieved: 2026-08-10T16:55:20Z)
[21] Tenable. "Tenable OT Security (Tenable One Deployment Guide)". https://docs.tenable.com/quick-reference/tenable-one-deployment-guide/Content/Tenable-ot.htm (Retrieved: 2026-08-10T16:55:20Z)
[22] Tenable. "Tenable OT Exposure Integrations (Tenable Developer Portal)". https://developer.tenable.com/docs/ot-integrations (Retrieved: 2026-08-10T16:55:20Z)
[23] Center for Internet Security. "Tenable OT Security (CIS CyberMarket)". https://www.cisecurity.org/services/cis-cybermarket/tenable-ot-security (Retrieved: 2026-08-10T16:55:20Z)
[24] Tenable. "Tenable OT Security Asset Inventory Solution Overview (Jul 2023)". https://static.tenable.com/marketing/solution-briefs/SolutionBrief-Tenable-ot_Asset_Inventory.pdf (Retrieved: 2026-08-10T16:55:20Z)
[25] Tenable. "Welcome to Tenable Core + Tenable OT Security". https://docs.tenable.com/tenable-core/OT-security/Content/Introduction_OT.htm (Retrieved: 2026-08-10T16:55:20Z)
[26] Tenable. "Welcome to Tenable One OT Exposure (docs index)". https://docs.tenable.com/OT-security/Content/Introduction/Welcome.htm (Retrieved: 2026-08-10T16:55:20Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 26 (kept: 26, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, third_party_review: 2, vendor_datasheet: 3, vendor_doc: 20
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
