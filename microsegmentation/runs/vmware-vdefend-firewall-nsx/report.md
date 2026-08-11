# Microsegmentation Product Assessment: VMware (by Broadcom) - VMware vDefend Firewall (NSX)

**Product ID:** `vmware-vdefend-firewall-nsx`
**Version reference:** VMware vDefend Firewall 9.1 / NSX 4.2 (VCF 9.x era); staged sources cover vDefend Firewall 9.1, NSX 4.2, NSX-T Data Center 3.2, vDefend Security Intelligence 3.2, vDefend ATP 4.2 and Aria Operations for Networks 6.14
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T08:40:00Z
**Total evidence items collected:** 72
**Total distinct sources:** 38

---

## 1. Overview

VMware vDefend Firewall (formerly the NSX-T Data Center distributed and gateway firewalls) is Broadcom's software-defined Layer 2-7 firewall for private-cloud workloads [1]. It ships in two form factors: a Distributed Firewall enforced in the ESXi hypervisor kernel at each workload - agentless, east-west microsegmentation for virtualized, container and bare-metal workloads - and a Gateway Firewall for north-south traffic on NSX Edge nodes [1][2]. VMware positions it as the security layer of the NSX/VMware Cloud Foundation networking stack, with L7 application identity, AD user identity and FQDN filtering, plus flow visualization through NSX Intelligence and Aria Operations for Networks [1][17][16]. Deployment shapes span vSphere hosts, physical servers, Kubernetes clusters via the Antrea CNI, and multi-site NSX Federation, all managed through NSX Manager, the REST API or the Terraform provider [25][12][5]. The product runs on FIPS 140-3 validated cryptographic modules by default [29]. This assessment is anchored to vDefend Firewall 9.1 / NSX 4.2 documentation (see version reference).

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 16    | 1                | 15     | 0   |
| partial          | 10    | 0                | 10     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 4     | 0                | 4      | 0   |

**Evidence quality:** 6 items backed by ≥ 2 source_types; 27 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** Not applicable: vDefend Distributed Firewall is enforced in the ESXi kernel (VSIP) with no in-guest agent, so there is no agent CPU footprint to measure.
- **4.2:** Not applicable: enforcement is agentless in the hypervisor kernel, so no in-guest agent memory footprint exists for the DFW.
- **4.4:** Not applicable: there is no in-guest agent whose failure could interrupt traffic; enforcement runs in the hypervisor kernel.
- **4.5:** Not applicable: no guest agent is installed or updated on servers for the DFW, so a reboot-on-update requirement does not arise.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Continuous flow visibility is built in: NSX Intelligence renders a graphical view of groups, VMs, physical servers, IPs and traffic flows, and DFW IPFIX flows are viewable in Aria Operations for Networks; the vDefend overview documents scalable traffic-flow analysis and a PeerSpot user describes using NSX microsegmentation for workload isolation. [1], [16], [17], [34] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | medium | — | NSX Intelligence provides a graphical visualization of groups, VMs, physical servers, IPs and traffic flows, and the Security Overview dashboard presents a visual summary of the security configuration; tag-based groups support organization by application, environment and role. [1], [3], [17] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | 30 days | NSX Intelligence stores collected flow data and persists it for 30 days, below the 90-day requirement; longer forensic retention would depend on external flow collectors whose retention is not documented in the staged sources. [19] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | The Security Overview dashboard can rank top VMs by vulnerability severity in the IDS/IPS summaries, but no staged source documents a CVE overlay rendered directly on the connectivity map. [3] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | Live Traffic Analysis traces live traffic and identifies bad flows, and the NSX Suspicious Traffic feature flags suspicious or anomalous east-west network behaviors using ML detectors on collected flow data. [15], [19] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | Policy identification is built on VM tags and dynamic groups (tag, machine name, OS name) rather than IP/VLAN, and Identity Firewall adds Active Directory user-based rules. [4], [8], [10] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | — | NSX Intelligence generates micro-segmentation recommendations covering security policies, policy security groups and services, derived from observed network traffic flow patterns. [17], [18] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | — | Traceflow injects a packet into the network to observe its path, and firewall drafts let a complete DFW configuration be staged and published later; no dedicated policy dry-run/simulation mode is documented in the staged sources. [6], [14] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Supported | medium | — | Firewall drafts can be loaded and published to become the active configuration, with a Revert action returning to the previous published configuration; publishing creates a new auto-draft for rollback. [6], [7] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | — | DFW rule categories (Ethernet, Emergency, Infrastructure, Environment, Application) are evaluated in order with rules evaluated top-down inside each category, and groups support static/dynamic membership. [4], [37] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | medium | — | The distributed firewall is enforced in the hypervisor kernel without a guest agent (guest-OS agnostic for VMs on ESXi), and the Gateway Firewall enforces policy for physical servers such as AIX/Solaris systems that cannot be virtualized. [1], [2], [5] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | — | Kubernetes clusters (TKG, OpenShift or DIY) with Antrea CNI integrate with NSX so security policies are centrally managed and enforced in-cluster by the Antrea controller; DFW policies can secure pod-to-pod traffic within a cluster. [25], [26] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | — | Core DFW enforcement is agentless in the hypervisor kernel, while optional Guest Introspection thin agents and a gateway firewall for bare-metal/virtualized workloads provide additional deployment shapes. [1], [5], [9] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | NSX supports operation without Internet connectivity: IDS/IPS signature bundles can be downloaded via API on another machine and uploaded to NSX Manager, keeping signature updates functional in an air-gapped environment. [20] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Documented scale covers NSX Manager clusters of 128+ hypervisors (Large/XL sizes) and vendor claims of massive automatic scaling, but no staged source states a workload count of 50,000 or more. [1], [33], [34] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | Not applicable: vDefend Distributed Firewall is enforced in the ESXi kernel (VSIP) with no in-guest agent, so there is no agent CPU footprint to measure. [2], [5] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | Not applicable: enforcement is agentless in the hypervisor kernel, so no in-guest agent memory footprint exists for the DFW. [5] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Vendor sources describe a fast path designed for minimal overhead and EDP delivering superior latency and throughput, but no staged source publishes a sub-0.1 ms added-latency figure. [5], [12] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | Not applicable: there is no in-guest agent whose failure could interrupt traffic; enforcement runs in the hypervisor kernel. [5] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | Not applicable: no guest agent is installed or updated on servers for the DFW, so a reboot-on-update requirement does not arise. [5] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | — | NSX exposes a JSON-based RESTful API for integration with cloud management platforms and DevOps automation with documented authentication mechanisms, and the vendor describes an API-driven, object-based automation model. [1], [12], [28] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Syslog servers can be configured for NSX Manager and Edge nodes, DFW packet logs are produced on ESXi hosts, and NSX monitoring is supported via Aria Operations for Logs or a Splunk app. [27], [32], [38] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | — | The vendor documents a fully supported Terraform provider and PowerShell integration, plus Infrastructure-as-Code support for defining and managing networking resources programmatically in CI/CD workflows. [12] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | — | Process context is monitored (user behavior, processes, workload context) and exposed to security services via the Guest Introspection context API, but staged sources document rule matching at group, identity and application level rather than native process-level enforcement. [1], [9] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Threat intelligence is integrated through Malicious IP Filtering with vTIS/NTICS feeds and ML-based suspicious-traffic detection; no honeypot/deception capability is documented in the staged sources. [10], [11], [19] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | NSX provides standards-compliance configuration with a compliance status report (FIPS 140-3 modules, CC EAL4+ design) and segmentation reports (Security Segmentation, Blast Radius), but PCI-DSS, NIST 800-207, ISO 27001 or IEC 62443-specific compliance reporting is not documented in the staged sources. [2], [29], [30] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | NSX creates certificates for appliance-to-appliance and external communication including federation, and the documented API TLS configuration enables TLSv1.1 and TLSv1.2; TLS 1.3 is not listed in that configuration. [28], [31] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | For fault tolerance the vendor recommends a three-node NSX Manager cluster, which now also hosts the central control plane role formerly provided by a separate controller appliance. [21], [33] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (No staged source explicitly states DFW behavior during a total controller/management-plane outage; enforcement is documented as running locally in the hypervisor kernel.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | — | NSX Federation supports switching to a standby Global Manager for disaster recovery, backup and restore of NSX Manager is documented, and the vendor cites federation's simplified disaster recovery architecture. [12], [23], [24] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | NSX is configured by default to use FIPS 140-3 validated modules whose certificates (e.g., VMware VPN Crypto Module #4881) appear in the NIST CMVP registry, and the vendor documents EAL4+ design compliance; the Common Criteria portal lists VMware ESXi and Avi Load Balancer but no NSX product certificate. [29], [30], [35], [36] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found |

---

## 4. Notable Strengths

- **Agentless hypervisor-enforced firewalling (items 3.3, 4.1, 4.2, 4.4, 4.5):** the Distributed Firewall runs in the ESXi kernel (VSIP) with no in-guest agent, so there is no agent CPU/RAM footprint, no agent-failure interruption and no reboot requirement [5][2].
- **Tag and identity-based policy at scale (items 2.1, 2.5):** rules are built on VM tags, dynamic groups and Active Directory user identity rather than IP/VLAN, with a documented hierarchical category evaluation order [4][8][37].
- **AI-assisted micro-segmentation (item 2.2):** NSX Intelligence generates security policy, group and service recommendations from observed traffic flows [17][18].
- **Kubernetes-native isolation (item 3.2):** Antrea-CNI clusters integrate with NSX so distributed firewall policies are enforced in-cluster by the Antrea controller [25][26].
- **High availability and disaster recovery (items 7.1, 7.3):** a three-node NSX Manager cluster provides management/control-plane redundancy, and NSX Federation adds standby Global Manager failover plus documented backup/restore [21][23][24].

## 5. Notable Gaps / Risks

- **Flow-history retention below the 90-day threshold (item 1.3):** NSX Intelligence persists flow data for 30 days; meeting the forensic requirement depends on an external flow collector whose retention is not documented in the staged sources.
- **No documented workload-count scale figure (item 3.5):** sources document 128+ hypervisors per management cluster and qualitative "massive scale" claims, but no staged source states 50,000+ workloads.
- **Latency impact unquantified (item 4.3):** only qualitative "minimal overhead" and "superior latency" language exists; no sub-0.1 ms added-latency figure was found.
- **TLS 1.3 not enabled on documented channels (item 6.4):** the API TLS configuration lists TLSv1.1/TLSv1.2 only, with certificate-based mutual-authenticated channels documented.
- **No evidence found for ServiceNow CMDB sync (5.3), autonomous policy enforcement under total controller outage (7.2) or OT vendor certifications (8.2):** all rated unknown; Common Criteria status (8.1) is vendor-documented design compliance only, with no NSX certificate listed in the CC portal [36].

## 6. Evidence Quality Notes

The assessment draws on 72 evidence entries from 38 staged sources. Six items are backed by two or more source types: 1.1 (vendor docs plus a PeerSpot community review), 3.5 (vendor docs, datasheet, community), 4.3 and 5.1 (vendor docs plus datasheet), 7.3 (vendor docs plus datasheet) and 8.1 (vendor docs plus the NIST CMVP and Common Criteria portal registries). The remaining 27 items rest on Broadcom/VMware documentation only, which caps confidence at medium per project rules; no item reached three independent sources because public search engines were largely unreachable from the research environment and analyst reports could not be retrieved. All quotes are verified verbatim against the staged artifacts (72/72 grounded, 0 fabricated, 0 unverifiable).

The main contradiction is in certifications (8.1): Broadcom documents FIPS 140-3 validated module usage and EAL4+ design compliance, while the NIST CMVP registry corroborates the module certificates (e.g., VMware VPN Crypto Module #4881) but lists no NSX module, and the Common Criteria portal lists only VMware ESXi and Avi Load Balancer products - so the verdict is partial rather than supported. Numeric-threshold items were downgraded to partial wherever the sources offered only qualitative language (3.5 workloads, 4.3 latency) or a documented figure below the threshold (1.3, 30-day flow retention).

---

## Bibliography

[1] Broadcom. "vDefend Firewall Overview (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-firewall-overview.html (Retrieved: 2026-08-10T08:40:00Z)
[2] Broadcom. "vDefend Distributed Firewall (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall.html (Retrieved: 2026-08-10T08:40:00Z)
[3] Broadcom. "Security Overview Dashboard (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/monitoring-and-troubleshooting-dfw/security-overview.html (Retrieved: 2026-08-10T08:40:00Z)
[4] Broadcom. "vDefend Firewall Policy Basics (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/configuring-distributed-firewall/about-firewall-rules/vdefend-firewall-policy-basics.html (Retrieved: 2026-08-10T08:40:00Z)
[5] Broadcom. "Distributed Firewall Enforcement (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/configuring-distributed-firewall/about-firewall-rules/firewall-rule-enforcement.html (Retrieved: 2026-08-10T08:40:00Z)
[6] Broadcom. "Distributed Firewall Drafts (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/configuring-distributed-firewall/add-a-distributed-firewall-policy/firewall-drafts.html (Retrieved: 2026-08-10T08:40:00Z)
[7] Broadcom. "Publish or Revert a Firewall Draft (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/configuring-distributed-firewall/add-a-distributed-firewall-policy/firewall-drafts/publish-or-revert-a-firewall-draft.html (Retrieved: 2026-08-10T08:40:00Z)
[8] Broadcom. "Identity Firewall (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/identity-firewall.html (Retrieved: 2026-08-10T08:40:00Z)
[9] Broadcom. "Guest Introspection (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/identity-firewall/guest-introspection.html (Retrieved: 2026-08-10T08:40:00Z)
[10] Broadcom. "Add a Group (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/add-a-group.html (Retrieved: 2026-08-10T08:40:00Z)
[11] Broadcom. "Malicious IP Filtering (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/malicious-ip-feeds.html (Retrieved: 2026-08-10T08:40:00Z)
[12] VMware / Broadcom. "VMware Cloud Foundation Networking (NSX) Datasheet (May 2026)". https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/products/nsx/vmware-nsx-datasheet.pdf (Retrieved: 2026-08-10T08:40:00Z)
[13] Broadcom. "Network Monitoring (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/network-monitoring.html (Retrieved: 2026-08-10T08:40:00Z)
[14] Broadcom. "Traceflow (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/network-monitoring/advanced-monitoring-tools/traceflow.html (Retrieved: 2026-08-10T08:40:00Z)
[15] Broadcom. "Live Traffic Analysis (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/network-monitoring/live-traffic-analysis.html (Retrieved: 2026-08-10T08:40:00Z)
[16] Broadcom. "Enable VMware NSX-T DFW IPFIX (VMware Aria Operations for Networks 6.14 documentation)". https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations-for-networks/6-14/vrealize-network-insight-ug-4-1-and-later-6-14/configuring-flows/enabling-ipfix-configuration/nsx-ipfix/enabling-vmware-nsx-t-ipfix.html (Retrieved: 2026-08-10T08:40:00Z)
[17] Broadcom. "Overview of NSX Intelligence (vDefend Security Intelligence 3.2 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/security-intelligence/3-2/activating-and-upgrading-vmware-nsx-intelligence/overview-of-nsx-intelligence.html (Retrieved: 2026-08-10T08:40:00Z)
[18] Broadcom. "Understanding NSX Intelligence Recommendations (vDefend Security Intelligence 3.2 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/security-intelligence/3-2/using-and-managing-vmware-nsx-intelligence/working-with-nsx-intelligence-recommendations/understanding-nsx-intelligence-recommendations.html (Retrieved: 2026-08-10T08:40:00Z)
[19] Broadcom. "Overview of the NSX Suspicious Traffic Feature (vDefend Security Intelligence 3.2 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/security-intelligence/3-2/using-and-managing-vmware-nsx-intelligence/detecting-suspicious-traffic-events-in-nsx/-preparing-for-detecting-suspicious-traffic-using-nsx-intelligence/overview-of-nsx-suspicious-traffic-feature.html (Retrieved: 2026-08-10T08:40:00Z)
[20] Broadcom. "Offline Downloading and Uploading Intrusion Detection Signatures (vDefend Advanced Threat Prevention 4.2 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-atp/4-2/nsx-ids-ips-and-nsx-malware-prevention/nsx-ids-ips-and-nsx-malware-prevention/offline-downloading-and-uploading-nsx-intrusion-detection-signatures.html (Retrieved: 2026-08-10T08:40:00Z)
[21] Broadcom. "Installing NSX Manager Cluster on vSphere (VMware NSX 4.2 Installation Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide/installing-nsx-manager-cluster-on-vsphere.html (Retrieved: 2026-08-10T08:40:00Z)
[22] Broadcom. "NSX Federation (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation.html (Retrieved: 2026-08-10T08:40:00Z)
[23] Broadcom. "Disaster Recovery for Global Manager (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/managing-nsx-t-in-multiple-locations/nsx-t-federation/disaster-recovery-using-federation.html (Retrieved: 2026-08-10T08:40:00Z)
[24] Broadcom. "Back up and restore NSX configured in VMware vCenter (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/operations-and-management/back-up-and-restore-nsx-configured-in-vcenter-server.html (Retrieved: 2026-08-10T08:40:00Z)
[25] Broadcom. "Integration of Kubernetes Clusters with Antrea CNI (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni.html (Retrieved: 2026-08-10T08:40:00Z)
[26] Broadcom. "Distributed Firewall Policies for Securing Traffic Within an Antrea Kubernetes Cluster (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/integration-of-kubernetes-clusters-with-antrea-cni/distributed-firewall-policies-for-securing-traffic-within-an-antrea-kubernetes-cluster.html (Retrieved: 2026-08-10T08:40:00Z)
[27] Broadcom. "Add Syslog Servers for NSX Nodes (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/operations-and-management/log-messages-and-error-codes/add-syslog-servers-for-nsx-nodes.html (Retrieved: 2026-08-10T08:40:00Z)
[28] Broadcom. "NSX API Authentication Using a Session Cookie (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/authentication-and-authorization/nsx-api-authentication-using-a-session-cookie.html (Retrieved: 2026-08-10T08:40:00Z)
[29] Broadcom. "Standards Compliance (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/operations-and-management/compliance-based-configurations.html (Retrieved: 2026-08-10T08:40:00Z)
[30] Broadcom. "Common Criteria Compliance (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/operations-and-management/compliance-based-configurations/common-criteria-compliance.html (Retrieved: 2026-08-10T08:40:00Z)
[31] Broadcom. "Certificates for NSX and NSX Federation (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/certificates/certificates-for-nsx-and-nsx-federation.html (Retrieved: 2026-08-10T08:40:00Z)
[32] Broadcom. "Using Aria Operations for Logs or Splunk for System Monitoring (VMware NSX 4.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/administration-guide/system-monitoring/using-aria-operations-for-logs-or-splunk-for-system-monitoring.html (Retrieved: 2026-08-10T08:40:00Z)
[33] Broadcom. "NSX Manager VM and Host Transport Node System Requirements (VMware NSX 4.2 Installation Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide/preparing-for-installation/system-requirements/nsx-manager-and-host-transport-node-system-requirements.html (Retrieved: 2026-08-10T08:40:00Z)
[34] PeerSpot. "VMware NSX Reviews (PeerSpot)". https://www.peerspot.com/products/vmware-nsx-reviews (Retrieved: 2026-08-10T08:40:00Z)
[35] NIST CSRC. "NIST CMVP Validated Modules Search (keyword: NSX)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&CertificateStatus=Active&ValidationYear=0&Keyword=nsx (Retrieved: 2026-08-10T08:40:00Z)
[36] Common Criteria Portal. "Common Criteria Portal - Certified Products List". https://www.commoncriteriaportal.org/products/index.cfm (Retrieved: 2026-08-10T08:40:00Z)
[37] Broadcom. "Distributed Firewall (NSX-T Data Center 3.2 Administration Guide)". https://techdocs.broadcom.com/us/en/vmware-cis/nsx/nsxt-dc/3-2/administration-guide/security/distributed-firewall.html (Retrieved: 2026-08-10T08:40:00Z)
[38] Broadcom. "Distributed Firewall Packet Logs (VMware vDefend Firewall 9.1 documentation)". https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend/vdefend-firewall/9-1/vdefend-distributed-firewall/monitoring-and-troubleshooting-dfw/firewall-packet-logs.html (Retrieved: 2026-08-10T08:40:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 30
- **Sources reviewed:** 38 (kept: 38, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, community: 1, vendor_datasheet: 1, vendor_doc: 34
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
