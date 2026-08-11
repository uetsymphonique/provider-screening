# Microsegmentation Product Assessment: Cisco Systems - Cisco Secure Workload (Tetration)

**Product ID:** `cisco-secure-workload-tetration`
**Version reference:** Secure Workload 3.9 release docs, compatibility matrix and Secure Essentials hub captured 2026-08-10; CiscoDevNet Terraform/Ansible modules; 2018 Tufin partner brief for integrations
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T08:55:00Z
**Total evidence items collected:** 83
**Total distinct sources:** 18

---

## 1. Overview

Cisco Secure Workload (formerly Tetration) is Cisco's zero-trust microsegmentation platform for workloads across on-premises data centers, public cloud, and Kubernetes/OpenShift clusters, offered as a SaaS service or an on-premises hardware appliance [1], [7]. Cisco positions it around three use cases: agent- and agentless-based microsegmentation, vulnerability detection and protection, and behavioral (process-level) detection [11], [15]. Enforcement spans host OS firewalls (Windows Firewall, Linux iptables), DPUs, network firewalls via Secure Firewall/FMC, cloud security groups, and load balancers [11], [13]. Policies are defined from labels and workload context rather than IP/VLAN, with automatic ML-based policy discovery, policy analysis before enforcement, and hierarchical scopes [9], [10], [11]. The agent runs in userspace and is designed so application traffic continues if it fails [13]. Integration coverage includes Terraform, Ansible and Jenkins CI/CD, ServiceNow label synchronization, and IBM QRadar [3], [6], [7], [9], [14], [17]. Assessed against the 33-item checklist, 16 items are supported, 10 partial, and 7 unknown; the unknowns concentrate on numeric thresholds (agent CPU/RAM/latency, 90-day flow retention) and certifications (FIPS, Common Criteria, OT) that the staged documentation does not quantify.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 16    | 9                | 7      | 0   |
| partial          | 10    | 0                | 10     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 7     | 0                | 0      | 7   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 21 items backed by ≥ 2 source_types; 7 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Cisco documents real-time flow visibility from agents on workloads and Kubernetes nodes, and PeerSpot summarizes 100% unsampled telemetry coverage; the vendor blog quotes Forrester on excellent flow and asset discovery capabilities. [1], [5], [9], [14] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | medium | — | PeerSpot summarizes application dependency mapping that visualizes connections and interactions, and a Cisco doc describes a context-based topology/scope tree for grouping applications; a reviewer reports visibility into running processes and unused ports. [5], [10] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | — | no evidence found (No staged source quantifies flow-history retention; the >=90-day forensic retention requirement could not be verified.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | — | Cisco documents CVE risk scoring as part of visibility and policy creation, and the Kubernetes deep-dive describes CVE reports published in the UI; a PeerSpot reviewer notes the tool catalogs vulnerabilities and their locations on endpoints. [4], [5], [9] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | The firewall-integration whitepaper documents policy compliance monitoring with alerts and reports for deviation conditions, and the Kubernetes doc describes analyzing live traffic for unexpected allows or blocks; a reviewer describes monitoring escaped traffic that does not match policy. [5], [9], [11] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | — | Cisco documents workload discovery based on labels and dynamic policy objects built from workload metadata, and the compatibility matrix lists label context from external systems; a reviewer notes support for annotations. [3], [5], [9], [11] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | high | — | Cisco documents automatic policy discovery using machine-learning and behavioral algorithms on flow data plus AI/ML-driven automation; a PeerSpot reviewer highlights the system's strength in proposing policies. [4], [5], [11], [15] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | high | — | Cisco documents validating and testing policies without operational impact and policy analysis that does not require enforcement; a reviewer describes trying policies out in a real environment before switching to enforcement. [5], [9], [11] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found (No staged source documents an instant one-click policy rollback; policy versioning and cluster reset are mentioned but not a rollback workflow.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | high | — | Cisco documents a hierarchical policy engine with parent/child scopes and topology-based inheritance of policy; a reviewer lists hierarchical policies among valuable features. [5], [9], [10], [11] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | The compatibility matrix lists IBM AIX, Oracle Solaris, Linux distributions (RHEL, CentOS, Ubuntu and others) and Microsoft Windows as supported agent operating systems; Windows Server version ranges such as 2003 are not enumerated and a reviewer reports weaker AIX support. [3], [5], [12] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | high | — | The compatibility matrix lists Kubernetes 1.16-1.31/1.36 and Red Hat OpenShift 3.11/4.2-4.22 support, and the Kubernetes deep-dive documents flow visibility, iptables-based enforcement and container CVE scanning on those clusters; a reviewer reports evaluating it with Kubernetes. [3], [4], [5], [9] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | — | Cisco documents an agent and agentless approach with native firewall integration and DPU support, listing IPFIX/NetFlow/NSEL/ERSPAN telemetry and firewall or cloud-security-group enforcement; a reviewer describes agentless flow sensors in the network. [3], [4], [5], [13], [14] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | — | The product page documents an on-premises hardware appliance option, and a Cisco blog describes a logically air-gapped governance model integrating Secure Workload with Cilium/Isovalent; no source explicitly states fully disconnected (no-internet) operation. [1], [16] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Available sources give only qualitative scale language ('designed for scale and speed') and customer deployments in the 4,000-5,000 workload range; no documented figure at or above 50,000 workloads was found. [1], [5] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | — | no evidence found (No staged source quantifies agent CPU overhead; the <1% threshold could not be verified.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | The 3.9 release notes document a process-visibility/forensics memory quota limit of 512MB (raised from 256MB); the agent's baseline RAM footprint is not quantified, so the <100MB threshold cannot be confirmed. [12] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | — | no evidence found (No staged source quantifies added network latency; the <0.1ms threshold could not be verified.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | high | — | A Cisco blog states the agent runs in userspace so that if it fails the application continues to function normally, and a PeerSpot reviewer reports that enforced policies remain active when the platform is down. [5], [13] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | — | A Cisco blog documents a userspace agent and staged agent upgrades via configuration profiles; no source explicitly states that install or update never requires a reboot. [13] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | — | Cisco documents published APIs for automating security workflows, and the official Ansible and Terraform modules use API keys with administrative permissions (policy, sensor, user and scope management); the whitepaper notes the REST API used for FMC onboarding requires admin privileges. [6], [11], [14], [17] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | The official Secure Workload hub lists IBM QRadar among its integrations and tech alliances, and the compatibility matrix documents connectors that provide alert notification; Splunk/Sentinel and Syslog/CEF forwarding are not evidenced in staged sources. [3], [7] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | high | — | The compatibility matrix documents ServiceNow (New York and higher) integration with context/label capability, and a PeerSpot reviewer describes using ServiceNow for requests to modify policies. [3], [5] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | — | The Kubernetes doc's FAQ confirms policy provisioning from CI/CD pipelines via Terraform or Ansible providers, and the vendor blog cites Terraform, Ansible and Jenkins integration; official CiscoDevNet Terraform and Ansible modules exist for the product. [6], [9], [14], [17] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | medium | — | Cisco documents segmentation down to the process level and runtime process-level activity (MITRE TTPs); a reviewer describes identifying running processes and unused ports to secure servers. [5], [9], [14] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Cisco documents integrated threat intelligence for blocking malicious-IP traffic and behavioral anomaly detection using MITRE ATT&CK; honeypot/deception capabilities were not found in staged sources. [4], [14], [15] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | A Cisco blog documents mapping DORA/NIS2 requirements to NIST CSF 2.0 with Secure Workload, and docs describe continuous policy-compliance monitoring with alerts and reports; no staged source shows out-of-the-box PCI-DSS, ISO 27001, IEC 62443 or NIST 800-207 report templates. [4], [11], [15] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Unknown | low | — | no evidence found (No staged source describes agent-to-controller transport security (e.g., TLS 1.3 or mutual authentication).) |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | — | The product page claims high availability for both SaaS and on-premises, and the 3.9 release notes document automated failover for the Hadoop Namenode VM; a 2021 reviewer reported the cluster cannot be deployed geo-redundantly, and no active-active/active-passive detail was found. [1], [5], [12] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | — | A PeerSpot reviewer (MUFG) reports that when the Tetration platform goes down the enforced policies remain active and only the ability to push changes or updates is affected. [5] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | The 3.9 release notes document data backup and restore (DBR) with dual-stack support and migration workflows; no evidence of DR-site replication/sync was found, and a 2021 reviewer reported no data-lake backup option. [5], [12] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No staged source shows FIPS 140-2/140-3 or Common Criteria EAL4+ validation for Secure Workload; the NIST CMVP listing does not include a Secure Workload module.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No staged source shows industrial software compatibility certifications (Siemens, Honeywell, ABB) for OT environments.) |

---

## 4. Notable Strengths

- **Real-time visibility and flow discovery (items 1.1, 1.2):** Agents provide real-time, unsampled flow visibility with dependency mapping and scope-based topology for grouping workloads by application context [5], [9], [14].
- **Label-based policy engine with ML recommendation and analysis (items 2.1, 2.2, 2.3):** Policies are built on labels/annotations, policies are auto-discovered with ML, and they can be validated against live traffic before any enforcement [9], [11], [15].
- **Agent plus agentless enforcement breadth (items 3.2, 3.3):** Kubernetes/OpenShift enforcement via iptables, host firewalls, Secure Firewall, cloud security groups and DPUs are managed through one policy model [3], [4], [11], [13].
- **Fail-safe agent design (item 4.4):** The userspace agent keeps application traffic flowing if the agent fails, and enforced policies remain active during platform outages [5], [13].
- **Automation and integrations (items 5.1, 5.3, 5.4):** A REST API with administrative permissions, official Terraform/Ansible modules and Jenkins support for CI/CD, and ServiceNow label synchronization [3], [6], [9], [17].

## 5. Notable Gaps / Risks

- **Flow-retention duration undocumented (item 1.3):** No staged source confirms the >=90-day connection-history retention needed for forensic tracing; the official user guide would resolve this.
- **Agent resource thresholds unquantified (items 4.1, 4.2):** No CPU overhead figure is documented and the process-visibility memory quota is 512MB, so the <1% CPU and <100MB RAM requirements are unverified (4.2 partial, 4.1 unknown).
- **No one-click policy rollback evidence (item 2.4):** Policy versioning exists but an instant rollback workflow is not documented; confirmation from the admin guide is needed.
- **Agent-controller transport security undocumented in staged sources (item 6.4):** TLS 1.3 or mutual authentication between agent and controller could not be verified; this screen-gate item should be confirmed before procurement.
- **Certification coverage unverified (items 8.1, 8.2):** No FIPS 140-2/140-3, Common Criteria EAL4+, or Siemens/Honeywell/ABB OT compatibility certifications were found; the buyer should request validation certificates directly.

## 6. Evidence Quality Notes

Evidence was collected from 18 staged sources: 10 vendor docs, 5 vendor blogs, 1 community source (PeerSpot), 1 third-party brief (Tufin), and 1 product release notes page; all 83 evidence quotes were verified as exact substrings of the staged text (grounding check: 83 grounded, 0 fabricated, 0 unverifiable). 26 of 33 items have evidence and 7 are unknown. 21 items are backed by 2+ source types; 8 items (3.4, 4.2, 4.5, 5.1, 5.2, 5.4, 6.2, 6.3) draw only on vendor-authored material, which caps their confidence at medium per the validator rule.

The main limitation was source access: Cisco's primary documentation host (www.cisco.com/c/en/us/td/docs/...) returned HTTP 403 and the Wayback Machine returned HTTP 429 throughout the session, so the full Secure Workload admin/user guide could not be staged. The accessible Secure Essentials docs hub (secure.cisco.com) plus product pages, blogs, and CiscoDevNet repos were used instead. Two contradictions were resolved conservatively: a 2021 PeerSpot review reported no geo-redundant cluster and no data-lake backup, while 3.9 release notes document automated Namenode failover and data backup/restore, so items 7.1 and 7.3 are rated partial; and a reviewer described IBM AIX support as weaker than other OSes, contributing to the partial verdict on item 3.1. PeerSpot is community evidence, so the item resting on it alone (7.2) is capped at medium confidence.

---

## Bibliography

[1] Cisco Systems. "Cisco Secure Workload product page (zero trust microsegmentation)". https://www.cisco.com/site/us/en/products/security/secure-workload/index.html (Retrieved: 2026-08-10T08:50:30Z)
[2] Cisco Systems. "Cisco Secure Workload resources page". https://www.cisco.com/site/us/en/products/security/secure-workload/resources.html (Retrieved: 2026-08-10T08:50:30Z)
[3] Cisco Systems. "Cisco Secure Workload Compatibility Matrix". https://www.cisco.com/c/m/en_us/products/security/secure-workload-compatibility-matrix.html (Retrieved: 2026-08-10T08:50:30Z)
[4] Cisco Blogs. "Cisco Secure Workload 3.9 Delivers Stronger Security and Greater Operational Efficiency". https://blogs.cisco.com/security/cisco-secure-workload-3-9-delivers-stronger-security-and-greater-operational-efficiency (Retrieved: 2026-08-10T08:50:30Z)
[5] PeerSpot. "Cisco Secure Workload reviews (PeerSpot, 15 reviews)". https://www.peerspot.com/products/cisco-secure-workload-reviews (Retrieved: 2026-08-10T08:50:30Z)
[6] CiscoDevNet (GitHub). "CiscoDevNet terraform-provider-tetration (GitHub) - Terraform Provider for Cisco Secure Workload (Tetration)". https://github.com/CiscoDevNet/terraform-provider-tetration (Retrieved: 2026-08-10T08:50:30Z)
[7] Cisco Systems. "Cisco Secure Essentials - Cisco Secure Workload hub (Integrations & Tech Alliances)". https://secure.cisco.com/secure-workload (Retrieved: 2026-08-10T08:50:30Z)
[8] Cisco Systems. "Secure Workload and Secure Firewall - Overview (Cisco Secure Workload docs)". https://secure.cisco.com/secure-workload/docs (Retrieved: 2026-08-10T08:50:30Z)
[9] Cisco Systems. "Secure Workload and Kubernetes Security - Deep Dive (Cisco Secure Workload docs)". https://secure.cisco.com/secure-workload/docs/secure-workload-and-k8s (Retrieved: 2026-08-10T08:50:30Z)
[10] Cisco Systems. "Secure Workload - Importance of Topology Awareness (Cisco Secure Workload docs)". https://secure.cisco.com/secure-workload/docs/secure-workload-compliance (Retrieved: 2026-08-10T08:50:30Z)
[11] Cisco Systems. "Secure Workload - Deep Dive of Secure Workload & Firewall Integration (whitepaper)". https://secure.cisco.com/secure-workload/docs/secure-workload-whitepaper (Retrieved: 2026-08-10T08:50:30Z)
[12] Cisco Systems. "What to Expect with Cisco Secure Workload version 3.9 (release notes/changelog)". https://secure.cisco.com/secure-workload/docs/what-to-expect-with-cisco-secure-workload-version-39 (Retrieved: 2026-08-10T08:50:30Z)
[13] Cisco Blogs. "Building a Resilient Network and Workload Security Architecture from the Ground Up". https://blogs.cisco.com/security/building-a-resilient-network-and-workload-security-architecture-from-the-ground-up (Retrieved: 2026-08-10T08:50:30Z)
[14] Cisco Blogs. "Forrester Named Cisco Leader in 2024 Microsegmentation Wave (Cisco blog citing Forrester Wave Q3 2024)". https://blogs.cisco.com/security/forrester-named-cisco-a-leader-in-the-2024-microsegmentation-wave (Retrieved: 2026-08-10T08:50:30Z)
[15] Cisco Blogs. "Streamline Regulation With NIST CSF & Secure Workload". https://blogs.cisco.com/security/streamline-regulation-mandates-with-nist-csf-and-secure-workload (Retrieved: 2026-08-10T08:50:30Z)
[16] Cisco Blogs. "The Journey towards Logically Air-Gapped Deployment". https://blogs.cisco.com/security/the-journey-towards-logically-air-gapped-deployment (Retrieved: 2026-08-10T08:50:30Z)
[17] CiscoDevNet (GitHub). "CiscoDevNet ansible-secure-workload (GitHub) - Secure Workload (Tetration) Ansible Module". https://github.com/CiscoDevNet/ansible-secure-workload (Retrieved: 2026-08-10T08:50:30Z)
[18] Tufin. "Cisco Tetration Analytics & Tufin Orchestration Suite Solution Brief (PDF)". https://lp.tufin.com/rs/769-ICF-145/images/cisco-tetration-analytics-tufin-solution-brief.pdf (Retrieved: 2026-08-10T08:50:30Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 18 (kept: 18, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, product_release_notes: 1, third_party_review: 1, vendor_blog: 5, vendor_doc: 10
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
