# Microsegmentation Product Assessment: WatchGuard Technologies - WatchGuard Firebox (Fireware OS + WatchGuard Cloud + FireCloud ZTNA)

**Product ID:** `watchguard-firebox`
**Version reference:** Fireware v12.11/v12.12 (FIPS 140-3 supported in v12.11), WatchGuard Cloud, FireCloud (Zero Trust Network Access); NIST CMVP certificates #5301 and #5240
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T23:59:00Z
**Total evidence items collected:** 61
**Total distinct sources:** 31

---

## 1. Overview

WatchGuard Firebox is a network-enforced security appliance family (T-series and M-series hardware, FireboxV, Firebox Cloud) running the Fireware OS, managed either locally through Fireware Web UI or WatchGuard System Manager (WSM) or centrally in WatchGuard Cloud [25]. Its microsegmentation-adjacent capabilities are zone/VLAN-based firewall policies keyed on port, protocol and user/group identity [2, 9], Firebox Network Discovery for device-level network mapping [4, 30], NetFlow export for flow visibility [13], and FireCloud (Zero Trust Network Access) for identity-based, per-application access via the Connection Manager client [22]. High availability is delivered by FireCluster active/passive or active/active pairs [3]. Deployment shapes span hardware appliances and validated FIPS 140-3 Level 2 modes on the T/M-series per NIST CMVP [27, 28]. WatchGuard does not position Firebox as a workload-based microsegmentation platform: there are no host agents on servers (the only documented agent is the end-user ZTNA Connection Manager [22]), no Kubernetes-native isolation, and no tag/label policy model - segmentation is network-layer enforcement plus ZTNA remote access.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 4     | 0                | 4      | 0   |
| partial          | 17    | 0                | 17     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 11    | 0                | 0      | 11  |
| not_applicable   | 1     | 0                | 1      | 0   |

**Evidence quality:** 1 items backed by ≥ 2 source_types; 21 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** Firebox is a network appliance with no workload host agent; the only documented agent is the WatchGuard Connection Manager installed on end-user computers for FireCloud access, so per-OS server-agent compatibility does not apply.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | - | Network Discovery scans internal networks to detect devices and show them on a network map (manual or scheduled scans), Traffic Monitor shows log messages as events occur, and the Firebox exports NetFlow flow records to collectors; this is device- and flow-level visibility rather than full application-flow auto-discovery across the data center. [4], [5], [13], [17], [30], [31] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | The Network Discovery map is organized by Firebox interfaces and networks and shows per-device details such as IP address, host name, MAC address, operating system and open ports; it is not organized by application, environment, role or process. [4] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 90 days | WatchGuard Cloud Log Manager and Log Search retain Firebox log data for 90 days with Basic Security Suite and 365 days with Total Security Suite, and the visible period is bounded by the device's Data Retention license. [18], [29] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | - | Network Discovery reports each device's Known/Unknown status and lets administrators mark Approved Devices to identify rogue devices, and Application Control identifies over 1800 applications by signature; unrecognized-device detection is documented but flow-level 'unrecognized traffic' classification is not. [4], [11] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | - | Fireware supports user/group-based firewall policies through authentication (Active Directory, LDAP, RADIUS, SSO), and WatchGuard Cloud Zero Trust policies and FireCloud access rules match connections to user groups; base Firebox policies otherwise key on port/protocol/zone rather than tags or labels. [2], [9], [20], [23], [24] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | - | no evidence found (Rai provides AI-driven security operations and incident correlation in WatchGuard Cloud, but no firewall rule-recommendation feature is documented in staged sources.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | Policy Checker sends a test packet through the Firebox for a specified protocol between a source and destination and highlights the policy that manages it, letting administrators verify how traffic is handled before/without committing changes. [1] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | Backup images restore the Firebox to a previous state (configuration, certificates, feature key), configuration can be backed up and restored through WatchGuard Cloud, and WatchGuard Cloud templates manage policies across multiple Fireboxes; an explicit one-click policy rollback is not documented. [6], [25] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found (Fireware/FireCloud rules are evaluated by priority/precedence ordering; no inherited or hierarchical policy model is documented.) |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | - | Firebox is a network appliance with no workload host agent; the only documented agent is the WatchGuard Connection Manager installed on end-user computers for FireCloud access, so per-OS server-agent compatibility does not apply. [22] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | Firebox provides network-layer (agentless) enforcement, and FireCloud ZTNA is delivered through a Connection Manager agent installed on end-user computers; the agent path is remote-access oriented rather than a workload segmentation agent. [22] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | The hardware guide documents local management via Fireware Web UI or WatchGuard System Manager as an alternative to WatchGuard Cloud, and the Firebox stores recent log messages locally, indicating operation without cloud connectivity; signature updates and cloud services still require Internet. [12], [25], [31] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scalability is documented in appliance terms: FireCluster pairs two Fireboxes for HA and performance and the rackmount M-series is positioned for higher throughput and scalability; no workload-per-controller count is published. [3], [25] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | The WatchGuard Agent is described as having low CPU, memory and bandwidth usage, using less than 2 MB of data each day; no numeric CPU percentage is published. [22] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | The WatchGuard Agent is described as having low CPU, memory and bandwidth usage, using less than 2 MB of data each day; no numeric RAM footprint is published. [22] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | - | no evidence found (No packet-forwarding latency figure is published for Firebox in staged sources.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | Enforcement runs on the Firebox at the network layer (firewall policies based on port and protocol), and the Connection Manager agent is an end-user client for FireCloud connectivity; no explicit fail-open or fail-closed statement for agent failure is documented. [2], [22] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Unknown | low | - | no evidence found (No WatchGuard Firebox REST API reference covering 100% of administration functions was found in the Help Center; the WatchGuard Cloud API documentation site returned an empty shell.) |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | The Firebox can be configured to send syslog log messages to up to three servers in Syslog or IBM LEEF format, the latter targeting IBM QRadar. [7] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | - | no evidence found (Application Control works at application-signature level; process-level network identity enforcement is not documented.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | IPS provides signature-based real-time protection, FireCloud includes botnet detection that blocks known botnet IPs at the packet level, and Rai correlates signals from WatchGuard products into incidents; honeypot/deception capabilities are not documented. [10], [19], [22] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Fireware Report Manager ships HIPAA and PCI compliance reports, and WatchGuard Cloud Compliance Reporting provides ISO 27001, NIST 800-53/800-171/CSF, NIS2, DORA and other defense-goal reports; IEC 62443 and NIST 800-207 reports are not documented. [16], [26] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | Firebox management session data is secured with certificates, Fireboxes with a TPM register with WatchGuard Cloud using the TPM, and FIPS mode requires browsers to use TLS v1.2/v1.3; no workload agent-controller channel exists in this network-enforced architecture. [12], [14], [15] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | FireCluster is the HA solution for Fireboxes with two cluster members in active/passive or active/active configurations; if one member fails the other takes over its connections. [3] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | The Firebox can be locally managed and stores recent log messages locally, and WatchGuard Cloud is positioned as an optional centralized monitoring platform, implying enforcement continues independent of the cloud controller; no explicit autonomous-mode statement for a complete controller outage is documented. [25], [31] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Firebox backup images (configuration, certificates, feature key) restore the device to a previous state and can be saved to the Firebox, a USB drive, or WatchGuard Cloud; an automated disaster-recovery site-sync is not documented. [6] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | NIST CMVP lists WatchGuard Firebox T/M-series modules as FIPS 140-3 Level 2 validated (certificates 5301 and 5240) and Fireware documents FIPS 140-3 Level 2 support in v12.11; no Common Criteria EAL4+ validation is evidenced. [15], [27], [28] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found |

---

## 4. Notable Strengths

- **FireCluster high availability (7.1):** FireCluster pairs two Fireboxes in active/passive or active/active configurations with connection takeover when a member fails [3].
- **Built-in policy simulation (2.3):** Policy Checker sends test packets through the Firebox and highlights the policy that manages a given flow, supporting policy dry-run verification [1].
- **Documented flow-log retention (1.3):** WatchGuard Cloud Log Manager/Log Search retain Firebox log data for 90 days (Basic Security Suite) or 365 days (Total Security Suite), meeting the 90-day forensic threshold [29, 18].
- **SIEM integration (5.2):** Firebox exports syslog messages to up to three servers in Syslog or IBM LEEF format, the latter targeting IBM QRadar [7].
- **FIPS 140-3 validation (8.1):** NIST CMVP certificates #5301 and #5240 list the Firebox T/M-series at FIPS 140-3 Level 2, and Fireware v12.11 documents a FIPS-compliant mode [27, 28, 15].

## 5. Notable Gaps / Risks

- **No workload-based microsegmentation (3.2, 6.1):** no container/Kubernetes/OpenShift native isolation or process-level enforcement is documented; enforcement is network-layer, so intra-datacenter east-west segmentation depends on zone/VLAN policies and firewall placement [2].
- **No tag/label policy model or AI rule recommendation (2.1, 2.2):** policies key on port/protocol/zone and user/group identity via authentication; there is no tag/label abstraction and Rai's AI is incident-correlation rather than policy recommendation [9, 2].
- **Scale not expressed in workloads (3.5):** no workload-per-controller figure is published; FireCluster pairs two units and the rackmount M-series is positioned in throughput terms, leaving the 50,000-workload requirement unverifiable [3, 25].
- **Integration gaps (5.1, 5.3, 5.4):** no full REST API reference, ServiceNow CMDB tag sync, or CI/CD pipeline integration could be evidenced from staged documentation.
- **OT software certifications absent (8.2):** no Siemens/Honeywell/ABB industrial software-compatibility certifications were found for Firebox.

## 6. Evidence Quality Notes

22 of 33 checklist items carry evidence, 21 of them relying exclusively on WatchGuard-published documentation (Fireware / WatchGuard Cloud / FireCloud Help Center pages and the M4850-M6850 hardware guide), which caps confidence at medium under the validator rule; only item 8.1 triangulates with an independent registry - NIST CMVP certificates #5301 and #5240 (certification_registry) corroborating the vendor's FIPS 140-3 claim. The remaining 11 items are unknown because no staged source addresses the capability; several have documented near-neighbors (Rai AI for 2.2, Application Control signatures for 6.1, NetFlow for 4.3) that were judged insufficient for a non-unknown verdict.

Search engines (Google/Bing/DuckDuckGo) were bot-blocked from this research network, so no analyst reports, third-party reviews, or Common Criteria portal entries could be staged - the same limitation recorded in the FortiGate run. The Common Criteria portal returned HTTP 403, leaving the EAL4+ half of 8.1 unverified; the CC portal should be re-checked from a network with search access. No contradictions were found among staged sources; verdicts were chosen conservatively, with `partial` used where only qualitative claims exist (4.1, 4.2 agent resource usage; 3.5 scale) and `unknown` where documentation is silent.

---

## Bibliography

[1] WatchGuard Technologies. "Use Policy Checker to Find a Policy (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/policies/policy_checker_web.html (Retrieved: 2026-08-10T23:50:00Z)
[2] WatchGuard Technologies. "Add Policies to Your Configuration (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/policies/add_policy_c.html (Retrieved: 2026-08-10T23:50:00Z)
[3] WatchGuard Technologies. "About FireCluster (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/ha/cluster_about_wsm.html (Retrieved: 2026-08-10T23:50:00Z)
[4] WatchGuard Technologies. "Network Discovery (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/network_discovery/network_discovery_web.html (Retrieved: 2026-08-10T23:50:00Z)
[5] WatchGuard Technologies. "Monitor Devices on Your Internal Networks (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/network_discovery/monitor_network-discovery.html (Retrieved: 2026-08-10T23:50:00Z)
[6] WatchGuard Technologies. "Firebox Backup and Restore (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/backup_upgrade_recovery/backup_restore_intro.html (Retrieved: 2026-08-10T23:50:00Z)
[7] WatchGuard Technologies. "Configure Syslog Server Settings (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/logging/send_logs_to_syslog_c.html (Retrieved: 2026-08-10T23:50:00Z)
[8] WatchGuard Technologies. "Set Up Logging and Reporting for Your Network (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/logging/set-up_logging-reporting_network.html (Retrieved: 2026-08-10T23:50:00Z)
[9] WatchGuard Technologies. "User Authentication (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/other/chapters/authentication.html (Retrieved: 2026-08-10T23:50:00Z)
[10] WatchGuard Technologies. "Intrusion Prevention Service (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/ips/ips_intro_c.html (Retrieved: 2026-08-10T23:50:00Z)
[11] WatchGuard Technologies. "Application Control (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/app_control/app_control_intro_c.html (Retrieved: 2026-08-10T23:50:00Z)
[12] WatchGuard Technologies. "WatchGuard Cloud on Your Firebox (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/wg_cloud/wg-cloud_fb-enable_c.html (Retrieved: 2026-08-10T23:50:00Z)
[13] WatchGuard Technologies. "About NetFlow (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/basicadmin/netflow_about.html (Retrieved: 2026-08-10T23:50:00Z)
[14] WatchGuard Technologies. "Certificates (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/certificates/certificates_intro_c.html (Retrieved: 2026-08-10T23:50:00Z)
[15] WatchGuard Technologies. "FIPS Support in Fireware (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/overview/fireware/fips_about_c.html (Retrieved: 2026-08-10T23:50:00Z)
[16] WatchGuard Technologies. "View Compliance Reports (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/reports/report_mgr_compliance_reports_wsm.html (Retrieved: 2026-08-10T23:50:00Z)
[17] WatchGuard Technologies. "Monitor Network Activity (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/monitor/monitor_network-activity.html (Retrieved: 2026-08-10T23:50:00Z)
[18] WatchGuard Technologies. "Log Manager (WatchGuard Cloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/WG-Cloud/Devices/reports/log_manager_wgc.html (Retrieved: 2026-08-10T23:50:00Z)
[19] WatchGuard Technologies. "About Rai (WatchGuard Cloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/WG-Cloud/Rai/rai_about.html (Retrieved: 2026-08-10T23:50:00Z)
[20] WatchGuard Technologies. "About Zero Trust in WatchGuard Cloud (WatchGuard Cloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/WG-Cloud/Zero-Trust/about.html (Retrieved: 2026-08-10T23:50:00Z)
[21] WatchGuard Technologies. "Manage the Firebox Configuration (WatchGuard Cloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/WG-Cloud/Devices/managed/device_configuration_dashboard.html (Retrieved: 2026-08-10T23:50:00Z)
[22] WatchGuard Technologies. "About FireCloud (FireCloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/FireCloud/firecloud_about.html (Retrieved: 2026-08-10T23:50:00Z)
[23] WatchGuard Technologies. "FireCloud Access Rules (FireCloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/FireCloud/firecloud_policies.html (Retrieved: 2026-08-10T23:50:00Z)
[24] WatchGuard Technologies. "Integrate FireCloud with Zero Trust (FireCloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/FireCloud/zero-trust_firecloud.html (Retrieved: 2026-08-10T23:50:00Z)
[25] WatchGuard Technologies. "Firebox M4850/M5850/M6850 Hardware Guide (Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Hardware-Guides/firebox-m4850-5850-6850-hardware-guide.html (Retrieved: 2026-08-10T23:50:00Z)
[26] WatchGuard Technologies. "About WatchGuard Compliance Reporting (WatchGuard Cloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/WG-Cloud/Compliance%20Reporting/compliance_reporting_intro.html (Retrieved: 2026-08-10T23:50:00Z)
[27] NIST CMVP. "NIST CMVP Certificate #5301 - WatchGuard Firebox (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5301 (Retrieved: 2026-08-10T23:50:00Z)
[28] NIST CMVP. "NIST CMVP Certificate #5240 - WatchGuard Firebox M4800 and M5800 (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5240 (Retrieved: 2026-08-10T23:50:00Z)
[29] WatchGuard Technologies. "Manage Data Retention Licenses (WatchGuard Cloud Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/WG-Cloud/Devices/data_retention_licenses_manage.html (Retrieved: 2026-08-10T23:50:00Z)
[30] WatchGuard Technologies. "Network Discovery Scan (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/services/network_discovery/network_discovery_scan_web.html (Retrieved: 2026-08-10T23:50:00Z)
[31] WatchGuard Technologies. "About Firebox Logging and Notification (Fireware Help Center)". https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/logging/logging_and_logfiles_about_c.html (Retrieved: 2026-08-10T23:50:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 31 (kept: 31, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, vendor_doc: 29
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
