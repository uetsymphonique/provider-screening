# Microsegmentation Product Assessment: Cloudflare - Cloudflare One

**Product ID:** `cloudflare-one`
**Version reference:** Cloudflare One / Cloudflare Zero Trust documentation (Apr-Jul 2026, docs snapshot at capture time)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T13:55:15Z
**Total evidence items collected:** 55
**Total distinct sources:** 27

---

## 1. Overview

Cloudflare One is Cloudflare's Secure Access Service Edge (SASE) platform, a cloud security offering that replaces legacy perimeters with Cloudflare's global network [1]. It consolidates Cloudflare Access (identity-based application access), Secure Web Gateway (DNS/HTTP/network filtering), Cloudflare Tunnel (outbound-only connectivity via cloudflared), the Cloudflare One Client (formerly WARP) for devices, plus CASB, DLP, RBI, and Email security into a unified control plane [1]. The vendor positions the product around Zero Trust and identity-based policy rather than host-agent microsegmentation: Gateway and Access policies key on user identity, groups, SAML/OIDC claims, and device posture instead of IPs or VLANs [2][3][4], and enforcement happens on Cloudflare's 300+ point-of-presence anycast network with cached-policy resilience on clients [8]. Deployment shapes include device agents, DNS-only router/network on-ramps without a client, and cloudflared in Kubernetes or other infrastructure [1][10][22]. This assessment evaluates the platform's fit against a host-centric microsegmentation checklist, where several classic capabilities (host-agent flow mapping, process-level enforcement, FIPS/Common Criteria certification) are absent or undocumented.

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 7     | 1                | 6      | 0   |
| partial          | 15    | 0                | 15     | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 4 items backed by ≥ 2 source_types; 19 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Partial | medium | - | Cloudflare Gateway records DNS, HTTP, and network sessions for traffic through its on-ramps, and Network Flow analyzes router/cloud flow data (NetFlow, IPFIX, sFlow); however, coverage depends on traffic being routed through Cloudflare, and no in-datacenter agent is documented that auto-discovers workload-to-workload flows. [5], [6], [15] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | Gateway analytics dashboards visualize sessions over time by user, device, action, and application; no dependency map grouped by environment, role, or process is documented. [20] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Cloudflare documents Logpush for long-term log storage with export to third-party or SIEM destinations, but no staged source quantifies retention in days, so the >=90-day threshold is unconfirmed (qualitative evidence only). [5], [19] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (No source found describing vulnerability/CVE context displayed on a connectivity map.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | - | Network Flow rules alert on traffic-volume thresholds and Gateway analytics flag anomalies or shifts in session patterns; no explicit unrecognized/unknown-traffic classification for internal segmentation is documented. [15], [20] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Gateway and Access policies are built on identity attributes such as user email, group memberships, SAML/OIDC claims, and device posture rather than on IP addresses or VLANs. [2], [3], [4] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | - | no evidence found (No source found for AI/ML-based automatic policy recommendation in Cloudflare One.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | Cloudflare documents a DNS policy test procedure to confirm filtering before production rollout; no full simulation/dry-run engine spanning all policy types is documented. [22] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No source found for one-click instant policy rollback.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Supported | medium | - | Tiered policies share and enforce Gateway policies across multiple Zero Trust accounts, including parent/child inheritance via the Tenant API. [21] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Not Supported | medium | - | The Cloudflare One Client explicitly does not run on Windows Server, and the documented client platforms are Windows, macOS, Linux, iOS, Android, and ChromeOS; AIX and Solaris are not mentioned. [7] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | - | cloudflared can run inside a Kubernetes cluster to connect applications to Cloudflare, with tunnel routes and Access policies controlling which services are reachable; native in-cluster pod-level isolation is not documented, and OpenShift is not mentioned. [10] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | Cloudflare One provides both an on-device client (Cloudflare One Client) and network-level on-ramps including cloudflared tunnels and DNS-only locations that work without the client. [1], [22] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Unknown | low | - | no evidence found (No source addresses fully air-gapped (no-internet) deployments; Cloudflare One policy enforcement is cloud-based.) |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | PeerSpot reviewers describe Cloudflare One as highly scalable with deployments of thousands of users, and Cloudflare documents a 300+ PoP anycast network; no workload-count figure is published, so the 50,000-workload threshold is unconfirmed. [8], [26] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Unknown | low | - | no evidence found (No source provides a numeric CPU-overhead figure for the Cloudflare One Client.) |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Unknown | low | - | no evidence found (No source provides a numeric RAM-footprint figure for the Cloudflare One Client.) |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | PeerSpot reviewers report shorter hops and improved latency compared with previous VPN solutions, but no numeric latency measurement is published, so the <0.1 ms threshold is unconfirmed. [26] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | When the client cannot establish the tunnel, users lose access to protected applications by default; fail-open behavior is available only through pre-configured Global, External, or Local Emergency Disconnect mechanisms. [8], [9] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Unknown | low | - | no evidence found (No source states whether Cloudflare One Client install or update requires a server reboot.) |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | Zero Trust configuration can be managed via the Cloudflare API and Terraform, and a read-only dashboard mode enforces API-only management; no statement claims the API covers 100% of dashboard functions. [12] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | medium | - | Logpush exports Zero Trust datasets (DNS, HTTP, network sessions, posture) to third-party SIEM/storage destinations, and Splunk and IBM QRadar appear in the supported destinations list. [5], [23] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Unknown | low | - | no evidence found (No source found for ServiceNow CMDB tag synchronization.) |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | Scoped API tokens let automated systems manage Zero Trust settings, and Cloudflare Tunnels and other Zero Trust resources are deployable through the Terraform provider, enabling policy-as-code in CI/CD pipelines. [12], [24] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Partial | medium | - | Application Check posture verifies that a specific application process is running, and Device Posture selectors gate access based on device state; per-process network-flow enforcement is not documented. [2], [14] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | - | IDS monitors traffic against known threat signatures and leverages Cloudflare's global threat intelligence, and Gateway blocks risky sites with custom blocklists and threat intel; no honeypot/deception capability is documented. [1], [13] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | Cloudflare provides compliance documentation for PCI, SOC 2, and ISO via the dashboard and Trust Hub; NIST 800-207 and IEC 62443 are not covered in the staged sources. [16], [17] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | The client-to-Cloudflare transport uses WireGuard/MASQUE tunnels with HTTPS device orchestration, and Access supports mutual TLS client-certificate authentication; TLS 1.3 in the agent-to-controller path is not explicitly documented. [11], [18], [25] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | high | - | Cloudflare's 300+ PoP anycast network routes clients to the nearest healthy PoP automatically, with built-in redundancy and failover for edge services; PeerSpot reviewers report stable, reliable operation. [8], [13], [26] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | The client keeps locally cached policies and continues enforcing security controls when Cloudflare's management systems are unreachable, and edge services keep enforcing cached configurations during management outages. [8] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | - | Emergency Disconnect provides disaster-recovery mechanisms, including customer-hosted HTTPS endpoints and local signal files, that work even when Cloudflare infrastructure is unreachable. [9] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Not Supported | medium | - | The NIST CMVP validated-modules list staged for the 'cloudflare' keyword contains no Cloudflare entries, and Cloudflare's compliance documentation names PCI, SOC 2, and ISO rather than FIPS 140-2/140-3 or Common Criteria EAL4+. [17], [27] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | - | no evidence found (No source found for industrial software compatibility certifications from Siemens, Honeywell, or ABB.) |

---

## 4. Notable Strengths

- **Identity-based policy engine (items 2.1, 3.3):** Gateway and Access policies can be built entirely on identity attributes (user email, groups, SAML/OIDC claims, device posture) rather than IP/VLAN, and enforcement works through both an on-device client and agentless network on-ramps (cloudflared tunnels, DNS-only locations) [2][3][4][1][22].
- **Globally redundant control plane (items 7.1, 7.2):** the 300+ PoP anycast network routes clients to the nearest healthy PoP with built-in redundancy and failover, and clients keep locally cached policies that continue enforcing when management systems are unreachable [8][13]; PeerSpot reviewers rate stability between eight and ten out of ten [26].
- **SIEM/automation readiness (items 5.2, 5.4):** Logpush exports Zero Trust datasets to third-party SIEM/storage destinations including Splunk and IBM QRadar, and the whole Zero Trust configuration is manageable through the Cloudflare API and Terraform, including a read-only dashboard mode [5][23][12][24].
- **Traffic visibility and threat intelligence (items 1.1, 6.2):** Gateway records DNS, HTTP, and network sessions for all proxied traffic, Network Flow analyzes router/cloud flow data (NetFlow v5/v9, IPFIX, sFlow), and IDS monitors traffic against known threat signatures using Cloudflare's global threat intelligence [6][5][15][13][1].

## 5. Notable Gaps / Risks

- **Not a host-agent microsegmentation platform (items 1.1, 1.2, 3.4):** flow visibility depends on traffic being routed through Cloudflare on-ramps; there is no in-datacenter agent auto-discovering workload-to-workload flows, no dependency map grouped by environment/role/process, and no documented support for fully air-gapped networks since policy enforcement is cloud-based [6][15][20].
- **No Windows Server support (item 3.1):** the Cloudflare One Client explicitly does not run on Windows Server, and AIX/Solaris are not mentioned, which rules out the classic server OS estate the checklist targets [7].
- **No FIPS or Common Criteria certification (item 8.1):** the NIST CMVP validated-modules search for "cloudflare" returns no entries, and Cloudflare's compliance documentation names PCI, SOC 2, and ISO but not FIPS 140-2/140-3 or Common Criteria EAL4+ [27][17].
- **Unquantified operational metrics (items 1.3, 3.5, 4.1, 4.2, 4.3):** log retention, workload scale, and agent CPU/RAM/latency are either undocumented or only qualitatively described (Logpush long-term storage, "thousands of users", review reports of improved latency), so the numeric thresholds in the checklist cannot be confirmed [19][5][26].
- **Missing policy-management conveniences (items 2.2, 2.3, 2.4):** no AI/ML policy recommendation, no full policy simulation/dry-run engine (only a DNS policy test procedure), and no one-click instant policy rollback are documented [22].

## 6. Evidence Quality Notes

Evidence was staged from 27 sources (25 vendor docs, 1 community review site, 1 third-party encyclopedia entry, 1 government registry) yielding 55 grounded quotes. Only 4 items (3.5, 6.4, 7.1, 8.1) were triangulated across two or more source types; the remaining non-unknown items rest on vendor documentation only, which caps confidence at medium per the project's validator rule. The vendor docs used are the official developers.cloudflare.com pages for Cloudflare One (staged April-July 2026 revisions), so claims reflect the current documented product state.

The most load-bearing verdicts are supported by independent or registry evidence: 7.1 (HA) combines the vendor's Business Continuity Guide with PeerSpot stability reviews; 6.4 (transport encryption) combines vendor client-architecture and mTLS docs with Wikipedia's independent description of WARP's WireGuard implementation; 8.1 (certification) rests on the NIST CMVP registry search, which returned zero Cloudflare modules. No contradictions between sources surfaced; where sources were silent on a checklist dimension (e.g., 2.2 AI recommendation, 3.4 air-gapped, 4.1/4.2 resource figures, 5.3 ServiceNow CMDB, 8.2 OT certifications), the item was marked unknown with empty evidence rather than inferred unsupported.

---

## Bibliography

[1] Cloudflare, Inc.. "Cloudflare One documentation overview". https://developers.cloudflare.com/cloudflare-one/ (Retrieved: 2026-08-10T13:55:15Z)
[2] Cloudflare, Inc.. "Cloudflare One docs - Network policies". https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/ (Retrieved: 2026-08-10T13:55:15Z)
[3] Cloudflare, Inc.. "Cloudflare One docs - Identity-based policies". https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/ (Retrieved: 2026-08-10T13:55:15Z)
[4] Cloudflare, Inc.. "Cloudflare One docs - Access policies". https://developers.cloudflare.com/cloudflare-one/access-controls/policies/ (Retrieved: 2026-08-10T13:55:15Z)
[5] Cloudflare, Inc.. "Cloudflare One docs - Logpush integration". https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/ (Retrieved: 2026-08-10T13:55:15Z)
[6] Cloudflare, Inc.. "Cloudflare One docs - Gateway activity logs". https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/ (Retrieved: 2026-08-10T13:55:15Z)
[7] Cloudflare, Inc.. "Cloudflare One docs - Cloudflare One Client known limitations". https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/ (Retrieved: 2026-08-10T13:55:15Z)
[8] Cloudflare, Inc.. "Cloudflare One docs - Business Continuity Guide". https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/business-continuity/ (Retrieved: 2026-08-10T13:55:15Z)
[9] Cloudflare, Inc.. "Cloudflare One docs - Emergency Disconnect". https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/ (Retrieved: 2026-08-10T13:55:15Z)
[10] Cloudflare, Inc.. "Cloudflare One docs - Deploy cloudflared in Kubernetes". https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/ (Retrieved: 2026-08-10T13:55:15Z)
[11] Cloudflare, Inc.. "Cloudflare One docs - Mutual TLS". https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/ (Retrieved: 2026-08-10T13:55:15Z)
[12] Cloudflare, Inc.. "Cloudflare One docs - API and Terraform". https://developers.cloudflare.com/cloudflare-one/api-terraform/ (Retrieved: 2026-08-10T13:55:15Z)
[13] Cloudflare, Inc.. "Cloudflare One docs - Enable Intrusion Detection System". https://developers.cloudflare.com/cloudflare-one/traffic-policies/enable-ids/ (Retrieved: 2026-08-10T13:55:15Z)
[14] Cloudflare, Inc.. "Cloudflare One docs - Application Check posture". https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/application-check/ (Retrieved: 2026-08-10T13:55:15Z)
[15] Cloudflare, Inc.. "Cloudflare docs - Network Flow (formerly Magic Network Monitoring)". https://developers.cloudflare.com/network-flow/ (Retrieved: 2026-08-10T13:55:15Z)
[16] Cloudflare, Inc.. "Cloudflare - Certifications and Compliance Resources". https://www.cloudflare.com/trust-hub/compliance-resources/ (Retrieved: 2026-08-10T13:55:15Z)
[17] Cloudflare, Inc.. "Cloudflare Fundamentals docs - Compliance documentation". https://developers.cloudflare.com/fundamentals/reference/policies-compliances/compliance-docs/ (Retrieved: 2026-08-10T13:55:15Z)
[18] Cloudflare, Inc.. "Cloudflare One docs - Client architecture". https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/ (Retrieved: 2026-08-10T13:55:15Z)
[19] Cloudflare, Inc.. "Cloudflare One docs - Dashboard logs". https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ (Retrieved: 2026-08-10T13:55:15Z)
[20] Cloudflare, Inc.. "Cloudflare One docs - Gateway analytics". https://developers.cloudflare.com/cloudflare-one/insights/analytics/gateway/ (Retrieved: 2026-08-10T13:55:15Z)
[21] Cloudflare, Inc.. "Cloudflare One docs - Tiered policies". https://developers.cloudflare.com/cloudflare-one/traffic-policies/tiered-policies/ (Retrieved: 2026-08-10T13:55:15Z)
[22] Cloudflare, Inc.. "Cloudflare One docs - Test DNS filtering". https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/ (Retrieved: 2026-08-10T13:55:15Z)
[23] Cloudflare, Inc.. "Cloudflare Logs docs - Enable Logpush destinations". https://developers.cloudflare.com/logs/get-started/enable-destinations/ (Retrieved: 2026-08-10T13:55:15Z)
[24] Cloudflare, Inc.. "Cloudflare One docs - Deploy Tunnels with Terraform". https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/terraform/ (Retrieved: 2026-08-10T13:55:15Z)
[25] Wikipedia. "Wikipedia - Cloudflare". https://en.wikipedia.org/wiki/Cloudflare (Retrieved: 2026-08-10T13:55:15Z)
[26] PeerSpot (IT Central Station). "PeerSpot - Cloudflare One reviews". https://www.peerspot.com/products/cloudflare-one-reviews (Retrieved: 2026-08-10T13:55:15Z)
[27] NIST. "NIST CMVP - validated modules search (keyword=cloudflare)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&CertificateStatus=Active&ValidationYear=0&Keyword=cloudflare (Retrieved: 2026-08-10T13:55:15Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 27 (kept: 27, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, community: 1, third_party_review: 1, vendor_doc: 24
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
