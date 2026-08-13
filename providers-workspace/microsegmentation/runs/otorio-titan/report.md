# Microsegmentation Product Assessment: OTORIO - OTORIO Titan (asset-centric IoT-OT-CPS security platform; now Armis Centrix for OT/IoT Security On-Prem)

**Product ID:** `otorio-titan`
**Version reference:** OTORIO Titan platform (launched Sep 2024); OTORIO Security Platform / RAM2 documentation corpus (2021-2024); Armis Centrix for OT/IoT Security (On-Prem) 2026
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:13:28Z
**Total evidence items collected:** 55
**Total distinct sources:** 28

---

## 1. Overview

OTORIO Titan is an asset-centric IoT-OT-CPS security platform launched in September 2024 as the successor to OTORIO's RAM² platform, acquired by Armis in March 2025; the on-premises edition now ships as Armis Centrix for OT/IoT Security (On-Prem) [2][13]. OTORIO positions Titan as a cyber-risk and exposure-management platform for industrial environments rather than a microsegmentation enforcement product: it discovers assets through passive network monitoring, Safe Active Query and ecosystem integrations [1][3], maps vulnerabilities and attack paths in an attack-graph view [4][5], automates compliance assessment for IEC 62443, NIST, NIS2 and NERC CIP [6], and provides secure remote access (remOT/SRA) [7]. Deployment shapes include cloud/SaaS and fully air-gapped on-premises installations [18][21]. Titan is 100% agentless on the discovery side [18] and explicitly avoids automated enforcement, delivering advisory mitigation playbooks instead [21].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 2                | 4      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 3     | 0                | 2      | 1   |
| unknown          | 10    | 0                | 0      | 10  |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 12 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** OTORIO Titan is 100% agentless for asset discovery and remOT is clientless with no agents, so there is no endpoint-agent OS support matrix to evaluate (assets are monitored via network traffic and industrial protocols).
- **4.1:** No endpoint agent exists (100% agentless discovery; clientless remote access), so there is no agent CPU overhead metric to measure against the <1% threshold.
- **4.2:** No endpoint agent exists (100% agentless discovery; clientless remote access), so there is no agent RAM footprint metric to measure against the 100MB threshold.
- **4.3:** The platform is out-of-band and agentless (passive monitoring plus a deliberately slow ping sweep that places no load on the network), so no inline agent adds latency to measure against the 0.1ms threshold.
- **4.4:** There are no enforcement agents in the data path and the platform avoids automated enforcement, so the agent-crash/fail-safe scenario does not apply.
- **4.5:** No endpoint agent is installed on hosts (clientless web-based remote access; agentless discovery), so agent install/update reboot concerns do not apply.
- **7.2:** No enforcement agents exist and automated enforcement is avoided, so an autonomous enforcement mode during controller outage does not apply.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | Passive network monitoring plus Safe Active Query (SAQ) automatically discover and attribute OT assets, corroborated by an independent PAC review and Armis documentation of the platform (agentless discovery of every asset). [1], [3], [18], [21] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | OTORIO visualizes assets, inter-process connectivity and vulnerabilities in an attack-graph map and maps assets to operational processes and roles, but there is no documented App/Environment grouping view as in agent-based microsegmentation products. [3], [5], [15] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | - | no evidence found (No published figure for connection/flow history retention was found in the staged corpus (product help center is closed).) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | - | The attack-graph map lets users navigate between assets, vulnerabilities and connections, and asset inventories are automatically mapped to publicly known vulnerabilities (CVE context is rendered in the operational map). [4], [14], [15] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | The platform identifies rogue/unauthorized devices and correlates sensor and third-party alerts to MITRE ATT&CK techniques, covering unrecognized devices and suspicious inter-process communication. [18], [24], [28] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Not Supported | low | - | An independent PAC review states OTORIO Titan avoids automated enforcement and instead delivers advisory mitigation playbooks; an Armis page mentions automated network segmentation, but no tag/label/identity-based policy authoring is documented. [18], [21] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | - | no evidence found (No evidence of AI/ML-driven policy or rule recommendations; EM360 describes machine-learning threat detection, not policy suggestion.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | A sandboxed cyber-digital-twin simulates the impact of new security policies/configuration changes and threat models without touching production, which approximates policy dry-run but is not a microsegmentation policy simulation feature. [5], [18] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No evidence of one-click policy rollback.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found (No evidence of inherited/hierarchical policy rules.) |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | - | OTORIO Titan is 100% agentless for asset discovery and remOT is clientless with no agents, so there is no endpoint-agent OS support matrix to evaluate (assets are monitored via network traffic and industrial protocols). [7], [18] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (No evidence of container/Kubernetes/OpenShift native isolation capabilities.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Not Supported | medium | - | The platform is documented as 100% agentless (passive monitoring plus SAQ, clientless remote access); no agent-based mode exists, so support for both deployment modes is not met. [7], [18], [21] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | high | - | The on-premises deployment (the OTORIO Titan platform under Armis) is specifically tailored for fully air-gapped environments with no data leaving the site, corroborated by the acquisition announcement and an independent review. [2], [18], [21] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Armis documents the platform as built for large, distributed operations with multi-site deployments, but no numeric workload/asset capacity figure is published, so the 50,000-workload threshold cannot be confirmed. [18] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | - | No endpoint agent exists (100% agentless discovery; clientless remote access), so there is no agent CPU overhead metric to measure against the <1% threshold. [7], [18] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | - | No endpoint agent exists (100% agentless discovery; clientless remote access), so there is no agent RAM footprint metric to measure against the 100MB threshold. [7], [18] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | - | The platform is out-of-band and agentless (passive monitoring plus a deliberately slow ping sweep that places no load on the network), so no inline agent adds latency to measure against the 0.1ms threshold. [14], [18] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | - | There are no enforcement agents in the data path and the platform avoids automated enforcement, so the agent-crash/fail-safe scenario does not apply. [18], [21] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | - | No endpoint agent is installed on hosts (clientless web-based remote access; agentless discovery), so agent install/update reboot concerns do not apply. [7], [18] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Unknown | low | - | no evidence found (No public API documentation was found in the staged corpus (OTORIO help center is closed); REST API coverage of admin functions is unverified.) |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Titan integrates natively with SIEM/SOAR platforms, firewalls, EDR and other security tools; EM360 and an independent review list SIEM integration among its documented ecosystem integrations. [18], [21], [28] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | OTORIO's RAM2 integrates with ServiceNow CMDB (Service Graph Connector) to discover, enrich and synchronize OT/IT/IoT inventory. [10] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No evidence of CI/CD pipeline integration (Jenkins/GitLab/Terraform).) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | - | An independent review states OTORIO Titan avoids automated enforcement and provides step-by-step mitigation playbooks instead, so process-level enforcement is not provided. [21] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat intelligence enrichment (MITRE ATT&CK for ICS mapping, KEV/EPSS/Exploit-DB scoring, proprietary research) is well documented, but no honeypot/deception capability is evidenced. [4], [21], [24] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Automated compliance assessment and reporting exist for IEC 62443, NIST 800-82, NIS2, NERC CIP and PCI DSS, but NIST 800-207 is not named in the staged sources. [6], [21], [28] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | The vendor documents full data encryption in transit and encryption of sensitive data in motion, but no TLS 1.3/mTLS specification or agent-controller channel details are published (the platform is agentless). [20] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | - | no evidence found (No evidence of controller clustering (active-active/active-passive) was found.) |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | N/A | medium | - | No enforcement agents exist and automated enforcement is avoided, so an autonomous enforcement mode during controller outage does not apply. [18], [21] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | - | no evidence found (Multi-site deployments are mentioned, but no disaster-recovery site synchronization or backup/restore evidence was found.) |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | - | no evidence found (No FIPS 140-2/140-3 or Common Criteria EAL4+ validation entries were found for OTORIO Titan.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | OTORIO validates each release in automation-vendor labs, queries industrial assets with vendor-native protocols (DCP, Ethernet/IP, ABB) and is founded with industrial partner Andritz, but no formal Siemens/Honeywell/ABB compatibility certificates are documented. [13], [14] |

---

## 4. Notable Strengths

- **Agentless OT asset discovery with CVE context (items 1.1, 1.4):** passive monitoring plus Safe Active Query automatically build an asset inventory that is mapped to publicly known vulnerabilities and rendered in the attack-graph view [1][3][4][5].
- **Air-gapped on-premises deployment (item 3.4):** the Titan platform ships as an on-prem solution tailored for fully air-gapped environments, with no data leaving the site [2][18][21].
- **Ecosystem and SIEM/SOAR integration (items 5.2, 5.3):** native integration with SIEM/SOAR platforms, firewalls, EDR and ServiceNow CMDB via the Service Graph Connector [10][18][21][28].
- **Automated compliance reporting (item 6.3):** out-of-the-box compliance assessment for IEC 62443, NIST 800-82, NIS2 and NERC CIP, customizable to PCI DSS [6][21][28].
- **Threat-intelligence-driven detection (items 1.5, 6.2):** MITRE ATT&CK for ICS mapping, KEV/EPSS/Exploit-DB enrichment and proprietary threat intelligence feed anomaly and rogue-asset detection [4][21][24].

## 5. Notable Gaps / Risks

- **No policy authoring or enforcement (items 2.1, 3.3, 6.1):** the platform is 100% agentless and, per an independent review, avoids automated enforcement, so tag/label-based policy creation, agent-based deployment and process-level enforcement are absent [18][21].
- **No numeric capacity or performance data (items 3.5, 4.1-4.3):** no workload figure, agent resource metric or latency number is published; scalability is described only qualitatively, and agent metrics are not applicable to an agentless design [18].
- **Forensics and retention unverified (item 1.3):** no connection-flow history retention period is published; OTORIO's help center is closed, so documentation is not publicly retrievable.
- **HA/DR and security certifications unverified (items 7.1, 7.3, 8.1):** no evidence of controller clustering, disaster-recovery site sync, FIPS 140-2/140-3 or Common Criteria EAL4+ validation was found.
- **Not an enforcement-based microsegmentation product (items 2.3, 7.2):** buyers requiring enforcement or autonomous policy continuity must rely on other controls; Titan's digital-twin sandbox simulates security changes but is not a microsegmentation policy dry-run [18][21].

## 6. Evidence Quality Notes

Of 33 items, 13 are backed by two or more source types and 10 rely on a single source; the dominant base is vendor material (14 vendor_doc, 8 vendor_blog, 1 vendor_datasheet, 3 case_study). Independent corroboration comes from a PAC/SITSI analyst review (Dec 2024), an EM360Tech solution overview (Oct 2024, vendor-assisted editorial), and GigaOm analysis quoted on OTORIO's blog; these support the high-confidence ratings on 1.1 and 3.4. Ten items (1.3, 2.2, 2.4, 2.5, 3.2, 5.1, 5.4, 7.1, 7.3, 8.1) have no evidence and are rated unknown - OTORIO's help center is closed/restricted, so product documentation is not publicly retrievable.

Sources partially contradict each other on enforcement: an Armis page blurb says the platform can "automate network segmentation" while PAC/SITSI states Titan "avoids automated enforcement"; the not_supported verdicts on 2.1, 3.3 and 6.1 follow the analyst's explicit statement, with the vendor marketing language flagged in the item notes. Because otorio.com now redirects to armis.com post-acquisition, vendor product pages were recovered from Common Crawl snapshots (2022-2024); the Armis Centrix On-Prem page (2026) confirms the same capabilities carried into Titan's successor, and all 55 evidence quotes are verified verbatim against the staged artifacts.

---

## Bibliography

[1] Microsoft Marketplace / OTORIO LTD. "OTORIO Titan - Microsoft Marketplace listing (by OTORIO LTD)". https://marketplace.microsoft.com/en-us/product/saas/otorio.otorio-titan (Retrieved: 2026-08-10T14:13:28Z)
[2] Armis. "Armis Acquires OTORIO to Expand Its Leadership in Operational Technology and Cyber-Physical Security (press release)". https://www.armis.com/newsroom/press/armis-acquires-otorio-to-expand-its-leadership-in-operational-technology-and-cyber-physical-security/ (Retrieved: 2026-08-10T14:13:28Z)
[3] OTORIO. "OTORIO - Asset Visibility (platform page, archived Jun 2024)". https://www.otorio.com/asset-visibility/ (Retrieved: 2026-08-10T14:13:28Z)
[4] OTORIO. "OTORIO - OT Vulnerability Management (platform page, archived Jun 2024)". https://www.otorio.com/ot-vulnerability-management/ (Retrieved: 2026-08-10T14:13:28Z)
[5] OTORIO. "OTORIO - Exposure Management (platform page, archived Jun 2024)". https://www.otorio.com/exposure-management/ (Retrieved: 2026-08-10T14:13:28Z)
[6] OTORIO. "OTORIO - Compliance Management (platform page, archived Jun 2024)". https://www.otorio.com/compliance-management/ (Retrieved: 2026-08-10T14:13:28Z)
[7] OTORIO. "OTORIO remOT - Secure Remote Access (platform page, archived Jun 2024)". https://www.otorio.com/secure-remote-access/ (Retrieved: 2026-08-10T14:13:28Z)
[8] OTORIO. "OTORIO - On Demand OT Risk Assessment (platform page, archived Jun 2024)". https://www.otorio.com/ot-risk-assessment/ (Retrieved: 2026-08-10T14:13:28Z)
[9] OTORIO. "OTORIO - OT Security FAQs (archived Jun 2024)". https://www.otorio.com/ot-security-faqs/ (Retrieved: 2026-08-10T14:13:28Z)
[10] OTORIO. "OTORIO and ServiceNow integration page (archived Jun 2024)". https://www.otorio.com/solutions/otorio-and-servicenow/ (Retrieved: 2026-08-10T14:13:28Z)
[11] OTORIO. "OTORIO Achieves ISO 27001 & IEC 62443 (news, Sep 2023)". https://www.otorio.com/news/otorio-awarded-iec-62443-cybersecurity-certification/ (Retrieved: 2026-08-10T14:13:28Z)
[12] OTORIO. "GigaOm: OTORIO a Future-Proof Investment for IIoT Security (vendor blog, Jun 2024)". https://www.otorio.com/blog/gigaom-otorio-a-future-proof-investment-for-iiot-security/ (Retrieved: 2026-08-10T14:13:28Z)
[13] GlobeNewswire / OTORIO. "Introducing OTORIO Titan, The Next Evolution in IoT-OT-CPS Security (GlobeNewswire via EIN Presswire, Sep 2024)". https://www.einpresswire.com/article/744470593/introducing-otorio-titan-the-next-evolution-in-iot-ot-cps-security (Retrieved: 2026-08-10T14:13:28Z)
[14] OTORIO. "OTORIO - Enhance Visibility with Safe Active Query (blog, Mar 2024)". https://www.otorio.com/blog/passive-vs-active-discovery-of-ot-assets/ (Retrieved: 2026-08-10T14:13:28Z)
[15] OTORIO. "OTORIO Wins Policy Management Solution Provider of the Year (news, Oct 2023)". https://www.otorio.com/news-events/news/otorio-wins-policy-management-solution-provider-of-the-year-at-cybersecurity-breakthrough-awards/ (Retrieved: 2026-08-10T14:13:28Z)
[16] OTORIO. "OTORIO Meets IEC 62443 Cybersecurity Standard for Critical Infrastructure (news, Oct 2022)". https://www.otorio.com/news-events/news/otorio-meets-iec-62443-cybersecurity-standard-for-critical-infrastructure/ (Retrieved: 2026-08-10T14:13:28Z)
[17] OTORIO. "OTORIO - Mastering Security for OT Networks (knowledge hub, archived Jun 2024)". https://www.otorio.com/resources/mastering-security-for-ot-networks/ (Retrieved: 2026-08-10T14:13:28Z)
[18] Armis. "Armis Centrix for OT/IoT Security (On-Prem) - formerly OTORIO Titan (product page, 2026)". https://www.armis.com/platform/armis-centrix-for-ot-iot-security-on-prem/ (Retrieved: 2026-08-10T14:13:28Z)
[19] OTORIO. "OTORIO Service Level Agreement / Software Support and Maintenance Policy (archived Apr 2024)". https://www.otorio.com/sla/ (Retrieved: 2026-08-10T14:13:28Z)
[20] OTORIO. "OTORIO GDPR Whitepaper (May 2023)". https://www.otorio.com/gdpr/ (Retrieved: 2026-08-10T14:13:28Z)
[21] PAC (Pierre Audoin Consultants). "PAC/SITSI - Exploring OTORIO: Enhancing Operational Security with the OTORIO Titan Platform (Dec 2024)". https://sitsi.pacanalyst.com/exploring-otorio-enhancing-operational-security-with-the-otorio-titan-platform/ (Retrieved: 2026-08-10T14:13:28Z)
[22] OTORIO. "OTORIO RAM2 - Continuous OT cyber security and digital risk management platform (archived Nov 2022)". https://www.otorio.com/ram-continuous-ot-cyber-security-and-digital-risk-management-platform/ (Retrieved: 2026-08-10T14:13:28Z)
[23] OTORIO. "OTORIO remOT Product Brief (archived Sep 2023)". https://www.otorio.com/resources/pb-ram2-remot/ (Retrieved: 2026-08-10T14:13:28Z)
[24] OTORIO. "OTORIO - Why We Integrated MITRE ATT&CK Into Our Risk Management Platform (blog, Mar 2021)". https://www.otorio.com/blog/why-we-integrated-mitre-att-ck-into-ram2/ (Retrieved: 2026-08-10T14:13:28Z)
[25] OTORIO. "OTORIO - Enabling Integration of OT Assets in Automotive Industry (case study, archived Feb 2024)". https://www.otorio.com/resources/cs-auto-spot/ (Retrieved: 2026-08-10T14:13:28Z)
[26] OTORIO. "OTORIO - Speeding Up OT Network Security Posture of Large Energy Company (case study, archived Feb 2024)". https://www.otorio.com/resources/cs-south-american-energy-company/ (Retrieved: 2026-08-10T14:13:28Z)
[27] OTORIO. "OTORIO - Prevents Cyberattack on a Global Industrial Company (case study, archived Feb 2024)". https://www.otorio.com/resources/cs-manufacturing-ir/ (Retrieved: 2026-08-10T14:13:28Z)
[28] EM360Tech. "EM360Tech - Solution overview: What is OTORIO Titan? (Oct 2024)". https://em360tech.com/tech-articles/solution-overview-what-otorio-titan (Retrieved: 2026-08-10T14:13:28Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 28 (kept: 28, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 3, third_party_review: 2, vendor_blog: 8, vendor_datasheet: 1, vendor_doc: 14
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
