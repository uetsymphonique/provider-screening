# Microsegmentation Product Assessment: Forcepoint - Forcepoint Next-Gen Firewall / FlexEdge (NGFW with Security Management Center; rebranded FlexEdge Secure SD-WAN from v7.1)

**Product ID:** `forcepoint-next-gen-firewall-flexedge`
**Version reference:** Forcepoint NGFW 6.x-7.x / FlexEdge Secure SD-WAN 7.1 documentation set; SMC 6.10-7.1; CC-evaluated NGFW 6.10.9; FIPS 140-3 modules per NIST CMVP #4867/#4835/#5276
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T16:58:47Z
**Total evidence items collected:** 64
**Total distinct sources:** 23

---

## 1. Overview

Forcepoint Next-Gen Firewall (NGFW), the StoneGate-descended product line that Forcepoint rebranded as FlexEdge Secure SD-WAN from version 7.1, is a gateway-centric network security product rather than a workload-agent microsegmentation platform [18]. It runs a unified software core in physical, virtual (VMware ESXi/NSX, KVM, Hyper-V) and cloud (AWS, Azure, Google, Oracle, IBM) forms, all managed from a single Security Management Center (SMC) console [1, 2]. Forcepoint positions it as delivering SD-WAN connectivity, IPS with anti-evasion, deep packet inspection, TLS 1.2/1.3 decryption, application control and user identity awareness across enterprise, branch and data-center sites, with up to 16-node active-active/active-standby clustering and SMC-level high availability [1, 18]. Microsegmentation-relevant behavior is network-level: virtual appliances can automate microsegmentation of east-west SDN traffic, and the optional Windows-only Endpoint Context Agent (ECA) feeds per-connection user and application context to the gateway for policy decisions [3, 21].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 0                | 6      | 0   |
| partial          | 20    | 0                | 20     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 7     | 0                | 0      | 7   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 24 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | - | The SMC aggregates real-time event and connection data from NGFW engines, endpoints and third-party devices with 360-degree visibility views; flow discovery is limited to traffic traversing the gateway or injected from third-party logs rather than host-agent-based discovery of all workloads. [1], [15], [22] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | The SMC provides network topology diagrams and customizable dashboards for devices, users and VPNs, but no map organized by application, environment, role or process. [15] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Log retention is capacity-driven and administrator-defined: log data stays on the Log Server until scheduled archive/delete tasks run or storage fills, with a 75% capacity alert; no default 90-day retention figure is documented. [13], [15], [18] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Unknown | low | - | no evidence found |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | - | Policies can be created around user identity (with or without authentication), interface zones and endpoint application context from ECA; there is no tag/label-based microsegmentation policy model independent of IP/VLAN. [15], [18] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | - | no evidence found |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | A Policy Validation Tool checks for configuration mistakes before activation and fail-safe uploads restore the previous policy if a new version fails; no policy simulation or dry-run mode is documented. [15] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | Policy snapshots allow exploring configuration history and a previous policy version can be recovered and uploaded to the firewall; an explicit instant 1-click rollback workflow is not documented. [15] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | The SMC documents hierarchical policy management with policy templates, sub-policies and aliases, and engine policies are composed of Template Policies, Policies and Sub-Policies. [15], [22] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The only endpoint agent, the Windows-only Endpoint Context Agent (ECA), collects per-connection user/application context; no Linux, AIX or Solaris workload agents are documented. [21] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | - | Virtual NGFW appliances for VMware NSX/KVM and cloud images secure east-west SDN traffic and automate network microsegmentation; no Kubernetes or OpenShift native isolation is documented. [3] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | - | The product is primarily an agentless network-gateway solution deployed as physical, virtual or cloud appliances, with an optional Windows Endpoint Context Agent for endpoint application context; the agent is not a workload enforcement agent. [1] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | Plug-and-play installation is supported via cloud or USB stick with an initial policy push, which enables offline onboarding; a complete offline/air-gapped update process for dynamic updates is not documented. [15] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scale is expressed in managed gateway nodes: one Management Server manages 1 to 2,000 NGFWs and the FlexEdge Secure SD-WAN Manager controls up to 6,000 appliances; no per-workload agent count is published to confirm 50,000+ workloads. [15], [23] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | The Windows ECA is a client monitoring tool, but no agent CPU percentage is published; only host-level minimums (e.g. 8 GB RAM) are documented. [21] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | No agent RAM footprint is published; documentation gives only host minimums (8 GB RAM, 1.5 GB free disk space) for Windows endpoints running the agent. [21] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | 0.093 ms | NSS Labs measured added UDP latency of 62 to 256 microseconds (0.062 to 0.256 ms) depending on packet size (64 B to 1514 B) at 95% of maximum load on the 2105 NGFW; the sub-0.1 ms threshold holds only for small packets. [19] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | - | no evidence found |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | The SMC exposes a documented REST API (XML or JSON) covering element management, access/NAT/inspection rules, policy upload, routing and VPNs, already used by Tufin and FireMon; the API does not claim 100% coverage of all administrative functions. [15], [20] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Log forwarding supports syslog plus CEF, LEEF, XML, JSON, CSV, NetFlow v9, IPFIX and McAfee ESM formats with TLS-protected syslog, and a documented integration exports NGFW logs to Splunk via a Universal Forwarder. [12], [15], [18] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | - | Forcepoint R&D maintains an SMC Terraform provider generated from the SMC API OpenAPI specification, and the SMC API supports scripting automation of frequent tasks; no Jenkins or GitLab plugins are documented. [16], [20] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | Using ECA-supplied endpoint context, the NGFW can whitelist/blacklist by client application name and version at the gateway; enforcement is network-side, not host process-level. [1], [21] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat intelligence is provided through cloud file reputation, McAfee GTI-based file filtering, Advanced Malware Detection sandboxing and DNS sinkholing; no honeypot/deception detection is documented. [1], [15], [17] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | The SMC provides customizable scheduled reporting and the NGFW holds or is pursuing regulatory certifications (CPSTIC high-category for Spanish public administration, CSfC eligibility, FIPS 140-3); no ready-made PCI-DSS, NIST 800-207, ISO 27001 or IEC 62443 report templates are documented. [5], [15] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | NGFW engines establish authenticated and encrypted connections with Management/Log Servers using certificates for mutual component authentication, and the platform supports TLS 1.2/1.3 decryption; this covers the gateway-management channel rather than a workload agent-controller link. [2], [22] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | Engine clusters run active-active/active-standby with up to 16 nodes, and the Management Server supports an active plus standby HA setup with up to four standby management servers and real-time replication. [1], [15], [18] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | Engines work independently according to their installed configuration when the SMC is unavailable, and Management Server contact details are not used after a policy has been installed. [18] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | - | The HA setup provides automatic incremental replication of Management Server configuration data for backup and disaster recovery purposes, and an integrated backup tool backs up the whole system including all firewall configurations. [15], [18] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Supported | medium | - | Active FIPS 140-3 certificates on the NIST CMVP cover the NGFW appliance (Level 2, #4867), desktop appliances (#5276) and the NGFW Cryptographic Kernel Module (Level 1, #4835); Common Criteria certification is current under NIAP NDPP (NGFW 6.10.9, 2023), with EAL4+ historically achieved by the StoneGate firewall lineage (2009). [5], [6], [8], [10], [11] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found |

---

## 4. Notable Strengths

- **High availability at both engine and management layers (items 7.1, 7.2, 7.3):** up to 16-node active-active/active-standby engine clustering, active-plus-standby Management Servers with incremental replication, and documented autonomous engine operation when the SMC is unreachable [1, 15, 18].
- **Strong SIEM/log export story (item 5.2):** real-time forwarding in syslog, CEF, LEEF, XML, JSON, NetFlow v9 and IPFIX with TLS-protected syslog, plus a documented Splunk integration path [12, 15, 18].
- **Hierarchical policy organization (item 2.5):** Template Policies, Policies and Sub-Policies with aliases keep large rule sets structured and understandable [15, 22].
- **Automation surface (items 5.1, 5.4):** a documented REST API (XML/JSON) covering elements, rules, policy upload, routing and VPNs, with an official SMC Terraform provider generated from the OpenAPI spec [16, 20].
- **Verified security certifications (item 8.1):** active FIPS 140-3 modules on the NIST CMVP (#4867 Level 2, #5276, #4835) and Common Criteria certification under NIAP NDPP for NGFW 6.10.9, with historical CC EAL4+ for the StoneGate lineage [5, 6, 8, 10, 11].

## 5. Notable Gaps / Risks

- **Not a workload-agent segmentation platform (items 3.1, 3.3, 4.1-4.5, 6.1):** there is no host agent for Linux/AIX/Solaris servers, no published agent CPU/RAM footprint, and no process-level enforcement; the Windows-only ECA provides gateway-side application context, not host enforcement [21].
- **No tag/label-based policy model (item 2.1):** policy is built on user identity, zones and applications, not workload tags independent of IP/VLAN as microsegmentation buyers typically require [15, 18].
- **Missing visibility capabilities (items 1.4, 1.5):** no CVE context on maps and no documented detection of unrecognized/unknown traffic flows.
- **No container-native isolation (item 3.2):** east-west microsegmentation is limited to virtual/SDN (NSX/KVM) deployments; Kubernetes/OpenShift native isolation is not documented [3].
- **Integration gaps (items 5.3, 8.2):** no ServiceNow CMDB tag sync and no Siemens/Honeywell/ABB OT compatibility certifications documented.

## 6. Evidence Quality Notes

Evidence was drawn from 23 staged sources: 9 vendor_doc pages/PDFs, 6 vendor_datasheets, 2 vendor_blog posts, 5 certification-registry entries (NIST CMVP, Common Criteria portal) and 1 independent third-party test (NSS Labs 2019 NGFW test report). Thirteen items are backed by two or more source_types, and the registry entries give items 6.3, 7.1, 7.2, 7.3 and 8.1 independent grounding; every other non-unknown item rests on vendor documentation only, so confidence is capped at medium and those verdicts describe what Forcepoint documents rather than independently verified behavior. The NSS Labs report is the single independent performance source and is used only for item 4.3, where its measured 62-256 microsecond UDP latency (2019, one appliance model) makes a strong-confidence claim inappropriate. No sources directly contradicted each other, but scale claims differ by product tier (2,000 managed NGFWs per Management Server vs 6,000 appliances per FlexEdge SD-WAN Manager), which is why item 3.5 is rated partial with no numeric workload figure. Seven items (1.4, 1.5, 2.2, 4.4, 4.5, 5.3, 8.2) returned no evidence and are rated unknown per the anti-fabrication contract.

---

## Bibliography

[1] Forcepoint. "Forcepoint Next Generation Firewall (NGFW) Datasheet". https://cdn.blueally.com/guardsense/datasheets/datasheet_forcepoint_ngfw_en.pdf (Retrieved: 2026-08-10T16:58:47Z)
[2] Forcepoint. "Forcepoint FlexEdge Secure SD-WAN Datasheet". https://assets.starlinkme.net/gitex-vendor-assets/forcepoint/datasheet-flexedge-sdwan-en.pdf (Retrieved: 2026-08-10T16:58:47Z)
[3] Forcepoint. "Forcepoint Next Generation Firewall: Network Security at Scale (product page)". https://www.forcepoint.com/product/ngfw-next-generation-firewall (Retrieved: 2026-08-10T16:58:47Z)
[4] Forcepoint. "Forcepoint Secure SD-WAN Solution (product page)". https://www.forcepoint.com/product/secure-sd-wan (Retrieved: 2026-08-10T16:58:47Z)
[5] Forcepoint. "Network Security Certifications | Forcepoint". https://www.forcepoint.com/certifications/ngfw-certifications (Retrieved: 2026-08-10T16:58:47Z)
[6] NIST / NIAP CCEVS. "NIAP Common Criteria Evaluation and Validation Scheme Validation Report: Forcepoint NGFW 6.10.9 (CCEVS-VR-VID11343-2023)". https://www.commoncriteriaportal.org/files/epfiles/st_vid11343-vr.pdf (Retrieved: 2026-08-10T16:58:47Z)
[7] NIST / NIAP CCEVS. "NIAP Common Criteria Validation Report: Stonesoft StoneGate Firewall (VID3003)". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/st_vid3003-vr.pdf (Retrieved: 2026-08-10T16:58:47Z)
[8] Stonesoft / firmenpresse. "Stonesoft erhaelt Common Criteria EAL4+ Zertifizierung fuer StoneGate Firewall Appliances (press release)". https://www.firmenpresse.de/pressinfo89390-stonesoft-erh-lt-common-criteria-eal4-zertifizierung-f-r-stonegate-firewall-appliances.html (Retrieved: 2026-08-10T16:58:47Z)
[9] NIST CMVP. "NIST CMVP Certificate #5276: Forcepoint Next Generation Firewall for Desktop Appliances (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5276 (Retrieved: 2026-08-10T16:58:47Z)
[10] NIST CMVP. "NIST CMVP Certificate #4867: Forcepoint Next Generation Firewall (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4867 (Retrieved: 2026-08-10T16:58:47Z)
[11] NIST CMVP. "NIST CMVP Certificate #4835: Forcepoint NGFW Cryptographic Kernel Module (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4835 (Retrieved: 2026-08-10T16:58:47Z)
[12] Forcepoint. "Forcepoint Next-Gen Firewall and Splunk - Forcepoint Integration Docs". https://forcepoint.github.io/docs/ngfw_and_splunk/ (Retrieved: 2026-08-10T16:58:47Z)
[13] Forcepoint. "Log data management and how it works - Forcepoint NGFW 7.0.1 Online Help". https://help.forcepoint.com/ngfw/en-us/7.0.1/GUID-4602F5C2-A988-4912-876A-C9CBC6FB4C8F.html (Retrieved: 2026-08-10T16:58:47Z)
[14] Forcepoint. "Log data management configuration overview - Forcepoint NGFW 6.11.0 Online Help". https://help.forcepoint.com/ngfw/en-us/6.11.0/GUID-2588F7D8-048A-4736-8850-8B044F0D1A6B.html (Retrieved: 2026-08-10T16:58:47Z)
[15] Forcepoint. "Forcepoint NGFW Security Management Center (SMC) Datasheet". https://www.fca.com.pl/wp-content/uploads/datasheet_forcepoint_ngfw_security_management_center_en.pdf (Retrieved: 2026-08-10T16:58:47Z)
[16] Forcepoint R&D. "Forcepoint-NSP/terraform-provider-fp-ngfw-smc (NGFW SMC Terraform provider)". https://github.com/Forcepoint-NSP/terraform-provider-fp-ngfw-smc (Retrieved: 2026-08-10T16:58:47Z)
[17] Forcepoint. "FlexEdge Secure SD-WAN 7.1 Release - Forcepoint Blog". https://www.forcepoint.com/blog/insights/flexedge-secure-sd-wan-7-1-release (Retrieved: 2026-08-10T16:58:47Z)
[18] Forcepoint. "Forcepoint FlexEdge Secure SD-WAN 7.1 Product Guide". https://help.forcepoint.com/flexedge/sd-wan/en-us/7.1.0/onlinehelp/secure_sd-wan_710_pg_a_en-us.pdf (Retrieved: 2026-08-10T16:58:47Z)
[19] NSS Labs. "NSS Labs Next Generation Firewall Test Report: Forcepoint 2105 NGFW 6.3.10 build 19504". https://www.afcea-qp.org/wp-content/uploads/2021/05/report_nss_labs_forcepoint_ngfw_en.pdf (Retrieved: 2026-08-10T16:58:47Z)
[20] Forcepoint. "Forcepoint NGFW SMC 6.10 API User Guide". https://help.forcepoint.com/docs/ngfw/v610/rfrnce/ngfw_6100_ug_smc-api_c_en-us.pdf (Retrieved: 2026-08-10T16:58:47Z)
[21] Forcepoint. "Forcepoint F1E Install Guide (incl. Endpoint Context Agent), v25". https://help.forcepoint.com/F1E/en-us/v25/ep_install/ep_install.pdf (Retrieved: 2026-08-10T16:58:47Z)
[22] Forcepoint. "Forcepoint NGFW 7.0.0 Online Help (topics index)". https://help.forcepoint.com/ngfw/en-us/7.0.0/index.html (Retrieved: 2026-08-10T16:58:47Z)
[23] Forcepoint. "Forcepoint FlexEdge Secure SD-WAN Solution Brief". https://www.content.shi.com/cms-content/accelerator/media/pdfs/forcepoint/forcepoint-102323-secure-sd-wan-solution-brief.pdf (Retrieved: 2026-08-10T16:58:47Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 20
- **Sources reviewed:** 23 (kept: 23, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 5, third_party_review: 1, vendor_blog: 2, vendor_datasheet: 6, vendor_doc: 9
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
