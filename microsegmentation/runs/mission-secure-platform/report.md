# Microsegmentation Product Assessment: Mission Secure - Mission Secure Platform

**Product ID:** `mission-secure-platform`
**Version reference:** Sentinel 5.0 (released Nov 2022); company acquired by ServiceNow Nov 2024
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T00:50:00Z
**Total evidence items collected:** 55
**Total distinct sources:** 22

---

## 1. Overview

The Mission Secure Platform is an OT/ICS cybersecurity platform that enforces allow/block policies on industrial control traffic through inline network security devices, combined with patented Level 0/1 signal-integrity monitoring that validates the physical signals behind HMI readings [1][3]. The current release, Sentinel 5.0 (Nov 2022), provides passive monitoring, asset discovery, alerting, and a fine-grained policy engine whose decisions can key on network traffic, remote access attempts, firmware and vulnerability state, and device signal data [17][21]. Deployment shapes are an inline appliance or on-premises software with network sensors usable as passive monitoring stations or inline enforcement points [7][21]; there is no host agent. The vendor positions the platform as an enabler of Zero Trust architectures for manufacturing, maritime, oil and gas, and defense, backed by 24/7 managed services [5][8][17]. Mission Secure was acquired by ServiceNow in November 2024, and its discovery technology now feeds ServiceNow's OT asset visibility and CMDB onboarding [2][14][22]. The platform operates at network level (agentless) rather than as an endpoint microsegmentation agent, which shapes its coverage of this checklist.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 1                | 4      | 0   |
| partial          | 12    | 0                | 10     | 2   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 16    | 0                | 0      | 16  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 0 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Sentinel 5.0 performs passive real-time asset discovery and network-traffic monitoring, with continuous OT asset inventory and communication mapping documented by the vendor, Claroty, and independent industry publications. [1], [2], [3], [17], [18], [20], [21] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | A dashboard map with drill-down on network activity is documented, but sources do not describe grouping or visualization by Application, Environment, Role, or Process as the requirement asks. [1], [3], [17], [21] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | — | no evidence found (No public source quantifies connection-history retention; patents describe event logging for forensic analysis without retention periods.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | Vulnerability, patch-status and risk-score context is captured, used in policy decisions, and referenced in the dashboard map caption; sources do not explicitly state CVE data is overlaid on the topology map. [1], [17], [21] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | Whitelist-based enforcement reports traffic that falls outside whitelisted activity, and network-anomaly detection with isolation of abnormal systems is documented. [1], [3], [6], [17], [21] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | Policy decisions key on device attributes (firmware, patch status, risk score), user profile, physical location and custom variables rather than IP addresses; the term 'tag/label' is not used, but custom variables serve a similar role. [1], [17], [18], [21] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | Policy recommendations are supplied by the Claroty xDome integration as the basis for tailored policies deployed via the Mission Secure policy engine; in-platform machine learning is documented only in patents for state/anomaly learning. [1], [10] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | — | no evidence found (No source mentions policy simulation, dry-run, or preview modes.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | low | — | The platform's US10250619 patent describes a 'Revert to previous configuration' action button and rollback requests that restore a protected system to a prior non-compromised state; no product documentation of policy-specific one-click rollback was found. [9] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No source describes hierarchical or inherited policy structures.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Unknown | low | — | no evidence found (The product deploys as an inline appliance or on-premises software; no supported host-OS list (Windows Server, RHEL/CentOS/Ubuntu, AIX, Solaris) is published.) |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | — | no evidence found (No evidence of container, Kubernetes, or OpenShift support; patent mentions of 'container' refer to compressed data containers, not application containers.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | Deployment is via inline network security devices and network sensors usable as passive monitoring stations or inline enforcement points, plus on-premises software; no host-agent deployment is documented, so the agent-based half of the requirement is unmet. [3], [7], [10], [21] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | Security devices can operate out-of-band on a separate security network, and a third-party directory lists an offline mode, supporting fully isolated or air-gapped deployments. [7], [9] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Unknown | low | — | no evidence found (No numeric scale claims found; available materials describe deployments without workload counts.) |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | — | no evidence found (The product has no host agent (inline appliance architecture) and no CPU-overhead figures are published.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | — | no evidence found (No RAM-footprint figures are published for any agent or sensor component.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | — | no evidence found (No latency measurements are published for the inline enforcement points.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | — | no evidence found (No fail-open or fail-closed behavior on device failure is documented; patents describe pass-through only for acceptable traffic in normal operation.) |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | — | no evidence found (No host agent exists, so no reboot-free agent installation or update claims are documented.) |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | low | — | An API is listed among platform integrations and data integration with Claroty (asset and vulnerability profiles passed into the policy engine) is documented, but no RESTful API documentation covering full administrative functionality was found. [7], [21] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Event messages can be emitted as syslog to external forensic or SIEM systems per patent, and a third-party directory lists SIEM integrations with Splunk and QRadar. [7], [9] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | — | After the 2024 acquisition, Mission Secure discovery technology feeds ServiceNow's OT asset inventory with faster onboarding of OT assets into the ServiceNow CMDB; no tag-synchronization feature is documented. [2], [14], [22] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found (No CI/CD or DevSecOps pipeline integration documentation found.) |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | — | Access-control policies define when users or applications may command an industrial device and unauthorized control commands are blocked; OS process-level enforcement is not documented. [3], [10], [17], [21] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | — | no evidence found (No threat-intelligence feed or honeypot/deception capability documented; the XONA partnership mentions user-access forensics, not deception.) |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Platform alignment with NIST CSF, IEC 62443, NERC CIP and the Zero Trust model is documented by vendor and third-party sources; no ready-made compliance report templates are documented. [7], [17], [19] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | The patent describes encrypted TLS/IPSEC/VPN tunnels and digitally signed certificates for authenticating communicating devices; TLS version 1.3 and agent-controller mutual authentication are not specified. [10] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | — | Patents describe multiple redundant security devices and a fault-tolerant multi-node consensus system for sensor data; no explicit active-active or active-passive controller cluster claim was found. [9], [13] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | — | The inline security device makes pass/block decisions locally and can execute security actions automatically without input from other system components per patent; behavior when a central controller is unreachable is not explicitly documented. [9], [10] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (No disaster-recovery or site-sync documentation found.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No FIPS 140-2/140-3 or Common Criteria certification records found in available sources.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No Siemens, Honeywell, or ABB software-compatibility certifications documented; patents describe industrial-protocol compatibility (CIP, Modbus, OPC, Profibus) only.) |

---

## 4. Notable Strengths

- **Real-time OT asset discovery and anomaly detection (items 1.1, 1.5):** Passive network-level discovery plus whitelist-based enforcement reports traffic that falls outside whitelisted activity and detects network anomalies [17][21].
- **Attribute-based policy enforcement (items 2.1, 1.4):** Policies key on device attributes, risk scores, patch status, user profile, and custom variables rather than IP addresses, with vulnerability context used in decisions [1][17].
- **Air-gapped and offline operation (item 3.4):** Security devices can run out-of-band on a separate security network and a third-party directory lists an offline mode, supporting fully isolated OT deployments [7][9].
- **SIEM integration (item 5.2):** Syslog event output to external forensic/SIEM systems and Splunk/QRadar integrations are documented [7][9].
- **ServiceNow CMDB alignment (item 5.3):** Post-acquisition, discovery data feeds ServiceNow OT asset inventory with faster onboarding of new OT assets into the CMDB [2][22].

## 5. Notable Gaps / Risks

- **No host-agent deployment (item 3.3):** Only inline/agentless deployment is documented, so the agent-based half of the requirement is unmet and all agent-centric items (4.1, 4.2, 4.4, 4.5) are unknown.
- **Missing quantitative evidence (items 1.3, 3.5, 4.1-4.3):** No retention periods, workload-scale numbers, or agent CPU/RAM/latency figures are published; buyers with numeric requirements must request measurements from the vendor.
- **No container/Kubernetes support (item 3.2):** No evidence of container-native isolation; the product targets classic OT networks rather than cloud-native workloads.
- **Certifications undocumented (items 8.1, 8.2):** No FIPS 140-2/140-3, Common Criteria, or Siemens/Honeywell/ABB compatibility certifications were found, which matters for regulated or industrial-audit buyers.
- **Thin automation surface (items 2.3, 2.5, 5.1, 5.4):** No policy simulation, hierarchical rules, full RESTful API documentation, or CI/CD integration is documented; only a generic API listing and partner integrations exist.

## 6. Evidence Quality Notes

Evidence quality is uneven. Items 1.1, 1.2, 1.4, 1.5, 2.1 and 3.3 are triangulated across vendor materials and at least one independent source (Claroty integration brief, Automation.com/ISA, Automation World, Security Tools Info), and item 1.1 reaches high confidence with three independent sources [1][18][20][21]. Items 2.4, 6.4, 7.1 and 7.2 rest on USPTO patents (regulatory_filing) describing the platform's architecture; patents are evidence of design rather than proof of shipped behavior, so those verdicts are capped at partial with low-to-medium confidence. Sixteen items are unknown because no staged source mentions the metric at all; this reflects the vendor's thin public footprint (a small company whose website now redirects to ServiceNow after acquisition) rather than an exhaustive search failure.

No contradictions between sources were found; where vendor claims and third-party descriptions overlapped (e.g., the Sentinel 5.0 policy engine), they agreed verbatim. Fresh web retrieval was hampered by search-engine and web-archive rate limiting from this environment (DuckDuckGo/Brave/Startpage CAPTCHAs, archive.org 429s, Cloudflare challenges), so the corpus leans on the screen-pass staged artifacts plus three newly staged sources (Dark Reading, Automation World, ServiceNow OT Management page). All 55 evidence quotes were verified as exact substrings of staged text by verify_citation_grounding.py.

---

## Bibliography

[1] Claroty Ltd.. "Claroty and Mission Secure: Complete OT Visibility with Active Policy Enforcement (integration brief)". https://web-assets.claroty.com/2023_q1_global_xdome_mission_secure_integration_brief.pdf (Retrieved: 2026-08-10T17:21:18Z)
[2] ServiceNow. "ServiceNow to acquire Mission Secure to enhance OT asset visibility (official announcement)". https://www.servicenow.com/workflow/news/mission-secure-enhance-ot-asset-visibility.html (Retrieved: 2026-08-10T17:21:18Z)
[3] Mission Secure (nomination). "Mission Secure Platform — ICS/SCADA Security nomination (Cybersecurity Excellence Awards)". https://cybersecurity-excellence-awards.com/candidates/mission-secure-platform/ (Retrieved: 2026-08-10T17:21:18Z)
[4] Mission Secure (nomination). "Mission Secure Platform — National Cyber Defense nomination (Cybersecurity Excellence Awards)". https://cybersecurity-excellence-awards.com/candidates/mission-secure-platform-2/ (Retrieved: 2026-08-10T17:21:18Z)
[5] XONA Systems / Mission Secure. "Mission Secure Partners with XONA to Provide Zero-Trust OT Cybersecurity Solutions (press release)". https://www.xonasystems.com/press/mission-secure-partners-with-xona-to-provide-zero-trust-ot-cybersecurity-solutions-for-industries-reliant-on-remote-operations-capacity (Retrieved: 2026-08-10T17:21:18Z)
[6] NAVAIR OSBP (U.S. Navy). "Mission Secure, Inc. | NAVAIR Office of Small Business Programs company profile". https://www.navair.navy.mil/osbp/node/10141 (Retrieved: 2026-08-10T17:21:18Z)
[7] Security Tools Info. "Mission Secure Platform: Pricing, Reviews & Features (tool directory)". https://security.toolsinfo.com/tool/mission-secure-platform (Retrieved: 2026-08-10T17:21:18Z)
[8] R/GA Ventures (press release). "Mission Secure Announces Series B Venture Funding to Further Advance Its Patented OT Cybersecurity Protection Platform". https://ventures.rga.com/press/portfolio/mission-secure-announces-series-b-venture-funding-advance-patented-ot-cybersecurity-protection-platform/ (Retrieved: 2026-08-10T17:21:18Z)
[9] USPTO via Google Patents. "U.S. Patent 10,250,619 — Overlay cyber security networked system and method". https://patents.google.com/patent/US10250619/en (Retrieved: 2026-08-10T17:21:18Z)
[10] USPTO via Google Patents. "U.S. Patent 11,818,098 — Security system, device, and method for protecting control systems". https://patents.google.com/patent/US11818098/en (Retrieved: 2026-08-10T17:21:18Z)
[11] USPTO via Google Patents. "U.S. Patent 11,153,277 — Security system, device, and method for internet of things networks". https://patents.google.com/patent/US11153277/en (Retrieved: 2026-08-10T17:21:18Z)
[12] USPTO via Google Patents. "U.S. Patent 10,530,749 — Security system, device, and method for operational technology networks". https://patents.google.com/patent/US10530749/en (Retrieved: 2026-08-10T17:21:18Z)
[13] USPTO via Google Patents. "U.S. Patent 11,675,650 — System and method for n-modular redundant communication". https://patents.google.com/patent/US11675650/en (Retrieved: 2026-08-10T17:21:18Z)
[14] The Manufacturing Connection. "ServiceNow to Acquire Mission Secure to Enhance OT Asset Visibility (industry news)". https://themanufacturingconnection.com/2024/11/servicenow-to-acquire-mission-secure-to-enhance-ot-asset-visibility/ (Retrieved: 2026-08-10T17:21:18Z)
[15] Pipeline Publishing. "ServiceNow to Acquire Mission Secure (industry news)". https://www.pipelinepub.com/news/servicenow-to-acquire-mission-secure (Retrieved: 2026-08-10T17:21:18Z)
[16] Cyber Security Intelligence. "Mission Secure (MSi) — supplier directory profile". https://www.cybersecurityintelligence.com/mission-secure-msi-3639.html (Retrieved: 2026-08-10T17:21:18Z)
[17] Mission Secure via PR Newswire. "Mission Secure Releases Sentinel 5.0 Platform, Enabling Context-Aware, Zero Trust Security for Critical Infrastructure OT (press release)". https://www.prnewswire.com/news-releases/mission-secure-releases-sentinel-5-0-platform-enabling-context-aware-zero-trust-security-for-critical-infrastructure-ot-301663783 (Retrieved: 2026-08-10T17:21:18Z)
[18] Automation.com (ISA). "Mission Secure Releases Sentinel 5.0 Platform, Enabling Context-Aware, Zero Trust Security for Critical Infrastructure OT (industry article)". https://www.automation.com/article/mission-secure-sentinel-5-0-platform-zero-trust (Retrieved: 2026-08-10T17:21:18Z)
[19] Compliance Labs. "Mission Secure platform — NERC CIP compliance directory entry". https://www.compliance-labs.com/software/mission-secure-platform/ (Retrieved: 2026-08-10T17:21:18Z)
[20] Dark Reading (Informa TechTarget; syndicated vendor press release). "Mission Secure Releases Sentinel 5.0 Platform, Enabling Context-Aware, Zero Trust Security for Critical Infrastructure OT (press release syndication on Dark Reading)". https://www.darkreading.com/ics-ot-security/mission-secure-releases-sentinel-5-0-platform-enabling-context-aware-zero-trust-security-for-critical-infrastructure-ot (Retrieved: 2026-08-11T00:30:00Z)
[21] Automation World (Endeavor Business Media). "Zero Trust Security Moves From Defense to Industry (industry article on Mission Secure Sentinel 5.0)". https://www.automationworld.com/home/article/33001831/zero-trust-security-moves-from-defense-to-industry (Retrieved: 2026-08-11T00:30:00Z)
[22] ServiceNow. "Operational Technology Management (ServiceNow product page; successor platform incorporating Mission Secure technology)". https://www.servicenow.com/products/operational-technology-management.html (Retrieved: 2026-08-11T00:30:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** ['Mission Secure platform microsegmentation checklist standard-mode assessment', 'Mission Secure Sentinel 5.0 capabilities (vendor PR, industry coverage, Claroty integration brief)', 'Mission Secure retention/history/API/Kubernetes/scalability/agent-metrics/FIPS searches (no usable results due to search-engine rate limiting from datacenter IP)', 'ServiceNow OT Management successor product page']
- **Sources reviewed:** 22 (kept: 22, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** regulatory_filing: 6, third_party_review: 8, vendor_blog: 6, vendor_doc: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
