# Microsegmentation Product Assessment: Nutanix - Nutanix Flow Network Security

**Product ID:** `nutanix-flow-network-security`
**Version reference:** NCI 7.5 / AOS 7.5 (Flow Network Security 5.3.0)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T15:00:00Z
**Total evidence items collected:** 68
**Total distinct sources:** 16

---

## 1. Overview

Nutanix Flow Network Security (FNS) is the microsegmentation capability of the Nutanix Cloud Platform: an agentless, stateful distributed firewall embedded in the AHV hypervisor, with policy management and flow visualization delivered through Prism Central [6]. Nutanix positions FNS as an application-centric, identity-aware microsegmentation layer that abstracts security policy from IP addresses and VLANs, supporting Zero Trust and lateral-movement reduction for east-west traffic across AHV VMs, Nutanix Kubernetes Platform (NKP) clusters, and Nutanix Cloud Clusters in public clouds [2, 3]. Deployment shapes are the two Flow planes: Flow Network Security (distributed stateful firewall with saved/enforced/monitoring policy modes) and Flow Virtual Networking (VPCs and overlays), controlled by a Flow Controller that runs integrated on Prism Central or standalone on three worker plus two load-balancer VMs [5]. FNS 5.3.0, shipping with NCI 7.5, adds the Flow CNI plugin for Kubernetes, virtual TAP service insertion, exception groups, and cross-site policy replication via Entity Sync [4].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 11    | 7                | 4      | 0   |
| partial          | 13    | 0                | 13     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 4     | 0                | 0      | 4   |
| not_applicable   | 4     | 0                | 4      | 0   |

**Evidence quality:** 10 items backed by ≥ 2 source_types; 19 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** No guest agent runs on workloads (fully agentless, hypervisor-embedded), so agent CPU overhead does not apply.
- **4.2:** No guest agent runs on workloads, so there is no agent RAM footprint to measure.
- **4.4:** No guest enforcement agent exists whose failure could interrupt workload traffic; enforcement runs in the AHV hypervisor.
- **4.5:** No agent installation/update cycle exists in the agentless architecture, so reboot requirements do not apply.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Vendor docs describe built-in flow visualization giving real-time visibility into traffic flows for anomaly and dependency detection; AIMultiple independently confirms granular management and control of all VM traffic. [3], [6], [15] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Flow visualization maps application workflows at port level and groups VMs by categories (e.g. AppType, Environment); a per-process traffic view is not documented. [1], [3], [15] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | 1 days | Vendor docs state discovered traffic in the built-in flow visualization remains visible for 24 hours; no staged source documents at least 90 days of in-product flow retention, so the threshold is not met and longer-term storage would rely on external syslog capture. [6] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | — | no evidence found (No staged source describes CVE/vulnerability context rendered on the Flow connectivity map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | — | Vendor docs state visualization enables rapid detection of unexpected flows and security anomalies, with real-time visibility to detect anomalies; independent listing confirms network traffic monitoring. [3], [6], [15] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | — | Vendor docs state policies are attached to VMs/applications using dynamic categories and logical labels rather than IP/VLAN, with identity-based (Active Directory) policy context; independent listing confirms granular policy control of VM traffic. [1], [3], [6], [15] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | — | no evidence found (No staged source documents AI/ML-based automatic policy recommendation for Flow Network Security.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | high | — | Vendor docs describe Monitoring Mode as a dry-run: it allows all traffic while showing what would be blocked if the policy were enforced; AIMultiple independently notes a test function verifies policies before implementation. [6], [15] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | — | Vendor docs document policy backup and restore via the Prism Central GUI that reverts policies to a prior snapshot; a dedicated one-click rollback control is not documented. [6] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | — | Vendor docs document rule priority (intra-tier processed before inbound/outbound) and a policy evaluation order across policy types; an inherited parent-child rule model is not explicitly documented. [4], [6] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | The product is agentless (zero guest agents embedded in the AHV hypervisor), so guest-OS compatibility is not a factor; no staged source documents AIX/Solaris guest support on AHV, which supports Windows/Linux guests. [3], [6] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | high | — | Vendor docs state FNS extends microsegmentation to the Nutanix Kubernetes Platform with Cilium CNI network policies for VMs and pods, and the 7.5 CNI plugin integrates FNS with NKP; independent coverage confirms microsegmentation now extends to containerized workloads. [4], [6], [13] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | Vendor docs describe an agentless, hypervisor-embedded distributed firewall with zero guest agents; no agent-based deployment option is documented. [5], [6] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | high | — | Independent coverage states Nutanix supports fully disconnected dark-site environments without external SaaS control planes, and on-prem Nutanix Central enables upgrades in dark sites without external connections. [13], [14] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Vendor claims are qualitative (scales seamlessly across virtualized and multicloud environments) or cluster-scoped (up to 25 K8s clusters per console); no published per-deployment workload count demonstrates 50,000+ workloads (Configuration Maximums are on the gated support portal). [3], [6] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | No guest agent runs on workloads (fully agentless, hypervisor-embedded), so agent CPU overhead does not apply. [6] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No guest agent runs on workloads, so there is no agent RAM footprint to measure. [6] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Vendor docs describe line-rate stateful performance with linear scaling and no overhead, but publish no measured latency figure, so the <0.1 ms threshold is not demonstrated. [2], [6] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | No guest enforcement agent exists whose failure could interrupt workload traffic; enforcement runs in the AHV hypervisor. [6] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No agent installation/update cycle exists in the agentless architecture, so reboot requirements do not apply. [6] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | Prism Central v3/v4 REST APIs manage Flow Network Security (policy CRUD, quarantine via API, policy config export); documentation states 'most functionality' is exposed via APIs rather than claiming 100% coverage. [6], [8] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Vendor docs state FNS policy hit logs and API audit logs are exported via Syslog configured in Prism Central, enabling SIEM ingestion; no CEF-format or vendor-specific SIEM adapter is documented. [6] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | — | Independent coverage documents Nutanix-ServiceNow ITSM integration (respond to alerts/incidents and create tickets in ServiceNow); CMDB label/tag synchronization is not documented in staged sources. [16] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | — | The official Nutanix Terraform provider exposes Flow Network Security resources (network security policy, rules, entity groups, categories), enabling IaC/DevSecOps policy management. [10] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | — | Vendor docs explicitly state FNS is a stateful layer-4 microsegmentation platform filtering on packet/frame headers, with no process-level inspection; Layer 7 requires partner service insertion. [3], [6] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Vendor docs list traffic monitoring and threat detection as functions and describe service insertion for third-party L7 firewalls, IDS/IPS and threat-detection platforms; no native honeypot/deception capability is documented. [1], [3] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Vendor docs state FNS aligns with NIST SP 800-207 and PCI-DSS (plus HIPAA/SOX) with out-of-box audit and reporting; ISO 27001 and IEC 62443 are not mentioned in staged sources. [1], [3] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Unknown | low | — | no evidence found (No staged source documents TLS version or mutual authentication for Flow Network Security control channels (the product has no guest agents).) |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | Vendor docs recommend Prism Central scale-out for management/control-plane HA, describe a standalone Flow Controller with three worker and two load-balancer VMs, and document Prism leader election on failure. [5], [6], [9] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | — | Vendor docs state failure of the management/control plane does not immediately impact policy enforcement, and distributed firewall rules are enforced directly on each host. [2], [6] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | high | — | Vendor docs describe Entity Sync replicating security policies across availability zones for DR with CCLM and Multi-PC DR support; independent coverage confirms security policies are preserved during failover and restore. [4], [6], [13] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | NIST CMVP lists active FIPS 140-2 validated Nutanix cryptographic modules (OpenSSH client at level 1, another module at level 2); no Common Criteria EAL4+ entry was found and the CC portal was inaccessible, so platform-level FIPS 140-3/CC status remains unverified. [11], [12] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No staged source documents industrial software compatibility certifications from Siemens, Honeywell, or ABB for OT use.) |

---

## 4. Notable Strengths

- **Agentless hypervisor-native enforcement (items 3.3, 4.1, 4.2, 4.4):** FNS embeds a stateful distributed firewall directly in the AHV hypervisor with zero guest agents, eliminating agent CPU/RAM overhead, agent fail-open concerns, and agent lifecycle maintenance [6].
- **Application-centric, label-based policy model (items 2.1, 2.5):** policies attach to dynamic categories (Key:Value labels) and identity (Active Directory groups) instead of IP/VLAN, with documented rule priority and a policy-type evaluation order [1, 3, 6].
- **Kubernetes-native microsegmentation (item 3.2):** FNS extends to NKP using standard Cilium CNI Network Policies from a single Prism Central console covering both VMs and pods, with the 7.5 Flow CNI plugin unifying VM/container networking [4, 6].
- **Dry-run policy workflow (item 2.3):** Monitor Mode allows all traffic while showing what would be blocked if the policy were enforced, enabling safe staged rollout; AIMultiple independently confirms a test function that verifies policies before implementation [6, 15].
- **Air-gapped and DR-resilient operations (items 3.4, 7.2, 7.3):** dark-site/air-gapped operation is documented, policy enforcement continues if the management/control plane fails, and Entity Sync replicates policies across availability zones for disaster recovery [6, 13, 14].

## 5. Notable Gaps / Risks

- **No in-product 90-day flow history (item 1.3):** built-in flow visualization retains discovered traffic for only 24 hours, so the 90-day forensic-retention requirement is not met unless flows are shipped to an external syslog store [6].
- **Layer-4-only enforcement, no process-level control (item 6.1):** FNS filters on ports/protocols without inspecting process identity; process-level or deep L7 inspection requires partner service insertion, which is currently VLAN-scoped only [3, 6].
- **No AI/ML rule recommendation and no CVE context on the map (items 2.2, 1.4):** neither capability is documented in any staged source; both are common differentiators in competing microsegmentation platforms.
- **Scale above 50,000 workloads is unquantified (item 3.5):** published claims are qualitative or cluster-scoped (up to 25 K8s clusters per console); the authoritative Configuration Maximums page sits behind the login-gated support portal [3, 6].
- **Control-channel crypto and OT certifications undocumented (items 6.4, 8.2):** no staged source specifies TLS version or mutual authentication for Flow control channels, and no Siemens/Honeywell/ABB industrial certifications are documented.

## 6. Evidence Quality Notes

Ten of 33 items were triangulated across two or more source types, and 19 items rest on vendor documentation only (vendor_doc/vendor_datasheet/vendor_blog), which caps their confidence at medium per the project's validator rule. The seven high-confidence verdicts (1.1, 1.5, 2.1, 2.3, 3.2, 3.4, 7.3) all include at least one independent source: SiliconANGLE and The Register (sovereign cloud / air-gapped operation, DR policy preservation), AIMultiple (microsegmentation tool listing), and NIST CMVP registry entries (FIPS 140-2 modules for item 8.1). The StorageReview article is the sole evidence for the ServiceNow ITSM integration (5.3).

The official Nutanix support-portal documentation and Configuration Maximums page are login-gated and could not be staged, so the primary vendor documentation is the publicly accessible Nutanix Cloud Bible (based on PC/AOS 7.5) plus Nutanix.com product pages and the NCI 7.5 blog; this is noted in run_manifest.json assumptions. No contradictions between sources were found. Where sources were silent — 1.4 (CVE context), 2.2 (recommendations), 6.4 (TLS), 8.2 (OT certifications) — verdicts were left unknown rather than inferred as unsupported. The Common Criteria portal returned HTTP 403 during research, so the Common Criteria component of 8.1 remains unverified rather than asserted absent.

---

## Bibliography

[1] Nutanix, Inc.. "Nutanix Flow Solution Brief (PDF)". https://www.nutanix.com/content/dam/nutanix/en/resources/datasheets/ds-nutanix-flow.pdf (Retrieved: 2026-08-10T15:00:00Z)
[2] Nutanix, Inc.. "Nutanix Flow - Microsegmentation & Zero-Trust Security for Hybrid Clouds (product page)". https://www.nutanix.com/products/flow (Retrieved: 2026-08-10T15:00:00Z)
[3] Nutanix, Inc.. "Flow Network Security - Microsegmentation & Data Protection (product page)". https://www.nutanix.com/products/flow-network-security (Retrieved: 2026-08-10T15:00:00Z)
[4] Nutanix, Inc.. "Nutanix Cloud Infrastructure 7.5: Integrated Security is a Key Part of a Distributed Sovereign Cloud (blog)". https://www.nutanix.com/blog/nci-7-5-integrated-security-is-key-part-of-distributed-sovereign-cloud (Retrieved: 2026-08-10T15:00:00Z)
[5] Nutanix Cloud Bible. "The Nutanix Cloud Bible - Network Services (Flow architecture)". https://www.nutanixbible.com/12-book-of-network-services.html (Retrieved: 2026-08-10T15:00:00Z)
[6] Nutanix Cloud Bible. "The Nutanix Cloud Bible - Flow Network Security (FNS) chapter". https://www.nutanixbible.com/12a-book-of-network-services-flow-network-security.html (Retrieved: 2026-08-10T15:00:00Z)
[7] Nutanix Cloud Bible. "The Nutanix Cloud Bible - APIs chapter". https://www.nutanixbible.com/19-book-of-apis.html (Retrieved: 2026-08-10T15:00:00Z)
[8] Nutanix Cloud Bible. "The Nutanix Cloud Bible - REST APIs chapter". https://www.nutanixbible.com/19a-rest-apis.html (Retrieved: 2026-08-10T15:00:00Z)
[9] Nutanix Cloud Bible. "The Nutanix Cloud Bible - Prism Architecture chapter". https://www.nutanixbible.com/3a-book-of-prism-architecture.html (Retrieved: 2026-08-10T15:00:00Z)
[10] Nutanix, Inc.. "nutanix/terraform-provider-nutanix - official Terraform provider README". https://github.com/nutanix/terraform-provider-nutanix (Retrieved: 2026-08-10T15:00:00Z)
[11] NIST. "NIST CMVP Certificate #4364 - Nutanix Cryptographic Module for OpenSSH Client". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4364 (Retrieved: 2026-08-10T15:00:00Z)
[12] NIST. "NIST CMVP Certificate #4247 - Nutanix cryptographic module (FIPS 140-2, level 2)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4247 (Retrieved: 2026-08-10T15:00:00Z)
[13] SiliconANGLE. "Nutanix broadens sovereign cloud support (SiliconANGLE)". https://siliconangle.com/2025/12/17/nutanix-broadens-sovereign-cloud-support/ (Retrieved: 2026-08-10T15:00:00Z)
[14] The Register. "Nutanix pushes sovereign cloud in another swipe at VMware (The Register)". https://www.theregister.com/software/2025/12/15/nutanix-pushes-sovereign-cloud-in-another-swipe-at-vmware/1904846 (Retrieved: 2026-08-10T15:00:00Z)
[15] AIMultiple. "Top 10 Microsegmentation Tools in 2026 (AIMultiple)". https://www.aimultiple.com/microsegmentation-tools (Retrieved: 2026-08-10T15:00:00Z)
[16] StorageReview.com. "Nutanix Expands ServiceNow Integration (StorageReview)". https://www.storagereview.com/news/nutanix-expands-servicenow-integration (Retrieved: 2026-08-10T15:00:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 16 (kept: 16, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, third_party_review: 4, vendor_blog: 1, vendor_datasheet: 1, vendor_doc: 8
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
