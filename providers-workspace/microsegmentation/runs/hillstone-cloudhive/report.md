# Microsegmentation Product Assessment: Hillstone Networks - Hillstone CloudHive (山石云·格)

**Product ID:** `hillstone-cloudhive`
**Version reference:** CloudHive v2.9.4 (datasheet EX-08.01-CloudHive-V2.9.4-0124-EN-01); v2.9 GA per Nov 2022 release note
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T13:58:20Z
**Total evidence items collected:** 75
**Total distinct sources:** 20

---

## 1. Overview

Hillstone CloudHive (山石云·格) is a network-side, agentless micro-segmentation and cloud workload protection platform for private-cloud VM environments, positioned by Hillstone against east-west lateral movement in data centers [1][5]. Enforcement is delivered by per-host Virtual Security Service Modules (vSSM) that inspect VM traffic at L2-L7, orchestrated by vSOM (lifecycle) and vSCM (policy control) modules with optional vDSM syslog forwarding [1]. It deploys in transparent Layer 2 (Layer 3 on VMware vSphere) without changing network topology, supports VMware vSphere 5.5-8.0, FusionCompute, FusionOne HCI and OpenStack OVS, and holds VMware Ready status with NSX integration for traffic redirection [1][13][16]. Policies follow VMs across vMotion [1][2]. Hillstone was cited in the 2020 Gartner Market Guide for CWPP under identity-based segmentation capabilities [8]; published deployments cover a UK MSP (K3), a large Asian airport, Peking University and a provincial government [2][3][9][10]. The vendor's container/host agent coverage sits in the separate CloudArmour CNAPP product [19][20].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 0                | 5      | 0   |
| partial          | 15    | 1                | 13     | 1   |
| not_supported    | 1     | 0                | 0      | 1   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 3     | 0                | 3      | 0   |

**Evidence quality:** 20 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** CloudHive has no in-guest agent: enforcement runs in the per-host vSSM virtual appliance (2 vCPU/6 GB for the standard module) and a user review confirms no software is installed on each VM, so per-workload agent CPU overhead does not apply.
- **4.2:** There is no in-guest agent; memory consumption is that of the per-host vSSM appliance (6 GB for the standard module), not a workload agent, so an agent RAM footprint threshold is not applicable.
- **4.5:** There is no in-guest agent to install or update; module upgrades are in-service (ISSU) and vSSM scales up without interrupting the security service, so a workload reboot requirement does not apply.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | Datasheet and white paper document automatic discovery of virtual assets (networks and VMs) with a visual map of cloud resources; the vendor's Chinese product page describes real-time collection and analysis of inter-VM traffic flows. [1], [2], [4], [18] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Topology maps visualize VMs, traffic, applications, threats and multi-dimensional groupings (business group, time, application, flow relationship); no process- or role-level grouping dimension is documented. [1], [4], [18] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Session, threat and system logs are generated and can be forwarded to external syslog servers via vDSM, but no retention-period figure (e.g. 90 days) is documented. [1], [4] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Datasheet documents monitoring and visualization of new traffic and applications over a period to surface changes in the virtual network; a government case study reports CloudHive detected over 80,000 previously unseen threat events. [1], [10] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Access control is defined against VMs/port groups, AD accounts and custom asset groups (business group, business type, org structure, job function) rather than raw IP/VLAN, per datasheet and the vendor's Chinese product page. [1], [18] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | - | A learning-based policy assistant groups traffic by service protocol/VM/business group and converges similar policies, with pre-learning for policy optimization; the feature is not described as AI/ML and a 2024 user review notes AI-based automation is absent. [3], [11], [17] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | - | no evidence found |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | Policy and configuration files can be imported/exported and global configuration is backed up regularly via FTP/SMTP, enabling policy restore; a dedicated one-click rollback is not documented. [1], [12] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | CloudHive deploys without root authority or in-guest plugins and a user review confirms no software is installed on each VM, so guest OS is not a constraint; no explicit compatibility list covering the named OSes (e.g. Windows Server 2003-2022, RHEL, AIX, Solaris) is published. [1], [17] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Not Supported | low | - | CloudHive documentation covers only VM platforms (VMware vSphere, FusionCompute, FusionOne HCI, OpenStack OVS); the vendor's data-center micro-segmentation solution assigns container/Kubernetes coverage to the separate CloudArmour CNAPP product. [1], [19], [20] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | CloudHive is agentless network-side enforcement (vSSM per host, NSX traffic redirection, no in-guest software); the vendor's agent-based workload option is the separate CloudArmour product, so CloudHive alone offers only the agentless path. [1], [16], [20] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | - | no evidence found |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scalability is documented as up to 200 vSSM modules and 1 Tbps (a case study describes >1,000 CPUs), but no workload-count figure is published, so the ≥50,000 workload threshold cannot be confirmed. [1], [3] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | - | CloudHive has no in-guest agent: enforcement runs in the per-host vSSM virtual appliance (2 vCPU/6 GB for the standard module) and a user review confirms no software is installed on each VM, so per-workload agent CPU overhead does not apply. [1], [17] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | - | There is no in-guest agent; memory consumption is that of the per-host vSSM appliance (6 GB for the standard module), not a workload agent, so an agent RAM footprint threshold is not applicable. [1], [17] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Vendor materials state Layer 2 deployment does not impact network topology and enforcement avoids traffic detours that typically add latency, but no measured latency figure (e.g. <0.1 ms) is provided. [1], [2], [4] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | - | The datasheet states a single vSSM 'VM down' does not affect the system and user VM traffic bypasses the vSSM, and vSOM shutdown does not affect the service, i.e. module failure is fail-open so communication continues. [1] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | - | There is no in-guest agent to install or update; module upgrades are in-service (ISSU) and vSSM scales up without interrupting the security service, so a workload reboot requirement does not apply. [1], [17] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | RESTful API, CLI and WebUI are documented management interfaces and the REST API is exposed for partner automation; complete API coverage of 100% of admin functions is not verifiable from documentation. [1], [4] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | - | Logs are forwarded to external syslog servers through vDSM with support for massive, high-speed forwarding; no named SIEM/SOAR integrations (Splunk, QRadar, Sentinel) or CEF format are documented. [1], [4] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | - | no evidence found |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat-intelligence-driven capabilities are documented (IPS signature/encyclopedia updates, botnet C&C feed blocking, cloud sandbox analysis); no honeypot or deception detection is documented. [1] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Reporting and logs are described as supporting compliance and security audit requirements in general terms, and a case study notes ISO-certified data-center operations; no named framework templates (PCI-DSS, NIST 800-207, ISO 27001, IEC 62443) are documented. [2], [4] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Unknown | low | - | no evidence found |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | vSOM and vSCM support active/passive paired HA per the datasheet and v2.7.2 release notes; Broadcom's VMware interoperability article confirms a primary/secondary vSCM topology per vSOM. [1], [12], [16] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | low | - | Management, control and service planes are separated, vSOM shutdown does not affect the service and vSCM can automatically restart security service after failure; an explicit statement that vSSM keeps enforcing policies during total control-plane loss is not documented. [1], [4] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Global configuration is backed up on a schedule and delivered via FTP/SMTP, and configuration files can be imported/exported; no multi-site disaster-recovery synchronization is documented. [1], [11], [12] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | high | - | Common Criteria EAL4 is held by Hillstone's SG-6000 A-Series NGFW (StoneOS 5.5R9, NL scheme, 2022) rather than CloudHive specifically, and NIST CMVP lists no FIPS 140-2/140-3 validation for Hillstone. [14], [15] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found |

---

## 4. Notable Strengths

- **Agentless network-side enforcement (items 3.3, 4.1, 4.2, 4.5):** CloudHive installs no in-guest software (vSSM per host, no root authority or plugins), so per-workload agent footprint and reboot concerns do not apply; module upgrades are in-service (ISSU) [1][17].
- **Real-time east-west visibility and auto-discovery (items 1.1, 1.5):** automatic asset discovery and VM/IP address-book updates surface new traffic and application changes, with a government case study reporting over 80,000 previously undetected threat events [1][4][10].
- **Identity/asset-group policy model (item 2.1):** access control attaches to VMs, port groups, AD accounts and custom asset groups (business group, org structure, job function) rather than raw IP/VLAN [1][18].
- **High availability and policy mobility (items 7.1, 4.4):** vSOM and vSCM deploy in active/passive pairs, vSSM failure is fail-open with user VM traffic bypassing the module, and policies/sessions follow VMs across vMotion [1][12][16].
- **Scale headroom (item 3.5):** the architecture documents up to 200 vSSM modules with up to 1 Tbps aggregate throughput, and a case study describes an airport deployment exceeding 1,000 CPUs [1][3].

## 5. Notable Gaps / Risks

- **No container/Kubernetes isolation in CloudHive (item 3.2):** vendor documentation covers only VM platforms, and the data-center micro-segmentation solution routes host/container workloads to the separate CloudArmour product; buyers with K8s workloads need the sibling product, not CloudHive [19][20].
- **Numeric claims are qualitative (items 1.3, 3.5, 4.3):** no flow-retention period, workload-count scale figure, or measured latency is published; only log/syslog forwarding, 200 vSSM/1 Tbps capacity, and 'no traffic detours' language, so the 90-day, 50,000-workload and <0.1 ms thresholds cannot be confirmed [1][4].
- **Certification gap (item 8.1):** Common Criteria EAL4 covers Hillstone's SG-6000 A-Series NGFW (StoneOS 5.5R9), not CloudHive, and NIST CMVP lists no FIPS validation for Hillstone at all [14][15].
- **Weak automation/ops story (items 2.3, 2.4, 2.5, 5.1, 5.2):** no policy simulation, one-click rollback (only backup/import-export) or hierarchical rules are documented, and SIEM integration is generic syslog with no named Splunk/QRadar/Sentinel connectors [1][4][12].
- **Unresolved security-architecture items (items 6.1, 6.4, 3.4, 8.2):** no evidence for process-level enforcement, TLS 1.3/mutual auth on the control path, air-gapped operation, or industrial (Siemens/Honeywell/ABB) compatibility certifications; a 2024 user review also notes AI-based automation is absent (item 2.2) [17].

## 6. Evidence Quality Notes

Evidence spans 20 staged sources and 75 evidence quotes, all grounded verbatim in fetched artifacts (0 fabricated, 0 unverifiable on the grounding check). Only one item (8.1) reaches high confidence, backed by two certification registries (NIST CMVP and the Common Criteria portal); every other verdict is capped at medium or low because the evidence base is dominated by vendor documentation, datasheets, blogs and vendor-hosted case studies. The two genuinely independent non-vendor sources - Broadcom's VMware interoperability KB article [16] and a single PeerSpot user review [17] - corroborate the agentless architecture, HA topology and scale story but are too thin to lift confidence on their own. 20 of 33 items draw on two or more source types; 11 items rest on vendor material only.

Contradictions were resolved conservatively. For 2.2, the vendor's 'policy assistant' (traffic grouping, policy convergence, duplication detection) is presented as rule learning rather than AI/ML, and a Nov 2024 PeerSpot review explicitly says AI features are missing, so the verdict is partial rather than supported [11][17]. For 8.1, the Common Criteria EAL4 certificate belongs to the SG-6000 A-Series NGFW (StoneOS 5.5R9), not the CloudHive virtual product, and the CMVP search returns no Hillstone certificates, so partial is the honest ceiling [14][15]. For the numeric-threshold items (1.3, 3.5, 4.1, 4.2, 4.3), vendor materials provide no figures in the required units; 4.1/4.2 are rated not_applicable because no agent exists, while the others stay partial with null numeric_value. Items with no evidence at all (1.4, 2.3, 2.5, 3.4, 5.3, 5.4, 6.1, 6.4, 8.2) are unknown, never inferred as not_supported.

---

## Bibliography

[1] Hillstone Networks. "Hillstone CloudHive Micro-segmentation Solution for the Cloud (Datasheet v2.9.4)". https://www.hillstonenet.com/wp-content/uploads/Hillstone_CloudHive_2.9.4_EN.pdf (Retrieved: 2026-08-10T13:58:20Z)
[2] Hillstone Networks. "K3 MSP Cloud Services Achieves Secure Segmentation Across Network Environments with Hillstone CloudHive (case study)". https://www.hillstonenet.com/wp-content/uploads/K3-MSP-Cloud-Services-Achieves-Secure-Segmentation-Across-Network-Environments-with-Hillstone-CloudHive.pdf (Retrieved: 2026-08-10T13:58:20Z)
[3] Hillstone Networks. "From Edge to Cloud, Hillstone Solutions Secure the World's Largest, Single-Terminal Airport (case study)". https://www.hillstonenet.com/wp-content/uploads/From-Edge-to-Cloud-Hillstone-Solutions-Secure-the-Worlds-Largest-Single-Terminal-Airport.pdf (Retrieved: 2026-08-10T13:58:20Z)
[4] Hillstone Networks. "Hillstone Solution for Micro-segmentation: Securing Cloud Data Centers with Unprecedented Visibility (white paper)". https://www.hillstonenet.com/wp-content/uploads/Securing-Cloud-Data-Centers-with-Unprecedented-Visibility-2023.pdf (Retrieved: 2026-08-10T13:58:20Z)
[5] Hillstone Networks. "Hillstone CloudHive Solution - Product Page". https://www.hillstonenet.com/products/cloud-protection/cloud-security-cloudhive/ (Retrieved: 2026-08-10T13:58:20Z)
[6] Hillstone Networks. "Micro-Segmentation for Cloud Data Centers - Solution Page". https://www.hillstonenet.com/solutions/micro-segmentation/ (Retrieved: 2026-08-10T13:58:20Z)
[7] Hillstone Networks. "CloudHive and VMware NSX - Advanced Threat Prevention for the Software-Defined Data Center". https://www.hillstonenet.com/more/resources/cloudhive-and-vmware-nsx-advanced-threat-prevention-for-the-software-defined-data-center/ (Retrieved: 2026-08-10T13:58:20Z)
[8] Hillstone Networks. "Hillstone Networks Recognized in Gartner Market Guide for Cloud Workload Protection Platforms for its CloudHive Solution (press release)". https://www.hillstonenet.com/more/company/press-releases/hillstone-networks-recognized-in-gartner-market-guide-for-cloud-workload-protection-platforms-for-its-cloudhive-solution/ (Retrieved: 2026-08-10T13:58:20Z)
[9] Hillstone Networks. "Peking University Launches Cloud-based Campus Secured by Hillstone Networks CloudHive Solution (case study)". https://www.hillstonenet.com/wp-content/uploads/Peking-University-Launches-Cloud-based-Campus-Secured-by-Hillstone-Networks-CloudHive-Solution.pdf (Retrieved: 2026-08-10T13:58:20Z)
[10] Hillstone Networks. "Hillstone CloudHive Secures Private Cloud for a Large Provincial Government (case study)". https://www.hillstonenet.com/wp-content/uploads/Hillstone-CloudHive-Secures-Private-Cloud-for-a-Large-Provincial-Government.pdf (Retrieved: 2026-08-10T13:58:20Z)
[11] Hillstone Networks. "Secure Challenging Cloud Migrations with Hillstone CloudHive V2.9 (blog)". https://www.hillstonenet.com/blog/secure-challenging-cloud-migrations-with-hillstone-cloudhive-v2-9/ (Retrieved: 2026-08-10T13:58:20Z)
[12] Hillstone Networks. "Hillstone CloudHive Simplifies the Management of Cloud Security (blog, v2.7.2)". https://www.hillstonenet.com/blog/hillstone-cloudhive-simplifies-the-management-of-cloud-security/ (Retrieved: 2026-08-10T13:58:20Z)
[13] Hillstone Networks. "Hillstone Networks CloudHive Achieves VMware Ready Status". https://www.hillstonenet.com/blog/hs_awards/hillstone-networks-cloudhive-achieves-vmware-ready-status/ (Retrieved: 2026-08-10T13:58:20Z)
[14] NIST. "NIST CMVP Validated Modules Search - vendor=Hillstone (no certificates)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?searchType=basic&vendor=Hillstone (Retrieved: 2026-08-10T13:58:20Z)
[15] Common Criteria Portal. "Common Criteria Certified Products - vendor search: Hillstone". https://www.commoncriteriaportal.org/products/index.cfm?search=Hillstone (Retrieved: 2026-08-10T13:58:20Z)
[16] Broadcom (VMware Knowledge Base). "Hillstone CloudHive v2.5, NSX 6.3, 6.4 (vSphere 6.5, 6.0 and 5.5) and NSX 6.2.4 - VMware interoperability knowledge base". https://knowledge.broadcom.com/external/article/319643/hillstone-cloudhive-v25-nsx-63-64-vspher.html (Retrieved: 2026-08-10T13:58:20Z)
[17] PeerSpot. "Hillstone CloudHive Reviews 2026 (PeerSpot)". https://www.peerspot.com/products/hillstone-cloudhive-reviews (Retrieved: 2026-08-10T13:58:20Z)
[18] Hillstone Networks (China). "山石云·格 - 云内东西向微隔离可视化平台（CloudHive Chinese product page）". https://www.hillstonenet.com.cn/product_service/cloud-security/cloudhive/ (Retrieved: 2026-08-10T13:58:20Z)
[19] Hillstone Networks (China). "数据中心微隔离解决方案（Data Center Micro-segmentation Solution, Chinese）". https://www.hillstonenet.com.cn/industry-solutions/2025/01/17/sjzxwgl/ (Retrieved: 2026-08-10T13:58:20Z)
[20] Hillstone Networks. "Hillstone CloudArmour CNAPP Solution - Product Page". https://www.hillstonenet.com/products/cloud-protection/hillstone-cloudarmour/ (Retrieved: 2026-08-10T13:58:20Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 20 (kept: 20, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 4, certification_registry: 2, community: 1, third_party_review: 1, vendor_blog: 4, vendor_datasheet: 1, vendor_doc: 7
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
