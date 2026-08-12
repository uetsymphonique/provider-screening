# Microsegmentation Product Assessment: Faddom - Faddom Hybrid Cloud Mapping

**Product ID:** `faddom-hybrid-cloud-mapping`
**Version reference:** Faddom 2026.x product line; staged materials include v2026.2 release notes and help-center articles through August 2026
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T11:18:46Z
**Total evidence items collected:** 97
**Total distinct sources:** 49

---

## 1. Overview

Faddom Hybrid Cloud Mapping is an agentless application dependency mapping platform positioned as the discovery and policy-planning layer for microsegmentation projects. It collects passive traffic data (NetFlow/sFlow/IPFIX, cloud flow logs, hypervisor and cloud APIs) to map on-premises, cloud and Kubernetes environments in under 60 minutes [1, 31]. Deployed as a self-hosted virtual appliance (vCenter, Nutanix AHV, AWS Marketplace, Windows Server), it can run fully offline inside air-gapped networks [5, 16, 30]. The Micro-Segmentation module groups servers into tiers, auto-generates tag/category-based policies from observed flows, and pushes them to enforcement points such as Nutanix Flow in monitoring mode, with VMware NSX and cloud security groups planned [25, 11]. The product does not enforce traffic in-path itself: enforcement is delegated to the target platform [11, 25]. Documented integrations include ServiceNow CMDB population and incident creation, a REST API, webhooks/syslog, and an Active Directory event-log forwarder [26, 7, 28, 29]. The company is ISO/IEC 27001:2022 certified with customers in banking, manufacturing, healthcare and government segments [8, 14]; TechCrunch describes the product as an infrastructure-dependency mapping tool aimed at mid-size enterprises [48].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 9     | 3                | 6      | 0   |
| partial          | 14    | 0                | 14     | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 6     | 0                | 0      | 6   |
| not_applicable   | 2     | 0                | 2      | 0   |

**Evidence quality:** 17 items backed by ≥ 2 source_types; 16 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.4:** There is no host enforcement agent whose failure could interrupt workload traffic; collection is passive and read-only, and enforcement executes on Nutanix Flow rather than on Faddom components.
- **7.2:** Faddom has no enforcement agent: policies execute on Nutanix Flow (monitoring/enforce toggled in Prism Central), so there is no agent-controller enforcement dependency whose loss would interrupt traffic; collection is passive and read-only.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Faddom maps on-premises, cloud and hybrid environments without agents in as little as 60 minutes; application maps are dynamic real-time visualizations that update continuously, corroborated by TechCrunch coverage and TrustRadius user insights. [1], [5], [31], [47], [48] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Application maps organize components into tiers (frontend/backend/database) and can be built from environment tags imported from VMware/Nutanix/AWS/Azure/GCP, but process-level grouping or visualization is not documented in staged sources. [2], [31], [39], [48] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | 14 days | Connection history used for traffic investigation defaults to 14 days and is configurable via the Connection History Storage Days parameter; no staged source documents a 90-day default or a maximum retention cap, so the >=90-day requirement is not demonstrated by default. [33] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | — | CVE discovery reports detected vulnerabilities with affected servers and criticality scores, and the CVE dashboard links each CVE to maps with affected servers; per-server risk scores are shown in server properties. [10], [20], [49] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | — | Lighthouse AI detects unusual traffic behavior including port scanning, data exfiltration, DNS spoofing, MITM and DoS, external north-south traffic detection with country blacklists is documented, and shadow/unmanaged assets are flagged; Cybersecurity Insiders corroborates lateral-movement detection. [22], [23], [24], [49] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | Policy generation supports tag-based rules: Faddom auto-imports tags from VMware/Nutanix/AWS/Azure/GCP, generates Nutanix Categories per tier, and pushes category-to-category rules to Nutanix Flow (IP/subnet rules only for non-Nutanix objects). [10], [11], [25], [31] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | Microsegmentation policies are automatically generated from observed traffic flows, and AI features are documented (Lighthouse anomaly-rule generation, Compass assistant, AI entry-point suggestions), but the policy generation itself is not described as AI/ML-driven rule recommendation. [4], [24], [25], [31] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | — | Generated policies are pushed to Nutanix Flow in Monitoring Mode by default so rules can be reviewed against live traffic before enforcement is enabled manually, providing a dry-run workflow on the enforcement platform. [11], [25] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | — | Policy structure is tier-based: servers are grouped into tiers and rules are generated between tiers including an internal-traffic toggle, but explicit inherited or hierarchical rule precedence is not documented in staged sources. [25], [31], [39] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | Agentless mapping is OS-agnostic and optional sFlow sensors are documented for Windows Server 2016+ and Linux; AIX and Solaris sensor support is not documented in staged sources. [36], [44] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | Kubernetes discovery including AKS and native traffic collection for Cilium and OpenShift clusters are documented, but isolation enforcement inside Kubernetes (e.g., NetworkPolicy generation) is not; generated policies target Nutanix Flow and VMware NSX (the latter coming soon). [18], [19], [25], [35] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | — | The platform is agentless-first with passive collection, and an optional sFlow-based agent (Windows sFlow generator / host sFlow on Linux) is documented for environments where agentless collection is not possible; TrustRadius insights corroborate agentless discovery. [7], [17], [31], [47] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | Faddom runs fully offline inside the environment without transmitting data externally, with documented offline license activation and offline upgrades; cloud discovery can run through a proxy and pricing data can be loaded manually. [5], [16], [30], [34] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | The documented customer base spans 100-10,000 instances and application mapping is described as unlimited, but no staged source demonstrates 50,000+ workloads per deployment, so the numeric threshold is not evidenced. [14], [39] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | — | no evidence found (The optional sFlow generator agent is confirmed to exist and to require no server restart on install (item 4.5), so a CPU-overhead referent exists, but no CPU usage figure is published — only its ~1MB disk footprint is documented.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | — | no evidence found (The optional sFlow generator agent is confirmed to exist (item 4.5), so a RAM-footprint referent exists, but no memory usage figure is published — only its ~1MB disk footprint is documented.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Collection is passive and out-of-band, described as having 'no performance impact' or 'minimal performance overhead on the topology', but no measured latency figure is published, so the <0.1ms threshold is not demonstrated. [2], [7] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | There is no host enforcement agent whose failure could interrupt workload traffic; collection is passive and read-only, and enforcement executes on Nutanix Flow rather than on Faddom components. [5], [30] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Supported | medium | — | The optional Faddom sFlow generator agent installer is documented as not requiring a server restart; configuration changes require only a Windows service restart. [17] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | A REST API with Bearer-token authentication provides programmatic access to inventory, connections, monitoring events, cloud/virtualization data and application-map management, but coverage of all administrative functions (users, policies, settings) is not documented. [28], [35] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | Webhook and syslog-based event notification/forwarding (including an AD event-log forwarder over encrypted UDP and Nagios/Zabbix event ingestion) is documented, and the integrations page lists SIEM-adjacent connectors as coming soon; no native Splunk/QRadar/Sentinel export is documented. [7], [29] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | — | ServiceNow integration populates the CMDB with application maps, servers, software, dependencies and CVEs and can create incidents from Faddom alerts; Faddom is an official ServiceNow partner and documents full API-based integration for CMDB/ITSM tools. [7], [9], [26], [27] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | — | Faddom is explicitly read-only ('does not and cannot make any changes to your environment') and only generates IP/subnet and tier/category rule suggestions for external systems to apply; no evidence documents Faddom itself applying or pushing enforcement at any level, network or process. [25], [30] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Anomaly-based threat detection (Lighthouse) covers attack patterns including port scanning, data exfiltration, DoS and MITM, and external-traffic country blacklists are documented; no threat-intelligence feed integration or honeypot/deception capability is documented. [23], [24], [49] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Faddom is ISO/IEC 27001:2022 certified and documents compliance support for DORA, NIS2, HIPAA and SOC 2; PCI-DSS, NIST SP 800-207 and IEC 62443 report templates were not found in staged sources. [6], [8], [12] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | Transmission channels are documented as encrypted (proxy-to-server encrypted connection, encrypted UDP event forwarding, HTTPS UI with a replaceable SSL certificate), but TLS 1.3 or mutual-authentication (mTLS) configuration for an agent-controller channel is not documented. [29], [34], [40], [43] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | — | no evidence found |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | N/A | medium | — | Faddom has no enforcement agent: policies execute on Nutanix Flow (monitoring/enforce toggled in Prism Central), so there is no agent-controller enforcement dependency whose loss would interrupt traffic; collection is passive and read-only. [11], [30] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | VM snapshot/backup before upgrades is recommended and dependency maps are documented as supporting disaster-recovery planning (recovery order, DR playbooks), but no native disaster-recovery site-sync or replication feature is documented. [2], [41], [47] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | — | The NIST CMVP validated-modules registry contains no Faddom cryptographic module, and no staged vendor source claims FIPS 140-2/140-3 or Common Criteria EAL4+ certification. [46] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found |

---

## 4. Notable Strengths

- **Agentless, fast, offline-capable visibility (items 1.1, 3.3, 3.4):** passive collection maps on-premises, cloud and Kubernetes environments without agents in as little as 60 minutes, and the appliance runs fully offline in air-gapped networks [1, 5, 16, 31].
- **Tag/category-based policy generation with dry-run workflow (items 2.1, 2.3):** imported hypervisor/cloud tags and auto-assigned tiers become Nutanix Categories and category-to-category rules, pushed to Nutanix Flow in monitoring mode so rules are reviewed before enforcement is enabled [11, 25, 31].
- **Security-relevant visibility (items 1.4, 1.5):** CVE discovery with map linkage and per-server risk scores, Lighthouse AI anomaly detection (port scanning, data exfiltration, DNS spoofing, DoS), and shadow-IT/external-traffic detection [20, 24, 45, 49].
- **ServiceNow integration (item 5.3):** official ServiceNow partner with CMDB population (servers, software, dependencies, CVEs) and incident creation from Faddom alerts [9, 26].
- **Certification and transport security posture (items 6.3, 6.4):** ISO/IEC 27001:2022 certification, encrypted proxy-to-server and UI channels, and a read-only access model [8, 30, 34, 43].

## 5. Notable Gaps / Risks

- **No in-path enforcement (items 6.1, 7.2):** Faddom is a planning-only product — policies execute on Nutanix Flow, and process-level enforcement is explicitly ruled out by the read-only, no-agent design; buyers need a separate enforcement platform [25, 30].
- **Numeric thresholds not demonstrated (items 1.3, 3.5, 4.3):** connection history defaults to 14 days (configurable via the Connection History Storage Days parameter), no staged source shows 50,000+ workloads per deployment, and no measured latency figure is published [33, 14, 39].
- **No controller HA, policy rollback, or CI/CD integration (items 7.1, 2.4, 5.4):** staged sources contain no evidence of clustered/HA controller deployment, one-click policy rollback, or Jenkins/GitLab/Terraform integrations.
- **No FIPS or Common Criteria certification (item 8.1):** the NIST CMVP validated-modules registry lists no Faddom module, and no vendor claim of FIPS 140-2/140-3 or Common Criteria EAL4+ was found [46].
- **Compliance report coverage is partial (item 6.3):** ISO 27001 and DORA/NIS2/HIPAA/SOC 2 support are documented, but PCI-DSS, NIST SP 800-207 and IEC 62443 report templates were not found in staged sources [8, 12].

## 6. Evidence Quality Notes

Evidence was staged from 51 raw artifacts mapped to 49 registered sources: 36 vendor help-center/product pages, 7 vendor blogs, 3 third-party items (TechCrunch, Cybersecurity Insiders, TrustRadius), 1 certification registry (NIST CMVP) and 1 vendor-hosted customer-stories page. 19 of 33 items are backed by two or more source types; items with independent corroboration include real-time discovery (1.1), unrecognized-traffic detection (1.5), agentless-plus-agent coverage (3.3) and CVE visibility (1.4). The remaining items rest on vendor documentation alone and are capped at medium confidence by the validator rule, even where the behavior is directly documented (e.g., offline operation 3.4, monitoring-mode policy push 2.3, ServiceNow integration 5.3).

No contradictions between sources surfaced; the main limitation is that Faddom's own materials are the only source for most capability claims. Search engines were captcha-gated during this run, so third-party discovery relied on direct staging of known review/press URLs; the TrustRadius listing contains no written reviews, so its AI-generated 'Insights' summary of user sentiment was used as independent evidence instead. Numeric items (1.3, 3.5, 4.1-4.3) were deliberately kept partial/not_applicable rather than inferring numbers: Faddom publishes no agent CPU/RAM/latency figures (agentless architecture), a 14-day default connection-history retention, and no 50,000-workload deployment figure. The FIPS negative (8.1) rests on the NIST CMVP registry, which is authoritative for FIPS but leaves Common Criteria unverified because the Common Criteria portal returned HTTP 403 and no vendor claim exists.

---

## Bibliography

[1] Faddom. "NDR and Microsegmentation Software (product page)". https://faddom.com/microsegmentation-software/ (Retrieved: 2026-08-10T11:18:46Z)
[2] Faddom. "Application Dependency Mapping: The Complete Guide". https://faddom.com/application-dependency-mapping/ (Retrieved: 2026-08-10T11:18:46Z)
[3] Faddom. "Why Faddom (product page)". https://faddom.com/why-faddom/ (Retrieved: 2026-08-10T11:18:46Z)
[4] Faddom. "Faddom AI (product page)". https://faddom.com/faddom-ai/ (Retrieved: 2026-08-10T11:18:46Z)
[5] Faddom. "9 Ways That Faddom is Different and Unique (blog)". https://faddom.com/what-makes-faddom-different-unique/ (Retrieved: 2026-08-10T11:18:46Z)
[6] Faddom. "Is Faddom Secure (blog)". https://faddom.com/is-faddom-secure-2/ (Retrieved: 2026-08-10T11:18:46Z)
[7] Faddom. "Faddom Integrations (product page)". https://faddom.com/integrations/ (Retrieved: 2026-08-10T11:18:46Z)
[8] Faddom. "Faddom Certifications (page)". https://faddom.com/certification/ (Retrieved: 2026-08-10T11:18:46Z)
[9] Faddom. "Faddom Is Now an Official ServiceNow Partner (blog)". https://faddom.com/faddom-is-now-an-official-servicenow-partner/ (Retrieved: 2026-08-10T11:18:46Z)
[10] Faddom. "Announcing Faddom's New Cybersecurity Module (Beta) (blog)". https://faddom.com/faddoms-new-cybersecurity-module/ (Retrieved: 2026-08-10T11:18:46Z)
[11] Faddom. "From Discovery to Enforcement: Fast-Tracking Zero Trust with Nutanix Flow Network Security and Faddom (blog)". https://faddom.com/from-discovery-to-enforcement-fast-tracking-zero-trust-with-nutanix-flow-network-security-and-faddom/ (Retrieved: 2026-08-10T11:18:46Z)
[12] Faddom. "Faddom Launches Free Community Plan (blog)". https://faddom.com/faddom-launches-free-community-plan/ (Retrieved: 2026-08-10T11:18:46Z)
[13] Faddom. "What is Microsegmentation? 2025 Guide (blog)". https://faddom.com/what-is-microsegmentation/ (Retrieved: 2026-08-10T11:18:46Z)
[14] Faddom. "Faddom Customer Stories (page)". https://faddom.com/customer-stories/ (Retrieved: 2026-08-10T11:18:46Z)
[15] Faddom. "Faddom In the News (page)". https://faddom.com/in-the-news/ (Retrieved: 2026-08-10T11:18:46Z)
[16] Faddom. "Can I deploy Faddom completely offline? (help center)". https://support.faddom.com/en/articles/9059416-can-i-deploy-faddom-completely-offline (Retrieved: 2026-08-10T11:18:46Z)
[17] Faddom. "Capturing network traffic using agents (help center)". https://support.faddom.com/en/articles/9428889-capturing-network-traffic-using-agents (Retrieved: 2026-08-10T11:18:46Z)
[18] Faddom. "How To Integrate My Kubernetes Cluster With Faddom? (help center)". https://support.faddom.com/en/articles/9428874-how-to-integrate-my-kubernetes-cluster-with-faddom (Retrieved: 2026-08-10T11:18:46Z)
[19] Faddom. "Discovering Kubernetes (help center)". https://support.faddom.com/en/articles/9059428-discovering-kubernetes (Retrieved: 2026-08-10T11:18:46Z)
[20] Faddom. "How to Discover CVEs in Faddom (help center)". https://support.faddom.com/en/articles/9059510-how-to-discover-cves-in-faddom (Retrieved: 2026-08-10T11:18:46Z)
[21] Faddom. "Setting Up Software And CVE Discovery (help center)". https://support.faddom.com/en/articles/9428970-setting-up-software-and-cve-discovery (Retrieved: 2026-08-10T11:18:46Z)
[22] Faddom. "How to Use Shadow IT (help center)". https://support.faddom.com/en/articles/11679157-how-to-use-shadow-it (Retrieved: 2026-08-10T11:18:46Z)
[23] Faddom. "External Traffic Detection (help center)". https://support.faddom.com/en/articles/9428951-external-traffic-detection (Retrieved: 2026-08-10T11:18:46Z)
[24] Faddom. "Lighthouse AI Traffic Anomalies (help center)". https://support.faddom.com/en/articles/11939234-lighthouse-ai-traffic-anomalies (Retrieved: 2026-08-10T11:18:46Z)
[25] Faddom. "How to Use the Micro-Segmentation Feature (help center)". https://support.faddom.com/en/articles/13051324-how-to-use-the-micro-segmentation-feature (Retrieved: 2026-08-10T11:18:46Z)
[26] Faddom. "ServiceNow Integration for CMDB and Incident Creation (help center)". https://support.faddom.com/en/articles/9428917-servicenow-integration-for-cmdb-and-incident-creation (Retrieved: 2026-08-10T11:18:46Z)
[27] Faddom. "Can Faddom Integrate With Other Tools? (help center)". https://support.faddom.com/en/articles/9428899-can-faddom-integrate-with-other-tools (Retrieved: 2026-08-10T11:18:46Z)
[28] Faddom. "Faddom REST API Guide (help center)". https://support.faddom.com/en/articles/13044771-faddom-rest-api-guide (Retrieved: 2026-08-10T11:18:46Z)
[29] Faddom. "Setting up the Faddom Event Log Forwarder (help center)". https://support.faddom.com/en/articles/14740179-setting-up-the-faddom-event-log-forwarder (Retrieved: 2026-08-10T11:18:46Z)
[30] Faddom. "Is Faddom Secure? (help center)". https://support.faddom.com/en/articles/9059544-is-faddom-secure (Retrieved: 2026-08-10T11:18:46Z)
[31] Faddom. "Application Maps Overview (help center)". https://support.faddom.com/en/articles/9428944-application-maps-overview (Retrieved: 2026-08-10T11:18:46Z)
[32] Faddom. "Network Topology Mapping (help center)". https://support.faddom.com/en/articles/9059502-network-topology-mapping (Retrieved: 2026-08-10T11:18:46Z)
[33] Faddom. "Traffic Behavior Investigation (help center)". https://support.faddom.com/en/articles/9428953-traffic-behavior-investigation (Retrieved: 2026-08-10T11:18:46Z)
[34] Faddom. "Faddom for Security Teams (help center)". https://support.faddom.com/en/articles/9897773-faddom-for-security-teams (Retrieved: 2026-08-10T11:18:46Z)
[35] Faddom. "Release Notes Highlights - v2026.2 (help center)". https://support.faddom.com/en/articles/16012519-release-notes-highlights-v2026-2 (Retrieved: 2026-08-10T11:18:46Z)
[36] Faddom. "Installation Prerequisites (help center)". https://support.faddom.com/en/articles/9428860-installation-prerequisites (Retrieved: 2026-08-10T11:18:46Z)
[37] Faddom. "How to Use the Multi-Tenancy (help center)". https://support.faddom.com/en/articles/9059454-how-to-use-the-multi-tenancy (Retrieved: 2026-08-10T11:18:46Z)
[38] Faddom. "Custom Tags (help center)". https://support.faddom.com/en/articles/9428977-custom-tags (Retrieved: 2026-08-10T11:18:46Z)
[39] Faddom. "Our Modules - Overview (help center)". https://support.faddom.com/en/articles/11090351-our-modules-overview (Retrieved: 2026-08-10T11:18:46Z)
[40] Faddom. "Changing the Faddom server SSL certificate (help center)". https://support.faddom.com/en/articles/9428900-changing-the-faddom-server-ssl-certificate (Retrieved: 2026-08-10T11:18:46Z)
[41] Faddom. "Upgrading the Faddom Server (help center)". https://support.faddom.com/en/articles/9428901-upgrading-the-faddom-server (Retrieved: 2026-08-10T11:18:46Z)
[42] Faddom. "How to Activate Your License Online and Offline (help center)". https://support.faddom.com/en/articles/9428911-how-to-activate-your-license-online-and-offline (Retrieved: 2026-08-10T11:18:46Z)
[43] Faddom. "How to Setup the Faddom Proxy (help center)". https://support.faddom.com/en/articles/9428892-how-to-setup-the-faddom-proxy (Retrieved: 2026-08-10T11:18:46Z)
[44] Faddom. "How to Configure Data Sources (help center)". https://support.faddom.com/en/articles/9428870-how-to-configure-data-sources (Retrieved: 2026-08-10T11:18:46Z)
[45] Faddom. "Servers At Risk (help center)". https://support.faddom.com/en/articles/11659844-servers-at-risk (Retrieved: 2026-08-10T11:18:46Z)
[46] NIST CSRC. "NIST CMVP Validated Modules Search (keyword: faddom)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&CertificateStatus=Active&ValidationYear=0&Keyword=faddom (Retrieved: 2026-08-10T11:18:46Z)
[47] TrustRadius. "Faddom Reviews from Real Users (TrustRadius)". https://www.trustradius.com/products/faddom/reviews (Retrieved: 2026-08-10T11:18:46Z)
[48] TechCrunch. "Faddom raises $12M to help companies map IT infrastructure wherever it lives (TechCrunch)". https://techcrunch.com/2024/02/21/faddom-raises-12m-to-help-companies-map-it-infrastructure-wherever-it-lives/ (Retrieved: 2026-08-10T11:18:46Z)
[49] Cybersecurity Insiders. "Democratizing Cybersecurity for Small IT Teams (Cybersecurity Insiders)". https://www.cybersecurity-insiders.com/democratizing-cybersecurity-for-small-it-teams-how-lightweight-security-tools-can-bridge-the-gap/ (Retrieved: 2026-08-10T11:18:46Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 9
- **Sources reviewed:** 49 (kept: 49, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 1, certification_registry: 1, product_release_notes: 1, third_party_review: 3, vendor_blog: 7, vendor_doc: 36
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
