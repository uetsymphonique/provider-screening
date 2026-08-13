# Microsegmentation Product Assessment: AlgoSec - AlgoSec Horizon (Horizon Security Analyzer / FireFlow / AppViz / ACE)

**Product ID:** `algosec-horizon`
**Version reference:** ACE (AlgoSec Cloud Enterprise) docs & release notes updated 4 Aug 2026; ASMS A33.00-A33.20 docs; Horizon platform launched Feb 2025
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T11:24:19Z
**Total evidence items collected:** 80
**Total distinct sources:** 31

---

## 1. Overview

AlgoSec Horizon is an application-centric security management platform announced in February 2025, converging AlgoSec's security-policy products (Horizon Security Analyzer/ASMS, FireFlow, AppViz, ObjectFlow) with the cloud-native module AlgoSec Cloud Enterprise (ACE) [2]. AlgoSec positions the platform's microsegmentation as orchestration of existing enforcement layers rather than a host agent: ACE manages network security rules deployed in cloud-native controls (AWS Security Groups and Network Firewall, Azure NSG and Firewall, GCP project firewall) [5], while ASMS orchestrates on-premises firewall and SDN policies [24]. Deployment shapes are SaaS (ACE, hosted in AWS regions) plus an on-premises appliance (ASMS) that can connect to the SaaS over an HTTPS tunnel [6, 12]. Discovery and visibility are agentless: applications, microservices and dependencies are auto-discovered from cloud configuration and flow logs, and policies are simulated, approved and pushed to the controls [11, 21]. The assessment found strong policy-management, integration and high-availability capabilities, but flow-history retention of only 7 days [16] and no documented scale or FIPS/Common Criteria evidence (items 3.5, 8.1).

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 10    | 1                | 9      | 0   |
| partial          | 12    | 0                | 12     | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 6     | 0                | 6      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 24 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** Horizon is fully agentless (Cloud App Analyzer deploys no agents to workloads) and manages network security rules in cloud-native controls and devices, so workload host-OS coverage does not apply.
- **4.1:** No host agent is installed on workloads (fully agentless), so agent CPU consumption does not apply.
- **4.2:** No host agent is deployed on workloads (fully agentless), so agent RAM footprint does not apply.
- **4.3:** ACE collects data out-of-band via cloud APIs (AWS assume-role) and manages rules that are already deployed in the cloud-native controls, adding no inline data-path element whose latency would apply.
- **4.4:** There is no host agent whose crash could interrupt workload traffic; enforcement rules are deployed in the cloud-native controls themselves.
- **4.5:** No agent software is installed on hosts, so install/update reboot requirements do not apply.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | ACE automatically discovers cloud resources, applications and traffic and maps more than 150 cloud-specific risks; AppViz AI discovers applications and their dependencies, and the AWS Marketplace description and an independent tool comparison corroborate automatic application/flow discovery. [3], [4], [11], [27], [28] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Application dependency graphs visualize applications, microservices and their connections, and the platform provides a unified view of application traffic flows across hybrid/multi-cloud environments, but organization by environment, role and process dimensions is not documented. [3], [11], [30] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Not Supported | medium | 7.0 days | ACE's flow-log-based traffic visibility uses a sliding 7-day window, with activity older than seven days rolling out of view, which is below the 90-day requirement; only customer activity audit logs are retained for 90 days. [6], [10], [16] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | - | Application Discovery graphs highlight security issues and where vulnerabilities occur within an application, container scanning detects CVEs and malware, and ACE maps vulnerabilities in security groups, cloud firewalls and container configurations. [11], [13], [30] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Flow Log Analysis surfaces unexpected external traffic, unintended exposure and anomalies in real network behavior, and Cloud App Analyzer detects exposed applications, unauthorized connections and risky connectivity paths. [4], [16] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | - | The policy model is application-centric: applications/microservices can be identified by resource tags, allow-lists are built for app components and identity groups, but the underlying enforcement rules are managed in cloud security groups and firewalls, which are network-based controls. [3], [5], [11], [24] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | AppViz AI Application Discovery uses AI to identify and suggest applications and their flows for onboarding from FireFlow tickets and device policy tables, ACE surfaces risk remediation suggestions for risky rules, and FireFlow automatically analyzes proposed changes before implementation. [5], [22], [26] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | ASMS Traffic Simulation Query tests traffic against current or past device policies and simulates policy on each device in the path; proposed security policy changes can be previewed and simulated, and ACE can run traffic simulation queries against ASMS. [12], [21], [25] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | FireFlow ActiveChange documents a Rollback procedure for implemented changes and failed Juniper implementations are automatically rolled back, but a universal one-click rollback across all managed controls is not documented. [23] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | ACE manages Google Cloud hierarchical (inherited) firewall rules, tracks rule usage for inherited and VPC firewall rules, and displays a flattened hierarchical view distinguishing inherited rules above VPC firewall rules. [8] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | - | Horizon is fully agentless (Cloud App Analyzer deploys no agents to workloads) and manages network security rules in cloud-native controls and devices, so workload host-OS coverage does not apply. [4], [5] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | - | ACE discovers, visualizes and continuously scans EKS, AKS and GKE clusters (pods, containers, CIS benchmarks) and orchestrates Kubernetes policies as an enforcement layer, but OpenShift support and native in-cluster isolation enforcement are not documented. [7], [11], [24] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | The platform is agentless: Cloud App Analyzer is fully agentless and policies are implemented through cloud security groups, firewalls, SDN fabrics and host controls as existing enforcement layers; no vendor-supplied host agent product is documented. [4], [24] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | ASMS runs as an on-premises hardened appliance and SaaS connectivity (ACE/AppViz via HTTPS tunnel) is optional, but the SaaS modules require internet and no explicit fully air-gapped deployment documentation exists. [6], [12], [18] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Unknown | low | - | no evidence found |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | - | No host agent is installed on workloads (fully agentless), so agent CPU consumption does not apply. [4], [5] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | - | No host agent is deployed on workloads (fully agentless), so agent RAM footprint does not apply. [4] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | - | ACE collects data out-of-band via cloud APIs (AWS assume-role) and manages rules that are already deployed in the cloud-native controls, adding no inline data-path element whose latency would apply. [4], [6] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | - | There is no host agent whose crash could interrupt workload traffic; enforcement rules are deployed in the cloud-native controls themselves. [4] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | - | No agent software is installed on hosts, so install/update reboot requirements do not apply. [4] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | ASMS exposes REST web services for AFA, FireFlow and AppViz (plus SOAP) with Swagger documentation, and ACE provides public APIs for network policy and report management, but full 100% coverage of every administrative function is not explicitly documented. [8], [9], [20] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | ASMS architecture includes Syslog NG log processing and SaaS audit logs can be exported and integrated with customer SIEM platforms, with users reporting syslog-based firewall connectivity. [6], [27], [31] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | - | FireFlow/ASMS integrate with ServiceNow, BMC Remedy and HP ServiceCenter for change-management workflow (CMS linking and ITSM integration), but tag/label synchronization with a CMDB is not explicitly documented. [19], [26], [29] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | ACE provides IaC Connectivity Risk Analysis for Terraform (including a GitLab CI job), CI/CD container security scanning on GitHub pull requests, and ECR/ACR/GAR CD mitigation integrations. [14], [15] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | - | Enforcement is documented at the network policy layer (security rules deployed in cloud security groups and firewalls); no process-level enforcement capability is documented. [4], [5] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat Management detonates container images for dynamic behavior analysis (IPs, domains, countries, open ports), statically detects malware and CVEs, and maintains a daily-updated high-risk port list, but no honeypot/deception capability is documented. [13] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Compliance reporting covers PCI DSS, SOX, HIPAA and ISO/IEC 27001, ACE scans SOC 2, NIS 2 and CIS benchmarks, and AlgoSec holds ISO/IEC 27001:2022/27017 and SOC 2 Type II certifications; NIST 800-207 and IEC 62443 are not specifically documented. [1], [6], [8], [27] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | All data in transit is encrypted with TLS 1.2 or 1.3 and ASMS-to-SaaS communication uses certificate-based mutual authentication, but there is no agent-controller channel because the product is agentless and TLS 1.3 is not the exclusive baseline. [4], [6] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | ASMS supports active/standby HA clusters with automatic failover and a shared virtual IP, and the SaaS platform runs in AWS regions distributed across three Availability Zones. [6], [17] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | Enforcement rules are deployed in and executed by the cloud-native controls and managed devices themselves rather than a controller-dependent agent, so enforcement persists if the management platform is unreachable, but no explicit autonomous-mode documentation exists. [4], [5] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | - | ASMS supports DR clusters with nodes at different sites, and the SaaS platform performs nightly backups (14-day retention) with documented DR RTO of 24 hours and RPO of 72 hours. [6], [17] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | - | no evidence found |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found |

---

## 4. Notable Strengths

- **Application-centric policy orchestration across hybrid controls (items 2.1, 2.5, 3.3):** Policies are modeled around applications, resource tags and identity groups and enforced through cloud security groups, firewalls, SDN fabrics and Kubernetes [3, 5, 24].
- **Policy simulation before enforcement (items 2.3, 2.2):** Traffic Simulation Query tests traffic against current or past policies on every device in the path, and AppViz AI suggests applications and flows for onboarding [21, 22].
- **Agentless zero-footprint model (items 3.1, 4.1-4.5):** Cloud App Analyzer is fully agentless and enforcement lives in the cloud-native controls, so there is no agent resource consumption, reboot or fail-safe burden on workloads [4, 5].
- **Deep cloud risk and compliance coverage (items 1.4, 6.2, 6.3):** ACE maps 150+ cloud-specific risks, detonates containers for malware/CVE analysis, and scans compliance standards including PCI DSS, SOC 2, NIS 2 and CIS benchmarks [4, 8, 13].
- **Resilient management plane (items 7.1, 7.3):** ASMS HA clusters provide automatic failover with a shared virtual IP, DR clusters run at separate sites, and the SaaS performs nightly backups with documented RTO/RPO [6, 17].

## 5. Notable Gaps / Risks

- **Flow-history retention (item 1.3):** ACE's flow-log analysis keeps only a sliding 7-day window, below the 90-day forensic-tracing requirement [16].
- **No process-level enforcement (item 6.1):** enforcement is limited to network-layer rules deployed in cloud controls and firewalls [5].
- **No documented scale limit (item 3.5):** no source states a workload count at or above 50,000; the AWS Marketplace listing licenses ACE in 100-workload units without a documented maximum [27].
- **Air-gapped and TLS constraints (items 3.4, 6.4):** ACE is SaaS-only, so fully isolated networks are not documented, and transit encryption supports TLS 1.2 or 1.3 rather than TLS 1.3 exclusively [6, 12].
- **Certification gaps (items 8.1, 8.2):** no FIPS 140-2/140-3 or Common Criteria evidence, and no Siemens/Honeywell/ABB OT compatibility certifications, were found.

## 6. Evidence Quality Notes

Of the 33 items, 30 carry cited evidence and 3 are unknown; 12 items draw on 2+ source types, while 24 are backed only by vendor documentation. Item 1.1 is the only high-confidence verdict, triangulated across vendor docs, the solution brief, AWS Marketplace user reviews (community) and the independent AIMultiple comparison (third-party review) [3, 4, 11, 27, 28]. The remaining non-vendor sources are the AWS Marketplace listing (user reviews, tagged community) and the CyberSecTools directory (third-party listing), which corroborate FireFlow's change-management description [29] and real-world compliance checking [27]; Gartner Peer Insights and G2 pages were blocked and could not be staged, so analyst-review triangulation was not possible. No contradictions between sources were found: the documented 7-day flow-log window [16] is consistent with the absence of any longer retention claim, and the "fully agentless" positioning in the tech docs [4] is consistent across all performance-related items. The main limitation is that numeric performance, scale and certification items rest on absence of evidence and are therefore rated not_applicable or unknown rather than supported.

---

## Bibliography

[1] AlgoSec. "AlgoSec Horizon platform modules (product page)". https://www.algosec.com/products/algosec-horizon (Retrieved: 2026-08-10T11:24:19Z)
[2] AlgoSec. "AlgoSec Launches AlgoSec Horizon platform (press release)". https://www.algosec.com/press-release/algosec-launches-algosec-horizon-platform (Retrieved: 2026-08-10T11:24:19Z)
[3] AlgoSec (via ICOS). "AlgoSec Horizon: Secure application connectivity across your hybrid environment (solution brief)". https://www.icos.it/wp-content/uploads/2025/09/AlgoSec-Horizon-Platform-Solution-brief.pdf (Retrieved: 2026-08-10T11:24:19Z)
[4] AlgoSec Tech Docs. "ACE Documentation - Welcome to ACE". https://techdocs.algosec.com/en/ace/content/cloud-common/newace-intro.htm (Retrieved: 2026-08-10T11:24:19Z)
[5] AlgoSec Tech Docs. "ACE Documentation - Manage Network Policies". https://techdocs.algosec.com/en/ace/content/cloud-sec/manage-policies.htm (Retrieved: 2026-08-10T11:24:19Z)
[6] AlgoSec Tech Docs. "ACE Documentation - AlgoSec SaaS Services Security Practices". https://techdocs.algosec.com/en/ace/content/cloud-common/security.htm (Retrieved: 2026-08-10T11:24:19Z)
[7] AlgoSec Tech Docs. "ACE Documentation - Kubernetes Services Risks Management". https://techdocs.algosec.com/en/ace/content/cloud-apps/prev-kubernetes-risks.htm (Retrieved: 2026-08-10T11:24:19Z)
[8] AlgoSec Tech Docs. "ACE Release Notes (What's New)". https://techdocs.algosec.com/en/ace/content/cloud-common/ace-whats-new.htm (Retrieved: 2026-08-10T11:24:19Z)
[9] AlgoSec Tech Docs. "ACE Documentation - ACE API Reference". https://techdocs.algosec.com/en/ace/content/cloud-sec/cf-apis.htm (Retrieved: 2026-08-10T11:24:19Z)
[10] AlgoSec Tech Docs. "ACE Documentation - View Changes History". https://techdocs.algosec.com/en/ace/content/cloud-sec/changes.htm (Retrieved: 2026-08-10T11:24:19Z)
[11] AlgoSec Tech Docs. "ACE Documentation - Cloud App Analyzer Application Discovery". https://techdocs.algosec.com/en/ace/content/cloud-apps/prev-app-disc.htm (Retrieved: 2026-08-10T11:24:19Z)
[12] AlgoSec Tech Docs. "ACE Documentation - ASMS integration to SaaS services". https://techdocs.algosec.com/en/ace/content/cloud-common/asms-integration.htm (Retrieved: 2026-08-10T11:24:19Z)
[13] AlgoSec Tech Docs. "ACE Documentation - Threat Management". https://techdocs.algosec.com/en/ace/content/cloud-apps/prev-mitigationrules.htm (Retrieved: 2026-08-10T11:24:19Z)
[14] AlgoSec Tech Docs. "ACE Documentation - IaC Connectivity Risk Analysis". https://techdocs.algosec.com/en/ace/content/cloud-sec/iac.htm (Retrieved: 2026-08-10T11:24:19Z)
[15] AlgoSec Tech Docs. "ACE Documentation - Cloud App Analyzer CI/CD Container Security". https://techdocs.algosec.com/en/ace/content/cloud-apps/prev-integration-cicd.htm (Retrieved: 2026-08-10T11:24:19Z)
[16] AlgoSec Tech Docs. "ACE Documentation - Flow Logs Analysis (AWS)". https://techdocs.algosec.com/en/ace/content/cloud-apps/prev-app-disc-flowlogs.htm (Retrieved: 2026-08-10T11:24:19Z)
[17] AlgoSec Tech Docs. "ASMS A33.10 - Manage clusters (HA/DR)". https://techdocs.algosec.com/en/asms/a33.10/asms-help/content/install-guide/deploying-clusters.htm (Retrieved: 2026-08-10T11:24:19Z)
[18] AlgoSec Tech Docs. "ASMS A33.20 - External system integration (SIEM)". https://techdocs.algosec.com/en/asms/a33.20/asms-help/content/afa-admin/integrating-afa-with-external.htm (Retrieved: 2026-08-10T11:24:19Z)
[19] AlgoSec Tech Docs. "ASMS A33.00 - Workflow (CMS/ServiceNow integration)". https://techdocs.algosec.com/en/asms/a33.00/asms-help/content/afa-admin/workflow.htm (Retrieved: 2026-08-10T11:24:19Z)
[20] AlgoSec Tech Docs. "ASMS A33.10 - ASMS API reference". https://techdocs.algosec.com/en/asms/a33.10/asms-help/content/api-guide/api_introduction.htm (Retrieved: 2026-08-10T11:24:19Z)
[21] AlgoSec Tech Docs. "ASMS A33.20 - Run traffic simulation queries". https://techdocs.algosec.com/en/asms/a33.20/asms-help/content/afa-ug/running-traffic-simulation.htm (Retrieved: 2026-08-10T11:24:19Z)
[22] AlgoSec Tech Docs. "ASMS A33.20 - AI Application Discovery in AppViz". https://techdocs.algosec.com/en/asms/a33.20/asms-help/content/bf-ug/ai-app-disc.htm (Retrieved: 2026-08-10T11:24:19Z)
[23] AlgoSec Tech Docs. "ASMS A33.10 - Implement changes with ActiveChange". https://techdocs.algosec.com/en/asms/a33.10/asms-help/content/ff-ug/implementing-changes-with.htm (Retrieved: 2026-08-10T11:24:19Z)
[24] AlgoSec. "Zero trust vs micro segmentation (AlgoSec solution article)". https://www.algosec.com/solutions/zero-trust-vs-micro-segmentation (Retrieved: 2026-08-10T11:24:19Z)
[25] AlgoSec. "Network segmentation solution & software (AlgoSec solution article)". https://www.algosec.com/solutions/network-segmentation (Retrieved: 2026-08-10T11:24:19Z)
[26] AlgoSec. "Automated security policy management (Horizon FireFlow product page)". https://www.algosec.com/products/fireflow (Retrieved: 2026-08-10T11:24:19Z)
[27] AWS Marketplace. "AlgoSec Horizon on AWS Marketplace (listing + user reviews)". https://aws.amazon.com/marketplace/pp/prodview-6blnbzj52cfou (Retrieved: 2026-08-10T11:24:19Z)
[28] AIMultiple. "Microsegmentation Tools (AIMultiple comparison/reviews)". https://aimultiple.com/microsegmentation-tools (Retrieved: 2026-08-10T11:24:19Z)
[29] CyberSecTools. "AlgoSec FireFlow (CyberSecTools directory)". https://cybersectools.com/tools/algosec-fireflow (Retrieved: 2026-08-10T11:24:19Z)
[30] AlgoSec. "AlgoSec Cloud Enterprise (Horizon ACE product page)". https://www.algosec.com/products/algosec-cloud-enterprise (Retrieved: 2026-08-10T11:24:19Z)
[31] AlgoSec Tech Docs. "ASMS A33.10 - ASMS system architecture". https://techdocs.algosec.com/en/asms/a33.10/asms-help/content/install-guide/system-arch.htm (Retrieved: 2026-08-10T11:24:19Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 22
- **Sources reviewed:** 31 (kept: 31, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, product_release_notes: 1, third_party_review: 2, vendor_blog: 3, vendor_datasheet: 4, vendor_doc: 20
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
