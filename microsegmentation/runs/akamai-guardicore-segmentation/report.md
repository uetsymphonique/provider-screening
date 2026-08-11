# Microsegmentation Product Assessment: Akamai Technologies (Guardicore) - Akamai Guardicore Segmentation

**Product ID:** `akamai-guardicore-segmentation`
**Version reference:** Centra/Guardicore Segmentation platform, current product line (v49-v54); staged docs span Centra 5.0 through 2026 product materials
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T07:42:31Z
**Total evidence items collected:** 109
**Total distinct sources:** 23

---

## 1. Overview

Akamai Guardicore Segmentation (formerly Guardicore Centra) is Akamai's agent-based microsegmentation platform for east-west traffic, positioned around AI-assisted discovery, policy recommendation and enforcement across hybrid cloud, data center, Kubernetes and OT/IoMT environments [1, 2]. The platform decouples policy from the underlying network: assets are grouped by labels (Environment/Application/Role) and enforced by host agents, with agentless coverage via network collectors, VPC flow logs and, most recently, NVIDIA BlueField DPUs for environments that cannot run host software [1, 5, 16, 23]. Deployment is available as SaaS or on-premises, and the product line is in active development (v49-v54-era documentation) [1, 11]. It ships with AI-powered policy workflows, a threat-intelligence firewall, built-in deception (honeypot) capabilities, a full REST API, and documented HA/DR options for the management plane [2, 15, 16, 20]. The 2025-era materials emphasize exposure-aware detection, process-level context and proof-driven policy rollout as differentiators [2, 4].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 22    | 6                | 16     | 0   |
| partial          | 9     | 0                | 9      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 1     | 0                | 0      | 1   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 22 items backed by ≥ 2 source_types; 12 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | The product auto-discovers assets and communication flows in real time across on-prem, cloud, Kubernetes and OT workloads; the Akamai product page, the Centra datasheet and the product brief all document continuous discovery, corroborated by PeerSpot user reviews and an independent technical blog. [1], [2], [16], [18], [19] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | high | — | A single interactive Reveal map visualizes all assets, flows and dependencies with process-level granularity, and label hierarchies (Environment/Application/Role) render as nested groups; corroborated by the user guide, datasheet and peer reviews. [1], [13], [16], [18] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | 30 days | Raw connection-flow retention in the management Elasticsearch defaults to 30 days (connections_delete_after_days) while daily grouped connections default to 90 days; both are configurable via CLI (gc-mgmtctl elastic_archive), so the 90-day requirement is met by default only for aggregated data or with custom retention settings. [11] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | Vulnerability data is collected via osquery-based Insight queries and a PeerSpot user describes Tenable integration that surfaces assets with highly exploitable vulnerabilities for policy building, but a dedicated CVE overlay rendered directly on the connectivity map is not explicitly documented in staged sources. [13], [18] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | The Network Log surfaces security violations with filters and rule suggestions, the datasheet documents policy-based detection of unsanctioned activity plus reputation analysis of suspicious domains/IPs/hashes, and the product page highlights identification of known, unknown and unmanaged assets. [1], [9], [16] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | — | Policies are built from labels (application/environment/role) and are decoupled from the underlying infrastructure; vendor documentation, the Centra datasheet and peer reviews all describe label-based, IP-independent policy creation. [1], [9], [16], [18] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | — | Centra's AI-powered engine auto-generates policy rules from templates and observed traffic, and the product page documents machine-learning-based policy recommendations; a PeerSpot reviewer notes that more AI automation for policy creation would still be welcome, so the feature is confirmed by vendor sources only. [1], [9] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | — | The product page states that security teams can simulate the impact of policies before they go live, the product brief documents staged draft/alert/block workflows with readiness measurement, and an independent blog describes Allow Mode simulation before any traffic is blocked. [1], [2], [19], [20] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Supported | medium | — | The user guide documents a Revisions screen that saves every policy change indefinitely and allows reverting to a previous revision at any time, providing one-click rollback of published policies. [13] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | — | Label keys form a configurable hierarchy (e.g., Environment/Application/Role) that nests assets in the map, and policy rules support priority tiers (implied, override and standard rules), but explicit rule inheritance down a label hierarchy is not documented in staged sources. [13], [14], [16] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | medium | — | Vendor documentation states agents run on all Windows and Linux operating systems, new and legacy, with OS tables covering Windows Server 2003-2019, RHEL/CentOS/Ubuntu/Debian/SUSE, AIX 6.1/7.1/7.2 and Solaris 10/11; an independent blog corroborates Windows Server 2012+, major Linux distributions and Unix variants including AIX and Solaris. [4], [11], [19] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | — | Kubernetes enforcement is native via the Container Network Interface (CNI) controller, OpenShift is listed in the datasheet, and peer reviews describe K8s and OpenShift instrumentation; a couple of reviewers note K8s installation caveats. [1], [3], [16], [18] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | — | The product page explicitly states the solution includes both agent-based and agentless options, with agentless ideal for PaaS, IoT and OT; the datasheet describes agent sensors plus network collectors and VPC flow logs, and independent sources document NetFlow/sFlow/IPFIX collection and NVIDIA BlueField DPU agentless enforcement. [1], [5], [16], [19], [23] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | The installation guide documents offline-mode Linux agent installation (IS_OFFLINE_PACKAGE=true) and the product page states the platform can be deployed on-premises or in the cloud, supporting air-gapped deployments. [1], [5], [12] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 300000 workloads | A vendor customer story documents agent-based deployment across all 300,000 workloads and endpoints of a global consulting firm, and the product page states the AI algorithm learns tens of thousands of applications and millions of flows; peer reviews also praise scalability. [1], [6], [18] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | Vendor documentation states agent CPU utilization can reach up to 5% (Windows and AIX), while an implementation partner reports typical usage generally under 1-2%; no source confirms a sustained sub-1% figure, so the <1% requirement is not demonstrated. [11], [20] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | Vendor documentation states agent memory usage up to 400MB (Windows and AIX), while an implementation partner describes a small memory footprint; no staged source documents RAM below 100MB. [11], [20] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | The comparison guide documents a latency-optimized engine whose latency is relatively insensitive to policy size, and the product page mentions low-latency enforcement, but no staged source gives a measured latency figure, so the <0.1ms threshold is not demonstrated. [1], [4], [16] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | — | If the enforcement kernel module is missing the agent falls back to polling mode where enforcement is not performed, so traffic continues, and the agent persists and keeps enforcing the last received policy when disconnected; however an explicit fail-open/fail-closed configuration setting is not documented, and a peer reviewer flags kernel-module blue-screen risk. [11], [13], [18] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Supported | medium | — | The installation guide states that after AIX agent installation all processes start automatically with no server reboot required, and agent upgrades are performed in place or via remote agent upgrade from the Centra UI; no staged source documents a reboot requirement for agent install or update. [11], [12] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | — | Akamai training material states the RESTful API provides programmatic access to all Centra functionality and that every UI action is backed by an API call; the datasheet lists an Open REST API export protocol, and a peer reviewer confirms APIs support building external reports. [15], [16], [18] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | The Kubernetes brief documents export of network-log data to SIEM, the datasheet lists STIX/Syslog/CEF exports and automatic IOC exports to SIEM systems, a Fortinet brief documents syslog ingestion of Guardicore data, and the user guide documents TLS-encrypted syslog. [3], [13], [16], [17] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | — | The datasheet documents integration with orchestration systems and configuration management databases, an independent blog describes ServiceNow change-management integration, and an implementation partner describes automated API integration with CMDBs. [16], [19], [20] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | — | An independent blog documents Ansible and Terraform managing Guardicore policies as code with GitOps-style review and deployment, and a Fortinet brief describes automation that keeps pace with DevOps; the full REST API underpins this programmatic control. [15], [17], [19] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | high | — | Policy criteria include process and service attributes, the datasheet documents process-level and user-level enforcement, the Platform Agent documentation describes connection validation with process context, and peer reviews confirm process-level segmentation. [4], [10], [16], [18] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Supported | high | — | The datasheet documents a threat-intelligence firewall, reputation analysis and a high-interaction deception engine, the comparison guide describes redirecting blocked sessions to a dynamic deception engine, peer reviews confirm the honeypot model, and an independent blog describes deception-derived IOCs feeding threat feeds and SIEM. [4], [16], [18], [19] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | The product page documents support for PCI-DSS, HIPAA and SWIFT audit requirements, an independent blog describes PCI-DSS 1.3 evidence and alignment with NIST SP 800-207, and customer stories describe CJIS and DWI compliance evidence; however ISO 27001 and IEC 62443 report templates were not found in staged sources. [1], [7], [8], [19], [20] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | The admin guide documents that agent-to-aggregator channels are encrypted and authenticated on TCP/443 using TLS 1.2, and syslog export can be TLS-encrypted; TLS 1.3 is not documented and mutual authentication is described as certificate-based 'authenticated' channels rather than an explicit mTLS mode. [11], [13] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | The admin guide documents aggregator clusters with agent-to-aggregator high availability and round-robin load balancing, a three-node MongoDB cluster for automatic failover, and configurable HA within Elasticsearch clusters. [11] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | — | The user guide states that when the Enforcement module cannot connect to Centra the agent continues enforcing the latest policy it received, and the admin guide documents persistent local storage of the last policy used after restart until an update is fetched. [11], [13] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | — | The admin guide documents a primary/standby management-cluster disaster-recovery scheme with ongoing configuration, inventory and policy sync, plus manual failover/failback procedures. [11] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | — | The NIST CMVP validated-modules registry (1,168 active certificates listed as of the search) contains no Guardicore or Akamai cryptographic module for FIPS 140-2/140-3, and no vendor document claims a FIPS validation or Common Criteria certification. [22] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No staged source mentions Siemens, Honeywell or ABB compatibility certifications; OT segmentation capability is documented (IoT/OT brief, water-utility customer story) but not vendor-specific ICS certifications.) |

---

## 4. Notable Strengths

- **Label-based, IP-independent policy engine (items 2.1, 2.5):** policies are built from a configurable label hierarchy and are completely decoupled from the underlying infrastructure, so rules survive IP and workload changes [1, 9, 13].
- **Process-level visibility and enforcement (items 6.1, 1.2):** connection telemetry is tied to processes and services, and policy criteria can include process, service, user and FQDN, enabling enforcement below the network layer [4, 10, 16].
- **Agent-based plus agentless coverage (items 3.3, 3.4):** the platform combines host agents with NetFlow/sFlow/IPFIX collectors, VPC flow logs, IoT/OT fingerprinting and DPU-based agentless enforcement, including offline-mode agent installation for air-gapped sites [1, 5, 6, 16].
- **Resilient enforcement and management plane (items 7.2, 7.3, 7.1):** agents keep enforcing the last received policy when the controller is unreachable, aggregators and databases cluster for HA, and a primary/standby DR scheme syncs configuration, inventory and policy [11, 13].
- **Automation surface (items 5.1, 5.4):** the REST API backs every UI action, and policies can be managed as code with Ansible/Terraform in GitOps-style workflows [15, 19].

## 5. Notable Gaps / Risks

- **Agent resource footprint vs. stated thresholds (items 4.1, 4.2):** vendor documentation cites up to 5% CPU and 400MB RAM for the agent, while an implementation partner reports typical usage under 1-2% CPU; neither confirms the checklist's <1% CPU / <100MB RAM targets, and 4.3 has no measured latency figure at all [11, 20].
- **Flow-history retention below 90 days by default (item 1.3):** raw connection history defaults to 30 days (daily grouped flows default to 90); meeting a 90-day forensic window requires changing the retention policy via CLI [11].
- **Compliance report coverage is partial (item 6.3):** PCI-DSS, HIPAA, SWIFT, CJIS and DWI evidence are documented, but ISO 27001 and IEC 62443 templates were not found; CVE display directly on the map is also not explicitly documented (item 1.4) [1, 7, 8, 13, 19].
- **No FIPS 140-2/140-3 or Common Criteria certification found (item 8.1):** the NIST CMVP registry lists no Guardicore/Akamai module; transport security is TLS 1.2 with authenticated channels rather than documented TLS 1.3/mTLS (item 6.4) [11, 22].
- **No evidence of Siemens/Honeywell/ABB compatibility certifications (item 8.2):** OT segmentation is supported, but vendor-specific industrial certification claims are absent from staged sources.

## 6. Evidence Quality Notes

22 of 33 items were triangulated across two or more source types; 12 items rest on vendor documentation alone (admin/installation/user guides, datasheet, product briefs, training decks) and are capped at medium confidence by the validator rule, even where the underlying behavior is directly documented (e.g., HA, DR, policy revisions, TLS 1.2, offline install). The main official docs on techdocs.akamai.com are SSO-gated, so the Centra 5.0-era guides were staged from Scribd copies and the newest behavior (AI labeling, exposure-aware assurance) comes from 2025-2026 Akamai product materials; there is a version gap between these document sets that the reviewer should keep in mind.

Items with independent corroboration include discovery/visibility (1.1-1.2), label-based policy (2.1), K8s support (3.2), agent+agentless (3.3), process-level enforcement (6.1) and deception (6.2), backed by PeerSpot user reviews and independent technical blogs. One explicit contradiction was resolved conservatively: vendor guides document agent CPU/RAM ceilings of 5% / 400MB while a partner reports typical usage under 1-2% CPU, so 4.1/4.2 were left partial with no numeric_value rather than asserting either figure. The FIPS negative (8.1) relies on the NIST CMVP registry search, which is authoritative for FIPS but leaves Common Criteria unverified because the CC portal was inaccessible; 8.2 (OT vendor certifications) is unknown due to total absence of evidence.

---

## Bibliography

[1] Akamai Technologies. "Akamai Guardicore Segmentation for Hybrid Cloud (product page)". https://www.akamai.com/products/akamai-guardicore-segmentation (Retrieved: 2026-08-10T07:43:20Z)
[2] Akamai Technologies. "Akamai Guardicore Segmentation Product Brief (PDF)". https://www.akamai.com/content/dam/site/en/documents/brief/akamai-guardicore-segmentation.pdf (Retrieved: 2026-08-10T07:43:20Z)
[3] Akamai Technologies. "Visualize and Secure Kubernetes with Akamai Guardicore Segmentation (solution brief)". https://www.akamai.com/content/dam/site/en/documents/brief/2025/visualize-and-secure-kubernetes-akamai-segmentation.pdf (Retrieved: 2026-08-10T07:43:20Z)
[4] Akamai Technologies. "Akamai Guardicore Segmentation vs. Traditional Microsegmentation Solutions (comparison guide)". https://www.akamai.com/content/dam/site/en/documents/brief/2023/akamai-guardicore-segmentation-vs-traditional-microsegmentation-solutions.pdf (Retrieved: 2026-08-10T07:43:20Z)
[5] Akamai Technologies. "Segmentation for IoT and OT (product brief)". https://www.akamai.com/content/dam/site/en/documents/brief/2024/segmentation-for-iot-and-ot.pdf (Retrieved: 2026-08-10T07:43:20Z)
[6] Akamai Technologies. "Global Consulting Firm Secured 300,000 Endpoints in Record Time (customer story)". https://www.akamai.com/resources/customer-story/global-consulting-firm (Retrieved: 2026-08-10T07:43:20Z)
[7] Akamai Technologies. "U.K. Utility Company Protected Vital Water Utilities (customer story)". https://www.akamai.com/resources/customer-story/uk-utility (Retrieved: 2026-08-10T07:43:20Z)
[8] Akamai Technologies. "North Texas City Secured Critical Infrastructure and CJIS Data (customer story)". https://www.akamai.com/resources/customer-story/north-texas-city (Retrieved: 2026-08-10T07:43:20Z)
[9] Akamai Technologies. "Create effective segmentation security policies (Zero Trust Security documentation)". https://zero-trust-security.readme.io/docs/segmentation-policies (Retrieved: 2026-08-10T07:43:20Z)
[10] Akamai Technologies. "About Access, Threat Protection, and Segmentation (Guardicore Platform Agent documentation)". https://guardicore-platform-agent.readme.io/docs/about-aztc (Retrieved: 2026-08-10T07:43:20Z)
[11] Guardicore / Akamai. "Guardicore Centra 5.0 Administration Guide (Scribd copy)". https://www.scribd.com/document/727768570/Akamai-Guardicore-Segmentation-Admin-User-Guide (Retrieved: 2026-08-10T07:43:20Z)
[12] Guardicore / Akamai. "Guardicore Centra Installation Guide (Scribd copy)". https://www.scribd.com/document/727768573/Akamai-Guardicore-Segmentation-Installation-Guide (Retrieved: 2026-08-10T07:43:20Z)
[13] Guardicore / Akamai. "Akamai Guardicore Segmentation User Guide (Scribd copy)". https://www.scribd.com/document/727768579/Akamai-Guardicore-Segmentation-User-Guide (Retrieved: 2026-08-10T07:43:20Z)
[14] Akamai Technologies. "GCSA Unit 3.01: Policy Rules Structure (training material)". https://www.scribd.com/document/815696882/UNIT-3-01-GCSA-Policy-Rules-Structure (Retrieved: 2026-08-10T07:43:20Z)
[15] Akamai Technologies. "GCSA Unit 5.08: Useful System Configurations, Auditing and API (training material)". https://www.scribd.com/document/998837701/UNIT-5-08-GCSA-Useful-System-Configurations-Auditing-and-API-v48 (Retrieved: 2026-08-10T07:43:20Z)
[16] Guardicore / Akamai. "Guardicore Centra Security Platform Data Sheet (v32, partner-hosted)". https://www.infoguard.ch/hubfs/partner/_partner-downloads/Guardicore-Centra-Data-Sheet_English.pdf (Retrieved: 2026-08-10T07:43:20Z)
[17] Fortinet, Inc.. "Fortinet and Guardicore Security Solution (solution brief)". https://www.fortinet.com/content/dam/fortinet/assets/alliances/sb-fortinet-guardicore-centra-connector-solution.pdf (Retrieved: 2026-08-10T07:43:20Z)
[18] PeerSpot. "Akamai Guardicore Segmentation Reviews (PeerSpot)". https://www.peerspot.com/products/akamai-guardicore-segmentation-reviews (Retrieved: 2026-08-10T07:43:20Z)
[19] Security Scientist. "12 Questions and Answers About Akamai Guardicore Segmentation". https://www.securityscientist.net/blog/12-questions-and-answers-about-akamai-guardicore-segmentation-akamai/ (Retrieved: 2026-08-10T07:43:20Z)
[20] Evolvous. "Akamai Guardicore Segmentation 2026 Guide (Evolvous)". https://evolvous.com/akamai-guardicore-implementation/ (Retrieved: 2026-08-10T07:43:20Z)
[21] Center for Internet Security. "Akamai Guardicore Segmentation (CIS CyberMarket listing)". https://www.cisecurity.org/services/cis-cybermarket/akamai-guardicore-segmentation (Retrieved: 2026-08-10T07:43:20Z)
[22] NIST CSRC. "NIST CMVP Validated Modules Search (keyword: guardicore)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&CertificateStatus=Active&ValidationYear=0&Keyword=guardicore (Retrieved: 2026-08-10T07:43:20Z)
[23] Enterprise IT World. "Akamai and NVIDIA Deliver Agentless Zero Trust Segmentation". https://www.enterpriseitworld.com/akamai-and-nvidia-deliver-agentless-zero-trust-segmentation-for-critical-infrastructure/ (Retrieved: 2026-08-10T07:43:20Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 23 (kept: 23, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 3, certification_registry: 1, community: 1, third_party_review: 5, vendor_datasheet: 1, vendor_doc: 12
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
