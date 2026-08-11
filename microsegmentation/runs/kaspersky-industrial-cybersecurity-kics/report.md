# Microsegmentation Product Assessment: Kaspersky - Kaspersky Industrial CyberSecurity (KICS)

**Product ID:** `kaspersky-industrial-cybersecurity-kics`
**Version reference:** KICS for Networks 4.5 / KICS for Nodes 4.5 Administrator's Guides (Online Help, 2026); KICS platform four-pager datasheet (2025)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:01:37Z
**Total evidence items collected:** 70
**Total distinct sources:** 11

---

## 1. Overview

Kaspersky Industrial CyberSecurity (KICS) is an OT-focused native XDR platform for critical infrastructure, composed of KICS for Networks (passive network traffic analysis, detection and response with asset discovery) and KICS for Nodes (endpoint protection, detection and response) [4]. It is positioned as a detection-and-visibility platform for industrial control systems rather than an inline microsegmentation enforcement engine: network monitoring is out-of-band over mirrored traffic (SPAN/ERSPAN) or data diodes [3][5], while endpoint protection runs as an agent on Windows Server 2003-2025 and (via the sibling KICS for Linux Nodes product) Linux hosts [6][11]. Deployment is a single Server with up to 50 sensors, managed together with Kaspersky Security Center, in distributed, air-gapped or isolated OT environments [3][5]. The closest analogues to microsegmentation policy are Interaction Control "allow rules" (auto-generated in learning mode from observed traffic) and the KICS for Nodes Firewall and Applications Launch Control components [5][6].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 1                | 5      | 0   |
| partial          | 21    | 0                | 21     | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 4     | 0                | 0      | 4   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 11 items backed by ≥ 2 source_types; 21 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | — | Device Activity Detection monitors devices appearing in industrial traffic and automatically adds/updates devices in the asset table; the vendor case study describes asset discovery and network map visualization. [3], [5], [7] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Network interaction and topology maps are provided with automatic device grouping by category, vendor or subnet and up to 16 device labels; no App/Environment/Role/Process-specific map views are documented. [5], [7] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Event/log and traffic storage in the Server database is configurable (max volume plus an optional minimum storage time in days), but no default or guarantee of >=90-day retention is published. [5] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | Vulnerabilities are displayed as CVE IDs in device details and risk views reachable from the maps; CVE context is not overlaid directly on the map itself. [5] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | Activity of unknown devices is detected and flagged, unknown-device nodes appear on the network interaction map, and unauthorized communications trigger Network Integrity Control events in monitoring mode. [5] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Not Supported | medium | — | Interaction Control (allow) rules are constructed from protocol, system commands and MAC/IP/port address data of the interaction sides; no tag/label/identity-driven policy creation is documented. [5] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | Interaction Control rules are auto-generated in learning mode from observed network interactions, and the platform can generate exclusion rules from collected health data; no AI/ML-labeled recommendation engine is documented. [5], [11] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | — | Learning mode accumulates interaction data without enforcement and can auto-switch to monitoring mode; it functions as a dry-run but is not a dedicated policy-simulation engine. [5] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | — | Security policies can be exported and re-imported and node data backed up/restored via script; policy import is a manual multi-step process that temporarily takes the Server offline, not instant 1-click rollback. [5] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | — | Technology settings inherit from Server to sensors and monitoring points, and the device group tree supports six nesting levels; this is configuration inheritance rather than a hierarchical policy-rule model. [5] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | KICS for Nodes supports Windows Server 2003 through 2025 plus Windows desktop/embedded variants; Linux is covered by the separate KICS for Linux Nodes product; no AIX/Solaris support is documented. [3], [6], [11] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | — | no evidence found (No evidence found for container/Kubernetes/OpenShift isolation support in KICS documentation.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | — | The platform combines KICS for Networks (passive network sensors with agentless polling of network devices) and KICS for Nodes (endpoint agent); the VDC Research profile confirms the two-component architecture. [3], [4], [11] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | Deployment in air-gapped and isolated environments is documented, including data-diode connectivity for Server/sensors and fully offline operation certified by AV-Comparatives. [3], [5], [10] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Documented scale limits are up to 50 sensors per Server and 1000 computers receiving EPP telemetry; no workload count reaching 50,000 is published. [5] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | The vendor claims low footprint and tunable resource consumption without publishing CPU percentage figures. [1], [3] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | No agent RAM footprint is published; only host-level hardware minimums (e.g., 512 MB RAM for the protected device) and qualitative low-footprint claims appear in the documentation. [1], [6] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | KICS for Networks is deployed out-of-band on mirrored traffic (SPAN/ERSPAN), so it does not sit in the forwarding path; no measured latency figure is published. [3], [5] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | — | Network monitoring is passive and out-of-band, and the customer case study states the solution operates without affecting the operational continuity of technological processes. [3], [7] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | — | Version updates install over the existing installation without requiring a computer restart; the installation wizard's reboot prompt for the console is explicitly non-mandatory. [6] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | A documented REST API (versions 3/4 with SDK package) covers devices, events, tags, allow rules, vulnerabilities, risks and address spaces over HTTPS; 100% coverage of all admin functions is not documented. [5] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Connectors forward events to Syslog servers and SIEM systems in CEF format, with an HP ArcSight integration example documented. [5] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found (No evidence found for ServiceNow/CMDB integration.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found (No evidence found for CI/CD pipeline integration (Jenkins/GitLab/Terraform).) |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | — | Applications Launch Control allow/deny rules scope to executable files, scripts and MSI packages, and Process Control monitors industrial system commands; enforcement is application/command-level, not network-flow-at-process granularity. [5], [6] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | KSN/TI-Portal reputation lookups and IOC export are documented; no honeypot/deception capability is documented. [5], [6] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Security audit provides 3100+ pre-defined compliance audit rules with reports, and the company holds IEC 62443-4-1/ISO 27001/SOC 2 certifications; PCI-DSS/NIST 800-207-specific report templates are not evidenced. [1], [3], [5] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | Server-sensor, API and Endpoint Agent connections are encrypted over HTTPS with certificates, and client certificate verification is available for Endpoint Agent connections; TLS version and default mutual-auth settings are not specified. [5] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Not Supported | medium | — | The documentation states only one Server can be used per KICS for Networks deployment; no clustering or failover architecture is documented. [5] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (No evidence found for documented agent behavior when the Server/controller is unreachable.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | Node data (database, traffic, settings) can be backed up and restored locally via the kics4net-backup.sh script on Server and sensors; no multi-site disaster-recovery synchronization is documented. [5] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | The ecosystem holds Common Criteria ISO/IEC 15408 for Kaspersky Security Center 13 at EAL2+ (below EAL4+), IEC 62443-4-1 ML3 (TUV AUSTRIA) and an AV-Comparatives OT certification; no FIPS 140-2/140-3 or CC EAL4+ for KICS components was found. [8], [9], [10] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | — | Compatibility certificates cover Siemens (SIMATIC PCS 7, SPPA-T3000, WinCC OA), Schneider Electric, Emerson, Yokogawa and others; no Honeywell or ABB certificates are listed. [2] |

---

## 4. Notable Strengths

- **Deep OT asset discovery and network mapping (items 1.1, 1.2):** device activity detection automatically populates an asset table from traffic, and network interaction/topology maps with grouping and labels are documented [5][7].
- **Unrecognized/unauthorized traffic detection (items 1.5, 2.2):** unknown devices are flagged and unauthorized communications register Network Integrity Control events, with Interaction Control rules auto-generated in learning mode [5].
- **Dual agent-based and agentless architecture (item 3.3):** KICS for Networks provides passive, agentless network monitoring and polling while KICS for Nodes provides endpoint agents, a combination confirmed by VDC Research [3][4].
- **Air-gapped and offline operation (item 3.4):** deployment via data diodes and in fully isolated environments is documented, and AV-Comparatives certified offline post-breach execution prevention for KICS for Nodes [3][5][10].
- **SIEM integration via Syslog/CEF (item 5.2):** built-in connectors forward events in CEF format to Syslog and SIEM systems, with an HP ArcSight example [5].

## 5. Notable Gaps / Risks

- **No tag/label/identity-based policy (item 2.1):** Interaction Control rules are explicitly built from protocol, system commands and MAC/IP/port data, so the platform cannot express the label-based microsegmentation policy the checklist assumes; a buyer needing tag-driven segmentation would have to look elsewhere or layer another product on top.
- **No controller high availability (item 7.1):** the manual states only one Server per deployment and documents no clustering/failover, so the controller is a single point of failure in large or critical deployments.
- **Unknown container/Kubernetes, CMDB and CI/CD coverage (items 3.2, 5.3, 5.4):** no evidence was found for container isolation, ServiceNow/CMDB tag sync, or CI/CD pipeline integration in the current documentation; these are load-bearing for modern hybrid/DevSecOps use cases.
- **Numeric performance/scale claims are unquantified (items 1.3, 3.5, 4.1, 4.2, 4.3):** retention is configurable but no >=90-day guarantee is published, scale is documented only as sensor/EPP-count limits, and CPU/RAM/latency figures are qualitative, so capacity planning must rely on the vendor's stated hardware guidance.
- **Certification gap below procurement thresholds (item 8.1):** the ecosystem's Common Criteria certificate is EAL2+ on Kaspersky Security Center 13 [9], not EAL4+, and no FIPS 140-2/140-3 validation for KICS was found.

## 6. Evidence Quality Notes

Evidence rests on 11 staged sources: the two official Administrator's Guides (KICS for Networks 4.5 and KICS for Nodes 4.5 PDFs, ~19K and ~23K lines of extracted text), the platform page, certification/compatibility page, four-pager datasheet, two press releases, one vendor-hosted customer case study, and two certificate documents (TUV AUSTRIA IEC 62443-4-1 and the Italian Common Criteria EAL2+ certificate). Only one source is genuinely independent of the vendor (the VDC Research analyst profile, hosted by Kaspersky); everything else is vendor documentation or vendor-hosted material, so confidence is capped at medium for all but item 3.3. Eleven items draw on 2+ source types; the rest rely on vendor_doc only.

No contradictions between sources were found; the main judgment calls were (a) rating 2.1 and 7.1 as not_supported from explicit documentation (rule fields are MAC/IP/port-based; "only one Server can be used" per deployment) rather than from silence, and (b) keeping 1.3, 3.5, 4.1, 4.2 and 4.3 at partial with no numeric_value because the vendor publishes configurable-but-undocumented retention, sensor/EPP-count limits instead of workload counts, and qualitative footprint/latency language. The AV-Comparatives press release was treated as vendor-reported (product_release_notes) rather than third-party evidence, since only the announcement, not the test report, was accessible.

---

## Bibliography

[1] Kaspersky. "Kaspersky Industrial Cybersecurity Platform - product page". https://www.kaspersky.com/enterprise-security/industrial-cybersecurity (Retrieved: 2026-08-10T17:00:30Z)
[2] Kaspersky. "Certificates for Kaspersky Industrial CyberSecurity (certification & compatibility page)". https://www.kaspersky.com/enterprise-security/industrial-cybersecurity/certification (Retrieved: 2026-08-10T17:00:30Z)
[3] Kaspersky. "Kaspersky Industrial CyberSecurity - four-pager datasheet". https://content.kaspersky-labs.com/se/media/en/enterprise-security/kics/kaspersky-industrial-cybersecurity-four-pager-datasheet.pdf (Retrieved: 2026-08-10T17:00:30Z)
[4] VDC Research. "VDC Research: Kaspersky Profile - The Global Market for OT Cybersecurity Software & Services (Aug 2024)". https://content.kaspersky-labs.com/se/media/en/enterprise-security/Kaspersky%20Profile%20-%202024-The-Global-Market-for-OT-Cybersecurity-Software-and-Services-VDC-Research.pdf (Retrieved: 2026-08-10T17:00:30Z)
[5] Kaspersky. "Kaspersky Industrial CyberSecurity for Networks 4.5 - Administrator's Guide (Online Help)". https://img.kaspersky.com/oh/KICSforNetworks/4.5/en-US/KICSforNetworks-4.5-en-US.pdf (Retrieved: 2026-08-10T17:00:30Z)
[6] Kaspersky. "Kaspersky Industrial CyberSecurity for Nodes 4.5 - Administrator's Guide (Online Help)". https://img.kaspersky.com/oh/KICS4Nodes/4.5/en-US/KICS4Nodes-4.5-en-US.pdf (Retrieved: 2026-08-10T17:00:30Z)
[7] Kaspersky. "Kaspersky protects AGC plant in Germany (case study)". https://content.kaspersky-labs.com/se/media/en/business-security/enterprise/kics-agc-case-study.pdf (Retrieved: 2026-08-10T17:00:30Z)
[8] TUV AUSTRIA Standards & Compliance. "TUV AUSTRIA Certificate IEC 62443-4-1 (ML3) for KICS for Networks and KICS for Nodes". https://content.kaspersky-labs.com/fm/site-editor/e8/e84dbf46f59b35cfbdf970dfe86f2504/source/tasccertificateiec6244341kaspersky20262.pdf (Retrieved: 2026-08-10T17:00:30Z)
[9] Ministero dello Sviluppo Economico (Italy). "Common Criteria ISO/IEC 15408 certificate No. 5/22 - Kaspersky Security Center 13.0.0.11247 (EAL2+)". https://content.kaspersky-labs.com/se/media/en/enterprise-security/common-criteria-isoiec-15408.pdf (Retrieved: 2026-08-10T17:00:30Z)
[10] Kaspersky. "Kaspersky Industrial CyberSecurity receives OT Certification from AV-Comparatives (press release)". https://www.kaspersky.com/about/press-releases/kaspersky-industrial-cybersecurity-receives-ot-certification-from-av-comparatives (Retrieved: 2026-08-10T17:00:30Z)
[11] Kaspersky. "Kaspersky Industrial Cybersecurity enhances performance (press release, Nov 5 2025)". https://www.kaspersky.com/about/press-releases/kaspersky-industrial-cybersecurity-enhances-performance-new-capabilities-improve-network-security-and-operational-effectiveness (Retrieved: 2026-08-10T17:00:30Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 11 (kept: 11, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 1, case_study: 1, certification_registry: 2, product_release_notes: 2, vendor_datasheet: 1, vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
