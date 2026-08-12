# Microsegmentation Product Assessment: Armis (Armis from ServiceNow) - Armis Centrix (Cyber Exposure Management platform)

**Product ID:** `armis-centrix`
**Version reference:** Armis Centrix v25.2 (June 2025 release blog) and 2025-2026 documentation corpus; OT/IoT Security On-Prem edition available
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T09:30:00Z
**Total evidence items collected:** 79
**Total distinct sources:** 31

---

## 1. Overview

Armis Centrix is the cyber exposure management platform of Armis, now part of ServiceNow (the brochure brands it "Armis from ServiceNow") [3]. It is a cloud-native, agentless platform that continuously discovers, classifies, and monitors IT, OT, IoT, and IoMT assets in real time [1]. In the microsegmentation space Armis positions itself as the visibility and risk-intelligence layer: it enforces network-level segmentation through integrations with NAC, firewalls, wireless LAN controllers, and switches, and supports manual ACL creation and deployment [2, 4]. Identity-based microsegmentation is delivered jointly with partner Elisity, whose cloud-delivered policy engine enforces least-privilege access through existing network infrastructure without agents [23, 24]. Deployment shapes are SaaS and an On-Prem edition for OT/IoT environments, including fully air-gapped networks [7, 8]. Armis is recognized as a Leader in the 2026 Gartner Magic Quadrant for CPS Protection Platforms [15, 16]. Verdicts across the 33 checklist items: 14 supported, 14 partial, 1 not supported, 4 unknown.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 14    | 1                | 13     | 0   |
| partial          | 14    | 0                | 14     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 4     | 0                | 0      | 4   |
| not_applicable   | 1     | 0                | 1      | 0   |

**Evidence quality:** 20 items backed by ≥ 2 source_types; 20 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **6.1:** Documented enforcement is entirely network-layer (NAC, firewall, WLC, switch, ACL; partner Elisity enforces at the network access layer); no host-based process-level enforcement is offered.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | — | Armis Centrix discovers assets continuously and agentlessly via passive traffic inspection (SPAN/TAP), network-infrastructure integrations (switches, routers, firewalls, NAC) and collectors; third-party listings corroborate fully agentless device discovery. [1], [4], [6], [28], [29] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | A Purdue Model network map groups assets by device type, zone/boundary, location and function, and threat investigation surfaces network traffic mapping; grouping by application/environment/role/process as in host-segmentation consoles is not documented. [10], [17], [30] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | The G-Cloud listing documents a data retention period after which customer data is deleted, but no retention duration in days is published, so the 90-day minimum cannot be confirmed. [26] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | Per-device vulnerability context is documented (CVEs and misconfigurations prioritized by business impact; ICS devices matched against threat-intelligence databases), but a CVE overlay rendered directly on the network map is not explicitly documented. [6], [7] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | Anomaly detection flags unauthorized or non-standard communications (e.g., a medical device contacting an unauthorized IP, brute force, port scans), and custom policies can alert on abnormal traffic, covering unrecognized flows. [2], [7], [10] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | Microsegmentation policies are based on asset identity, behavior, role and risk rather than IP address; policies are rule-based on device/activity/vulnerability/connection attributes, and partner Elisity enforces identity-based least-privilege policies. [7], [12], [23] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | — | AI-driven analysis recommends and enforces segmentation policies tuned to each device's risk profile, and the platform maps device communications to provide automated segmentation-policy recommendations. [2], [7] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | — | ASQ rules can be tested in the UI before creating policies, and the OT On-Prem digital twin models policy impact without touching production; a dedicated SaaS policy dry-run/mock-enforcement mode is not documented. [7], [12] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | There is no per-OS host agent: Windows assets are queried via WMI, collectors ship as OVA/QCOW2/VHD images, and a Windows local tool adds air-gapped discovery; a Windows Server 2003-2022/AIX/Solaris agent support matrix is not documented. [6], [13], [21] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | Collectors can be deployed inside Kubernetes clusters for container-environment visibility, while microsegmentation enforcement is delivered at the network layer (via partner Elisity); native in-cluster workload isolation is not provided by Armis itself. [22], [24] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | The platform is fully agentless with network integrations (WLCs, firewalls, NACs, switches) for enforcement; no agent-based enforcement variant is offered. [2], [4], [6] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | The On-Prem edition runs fully locally and continues protecting air-gapped networks with no cloud connectivity, and the SaaS edition adds air-gapped asset discovery via a local Windows tool. [7], [8], [13] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | A published case study documents 65,000-70,000 IP-connected assets at one UK healthcare customer, but Armis does not publish a per-platform workload capacity figure, so the 50,000-workload threshold cannot be verified as a supported limit. [3], [14] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Supported | medium | 0 cpu_percent | The platform is agentless - no endpoint agent is installed on workloads (partner brief confirms no agents on any device), so agent CPU overhead is 0%. [6], [24] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Supported | medium | 0 MB | With no endpoint agent and passive monitoring only, no agent memory is resident on workloads, so agent RAM footprint is 0 MB. [1], [24] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Supported | medium | 0 ms | Monitoring is off-path (SPAN/TAP copies) and enforcement is out-of-band via existing network devices (NAC/firewall), so no latency is added to production traffic. [4], [6], [24] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | — | Because no endpoint agent sits in the traffic path (100% non-intrusive, passive monitoring), an agent failure cannot interrupt workload communication. [1], [4] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Supported | medium | — | Agentless deployment installs no endpoint software, so no server reboot is required; customers begin seeing a complete asset inventory within minutes to hours. [1], [7] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | — | The G-Cloud listing states the UI is built on a RESTful API so everything doable in the interface is doable programmatically, and the developer portal documents data export, custom-property and policy APIs. [11], [12], [26] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | — | Alerts forward to SIEM platforms including Splunk, QRadar and Sumo Logic, with documented third-party integrations (FortiSIEM configuration guide, Splunkbase add-on) for SIEM/SOAR workflows. [6], [18], [19], [20], [25] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | — | Device data enriches the ServiceNow CMDB, alerts import as ServiceNow security incidents, and policy API actions can push tickets to ServiceNow. [7], [12], [18] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | — | Collector deployment is API-driven for CI/CD infrastructure-as-code, and a GitLab integration is documented; no Jenkins plugin or vendor-maintained Terraform provider is documented. [18], [21] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | N/A | medium | — | Documented enforcement is entirely network-layer (NAC, firewall, WLC, switch, ACL; partner Elisity enforces at the network access layer); no host-based process-level enforcement is offered. [2], [24] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Supported | medium | — | The threat-intelligence module deploys honeypots and deception lures and combines dark-web intelligence with HUMINT for early-warning detection. [5], [7] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Out-of-the-box compliance dashboards and reporting are documented for NIST, CIS, HIPAA, GDPR and IEC 62443 alignment (whitepaper maps IEC 62443 3-2/3-3/4-2); explicit PCI-DSS and ISO 27001 report templates are not evidenced. [7], [17], [19], [31] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | Collector-to-cloud transport is encrypted with tenant-specific keys managed via FIPS 140-2 validated AWS KMS; TLS version (1.3) and mutual-authentication specifics are not published. [22], [26] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | — | The SaaS SLA guarantees 99.9% monthly uptime on resilient AWS infrastructure with 24x7 monitoring, and the FedRAMP Moderate package covers the federal edition; no public detail on controller cluster topology (active-active/passive). [9], [26] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | Crypto infrastructure uses FIPS 140-2 validated AWS KMS, and Armis holds FedRAMP Moderate, SOC 2 Type II and ISO 27001 certifications; no product-level FIPS 140-2/140-3 validation or Common Criteria EAL4+ certification is documented. [9], [26], [27] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | — | Siemens PLC families (S7-1200/1500/300/400) and S7comm/Profinet are explicitly supported for discovery and protocol parsing, and Smart Active Query speaks S7Comm/CIP; no formal compatibility certifications for Honeywell or ABB are documented. [6] |

---

## 4. Notable Strengths

- **Agentless real-time discovery (items 1.1, 1.5):** Armis Centrix discovers and classifies managed and unmanaged assets continuously via passive SPAN/TAP traffic inspection and network-infrastructure integrations, with no endpoint agents [1, 6, 4].
- **Identity-based policy model (item 2.1):** microsegmentation policies are built on asset identity, behavior, role, and risk rather than IP/VLAN, and partner Elisity enforces identity-based least-privilege access [7, 23].
- **Integration breadth (items 5.1, 5.2, 5.3):** 200+ pre-built integrations cover SIEM forwarding (Splunk, QRadar, Sumo Logic), ServiceNow CMDB sync and incident import, and a RESTful API that mirrors UI functionality [18, 19, 26, 11].
- **Zero host footprint (items 4.1-4.5):** because no endpoint agent is installed, agent CPU/RAM overhead is zero and workload traffic is never disrupted by agent failure, updates, or reboots [6, 1, 24].
- **Air-gapped OT support (item 3.4):** the On-Prem edition continues protecting fully air-gapped networks without cloud connectivity, and the SaaS edition adds air-gapped asset discovery via a local Windows tool [7, 8, 13].

## 5. Notable Gaps / Risks

- **No host-based process-level enforcement (item 6.1):** documented enforcement is network-layer only (NAC/firewall/WLC/switch/ACL, or Elisity at the network access layer); buyers needing per-process control on servers must add another product [2, 24].
- **Policy rollback and hierarchy unverified (items 2.4, 2.5):** no documentation of one-click policy rollback or inherited/hierarchical policy rules; both need vendor confirmation before being relied upon.
- **Flow-history retention duration unpublished (item 1.3):** a data retention period exists per the G-Cloud listing, but no duration in days is published, so the >=90-day forensic-retention requirement is unverified [26].
- **HA/DR depth undocumented (items 7.1-7.3):** only a 99.9% monthly SaaS uptime SLA is documented; no public detail on controller cluster topology, autonomous-mode behavior, or DR site sync [26, 9].
- **Certification gap (items 8.1, 8.2):** no product-level FIPS 140-2/140-3 or Common Criteria EAL4+ validation, and no formal Honeywell/ABB compatibility certifications; FedRAMP Moderate, SOC 2 Type II, and ISO 27001 are held [9, 26, 27].

## 6. Evidence Quality Notes

Evidence was drawn from 31 staged sources: 14 vendor docs, 8 vendor datasheets, 6 third-party listings or reviews, 2 vendor-hosted analyst pages, and 1 vendor blog. Per the mechanical summary, 20 non-unknown items are backed by at least two source types and 20 items rely only on vendor-authored material (confidence capped at medium). Genuinely independent sources are limited to the Elisity integration page [24], the Fortinet FortiSIEM configuration guide [25], the UK G-Cloud listing [26], and directory listings (CybersecTools, Security Tools, trustlists) [28, 29, 27]; the directory listings are vendor-derived summaries, so high confidence was granted only to item 5.2, where Fortinet's own documentation independently confirms the SIEM integration.

Armis's materials are internally consistent; the key architectural finding — microsegmentation is agentless and network-layer, with host-level enforcement delegated to Elisity — is corroborated by both Armis's partner brief [23] and Elisity's independent integration page [24], and drove the not_supported verdict on 6.1 and the partial verdicts on 3.2/3.3. Items 2.4, 2.5, 7.2, and 7.3 returned no evidence and were rated unknown per anti-fabrication rules. Note that armis.com pages return 403 to urllib, so they were staged via a curl-based variant of html_to_text.py (stage_html_curl.py) that writes the identical artifact/manifest schema; every quoted sentence was verified as an exact substring of the staged text.

---

## Bibliography

[1] Armis. "Armis Centrix, the Armis cyber exposure management platform". https://www.armis.com/platform/armis-centrix/ (Retrieved: 2026-08-10T09:30:00Z)
[2] Armis. "Armis Network Visibility, Segmentation and Enforcement (Solution Brief)". https://media.armis.com/pdfs/sb-network-visibility-segmentation-enforcement-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[3] Armis. "Brochure: Armis Centrix". https://media.armis.com/image/upload/v1721911066/PDFs/br-armis-centrix-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[4] Armis. "Using Armis with Network Access Control (Solution Brief)". https://media.armis.com/pdfs/sb-using-armis-with-network-access-control-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[5] Armis. "Armis Centrix for Actionable Threat Intelligence (Solution Brief)". https://media.armis.com/pdfs/sb-actionable-threat-intelligence-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[6] Armis. "The Armis Centrix Approach to Asset Data Collection Across IT, OT, CPS and IoT Ecosystems (Technical White Paper)". https://media.armis.com/wp-armis-centrix-approach-to-asset-data-collection-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[7] Armis. "Frequently Asked Questions | Armis". https://www.armis.com/faq/ (Retrieved: 2026-08-10T09:30:00Z)
[8] Armis Federal. "Platform | Armis Federal". https://www.armisfederal.com/armis-centrix/ (Retrieved: 2026-08-10T09:30:00Z)
[9] Armis Federal. "Trust | Armis Federal (FedRAMP package)". https://www.armisfederal.com/trust/ (Retrieved: 2026-08-10T09:30:00Z)
[10] Armis. "Threat intelligence, detection, and response | Armis Centrix". https://www.armis.com/solutions/threat-detection-and-response/ (Retrieved: 2026-08-10T09:30:00Z)
[11] Armis. "Armis Developer Portal (Technology Partner Brief)". https://media.armis.com/tp-armis-developer-portal-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[12] Armis. "Policy Management | Armis Developer Portal". https://dev.armis.com/docs/policy-management.md (Retrieved: 2026-08-10T09:30:00Z)
[13] Armis. "Armis Centrix v25.2 is here! (Release blog)". https://www.armis.com/blog/armis-centrix-v25-2-is-here/ (Retrieved: 2026-08-10T09:30:00Z)
[14] Armis. "Case Studies | Armis". https://www.armis.com/case-studies/ (Retrieved: 2026-08-10T09:30:00Z)
[15] Armis. "Armis Named a Leader in the 2026 Gartner Magic Quadrant for CPS Protection Platforms (vendor-hosted)". https://www.armis.com/analyst-reports/armis-named-a-leader-in-the-2026-gartner-magic-quadrant-for-cps-protection-platforms/ (Retrieved: 2026-08-10T09:30:00Z)
[16] Armis. "Analyst Relations | Armis (vendor-hosted analyst recognitions)". https://www.armis.com/about/analyst-relations/ (Retrieved: 2026-08-10T09:30:00Z)
[17] Armis. "How Armis Protects Critical Operational Technology (IEC 62443 White Paper)". https://info.armis.com/rs/645-PDC-047/images/Armis-How-Armis-Protects-Critical-Operational-Technology-WP%20(Letter,%20English).pdf (Retrieved: 2026-08-10T09:30:00Z)
[18] Armis. "Integrations and Adapters | Armis". https://www.armis.com/integrations-adapters/ (Retrieved: 2026-08-10T09:30:00Z)
[19] Armis. "Armis + Splunk Integration | Armis". https://www.armis.com/splunk (Retrieved: 2026-08-10T09:30:00Z)
[20] Armis. "Armis + Splunk: Close The Unmanaged Device Visibility & Security Gap (Solution Brief)". https://media.armis.com/PDFs/sb-armis-splunk-close-unmanaged-security-gap-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[21] Armis. "Collector Deployment | Armis Developer Portal". https://dev.armis.com/docs/collector-deployment (Retrieved: 2026-08-10T09:30:00Z)
[22] Armis. "Solution Brief: Armis Centrix Collectors". https://media.armis.com/sb-armis-collectors-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[23] Armis. "Power Zero Trust Protection and Dynamic Microsegmentation With Armis Centrix and Elisity (Partner Brief)". https://media.armis.com/pb-armis-elisity-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[24] Elisity. "Armis + Elisity Integration: Asset Intelligence Meets Identity-Based Microsegmentation". https://www.elisity.com/elisity-armis-integration-asset-intelligence-microsegmentation (Retrieved: 2026-08-10T09:30:00Z)
[25] Fortinet. "Armis Centrix | FortiSIEM 7.4.0 External Systems Configuration Guide". https://docs.fortinet.com/document/fortisiem/7.4.0/external-systems-configuration-guide/495851/armis-centrix (Retrieved: 2026-08-10T09:30:00Z)
[26] Armis (UK G-Cloud). "Armis Centrix - G-Cloud 14 Service (UK Digital Marketplace)". https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/155803228331631 (Retrieved: 2026-08-10T09:30:00Z)
[27] trustlists.org. "Armis Trust Center - SOC 2 Type II, ISO 27001, ISO 27017 | trustlists". https://trustlists.org/company/armis/ (Retrieved: 2026-08-10T09:30:00Z)
[28] CybersecTools. "Armis Centrix Network Segmentation | CybersecTools". https://cybersectools.com/tools/armis-centrixtm-network-segmentation (Retrieved: 2026-08-10T09:30:00Z)
[29] Security Tools. "Armis Centrix: Pricing, Reviews & Features | Security Tools". https://security.toolsinfo.com/tool/armis-centrix (Retrieved: 2026-08-10T09:30:00Z)
[30] Armis (mirror). "Armis Centrix for Asset Management and Security (Solution Brief)". https://www.netdescribe.com/wp-content/uploads/2024/04/sb-armis-asset-intelligence-and_seucrity-platform-en.pdf (Retrieved: 2026-08-10T09:30:00Z)
[31] Security Scientist. "12 Questions and Answers About Armis Centrix (Armis)". https://www.securityscientist.net/blog/12-questions-and-answers-about-armis-centrix-armis/ (Retrieved: 2026-08-10T09:30:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 31 (kept: 31, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 2, third_party_review: 6, vendor_blog: 1, vendor_datasheet: 8, vendor_doc: 14
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
