# Microsegmentation Product Assessment: BlastWave - BlastShield

**Product ID:** `blastshield`
**Version reference:** BlastShield firmware 1.14.x era (2026); staged materials span 2021-2026 (firmware changelog, solution briefs v20260330, ZTNA technical white paper, KB articles)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T16:55:35Z
**Total evidence items collected:** 76
**Total distinct sources:** 28

---

## 1. Overview

BlastShield is BlastWave's zero-trust software-defined perimeter (SDP) for OT, IT and IoT environments, deployed as an encrypted peer-to-peer overlay network rather than a hardware or cloud-gateway architecture [3][16]. It combines three capabilities: network cloaking (rendering protected assets invisible to scans), passwordless phishing-resistant multi-factor authentication, and software-defined micro-segmentation via identity-based groups and directional From/To policies [18]. Enforcement runs at the network layer (Layer 2/3): a Host Agent protects individual servers, while the agentless Security Gateway (software, VM, container, or partner appliance) segments groups of devices that cannot run an agent, including legacy OT/IIoT endpoints [3][16][25]. Policies and users are managed through the Orchestrator, which can be cloud-hosted, on-premises, or fully air-gapped [8]. BlastShield explicitly does not scan traffic or detect anomalies; asset discovery and threat monitoring are delivered through partner visibility tools such as Dragos, Nozomi and Phosphorus [14][18]. Deployment is overlay-based with no underlay changes, and agent/network components keep enforcing cached policies even when the Orchestrator is unreachable [2][19].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 11    | 1                | 10     | 0   |
| partial          | 12    | 0                | 12     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 1     | 0                | 1      | 0   |

**Evidence quality:** 18 items backed by ≥ 2 source_types; 9 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **6.1:** Enforcement is documented at the network layer (Layer 2/3 microsegmentation of users, agents and gateway endpoints); no process-level access control is described.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | — | BlastShield nodes auto-discover peers and routes in the overlay, but the vendor states BlastShield does not scan for or detect suspicious activity and asset discovery is delegated to partner visibility tools (Dragos, Nozomi, Phosphorus). [3], [14], [18] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | The Orchestrator GUI provisions groups and policies and provides list views for endpoints, nodes, groups and policies; no connection topology map organized by app/environment/role/process is documented. [2], [3], [24] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Per-connection logs can be exported to syslog and persisted to external storage via public API endpoints, but no built-in retention period of 90 days or more is documented. [12], [13], [24] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Not Supported | medium | — | The vendor states BlastShield does not scan for or detect suspicious activity and relies on partner visibility vendors for asset discovery, so CVE/vulnerability context on a map is not provided. [14], [18] |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | — | Connections not matching policy are dropped and logged (terminated_by_policy events), and unauthorized egress attempts are identified and shut down, but no unrecognized-traffic discovery or visualization feature is documented. [12], [15] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | — | Policies are defined between identity-based groups that are independent of the underlying IP/VLAN segmentation; SCIM 2.0 integration with Okta/Azure AD/One Identity and public-key identity are documented. [2], [4], [18], [26], [27] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | — | no evidence found |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | — | no evidence found |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | — | no evidence found |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | — | Host Agent support covers Windows Server 2012+ and Windows 10+, Debian/Ubuntu and RPM-based (CentOS 7+) Linux, and macOS; AIX, Solaris and Windows Server 2003 are not supported. [6], [16] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | The BlastShield Gateway runs as a container in Kubernetes clusters and the vendor states containers/Kubernetes clusters are secured, but per-pod native isolation and OpenShift support are not documented. [9], [17], [22] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | — | Both agent-based protection (Host Agent) and agentless protection (Gateway/Virtual Gateway in front of devices that cannot run an agent) are documented. [3], [16] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | A fully air-gapped deployment with an on-premises Orchestrator (no internet access) is documented, with FIDO2 keys replacing the mobile authenticator in that mode. [7], [8], [16] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Vendor material reports protecting over 5,000 industrial control sites across 13 countries and describes the peer-to-peer mesh as inherently scalable, but no per-controller workload count reaching 50,000 is published. [14], [17], [19] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | — | no evidence found |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Supported | medium | 50 MB | The vendor spec table lists Host Agent memory of 50 MB, and the 2021 DOE briefing describes the deployed software as taking up less than 40 MB of memory; both figures are below the 100 MB threshold. [16], [19] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | — | no evidence found |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Supported | medium | — | Policy checking and enforcement are performed by clients and Host Agents/Gateways independently of the Orchestrator, nodes keep talking when the Orchestrator is down, and gateways restore the last known policy set if the Orchestrator is unreachable. [2], [19], [24] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Supported | medium | — | Deployment does not require shutting the network down or rebooting hosts; agent upgrades restart the agent service only. [14], [28] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Supported | medium | — | A public REST API covers list/add/remove/update of users, endpoints, agents, gateways, groups and policies, and release notes document ongoing API expansion (events endpoints, openapi.json). [5], [16], [24] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | — | Machine-readable syslog events (events/audit/connections scopes, JSON/CSV formats) are exported to remote receivers for SIEMs; the S&P Global analyst report and Tolly report both document Splunk/QRadar and SIEM integration. [12], [13], [17], [18] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | — | no evidence found |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | — | An official Terraform provider for BlastShield is published on the Terraform Registry (driven by the REST API); no native Jenkins or GitLab CI/CD integrations are documented. [5], [21] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | N/A | medium | — | Enforcement is documented at the network layer (Layer 2/3 microsegmentation of users, agents and gateway endpoints); no process-level access control is described. [3], [25] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | Threat intelligence and asset discovery are delivered through integrations with partners (Dragos, Nozomi Networks, Phosphorus) rather than a built-in capability; no honeypot/deception feature is documented. [14], [18] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | Vendor documentation maps BlastShield to frameworks including IEC 62443-3-3, ISO/IEC 27001 and NIST SP 800-207, but no built-in compliance report templates for the listed standards are documented. [16], [23], [25] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Supported | medium | — | Data in motion is encrypted with AES-256-GCM over mutually authenticated sessions (ECDSA challenge/response key exchange, ECDHE + HKDF); TLS 1.3 specifically is not named but mutual authentication is documented. [4], [16] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | Orchestrators can be deployed in a High-Availability team (leader election documented in release notes; syslog guide describes a 'High-Availability Team'), and gateways support active/standby stateful failover. [10], [11], [19], [24] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | — | Nodes continue enforcing cached policies and peer tunnels when the Orchestrator is down, and gateways restore the last known policy and endpoint set if the Orchestrator is unreachable after a reboot. [2], [19], [24] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | Database backups and gateway factory-reset restore are documented in release notes, and on-premises Orchestrator deployments are supported; no explicit multi-site DR replication/sync feature is documented. [8], [24] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | The vendor states BlastShield uses the wolfCrypt FIPS 140-2 Level 1 validated crypto engine, but no BlastWave/BlastShield module appears in the NIST CMVP validated-modules list, and no Common Criteria certification was found. [16], [20] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found |

---

## 4. Notable Strengths

- **Identity-based, IP/VLAN-independent microsegmentation (2.1):** policies are defined over logical groups that are independent of the underlying network segmentation, with SCIM 2.0 integration to Okta, Azure AD and One Identity for identity sync [2][26].
- **Fail-safe, autonomous enforcement (4.4, 7.2):** policy checking is done by clients and Host Agents/Gateways independently of the Orchestrator, nodes keep talking when the Orchestrator is down, and gateways restore the last known policy set if the Orchestrator is unreachable [2][19][24].
- **Agent and agentless coverage for OT (3.3, 3.4):** Host Agents protect servers while agentless Gateways segment legacy OT/IIoT devices, and fully air-gapped deployments with an on-premises Orchestrator are documented [3][7][8].
- **Strong automation and integration surface (5.1, 5.2, 5.4):** a public REST API covers users/endpoints/agents/gateways/groups/policies, syslog exports feed SIEMs (Splunk, IBM QRadar), and an official Terraform provider exists [5][12][18][21].
- **Documented HA posture (7.1):** Orchestrators can be deployed in a High-Availability team with leader election, and gateways support active/standby stateful failover [10][11][24].

## 5. Notable Gaps / Risks

- **No flow-level visibility or discovery (1.1, 1.2, 1.4):** BlastShield does not scan for or detect traffic and provides no connection topology map or CVE context; buyers needing visibility must pair it with a partner tool such as Nozomi, Dragos or Phosphorus [14][18].
- **Unverified numeric performance thresholds (4.1, 4.3):** no source quantifies agent CPU overhead or added network latency, so the <1% CPU and <0.1 ms latency checklist thresholds remain unverified; only throughput (Tolly) is benchmarked [17].
- **Policy lifecycle tooling absent (2.2, 2.3, 2.4):** no AI/ML rule recommendation, policy simulation/dry-run, or one-click rollback is documented; policy changes are enforced directly on nodes [24].
- **Kubernetes support is gateway-level, not native per-pod isolation (3.2):** the Gateway runs as a K8s container and the vendor states containers/Kubernetes clusters are secured, but no per-pod enforcement or OpenShift support is documented [9][22].
- **Certification posture is engine-level only (8.1):** the vendor claims a FIPS 140-2 Level 1 validated wolfCrypt crypto engine, but no BlastWave module is listed in the NIST CMVP registry and no Common Criteria certification was found; items 2.5, 5.3, 8.2 also lack evidence [16][20].

## 6. Evidence Quality Notes

Of the 33 checklist items, 17 were supported by evidence spanning at least two source types and 10 relied on vendor documentation only (confidence capped at medium). The strongest triangulation is on items 5.2 and 2.1, where an independent S&P Global (451 Research) analyst report corroborates vendor documentation, and on 3.2/3.5 where the Tolly Group benchmark and a press release add non-datasheet sources. Independent sources are otherwise limited: the Tolly report is vendor-commissioned, the U.S. DOE-hosted 2021 briefing deck is vendor-authored, and the only truly independent materials are the S&P Global report and the NIST CMVP registry. No direct contradictions between sources were found; where vendor claims were thin, verdicts were set to partial with explicit notes (e.g. 1.3 retention depends on the external syslog/storage receiver; 7.3 documents backup/restore but not multi-site DR replication) rather than being upgraded from silence.

Numeric-threshold items were handled conservatively: 4.2 uses the vendor's documented Host Agent memory figure (50 MB) plus the 2021 deck's under-40 MB statement, 3.5 cites the "over 5,000 industrial control sites" scale datapoint as partial (no per-controller workload count), and 4.1/4.3 were left unknown because no source mentions CPU or latency figures at all. The Common Criteria portal returned HTTP 403 to all fetch attempts, so CC status is unverifiable; the 8.1 verdict rests on the FIPS-validated wolfCrypt engine claim plus the authoritative negative CMVP registry result. Sources 23 (reseller) and 27 (policy configuration guide) add corroboration for 6.3 and 2.1 respectively but are not independent of vendor influence.

---

## Bibliography

[1] BlastWave. "BlastShield Software-Defined Perimeter (SDP) - product page". https://www.blastwave.com/blastshield (Retrieved: 2026-08-10T23:50:00Z)
[2] BlastWave Support. "How BlastShield Provides Microsegmentation". https://support.blastwave.com/bws/how-blastshield-provides-micro-segmentation (Retrieved: 2026-08-10T23:50:00Z)
[3] BlastWave Support. "BlastShield Overview and Architecture". https://support.blastwave.com/bws/blastshieldtm-overview-and-architecture (Retrieved: 2026-08-10T23:50:00Z)
[4] BlastWave Support. "Security (BlastShield knowledge base)". https://support.blastwave.com/bws/security (Retrieved: 2026-08-10T23:50:00Z)
[5] BlastWave Support. "Enable the BlastShield API". https://support.blastwave.com/bws/enable-the-blastshield-api (Retrieved: 2026-08-10T23:50:00Z)
[6] BlastWave Support. "BlastShield Agent supported operating systems". https://support.blastwave.com/bws/blastshieldtm-agent-supported-operating-systems (Retrieved: 2026-08-10T23:50:00Z)
[7] BlastWave Support. "On-premise installation of an air-gapped Orchestrator on VMware ESXi". https://support.blastwave.com/bws/on-premise-installation-of-an-air-gapped-orchestra (Retrieved: 2026-08-10T23:50:00Z)
[8] BlastWave Support. "Deployment options (Orchestrator cloud/on-prem/air-gapped)". https://support.blastwave.com/bws/deployment-options (Retrieved: 2026-08-10T23:50:00Z)
[9] BlastWave Support. "Kubernetes Gateway deployment". https://support.blastwave.com/bws/kubernetes-gateway-deployment-1 (Retrieved: 2026-08-10T23:50:00Z)
[10] BlastWave Support. "Configure Gateway High Availability". https://support.blastwave.com/bws/configure-gateway-high-availability (Retrieved: 2026-08-10T23:50:00Z)
[11] BlastWave Support. "Syslog Setup with Windows-Based SIEM". https://support.blastwave.com/bws/syslog-setup-with-windows-based-siem (Retrieved: 2026-08-10T23:50:00Z)
[12] BlastWave Support. "BlastShield Remote Syslog Event Reference". https://support.blastwave.com/bws/syslog-format (Retrieved: 2026-08-10T23:50:00Z)
[13] BlastWave Support. "Enable Extended Access Logging". https://support.blastwave.com/bws/enable-extended-access-logging (Retrieved: 2026-08-10T23:50:00Z)
[14] BlastWave. "BlastShield Introduction - Securing Europe's Critical Infrastructure Against Dormant Threats (solution brief)". https://go.blastwave.com/hubfs/DOWNLOADS/Solution%20Briefs/SB-BlastShield-Introduction.pdf (Retrieved: 2026-08-10T23:50:00Z)
[15] BlastWave. "BlastShield Technical (solution brief)". https://go.blastwave.com/hubfs/DOWNLOADS/Solution%20Briefs/SB-BlastShield-Technical.pdf (Retrieved: 2026-08-10T23:50:00Z)
[16] BlastWave. "Zero Trust Network Access (ZTNA) Technical white paper". https://www.blastwave.com/zero-trust-network-access-ztna-technical (Retrieved: 2026-08-10T23:50:00Z)
[17] The Tolly Group / BlastWave. "BlastShield ZTNA Performance vs. OpenVPN, Perimeter 81, Tailscale, and Twingate (Tolly Group report landing page)". https://www.blastwave.com/tolly-report (Retrieved: 2026-08-10T23:50:00Z)
[18] S&P Global Market Intelligence. "Coverage Initiation: BlastWave elevates OT security with BlastShield zero-trust overlay for critical infrastructure (S&P Global Market Intelligence / 451 Research)". https://go.blastwave.com/hubfs/DOWNLOADS/In-the-News/SP-Global-Analyst-Report.pdf (Retrieved: 2026-08-10T23:50:00Z)
[19] BlastWave (hosted by U.S. DOE). "Introduction to BlastShield - BlastWave (DOE Critical Electric Infrastructure briefing deck)". https://www.energy.gov/sites/default/files/2021-06/Doug%20Compere%20Blastwave-A1.pdf (Retrieved: 2026-08-10T23:50:00Z)
[20] NIST CSRC. "NIST CMVP Validated Modules (complete active validation list)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all (Retrieved: 2026-08-10T23:50:00Z)
[21] BlastWave Inc.. "terraform-provider-blastshield README (GitHub)". https://raw.githubusercontent.com/blastwaveinc/terraform-provider-blastshield/main/README.md (Retrieved: 2026-08-10T23:50:00Z)
[22] BlastWave / PR Newswire. "A2i Selects BlastWave's BlastShield Passwordless Software-Defined Perimeter Solution (press release)". https://www.prnewswire.com/news-releases/a2i-selects-blastwaves-blastshield-passwordless-software-defined-perimeter-solution-301446208.html (Retrieved: 2026-08-10T23:50:00Z)
[23] OT Cyber Direct. "BlastShield Segmentation Gateway - OT Cyber Direct (reseller product page)". https://otcyberdirect.com/products/blastwave-segmentation-gateway (Retrieved: 2026-08-10T23:50:00Z)
[24] BlastWave. "BlastWave Firmware Changelog (machine-readable release notes API)". https://dl.blastwave.io/firmware/changes (Retrieved: 2026-08-10T23:50:00Z)
[25] BlastWave. "Network Segmentation | OT Microsegmentation (product page)". https://www.blastwave.com/network-segmentation (Retrieved: 2026-08-10T23:50:00Z)
[26] BlastWave Support. "External Identity Providers (SCIM 2.0 / OIDC)". https://support.blastwave.com/bws/external-identity-providers (Retrieved: 2026-08-10T23:50:00Z)
[27] BlastWave Support. "Configure an access policy and microsegmentation". https://support.blastwave.com/bws/configure-an-access-policy-and-microsegmentation (Retrieved: 2026-08-10T23:50:00Z)
[28] BlastWave Support. "Upgrade the Agent from the Orchestrator". https://support.blastwave.com/bws/upgrade-the-agent-from-the-orchestrator (Retrieved: 2026-08-10T23:50:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 28 (kept: 28, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 1, certification_registry: 1, product_release_notes: 1, third_party_review: 2, vendor_blog: 1, vendor_datasheet: 2, vendor_doc: 20
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
