# Microsegmentation Product Assessment: Trend Micro - Trend Vision One / Cloud One

**Product ID:** `trend-vision-one-cloud-one`
**Version reference:** TrendAI Vision One / Trend Cloud One platform line (2026 product documentation; Workload Security agent lineage from Deep Security 20.x)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:39:54Z
**Total evidence items collected:** 64
**Total distinct sources:** 36

---

## 1. Overview

Trend Vision One (marketed as TrendAI Vision One) is Trend Micro's enterprise cybersecurity platform, and Cloud One is its cloud-security suite spanning Workload Security (agent-based protection of servers, VMs and cloud workloads with Firewall, Intrusion Prevention, Application Control, Integrity Monitoring and Log Inspection), agentless Network Security (IPS filters on cloud traffic), Container Security / Sentry (image scanning and runtime protection), and cloud posture and risk capabilities [2, 3, 9, 14]. Trend positions the platform around proactive security: continuous discovery, attack surface risk management, XDR correlation across endpoints, networks, email, cloud and OT, and global threat intelligence [1, 4, 21]. Deployment shapes include a kernel agent for servers and containers including Red Hat OpenShift [10, 16], agentless cloud-traffic inspection [18, 22], and network sensors feeding XDR detection [24, 25]. It is delivered as SaaS from regional data centers with scheduled maintenance windows [20]. Unlike dedicated microsegmentation vendors, Trend's segmentation capability is exercised through host-based firewall/IPS rules, application control, cloud network filters and XDR visibility rather than a labeled connectivity-map policy engine, which shapes the verdicts below [11, 13].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 1                | 5      | 0   |
| partial          | 15    | 0                | 15     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 12    | 0                | 0      | 12  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 3 items backed by ≥ 2 source_types; 18 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Vision One and Cloud One continuously discover assets and flows: Network Analysis documents Active Asset Discovery from network sensor traffic, the Cloud One product page documents automated discovery of workloads across AWS/Azure/GCP, and the hybrid-cloud page documents continuous discovery and real-time risk assessment; PeerSpot reviewers report complete visibility of cloud assets. [2], [3], [21], [25], [36] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Visualizations exist (impactful visualizations, network inventory dashboard, single-dashboard asset views per PeerSpot), but no staged source documents a connectivity map organized by Application/Environment/Role/Process as the checklist requires. [21], [24], [36] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Retention is configurable for Cyber Risk Exposure Management risk-event data per the Vision One What's New notes, and XDR Data Explorer lets queries specify time ranges, but no staged source states a default retention of 90 days or more for connection flow history. [22], [30] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | CVE context is surfaced in risk views: Vulnerability Management scans/assesses/prioritizes vulnerabilities, RBVM uses a context-aware CVE Impact Score, and ZDI zero-day risk events are shown; but a CVE overlay rendered directly on a connectivity map is not documented. [5], [22], [29] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | Network sensors monitor traffic for XDR detection, XDR for Networks surfaces lateral movement, hidden paths through encrypted traffic and unmanaged-asset risk, and Network Analysis manages detection rules and packet capture - together documenting detection of unrecognized/non-standard flows. [4], [24], [25] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | — | Policies are context-aware with role-based access control and are applied through a management console, but the staged firewall documentation shows enforcement rules filtered by IP/MAC/port; tag/label-based (non-IP) policy definition is not documented in staged sources. [9], [11], [14] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | Workload Security's Recommendation Scan identifies IPS, integrity-monitoring and log-inspection rules that should be applied or removed by scanning installed applications, ports, processes and users; the documentation does not frame this as AI/ML-based policy recommendation. [14], [15] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | — | The Firewall module supports Tap and Inline modes for testing rules before deployment, and rules can use a Log Only action that observes traffic without blocking - equivalent to simulation/dry-run of policy. [11] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found (No staged source documents one-click policy rollback.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No staged source documents inherited or hierarchical policy rules.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | medium | — | The agent platform compatibility table documents support for Windows Server 2003 SP1/SP2 through 2022, Solaris 10/11.4, AIX 6.1-7.3, Red Hat Enterprise Linux, CentOS and Ubuntu families; system requirements list Windows, Linux, Solaris and AIX agent configurations. [10], [16] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | — | Container Security provides policy-based deployment control through native Kubernetes and Amazon ECS integration with an admission-control webhook; the Cloud One page documents Kubernetes posture management, and the compatibility table lists Red Hat OpenShift agent support. [3], [16], [28] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | — | Both deployment shapes are documented: an agent deployed on computers (Application Control, Firewall, Intrusion Prevention, etc.) and agentless Network Security IPS filters plus agentless vulnerability/threat detection for cloud accounts. [9], [18], [22] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | — | Relay-enabled agents distribute software and security updates throughout the internal network, which reduces external connectivity needs, but no staged source explicitly documents fully air-gapped deployment with no Internet access. [9] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Unknown | low | — | no evidence found (No staged source mentions workload count scaling or a workload capacity figure.) |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | — | no evidence found (Staged sources give host RAM/CPU requirements but no agent CPU-overhead figure.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | — | no evidence found (Staged sources give host RAM requirements but no agent memory-footprint figure.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | — | no evidence found (No staged source quantifies network policy latency.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | — | no evidence found (No staged source documents network behavior when the agent crashes or fails.) |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | — | no evidence found (No staged source states whether agent install/update requires a server reboot.) |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | The Automation Center documents Vision One and Cloud One APIs for automation/integration, and vendor GitHub repos provide an API cookbook and a Terraform provider; whether 100% of administrative functions are exposed via REST API is not demonstrated. [31], [33], [34] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | A vendor-published Splunk SOAR connector (v3.0.0) for Vision One is documented, but direct SIEM feeds (Splunk ES/QRadar/Sentinel syslog ingestion) are not documented in staged sources, and a PeerSpot reviewer notes limited ingestion from third-party solutions. [32], [36] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found (No staged source documents a ServiceNow CMDB integration.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | — | A vendor Terraform provider for Vision One and Terraform support for Cloud Risk Management misconfiguration/compliance are documented, and the Cloud One page documents automated CI/CD testing in Code Security; Jenkins/GitLab pipeline specifics are not documented. [3], [22], [34] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | — | Application Control continuously monitors servers and allows/blocks software changes, and Activity Monitoring forwards process/file/network activity to XDR; however the firewall itself filters by IP/MAC/port, so network enforcement is not process-granular. [11], [13], [14] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Threat intelligence is well documented (Threat Intelligence Hub, Network Security threat-intelligence packages, ZDI 450-researcher program), but deception/honeypot detection is not documented for Vision One/Cloud One in staged sources. [5], [18], [26] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Workload Security documents comprehensive auditing/reporting plus PCI DSS and GDPR compliance paths and TLS 1.2, and the Trend Trust Center lists ISO/IEC 27001:2022 and SOC 2 Type II attestations; NIST 800-207 and IEC 62443 report templates are not documented. [6], [17] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | TLS 1.2 is documented for Workload Security and agent heartbeat connections require SSL/TLS; TLS 1.3 and mutual-authentication specifics between agent and controller are not documented in staged sources. [12], [17] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | — | Trend Cloud One maintenance documentation states upgrades and routine maintenance are performed without service impact, with maintenance windows per data-center region and a public service-status page; an active-active/active-passive controller cluster architecture is not documented. [20] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (No staged source documents policy enforcement continuing when the controller is unreachable.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (No staged source documents disaster-recovery site sync or backup/restore for Cloud One.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | The Trend Trust Center documents FIPS 140-2-compliant modes for Deep Security (Workload Security lineage) crypto modules and Common Criteria certification at EAL2+ level; FIPS 140-3 and CC EAL4+ are not documented. [6] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No staged source documents Siemens/Honeywell/ABB compatibility certifications for Cloud One.) |

---

## 4. Notable Strengths

- **Broad agent OS coverage (item 3.1):** the Workload Security agent supports Windows Server 2003 through 2022, Solaris 10/11.4, AIX 6.1-7.3, RHEL, CentOS, Ubuntu, SUSE and Oracle Linux per the official compatibility table [10, 16].
- **Container-native protection (item 3.2):** Container Security enforces policy via a Kubernetes/Amazon ECS admission-control webhook, with Red Hat OpenShift agent support documented [3, 16, 28].
- **Agent-based plus agentless (item 3.3):** both a host agent (Firewall, IPS, Application Control) and agentless Network Security / agentless vulnerability detection are documented [9, 18, 22].
- **Policy simulation before enforcement (item 2.3):** the Firewall module's Tap and Inline modes plus a Log Only rule action let teams validate rules without blocking traffic [11].
- **Real-time discovery and network visibility (items 1.1, 1.5):** Active Asset Discovery from network sensors and XDR network detection are documented, corroborated by PeerSpot reviewers reporting complete cloud asset visibility [24, 25, 36].
- **Automation surface (items 5.1, 5.4):** an Automation Center, Vision One API cookbook and an official Terraform provider are published [31, 33, 34].

## 5. Notable Gaps / Risks

- **No connectivity map by App/Env/Role/Process (item 1.2):** visualizations are dashboards and asset views, not a flow-oriented map; a buyer needing flow maps for policy design should confirm this with the vendor or pair with a mapping tool.
- **Numeric thresholds unverifiable (items 1.3, 3.5, 4.1-4.3):** staged sources publish no flow-history retention of 90+ days, no workload-count scale figure, no agent CPU/RAM overhead and no policy latency figures; 1.3 is Partial (retention is configurable), the rest are Unknown until vendor figures are provided.
- **Fail-safe and autonomous behavior undocumented (items 4.4, 7.2):** no staged source states what happens to network traffic if the agent crashes or if the controller is unreachable; these are load-bearing for production microsegmentation and should be verified with Trend.
- **Policy-management depth unproven (items 2.4, 2.5):** no evidence of one-click rollback or inherited/hierarchical rules; the Workload Security policies/tags documentation was unavailable during the assessment window.
- **SIEM/CMDB integration thin (items 5.2, 5.3):** only a Splunk SOAR connector is documented and a PeerSpot reviewer notes limited third-party ingestion; no ServiceNow CMDB evidence was found.
- **Certifications below checklist target (item 8.1):** FIPS 140-2-compliant crypto modes and Common Criteria EAL2+ are documented for Deep Security (Workload Security lineage), but not FIPS 140-3 or CC EAL4+ [6].

## 6. Evidence Quality Notes

64 evidence entries were collected across 36 staged sources (35 vendor docs, 1 community review site). Three items (1.1, 1.2, 5.2) were triangulated across at least two source types by including PeerSpot user reviews; the remaining non-unknown items rely on vendor documentation only, so their confidence is capped at medium per the project's validator rule. The PeerSpot reviews independently corroborated asset discovery and dashboard visibility for items 1.1 and 1.2 and added a counterpoint on limited third-party ingestion for item 5.2.

Several docs.trendmicro.com articles (policies, tags, relay, agent deployment, IPS, backup/restore, communication/TLS, SIEM, ServiceNow, data retention, Conformity help, integrations) consistently returned maintenance shells during the assessment window and could not be staged; items resting on that content were marked Unknown rather than inferred, and no source contradicted another where evidence did exist. Marketing pages and documentation agreed wherever they overlapped, and the documentation took precedence for verdicts.

---

## Bibliography

[1] Trend Micro. "Trend Vision One platform (product page)". https://www.trendmicro.com/en_us/business/products/one-platform.html (Retrieved: 2026-08-10T17:39:00Z)
[2] Trend Micro. "Cloud Workload Security solution page". https://www.trendmicro.com/en_us/business/products/endpoint-security/workload-security.html (Retrieved: 2026-08-10T17:39:00Z)
[3] Trend Micro. "Cloud One - hybrid cloud security (product page)". https://www.trendmicro.com/en_us/business/products/hybrid-cloud.html (Retrieved: 2026-08-10T17:39:00Z)
[4] Trend Micro. "Trend Vision One XDR for Networks (product page)". https://www.trendmicro.com/en_us/business/products/network/detection-response.html (Retrieved: 2026-08-10T17:39:00Z)
[5] Trend Micro. "Risk-based Vulnerability Management (product page)". https://www.trendmicro.com/en_us/business/products/cyber-risk-exposure-management/risk-based-vulnerability-management.html (Retrieved: 2026-08-10T17:39:00Z)
[6] Trend Micro. "Trust Center - Compliance". https://www.trendmicro.com/en_us/about/trust-center/compliance.html (Retrieved: 2026-08-10T17:39:00Z)
[7] Trend Micro. "Trust Center - Privacy". https://www.trendmicro.com/en_us/about/trust-center/privacy.html (Retrieved: 2026-08-10T17:39:00Z)
[8] Trend Micro. "Trust Center - Security Practices". https://www.trendmicro.com/en_us/about/trust-center/security-practices.html (Retrieved: 2026-08-10T17:39:00Z)
[9] Trend Micro. "Cloud One Workload Security - About the components". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-components (Retrieved: 2026-08-10T17:39:00Z)
[10] Trend Micro. "Cloud One Workload Security - System requirements". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-system-requirements (Retrieved: 2026-08-10T17:39:00Z)
[11] Trend Micro. "Cloud One Workload Security - About Firewall". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-firewall (Retrieved: 2026-08-10T17:39:00Z)
[12] Trend Micro. "Cloud One Workload Security - Offline agent". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-agent-offline (Retrieved: 2026-08-10T17:39:00Z)
[13] Trend Micro. "Cloud One Workload Security - About Application Control". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-application-control (Retrieved: 2026-08-10T17:39:00Z)
[14] Trend Micro. "Cloud One Workload Security - Protection modules". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-protection-modules (Retrieved: 2026-08-10T17:39:00Z)
[15] Trend Micro. "Cloud One Workload Security - Classic recommendation scan". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-recommendation-scan (Retrieved: 2026-08-10T17:39:00Z)
[16] Trend Micro. "Cloud One Workload Security - Agent platform compatibility". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-agent-compatibility (Retrieved: 2026-08-10T17:39:00Z)
[17] Trend Micro. "Cloud One Workload Security - About compliance". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-workload-security-compliance (Retrieved: 2026-08-10T17:39:00Z)
[18] Trend Micro. "Cloud One Network Security - IPS Filters overview". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-network-security-Filters_overview (Retrieved: 2026-08-10T17:39:00Z)
[19] Trend Micro. "Cloud One Sentry - About Sentry (container image security)". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-sentry-about-sentry (Retrieved: 2026-08-10T17:39:00Z)
[20] Trend Micro. "Trend Cloud One - Maintenance schedule". https://docs.trendmicro.com/en-us/documentation/article/trend-micro-cloud-one-main-maintenance-schedule (Retrieved: 2026-08-10T17:39:00Z)
[21] Trend Micro. "TrendAI Vision One - About (product overview)". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-trend-Vision-One-About (Retrieved: 2026-08-10T17:39:00Z)
[22] Trend Micro. "TrendAI Vision One - Attack Surface Risk Management (What's New)". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-attack-surface-risk-management (Retrieved: 2026-08-10T17:39:00Z)
[23] Trend Micro. "TrendAI Vision One - APIs (Attack Surface Discovery)". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-apis (Retrieved: 2026-08-10T17:39:00Z)
[24] Trend Micro. "TrendAI Vision One - Network Inventory". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-network-inventory (Retrieved: 2026-08-10T17:39:00Z)
[25] Trend Micro. "TrendAI Vision One - Network Analysis Configuration". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-network-analysis-configuration (Retrieved: 2026-08-10T17:39:00Z)
[26] Trend Micro. "TrendAI Vision One - Threat Intelligence Hub". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-threat-insights (Retrieved: 2026-08-10T17:39:00Z)
[27] Trend Micro. "TrendAI Vision One - Forensics". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-forensics (Retrieved: 2026-08-10T17:39:00Z)
[28] Trend Micro. "TrendAI Vision One - Container Security". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-container-security (Retrieved: 2026-08-10T17:39:00Z)
[29] Trend Micro. "TrendAI Vision One - Vulnerability Management". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-vuln-management-app (Retrieved: 2026-08-10T17:39:00Z)
[30] Trend Micro. "TrendAI Vision One - XDR Data Explorer". https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-search-app (Retrieved: 2026-08-10T17:39:00Z)
[31] Trend Micro. "Trend Micro Automation Center (API portal)". https://automation.trendmicro.com/ (Retrieved: 2026-08-10T17:39:00Z)
[32] Trend Micro. "Trend Vision One for Splunk SOAR (connector README)". https://raw.githubusercontent.com/trendmicro/v1-connector-splunk-soar/main/README.md (Retrieved: 2026-08-10T17:39:00Z)
[33] Trend Micro. "tm-v1-api-cookbook (README)". https://raw.githubusercontent.com/trendmicro/tm-v1-api-cookbook/main/README.md (Retrieved: 2026-08-10T17:39:00Z)
[34] Trend Micro. "Terraform Provider for Vision One (README)". https://raw.githubusercontent.com/trendmicro/terraform-provider-vision-one/main/README.md (Retrieved: 2026-08-10T17:39:00Z)
[35] Trend Micro. "Cloud One Workload Security MITRE ATT&CK policies (README)". https://raw.githubusercontent.com/trendmicro/c1ws-mitre-policy/main/README.md (Retrieved: 2026-08-10T17:39:00Z)
[36] PeerSpot. "PeerSpot - TrendAI Vision One Cloud Security reviews". https://www.peerspot.com/products/trend-micro-cloud-one-workload-security-reviews (Retrieved: 2026-08-10T17:39:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 36 (kept: 36, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, vendor_doc: 35
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
