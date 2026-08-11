# Microsegmentation Product Assessment: Claroty - Claroty xDome / Continuous Threat Detection (CTD)

**Product ID:** `claroty-xdome-ctd`
**Version reference:** Claroty xDome (SaaS, current platform line) and Claroty CTD (on-premise); staged materials span CTD v4.2.3 - v5.x and xDome 2022-2026 datasheets/overviews
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:01:47Z
**Total evidence items collected:** 99
**Total distinct sources:** 30

---

## 1. Overview

Claroty xDome and Claroty Continuous Threat Detection (CTD) are the SaaS and on-premise deployment shapes of the Claroty Platform, an agentless cyber-physical systems (CPS) security platform that discovers, profiles and monitors OT, IoT and IT assets over 450+ industrial protocols [1][2][11]. Visibility is delivered through passive network monitoring, the Windows-based Claroty Edge host collector, and CMDB/asset-tool enrichment; the platform is deployed via cloud SaaS (xDome) or on-premise servers/sensors (CTD) [1][9][27]. In the microsegmentation space Claroty positions itself as the visibility and policy-intelligence layer: it automatically builds zones from asset behavior, recommends segmentation policies (ML-driven), lets teams simulate policy impact before enforcement, and pushes enforceable policies to existing firewalls, switches and NAC devices rather than deploying enforcement agents on workloads [2][4][7][14]. Enforcement is therefore out-of-band: policy runs on the customer's network infrastructure while Claroty monitors policy compliance and alerts on deviations [8][12]. The platform is a Leader in the 2026 Gartner Magic Quadrant for CPS Protection Platforms [1] and integrates with SIEM, SOAR, CMDB and industrial engineering ecosystems (Siemens, Honeywell, ABB, Rockwell) [10][17][25].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 13    | 8                | 5      | 0   |
| partial          | 9     | 0                | 9      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 6     | 0                | 0      | 6   |
| not_applicable   | 4     | 0                | 4      | 0   |

**Evidence quality:** 23 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** No host agent runs on protected workloads: monitoring is agentless passive collection with an optional Windows-based Edge collector, so an agent CPU-consumption figure is not applicable.
- **4.2:** The platform is agentless for workloads (passive sensors, Windows Edge collector, agentless secure access), so an agent RAM-footprint metric does not apply.
- **4.4:** There is no workload agent whose failure could interrupt traffic: visibility is passive/out-of-band and enforcement executes on existing firewall/NAC infrastructure.
- **4.5:** No agent is installed or updated on workloads (agentless deployment; Windows Edge collector is a separate collector host), so reboot-free agent rollout is not a meaningful metric.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | The platform continuously discovers CPS assets across OT, IT and IoT environments through passive monitoring, Claroty Edge and integration enrichment; the xDome product page, datasheet, CTD product page and an AWS guidance document all document automated real-time discovery. [1], [2], [11], [12], [14] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | medium | — | The platform provides communication mapping and visualization that underpins segmentation, and the exposure views are organized by production lines, systems and business purpose; zones provide a visualized baseline of normal network behavior. [1], [4], [6], [11] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Claroty documents data-retention and log-retention policies (retention for regulatory/forensic needs) but publishes no specific duration for connection-flow history, so the ≥90-day requirement is not confirmed. [23] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | CVE, KEV/EPSS and Team82 findings are correlated to each asset and surfaced in exposure/risk views, but the sources do not explicitly state that vulnerability context renders directly on the network communication map. [2], [11], [14], [19] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | — | Behavioral baselining and multiple detection engines alert in real time to anomalous, unknown and emerging communications, and CTD adds cross-zone communication violation alerts; a third-party review confirms real-time anomaly flagging. [2], [3], [4], [11], [14] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | — | Policies are defined over logical zones/security zones built from asset attribute profiles and imported into firewalls/NACs as tags and device lists; a third-party review notes recommendations reflect operational context rather than IP subnets. [5], [7], [9], [14], [30] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | high | — | AI-powered device clustering and behavioral baselining automatically produce recommended segmentation zones and communication policies; the vendor and a third-party review both document ML-driven recommendations. [1], [2], [4], [14] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | — | Recommended policies can be simulated to demonstrate network impact before enforcement and tested before being copied into firewalls; the platform also continuously tests policies with real-time alerting (vendor documentation). [1], [2], [4], [8] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found (No source documents a one-click rollback capability for segmentation policies.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No source documents inherited/hierarchical rule structures for segmentation policies.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | Platform components run on a Windows-based Edge collector and a Linux-based ClarotyOS server/sensor, and asset discovery is protocol-based across OS types; explicit support for AIX/Solaris hosts or the full Windows Server 2003-2022 span is not documented. [5], [27], [29] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | — | no evidence found (No source documents native Kubernetes/OpenShift workload isolation; xDome's SaaS itself runs on Amazon EKS, which is not workload-side support.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | — | The platform combines agentless passive network sensors and out-of-band enforcement with Claroty Edge, a Windows-based host collector for localized asset discovery; no workload enforcement agent is involved. [2], [4], [5], [14], [27], [30] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | The Edge collector and xDome federal deployments explicitly support air-gapped environments, and the platform offers on-premise deployment (CTD) as well as SaaS (vendor documentation). [5], [9], [19], [27] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scale is described qualitatively (SaaS 'designed with scalability in mind'; 40M+ CPS assets secured platform-wide, multi-site deployments from a single dashboard); no per-deployment figure of 50,000+ workloads is published. [1], [4], [14] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | No host agent runs on protected workloads: monitoring is agentless passive collection with an optional Windows-based Edge collector, so an agent CPU-consumption figure is not applicable. [2], [5], [27] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | The platform is agentless for workloads (passive sensors, Windows Edge collector, agentless secure access), so an agent RAM-footprint metric does not apply. [5], [22] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Collection is passive and out-of-band (SPAN/TAP mirroring, metadata forwarded to SaaS) with 'zero impact on industrial processes' claimed, but no numeric latency figure is published. [2], [5], [12] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | There is no workload agent whose failure could interrupt traffic: visibility is passive/out-of-band and enforcement executes on existing firewall/NAC infrastructure. [5], [27] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No agent is installed or updated on workloads (agentless deployment; Windows Edge collector is a separate collector host), so reboot-free agent rollout is not a meaningful metric. [5], [22] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | high | — | xDome exposes a REST API (v1) with API users/tokens (base URL api.claroty.com), documented independently by Elastic and Synqly, and CTD's Swagger-based API Explorer exposes all supported calls. [16], [18], [24], [28] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | — | Ready-made SIEM/SOAR integrations cover Splunk, Microsoft Sentinel, IBM QRadar, AWS Security Hub/Security Lake, Rapid7 InsightIDR and Palo Alto Cortex XSOAR, plus Syslog. [10], [12], [14], [16] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | high | — | A joint Claroty-ServiceNow integration and the Service Graph Connector import Claroty asset data into ServiceNow; a third-party review confirms ServiceNow ITSM ticketing integration. [10], [14], [17] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found (No source documents CI/CD pipeline integrations (Jenkins/GitLab/Terraform) for DevSecOps.) |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | — | no evidence found (CTD provides industrial process-value visibility, but no source documents access enforcement at the OS process level.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Threat intelligence (Team82 Threat Center, Exposure Scenarios, weekly detection updates, MITRE ATT&CK for ICS mapping) is well documented, but honeypot/deception detection integration is not found in the reviewed sources. [2], [3], [20] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Claroty maps xDome/CTD to ISA/IEC-62443-3-3 SR requirements, holds ISO/IEC 27001 and SOC 2 certifications, aligns with the NIST CSF and is pursuing FedRAMP High; PCI-DSS-specific compliance reporting is not documented. [6], [19], [20], [21] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | Sensor-to-platform transport is encrypted (TLS and IPsec for collection servers; compressed/encrypted sensor data; TLS/SSL in transit for SaaS), but TLS 1.3 and mutual-TLS specifics are not documented. [12], [22], [23], [29] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | — | The SaaS platform runs on AWS managed services (EKS, RDS with disaster recovery, S3 backups, multi-AZ VPCs) implying managed high availability, but no explicit active-active/active-passive controller cluster configuration is documented. [12], [13], [23] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (Enforcement is off-box via firewall/NAC integrations, but no source states that policy enforcement continues autonomously if the Claroty platform loses connectivity.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | — | AWS documentation describes RDS disaster recovery and S3 backups for xDome, and Claroty's security FAQ documents regular encrypted backups in geographically separate locations plus a disaster recovery plan. [12], [23] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | — | The NIST CMVP registry returns no FIPS-validated modules for vendor 'Claroty', and Claroty cites ISO/IEC 27001 and SOC 2 rather than FIPS or Common Criteria; no Common Criteria listing was found in public sources. [21], [26] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Supported | high | — | The Claroty-Siemens joint solution brief documents integration with Siemens hardware (RUGGEDCOM) and the integrations catalog lists Siemens PCS7/TIA, Honeywell EHPM/Experion and ABB 800xA project-file support, corroborated by the Rockwell partnership page and an independent comparison. [5], [10], [15], [25] |

---

## 4. Notable Strengths

- **Real-time asset and flow discovery (items 1.1, 1.5):** Passive monitoring, Claroty Edge and integration enrichment give automated, ongoing inventory of CPS assets, with behavioral baselining that alerts on known, unknown and anomalous communications [1][2][11][14].
- **ML-driven segmentation with simulation (items 2.1, 2.2, 2.3):** AI-based device clustering recommends zones and policies based on operational context rather than IP subnets, and policies can be simulated/tested for network impact before enforcement [1][2][4][14].
- **Enforcement through existing infrastructure (items 2.1, 3.3):** Policies are exported as tags/device lists to firewalls and NAC (e.g., FortiManager/FortiGate, Palo Alto) so segmentation runs on trusted network gear with no workload agent [5][7][9][14].
- **Air-gapped and on-premise suitability (item 3.4):** Claroty Edge and CTD explicitly support air-gapped, remote-isolated and on-premise deployments alongside the SaaS option [5][9][19][27].
- **Integration breadth (items 5.1, 5.2, 5.3, 8.2):** A documented REST API (v1, API tokens), native SIEM/SOAR connectors (Splunk, Sentinel, QRadar, InsightIDR, XSOAR), ServiceNow integration, and deep industrial-ecosystem compatibility with Siemens, Honeywell, ABB and Rockwell [10][14][16][17][18][28].

## 5. Notable Gaps / Risks

- **No FIPS or Common Criteria certification (item 8.1):** NIST CMVP lists no FIPS-validated Claroty modules and no Common Criteria listing was found; Claroty holds ISO/IEC 27001 and SOC 2 instead, which may fail buyers that require FIPS 140-2/140-3 or CC EAL4+ [21][26].
- **Quantitative claims are missing (items 1.3, 3.5, 4.3):** No published figures for flow-history retention (≥ 90 days), per-deployment workload scale (≥ 50,000), or added network latency (< 0.1 ms); buyers needing documented capacity/retention numbers would need vendor engineering data [1][4][14][23].
- **No CI/CD or policy-rollback/hierarchy features documented (items 2.4, 2.5, 5.4):** One-click policy rollback, inherited/hierarchical rules and Jenkins/GitLab/Terraform integrations are absent from all reviewed sources.
- **Process-level enforcement unavailable (item 6.1):** CTD offers industrial process-value visibility but no OS process-level access enforcement; segmentation control is network-based only.
- **Autonomous-mode behavior unverified (item 7.2):** No source states what happens to policy enforcement if the Claroty platform loses connectivity, though enforcement architecture is off-box via firewalls/NAC.

## 6. Evidence Quality Notes

The assessment rests on 99 evidence entries drawn from 30 staged sources across 7 source types (14 vendor_doc, 4 vendor_datasheet, 3 vendor_blog, 8 third_party_review, 1 certification_registry). Thirteen items were triangulated across at least two source types and most supported items (1.1, 1.5, 2.1, 2.2, 5.1, 5.2, 5.3, 8.2) combine vendor materials with independent documentation from AWS, Rapid7, Elastic, Synqly, SecurityScientist, DecryptionDigest or Rockwell Automation; those carry high confidence. The numeric items (1.3, 3.5, 4.3) and several capability items (1.4, 3.1, 6.2, 6.3, 6.4, 7.1) rely on qualitative vendor language only and are capped at medium confidence.

Sources were consistent — no direct contradictions were found — but two caveats apply. First, several items (2.3, 3.4, 7.3) rest entirely on vendor documentation, so their verdicts are only as strong as Claroty's claims; the xDome SaaS itself is described only through vendor material and the AWS guidance. Second, the NIST CMVP negative result is treated as authoritative for FIPS (the advanced search explicitly returns "No certificates match the search criteria" for vendor Claroty), while Common Criteria status is reported as unknown rather than confirmed absent, because the CC portal is JavaScript-rendered and could not be searched programmatically.

---

## Bibliography

[1] Claroty. "xDome - Industrial CPS Cybersecurity Solution (product page)". https://www.claroty.com/industrial-cybersecurity/xdome (Retrieved: 2026-08-10T14:01:47Z)
[2] Claroty. "Claroty xDome Data Sheet (2022)". https://web-assets.claroty.com/resource-downloads/xdome_ds_0722.pdf (Retrieved: 2026-08-10T14:01:47Z)
[3] Claroty. "Claroty Continuous Threat Detection (CTD) Data Sheet (2023)". https://web-assets.claroty.com/resource-downloads/ctd-ds.pdf (Retrieved: 2026-08-10T14:01:47Z)
[4] Claroty. "Claroty xDome Platform Overview - Industrial (June 2024)". https://web-assets.claroty.com/resource-downloads/xdome-ind-platformoverview-0624.pdf (Retrieved: 2026-08-10T14:01:47Z)
[5] Siemens AG / Claroty. "Joint Solution Brief: Claroty and Siemens". https://cache.industry.siemens.com/dl/files/486/109820486/att_1139869/v1/SL_Flyer_Claroty_Siemens_JointSolutionBrief_EN.pdf (Retrieved: 2026-08-10T14:01:47Z)
[6] Claroty. "Claroty & ISA/IEC-62443-3-3: Supporting Compliance with Claroty Industrial Solutions (white paper)". https://web-assets.claroty.com/claroty-isa-iec-62443-3-3-paper.pdf (Retrieved: 2026-08-10T14:01:47Z)
[7] Claroty. "Integration Brief: Claroty xDome and Fortinet FortiManager". https://web-assets.claroty.com/xdome-fortimanager-integration-brief-final.pdf (Retrieved: 2026-08-10T14:01:47Z)
[8] Claroty. "Network Protection for Cyber-Physical Systems (blog)". https://blog.claroty.com/platform/network-protection (Retrieved: 2026-08-10T14:01:47Z)
[9] Claroty. "The Claroty Platform (product page)". https://claroty.com/platform (Retrieved: 2026-08-10T14:01:47Z)
[10] Claroty. "Claroty Platform Integrations (catalog page)". https://claroty.com/platform/integrations (Retrieved: 2026-08-10T14:01:47Z)
[11] Claroty. "Continuous Threat Detection (CTD) (product page)". https://claroty.com/industrial-cybersecurity/ctd (Retrieved: 2026-08-10T14:01:47Z)
[12] Amazon Web Services. "Guidance for Securing OT Assets with Claroty xDome on AWS". https://docs.aws.amazon.com/solutions/securing-operational-technology-assets-with-claroty-xdome-on-aws/ (Retrieved: 2026-08-10T14:01:47Z)
[13] Amazon Web Services. "AWS Reference Architecture: Securing OT Assets using Claroty xDome on AWS (diagram)". https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/securing-operational-technology-assets-with-claroty-xdome-on-aws.pdf (Retrieved: 2026-08-10T14:01:47Z)
[14] SecurityScientist. "12 Questions and Answers About Claroty xDome (independent Q&A review)". https://www.securityscientist.net/blog/12-questions-and-answers-about-claroty-xdome/ (Retrieved: 2026-08-10T14:01:47Z)
[15] DecryptionDigest. "OT/ICS Security 2026: Dragos vs Claroty vs Nozomi Networks vs Microsoft Defender for IoT". https://www.decryptiondigest.com/blog/ot-ics-security-platform-comparison-2026-dragos-claroty-nozomi-defender-iot (Retrieved: 2026-08-10T14:01:47Z)
[16] Rapid7. "Claroty xDome | SIEM Documentation (Rapid7 InsightIDR)". https://docs.rapid7.com/insightidr/claroty-xdome/ (Retrieved: 2026-08-10T14:01:47Z)
[17] Claroty. "Claroty & ServiceNow - Joint Solution (integration brief)". https://claroty.com/resources/integration-briefs/claroty-and-servicenow-integration-brief (Retrieved: 2026-08-10T14:01:47Z)
[18] Synqly. "Claroty xDome Provider Configuration Guide (Synqly)". https://docs.synqly.com/guides/provider-configuration/claroty-asset-setup (Retrieved: 2026-08-10T14:01:47Z)
[19] Claroty. "Claroty xDome for Federal Environments (product page)". https://claroty.com/public-sector-cybersecurity/us-government-cybersecurity/xdome (Retrieved: 2026-08-10T14:01:47Z)
[20] Claroty. "Threat Intelligence for CPS Environments (product page)". https://claroty.com/threat-intelligence (Retrieved: 2026-08-10T14:01:47Z)
[21] Claroty. "xDome Secure Access - Commercial CPS Cybersecurity Solution (product page)". https://claroty.com/commercial-cybersecurity/xdome-secure-access (Retrieved: 2026-08-10T14:01:47Z)
[22] Claroty. "Claroty xDome Secure Access - Solution Overview (2024)". https://web-assets.claroty.com/xdome-secure-access-solution-brief.pdf (Retrieved: 2026-08-10T14:01:47Z)
[23] Claroty. "Claroty Security & Privacy FAQs (updated 2026-03-12)". https://claroty.com/security-and-privacy-faqs (Retrieved: 2026-08-10T14:01:47Z)
[24] Claroty. "Feature Spotlight: Claroty API Explorer (blog)". https://claroty.com/blog/product-feature-spotlight-api-explorer (Retrieved: 2026-08-10T14:01:47Z)
[25] Rockwell Automation. "Rockwell Automation and Claroty: Comprehensive OT Cybersecurity". https://www.rockwellautomation.com/en-us/support/documentation/overview/rockwell-automation-and-claroty--comprehensive-ot-cybersecurity.html (Retrieved: 2026-08-10T14:01:47Z)
[26] NIST / CMVP. "NIST CMVP Validated Modules search (Vendor: Claroty)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&Vendor=Claroty (Retrieved: 2026-08-10T14:01:47Z)
[27] Claroty. "Claroty Edge Data Sheet (2022)". https://web-assets.claroty.com/resource-downloads/edge_ds_0822.pdf (Retrieved: 2026-08-10T14:01:47Z)
[28] Elastic. "Elastic Integration: Claroty xDome (README)". https://raw.githubusercontent.com/elastic/integrations/main/packages/claroty_xdome/docs/README.md (Retrieved: 2026-08-10T14:01:47Z)
[29] Claroty. "Claroty CTD v4.2.3 Quick Installation Guide Rev1 (mirror)". https://kupdf.net/download/div-class2qs3tf-truncatedtext-modulewrapperfg1km9p-classtruncatedtext-modulelineclamped85ulhh-style-max-lines5claroty-ctd-v423-quick-installation-guide-rev1-p-div_67a2014bb6d6921d7b8b456c_pdf (Retrieved: 2026-08-10T14:01:47Z)
[30] Claroty. "Q&A: Claroty xDome and the Extended Internet of Things (XIoT) (blog)". https://blog.claroty.com/blog/q-and-a-claroty-xdome-and-the-extended-internet-of-things-xiot (Retrieved: 2026-08-10T14:01:47Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 28
- **Sources reviewed:** 30 (kept: 30, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, third_party_review: 8, vendor_blog: 3, vendor_datasheet: 4, vendor_doc: 14
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
