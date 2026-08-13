# Microsegmentation Product Assessment: Nozomi Networks - Nozomi Guardian / Vantage

**Product ID:** `nozomi-guardian-vantage`
**Version reference:** N2OS 26.4.0 (Guardian/CMC sensors), Arc 2.9.0, Vantage SaaS (documentation dated 2026-08-07)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T16:59:00Z
**Total evidence items collected:** 82
**Total distinct sources:** 28

---

## 1. Overview

Nozomi Networks positions Guardian/Vantage as an OT, IoT and ICS visibility and threat-detection platform rather than a microsegmentation enforcement product. Guardian is a passive network sensor that observes mirrored traffic to discover assets, assess vulnerabilities and detect anomalies [1][3]; it is explicitly passive-only and air-gap capable [1]. Vantage is the SaaS management layer that centralizes sensors and adds AI-driven analytics [2][4]. The optional Arc host sensor adds endpoint visibility and file-level threat prevention [5][6]. Deployment shapes include hardware appliances, VMs, embedded devices and containers, managed by either the on-prem Central Management Console or Vantage [1][11]. Because the platform does not enforce segmentation policies (blocking is deferred to firewalls, NAC or manual action [28]), the policy-management checklist items are largely not supported; strengths sit in visibility, scale, SIEM/CMDB integration and OT-specific threat intelligence [7][22][23]. PeerSpot users rate the platform 4.3 out of 5 with 100% willingness to recommend [28].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 12    | 2                | 10     | 0   |
| partial          | 12    | 0                | 12     | 0   |
| not_supported    | 7     | 0                | 7      | 0   |
| unknown          | 1     | 0                | 0      | 1   |
| not_applicable   | 1     | 0                | 1      | 0   |

**Evidence quality:** 23 items backed by ≥ 2 source_types; 15 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.3:** The platform is an out-of-band passive monitor on mirrored ports/taps with no in-path enforcement, so it introduces no network policy latency; the metric is not applicable to this architecture.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | Guardian passively observes and analyzes local network traffic and continuously monitors to discover newly connected assets; PeerSpot users confirm fast asset discovery on deployment. [1], [3], [28] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | A network topology graph shows devices, communications flows, protocols and traffic patterns, with node details including asset roles and data flows; an explicit App/Process-dimensioned map is not documented. [1], [4], [28] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Guardian retention is configurable per data category (count, space or age-in-days, with 'Never' meaning indefinite) and Vantage applies a configurable retention window; no fixed published default of 90+ days was found, so the numeric threshold could not be verified. [11], [18], [19] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | - | NVD-based vulnerability assessment with dashboards, drill-downs and reports is documented, and Vantage correlates known vulnerabilities to CVE reports; direct rendering of vulnerability context on the topology map is not explicitly documented. [3], [4] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Guardian builds a behavior baseline and flags deviations such as anomalous traffic, suspicious communications and unwanted operations. [1], [3] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Not Supported | medium | - | A PeerSpot reviewer states the product is a detection/visibility tool that does not actively block traffic by design and suggests firewalls, NAC or manual action instead; Nozomi documents the Guardian sensor as passive-only monitoring. [1], [28] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Not Supported | medium | - | No segmentation policy recommendation engine is documented; the platform's AI features target threat detection, alert correlation and query generation rather than policy rule recommendations. [1], [2], [28] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Not Supported | medium | - | No policy simulation or dry-run capability is documented; the platform is documented and reviewed as passive monitoring-only with no segmentation policy lifecycle. [1], [28] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Not Supported | medium | - | No instant rollback mechanism for segmentation policies is documented because the passive architecture has no segmentation policy store to roll back. [1], [28] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Not Supported | medium | - | No inherited or hierarchical segmentation policy rules are documented; the CMC hierarchy is operational sensor management, and the platform performs no policy enforcement. [25], [28] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | medium | - | Network sensors are agentless and OS-agnostic, while the Arc host sensor runs on Windows, Linux and macOS; AIX/Solaris hosts remain observable via passive network monitoring. [5], [28] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Not Supported | medium | - | No container/Kubernetes/OpenShift native isolation is documented; the platform is passive monitoring-only, and container deployment refers to running the Guardian sensor itself as a container. [1], [28] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | - | The platform combines agentless network sensors (Guardian, Guardian Air, Remote Collectors) with host-based Arc sensors, including Arc Embedded in OEM controllers, so both agent-based and agentless deployment models are supported. [1], [5], [27], [28] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | - | Guardian and CMC are documented for fully on-prem and air-gapped deployments, and Arc supports incorporating air-gapped devices into analysis; Vantage itself is a SaaS service requiring connectivity. [1], [5], [11] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 1000000 workloads | Vantage reports a customer monitoring 1 million assets, PeerSpot reviewers describe scaling to hundreds and thousands of assets, and Vantage documentation states an unlimited device count. [2], [4], [28] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | Arc is described as a lightweight, low-impact endpoint sensor, but no CPU-percentage overhead figure is published; consumption is said to vary with enabled options and traffic load. [6], [20] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Supported | medium | 80 MB | The Arc administrator guide states a baseline installation requires up to 80 MB of free RAM, below the 100 MB threshold. [20] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | - | The platform is an out-of-band passive monitor on mirrored ports/taps with no in-path enforcement, so it introduces no network policy latency; the metric is not applicable to this architecture. [1], [28] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | - | Sensors are passive and out-of-band and a reviewer confirms the product does not block traffic by design; Arc operates primarily in user space, so sensor or agent failure cannot interrupt network communication. [1], [6], [28] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | - | Arc deployment notes state the host must be rebooted after installing the USBPcap dependency, so a reboot-free install is not guaranteed for all configurations. [20] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | An OpenAPI-based query/REST API with node-update endpoints is documented in the Universal SDK, but coverage of 100% of administrative functions is not claimed. [21] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | SIEM integration is documented via the Splunk Universal Add-on and the QRadar Universal Application (HTTP OpenAPI), and PeerSpot users report easy integration with SIEM tools and Microsoft Sentinel. [22], [23], [28] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | Vantage imports CMDB asset and software data from ServiceNow via REST API, and the Service Graph Connector is available on the ServiceNow Store. [9], [13] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No Jenkins/GitLab/Terraform CI/CD integration is documented in the vendor's integration catalog or technical documentation.) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | - | No process-level network enforcement is documented; the platform is passive monitoring-only and Arc prevention is limited to file-level quarantine/delete actions. [6], [28] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat intelligence (YARA/Sigma/packet rules, STIX/TAXII feed, Mandiant expansion, AI detection) is integrated into sensors and Vantage; honeypot/deception detection is not documented. [7] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | IEC 62443 content packs and ISO 27001:2022/SOC 2 assurance are documented, and a user confirms IEC 62443 compliance reports; PCI-DSS and NIST 800-207-specific report packs were not found. [8], [10], [26], [28] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | - | Arc communicates with the upstream controller using TLS 1.2/1.3 with certificate validation, and internal Vantage traffic is secured with TLS 1.3; mutual TLS is not explicitly documented. [10], [16], [20] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | - | Vantage runs across multiple AWS availability zones with stateless Kubernetes clusters and resilient multi-data-center databases; no active-active/active-passive clustering is documented for on-prem Guardian/CMC controllers. [14] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | Arc keeps collecting and storing data locally when the Vantage/Guardian link is unavailable and enforces local file-level prevention; the platform has no controller-distributed network policies whose execution could be preserved. [5], [20] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | - | Vantage replicates customer data across regions with RTO 12h/RPO 4h and bi-annual DR testing, and Guardian/CMC support scheduled full backups and restore from the web UI. [14], [15], [24] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | N2OS documents a FIPS-140-2-compliant mode enabled via license with TLS 1.2/1.3 ciphers; no Common Criteria EAL4+ certification or CMVP-validated product entry was found. [17] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | Siemens integration is documented (Guardian Remote Collector embedded in Siemens Scalance LPE and Ruggedcom APE platforms) and Arc Embedded ships with Schneider Electric RTUs; no Honeywell or ABB compatibility certification was found. [12], [27] |

---

## 4. Notable Strengths

- **Real-time asset discovery and network visualization (items 1.1, 1.2):** passive traffic analysis auto-discovers assets and maps devices, flows and protocols on a topology graph, confirmed by PeerSpot practitioners [1][3][28].
- **Agentless plus agent-based coverage (item 3.3):** network sensors (Guardian, Guardian Air, Remote Collectors) are complemented by host-based Arc sensors, including Arc Embedded inside OEM controllers [1][5][27].
- **Scalability (item 3.5):** Vantage reports a customer monitoring 1 million assets and is designed for an unlimited device count [2][4].
- **SIEM/CMDB integration (items 5.2, 5.3):** Splunk Universal Add-on, QRadar Universal Application and ServiceNow CMDB import are documented [22][23][9].
- **OT threat intelligence and encrypted sensor links (items 6.2, 6.4):** STIX/TAXII, YARA and Sigma feeds are distributed to sensors, and Arc communicates upstream over TLS 1.2/1.3 [7][20].

## 5. Notable Gaps / Risks

- **No microsegmentation policy engine (items 2.1-2.5, 6.1):** the platform is passive monitoring-only with no tag-based policy creation, simulation, rollback, hierarchy or process-level enforcement; segmentation must be delivered by firewalls/NAC that Nozomi can suggest actions to [1][28].
- **Agent CPU overhead unquantified (item 4.1):** no CPU-percentage figure is published; only the RAM baseline (80 MB, item 4.2) is documented, and deployment can require a host reboot for some dependencies (item 4.5) [20].
- **Air-gap is limited to on-prem components (item 3.4):** Vantage is SaaS and requires connectivity, so fully isolated sites rely on Guardian/CMC only [1][11].
- **Compliance reporting is partial (item 6.3):** IEC 62443 content packs and ISO 27001/SOC 2 assurance are covered, but PCI-DSS and NIST 800-207-specific report packs were not found [8][10][28].
- **Certification gaps (items 8.1, 8.2):** FIPS-140-2 mode is documented but no Common Criteria EAL4+ or CMVP entry was found, and no Honeywell/ABB compatibility certification is evidenced [17][12].

## 6. Evidence Quality Notes

Evidence came from 28 staged sources: 15 vendor_doc (technical guides and white papers), 8 vendor_datasheet, 3 vendor_blog (press releases/resource pages), 1 analyst_report (ARC Advisory Group) and 1 community (PeerSpot, 26 user reviews). 23 of 33 items were backed by at least two source types; items such as 6.2 (threat intelligence), 7.1 (HA) and 8.1 (FIPS) rely on vendor documentation only, which caps their confidence at medium. The independent PeerSpot reviews were decisive for the policy-management verdicts: a practitioner explicitly states the product does not actively block traffic by design [28], which, together with Nozomi's own passive-only positioning [1], justifies not_supported for items 2.1-2.5 rather than unknown.

No direct contradictions between sources were found; where emphasis differed (e.g., scale claims for item 3.5), the verdict used the vendor-published figure with community corroboration. Numeric-threshold items 1.3 (retention), 4.1 (CPU) and 4.2 (RAM) could only be partially quantified because the vendor publishes no fixed day-count or CPU-percentage figures; item 4.3 is marked not_applicable because the architecture has no in-path enforcement to add latency. One search limitation is noted: the NIST CMVP validated-modules search is JavaScript-rendered, so the absence of a Nozomi entry (item 8.1) could not be confirmed against a primary registry.

---

## Bibliography

[1] Nozomi Networks. "Nozomi Guardian - Passive Network Security Monitoring for OT and IoT Asset Visibility". https://www.nozominetworks.com/products/guardian (Retrieved: 2026-08-10T16:42:49Z)
[2] Nozomi Networks. "Nozomi Vantage - Cloud-Powered OT & IoT Security". https://www.nozominetworks.com/products/vantage (Retrieved: 2026-08-10T16:42:50Z)
[3] Nozomi Networks. "Guardian overview (N2OS technical documentation)". https://technicaldocs.nozominetworks.com/products/guardian/topics/intro/c_guardian_2.html (Retrieved: 2026-08-10T16:43:33Z)
[4] Nozomi Networks. "Vantage overview (N2OS technical documentation)". https://technicaldocs.nozominetworks.com/products/vantage/topics/intro/c_vantage-1.html (Retrieved: 2026-08-10T16:43:34Z)
[5] Nozomi Networks. "Arc overview (N2OS technical documentation)". https://technicaldocs.nozominetworks.com/products/arc/topics/intro/c_arc-1.html (Retrieved: 2026-08-10T16:43:34Z)
[6] Nozomi Networks. "Nozomi Arc - OT & IoT Endpoint Security". https://www.nozominetworks.com/platform/arc (Retrieved: 2026-08-10T16:43:38Z)
[7] Nozomi Networks. "Nozomi Threat Intelligence". https://www.nozominetworks.com/platform/threat-intelligence (Retrieved: 2026-08-10T16:43:38Z)
[8] Nozomi Networks. "Apply ISA/IEC 62443 Standards". https://www.nozominetworks.com/compliance/isa-iec-62443-standards (Retrieved: 2026-08-10T16:43:39Z)
[9] Nozomi Networks. "ServiceNow integration". https://www.nozominetworks.com/integrations/servicenow (Retrieved: 2026-08-10T16:43:39Z)
[10] Nozomi Networks. "Nozomi Networks Trust Center". https://www.nozominetworks.com/trust-center (Retrieved: 2026-08-10T16:43:46Z)
[11] Nozomi Networks. "Nozomi Central Management Console". https://www.nozominetworks.com/platform/central-management-console (Retrieved: 2026-08-10T16:43:47Z)
[12] Nozomi Networks. "Press release: Nozomi Networks and Siemens Bring Scalable Cybersecurity to Industrial Automation". https://www.nozominetworks.com/press-release/nozomi-networks-and-siemens-bring-scalable-cybersecurity-to-industrial-automation (Retrieved: 2026-08-10T16:43:46Z)
[13] Nozomi Networks. "Press release: Nozomi Networks Integrates with ServiceNow". https://www.nozominetworks.com/press-release/nozomi-networks-integrates-with-servicenow-to-help-automate-optimize-and-secure-manufacturing-operations-worldwide (Retrieved: 2026-08-10T16:43:46Z)
[14] Nozomi Networks. "White paper: Vantage Availability and Assurance". https://cdn.prod.website-files.com/645a4534705010e2cb244f50/6925d8e0105ff115c9799721_Nozomi-Networks-WP-VANTAGE-AV.pdf (Retrieved: 2026-08-10T16:44:28Z)
[15] Nozomi Networks. "White paper: Security Measures for Nozomi Networks Vantage". https://cdn.prod.website-files.com/645a4534705010e2cb244f50/688c42ba3e1e36106c2d767a_Nozomi-Networks-WP-Security-Measures-for-Nozomi-Networks-Vantage.pdf (Retrieved: 2026-08-10T16:44:29Z)
[16] Nozomi Networks. "White paper: Protecting Customer Data - Vantage SaaS Multi-tenancy". https://cdn.prod.website-files.com/645a4534705010e2cb244f50/688c48ad19292502273bc021_Nozomi-Networks-WP-Vantage-SaaS-Multi-tenancy.pdf (Retrieved: 2026-08-10T16:44:30Z)
[17] Nozomi Networks. "Federal Information Processing Standards - Reference Guide". https://technicaldocs.nozominetworks.com/out/pdf-output/Federal%20Information%20Processing%20Standards-Reference%20Guide.pdf (Retrieved: 2026-08-10T16:46:42Z)
[18] Nozomi Networks. "N2OS Configuration Reference Guide". https://technicaldocs.nozominetworks.com/out/pdf-output/N2OS%20Configuration-Reference%20Guide.pdf (Retrieved: 2026-08-10T16:47:44Z)
[19] Nozomi Networks. "Vantage Administrator Guide". https://technicaldocs.nozominetworks.com/out/pdf-output/Vantage-Administrator%20Guide.pdf (Retrieved: 2026-08-10T16:50:39Z)
[20] Nozomi Networks. "Arc Administrator Guide". https://technicaldocs.nozominetworks.com/out/pdf-output/Arc-Administrator%20Guide.pdf (Retrieved: 2026-08-10T16:49:05Z)
[21] Nozomi Networks. "Universal Software Development Kit". https://technicaldocs.nozominetworks.com/out/pdf-output/Universal-Software%20Development%20Kit.pdf (Retrieved: 2026-08-10T16:47:43Z)
[22] Splunkbase / Nozomi Networks. "Nozomi Networks Universal Add-on for Splunk (Splunkbase)". https://splunkbase.splunk.com/app/6905 (Retrieved: 2026-08-10T16:47:53Z)
[23] Nozomi Networks. "QRadar Universal Application Integration Guide". https://technicaldocs.nozominetworks.com/out/pdf-output/QRadar%20Universal%20Application-Integration%20Guide.pdf (Retrieved: 2026-08-10T16:53:19Z)
[24] Nozomi Networks. "Guardian and Central Management Console Maintenance Guide". https://technicaldocs.nozominetworks.com/out/pdf-output/Guardian%20and%20Central%20Management%20Console-Maintenance%20Guide.pdf (Retrieved: 2026-08-10T16:47:41Z)
[25] Nozomi Networks. "Central Management Console overview (N2OS technical documentation)". https://technicaldocs.nozominetworks.com/products/cmc/topics/intro/c_cmc_2.html (Retrieved: 2026-08-10T16:46:23Z)
[26] Nozomi Networks. "How the Nozomi Networks Platform Supports the U.S. DoW Zero Trust for OT Activities and Outcomes". https://www.nozominetworks.com/resources/how-the-nozomi-networks-platform-supports-the-u-s-dow-zero-trust-for-ot-activities-and-outcomes (Retrieved: 2026-08-10T16:50:50Z)
[27] ARC Advisory Group. "Nozomi Networks and Schneider Electric Deliver World's First Security Sensor Embedded in Remote Terminal Units". https://www.arcweb.com/blog/nozomi-networks-schneider-electric-deliver-worlds-first-security-sensor-embedded-remote (Retrieved: 2026-08-10T16:51:42Z)
[28] PeerSpot (IT Central Station). "Nozomi Networks reviews". https://www.peerspot.com/products/nozomi-networks-reviews (Retrieved: 2026-08-10T16:51:34Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** Direct site crawl (Bing/DDG search engines returned blocked/cached results): nozominetworks.com sitemap.xml and product/docs/integrations/press pages; technicaldocs.nozominetworks.com (intro pages, admin/reference guides, FIPS guide, SDK); trust-center white papers (Vantage Availability, Security Measures, Multi-tenancy); NIST CMVP and Common Criteria portal registry checks; PeerSpot reviews; ARC Advisory Group article; Splunkbase add-on listing.
- **Sources reviewed:** 28 (kept: 28, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 1, community: 1, vendor_blog: 3, vendor_datasheet: 8, vendor_doc: 15
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
