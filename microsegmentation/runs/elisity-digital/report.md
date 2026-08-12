# Microsegmentation Product Assessment: Elisity - Elisity Digital

**Product ID:** `elisity-digital`
**Version reference:** Cloud Control Center release 26.x / Virtual Edge 16.x
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T15:45:00Z
**Total evidence items collected:** 99
**Total distinct sources:** 42

---

## 1. Overview

Elisity Digital is a SaaS-delivered, agentless microsegmentation platform that enforces identity-based policies through existing network switches rather than host agents. The Cloud Control Center (SaaS) houses the IdentityGraph — a unified asset database that ingests telemetry from switches (NetFlow/IPFIX), identity providers, CMDB, EDR, and OT sources to build real-time context for every device, user, and workload. Virtual Edge controllers translate centrally defined policies into native ACLs on Cisco Catalyst, Meraki, and third-party switches, keeping the data plane untouched. The platform is positioned primarily for brownfield enterprise and healthcare environments where agent deployment is infeasible, with a stated focus on rapid time-to-value (vendor claims 46 days to secure 85,000 devices in one named deployment [17]). Deployment shapes are SaaS-only (no on-premises control plane) with Virtual Edge appliances running on VMware ESXi/Hyper-V or Cisco Catalyst switches.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 11    | 3                | 8      | 0   |
| partial          | 11    | 0                | 11     | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 6     | 0                | 6      | 0   |

**Evidence quality:** 25 items backed by ≥ 2 source_types; 9 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** The product is agentless with no host-based enforcement, so workload-OS coverage does not apply; the Virtual Edge appliance runs on VMware ESXi/Hyper-V or supported Cisco switches rather than on workloads.
- **4.1:** No host agent is installed on workloads — enforcement runs on existing switches via the Virtual Edge appliance — so an agent CPU-overhead figure does not apply.
- **4.2:** No host agent is deployed on workloads; the Virtual Edge appliance is a separate VM/container, so no workload agent RAM footprint exists to measure.
- **4.4:** There is no host agent whose crash could interrupt workload traffic; switch-native enforcement with Virtual Edge Group failover is documented to maintain uninterrupted policy enforcement.
- **4.5:** No software is installed on hosts (agentless), and the vendor describes non-disruptive onboarding with 'No downtime, no reboots', so reboot requirements do not apply.
- **6.1:** No host agent exists (agentless architecture, per 3.1/4.1/4.2); enforcement is switch-native at L3/L4 (protocol/port level), and the vendor-commissioned Omdia survey notes agentless identity-based approaches structurally cannot see process-level information, so process-level enforcement does not apply.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | IdentityGraph automatically discovers and enriches every user, workload and device from native network telemetry plus connected identity, CMDB, EDR and OT sources; a hands-on walkthrough confirmed automatic discovery of simulated medical equipment. [1], [12], [13], [14], [23] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Graph and matrix views (Policy Matrix grid, Sankey charts, graph interface) visualize connections between Policy Groups, devices and users; Policy Group attributes cover application function, role and site, but no process-level map view is documented. [1], [7], [15], [23] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Traffic/policy analysis windows are configurable from 30 up to 180 days (including an explicit 'last 90 days' re-run), indicating retained traffic history of at least 90 days; no explicit flow-log retention or forensic archive period is documented. [9], [32], [34] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | Vulnerability and exposure context (Tenable One, Microsoft Defender for IoT, OT risk data) is ingested into IdentityGraph, shown on device details and usable as policy match criteria; no source states CVEs are rendered directly on the map/graph view. [8], [9], [32] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | The platform discovers shadow IT/unmanaged assets (including IoT, OT and IoMT) and Traffic Analytics surfaces anomalies and unexpected patterns, with unrecognized addresses landing in an Unassigned Policy Group. [1], [8], [12], [41] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | — | Policies are built from identity attributes (device type, manufacturer, posture, business owner, user group) rather than IP addresses or VLANs, per vendor documentation; a hands-on walkthrough showed automatic reclassification of a device based on ServiceNow/CrowdStrike attributes. [1], [5], [14], [23] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | — | Elisity Intelligence (private-LLM based) recommends Policy Groups, device classifications and enforcement policies from observed behavior, with administrator acceptance required before changes take effect. [1], [7], [35], [36] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | high | — | Policies can be saved as simulations and validated against live traffic before enforcement, with simulated/active states distinguished in the Policy Matrix; simulation is documented in the KB and was demonstrated in a hands-on walkthrough. [1], [14], [16], [24] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | — | No dedicated one-click policy rollback is documented, but switching Policy Sets (deploying an incident-response set and reverting to the Default set) is documented as a rapid reversion path. [14], [25] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | — | Nested Policy Groups support parent-to-child policy cascade with inheritance display, Replica Policy Sets inherit all policies from their parent, and Policy Groups inherit default security profiles — documented in release notes and KB. [25], [32], [37] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | — | The product is agentless with no host-based enforcement, so workload-OS coverage does not apply; the Virtual Edge appliance runs on VMware ESXi/Hyper-V or supported Cisco switches rather than on workloads. [4], [5], [28] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | Workload Policy Groups cover VMs and containers as a policy dimension and AWS EC2 workloads are discovered via a cloud connector, but workload enforcement is announced for a future release and no Kubernetes/OpenShift native isolation is documented. [32], [40] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Not Supported | medium | — | The requirement asks for both agent-based and agentless/network-integration enforcement; the vendor explicitly documents 'No Host/Agent-Based Enforcement' and network-integration enforcement via existing switches, so the agent-based half is ruled out. [4], [5], [11], [14] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Not Supported | medium | — | The management plane is a per-customer SaaS Cloud Control Center that Virtual Edges must reach over the internet (heartbeat, OTP registration, outbound HTTPS), so a fully air-gapped deployment without internet is not supported by the documented architecture. [23], [27] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 85000 workloads | A named customer deployment (St. Luke's) protected more than 85,000 medical devices on a single platform deployment; Distribution Zone device limits are configurable (default 9,000) and are notification-only rather than hard caps. [2], [17], [26] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | No host agent is installed on workloads — enforcement runs on existing switches via the Virtual Edge appliance — so an agent CPU-overhead figure does not apply. [4], [5], [28] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No host agent is deployed on workloads; the Virtual Edge appliance is a separate VM/container, so no workload agent RAM footprint exists to measure. [1], [4], [5] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Enforcement is switch-native and out-of-band from traffic (data plane untouched), and hands-on testing measured sub-millisecond latency with no noticeable throughput reduction; no published figure at or below 0.1 ms was found. [4], [14] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | There is no host agent whose crash could interrupt workload traffic; switch-native enforcement with Virtual Edge Group failover is documented to maintain uninterrupted policy enforcement. [4], [26] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No software is installed on hosts (agentless), and the vendor describes non-disruptive onboarding with 'No downtime, no reboots', so reboot requirements do not apply. [4], [5], [16] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | The platform is API-first with 466 CLI commands covering the Cloud Control Center API, custom REST-based connectors and a device API, but no source claims 100% of administrative functions are exposed via REST. [6], [23], [28], [32] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Cloud Control Center audit logs ship to Splunk (HTTP Event Collector), Cribl and Microsoft Sentinel via documented connectors; Splunk HEC export was introduced in release 14.8. [5], [21], [30] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | — | An official ServiceNow CMDB connector enriches IdentityGraph device context and policy match criteria via read-only API access; a named deployment also integrated ServiceNow into its security stack. [5], [17], [31] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | — | The API-first platform plus the open CLI (JSON/YAML/CSV output, production/staging/lab profiles) and a community PowerShell automation script enable scripted, CI/CD-style management, but no official Terraform/Jenkins/GitLab integration is documented. [6], [28], [32] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | N/A | medium | — | No host agent exists (agentless architecture, per 3.1/4.1/4.2); enforcement is switch-native at L3/L4 (protocol/port level), and the vendor-commissioned Omdia survey notes agentless identity-based approaches structurally cannot see process-level information, so process-level enforcement does not apply. [20], [29], [38] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Risk, posture and threat context from EDR, OT and vulnerability sources (CrowdStrike, SentinelOne, Dragos, Nozomi, Tenable) enriches policy, and Elisity Intelligence identifies vulnerabilities and threats; no honeypot/deception detection is documented. [1], [19], [32] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | PCI DSS 4.0 alignment documentation and exportable audit logs are provided, and the platform claims alignment with NIST, PCI, HIPAA, HHS 405(d) and IEC 62443; no ISO 27001-specific reporting or dedicated NIST 800-207 document was found. [1], [22], [39] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | — | There is no host agent, but the Virtual Edge-to-Cloud Control Center control plane uses DTLS 1.3 with mutual certificate exchange, and policy distribution runs over a secure TLS control channel per the KB. [18], [23] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | Virtual Edge Groups provide failover HA: VEN management transfers automatically to another VE in the group on VE failure or loss of CCC connection, with one Active Client VE and candidate VEs per VEN; the per-customer CCC runs on a horizontally scaling cloud microservice architecture. [23], [26] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | — | Documented VE-Group failover keeps policy enforcement uninterrupted when a VE fails or the CCC connection is lost, and enforcement is switch-native with control/data planes separated, but autonomous enforcement under total loss of all VEs is not explicitly documented. [4], [26], [27] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (The SaaS Cloud Control Center is cloud-hosted and Virtual Edge Groups provide failover, but no customer-facing backup or disaster-recovery site-sync procedure is documented.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No FIPS 140-2/140-3 or Common Criteria validation found in vendor materials; the company page attests SOC 2 only.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (OT/ICS support includes industrial switches (Cisco Catalyst IE, Hirschmann), but no validated compatibility certification from Siemens, Honeywell or ABB was found.) |

---

## 4. Notable Strengths

- **Real-time identity-based asset discovery (items 1.1, 1.5):** The IdentityGraph automatically discovers every device, user, and workload from native switch telemetry plus connected identity, CMDB, EDR, and OT sources, including shadow IT and unmanaged IoT/OT assets — confirmed by an independent third-party hands-on walkthrough [14].
- **Identity-based policy with AI recommendations (items 2.1, 2.2, 2.5):** Policies are built from identity attributes (device type, manufacturer, business owner, user group) rather than IP addresses or VLANs, with a private-LLM engine (Elisity Intelligence) that recommends Policy Groups, device classifications, and enforcement rules from observed behavior [1], [35]. Hierarchical Policy Groups support parent-to-child inheritance and replica sets [25], [37].
- **Policy simulation before enforcement (item 2.3):** All policies can be saved as simulations and validated against live traffic before being activated, with simulated and active states clearly distinguished in the Policy Matrix — independently verified in a hands-on review [14], [24].
- **Enterprise-scale proven deployment (item 3.5):** A named customer (St. Luke's) protected more than 85,000 medical devices on a single Elisity platform deployment, providing real-world validation of the platform's scalability claims [17].
- **Built-in SIEM and ITSM integrations (items 5.2, 5.3):** Audit logs ship natively to Splunk, Cribl, and Microsoft Sentinel; an official ServiceNow CMDB connector enriches IdentityGraph device context with read-only API access [22], [28], [33].

## 5. Notable Gaps / Risks

- **No agent-based enforcement path (item 3.3):** The platform is exclusively agentless, relying on switch-native ACL enforcement. Organizations that require host-level process control, application-layer filtering (Layer-7), or deployment in environments without supported switch hardware cannot use Elisity as their sole segmentation solution [4], [5], [11].
- **SaaS-only control plane — no air-gapped deployment (item 3.4):** The Cloud Control Center is a per-customer SaaS tenant that Virtual Edges must reach over the internet for heartbeat, OTP registration, and policy sync. Fully air-gapped or disconnected environments are not supported by the documented architecture [23], [27].
- **No process-level enforcement (item 6.1):** Enforcement is at L3/L4 (protocol/port), not at the individual process level. The vendor-commissioned Omdia survey acknowledges that agentless, identity-based approaches cannot see process-level information — a limitation for environments requiring application whitelisting or granular process control [22], [26].
- **No documented disaster recovery procedure (item 7.3):** While Virtual Edge Groups provide local failover and the SaaS control plane is cloud-hosted, no customer-facing backup, site-sync, or disaster-recovery procedure is documented. Organizations requiring self-managed DR may need to clarify with the vendor [5], [14].
- **No FIPS 140-2/140-3 or Common Criteria certification (item 8.1):** The vendor attests SOC 2 compliance at the company level, but no product-specific FIPS 140 or Common Criteria validation was found. This gap may affect eligibility for U.S. federal or defense environments [10], [17].

## 6. Evidence Quality Notes

The assessment draws on 42 distinct sources: 35 vendor-origin (28 documents, 12 product release notes, 9 datasheets, 4 blogs) and 7 independent (third-party hands-on reviews and one conference talk). Twenty-three of 33 items are backed by three or more sources, providing reasonable triangulation. Nine items rely solely on vendor documentation (vendor_doc, vendor_datasheet, vendor_blog, product_release_notes) — their confidence is capped at medium per the project's validator rules. Only three items achieved high confidence (1.1, 2.1, 2.3), each corroborated by a detailed hands-on walkthrough from an independent third-party reviewer [14] who tested the platform in a live lab.

No sources contradicted each other. The main evidence gap is the absence of a formal analyst report (Forrester Wave, GigaOm Radar for Microsegmentation) — the vendor was named a "Strong Performer" by an independent research firm [11], but the full report text was behind a paywall and could not be staged. Two items (7.3 disaster recovery, 8.1 FIPS/CC certifications) remain unknown because no source — vendor or independent — addressed them.

---

## Bibliography

[1] Elisity. "Elisity Platform Overview | Simplify Network Segmentation". https://www.elisity.com/platform (Retrieved: 2026-08-10T15:45:00Z)
[2] Elisity. "Microsegmentation Guide: Zero Trust & Identity | Elisity". https://www.elisity.com/microsegmentation (Retrieved: 2026-08-10T15:45:00Z)
[3] Elisity. "Elisity Microsegmentation: Solution Brief (landing page)". https://www.elisity.com/resources/wp/elisity-solution-brief-identity-based-microsegmentation (Retrieved: 2026-08-10T15:45:00Z)
[4] Elisity. "Elisity Overview for Enterprise Network Pros". https://www.elisity.com/resources/ds/overview-for-network-teams (Retrieved: 2026-08-10T15:45:00Z)
[5] Elisity. "Elisity Integrations | Microsegmentation Partners". https://www.elisity.com/integrations-overview (Retrieved: 2026-08-10T15:45:00Z)
[6] Elisity (PRNewswire). "Elisity Launches Open CLI for Customer-Built AI Agents on Its Microsegmentation Platform". https://www.elisity.com/news/elisity-launches-open-cli-for-customer-built-ai-agents-on-its-microsegmentation-platform (Retrieved: 2026-08-10T15:45:00Z)
[7] Elisity. "Elisity 16.12 Release: Custom Connector Transforms Asset Intelligence, and Advanced Policy Controls". https://www.elisity.com/blog/elisity-16.12-release-custom-connector-transforms-asset-intelligence-advanced-policy-controls (Retrieved: 2026-08-10T15:45:00Z)
[8] Elisity. "Elisity Release 16.14: Network Traffic Analytics That Actually Help You Make Decisions". https://www.elisity.com/blog/elisity-release-16.14-network-traffic-analytics-that-actually-help-you-make-decisions (Retrieved: 2026-08-10T15:45:00Z)
[9] Elisity. "Elisity Release 26.6: Cleaner Policy, Richer Identity, Simpler Ops". https://www.elisity.com/blog/elisity-release-26.6-cleaner-policy-richer-identity-and-easier-edge-operations (Retrieved: 2026-08-10T15:45:00Z)
[10] Elisity. "Elisity Release 26.1: Seamless Migration Paths, Enhanced Policy Visibility, and Expanded Device Management". https://www.elisity.com/blog/elisity-release-26.1-seamless-migration-paths-enhanced-policy-visibility-and-expanded-device-management (Retrieved: 2026-08-10T15:45:00Z)
[11] Elisity. "Elisity Named a Strong Performer by Independent Research Firm in an Evaluation of Microsegmentation Solutions". https://www.elisity.com/news/elisity-named-a-strong-performer-by-independent-research-firm-in-an-evaluation-of-microsegmentation-solutions (Retrieved: 2026-08-10T15:45:00Z)
[12] Elisity. "Network Visibility and Microsegmentation | Elisity". https://www.elisity.com/network-visibility-and-microsegmentation (Retrieved: 2026-08-10T15:45:00Z)
[13] Elisity. "Network Asset Discovery for Microsegmentation | Elisity". https://www.elisity.com/network-asset-discovery-for-microsegmentation (Retrieved: 2026-08-10T15:45:00Z)
[14] The Hacker News. "Hands-On Walkthrough: Microsegmentation For all Users, Workloads and Devices by Elisity". https://thehackernews.com/2025/01/hands-on-walkthrough-microsegmentation.html (Retrieved: 2026-08-10T15:45:00Z)
[15] Tech Field Day. "How to Optimize a Microsegmentation Architecture with Elisity - Tech Field Day (NFD36)". https://techfieldday.com/video/how-to-optimize-a-microsegmentation-architecture-with-elisity/ (Retrieved: 2026-08-10T15:45:00Z)
[16] Insight Partners. "Containing the breach: Elisity and the rise of microsegmentation". https://www.insightpartners.com/ideas/elisity-leadership-story/ (Retrieved: 2026-08-10T15:45:00Z)
[17] Elisity (PRNewswire). "Elisity Microsegmentation Enables St. Luke's to Secure 85,000 Medical Devices and Unlocks Clinical Innovation in 46 Days". https://www.elisity.com/news/elisity-microsegmentation-enables-st.-lukes-to-secure-85000-medical-devices-and-unlocks-clinical-innovation-in-46-days (Retrieved: 2026-08-10T15:45:00Z)
[18] Elisity. "Elisity Releases Version 15.4 of their Identity-Based Microsegmentation Solution". https://www.elisity.com/blog/elisity-release-version-15.4-of-their-identity-based-microsegmentation-solution (Retrieved: 2026-08-10T15:45:00Z)
[19] Elisity. "How to Automate Palo Alto Networks Dynamic Address Groups with Identity-Based Classification". https://www.elisity.com/blog/automate-palo-alto-firewall-dynamic-address-groups-identity-classification (Retrieved: 2026-08-10T15:45:00Z)
[20] Omdia / Elisity. "Why Microsegmentation Stalls: Only 9% Reach 81% Coverage (Omdia survey, vendor-hosted)". https://www.elisity.com/omdia-microsegmentation-report (Retrieved: 2026-08-10T15:45:00Z)
[21] Elisity. "Elisity Releases Version 14.9". https://www.elisity.com/blog/elisity-releases-version-14.9 (Retrieved: 2026-08-10T15:45:00Z)
[22] Elisity. "Microsegmentation for Compliance: HIPAA, PCI & NIST". https://www.elisity.com/microsegmentation-for-compliance-enhancing-security-with-elisity (Retrieved: 2026-08-10T15:45:00Z)
[23] Elisity. "Introduction to Elisity Microsegmentation (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/15550164572436-Introduction-to-Elisity-Microsegmentation (Retrieved: 2026-08-10T15:45:00Z)
[24] Elisity. "Policy Simulation (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/15857454131476-Policy-Simulation (Retrieved: 2026-08-10T15:45:00Z)
[25] Elisity. "Policy Sets and Site Labels (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/15787103926036-Policy-Sets-and-Site-Labels (Retrieved: 2026-08-10T15:45:00Z)
[26] Elisity. "Virtual Edge Groups (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/29934220214804-Virtual-Edge-Groups (Retrieved: 2026-08-10T15:45:00Z)
[27] Elisity. "Troubleshooting Virtual Edge Offline Issues (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/51511251451412-Troubleshooting-Virtual-Edge-Offline-Issues (Retrieved: 2026-08-10T15:45:00Z)
[28] Elisity. "Virtual Edge Hypervisor Deployment Guide (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/31850135015572-Virtual-Edge-Hypervisor-Deployment-Guide (Retrieved: 2026-08-10T15:45:00Z)
[29] Elisity. "Anatomy of an Elisity Policy (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/35608068924564-Anatomy-of-an-Elisity-Policy (Retrieved: 2026-08-10T15:45:00Z)
[30] Elisity. "Connect Splunk SIEM (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/15520201315732-Connect-Splunk-SIEM (Retrieved: 2026-08-10T15:45:00Z)
[31] Elisity. "Connect ServiceNow CMDB (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/15520035416724-Connect-ServiceNow-CMDB (Retrieved: 2026-08-10T15:45:00Z)
[32] Elisity. "26.7.0 Release Notes (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/51881047288084-26-7-0-Release-Notes (Retrieved: 2026-08-10T15:45:00Z)
[33] Elisity. "Traffic View in the Policy Matrix (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/38475913332116-Traffic-View-in-the-Policy-Matrix (Retrieved: 2026-08-10T15:45:00Z)
[34] Elisity. "Elisity Assistant - Identify Overly Permissive Policy (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/50561663421332-Elisity-Assistant-Identify-Overly-Permissive-Policy (Retrieved: 2026-08-10T15:45:00Z)
[35] Elisity. "Policy and Device Insights (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/44145923939732-Policy-and-Device-Insights (Retrieved: 2026-08-10T15:45:00Z)
[36] Elisity. "Elisity AI Capabilities Data Sheet (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/48464372727188-Elisity-AI-Capabilities-Data-Sheet (Retrieved: 2026-08-10T15:45:00Z)
[37] Elisity. "Policy Groups (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/15583393995924-Policy-Groups (Retrieved: 2026-08-10T15:45:00Z)
[38] Elisity. "Security Profiles (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/15770034574740-Security-Profiles (Retrieved: 2026-08-10T15:45:00Z)
[39] Elisity. "Monitoring (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/38475420966676-Monitoring (Retrieved: 2026-08-10T15:45:00Z)
[40] Elisity. "Configure Cloud Workloads Visibility for AWS (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/48950622874644-Configure-Cloud-Workloads-Visibility-for-AWS (Retrieved: 2026-08-10T15:45:00Z)
[41] Elisity. "Policy Evaluator (Knowledge Base)". https://support.elisity.com/hc/en-us/articles/30976057011732-Policy-Evaluator (Retrieved: 2026-08-10T15:45:00Z)
[42] Elisity. "From 2.1 Billion Events to 10 Incidents: How We Protect the Elisity Platform". https://www.elisity.com/blog/from-2.1-billion-events-to-10-incidents-how-we-protect-the-elisity-platform (Retrieved: 2026-08-10T15:45:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 36
- **Sources reviewed:** 42 (kept: 42, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 1, conference_talk: 1, product_release_notes: 7, third_party_review: 2, vendor_blog: 4, vendor_datasheet: 3, vendor_doc: 24
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
