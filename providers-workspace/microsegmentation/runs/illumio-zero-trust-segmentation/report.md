# Microsegmentation Product Assessment: Illumio - Illumio Zero Trust Segmentation (Illumio Segmentation / Illumio Core)

**Product ID:** `illumio-zero-trust-segmentation`
**Version reference:** Illumio Core 26.x documentation set (SaaS 26.1 / On-Prem 25.2.x); VEN Install & Upgrade 24.4 PDF
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T08:52:09Z
**Total evidence items collected:** 100
**Total distinct sources:** 49

---

## 1. Overview

Illumio Zero Trust Segmentation (marketed since 2025 as "Illumio Segmentation"; the on-premises controller is Illumio Core / "Illumio Segmentation for Data Centers") is a host-agent microsegmentation platform built on the Policy Compute Engine (PCE) and Virtual Enforcement Nodes (VENs). VENs run on bare-metal, VM and container workloads, collect traffic flows and program OS-native firewalls (iptables/nftables, Windows Filtering Platform, IPFilter/Packet Filter) with label-based policy computed centrally by the PCE [1]. The platform adds agentless coverage through the Network Enforcement Node (NEN) for load balancers and switches [20] and container-native enforcement for Kubernetes/OpenShift via C-VEN and Kubelink [19]. Vendor positioning emphasizes real-time telemetry with AI-based policy recommendations [12]; Illumio was named a Leader in The Forrester Wave: Microsegmentation Solutions Q3 2024 and a 2026 Gartner Peer Insights Customers' Choice for Network Security Microsegmentation [47][48]. Deployments scale to 125,000 workloads per 4x2 PCE cluster [23][24], with optional PCE Superclusters spanning multiple sites [42].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 27    | 6                | 21     | 0   |
| partial          | 4     | 0                | 4      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 2     | 0                | 0      | 2   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 21 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | VENs automatically report workload properties, interfaces, processes and 10-minute flow snapshots to the PCE, which the product page describes as continuous automated segmentation; an independent review corroborates real-time flow visibility. [1], [4], [12], [49] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | high | - | The PCE Map groups workloads by labels (default dimensions Role, Application, Environment, Location) and shows the process/service name of each connection, so maps can be organized by app, environment, role and process. [2], [3], [4] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 90.0 days | Traffic-flow summaries are pruned only when their disk allocation is exceeded or the traffic database has been inactive for 90 days, so active environments retain flow history beyond 90 days; separate event data defaults to 30 days. [5], [6], [40] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | - | The Vulnerability Map overlays the App Group Map with Qualys (and other scanner) vulnerability data and shows exposure/attack paths per workload, with vulnerability data uploadable via CLI or REST API. [7], [8] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | - | Flow logs classify traffic as Allowed, Blocked or Potentially Blocked and the Illumination map marks new, unaddressed traffic as red lines; an independent review notes flow maps expose unexpected east-west paths. [4], [9], [10] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | - | Policies are written against labels (Role, Application, Environment, Location and custom dimensions) rather than IPs, and the policy model is label/scope-based; an independent review confirms policies are written against labels rather than IPs. [3], [4], [10] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | The Policy Advisor generates tailored policy recommendations with AI-powered analysis from observed traffic and labels, and the product page states telemetry plus AI recommend policies instantly. [11], [12] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | Illumination's Draft View previews the effect of a policy before enforcement, Idle/Visibility-only states monitor without blocking, and Static Policy stages rules without enforcing them, providing dry-run equivalents. [10], [11], [13], [14] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Supported | medium | - | Every provision is versioned and the Revert Immediately action rolls back and provisions an earlier version, with a Restore action to return to a known-good baseline. [14] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | The policy model supports scopeless policies (broad application) and scope-based policies that restrict rules to workload groups, including multi-scope and single-scope variants, giving a hierarchical policy structure. [15] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | medium | - | Dedicated VEN install/upgrade guides exist for AIX and Solaris (SPARC/x86_64), and the VEN Library supports RPM, Debian and Windows distributions, covering Windows Server, RHEL/CentOS and Ubuntu-class Linux. [16], [17], [18] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | high | - | A container-native solution (C-VEN DaemonSet + Kubelink) enforces policy at node and pod level for Kubernetes and OpenShift clusters, with iptables/nftables enforcement and Helm deployment. [4], [19] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | The Network Enforcement Node (NEN) extends visibility and policy enforcement to agentless workloads via load-balancer virtual servers and switch/router ACLs, complementing the agent-based VEN. [20] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | The on-premises PCE is self-contained: on-prem customers download VEN packages directly to the PCE, and VEN-to-PCE proxy support covers restricted networks, so no external internet connectivity is required for operation. [21], [22] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 125000.0 workloads | Capacity tables size a 2x2 PCE cluster for 10,000 VENs/50,000 workloads and a 4x2 cluster for 25,000 VENs/125,000 workloads; the object-limits table lists a 125,000-workload hard limit for 4x2 deployments. [23], [24] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | 2.0 cpu_percent | An Illumio engineering blog measured ~2% CPU overhead at 10,000 connections/second (higher than the 1% threshold at that load), while the VEN otherwise remains idle in the background; no idle/typical-load percentage is published. [1], [4], [25] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Supported | medium | 58.0 MB | The vendor's load test measured 37-58MB memory overhead at 10,000 connections/second, below the 100MB threshold; the cited upper bound is 58MB. [4], [25] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | The VEN does not process data packets in-line and uses no custom kernel modules, so its architecture adds no in-path latency, but no numeric latency figure is published to verify the <0.1ms threshold. [4], [26] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | high | - | Enforcement is programmed into OS-native kernel firewalls, policy remains in the kernel during VEN restarts, and AgentMonitor restarts failed VEN processes, so traffic is not disrupted on agent failure; an independent review notes enforcement is local to the workload. [1], [4], [27], [28] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Supported | medium | - | The Windows VEN installer ships a /norestart option and installs/upgrades via package managers with no reboot step in the documented procedures, and golden-image 'prepare script' installation activates at next boot rather than requiring a reboot. [18], [29] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | - | The REST API reference documents management of the PCE (auth, health, org settings, policy, workloads, provisioning, RBAC, visualization) via documented Public Stable APIs. [30], [31] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | PCE events forward over syslog in JSON (Splunk), CEF (ArcSight) and LEEF (QRadar) formats, with dedicated Splunk/QRadar apps and an Illumio Sentinel Solution (data connector, workbooks, playbooks). [32], [33] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | The Illumio App for CMDB (ServiceNow) ingests ServiceNow-discovered workloads into the PCE and synchronizes workload label updates between CMDB and PCE automatically and manually. [34] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | An official Terraform provider manages PCE objects (workloads, labels, IP lists, services, rules, enforcement boundaries, pairing profiles) as HCL, enabling infrastructure-as-code CI/CD pipelines; Jenkins/GitLab integration would go through the same REST API. [35] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | medium | - | Windows rules support process/service-based inbound definitions, and Linux process-based (eBPF) rules enforce outbound connections by process identity, giving process-level policy context on both platforms. [36], [37] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | - | no evidence found (No evidence found for native honeypot/deception or threat-intelligence feed integration.) |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Supported | medium | - | Policy Advisor applies compliance frameworks including PCI DSS, ISO 27001 and NIST CSF to recommended policies; Illumio publishes a NIST SP 800-207 ZTA mapping, and the Armis OT integration is aligned with IEC 62443 and NIST. [11], [38], [39] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | VEN-to-PCE communication is TLS-encrypted (HTTPS plus long-lived TLS channel) with the VEN authenticating via a unique agent token and validating the PCE certificate, but the documented default/maximum TLS version is 1.2, not 1.3. [18], [21], [40] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | 2x2/4x2 PCE clusters provide 1+1 redundancy (survive loss of one data node plus half the core nodes) with quorum-based leader election, and PCE Superclusters span multiple replicating sites that keep enforcing even if the leader is down. [41], [42] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | When the PCE is unreachable, the VEN continues to enforce the last-known-good policy while reconnecting, exiting its degraded state after connectivity is restored. [40] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | - | Active-standby PCE pairs with continuous real-time replication and periodic synchronization provide warm-standby disaster recovery, and the standby can be promoted to active on failure. [43] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | FIPS 140-2 compliance is supported for the PCE and Linux/Windows VENs (via validated OS crypto modules plus third-party affirmation letters), and Illumio Core is Common Criteria certified (NIAP, PP-compliant) per the CC portal; the certification is PP-based rather than EAL4+, and FIPS 140-3 is only documented for Flowlink. [44], [45], [46] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (No evidence found of industrial-software compatibility certifications from Siemens, Honeywell or ABB.) |

---

## 4. Notable Strengths

- **Label-driven policy model (items 2.1, 2.5):** policies are written against Role/Application/Environment/Location labels and scope-based rules rather than IPs or VLANs, with the Policy Advisor generating AI-analyzed recommendations [3][4][11].
- **Container and agentless coverage (items 3.2, 3.3):** C-VEN and Kubelink deliver native Kubernetes/OpenShift enforcement, and the NEN enforces policy on load balancers and switches where agents cannot be installed [19][20].
- **Scale and availability (items 3.5, 7.1, 7.3):** documented capacity to 125,000 workloads per 4x2 cluster, 1+1 redundant PCE clusters, and active-standby replication for disaster recovery [23][24][41][43].
- **Fail-safe agent architecture (item 4.4):** enforcement lives in OS-native kernel firewalls, persists across VEN restarts, and the AgentMonitor restarts failed processes, so agent failure does not disrupt traffic [1][27][28].
- **Compliance depth (items 6.3, 8.1):** the Policy Advisor applies PCI DSS, ISO 27001 and NIST CSF frameworks, an official NIST SP 800-207 mapping exists, and the platform supports FIPS 140-2 and holds NIAP Common Criteria certification [11][38][45][46].

## 5. Notable Gaps / Risks

- **VEN CPU overhead not under 1% at load (item 4.1):** the vendor's own test shows ~2% CPU at 10,000 connections/second, so buyers with strict <1% budgets should benchmark at their typical connection rates [25].
- **No quantified latency guarantee (item 4.3):** latency impact is described only qualitatively (no in-line packet processing); the <0.1ms threshold is unverified by any published measurement [26].
- **TLS 1.2, not TLS 1.3 (item 6.4):** VEN-to-PCE encryption and mutual authentication are documented on TLS 1.2, so requirements mandating TLS 1.3 are not met [21][40].
- **Common Criteria below EAL4+ and no FIPS 140-3 for PCE/VEN (item 8.1):** the CC portal listing is NIAP PP-compliant with no EAL rating, and FIPS 140-3 is documented only for Flowlink [44][45][46].
- **No honeypot/deception or OT-vendor certifications documented (items 6.2, 8.2):** no evidence of threat-intelligence/deception features or Siemens/Honeywell/ABB compatibility certifications was found; both remain unknown rather than confirmed absent.

## 6. Evidence Quality Notes

Evidence is dominated by official Illumio documentation: 41 of 49 cited sources are vendor_doc pages from the public product-docs-repo.illumio.com corpus (Core 26.x Admin, Install-Upgrade-Admin, Security-Policy, REST-APIs, Visualization and Integrations guides) plus vendor datasheets and blogs. Only 12 items are backed by two or more source_types; the remaining 21 items rely on vendor documentation alone, so their confidence is capped at medium. One genuinely independent third-party review (ContentWave, tagged third_party_review) corroborates several visibility, policy and enforcement items, and the Common Criteria portal entry (certification_registry) independently confirms the CC listing; the Forrester and Gartner landing pages are vendor-hosted summaries of analyst reports and were treated as such.

The main numeric tension is in Category 4: the only published VEN resource figure (~2% CPU and 37-58MB at 10,000 connections/second, from an Illumio engineering blog) drove 4.1 to partial because 2% exceeds the <1% threshold at that load, while 4.2 (58MB upper bound) is supported and 4.3 is partial because latency is only described qualitatively. For 8.1 the CC portal record shows "PP Compliant" with no EAL rating, which is why the item is partial despite FIPS 140-2 support being well documented. Items 6.2 and 8.2 were left unknown rather than not_supported because no source addresses them.

---

## Bibliography

[1] Illumio. "Illumio Administration Guide 26.x - VEN Architecture and Components". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/ven-administration-guide/overview-of-ven-administration/ven-architecture-and-components.html (Retrieved: 2026-08-10T08:52:09Z)
[2] Illumio. "Illumio Visualization Guide - Map View". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Visualization/out/en/visualization-tools/map-view.html (Retrieved: 2026-08-10T08:52:09Z)
[3] Illumio. "Illumio Security Policy Guide 26.x - Label Types". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/security-policy-objects/about-labels-and-label-groups/label-types.html (Retrieved: 2026-08-10T08:52:09Z)
[4] ContentWave. "Illumio Core 2026: Microsegmentation Review & Verdict (ContentWave)". https://contentwave.net/article/illumio-core-2026-review-microsegmentation-for-hybrid-zero-trust (Retrieved: 2026-08-10T08:52:09Z)
[5] Illumio. "Illumio Administration Guide 26.x - About the PCE Databases". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/pce-administration/pce-database-management/about-the-pce-databases.html (Retrieved: 2026-08-10T08:52:09Z)
[6] Illumio. "Illumio Administration Guide 26.x - Manage Data and Disk Capacity". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/pce-administration/manage-pce-nodes-and-clusters/manage-data-and-disk-capacity.html (Retrieved: 2026-08-10T08:52:09Z)
[7] Illumio. "Illumio Visualization Guide - About the Vulnerability Map". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Visualization/out/en/vulnerability-map/about-the-vulnerability-map.html (Retrieved: 2026-08-10T08:52:09Z)
[8] Illumio. "Illumio CLI Tool Guide - Upload Vulnerability Data". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/illumio-core-pce-cli-tool-guide-1-4-3/cli-tool-commands-for-resources/upload-vulnerability-data.html (Retrieved: 2026-08-10T08:52:09Z)
[9] Illumio. "Illumio Administration Guide 26.x - Traffic Flow Types and Properties". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/events-administration/traffic-flow-types-and-properties.html (Retrieved: 2026-08-10T08:52:09Z)
[10] Illumio. "Illumio Security Policy Guide 26.x - The Illumio Policy Model". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/overview-of-security-policy/the-illumio-policy-model.html (Retrieved: 2026-08-10T08:52:09Z)
[11] Illumio. "Illumio Security Policy Guide 26.x - Introducing the Policy Advisor". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/introducing-the-policy-advisor.html (Retrieved: 2026-08-10T08:52:09Z)
[12] Illumio. "Illumio Segmentation - product page". https://www.illumio.com/illumio-segmentation (Retrieved: 2026-08-10T08:52:09Z)
[13] Illumio. "Illumio Security Policy Guide 26.x - Illumio Policy Enforcement Model". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/illumio-policy-enforcement-model.html (Retrieved: 2026-08-10T08:52:09Z)
[14] Illumio. "Illumio Security Policy Guide 26.x - About Provisioning". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/about-provisioning.html (Retrieved: 2026-08-10T08:52:09Z)
[15] Illumio. "Illumio Security Policy Guide 26.x - Scope-based and Scopeless Policies". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/overview-of-security-policy/scope-based-and-scopeless-policies.html (Retrieved: 2026-08-10T08:52:09Z)
[16] Illumio. "Illumio Install/Upgrade Guide 26.x - AIX VEN Installation and Upgrade". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/ven-installation-and-upgrade/ven-installation---upgrade-with-ven-ctl/aix-ven-installation-and-upgrade-with-cli-and-ven-ctl.html (Retrieved: 2026-08-10T08:52:09Z)
[17] Illumio. "Illumio Install/Upgrade Guide 26.x - Solaris VEN Installation and Upgrade". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/ven-installation-and-upgrade/ven-installation---upgrade-with-ven-ctl/solaris--install-and-upgrade-with-cli-and-ven-ctl.html (Retrieved: 2026-08-10T08:52:09Z)
[18] Illumio. "Illumio Install/Upgrade Guide 26.x - Ways to Install the VEN". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/ven-installation-and-upgrade/overview-of-ven-installation/ways-to-install-the-ven.html (Retrieved: 2026-08-10T08:52:09Z)
[19] Illumio. "Illumio Install/Upgrade Guide 26.x - Overview of Containers (Kubernetes/OpenShift)". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/kubernetes-and-openshift/overview-of-containers/overview-of-containers.html (Retrieved: 2026-08-10T08:52:09Z)
[20] Illumio. "Illumio Install/Upgrade Guide 26.x - Overview of the NEN". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/nen-installation-and-usage-guide/introducing-the-illumio-network-enforcement-node/overview-of-the-nen.html (Retrieved: 2026-08-10T08:52:09Z)
[21] Illumio. "Illumio Install/Upgrade Guide 26.x - Prerequisites for VEN Installation". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/ven-installation-and-upgrade/prepare-for-ven-installation/prerequisites-for-ven-installation.html (Retrieved: 2026-08-10T08:52:09Z)
[22] Illumio. "Illumio Install/Upgrade Guide 26.x - VEN Proxy Support". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/ven-installation-and-upgrade/prepare-for-ven-installation/ven-proxy-support.html (Retrieved: 2026-08-10T08:52:09Z)
[23] Illumio. "Illumio Install/Upgrade Guide 26.x - PCE Capacity Planning". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/pce-installation-and-upgrade-guide/prepare-for-pce-installation/pce-capacity-planning.html (Retrieved: 2026-08-10T08:52:09Z)
[24] Illumio. "Illumio Administration Guide 26.x - PCE Default Object Limits". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/pce-administration/pce-database-management/pce-default-object-limits.html (Retrieved: 2026-08-10T08:52:09Z)
[25] Illumio. "Floats Like a Butterfly: How Illumio Ensures the VEN Stays Light (Illumio blog)". https://medium.com/@illumio/floats-like-a-butterfly-how-illumio-ensures-the-ven-stays-light-90e79b559732 (Retrieved: 2026-08-10T08:52:09Z)
[26] Illumio. "The Lightness of the Illumio VEN (Illumio blog)". https://medium.com/@illumio/the-lightness-of-the-illumio-ven-7c9491f81f5f (Retrieved: 2026-08-10T08:52:09Z)
[27] Illumio. "Illumio Administration Guide 26.x - VEN Startup and Shutdown". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/ven-administration-guide/ven-state/ven-startup-and-shutdown.html (Retrieved: 2026-08-10T08:52:09Z)
[28] Illumio. "Illumio Administration Guide 26.x - VEN Suspension". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/ven-administration-guide/ven-state/ven-suspension.html (Retrieved: 2026-08-10T08:52:09Z)
[29] Illumio. "Illumio VEN Install and Upgrade 24.4 (PDF)". https://product-docs-repo.illumio.com/Tech-Docs/Core/PDFs/VEN-Install-Upgrade.pdf (Retrieved: 2026-08-10T08:52:09Z)
[30] Illumio. "Illumio REST APIs 26.1 - About PCE Management". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/REST-APIs/out/en/rest-apis-26-1--saas-/about-pce-management.html (Retrieved: 2026-08-10T08:52:09Z)
[31] Illumio. "Illumio REST APIs 26.1 - API Classification and Version". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/REST-APIs/out/en/rest-apis-26-1--saas-/api-classification-and-version.html (Retrieved: 2026-08-10T08:52:09Z)
[32] Illumio. "Illumio Administration Guide 26.x - SIEM Integration for Events". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/events-administration/events-settings/siem-integration-for-events.html (Retrieved: 2026-08-10T08:52:09Z)
[33] Illumio. "Illumio Integrations Guide - Introduction to the Illumio Sentinel Solution". https://product-docs-repo.illumio.com/Tech-Docs/Integrations/out/en/illumio-sentinel-solution-3-4-1/introduction-to-the-illumio-sentinel-solution.html (Retrieved: 2026-08-10T08:52:09Z)
[34] Illumio. "Illumio App for CMDB v2.1.0 Installation and Configuration Guide (PDF)". https://product-docs-repo.illumio.com/Tech-Docs/Integrations/PDFs/ServiceNowCMDB-2.1.0.pdf (Retrieved: 2026-08-10T08:52:09Z)
[35] Illumio. "Terraform Provider for Illumio Core (GitHub README)". https://raw.githubusercontent.com/illumio/terraform-provider-illumio-core/main/README.md (Retrieved: 2026-08-10T08:52:09Z)
[36] Illumio. "Illumio Security Policy Guide 26.x - Windows Process-Based Rules". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/about-rules/windows-process-based-rules.html (Retrieved: 2026-08-10T08:52:09Z)
[37] Illumio. "Illumio Security Policy Guide 26.x - Linux Process-Based Flow Visibility and Outbound Policy Enforcement". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/about-rules/linux-process-based-flow-visibility-and-outbound-policy-enforcement.html (Retrieved: 2026-08-10T08:52:09Z)
[38] Illumio. "Mapping Illumio to NIST SP 800-207 Zero Trust Architecture". https://www.illumio.com/resource-center/mapping-illumio-to-nist-sp-800-207-zero-trust-architecture (Retrieved: 2026-08-10T08:52:09Z)
[39] Illumio. "How Illumio + Armis Secure Modern OT Environments (Illumio blog)". https://www.illumio.com/blog/how-illumio-armis-secure-modern-ot-environments (Retrieved: 2026-08-10T08:52:09Z)
[40] Illumio. "Illumio Administration Guide 26.x - VEN-to-PCE Communication". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/ven-administration-guide/ven-to-pce-communication.html (Retrieved: 2026-08-10T08:52:09Z)
[41] Illumio. "Illumio Administration Guide 26.x - PCE High Availability and Disaster Recovery Concepts". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/pce-administration/pce-high-availability-and-disaster-recovery/pce-high-availability-and-disaster-recovery-concepts.html (Retrieved: 2026-08-10T08:52:09Z)
[42] Illumio. "Illumio Install/Upgrade Guide 26.x - PCE Supercluster Concepts". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/pce-supercluster/about-supercluster-deployment/pce-supercluster-concepts.html (Retrieved: 2026-08-10T08:52:09Z)
[43] Illumio. "Illumio Administration Guide 26.x - PCE Replication and Failover". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Admin/out/en/pce-administration/pce-high-availability-and-disaster-recovery/pce-replication-and-failover.html (Retrieved: 2026-08-10T08:52:09Z)
[44] Illumio. "Illumio Install/Upgrade Guide 26.x - FIPS Compliance for PCE and VEN". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Install-Upgrade-Admin/out/en/pce-installation-and-upgrade-guide/pce-installation-reference--pce-runtime-parameters/fips-compliance-for-pce-and-ven.html (Retrieved: 2026-08-10T08:52:09Z)
[45] Illumio. "Illumio Certifications". https://www.illumio.com/resources/certifications (Retrieved: 2026-08-10T08:52:09Z)
[46] Common Criteria Portal (NIAP). "Common Criteria Portal - certified products search: Illumio". https://www.commoncriteriaportal.org/products/index.cfm?search=Illumio (Retrieved: 2026-08-10T08:52:09Z)
[47] Forrester (hosted by Illumio). "Illumio: A Leader in Microsegmentation (Forrester Wave Q3 2024 landing page)". https://www.illumio.com/resource-center/forrester-wave-microsegmentation (Retrieved: 2026-08-10T08:52:09Z)
[48] Gartner Peer Insights (hosted by Illumio). "Gartner Peer Insights Voice of the Customer for Network Security Microsegmentation 2026 (Illumio landing page)". https://www.illumio.com/resource-center/gartner-peer-insights-voice-of-the-customer-for-network-security-2026 (Retrieved: 2026-08-10T08:52:09Z)
[49] Illumio. "Illumio Security Policy Guide 26.x - Workload Enforcement States". https://product-docs-repo.illumio.com/Tech-Docs/Core/26.1/Security-Policy/out/en/illumio-security-policy-guide-26-x/workloads/workload-enforcement-states.html (Retrieved: 2026-08-10T08:52:09Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 49 (kept: 49, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 2, certification_registry: 1, third_party_review: 1, vendor_blog: 3, vendor_datasheet: 1, vendor_doc: 41
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
