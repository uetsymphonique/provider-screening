# Microsegmentation Product Assessment: AppViewX - AppViewX AVX ONE (AVX Platform)

**Product ID:** `appviewx-avx-one`
**Version reference:** AVX ONE product pages, AVX ONE CLM / CLM-for-Kubernetes / SSH / PKIaaS datasheets, Spring/Summer 2026 release information sheets, technology-partner catalog, FAQ, PacificSource case study and analyst landing pages (IDC MarketScape 2026, KuppingerCole NHIM 2025, Forrester TEI 2026), captured 2026-08-10; platform formerly named AppViewX ONE, current branding 'AVX Platform'
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T15:30:00Z
**Total evidence items collected:** 67
**Total distinct sources:** 30

---

## 1. Overview

AppViewX AVX ONE — now branded the AVX Platform — is a machine-identity security platform: certificate lifecycle management (CLM), PKI-as-a-Service, SSH key governance, code signing, agent identity security, and ADC/firewall configuration automation [1], [3], [6]. The vendor positions it as "the leading unified solution for certificate lifecycle management (CLM), PKI automation, agent identity security, and crypto-agility" that discovers, issues, renews, deploys, revokes and governs digital certificates and cryptographic assets across cloud, hybrid, Kubernetes and on-premises environments [1]. It is not a workload microsegmentation product: its documented discovery scope covers certificates, SSH keys, AI agents and crypto credentials rather than network traffic flows [1], [3], and its policy engine governs certificate/PKI policies and network-device configurations rather than workload communications [2], [3], [9]. Deployment shapes are SaaS-first with private-cloud, hybrid and on-premises options [1], [9], plus a Kubernetes-native CLM module across EKS/AKS/GKE, OpenShift, Tanzu and Rancher [4]. Analyst recognition (IDC MarketScape 2026 leader, KuppingerCole NHIM 2025 leader, Forrester TEI 302% ROI) is for the CLM/NHI domain, not segmentation [18], [19], [20].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 1                | 1      | 0   |
| partial          | 12    | 0                | 12     | 0   |
| not_supported    | 4     | 0                | 4      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 20 items backed by ≥ 2 source_types; 14 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** No workload-resident traffic agent is documented; the platform is an out-of-band management plane (agentless discovery and integrations), so the agent CPU-overhead metric does not apply.
- **4.2:** No workload-resident agent is documented, so the agent RAM-footprint metric does not apply to the documented platform architecture.
- **4.3:** The platform is out-of-band and does not process in-path traffic, so the added network-latency metric does not apply.
- **4.4:** No in-path agent exists whose failure could interrupt workload traffic, so the agent fail-safe requirement does not apply to the documented architecture.
- **4.5:** No agent software is installed or updated on workloads, so the reboot-free agent installation requirement does not apply to the documented architecture.
- **6.4:** No workload agent-controller channel is documented (agentless discovery, no in-path agent), so a TLS 1.3/mTLS agent-channel requirement has no documented counterpart; no such statement exists in staged sources.
- **7.2:** No workload agent exists whose policy execution could continue autonomously during controller loss, so the autonomous-mode requirement does not apply to the documented architecture.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Not Supported | medium | — | Documented Smart Discovery is scoped to machine identities - certificates, SSH keys, AI agents and crypto credentials - discovered across CAs and endpoints; no real-time network data-flow discovery is documented. [1], [3], [13] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Visualization is documented as certificate chain-of-trust views, certificate inventory dashboards and app-centric InfraMaps of ADC/firewall infrastructure; no connection map organized by Application/Environment/Role/Process is documented. [3], [19], [22] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | — | no evidence found (No staged source quantifies connection/flow-history retention; the >=90-day forensic retention requirement could not be verified.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | — | no evidence found (No staged source documents vulnerability/CVE context displayed on a network/connection map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Not Supported | medium | — | Documented detection covers unmanaged, rogue and non-compliant certificates plus real-time firewall-policy risk alerts; no unrecognized or hidden network-flow detection is documented. [2], [9] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Not Supported | medium | — | The documented policy engine defines and enforces enterprise-wide PKI/certificate policies with RBAC and governs firewall rules and configurations; no workload communication policy keyed to tags/labels is documented. [2], [3], [9] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | — | AI-driven recommendations are documented (InfinityAI anomaly detection and fix suggestions, risk profiles that generate firewall rules, AI-generated PKI rules from policy documents), but they are scoped to certificate/PKI and firewall operations rather than microsegmentation rule recommendation. [1], [2], [8] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | — | no evidence found (No policy simulation/dry-run mode is documented; only policy validation and audit.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found (No 1-click policy rollback capability is documented.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No inherited/hierarchical policy-rule model is documented.) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | Endpoint coverage for certificate management is documented across Windows and Linux server platforms (Microsoft IIS/SQL/ADFS/Exchange, IBM WAS/MQ, Oracle WebLogic, Apache, Nginx, Tomcat, load balancers, firewalls, containers); no explicit OS support matrix for Windows 2003-2022/RHEL/CentOS/Ubuntu/AIX/Solaris is documented. [9], [14], [16] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | Kubernetes certificate lifecycle management is documented across EKS/AKS/GKE, OpenShift, Tanzu and Rancher clusters, including service-mesh pod-to-pod mTLS; native network isolation/segmentation enforcement in Kubernetes is not documented. [4], [11] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | Agentless discovery is explicitly documented (enhanced discovery without deploying additional agents) alongside SaaS, private-cloud, hybrid and on-prem deployment models; no workload-resident agent-based enforcement is documented. [1], [7] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | — | Air-gapped/offline root CA support and on-prem/private-cloud deployment are documented, but the platform is SaaS-first with cloud and CA integrations, and full operation in a completely air-gapped network is not explicitly documented. [6], [9] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scale is documented only qualitatively for certificate provisioning ('auto-scale with enterprise needs', 'massive scale', 'high availability and scalability'); no workload count is given, so the >=50,000 workloads threshold cannot be verified. [6] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | No workload-resident traffic agent is documented; the platform is an out-of-band management plane (agentless discovery and integrations), so the agent CPU-overhead metric does not apply. [1], [7] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No workload-resident agent is documented, so the agent RAM-footprint metric does not apply to the documented platform architecture. [1], [7] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | — | The platform is out-of-band and does not process in-path traffic, so the added network-latency metric does not apply. [1], [7] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | No in-path agent exists whose failure could interrupt workload traffic, so the agent fail-safe requirement does not apply to the documented architecture. [1], [7] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No agent software is installed or updated on workloads, so the reboot-free agent installation requirement does not apply to the documented architecture. [1], [7] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | REST APIs are documented for certificate operations, automation workflows and CA-agnostic integration, and a public Terraform provider is published; no statement that APIs cover 100% of administration functions was found. [4], [6], [9], [24] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | SIEM integration is documented as part of the platform's native integrations (ITSM, SIEM, MDMs; 200+ enterprise systems including SIEMs), but named SIEM/SOAR products (Splunk, QRadar, Sentinel) and Syslog/CEF protocols are not specified in staged sources. [1], [3], [4] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | — | ServiceNow is documented as an ITSM integration with a dedicated ServiceNow plugin for certificate workflows; CMDB tag synchronization for segmentation labels is not documented. [14], [28] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | high | — | CI/CD and IaC integrations with Ansible, Terraform, Jenkins, GitLab, HashiCorp Vault and service mesh (Istio, Linkerd) are documented, a public Terraform provider is published, and KuppingerCole cites broad integrations with DevOps pipelines and CI/CD tools. [4], [14], [18] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Not Supported | medium | — | Documented policy enforcement automates enterprise PKI/certificate policies, RBAC, crypto-standard and network-device configuration compliance; no workload process-level enforcement is documented. [2], [3], [12] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | — | no evidence found (No threat-intelligence feed integration or deception/honeypot capability is documented.) |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Compliance policy enforcement and audit reporting are documented with explicit coverage of GDPR, Sarbanes-Oxley, PCI-DSS and HIPAA; NIST 800-207 and IEC 62443 are not mentioned in staged sources. [2], [3], [12] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | N/A | medium | — | No workload agent-controller channel is documented (agentless discovery, no in-path agent), so a TLS 1.3/mTLS agent-channel requirement has no documented counterpart; no such statement exists in staged sources. [1], [7] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | High availability is documented for the SaaS/PKI service - multi-tenant SaaS delivery ensuring high availability and scalability, and CA load sharing for high availability, redundancy and scalability. [3], [6] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | N/A | medium | — | No workload agent exists whose policy execution could continue autonomously during controller loss, so the autonomous-mode requirement does not apply to the documented architecture. [1], [7] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | — | no evidence found (Only generic redundancy language is documented; no disaster-recovery site-sync configuration.) |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | FIPS 140-2 Level 3 HSMs are documented as backing PKIaaS CA keys, and code signing secures keys in FIPS-certified HSMs; no FIPS 140-2/140-3 validation of the platform software itself or Common Criteria certification is documented. [1], [6] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No OT/ICS compatibility certifications from Siemens, Honeywell or ABB are documented.) |

---

## 4. Notable Strengths

- **DevSecOps pipeline integration (item 5.4):** CI/CD and IaC integrations with Ansible, Terraform, Jenkins, GitLab, HashiCorp Vault and Istio/Linkerd service mesh are documented, backed by a public Terraform provider and KuppingerCole's citation of broad CI/CD-toolchain integrations [4], [14], [18], [24].
- **Kubernetes certificate automation (item 3.2):** Certificate lifecycle automation is documented across EKS/AKS/GKE, OpenShift, Tanzu and Rancher, including service-mesh pod-to-pod mTLS and REST-API-driven issuance [4], [11].
- **REST API surface (item 5.1):** REST APIs are documented for certificate operations, automation workflows and CA-agnostic integration, with an auto-enrollment protocol stack (EST, SCEP, NDES, CMP, ACME) and a published Terraform provider [4], [6], [9], [24].
- **ServiceNow and SIEM connectivity (items 5.2, 5.3):** ServiceNow is a documented ITSM integration with a dedicated plugin, and SIEM integration is listed among 200+ native enterprise integrations [1], [3], [14], [28].
- **SaaS high availability (item 7.1):** Multi-tenant SaaS delivery with documented high availability/scalability, plus CA load sharing for redundancy in the PKIaaS service [3], [6].

## 5. Notable Gaps / Risks

- **Not a microsegmentation product (items 1.1, 1.5, 2.1, 6.1):** No traffic-flow discovery, unrecognized-traffic detection, tag-based workload policy or process-level enforcement is documented; the platform governs machine identities and network-device configurations, so a buyer seeking workload segmentation would need a different product.
- **No quantified scale or agent metrics (items 3.5, 4.1-4.5):** Scale is described only qualitatively ("massive scale", "auto-scale"), and no workload-resident agent exists whose CPU/RAM/latency/fail-safe behavior could be measured, leaving the >50,000-workload and <1% CPU thresholds unverifiable.
- **Flow-retention and forensic history (item 1.3):** No connection-history retention duration is documented, so the >=90-day forensic retention requirement cannot be confirmed.
- **Simulation, rollback and hierarchical policy (items 2.3, 2.4, 2.5):** No policy simulation/dry-run, 1-click rollback or inherited/hierarchical policy model is documented.
- **Certification depth (items 8.1, 8.2):** Only HSM-level FIPS 140-2 claims are documented (no product-level FIPS 140-2/140-3 validation or Common Criteria certification found), and no OT certifications from Siemens/Honeywell/ABB exist in the staged evidence.

## 6. Evidence Quality Notes

Evidence was staged from 30 distinct sources: 17 vendor_doc pages, 4 vendor_datasheets, 2 product_release_notes, 2 vendor_blog posts, 3 analyst_report landing pages (IDC, KuppingerCole, Forrester — vendor-hosted), 1 case study, and 1 certification_registry search (NIST CMVP). 20 of 33 items are backed by >= 2 source_types; 14 items rely on vendor_doc only, which is why their confidence is capped at medium. Only one item (5.4, CI/CD integration) reaches high confidence, triangulated across the CLM-for-Kubernetes datasheet, the technology-partner catalog and the KuppingerCole analyst page.

The dominant limitation is source independence: all staged materials are AppViewX-controlled (product pages, datasheets, release sheets, GitHub repos, and vendor-hosted analyst summaries), so even items rated supported (7.1) or partial rest on vendor claims. Items rated not_supported (1.1, 1.5, 2.1, 6.1) were decided not from silence but because the documentation comprehensively describes an alternative scope (identity/certificate discovery, PKI/crypto and network-device policy enforcement) that excludes the checklist capability. Items rated not_applicable (4.1-4.5, 6.4, 7.2) follow the documented agentless, out-of-band architecture, consistent with the tufin-orchestration-suite and algosec-horizon precedents. PeerSpot review pages staged for this run rendered no review text (JavaScript-only content) and were excluded. No contradictory sources were found among the staged evidence.

---

## Bibliography

[1] AppViewX. "AVX ONE / AVX Platform overview page (Machine & AI Identity Security)". https://www.appviewx.com/avx-one/ (Retrieved: 2026-08-10T14:00:00Z)
[2] AppViewX. "Firewall Policy Management for Enterprise Security Teams (AppViewX ADC+)". https://www.appviewx.com/solutions/firewall-policy-management/ (Retrieved: 2026-08-10T14:00:00Z)
[3] AppViewX. "AppViewX AVX ONE CLM Datasheet (Simplify Enterprise-wide Certificate Lifecycle Management)". https://www.appviewx.com/Collaterals/Datasheet/AVX-ONE/AVX-ONE-CLM.pdf (Retrieved: 2026-08-10T14:00:00Z)
[4] AppViewX. "AppViewX AVX ONE CLM for Kubernetes Datasheet". https://www.appviewx.com/Collaterals/Datasheet/AVX-ONE-CLM-for-Kubernetes.pdf (Retrieved: 2026-08-10T14:00:00Z)
[5] AppViewX. "AppViewX AVX ONE SSH Lifecycle Management Datasheet". https://www.appviewx.com/Collaterals/Datasheet/AVX-ONE-SSH.pdf (Retrieved: 2026-08-10T14:00:00Z)
[6] AppViewX. "AppViewX AVX ONE PKI-as-a-Service Datasheet (Modern, Secure, Scalable Private PKI)". https://www.appviewx.com/Collaterals/Datasheet/AVX-ONE-PKIaaS.pdf (Retrieved: 2026-08-10T14:00:00Z)
[7] AppViewX. "AppViewX Spring 2026 Product Release Datasheet". https://www.appviewx.com/Collaterals/Release-Information/spring-release-2026-information-release.pdf (Retrieved: 2026-08-10T14:00:00Z)
[8] AppViewX. "AppViewX Summer 2026 Product Release Datasheet". https://www.appviewx.com/Collaterals/Release-Information/summer-release-2026-information-release.pdf (Retrieved: 2026-08-10T14:00:00Z)
[9] AppViewX. "AppViewX CLM product page (Automate Certificate Lifecycle Management)". https://www.appviewx.com/products/ (Retrieved: 2026-08-10T14:00:00Z)
[10] AppViewX. "Kubernetes Container Security | Certificate Lifecycle Management for Kubernetes". https://www.appviewx.com/solutions/kubernetes-container-security/ (Retrieved: 2026-08-10T14:00:00Z)
[11] AppViewX. "AVX CLM for Kubernetes product page". https://www.appviewx.com/products/avx-one-clm-for-kubernetes/ (Retrieved: 2026-08-10T14:00:00Z)
[12] AppViewX. "Compliance Policy Enforcement and Reporting (machine identity governance)". https://www.appviewx.com/solutions/compliance-policy-enforcement-and-reporting/ (Retrieved: 2026-08-10T14:00:00Z)
[13] AppViewX. "AVX CLM with Smart Discovery (certificate discovery)". https://www.appviewx.com/solutions/clm-smart-discovery/ (Retrieved: 2026-08-10T14:00:00Z)
[14] AppViewX. "AppViewX Technology Partner Ecosystem (integration catalog)". https://www.appviewx.com/partners/technology-partners/ (Retrieved: 2026-08-10T14:00:00Z)
[15] AppViewX. "AppViewX Integrations hub". https://www.appviewx.com/integrations/ (Retrieved: 2026-08-10T14:00:00Z)
[16] AppViewX. "AppViewX Frequently Asked Questions". https://www.appviewx.com/resources/faqs/ (Retrieved: 2026-08-10T14:00:00Z)
[17] AppViewX. "AppViewX Documentation portal (product/module index)". https://docs.appviewx.com/ (Retrieved: 2026-08-10T14:00:00Z)
[18] KuppingerCole (hosted by AppViewX). "KuppingerCole Leadership Compass NHIM Report (AppViewX landing page)". https://www.appviewx.com/kuppingercole-leadership-compass-nhim-report/ (Retrieved: 2026-08-10T14:00:00Z)
[19] IDC (hosted by AppViewX). "IDC MarketScape Worldwide CLM Software 2026 (AppViewX landing page)". https://www.appviewx.com/idc-marketscape-on-certificate-lifecycle-management/ (Retrieved: 2026-08-10T14:00:00Z)
[20] Forrester Consulting (hosted by AppViewX). "Forrester TEI study of AppViewX 2026 (landing page)". https://www.appviewx.com/forrester-report-2026-the-total-economic-impact-of-appviewx/ (Retrieved: 2026-08-10T14:00:00Z)
[21] AppViewX. "AppViewX Industry Recognition page". https://www.appviewx.com/company/industry-recognition/ (Retrieved: 2026-08-10T14:00:00Z)
[22] AppViewX. "AppViewX blog: Gain App-centric Visibility and Smart Insights into the Network Infrastructure (ADC+)". https://www.appviewx.com/blogs/gain-app-centric-visibility-and-smart-insights-into-the-network-infrastructure/ (Retrieved: 2026-08-10T14:00:00Z)
[23] AppViewX. "AppViewX blog: How Machine Identity Management Powers the Zero Trust Security Model". https://www.appviewx.com/blogs/how-machine-identity-management-powers-zero-trust-security-model/ (Retrieved: 2026-08-10T14:00:00Z)
[24] AppViewX (GitHub). "AppViewX Terraform provider (terraform-provider-appviewx GitHub repository)". https://github.com/AppViewX/terraform-provider-appviewx (Retrieved: 2026-08-10T14:00:00Z)
[25] AppViewX (GitHub). "AppViewX Helm charts for Kubernetes (crypto-mesh / Istio CSR, GitHub repository)". https://github.com/AppViewX/helm-chart (Retrieved: 2026-08-10T14:00:00Z)
[26] AppViewX (GitHub). "AppViewX Kubernetes CSI provider (certificate provisioning, GitHub repository)". https://github.com/AppViewX/appviewx-csi-provider (Retrieved: 2026-08-10T14:00:00Z)
[27] AppViewX. "Case Study: How PacificSource Transformed Certificate Management with AppViewX". https://www.appviewx.com/Collaterals/Case-Studies/Case-Study-AppViewX-Pacific-Source-2025.pdf (Retrieved: 2026-08-10T14:00:00Z)
[28] AppViewX. "47-Day Countdown: ServiceNow Plugin and Pages (webinar page)". https://www.appviewx.com/47-day-countdown-servicenow-plugin-and-pages/ (Retrieved: 2026-08-10T14:00:00Z)
[29] NIST CSRC. "NIST CMVP Validated Modules search (Advanced, keyword AppViewX)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&Keyword=AppViewX (Retrieved: 2026-08-10T14:00:00Z)
[30] AppViewX. "AppViewX SSH product page (govern SSH access at scale)". https://www.appviewx.com/products/ssh/ (Retrieved: 2026-08-10T14:00:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 34
- **Sources reviewed:** 30 (kept: 30, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 3, case_study: 1, certification_registry: 1, product_release_notes: 2, vendor_blog: 2, vendor_datasheet: 4, vendor_doc: 17
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
