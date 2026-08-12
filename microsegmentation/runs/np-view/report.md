# Microsegmentation Product Assessment: Network Perception (acquired by Dragos) - NP-View

**Product ID:** `np-view`
**Version reference:** NP-View Desktop and Server 6.x (release notes current to 6.6.0, 2026-07-07)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:10:00Z
**Total evidence items collected:** 64
**Total distinct sources:** 54

---

## 1. Overview

NP-View is an agentless, read-only OT network access modeling platform from Network Perception (acquired by Dragos in October 2024), positioned for network visibility, segmentation analysis, and compliance auditing rather than runtime policy enforcement [1, 39, 52]. It builds an automated topology map by importing firewall, router, and switch configuration files via scheduled connectors (HTTPS/SSH/SMB to devices and configuration managers) and supports both a standalone Desktop mode and a multi-user Server deployment [1, 8, 22]. The platform analyzes all possible connectivity paths, verifies zone-based segmentation via the zone matrix, and flags overly permissive rules and risky paths [10, 11, 38]. Vulnerability scanner data can be imported and shown directly on the map [15]. It is designed for air-gapped environments, running on-premise in offline mode with no internet requirement and no agents, sensors, or network taps on the OT network [1]. Compliance evidence and reporting cover NERC CIP, TSA, IEC 62443, and NIST SP 800-82r3 alignment [5, 39, 54].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 4     | 0                | 4      | 0   |
| partial          | 9     | 0                | 9      | 0   |
| not_supported    | 3     | 0                | 3      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 8     | 0                | 8      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 20 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** NP-View is agentless and requires no endpoint software, so per-OS endpoint agent support (Windows Server/Linux/AIX/Solaris) does not apply.
- **4.1:** No endpoint agent is installed, so the <1% agent CPU overhead metric does not apply.
- **4.2:** No endpoint agent is installed, so the <100MB agent RAM footprint metric does not apply.
- **4.3:** No in-path agent or enforcement engine exists, so network latency impact does not apply.
- **4.4:** No in-path agent exists whose failure could interrupt workload traffic; NP-View is a read-only analysis application.
- **4.5:** No agent is installed or updated on servers, so the reboot-free agent installation requirement does not apply.
- **6.4:** No agent-controller channel exists to encrypt; connector data is retrieved via HTTPS/SSH and the connector file store is PGP-encrypted at rest and in transit.
- **7.2:** No agent exists to enter an autonomous enforcement mode; policy enforcement is not performed by NP-View.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | — | NP-View automatically generates topology maps from imported device configs and polls devices on schedules for continuous (24/7) change detection, but discovery is config-driven modeling of possible paths rather than real-time observation of live traffic flows. [1], [7], [8], [9], [10], [11] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | The topology map visualizes devices, networks, VPNs and hosts organized by zones and logical levels with category/criticality tags; no App/Environment/Role/Process-level grouping is documented. [11], [12], [19] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Flow data (Zeek logs, Cisco IOS NetFlow, PCAP) can be imported as auxiliary topology enrichment and config 'time machine' history is retained, but no >=90-day connection-flow retention for forensic tracing is documented. [9], [26], [42] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | — | Imported vulnerability scanner data (e.g., Nessus) is displayed on the topology map with shield markers on affected nodes and vulnerability details in device info panels. [1], [15], [26] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | External/unknown IP spaces referenced in rule sets are surfaced as unmapped hosts/networks behind an Unmapped gateway, and proactive risk alerts flag overly permissive or misconfigured rules. [3], [4], [11] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Not Supported | medium | — | NP-View is a read-only, non-invasive analysis platform that models and evaluates existing firewall rules; zones are visual analysis labels (auto-generated grouping markers) and no tag/label-based policy creation or enforcement capability is documented. [1], [12], [39] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | — | no evidence found |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | — | The Network Sandbox is an isolated workspace for evaluating proposed configuration changes against policies and best practices without production impact, including risk/vulnerability reporting on imported modified configs. [9] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | — | NP-View is agentless and requires no endpoint software, so per-OS endpoint agent support (Windows Server/Linux/AIX/Solaris) does not apply. [1], [50] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Not Supported | medium | — | NP-View has no enforcement engine of any kind (confirmed by item 6.1): it models and visualizes network-device configurations offline and never applies or pushes container, Kubernetes, or any other workload isolation itself; its own Server component running in Docker is unrelated to isolating customer workloads. [22], [50] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | Agentless/network-integration mode is fully supported via config-file connectors (HTTPS/SSH/SMB to devices and config managers), but agent-based deployment is explicitly not offered by design. [1], [8], [40] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | NP-View runs on-premise in offline mode without internet connectivity and can build the model from config-file backups, confirmed by the product FAQ and a customer case study. [1], [46] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scale is documented in managed devices (tiers up to 500 devices, larger by request) and 25+ supported manufacturers, not in workloads, so the >=50,000-workload threshold cannot be confirmed. [1], [22] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | No endpoint agent is installed, so the <1% agent CPU overhead metric does not apply. [1], [50] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No endpoint agent is installed, so the <100MB agent RAM footprint metric does not apply. [1] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | — | No in-path agent or enforcement engine exists, so network latency impact does not apply. [50] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | No in-path agent exists whose failure could interrupt workload traffic; NP-View is a read-only analysis application. [1] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No agent is installed or updated on servers, so the reboot-free agent installation requirement does not apply. [50] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | Documented REST endpoints exist for specific functions (e.g., GET /license/ha-groups export via Postman) and a Dragos API connector is provided, but no evidence that 100% of admin functions are API-accessible. [26], [35] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | Asset Inventory reports can be sent to and queried from Splunk and Elasticsearch, and notifications can be delivered to syslog and ticketing systems; QRadar/Sentinel and CEF format are not documented. [9], [13] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | — | NP-View is a read-only analysis tool with no enforcement engine of any kind (network or process-level); it evaluates existing device configs but never enforces access control itself. [1] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | — | no evidence found |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Automated compliance reports and evidence collection cover NERC CIP (CIP-002/003/005/007/010), TSA, IEC 62443 and NIST SP 800-82r3 alignment; a PCI DSS page exists; ISO 27001 and NIST SP 800-207 are not documented. [5], [20], [39], [54] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | N/A | medium | — | No agent-controller channel exists to encrypt; connector data is retrieved via HTTPS/SSH and the connector file store is PGP-encrypted at rest and in transit. [1], [16] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | — | no evidence found (No HA/cluster/failover architecture documented for the NP-View Server.) |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | N/A | medium | — | No agent exists to enter an autonomous enforcement mode; policy enforcement is not performed by NP-View. [1] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | A manual database backup procedure for the NP-View Server is documented; no automated disaster-recovery site sync is documented. [22] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No NIST CMVP or Common Criteria entry for NP-View/Network Perception could be verified.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No industrial-vendor compatibility certification (Siemens/Honeywell/ABB) documented.) |

---

## 4. Notable Strengths

- **Air-gapped, non-intrusive deployment (items 3.4, 4.4):** NP-View runs on-premise in offline mode without internet connectivity and without agents, sensors, or taps on the OT network, so it adds no in-path failure risk [1, 46].
- **Automated topology mapping and segmentation verification (items 1.1, 1.2, 1.5):** topology maps are auto-generated from device configs with zone/criticality tagging, and unmapped or unknown IP spaces are surfaced for review [7, 10, 11].
- **Vulnerability context on the map (item 1.4):** imported scanner data marks affected nodes with shields and exposes vulnerability details in device panels [15, 26].
- **What-if change evaluation (item 2.3):** the Network Sandbox lets engineers evaluate proposed configuration changes against policies and best practices without production impact [9].
- **Compliance evidence and reporting (item 6.3):** automated NERC CIP (CIP-002/003/005/007/010) reports, mock audits, and evidence collection are documented, with TSA, IEC 62443, and NIST SP 800-82r3 alignment [5, 20, 39, 54].

## 5. Notable Gaps / Risks

- **No policy creation or enforcement (item 2.1):** NP-View is read-only analysis of existing firewall rules; tag/label-based policy creation is not provided, so it cannot act as the enforcement layer of a microsegmentation program [1, 39].
- **No real-time flow visibility (items 1.1, 1.3):** discovery is config-driven and flow data is only imported as auxiliary enrichment; no 90-day connection-flow history for forensics is documented [9, 26, 42].
- **Scale measured in devices, not workloads (item 3.5):** licensing tiers are documented up to 500 managed devices with larger sizes by request, so the 50,000-workload requirement cannot be confirmed [22].
- **No server HA/cluster or automated DR (items 7.1, 7.3):** no server-level HA or DR site sync is documented; only a manual database backup procedure exists [22].
- **Integration and certification gaps (items 5.1, 5.3, 5.4, 8.1, 8.2):** REST API coverage of admin functions is not documented as complete, no ServiceNow or CI/CD integration is documented, and no FIPS/Common Criteria or Siemens/Honeywell/ABB certifications were found [26, 35].

## 6. Evidence Quality Notes

All 64 evidence entries are grounded verbatim in 54 staged sources (all HTML pages; no PDFs were used). Every item with a non-unknown verdict rests on 1-6 evidence entries drawn from 1-6 sources, but every source is vendor-authored: Network Perception product/KB pages and press/blog content, Dragos-hosted press release and blogs, plus vendor-hosted case studies and release notes. No genuinely independent source (analyst report, third-party lab, or independent news outlet) could be staged: search engines, archive.org, and most independent news sites (SecurityWeek, Industrial Cyber, SiliconANGLE, FinSMEs, Business Wire) were unreachable, Cloudflare-walled, or rate-limited from this network; the one independent article located via Google News RSS (Industrial Cyber on the Dragos acquisition) could not be fetched beyond its challenge page. Because every item is vendor-only, confidence is capped at medium per the validator rule; no item reaches high confidence.

No contradictions between sources were observed. The main judgment calls: item 2.1 is not_supported (not unknown) because the product's documented scope - read-only, non-invasive analysis of existing firewall rules - explicitly rules out policy creation [1, 39]; items 3.1, 4.1-4.5, 6.1, 6.4, and 7.2 are not_applicable on the documented agentless architecture, following the tufin-orchestration-suite precedent for agentless platforms; and items 1.3 and 3.5 are partial with null numeric values because the sources provide no workload counts or flow-retention periods, only qualitative statements.

---

## Bibliography

[1] Network Perception. "NP-View product page (Cyber Risk Mitigation & Management Software)". https://www.network-perception.com/product (Retrieved: 2026-08-10T16:42:28Z)
[2] Network Perception. "Network Visibility software solution page". https://www.network-perception.com/solutions/network-visibility-software (Retrieved: 2026-08-10T16:42:29Z)
[3] Network Perception. "Network Segmentation software solution page". https://www.network-perception.com/solutions/network-segmentation-software (Retrieved: 2026-08-10T16:42:29Z)
[4] Network Perception. "Network Auditing software solution page". https://www.network-perception.com/solutions/network-auditing-software (Retrieved: 2026-08-10T16:42:29Z)
[5] Network Perception. "NERC CIP Compliance software solution page". https://www.network-perception.com/solutions/nerc-cip-compliance (Retrieved: 2026-08-10T16:43:26Z)
[6] Network Perception. "PCI Compliance page". https://www.network-perception.com/pci-compliance (Retrieved: 2026-08-10T16:43:26Z)
[7] Network Perception. "Knowledge Base: What We Do". https://www.network-perception.com/kb/what-we-do (Retrieved: 2026-08-10T16:42:38Z)
[8] Network Perception. "Knowledge Base: Connectors". https://www.network-perception.com/kb/connectors (Retrieved: 2026-08-10T16:42:39Z)
[9] Network Perception. "Knowledge Base: Change Management (continuous configuration monitoring)". https://www.network-perception.com/kb/continuous-configuration-monitoring (Retrieved: 2026-08-10T16:42:39Z)
[10] Network Perception. "Knowledge Base: Path Analysis". https://www.network-perception.com/kb/path-analysis (Retrieved: 2026-08-10T16:42:40Z)
[11] Network Perception. "Knowledge Base: Topology Map". https://www.network-perception.com/kb/topology-map (Retrieved: 2026-08-10T16:42:40Z)
[12] Network Perception. "Knowledge Base: Manage Zones". https://www.network-perception.com/kb/manage-zones (Retrieved: 2026-08-10T16:42:41Z)
[13] Network Perception. "Knowledge Base: Security Information and Event Management (SIEM) Integration". https://www.network-perception.com/kb/security-information-and-event-management-siem-integration (Retrieved: 2026-08-10T16:42:41Z)
[14] Network Perception. "Knowledge Base: Policy Manager". https://www.network-perception.com/kb/policy-manager (Retrieved: 2026-08-10T16:42:42Z)
[15] Network Perception. "Knowledge Base: 3. Segmentation Verification (network risk assessment)". https://www.network-perception.com/kb/network-risk-assessment (Retrieved: 2026-08-10T16:42:43Z)
[16] Network Perception. "Knowledge Base: Configuring Connectors (legacy)". https://www.network-perception.com/kb/np-connect (Retrieved: 2026-08-10T16:42:43Z)
[17] Network Perception. "Knowledge Base: Identifying Risks". https://www.network-perception.com/kb/id-risks (Retrieved: 2026-08-10T16:43:00Z)
[18] Network Perception. "Knowledge Base: Risks & Warnings Report". https://www.network-perception.com/kb/risks-warnings-report (Retrieved: 2026-08-10T16:43:01Z)
[19] Network Perception. "Knowledge Base: 1. Network Mapping (architecture review)". https://www.network-perception.com/kb/architecture-review (Retrieved: 2026-08-10T16:43:01Z)
[20] Network Perception. "Knowledge Base: 4. Audit Assistance". https://www.network-perception.com/kb/audit (Retrieved: 2026-08-10T16:43:01Z)
[21] Network Perception. "Knowledge Base: Vulnerability Prioritization (incident response)". https://www.network-perception.com/kb/incident-response (Retrieved: 2026-08-10T16:43:02Z)
[22] Network Perception. "Knowledge Base: Installing NP-View Server". https://www.network-perception.com/kb/installing-np-view-server (Retrieved: 2026-08-10T16:43:03Z)
[23] Network Perception. "Knowledge Base: Configuring NP-View Server". https://www.network-perception.com/kb/configuration-np-view-server (Retrieved: 2026-08-10T16:43:03Z)
[24] Network Perception. "Knowledge Base: Updating NP-View Server". https://www.network-perception.com/kb/updating-np-view-server (Retrieved: 2026-08-10T16:43:04Z)
[25] Network Perception. "Knowledge Base: Background Tasks". https://www.network-perception.com/kb/background-tasks (Retrieved: 2026-08-10T16:43:04Z)
[26] Network Perception (Dragos). "Knowledge Base: Release Notes (NP-View Desktop and Server, 2025-2026)". https://www.network-perception.com/kb/release-notes (Retrieved: 2026-08-10T16:43:05Z)
[27] Network Perception. "Knowledge Base: Workspace Reports Overview". https://www.network-perception.com/kb/reports (Retrieved: 2026-08-10T16:43:15Z)
[28] Network Perception. "Knowledge Base: Connectivity Paths Report". https://www.network-perception.com/kb/connectivity-paths-report (Retrieved: 2026-08-10T16:43:16Z)
[29] Network Perception. "Knowledge Base: Change Tracking Report". https://www.network-perception.com/kb/change-tracking-report (Retrieved: 2026-08-10T16:43:16Z)
[30] Network Perception. "Knowledge Base: Compare Path History". https://www.network-perception.com/kb/compare-path-history (Retrieved: 2026-08-10T16:43:17Z)
[31] Network Perception. "Knowledge Base: Importing and Exporting Data". https://www.network-perception.com/kb/data-import (Retrieved: 2026-08-10T16:43:17Z)
[32] Network Perception. "Knowledge Base: Workspaces". https://www.network-perception.com/kb/workspaces (Retrieved: 2026-08-10T16:43:18Z)
[33] Network Perception. "Knowledge Base: Manage Views". https://www.network-perception.com/kb/manage-views (Retrieved: 2026-08-10T16:43:19Z)
[34] Network Perception. "Knowledge Base: Users & Groups (Server)". https://www.network-perception.com/kb/users-groups (Retrieved: 2026-08-10T16:43:20Z)
[35] Network Perception. "Knowledge Base: Licensing". https://www.network-perception.com/kb/licensing (Retrieved: 2026-08-10T16:43:21Z)
[36] Network Perception. "Knowledge Base: Firewalls, Routers, Switches (supported devices)". https://www.network-perception.com/kb/firewalls-routers-switches (Retrieved: 2026-08-10T16:43:21Z)
[37] Network Perception. "Knowledge Base: Network Visualization". https://www.network-perception.com/kb/network-visualization (Retrieved: 2026-08-10T16:43:22Z)
[38] Network Perception. "Knowledge Base: Zone Matrix". https://www.network-perception.com/kb/zone-matrix (Retrieved: 2026-08-10T16:43:22Z)
[39] Network Perception. "Press Release: Dragos Acquires Network Perception, Delivers the Industry's Most Comprehensive Visibility of OT Environments". https://www.network-perception.com/press-release/dragos-acquires-network-perception-delivers-the-industrys-most-comprehensive-visibility-of-ot-environments (Retrieved: 2026-08-10T16:43:27Z)
[40] Network Perception. "Blog: Network Perception Acquisition Strengthens Industrial Cyber Defense". https://www.network-perception.com/blog/network-perception-acquisition-strengthens-industrial-cyber-defense-with-network-segmentation-and-access-analysis (Retrieved: 2026-08-10T16:43:28Z)
[41] Network Perception. "Blog: Bolstering Network Segmentation with NP-View - A Cyber Hygiene Perspective". https://www.network-perception.com/blog/bolstering-network-segmentation-with-np-view-a-cyber-hygiene-perspective (Retrieved: 2026-08-10T16:43:29Z)
[42] Network Perception. "Blog: Do you know the difference between Network Traffic Monitoring & Network Access Modeling?". https://www.network-perception.com/blog/difference-between-network-traffic-monitoring-and-network-access-modeling (Retrieved: 2026-08-10T16:43:29Z)
[43] Network Perception. "Blog: Preventing Lateral Movement through Network Access Visibility". https://www.network-perception.com/blog/preventing-lateral-movement-through-network-access-visibility (Retrieved: 2026-08-10T16:43:30Z)
[44] Network Perception. "Blog: The Importance of Velocity in Cybersecurity". https://www.network-perception.com/blog/the-importance-of-velocity-in-cybersecurity (Retrieved: 2026-08-10T16:43:31Z)
[45] Network Perception. "Blog: Accelerate Incident Response with Next-Generation Network Access Visualization". https://www.network-perception.com/blog/accelerate-incident-response-with-next-generation-network-access-visualization (Retrieved: 2026-08-10T16:43:32Z)
[46] Network Perception. "Case Study: PSEG (Save Time in Your Audit)". https://www.network-perception.com/resource/pseg (Retrieved: 2026-08-10T16:43:40Z)
[47] Network Perception. "Case Study: EDF Renewables". https://www.network-perception.com/resource/edf-renewables (Retrieved: 2026-08-10T16:43:40Z)
[48] Network Perception. "Case Study: Crown Computers". https://www.network-perception.com/resource/crown-computers (Retrieved: 2026-08-10T16:43:41Z)
[49] Network Perception. "Case Study: Network Access (renewables company)". https://www.network-perception.com/resource/network-access-case-study (Retrieved: 2026-08-10T16:43:41Z)
[50] Network Perception. "White paper page: The Power of NP-View". https://www.network-perception.com/resource/the-power-of-np-view (Retrieved: 2026-08-10T16:43:42Z)
[51] Network Perception. "White Papers index (Cyber Hygiene, NERC CIP 003/005, Evidence eGuide)". https://www.network-perception.com/white-papers (Retrieved: 2026-08-10T16:43:43Z)
[52] Dragos. "Press Release (Dragos site): Dragos Acquires Network Perception". https://www.dragos.com/resources/press-release/dragos-acquires-network-perception (Retrieved: 2026-08-10T16:49:23Z)
[53] Dragos. "Blog (Dragos site): Network Perception Strengthens Industrial Cyber Defense". https://www.dragos.com/blog/network-perception-strengthens-industrial-cyber-defense-with-network-segmentation-and-access-analysis (Retrieved: 2026-08-10T16:49:24Z)
[54] Dragos. "Blog (Dragos site): NIST SP 800-82r3 - Enhancing OT Security with Dragos and NP-View". https://www.dragos.com/blog/nist-sp-800-82r3-enhancing-ot-security-with-dragos-and-np-view (Retrieved: 2026-08-10T16:49:26Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 54 (kept: 54, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 4, product_release_notes: 1, vendor_blog: 10, vendor_doc: 39
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
