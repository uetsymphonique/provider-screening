# Microsegmentation Product Assessment: ColorTokens - ColorTokens Xshield

**Product ID:** `colortokens-xshield`
**Version reference:** Xshield Enterprise Microsegmentation Platform (2026 data sheet; Spectrum cloud console; agent 8.x); staged evidence spans a 2019 solution brief through 2026 materials
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T08:48:01Z
**Total evidence items collected:** 102
**Total distinct sources:** 45

---

## 1. Overview

ColorTokens Xshield is the vendor's enterprise microsegmentation platform, delivered as a cloud (SaaS) console on the Spectrum platform with an optional on-premises ColorMaster controller [18]. Xshield positions itself around "breach readiness": stopping the lateral spread of malware and ransomware by placing a micro-perimeter around each asset, then progressing from enterprise-wide high-risk-port controls to fine-grained application-specific zero-trust policies [1][50]. It covers data-center servers and VMs, cloud workloads (AWS, Azure, GCP), Kubernetes containers, user endpoints, and OT/IoT/legacy devices through three documented enforcement shapes: agent-based (Xshield agent or existing EDR agents such as CrowdStrike and SentinelOne), agentless via the Xshield Gatekeeper appliance for OT/IoT/legacy systems, and native controls such as AWS security groups, Azure NSGs, and Kubernetes service-mesh sidecars (Istio Envoy, Ambient Mesh, OpenShift OPA) [50]. Visibility and policy automation are the flagship capabilities: real-time traffic mapping, tag/role-based policies, AI-assisted policy recommendation and simulation-before-enforcement [6][8][52]. Named a Leader in the Forrester Wave Microsegmentation Solutions Q3 2024 and the 2026 GigaOm Radar, the product carries FedRAMP Moderate, IRAP PROTECTED, SOC 2 Type II, ISO/IEC 27001 and TX-RAMP credentials, but no FIPS 140 or Common Criteria certification was found [14][15][57][58].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 17    | 8                | 9      | 0   |
| partial          | 12    | 0                | 12     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 23 items backed by ≥ 2 source_types; 16 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | Xshield continuously maps assets and east-west/north-south traffic through its Visualizer, Flow Explorer and cloud connectors; the data sheet, real-time-visibility blog and SiliconANGLE coverage corroborate real-time visibility across IT, OT, cloud and legacy environments. [8], [18], [48], [51], [54] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Supported | medium | - | The Visualizer renders a group topology and assets can be analyzed along 20+ dimensions including application, environment, role and location; tags and role-based Security Policy Templates provide App/Environment/Role views, though a dedicated process-level map pivot is not explicitly documented. [34], [43], [44], [50], [52] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 365 days | The Secure Cloud status dashboard aggregates connection statistics over windows up to 365 days, and policy-impact simulation runs over historical traffic spanning days, weeks, months or years; no hard retention limit is published. [7], [27], [47] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Supported | medium | - | The built-in CT vulnerability scanner lists CVEs (referenced from NVD) on asset fly panels and the AI agent can interrogate assets for CVE exposure; presentation is via asset fly panels and AI queries rather than directly on the network map. [6], [30], [38] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | - | Xshield flags unexpected, unauthorized or blocked flows as distinct session states and surfaces unauthorized paths in the Visualizer; the ATARC lab narrative documents XShield surfacing a live unauthorized OT-to-IT flow. [8], [18], [19] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | - | Policies are defined against tags/labels (Application, Role, Environment, Service) and workload identity rather than IPs; ATARC documents policies written against tag groups, and the cloud blog states policies are anchored to workload identity and metadata tags. [12], [19], [34], [44] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | high | - | Policy Builder generates recommendations from observed traffic and the Xshield AI Agent (2026) automates policy discovery and rule synthesis; SiliconANGLE reports policy design and rollout accelerating from days to minutes. [1], [6], [32], [54] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Supported | high | - | Simulation on historical data before enforcement is documented in the data sheet, product page, ATARC demo narrative and Global Security Mag coverage; policies first run in simulate/observe mode before enforcement. [1], [19], [48], [52] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | One-click quarantine/unquarantine and Breach Response Levels restore the prior policy state in seconds, and policy tampering is auto-reverted; no explicit 'undo last policy edit' rollback control is documented. [9], [29], [45] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | Security and Corporate Policy Templates propagate edits to all Workload groups that use them, and CPT changes auto-update group policies; template-based inheritance is documented, though explicit parent-child rule hierarchies are not described. [1], [33], [34] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | The Xshield agent supports Windows Server 2003-2019 (64-bit), RHEL/CentOS/Ubuntu/SUSE and AIX 7.1 workloads; AIX/HP-UX/legacy/mainframe assets are protected agentlessly via the Gatekeeper appliance, but Solaris and Windows Server 2022 are not documented. [11], [28], [50] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | high | - | Kubernetes communications are controlled at the API layer via service-mesh sidecars (Istio Envoy, Ambient Mesh, OpenShift OPA); the container tech brief and AWS Marketplace document per-Kubernetes-service sidecar enforcement. [1], [21], [49], [50], [52] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | - | Enforcement is offered agent-based (Xshield agent or existing EDR agents), agentless (Gatekeeper appliance for OT/IoT/legacy) and via native cloud controls (AWS security groups, Azure NSGs); the OT page and Global Security Mag confirm both agent and agentless paths. [5], [13], [50], [52] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | - | no evidence found (No documentation found on fully air-gapped operation; agent prerequisites require outbound HTTPS 443 to the Xshield instance, so offline deployment is unverified.) |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Supported | medium | 100000 workloads | Vendor materials state policy-impact simulation scales to networks of 100,000+ assets and cite a top-50 service provider customer segmenting hundreds of thousands of servers; each Gatekeeper HA pair covers up to 1,000 agentless devices. [7], [21] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | The 2019 solution brief claims the agent consumes less than 1% CPU, but 2021-22 admin documentation states CPU can momentarily rise up to 50% during enforcement on resource-constrained agents; the sub-1% figure is therefore not reliably demonstrated. [18], [29] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Supported | medium | 30 MB | The solution brief states the agent consumes 30 MB of RAM and describes it as an ultra-lightweight, small-footprint agent; no newer memory figure contradicts this. [18], [41] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | - | no evidence found (No source quantifies network latency added by enforcement.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | Enforcement is implemented in the host OS native firewall, and docs describe the agent recovering from an unexpected stop/crash using the existing native-firewall rules snapshot; no explicit fail-open/fail-closed statement for a prolonged agent outage is published. [29] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | - | Install/upgrade docs describe UI, CLI and at-scale (Ansible/GPO) procedures with no reboot step, and the vendor positions deployment as non-disruptive; no source explicitly confirms reboot-free operation. [1], [16], [42] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | - | A public API docs portal (api-bom.colortokens.com) documents the Xshield REST API v1 with token authentication, and D3's SOAR integration guide consumes endpoints for assets, tags and policies; the integrations page cites an open API for ad-hoc integrations. [3], [22], [23] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | - | SIEM integration is documented via syslog (Splunk, Sumo Logic, Kiwi Syslog) in RFC 5424, REST-based telemetry to Splunk/Sentinel/QRadar, and D3 documents a SOAR integration; the syslog doc notes one syslog destination at a time is supported. [3], [22], [35] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | - | The integrations page documents ServiceNow CMDB integration for dynamic policy mapping and enforcement based on real-time asset configurations. [3] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | - | Agent operations can be automated via Ansible/GPO, the native AWS/Azure cloud connector syncs via provider APIs, and CI/CD runners are listed among protected ephemeral workloads; no Jenkins/GitLab/Terraform-specific integration is documented. [12], [42] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | Alerts and syslog events include process context and visibility docs describe per-workload process insight, but enforcement is documented at host-firewall port/protocol and API level rather than explicitly process-level. [10], [35] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | Threat-intelligence integration (reputation scoring, MITRE ATT&CK TTPs and CISA advisories via the AI agent) is documented; no deception/honeypot capability was found. [1], [6], [54] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | The OT page cites NERC CIP, IEC 62443 and ISO/IEC 27001 compliance support, FedRAMP Moderate is based on NIST SP 800-53, and PCI-DSS compliance is addressed in vendor guidance; NIST 800-207 is not explicitly cited. [5], [15], [57], [59] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | - | Agent-to-controller communication uses mutual TLS (mTLS, TLS 1.2) over HTTPS 443 as documented in agent prerequisite and release-notes articles; TLS 1.3 is not explicitly documented. [28], [29], [46] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | - | The SaaS console runs in an AWS cluster with a core-services status dashboard, Gatekeeper appliances support HA pairs, and web-proxy HA is documented via a 2-node Pacemaker cluster; an explicit active-active/active-passive controller-cluster spec is not published. [21], [27], [36] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Partial | medium | - | Enforcement lives in the host OS firewall so rules persist independently, and agents cache telemetry (up to 10 MB) and fail over when the controller or Agent Proxy is unreachable; no explicit statement describes prolonged autonomous enforcement during total controller loss. [29], [46] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | - | no evidence found (No documentation found on disaster-recovery site sync or backup/restore of the controller.) |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | - | The NIST CMVP validated-modules registry contains no ColorTokens module (FIPS 140-2/140-3 not found), and the vendor certifications page lists SOC 2 Type II, ISO/IEC 27001, TX-RAMP, FedRAMP Moderate and IRAP but no FIPS or Common Criteria certification. [14], [15], [58] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | No compatibility certifications from Siemens, Honeywell or ABB were found; the ATARC Zero Trust OT Lab narrative documents XShield interoperating with Siemens WinCC SCADA and Rockwell PLCs in a joint Armis+XShield demo. [19] |

---

## 4. Notable Strengths

- **Real-time visibility and unrecognized-traffic detection (items 1.1, 1.5):** Xshield maps active east-west and north-south traffic continuously and highlights unexpected pathways such as unauthorized RDP/SSH, unused SMB, or risky OT-to-IT flows; the ATARC lab narrative independently documents XShield surfacing a live unauthorized cross-boundary flow [8][19].
- **Tag/identity-based policy with AI-assisted workflows (items 2.1, 2.2, 2.3):** Policies are anchored to tags, roles and workload identity rather than IPs, Policy Builder recommends rules from observed traffic, the 2026 Xshield AI Agent automates rule synthesis, and policies are simulated on historical data before enforcement [6][12][34][54].
- **Multi-shape enforcement coverage (items 3.2, 3.3):** A single console drives host-firewall agents, the agentless Gatekeeper appliance for OT/IoT/legacy systems, Kubernetes API-layer sidecars, and native cloud controls, so no asset class is left to a single enforcement mechanism [50][52].
- **SIEM/SOAR and CMDB integration depth (items 5.2, 5.3):** Syslog (Splunk, Sumo Logic, Kiwi) in RFC 5424, REST-based telemetry to Splunk/Sentinel/QRadar, a documented D3 SOAR integration, and ServiceNow CMDB synchronization are documented [3][22][35].
- **Security posture of the agent channel (item 6.4):** Agent-to-controller communication uses mutual TLS (mTLS, TLS 1.2) over HTTPS 443, and the platform carries FedRAMP Moderate plus IRAP PROTECTED assessments (items 8.1 context) [28][29][46][57].

## 5. Notable Gaps / Risks

- **No FIPS 140 or Common Criteria certification (item 8.1):** The NIST CMVP registry contains no ColorTokens module and the vendor certifications page lists SOC 2, ISO 27001, TX-RAMP, FedRAMP Moderate and IRAP but no FIPS/Common Criteria - a blocker for environments that mandate FIPS-validated cryptography [14][58].
- **Agent resource figures conflict (items 4.1, 4.2):** The 2019 brief claims "less than 1% CPU and 30 MB of RAM," but 2021-22 admin docs state CPU can momentarily spike up to 50% during enforcement on low-resource agents; the sub-1% claim is not reliable, and no independent benchmark exists [18][29].
- **Unverified operational claims (items 3.4, 4.3, 7.3):** Air-gapped operation, added network latency, and disaster-recovery site sync are not documented anywhere; agent prerequisites require outbound HTTPS 443 to the Xshield instance, so fully offline deployments are unproven [28].
- **Partial policy-rollback semantics (item 2.4):** One-click quarantine/unquarantine and Breach Response Levels restore prior policy state, and tampering is auto-reverted, but a generic "undo last policy edit" rollback control is not documented [9][45].
- **Process-level enforcement unconfirmed (item 6.1):** Process context appears in alerts and logs, but enforcement is documented at host-firewall port/protocol and API level, not explicitly per-process [35].
- **OT compatibility without formal certifications (item 8.2):** ATARC lab interop with Siemens WinCC and Rockwell PLCs is documented, but no compatibility certifications from Siemens, Honeywell or ABB were found [19].

## 6. Evidence Quality Notes

Evidence was staged from 45 distinct sources (102 grounded quotes): 33 vendor pages/blogs/docs, 5 vendor PDFs (solution briefs, technical brief, 2026 data sheet), 2 marketplace listings, the NIST CMVP registry, and 5 independent third-party sources (ATARC demo narrative, D3 SOAR integration guide, SiliconANGLE, Global Security Mag, rfp.wiki). 23 items are backed by at least 2 source types; 8 items reached high confidence, each with at least one non-vendor source (e.g., ATARC for items 1.5/2.1/2.3/3.2/3.3, SiliconANGLE for 1.1/2.2). Sixteen items rest on vendor documentation only and are therefore capped at medium confidence.

Two items have genuinely contradictory or thin vendor evidence that drove conservative verdicts. Item 4.1 (agent CPU) is marked partial because the 2019 solution brief claims "less than 1% CPU" while the 2021-22 admin documentation warns of momentary spikes up to 50% during enforcement on low-resource agents; the newer, more specific documentation was treated as the tie-breaker. Item 8.1 is marked not supported because the NIST CMVP validated-modules search (vendor=ColorTokens) returned no module - absence in the authoritative registry, corroborated by the vendor's own certifications page which lists no FIPS or Common Criteria entry, was treated as sufficient for a negative verdict (per the project's precedent). Numeric items 1.3 (365-day aggregation window), 3.5 (100,000+ assets), and 4.2 (30 MB RAM) use the most specific figures found; none were independently measured. Items 3.4, 4.3, and 7.3 are unknown - searches for air-gapped deployment, latency figures, and disaster-recovery documentation produced no evidence, and no verdict was invented from silence.

---

## Bibliography

[1] ColorTokens. "Xshield: Enterprise Microsegmentation Platform (product page)". https://www.colortokens.com/xshield/ (Retrieved: 2026-08-10T08:45:00Z)
[3] ColorTokens. "Integrations - ColorTokens". https://colortokens.com/integrations/ (Retrieved: 2026-08-10T08:45:00Z)
[5] ColorTokens. "OT Security with Microsegmentation (solution page)". https://colortokens.com/ot-security-microsegmentation/ (Retrieved: 2026-08-10T08:45:00Z)
[6] ColorTokens. "Xshield AI Agent: AI-Assisted Microsegmentation". https://colortokens.com/ai-assisted-microsegmentation/ (Retrieved: 2026-08-10T08:45:00Z)
[7] ColorTokens. "Infinite Microsegmentation Policy Impact Simulation (blog)". https://colortokens.com/blogs/microsegmentation-policy-simulation/ (Retrieved: 2026-08-10T08:45:00Z)
[8] ColorTokens. "Real-Time Traffic Visibility for Faster and More Secure Microsegmentation (blog)". https://colortokens.com/blogs/real-time-traffic-visibility-zero-trust-microsegmentation/ (Retrieved: 2026-08-10T08:45:00Z)
[9] ColorTokens. "Be Breach Ready: How ColorTokens Xshield Stops Cyber Threats Before They Spread (blog)". https://colortokens.com/blogs/cve-xshield-microsegmentation/ (Retrieved: 2026-08-10T08:45:00Z)
[10] ColorTokens. "3 Approaches to Microsegmentation and Their Pros and Cons (blog)". https://colortokens.com/blogs/approaches-micro-segmentation-pros-and-cons/ (Retrieved: 2026-08-10T08:45:00Z)
[11] ColorTokens. "Breach Readiness In A Legacy World (blog)". https://colortokens.com/blogs/legacy-systems-breach-readiness/ (Retrieved: 2026-08-10T08:45:00Z)
[12] ColorTokens. "Securing Today's Cloud-Native Workloads (blog)". https://colortokens.com/blogs/cloud-native-microsegmentation-aws-azure/ (Retrieved: 2026-08-10T08:45:00Z)
[13] ColorTokens. "Insights from Fal.Con 2025 Interview: Frictionless Microsegmentation with CrowdStrike and ColorTokens (blog)". https://colortokens.com/blogs/frictionless-microsegmentation-crowdstrike-falcon-integration/ (Retrieved: 2026-08-10T08:45:00Z)
[14] ColorTokens. "Analyst Mentions, Awards, and Certifications". https://colortokens.com/analyst-mentions-certifications-awards/ (Retrieved: 2026-08-10T08:45:00Z)
[15] ColorTokens. "ColorTokens Achieves FedRAMP Moderate ATO for Xshield (blog)". https://colortokens.com/blogs/fedramp-moderate-ato-xshield-microsegmentation/ (Retrieved: 2026-08-10T08:45:00Z)
[16] ColorTokens. "Livi Bank Secures IT Operations with ColorTokens Xshield (case study)". https://colortokens.com/case-studies/livi-bank-it-security-xshield-microsegmentation/ (Retrieved: 2026-08-10T08:45:00Z)
[18] ColorTokens. "ColorTokens Xshield for Visibility and Cloud Workload Protection (solution brief PDF)". https://kidan.com/wp-content/uploads/2026/06/ColorTokens-Solution-Brief-Xshield.pdf (Retrieved: 2026-08-10T08:45:00Z)
[19] ATARC. "Armis Centrix + ColorTokens XShield: ATARC Zero Trust OT Lab Demo Narrative (PDF)". https://atarc.org/wp-content/uploads/2026/04/xshield_atarc_demo_narrative.pdf (Retrieved: 2026-08-10T08:45:00Z)
[21] AWS Marketplace (ColorTokens listing). "ColorTokens Xshield Enterprise Microsegmentation Platform | AWS Marketplace". https://aws.amazon.com/marketplace/pp/prodview-dd4ze4gewomem (Retrieved: 2026-08-10T08:45:00Z)
[22] D3 Security. "Colortokens Xshield | D3 Docs (SOAR integration guide)". https://docs.d3security.com/integration-docs/morpheus-integrations/colortokens-xshield (Retrieved: 2026-08-10T08:45:00Z)
[23] ColorTokens. "ColorTokens Xshield API Docs". https://api-bom.colortokens.com/ (Retrieved: 2026-08-10T08:45:00Z)
[27] ColorTokens. "Monitor ColorTokens Secure Cloud status - Spectrum Help Center". https://docs.colortokens.com/article/585-monitor-colortokens-secure-cloud-status (Retrieved: 2026-08-10T08:45:00Z)
[28] ColorTokens. "Supported OSes and prerequisites - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/170-xshield-agent-supported-oses-and-prerequisites (Retrieved: 2026-08-10T08:45:00Z)
[29] ColorTokens. "Expected behavior with Xshield agents - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/559-expected-behavior-with-xshield-agents (Retrieved: 2026-08-10T08:45:00Z)
[30] ColorTokens. "Expected behaviour - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/253-xshield-expected-behaviour (Retrieved: 2026-08-10T08:45:00Z)
[32] ColorTokens. "Use Policy Builder to create policies - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/373-use-policy-builder-to-create-policies (Retrieved: 2026-08-10T08:45:00Z)
[33] ColorTokens. "Corporate policy templates - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/36-corporate-policy-templates (Retrieved: 2026-08-10T08:45:00Z)
[34] ColorTokens. "Security policy templates - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/38-security-policy-templates (Retrieved: 2026-08-10T08:45:00Z)
[35] ColorTokens. "Integrate third-party Syslog tools - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/77-integrate-third-party-syslog-tools (Retrieved: 2026-08-10T08:45:00Z)
[36] ColorTokens. "HA for Squid Proxy with Pacemaker, Fencing, and Floating IP address - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/473-ha-for-squid-proxy-with-pacemaker-fencing-and-floating-ip-address (Retrieved: 2026-08-10T08:45:00Z)
[38] ColorTokens. "Known Issues - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/247-xshield-known-issues (Retrieved: 2026-08-10T08:45:00Z)
[41] ColorTokens. "Download Xshield agent - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/161-download-agent (Retrieved: 2026-08-10T08:45:00Z)
[42] ColorTokens. "Upgrade agents - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/178-upgrade-agent (Retrieved: 2026-08-10T08:45:00Z)
[43] ColorTokens. "Visualizer - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/602-visualizer (Retrieved: 2026-08-10T08:45:00Z)
[44] ColorTokens. "Tag assets - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/39-tag-asset (Retrieved: 2026-08-10T08:45:00Z)
[45] ColorTokens. "Quarantine templates - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/239-quarantine-templates (Retrieved: 2026-08-10T08:45:00Z)
[46] ColorTokens. "April 2020 (release notes) - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/248-xshield-new-features-april2020 (Retrieved: 2026-08-10T08:45:00Z)
[47] ColorTokens. "Interpret traffic flows downloaded from Flow Explorer - XSHIELD HELP CENTER". https://docs.xshield.colortokens.com/article/345-interpret-traffic-flows-downloaded-from-flow-explorer (Retrieved: 2026-08-10T08:45:00Z)
[48] ColorTokens. "Xshield Enterprise Microsegmentation Platform solution brief (PDF)". https://colortokens.com/wp-content/uploads/ColorTokens_Xshield-Solution_Brief.pdf (Retrieved: 2026-08-10T08:45:00Z)
[49] ColorTokens. "How to Secure Containerized Applications technical brief (PDF)". https://colortokens.com/wp-content/uploads/CT_Secure_Containerized_Applications_TechBrief.pdf (Retrieved: 2026-08-10T08:45:00Z)
[50] ColorTokens. "Xshield Enterprise Microsegmentation Platform data sheet (PDF)". https://colortokens.com/wp-content/uploads/ColorTokens-Xshield-Data-Sheet-26.pdf (Retrieved: 2026-08-10T08:45:00Z)
[51] rfp.wiki. "ColorTokens Xshield - Strengths, Gaps & Best Fit | rfp.wiki". https://www.rfp.wiki/cloud-computing/cloud-security-posture-management/cloud-network-security/colortokens-xshield (Retrieved: 2026-08-10T08:45:00Z)
[52] Global Security Mag. "ColorTokens, Inc. unveiled significant upgrades to Xshield (Global Security Mag)". https://www.globalsecuritymag.com/colortokens-inc-unveiled-significant-upgrades-to-xshield-tm.html (Retrieved: 2026-08-10T08:45:00Z)
[54] SiliconANGLE. "ColorTokens launches Xshield AI Agent to automate microsegmentation policy enforcement (SiliconANGLE)". https://siliconangle.com/2026/03/10/colortokens-launches-xshield-ai-agent-automate-microsegmentation-policy-enforcement/ (Retrieved: 2026-08-10T08:45:00Z)
[57] ColorTokens. "Colortokens Completes IRAP PROTECTED in Australia (news)". https://colortokens.com/news/irap-protected-assessment-australia/ (Retrieved: 2026-08-10T08:45:00Z)
[58] NIST CSRC. "NIST CMVP Validated Modules search (vendor=ColorTokens)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?Form.SearchMode=Advanced&Form.Vendor=ColorTokens&ipp=25&sortBy=relevance (Retrieved: 2026-08-10T08:45:00Z)
[59] ColorTokens. "Simplifying PCI-DSS Compliance with Microsegmentation (blog)". https://colortokens.com/blogs/simplifying-pci-dss-compliance-microsegmentation/ (Retrieved: 2026-08-10T08:45:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 26
- **Sources reviewed:** 45 (kept: 45, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 1, certification_registry: 1, third_party_review: 5, vendor_blog: 10, vendor_datasheet: 5, vendor_doc: 23
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
