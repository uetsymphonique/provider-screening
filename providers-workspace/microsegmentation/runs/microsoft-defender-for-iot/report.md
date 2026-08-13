# Microsegmentation Product Assessment: Microsoft - Microsoft Defender for IoT

**Product ID:** `microsoft-defender-for-iot`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T16:49:36Z
**Total evidence items collected:** 71
**Total distinct sources:** 32

---

## 1. Overview

Microsoft Defender for IoT is Microsoft's OT/IoT security monitoring product: an agentless, network-layer detection and visibility platform that discovers devices, tracks connections, assesses vulnerabilities, and detects threats across industrial control networks [1]. It is positioned as a visibility and NDR layer rather than a microsegmentation enforcement product: network sensors connect to SPAN ports or network TAPs and perform detection locally, with telemetry forwarded to the Azure portal for central management [2]. Deployment shapes include cloud-connected sensors managed from the Azure portal, locally managed sensors, and fully air-gapped on-premises deployments managed via the sensor console UI or CLI [1], [14]. It integrates with Microsoft Sentinel, Splunk, QRadar and other SIEMs, and with ServiceNow for OT asset synchronization [22], [25], [26]. Enterprise IoT coverage is available through Microsoft Defender for Endpoint [18]. Against the 33-item checklist it scores strongly on visibility, SIEM integration, air-gapped support and OT protocol breadth, but has no policy creation, enforcement, simulation, rollback, or hierarchical rule management capabilities.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 7     | 2                | 5      | 0   |
| partial          | 14    | 0                | 14     | 0   |
| not_supported    | 4     | 0                | 4      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 5     | 0                | 5      | 0   |

**Evidence quality:** 4 items backed by ≥ 2 source_types; 26 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** No host agent is installed; monitoring is agentless at the network layer, so a per-host agent CPU overhead does not apply.
- **4.2:** No host agent is deployed; sensors run on dedicated physical or virtual appliances connected to SPAN ports or TAPs, so a per-host agent RAM footprint does not apply.
- **4.3:** Sensors attach out-of-band to SPAN ports or TAPs and are not in the forwarding path, so no inline latency is added to monitored traffic.
- **4.4:** With no host agent installed, there is no agent whose failure could interrupt host traffic; sensors passively tap mirrored traffic.
- **4.5:** Nothing is installed on monitored hosts, so agent installation or updates involve no reboot.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | Network sensors continuously discover devices and monitor traffic using agentless, network-layer monitoring; PeerSpot users report real-time alerts and detailed threat graphics. [1], [2], [32] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | A device map shows detected devices and their connections, organized by Purdue layers, subnets, zones, VLANs, or custom groups; no App/Environment/Role/Process grouping views are documented. [6] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 90 days | Device and alert data are retained for 90 days in both the Azure portal and on OT sensors, and sensor event timeline retention is not time-limited, retaining at least 90 days of events on all hardware profiles. [8] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | - | CVE details and CVSS scores are shown on device details and inventory pages reachable from the device map via drill-down, rather than rendered directly on the map itself. [4], [5], [6] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Devices detected after the learning period are flagged as unauthorized and new, and the device map marks newly detected or unauthorized devices. [3], [6] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Not Supported | medium | - | Documented as agentless, passive network-layer monitoring with no policy creation or enforcement; device tags exist only as inventory metadata, not as a basis for traffic policy. [1], [2], [3] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | - | Machine-generated security recommendations exist for device health (e.g., review unauthorized devices, patch vulnerable vendors), but they are remediation suggestions, not connectivity policy rule recommendations. [29] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | Risk assessment reports evaluate risks from imported firewall rules, but no policy simulation or dry-run mode for segmentation policies is documented. [30] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Not Supported | medium | - | With no policy creation or enforcement in the product, no policy rollback mechanism exists or is documented. [1], [2] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Not Supported | medium | - | Sites and zones provide an organizational hierarchy used for grouping and access control, but no inherited or hierarchical traffic rule management is documented. [9] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | medium | - | Agentless network sensors discover devices of all types regardless of OS, and the device inventory records OS platform and version (e.g., Windows 10, Ubuntu 20.04.1); PeerSpot users note it is easy to install on any OS. [2], [3], [32] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | OT monitoring is agentless via network sensors; an agent-based path exists only for enterprise IoT discovery through Microsoft Defender for Endpoint, not as a host microsegmentation agent. [1], [18] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | Air-gapped deployments are explicitly supported: sensors are managed via the sensor console UI or CLI with all data kept on-premises, and this support is unaffected by the on-premises management console retirement. [1], [14], [15] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | 12000 workloads | Vendor sizing caps the largest sensor profile (C5600) at 12,000 monitored assets; scale-out across multiple sensors is possible but no single-controller capacity of 50,000+ is documented, and a PeerSpot user reports needing an additional server per industrial network. [12], [32] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | - | No host agent is installed; monitoring is agentless at the network layer, so a per-host agent CPU overhead does not apply. [1] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | - | No host agent is deployed; sensors run on dedicated physical or virtual appliances connected to SPAN ports or TAPs, so a per-host agent RAM footprint does not apply. [2] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | - | Sensors attach out-of-band to SPAN ports or TAPs and are not in the forwarding path, so no inline latency is added to monitored traffic. [2] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | - | With no host agent installed, there is no agent whose failure could interrupt host traffic; sensors passively tap mirrored traffic. [2] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | - | Nothing is installed on monitored hosts, so agent installation or updates involve no reboot. [1] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | REST APIs cover sensor data access (device inventory, CVEs, alerts, timeline events, vulnerabilities) and some actions, but vendor docs do not claim 100% coverage of administrative functions. [31] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | - | Cloud alerts stream to Microsoft Sentinel and onward to SIEMs such as Splunk and QRadar via Event Hubs; on-premises sensors forward alerts via syslog (CEF) to partner systems, and PeerSpot users confirm Sentinel integration. [22], [25], [26], [28], [32] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | - | ServiceNow integrations (Operational Technology Manager, Service Graph Connector) synchronize OT assets, network connections, and vulnerabilities into the CMDB; tag synchronization specifically is not documented. [22], [24] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | - | The product is documented as a passive detection and visibility solution with no traffic or process-level enforcement capability. [1], [2] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat intelligence packages (malware signatures, CVEs) are delivered and updated on sensors; no honeypot or deception detection capability was found in the staged documentation. [21] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Compliance resources document FedRAMP High and DoD IL2/IL4/IL5 provisional authorizations, Zero Trust principle alignment, and IEC 62443-oriented deployments; no built-in PCI-DSS, ISO 27001, or NIST 800-207 report templates were found. [9], [11], [14] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | Sensor-to-cloud traffic uses HTTPS on port 443, alert forwarding supports TLS certificate encryption, and API connections are SSL-secured; there is no agent, and TLS 1.3 or mutual-auth specifics are not documented. [16], [27], [31] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | - | Management moved to the Azure portal as sensors are onboarded per site; no active-active or active-passive controller cluster architecture is documented, and the on-premises management console is retired. [2], [15], [16] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | Sensors keep analyzing and securing the network when management is unavailable and process data locally, but there are no host agents or enforced policies to keep executing; autonomy applies to monitoring, not policy enforcement. [2], [15] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Daily automated sensor backups and external SMB backup targets are documented; no multi-site controller disaster-recovery synchronization is documented. [14], [19] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | - | no evidence found |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Supported | medium | - | The supported OT protocol list includes Siemens (S7, PCS7, WinCC), Honeywell (Experion DCS, ENAP), and ABB (800xA DCS, Totalflow) protocols for device discovery. [10] |

---

## 4. Notable Strengths

- **Agentless real-time OT/IoT discovery (items 1.1, 1.5):** Network sensors continuously discover and monitor devices with no host agents, and devices detected after the learning period are flagged as unauthorized or new [2], [3].
- **Air-gapped deployment (item 3.4):** Fully offline management via the sensor console UI or CLI is explicitly supported and is unaffected by the on-premises management console retirement [14], [15].
- **SIEM/SOAR integration breadth (items 5.2, 5.3):** Sentinel, Splunk, QRadar, syslog/CEF forwarding, and ServiceNow OT asset sync are documented and user-confirmed [22], [25], [26], [32].
- **OT protocol compatibility (item 8.2):** Siemens (S7, PCS7, WinCC), Honeywell (Experion DCS), and ABB (800xA DCS) protocols are supported for device discovery [10].
- **90-day forensic retention (item 1.3):** Device and alert data are retained for 90 days in the portal and on sensors, and sensor event timeline retention is not time-limited [8].

## 5. Notable Gaps / Risks

- **No microsegmentation enforcement (items 2.1, 6.1):** The product is passive detection only, with no policy creation, process-level control, or enforcement; buyers needing traffic isolation must pair it with firewall or segmentation tooling [1], [2].
- **No policy lifecycle tooling (items 2.3, 2.4, 2.5):** No policy simulation, one-click rollback, or hierarchical rule management exists because no enforcement engine exists to manage [1], [9].
- **Controller scale below 50,000 (item 3.5):** The largest documented sensor profile monitors 12,000 assets, no single-controller capacity of 50,000+ workloads is documented, and a PeerSpot user reports needing an additional server per industrial network [12], [32].
- **Kubernetes, CI/CD, and certification gaps (items 3.2, 5.4, 8.1):** No evidence found for container/Kubernetes isolation, CI/CD pipeline integration, or FIPS 140-2/140-3 or Common Criteria EAL4+ certification.
- **Agent-centric checklist items are not applicable (items 4.1-4.5):** The agentless architecture means there is no agent overhead, agent fail-safe, or reboot concern to evaluate; sensor appliance availability is the relevant resilience surface [1], [2].

## 6. Evidence Quality Notes

The assessment covers all 33 items with 71 evidence entries drawn from 32 staged sources. Only one source is independent of the vendor (PeerSpot community reviews, source [32]), so 26 items rest on vendor documentation alone and are capped at medium confidence per the validator rule; the four items that also cite PeerSpot (1.1, 3.1, 3.5, 5.2) reach high confidence on 1.1 and 5.2 where the community evidence is directly on-point. Unknown items (3.2, 5.4, 8.1) reflect a genuine absence of evidence in the staged material rather than verified absence of the capability.

One direct contradiction surfaced: a PeerSpot reviewer states the product "is not scalable" while vendor sizing tables document multi-profile scale-out with a 12,000-asset per-sensor ceiling [12], [32]; the verdict for 3.5 is therefore partial, anchored to the vendor's explicit per-sensor number with the community concern noted. High-availability items (7.1-7.3) rely on the on-premises management console retirement notice and sensor backup documentation, which describe operational resilience of sensors but no controller-tier cluster or multi-site DR architecture.

---

## Bibliography

[1] Microsoft Learn. "Microsoft Defender for IoT overview". https://learn.microsoft.com/en-us/azure/defender-for-iot/overview (Retrieved: 2026-08-10)
[2] Microsoft Learn. "Defender for IoT OT architecture and components". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/architecture (Retrieved: 2026-08-10)
[3] Microsoft Learn. "Defender for IoT device inventory". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/device-inventory (Retrieved: 2026-08-10)
[4] Microsoft Learn. "Vulnerability management for Defender for IoT". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/vulnerability-management (Retrieved: 2026-08-10)
[5] Microsoft Learn. "Manage device inventory from the Azure portal". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-manage-device-inventory-for-organizations (Retrieved: 2026-08-10)
[6] Microsoft Learn. "Investigate devices on a device map". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-work-with-the-sensor-device-map (Retrieved: 2026-08-10)
[7] Microsoft Learn. "Manage OT device inventory from a sensor console". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-investigate-sensor-detections-in-a-device-inventory (Retrieved: 2026-08-10)
[8] Microsoft Learn. "Data retention, privacy, and sharing". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/references-data-retention (Retrieved: 2026-08-10)
[9] Microsoft Learn. "Zero Trust and your OT networks". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/concept-zero-trust (Retrieved: 2026-08-10)
[10] Microsoft Learn. "Supported IoT, OT, ICS, and SCADA protocols". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/concept-supported-protocols (Retrieved: 2026-08-10)
[11] Microsoft Learn. "Defender for IoT compliance resources". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/compliance (Retrieved: 2026-08-10)
[12] Microsoft Learn. "Which OT appliances do I need?". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/ot-appliance-sizing (Retrieved: 2026-08-10)
[13] Microsoft Learn. "Preconfigured physical appliances for OT monitoring". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/ot-pre-configured-appliances (Retrieved: 2026-08-10)
[14] Microsoft Learn. "Deploy hybrid or air-gapped OT sensor management". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/ot-deploy/air-gapped-deploy (Retrieved: 2026-08-10)
[15] Microsoft Learn. "On-premises management console retirement". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/ot-deploy/on-premises-management-console-retirement (Retrieved: 2026-08-10)
[16] Microsoft Learn. "Manage sensors in the Azure portal". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-manage-sensors-on-the-cloud (Retrieved: 2026-08-10)
[17] Microsoft Learn. "Manage individual OT network sensors". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-manage-individual-sensors (Retrieved: 2026-08-10)
[18] Microsoft Learn. "Get started with enterprise IoT security monitoring". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/eiot-defender-for-endpoint (Retrieved: 2026-08-10)
[19] Microsoft Learn. "Back up and restore OT network sensors". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/back-up-restore-sensor (Retrieved: 2026-08-10)
[20] Microsoft Learn. "Configure active monitoring for OT networks". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/configure-active-monitoring (Retrieved: 2026-08-10)
[21] Microsoft Learn. "Maintain threat intelligence packages on OT sensors". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-work-with-threat-intelligence-packages (Retrieved: 2026-08-10)
[22] Microsoft Learn. "Integrations with Microsoft and partner services". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/integrate-overview (Retrieved: 2026-08-10)
[23] Microsoft Learn. "Stream Defender for IoT cloud alerts to a partner SIEM". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/integrations/send-cloud-data-to-partners (Retrieved: 2026-08-10)
[24] Microsoft Learn. "Integrate ServiceNow with Microsoft Defender for IoT". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/tutorial-servicenow (Retrieved: 2026-08-10)
[25] Microsoft Learn. "Integrate Splunk with Microsoft Defender for IoT". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/tutorial-splunk (Retrieved: 2026-08-10)
[26] Microsoft Learn. "Integrate Qradar with Microsoft Defender for IoT". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/tutorial-qradar (Retrieved: 2026-08-10)
[27] Microsoft Learn. "Connect OT network sensors to Microsoft Sentinel (legacy)". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/integrations/on-premises-sentinel (Retrieved: 2026-08-10)
[28] Microsoft Learn. "Forward on-premises OT alert information to partners". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-forward-alert-information-to-partners (Retrieved: 2026-08-10)
[29] Microsoft Learn. "Enhance security posture with security recommendations". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/recommendations (Retrieved: 2026-08-10)
[30] Microsoft Learn. "Create risk assessment reports on an OT sensor". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/how-to-create-risk-assessment-reports (Retrieved: 2026-08-10)
[31] Microsoft Learn. "Defender for IoT API reference". https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/references-work-with-defender-for-iot-apis (Retrieved: 2026-08-10)
[32] PeerSpot. "Microsoft Defender for IoT reviews (PeerSpot)". https://www.peerspot.com/products/microsoft-defender-for-iot-reviews (Retrieved: 2026-08-10)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 32 (kept: 32, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** community: 1, vendor_doc: 31
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
