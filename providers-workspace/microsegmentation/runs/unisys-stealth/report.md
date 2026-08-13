# Microsegmentation Product Assessment: Unisys - Unisys Stealth

**Product ID:** `unisys-stealth`
**Version reference:** Stealth 6.0 (2020 release) / 5.3 (2022-2025 documentation); staged docs span Stealth 5.0-6.0
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:02:29Z
**Total evidence items collected:** 68
**Total distinct sources:** 31

---

## 1. Overview

Unisys Stealth is an identity-based, encrypted microsegmentation suite that the vendor positions as a zero-trust network overlay spanning data centers, clouds, mobile and IoT [1, 2]. It enforces policy through Communities of Interest (COIs) - identity-driven microsegments - using IKE/IPsec and the Secure Community of Interest Protocol (SCIP) to cryptographically cloak endpoints from unauthorized traffic [1]. The control plane comprises an Enterprise Manager with a RESTful EcoAPI, standalone Authorization Servers, and a Security Dashboard built on the ELK stack [1, 2]. Enforcement is agent-based on Windows 7 SP1+ and common Linux distributions, while Secure Virtual Gateways and Smart Wire appliances extend protection to devices where an agent cannot be installed [1]. Docker and Kubernetes environments are covered via an in-container agent and the Stealth Operator for Kubernetes [4, 5]. Stealth(aware) adds auto-discovery, policy generation and a learning mode for staged deployment [7], and Stealth 6.0 adds AI/ML policy translation, visualization and dashboard tooling [9]. The product holds NIAP Common Criteria validation, an NSA CSfC listing and FIPS 140-2 Level 1 validated crypto modules [12, 24, 25, 26, 27].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 12    | 1                | 11     | 0   |
| partial          | 13    | 0                | 13     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 18 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | Stealth(aware) Auto-Discover automatically determines endpoints and network data flows; the executive brief describes live traffic discovery with rules-based and machine-learning classification. [2], [7] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Network visualization is documented via Stealth(aware) graphical infrastructure views, Stealth 6.0's visual interface and asset clustering into network maps; views at environment or process granularity are not documented. [2], [7], [9] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | - | no evidence found (No retention duration for Stealth log/dashboard history is published in staged sources.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (No CVE/vulnerability overlay on the Stealth network map is documented.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | - | Dashboards surface unauthorized tunnels and risk sources and visualization highlights harmful traffic; a dedicated unrecognized-traffic anomaly classifier is not documented. [1], [2] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Stealth policies (COIs and filters) are identity-based on user credentials or certificates; identity-driven microsegmentation is confirmed by vendor materials and an independent review. [1], [18], [29] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | Stealth 6.0 uses AI/ML to translate thousands of network communication flows into streamlined security policies; Stealth(aware) Auto-Configure generates policies from discovery results. [7], [9] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | Stealth(aware) provides a non-enforcement or learning mode that monitors the environment and shows how segmentation would impact it before enforcement is applied. [7] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | Automatic rollback of unsuccessful endpoint software updates is documented; an explicit one-click policy rollback capability is not documented. [3] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | - | A user/group-to-role-to-COI-to-filter object hierarchy and reusable Stealth(aware) security profiles are documented; explicit inherited-rule semantics are not. [1], [7] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | Agents cover Windows 7 SP1 and later and commonly used Linux distributions, with virtual agents for macOS, iOS, iPadOS and Android; AIX, Solaris and Windows Server 2003 are not documented. [1], [9], [28] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | - | Container and Kubernetes protection is documented (agent installed in Docker containers and a dedicated Stealth Operator for Kubernetes); OpenShift is not documented. [4], [5], [8], [31] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | Endpoint agents enforce policies while Secure Virtual Gateways front-end systems without an available agent, and physical/virtual gateways protect IoT devices where Stealth cannot be installed. [1], [11] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | All control-plane components (Enterprise Manager, standalone Authorization Servers) install on-premises on Windows servers with no documented internet dependency; an explicit air-gapped validation is not stated. [1], [9] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scalability is documented only qualitatively - unlimited standalone Authorization Servers, gateways that scale with performance demand, thousands of endpoints deployed at once; no 50,000+ workload figure is published. [1], [3], [9] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | - | no evidence found (No agent CPU-overhead figure is published in staged sources.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | - | no evidence found (No agent RAM-footprint figure is published in staged sources.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | - | no evidence found (No network-latency impact figure is published in staged sources.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | - | Stealth fails open, using clear-text communication, in the case of an endpoint failure, and existing tunnels remain open during controller outages. [3] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Supported | medium | - | Endpoint software updates deploy via an automatic restart of Stealth services without a server reboot, and the standard Windows install flow completes without a reboot step. [1], [3] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | - | The EcoAPI RESTful interface provides full CRUD operations across the entire Stealth policy object model, and a robust API framework automates installation, configuration and deployment. [1], [2], [9] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Stealth logging integrates with SIEM products such as LogRhythm, Splunk and Azure Sentinel via log forwarding, with a production SIEM integration confirmed in the Flowserve deployment. [1], [10], [18] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found (No ServiceNow/CMDB tag-sync integration is documented.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | - | Unattended automated installation via API and robust scripting is documented; explicit Jenkins/GitLab/Terraform pipeline integrations are not. [1], [2], [9] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | - | no evidence found (Enforcement is identity/network-level (IPsec COIs and filters); no process-level enforcement is documented.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | - | no evidence found (No threat-intelligence feed or honeypot/deception capability is documented.) |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Audit and compliance reporting is documented, but no named-standard report templates (PCI-DSS, ISO 27001, IEC 62443, NIST 800-207) are evidenced. [1], [9] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | Mutual-certificate TLS, AES-256 encryption and FIPS-mode cryptography are documented; TLS 1.3 specifically is not named in the cited sources. [2], [12], [25] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | Redundant standalone Authorization Servers with no count limit, plus active/standby gateway failover, provide controller high availability. [1], [3] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | Endpoints continue enforcing their distributed policies and existing tunnels stay open during Management Server or Authorization Server outages within a one-hour grace period. [1], [3] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Enterprise Manager database backup and restore (BackupEM.ps1) is documented for disaster recovery scenarios; continuous site-to-site sync is not documented. [3] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Supported | high | - | Registry sources confirm Common Criteria EAL4 augmented (2011 security target), NIAP protection-profile certification (2019/2020) and FIPS 140-2 Level 1 validated Unisys cryptographic modules. [12], [24], [25], [26], [27] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | OT/industrial protection is documented (IoT and medical devices, industrial control systems, SCADA, an energy-sector client); no Siemens/Honeywell/ABB compatibility certification is evidenced. [2], [11], [21] |

---

## 4. Notable Strengths

- **Identity-based, IP-independent policy model (items 2.1, 1.1):** Policies are defined on user credentials or certificates and roles rather than IPs or VLANs, with automated flow discovery feeding policy generation [1, 7, 18].
- **Agentless coverage via gateways (item 3.3):** Secure Virtual Gateways, physical/virtual gateways and Smart Wire protect legacy, IoT and purpose-built devices without requiring an agent [1, 11].
- **Operational resilience (items 4.4, 7.1, 7.2):** Stealth fails open on endpoint failure, endpoints keep enforcing policies during controller outages, and redundant Authorization Servers plus gateway failover provide high availability [3].
- **Automation and integration surface (items 5.1, 5.2):** The EcoAPI exposes full CRUD over all policy objects, and logging integrates with Splunk, LogRhythm and Azure Sentinel [1].
- **Credentialed security posture (item 8.1):** Common Criteria EAL4 augmented, NIAP protection-profile certification and FIPS 140-2 Level 1 validated modules are recorded in official registries [24, 25, 26, 27].

## 5. Notable Gaps / Risks

- **Performance figures unpublished (items 4.1, 4.2, 4.3):** No agent CPU, RAM or network-latency figures are published, so the resource-impact and latency requirements cannot be verified; vendor benchmark data would resolve this.
- **Retention and CVE context (items 1.3, 1.4):** No flow-history retention duration or CVE overlay on the network map is documented, leaving forensic-history and vulnerability-context requirements unverified.
- **Container/OpenShift coverage (item 3.2):** Kubernetes and Docker support are documented, but OpenShift is not, so the compound container requirement is only partially met.
- **Process-level control and deception (items 6.1, 6.2):** Enforcement is network/identity-level; no process-level enforcement or threat-intelligence/honeypot-deception integration is documented.
- **CI/CD and CMDB integration (items 5.4, 5.3):** API/script automation exists, but no Jenkins/GitLab/Terraform pipeline or ServiceNow/CMDB tag-sync integrations are documented.

## 6. Evidence Quality Notes

Evidence was gathered from 31 staged sources: 19 vendor documentation items (architecture white paper, Information Center admin guide, Kubernetes operator and Docker guides, executive brief, press releases, one blog), 4 certification-registry documents (2 Common Criteria security targets, 2 NIST CMVP security policies), 3 third-party reviews, 3 vendor-hosted case studies, 1 community review page and 1 third-party news article. All 68 evidence quotes were verified verbatim against the staged artifact text (0 fabricated, 0 unverifiable), and every cited source is persisted in artifacts/ with a sha256 anchor.

Items 8.1 and 2.1 are backed by multiple source types (certification registries and an independent review respectively); 8.1 is the only high-confidence verdict because it rests on independent registries. 18 items rely solely on vendor documentation, with confidence capped at medium by the validator - notably the resilience claims (4.4, 7.1, 7.2), API/SIEM integration (5.1, 5.2) and fail-open behavior (4.4), which would benefit from independent lab or customer validation. No outright contradictions were found between sources; where vendor materials were qualitative (scalability 3.5, compliance reports 6.3, OS coverage 3.1), verdicts were held at partial rather than inferred as supported.

---

## Bibliography

[1] Unisys Corporation. "Unisys Stealth(core) v5 Release Architecture and Feature Overview (white paper, 8232 2009-000)". https://public.support.unisys.com/st3/docs/Stealth-5.3/82322009-000.pdf (Retrieved: 2026-08-10T13:50:24Z)
[2] Unisys Corporation. "Stealth Products and Services - Zero Trust Networks Built on Identity-Based, Encrypted Micro-segmentation (executive brief, 20-0553)". https://www.unisys.com/siteassets/collateral/executive-brief/ex_200553_stealthproductsandservices.pdf (Retrieved: 2026-08-10T13:49:45Z)
[3] Unisys Corporation. "Unisys Stealth Information Center Release 5.3 (8232 3205-005)". https://public.support.unisys.com/st3/docs/Stealth-5.3/82323205-005.pdf (Retrieved: 2026-08-10T13:52:48Z)
[4] Unisys Corporation. "Unisys Stealth Operator for Kubernetes Implementation and Operations Guide (8231 3719-002)". https://public.support.unisys.com/st3/docs/Stealth-5.2/82313719-002.pdf (Retrieved: 2026-08-10T13:58:18Z)
[5] Unisys Corporation. "Guidelines for Using Stealth with Docker Containers (8225 6728-002)". https://public.support.unisys.com/st3/docs/Stealth-5.2/82256728-002.pdf (Retrieved: 2026-08-10T13:58:08Z)
[6] Unisys Corporation. "Unisys Stealth Secure Virtual Gateway Installation and User's Guide Release 5.2 (8225 3899-021)". https://public.support.unisys.com/st3/docs/Stealth-5.2/82253899-021.pdf (Retrieved: 2026-08-10T13:53:15Z)
[7] Unisys Corporation. "New Unisys Stealth(aware) Software Automates Implementation of Advanced Micro-Segmentation Security (news release, Dec 6 2016)". https://www.unisys.com/news-release/new-unisys-stealth-aware-software-automates-implementation-of-advanced-micro-segmentation-security/ (Retrieved: 2026-08-10T13:44:48Z)
[8] Unisys Corporation. "Unisys Unveils Unisys Stealth 5.0 Software Extending Protection to Container and Kubernetes Environments (news release, Feb 24 2020)". https://www.unisys.com/news-release/unisys-unveils-stealth-5-software-protection-container-kubernetes-environments/ (Retrieved: 2026-08-10T13:44:42Z)
[9] Unisys Corporation. "Latest Version of Unisys Stealth Features New Automation and Visualization Tools (news release, Nov 10 2020)". https://www.unisys.com/news-release/latest-version-of-unisys-stealth-features-new-automation-and-visualization-tools-to-accelerate-deployment-and-simplify-management/ (Retrieved: 2026-08-10T13:44:42Z)
[10] Unisys Corporation. "Latest Release of Unisys Stealth Microsegmentation Security Software Introduces Greater Interoperability and Scalability (news release, Nov 7 2017)". https://www.unisys.com/news-release/latest-release-unisys-stealth-security-software-introduces-greater-interoperability/ (Retrieved: 2026-08-10T13:44:50Z)
[11] Unisys Corporation. "Latest Release of Unisys Stealth Security Software Extends Microsegmentation Protection to Include Medical and IoT Devices (news release, Apr 17 2018)". https://www.unisys.com/news-release/latest-release-unisys-stealth-security-extends-protection-to-include-medical-iot-devices/ (Retrieved: 2026-08-10T13:44:50Z)
[12] Unisys Corporation. "Unisys Stealth Achieves Exclusive U.S. Federal Government Certification to Protect National Security Systems (news release, May 27 2020)". https://www.unisys.com/news-release/unisys-stealth-achieves-exclusive-us-govt-certification/ (Retrieved: 2026-08-10T13:44:48Z)
[13] Unisys Corporation. "NIAP Designation Allowing Government Agencies to Use Unisys Stealth Broadened to Include Windows 10 and Windows Server 2016 (news release, Feb 22 2018)". https://www.unisys.com/news-release/niap-designation-allowing-government-agencies-to-use-unisys-stealth-broadened/ (Retrieved: 2026-08-10T13:44:50Z)
[14] Unisys Corporation. "National Security Agency Designation Allows Government Agencies to Use Unisys Stealth (news release, Jul 25 2016)". https://www.unisys.com/news-release/nsa-designation-allows-government-agencies-to-use-unisys-stealth/ (Retrieved: 2026-08-10T13:44:49Z)
[15] Unisys Corporation. "Unisys Stealth Integrates New Microsoft API to Provide Uninterrupted Security for Critical Workloads in Microsoft Azure (news release, Sep 30 2019)". https://www.unisys.com/news-release/unisys-stealth-integrates-new-microsoft-api-to-provide-uninterrupted-security-for-azure/ (Retrieved: 2026-08-10T13:44:54Z)
[16] Unisys Corporation. "Participants Unable to Hack Unisys Stealth Solution During Contest Held at RSA 2020 Conference (news release, Mar 9 2020)". https://www.unisys.com/news-release/participants-unable-to-hack-unisys-stealth-during-rsa-contest/ (Retrieved: 2026-08-10T13:44:55Z)
[17] Unisys Corporation. "Unisys Stealth Defeats Hackers at University of Hawaii Capture the Flag Event (news release, Oct 18 2016)". https://www.unisys.com/news-release/unisys-stealth-defeats-hackers-at-university-of-hawaii/ (Retrieved: 2026-08-10T13:44:56Z)
[18] Unisys Corporation. "Flowserve Expands Use of Unisys Stealth Microsegmentation (news release, Apr 17 2018)". https://www.unisys.com/news-release/flowserve-expands-use-of-unisys-stealth-microsegmentation/ (Retrieved: 2026-08-10T13:44:54Z)
[19] Unisys Corporation. "Yorkshire Building Society Selects Unisys Stealth to Secure Customer Data (news release, 2018)". https://www.unisys.com/news-release/yorkshire-building-society-selects-unisys-stealth-to-secure-customer-data/ (Retrieved: 2026-08-10T13:44:55Z)
[20] Unisys Corporation. "Unisys Announces Integration of Unisys Stealth Security with Industry-Leading Cyber Recovery Software (news release, May 1 2019)". https://www.unisys.com/news-release/unisys-announces-integration-stealth-security-with-leading-cyber-recovery-software/ (Retrieved: 2026-08-10T13:45:00Z)
[21] Unisys Corporation. "Unisys Stealth to Protect Critical Data at PBF Energy Locations Throughout U.S. (news release, Jan 26 2016)". https://www.unisys.com/news-release/unisys-stealth-to-protect-critical-data-at-pbf-energy-locations/ (Retrieved: 2026-08-10T13:45:00Z)
[22] Unisys Corporation. "Unisys Stealth Earns Frost & Sullivan 2015 Award (news release, 2015)". https://www.unisys.com/news-release/unisys-stealth-earns-frost-sullivan-2015-award/ (Retrieved: 2026-08-10T13:45:00Z)
[23] Unisys Corporation. "Navigating the Cyber Battlefield: Exploring the Power of Micro-segmentation (Unisys blog)". https://www.unisys.com/blog-post/cis/navigating-the-cyber-battlefield-exploring-the-power-of-micro-segmentation/ (Retrieved: 2026-08-10T13:45:00Z)
[24] Common Criteria Portal (NIAP-CCEVS archive). "UNISYS Stealth Solution for Networks Security Target v2.7 (2011, Common Criteria portal st_vid10304)". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/st_vid10304-st.pdf (Retrieved: 2026-08-10T13:51:24Z)
[25] Common Criteria Portal (NIAP-CCEVS archive). "Unisys Stealth Solution Release v4.0 Windows and Linux Endpoints Security Target v1.0 (Dec 2019, Common Criteria portal st_vid10989)". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/st_vid10989-st.pdf (Retrieved: 2026-08-10T13:51:35Z)
[26] NIST CMVP (certificate 3959) / Unisys Corporation. "Unisys Linux OpenSSL FIPS Object Module Version 2.0 - FIPS 140-2 Level 1 Non-Proprietary Security Policy". https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp3959.pdf (Retrieved: 2026-08-10T13:51:24Z)
[27] NIST CMVP (certificate 4068) / Unisys Corporation. "Unisys Linux Kernel Cryptographic API Module Version 2.0 - FIPS 140-2 Level 1 Non-Proprietary Security Policy". https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp4068.pdf (Retrieved: 2026-08-10T13:51:26Z)
[28] TechWalls. "Unisys' Stealth network traffic hider is better than encryption (TechWalls review)". https://www.techwalls.com/unisys-stealth-network-traffic-hider-better-encryption/ (Retrieved: 2026-08-10T13:56:38Z)
[29] Top Business Software. "Unisys Stealth Reviews (TopBusinessSoftware)". https://topbusinesssoftware.com/products/Unisys-Stealth/reviews/ (Retrieved: 2026-08-10T13:56:44Z)
[30] PeerSpot (IT Central Station). "Unisys Stealth Reviews (PeerSpot)". https://www.peerspot.com/products/unisys-stealth-reviews (Retrieved: 2026-08-10T13:56:38Z)
[31] Enterprise IT World. "Unisys Extends Protection to Container and Kubernetes Environments (Enterprise IT World)". https://www.enterpriseitworld.com/unisys-extends-protection-to-container-and-kubernetes-environments/ (Retrieved: 2026-08-10T13:58:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 31 (kept: 31, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 3, certification_registry: 4, community: 1, third_party_review: 3, vendor_blog: 1, vendor_doc: 19
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
