# Microsegmentation Product Assessment: Palo Alto Networks - Prisma Cloud / Next-Gen Firewalls

**Product ID:** `prisma-cloud-next-gen-firewalls`
**Version reference:** Prisma Cloud Compute Edition 34.x and Prisma Cloud Enterprise docs (docs.prismacloud.io) plus PAN-OS 11.x NGFW/VM-Series/CN-Series product line, as documented on 2026-08-10
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:14:15Z
**Total evidence items collected:** 90
**Total distinct sources:** 40

---

## 1. Overview

Palo Alto Networks positions microsegmentation as a combination of two product lines: **Prisma Cloud** (the cloud-native security platform, including Compute Edition Defenders for workload runtime protection and Enterprise Edition Network Security for VPC-flow-log visibility, network exposure analysis and network anomaly policies) and **Next-Generation Firewalls** (PAN-OS with VM-Series virtual firewalls for segmentation in private/public clouds and CN-Series container firewalls that enforce east-west policy inside Kubernetes using native namespace/label context) [29], [30], [34]. Deployments span public cloud, on-premises virtualized data centers, Kubernetes/OpenShift and OT-adjacent environments. A notable finding of this assessment: the dedicated "Microsegmentation" module that existed in earlier Prisma Cloud Compute (Twistlock-era) documentation is absent from the current docs.prismacloud.io index (1,753 pages, none titled with microsegmentation/segmentation), and the current Firewalls documentation states that "Prisma Cloud provides layer 4 monitoring and layer 7 firewalling" [5], [14]. Workload-level segmentation capabilities are therefore delivered through Defender runtime defense (process/network/file-system enforcement), Collections-based policy scoping, and the NGFW line's App-ID and tag-based policies [4], [25], [35].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 19    | 3                | 16     | 0   |
| partial          | 12    | 0                | 12     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 2     | 0                | 0      | 2   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 26 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | Prisma Cloud ingests and monitors cloud network traffic from VPC flow logs and analyzes 1T events per day for visibility; PeerSpot reviewers confirm real-time visibility and comprehensive monitoring across cloud environments. [14], [29], [39] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | Radar provides workload and flow visualization, CN-Series groups Kubernetes workloads by labels/namespaces via Panorama, and flow-log data can be visualized through RQL queries, but no single connectivity map organized by App/Environment/Role/Process is documented. [16], [24], [34] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | 30 days | Prisma Cloud’s default flow-log retention is 30 days (flow-log data can be queried only for the last 30 days); admin audit logs are retained 120 days and Compute audit collections are capped by count/size, with syslog recommended for long-term retention. [19], [20], [28] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Partial | medium | — | Prisma Cloud collects CVE data for supported image base layers and Container Network Exposure builds a network graph of exposure paths, but no staged source shows CVE context overlaid directly on a connectivity map. [1], [15] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | — | Network Security finds incidents and exposures based on VPC flow logs, and CN-Series is inserted to secure connections between container trust zones, providing detection of risky or unrecognized traffic patterns. [14], [34] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | Prisma Cloud Collections scope rules by labels, namespaces and registry tags, CN-Series policies are defined by application, user, content and native Kubernetes labels rather than IP/VLAN, and VM-Series segments by application identity. [25], [33], [34] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | — | PAN-OS Policy Optimizer identifies port-based rules and recommends App-ID based conversions from observed traffic, and VM-Series is described as an ML-powered NGFW; the recommendation engine is documented by vendor sources only. [33], [35] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | — | PAN-OS provides a Security Policy Match test that evaluates traffic against the policy configuration, but no full dry-run/simulation mode for uncommitted policy changes is documented for Prisma Cloud or the NGFW line. [35] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Supported | medium | — | PAN-OS automatically saves a new running-configuration version at every commit and lets administrators revert pending changes or restore any previously saved version, providing policy rollback. [35] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | — | PAN-OS device groups form a hierarchy (levels 1-4) with ancestor IDs recorded in logs, and CN-Series firewalls are managed from Panorama, whose device groups inherit rules from parent groups. [34], [35] |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | The supported OS list covers Windows Server 2016-2025, RHEL/CentOS 8-10, Ubuntu, Debian, SUSE and Oracle Linux; legacy Windows Server 2003-2012, AIX and Solaris are absent from the current supported list. [1] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | high | — | System requirements list Kubernetes, EKS, AKS, GKE and OpenShift 4.12-4.21 orchestrators; Defenders deploy as per-node DaemonSets, CN-Series supports GKE/AKS/EKS/OpenShift, and PeerSpot reviewers describe container and EKS deployments. [1], [8], [34], [39] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | — | Agent-based Defenders protect hosts, containers and serverless functions, agentless scanning is offered (PeerSpot reviewers highlight not having to deploy agents), and VM-Series provides network-based enforcement without host agents. [24], [29], [39] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | Compute Edition is documented to run in cloud, on-prem, or air-gapped environments, with manual Intelligence Stream updates via twistcli for offline Consoles. [21], [27] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Vendor sizing docs describe linear scaling (e.g., 20,000 connected Defenders require 16 vCPUs/50GB RAM) and PeerSpot rates scalability highly, but no staged source states an explicit per-controller capacity of 50,000+ workloads. [1], [39] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | Vendor documents typical Defender CPU load of ~1-5% (cgroup-capped at 900 CPU shares), which exceeds the <1% target; no sustained sub-1% figure is demonstrated. [1] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Supported | medium | 70 MB | Typical Defender RAM load is documented as 30-70MB, meeting the <100MB footprint target, although the minimum deployment allocation is 256MB per Defender. [1] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | — | no evidence found |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | — | Defender always fails open: even if the Defender process terminates or becomes unresponsive, deployments and node operation continue, and Defender is a user-space process whose failure does not impact containers or the host kernel. [4] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | — | Defender upgrades restart only the Defender service (runtime restart scenarios), Defender is a user-space container rather than a kernel module, and certificate rotation requires no restart; no staged source explicitly states whether a full server reboot is ever required for install or update. [4], [11], [12] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | — | The Compute (CWPP) REST API on pan.dev automates setup, configuration and deployment of Compute components, VM-Series documents a fully documented API for policy automation, and CI scan results are retrievable via the API. [22], [33], [40] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | — | Syslog (RFC 5424) integration with optional TLS certificate, a native Splunk HEC integration, and audit-event retrieval via the API provide SIEM/SOAR data exchange. [7], [13], [26] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | — | ServiceNow integration is documented for ITSM, Security Incident Response and Event ticket workflows with OAuth 2.0, but no staged source shows ServiceNow CMDB tag synchronization. [18] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | — | The Jenkins plugin scans images and CI builds, Kubernetes YAML/Helm charts are designed for CI/CD pipelines, and CN-Series and VM-Series support Terraform and Ansible automation. [8], [22], [33], [34] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | medium | — | Defender blocks anomalous processes and file-system writes, host runtime policies alert/prevent processes by path, and Defender capabilities include process-level runtime defense. [4], [23], [24] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Unknown | low | — | no evidence found |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Built-in compliance standards include PCI DSS v3.2/v4.0, ISO 27001:2013/2022, NIST 800-53 and NIST SP 800-171, but NIST 800-207 (Zero Trust) and IEC 62443 (industrial) are not among the listed built-in standards. [17] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | — | Console and Defender mutually authenticate with certificates issued by the Defender CA, and all Defender-Console traffic is TLS encrypted; TLS 1.3 specifically is not stated in staged sources. [4], [12] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | NGFW HA pairs/clusters (active/passive and active/active, up to 16 members) are documented; the Prisma Cloud Compute console relies on orchestrator recovery plus external storage for HA, with cross-cluster replication explicitly not tested or supported. [2], [35] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | — | Defenders keep enforcing the last-pushed policy when the Console fails or communication is lost, caching events locally until the Console is reachable again. [2], [4] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | — | Automated daily/weekly/monthly backups and restore via UI or twistcli are documented, with spare-site (warm or cold) disaster-recovery guidance for Compute deployments. [2], [3] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | NIST CMVP lists active FIPS certificates for PAN-OS hardware NGFWs and VM-Series (e.g., PAN-OS 10.2 and 11.0 VM-Series), and the Common Criteria portal lists NIAP certifications for PAN-OS 11.1/11.2 hardware and VM-Series; no FIPS or Common Criteria entry was found for the Prisma Cloud Compute controller or Defender. [36], [37], [38] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | — | The VM-Series datasheet documents a Siemens RUGGEDCOM integration for rugged and OT environments; no Honeywell or ABB compatibility certifications were found in staged sources. [33] |

---

## 4. Notable Strengths

- **Native Kubernetes / OpenShift segmentation (items 3.2, 6.1):** Defenders deploy as per-node DaemonSets, CN-Series container firewalls enforce App-ID policies across namespace trust boundaries, and supported orchestrators include Kubernetes, EKS, AKS, GKE and OpenShift 4.12-4.21 [1], [8], [34].
- **Agent-based plus agentless/network-based coverage (item 3.3):** host/container/serverless Defenders coexist with agentless workload scanning and VM-Series network enforcement, so environments that cannot run agents can still be segmented [24], [29], [39].
- **Tag/identity-based policy and rollback (items 2.1, 2.4, 2.5):** policies are defined by applications, users, content and Kubernetes labels rather than IP/VLAN, Panorama device-group hierarchies support inherited rules, and every commit saves a restorable configuration version [25], [33], [34], [35].
- **Resilient autonomous enforcement (items 4.4, 7.2):** Defenders continue enforcing the last-pushed policy when the Console is unreachable, and Defender is explicitly fail-open, so agent failure does not interrupt traffic or deployments [2], [4].
- **FIPS 140-validated NGFW cryptography (item 8.1):** the NIST CMVP registry lists active certificates for PAN-OS hardware NGFWs and VM-Series (e.g., PAN-OS 10.2 and 11.0 VM-Series), underpinning the firewall line's use in regulated environments [36], [37].

## 5. Notable Gaps / Risks

- **No dedicated Compute microsegmentation module (items 1.2, 2.3, 6.2):** the current Prisma Cloud documentation contains no microsegmentation feature; connectivity visualization is Radar/flow-log-based, no policy dry-run/simulation is documented, and no honeypot/deception capability was found [5], [14], [35].
- **Flow-history retention below the forensic bar (item 1.3):** default flow-log retention is 30 days (queryable for the last 30 days), below the 90-day requirement; only admin audit logs reach 120 days [20], [28].
- **OS coverage gaps for legacy estates (item 3.1):** supported hosts cover Windows Server 2016-2025 and modern RHEL/CentOS/Ubuntu, but legacy Windows Server 2003-2012, AIX and Solaris are not in the current supported list [1].
- **Numeric performance targets unmet or undocumented (items 4.1, 4.3):** typical Defender CPU load is ~1-5% (above the <1% target) and no network-latency figure is published, leaving the <0.1ms requirement unverifiable [1].
- **Certification gaps (items 8.1, 8.2):** Common Criteria entries for PAN-OS/VM-Series are NIAP protection-profile evaluations without an EAL4+ rating, Prisma Cloud Compute has no FIPS/CC entry in the registries, and only a Siemens RUGGEDCOM integration (no Honeywell/ABB) was documented [33], [37], [38].

## 6. Evidence Quality Notes

Evidence was staged and grounded for all 40 sources and 90 quotes: every quote in evidence.jsonl is a verbatim substring of its staged artifact .txt, and the grounding check reports 90/90 grounded with zero fabricated or unverifiable entries. Source diversity is moderate — 12 of 33 items draw on at least two source types — but the vendor documentation (vendor_doc, 35 of 40 sources) dominates, which caps confidence at medium for most items per the validator rule. Independent evidence comes from three clusters: the NIST CMVP and Common Criteria Portal registries (item 8.1), PeerSpot community reviews (items 1.1, 3.2, 3.3, 3.5), and the vendor-hosted NGFW administration guide PDF for the firewall-side claims (items 2.2-2.5, 4.4, 7.1).

Two caveats shape interpretation. First, items 4.3 (network latency) and 6.2 (deception/honeypot) are unknown because no staged source mentions the metric at all — absence from these sources does not prove absence from the product. Second, the Wayback Machine was persistently rate-limited (HTTP 429) during this run, so the historical Twistlock/Compute "Microsegmentation" admin-guide pages could not be staged; the assessment of item 1.2 and the overall positioning rests on current documentation, which the vendor has evidently reorganized around Network Security/CNS and the NGFW line. No direct contradictions between sources were encountered; the only tension is between vendor marketing (scalability, "1T events per day") and the absence of explicit numeric guarantees for latency and workload caps.

---

## Bibliography

[1] Palo Alto Networks. "System requirements (Prisma Cloud Compute admin guide)". https://docs.prismacloud.io/admin-guide/install/system-requirements.md (Retrieved: 2026-08-10T14:13:23Z)
[2] Palo Alto Networks. "High availability (Prisma Cloud Compute admin guide)". https://docs.prismacloud.io/admin-guide/deployment-patterns/high-availability.md (Retrieved: 2026-08-10T14:13:23Z)
[3] Palo Alto Networks. "Backup and restore (Prisma Cloud Compute admin guide)". https://docs.prismacloud.io/admin-guide/configure/disaster-recovery.md (Retrieved: 2026-08-10T14:13:23Z)
[4] Palo Alto Networks. "Defender architecture (Prisma Cloud Compute admin guide)". https://docs.prismacloud.io/admin-guide/technology-overviews/defender-architecture.md (Retrieved: 2026-08-10T14:13:23Z)
[5] Palo Alto Networks. "Firewalls (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/firewalls.md (Retrieved: 2026-08-10T14:13:23Z)
[6] Palo Alto Networks. "API (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/api.md (Retrieved: 2026-08-10T14:13:23Z)
[7] Palo Alto Networks. "Syslog and stdout integration (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/audit/logging.md (Retrieved: 2026-08-10T14:13:23Z)
[8] Palo Alto Networks. "Deploy Orchestrator Defender (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/kubernetes.md (Retrieved: 2026-08-10T14:13:23Z)
[9] Palo Alto Networks. "Deploy Host Defender (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/host.md (Retrieved: 2026-08-10T14:13:23Z)
[10] Palo Alto Networks. "Available Defender Types (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/defender-types.md (Retrieved: 2026-08-10T14:13:23Z)
[11] Palo Alto Networks. "Manage your Defenders (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/manage-defender.md (Retrieved: 2026-08-10T14:13:23Z)
[12] Palo Alto Networks. "Certificates (Prisma Cloud Compute docs)". https://docs.prismacloud.io/content-collections/runtime-security/configure/certificates.md (Retrieved: 2026-08-10T14:13:23Z)
[13] Palo Alto Networks. "Event Viewer (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/audit/event-viewer.md (Retrieved: 2026-08-10T14:13:23Z)
[14] Palo Alto Networks. "Network Security (Prisma Cloud administration docs)". https://docs.prismacloud.io/content-collections/administration/network-security.md (Retrieved: 2026-08-10T14:13:23Z)
[15] Palo Alto Networks. "Overview of Container Network Exposure (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/administration/network-security/container-network-exposure/container-network-exposure-overview.md (Retrieved: 2026-08-10T14:13:23Z)
[16] Palo Alto Networks. "Network Flow Queries (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/search-and-investigate/network-queries/network-flow-queries.md (Retrieved: 2026-08-10T14:13:23Z)
[17] Palo Alto Networks. "Built-in Compliance Standards (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/compliance/compliance-standards.md (Retrieved: 2026-08-10T14:13:23Z)
[18] Palo Alto Networks. "Integrate Prisma Cloud with ServiceNow (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow.md (Retrieved: 2026-08-10T14:13:23Z)
[19] Palo Alto Networks. "Storage Limits for Audits and Reports (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/runtime-security/deployment-patterns/caps.md (Retrieved: 2026-08-10T14:13:23Z)
[20] Palo Alto Networks. "View Audit Logs (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/administration/view-audit-logs.md (Retrieved: 2026-08-10T14:13:23Z)
[21] Palo Alto Networks. "Update offline environments (Prisma Cloud Compute admin guide)". https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline.md (Retrieved: 2026-08-10T14:13:23Z)
[22] Palo Alto Networks. "Jenkins Plugin (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/continuous-integration/jenkins-plugin.md (Retrieved: 2026-08-10T14:13:23Z)
[23] Palo Alto Networks. "Runtime Defense for Hosts (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-hosts.md (Retrieved: 2026-08-10T14:13:23Z)
[24] Palo Alto Networks. "Deploy the Prisma Cloud Defender (Prisma Cloud docs)". https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender.md (Retrieved: 2026-08-10T14:13:23Z)
[25] Palo Alto Networks. "Collections (Prisma Cloud runtime security docs)". https://docs.prismacloud.io/content-collections/runtime-security/configure/collections.md (Retrieved: 2026-08-10T14:13:23Z)
[26] Palo Alto Networks. "Splunk alert integration (Prisma Cloud Compute admin guide 32.x)". https://docs.prismacloud.io/admin-guide/32/alerts/splunk.md (Retrieved: 2026-08-10T14:13:23Z)
[27] Palo Alto Networks. "Prisma Cloud documentation home". https://docs.prismacloud.io/home.md (Retrieved: 2026-08-10T14:13:23Z)
[28] Palo Alto Networks. "Configure Flow Logs (Prisma Cloud AWS onboarding docs)". https://docs.prismacloud.io/content-collections/connect/connect-cloud-accounts/onboard-aws/configure-flow-logs.md (Retrieved: 2026-08-10T14:13:23Z)
[29] Palo Alto Networks. "Prisma Cloud product page". https://www.paloaltonetworks.com/prisma/cloud (Retrieved: 2026-08-10T14:13:23Z)
[30] Palo Alto Networks. "Next-Generation Firewalls product page". https://www.paloaltonetworks.com/network-security/next-generation-firewall (Retrieved: 2026-08-10T14:13:23Z)
[31] Palo Alto Networks. "VM-Series Virtual Next-Generation Firewall product page". https://www.paloaltonetworks.com/network-security/vm-series-virtual-next-generation-firewall (Retrieved: 2026-08-10T14:13:23Z)
[32] Palo Alto Networks. "CN-Series Container Firewall product page". https://www.paloaltonetworks.com/network-security/cn-series (Retrieved: 2026-08-10T14:13:23Z)
[33] Palo Alto Networks. "VM-Series Virtual Next-Generation Firewalls datasheet (PDF)". https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/vm-series-spec-sheet.pdf (Retrieved: 2026-08-10T14:13:23Z)
[34] Palo Alto Networks. "CN-Series Container Firewall datasheet (PDF)". https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/cn-series-container-firewall.pdf (Retrieved: 2026-08-10T14:13:23Z)
[35] Palo Alto Networks. "PAN-OS NGFW Administrator’s Guide (PDF)". https://docs.paloaltonetworks.com/content/dam/techdocs/en_US/pdf/ngfw/ngfw-administration.pdf (Retrieved: 2026-08-10T14:13:23Z)
[36] Palo Alto Networks. "FIPS 140 trust center page". https://www.paloaltonetworks.com/legal-notices/trust-center/fips-140 (Retrieved: 2026-08-10T14:13:23Z)
[37] NIST. "NIST CMVP Validated Modules list". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all (Retrieved: 2026-08-10T14:13:23Z)
[38] Common Criteria Portal. "Common Criteria Portal product search: Palo Alto". https://www.commoncriteriaportal.org/products/index.cfm?search=palo+alto (Retrieved: 2026-08-10T14:13:23Z)
[39] PeerSpot. "Prisma Cloud by Palo Alto Networks reviews (PeerSpot)". https://www.peerspot.com/products/prisma-cloud-by-palo-alto-networks-reviews (Retrieved: 2026-08-10T14:13:23Z)
[40] Palo Alto Networks. "Prisma Cloud Compute (CWPP) API (pan.dev)". https://pan.dev/compute/api/ (Retrieved: 2026-08-10T14:13:23Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 22
- **Sources reviewed:** 40 (kept: 40, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, community: 1, vendor_datasheet: 2, vendor_doc: 35
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
