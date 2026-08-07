# Microsegmentation Product Assessment: Akamai Technologies — Akamai Guardicore Segmentation

**Product ID:** `akamai-guardicore-segmentation`
**Version reference:** Akamai product brief published 03/26; Guardicore Platform Agent 7.2.x line
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-07T00:00:00Z
**Total evidence items collected:** 35
**Total distinct sources:** 20

---

## 1. Overview

Akamai Guardicore Segmentation (formerly Guardicore Centra, acquired by Akamai in 2021) is a software-defined microsegmentation platform that combines host-agent enforcement with agentless network-flow collection to control east-west traffic across data centers, cloud, containers, and OT [1, 6]. The vendor positions it as a Zero Trust segmentation platform with continuous, AI-driven discovery, process-level enforcement, and dynamic deception for breach detection [2, 10, 13]. Supported deployment shapes include Windows and Linux servers, macOS endpoints, VMs across AWS/Azure/GCP, Kubernetes via CNI-level enforcement, and BlueField-DPU-based agentless enforcement for OT [3, 6, 14]. The management server is available in both SaaS and on-premises form [6].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 14    | 10               | 4      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 12    | 0                | 0      | 12  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 9 items backed by ≥ 2 source_types; 3 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Vendor and third-party sources describe continuous, real-time discovery via lightweight sensors and flow telemetry that build a living application dependency map. [2], [6], [8] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | high | — | The Reveal map ties each connection to processes and services, giving App / Environment / Role / Process granularity at Layer 7. [2], [6] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | — | no evidence found (Public sources describe rich historical telemetry export but do not state a specific default flow-history retention in days.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | — | The Tenable integration brief describes labelling assets with CVE and risk scores and shows CVE labels on assets in the Reveal map for risk-based segmentation. [14] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | AI-analyzed flow telemetry surfaces unmanaged assets and non-standard flows, which the platform then presents in the dependency map. [6] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | — | Independent write-ups describe granular policies authored against flexible labels, process, user identity and FQDN, independent of IP/VLAN. [6], [8] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | high | — | The 2026 AI update to Guardicore automatically generates and explains segmentation policies and simulates impact before enforcement, per Akamai and SiliconAngle coverage. [2], [12] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | — | Guardicore's 'Allow Mode' runs AI-generated policies in simulation showing projected impact before any traffic is blocked. [6] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found (Public sources reference 'rollback rates' as an operational metric but do not document a documented one-click instant rollback control.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No public description of hierarchical / inherited policy structures was located.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Supported | high | — | Guardicore's 2021 legacy-support release brought coverage for Windows 2000/2003/2008, RHEL 4/5, Solaris SPARC 10/11 and HP-UX 11.23/11.31; current Platform Agent docs list Windows 10-11, Server 2012-2019, RHEL 8+, Debian 11 and Ubuntu 18-22. [5], [11] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | Kubernetes enforcement is native via CNI controller with DaemonSet+Helm deployment and a third-party review lists OpenShift OVN among supported CNIs, but the Akamai blog itself notes OpenShift and Cilium support was still being expanded at time of writing. [3], [6] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | — | Guardicore combines agent-based enforcement with agentless visibility via NetFlow/sFlow/IPFIX network collectors, per independent reviews. [6], [20] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | — | The management server is documented for both on-prem and SaaS; support for fully air-gapped operation is not explicitly certified in public sources. [6] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 300000 workloads | Akamai cites a global consulting-firm deployment of 300,000 endpoints secured in two weeks, well above the 50,000-workload threshold; the figure is a vendor-attributed customer case. [1] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | — | no evidence found (Public sources describe the agent as 'lightweight' but do not cite a measured CPU percentage under load.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | — | no evidence found (Only macOS memory profile ranges (10 MB soft up to 1000 MB hard limit by host RAM tier) surfaced; that is agent configuration, not measured resident RAM on Windows/Linux at production load.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | — | no evidence found (No public benchmark of added network latency (ms) attributable to the agent was located.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | — | no evidence found (Public documentation and third-party reviews do not describe agent fail-safe behavior when the agent crashes or is stopped (fail-open vs fail-close, traffic continuity).) |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | — | no evidence found (Vendor techdocs describe silent install and remote upgrade but do not explicitly state whether a reboot is required.) |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | Guardicore exposes a REST API used by SIEM add-ons and automation recipes; public sources confirm the API's existence but do not verify 100% coverage of admin console functionality. [1], [9] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | — | Guardicore telemetry is shipped to Splunk and IBM QRadar via CEF/syslog, with a dedicated Splunkbase add-on that pulls data through the REST API. [6], [9] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | high | — | A ServiceNow-certified Guardicore application in the ServiceNow Store pulls CMDB data via REST to produce labels for Reveal maps and policies. [18], [19] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | — | Vendor pages mention REST API and automation recipes for DevOps and CI/CD frameworks, but specific Jenkins / GitLab / Terraform module coverage is not detailed in public documents. [1] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | high | — | Independent reviews describe the enforcement agent as a process-level Layer 7 firewall that ties each connection to the initiating process. [6], [20] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Supported | high | — | Guardicore's patented dynamic deception can redirect attackers into a Guardicore-hosted honeypot on anomalous behaviour and records their actions. [10], [13] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Akamai publishes a PCI DSS mapping whitepaper (March 2024) and third parties note NIST SP 800-207 alignment; ready-made ISO 27001 and IEC 62443 reports were not confirmed in public sources. [6], [15] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | — | Guardicore training material states the agent-to-aggregator connection is encrypted and authenticated on TCP/443 using TLS 1.2; the traffic is authenticated but the checklist's TLS 1.3 requirement is not explicitly met. [7] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Unknown | low | — | no evidence found (The Centra installation guide references a Scaling Architecture section but the public excerpts do not describe controller HA cluster (active-active / active-passive) topology.) |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | — | no evidence found (Publicly available material implies local policy decisions on the agent but does not describe explicit autonomous mode when controller connectivity is lost.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (The Centra installation guide explicitly notes disaster-recovery setup is not covered in the guide, and no public DR sync procedure was located.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | — | no evidence found (No entry in NIST CMVP or Common Criteria portals for Guardicore was located from public searches; absence of evidence is not evidence of absence.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | — | An OT integration with NVIDIA BlueField and Siemens is described as aligning with IEC 62443, which is architectural alignment, not a Siemens/Honeywell/ABB software-compatibility certification for the checklist's target vendors. [16] |

---

## 4. Notable Strengths

- **Continuous, process-level visibility (items 1.1, 1.2, 6.1):** Guardicore ties every observed flow to the initiating process and refreshes the map as workloads change, giving Layer-7 application context that IP-based tools miss [2, 6, 11].
- **Rich integration surface (items 5.2, 5.3, 1.4):** Purpose-built connectors for Splunk, QRadar, ServiceNow CMDB, and Tenable make Guardicore a first-class citizen in existing SecOps stacks [9, 13a, 14].
- **Dynamic deception for breach containment (item 6.2):** Patented honeypot redirection converts lateral-movement attempts into recorded attacker behaviour and IOCs [10, 13].
- **Proven scale (item 3.5):** A vendor-cited customer secured 300,000 endpoints in two weeks, comfortably exceeding the 50,000-workload gate [1].
- **AI-driven policy authoring with simulation (items 2.2, 2.3):** The March 2026 AI update generates and explains policies and validates them in Allow Mode before enforcement [12, 6].

## 5. Notable Gaps / Risks

- **Transport encryption below the checklist bar (item 6.4):** Public architecture material describes TLS 1.2, not TLS 1.3, and does not confirm mutual (client-cert) authentication of agents [7].
- **No quantitative performance evidence (items 4.1, 4.2, 4.3, 4.4):** CPU, RAM, latency, and fail-safe behaviour are all unknown from public sources; a proof-of-value or vendor benchmark request will be needed before procurement.
- **High-availability internals opaque (items 7.1, 7.2, 7.3):** Controller HA topology, autonomous-mode behaviour on controller loss, and DR sync procedures are not documented in publicly available material.
- **No public FIPS / Common Criteria certification found (item 8.1):** Absence in NIST CMVP and CC portal searches; needs vendor confirmation for regulated environments.
- **OpenShift maturity mixed (item 3.2):** Third-party review lists OpenShift OVN as supported CNI, but the Akamai blog still describes it as work-in-progress; needs verification against current release notes.

## 6. Evidence Quality Notes

Non-unknown verdicts drew on 18 distinct sources including vendor product page and product brief, Akamai TechDocs, three staged Akamai solution briefs (PCI whitepaper, ServiceNow CMDB integration, Tenable integration), an Akamai press release, and independent sources (Security Scientist, PeerSpot, SiliconAngle, CSO Online, Help Net Security, PR Newswire, Industrial Cyber, Splunkbase, and a leaked Guardicore training excerpt on Course Hero). 15 of the 20 non-unknown items cite ≥ 1 independent source; the remainder rely on vendor documentation and are capped at medium confidence per validator rule.

Three tensions surfaced. First, on Kubernetes/OpenShift, a 2022-era Akamai blog says OpenShift support was still being expanded while a 2025 third-party review lists OpenShift OVN as supported — the verdict was set to partial. Second, on TLS, the only concrete number located is TLS 1.2 on TCP/443, which is short of the TLS 1.3 requirement, so 6.4 is partial rather than supported. Third, on IEC 62443, an Industrial Cyber article describes architectural alignment via the NVIDIA BlueField OT integration; that is not the Siemens/Honeywell/ABB software-compatibility certification asked for in item 8.2, so the verdict is partial with an explicit gap note.

Thirteen items are unknown — mostly quantitative (4.1-4.3), operational (4.4, 4.5), HA (7.1-7.3), and certification (8.1) — because no public numeric or certification evidence was located. Per the anti-fabrication contract these are not converted to `not_supported`; a deep pass with vendor SEs or a proof-of-value would be needed to close them.

---

## Bibliography

[1] Akamai Technologies. "Akamai Guardicore Segmentation for Hybrid Cloud". https://www.akamai.com/products/akamai-guardicore-segmentation (Retrieved: 2026-08-07)
[2] Akamai Technologies. "Akamai Product Brief: Akamai Guardicore Segmentation (Published 03/26)". https://www.akamai.com/site/en/documents/product-brief/akamai-guardicore-segmentation.pdf (Retrieved: 2026-08-07)
[3] Akamai Technologies. "Feature Spotlight: Kubernetes Enforcement". https://www.akamai.com/blog/security/feature-spotlight-kubernetes-enforcement (Retrieved: 2026-08-07)
[4] Akamai Technologies. "About Access, Threat Protection, and Segmentation - Guardicore Platform Agent". https://techdocs.akamai.com/guardicore-platform-agent/docs/about-aztc (Retrieved: 2026-08-07)
[5] Akamai Technologies. "Guardicore Platform Agent - Requirements". https://techdocs.akamai.com/guardicore-platform-agent/docs/requirements (Retrieved: 2026-08-07)
[6] Security Scientist. "12 Questions and Answers About Akamai Guardicore Segmentation". https://www.securityscientist.net/blog/12-questions-and-answers-about-akamai-guardicore-segmentation-akamai/ (Retrieved: 2026-08-07)
[7] Guardicore (via Course Hero). "GCSA - Centra Components Architecture (training material excerpt)". https://www.coursehero.com/file/189598805/Day-1-01-GCSA-Centra-Components-Architecture-v42pdf/ (Retrieved: 2026-08-07)
[8] Data Sciences Corporation. "Solution Brief: Akamai Guardicore Segmentation". https://datasciences.co.za/wp-content/uploads/2025/09/Solution-Brief-Akamai-Guardicore-Segmentation.pdf (Retrieved: 2026-08-07)
[9] Splunkbase. "Akamai Guardicore Add-on for Splunk". https://splunkbase.splunk.com/app/7426 (Retrieved: 2026-08-07)
[10] Akamai Technologies. "Guardicore Expands Breach and Threat Detection". https://www.akamai.com/newsroom/press-release/guardicore-expands-threat-detection-and-response-capabilities-to-cover-more-attack-types-aimed-at-data-centers-and-clouds (Retrieved: 2026-08-07)
[11] Help Net Security. "Guardicore extends microsegmentation and Zero Trust security to legacy infrastructure". https://www.helpnetsecurity.com/2021/04/09/guardicore-microsegmentation-zero-trust/ (Retrieved: 2026-08-07)
[12] SiliconANGLE. "Akamai updates Guardicore Segmentation with AI to automate zero-trust policy enforcement". https://siliconangle.com/2026/03/24/akamai-updates-guardicore-segmentation-ai-automate-zero-trust-policy-enforcement/ (Retrieved: 2026-08-07)
[13] CSO Online. "Guardicore Centra provides visibility, protection through advanced micro-segmentation". https://www.csoonline.com/article/563289/guardicore-centra-provides-visibility-protection-through-advanced-micro-segmentation.html (Retrieved: 2026-08-07)
[14] Akamai Technologies. "Akamai Solution Brief: Tenable Vulnerability Management for Guardicore Segmentation (2023)". https://www.akamai.com/site/en/documents/brief/2023/tenable-vulnerability-management-for-akamai-guardicore-segmentation.pdf (Retrieved: 2026-08-07)
[15] Akamai Technologies / GRSee Consulting. "Akamai Guardicore Segmentation PCI DSS Whitepaper (March 2024)". https://www.akamai.com/site/en/documents/white-paper/2024/pci-whitepaper-akamai-guardicore-segmentation-revision.pdf (Retrieved: 2026-08-07)
[16] Industrial Cyber. "NVIDIA partners with Akamai, Forescout, Palo Alto Networks and Siemens for OT threat detection". https://industrialcyber.co/ai/nvidia-partners-with-akamai-forescout-palo-alto-networks-and-siemens-to-target-real-time-ot-threat-detection/ (Retrieved: 2026-08-07)
[17] PR Newswire. "Guardicore Simplifies Micro-Segmentation To Speed Deployment In Hybrid Data Center Environments". https://www.prnewswire.com/news-releases/guardicore-simplifies-micro-segmentation-to-speed-deployment-in-hybrid-data-center-environments-300805772.html (Retrieved: 2026-08-07)
[18] PR Newswire. "Guardicore Receives Application Certification from ServiceNow". https://www.prnewswire.com/news-releases/guardicore-receives-application-certification-from-servicenow-301103015.html (Retrieved: 2026-08-07)
[19] Akamai Technologies. "Akamai Solution Brief: Guardicore Segmentation + ServiceNow CMDB Integration (2023)". https://www.akamai.com/site/en/documents/brief/2023/akamai-guardicore-segmentation-and-servicenow-cmdb-integration.pdf (Retrieved: 2026-08-07)
[20] PeerSpot. "PeerSpot: Akamai Guardicore Segmentation vs VMware NSX". https://www.peerspot.com/products/comparisons/akamai-guardicore-segmentation_vs_vmware-nsx (Retrieved: 2026-08-07)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 20 (kept: 20, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 11, vendor_blog: 2, vendor_datasheet: 3, vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
