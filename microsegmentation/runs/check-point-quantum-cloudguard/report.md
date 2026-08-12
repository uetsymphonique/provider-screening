# Microsegmentation Product Assessment: Check Point Software Technologies - Check Point Quantum / CloudGuard

**Product ID:** `check-point-quantum-cloudguard`
**Version reference:** Quantum R81.10/R82/R82.10 security gateways (R82 CC EAL4+ certified); CloudGuard Network Security solution overview datasheet (2024); CloudGuard Controller R82.10 Administration Guide; Smart-1 600-S/600-M/6000-L/6000-XL management platform (2023 datasheet)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T11:43:30Z
**Total evidence items collected:** 79
**Total distinct sources:** 32

---

## 1. Overview

Check Point Quantum / CloudGuard is the vendor's network-centric route to microsegmentation. CloudGuard Network Security (cloud-native security gateways across AWS, Azure, GCP, Oracle and private clouds) enforces segmentation in the network path, while the CloudGuard Controller on the Security Management Server polls cloud and data-center APIs so policies stay in sync with dynamic assets such as subnets, security groups, VMs and tags [1][2][3]. Workload-level visibility and east-west traffic maps are delivered through an Illumio partnership (Illumio Insights/Segmentation), and cloud risk context through a Wiz CNAPP integration [4][5][16]. Enforcement is agentless for cloud workloads (GCP Network Security Integration intercepts, agentless workload posture scanning) with container agents for Kubernetes deployed via a Helm chart [19][20][32]. On-premises, Quantum security gateways and Maestro clusters provide east-west segmentation at scale, managed by the Smart-1 platform [6][27]. Check Point positions CloudGuard in the zero-trust / micro-segmentation space as a prevention-first platform that extends on-premises policy to hybrid clouds [2][4][13]. Across the 33 checklist items the product scores 8 supported, 15 partial, 4 not-applicable and 6 unknown.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 0                | 8      | 0   |
| partial          | 15    | 1                | 14     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 1     | 0                | 1      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 16 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.4:** No in-path host agent exists for CloudGuard segmentation (agentless intercept/gateway enforcement), so an agent-crash fail-open/fail-closed question does not apply; no agent fail-safe behavior is documented.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | — | CloudGuard Controller polls cloud environments via vendor APIs and auto-pushes object/attribute changes (subnets, security groups, VMs, tags) to gateways; flow-level east-west visibility is described via gateway traffic visibility and the Illumio integration. [1], [3], [7], [13], [29] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Traffic-map visualization is delivered through the Illumio Insights integration (agentless telemetry from Check Point firewalls), while Check Point documents unified visibility from a single console; no per-App/Environment/Role/Process map view is documented. [2], [7], [9] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Log retention is configurable since R80.40 (logs deleted after a configured period) and Smart-1 stores up to 48TB, but no retention default of 90 days or more is documented. [27], [28] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | Vulnerability context is surfaced by correlating Wiz CNAPP findings with Check Point firewall rules and topology, and Cloud Firewall is described as including vulnerability management; no CVE layer rendered directly on a Check Point map is documented. [5], [16] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | — | East-west traffic paths and lateral movement are surfaced via Illumio Insights and blocked via Check Point micro-segmentation and threat prevention; no native unrecognized-traffic classifier is documented. [4], [8] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | CloudGuard policy is built from cloud tags/objects (e.g. a 'department=rnd' tag replaces IP tables) and cloud-defined Security Groups, and Identity Awareness lets rules use Access Role objects; enforcement is pushed to gateways automatically. [1], [2], [30] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | AI-driven policy automation and orchestration is documented (agentic network security orchestration; AI Security Management dynamic policy engine), but no explicit ML-based rule-recommendation feature is described. [6], [7] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | — | no evidence found (No evidence found for policy simulation or dry-run mode.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | — | Policy installation history lets an admin revert to a specific previously installed version ('Install specific version'), documented as a revert flow rather than a one-click rollback. [25] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | — | Policy layers and pre-defined policy templates, policy packages that group policies for shared install targets, and up to 200 multi-domain policy domains are documented. [2], [26], [27] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | CloudGuard protects workloads across AWS/Azure/GCP/Oracle/Alibaba/Huawei/Tencent/IBM and hypervisors (VMware, Hyper-V, KVM, Xen, NSX, ACI, Nutanix, OpenStack) via network enforcement with 17 documented data-center connectors; no per-OS host agent support matrix (Windows 2003-2022, AIX, Solaris) is documented. [1], [2], [3], [31] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | — | CloudGuard Controller provides a container security component for native Kubernetes and managed services (AKS, EKS, GKE) with OpenShift setup commands, and a Helm chart deploys CloudGuard agents for inventory, posture, image assurance, visibility, threat intelligence, runtime protection and admission control. [1], [20] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | — | Both enforcement models are documented: agentless network/cloud-native enforcement (GCP Network Security Integration intercept deployments, agentless workload posture scanning) and agent-based container agents deployed via Helm chart. [10], [19], [32] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | — | no evidence found (No evidence found for fully air-gapped (no-internet) deployment of CloudGuard components.) |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scalability is described in throughput/management terms: up to 3 Tbps unified network throughput, Maestro hyperscale clusters, elastic cloud scaling, and up to 400 managed gateways per Smart-1; no workload count of 50,000 or more is published. [3], [6], [27] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | — | no evidence found (CloudGuard deploys container agents for Kubernetes workloads (confirmed elsewhere in this assessment, e.g. items 3.1/6.4), so a CPU-overhead referent exists, but no CPU percentage figure for that agent is published in staged sources.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | — | no evidence found (CloudGuard deploys container agents for Kubernetes workloads (confirmed elsewhere in this assessment), so a RAM-footprint referent exists, but no memory figure for that agent is published in staged sources.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Vendor cites sub-3μs accelerated firewalling latency on Quantum hardware gateways, below the 0.1ms threshold, but the figure is qualitative/marketing and no latency is published for cloud gateways or container agents. [6] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | No in-path host agent exists for CloudGuard segmentation (agentless intercept/gateway enforcement), so an agent-crash fail-open/fail-closed question does not apply; no agent fail-safe behavior is documented. [19], [32] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | — | no evidence found (Kubernetes agents are deployed via Helm chart, so an install/update referent exists, but no explicit reboot-or-not statement for that agent is documented in staged sources.) |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | RESTful Management API automation is documented (Trusted API with scoped privileges, official Python SDK, Terraform/Management API for data-center objects), but no statement that 100% of admin functions are API-exposed. [1], [2], [21] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Log Exporter sends Check Point logs over syslog in Syslog/CEF/LEEF/JSON formats to multiple SIEMs, with an official Splunk app and a Microsoft Sentinel integration documented. [14], [15], [16] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | — | CloudGuard Controller integrates the Security Management Server with ServiceNow CMDB (imports CIs and Tags as policy objects), and the Check Point-ServiceNow integration page documents using CMDB attributes to build asset-driven policies for Cloud Network Security. [1], [23] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | — | CI/CD and IaC automation is documented: Terraform provider and modules for CloudGuard, plus Cloud Firewall integration with DevOps/CI/CD pipelines enabling security-as-code. [4], [5], [22] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | — | no evidence found (No evidence found for process-level enforcement granularity.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Threat intelligence (ThreatCloud-driven threat prevention, threat emulation/extraction, anti-bot) is documented; deception is only described generically (honeypots supported via XDR/XPR threat-intel use), not as a CloudGuard microsegmentation module. [4], [6], [24] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | CloudGuard CSPM runs compliance rulesets for PCI-DSS, CIS Foundations, ISO, HIPAA and SOC2 with automated compliance reporting; NIST 800-207 and IEC 62443 rulesets are not evidenced. [4], [10] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | Mutual trust between gateways and management is established via Secure Internal Communication (SIC) secrets, and Log Exporter supports mutual authentication over TLS 1.2; no TLS 1.3 agent-controller channel is documented. [14], [17] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | HA is documented across deployment shapes: CloudGuard HA Terraform module for Azure (availability sets/zones, load balancers), AWS cross-AZ cluster and autoscaling GWLB modules, and Quantum firewall clustering with Maestro 99.999% resiliency. [6], [17], [18] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (No evidence found describing autonomous policy enforcement while the controller/management is disconnected.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (No evidence found for disaster-recovery site sync.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | high | — | NIST CMVP lists the Quantum Security Gateway Cryptographic Library as FIPS 140-2 (Level 1, active), and the Common Criteria portal lists Quantum Gateway R81.10 and R82 configurations at EAL4+; FIPS 140-3 is not evidenced. [11], [12] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No evidence found for Siemens/Honeywell/ABB industrial compatibility certifications.) |

---

## 4. Notable Strengths

- **Tag- and identity-driven policy (2.1):** CloudGuard policy is built from cloud tags (a "department=rnd" tag replaces manual IP tables) and cloud-defined Security Groups, with Identity Awareness access roles in rules [1][2][30].
- **Kubernetes / OpenShift native support (3.2):** CloudGuard Controller's container security component supports native Kubernetes and managed services (AKS, EKS, GKE) plus OpenShift, and a Helm chart deploys agents for admission control, runtime protection, image assurance and posture [1][20].
- **Agentless and agent enforcement coexist (3.3):** agentless network intercepts (GCP Network Security Integration) and agentless workload posture scanning sit alongside container agents, so deployments can avoid host agents entirely [10][19][32].
- **SIEM, CMDB and CI/CD integrations (5.2, 5.3, 5.4):** Log Exporter ships logs over syslog/CEF/LEEF with an official Splunk app and Microsoft Sentinel integration, ServiceNow CMDB data becomes policy objects, and Terraform/CI-CD enable security-as-code [1][14][15][22][23].
- **Certified security baselines (8.1):** FIPS 140-2 (Level 1, active) for the Quantum Security Gateway Cryptographic Library and Common Criteria EAL4+ for R81.10/R82 gateway configurations [11][12].

## 5. Notable Gaps / Risks

- **Flow-level visibility and mapping are partner-delivered (1.1, 1.2):** CloudGuard auto-discovers cloud assets and objects, but connection-flow discovery and per-App/Environment/Role/Process maps come from the Illumio and Wiz integrations rather than a native Check Point feature; buyers needing native flow mapping should verify the roadmap.
- **No policy simulation and no one-click rollback (2.3, 2.4):** no dry-run mode is documented, and reverting a policy requires reinstalling a specific version from Installation History rather than a one-click action.
- **Process-level enforcement is not evidenced (6.1):** no documentation describes enforcement below service/port granularity.
- **Autonomous mode and DR are undocumented (7.2, 7.3):** there is no staged evidence that enforcement continues when the controller/management is fully disconnected, or for disaster-recovery site sync.
- **Compliance-standard coverage is partial (6.3):** PCI-DSS, ISO, HIPAA, SOC2 and CIS rulesets are evidenced, but NIST 800-207 and IEC 62443 are not, and scalability is documented in throughput/gateway counts rather than the checklist's 50,000-workload threshold (3.5).

## 6. Evidence Quality Notes

Evidence came from 32 staged sources: 23 vendor documentation items (the R82.10 CloudGuard Controller admin-guide PDF, R81 admin-guide pages, GitHub SDK/module/Helm repos), 2 vendor datasheets, 4 third-party reviews (two IT Security Guru articles, AIMultiple's microsegmentation list, the AWS Marketplace blog), 1 community source (Wikipedia) and 2 certification registries (NIST CMVP, Common Criteria portal). 14 items were backed by at least 2 source types; 17 items relied only on vendor documentation and were capped at medium confidence, and only 8.1 reached high confidence via the registries. Because checkpoint.com is WAF-protected, product pages were staged through the r.jina.ai reader proxy and official PDFs from checkpoint.com/downloads and sc1.checkpoint.com were staged directly; every cited quote was verified verbatim against the staged text (79 evidence entries, all grounded).

No direct contradictions between sources surfaced; the main triangulation caveat is that flow visibility (1.1, 1.2, 1.5) and vulnerability context (1.4) rest on partner capabilities (Illumio, Wiz) that Check Point integrates with rather than owns, so those items were rated partial even where the integration is well documented. Numeric-threshold items stayed qualitative: 1.3 and 3.5 are configurable/elastic without published values, 4.3 cites sub-3us latency for hardware gateways only, and 4.1/4.2/4.4/4.5 were marked not-applicable because CloudGuard segmentation enforcement is agentless (with the Kubernetes-agent exception noted). Six items (2.3, 3.4, 6.1, 7.2, 7.3, 8.2) had no evidence and were rated unknown per the anti-fabrication contract.

---

## Bibliography

[1] Check Point. "CloudGuard Controller R82.10 Administration Guide". https://sc1.checkpoint.com/documents/R82.10/WebAdminGuides/EN/CP_R82.10_CloudGuard_Controller_AdminGuide/CP_R82.10_CloudGuard_Controller_AdminGuide.pdf (Retrieved: 2026-08-10T11:43:30Z)
[2] Check Point. "CloudGuard IaaS for Private and Public Clouds - White Paper (2018)". https://www.checkpoint.com/downloads/products/cloudguard-iaas-security-public-private-cloud-whitepaper.pdf (Retrieved: 2026-08-10T11:43:30Z)
[3] Check Point. "CloudGuard Network Security - Solution Overview datasheet (2024)". https://www.checkpoint.com/downloads/products/cloudguard-network-security-solution-overview.pdf (Retrieved: 2026-08-10T11:43:30Z)
[4] Check Point. "Check Point Cloud Network Security product page". https://www.checkpoint.com/cloudguard/cloud-network-security/ (Retrieved: 2026-08-10T11:43:30Z)
[5] Check Point. "Check Point Cloud Security Services (CloudGuard) product page". https://www.checkpoint.com/cloudguard/ (Retrieved: 2026-08-10T11:43:30Z)
[6] Check Point. "Check Point Quantum Network Security Services product page". https://www.checkpoint.com/quantum/ (Retrieved: 2026-08-10T11:43:30Z)
[7] IT Security Guru. "Check Point and Illumio Team Up to Advance Zero Trust with Unified Security and Threat Prevention". https://www.itsecurityguru.org/2025/04/25/check-point-and-illumio-team-up-to-advance-zero-trust-with-unified-security-and-threat-prevention/ (Retrieved: 2026-08-10T11:43:30Z)
[8] IT Security Guru. "Check Point and Illumio Deepen Alliance to Counter AI-Powered Cyberattacks". https://www.itsecurityguru.org/2026/06/17/check-point-and-illumio-deepen-alliance-to-counter-ai-powered-cyberattacks/ (Retrieved: 2026-08-10T11:43:30Z)
[9] AIMultiple. "Top 10 Microsegmentation Tools in 2026". https://aimultiple.com/microsegmentation-tools (Retrieved: 2026-08-10T11:43:30Z)
[10] AWS Marketplace Blog. "Enable security and automated continuous compliance using CloudGuard from AWS Marketplace". https://aws.amazon.com/blogs/awsmarketplace/enable-security-and-automated-continuous-compliance-using-cloudguard-from-aws-marketplace/ (Retrieved: 2026-08-10T11:43:30Z)
[11] NIST. "NIST CMVP Certificate #4264 - Quantum Security Gateway Cryptographic Library". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4264 (Retrieved: 2026-08-10T11:43:30Z)
[12] Common Criteria Portal. "Common Criteria Certified Products list". https://www.commoncriteriaportal.org/products/index.cfm (Retrieved: 2026-08-10T11:43:30Z)
[13] Wikipedia. "Check Point Software Technologies (Wikipedia)". https://en.wikipedia.org/wiki/Check_Point (Retrieved: 2026-08-10T11:43:30Z)
[14] Check Point. "R81 Logging and Monitoring Administration Guide - Log Exporter". https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_LoggingAndMonitoring_AdminGuide/Topics-LMG/Log-Exporter.htm (Retrieved: 2026-08-10T11:43:30Z)
[15] Check Point. "Check Point App for Splunk - GitHub README". https://raw.githubusercontent.com/CheckPointSW/Check_Point_App_for_Splunk/master/README.md (Retrieved: 2026-08-10T11:43:30Z)
[16] Check Point. "Check Point CloudGuard Wiz integration page (workload protection URL)". https://www.checkpoint.com/cloudguard/workload-protection/ (Retrieved: 2026-08-10T11:43:30Z)
[17] Check Point. "CloudGuard Network Security High Availability Terraform module (Azure) - README". https://raw.githubusercontent.com/CheckPointSW/terraform-azure-cloudguard-network-security/master/modules/high-availability/README.md (Retrieved: 2026-08-10T11:43:30Z)
[18] Check Point. "Terraform Modules for CloudGuard Network Security (CGNS) - AWS - README". https://raw.githubusercontent.com/CheckPointSW/terraform-aws-cloudguard-network-security/master/README.md (Retrieved: 2026-08-10T11:43:30Z)
[19] Check Point. "Check Point Network Security Integration Terraform module for GCP - README". https://raw.githubusercontent.com/CheckPointSW/terraform-gcp-cloudguard-network-security/master/modules/network-security-integration/README.md (Retrieved: 2026-08-10T11:43:30Z)
[20] Check Point. "Check Point CloudGuard agents Helm chart - README". https://raw.githubusercontent.com/CheckPointSW/charts/master/checkpoint/cloudguard/README.md (Retrieved: 2026-08-10T11:43:30Z)
[21] Check Point. "Check Point Management API Python SDK - GitHub README". https://raw.githubusercontent.com/CheckPointSW/cp_mgmt_api_python_sdk/master/README.md (Retrieved: 2026-08-10T11:43:30Z)
[22] Check Point. "Terraform Provider for Check Point - GitHub README". https://raw.githubusercontent.com/CheckPointSW/terraform-provider-checkpoint/master/README.md (Retrieved: 2026-08-10T11:43:30Z)
[23] Check Point. "Check Point Configuration Management Database (CMDB) integration page". https://www.checkpoint.com/integrations/configuration-management-database-cmdb/ (Retrieved: 2026-08-10T11:43:30Z)
[24] Check Point. "What Is Deception Technology? - Check Point Cyber Hub". https://www.checkpoint.com/cyber-hub/cyber-security/what-is-deception-technology/ (Retrieved: 2026-08-10T11:43:30Z)
[25] Check Point. "R81 Quantum Security Management Admin Guide - Policy Installation History". https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_SecurityManagement_AdminGuide/Topics-SECMG/Policy-Installation-History.htm (Retrieved: 2026-08-10T11:43:30Z)
[26] Check Point. "R81 Quantum Security Management Admin Guide - Managing Policies". https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_SecurityManagement_AdminGuide/Topics-SECMG/Managing-Policies.htm (Retrieved: 2026-08-10T11:43:30Z)
[27] Check Point. "Quantum Smart-1 Security Management Platform datasheet (600-S/600-M/6000-L/6000-XL)". https://www.checkpoint.com/downloads/products/smart-1-security-management-platform-datasheet.pdf (Retrieved: 2026-08-10T11:43:30Z)
[28] Check Point. "R81 Logging and Monitoring Admin Guide - Daily Logs Retention". https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_LoggingAndMonitoring_AdminGuide/MicroContent/Resources/MicroContent/MicroContent_LMG/Daily_Logs_Retention/Daily-Logs-Retention.htm (Retrieved: 2026-08-10T11:43:30Z)
[29] Check Point. "CloudGuard Cloud Native Application Protection Platform Admin Guide - Assets". https://sc1.checkpoint.com/documents/Infinity_Portal/WebAdminGuides/EN/CloudGuard-PM-Admin-Guide/Documentation/Assets/CloudInventory.htm (Retrieved: 2026-08-10T11:43:30Z)
[30] Check Point. "R81 Quantum Security Gateway Admin Guide - Security Policy". https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_NextGenSecurityGateway_Guide/Topics-FWG/Security-Policy.htm (Retrieved: 2026-08-10T11:43:30Z)
[31] Check Point. "CloudGuardIaaS (CloudGuard Network Security) repository README". https://raw.githubusercontent.com/CheckPointSW/CloudGuardIaaS/master/README.md (Retrieved: 2026-08-10T11:43:30Z)
[32] Check Point. "CloudGuard AWP (Agentless Workload Posture) for AWS Terraform module - README". https://raw.githubusercontent.com/dome9/terraform-dome9-awp-aws/master/README.md (Retrieved: 2026-08-10T11:43:30Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 30
- **Sources reviewed:** 32 (kept: 32, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, community: 1, third_party_review: 4, vendor_datasheet: 2, vendor_doc: 23
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
