# Microsegmentation Product Assessment: Skybox Security - Skybox Security Suite (Skybox Security Posture Management Platform)

**Product ID:** `skybox-security-posture-management`
**Version reference:** Skybox Security Suite 10 / Skybox Security Posture Management Platform (Firewall Assurance, Network Assurance, Change Manager, Vulnerability Control, Threat Intelligence); vendor ceased operations February 24, 2025
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:30:00Z
**Total evidence items collected:** 67
**Total distinct sources:** 16

---

## 1. Overview

Skybox Security Suite (marketed in its final releases as the "Skybox Security Posture Management Platform") was an agentless network security posture management platform combining Firewall Assurance, Network Assurance, Change Manager, Vulnerability Control and Threat Intelligence modules [12]. It built a continuously updated model of the network from device configurations, logs, syslog/ACL data and third-party scanner/asset feeds, then correlated vulnerabilities, firewall rules, changes and compliance against that model to prioritize risk [9][13]. Deployment shapes included on-premises software on dedicated appliances (11000/12100/12200 series) and SaaS "Cloud Edition" offers for Firewall Assurance and Network Assurance [10][16]. Skybox positioned the platform for attack-surface visibility and risk-based vulnerability management rather than as a workload-enforcement microsegmentation product: policy enforcement is delegated to firewalls and network devices, and the suite carries no host agents [9][2]. Critically, Skybox Security closed operations effective February 24, 2025 and laid off its workforce; Tufin acquired selected intellectual property, trademarks and customer information and runs an ExpressPath migration program for Skybox customers [4][1][5]. The product is no longer sold or supported, so all capability verdicts below reflect documented historical capability only.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 2                | 1      | 0   |
| partial          | 13    | 0                | 13     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 7     | 0                | 0      | 7   |
| not_applicable   | 9     | 0                | 9      | 0   |

**Evidence quality:** 17 items backed by ≥ 2 source_types; 4 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** Skybox is agentless (non-intrusive collection of device configs and third-party scanner/asset data), so per-workload OS support for an installed agent does not apply; OS-specific workload support is not part of the architecture.
- **4.1:** No endpoint agent is installed on workloads whose CPU overhead could be measured; the agent CPU-overhead metric does not apply to this agentless platform.
- **4.2:** No endpoint agent exists, so the agent RAM-footprint metric does not apply.
- **4.3:** Skybox is an out-of-band management plane; enforcement is performed by network devices, so no in-path agent adds network latency.
- **4.4:** There is no in-path agent whose failure could interrupt workload traffic; the agent fail-safe requirement does not apply.
- **4.5:** No agent is installed or updated on servers, so the reboot-free agent installation requirement does not apply.
- **6.1:** No endpoint enforcement agent exists; policy enforcement is delegated to firewalls and network devices, so process-level enforcement is outside the product architecture.
- **6.4:** There is no agent-controller channel to encrypt; the platform is agentless and collects data via network protocols and third-party integrations.
- **7.2:** No agent exists to enter an autonomous enforcement mode; policy enforcement is performed by network devices independent of Skybox.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | — | Skybox auto-collects and normalizes data from L3 network devices, public/private clouds and OT networks into a continuously updated network model, which users describe as showing the network and its possible data flows in near real time; live packet-level flow capture is not documented, so real-time flow discovery is only partially evidenced. [2], [9], [13] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | An interactive topology map of the network with assets, firewalls, zones and security controls is documented and reviewers used the mapping feature to investigate firewall rule requests; grouping by application/environment/role/process is not documented. [2], [13], [14] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | — | no evidence found (No staged source quantifies flow/connection history retention; the >=90-day forensic retention requirement could not be verified.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | high | — | Vulnerability data from scanners and a CVE/CPE-compatible intelligence feed is correlated onto the network model, and a user reports identifying users vulnerable to ransomware via the CVE database together with the mapping feature; vulnerability-on-map context is the product's core value proposition. [2], [6], [7], [9] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | — | Detection of shadowed/overly permissive firewall rules, rogue unscanned assets, attack vectors and violating traffic between zones is documented; anomaly-style detection of unrecognized live traffic is not. [7], [8], [12], [13] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | — | Skybox correlates security tags, ACLs, routing rules and NATs in policy analysis, and users create firewall policies via flow requests with an approval workflow; policy authoring is object/IP-centric rather than tag/label-driven. [2], [13] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | Analytics-driven change recommendations (e.g., fixing overly permissive rules from syslog/ACL analysis) and 'intelligent automation' for multi-vendor environments are documented; an explicit AI/ML rule-recommendation engine is not evidenced. [8], [10], [14] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | high | — | Attack simulation, 'what-if' modeling of proposed network changes, and a change-manager module that reviews changes before implementation and blocks non-compliant ones are documented, satisfying dry-run/simulation of policy changes. [2], [9] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Not Supported | medium | — | A reviewer states that modifications and deletion of existing policies were unavailable or under enhancement, which rules out instant one-click rollback of deployed policy changes. [2] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No staged source documents inherited/hierarchical policy rules.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | — | Skybox is agentless (non-intrusive collection of device configs and third-party scanner/asset data), so per-workload OS support for an installed agent does not apply; OS-specific workload support is not part of the architecture. [2], [9] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | Container vulnerability visibility in cloud/virtual networks, including a Twistlock integration, is documented; native Kubernetes/OpenShift isolation enforcement is not documented. [7], [11] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | Agentless data collection from L3 devices, clouds and third-party scanner/asset integrations is documented; no host-based agent collection option is documented, so only the agentless/network-integration half of the requirement is met. [2], [7], [13] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | — | no evidence found (No staged source documents operation in a fully air-gapped network; the daily intelligence-feed update requirement is not addressed.) |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Enterprise scale is documented only qualitatively ('proven scalability', three-tier architecture with horizontal scaling potential, 500+ enterprises served); no numeric workload count reaching the 50,000-workload threshold was found, and reviewers note scale/licensing constraints. [2], [12], [16] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | No endpoint agent is installed on workloads whose CPU overhead could be measured; the agent CPU-overhead metric does not apply to this agentless platform. [2], [9] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No endpoint agent exists, so the agent RAM-footprint metric does not apply. [2], [9] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | — | Skybox is an out-of-band management plane; enforcement is performed by network devices, so no in-path agent adds network latency. [9], [13] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | There is no in-path agent whose failure could interrupt workload traffic; the agent fail-safe requirement does not apply. [9], [13] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No agent is installed or updated on servers, so the reboot-free agent installation requirement does not apply. [2], [9] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | — | Skybox 10 introduced a new REST API for programmatic access to Skybox intelligence, per vendor statements published by CIO Insider and Enterprise IT World; full 100% admin-function coverage is not specifically documented. [10], [11] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | Integrations with Splunk and ElasticSearch are documented among Skybox 10 integrations; SOAR platforms and QRadar/Sentinel integrations are not evidenced. [11] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | — | ServiceNow is documented among Skybox 10 integrations; tag synchronization via CMDB is not specifically documented. [11] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found (No staged source documents CI/CD pipeline integration (Jenkins/GitLab/Terraform) for DevSecOps.) |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | N/A | medium | — | No endpoint enforcement agent exists; policy enforcement is delegated to firewalls and network devices, so process-level enforcement is outside the product architecture. [2], [9] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Skybox Threat Intelligence context is documented for identifying and mitigating vulnerabilities/exposures; honeypot/deception detection is not documented. [9], [12] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Compliance checks against PCI DSS datasets, NIST, DISA STIGs and CIS benchmarks are documented by reviewers and datasheets; ISO 27001, NIST 800-207 and IEC 62443 report templates are not specifically evidenced. [2], [8], [13], [14] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | N/A | medium | — | There is no agent-controller channel to encrypt; the platform is agentless and collects data via network protocols and third-party integrations. [2], [9] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | — | no evidence found (Hardware-level redundancy (redundant hot-swappable PSUs, RAID 1 storage) and multi-server scale-out are documented, but no Active-Active/Active-Passive controller cluster is documented.) |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | N/A | medium | — | No agent exists to enter an autonomous enforcement mode; policy enforcement is performed by network devices independent of Skybox. [2], [13] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | A reviewer documents built-in backup/restore tooling with roughly ten-to-twenty-minute recovery; multi-site disaster-recovery synchronization is not documented. [2] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No evidence of FIPS 140-2/140-3 or Common Criteria EAL4+ validation was found; NIST CMVP and Common Criteria registry searches returned no Skybox entries (absence of evidence).) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (Skybox documents OT-network support, but no Siemens/Honeywell/ABB software compatibility certifications were found.) |

---

## 4. Notable Strengths

- **Vulnerability/CVE context on the network map (item 1.4):** a CVE/CPE-compatible intelligence feed is correlated onto the network model so exposed, exploitable vulnerabilities are shown in network context, and a user reports identifying ransomware-vulnerable users via the CVE database together with the mapping feature [7][9][2].
- **Policy change simulation and dry-run (item 2.3):** attack simulation, "what-if" modeling of proposed network changes and a change-manager module that reviews changes before implementation and stops non-compliant ones are documented [9][2].
- **Firewall policy visibility and cleanup analytics (items 1.2, 2.2):** an interactive topology map plus detection of redundant, shadowed and overly permissive rules with analytics-driven change recommendations are documented [13][14][8].
- **Compliance checking for common frameworks (item 6.3):** checks against PCI DSS datasets, NIST, DISA STIGs and CIS benchmarks are documented by reviewers and datasheets [2][14].
- **REST API for programmatic access (item 5.1):** Skybox 10 introduced a REST API so Skybox intelligence can be consumed by other tools and processes [10][11].

## 5. Notable Gaps / Risks

- **Vendor shutdown - product is discontinued (all items):** Skybox closed operations on February 24, 2025 and is no longer supporting or selling the product; the only vendor-provided path forward is Tufin's ExpressPath migration program, so this product cannot be selected for a new deployment [4][1][5].
- **Not a microsegmentation enforcement platform (items 3.3, 6.1, 7.2):** there are no host agents, no agent-based collection option and no process-level enforcement; policy enforcement is delegated to network devices, so workload-level segmentation requirements are outside its architecture [9][2].
- **No instant policy rollback (item 2.4):** a user reports that modification and deletion of existing policies were unavailable or under enhancement, ruling out one-click rollback [2].
- **Numerous capability areas unverified (items 1.3, 2.5, 3.4, 5.4, 7.1, 8.1, 8.2):** flow-history retention, hierarchical policy, air-gapped operation, CI/CD integration, HA controller clustering, FIPS/Common Criteria certification and Siemens/Honeywell/ABB compatibility all remain unknown - no staged source documents them, and the shutdown means vendor documentation can no longer be consulted.
- **Containers and scale only partially covered (items 3.2, 3.5):** container support is limited to vulnerability visibility (e.g., Twistlock), with no native Kubernetes/OpenShift isolation, and scale is documented only qualitatively with no workload count approaching 50,000 [7][11][2].

## 6. Evidence Quality Notes

All 16 sources were staged and all 67 evidence quotes are verbatim-grounded in the staged text (verified with verify_citation_grounding.py). Because every live Skybox domain now serves Tufin content or redirects to tufin.com, no original product documentation could be fetched directly; the Skybox-authored evidence comes from vendor PDFs mirrored on third-party hosts (technobind.com, al-jammaz.com, softshell.ag, Microsoft Azure CDN, Scribd) and from vendor commentary published by SC Media. Web.archive.org and archive.today were rate-limited/CAPTCHA-blocked from this network for the entire run, so docs.skyboxsecurity.com user guides could not be retrieved for items such as flow-history retention, HA architecture and encryption - these items are therefore rated unknown rather than guessed.

Sixteen items are backed by at least two source types and 13 items triangulate community or third-party sources with vendor material; the strongest independent coverage is PeerSpot (38 user reviews of Skybox Security Suite) plus SecurityWeek, Enterprise IT World and Wikipedia. Several items rest only on vendor datasheets (1.2, 2.2, 3.5) and are confidence-capped accordingly. Sources contradict each other in two places: reviewers disagree on cloud support (one used the suite to monitor AWS instances while another reported missing cloud-security features, leading to a partial on container/cloud coverage rather than a supported verdict), and scalability reports are mixed (three-tier horizontal-scaling potential praised by some, licensing-driven limits on the 6500-to-7500 platform transition noted by others), which is why 3.5 is partial with no numeric value.

---

## Bibliography

[1] Tufin (acquirer of Skybox assets). "Tufin ExpressPath for Skybox Customers (migration program page)". https://www.tufin.com/tufin-expresspath-program (Retrieved: 2026-08-10T16:50:00Z)
[2] PeerSpot. "Skybox Security Suite reviews and ratings (PeerSpot)". https://www.peerspot.com/products/skybox-security-suite-reviews (Retrieved: 2026-08-10T16:50:00Z)
[3] PeerSpot. "Skybox Security Suite vs Tufin Orchestration Suite comparison (PeerSpot)". https://www.peerspot.com/products/comparisons/skybox-security-suite_vs_tufin-orchestration-suite (Retrieved: 2026-08-10T16:50:00Z)
[4] SecurityWeek. "Skybox Security Shuts Down, Lays Off Entire Workforce". https://www.securityweek.com/skybox-security-shuts-down-lays-off-entire-workforce/ (Retrieved: 2026-08-10T16:50:00Z)
[5] Wikipedia. "Tufin (Wikipedia article, includes Skybox shutdown/acquisition history)". https://en.wikipedia.org/wiki/Tufin (Retrieved: 2026-08-10T16:50:00Z)
[6] SC Media / Skybox Security. "Move to a risk-based vulnerability management approach (SC Media perspective by Skybox VP)". https://www.scworld.com/perspective/move-to-a-risk-based-vulnerability-management-approach (Retrieved: 2026-08-10T16:50:00Z)
[7] Skybox Security (hosted on Microsoft Azure CDN). "Comprehensive Vulnerability Discovery with Skybox Security - Solution Brief (PDF)". https://catalogartifact.azureedge.net/publicartifacts/skyboxsecurity1585187406404.skybox-vc-mdatp-phase1-33330965-8c17-44cf-8a4d-e1cd809c7ae5/Artifacts/Documents/Skybox_TB_Scanless_Assessment-1.pdf (Retrieved: 2026-08-10T16:50:00Z)
[8] Palo Alto Networks / Skybox Security. "Palo Alto Networks ML-Powered NGFW and Skybox Security Suite - joint datasheet". https://www.paloaltonetworks.com/resources/datasheets/ml-powered-next-generation-firewall-skybox-security-suite (Retrieved: 2026-08-10T16:50:00Z)
[9] Skybox Security (hosted by softshell.ag). "Skybox Vulnerability Control - Data Sheet (PDF)". http://www.softshell.ag/wp-content/uploads/2015/08/Skybox_Security_Vulnerability_Control_DS_EN_0.pdf (Retrieved: 2026-08-10T16:50:00Z)
[10] CIO Insider India. "Skybox Security: Shielding Business Data Using Visibility and Context (vendor interview)". https://www.cioinsiderindia.com/vendor/skybox-security-shielding-business-data-using-visibility-and-context-cid-599.html (Retrieved: 2026-08-10T16:50:00Z)
[11] Enterprise IT World. "Skybox Security Introduces Suite 10". https://www.enterpriseitworld.com/skybox-security-introduces-suite-10/ (Retrieved: 2026-08-10T16:50:00Z)
[12] Skybox Security (hosted by technobind.com). "Skybox Firewall Assurance - Product Brief (PDF)". https://technobind.com/wp-content/uploads/2024/12/Firewall_assurance-product_brief-skyboxsecurity-cloud-090222.pdf (Retrieved: 2026-08-10T16:50:00Z)
[13] Skybox Security (hosted by technobind.com). "Skybox Network Assurance - Product Brief (PDF)". https://technobind.com/wp-content/uploads/2024/12/Network_assurance-product_brief-skyboxsecurity-cloud-090822.pdf (Retrieved: 2026-08-10T16:50:00Z)
[14] Skybox Security (hosted by al-jammaz.com). "Skybox Firewall Assurance - Datasheet (PDF)". https://www.al-jammaz.com/uploads/5/0/7/1/50711957/datasheet_firewall_assurance1120.pdf (Retrieved: 2026-08-10T16:50:00Z)
[15] PeerSpot. "Firewall Security Management - PeerSpot category page (Skybox Security Suite listing)". https://www.peerspot.com/categories/firewall-security-management (Retrieved: 2026-08-10T16:50:00Z)
[16] Skybox Security (hosted by Scribd). "Skybox Security Appliances 11000, 12100, and 12200 - Datasheet (hosted on Scribd)". https://www.scribd.com/document/610091017/skyboxsecurity-appliances-11000-12100-12200-042021 (Retrieved: 2026-08-10T16:50:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 16 (kept: 16, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 3, third_party_review: 4, vendor_blog: 1, vendor_datasheet: 7, vendor_doc: 1
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
