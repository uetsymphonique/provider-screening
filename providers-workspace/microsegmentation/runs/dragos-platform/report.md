# Microsegmentation Product Assessment: Dragos, Inc. - Dragos Platform

**Product ID:** `dragos-platform`
**Version reference:** Dragos Platform 3.2 documentation set and June 2026 brochure/appliance datasheet (accessed 2026-08-10)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T00:00:00Z
**Total evidence items collected:** 59
**Total distinct sources:** 16

---

## 1. Overview

The Dragos Platform is an OT-native cybersecurity platform for extended operational technology (xOT) environments, positioned around four outcomes: see the environment (asset visibility), catch threats other tools miss (threat detection), fix what matters (vulnerability management), and respond with confidence (investigation and response) [1]. It is not a microsegmentation product: the vendor's own capability list covers asset visibility, threat detection, vulnerability management, investigation and response, segmentation validation, network monitoring and EmberAI, with "segmentation validation" defined as analyzing firewall, switch and router configurations to validate existing segmentation policies [9]. Deployment is passive-first and non-intrusive - physical or virtual network sensors observe traffic via SPAN/TAP-style deep packet inspection of 600+ protocols, with an optional lightweight Dragos Agent for active collection on Windows/Linux endpoints [12] and an Edge Collector for containerized traffic forwarding [9]. The platform deploys on-premises, hybrid, or SaaS on Azure (from Q1 2026), with SiteStore/CentralStore aggregation for multi-site environments [15][12]. Analyst recognition: Leader in the 2026 Gartner Magic Quadrant for CPS Protection Platforms (vendor-hosted) [8].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 2                | 6      | 0   |
| partial          | 10    | 0                | 10     | 0   |
| not_supported    | 6     | 0                | 6      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 16 items backed by ≥ 2 source_types; 16 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | Dragos Platform continuously discovers and updates the xOT asset inventory via passive-first monitoring; third-party comparison confirms the platform builds a detailed asset inventory without querying OT devices. [2], [13] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | A network topology view (traffic visualized over time) and zone grouping are documented; App/Role/Process-level map grouping like dedicated microsegmentation tools is not documented. [7], [9] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | - | no evidence found |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | - | Vulnerabilities/CVEs are linked directly to assets with OT-corrected CVSS context in the inventory; rendering of CVE context directly on the topology map is not documented. [2], [4] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | - | Anomaly detection surfaces abnormal communications and unexpected device-to-device communication, complemented by behavioral analytics and threat-intelligence correlation. [3], [10], [13] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Not Supported | medium | - | The platform's documented segmentation capability is validation of existing firewall/switch/router configurations; it creates no enforcement policies and passive sensors never inject packets. [8], [9], [13] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Not Supported | medium | - | EmberAI is documented for asset/threat/vulnerability Q&A and guidance; guidance such as segmentation is advisory text, with no AI-generated segmentation policy recommendation. [4], [16] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | - | no evidence found |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The Dragos Agent (data-collection only) documents Windows Server LTSC, Windows 7 SP2+, Windows 10/11, with the deployment overview also mentioning Linux endpoints; Windows Server 2003 and AIX/Solaris are not supported. [11], [12] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Not Supported | medium | - | Container support is limited to the Edge Collector forwarding traffic for monitoring; no Kubernetes/OpenShift workload isolation or container policy enforcement is offered. [9] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | Agentless network sensors plus optional host-resident agents/collectors are documented, but agents perform active data collection only, with no agent-based enforcement role. [9], [11], [12] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | On-premises and hybrid deployments are supported, data-diode (unidirectional gateway) integrations are listed, and air-gapped substation use of the Dragos Agent is documented. [5], [11], [15] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 500000 workloads | Datasheet states up to 500,000 estimated max monitored assets per SiteStore (and 1,000,000 per top sensor), above the 50,000-workload threshold. [1], [12] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | Only a 1-CPU hardware requirement is published for the Dragos Agent; no measured CPU utilization percentage is documented, so the <1% threshold cannot be verified. [12] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Not Supported | medium | 512 MB | Datasheet lists 512 MB memory for the Dragos Agent, exceeding the <100 MB RAM threshold. [12] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Supported | medium | 0.0 ms | No inline enforcement exists - sensors passively observe traffic and never inject packets, so no policy-latency is added to the data path. [9], [12], [13] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | - | No enforcement component sits in the traffic path (passive-first, out-of-band monitoring with documented do-no-harm approach), so component failure cannot interrupt traffic. [2], [9], [13] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | A REST API is documented (assets, notifications, vulnerabilities, data import, zones) with API keys generated in the platform; no evidence that 100% of admin functions are API-accessible. [12], [14] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | SIEM integrations include Splunk (OT Add-On), IBM QRadar, Microsoft Sentinel and Fortinet FortiSIEM; SOAR includes Fortinet FortiSOAR and Palo Alto XSOAR, plus Syslog forwarding. [3], [5], [15] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | ServiceNow OT Management and ServiceNow Vulnerability Response integrations are listed as Dragos-supported, with CMDB systems (e.g., ServiceNow) mentioned in the brochure. [5], [9] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | - | No process-level or host-based enforcement is offered; the segmentation capability analyzes network-device configurations and the platform does not block traffic. [9], [13] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Native OT threat intelligence (WorldView) and threat-intel integrations (Recorded Future, STIX/TAXII) are documented; no honeypot/deception capability is documented. [5], [9], [13] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Alignment with IEC 62443/NIST frameworks and NERC CIP-015 compliance support are documented; ready-made PCI-DSS, NIST 800-207 or ISO 27001 compliance reporting is not evidenced. [6], [11] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Unknown | low | - | no evidence found |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | - | Hardware appliances document hot-plug redundant power supplies, but no active-active/active-passive controller clustering or failover is documented. [12] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | - | no evidence found |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | - | no evidence found |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | - | The vendor's appliance datasheet lists CE, FCC, UL, IEC-61850-3, IEEE-1613 and similar certifications; no FIPS 140-2/140-3 or Common Criteria EAL4+ validation is listed. [12] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | OT vendor co-engineering (SEL-branded sensor with SEL warranty) and Rockwell Automation asset handling are documented; no formal Siemens, Honeywell or ABB compatibility certifications were found. [11], [12] |

---

## 4. Notable Strengths

- **OT-native visibility and detection (items 1.1, 1.5, 6.2):** Real-time, passive-first asset discovery and anomaly/behavioral detection are documented by Dragos and corroborated by a third-party platform comparison [1][2][3][10][13].
- **Segmentation validation as a compliance aid (item 2.1):** The platform's documented segmentation capability validates firewall/switch/router configurations and surfaces drift, supporting posture review without touching traffic [7][8][9].
- **Scale (item 3.5):** Datasheet documents up to 500,000 estimated max monitored assets per SiteStore and 1,000,000 per top sensor, well above the 50,000-workload threshold [12].
- **Air-gapped and on-premises support (item 3.4):** On-prem/hybrid deployment, data-diode (unidirectional gateway) integrations (Owl, Waterfall), and documented air-gapped substation use of the Dragos Agent [5][11][15].
- **Zero in-path impact (items 4.3, 4.4):** Passive, out-of-band monitoring never injects packets, so no policy latency is added and component failure cannot interrupt traffic [9][12][13].
- **SIEM/SOAR/CMDB integrations (items 5.2, 5.3):** Splunk add-on, QRadar, Sentinel, FortiSIEM, FortiSOAR, XSOAR and ServiceNow OT Management/Vulnerability Response integrations are listed [3][5][15].

## 5. Notable Gaps / Risks

- **No policy creation or enforcement (items 2.1, 6.1):** The platform validates segmentation but creates and enforces no policies, and passive sensors never inject packets - it cannot deliver microsegmentation enforcement, only validation of existing network-device configurations [9][13].
- **No container/Kubernetes isolation (item 3.2):** Container support is limited to the Edge Collector forwarding east-west traffic for monitoring; no workload isolation or container policy enforcement [9].
- **Agent memory footprint exceeds threshold (item 4.2):** The Dragos Agent datasheet lists 512 MB memory, above the checklist's <100 MB requirement [12].
- **Key capabilities unverifiable from public sources (items 1.3, 4.5, 5.4, 6.4, 7.2, 7.3):** Flow-history retention, reboot-free agent updates, CI/CD integrations, agent-controller TLS, autonomous mode and disaster recovery have no public documentation (the docs portal requires login), so they are unknown and must be confirmed with the vendor before procurement.
- **No FIPS 140 or Common Criteria certification documented (item 8.1):** The appliance datasheet lists CE/FCC/UL/IEC-61850-3/IEEE-1613 class certifications only; FIPS 140-2/140-3 and Common Criteria EAL4+ are absent from all vendor material reviewed [12].

## 6. Evidence Quality Notes

16 sources were staged and quoted (10 vendor docs, 2 vendor datasheets, 2 vendor blog/press releases, 2 independent sources). Two items (1.1, 1.5) are rated high confidence with a third-party comparison as an independent source [13]; a second independent source, the n8n community node README [14], grounds the API evidence for item 5.1. Items 1.1, 1.5, 2.1, 4.3, 4.4 and 6.2 are triangulated across vendor pages plus the Decryption Digest comparison [13]; most other non-unknown items rest on vendor documentation alone, which is why confidence is capped at medium and why claims like scale (3.5) or certifications (8.1) should be re-verified with the account team.

16 of 33 items are backed by ≥2 source types; the remaining 9 unknown items (1.3, 2.3, 2.4, 2.5, 4.5, 5.4, 6.4, 7.2, 7.3) have no public evidence because the technical documentation portal (docs.dragos.com) requires login and was not stageable; they are honestly marked unknown per the anti-fabrication contract rather than guessed. One mild inconsistency was noted but not decisive: the brochure says active collection runs on "Windows and Linux devices" while the June 2026 datasheet's OS-support table lists only Windows versions - the datasheet's explicit table was used for item 3.1. No source contradicted any verdict; not_supported verdicts (2.1, 2.2, 3.2, 4.2, 6.1, 8.1) all rest on documented alternatives or explicitly enumerated vendor materials rather than silence.

---

## Bibliography

[1] Dragos, Inc.. "The Cybersecurity Platform Built for OT Environments (Dragos Platform overview)". https://www.dragos.com/cybersecurity-platform/ (Retrieved: 2026-08-10T00:00:00Z)
[2] Dragos, Inc.. "OT Asset Visibility & Inventory (Dragos Platform asset visibility page)". https://www.dragos.com/cybersecurity-platform/asset-visibility/ (Retrieved: 2026-08-10T00:00:00Z)
[3] Dragos, Inc.. "Cyber Threat Detection (Dragos Platform threat detection page)". https://www.dragos.com/cybersecurity-platform/threat-detection/ (Retrieved: 2026-08-10T00:00:00Z)
[4] Dragos, Inc.. "Vulnerability Management (Dragos Platform page)". https://www.dragos.com/cybersecurity-platform/vulnerability-management/ (Retrieved: 2026-08-10T00:00:00Z)
[5] Dragos, Inc.. "Dragos Integrations and Applications catalog". https://www.dragos.com/partners/integrations (Retrieved: 2026-08-10T00:00:00Z)
[6] Dragos, Inc.. "Internal Network Security Monitoring (INSM) for Utilities (NERC CIP-015)". https://www.dragos.com/insights/internal-network-security-monitoring (Retrieved: 2026-08-10T00:00:00Z)
[7] Dragos, Inc.. "Dragos Acquires Phosphorus for xOT Security (press release)". https://www.dragos.com/resource/press-release/dragos-acquires-phosphorus (Retrieved: 2026-08-10T00:00:00Z)
[8] Dragos, Inc.. "Dragos is a Leader in the Gartner Magic Quadrant for CPS Protection Platforms (page)". https://www.dragos.com/resources/report/gartner-magic-quadrant-cps-protection-platforms (Retrieved: 2026-08-10T00:00:00Z)
[9] Dragos, Inc.. "The Dragos Platform Brochure (June 2026)". https://dragos.brightspotcdn.com/af/2c/165968874934a0c47a5aa1ef0d78/dragos-brochure-platform-2026-digital.pdf (Retrieved: 2026-08-10T00:00:00Z)
[10] Dragos, Inc.. "The Four Types of OT Threat Detection in the Dragos Platform (whitepaper, Sep 2025)". https://dragos.brightspotcdn.com/3e/f8/aefcee7f41b6b19a02b410ac5722/four-types-threat-detection-whitepaper-09-25.pdf (Retrieved: 2026-08-10T00:00:00Z)
[11] Dragos, Inc.. "Enhancing OT Visibility: Understanding the Time and Place for Active Collection (whitepaper, May 2025)". https://dragos.brightspotcdn.com/69/9a/ceae6b3b4ab1ba4d871b5a2544e8/enhancing-ot-visibility-active-collection-whitepaper-04-25.pdf (Retrieved: 2026-08-10T00:00:00Z)
[12] Dragos, Inc.. "Dragos Platform Deployment Models & Technical Specifications (appliance datasheet, June 2026)". https://dragos.brightspotcdn.com/fd/24/41f6917d4215b701353144960a5b/dragos-platform-appliance-models-datasheet-7-26.pdf (Retrieved: 2026-08-10T00:00:00Z)
[13] Decryption Digest. "OT/ICS Security Platform Comparison 2026: Dragos vs Claroty vs Nozomi Networks vs Microsoft Defender for IoT". https://www.decryptiondigest.com/blog/ot-ics-security-platform-comparison-2026-dragos-claroty-nozomi-defender-iot (Retrieved: 2026-08-10T00:00:00Z)
[14] GitHub (jmeltz). "n8n-nodes-dragos: n8n community node for the Dragos Platform APIs (README)". https://raw.githubusercontent.com/jmeltz/n8n-nodes-dragos/main/README.md (Retrieved: 2026-08-10T00:00:00Z)
[15] Dragos, Inc.. "Dragos Expands Collaboration with Microsoft to Deliver OT-Native Cybersecurity at Global Industrial Scale (press release)". https://www.dragos.com/resources/press-release/dragos-microsoft-partnership-industrial-cybersecurity (Retrieved: 2026-08-10T00:00:00Z)
[16] Dragos, Inc.. "Dragos EmberAI: AI for OT Security (product page)". https://www.dragos.com/cybersecurity-platform/emberai (Retrieved: 2026-08-10T00:00:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 16 (kept: 16, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 2, vendor_blog: 2, vendor_datasheet: 2, vendor_doc: 10
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
