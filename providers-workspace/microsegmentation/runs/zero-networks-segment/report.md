# Microsegmentation Product Assessment: Zero Networks - Zero Networks Segment

**Product ID:** `zero-networks-segment`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T18:00:00Z
**Total evidence items collected:** 69
**Total distinct sources:** 25

---

## 1. Overview

Zero Networks Segment is the network-segmentation component of the Zero Networks platform, positioned as an automated, agentless, MFA-powered microsegmentation solution [7]. It automatically discovers assets and identities, learns all network connections over a roughly 30-day period, and generates deterministic least-privilege policies that are enforced through native host firewalls (Windows Firewall, Linux IPTables/NFTables) and, for IoT/OT, switch ACLs [6, 24]. Deployment consists of a SaaS admin portal (the "cloud service") plus an on-premises segment/trust server per environment that orchestrates enforcement out-of-band and is never inline to traffic [24]. Policies are written at the label and group level, and network-layer MFA is applied to privileged ports (RDP, SSH, WinRM) through SAML identity providers [6, 24]. The product also ships a real-time Network Map, AI visibility and compliance capabilities, Kubernetes support (eBPF-based monitoring with native Kubernetes enforcement), and official Python SDK and Terraform provider [2, 5, 18, 19]. Evidence draws on vendor documentation and datasheets, a technical product overview hosted by SRC Cyber Solutions, a Network World review, BankInfoSecurity coverage, and a Palo Alto Networks partner brief [6, 17, 22, 24].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 10    | 3                | 7      | 0   |
| partial          | 11    | 0                | 11     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 7     | 0                | 0      | 7   |
| not_applicable   | 4     | 0                | 4      | 0   |

**Evidence quality:** 15 items backed by ≥ 2 source_types; 16 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** No host agent is deployed - enforcement runs on native host firewalls controlled remotely from the trust server - so an agent CPU-overhead figure does not apply.
- **4.2:** The product is agentless and requires no software installation on workloads or OT devices, so an agent RAM-footprint figure does not apply.
- **4.4:** There is no host agent whose crash could interrupt traffic; the orchestrator is a stateless, out-of-band appliance and the enforced rules live in native host firewalls.
- **4.5:** No per-host software is installed (agentless; OT devices require no software), and the vendor states assets are microsegmented without downtime, so reboot requirements do not apply.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | The product automatically discovers all network assets and identities, and the network map continuously ingests traffic across on-prem, cloud, IoT/OT and Kubernetes; Network World independently confirms inventory is built by syncing Active Directory, Microsoft Entra ID and tools like Axonius. [1], [2], [6] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | medium | - | The Network Map provides an interactive graphical view of actual asset-to-asset and identity-to-asset communication, with a unified asset-to-asset map across environments and drill-down from global architecture to process-level detail. [2], [10] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | - | no evidence found (No source states a flow-history retention period; vendor materials emphasize live, always-current network mapping rather than historical flow retention.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (Map risk context covers privileged access, high-risk ports and external exposure, but no source mentions vulnerability/CVE context displayed on the map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | The Network Mapping infosheet documents identification of unexpected or newly discovered internal communication paths, hidden or unnecessary east-west access, and anomalous internal connections. [10] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | - | Network World reports that policy is written at the label and group level rather than against raw IP addresses; the Palo Alto Networks partner brief documents tag-based policy enforcement, and GigaOm coverage cites identity-driven enforcement using user, device and environment attributes. [6], [8], [17] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | - | Suggested policies derived from observed traffic are offered for review, but the vendor explicitly states it does not rely on AI for enforcement decisions - policy generation is positioned as deterministic automation rather than AI/ML-based recommendation. [4], [10], [25] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | high | - | Before enforcement begins, policies are simulated against observed traffic to show what would be allowed, blocked or MFA-challenged; Network World and vendor materials (map page, mapping infosheet, visibility blog) all document simulation and staged rollout. [2], [6], [10], [16] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No source documents a one-click policy rollback; the closest documented actions are staged rollout and click-to-quarantine during incidents.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found (Policies are tied to labels and groups, but no source describes inherited or hierarchical rule structures.) |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The product overview documents Windows (2008 and above), Linux (post-2007) and macOS support, with enforcement via Windows Firewall and Linux IPTables/NFTables; Windows Server 2003 and AIX/Solaris are not evidenced. [6], [24] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | - | A Kubernetes solution brief documents eBPF-based monitoring with native Kubernetes enforcement, and the network mapping infosheet covers Kubernetes alongside on-prem, cloud and IoT/OT in a single view. [5], [10] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | The product is documented as agentless with network integration (native host firewalls, switch ACLs, SaaS portal); Network World and the AWS Marketplace listing confirm no dedicated agents are used, so the agent-based half of the requirement is not provided. [6], [7], [24] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Not Supported | medium | - | The management and learning plane is a SaaS cloud service ('the brains of the operations') from which the on-premises segment/trust server is automatically updated, and a break-glass procedure covers loss of connectivity - no fully air-gapped operating mode is documented. [24] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scale is described only qualitatively ('tens of thousands of assets', 'infinitely scalable', 'any number of hosts'); no source cites a workload count of 50,000 or more. [4], [11], [13] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | - | No host agent is deployed - enforcement runs on native host firewalls controlled remotely from the trust server - so an agent CPU-overhead figure does not apply. [6], [24] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | - | The product is agentless and requires no software installation on workloads or OT devices, so an agent RAM-footprint figure does not apply. [7], [12] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Enforcement is out-of-band - the segment/trust server is not inline to traffic - and the vendor and a third-party review describe minimal performance overhead, but no measured latency figure is published. [23], [24] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | - | There is no host agent whose crash could interrupt traffic; the orchestrator is a stateless, out-of-band appliance and the enforced rules live in native host firewalls. [6], [24] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | - | No per-host software is installed (agentless; OT devices require no software), and the vendor states assets are microsegmented without downtime, so reboot requirements do not apply. [11], [12] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | A RESTful API (portal.zeronetworks.com/v1/api) with API-key authentication covers assets, groups, policies, rules and MFA, backed by an official Python SDK and Terraform provider, but no source claims the API covers 100% of administrative functions. [18], [19], [24] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | The product overview documents API-based synchronization to SIEMs including Splunk, Azure Sentinel and IBM QRadar plus SOAR automation scripts; a Splunkbase add-on ingests Segment audit logs, and a third-party review confirms SIEM/SOAR integration. [20], [23], [24] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | Zero Networks Inc publishes an official 'Zero Networks App for CMDB' on the ServiceNow Store, providing the ServiceNow/CMDB integration channel for the platform. [21] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | An official Terraform provider (zeronetworks/zeronetworks) manages policies, rules, groups and MFA resources as code, and the Python SDK exposes the same operations programmatically, enabling CI/CD-driven DevSecOps. [18], [19] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | Identity-based controls extend to AI agents treated as processes, and BankInfoSecurity reports segmentation can be applied to individual applications and processes, but enforcement itself is network-layer (host firewall/ACL) with no host-level process firewall documented. [9], [10], [22] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | - | no evidence found (No source documents threat-intelligence feeds or honeypot/deception detection for the Segment product.) |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | The product generates reporting supporting several compliance standards, the vendor attests SOC 2 Type 2 and GDPR, and it publishes mapping guides for PCI DSS and ISA/IEC 62443-3-3 plus an AI risk engine mapped to NIS2/CIS; explicit ISO 27001 or NIST 800-207 reporting is not evidenced. [3], [14], [15], [24] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | No agent-controller channel exists (agentless); control traffic uses WinRM/SSH and the HTTPS portal API, and the vendor states cloud data is segregated and encrypted, but TLS 1.3 or mutual-auth specifics are not documented. [18], [24] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | High availability is provided by deploying an additional trust server with no configuration required, avoiding a single point of failure; the active-active/active-passive mode is not specified. [24] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | The orchestrator is stateless and not inline to traffic, and the vendor documents a break-glass procedure for total loss of service or connectivity, but no source explicitly states policy enforcement continues autonomously on hosts during a controller outage. [24] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | The cloud control plane runs in worldwide data centers (US, EU, APAC) for redundancy, and the trust server is a stateless appliance that needs no backup; a dedicated DR site-sync procedure is not detailed. [24] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | - | no evidence found (No FIPS 140-2/140-3 or Common Criteria validation found; NIST CMVP search returned no certificates for Zero Networks; the vendor attests SOC 2 Type 2 and GDPR, which are not FIPS/CC.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (OT/IoT segmentation is documented, but no certification or validated compatibility with Siemens, Honeywell or ABB was found.) |

---

## 4. Notable Strengths

- **Automated agentless microsegmentation (items 3.3, 4.1, 4.2):** no agents are deployed on workloads; enforcement runs on native OS firewalls orchestrated by a stateless, out-of-band trust server, which also makes agent-specific operational overhead (CPU, RAM) structurally out of scope [6, 24].
- **Identity/label-based policy engine with simulation (items 2.1, 2.3):** policies are written at the label and group level rather than against raw IP addresses, and every policy is simulated against observed traffic before enforcement - corroborated by independent press [6].
- **Real-time visibility (items 1.1, 1.2, 1.5):** continuous auto-discovery and an interactive Network Map expose asset-to-asset and identity-to-asset communication, including unexpected or hidden east-west paths, with drill-down to process level [1, 2, 10].
- **Integration and automation surface (items 5.2, 5.3, 5.4):** API-based SIEM/SOAR synchronization (Splunk, Azure Sentinel, IBM QRadar), an official ServiceNow CMDB app, and a Terraform provider enable policy-as-code and DevSecOps workflows [18, 19, 20, 21, 24].
- **High-availability support (item 7.1):** deploying an additional trust server provides built-in high availability without configuration; the cloud control plane runs in US/EU/APAC data centers for redundancy, and the trust server is stateless with auto scale-out [24].

## 5. Notable Gaps / Risks

- **Air-gapped environments are not supported (item 3.4):** the management and learning plane is a SaaS cloud service that the on-premises server auto-updates from, so fully offline networks cannot run the product normally - only a break-glass procedure for connectivity loss is documented [24].
- **No documented scale figure (item 3.5):** coverage is limited to qualitative claims ("tens of thousands of assets", "infinitely scalable"); buyers needing more than 50,000 centrally managed workloads would require vendor sizing validation [4, 11, 13].
- **No measured latency figure (item 4.3):** enforcement is out-of-band and described as minimal-overhead, but no published measurement supports the under-0.1 ms requirement [23, 24].
- **Compliance reporting is partial (item 6.3):** PCI DSS and ISA/IEC 62443 guides plus SOC 2 Type 2/GDPR attestation exist, but ISO 27001 and NIST 800-207 reporting are not evidenced [14, 15, 24].
- **Unevidenced capabilities (items 1.3, 1.4, 2.4, 2.5, 6.2, 8.1, 8.2):** flow-history retention, CVE context on the map, one-click rollback, hierarchical rules, threat-intel/deception integration, FIPS/Common Criteria certification, and Siemens/Honeywell/ABB OT certifications are all unknown and would need vendor confirmation.

## 6. Evidence Quality Notes

The run collected 69 grounded evidence entries across 25 sources. Three items (1.1, 2.1, 2.3) reached high confidence with at least one independent source (Network World) alongside vendor material; 15 items are backed by two or more source types, while 16 items rest on vendor-only material and are capped at medium confidence per the validator rule. The strongest independent corroboration comes from Network World (agentless approach, label-based policy, pre-enforcement simulation) and BankInfoSecurity (process-level controls for AI agents). The single richest source is the vendor-authored Zero Networks Segment technical product overview hosted by SRC Cyber Solutions, which underpins the architecture, HA/DR, OS support, SIEM and compliance items; it is vendor-published and was treated as such. Vendor-hosted pages describing the Gartner and GigaOm reports were also treated as vendor content rather than independent analyst evidence.

Search-engine access was heavily rate-limited during the run, so items 1.3, 1.4, 2.4, 2.5, 6.2, 8.1 and 8.2 yielded no evidence and were honestly marked unknown rather than inferred as unsupported; the ServiceNow Store evidence is limited to the listing title because the page is JavaScript-rendered. No contradictions between sources were observed. Where vendor claims were qualitative (scale, latency, compliance breadth), verdicts were downgraded to partial with numeric_value left null rather than rounding to the checklist threshold.

---

## Bibliography

[1] Zero Networks. "Network Segmentation | Zero Networks". https://zeronetworks.com/platform/network-segmentation (Retrieved: 2026-08-10T07:04:04Z)
[2] Zero Networks. "Network Map | Zero Networks". https://zeronetworks.com/platform/network-map (Retrieved: 2026-08-10T07:04:04Z)
[3] Zero Networks. "AI Segmentation Is Here (Zero Networks blog)". https://zeronetworks.com/blog/ai-segmentation-is-here (Retrieved: 2026-08-10T07:04:04Z)
[4] Zero Networks. "How to Automatically Generate Least-Privilege Policies Based on Network Behavior". https://zeronetworks.com/blog/how-to-automatically-generate-least-privilege-policies-based-on-network-behavior (Retrieved: 2026-08-10T07:04:04Z)
[5] Zero Networks. "Solution Brief: Zero Networks for Kubernetes". https://zeronetworks.com/resource-center/brochures/solution-brief-zero-networks-for-kubernetes (Retrieved: 2026-08-10T07:04:04Z)
[6] Network World (Sean Michael Kerner). "How Zero Networks is closing the network enforcement gap for AI agents". https://www.networkworld.com/article/4161533/how-zero-networks-is-closing-the-network-enforcement-gap-for-ai-agents.html (Retrieved: 2026-08-10T07:04:04Z)
[7] AWS Marketplace (Zero Networks listing). "AWS Marketplace: Zero Networks Segment". https://aws.amazon.com/marketplace/pp/prodview-c7kbeyjo2yspg (Retrieved: 2026-08-10T07:04:04Z)
[8] Zero Networks. "2026 GigaOm Radar for Microsegmentation (Zero Networks page)". https://zeronetworks.com/resource-center/reports/2026-gigaom-radar-for-microsegmentation (Retrieved: 2026-08-10T07:04:04Z)
[9] Zero Networks. "Zero Networks AI Segmentation Datasheet". https://zeronetworks.com/files/brochures/ZN_AI-Segmentation_Datasheet.pdf (Retrieved: 2026-08-10T07:04:04Z)
[10] Zero Networks. "Zero Networks Network Mapping Infosheet". https://zeronetworks.com/files/brochures/NetworkMapping-Infosheet.pdf (Retrieved: 2026-08-10T07:04:04Z)
[11] Zero Networks. "Zero Networks Network Segmentation Brochure". https://zeronetworks.com/files/brochures/Zero-Networks-Network-Segmentation-Brochure.pdf (Retrieved: 2026-08-10T07:04:04Z)
[12] Zero Networks. "Zero Networks IoT and OT Segmentation Infosheet". https://zeronetworks.com/files/brochures/OT-IoT-Segmentation_Infosheet_Zero_Networks.pdf (Retrieved: 2026-08-10T07:04:04Z)
[13] Zero Networks. "Zero Networks vs VMware NSX Brochure". https://zeronetworks.com/files/Zero-Networks_vs_NSX-Brochure.pdf (Retrieved: 2026-08-10T07:04:04Z)
[14] Zero Networks. "Compliance Guide: How Zero Networks Helps with ISA/IEC 62443". https://zeronetworks.com/resource-center/guides/how-zero-networks-helps-with-isa-iec-62443 (Retrieved: 2026-08-10T07:04:04Z)
[15] Zero Networks. "Compliance Guide: How Zero Networks Helps with PCI DSS". https://zeronetworks.com/resource-center/guides/how-zero-networks-helps-with-pci-dss-regulation-requirements (Retrieved: 2026-08-10T07:04:04Z)
[16] Zero Networks. "How Real-Time Network Visibility Enables Automated Zero Trust Enforcement". https://zeronetworks.com/blog/how-real-time-network-visibility-enables-automated-zero-trust-enforcement (Retrieved: 2026-08-10T07:04:04Z)
[17] Palo Alto Networks / Zero Networks. "Palo Alto Networks and Zero Networks Partner Brief". https://prod.prmcdn.io/attachments/bd8ecf7b8b294b07b5d7755f13b507a3/1/parent_pb_zero-networks_022125%20(1).pdf (Retrieved: 2026-08-10T07:04:04Z)
[18] Zero Networks (GitHub). "zeronetworks/zeronetworks-python-sdk (GitHub)". https://github.com/zeronetworks/zeronetworks-python-sdk (Retrieved: 2026-08-10T07:04:04Z)
[19] Zero Networks (GitHub). "zeronetworks/terraform-provider-zeronetworks (GitHub)". https://github.com/zeronetworks/terraform-provider-zeronetworks (Retrieved: 2026-08-10T07:04:04Z)
[20] Splunkbase (Nicholas DiCola). "Zero Networks Add-on for Splunk | Splunkbase". https://splunkbase.splunk.com/app/6539 (Retrieved: 2026-08-10T07:04:04Z)
[21] ServiceNow Store (Zero Networks Inc). "Zero Networks App for CMDB - ServiceNow Store". https://store.servicenow.com/store/app/b30c6f2e1b246a50a85b16db234bcba7 (Retrieved: 2026-08-10T07:04:04Z)
[22] BankInfoSecurity (ISMG). "How Zero Networks Targets AI Agents With Microsegmentation". https://www.bankinfosecurity.com/how-zero-networks-targets-ai-agents-microsegmentation-a-32283 (Retrieved: 2026-08-10T07:04:04Z)
[23] Startup Defense. "Palo Alto + Zero Networks: NGFW Meets Microsegmentation". https://www.startupdefense.io/blog/palo-alto-networks-and-zero-networks-integration-how-microsegmentation-and-ngfws-work-together (Retrieved: 2026-08-10T07:04:04Z)
[24] Zero Networks (hosted by SRC Cyber Solutions). "Zero Networks Segment Technical Product Overview". https://srccybersolutions.com/uploads/Zero-Networks-Segment-Product-Overview.pdf (Retrieved: 2026-08-10T07:04:04Z)
[25] Zero Networks. "6 Processes to Automate When Implementing Microsegmentation". https://zeronetworks.com/blog/6-processes-to-automate-when-implementing-microsegmentation (Retrieved: 2026-08-10T07:04:04Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 16
- **Sources reviewed:** 25 (kept: 25, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, third_party_review: 3, vendor_blog: 4, vendor_datasheet: 6, vendor_doc: 11
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
