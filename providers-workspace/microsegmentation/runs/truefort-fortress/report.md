# Microsegmentation Product Assessment: TrueFort Inc. - TrueFort Fortress (Fortress Platform / Fortress XDR)

**Product ID:** `truefort-fortress`
**Version reference:** Fortress platform, Fortress XDR line; staged material spans 2019-2024 (vendor ceased operations May 21, 2025 per truefort.com homepage capture of 2025-07-16)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:30:33Z
**Total evidence items collected:** 59
**Total distinct sources:** 24

---

## 1. Overview

TrueFort Fortress (also marketed as Fortress XDR / the TrueFort Platform) is an application-centric, behavior-based microsegmentation and workload-protection platform for data center, cloud, Kubernetes and OT environments [1, 7]. Rather than IP-based rules, it uses machine learning to baseline normal application, workload and service-account behavior, then enforces zero-trust segmentation at the workload through host firewalls, including process- and command-line-level controls [1, 8, 10]. Deployment is agent-based with a bring-your-own-agent option (CrowdStrike Falcon, SentinelOne) plus agentless device visibility through the Armis alliance, and TrueFort Cloud is a hosted AWS service supporting hybrid/on-premises architectures [4, 6, 16]. The platform was cited in Forrester's "Manage Insider Risk With Zero Trust" report as a sample microsegmentation vendor [23]. Critically, the TrueFort homepage announced that the company shut down on May 21, 2025 and is no longer conducting business [24]; the verdicts below reflect capabilities documented in 2019-2024 materials, but the product is not available to new buyers or ongoing support.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 1                | 7      | 0   |
| partial          | 10    | 0                | 10     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 14    | 0                | 0      | 14  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 13 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | Vendor product page, application-discovery solution brief and TrueFort Cloud press release all document real-time discovery and mapping of workloads, applications and data flows; the TechCrunch funding article independently describes TrueFort gathering telemetry from partners and infrastructure to analyze application behavior, and the customer case study reports an application map appearing within hours. [1], [2], [3], [4], [5] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | medium | - | The product page documents automated mapping of application relationships and data flows 'including the process, identity, and location', and the case study describes an application map with traffic flows and dependencies; dependency maps are stated to be infrastructure-agnostic and dynamically updated. [1], [2], [5], [6] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | The Reporter module provides on-demand playback of real-time and historical data spanning 'minutes, months or even years', and the Fortress DVR feature replays incidents over time; no exact retention-period figure is published, so the 90-day bar is met qualitatively but not quantified. [5], [7] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | The product page and lateral-movement solution page document machine-learning baselining that blocks unrecognized behaviors, and the discovery brief says all workloads and communications, known and unknown, are cataloged. [1], [2], [8] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Vendor material consistently states policies are identity-based rather than IP-based: policies built on network/identity/process/application profiles, tags around OS/application type/other attributes, and explicit guidance not to use IP addresses or network location as the policy foundation. [4], [9], [10], [11] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | The product page, CrowdStrike integration press release, cloud-workload solution page and a vendor blog all document machine-intelligence/ML-driven automated policy generation and recommendations. [1], [11], [12], [13] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | The CrowdStrike integration press release documents policy 'creation, testing, and deployment' as a staged workflow, and the case study describes baselining and visibility phases that precede enforcement; a dedicated simulation/dry-run mode is not explicitly documented. [5], [11], [12] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The customer case study reports 'complete OS server coverage' and 'full environment coverage including legacy OS's', and the Kubernetes solution page says hardware servers, VMs and cloud-native workloads are secured from one platform; no staged source enumerates specific OS versions such as AIX or Solaris. [5], [14] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | - | The Kubernetes solution page documents container microsegmentation with runtime baselining, and the 2019 press release states Fortress XDR supports Kubernetes and Istio, deploying as a daemon set within nodes; OpenShift is not mentioned in staged sources. [7], [14], [15] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | The product FAQ documents both agent-based and network-device deployment models; the Fortified ecosystem press release and DoD brief document bring-your-own-agent, and the Armis alliance page documents agentless device discovery feeding the platform. [1], [6], [7], [16] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | - | no evidence found |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Staged sources cite deployments of 'tens of thousands' of Falcon-protected workloads and visibility into 'millions of containers', but no explicit 50,000+ workload per-controller figure is published. [7], [14] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | Only qualitative footprint claims are published: bring-your-own-agent deployment 'eliminating the need for additional impact to the endpoint' and visibility 'with no additional agents'; no CPU percentage is documented, so the <1% threshold cannot be verified. [5], [6], [12] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | Only qualitative resource claims are published (BYO-agent reduces endpoint impact; EDR consolidation 'saves compute resources'); no memory figure for the Fortress agent is documented, so the <100 MB threshold cannot be verified. [6], [17] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | - | no evidence found |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | - | no evidence found |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | Fortress XDR exposes REST APIs for bi-directional integration through the Fortified ecosystem and customers receive automatic access to platform APIs, but no staged source demonstrates the API covers 100% of administrative functions. [7] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | - | Documented integrations are EDR/asset platforms (CrowdStrike Falcon, SentinelOne, Armis) via telemetry/API; no staged source documents a SIEM/SOAR integration (Splunk, QRadar, Azure Sentinel) or Syslog/CEF export, so SIEM-specific integration is only partially evidenced. [12], [16], [17] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | medium | - | The lateral-movement solution page documents enforcement via host firewalls, blocking unusual command-line arguments and killing anomalous processes at execution; the DoD brief and Forrester-mention press release document process-, identity- and service-account-level controls. [6], [8], [23] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | - | no evidence found |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Dedicated framework pages document built-in alignment with PCI DSS 4.0, NIST (CSF/SP 800-53), ISO 27001, HIPAA, CMMC and other standards; IEC 62443 and NIST SP 800-207 are not explicitly covered in staged sources. [16], [18], [19], [20] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Unknown | low | - | no evidence found |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | - | The SOC 2 Type II press release quotes the CTO stating the platform 'requires 99.99 uptime from our systems', but no staged source documents an explicit controller cluster architecture (active-active/active-passive), so HA support is only partially evidenced. [21] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | - | no evidence found |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | - | no evidence found |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | - | TrueFort's documented certifications are SOC 2 Type II (2022) and CIS Benchmarks (2023); neither is FIPS 140-2/140-3 nor Common Criteria EAL4+, and no staged source claims FIPS or Common Criteria validation. [21], [22] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found |

---

## 4. Notable Strengths

- **Behavior-based, identity-centric policy model (items 1.1, 1.5, 2.1, 2.2):** machine-learning baselining of application, workload and service-account behavior auto-generates and enforces segmentation policies keyed to identities, tags and labels rather than IP addresses [1, 4, 10].
- **Process-level enforcement (item 6.1):** host-firewall enforcement blocks unusual command-line arguments, disables rogue accounts and kills anomalous processes at execution time [8, 6, 23].
- **Deployment flexibility (item 3.3):** native agent, bring-your-own-agent via CrowdStrike Falcon and SentinelOne, and agentless device discovery via the Armis alliance cover on-prem, cloud and hybrid environments [7, 6, 16].
- **Kubernetes support (item 3.2):** container microsegmentation with runtime behavior baselining, deployed as a daemon set within nodes and supporting the Istio standard [14, 7].
- **Documented compliance alignment (item 6.3):** dedicated framework pages map the platform to PCI DSS 4.0, NIST CSF/SP 800-53, ISO 27001, HIPAA and CMMC requirements [18, 19, 20, 16].

## 5. Notable Gaps / Risks

- **Company shutdown (all items):** TrueFort announced on its homepage that it ceased operations on May 21, 2025, so the platform cannot be procured, renewed or supported going forward regardless of documented capability [24].
- **Unquantified agent resource footprint (items 4.1, 4.2):** only qualitative claims ("no additional impact to the endpoint", "no additional agents required") are published; no CPU% or RAM figures exist to confirm the <1% / <100 MB thresholds [6, 12].
- **Unverified HA and DR architecture (items 7.1, 7.2, 7.3):** evidence is limited to a 99.99% uptime quote; no controller clustering, agent autonomous mode, or disaster-recovery sync is documented [21].
- **Missing integration evidence (items 5.2, 5.3, 5.4):** documented integrations cover EDR/asset platforms only; no SIEM/SOAR (Splunk/QRadar/Sentinel), ServiceNow CMDB, or CI/CD pipeline integration is documented.
- **No FIPS/Common Criteria certification (item 8.1):** the documented certification portfolio (SOC 2 Type II, CIS Benchmarks) does not include FIPS 140-2/140-3 or Common Criteria EAL4+ [21, 22].

## 6. Evidence Quality Notes

Only 1 of 33 items (1.1) is backed by an independent non-vendor source - the TechCrunch funding article - and it is the sole high-confidence verdict; every other non-unknown verdict rests on vendor documentation, press releases or vendor-hosted case studies and is capped at medium. Analyst references (Forrester, ESG, KuppingerCole) and awards (CISO Choice, InfoSec, Cybersecurity Excellence) appear only inside vendor-hosted press releases, so they do not qualify as independent sources under the project's taxonomy. No sources contradicted each other; the main judgment calls were threshold-related - for example, 1.3 (retention) is partial because the Reporter module's "minutes, months or even years" playback span is qualitative, and 3.5 (scale) is partial because only "tens of thousands" of workloads are cited. 14 of 33 items are unknown purely due to absent public documentation (agent fail-safe, reboot-free install, TLS/mTLS transport, SIEM/SOAR, rollback, hierarchical rules, air-gap, autonomous mode, DR, IEC 62443 and OT-vendor certifications). Methodological note: truefort.com rejects all TLS handshakes from this environment and web.archive.org rate-limited the research IP, so all vendor content was recovered from Common Crawl WARC archives and staged with hash-anchored manifest entries (artifacts/manifest.jsonl); every evidence quote was verified verbatim against the staged text by verify_citation_grounding.py (59/59 grounded).

---

## Bibliography

[1] TrueFort Inc.. "TrueFort: Zero Trust Microsegmentation for Cyber Resilience (product page)". https://truefort.com/product/microsegmentation/ (Retrieved: 2026-08-10T14:30:33Z)
[2] TrueFort Inc.. "TrueFort Platform: Application Discovery and Mapping (solution brief)". https://truefort.com/wp-content/uploads/2023/12/TRUEFORT-Application-Discovery-001.pdf (Retrieved: 2026-08-10T14:30:33Z)
[3] TechCrunch. "TrueFort snares $30M Series B to expand zero trust application security solution". https://techcrunch.com/2021/09/08/truefort-snares-30m-series-b-to-expand-zero-trust-application-security-solution/ (Retrieved: 2026-08-10T14:30:33Z)
[4] TrueFort Inc.. "TrueFort Cloud Enables Application Intelligence-based Workload Protection to Secure Environments in Minutes (press release)". https://truefort.com/press-release/truefort-cloud-enables-application-intelligence-based-workload-protection-to-secure-environments-in-minutes/ (Retrieved: 2026-08-10T14:30:33Z)
[5] TrueFort Inc.. "Top Manufacturer Finds Superior Microsegmentation Solution with TrueFort & CrowdStrike (case study)". https://truefort.com/wp-content/uploads/2021/09/20210914-TF-Microsegmentation-Case-Study-Final.pdf (Retrieved: 2026-08-10T14:30:33Z)
[6] TrueFort Inc.. "Mapping TrueFort to the DoD Pillars of Zero Trust (solution brief)". https://truefort.com/wp-content/uploads/2022/07/Mapping-TrueFort-to-the-DoD_Solution-Brief_June-2022.pdf (Retrieved: 2026-08-10T14:30:33Z)
[7] TrueFort Inc.. "TrueFort Unveils Industry-First Application Detection and Response Platform to Secure Applications and Cloud Workloads (press release)". https://truefort.com/press-release/truefort-unveils-industry-first-application-detection-and-response-platform-to-secure-applications-and-cloud-workloads/ (Retrieved: 2026-08-10T14:30:33Z)
[8] TrueFort Inc.. "TrueFort: Lateral Movement Attack Prevention (solution page)". https://truefort.com/solutions/controlling-lateral-movement/ (Retrieved: 2026-08-10T14:30:33Z)
[9] TrueFort Inc.. "Microsegmentation is finally reaching the mainstream by dropping the network-centric approach (blog)". https://truefort.com/microsegmentation-is-finally-reaching-the-mainstream-by-dropping-the-network-centric-approach-2/ (Retrieved: 2026-08-10T14:30:33Z)
[10] TrueFort Inc.. "Microsegmentation Made Easy (how-to guide)". https://truefort.com/wp-content/uploads/2023/04/TrueFort-Microsegmentation-How-to-Guide_Mar-2023.pdf (Retrieved: 2026-08-10T14:30:33Z)
[11] TrueFort Inc.. "Microsegmentation visibility (blog)". https://truefort.com/microsegmentation-visibility/ (Retrieved: 2026-08-10T14:30:33Z)
[12] TrueFort Inc.. "TrueFort Announces Fast Zero Trust Workload Segmentation for CrowdStrike Customers (press release)". https://truefort.com/press-release/truefort-announces-fast-zero-trust-workload-segmentation-for-crowdstrike-customers/ (Retrieved: 2026-08-10T14:30:33Z)
[13] TrueFort Inc.. "TrueFort: Enterprise-grade Cloud Workload Protection Platform (solution page)". https://truefort.com/solutions/protecting-cloud-workloads/ (Retrieved: 2026-08-10T14:30:33Z)
[14] TrueFort Inc.. "TrueFort: Kubernetes Security Solutions through Container Microsegmentation (solution page)". https://truefort.com/solutions/container-kubernetes-security/ (Retrieved: 2026-08-10T14:30:33Z)
[15] TrueFort Inc.. "Improved Kubernetes security (blog)". https://truefort.com/improved-kubernetes-security/ (Retrieved: 2026-08-10T14:30:33Z)
[16] TrueFort Inc.. "TrueFort and Armis: Securing IT, IoT, and OT environments (technology alliance page)". https://truefort.com/armis/ (Retrieved: 2026-08-10T14:30:33Z)
[17] TrueFort Inc.. "Leveraging Existing EDR Agents for Cybersecurity ROI (blog)". https://truefort.com/existing-edr-agents/ (Retrieved: 2026-08-10T14:30:33Z)
[18] TrueFort Inc.. "TrueFort: Complying with PCI DSS (framework page)". https://truefort.com/frameworks/pci-dss/ (Retrieved: 2026-08-10T14:30:33Z)
[19] TrueFort Inc.. "TrueFort: NIST standards support (framework page)". https://truefort.com/frameworks/nist-standards/ (Retrieved: 2026-08-10T14:30:33Z)
[20] TrueFort Inc.. "TrueFort: ISO 27001 certification support (framework page)". https://truefort.com/frameworks/iso-27001-certification/ (Retrieved: 2026-08-10T14:30:33Z)
[21] TrueFort Inc.. "TrueFort Platform Achieves SOC 2 Type II Certification (press release)". https://truefort.com/press-release/truefort-platform-achieves-soc-2-type-ii-certification/ (Retrieved: 2026-08-10T14:30:33Z)
[22] TrueFort Inc.. "TrueFort Achieves Coveted CIS Benchmarks Certification (press release)". https://truefort.com/press-release/truefort-achieves-coveted-cis-benchmarks-certification/ (Retrieved: 2026-08-10T14:30:33Z)
[23] TrueFort Inc.. "TrueFort Mentioned for Microsegmentation in Best Practice Report by Independent Research Firm (press release)". https://truefort.com/press-release/truefort-mentioned-for-microsegmentation-in-best-practice-report-by-independent-research-firm/ (Retrieved: 2026-08-10T14:30:33Z)
[24] TrueFort Inc.. "TrueFort homepage - TrueFort Has Ceased Operations (shutdown notice)". https://truefort.com/ (Retrieved: 2026-08-10T14:30:33Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 24 (kept: 24, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 1, third_party_review: 1, vendor_blog: 4, vendor_datasheet: 1, vendor_doc: 17
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
