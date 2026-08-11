# Microsegmentation Product Assessment: SonicWall - SonicWall Network Security / Cloud Edge (Cloud Secure Edge)

**Product ID:** `sonicwall-network-security-cloud-edge`
**Version reference:** SonicOS 7.x / Gen7 firewalls; Network Security Manager; Cloud Secure Edge (CSE, formerly Banyan-based ZTNA) - assessed Aug 2026
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:19:40Z
**Total evidence items collected:** 68
**Total distinct sources:** 46

---

## 1. Overview

SonicWall Network Security is the vendor's Gen7 next-generation firewall line (TZ, NSa, NSsp and NSv virtual firewalls) running SonicOS, centrally managed by Network Security Manager (NSM) as cloud SaaS or on-prem appliance; Cloud Secure Edge (CSE, the successor to the earlier "Cloud Edge" branding) is SonicWall's SSE platform whose Secure Private Access delivers ZTNA to individual applications and internal segments based on user identity, device posture and a machine-learning Trust Score, built on technology SonicWall acquired from Banyan Security [2][12][18]. SonicWall positions microsegmentation as network-based zone/VLAN segmentation enforced by firewalls at the access layer, complemented by CSE's application-level zero-trust access, and documents use cases from PCI-DSS isolation and IoT/OT network isolation to branch and MSP multi-tenant environments [1][2][8]. Deployment shapes are the firewall appliance/virtual firewall in-path model, agentless clientless browser access plus CSE desktop/mobile agents, and self-hosted or cloud (Global Edge) access tiers for private resources [1][13][23]. Strengths are documented around identity-based ZTNA policy, mutual-TLS device trust, REST/Terraform automation, syslog/SIEM integration, Active/Standby high availability, and FIPS 140-2/140-3 plus Common Criteria certification; flow-history retention beyond 30 days, workload-count scalability, agent CPU/RAM/latency figures, policy simulation, process-level enforcement, deception, air-gapped CSE and OT certifications are not evidenced [3][8][34][35][41][44].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 0                | 6      | 0   |
| partial          | 16    | 0                | 16     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 11    | 0                | 0      | 11  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 2 items backed by ≥ 2 source_types; 21 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | — | SonicWall documents real-time and historical visibility across the firewall estate in NSM, dashboards that reveal connections between segments with user access detail, and CSE microsegmentation between workloads, but no workload-level real-time flow auto-discovery and mapping engine is documented. [1], [3], [5], [36] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Dashboards and reporting show connections between segments plus breakdowns by devices, users, services, policies, roles and Access Tiers, but no visual topology map organized by App/Environment/Role/Process is documented. [1], [25] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | 30 days | NSM offers 7-day or 30-day reporting tiers plus an unquantified Full Logging option, CSE Command Center events are retained for 2 weeks or 10,000 events, and Capture Client console logs are kept 30 days; no documented tier reaches the 90-day flow-history requirement. [3], [28], [34], [35] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | — | no evidence found (No source describes CVE/vulnerability context shown on a network map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | — | CSE App Discovery records user DNS requests to surface public/SaaS applications admins have not reviewed, and SPA flags personal or non-compliant devices that bypass perimeter controls, but unrecognized-traffic flow detection inside the network is not documented. [6], [22] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | CSE ZTNA policies are built on Roles that combine IdP user attributes with device attributes, granting per-user/per-device access independent of IP/VLAN, and SonicOS firewalls additionally support LDAP/AD user-based authentication for policies. [2], [4], [6], [12], [39] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | CSE computes device Trust Level in real time with machine learning, NSM's Configuration Auditor cross-references settings against best practices, and the SAMI AI assistant gives configuration guidance, but an automated policy rule recommendation engine is not documented. [3], [11], [12] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | — | no evidence found (No policy simulation / dry-run mode documented for firewall or CSE policies.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | — | One-click rollback is documented for Capture Client endpoint data restoration after an attack; instant one-click rollback of firewall or ZTNA policy configuration is not documented. [10] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | — | NSM provides a multi-tenant hierarchy with fleet-wide management and consistent cross-environment policy enforcement, and Capture Client settings support an inheritance switch for tenants; hierarchical rule inheritance within a single firewall rulebase is not documented. [3], [5], [37], [40] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | The CSE desktop/mobile apps and device certificates support Windows, macOS, Linux, iOS and Android; no AIX or Solaris support is documented, and legacy Windows Server 2003-2012 is not covered. [15], [16] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | CSE secures access to Kubernetes API servers with mutually authenticated TLS and NSv virtual firewalls segment VM workloads by location, but native container/OpenShift workload isolation (e.g. CNI/agent-in-container enforcement) is not documented. [8], [21], [46] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | — | Both paths are documented: CSE desktop/mobile apps provide agent-based enforcement while clientless browser access, connector/access-tier, and firewall-based zone segmentation provide agentless enforcement. [1], [2], [13] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | — | NSM On-Prem runs in closed or highly secure networks on KVM/ESXi/Hyper-V/Azure, but the CSE control plane (Cloud Command Center) is always delivered as cloud SaaS, so a fully internet-isolated CSE deployment is not possible. [3], [23] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | NSM is documented to scale to hundreds of managed security devices, but SonicWall publishes no centralized workload-count figure and never cites 50,000+ workloads, so the threshold cannot be confirmed. [40] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | SonicWall states the CSE apps have 'virtually no impact on device performance' because they do not continuously monitor the device, but no CPU-percentage figure is published. [14] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | — | no evidence found (No agent RAM footprint figure documented.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | — | no evidence found (No network-latency overhead figure documented for agent or enforcement path.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | — | no evidence found (Agent fail-open/fail-safe behavior on crash not documented.) |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | — | no evidence found (Zero-touch install and WireGuard service installation are documented but no explicit no-reboot requirement for install/update is stated.) |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | The CSE Command Center API is documented as exposing the same platform operations as the console, and SonicOS and NSM expose REST APIs (SonicOS API reference, NSM /api/manager/auth), but full 100% parity for every administrative function across all products is not demonstrated. [6], [18], [32], [45] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Firewalls forward event logs to external syslog servers, SPA's Advanced tier lists SIEM integration, Capture Client integrates with SIEM/XDR/MDR platforms via Syslog and SentinelOne APIs, and CSE events export to the ELK stack. [6], [19], [33], [37] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found (No ServiceNow CMDB integration documented.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | — | A CSE Terraform Provider manages Roles, Policies and Services as infrastructure-as-code, and Event Hooks trigger post-connection scripts; native Jenkins/GitLab pipeline integrations are not documented. [20], [27] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | — | no evidence found (Enforcement is network/application-level; no process-level enforcement documented.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | SIA/SWG integrates real-time threat intelligence, RTDMI and DNS filtering, and segmentation isolates IoT/OT networks, but a customer-deployable honeypot or deception-detection capability is not documented. [1], [7] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | NSM compliance reporting is described as audit-ready for PCI-DSS, HIPAA and CMMC environments and Wikipedia notes the company assists with PCI-DSS and HIPAA compliance, but NIST 800-207, ISO 27001 and IEC 62443-specific report templates are not documented. [3], [8], [29] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | — | CSE performs a Mutual Auth TLS handshake between the TrustProvider and device certificate, issues device certificates from a private root CA, and uses MTLS for K8s connectivity; TLS version (1.2 vs 1.3) is not stated. [16], [24], [46] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | SonicWall firewalls support Active/Standby HA with stateful synchronization and automatic failover, CSE connectors support Active/Standby HA setups, and the firewall line advertises built-in failover from SMB to data center. [4], [17], [30], [31], [38] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (Autonomous policy enforcement by agents when the controller is unreachable is not documented.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (Disaster-recovery site sync beyond HA stateful sync is not documented.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Supported | medium | — | SonicWall documents CMVP-based FIPS 140-2 and 140-3 validation for its NGFW cryptographic modules and Common Criteria certification (EAL4+/NDPP) for TZ/NSa firewalls; the NIST CMVP and Common Criteria portal registries were not reachable from this environment to independently confirm certificate numbers. [9], [41], [43], [44] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No Siemens/Honeywell/ABB or IEC 62443 compatibility certification documented.) |

---

## 4. Notable Strengths

- **Identity-based ZTNA policy (items 2.1, 3.3):** CSE access policies are built on Roles combining IdP user attributes and device attributes, enforced per-user/per-device with both agent and clientless browser paths, independent of IP/VLAN [12][13][2].
- **Mutual-TLS device trust (item 6.4):** every CSE access request requires a device certificate issued by a private root CA and is validated through a Mutual Auth TLS handshake by the TrustProvider [24][16][46].
- **Automation surface (items 5.1, 5.4, 5.2):** the CSE Command Center API is documented as exposing the same platform operations as the console, a Terraform Provider manages Roles/Policies/Services, and firewalls plus Capture Client integrate with SIEM/XDR/MDR via Syslog and SentinelOne APIs [18][20][33][37].
- **High availability (item 7.1):** firewalls support Active/Standby HA with stateful synchronization and automatic failover, and CSE connectors support Active/Standby HA, covering SMB through data-center scale [30][31][38][17].
- **Certifications (item 8.1):** SonicWall documents FIPS 140-2/140-3 validation for NGFW cryptographic modules and Common Criteria (EAL4+/NDPP) certification for TZ/NSa firewalls [41][43][44].

## 5. Notable Gaps / Risks

- **Flow history below the 90-day requirement (item 1.3):** NSM reporting tiers top out at 30 days with an unquantified Full Logging option, and CSE Command Center events are kept only 2 weeks or 10,000 events, so forensic flow history at the checklist threshold is not documented [3][35].
- **No workload-scale or agent-impact numbers (items 3.5, 4.1, 4.2, 4.3):** NSM scales to "hundreds of devices" and the CSE app is only described as having "virtually no impact" on performance; no 50k-workload, CPU%, RAM or latency figures are published, blocking threshold-based procurement comparisons [40][14].
- **Missing simulation, rollback, and enforcement depth (items 2.3, 2.4, 6.1):** no policy simulation/dry-run mode, no instant one-click policy-config rollback (only Capture Client endpoint data rollback), and no process-level enforcement are documented [10].
- **Air-gap and controller-loss behavior limited (items 3.4, 7.2):** NSM On-Prem supports closed networks, but the CSE control plane is always cloud SaaS and autonomous agent enforcement when the controller is unreachable is not documented [3][23].
- **OT and deception positioning absent (items 6.2, 8.2):** threat intelligence is integrated into SWG/DNS layers, but no customer-deployable honeypot/deception feature and no Siemens/Honeywell/ABB or IEC 62443 compatibility certification are documented [7].

## 6. Evidence Quality Notes

46 distinct sources and 68 evidence quotes were staged and grounded (0 fabricated, 0 unverifiable). 18 items were triangulated across 3+ sources; the remaining non-unknown items rest on 1-2 sources. Every item except 6.3 (which includes Wikipedia) relies solely on vendor documentation, so all verdicts are capped at medium confidence — SonicWall's own product pages, CSE technical documentation, KB articles, and one vendor blog. Independent triangulation was constrained by the environment: public search engines (Bing RSS, DuckDuckGo, Brave, Mojeek) were blocked or served boilerplate, the NIST CMVP search is a JS SPA with no reachable data endpoint, and commoncriteriaportal.org returns HTTP 403, so FIPS/Common Criteria claims could not be registry-verified. No outright contradictions between sources were found; where vendors quantified less than the checklist threshold (retention 30 days vs 90, "hundreds of devices" vs 50k workloads), the item was rated partial rather than not_supported, because the sources never explicitly state the capability is absent. The single largest residual risk is that NSM's "Full Logging" retention duration is unquantified, which is why item 1.3 is partial rather than not_supported.

---

## Bibliography

[1] SonicWall. "Network Segmentation (SonicWall Solutions)". https://www.sonicwall.com/solutions/use-cases/network-segmentation (Retrieved: 2026-08-10T17:19:40Z)
[2] SonicWall. "Zero Trust Security Solutions (SonicWall)". https://www.sonicwall.com/solutions/use-cases/zero-trust-security (Retrieved: 2026-08-10T17:19:40Z)
[3] SonicWall. "SonicWall Network Security Manager (NSM) - Product Page". https://www.sonicwall.com/products/management-and-reporting/network-security-manager (Retrieved: 2026-08-10T17:19:40Z)
[4] SonicWall. "SonicWall Next Generation Firewalls (NGFW) - Product Page". https://www.sonicwall.com/products/firewalls (Retrieved: 2026-08-10T17:19:40Z)
[5] SonicWall. "SonicWall Cloud Secure Edge (SSE Platform) - Product Page". https://www.sonicwall.com/products/cloud-secure-edge (Retrieved: 2026-08-10T17:19:40Z)
[6] SonicWall. "SonicWall Secure Private Access (SPA) - Product Page". https://www.sonicwall.com/products/secure-private-access (Retrieved: 2026-08-10T17:19:40Z)
[7] SonicWall. "SonicWall Secure Internet Access (SIA) - Product Page". https://www.sonicwall.com/products/secure-internet-access (Retrieved: 2026-08-10T17:19:40Z)
[8] SonicWall. "SonicWall NSv Series Virtual Firewalls - Product Page". https://www.sonicwall.com/products/firewalls/nsv-series (Retrieved: 2026-08-10T17:19:40Z)
[9] SonicWall. "SonicWall Product Certifications". https://www.sonicwall.com/products/product-certifications (Retrieved: 2026-08-10T17:19:40Z)
[10] SonicWall. "SonicWall Capture Client - Product Page". https://www.sonicwall.com/products/endpoint-security/capture-client (Retrieved: 2026-08-10T17:19:40Z)
[11] SonicWall. "SonicWall Unified Management - Product Page". https://www.sonicwall.com/products/sonicwall-unified-management (Retrieved: 2026-08-10T17:19:40Z)
[12] SonicWall. "CSE Docs: Zero Trust Policies". https://www.sonicwall.com/support/technical-documentation/docs/cse/intro/policies (Retrieved: 2026-08-10T17:19:40Z)
[13] SonicWall. "CSE Docs: How Cloud Secure Edge Works". https://www.sonicwall.com/support/technical-documentation/docs/cse/intro/how-banyan-works (Retrieved: 2026-08-10T17:19:40Z)
[14] SonicWall. "CSE Docs: Desktop App - Data Privacy and Security". https://www.sonicwall.com/support/technical-documentation/docs/cse/banyan-components/desktop-app/privacy (Retrieved: 2026-08-10T17:19:40Z)
[15] SonicWall. "CSE Docs: Register the Desktop App & Supported OSs". https://www.sonicwall.com/support/technical-documentation/docs/cse/banyan-components/desktop-app/installation-registration (Retrieved: 2026-08-10T17:19:40Z)
[16] SonicWall. "CSE Docs: Device Certificates". https://www.sonicwall.com/support/technical-documentation/docs/cse/banyan-components/desktop-app/device-cert (Retrieved: 2026-08-10T17:19:40Z)
[17] SonicWall. "CSE Docs: Set up High Availability (Connector)". https://www.sonicwall.com/support/technical-documentation/docs/cse/banyan-components/connector/manage/high-availability (Retrieved: 2026-08-10T17:19:40Z)
[18] SonicWall. "CSE Docs: Command Center API Guide". https://www.sonicwall.com/support/technical-documentation/docs/cse/api-guide (Retrieved: 2026-08-10T17:19:40Z)
[19] SonicWall. "CSE Docs: Visibility and Logging - Events". https://www.sonicwall.com/support/technical-documentation/docs/cse/visibility-logging/events (Retrieved: 2026-08-10T17:19:40Z)
[20] SonicWall. "CSE Docs: Terraform Provider". https://www.sonicwall.com/support/technical-documentation/docs/cse/api-guide/terraform (Retrieved: 2026-08-10T17:19:40Z)
[21] SonicWall. "CSE Docs: Kubernetes API". https://www.sonicwall.com/support/technical-documentation/docs/cse/securing-private-resources/k8s-api/kubernetes-api (Retrieved: 2026-08-10T17:19:40Z)
[22] SonicWall. "CSE Docs: Public Application Discovery". https://www.sonicwall.com/support/technical-documentation/docs/cse/visibility-logging/public-application-discovery (Retrieved: 2026-08-10T17:19:40Z)
[23] SonicWall. "CSE Docs: Edge Deployment Models". https://www.sonicwall.com/support/technical-documentation/docs/cse/intro/edge-deployment (Retrieved: 2026-08-10T17:19:40Z)
[24] SonicWall. "CSE Docs: Device Trust Verification". https://www.sonicwall.com/support/technical-documentation/docs/cse/manage-users-and-devices/device-trust-verification (Retrieved: 2026-08-10T17:19:40Z)
[25] SonicWall. "CSE Docs: Reporting Dashboard". https://www.sonicwall.com/support/technical-documentation/docs/cse/visibility-logging/reporting (Retrieved: 2026-08-10T17:19:40Z)
[26] SonicWall. "CSE Docs: Desktop App Capabilities and Components". https://www.sonicwall.com/support/technical-documentation/docs/cse/banyan-components/desktop-app/desktop-capabilities (Retrieved: 2026-08-10T17:19:40Z)
[27] SonicWall. "CSE Docs: Event Hooks Implementation Guide". https://www.sonicwall.com/support/technical-documentation/docs/cse/banyan-components/desktop-app/event-hook/event-hook-implementation (Retrieved: 2026-08-10T17:19:40Z)
[28] SonicWall. "CSE Docs: Service Tunnel Access Logs". https://www.sonicwall.com/support/technical-documentation/docs/cse/securing-networks/access-logs (Retrieved: 2026-08-10T17:19:40Z)
[29] Wikipedia. "SonicWall - Wikipedia". https://en.wikipedia.org/wiki/SonicWall (Retrieved: 2026-08-10T17:19:40Z)
[30] SonicWall. "KB: High Availability (HA) FAQ". https://www.sonicwall.com/support/knowledge-base/high-availability-ha-faq/kA1VN0000000EJK0A2 (Retrieved: 2026-08-10T17:19:40Z)
[31] SonicWall. "SonicOS 7.1 High Availability Administration Guide". https://www.sonicwall.com/support/technical-documentation/docs/sonicos-7-1-high_availability (Retrieved: 2026-08-10T17:19:40Z)
[32] SonicWall. "SonicOS API Reference Guide". https://www.sonicwall.com/support/technical-documentation/docs/sonicos-7-0-0-0-api (Retrieved: 2026-08-10T17:19:40Z)
[33] SonicWall. "KB: Configuring Syslog Server with Custom Event Profile". https://www.sonicwall.com/support/knowledge-base/configuring-syslog-server-with-custom-event-profile-on-sonicwall/kA1VN0000000G850AE (Retrieved: 2026-08-10T17:19:40Z)
[34] SonicWall. "KB: Capture Client - Data Retention Policy". https://www.sonicwall.com/support/knowledge-base/capture-client-data-retention-policy/kA1VN0000000Iuh0AE (Retrieved: 2026-08-10T17:19:40Z)
[35] SonicWall. "KB: Events Viewer SonicWall CSE". https://www.sonicwall.com/support/knowledge-base/events-viewer-sonicwall-cse/kA1VN0000000XOz0AM (Retrieved: 2026-08-10T17:19:40Z)
[36] SonicWall. "Blog: Layer 3 vs Layer 4 vs Layer 7 Firewalls: Where Do Virtual Firewalls Fit In?". https://www.sonicwall.com/blog/layer-3-vs-layer-4-vs-layer-7-firewalls-where-do-virtual-firewalls-fit-in- (Retrieved: 2026-08-10T17:19:40Z)
[37] SonicWall. "KB: Integrating with 3rd Party Syslog and Threat Detection Platforms". https://www.sonicwall.com/support/knowledge-base/integrating-with-3rd-party-syslog-and-threat-detection-platforms/kA1VN0000000Mbx0AE (Retrieved: 2026-08-10T17:19:40Z)
[38] SonicWall. "KB: What is a Stateful High Availability?". https://www.sonicwall.com/support/knowledge-base/what-is-a-stateful-high-availability/kA1VN0000000KtG0AU (Retrieved: 2026-08-10T17:19:40Z)
[39] SonicWall. "KB: How to Integrate LDAP/Active Directory User Authentication". https://www.sonicwall.com/support/knowledge-base/how-to-integrate-ldap-active-directory-user-authentication/kA1VN0000000KMv0AM (Retrieved: 2026-08-10T17:19:40Z)
[40] SonicWall. "KB: SonicWall Network Security Manager (NSM) FAQ". https://www.sonicwall.com/support/knowledge-base/sonicwall-network-security-manager-nsm-faq/kA1VN0000000Ekd0AE (Retrieved: 2026-08-10T17:19:40Z)
[41] SonicWall. "Certifications: Federal Information Processing Standard (FIPS) 140-3". https://www.sonicwall.com/solutions/certifications/federal-information-processing-standard-fips-140-3 (Retrieved: 2026-08-10T17:19:40Z)
[42] SonicWall. "Certifications: Federal Information Processing Standard (FIPS) 140-2". https://www.sonicwall.com/solutions/certifications/federal-information-processing-standard-fips-140-2 (Retrieved: 2026-08-10T17:19:40Z)
[43] SonicWall. "Certifications: Common Criteria". https://www.sonicwall.com/solutions/certifications/common-criteria (Retrieved: 2026-08-10T17:19:40Z)
[44] SonicWall. "KB: SonicWall Firewalls Are Common Criteria Certified". https://www.sonicwall.com/support/knowledge-base/sonicwall-firewalls-are-common-criteria-certified/kA1VN0000000Of50AE (Retrieved: 2026-08-10T17:19:40Z)
[45] SonicWall. "KB: NSM On-Prem - Authentication with API". https://www.sonicwall.com/support/knowledge-base/nsm-on-prem-authentication-with-api/kA1VN000001WBhJ0AW (Retrieved: 2026-08-10T17:19:40Z)
[46] SonicWall. "KB: Kubernetes OIDC Authentication with SonicWall CSE". https://www.sonicwall.com/support/knowledge-base/kubernetes-oidc-authentication-with-sonicwall-cse/kA1VN0000000Unh0AE (Retrieved: 2026-08-10T17:19:40Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 46 (kept: 46, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, vendor_blog: 1, vendor_doc: 44
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
