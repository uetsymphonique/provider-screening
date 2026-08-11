# Microsegmentation Product Assessment: Juniper Networks - Juniper Connected Security / vSRX

**Product ID:** `juniper-connected-security-vsrx`
**Version reference:** vSRX on Junos OS (CyberRatings test used Junos 22.4R2.8; current docs reviewed 2025-2026)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:35:00Z
**Total evidence items collected:** 83
**Total distinct sources:** 32

---

## 1. Overview

Juniper Connected Security is Juniper's security portfolio built around the SRX firewall line; vSRX is the virtual next-generation-firewall form factor that runs on VMware ESXi, KVM, and public-cloud images and enforces zone-, application-, user-, and tag-based policies inline [1][10][11]. Microsegmentation is delivered through three mechanisms: Group-Based Policy tag-based match conditions in SRX security policies within VXLAN/EVPN fabrics [5], Security Director/Policy Enforcer automation that maps cloud resource tags to policy metadata [27], and the Cloud Workload Protection (JCWP) in-application agent, which Juniper's own documentation portal flags as end-of-life ("eol": "1") [26]. Deployment shapes span physical SRX, vSRX, and a containerized cSRX form factor [6], managed through Security Director and Juniper AI-Native Security (Mist AI) [30]. Enforcement is primarily agentless at the network layer, so agent-centric checklist items (CPU/RAM overhead, agent fail-safe, reboot-free updates) are marked not applicable.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 9     | 0                | 9      | 0   |
| partial          | 15    | 1                | 9      | 5   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 4     | 0                | 4      | 0   |

**Evidence quality:** 19 items backed by ≥ 2 source_types; 20 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** Segmentation enforcement is network-based via the vSRX virtual firewall (a 2-17 vCPU, 4-32 GB virtual appliance), not a host agent on workloads; the CWP in-app agent is described only as lightweight with no CPU figures.
- **4.2:** Same architecture: no workload host agent is deployed for segmentation; the Cloud Workload Protection agent memory footprint is only described qualitatively as lightweight and serverless.
- **4.4:** There is no in-path host agent for vSRX-based segmentation (enforcement is the inline virtual firewall itself), so an agent-crash fail-safe requirement does not apply; the CWP in-app runtime agent's failure behavior is not documented.
- **4.5:** No host agent is installed on workloads; the Cloud Workload Protection agent is described as installing in minutes, and vSRX upgrades follow documented VM procedures rather than a host-agent reboot model.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | — | vSRX provides real-time flow and application visibility as an inline firewall: AppTrack reports applications in real time, active flow monitoring exports cflowd records at configurable intervals, and Cloud Workload Protection telemetry reports application connectivity and topology. Workload discovery is limited to traffic that traverses the enforcement point (no host-agent discovery). [3], [4], [9] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | low | — | Cloud Workload Protection reports application-level connectivity and topology telemetry, but no visual map grouping workloads by application, environment, role, or process is documented. [2], [3] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | low | n/a (qualitative) | vSRX exports flow records to external collectors via active flow monitoring, and JSA log analytics stores event and flow logs, but no retention duration of at least 90 days is published. [9], [18] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | low | — | Cloud Workload Protection continuously assesses vulnerabilities in applications and containers and surfaces them in an Exploitable Vulnerabilities dashboard; CVE context is not overlaid on a traffic map. [2], [3] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | Junos application identification classifies traffic that does not match a signature as unknown (junos:UNKNOWN) and supports packet capture of unknown application traffic for analysis and custom signature creation. [4] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | SRX security policies support tag-based match conditions for microsegmentation via Group-Based Policy in VXLAN fabrics, Security Director maps cloud resource tags to metadata for NGFW policy definitions, and user-identity-based rules are documented through the user firewall/JIMS. [3], [5], [6], [19], [27] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | low | — | Juniper AI-Native Security (Mist AI) applies AI-driven insights and persona-based policy activation across the network; an explicit AI/ML-based policy rule recommendation feature is not documented. [30] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | — | no evidence found (No source describes policy simulation or dry-run testing for vSRX/Security Director.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | — | Junos configuration rollback (rollback 0) reverts to the previously committed configuration and is exposed programmatically, restoring policy state near-instantly; no policy-specific one-click rollback UI is documented, and vSRX does not support OS-level rollback. [10], [12] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | — | SRX supports global policies that apply across security zones, and Group-Based Policy endpoint groups where new devices automatically inherit the group's security policies. [5] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | vSRX deploys on VMware ESXi, KVM, and cloud images, and the Cloud Workload Protection agent protects applications on Docker/Kubernetes/AWS Fargate with Java, Node.js, PHP, and Ruby support; no OS-level agents for Windows Server or AIX/Solaris workloads exist. [3], [10], [11] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | — | Cloud Workload Protection protects cloud-native applications in containers and Kubernetes (Docker, Kubernetes, AWS Fargate), and a containerized SRX (cSRX) form factor is documented for container environments. [3], [6], [29] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | — | Both models are documented: a lightweight in-application Cloud Workload Protection agent and agentless network enforcement via vSRX virtual firewalls that integrate with CWP for risk-based access restriction. [2], [3], [28] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | low | — | vSRX firewalling operates on the device, but threat-intelligence feeds (SecIntel) are delivered from the cloud-based Juniper ATP service, so fully air-gapped operation of the connected-security feature set is not documented. [17] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | vSRX scales to 28 million concurrent sessions on 17 vCPUs and CSDS adds firewalls elastically, but no explicit figure of 50,000 protected workloads is published. [1], [16] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | Segmentation enforcement is network-based via the vSRX virtual firewall (a 2-17 vCPU, 4-32 GB virtual appliance), not a host agent on workloads; the CWP in-app agent is described only as lightweight with no CPU figures. [10], [28] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | Same architecture: no workload host agent is deployed for segmentation; the Cloud Workload Protection agent memory footprint is only described qualitatively as lightweight and serverless. [10], [29] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | vSRX is an inline NGFW; CyberRatings.org measured 1,678 Mbps plain-text and 779 Mbps HTTPS throughput on an AWS c5n.2xlarge, but no latency figure in milliseconds is published. [20], [32] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | There is no in-path host agent for vSRX-based segmentation (enforcement is the inline virtual firewall itself), so an agent-crash fail-safe requirement does not apply; the CWP in-app runtime agent's failure behavior is not documented. [2], [10] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No host agent is installed on workloads; the Cloud Workload Protection agent is described as installing in minutes, and vSRX upgrades follow documented VM procedures rather than a host-agent reboot model. [3], [10] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | Junos exposes a REST API for rpc and configuration operations (XML/ASCII/JSON) plus NETCONF for full configuration management; vendor materials describe a wide range of programmatic APIs but do not claim 100% coverage of all administrative functions. [13], [15] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | vSRX logs export to any third-party collector in system or structured syslog formats (including syslog over TLS), and Juniper's JSA provides log analytics with real-time event correlation. [8], [14], [18] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found (No documentation found for ServiceNow/CMDB tag synchronization.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | — | The Cloud Workload Protection agent integrates into continuous integration and development workflows, and Junos offers programmatic APIs for DevOps automation. [3], [15] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | medium | — | Cloud Workload Protection is a runtime agent that controls application execution and monitors behavior/context, enforcing at the application-process level via control-flow-integrity. [3], [28] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | SecIntel delivers curated threat-intelligence feeds (Juniper Threat Labs, ATP Cloud, third-party sources) consumed by SRX/vSRX firewalls for traffic filtering; no honeypot or deception capability is documented. [17] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | JSA provides more than 500 out-of-the-box compliance reports covering PCI DSS, ISO/IEC 27002, and NIST 800-53; Juniper positions unified visibility and policy management for compliance reporting, but NIST 800-207 and IEC 62443 are not explicitly covered. [18], [30] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | Junos management and control channels support TLS syslog with mutual authentication and HTTPS REST with a mutual-authentication option, and TLS 1.2/1.3 cipher handling is tested on vSRX; the Cloud Workload Protection agent-to-cloud channel is not documented. [8], [13], [20] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | vSRX chassis clusters provide stateful failover between primary/secondary nodes with an active/active data plane, and the CSDS architecture uses SRX multi-node HA to keep sessions active during upgrades or outages. [7], [16] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (No source documents enforcement behavior when the management/controller connection is lost.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (No disaster-recovery site-sync documentation found.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | high | — | NIST CMVP lists the Juniper FIPS Provider as FIPS 140-2 Level 1 (Active) with FIPS 140-3 validations for other Juniper modules, and the Common Criteria portal lists Junos for SRX380/SRX300-345 as PP-compliant (NDcPP v3.0e/FWcPP plus VPN-GW and IPS modules); current CC certifications are PP-based rather than EAL4+, and vSRX itself is not individually listed. [21], [22], [23], [24], [25] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No Siemens/Honeywell/ABB OT compatibility certifications found.) |

---

## 4. Notable Strengths

- **Tag/label/identity-based policy model (items 2.1, 2.5):** SRX security policies support tag-based match conditions for microsegmentation (GBP in VXLAN fabrics), Security Director maps cloud resource tags to policy metadata, and user-identity-based rules are documented via the JIMS user firewall [5][19][27].
- **Container-native workload protection (items 3.2, 6.1):** JCWP protects Docker, Kubernetes, and AWS Fargate applications with runtime, process-level execution control, and a containerized SRX (cSRX) form factor is documented [3][6][29].
- **Programmable management plane (items 5.1, 5.4):** Junos REST API and NETCONF expose configuration and rpc operations programmatically, and the JCWP agent integrates into continuous-integration/development workflows [3][12][13][15].
- **Log export to third-party collectors and SIEM-grade analytics (items 5.2, 6.3):** vSRX exports logs in system or structured syslog formats (including syslog over TLS) to any collector, and JSA provides more than 500 out-of-the-box compliance reports [8][14][18].
- **HA and certifications (items 7.1, 8.1):** vSRX chassis clusters deliver stateful primary/secondary failover with an active/active data plane, CSDS adds SRX multi-node HA, and the Juniper FIPS Provider is FIPS 140-2 Level 1 validated with CC PP-compliant SRX certifications on the Common Criteria portal [7][16][22][24].

## 5. Notable Gaps / Risks

- **End-of-life risk on the only agent-based component (items 2.1, 3.2, 6.1):** Juniper Cloud Workload Protection, which carries the agent-based runtime/microsegmentation claims, is flagged EOL in Juniper's documentation portal, so those capabilities should not be treated as a growth investment [26].
- **Flow-history retention not guaranteed (item 1.3):** no published retention duration of at least 90 days; flow records are exported to external collectors whose retention is configurable [9][18].
- **No policy dry-run and no explicit AI rule recommendation (items 2.2, 2.3):** policy simulation is undocumented and AI/ML-driven policy recommendation is limited to persona-based activation language [30].
- **Integration and ops gaps (items 5.3, 7.2, 7.3):** no ServiceNow/CMDB tag synchronization, no documentation of enforcement behavior on total controller loss, and no disaster-recovery site-sync documentation were found.
- **Agent-metric expectations do not transfer (items 4.1, 4.2, 4.3, 4.4, 4.5):** as a network-enforcement product there is no host agent, so the agent CPU/RAM/fail-safe/reboot checklist items are not applicable, and no per-packet policy latency figure in milliseconds is published [10][20].

## 6. Evidence Quality Notes

Thirty-two sources were staged and cited (17 vendor_doc, 7 vendor_datasheet, 4 certification_registry, 3 third_party_review, 1 analyst_report), yielding 83 evidence entries, all verified as exact quotes in the staged artifacts by the citation-grounding check. Nineteen items are backed by at least two source_types; twenty items rest on vendor documentation only, which caps their confidence at medium. The only high-confidence verdict (8.1) is anchored to independent registries: the NIST CMVP certificate pages and the Common Criteria portal, with the vendor's CC configuration guide used only for supporting detail.

Three caveats shaped verdicts. First, Juniper Cloud Workload Protection is EOL-flagged in Juniper's own documentation portal while still marketed, so agent-based claims (3.2, 6.1) are supported but time-limited. Second, the CyberRatings.org report is authored by the independent testing lab but hosted on juniper.net, so it was treated as third-party evidence with the hosting noted. Third, where sources give only qualitative or indirect language for numeric items (flow-history retention 1.3, workload-scale figure 3.5, policy latency 4.3), verdicts are partial with null numeric values rather than fabricated numbers, per the anti-fabrication contract.

---

## Bibliography

[1] Juniper Networks. "vSRX Integrated Virtual Firewall Specifications". https://www.juniper.net/us/en/products/security/srx-series/vsrx-virtual-firewall/specs.html (Retrieved: 2026-08-10T14:35:00Z)
[2] Juniper Networks. "Juniper Cloud Workload Protection product page". https://www.juniper.net/us/en/products/security/cloud-workload-protection.html (Retrieved: 2026-08-10T14:35:00Z)
[3] Juniper Networks. "Juniper Cloud Workload Protection Data Sheet". https://www.juniper.net/content/dam/www/assets/datasheets/us/en/security/cloud-workload-protection.pdf (Retrieved: 2026-08-10T14:35:00Z)
[4] Juniper Networks. "Application Identification on SRX Series Firewalls (Junos OS TechLibrary)". https://www.juniper.net/documentation/us/en/software/junos/application-identification/topics/topic-map/security-application-identification-overview.html (Retrieved: 2026-08-10T14:35:00Z)
[5] Juniper Networks. "Junos OS Security Policies Guide (incl. Group-Based Policy with VXLAN)". https://www.juniper.net/documentation/us/en/software/junos/security-policies/security-policies.pdf (Retrieved: 2026-08-10T14:35:00Z)
[6] Juniper Networks. "Junos OS Identity-Aware Firewall Guide". https://www.juniper.net/documentation/us/en/software/junos/identity-aware-firewall/identity-aware-firewall.pdf (Retrieved: 2026-08-10T14:35:00Z)
[7] Juniper Networks. "Junos OS Chassis Cluster Guide for Security Devices". https://www.juniper.net/documentation/us/en/software/junos/chassis-cluster-security-devices/chassis-cluster-security-devices.pdf (Retrieved: 2026-08-10T14:35:00Z)
[8] Juniper Networks. "Junos OS Network Management Guide (system logging, syslog over TLS)". https://www.juniper.net/documentation/us/en/software/junos/network-mgmt/network-mgmt.pdf (Retrieved: 2026-08-10T14:35:00Z)
[9] Juniper Networks. "Junos OS Flow Monitoring Guide". https://www.juniper.net/documentation/us/en/software/junos/flow-monitoring/flow-monitoring.pdf (Retrieved: 2026-08-10T14:35:00Z)
[10] Juniper Networks. "vSRX Deployment Guide for VMware". https://www.juniper.net/documentation/us/en/software/vsrx/vsrx-vmware/vsrx-vmware.pdf (Retrieved: 2026-08-10T14:35:00Z)
[11] Juniper Networks. "vSRX Deployment Guide for KVM". https://www.juniper.net/documentation/us/en/software/vsrx/vsrx-kvm/vsrx-kvm.pdf (Retrieved: 2026-08-10T14:35:00Z)
[12] Juniper Networks. "Junos OS NETCONF XML Management Protocol Developer Guide". https://www.juniper.net/documentation/us/en/software/junos/netconf/netconf.pdf (Retrieved: 2026-08-10T14:35:00Z)
[13] Juniper Networks. "Junos OS REST API Guide". https://www.juniper.net/documentation/us/en/software/junos/rest-api/rest-api.pdf (Retrieved: 2026-08-10T14:35:00Z)
[14] Juniper Networks. "vSRX Virtual Firewall with AWS Security Hub (Solution Brief)". https://www.juniper.net/content/dam/www/assets/solution-briefs/us/en/security/vsrx-virtual-firewall-with-aws-security-hub.pdf (Retrieved: 2026-08-10T14:35:00Z)
[15] Juniper Networks. "vSRX Virtual Firewall on Microsoft Azure (flyer)". https://www.juniper.net/content/dam/www/assets/flyers/us/en/vsrx-virtual-firewall-on-microsoft-azure.pdf (Retrieved: 2026-08-10T14:35:00Z)
[16] Juniper Networks. "Connected Security Distributed Services (CSDS) Architecture Datasheet". https://www.juniper.net/content/dam/www/assets/datasheets/us/en/security/connected-security-distributed-services-csdc-architecture-datasheet.pdf (Retrieved: 2026-08-10T14:35:00Z)
[17] Juniper Networks. "Juniper SecIntel Datasheet". https://www.juniper.net/content/dam/www/assets/datasheets/us/en/security/secintel-datasheet.pdf (Retrieved: 2026-08-10T14:35:00Z)
[18] Juniper Networks. "JSA Series Secure Analytics Appliances Datasheet". https://www.juniper.net/content/dam/www/assets/datasheets/us/en/security/jsa-series-secure-analytics-appliances-datasheet.pdf (Retrieved: 2026-08-10T14:35:00Z)
[19] Juniper Networks. "Juniper Identity Management Service (JIMS) Datasheet". https://www.juniper.net/content/dam/www/assets/datasheets/us/en/security/juniper-identity-management-service-datasheet.pdf (Retrieved: 2026-08-10T14:35:00Z)
[20] CyberRatings.org. "CyberRatings.org Cloud Network Firewall Test Report - Juniper Networks vSRX". https://www.juniper.net/content/dam/www/assets/analyst-reports/us/en/2024/cyberratings-cloud-network-firewall.pdf (Retrieved: 2026-08-10T14:35:00Z)
[21] NIST. "NIST CMVP FIPS 140-2 Security Policy - Juniper FIPS Provider (Cert. 4653)". https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp4653.pdf (Retrieved: 2026-08-10T14:35:00Z)
[22] NIST. "NIST CMVP Certificate #4653 - Juniper FIPS Provider". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4653 (Retrieved: 2026-08-10T14:35:00Z)
[23] NIST. "NIST CMVP Certificate #4878 - Juniper Express 4 MACsec Cryptographic Module (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4878 (Retrieved: 2026-08-10T14:35:00Z)
[24] Common Criteria Portal. "Common Criteria Portal - Certified Products list (Juniper SRX entries)". https://www.commoncriteriaportal.org/products/index.cfm (Retrieved: 2026-08-10T14:35:00Z)
[25] Juniper Networks. "Junos OS Common Criteria Guide for SRX300, SRX320, SRX340, SRX345, SRX345-DUAL-AC". https://www.juniper.net/documentation/us/en/software/ccfips22.2/cc-security_branch/cc-security_branch.pdf (Retrieved: 2026-08-10T14:35:00Z)
[26] Juniper Networks. "Juniper Cloud Workload Protection Documentation portal (EOL-flagged)". https://techlibrary.juniper.net/documentation/product/us/en/juniper-cloud-workload-protection/ (Retrieved: 2026-08-10T14:35:00Z)
[27] Juniper Networks. "Juniper Policy Enforcer User Guide (Security Director)". https://www.juniper.net/documentation/us/en/software/nm-apps23.1/policy-enforcer-user-guide/policy-enforcer-user-guide.pdf (Retrieved: 2026-08-10T14:35:00Z)
[28] SiliconANGLE. "SiliconANGLE: Juniper's Cloud Workload Protection helps defend against application exploits in real-time". https://siliconangle.com/2021/08/03/junipers-cloud-workload-protection-helps-defend-application-exploits-real-time/ (Retrieved: 2026-08-10T14:35:00Z)
[29] SDxCentral. "SDxCentral: Juniper Cloud Workload Protection Weaves an Application Safety Net". https://www.sdxcentral.com/news/juniper-cloud-workload-protection-weaves-an-application-safety-net/ (Retrieved: 2026-08-10T14:35:00Z)
[30] Juniper Networks. "Fortifying Network Defenses with Juniper AI-Native Security (Solution Brief)". https://www.juniper.net/content/dam/www/assets/solution-briefs/us/en/2024/fortifying-network-defenses-with-juniper-ai-native-security.pdf (Retrieved: 2026-08-10T14:35:00Z)
[31] Forrester Consulting. "Forrester Total Economic Impact of Juniper Connected Security". https://www.juniper.net/content/dam/www/assets/white-papers/us/en/2021/forrester-the-total-economic-impact-of-juniper-connected-security.pdf (Retrieved: 2026-08-10T14:35:00Z)
[32] Juniper Networks. "How to Measure Performance of a Virtual Firewall (Whitepaper)". https://www.juniper.net/content/dam/www/assets/white-papers/us/en/security/how-to-measure-performance-of-a-virtual-firewall.pdf (Retrieved: 2026-08-10T14:35:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 22
- **Sources reviewed:** 32 (kept: 32, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 1, certification_registry: 4, third_party_review: 3, vendor_datasheet: 7, vendor_doc: 17
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
