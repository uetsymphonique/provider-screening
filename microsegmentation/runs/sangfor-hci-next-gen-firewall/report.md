# Microsegmentation Product Assessment: Sangfor Technologies - Sangfor HCI / Next-Gen Firewall (Athena NGFW)

**Product ID:** `sangfor-hci-next-gen-firewall`
**Version reference:** HCI 6.x / aSV hypervisor line and Athena NGFW (formerly Network Secure / NGAF) 8.0.x; staged sources are 2026 product materials
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T18:00:00Z
**Total evidence items collected:** 45
**Total distinct sources:** 15

---

## 1. Overview

Sangfor Technologies positions its microsegmentation capability inside the virtualization platform: Sangfor HCI (aSV hypervisor) and Sangfor Cloud Platform (SCP) ship a hypervisor-native distributed firewall (DFW) with aNI network-traffic/access visualization, identity-based policy objects (VM labels/groups), intelligent policy generation from historical traffic data stored in a Druid time-series database, and pre-enforcement (monitor-only) rule validation [4]. Deployments are agentless — the DFW is enabled on distributed-switch ports without plug-in installation — and extend to containers through Sangfor Kubernetes Engine (SKE), which integrates Kubernetes clusters into HCI/SCP and applies DFW policies to cluster nodes [4, 6]. The Athena NGFW (formerly Network Secure/NGAF) covers the perimeter with AI-based detection, Neural-X cloud threat intelligence, NGWAF and SOC Lite [2]. Supported deployment shapes are on-premises HCI clusters (a reported 48-node cluster [10]) with snapshot/CDP/stretched-cluster DR [1].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 7     | 0                | 7      | 0   |
| partial          | 10    | 0                | 10     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 11    | 0                | 0      | 11  |
| not_applicable   | 5     | 0                | 5      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 18 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** Microsegmentation is enforced natively in the type-1 KVM hypervisor data plane with no endpoint agent, so the agent CPU-overhead metric does not apply.
- **4.2:** No endpoint agent exists in the virtualization-native architecture, so the agent RAM-footprint metric does not apply.
- **4.4:** Because enforcement is hypervisor-native rather than via an endpoint agent, the agent-crash fail-safe scenario does not apply to this architecture.
- **4.5:** No endpoint agent is installed (hypervisor-native DFW), so agent install/update reboot requirements do not apply.
- **6.1:** The distributed firewall is documented as providing Layer 3-4 protection for east-west traffic, which rules out process-level (L7) enforcement.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | — | The aNI collector samples business access traffic 100% out-of-band and stores analyzed access relationships in a time-series database with real-time ingestion; the HCI dashboard shows real-time flows and aSV lists VM-level east-west traffic control with policy auto-generation. [1], [4], [5] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Traffic and access-relationship visualization (application topology views) is documented, including access relationships for cloud-native applications in SKE; environment/role/process-level views are not documented. [4], [6] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | 30 days | The aNI time-series database supports queries across 30 days of access data per the vendor blog, below the 90-day forensic-retention requirement; longer retention is not documented. [4] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | — | no evidence found (No staged source shows vulnerability/CVE context rendered on the traffic map; aSV mentions aSEC vulnerability management but not map display.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | — | Firewall rule-intent validation flags traffic that does not comply with policy and helps isolate abnormal traffic, and blast-radius identification is documented; an explicit 'unrecognized traffic' flag is not named. [4] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | DFW policy objects can reference VMs, VM groups and VM labels, with VM groups/labels serving as application identity attributes, so policies are not limited to IP/VLAN. [4] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | — | The microsegmentation service generates DFW rules from historical access relationships stored by aNI in a Druid database and presents a rule preview for administrator modification; aSV lists policy auto-generation. [4], [5] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | — | DFW rules can be placed in pre-enforcement where they only match and log; flows that would be denied by staged rules are highlighted as potential unintended blocks without interrupting production traffic. [4] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found (No staged source mentions one-click policy rollback.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No staged source mentions inherited/hierarchical policy rules.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | The HCI compatibility chart lists Microsoft Windows and RHEL/CentOS/Ubuntu-lineage Linux guest OS families; a PeerSpot reviewer reports the hypervisor supports fewer OS variants than ESXi/Hyper-V, and AIX/Solaris are not listed. [7], [10] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | — | SKE provides Kubernetes-based container management integrated into HCI and managed by SCP, and automatically applies distributed-firewall policies to cluster nodes for port whitelisting/blocking. [6] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | The DFW is deployed natively in the virtualization platform without plug-in installation (agentless path documented); an agent-based deployment option is not evidenced. [4] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | — | no evidence found (No staged source describes air-gapped/offline deployment.) |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Reviewers describe Sangfor HCI as highly scalable (e.g., a 48-node cluster deployment and 200+ VMs per customer), but no source quantifies workload capacity up to 50,000 VMs. [10] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | Microsegmentation is enforced natively in the type-1 KVM hypervisor data plane with no endpoint agent, so the agent CPU-overhead metric does not apply. [4], [5] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No endpoint agent exists in the virtualization-native architecture, so the agent RAM-footprint metric does not apply. [5] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | The vendor describes 100% traffic sampling with 'virtually no loss' of forwarding performance and out-of-band export with minimal impact, but no numeric latency figure is provided. [4] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | Because enforcement is hypervisor-native rather than via an endpoint agent, the agent-crash fail-safe scenario does not apply to this architecture. [4] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No endpoint agent is installed (hypervisor-native DFW), so agent install/update reboot requirements do not apply. [4], [5] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | Sangfor Cloud Platform publishes an OPEN API documentation category with API-key generation, and Athena NGFW ships an API User Manual; whether the API covers 100% of administrative functions is not verifiable from staged sources. [11], [14] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | An independent SIEM vendor documents syslog forwarding from Sangfor NGFW/NGAF devices to EventLog Analyzer; named Splunk/QRadar/Sentinel connectors are not evidenced. [8] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found (No staged source mentions CMDB (ServiceNow) integration for tag synchronization.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found (No staged source mentions CI/CD pipeline integration for DevSecOps.) |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | N/A | medium | — | The distributed firewall is documented as providing Layer 3-4 protection for east-west traffic, which rules out process-level (L7) enforcement. [4] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Neural-X cloud threat intelligence (IOC feeds from 20,000+ gateways) is documented as connectable to Sangfor security products including Athena NGFW; honeypot/deception detection is not evidenced. [2], [9] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Unknown | low | — | no evidence found (No staged source documents built-in compliance reports (PCI-DSS / NIST 800-207 / ISO 27001 / IEC 62443).) |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Unknown | low | — | no evidence found (No staged source documents TLS/mutual-auth specifics for a control channel; the architecture has no endpoint agent-controller pair.) |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | SCP documentation includes a failover-cluster deploy guide, and HCI provides HA mechanisms (sub-health monitoring, DRS, live migration); a PeerSpot reviewer reports excellent stability. Specific active-active/active-passive mode terminology is not used. [5], [6], [10], [14] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (No staged source documents hosts continuing to enforce policy if the controller is fully unreachable.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | — | The HCI page documents disaster recovery via snapshot, CDP and stretched cluster, and the Reliability Configuration Guide includes VM disaster-recovery and backup sections. [1], [12] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No staged source evidences FIPS 140-2/140-3 or Common Criteria EAL4+ certification; the vendor claims ICSA Labs (2021) and CyberRatings ratings instead, which are not FIPS/CC.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No staged source evidences Siemens/Honeywell/ABB industrial compatibility certifications.) |

---

## 4. Notable Strengths

- **Hypervisor-native, agentless microsegmentation (items 3.3, 4.1, 4.2, 4.4):** the DFW is deployed natively in the virtualization platform without plug-in installation, so there is no endpoint agent to impose CPU/RAM overhead or fail-safe behavior [4, 5].
- **Identity-based policy with intelligent generation and dry-run (items 2.1, 2.2, 2.3):** policy objects support VM labels/groups as application identity, rules are auto-generated from historical access relationships in the aNI/Druid database, and pre-enforcement lets administrators validate rules in monitor-only mode before activation [4].
- **Kubernetes isolation out of the box (item 3.2):** SKE integrates Kubernetes clusters into HCI/SCP and automatically applies distributed-firewall policies to cluster nodes, blocking high-risk ports and whitelisting required ones [6].
- **Real-time traffic visibility with 100% sampling (items 1.1, 1.2):** the aNI collector samples business access traffic out-of-band with 100% sampling at virtually no forwarding-performance loss and visualizes access relationships and application topology [4].
- **Controller-plane HA and DR (items 7.1, 7.3):** SCP ships a failover-cluster deploy guide and HCI provides HA mechanisms (sub-health monitoring, DRS, live migration) plus snapshot, CDP and stretched-cluster disaster recovery [14, 5, 6, 12, 1].

## 5. Notable Gaps / Risks

- **Process-level enforcement not supported (item 6.1):** the DFW is documented as Layer 3–4 only, ruling out process-level (L7) enforcement; buyers needing per-process east-west control should verify roadmap or use an endpoint agent product [4].
- **Flow-history retention below 90 days (item 1.3):** the only documented figure is a 30-day query horizon for aNI access data; forensic tracing beyond 30 days is not evidenced [4].
- **Thin third-party evidence (items 1.1–2.3, 6.1–6.2):** most microsegmentation capability claims rest on a single vendor blog and the aSV/SKE product pages, with no analyst or independent-lab coverage of the DFW; confidence stays at medium [4, 5, 6].
- **Unknown automation surface (items 5.1, 5.3, 5.4):** an OPEN API and NGFW API manual exist, but 100%-of-admin-functions coverage, ServiceNow CMDB sync and CI/CD pipeline integration are unverified [14, 11].
- **No compliance-report or certification evidence (items 6.3, 8.1, 8.2):** built-in PCI-DSS/NIST 800-207/ISO 27001/IEC 62443 reports, FIPS 140/Common Criteria and Siemens/Honeywell/ABB certifications are all undocumented in staged sources.

## 6. Evidence Quality Notes

Seven items (1.1, 2.2, 3.1, 3.5, 4.1, 7.1, 5.2) draw on more than one source type; the rest of the non-unknown items rely on a single vendor-authored source (mostly the Sangfor microsegmentation blog), capping confidence at medium under the validator rule. Only two independent sources were staggable: ManageEngine's EventLog Analyzer help page documenting syslog forwarding from Sangfor NGAF devices (item 5.2) and PeerSpot user reviews (items 3.1, 3.5, 7.1); no analyst report, independent lab test or peer-reviewed source covering the DFW could be fetched — Gartner, G2 and CyberRatings pages are bot-gated, and the CyberRatings Sangfor report references are vendor-claimed on the NGFW page rather than independently staged.

One explicit contradiction was found: a PeerSpot reviewer reports the Sangfor hypervisor is "not mature enough" for all OS flavors versus ESXi/Hyper-V, while the vendor compatibility chart lists a broad Microsoft/Linux OS family — item 3.1 is rated partial to reflect both. All 45 evidence quotes are verbatim substrings of 15 staged artifacts (manifest sha256-anchored); a routing fix was needed in verify_citation_grounding.py because support.sangfor.com document URLs differ only by query string and previously collapsed onto one staged text.

---

## Bibliography

[1] Sangfor Technologies. "Sangfor HCI - Hyperconverged Infrastructure (product page)". https://www.sangfor.com/cloud-and-infrastructure/products/hci-hyper-converged-infrastructure (Retrieved: 2026-08-10T18:00:00Z)
[2] Sangfor Technologies. "Athena Next-Generation Firewall (NGFW) - product page". https://www.sangfor.com/cybersecurity/sangfor-athena-foundation/next-generation-firewall-ngfw (Retrieved: 2026-08-10T18:00:00Z)
[3] Sangfor Technologies. "Sangfor Cloud Platform (SCP) - product page". https://www.sangfor.com/cloud-and-infrastructure/products/sangfor-cloud-platform (Retrieved: 2026-08-10T18:00:00Z)
[4] Sangfor Technologies. "Strengthening Cloud Security with Intelligent Microsegmentation (Sangfor blog)". https://www.sangfor.com/blog/cloud-and-infrastructure/vmware-replacement-intelligent-microsegmentation-cloud-security (Retrieved: 2026-08-10T18:00:00Z)
[5] Sangfor Technologies. "Sangfor aSV - Hypervisor (product page)". https://www.sangfor.com/cloud-and-infrastructure/products/asv-hypervisor-server-virtualization (Retrieved: 2026-08-10T18:00:00Z)
[6] Sangfor Technologies. "Sangfor Kubernetes Engine (SKE) - product page". https://www.sangfor.com/cloud-and-infrastructure/products/sangfor-kubernetes-engine-ske (Retrieved: 2026-08-10T18:00:00Z)
[7] Sangfor Technologies. "HCI Compatibility Chart". https://www.sangfor.com/cloud-and-infrastructure/products/hci-compatibility-chart (Retrieved: 2026-08-10T18:00:00Z)
[8] ManageEngine / Zoho. "Configuring the Syslog Service on Sangfor devices (EventLog Analyzer help)". https://www.manageengine.com/products/eventlog/help/StandaloneManagedServer-UserGuide/ConfiguringSyslogService/configuring-the-syslog-service-on-sangfor-devices.html (Retrieved: 2026-08-10T18:00:00Z)
[9] Sangfor Technologies. "Sangfor Threat Intelligence (Neural-X) - page". https://www.sangfor.com/cybersecurity/innovations/threat-intelligence (Retrieved: 2026-08-10T18:00:00Z)
[10] PeerSpot (IT Central Station). "Sangfor HCI - Hyper Converged Infrastructure Reviews (PeerSpot)". https://www.peerspot.com/products/sangfor-hci-hyper-converged-infrastructure-reviews (Retrieved: 2026-08-10T18:00:00Z)
[11] Sangfor Technologies. "Athena NGFW - SDKs, APIs documentation (Sangfor Technical Support)". https://support.sangfor.com/productDocument/read?product_id=21&version_id=1090&category_id=2640635 (Retrieved: 2026-08-10T18:00:00Z)
[12] Sangfor Technologies. "HCI/aSV Reliability Configuration Guide (Sangfor Technical Support)". https://support.sangfor.com/productDocument/read?product_id=10&version_id=1229&category_id=2639659 (Retrieved: 2026-08-10T18:00:00Z)
[13] Sangfor Technologies. "Athena NGFW Datasheet NSF-1200A-I (Scribd copy)". https://www.scribd.com/document/1055093721/Athena-NGFW-Datasheet-NSF-1200A-I-20260505 (Retrieved: 2026-08-10T18:00:00Z)
[14] Sangfor Technologies. "Sangfor Cloud Platform (SCP) - OPEN API documentation (Sangfor Technical Support)". https://support.sangfor.com/productDocument/read?product_id=45&doc_type=2&category_id=2632134 (Retrieved: 2026-08-10T18:00:00Z)
[15] Sangfor Technologies. "HCI/aSV Network Insight documentation (Sangfor Technical Support)". https://support.sangfor.com/productDocument/read?product_id=10&version_id=1229&category_id=2639694 (Retrieved: 2026-08-10T18:00:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 16
- **Sources reviewed:** 15 (kept: 15, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, third_party_review: 1, vendor_blog: 1, vendor_datasheet: 1, vendor_doc: 11
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
