# Microsegmentation Product Assessment: NanoLock Security (now OTOPIQ) - NanoLock ZeroTrust OT Security

**Product ID:** `nanolock-zerotrust-ot-security`
**Version reference:** Current product line as marketed by successor OTOPIQ (2026 solution brief and platform pages); NanoLock-branded materials staged from 2022-2023 third-party coverage because nanolocksecurity.com is decommissioned
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T21:05:00Z
**Total evidence items collected:** 40
**Total distinct sources:** 12

---

## 1. Overview

NanoLock ZeroTrust OT Security is a device-level, zero-trust protection and management platform for OT/ICS environments, now marketed by successor company OTOPIQ after nanolocksecurity.com was decommissioned [1, 2, 6]. The vendor positions it as probe-less, AI-driven security for Level 1-2 OT assets (PLCs, RTUs, HMIs and engineering workstations), combining continuous device discovery, live communication mapping, identity-based access control with MFA, CVE-correlated change detection, and one-click configuration rollback [1, 2]. It is not a network microsegmentation platform: policy is enforced at the device/configuration level rather than as IP-independent network segmentation rules, and the vendor does not document flow-history retention, container support, a REST API, or controller HA clustering [1, 2]. Deployment is embedded/probe-less across legacy and new devices, including offline and air-gapped networks, with SIEM export and generic regulatory-compliance support [1, 2]. Third-party coverage from 2022-2023 confirms the device-level zero-trust approach and its positioning for industrial and manufacturing customers [6, 7, 9, 10].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 0                | 3      | 0   |
| partial          | 14    | 0                | 14     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 15    | 0                | 0      | 15  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 11 items backed by ≥ 2 source_types; 14 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | The vendor documents continuous discovery of Level 1-2 OT devices via passive, probe-less technology that builds a live vendor-agnostic inventory, plus live communication mapping and continuous visibility powered by AI-driven automation. [1], [2] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Live communication mapping is documented, but the staged sources do not describe grouping the connectivity map by Application, Environment, Role or Process labels. [1], [2] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | - | no evidence found (No flow/connection-history retention period is published; only device configuration-history retention is documented, with no duration.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | - | CVE correlation is documented as a real-time detection feature that exposes vulnerabilities and unauthorized edits, but a CVE overlay rendered directly on the connectivity map is not documented. [1], [2] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | - | Communication-anomaly detection and ML-based correlation of communication patterns with user actions are documented, but explicit detection of hidden or unrecognized traffic flows is not described. [1], [2] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | - | Identity- and role-based access control for device configuration changes (with MFA and group policies) is documented and is not IP/VLAN-dependent, but a label/tag-based network segmentation policy engine is not documented. [1], [2], [3] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | - | no evidence found (ML-based analysis of device state and communication patterns is documented for risk triage, but automatic policy/rule recommendation is not mentioned.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | - | no evidence found (No policy simulation or dry-run mode is mentioned in any staged source.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Supported | medium | - | The solution brief documents automatic backup of every configuration change and one-click rollback to a known-good state, and the platform page advertises instant recovery from unauthorized changes. [1], [2] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found (Standardized governance across distributed operations is mentioned, but inherited or hierarchical rule structures are not documented.) |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Unknown | low | - | no evidence found (No OS support matrix (Windows Server versions, RHEL/CentOS/Ubuntu, AIX, Solaris) appears in staged sources.) |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (No container, Kubernetes or OpenShift support is mentioned in staged sources.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | A passive, probe-less (agentless) device-level approach is documented, but an agent-based deployment option is not documented in the staged sources. [1], [2] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | The platform page states devices are kept secure whether connected, offline, or air-gapped, and lists air-gapped networks as a supported environment. [1] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Unknown | low | - | no evidence found (No workload-scale figure (e.g., number of protected devices per management server) is published in staged sources.) |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | Only qualitative claims are available (zero impact on performance and functionality, zero disruption during deployment); no CPU-percentage figure is published, so the <1% CPU threshold cannot be verified. [1], [6], [9] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | Only qualitative claims of no impact on performance or functionality are available; no memory-footprint figure is published, so the <100MB RAM threshold cannot be verified. [1], [6], [10] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | - | no evidence found (No network-latency figure or latency-impact measurement is mentioned in staged sources.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | - | no evidence found (No documentation of agent fail-open/fail-closed behavior on agent crash; the 'Fail Safe Kit' refers to disaster recovery, not agent failure.) |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | - | Fast, non-disruptive deployment (no vendor coordination or system changes, uptime maintained during deployment) is claimed, but an explicit 'no reboot required for agent install/update' statement is not documented. [1], [6] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Unknown | low | - | no evidence found (No REST API or programmatic administration surface is documented in staged sources.) |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | - | Export/integration of audit trails and alerts with SOC, SIEM and analytics systems is documented, but specific SIEM/SOAR products (Splunk, QRadar, Sentinel) and protocols (Syslog/CEF) are not named. [1] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found (No CMDB (e.g., ServiceNow) integration for label/tag synchronization is documented.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No CI/CD pipeline integration (Jenkins, GitLab, Terraform) is documented.) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | - | no evidence found (Device- and configuration-level access control is documented, but process-level enforcement is not mentioned in staged sources.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Detection features correlate behaviors with known weaknesses and CVEs and apply ML-based analysis of communication patterns, but no honeypot or deception-detection capability is documented. [2] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | General compliance support (simplifying audits, meeting global regulatory standards) is documented, but no named report templates for PCI-DSS, NIST 800-207, ISO 27001 or IEC 62443 appear in staged sources. [1], [2], [3] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | Encryption in transit and at rest is documented, but the TLS version (1.3) and mutual authentication (mTLS) are not specified. [2] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | - | no evidence found (No high-availability cluster architecture for the management server is documented.) |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | The platform states devices remain secure whether connected, offline or air-gapped, which implies embedded enforcement independent of the management server, but explicit autonomous policy enforcement on controller loss is not documented. [1] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Disaster recovery via an encrypted Fail Safe Kit and restore from configuration history is documented, but DR-site synchronization is not documented. [2] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | - | The NIST CMVP active-module catalog embedded in the staged search pages for keywords 'nanolock' and 'otopiq' contains no NanoLock/Otopiq FIPS 140-2/140-3 validated module, and no staged vendor document claims FIPS or Common Criteria certification. [11], [12] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (No staged source mentions Siemens, Honeywell or ABB software compatibility certifications for OT.) |

---

## 4. Notable Strengths

- **Probe-less continuous discovery and communication mapping (items 1.1, 1.2):** the platform builds a live vendor-agnostic inventory of Level 1-2 devices using passive, probe-less technology and visualizes live communication mappings, covering connected, offline and air-gapped assets [1, 2].
- **Identity-based, IP-independent access control (item 2.1):** device configuration changes are gated by identity, MFA and role-based permissions rather than IP or VLAN, with full user-to-device accountability [2, 3].
- **One-click configuration rollback (item 2.4):** every configuration change is backed up automatically and can be rolled back to a known-good state in one click, including via an encrypted Fail Safe Kit for disaster recovery [2].
- **Air-gapped and offline support (items 3.4, 7.2):** the platform explicitly states devices remain secure whether connected, offline or air-gapped, consistent with embedded device-level enforcement [1].
- **Detection and recovery depth for OT (items 6.2, 7.3):** real-time monitoring of PLC logic and HMI projects correlates changes with known CVEs, and configuration history plus the Fail Safe Kit provide recovery paths after unauthorized changes [2].

## 5. Notable Gaps / Risks

- **Not a microsegmentation platform (items 1.3, 2.3, 5.1, 7.1):** no connection-flow history retention period, policy simulation/dry-run, REST API, or controller HA clustering is documented; buyers seeking network-level segmentation features would need to look elsewhere [1, 2].
- **No numeric performance data (items 4.1, 4.2, 4.3):** only qualitative claims (zero impact on performance) are published; the <1% CPU, <100MB RAM and <0.1ms latency thresholds are unverified, and no network-latency figure exists at all [1, 6, 9].
- **No evidence for agent-based deployment or process-level control (items 3.3, 6.1):** the approach is probe-less/agentless only, and process-level enforcement is not documented [1, 2].
- **No FIPS 140-2/140-3 or Common Criteria certification found (item 8.1):** the NIST CMVP active-module catalog contains no NanoLock/Otopiq module, and no vendor document claims FIPS or Common Criteria validation [11, 12].
- **Ecosystem integration is thin (items 5.2, 5.3, 5.4):** SIEM export is mentioned generically, but no named SIEM/SOAR products, protocols (Syslog/CEF), CMDB sync, or CI/CD integration is documented [1].

## 6. Evidence Quality Notes

No item was triangulated across three or more independent sources; 11 items were backed by two or more source types, and 14 items rested on vendor documentation alone (platform page, solution brief, vertical pages), capping their confidence at medium per the validator rule. The vendor's own site rebranded from NanoLock to OTOPIQ and the old nanolocksecurity.com domain is decommissioned, so vendor evidence for the current product line comes from the 2026 OTOPIQ pages and solution brief; NanoLock-branded materials (2022-2023) are represented by Help Net Security, CSO Online and SecurityBrief India coverage plus partner announcements from Waterfall and OTIFYD [1-10]. Because archive.org and archive.ph were rate-limited throughout the session, Wayback snapshots of the original NanoLock product pages could not be staged.

The main risk to these verdicts is absence-of-evidence: 15 items (flow retention, policy simulation, containers, scalability, latency, fail-safe, REST API, CMDB/CI/CD, process-level enforcement, HA clustering, OT vendor certifications) are `unknown` because no staged source addresses them, not because the vendor definitively lacks the feature [1, 2]. No direct contradictions were found between sources; the only qualitative-vs-quantitative gap is performance, where vendor and third-party materials uniformly claim zero impact on performance without publishing numbers, so 4.1/4.2 were kept partial with no numeric_value rather than asserting a figure [1, 6, 9, 10]. The FIPS negative (8.1) rests on the NIST CMVP registry catalog embedded in the staged search pages, which is authoritative for FIPS but leaves Common Criteria unverified because the Common Criteria portal blocked automated access [11, 12].

---

## Bibliography

[1] OTOPIQ (formerly NanoLock Security). "The OTOPIQ Platform (vendor product page; successor branding of NanoLock Security)". https://otopiqsecurity.com/platform-otopiq/ (Retrieved: 2026-08-10T21:00:00Z)
[2] OTOPIQ (formerly NanoLock Security). "The OTOPIQ Platform - Solution Brief (PDF; successor branding of NanoLock Security)". https://otopiqsecurity.com/wp-content/uploads/2026/06/The-OTOPIQ-Platform-Solution-Brief.pdf (Retrieved: 2026-08-10T21:00:00Z)
[3] OTOPIQ (formerly NanoLock Security). "Industrial and Manufacturing (vendor vertical page)". https://otopiqsecurity.com/industrial-and-manufacturing/ (Retrieved: 2026-08-10T21:00:00Z)
[4] OTOPIQ (formerly NanoLock Security). "Energy Utilities (vendor vertical page)". https://otopiqsecurity.com/energy-utility/ (Retrieved: 2026-08-10T21:00:00Z)
[5] OTOPIQ (formerly NanoLock Security). "Water Utilities (vendor vertical page)". https://otopiqsecurity.com/water-utility/ (Retrieved: 2026-08-10T21:00:00Z)
[6] Help Net Security. "NanoLock's zero trust security solutions protect ICS devices and industrial machines". https://www.helpnetsecurity.com/2022/05/18/nanolock-cybersecurity-solutions/ (Retrieved: 2026-08-10T21:00:00Z)
[7] CSO Online. "NanoLock's zero-trust cybersecurity suite to protect industrial machinery, production lines". https://www.csoonline.com/article/572753/nanolock-s-zero-trust-cybersecurity-suite-to-protect-industrial-machinery-production-lines.html (Retrieved: 2026-08-10T21:00:00Z)
[8] Waterfall Security Solutions. "NanoLock and Waterfall to Deliver OT Security for Industrial and Energy Applications (partner announcement)". https://waterfall-security.com/about-waterfall/news/nanolock-and-waterfall-to-deliver-ot-security-for-industrial-and-energy-applications/ (Retrieved: 2026-08-10T21:00:00Z)
[9] OTIFYD. "NanoLock Security and OTIFYD Partner to Provide World's Leading Industrial Cyber Protection (partner announcement)". https://otifyd.com/blog/nanolock-otifyd-partnership/ (Retrieved: 2026-08-10T21:00:00Z)
[10] SecurityBrief India. "NanoLock Security and OTIFYD to provide top-tier OT protection for manufacturing". https://securitybrief.in/story/nanolock-security-and-otifyd-to-provide-top-tier-ot-protection-for-manufacturing (Retrieved: 2026-08-10T21:00:00Z)
[11] NIST CSRC. "NIST CMVP Validated Modules Search (keyword: nanolock) - no NanoLock module listed". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&CertificateStatus=Active&ValidationYear=0&Keyword=nanolock (Retrieved: 2026-08-10T21:00:00Z)
[12] NIST CSRC. "NIST CMVP Validated Modules Search (keyword: otopiq) - no OTOPIQ module listed". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&CertificateStatus=Active&ValidationYear=0&Keyword=otopiq (Retrieved: 2026-08-10T21:00:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 8
- **Sources reviewed:** 12 (kept: 12, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, third_party_review: 3, vendor_blog: 2, vendor_datasheet: 1, vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
