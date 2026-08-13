# Microsegmentation Product Assessment: Cyolo - Cyolo PRO (with Cyolo CPS Segmentation)

**Product ID:** `cyolo-pro`
**Version reference:** Cyolo PRO 7.0.x (docs release notes 7.0.8; CPS Segmentation launched July 2026)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:00:00Z
**Total evidence items collected:** 58
**Total distinct sources:** 23

---

## 1. Overview

Cyolo is an OT/ICS-focused security vendor whose platform has two products: Cyolo PRO (Privileged Remote Operations), an identity-based secure remote access solution, and Cyolo CPS Segmentation, the microsegmentation offering launched in July 2026 that extends the platform from human-to-machine access into machine-to-machine communication control [5]. CPS Segmentation is agentless: a Fabric Controller collects passive telemetry from network switches to build a real-time OT asset inventory and connection map [14], and policies are identity-, protocol-, and zone-based with policy simulation before enforcement [3]. Deployment is infrastructure-agnostic, with four models from Cyolo Global Gateway through customer-managed Private Gateways to fully isolated, offline environments [13]; the IDAC controller runs as a lightweight Docker component on Linux (Ubuntu 22.04/24.04, RHEL 8/9) and clusters via RAFT consensus for high availability [16][17]. Cyolo positions the platform for manufacturing, energy and utilities, and critical infrastructure, emphasizing zero-trust access, legacy-system coverage, and compliance alignment with ISA/IEC 62443, NIS2, NERC CIP and ISO [7].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 11    | 1                | 10     | 0   |
| partial          | 12    | 0                | 11     | 1   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 10    | 0                | 0      | 10  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 19 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | CPS Segmentation passively discovers OT assets and communication flows via the Fabric Controller's switch telemetry, continuously building an asset inventory with real-time traffic insight. [3], [14], [15] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | medium | - | Visual flow mapping, blast-radius analysis, and topology views are documented, including asset-pair and protocol connection views. [3], [4], [5] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Log-export and session-recording retention are admin-configurable, with session recording defaulting to 0 days; no >=90-day default for connection-flow history is documented. [18], [21] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (No CVE/vulnerability context layer documented on the connection map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Shadow-access discovery and detection of unauthorized communication paths that bypass Cyolo are documented, with controls for unknown newly connected assets. [3], [6], [14] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Policy is identity-, protocol-, and zone-based, connecting verified identities to authorized applications instead of relying on network-based controls. [1], [3], [4] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | Intelligent grouping and policy recommendations are documented in CPS Segmentation. [3], [5] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | medium | - | Policies can be simulated against real network traffic before enforcement, including pre-enforcement simulation across the segmentation lifecycle. [1], [3], [5] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No one-click/instant policy rollback capability documented.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | Access Groups provide inherited access rules for applications, and Purdue-aligned zones support hierarchical segmentation. [3], [15] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | Agentless access extends to legacy Windows/Linux systems, dated PLCs and HMIs per the vendor and the SANS briefing; no AIX/Solaris support is documented. [2], [4], [11] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (No container/Kubernetes/OpenShift native isolation documented.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | Agentless remote access and agentless asset discovery are complemented by the optional Cyolo Connect agent for endpoint posture. [2], [3], [4] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | high | - | An Isolated deployment model routes IDACs exclusively through customer-managed Private Gateways, backed by an offline installer and an air-gapped customer deployment (Rapac Energy). [1], [10], [13], [19] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Only qualitative scale statements are published (100+ sites; one IDAC per 1,000 concurrent users); no total workload capacity figure is documented. [4], [16] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | - | no evidence found (No agent CPU-overhead figure published.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | - | no evidence found (No agent RAM-footprint figure published.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Vendor material and the SANS briefing describe fast, low-latency connections, but no per-connection policy-latency figure is published. [4], [11] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | Enforcement is agentless with no cloud dependency, and the vendor states deployment without disruption; no explicit fail-open guarantee for the enforcement path is documented. [3] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | - | Asset-side deployment is agentless and the vendor states deployment causes no disruptions or downtime; no explicit no-reboot statement for the optional endpoint agent is documented. [1], [4] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | A REST API with role-based access (roles apply to both the Admin Portal and API), API keys, and management-node endpoints is documented; an explicit 100% admin-function coverage claim is not published. [4], [17], [22] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | SIEM/SOAR integrations (IBM QRadar, Microsoft Sentinel, FortiSIEM/SOAR) plus Syslog/S3 log export in CEF format are documented. [8], [18] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | low | - | The vendor states integration with ITSM platforms among others; no ServiceNow-specific tag-sync integration is documented. [2] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No CI/CD pipeline (Jenkins/GitLab/Terraform) integration documented.) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | - | no evidence found (Session/action and SSH command controls exist, but no OS process-level enforcement is documented.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Malware detection (file hash checks, ICAP deep scanning) and AI-based risk scoring are documented; no honeypot/deception capability is documented. [4], [15] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Alignment with ISA/IEC 62443, NERC CIP, NIS2, CMMC/NIST and ISO is documented; PCI-DSS and NIST 800-207 are not specifically addressed. [4], [7] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | Connectivity uses TLS over TCP 443 with outbound-only IDAC connections; no explicit TLS 1.3 or mutual-TLS version statement is documented. [4], [16] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | Cluster HA is documented with a minimum of 3 IDACs for tenant/cluster HA and 2 for site HA, with RAFT-based consensus among management nodes. [15], [16], [17] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | - | no evidence found (No statement on continued policy enforcement when the controller is fully disconnected.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | - | no evidence found (Multi-site management is documented but no disaster-recovery site sync or backup/restore procedure.) |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Unknown | low | - | no evidence found (No FIPS 140-2/140-3 or Common Criteria certification found in vendor material or the Common Criteria portal.) |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | Siemens TIA Portal and Rockwell FactoryTalk/Studio 5000 are supported native applications, and Siemens Energy service teams connect via Cyolo per the Rapac case study; Honeywell/ABB are not explicitly documented. [2], [10] |

---

## 4. Notable Strengths

- **Real-time passive discovery and flow mapping (items 1.1, 1.2, 1.5):** the Fabric Controller collects passive switch telemetry with no agents or active probing, continuously building an asset inventory and exposing shadow access and unauthorized communication paths [14][6][3].
- **Simulation-first policy management (items 2.2, 2.3):** intelligent grouping and policy recommendations are paired with pre-enforcement simulation against real network traffic, reducing production risk before enforcement [3][5].
- **Identity-, protocol-, and zone-based policy (items 2.1, 2.5):** access is authorized to applications by verified identity, with inherited Access Groups and Purdue-aligned zones supporting hierarchical segmentation [4][15].
- **Air-gapped and isolated deployment (item 3.4):** an Isolated deployment model routes controllers exclusively through customer-managed Private Gateways, an offline installer is documented, and Rapac Energy runs Cyolo in a network disconnected from the public internet [13][19][10].
- **Cluster high availability (item 7.1):** tenant/cluster HA requires a minimum of 3 IDACs (2 for site HA), with RAFT-based consensus among management nodes [16][17][15].

## 5. Notable Gaps / Risks

- **No published performance figures (items 4.1, 4.2, 4.3):** agent CPU/RAM overhead and per-connection policy latency are undocumented; only qualitative "fast, low-latency" claims exist, so sizing against a <1% CPU / <100MB / <0.1ms requirement is not possible [4][11].
- **No documented flow-history retention of 90+ days (item 1.3):** retention is admin-configurable and session recordings default to 0 days; a forensic-grade 90-day flow history is not evidenced [18][21].
- **Container and process-level isolation absent from evidence (items 3.2, 6.1):** no Kubernetes/OpenShift native isolation and no OS process-level enforcement are documented; SSH command control and session action policies are the closest documented controls [23].
- **Rollback, autonomous enforcement, and DR are not evidenced (items 2.4, 7.2, 7.3):** there is no 1-click policy rollback, no statement on continued enforcement if the controller is fully disconnected, and no documented disaster-recovery site sync.
- **Certification gap (item 8.1):** no FIPS 140-2/140-3 or Common Criteria certification appears in vendor material or the Common Criteria portal; buyers with federal-certification requirements need vendor confirmation.

## 6. Evidence Quality Notes

Evidence for this assessment draws on 23 staged sources: 16 vendor documentation pages (cyolo.io product pages and docs.cyolo.io), 1 vendor datasheet PDF, 3 vendor release/press communications, 2 named-customer case studies (Tata Chemicals, Rapac Energy), and 1 independent third-party review (SANS Institute Product Briefing). 19 of 33 items are backed by 2+ source types; 11 items rely on vendor-only material and are confidence-capped at medium by the validator. Only item 3.4 (air-gapped deployment) reaches high confidence, triangulated across the Isolated deployment model documentation, the offline installer guide, and the Rapac Energy case study of a network disconnected from the public internet.

No source contradictions were found: vendor, datasheet, SANS, and case-study statements agree on the core claims (agentless operation, legacy-system support, low-latency access, isolated deployment). The main quality limitation is scope: numeric performance figures, Kubernetes/process-level isolation, policy rollback, DR sync, and FIPS/Common Criteria certification are simply not addressed anywhere in the staged material, so the corresponding items are rated unknown rather than not_supported. CPS Segmentation launched in July 2026 and has minimal third-party coverage; its capabilities are evidenced mainly through vendor product pages and the launch press release.

---

## Bibliography

[1] Cyolo. "Cyolo | Secure Connectivity for OT & Critical Infrastructure". https://cyolo.io/ (Retrieved: 2026-08-10T14:00:00Z)
[2] Cyolo. "Cyolo PRO | Secure OT-First Remote Privileged Access". https://cyolo.io/cyolo-pro-privileged-remote-operations (Retrieved: 2026-08-10T14:00:00Z)
[3] Cyolo. "Cyolo CPS Segmentation | Practical Zero Trust Microsegmentation for OT". https://cyolo.io/cyolo-cps-segmentation (Retrieved: 2026-08-10T14:00:00Z)
[4] Cyolo. "Datasheet: Enable Privileged Remote Access with Cyolo PRO (PDF)". https://cyolo.io/datasheets/enable-privileged-remote-access-with-cyolo-pro (Retrieved: 2026-08-10T14:00:00Z)
[5] Cyolo. "With Launch of CPS Segmentation, Cyolo Offers First Secure Connectivity Platform for Critical Infrastructure (Press Release)". https://cyolo.io/press-releases/cps-segmentation-first-secure-connectivity-platform-for-critical-infrastructure (Retrieved: 2026-08-10T14:00:00Z)
[6] Cyolo. "Cyolo Releases Powerful New Capabilities to Redefine Secure Remote Access for OT (Press Release)". https://cyolo.io/press-releases/cyolo-releases-powerful-new-capabilities-to-redefine-secure-remote-access-for-ot (Retrieved: 2026-08-10T14:00:00Z)
[7] Cyolo. "Compliance-First Secure Remote OT Access: Ready for ISA/IEC 62443, NIS2, and More". https://cyolo.io/regulatory-compliance (Retrieved: 2026-08-10T14:00:00Z)
[8] Cyolo. "Technology Integrations". https://cyolo.io/technology-integrations (Retrieved: 2026-08-10T14:00:00Z)
[9] Cyolo. "Case Study: Tata Chemicals - Secure Remote Access for Employees and Vendors". https://cyolo.io/case-studies/tata-chemicals-secure-remote-access-employees-vendors (Retrieved: 2026-08-10T14:00:00Z)
[10] Cyolo. "Case Study: How Rapac Energy Saved Weeks of Work Securing Its OT & SCADA Systems With Cyolo". https://cyolo.io/case-studies/how-rapac-energy-secures-scada-ot (Retrieved: 2026-08-10T14:00:00Z)
[11] SANS Institute. "SANS Institute Product Briefing: ICS/OT with Cyolo PRO (PDF)". https://cyolo.io/at-a-glance/sans-institute-product-briefing-cyolo-pro (Retrieved: 2026-08-10T14:00:00Z)
[12] Cyolo Docs. "Cyolo Documentation - Welcome to Cyolo". https://docs.cyolo.io/docs/overview (Retrieved: 2026-08-10T14:00:00Z)
[13] Cyolo Docs. "Cyolo Documentation - Core Components & Deployment Models". https://docs.cyolo.io/docs/overview-7.md (Retrieved: 2026-08-10T14:00:00Z)
[14] Cyolo Docs. "Cyolo Documentation - Asset and Network Traffic Visibility". https://docs.cyolo.io/docs/asset-and-network-traffic-visibility.md (Retrieved: 2026-08-10T14:00:00Z)
[15] Cyolo Docs. "Cyolo Documentation - Release Notes (7.0.x)". https://docs.cyolo.io/docs/release-notes-70.md (Retrieved: 2026-08-10T14:00:00Z)
[16] Cyolo Docs. "Cyolo Documentation - Prerequisites and Environment Check". https://docs.cyolo.io/docs/prerequisites-environment-check.md (Retrieved: 2026-08-10T14:00:00Z)
[17] Cyolo Docs. "Cyolo Documentation - Management Nodes". https://docs.cyolo.io/docs/management-nodes.md (Retrieved: 2026-08-10T14:00:00Z)
[18] Cyolo Docs. "Cyolo Documentation - Exporting Logs to Other Destinations". https://docs.cyolo.io/docs/exporting-logs-to-other-destinations.md (Retrieved: 2026-08-10T14:00:00Z)
[19] Cyolo Docs. "Cyolo Documentation - IDAC Offline Installation". https://docs.cyolo.io/docs/idac-offline-installation-1.md (Retrieved: 2026-08-10T14:00:00Z)
[20] Cyolo Docs. "Cyolo Documentation - Monitoring (Logging) Overview". https://docs.cyolo.io/docs/monitoring-logging-overview.md (Retrieved: 2026-08-10T14:00:00Z)
[21] Cyolo Docs. "Cyolo Documentation - Other Global Settings". https://docs.cyolo.io/docs/other-global-settings.md (Retrieved: 2026-08-10T14:00:00Z)
[22] Cyolo Docs. "Cyolo Documentation - How to Create API Keys". https://docs.cyolo.io/docs/how-to-create-api-keys.md (Retrieved: 2026-08-10T14:00:00Z)
[23] Cyolo Docs. "Cyolo Documentation - Commands Control". https://docs.cyolo.io/docs/command-control.md (Retrieved: 2026-08-10T14:00:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 23 (kept: 23, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 2, product_release_notes: 3, third_party_review: 1, vendor_datasheet: 1, vendor_doc: 16
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
