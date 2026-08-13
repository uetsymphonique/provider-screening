# Microsegmentation Product Assessment: Zentera Systems - Zentera CoShield

**Product ID:** `zentera-coshield`
**Version reference:** CoIP Access Platform v8.1 (per Zentera CISA Zero Trust Maturity Model mapping, 2022); current site brands microsegmentation as Virtual Chambers
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:06:19Z
**Total evidence items collected:** 78
**Total distinct sources:** 30

---

## 1. Overview

Zentera CoShield is the microsegmentation product line of Zentera Systems (Milpitas, CA), currently marketed as CoIP Access Platform with "Zero Trust Segmentation with Virtual Chambers" [1][2][3]. It is a software-defined overlay that sits on top of existing Layer 3 networks, adding identity-based segmentation without VLAN, firewall-rule, or IP changes [4][9]. Core components are the zCenter controller, the zLink host agent, the inline Zero Trust Gatekeeper appliance, and the CoIP Gateway Proxy [1][5]. Enforcement comes in agent-based and agentless forms: zLink Virtual Chambers on servers, containers, and cloud instances, and agentless chambers via Gatekeeper appliances for OT/IoT [2][19]. Traffic is carried over TLS 1.3 point-to-point tunnels with mutual authentication, decoupled from the physical network [9]. The platform spans AWS, Azure, GCP, on-premises data centers, ICS/OT, and edge locations, and can be deployed self-hosted (including air-gapped) or as the hosted Zentera Air service [1][13][12]. Zentera positions the product for lateral-movement defense, ransomware containment, IP protection, and hybrid/OT environments [2][10]. Public documentation is strongest on policy, automation, and cryptography; numeric performance figures and formal security certifications are not published.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 17    | 3                | 14     | 0   |
| partial          | 11    | 0                | 11     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 17 items backed by ≥ 2 source_types; 12 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | Vendor documentation states the platform monitors network activity to expose implicit trust relationships and automatically learns normal application behavior for detection, providing end-to-end visibility of user, endpoint and application behavior; the Siemens case study reports alerts on activity that does not match prescribed behavior. [3], [5], [11], [13] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Risk-scored visualization of application traffic, policy dashboards pairing violations with endpoint trust factors, and flow/throughput monitoring are documented; an explicit connectivity map grouped by App/Environment/Role/Process is not documented. [5], [10], [21] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | - | no evidence found (No public documentation of connection/flow history retention period found.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (No documentation of CVE/vulnerability context displayed on a map found.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | The Siemens case study reports the platform blocks and alerts on network activity that does not match prescribed behavior, and vendor materials state controls detect and flag anomalous behavior such as port scans and suspicious DNS queries. [2], [11], [24] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | - | Vendor documentation describes identity-based whitelist policies that replace IP/VLAN-based trust, integrating with SAML 2.0, OpenID Connect, OAuth 2.0 and LDAP; an independent comparison site lists identity-based access control with MFA as a core feature. [1], [4], [13], [27] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | Vendor materials describe AI-assist and a machine-learning-assisted policy engine that generate policies from observed traffic and learned application behavior and keep policies up to date automatically. [3], [9], [15], [24] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | Vendor pages document building and testing policies in the running environment before security protections are turned on, and a policy lifecycle that drafts and validates policies against observed traffic before publishing. [1], [5] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Supported | medium | - | Vendor pages state rollback is seamless and instant - disabling a policy or the overlay reverts traffic to previous behavior with no cleanup. [1] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | - | Reusable policy templates (Application Profiles) are documented; inherited or hierarchical rule structures are not described. [3], [5] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The zLink agent is documented for Windows (Server 2003-2019, XP-11) and Red Hat/CentOS/Ubuntu plus SLES and Amazon Linux; AIX and Solaris are not listed, with the Gatekeeper appliance positioned for unsupported OSes. [1], [12] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | - | Zentera announced full support for hybrid Kubernetes deployments with application-level container traffic segmentation (CoIP Enclave 4.3.1), and the current zLink agent is positioned for containerized workloads including a Kubernetes AI application example. [1], [19], [20] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | - | Both deployment models are documented: agent-based Virtual Chambers on application servers and agentless Virtual Chambers via Zero Trust Gatekeeper appliances (up to 32 protected assets per appliance without software installation); independent catalogs list agent-based and agentless models. [2], [19], [27], [28] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | The CISA-mapping document states the platform is available for on-premises and air-gapped deployments without a 3rd-party SaaS, and Carahsoft describes self-hosted deployment eliminating 3rd-party SaaS dependencies. [13], [25] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Only qualitative scale statements are published: ZNS virtual switches scale out/up with redundancy, an SDP can contain 'many thousands of servers', and a customer case study onboarded 700+ users; no workload-per-controller capacity figure is documented. [5], [14], [15] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | - | no evidence found (No public documentation of agent CPU overhead found.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | The only quantitative agent figure published is the ~50MB install size; no RAM footprint figure is documented. [1] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | The vendor claims custom packet encapsulations and network implementations ensure high throughput and low latency, but no numeric per-policy latency figure is published. [9] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | - | Vendor pages document configurable fail-open or fail-closed enforcement-point behavior and state control-plane outages do not break established connections; the Gatekeeper appliance supports optional hardware bypass failing open. [1], [19] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Supported | medium | - | Vendor pages state no reboot is required when installing agents and that the platform deploys to a running application server without requiring a restart. [1], [5] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | - | Rich APIs, SDKs and infrastructure-as-code deployment are documented, with configuration fully automatable via APIs and 'secure access as code'; explicit REST coverage of 100% of admin functions is not enumerated. [5], [9], [11], [13] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | The platform exports telemetry to SIEM platforms including Splunk and ELK and RFC 5424 syslog; a Splunk technology partnership is announced and a customer case study reports Splunk integration. [5], [11], [13], [22] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found (No documentation of CMDB (ServiceNow) tag-sync integration found.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | APIs for CI/CD and IaC automation are documented, with infrastructure-as-code deployment and 'secure access as code' policy implementation. [1], [5], [9] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | medium | - | The CISA-mapping document describes full visibility of process context (user, command line, process tree) and policies associated with specific application processes; enforcement includes application identity and process context at the application layer. [1], [13] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Inline threat detection/prevention and blocking of anomalous traffic are documented; no honeypot or deception capability is described. [2], [19], [24] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Compliance alignment is documented: PCI scope reduction, IEC 62443 alignment, and a self-contained NIST SP 800-207 implementation, plus published compliance guides (CISA ZTMM, NERC CIP, CMMC, NCSC, RIIO-2); ready-made named report templates such as ISO 27001 are not evidenced. [1], [2], [7], [25] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | high | - | All CoIP overlay traffic is documented as encrypted with TLS 1.3 and mutual authentication using certificate-based mTLS tunnels; an independent comparison site lists end-to-end encryption using TLS 1.3 and mTLS. [1], [9], [27] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | - | The zCenter controller is documented with robust high-availability (HA) and disaster recovery, and ZNS virtual switches support redundancy and scale out/up; active-active vs active-passive cluster topology is not specified. [5] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | Vendor pages document configurable fail-open/fail-closed behavior when enforcement points lose connectivity and state that control-plane outages do not break established connections. [1] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Disaster recovery is claimed for the zCenter controller; site-sync or replication mechanics are not documented. [5] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | - | no evidence found (No documentation or registry evidence of FIPS 140-2/140-3 or Common Criteria EAL4+ certification found.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | The Siemens case study documents CoIP platform deployment (zLink sensors and Virtual Chambers) in an industrial PLM environment, and the IT/OT brief covers brownfield OT protection; no formal compatibility certifications from Siemens, Honeywell or ABB are documented. [10], [11] |

---

## 4. Notable Strengths

- **Identity-based overlay segmentation without network changes (items 2.1, 3.4):** policies are identity-based whitelists that replace IP/VLAN trust, deployed as an overlay that works over any infrastructure, including air-gapped environments [1][4][13].
- **Dual agent/agentless enforcement (item 3.3):** zLink agent for VMs/containers/cloud instances plus Zero Trust Gatekeeper inline appliances protecting up to 32 assets each without software installation [2][19][27].
- **Automated policy lifecycle (items 2.2, 2.3, 2.4):** AI/ML-assisted policy generation from observed traffic, policy build/test before enforcement is enabled, and instant rollback [15][24][1].
- **TLS 1.3 + mTLS transport with process-level policy (items 6.4, 6.1):** end-to-end encrypted tunnels with mutual authentication, and policies bound to application processes with full process-tree visibility [9][13].
- **SIEM and automation integration (items 5.1, 5.2, 5.4):** Splunk/ELK export, RFC 5424 syslog to SIEM, and rich APIs enabling infrastructure-as-code and CI/CD automation [5][22][11].

## 5. Notable Gaps / Risks

- **Flow-history retention (item 1.3):** no retention period for connection/flow history is published, so the >=90-day forensic-retention requirement is unverifiable; the vendor should disclose log/flow retention defaults.
- **Agent performance figures (items 4.1, 4.2):** no CPU-overhead or RAM-footprint numbers are published (only a ~50MB install size), making capacity planning dependent on vendor benchmarks or a pilot measurement [1].
- **Scale capacity (item 3.5):** only qualitative scale statements exist (ZNS scale-out, SDPs of "many thousands of servers"); no workload-per-controller figure approaching 50,000 is documented [5][15].
- **Formal certifications (item 8.1):** no FIPS 140-2/140-3 or Common Criteria EAL4+ evidence was found, which matters for government and compliance-driven buyers.
- **Controller HA topology and DR mechanics (items 7.1, 7.3):** high availability and disaster recovery are claimed for the zCenter controller, but active-active/active-passive mode and site-sync/replication details are undocumented [5].

## 6. Evidence Quality Notes

The assessment draws on 30 distinct sources and 78 grounded evidence quotes across the 33 items. Seventeen items are backed by >=2 source_types; the three high-confidence items (2.1, 3.3, 6.4) each include at least one non-vendor source (CybersecTools comparison [27], CISOPick catalog [28], Carahsoft reseller page [25]). The majority of items rest primarily on vendor documentation (product pages, datasheets, whitepapers, and press releases) because public third-party analysis of Zentera CoShield is scarce: no independent lab benchmark, and no retrievable analyst-report text (Gartner/Forrester/IDC content is paywalled). Where available, independent reseller and comparison sites (Carahsoft, Oregon Systems, CybersecTools, CISOPick) corroborate core features, though those pages are substantially vendor-derived, so confidence is capped at medium except where the third-party content independently restates capabilities.

Two practical constraints shaped the evidence set. First, the legacy zentera.com domain now redirects to an unrelated site, so the assessment anchors on the live zentera.net product pages (which rebrand the product as "Virtual Chambers") plus archived vendor PDFs from 2020-2022 and press releases from 2017-2022 that use the CoIP Access Platform name. Second, the NIST CMVP and Common Criteria registry searches were not reliably queryable from the run environment, so item 8.1 is recorded as unknown rather than not_supported. No contradictions between sources were found; where quantitative claims were absent (retention, CPU, RAM, latency, scale counts, certifications), verdicts were set to unknown or partial rather than inferred, and the five unknown items (1.3, 1.4, 4.1, 5.3, 8.1) carry no fabricated evidence.

---

## Bibliography

[1] Zentera Systems. "Product Overview - Zentera Systems". https://www.zentera.net/products/overview (Retrieved: 2026-08-10T16:53:57Z)
[2] Zentera Systems. "Segmentation with Virtual Chambers". https://www.zentera.net/solutions/microsegmentation (Retrieved: 2026-08-10T16:53:58Z)
[3] Zentera Systems. "Virtual Chambers". https://www.zentera.net/technology/virtual-chamber (Retrieved: 2026-08-10T16:54:01Z)
[4] Zentera Systems. "Zero Trust Overlay Technology". https://www.zentera.net/technology/zero-trust-overlay (Retrieved: 2026-08-10T16:54:01Z)
[5] Zentera Systems. "CoIP Platform Details". https://www.zentera.net/products/coip-platform (Retrieved: 2026-08-10T16:54:02Z)
[6] Zentera Systems. "Who We Are & Who We Serve | Zentera Systems". https://www.zentera.net/company (Retrieved: 2026-08-10T16:54:04Z)
[7] Zentera Systems. "Zentera Resources". https://www.zentera.net/resources (Retrieved: 2026-08-10T16:54:05Z)
[8] Zentera Systems. "Zentera News". https://www.zentera.net/news (Retrieved: 2026-08-10T16:54:05Z)
[9] Zentera Systems. "CoIP Access Platform Zero Trust Network Access Technology Backgrounder (Q3 2020)". https://www.zentera.net/hubfs/Collateral/Zentera%20Systems%20Zero%20Trust%20Technology%20Backgrounder%20Q3%202020.pdf (Retrieved: 2026-08-10T16:55:06Z)
[10] Zentera Systems. "Zero Trust Boundary Security for IT/OT Convergence (Q1 2020)". https://www.zentera.net/hubfs/Collateral/Zentera%20Solution%20Brief%20-%20IT-OT%20Q1%202020.pdf (Retrieved: 2026-08-10T16:55:09Z)
[11] Zentera Systems. "Zentera Empowers Siemens for Secure Access and Collaboration". https://www.zentera.net/hubfs/Collateral/siemens_cs.pdf (Retrieved: 2026-08-10T16:55:10Z)
[12] Zentera Systems. "Zentera Air Datasheet". https://www.zentera.net/hubfs/Collateral/Zentera%20Air%20Datasheet.pdf (Retrieved: 2026-08-10T16:55:16Z)
[13] Zentera Systems. "CoIP Platform Zero Trust Mapping to the CISA Zero Trust Maturity Model (v8.1)". https://www.zentera.net/hubfs/Collateral/Zentera%20CISA%20Zero%20Trust%20Maturity%20Model.pdf (Retrieved: 2026-08-10T16:55:17Z)
[14] Zentera Systems. "Zentera Readies Ambarella for 100% Work From Home (Q3 2020)". https://www.zentera.net/hubfs/Collateral/Zentera%20Ambarella%20Success%20Story%20Q3%202020.pdf (Retrieved: 2026-08-10T16:55:20Z)
[15] Zentera Systems. "Zero Trust Patterns". https://www.zentera.net/solutions/zero-trust-patterns (Retrieved: 2026-08-10T16:56:10Z)
[16] Zentera Systems. "ZTNA - Zero Trust Network Access". https://www.zentera.net/technology/ztna (Retrieved: 2026-08-10T16:56:11Z)
[17] Zentera Systems. "Hybrid cloud security - Cloud Migration Use Case". https://www.zentera.net/use-cases/cloud-migration (Retrieved: 2026-08-10T16:56:15Z)
[18] Zentera Systems. "IT-OT Convergence Use Case". https://www.zentera.net/use-cases/it-ot-convergence (Retrieved: 2026-08-10T16:56:15Z)
[19] Zentera Systems via PR Newswire. "Zentera Systems Enhances Zero Trust Security Segmentation Solutions with New Micro-Segmentation Gatekeeper Appliances (press release, 2020-10-29)". https://www.prnewswire.com/news-releases/zentera-systems-enhances-zero-trust-security-segmentation-solutions-with-new-micro-segmentation-gatekeeper-appliances-301162695.html (Retrieved: 2026-08-10T16:57:32Z)
[20] Zentera Systems via PR Newswire. "Zentera Systems Announces Native Support for Hybrid Kubernetes Environments (press release, 2018-10-18)". https://www.prnewswire.com/news-releases/zentera-systems-announces-native-support-for-hybrid-kubernetes-environments-300733337.html (Retrieved: 2026-08-10T16:57:47Z)
[21] Zentera Systems via PR Newswire. "Zentera Systems Enhances CoIP Access Platform with Zero Trust Analytics (press release, 2021-01-26)". https://www.prnewswire.com/news-releases/zentera-systems-enhances-coip-access-platform-with-zero-trust-analytics-301214806.html (Retrieved: 2026-08-10T16:57:48Z)
[22] Zentera Systems via PR Newswire. "Zentera Systems Announces Technology Partnership with Splunk (press release, 2017-11-09)". https://www.prnewswire.com/news-releases/zentera-systems-announces-technology-partnership-with-splunk-to-advance-security-intelligence-tools-300552626.html (Retrieved: 2026-08-10T16:57:50Z)
[23] Zentera Systems via PR Newswire. "Cadence Design Systems Deploys Zentera for Critical IP Access (press release, 2022-01-18)". https://www.prnewswire.com/news-releases/cadence-design-systems-deploys-zentera-for-critical-ip-access-301462971.html (Retrieved: 2026-08-10T16:57:54Z)
[24] Zentera Systems via PR Newswire. "Zentera Upgrades SaaS with Application Cybershield for Ransomware Defense (press release, 2022-02-08)". https://www.prnewswire.com/news-releases/zentera-upgrades-saas-with-application-cybershield-for-ransomware-defense-301477578.html (Retrieved: 2026-08-10T16:57:57Z)
[25] Carahsoft Technology Corp.. "Zentera Systems - Zero Trust Network Segmentation Platform | Carahsoft". https://www.carahsoft.com/zentera (Retrieved: 2026-08-10T16:58:22Z)
[26] Oregon Systems. "Zentera - Oregon Systems". https://www.oregon-systems.com/vendors/zentera/ (Retrieved: 2026-08-10T16:58:27Z)
[27] CybersecTools. "Zentera Zero Trust Security vs Zero Networks Microsegmentation (comparison, 2026)". https://cybersectools.com/compare/zentera-zero-trust-security-vs-zero-networks-microsegmentation-58i93 (Retrieved: 2026-08-10T17:00:06Z)
[28] CISOPick. "Microsegmentation with Virtual Chambers by Zentera Systems | CISOPick". https://cisopick.com/product/zentera-systems-inc-microsegmentation-with-virtual-chambers (Retrieved: 2026-08-10T17:00:09Z)
[29] Cybersecurity Insiders. "The Security Step Too Many Companies Ignore: Tips for Micro-Segmenting Your Network (byline by J. Lee)". https://www.cybersecurity-insiders.com/the-security-step-too-many-companies-ignore-tips-for-micro-segmenting-your-network/ (Retrieved: 2026-08-10T17:02:30Z)
[30] Zentera Systems. "The Security Step Too Many Companies Ignore: Tips for Micro-Segmenting Your Network (Zentera summary)". https://www.zentera.net/news/the-security-step-too-many-companies-ignore-tips-for-micro-segmenting-your-network (Retrieved: 2026-08-10T17:02:12Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 30 (kept: 30, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 3, product_release_notes: 5, third_party_review: 4, vendor_blog: 2, vendor_datasheet: 1, vendor_doc: 15
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
