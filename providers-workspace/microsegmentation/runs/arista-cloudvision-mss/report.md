# Microsegmentation Product Assessment: Arista Networks - Arista CloudVision MSS (Multi-Domain Segmentation Service)

**Product ID:** `arista-cloudvision-mss`
**Version reference:** Arista MSS (formerly Macro-Segmentation Service; branded Multi-Domain Segmentation Services, MSS, as of the April 2024 launch; runs on Arista CloudVision / EOS, GA Q3 2024)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T14:12:24Z
**Total evidence items collected:** 75
**Total distinct sources:** 27

---

## 1. Overview

Arista CloudVision MSS (Multi-Domain Segmentation Service, formerly Macro-Segmentation Service) is Arista's agentless, network-based microsegmentation product. It creates per-asset "microperimeters" by enforcing stateless, wire-speed, identity-aware policy directly in Arista EOS switches, without endpoint software or proprietary protocols [7]. Segmentation policies are defined once in CloudVision and enforced dynamically from real-time network, application, device, or user identity information [1]. MSS integrates with stateful firewalls and cloud proxies from Palo Alto Networks and Zscaler for north-south L4-L7 inspection [7][25], and is managed end-to-end from CloudVision, which provides NetDL-powered real-time visibility into packets, flows, and endpoint identity plus dedicated MSS dashboards [7][4]. It is part of Arista's zero-trust portfolio alongside CV AGNI (network identity/NAC) and Arista NDR (the acquired Awake platform) for AI-driven discovery, classification, and threat detection [1][22]. Deployment spans campus and data center networks (general availability Q3 2024) [7], with CloudVision able to run on-premises or as-a-service [9][23]. Arista positions MSS for enterprises needing east-west lateral segmentation without per-host agents, complementing firewalls rather than replacing them [10].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 9     | 3                | 6      | 0   |
| partial          | 13    | 1                | 12     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 6     | 0                | 6      | 0   |

**Evidence quality:** 20 items backed by ≥ 2 source_types; 14 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **4.1:** MSS has no endpoint agent by design (enforcement is stateless in the network via EOS switches), so an agent CPU-overhead figure does not apply.
- **4.2:** MSS does not deploy endpoint software, so an agent RAM footprint does not apply.
- **4.4:** No endpoint agent exists in MSS - the network switch creates the microperimeters - so an agent crash fail-open/fail-closed consideration does not apply.
- **4.5:** MSS installs no host agents (agentless switches orchestrated by CloudVision), so reboot-free agent install/update requirements do not apply.
- **6.1:** Enforcement is documented as stateless, wire-speed, in-network via EOS switches with no endpoint software, so process-level enforcement is ruled out by the documented architecture.
- **6.4:** There is no endpoint agent communicating with a controller in MSS (network-enforced, no endpoint software), so the agent-to-controller TLS/mutual-auth requirement does not apply.

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | - | The MSS press release and product briefs document deep real-time visibility into packets, flows and endpoint identity, and Arista NDR autonomously discovers, profiles and classifies devices, users and applications across the network; the independent SiliconANGLE analysis corroborates real-time flow and identity visibility. [1], [7], [10] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | MSS dashboards in CloudVision and dedicated security dashboards manage the microsegmentation lifecycle, and devices are grouped for single-pane-of-glass control; a connectivity map organized specifically by App/Environment/Role/Process is not documented in the staged sources. [4], [5], [7] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | CloudVision's NetDL is described as streaming full network state in real time and storing it historically forever with full state history from any point in time; no source states an explicit retention period of 90 days or more for connection-flow history. [23], [26] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | high | - | Arista NDR detects threats to and from discovered entities, parses thousands of protocols to identify behavioral anomalies, and the SiliconANGLE briefing notes most devices on the network are unmanaged/unknown, which MSS and NDR surface; unrecognized/unknown traffic detection is documented. [1], [10], [22] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | - | Segmentation policies are defined in CloudVision and enforced dynamically from real-time network, application, device or user identity information; MSS-Group authorizes access by logical groups independent of interfaces, subnets or IP addressing, per the press release, Network World and Arista blog. [1], [7], [13], [22] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | Arista AVA applies machine learning to segmentation and policy, the AGNI blog documents AVA providing recommendations based on problem context, and MSS extends Ask AVA to let operators query and filter policy violations; vendor-only sources so confidence is capped at medium. [1], [7], [27] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | Cloud Test provides a digital-twin environment to test proposed network changes before deployment and change-control testing is part of the CI Pipeline, while the 2026 ETM release documents Traffic Simulation via Ask AVA; an MSS-specific policy dry-run/simulation mode is not explicitly documented. [6], [8] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | - | The CI Pipeline delivers version control and change management with change-control workflow enhancements, and the community Terraform provider exposes a cvp_workspace_rollback action; an instant one-click policy rollback is not explicitly documented. [8], [20], [24] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | MSS is network-agnostic and endpoint-independent with no endpoint software, so any endpoint OS is covered by network-layer enforcement; no per-OS compatibility matrix for Windows Server/Linux/AIX/Solaris agents is documented. [7], [12] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | high | - | Agentless/network-based enforcement is fully documented (switches create microperimeters, with steering to Palo Alto Networks/Zscaler for stateful inspection), but an agent-based mode is not offered, so the both-agent-and-agentless requirement is only partially met. [7], [10], [13], [25] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | CloudVision clusters can run on-premises in the operator's datacenter or in the cloud, and the on-premises and SaaS offerings share the same features; an explicit fully air-gapped (no Internet) deployment statement is not documented. [9], [23] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Scale is described qualitatively - zero trust at terabit scale and a horizontally scalable CloudVision cluster - but no source cites a workload count at or above 50,000 endpoints. [21], [23] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | - | MSS has no endpoint agent by design (enforcement is stateless in the network via EOS switches), so an agent CPU-overhead figure does not apply. [7], [12] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | - | MSS does not deploy endpoint software, so an agent RAM footprint does not apply. [7], [10] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | Enforcement is described as stateless wire-speed in the network (and quarantine at gigabit/terabit line rates), but no source provides a measured added-latency figure to compare against the 0.1 ms threshold. [7], [10], [25] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | - | No endpoint agent exists in MSS - the network switch creates the microperimeters - so an agent crash fail-open/fail-closed consideration does not apply. [7], [21] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | - | MSS installs no host agents (agentless switches orchestrated by CloudVision), so reboot-free agent install/update requirements do not apply. [10], [13] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | - | CloudVision exposes a RESTful API (cvprac client), state-based gRPC/protobuf resource APIs (cloudvision-python), and Arista describes the architecture as open and API-friendly with an API-rich strategy; vendor-hosted sources only, and 100%-of-admin-functions coverage is not explicitly claimed. [1], [16], [19], [27] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Arista's NDR integrates with Microsoft Azure Sentinel through MISA for network-context threat data, AGNI consumes context from SIEM systems including Splunk, and the zero-trust architecture integrates with Microsoft security offerings; all vendor press releases. [1], [3], [5] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | - | MSS is documented to integrate with IT service management such as ServiceNow as part of its zero-trust ecosystem; CMDB tag-synchronization specifics are not documented. [4], [7] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | The Arista CI Pipeline provides a DevOps environment for change control, Ansible modules and a Terraform provider manage CloudVision, and AVD-driven DevOps pipeline integrations automate network configuration deployment; sources are vendor or community hosted. [4], [8], [18], [20] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | N/A | medium | - | Enforcement is documented as stateless, wire-speed, in-network via EOS switches with no endpoint software, so process-level enforcement is ruled out by the documented architecture. [7], [21] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | AVA queries threat-intelligence sources and open-source intelligence, Zscaler brings attacker-infrastructure intelligence into Arista NDR, and NDR risk scores feed segmentation decisions; deception/honeypot capabilities are not documented. [1], [3], [22] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Automated compliance reporting and zero-trust alignment with NIST 800-207 (CISA Zero Trust Maturity Model) are documented; PCI-DSS, ISO 27001 or IEC 62443 report templates are not documented. [4], [13], [21] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | N/A | medium | - | There is no endpoint agent communicating with a controller in MSS (network-enforced, no endpoint software), so the agent-to-controller TLS/mutual-auth requirement does not apply. [7], [10] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | CloudVision - the platform that orchestrates MSS - is documented as a cluster with high availability where a pair of clusters co-ingest state so the other continues managing devices if one is down; vendor-only sources cap confidence at medium. [4], [23] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | MSS microperimeters are created by the network switches (data plane), and CloudVision management-plane failure is documented as having no impact on the network data plane, so enforcement continues when the controller is unreachable; vendor-blog only. [21], [23] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Unknown | low | - | no evidence found |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | NIST CMVP lists Arista's EOS Crypto Module as FIPS 140-2 (Level 1) and the Arista Crypto Module v3.0 as FIPS 140-3 (Level 1), covering the EOS-based enforcement plane; no Common Criteria EAL4+ certification was found, and MSS/CloudVision software itself is not listed separately. [14], [15], [21] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found |

---

## 4. Notable Strengths

- **Group-based, identity-aware policy independent of IP/VLAN (item 2.1):** MSS-Group authorizes access by logical groups rather than interfaces, subnets, or physical ports, with policies enforced dynamically from real-time identity information [13][1].
- **Agentless wire-speed enforcement (items 3.3, 4.3):** microperimeters are enforced statelessly in EOS switches at wire speed with no endpoint agents, so the agent-resource and reboot items (4.1, 4.2, 4.4, 4.5) are structurally not applicable [7][10].
- **Real-time visibility and AI-driven NDR (items 1.1, 1.5):** CloudVision/NetDL provides real-time visibility into packets, flows, and endpoint identity, while Arista NDR autonomously discovers, profiles, and classifies devices, users, and applications and detects threats [7][1][10].
- **AI-assisted policy operations (item 2.2):** Arista AVA applies machine learning to segmentation and policy, provides recommendations from problem context, and extends Ask AVA to MSS for querying and filtering policy violations [1][27][7].
- **Strong automation and API surface (items 5.1, 5.4):** CloudVision exposes RESTful and gRPC resource APIs, and the CI Pipeline with AVD, Ansible, and a Terraform provider supports declarative network-as-code operations [19][16][8][18][20].

## 5. Notable Gaps / Risks

- **No process-level enforcement (item 6.1):** enforcement is stateless and in-network only, so buyers needing host/process-level granularity must pair MSS with endpoint security tools.
- **Unquantified numeric claims (items 1.3, 3.5, 4.3):** flow-history retention is described only as "stored historically forever", scale only as "terabit", and latency only as "wire-speed" - none of the checklist's numeric thresholds (90 days, 50,000 workloads, 0.1 ms) is confirmed by a measured figure.
- **Native container/Kubernetes isolation not evidenced (item 3.2):** MSS protects any IP endpoint including containers, but native Kubernetes/OpenShift policy integration is undocumented.
- **No disaster-recovery site sync evidence (item 7.3):** controller HA is documented, but DR-site replication/backup-restore is not.
- **Compliance reports and certifications only partially covered (items 6.3, 8.1):** NIST 800-207 alignment and FIPS 140-2/140-3 EOS crypto are documented, but PCI-DSS/ISO 27001/IEC 62443 report templates and Common Criteria EAL4+ remain unverified.
- **Unknown items to close with vendor docs: CVE context on map (1.4), hierarchical/inherited policy (2.5), and OT certifications (8.2).**

## 6. Evidence Quality Notes

Evidence spans 27 staged sources and 75 evidence entries, all verified as exact substrings of the persisted artifact text (0 fabricated, 0 unverifiable under the strict grounding check). Four independent third-party sources (SiliconANGLE's MSS briefing and three Network World articles by Michael Cooney) plus two NIST CMVP registry entries triangulate the core claims: 1.1, 1.5, 2.1, and 3.3 each mix vendor documentation with at least one independent source, which is why those items reach high confidence. Items 1.2, 1.3, 2.2, 2.3, 2.4, 3.4, 3.5, 5.1, 5.2, 5.4, 6.2, 7.1, 7.2, and 8.1 rest on vendor-only documentation or blogs, capping confidence at medium per the validator rule.

The research environment could not fetch arista.com product pages (bot-protection challenge) or the Common Criteria portal, so official MSS product-page wording and EAL4+ status were not directly verifiable; this drove 8.1 to partial and left 8.2 unknown. No material contradictions surfaced - vendor press releases, Arista blogs, and independent coverage consistently describe MSS as agentless, network-enforced, and CloudVision-orchestrated, so the verdicts follow that agreement. Numeric items (1.3, 3.5, 4.3) were kept at partial with null values because available sources give qualitative language only, and 6.1 was rated not_supported on the documented agentless architecture (network-switch enforcement with no endpoint software) rather than on absence of mention.

---

## Bibliography

[1] Arista Networks. "Arista Networks Unveils Zero Trust Networking Vision (press release)". https://www.arista.com/en/company/news/press-release/18443-pr-20231109 (Retrieved: 2026-08-10T14:12:24Z)
[2] Arista Networks. "Arista Announces Acquisition of Awake Security (press release)". https://www.arista.com/en/company/news/press-release/11750-pr-20200928 (Retrieved: 2026-08-10T14:12:24Z)
[3] Arista Networks. "Arista Joins Microsoft Intelligent Security Association for Integration with Microsoft Azure Sentinel (press release)". https://www.arista.com/en/company/news/press-release/13414-pr-20211116 (Retrieved: 2026-08-10T14:12:24Z)
[4] Arista Networks. "CloudVision delivers Modern Network Operating Model across the Enterprise (press release)". https://www.arista.com/en/company/news/press-release/20387-pr-20240924 (Retrieved: 2026-08-10T14:12:24Z)
[5] Arista Networks. "Arista Networks Introduces AI-Driven Network Identity (press release)". https://www.arista.com/en/company/news/press-release/17244-pr-20230424 (Retrieved: 2026-08-10T14:12:24Z)
[6] Arista Networks. "Arista Networks Introduces AI-Driven Zero Trust Branch (press release)". https://www.arista.com/en/company/news/press-release/24357-pr-20260721 (Retrieved: 2026-08-10T14:12:24Z)
[7] Arista Networks. "Arista Launches Next Generation Multi-Domain Segmentation for Zero Trust Networking (press release)". https://www.arista.com/en/company/news/press-release/19297-pr-20240430 (Retrieved: 2026-08-10T14:12:24Z)
[8] Arista Networks. "Arista Delivers Continuous Integration Pipeline for Network as a Service Automation (press release)". https://www.arista.com/en/company/news/press-release/16344-pr-20221103 (Retrieved: 2026-08-10T14:12:24Z)
[9] Arista Networks. "Arista Launches Network Automation as a Service with CloudVision (press release)". https://www.arista.com/en/company/news/press-release/11689-pr-20200818 (Retrieved: 2026-08-10T14:12:24Z)
[10] SiliconANGLE. "Arista enhances its multi-domain segmentation to fight east-west threats". https://siliconangle.com/2024/04/30/arista-enhances-multi-domain-segmentation-fight-east-west-threats/ (Retrieved: 2026-08-10T14:12:24Z)
[11] Network World. "Arista, Palo Alto bolster AI data center security". https://www.networkworld.com/article/4089591/arista-palo-alto-bolster-ai-data-center-security.html (Retrieved: 2026-08-10T14:12:24Z)
[12] Network World. "Arista targets lateral security threat in campus and data center networks". https://www.networkworld.com/article/2096944/arista-targets-lateral-security-threat-in-campus-and-data-center-networks.html (Retrieved: 2026-08-10T14:12:24Z)
[13] Network World. "Arista embraces segmentation as part of its zero-trust security". https://www.networkworld.com/article/969582/arista-embraces-segmentation-as-part-of-its-zero-trust-security.html (Retrieved: 2026-08-10T14:12:24Z)
[14] NIST CSRC. "CMVP Certificate #4592 - Arista EOS Crypto Module (FIPS 140-2)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4592 (Retrieved: 2026-08-10T14:12:24Z)
[15] NIST CSRC. "CMVP Certificate #5403 - Arista Crypto Module v3.0 (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5403 (Retrieved: 2026-08-10T14:12:24Z)
[16] GitHub (Arista Networks). "aristanetworks/cloudvision-python README". https://raw.githubusercontent.com/aristanetworks/cloudvision-python/master/README.md (Retrieved: 2026-08-10T14:12:24Z)
[17] GitHub (Arista Networks). "aristanetworks/cloudvision-apis README". https://raw.githubusercontent.com/aristanetworks/cloudvision-apis/master/README.md (Retrieved: 2026-08-10T14:12:24Z)
[18] GitHub (Arista Networks). "aristanetworks/ansible-cvp README". https://raw.githubusercontent.com/aristanetworks/ansible-cvp/devel/README.md (Retrieved: 2026-08-10T14:12:24Z)
[19] GitHub (Arista Networks). "aristanetworks/cvprac README (RESTful API client)". https://raw.githubusercontent.com/aristanetworks/cvprac/develop/README.md (Retrieved: 2026-08-10T14:12:24Z)
[20] GitHub (community). "ioplane/terraform-provider-cvp README". https://raw.githubusercontent.com/ioplane/terraform-provider-cvp/main/README.md (Retrieved: 2026-08-10T14:12:24Z)
[21] Arista Networks blog. "The Era of Microperimeters". https://blogs.arista.com/blog/the-era-of-microperimeters (Retrieved: 2026-08-10T14:12:24Z)
[22] Arista Networks blog. "The Time for Zero Trust Networking is Now". https://blogs.arista.com/blog/time-for-zero-trust-networking-is-now (Retrieved: 2026-08-10T14:12:24Z)
[23] Arista Networks blog. "CloudVision: A Cognitive Management Plane". https://blogs.arista.com/blog/cloudvision-cognitive-management-plane (Retrieved: 2026-08-10T14:12:24Z)
[24] Arista Networks blog. "CI-Based Cloud Network Automation". https://blogs.arista.com/blog/ci-based-cloud-networking-automation (Retrieved: 2026-08-10T14:12:24Z)
[25] Arista Networks blog. "Arista and Palo Alto Networks Strengthen Partnership in the New Age of AI Security". https://blogs.arista.com/blog/arista-and-palo-alto-networks-strengthen-partnership-in-the-new-age-of-ai-security (Retrieved: 2026-08-10T14:12:24Z)
[26] Arista Networks blog. "CloudVision: The First Decade". https://blogs.arista.com/blog/cloudvision-the-first-decade-2025 (Retrieved: 2026-08-10T14:12:24Z)
[27] Arista Networks blog. "Network Identity Redefined for Zero Trust Enterprises". https://blogs.arista.com/blog/network-identity-redefined (Retrieved: 2026-08-10T14:12:24Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 22
- **Sources reviewed:** 27 (kept: 27, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, community: 1, third_party_review: 4, vendor_blog: 7, vendor_doc: 13
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
