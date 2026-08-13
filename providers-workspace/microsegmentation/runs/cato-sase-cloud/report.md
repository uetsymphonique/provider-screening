# Microsegmentation Product Assessment: Cato Networks - Cato SASE Cloud

**Product ID:** `cato-sase-cloud`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T12:00:00Z
**Total evidence items collected:** 80
**Total distinct sources:** 53

---

## 1. Overview

Cato SASE Cloud is a cloud-native single-vendor SASE platform that converges SD-WAN, a global private backbone, and a full network security stack delivered from Cato's worldwide points of presence (PoPs) [52, 1]. Its microsegmentation capability is agentless: enabling it for a Socket site breaks the network range into /32 host addresses and forces all intra-VLAN host-to-host traffic through the Socket, where the Next Gen LAN Firewall evaluates it against policy [3, 38]. Policy is defined centrally in the Cato Management Application and distributed to Sockets, which enforce it locally with Layer 2-7 inspection [38, 45]. The same platform provides the Cato Client agent for endpoints, ZTNA via client or clientless App Connectors, flow-level analytics, and a Data Lake for event retention [5, 25, 47, 20]. Cato positions the offering as zero-trust access extended into the LAN rather than a dedicated host-agent microsegmentation controller; there is no host-resident enforcement agent, so host-level isolation depends on the Socket remaining the traffic path for segmented ranges [3, 38].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 10    | 1                | 9      | 0   |
| partial          | 19    | 0                | 18     | 1   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 1 items backed by ≥ 2 source_types; 29 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | Cato generates enriched flow data inline for traffic processed by the Cato Cloud and passively discovers and classifies devices without agents, per the flow analytics and Device Inventory documentation. [5], [40], [50] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | The Topology page maps sites and connected users, and Segmentation Flows render a Sankey diagram of traffic by device type, application, protocol and destination; these views are not organized by the App/Environment/Role/Process model the checklist requires. [34], [37] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 90 days | The Cato Data Lake retains events for 3 months by default and can be extended with 6- or 12-month retention units, and the EventsFeed API and Event Discovery tools limit historical queries to roughly 90 days. [7], [9], [20] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | low | - | Cato's IPS engine protects against known CVEs, but no documentation shows vulnerability or CVE context displayed directly on the map or segmentation views. [12] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | - | Flow-level visibility covers all traffic inspected by the Cato Cloud, and Device Inventory passively discovers and classifies devices including unmanaged IoT/OT; a dedicated unrecognized-traffic alert feature is not documented. [36], [38], [40] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Firewall and segmentation rules match on user/group identity, application, and device attributes (OS, manufacturer, type) rather than raw IPs or VLANs, including identity-based rules on the Socket LAN Firewall. [2], [38], [43], [51] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | Autonomous Policies use an AI agent that analyzes real network behavior to recommend rule changes, and Ask AI can draft firewall rules from natural-language analysis. [29], [33] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | Policies support unpublished revisions so changes can be staged and reviewed before publishing, but no traffic-replay or impact-simulation dry-run engine is documented. [33], [46] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | Admins can discard unpublished revisions to revert to the published policy, but no explicit one-click restore of a previously published policy version is documented. [46] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | The account-level LAN Firewall policy supports a main policy with sub-policies anchored by scoping rules and RBAC delegation; nesting is limited to one level. [45] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The Cato Client supports Windows 8.1/10/11 and Server 2016-2022, macOS, and Linux (Ubuntu, RHEL, CentOS, Fedora, Debian); AIX and Solaris are not supported and Windows Server 2003-2012 is not covered. [3], [25] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (The Knowledge Base's only 'Container' feature is IoC-list containers, unrelated to workload isolation; no Kubernetes/OpenShift agent or native container isolation is documented.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | Microsegmentation is agentless (enforced on the Cato Socket), while the Cato Client provides an agent-based path and App Connectors provide agentless network integration for private applications. [25], [38], [39], [47] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | - | no evidence found (All documented deployment models assume connectivity to Cato Cloud PoPs; no air-gapped deployment mode is documented.) |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | The platform is a multi-tenant cloud with a single policy framework that scales to many sites and planning tables that cover up to roughly 35K SDP clients per account, but no explicit 50,000-workload figure is published. [7], [20], [38] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | No CPU usage figure for the Cato Client is published; documentation only describes resource usage qualitatively. [7] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | No RAM footprint figure for the Cato Client is published; documentation only notes a throughput overhead of up to 20% from encryption and encapsulation. [7] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Local Socket enforcement is described as minimal-latency, while cloud transaction processing latency is documented as up to 10 ms; no sub-0.1 ms figure is published. [7], [38] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | Enforcement is Socket-based rather than host-agent; Socket HA failover preserves flow and NAT state so applications keep operating, but no explicit fail-open behavior is documented for the Cato Client. [38], [41] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | - | Client installs use an installation wizard and updates can be rolled out automatically as a managed service with no documented reboot step, but Cato does not explicitly state that a reboot is never required. [21], [24] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | The Cato API is GraphQL-based (described as compatible with RESTful clients) and documented as the primary automation interface for deployment, configuration and monitoring; coverage of 100% of admin functions is not stated. [10], [42], [43] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Event Integrations forward Cato events to Splunk, Microsoft Sentinel and CrowdStrike with native connectors, to AWS S3/Azure storage, or via a custom HTTP push. [8], [17], [22] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | - | A ServiceNow integration exists but covers App Activities visibility of SaaS user activity; CMDB tag/label synchronization is not documented. [26] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | Cato publishes Terraform-based deployment documentation for vSockets, and the Cato API supports configuration automation usable in CI/CD pipelines. [11], [42] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | The LAN Firewall enforces at Layers 2-4 and Layer 7 (application) level with user/device context; process-level enforcement is not documented. [38], [45] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat intelligence feeds, reputation scoring and custom IoC lists are integrated; honeypot/deception detection is not documented. [4], [23] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Posture compliance reports map GDPR, ISO 27001:2022 and NIST SP 800-53 Rev. 5 controls, and Cato holds PCI-DSS Level 1 and ISO 27001 certifications; NIST 800-207 and IEC 62443 mappings are not documented. [16], [35], [53] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | Client-to-PoP traffic is encrypted over DTLS tunnels with device-certificate authentication, and TLS 1.3 is configurable in TLS inspection; the tunnel's DTLS version is not explicitly stated as 1.3. [14], [15], [32] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | high | - | Sites deploy Socket HA pairs, the Cato Cloud's PoPs continue processing traffic during maintenance windows, and the public status page tracks per-region services; Wikipedia corroborates more than 73 PoPs in over 150 countries. [1], [13], [30], [41], [48] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | The Socket enforces the LAN Firewall policy locally and continues traffic inspection even when the Cato Cloud is temporarily unreachable (WAN Recovery scenario). [27], [38] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | The Cato Cloud documents self-healing rollback of cloud updates and PoP redundancy, but no customer-facing configuration backup/restore or DR site-sync feature is documented. [30] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | - | Cato's own documentation states that Cato Networks is not FIPS-compliant and is not FIPS 140-2 or 140-3 certified; no Common Criteria EAL4+ certification is documented. [15] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (No Siemens, Honeywell or ABB compatibility certifications documented.) |

---

## 4. Notable Strengths

- **Agentless, policy-driven microsegmentation (items 3.3, 2.1):** Cato delivers host-level isolation without endpoint agents, enforced by the Socket LAN Firewall using identity-, application-, and device-attribute-based rules defined centrally in the CMA [38, 2].
- **AI-assisted policy management (items 2.2, 2.3):** Autonomous Policies and Ask AI analyze real network behavior and recommend or draft firewall rules, staged as unpublished revisions before publishing [29, 33].
- **Event retention plus SIEM/API integration (items 1.3, 5.2):** The Data Lake retains events for 3 months by default (extendable to 12 months) and native connectors push events to Splunk and Microsoft Sentinel [20, 17].
- **Resilient enforcement with local autonomy (items 7.1, 7.2):** Socket HA pairs preserve flow state on failover, other PoPs keep processing traffic during maintenance windows, and the LAN Firewall keeps enforcing locally even when the Cato Cloud is unreachable [41, 30, 27].
- **Compliance posture reporting (item 6.3):** Posture compliance reports map GDPR, ISO 27001:2022 and NIST SP 800-53 Rev. 5 controls, and Cato is PCI-DSS Level 1 and ISO 27001 certified [16, 53].

## 5. Notable Gaps / Risks

- **No FIPS 140-2/140-3 or Common Criteria certification (item 8.1):** Cato's own documentation states the platform is not FIPS-compliant and not FIPS 140-2/140-3 certified, which excludes it from US federal and some regulated deployments [15].
- **Quantified agent-resource and scale figures missing (items 4.1, 4.2, 4.3, 3.5):** No published CPU percentage, RAM footprint, sub-0.1 ms latency, or 50,000-workload figure exists; planning tables reach only roughly 35K SDP clients per account [7, 20].
- **No container/Kubernetes isolation or air-gapped mode (items 3.2, 3.4):** No native container isolation or offline/air-gapped deployment is documented, and all deployment models assume connectivity to Cato Cloud PoPs [3, 38].
- **Limited policy dry-run and rollback semantics (items 2.3, 2.4):** Policy revisions let admins discard unpublished drafts, but there is no traffic-simulation dry-run and no one-click restore of a previously published policy version [46].
- **CMDB tag sync absent (item 5.3):** The ServiceNow integration covers App Activities visibility of SaaS activity, not CMDB tag/label synchronization [26].

## 6. Evidence Quality Notes

All 33 checklist items carry verdicts, backed by 80 evidence entries drawn from 53 staged sources. The evidence base is overwhelmingly vendor-authored: 52 of 53 sources are Cato's own Knowledge Base or product/compliance pages (vendor_doc), which caps confidence at medium for every item except 7.1, where the Wikipedia company article (community) independently corroborates the 73+ PoP / 150+ country footprint. Only 7.1 therefore reaches high confidence. Items 3.2, 3.4 and 8.2 are unknown because no source describes the capability and none explicitly rules it out; item 8.1 is not_supported based on Cato's own explicit statement that it is not FIPS 140-2/140-3 certified.

Triangulation was mostly across multiple Cato documents per item (2-4 vendor sources each), so claims rest on internally consistent documentation rather than independent verification. No direct source contradictions surfaced; where documents were ambiguous, verdicts were set to partial with notes stating the imprecision, notably the numeric items 4.1/4.2/4.3/3.5 and the GraphQL-based API in 5.1. The marketing site (catonetworks.com) blocks direct fetches, and commercial review platforms (G2, TrustRadius, PeerSpot, Capterra) were unreachable from this environment, so independent corroboration is limited to Wikipedia.

---

## Bibliography

[1] Wikipedia. "Cato Networks - Wikipedia". https://en.wikipedia.org/wiki/Cato_Networks (Retrieved: 2026-08-10T12:00:00Z)
[2] Cato Networks. "Adding Device Conditions to Firewall Rules (Knowledge Base)". https://knowledge.catonetworks.com/docs/adding-device-conditions-to-firewall-rules.md (Retrieved: 2026-08-10T12:00:00Z)
[3] Cato Networks. "Adding Microsegmentation Zero-Trust Security to Sites (Knowledge Base)". https://knowledge.catonetworks.com/docs/adding-microsegmentation-zero-trust-security-to-sites.md (Retrieved: 2026-08-10T12:00:00Z)
[4] Cato Networks. "An Overview of Threat Intelligence (Knowledge Base)". https://knowledge.catonetworks.com/docs/an-overview-of-threat-intelligence.md (Retrieved: 2026-08-10T12:00:00Z)
[5] Cato Networks. "Analyzing Network Flows in Cato (Knowledge Base)". https://knowledge.catonetworks.com/docs/analyzing-network-flows-in-cato.md (Retrieved: 2026-08-10T12:00:00Z)
[6] Cato Networks. "Cato API - EventsFeed (Large Scale Event Monitoring) (Knowledge Base)". https://knowledge.catonetworks.com/docs/cato-api-eventsfeed-large-scale-event-monitoring.md (Retrieved: 2026-08-10T12:00:00Z)
[7] Cato Networks. "Cato Cloud Thresholds and Limits (Knowledge Base)". https://knowledge.catonetworks.com/docs/cato-cloud-thresholds-and-limits.md (Retrieved: 2026-08-10T12:00:00Z)
[8] Cato Networks. "Cato Event to Splunk CIM Field Mapping (Knowledge Base)". https://knowledge.catonetworks.com/docs/cato-event-to-splunk-cim-field-mapping.md (Retrieved: 2026-08-10T12:00:00Z)
[9] Cato Networks. "Cato Monitoring API - Reference Guide (Knowledge Base)". https://knowledge.catonetworks.com/docs/cato-monitoring-api-reference-guide.md (Retrieved: 2026-08-10T12:00:00Z)
[10] Cato Networks. "Configuration API - addSocketSite (Knowledge Base)". https://knowledge.catonetworks.com/docs/configuration-api-addsocketsite.md (Retrieved: 2026-08-10T12:00:00Z)
[11] Cato Networks. "Configuring a Cato vSocket in GCP Using Terraform (Knowledge Base)". https://knowledge.catonetworks.com/docs/configuring-a-cato-vsocket-in-gcp-using-terraform.md (Retrieved: 2026-08-10T12:00:00Z)
[12] Cato Networks. "Configuring IPS and Geo Restriction (Knowledge Base)". https://knowledge.catonetworks.com/docs/configuring-ips-and-geo-restriction.md (Retrieved: 2026-08-10T12:00:00Z)
[13] Cato Networks. "Configuring the Connection SLA Settings for Active/Passive Socket Sites (Knowledge Base)". https://knowledge.catonetworks.com/docs/connection-sla.md (Retrieved: 2026-08-10T12:00:00Z)
[14] Cato Networks. "Distributing Device Certificates to Windows Devices With Certutil (Knowledge Base)". https://knowledge.catonetworks.com/docs/distributing-and-installing-device-certificates.md (Retrieved: 2026-08-10T12:00:00Z)
[15] Cato Networks. "FIPS Compliance and TLS Configuration at Cato Networks (Knowledge Base)". https://knowledge.catonetworks.com/docs/fips-compliance-and-tls-configuration-at-cato-networks.md (Retrieved: 2026-08-10T12:00:00Z)
[16] Cato Networks. "Generating Posture or Posture Compliance Reports (Knowledge Base)". https://knowledge.catonetworks.com/docs/generating-a-posture-or-posture-compliance-report.md (Retrieved: 2026-08-10T12:00:00Z)
[17] Cato Networks. "Getting Started with Event Integrations (Knowledge Base)". https://knowledge.catonetworks.com/docs/getting-started-with-event-integrations.md (Retrieved: 2026-08-10T12:00:00Z)
[18] Cato Networks. "Getting Started with the Linux Client (Knowledge Base)". https://knowledge.catonetworks.com/docs/getting-started-with-the-linux-client.md (Retrieved: 2026-08-10T12:00:00Z)
[19] Cato Networks. "Getting Started with the Windows Client (Knowledge Base)". https://knowledge.catonetworks.com/docs/getting-started-with-the-windows-client.md (Retrieved: 2026-08-10T12:00:00Z)
[20] Cato Networks. "Guide to Cato Data Lake (Knowledge Base)". https://knowledge.catonetworks.com/docs/guide-to-cato-data-lake.md (Retrieved: 2026-08-10T12:00:00Z)
[21] Cato Networks. "Installing the Cato Client (Knowledge Base)". https://knowledge.catonetworks.com/docs/installing-the-cato-client.md (Retrieved: 2026-08-10T12:00:00Z)
[22] Cato Networks. "Integrating Cato Events with Microsoft Sentinel (Knowledge Base)". https://knowledge.catonetworks.com/docs/integrating-cato-events-with-microsoft-sentinel.md (Retrieved: 2026-08-10T12:00:00Z)
[23] Cato Networks. "Integrating Custom IoC Lists with Containers (Knowledge Base)". https://knowledge.catonetworks.com/docs/integrating-custom-ioc-lists-with-containers.md (Retrieved: 2026-08-10T12:00:00Z)
[24] Cato Networks. "Managing Vulnerabilities for the Cato Socket and Client (Knowledge Base)". https://knowledge.catonetworks.com/docs/managing-vulnerabilities-for-the-cato-socket-and-client.md (Retrieved: 2026-08-10T12:00:00Z)
[25] Cato Networks. "Preparing to Install the Cato Client (Knowledge Base)". https://knowledge.catonetworks.com/docs/preparing-to-install-the-cato-client.md (Retrieved: 2026-08-10T12:00:00Z)
[26] Cato Networks. "ServiceNow: Configuring the App Activities Integration (Knowledge Base)". https://knowledge.catonetworks.com/docs/servicenow-configuring-the-app-activities-integration.md (Retrieved: 2026-08-10T12:00:00Z)
[27] Cato Networks. "Socket Site Resiliency with WAN Recovery (Knowledge Base)". https://knowledge.catonetworks.com/docs/socket-site-resiliency-with-wan-recovery.md (Retrieved: 2026-08-10T12:00:00Z)
[28] Cato Networks. "Summary of Cato Client Releases (Knowledge Base)". https://knowledge.catonetworks.com/docs/summary-of-cato-client-releases.md (Retrieved: 2026-08-10T12:00:00Z)
[29] Cato Networks. "Understanding Cato Autonomous Policies (Knowledge Base)". https://knowledge.catonetworks.com/docs/understanding-cato-autonomous-policies.md (Retrieved: 2026-08-10T12:00:00Z)
[30] Cato Networks. "Understanding Rollout to the Cato Cloud (Knowledge Base)". https://knowledge.catonetworks.com/docs/understanding-rollout-to-the-cato-cloud.md (Retrieved: 2026-08-10T12:00:00Z)
[31] Cato Networks. "Understanding the Capabilities of the Cato Client (Knowledge Base)". https://knowledge.catonetworks.com/docs/understanding-the-capabilities-of-the-cato-client.md (Retrieved: 2026-08-10T12:00:00Z)
[32] Cato Networks. "Using an Alternate UDP Port for Socket and Client DTLS Traffic (Knowledge Base)". https://knowledge.catonetworks.com/docs/using-an-alternate-udp-port-for-socket-and-client-dtls-traffic.md (Retrieved: 2026-08-10T12:00:00Z)
[33] Cato Networks. "Using Ask AI to Create Internet Firewall Rules (Knowledge Base)". https://knowledge.catonetworks.com/docs/using-ask-ai-to-create-internet-firewall-rules.md (Retrieved: 2026-08-10T12:00:00Z)
[34] Cato Networks. "Using Segmentation Flows (Knowledge Base)". https://knowledge.catonetworks.com/docs/using-segmentation-flows.md (Retrieved: 2026-08-10T12:00:00Z)
[35] Cato Networks. "Using the Audit Trail (Knowledge Base)". https://knowledge.catonetworks.com/docs/using-the-audit-trail.md (Retrieved: 2026-08-10T12:00:00Z)
[36] Cato Networks. "Using the Device Inventory Page (Knowledge Base)". https://knowledge.catonetworks.com/docs/using-the-device-inventory-page.md (Retrieved: 2026-08-10T12:00:00Z)
[37] Cato Networks. "Using the Topology Page (Knowledge Base)". https://knowledge.catonetworks.com/docs/using-the-topology-page.md (Retrieved: 2026-08-10T12:00:00Z)
[38] Cato Networks. "What is Cato LAN Segmentation (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-cato-lan-segmentation.md (Retrieved: 2026-08-10T12:00:00Z)
[39] Cato Networks. "What is Cato's ZTNA Solution (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-cato-s-ztna-solution.md (Retrieved: 2026-08-10T12:00:00Z)
[40] Cato Networks. "What is Device Inventory? (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-device-inventory.md (Retrieved: 2026-08-10T12:00:00Z)
[41] Cato Networks. "What is Socket HA (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-socket-ha.md (Retrieved: 2026-08-10T12:00:00Z)
[42] Cato Networks. "What is the Cato API (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-the-cato-api.md (Retrieved: 2026-08-10T12:00:00Z)
[43] Cato Networks. "What is the Cato Firewall (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-the-cato-firewall.md (Retrieved: 2026-08-10T12:00:00Z)
[44] Cato Networks. "What is the Client Connectivity Policy? (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-the-client-connectivity-policy.md (Retrieved: 2026-08-10T12:00:00Z)
[45] Cato Networks. "What is the Socket Next Gen LAN Firewall (Knowledge Base)". https://knowledge.catonetworks.com/docs/what-is-the-socket-next-gen-lan-firewall.md (Retrieved: 2026-08-10T12:00:00Z)
[46] Cato Networks. "Working with Policy Revisions (Knowledge Base)". https://knowledge.catonetworks.com/docs/working-with-policy-revisions.md (Retrieved: 2026-08-10T12:00:00Z)
[47] Cato Networks. "Zero Trust Access to Private Applications with the Cato SASE Cloud (Knowledge Base)". https://knowledge.catonetworks.com/docs/zero-trust-access-to-private-applications-with-the-cato-sase-cloud.md (Retrieved: 2026-08-10T12:00:00Z)
[48] Cato Networks. "Cato Networks service status API". https://status.catonetworks.com/api/statuses (Retrieved: 2026-08-10T12:00:00Z)
[49] Cato Networks. "Firewall-as-a-Service (FWaaS) product page". https://www.catonetworks.com/platform/firewall-as-a-service-fwaas/ (Retrieved: 2026-08-10T12:00:00Z)
[50] Cato Networks. "IoT/OT Security product page". https://www.catonetworks.com/platform/iot-ot-security/ (Retrieved: 2026-08-10T12:00:00Z)
[51] Cato Networks. "Universal Zero Trust Network Access (ZTNA) product page". https://www.catonetworks.com/platform/universal-zero-trust-network-access-ztna/ (Retrieved: 2026-08-10T12:00:00Z)
[52] Cato Networks. "Cato SASE Cloud product page". https://www.catonetworks.com/sase/ (Retrieved: 2026-08-10T12:00:00Z)
[53] Cato Networks. "Security, Compliance and Privacy page". https://www.catonetworks.com/security-compliance-and-privacy/ (Retrieved: 2026-08-10T12:00:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 53 (kept: 53, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, vendor_doc: 52
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
