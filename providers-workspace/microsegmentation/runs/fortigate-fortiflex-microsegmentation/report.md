# Microsegmentation Product Assessment: Fortinet - FortiGate / FortiFlex Microsegmentation

**Product ID:** `fortigate-fortiflex-microsegmentation`
**Version reference:** FortiOS 7.4.4, FortiManager/FortiAnalyzer 7.4.0, FortiClient EMS 8.0, FortiSwitch 7.2.x, FortiNAC 9.x (per staged docs)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:30:00Z
**Total evidence items collected:** 92
**Total distinct sources:** 70

---

## 1. Overview

Fortinet's microsegmentation approach is network- and policy-centric rather than agent-centric: FortiGate/FortiOS security policies segment traffic using interfaces, addresses, dynamic tag/identity objects (EMS security-posture tags, FortiNAC tag dynamic addresses, Cisco SGT) [24][25][26], while FortiSwitch with FortiLink extends policy enforcement to the Ethernet access layer [14]. FortiNAC adds agentless discovery, profiling and access control for IT/IoT/OT devices [7], and FortiClient EMS provides the host agent with ZTNA tags and posture checks [5][63]. FortiManager centralizes policy packages, revision control and HA across managed devices [9][15], FortiAnalyzer provides log storage, SIEM parsing and compliance reporting [6][67], and FortiFlex supplies usage-based, points-based licensing for the virtualized components (FortiGate VM, FortiManager/FortiAnalyzer VM) across cloud, hybrid and on-premises deployments [13]. Deployment shapes cover hardware FortiGate appliances, cloud VMs, containerized FortiOS/FortiGate CNF, and campus/data-center switches [10][14].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 10    | 0                | 10     | 0   |
| partial          | 20    | 0                | 18     | 2   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 19 items backed by ≥ 2 source_types; 29 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | FortiView provides real-time and historical traffic/session monitoring, FortiNAC scans the network to discover users, applications and devices with active/passive techniques, and FortiSwitch onboarding auto-discovers ports and applies security policies. [7], [14], [37], [38] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | FortiView monitors group traffic by source/destination, application and policy, and the Security Fabric topology monitor and FortiNAC profiling provide device-level views; no role- or process-level application map was documented. [7], [36], [37], [39] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | FortiAnalyzer log storage policy lets administrators set how long Analytics and Archive logs are kept per ADOM, and the FortiAnalyzer datasheet cites configurable data-retention policies; no documented 90-day default or guarantee was found in staged sources. [6], [66] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | - | The Vulnerability Monitor displays endpoint vulnerabilities from FortiClient EMS by severity and shows the endpoint's location in the topology view; vulnerability context is not rendered directly on the traffic map. [5], [36] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | FortiOS classifies devices as unknown/manageable/unmanageable based on TLS fingerprint and user-agent learning, FortiView lists unscanned applications, and FortiNAC detects anomalous traffic patterns. [7], [33], [37], [40] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | FortiOS policies can match EMS security-posture tags, EMS dynamic endpoint groups, FortiNAC tag dynamic addresses and Cisco SGT tags, enabling access control that is not tied to IP/VLAN alone. [25], [26], [53], [58], [63] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | low | - | FortiManager is described as FortiAI-integrated with AI-driven configuration scripting, validation and IoT vulnerability analytics, and its AI Analysis monitor links to FortiAIOps; an ML-based microsegmentation rule-recommendation engine was not documented. [9], [48] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | FortiManager Policy Lookup searches for the policy that matches given traffic parameters, and policy hit counters and unused-policy checks provide visibility; no full dry-run traffic simulation was documented. [49], [70] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | FortiManager can revert a saved configuration revision and keeps revision history, and FortiGate supports configuration backup/restore; the revert is a multi-step operation rather than a one-click policy rollback. [41], [46], [52] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | - | FortiManager provides hierarchical management via ADOMs, global policy packages and reusable Policy Blocks, and FortiGate VDOMs act as independent virtual firewalls; no inherited-rule model was documented. [9], [42], [47] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The FortiClient agent supports Windows, macOS, Linux (Ubuntu/RHEL/CentOS), Chrome, iOS and Android; no AIX or Solaris agent is listed, though network-based enforcement via FortiNAC/FortiGate is OS-agnostic. [5], [7] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | - | FortiOS can run as a container, FortiGate CNF provides a managed cloud-native firewall for cloud workloads, EMS can be deployed on Kubernetes and FortiManager manages CNF instances; per-workload agent isolation or OpenShift support was not documented. [10], [51], [61], [69] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | FortiNAC scans actively or passively with permanent/dissolvable agents or agentless techniques, FortiClient provides the host agent, and FortiLink extends enforcement to the switch access layer. [5], [7], [14], [18] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | FortiGate hardware appliances support manual license and FortiGuard package upload for air-gapped operation (VMs excluded), FortiManager registers via entitlements-file upload, and EMS supports air-gapped install; FortiFlex cloud entitlement itself requires connectivity. [1], [34], [50], [57] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 50000 workloads | FortiClient EMS documents managing more than 50000 endpoints with appropriate PostgreSQL sizing, FortiNAC scales to 50000 endpoints, and FortiSwitch Manager manages up to 2500 switches. [4], [7], [56] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | - | no evidence found (No CPU-overhead figure for the FortiClient agent was found in any staged source.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | - | no evidence found (No RAM-footprint figure for the FortiClient agent was found in any staged source.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | 0.001 ms | The FortiSwitch Data Center Series datasheet lists about 1 microsecond (sub-0.1 ms) network latency for its hardware models; inline FortiGate policy latency is not quantified in staged sources. [3] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | FortiNAC is architected out-of-band so it does not sit inline with user traffic, meaning control-plane failure does not interrupt traffic; FortiClient agent crash/fail-open behavior is not documented in staged sources. [7] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | low | - | FortiClient EMS supports centralized remote deployment and controlled upgrades of the endpoint agent; no explicit statement that installation or updates require no reboot was found. [5] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | FortiOS REST API supports configuration CRUD, log/statistics retrieval and administrative actions, with REST APIs also documented for FortiManager, FortiClient EMS and FortiFlex; full coverage of every administrative function is not explicitly claimed. [9], [13], [31], [60] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | FortiManager lists turnkey integrations with Splunk and IBM QRadar, FortiGate logs can be forwarded via FortiAnalyzer to QRadar, FortiAnalyzer ingests syslog and offers SIEM log parsers, and FortiAnalyzer includes built-in SIEM/SOAR. [6], [11], [15], [68] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | - | The FortiManager product page lists turnkey integration with ServiceNow among partner integrations; tag/CMDB synchronization specifics were not documented in staged sources. [15] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | Fortinet provides an official Terraform provider for FortiOS, a FortiManager Ansible collection, and the FortiGate VM datasheet references IaC with auto scaling for DevSecOps workflows. [10], [32], [54] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | FortiClient's Application Firewall applies allow/block/monitor actions per application signature, and endpoint protection includes anti-malware/anti-exploit; process-level network identity enforcement is not documented. [5], [64] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Supported | medium | - | FortiDeceptor provides adaptive deception that detects reconnaissance, credential abuse and lateral movement, integrates into the Security Fabric, and FortiGuard threat intelligence feeds FortiGate services. [8], [10], [17], [43] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | FortiAnalyzer ships report templates including PCI-DSS Compliance Review and OT Security Risk, and the datasheet cites PCI-DSS/HIPAA compliance reports; NIST 800-207 and ISO 27001 templates were not found, with IEC 62443 covered via OT guidance. [6], [21], [67] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | - | EMS runs TLS services with managed server certificates, FortiClient obtains a client certificate from the EMS ZTNA CA to identify itself to FortiGate (mutual certificate trust), and FortiOS supports TLS 1.3. [27], [35], [59] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | FortiGate supports HA active-passive and active-active clusters (FGCP), FortiManager HA supports one primary plus up to four backups, EMS HA is active-passive, and FortiNAC offers active-passive HA. [7], [28], [29], [30], [45], [65] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | - | no evidence found (No staged source documents FortiClient behavior when EMS is unreachable (offline/autonomous policy enforcement).) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | FortiManager supports auto-backup of device configuration, FortiClient EMS supports scheduled database backups, and FortiManager HA supports geographically separated units for redundancy; an end-to-end DR site-sync workflow is not documented. [45], [55], [62] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | The NIST CMVP active list includes FortiGate/FortiOS modules (e.g. certificate 4497 'FortiGate Next-Generation Firewalls with FortiOS 6.4/7.0'), FortiOS documents FIPS cipher mode for cloud VMs, and Fortinet's certification page cites FIPS and Common Criteria programs; explicit FIPS 140-3 or Common Criteria EAL4+ entries for FortiGate were not found in staged sources. [19], [20], [22], [44] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | FortiSwitch Rugged is IEEE 1613/IEC 61850-3 compliant for power substations, Fortinet provides IEC 62443-based OT guidance, and FortiNAC lists Siemens among supported network-infrastructure vendors; certifications from Siemens/Honeywell/ABB for the microsegmentation stack were not found. [7], [12], [21] |

---

## 4. Notable Strengths

- **Identity- and tag-based policy matching (items 2.1, 6.4):** FortiOS firewall policies can match EMS security-posture tags, EMS dynamic endpoint groups, FortiNAC tag dynamic addresses and Cisco SGT tags, with FortiClient certificates providing device identity [25][26][63][27].
- **Real-time traffic visibility plus unknown-device handling (items 1.1, 1.5):** FortiView renders real-time and historical sessions, FortiNAC auto-discovers users/devices/applications, and FortiOS classifies unmanageable/unknown devices with unscanned-application visibility [37][38][7][40].
- **Hybrid agent and agentless enforcement (item 3.3):** the stack combines the FortiClient host agent with FortiNAC active/passive/agentless scanning and FortiLink access-layer enforcement, suiting heterogeneous estates [5][7][14].
- **Scale for large fleets (item 3.5):** FortiClient EMS documents managing more than 50,000 endpoints, FortiNAC models support up to 50,000 endpoints, and FortiSwitch Manager handles up to 2,500 switches [56][7][4].
- **Controller high availability (items 7.1, 7.3):** FortiGate supports active-passive and active-active clusters, FortiManager HA runs one primary plus up to four backups with geographic redundancy, and EMS and FortiNAC support active-passive HA [28][29][30][45][65][7].

## 5. Notable Gaps / Risks

- **No published agent footprint numbers (items 4.1, 4.2):** staged sources give no CPU or RAM figures for the FortiClient agent, so the <1% CPU and <100 MB RAM requirements could not be verified.
- **No documented autonomous agent mode (item 7.2):** no staged FortiClient/EMS document describes endpoint policy enforcement when EMS is unreachable; this should be confirmed with the vendor for offline/remote sites.
- **AI policy recommendation not evidenced (item 2.2):** FortiManager's AI/AI-ops capabilities cover configuration validation and analytics rather than ML-based microsegmentation rule recommendations.
- **Air-gapped operation has limits (item 3.4):** manual air-gap licensing is unsupported on FortiGate VM, and FortiFlex's cloud-based entitlement model itself requires FortiCloud connectivity, constraining fully isolated environments.
- **Certification claims only partially verified (items 8.1, 8.2):** NIST CMVP entries confirm FIPS-validated FortiGate modules but staged sources lack explicit FIPS 140-3/Common Criteria EAL4+ FortiGate entries, and no Siemens/Honeywell/ABB software-compatibility certification was found; OT coverage rests on IEC 61850-3/IEEE 1613 compliance and IEC 62443 guidance.

## 6. Evidence Quality Notes

92 evidence entries were collected across 70 staged sources, and every quote passed the grounding check (0 fabricated, 0 unverifiable) against the hash-anchored artifacts. 19 items are backed by at least 2 source types; most items cite 2-6 sources. However, because search engines, Gartner and the Common Criteria portal were bot-blocked from the research network, the source base is almost entirely vendor-published (59 vendor_doc, 10 vendor_datasheet, 1 certification_registry from NIST), which caps confidence at medium for every item per the validator's vendor-only rule.

Verdicts were chosen conservatively where evidence was qualitative: 1.3 (retention) stays partial because FortiAnalyzer retention is configurable but no 90-day figure is documented; 4.3 uses the FortiSwitch datasheet's sub-0.1 ms forwarding latency with the caveat that inline FortiGate latency is unquantified; 4.4 rests on FortiNAC's out-of-band design with the agent crash behavior undocumented; and 4.1, 4.2 and 7.2 are unknown because no source addresses them at all. No contradictions between sources were observed; the NIST CMVP registry corroborates Fortinet's FIPS claims, and 8.1/8.2 are held at partial rather than supported because the specific FIPS 140-3, Common Criteria EAL4+, and Siemens/Honeywell/ABB certifications are not present in the staged material.

---

## Bibliography

[1] Fortinet. "FortiFlex Program Ordering Guide (FVM-OG)". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/og-flex-vm.pdf (Retrieved: 2026-08-10T14:20:00Z)
[2] Fortinet. "FortiFlex Usage-Based Security Licensing for Microsoft - Solution Brief". https://www.fortinet.com/content/dam/fortinet/assets/solution-guides/sb-fortiflex-delivers-usage-based-security-licensing-at-speed-of-digital-acceleration.pdf (Retrieved: 2026-08-10T14:20:00Z)
[3] Fortinet. "FortiSwitch Data Center Series Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSwitch_Data_Center_Series.pdf (Retrieved: 2026-08-10T14:20:00Z)
[4] Fortinet. "FortiSwitch Manager Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortiswitch-mgr.pdf (Retrieved: 2026-08-10T14:20:00Z)
[5] Fortinet. "FortiClient Unified Agent Data Sheet (FCT-DAT)". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/forticlient.pdf (Retrieved: 2026-08-10T14:20:00Z)
[6] Fortinet. "FortiAnalyzer Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortianalyzer.pdf (Retrieved: 2026-08-10T14:20:00Z)
[7] Fortinet. "FortiNAC Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiNAC.pdf (Retrieved: 2026-08-10T14:20:00Z)
[8] Fortinet. "FortiDeceptor Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiDeceptor.pdf (Retrieved: 2026-08-10T14:20:00Z)
[9] Fortinet. "FortiManager Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiManager.pdf (Retrieved: 2026-08-10T14:20:00Z)
[10] Fortinet. "FortiGate Virtual Appliances Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiGate_VM.pdf (Retrieved: 2026-08-10T14:20:00Z)
[11] Fortinet. "Fortinet and IBM Security QRadar Integrated Solution Brief". https://www.fortinet.com/content/dam/fortinet/assets/alliances/sb-QRadar-for-Fortinet-FortiGate.pdf (Retrieved: 2026-08-10T14:20:00Z)
[12] Fortinet. "FortiSwitch Rugged Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiSwitchRugged.pdf (Retrieved: 2026-08-10T14:20:00Z)
[13] Fortinet. "FortiFlex - Flexible, Usage-Based Security Licensing (product page)". https://www.fortinet.com/products/fortiflex (Retrieved: 2026-08-10T14:20:00Z)
[14] Fortinet. "FortiSwitch Enterprise - Secure Ethernet Switches (product page)". https://www.fortinet.com/products/fortiswitch-enterprise (Retrieved: 2026-08-10T14:20:00Z)
[15] Fortinet. "FortiManager - Central Network Management (product page)". https://www.fortinet.com/products/fortimanager (Retrieved: 2026-08-10T14:20:00Z)
[16] Fortinet. "FortiClient Unified Agent (product page)". https://www.fortinet.com/products/forticlient (Retrieved: 2026-08-10T14:20:00Z)
[17] Fortinet. "FortiDeceptor - Deception-based Breach Protection (product page)". https://www.fortinet.com/products/fortideceptor (Retrieved: 2026-08-10T14:20:00Z)
[18] Fortinet. "FortiNAC - Network Access Control (product page)". https://www.fortinet.com/products/network-access-control (Retrieved: 2026-08-10T14:20:00Z)
[19] Fortinet. "Fortinet Security and Trust page". https://www.fortinet.com/trust (Retrieved: 2026-08-10T14:20:00Z)
[20] Fortinet. "Fortinet Security and Trust - Product Certifications page". https://www.fortinet.com/corporate/about-us/product-certifications (Retrieved: 2026-08-10T14:20:00Z)
[21] Fortinet. "ICS and SCADA Risks and Solutions (OT security page)". https://www.fortinet.com/solutions/industries/scada-industrial-control-systems (Retrieved: 2026-08-10T14:20:00Z)
[22] NIST. "NIST CMVP Validated Modules search for FortiGate". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&Keyword=FortiGate (Retrieved: 2026-08-10T14:20:00Z)
[23] Fortinet. "FortiSwitch 7.2.10 Administration Guide - Private VLANs". https://docs.fortinet.com/document/fortiswitch/7.2.10/administration-guide/104079/private-vlans (Retrieved: 2026-08-10T14:20:00Z)
[24] Fortinet. "FortiOS 7.4.4 Administration Guide - Firewall policy". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/656084/firewall-policy (Retrieved: 2026-08-10T14:20:00Z)
[25] Fortinet. "FortiOS 7.4.4 Administration Guide - Cisco Security Group Tag as policy matching criteria". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/322202/cisco-security-group-tag-as-policy-matching-criteria (Retrieved: 2026-08-10T14:20:00Z)
[26] Fortinet. "FortiOS 7.4.4 Administration Guide - FortiNAC tag dynamic address". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/582240/fortinac-tag-dynamic-address (Retrieved: 2026-08-10T14:20:00Z)
[27] Fortinet. "FortiOS 7.4.4 Administration Guide - Establish device identity and trust context with FortiClient EMS". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/25915/establish-device-identity-and-trust-context-with-forticlient-ems (Retrieved: 2026-08-10T14:20:00Z)
[28] Fortinet. "FortiOS 7.4.4 Administration Guide - High Availability". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/666376/high-availability (Retrieved: 2026-08-10T14:20:00Z)
[29] Fortinet. "FortiOS 7.4.4 Administration Guide - HA active-passive cluster setup". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/900885/ha-active-passive-cluster-setup (Retrieved: 2026-08-10T14:20:00Z)
[30] Fortinet. "FortiOS 7.4.4 Administration Guide - HA active-active cluster setup". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/357558/ha-active-active-cluster-setup (Retrieved: 2026-08-10T14:20:00Z)
[31] Fortinet. "FortiOS 7.4.4 Administration Guide - Using APIs". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/940602/using-apis (Retrieved: 2026-08-10T14:20:00Z)
[32] Fortinet. "FortiOS 7.4.4 Administration Guide - Terraform: FortiOS as a provider". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/763117/terraform-fortios-as-a-provider (Retrieved: 2026-08-10T14:20:00Z)
[33] Fortinet. "FortiOS 7.4.4 Administration Guide - Log settings and targets". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/250999/log-settings-and-targets (Retrieved: 2026-08-10T14:20:00Z)
[34] Fortinet. "FortiOS 7.4.4 Administration Guide - Licensing in air-gap environments". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/32287/licensing-in-air-gap-environments (Retrieved: 2026-08-10T14:20:00Z)
[35] Fortinet. "FortiOS 7.4.4 Administration Guide - TLS 1.3 support". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/29991/tls-1-3-support (Retrieved: 2026-08-10T14:20:00Z)
[36] Fortinet. "FortiOS 7.4.4 Administration Guide - Viewing the Vulnerability Monitor". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/387436/viewing-the-vulnerability-monitor (Retrieved: 2026-08-10T14:20:00Z)
[37] Fortinet. "FortiOS 7.4.4 Administration Guide - Using the FortiView interface". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/96300/using-the-fortiview-interface (Retrieved: 2026-08-10T14:20:00Z)
[38] Fortinet. "FortiOS 7.4.4 Administration Guide - FortiView Sessions". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/863511/fortiview-sessions (Retrieved: 2026-08-10T14:20:00Z)
[39] Fortinet. "FortiOS 7.4.4 Administration Guide - Viewing the Fabric Topology monitor". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/873590/viewing-the-fabric-topology-monitor (Retrieved: 2026-08-10T14:20:00Z)
[40] Fortinet. "FortiOS 7.4.4 Administration Guide - Access control of unmanageable and unknown devices". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/710195/access-control-of-unmanageable-and-unknown-devices (Retrieved: 2026-08-10T14:20:00Z)
[41] Fortinet. "FortiOS 7.4.4 Administration Guide - Backing up the configuration". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/324674/backing-up-the-configuration (Retrieved: 2026-08-10T14:20:00Z)
[42] Fortinet. "FortiOS 7.4.4 Administration Guide - VDOM overview". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/597696/vdom-overview (Retrieved: 2026-08-10T14:20:00Z)
[43] Fortinet. "FortiOS 7.4.4 Administration Guide - Configuring FortiDeceptor". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/414977/configuring-fortideceptor (Retrieved: 2026-08-10T14:20:00Z)
[44] Fortinet. "FortiOS 7.4.4 Administration Guide - FIPS cipher mode for cloud FortiGate VMs". https://docs.fortinet.com/document/fortigate/7.4.4/administration-guide/195210/fips-cipher-mode-for-aws-azure-oci-and-gcp-fortigate-vms (Retrieved: 2026-08-10T14:20:00Z)
[45] Fortinet. "FortiManager 7.4.0 Administration Guide - High Availability". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/568591/high-availability (Retrieved: 2026-08-10T14:20:00Z)
[46] Fortinet. "FortiManager 7.4.0 Administration Guide - Revert". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/854217/revert (Retrieved: 2026-08-10T14:20:00Z)
[47] Fortinet. "FortiManager 7.4.0 Administration Guide - Using Policy Blocks versus Global Policy Packages". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/352244/using-policy-blocks-versus-global-policy-packages (Retrieved: 2026-08-10T14:20:00Z)
[48] Fortinet. "FortiManager 7.4.0 Administration Guide - AI Analysis". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/925380/ai-analysis (Retrieved: 2026-08-10T14:20:00Z)
[49] Fortinet. "FortiManager 7.4.0 Administration Guide - Policy hit count". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/397218/policy-hit-count (Retrieved: 2026-08-10T14:20:00Z)
[50] Fortinet. "FortiManager 7.4.0 Administration Guide - Licensing in an air-gap environment". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/686126/licensing-in-an-air-gap-environment (Retrieved: 2026-08-10T14:20:00Z)
[51] Fortinet. "FortiManager 7.4.0 Administration Guide - Adding FortiGate CNF device". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/534577/adding-fortigate-cnf-device (Retrieved: 2026-08-10T14:20:00Z)
[52] Fortinet. "FortiManager 7.4.0 Administration Guide - Viewing configuration revision history". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/871900/viewing-configuration-revision-history (Retrieved: 2026-08-10T14:20:00Z)
[53] Fortinet. "FortiManager 7.4.0 Administration Guide - Creating ZTNA tag groups". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/790563/creating-ztna-tag-groups (Retrieved: 2026-08-10T14:20:00Z)
[54] Fortinet. "FortiManager 7.4.0 Administration Guide - Appendix D FortiManager Ansible Collection documentation". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/958156/appendix-d-fortimanager-ansible-collection-documentation (Retrieved: 2026-08-10T14:20:00Z)
[55] Fortinet. "FortiManager 7.4.0 Administration Guide - Auto-backup". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/478805/auto-backup (Retrieved: 2026-08-10T14:20:00Z)
[56] Fortinet. "FortiClient EMS 8.0 Administration Guide - Management capacity". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/282984/management-capacity (Retrieved: 2026-08-10T14:20:00Z)
[57] Fortinet. "FortiClient EMS 8.0 Administration Guide - Deploying EMS in air-gapped environments". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/359368/deploying-ems-in-air-gapped-environments (Retrieved: 2026-08-10T14:20:00Z)
[58] Fortinet. "FortiClient EMS 8.0 Administration Guide - FortiOS dynamic policies using EMS dynamic tags". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/584914/fortios-dynamic-policies-using-ems-dynamic-tags (Retrieved: 2026-08-10T14:20:00Z)
[59] Fortinet. "FortiClient EMS 8.0 Administration Guide - EMS Server Certificates". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/719821/ems-server-certificates (Retrieved: 2026-08-10T14:20:00Z)
[60] Fortinet. "FortiClient EMS 8.0 Administration Guide - FortiClient EMS API". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/30768/forticlient-ems-api (Retrieved: 2026-08-10T14:20:00Z)
[61] Fortinet. "FortiClient EMS 8.0 Administration Guide - Deploying EMS on Kubernetes". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/565859/deploying-ems-on-kubernetes (Retrieved: 2026-08-10T14:20:00Z)
[62] Fortinet. "FortiClient EMS 8.0 Administration Guide - Automating EMS DB backups". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/905015/automating-ems-db-backups (Retrieved: 2026-08-10T14:20:00Z)
[63] Fortinet. "FortiClient EMS 8.0 Administration Guide - Security Posture Tags". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/924998/security-posture-tags (Retrieved: 2026-08-10T14:20:00Z)
[64] Fortinet. "FortiClient EMS 8.0 Administration Guide - Firewall (Application Firewall)". https://docs.fortinet.com/document/forticlient/8.0.0/ems-administration-guide/247129/firewall (Retrieved: 2026-08-10T14:20:00Z)
[65] Fortinet. "FortiClient EMS 8.0 HA Deployment Guide". https://docs.fortinet.com/document/forticlient/8.0.0/ems-ha-deployment-guide (Retrieved: 2026-08-10T14:20:00Z)
[66] Fortinet. "FortiAnalyzer 7.4.0 Administration Guide - Configuring log storage policy". https://docs.fortinet.com/document/fortianalyzer/7.4.0/administration-guide/743670/configuring-log-storage-policy (Retrieved: 2026-08-10T14:20:00Z)
[67] Fortinet. "FortiAnalyzer 7.4.0 Administration Guide - List of report templates". https://docs.fortinet.com/document/fortianalyzer/7.4.0/administration-guide/2854/list-of-report-templates (Retrieved: 2026-08-10T14:20:00Z)
[68] Fortinet. "FortiAnalyzer 7.4.0 Administration Guide - SIEM log parsers". https://docs.fortinet.com/document/fortianalyzer/7.4.0/administration-guide/353514/siem-log-parsers (Retrieved: 2026-08-10T14:20:00Z)
[69] Fortinet. "FortiGate CNF Concept Guide - What is a cloud native firewall". https://docs.fortinet.com/document/fortigate-cnf/latest/concept-guide/126213/what-is-a-cloud-native-firewall (Retrieved: 2026-08-10T14:20:00Z)
[70] Fortinet. "FortiManager 7.4.0 Administration Guide - Policy Lookup". https://docs.fortinet.com/document/fortimanager/7.4.0/administration-guide/978135/policy-lookup (Retrieved: 2026-08-10T14:20:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 70 (kept: 70, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, vendor_datasheet: 10, vendor_doc: 59
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
