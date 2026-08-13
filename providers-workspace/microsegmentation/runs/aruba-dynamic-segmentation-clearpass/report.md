# Microsegmentation Product Assessment: HPE Aruba Networking - Aruba Dynamic Segmentation / ClearPass (ClearPass Policy Manager + Aruba Central NetConductor)

**Product ID:** `aruba-dynamic-segmentation-clearpass`
**Version reference:** ClearPass Policy Manager 6.11 (Common Criteria certified entry, 2025); Aruba Central NetConductor (2022); OnGuard agent family; PeerSpot reviews captured 2026-08
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:11:29Z
**Total evidence items collected:** 38
**Total distinct sources:** 9

---

## 1. Overview

Aruba Dynamic Segmentation / ClearPass is HPE Aruba Networking's identity-based network access control (NAC) and segmentation family, centered on ClearPass Policy Manager and extended to the network fabric by Aruba Central NetConductor [8], [9]. ClearPass authenticates and authorizes users, devices and guests across multi-vendor wired, wireless and VPN infrastructure using role- and device-based policy, with OnGuard posture agents available as persistent, dissolvable or agentless options [9]. Central NetConductor applies the same policy as dynamic segmentation across the fabric via EVPN/VXLAN/BGP overlays with cloud-native NAC [8]. Deployment shapes are physical or virtual appliances, standalone or clustered, on-premises or in public/private cloud [9]. Assessed against the 33-item checklist, 2 items are supported (identity-based policy and agent-plus-agentless enforcement), 13 partial, and 18 unknown; unknowns concentrate on host-agent metrics (CPU/RAM/latency, fail-safe, no-reboot), flow-mapping/forensics (visual map, 90-day retention, CVE context), and container-native or process-level controls, which are not part of a network-edge NAC and were not evidenced in staged sources.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 2                | 0      | 0   |
| partial          | 13    | 0                | 13     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 18    | 0                | 0      | 18  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 6 items backed by ≥ 2 source_types; 0 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | - | PeerSpot reviewers describe device/identity visibility and role-based segmentation at network access, and eSecurity Planet lists identifying users and devices connecting to networks as a core capability; continuous flow-level auto-discovery is not documented. [1], [9] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Unknown | low | - | no evidence found (No staged source describes a visual connection map grouped by application, environment, role, or process.) |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Unknown | low | - | no evidence found (No staged source quantifies flow/session history retention; the >=90-day forensic retention requirement could not be verified.) |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (No staged source documents vulnerability/CVE context shown on a network map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | - | Device fingerprinting and posture assessment identify unknown devices by type/model/MAC/vendor, and unrecognized devices that fail minimum standards are blocked; this is access-time profiling rather than flow-level anomaly detection. [1], [9] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | high | - | eSecurity Planet documents role- and device-based access control with a context-based policy engine keyed on user role, device type, authentication method, location and time-of-day; PeerSpot reviewers confirm role-based segmentation and Packet Pushers positions ClearPass as a RADIUS/identity authenticator. [1], [5], [7], [8], [9] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Partial | medium | - | Help Net Security reports Aruba Central NetConductor uses AI for management and optimization with business-intent workflows to automate network configuration; explicit ML-based policy rule recommendation is not documented. [8] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | - | no evidence found (No staged source documents a policy simulation or dry-run mode.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No staged source documents an instant one-click policy rollback.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | - | no evidence found (No staged source documents inherited or hierarchical policy rules.) |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | eSecurity Planet documents OnGuard agents for Windows, macOS and Linux (with some capabilities unavailable on macOS/Linux), and a reviewer notes the ClearPass platform is Linux-based; AIX/Solaris and Windows Server version ranges are not enumerated. [1], [9] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Unknown | low | - | no evidence found (No staged source documents container/Kubernetes/OpenShift native isolation.) |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | high | - | eSecurity Planet documents OnGuard as persistent agent, agentless, or dissolvable agent; Packet Pushers describes agentless 802.1X and device profiling alternatives; NetConductor adds fabric-wide NAC enforcement. [7], [8], [9] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Partial | medium | - | eSecurity Planet documents on-premises physical/virtual appliances and local authentication survivability across distributed geographies; an explicit fully disconnected (no-internet) operating statement was not found. [9] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | 25000 workloads | eSecurity Planet documents a 25,000 concurrent-session appliance (C3000) and clusters of appliances for reach/resilience; PeerSpot reviewers give only qualitative scalability ('thousands of users'); no single deployment at or above 50,000 workloads is documented, so the threshold is not confirmed. [1], [9] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | - | no evidence found (No staged source quantifies OnGuard agent CPU overhead; the <1% threshold could not be verified.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | - | no evidence found (No staged source quantifies OnGuard agent memory footprint; the <100MB threshold could not be verified.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Unknown | low | - | no evidence found (No staged source quantifies added network latency; the <0.1ms threshold could not be verified.) |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Unknown | low | - | no evidence found (No staged source states whether traffic continues if the OnGuard agent fails or crashes; eSecurity Planet only documents posture-based blocking of non-compliant devices.) |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found (No staged source states that agent install/update never requires a reboot.) |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | PeerSpot reviewers report ClearPass integrates with third-party devices via published APIs and can be extended through APIs; full REST API coverage of 100% of administrative functions is not documented in staged sources. [1] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | - | eSecurity Planet documents integration of security alerts from over 170 security and IT management solutions including SIEMs; specific Splunk/QRadar/Sentinel and syslog/CEF protocol details are not named in staged sources. [9] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found (No staged source documents ServiceNow/CMDB tag synchronization.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Unknown | low | - | no evidence found (No staged source documents CI/CD pipeline integration (Jenkins, GitLab, Terraform); NetConductor's network-configuration automation is not presented as DevSecOps pipeline integration.) |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Unknown | low | - | no evidence found (No staged source documents process-level access enforcement; ClearPass is a network-level NAC/identity platform.) |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | eSecurity Planet documents ClearPass acting as a clearing house for attack alerts from 170+ solutions and adjusting network access based on UEBA/threat indexes via ClearPass Exchange; honeypot/deception detection is not documented. [9] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Unknown | low | - | no evidence found (No staged source documents built-in compliance reporting per PCI-DSS, NIST 800-207, ISO 27001, or IEC 62443.) |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | The Common Criteria evaluation covered TLS/SSL processing and encryption for ClearPass, FIPS-mode operation uses a FIPS 140-2 validated cryptographic module, and 802.1X certificate-based EAP-TLS is described by Packet Pushers; explicit TLS 1.3/mTLS between agent and controller is not documented. [2], [7], [9] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Partial | medium | - | eSecurity Planet documents clusters of physical and virtual appliances deployed to expand reach and improve resilience through redundancy; active-active/active-passive cluster semantics are not specified. [9] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Unknown | low | - | no evidence found (No staged source documents agent policy enforcement continuing autonomously when the controller is unreachable.) |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | eSecurity Planet documents distributed deployments with local authentication survivability across multiple geographies (e.g., 30 points of presence); explicit disaster-recovery site sync/replication is not documented. [9] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | eSecurity Planet reports FIPS 140-2 Level 2/3 validation and Common Criteria type-accreditation, MeriTalk documents ClearPass as the first NAC certified under NDcPP and the Authentication Server Extended Package via NIAP, and the CC portal lists ClearPass Policy Manager 6.11; the CMVP registry lists Aruba crypto modules but no ClearPass-named module, and the certification is NDcPP-based rather than EAL4+ labeled. [2], [3], [4], [9] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (No staged source documents industrial interoperability certifications from Siemens, Honeywell, or ABB.) |

---

## 4. Notable Strengths

- **Identity/role-based policy independent of IP and VLAN (item 2.1):** ClearPass enforces role- and device-based access control with a context-based policy engine keyed on user role, device type, authentication method, location and time-of-day, confirmed across a third-party review, PeerSpot reviewers, and vendor NetConductor material [1], [5], [7], [8], [9].
- **Agent-based and agentless enforcement in one platform (item 3.3):** OnGuard supports persistent, dissolvable and agentless posture assessment, while 802.1X, MAC-auth and device profiling cover unmanaged endpoints, and NetConductor delivers fabric-wide NAC enforcement [7], [8], [9].
- **Security qualifications for government use (item 8.1):** ClearPass Policy Manager 6.11 is listed in the Common Criteria certified-products registry under NDcPP and the SSH package, and the vendor reports FIPS 140-2 Level 2/3 validation and UC-APL listing [2], [4], [9].
- **Demonstrated scale and stability in production (items 3.5, 7.1):** eSecurity Planet documents a 25,000-concurrent-session appliance (C3000) and clusters of appliances for reach and resilience, and PeerSpot reviewers report multi-year zero-downtime operation and easy licensing-based scaling [1], [9].
- **Broad third-party ecosystem integration (items 5.1, 5.2, 6.2):** ClearPass integrates with over 170 security and IT management solutions (including SIEMs), is extendable through published APIs, and adjusts network access from UEBA/threat analytics via ClearPass Exchange [1], [9].

## 5. Notable Gaps / Risks

- **No host-agent resource or fail-safe guarantees (items 4.1, 4.2, 4.3, 4.4, 4.5):** no staged source quantifies OnGuard CPU/RAM/latency overhead or documents fail-open behavior on agent crash or reboot-free updates; a buyer needing these guarantees would need Aruba's agent documentation or independent lab tests.
- **Scale claim below the 50,000-workload threshold (item 3.5):** the largest documented figure is 25,000 concurrent sessions on a C3000 appliance; nothing documents a single centralized deployment at or above 50,000 workloads, so the threshold is unconfirmed.
- **No flow-level visibility, forensics or vulnerability context (items 1.2, 1.3, 1.4):** ClearPass provides device/identity visibility at access time but no source documents a connection map by app/role/process, 90-day flow-history retention, or CVE context on a map, which are core expectations of host-agent microsegmentation platforms.
- **No container-native or process-level controls (items 3.2, 6.1):** Kubernetes/OpenShift native isolation and process-level enforcement are absent from staged evidence; for workload-centric segmentation inside clusters, ClearPass would need to be paired with a host or container agent platform.
- **Certification nuance (item 8.1):** Common Criteria certification is registry-confirmed but under the NDcPP/Authentication-Server profile rather than an EAL4+ label, and the NIST CMVP registry lists Aruba crypto modules but no ClearPass-named module, so FIPS claims rest on vendor-reported validation.

## 6. Evidence Quality Notes

Nine sources were staged and all 38 evidence quotes were verified verbatim against the persisted artifact text (grounding check passed with zero fabricated or unverifiable entries). Triangulation is strongest for identity-based policy (2.1) and agent-plus-agentless enforcement (3.3), each backed by four sources spanning third-party reviews (eSecurity Planet, Help Net Security, Packet Pushers), community reviews (PeerSpot), and a vendor doc; certification (8.1) combines two registries (Common Criteria portal CSV, NIST CMVP) with two third-party articles. Six items drew on at least two source types; the remaining non-unknown items rest on one or two sources, typically eSecurity Planet plus PeerSpot, which keeps confidence at medium rather than high.

No vendor-only items exist in this assessment (every cited item includes at least one non-vendor source), but vendor documentation itself was the hardest evidence to obtain: the classic ClearPass admin guides and datasheets are hosted on domains that were unreachable or rate-limited from the research network, so vendor claims are represented indirectly through a tech-news article on NetConductor (Help Net Security), the Central NAC docs landing page, and vendor-relayed claims inside eSecurity Planet and MeriTalk coverage. The only meaningful source disagreement is in scalability (3.5): PeerSpot reviewers describe strong scaling qualitatively while eSecurity Planet gives a concrete 25,000-session per-appliance figure; the verdict is partial with the concrete figure used as numeric_value, since neither source supports the 50,000-workload threshold. The 18 unknown items reflect genuine absence of staged evidence, not confirmed absence of capability.

---

## Bibliography

[1] PeerSpot. "Aruba ClearPass Reviews (PeerSpot)". https://www.peerspot.com/products/aruba-clearpass-reviews (Retrieved: 2026-08-10T17:11:02Z)
[2] MeriTalk. "Common Criteria Certification Gets Down to Network Access Control". https://meritalk.com/articles/common-criteria-certification-gets-down-to-network-access-control/ (Retrieved: 2026-08-10T17:11:02Z)
[3] NIST CMVP. "NIST Cryptographic Module Validation Program - Validated Modules (search/all)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all (Retrieved: 2026-08-10T17:11:02Z)
[4] Common Criteria Portal. "Common Criteria Portal - Certified Products list (CSV)". https://www.commoncriteriaportal.org/products/certified_products.csv (Retrieved: 2026-08-10T17:11:02Z)
[5] HPE Aruba Networking. "HPE Aruba Networking Central documentation - NAC overview". https://arubanetworking.hpe.com/techdocs/new-central/content/nac/nac-overview.htm (Retrieved: 2026-08-10T17:11:02Z)
[6] HPE Aruba Networking. "HPE Aruba Networking Documentation Portal". https://www.arubanetworks.com/techdocs/ (Retrieved: 2026-08-10T17:11:02Z)
[7] Packet Pushers. "Heavy Networking 608: Everything You Ever Wanted to Know About NAC and Then Some". https://packetpushers.net/podcasts/heavy-networking/hn608-everything-you-ever-wanted-to-know-about-nac-and-then-some/ (Retrieved: 2026-08-10T17:11:02Z)
[8] Help Net Security. "Aruba Central NetConductor enables IT teams to automate network configuration". https://www.helpnetsecurity.com/2022/03/30/aruba-central-netconductor/ (Retrieved: 2026-08-10T17:11:02Z)
[9] eSecurity Planet. "Aruba ClearPass Policy Manager NAC Solution Review". https://www.esecurityplanet.com/products/aruba-clearpass/ (Retrieved: 2026-08-10T17:11:02Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 22
- **Sources reviewed:** 9 (kept: 9, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, community: 1, third_party_review: 4, vendor_doc: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
