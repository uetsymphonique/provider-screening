# Microsegmentation Product Assessment: Radiflow - iSocio (central OT monitoring, now iCEN) + CIARA (OT risk assessment)

**Product ID:** `isocio-ciara`
**Version reference:** Product pages and datasheets as of Aug 2026; iSID/iCEN datasheets (2025), CIARA datasheet (2025), iSEG RF-3180 datasheet (2021), IEC 62443 security brief (2021), ServiceNow joint brochure (2024)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:30:00Z
**Total evidence items collected:** 63
**Total distinct sources:** 34

---

## 1. Overview

Radiflow is an Israeli OT-security vendor (part of the Sabanci Group) whose iSocio/CiARA assessment covers the current platform surface: iSID, a passive threat- and anomaly-detection sensor that inspects mirrored network traffic and builds an asset/topology baseline [4, 16, 33]; iCEN, the central monitoring and risk-management console (the successor of the iSocio industrial SOC) that aggregates iSID sites and schedules CIARA risk assessments [3, 17]; and CIARA, a data-driven OT risk-assessment platform that builds a digital twin of the network and runs machine-learning breach-and-attack simulations against threat intelligence [8, 27]. Deployment is agentless: iSID can run centrally, locally per site, or via vSAP smart collectors, with enforcement delivered by iSEG distributed DPI firewalls and firewall/NAC integrations (Cisco ISE, Fortinet, Palo Alto) [6, 13, 20, 21]. Radiflow reports deployments at over 8,000 sites, and over 10,000 in newer materials [8, 11]. In microsegmentation terms the suite provides visibility, monitoring and risk assessment rather than host-based workload segmentation; policy enforcement is network-level and IP/zone-based [9, 18].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 2                | 3      | 0   |
| partial          | 13    | 0                | 13     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 10    | 0                | 0      | 10  |
| not_applicable   | 5     | 0                | 5      | 0   |

**Evidence quality:** 17 items backed by ≥ 2 source_types; 15 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** No host agent is installed on Windows/Linux/AIX/Solaris workloads; iSID is out-of-band server software analyzing mirrored traffic, so the agent OS-support matrix does not apply.
- **4.1:** No host agent runs on workloads; iSID passively inspects mirrored traffic with documented non-disruption of operations, so agent CPU consumption does not apply.
- **4.2:** No host agent runs on workloads; iSID passively inspects mirrored traffic without loading the network, so agent RAM footprint does not apply.
- **4.4:** There is no host agent that could crash or fail; iSID inspects a mirrored traffic stream with no disruption of operations.
- **4.5:** No host agents are installed or updated on servers; iSID sensors are upgraded remotely from iCEN without site visits.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | iSID automatically discovers assets and builds an asset inventory with roles, learning network topology in real time via passive mirrored-traffic analysis; CIARA automatically discovers and learns risk indicators, corroborated by third-party coverage. [8], [16], [23], [33] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Map View displays network devices in Purdue/Flow/Analyst/Custom modes, assets carry roles, and iSID associates assets with business processes; CIARA shows zones, conduits and segments, but no App/Environment/Role/Process dimension as in workload-centric products. [2], [4], [16], [24] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | — | no evidence found (No retention period for flow/connection history is documented in any staged vendor or third-party source.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | iSID maps CVEs per asset and CIARA ranks vulnerabilities by CVSS score, with third-party confirmation of automated vulnerability mapping; the CVE context is shown in tables/reports rather than as an overlay on the interactive map. [16], [24], [29] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | — | iSID builds a behavioral baseline and flags deviations and unauthorized traffic, using machine-learning research with Fraunhofer for autonomous detection of non-compliant/anomalous behavior. [4], [16], [32], [33] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | — | Policies can be defined per asset type (FortiGate None/Block/Allow) and per device via the Cisco ISE integration, but enforcement is IP/MAC/zone-based whitelisting in distributed firewalls rather than host tag/label identity. [13], [18], [20], [21] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | — | Based on its automatic learning, iSID generates policy suggestions that operators adjust and approve, and the iSEG gateway suggests editable firewall rules; ML/AI anomaly detection is backed by a Fraunhofer research project. [4], [9], [32] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | — | CIARA builds a digital twin and simulates security controls and WHAT-IF mitigation scenarios, functioning as a dry-run for controls; this is attack/risk simulation rather than a firewall-policy simulation mode. [8], [27] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found (No one-click policy rollback capability is documented in any staged source.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (iSIM distributes security profiles as firewall rules, but inherited/hierarchical rule structures are not documented.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | — | No host agent is installed on Windows/Linux/AIX/Solaris workloads; iSID is out-of-band server software analyzing mirrored traffic, so the agent OS-support matrix does not apply. [16], [33] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | — | no evidence found (No container/Kubernetes/OpenShift support is mentioned in any staged source.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | Deployment is agentless passive monitoring (port mirroring, no infrastructure changes) plus network-integration enforcement through iSEG gateways and ISE/FortiGate/Palo Alto integrations; no host-agent option exists. [6], [20] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | iCEN supports one-way iSID-to-iCEN connections for OT isolation, vSAP provides one-way traffic transmission, and the iREC recorder captures traffic offline where no link to a SOC exists. [3], [6], [34] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Unknown | low | — | no evidence found (Deployment scale is expressed in sites (8,000-10,000+), not workloads; no workload-count scalability figure is documented.) |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | No host agent runs on workloads; iSID passively inspects mirrored traffic with documented non-disruption of operations, so agent CPU consumption does not apply. [4], [16] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No host agent runs on workloads; iSID passively inspects mirrored traffic without loading the network, so agent RAM footprint does not apply. [4], [16] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | The assessed suite is passive/out-of-band so no inline latency is added, and the iSEG gateway documents switching latency under 10 microseconds, but no explicit policy-enforcement latency figure is published for the suite. [16], [18] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | There is no host agent that could crash or fail; iSID inspects a mirrored traffic stream with no disruption of operations. [4], [16] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No host agents are installed or updated on servers; iSID sensors are upgraded remotely from iCEN without site visits. [16], [17] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Unknown | low | — | no evidence found (Integrations consume partner APIs (Cisco pxGrid, FortiGate) and export JSON/CSV/PCAP, but no full administrative REST API is documented.) |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | iSID makes enriched data available to external systems including SIEMs, and iCEN exports alerts/assets to SIEM/SOC systems in multiple formats; gateways support syslog, but no named SIEM vendors or CEF format are specified for iSID/iCEN. [16], [17], [18] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | — | A certified Radiflow Service Graph Connector synchronizes iSID's asset database with the ServiceNow OTM CMDB in real time, updating the CMDB as assets change. [23] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | — | no evidence found (No CI/CD pipeline integration (Jenkins/GitLab/Terraform) is documented.) |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | — | no evidence found (Enforcement is at network/device level (DPI firewall, APA); no process-level enforcement is documented.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | iSID uses threat intelligence, SNORT signatures and CVE feeds, and CIARA ingests MITRE ATT&CK-based adversary intelligence for risk simulation; no honeypot/deception capability is documented. [8], [16], [24] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | CIARA and iSID produce IEC 62443-compliant hardening plans and posture reports, with CIARA also covering NIS2, NERC CIP and NIST CSF; no PCI-DSS, NIST 800-207 or ISO 27001 report templates are documented. [8], [16], [28] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | All connectivity to and from iCEN is documented as secured and encrypted (including one-way iSID-to-iCEN), and iSEG uses IPsec with AES/3DES and X.509 certificates; no TLS 1.3 or mutual-auth specification is published for the sensor-controller channel. [3], [17], [18] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | — | no evidence found (No controller-cluster HA (active-active/active-passive) is documented for iCEN; iSEG gateways offer VRRP redundancy at network level only.) |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | — | Enforcement rules live in iSEG distributed firewalls at each access point with Monitoring/Enforcement modes, so enforcement does not depend on a central controller; no explicit host-agent autonomous-mode documentation exists because there are no host agents. [9], [18] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | iCEN schedules backup/restore of iSIDs centrally and iSIM backs up gateway configurations, but no multi-site disaster-recovery synchronization or secondary-site failover is documented. [17], [19] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No FIPS 140-2/140-3 or Common Criteria EAL4+ certification entries or claims were found.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | — | The iSEG DPI firewall documents SCADA protocol support including Siemens S7, and CIARA risk scenarios cover Siemens-protocol commands; no formal Siemens/Honeywell/ABB software-compatibility certifications were found. [18], [24] |

---

## 4. Notable Strengths

- **Real-time asset and flow discovery (items 1.1, 1.5):** iSID automatically learns topology and behavior baselines from mirrored traffic and flags unauthorized or anomalous flows, while CIARA automatically discovers and learns risk indicators [4, 8, 16, 33].
- **Agentless, non-intrusive design (items 3.3, 3.4, 4.1-4.5):** no host agents are installed; detection runs out-of-band on mirrored streams with documented non-disruption of operations, and one-way iSID-to-iCEN isolation plus offline iREC capture support air-gapped OT sites [3, 6, 16, 34].
- **Digital-twin risk simulation (items 2.3, 2.2):** CIARA simulates security controls and WHAT-IF mitigation scenarios on a network digital twin using MITRE ATT&CK-based threat intelligence, and iSID auto-generates policy suggestions from learned baselines [4, 8, 27].
- **Ecosystem integrations (items 5.2, 5.3, 2.1):** a certified ServiceNow OTM CMDB connector syncs asset data in real time, alerts export to SIEM/SOC systems, and per-asset-type or per-device policy enforcement is possible through FortiGate and Cisco ISE pxGrid integrations [20, 21, 23].
- **IEC 62443-oriented compliance workflow (item 6.3):** iSID and CIARA produce IEC 62443-compliant hardening plans and posture reports covering NIS2, NERC CIP and NIST CSF [8, 16, 28].

## 5. Notable Gaps / Risks

- **No host-based workload microsegmentation (items 2.1, 3.1, 3.2, 6.1):** there are no host agents and no container/Kubernetes support; enforcement is network-level IP/MAC/zone whitelisting and device-level NAC, with no tag/label identity policy and no OS process-level enforcement [18, 20, 21].
- **No flow-history retention commitment (item 1.3):** no retention period for connection history is documented anywhere in staged sources, which blocks 90-day forensic traceability requirements.
- **Controller HA and DR are undocumented (items 7.1, 7.3):** no active-active/active-passive cluster HA for the iCEN controller and no multi-site disaster-recovery sync are documented; only per-sensor backup/restore (iCEN) and gateway configuration backups (iSIM) exist [17, 19].
- **No administrative REST API or CI/CD automation (items 5.1, 5.4):** no full administrative REST API or Jenkins/GitLab/Terraform integration is documented; integrations consume partner APIs (pxGrid, FortiGate) and file exports only [20, 21].
- **No FIPS/Common Criteria and limited OT-vendor certification claims (items 8.1, 8.2):** no FIPS 140-2/140-3 or Common Criteria EAL4+ evidence was found, and compatibility with industrial vendors is documented only at Siemens S7 protocol level, without formal Siemens/Honeywell/ABB certifications [17, 24].

## 6. Evidence Quality Notes

17 of 33 items are backed by two or more source types, and 5 of those (1.1, 1.4, 1.5, 2.2, 2.3) include independent third-party coverage from Help Net Security or SecurityWeek; items 1.1 and 1.5 reach high confidence through vendor datasheets plus independent press. CIARA is the best-triangulated component (vendor product page and datasheet, Help Net Security launch and 2021 release coverage that also reports Gartner Hype Cycle recognition, and a SecurityWeek launch article), while iSID detection capabilities are corroborated by SecurityWeek (2015) and Help Net Security (2019). The remaining 15 non-unknown items rely on vendor documentation or datasheets only, so their confidence is capped at medium per the validator rule; this matters most for items 5.3 (ServiceNow), 6.4 (transport encryption) and 7.2 (distributed enforcement), which are single-vendor claims.

10 items (1.3, 2.4, 2.5, 3.2, 3.5, 5.1, 5.4, 6.1, 7.1, 8.1) are rated unknown because no staged source mentions retention, rollback, rule hierarchy, containers, workload counts, admin APIs, CI/CD, process enforcement, controller HA, or FIPS/Common Criteria. Search engines and the Wayback Machine were rate-limited or blocked during the run, so these gaps reflect absence of findable evidence rather than verified absence; the verdicts were chosen conservatively per the anti-fabrication contract. No contradictions between sources were found; where a verdict is partial, it reflects a capability documented in a different form than the checklist asks for (e.g., CIARA attack-simulation on a digital twin versus firewall-policy dry-run; network-level whitelisting versus tag-based policy).

---

## Bibliography

[1] Radiflow. "Radiflow Products | OT security solutions". https://www.radiflow.com/products/ (Retrieved: 2026-08-10T14:30:00Z)
[2] Radiflow. "CIARA OT Risk Management (product page)". https://www.radiflow.com/products/ciara/ (Retrieved: 2026-08-10T14:30:00Z)
[3] Radiflow. "iCEN Centralized security monitoring and risk management (product page)". https://www.radiflow.com/products/icen/ (Retrieved: 2026-08-10T14:30:00Z)
[4] Radiflow. "iSID Visibility and Anomaly Detection (product page)". https://www.radiflow.com/products/ot-visibility-and-anomaly-detection/ (Retrieved: 2026-08-10T14:30:00Z)
[5] Radiflow. "Radiflow OT Security Platform (product page)". https://www.radiflow.com/products/ot-security-and-risk-management-platform/ (Retrieved: 2026-08-10T14:30:00Z)
[6] Radiflow. "vSAP RF-2180 Smart Collector (product page)". https://www.radiflow.com/products/vsap/ (Retrieved: 2026-08-10T14:30:00Z)
[7] Radiflow. "Active Scanner (product page)". https://www.radiflow.com/products/active-scanner/ (Retrieved: 2026-08-10T14:30:00Z)
[8] Radiflow. "CIARA Data-Driven OT Risk Assessment and Management (datasheet)". https://www.radiflow.com/wp-content/uploads/CIARA-Brochure-UPDATED-WEB.pdf (Retrieved: 2026-08-10T14:30:00Z)
[9] Radiflow. "Secure Gateways (product page)". https://www.radiflow.com/products/secure-gateways/ (Retrieved: 2026-08-10T14:30:00Z)
[10] Radiflow. "iSEG RF-1031 Secure Gateway (product page)". https://www.radiflow.com/products/iseg-rf-1031/ (Retrieved: 2026-08-10T14:30:00Z)
[11] Radiflow. "Radiflow360 Full Visibility (product page)". https://www.radiflow.com/products/radiflow360/ (Retrieved: 2026-08-10T14:30:00Z)
[12] Radiflow. "iSIM Industrial Service Manager (product page)". https://www.radiflow.com/products/isim/ (Retrieved: 2026-08-10T14:30:00Z)
[13] Radiflow. "Cisco ISE and Radiflow iSID Joint Solution (product page)". https://www.radiflow.com/products/cisco-ise-radiflow-isid-joint-solution/ (Retrieved: 2026-08-10T14:30:00Z)
[14] Radiflow. "Fortinet & Radiflow Joint Solution (product page)". https://www.radiflow.com/products/fortinet-radiflow/ (Retrieved: 2026-08-10T14:30:00Z)
[15] Radiflow. "Palo Alto Networks & Radiflow Joint Solution (product page)". https://www.radiflow.com/products/joint-solution-palo-alto-networks-radiflow/ (Retrieved: 2026-08-10T14:30:00Z)
[16] Radiflow. "iSID Threat Detection for OT Environments (datasheet)". https://www.radiflow.com/wp-content/uploads/iSID-Brochure-WEB.pdf (Retrieved: 2026-08-10T14:30:00Z)
[17] Radiflow. "iCEN Centralized security monitoring and risk management (datasheet)". https://www.radiflow.com/wp-content/uploads/iCEN-Brochure-WEB.pdf (Retrieved: 2026-08-10T14:30:00Z)
[18] Radiflow. "iSEG RF-3180 Secure Gateway (datasheet)". https://www.radiflow.com/wp-content/uploads/RF-DS-iSEG-3180-APR22.pdf (Retrieved: 2026-08-10T14:30:00Z)
[19] Radiflow. "iSIM Industrial Service Management Tool (datasheet)". https://www.radiflow.com/wp-content/uploads/iSIM-2022.pdf (Retrieved: 2026-08-10T14:30:00Z)
[20] Radiflow / Cisco. "Radiflow iSID & Cisco ISE pxGRID-Certified Integration (joint solution report)". https://www.radiflow.com/wp-content/uploads/Radiflow-Cisco-ISE-JSB-032822.pdf (Retrieved: 2026-08-10T14:30:00Z)
[21] Radiflow / Fortinet. "Fortinet FortiGate NGFW and Radiflow iSID (joint solution brief)". https://www.radiflow.com/wp-content/uploads/JS-Radiflow-Fortinet-111820.pdf (Retrieved: 2026-08-10T14:30:00Z)
[22] Radiflow. "Radiflow360 Full Visibility and Control Across the OT Cybersecurity Lifecycle (brochure)". https://www.radiflow.com/wp-content/uploads/Radiflow360-Brochure.pdf (Retrieved: 2026-08-10T14:30:00Z)
[23] Radiflow / ServiceNow. "Continuous Collection of Accurate OT Asset Data for ServiceNow OT Management (joint brochure)". https://www.radiflow.com/wp-content/uploads/ServiceNow-Radiflow_A4-Brochure-1.pdf (Retrieved: 2026-08-10T14:30:00Z)
[24] Radiflow. "Practical guidelines for conducting IEC 62443 assessments using Radiflow products (security brief)". https://www.radiflow.com/wp-content/uploads/WP-62443-compliance-051120-1.pdf (Retrieved: 2026-08-10T14:30:00Z)
[25] Help Net Security. "Radiflow360 unifies OT risk, compliance, and response". https://www.helpnetsecurity.com/2025/10/08/radiflow-radiflow360/ (Retrieved: 2026-08-10T14:30:00Z)
[26] Help Net Security. "Sabanci acquires Radiflow to boost its cybersecurity offerings across various industrial sectors". https://www.helpnetsecurity.com/2022/05/04/radiflow-sabanci-group/ (Retrieved: 2026-08-10T14:30:00Z)
[27] Help Net Security. "Radiflow's risk management platform for OT facilities allows CISOs to view all their sites on one dashboard". https://www.helpnetsecurity.com/2021/08/25/radiflow-ciara-software/ (Retrieved: 2026-08-10T14:30:00Z)
[28] Help Net Security. "Radiflow launches CIARA, a ROI-driven risk assessment and management platform for industrial organizations". https://www.helpnetsecurity.com/2020/08/05/radiflow-ciara/ (Retrieved: 2026-08-10T14:30:00Z)
[29] Help Net Security. "Radiflow releases new version of its industrial threat detection solution". https://www.helpnetsecurity.com/2019/02/28/radiflow-isid/ (Retrieved: 2026-08-10T14:30:00Z)
[30] SecurityWeek. "Radiflow Launches Industrial Risk Analysis Platform". https://www.securityweek.com/radiflow-launches-industrial-risk-analysis-platform/ (Retrieved: 2026-08-10T14:30:00Z)
[31] SecurityWeek. "Radiflow Unveils New OT Security Platform". https://www.securityweek.com/radiflow-unveils-new-ot-security-platform/ (Retrieved: 2026-08-10T14:30:00Z)
[32] Help Net Security. "Radiflow and Fraunhofer develop ML and AI methods for industrial cybersecurity". https://www.helpnetsecurity.com/2020/02/03/radiflow-fraunhofer/ (Retrieved: 2026-08-10T14:30:00Z)
[33] SecurityWeek. "Radiflow Launches New Intrusion Detection System for ICS/SCADA Networks". https://www.securityweek.com/radiflow-launches-new-intrusion-detection-system-icsscada-networks/ (Retrieved: 2026-08-10T14:30:00Z)
[34] Radiflow. "Incorporating Radiflow's iSID in a managed OT SOC (case study)". https://www.radiflow.com/case-studies/incorporating-radiflows-isid-in-a-managed-ot-soc/ (Retrieved: 2026-08-10T14:30:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 28
- **Sources reviewed:** 34 (kept: 34, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 1, third_party_review: 9, vendor_datasheet: 6, vendor_doc: 18
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
