# Microsegmentation Product Assessment: Extreme Networks - Extreme Fabric Connect

**Product ID:** `extreme-fabric-connect`
**Version reference:** Fabric Engine v9.3 (September 2025) User Guide and Release Notes; ExtremeCloud IQ (New) v25.11.0 User Guide; ExtremeAnalytics 8.4; CMVP certificates 4887/4291; CC portal entry for Fabric Engine Switches v9.1.100 (2026-06-02)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T17:08:50Z
**Total evidence items collected:** 58
**Total distinct sources:** 41

---

## 1. Overview

Extreme Fabric Connect is an agentless, network-fabric segmentation technology built on Extreme's extended implementation of the IEEE 802.1aq Shortest Path Bridging (SPB) standard [34]. It provisions Layer 2 and Layer 3 "circuit-based" services identified by I-SIDs over a MAC-in-MAC encapsulated, IS-IS-driven fabric, segmenting users, guests, IoT and other services with an Ethernet-centric, IP-invisible stealth design [29, 34]. Edge devices attach automatically via Fabric Attach (LLDP element discovery) and auto-sense ports, with RADIUS/NAC-driven assignment of VLAN/I-SID mappings and ACL policy [3, 4]. Extreme positions it as a unified, automated and secure network solution spanning data center, campus, branch and WAN (Fabric Extend over VXLAN or IPsec), managed by ExtremeCloud IQ and ExtremeCloud IQ Site Engine [1, 31, 32]. Deployment shapes include wired/wireless access, data center, remote offices and industrial edge (ISW switches with Fabric Attach) [1, 31, 40].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 1                | 4      | 0   |
| partial          | 15    | 0                | 15     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 8     | 0                | 8      | 0   |

**Evidence quality:** 9 items backed by ≥ 2 source_types; 25 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **3.1:** Fabric Connect is a network-layer fabric with no endpoint software; any FA-capable device (switch, server, WLAN AP, camera) attaches at the network layer regardless of operating system, so a per-OS agent matrix does not apply.
- **4.1:** Fabric Connect deploys no endpoint agent; enforcement happens in the network fabric, so an agent CPU-overhead figure does not apply.
- **4.2:** No endpoint agent exists, so an agent RAM footprint does not apply.
- **4.3:** Segmentation is enforced in the fabric at documented wire speed with no agent in the data path, so an added-latency threshold for agent enforcement does not apply.
- **4.4:** No endpoint agent exists, so an agent crash fail-open/fail-closed consideration does not apply.
- **4.5:** No host agents are installed; Fabric Attach devices are provisioned zero-touch at the network edge, so reboot-free agent install/update does not apply.
- **6.1:** Enforcement operates at the network service level (I-SID circuits, MAC-in-MAC, Ethernet-centric fabric) with no endpoint agent, so process-level enforcement does not apply.
- **6.4:** There is no agent-to-controller channel; fabric control signaling (IS-IS / Fabric Attach) is authenticated with HMAC-SHA256, so an agent-to-controller TLS/mutual-auth requirement does not apply.

---

## 3. Per-Item Verdicts

### Category 1 — Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | high | — | The fabric self-forms and self-provisions, auto-sense ports detect and dynamically configure attached devices, Fabric Attach performs element discovery over LLDP, ExtremeAnalytics collects and aggregates flow data, and Tolly's evaluation documents device discovery. [1], [4], [8], [21], [36] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | — | ExtremeAnalytics provides Layer 7 application visibility and Site Engine provides end-to-end network visibility and fabric monitoring, but no role- or process-level map view is documented. [21], [29] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Partial | medium | n/a (qualitative) | Extreme Management Center flow-data retention is configurable in the ExtremeAnalytics Data Retention setting, but no default retention of at least 90 days is documented. [21] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | — | no evidence found (No evidence of vulnerability/CVE context on the map found in staged sources.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Partial | medium | — | Auto-sense ports detect IP phones, IoT devices and client PCs and the security blog describes auto-sensing of devices connected to the network, but a distinct unrecognized-traffic alerting function is not documented. [4], [29] |

### Category 2 — Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Partial | medium | — | Fabric Attach devices are authorized and attached to network service instances automatically based on policy, RADIUS/NAC assigns VLAN/I-SID mappings and ACL/policy from credentials, and Fabric Connect provisions circuit-based I-SID services; policies are network-service based rather than per-workload tags. [3], [4], [34] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Unknown | low | — | no evidence found (ExtremeCloud IQ CoPilot provides AIOps with Explainable ML, but staged sources do not describe automated segmentation rule recommendations.) |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Unknown | low | — | no evidence found (No policy simulation / dry-run capability found in staged sources.) |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Partial | medium | — | ExtremeCloud IQ automatically rolls a device configuration back to the last known good state when a device cannot reconnect after an update, but an instant one-click policy rollback is not documented. [32] |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Unknown | low | — | no evidence found (No inherited/hierarchical policy rule model found in staged sources (fabric supports up to 2 SPB IS-IS areas, which is network hierarchy, not policy hierarchy).) |

### Category 3 — Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | N/A | medium | — | Fabric Connect is a network-layer fabric with no endpoint software; any FA-capable device (switch, server, WLAN AP, camera) attaches at the network layer regardless of operating system, so a per-OS agent matrix does not apply. [3], [29] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Partial | medium | — | The hardware VXLAN Gateway (VTEP) and OVSDB-managed interfaces connect VXLAN/overlay segments to Fabric Connect I-SIDs, enabling virtualized/container overlay integration, but native Kubernetes/OpenShift isolation is not documented. [13], [14] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Partial | medium | — | Segmentation is enforced in the network fabric itself (SPBM/IS-IS, MAC-in-MAC, multiple virtual networks over one infrastructure) with no endpoint agent; an agent-based enforcement mode is not offered. [5], [29] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Supported | medium | — | ExtremeCloud IQ devices can operate in an on-premises operating mode and Site Engine provides on-premises management, and the fabric control plane (IS-IS) runs on the switches themselves, so the fabric and management can run without Internet. [32], [37] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | Documented scale is per-switch (up to 2,000 SPBM nodes per area, up to 120,000 SPBM MAC addresses and 4,000 I-SIDs on large platforms) and marketing cites tens of thousands of switches per fabric, but no source states an explicit workload count of 50,000 or more. [1], [17], [19] |

### Category 4 — Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | N/A | medium | — | Fabric Connect deploys no endpoint agent; enforcement happens in the network fabric, so an agent CPU-overhead figure does not apply. [29] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | N/A | medium | — | No endpoint agent exists, so an agent RAM footprint does not apply. [5] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | N/A | medium | — | Segmentation is enforced in the fabric at documented wire speed with no agent in the data path, so an added-latency threshold for agent enforcement does not apply. [40] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | N/A | medium | — | No endpoint agent exists, so an agent crash fail-open/fail-closed consideration does not apply. [1] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | N/A | medium | — | No host agents are installed; Fabric Attach devices are provisioned zero-touch at the network edge, so reboot-free agent install/update does not apply. [3] |

### Category 5 — Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | — | ExtremeCloud IQ exposes a comprehensive OpenAPI REST API, Fabric Engine switches expose on-switch RESTCONF with token authentication, and XMC offers GraphQL/REST APIs, but no source claims 100% administrative coverage. [22], [24], [38] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Partial | medium | — | ExtremeAnalytics can stream flow data to Splunk (IPFIX), ExtremeCloud IQ supports syslog server profiles, and Site Engine workflows can trigger on syslog messages or traps; QRadar/Sentinel integrations are not documented. [21], [32], [37] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Supported | medium | — | ExtremeCloud IQ Site Engine offers an open northbound API for ServiceNow and alarm-triggered workflows that open ServiceNow tickets populated with network event data. [37] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Partial | medium | — | Extreme publishes an Ansible collection for Fabric Engine and Site Engine automates network tasks via Python-script workflows, but no Jenkins/GitLab/Terraform pipeline integration is documented. [37], [39] |

### Category 6 — Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | N/A | medium | — | Enforcement operates at the network service level (I-SID circuits, MAC-in-MAC, Ethernet-centric fabric) with no endpoint agent, so process-level enforcement does not apply. [29], [34] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Partial | medium | — | ExtremeAnalytics' IP Reputation dashboard flags flows against Emerging Threats/CiArmy reputation feeds, but no honeypot/deception capability is documented. [21] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | — | PCI DSS support is documented (Fabric Connect plus Extreme Control enforcing PCI requirements 3/5/7/8/10), ExtremeCloud IQ holds ISO/IEC 27001 certification, and Platform ONE is positioned as identity-based zero trust; NIST 800-207 and IEC 62443 are not explicitly named. [33], [34], [35] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | N/A | medium | — | There is no agent-to-controller channel; fabric control signaling (IS-IS / Fabric Attach) is authenticated with HMAC-SHA256, so an agent-to-controller TLS/mutual-auth requirement does not apply. [10] |

### Category 7 — High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | — | The SPB control plane is distributed across all fabric switches (IS-IS, no central controller) and ExtremeCloud IQ documents an on-premises appliance-cluster management option, so there is no single controller point of failure. [5], [32] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | — | The fabric self-forms and self-provisions from a seed switch with a Zero-Touch Core, so forwarding and segmentation continue without any management-plane involvement. [3], [4] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Partial | medium | — | Fabric Extend connects remote sites and data centers over VXLAN or IPsec WAN tunnels and Tolly's evaluation documents Site Engine configuration backup/restore, but an explicit DR site-sync replication feature is not documented. [31], [36] |

### Category 8 — Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | — | NIST CMVP lists Extreme Networks Cryptographic Provider 3 (FIPS 140-3, level 1) and the SLX 9540/9740 switches (FIPS 140-2), and the CC portal lists Extreme Networks Fabric Engine Switches v9.1.100 as Common Criteria certified (NIAP, collaborative Protection Profile for Network Devices v3.0e, 2026-06-02); no explicit EAL4+ claim is made. [25], [27], [28] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Unknown | low | — | no evidence found (No evidence of Siemens/Honeywell/ABB compatibility certifications found in staged sources.) |

---

## 4. Notable Strengths

- **Zero-touch auto-discovery and provisioning (items 1.1, 1.5):** Auto-sense ports detect attached devices and apply configuration dynamically, Fabric Attach performs LLDP element discovery, and Tolly's evaluation documents Site Engine device discovery [1, 4, 8, 36].
- **Service-based, stealth segmentation (items 2.1, 6.1, 6.3):** Circuit-based I-SID services with strictly controlled reachability support PCI-DSS-aligned network separation, and RADIUS/NAC assigns per-credential VLAN/I-SID and ACL policy [3, 4, 34].
- **Distributed, self-forming control plane (items 7.1, 7.2):** The SPB IS-IS control plane runs on every fabric switch with a Zero-Touch Core, so forwarding and segmentation continue without management-plane involvement [3, 4, 5].
- **Air-gapped and on-premises operation (item 3.4):** Devices can run in an on-premises operating mode and Site Engine provides on-premises management, with no cloud dependency for fabric operation [32, 37].
- **Independent security certifications (item 8.1):** NIST CMVP lists FIPS 140-3 (certificate 4887) and FIPS 140-2 (certificate 4291) modules, and Extreme Networks Fabric Engine Switches v9.1.100 is Common Criteria certified under NIAP [25, 27, 28].

## 5. Notable Gaps / Risks

- **No endpoint agent (items 3.1, 4.1-4.5, 6.1, 6.4):** Segmentation is enforced only at the network-service level, so process-level enforcement, per-host agent metrics and agent fail-safe behavior do not apply; buyers needing workload-host control must pair the fabric with an agent-based product [5, 29].
- **Scale target unquantified (item 3.5):** Documented limits are per-switch (up to 2,000 SPBM nodes per area, 120,000 SPBM MACs and 4,000 I-SIDs on large platforms), with no explicit 50,000-workload figure; a sizing and validation exercise is needed before committing [17, 19].
- **No policy simulation, one-click policy rollback or AI rule recommendation (items 2.2, 2.3, 2.4):** CoPilot AIOps and automatic device-configuration rollback exist, but segmentation-rule simulation and instant policy rollback are not documented; a policy dry-run/rollback workflow would close the gap [32].
- **Forensic retention unverified (item 1.3):** XMC flow-data retention is configurable but no default of at least 90 days is documented; retention must be set and verified explicitly for forensic needs [21].
- **Container and OT gaps (items 3.2, 8.2):** Only VXLAN/OVSDB gateway integration is documented for virtualized overlays (no native Kubernetes/OpenShift isolation), and no Siemens/Honeywell/ABB compatibility certifications were found [13, 14].

## 6. Evidence Quality Notes

58 evidence entries were collected from 41 distinct sources. Only one source is genuinely non-vendor (the Tolly Group interoperability evaluation, tagged third_party_review), alongside four certification-registry sources (NIST CMVP and the Common Criteria portal); the remaining 36 are vendor documentation, marketing pages and vendor blogs. Nine items are backed by two or more source types; 25 items rest on vendor-only sources, which caps their confidence at medium per the validator rule. No contradictions between sources were observed.

Items with numeric thresholds (1.3 flow retention, 3.5 workloads) were kept partial because sources give configurable or per-switch numbers but no explicit 90-day retention or 50,000-workload figure; agent-related numeric items (4.1-4.3) are not_applicable because no endpoint agent exists. The eight not_applicable items carry network-enforcement evidence from the staged documentation rather than being asserted from silence, and the five items with no evidence at all (1.4, 2.2, 2.3, 2.5, 8.2) are unknown with empty evidence per the anti-fabrication contract.

---

## Bibliography

[1] Extreme Networks. "Extreme Fabric Connect product page". https://www.extremenetworks.com/solutions/network-fabric/fabric-connect (Retrieved: 2026-08-10T17:08:26Z)
[2] Extreme Networks. "Securely Connect Everyone, Everywhere (Extreme Fabric + Site Engine landing)". https://www.extremenetworks.com/learn/securing-your-network-fabric (Retrieved: 2026-08-10T17:08:26Z)
[3] Extreme Networks. "Fabric Attach Network Automation whitepaper". https://www.extremenetworks.com/resources/white-paper/fabric-attach-network-automation (Retrieved: 2026-08-10T17:08:26Z)
[4] Extreme Networks (blog). "5 Fabric Connect Features You Might Not be Using". https://www.extremenetworks.com/resources/blogs/fabric-connect-features (Retrieved: 2026-08-10T17:08:26Z)
[5] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - Basic SPBM Network Topology". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/basic_spbm_network_topology.shtml (Retrieved: 2026-08-10T17:08:26Z)
[6] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - Fabric Attach". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_fabricattach.shtml (Retrieved: 2026-08-10T17:08:26Z)
[7] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - Fabric Attach Components". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_fabricattachcomponents.shtml (Retrieved: 2026-08-10T17:08:26Z)
[8] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - FA Element Discovery". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_fabricattach_elementdiscovery.shtml (Retrieved: 2026-08-10T17:08:26Z)
[9] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - FA Zero Touch Client Attachment". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_fa_zerotouch.shtml (Retrieved: 2026-08-10T17:08:26Z)
[10] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - FA message authentication and integrity protection". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_fabricattach_messageauthentication_and_integrityprotection.shtml (Retrieved: 2026-08-10T17:08:26Z)
[11] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - FA Data Processing". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_fabricattach_dataprocessing_forvoss.shtml (Retrieved: 2026-08-10T17:08:26Z)
[12] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - SPBM Restrictions". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/spbm_restrictions_and_limitations.shtml (Retrieved: 2026-08-10T17:08:26Z)
[13] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - Configure OVSDB Managed Interfaces". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_ovsdb_vxlan_configuringovsdbmanagedinterfacescli.shtml (Retrieved: 2026-08-10T17:08:26Z)
[14] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - VXLAN Gateway Fundamentals". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/vspcommon_vxlan_gateway_fundamentals.shtml (Retrieved: 2026-08-10T17:08:26Z)
[15] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - Configure SPBM Layer 2 VSN". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/configuring_spbm_layer_2_vsn.shtml (Retrieved: 2026-08-10T17:08:26Z)
[16] Extreme Networks (documentation). "Fabric Engine v9.3 User Guide - Inter-VSN Routing with SPBM Configuration Example". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20User%20Guide/fe_9.3_ug_revacdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_user_guide/inter_vsn_routing_with_spbm_configuration_example.shtml (Retrieved: 2026-08-10T17:08:26Z)
[17] Extreme Networks (documentation). "Fabric Engine 9.3 Release Notes - Fabric Scaling". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20Release%20Notes/fe_9.3_rn_revafdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_release_notes/topics/fabric_scaling.shtml (Retrieved: 2026-08-10T17:08:26Z)
[18] Extreme Networks (documentation). "Fabric Engine 9.3 Release Notes - Number of I-SIDs Supported". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20Release%20Notes/fe_9.3_rn_revafdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_release_notes/topics/i_sids_supported.shtml (Retrieved: 2026-08-10T17:08:26Z)
[19] Extreme Networks (documentation). "Fabric Engine 9.3 Release Notes - Layer 2 maximums". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20Release%20Notes/fe_9.3_rn_revafdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_release_notes/topics/layer_2.shtml (Retrieved: 2026-08-10T17:08:26Z)
[20] Extreme Networks (documentation). "Fabric Engine 9.3 Release Notes - Recommendations". https://documentation.extremenetworks.com/Fabric%20Engine%20v9.3%20Release%20Notes/fe_9.3_rn_revafdev/content/documents/Switch_Operating_Systems/VOSS_and_Fabric_Engine/fabric_engine_release_notes/topics/fabric_recommendations.shtml (Retrieved: 2026-08-10T17:08:26Z)
[21] Extreme Networks (documentation). "ExtremeAnalytics 8.4 User Guide (PDF)". https://documentation.extremenetworks.com/netsight/8.4/ExtremeAnalytics_8.4_ExtremeAnalytics_User_Guide.pdf (Retrieved: 2026-08-10T17:08:26Z)
[22] Extreme Networks (documentation). "Fabric Engine and VOSS 9.3 RESTCONF API Guide - RESTCONF APIs". https://documentation.extremenetworks.com/Fabric%20Engine%20and%20VOSS%20v9.3%20RESTCONF%20API%20Guide/Switch_Operating_Systems/VOSS_and_Fabric_Engine/restconf_developer_guide/topics/APIs.shtml (Retrieved: 2026-08-10T17:08:26Z)
[23] Extreme Networks (documentation). "Fabric Engine and VOSS 9.3 RESTCONF API Guide - Authentication". https://documentation.extremenetworks.com/Fabric%20Engine%20and%20VOSS%20v9.3%20RESTCONF%20API%20Guide/Switch_Operating_Systems/VOSS_and_Fabric_Engine/restconf_developer_guide/topics/Authentication.shtml (Retrieved: 2026-08-10T17:08:26Z)
[24] Extreme Networks (documentation). "Extreme API with Python (PDF)". https://documentation.extremenetworks.com/api_python/Extreme_API.pdf (Retrieved: 2026-08-10T17:08:26Z)
[25] Common Criteria Recognition Arrangement. "Common Criteria Portal - Certified Products list". https://www.commoncriteriaportal.org/products/index.cfm (Retrieved: 2026-08-10T17:08:26Z)
[26] NIST CSRC. "NIST CMVP - Validated modules search for Extreme Networks". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&Vendor=Extreme (Retrieved: 2026-08-10T17:08:26Z)
[27] NIST CSRC. "NIST CMVP Certificate #4887 - Extreme Networks Cryptographic Provider 3". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4887 (Retrieved: 2026-08-10T17:08:26Z)
[28] NIST CSRC. "NIST CMVP Certificate #4291 - Extreme Networks SLX 9540 and SLX 9740 Switches". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4291 (Retrieved: 2026-08-10T17:08:26Z)
[29] Extreme Networks (blog). "How Secure Network Fabric Protects Against Emerging Threats". https://www.extremenetworks.com/resources/blogs/how-secure-network-fabric-protects-against-emerging-threats (Retrieved: 2026-08-10T17:08:26Z)
[30] Extreme Networks (blog). "Unlocking the Real-World Benefits of Secure Network Fabric". https://www.extremenetworks.com/resources/blogs/unlocking-the-real-world-benefits-of-secure-network-fabric (Retrieved: 2026-08-10T17:08:26Z)
[31] Extreme Networks. "The Value of Extending Fabric Connect to Your Remote Offices (solution brief)". https://www.extremenetworks.com/resources/solution-brief/extending-fabric-connect-remote-offices (Retrieved: 2026-08-10T17:08:26Z)
[32] Extreme Networks (documentation). "ExtremeCloud IQ (New) v25.11.0 User Guide (PDF)". https://documentation.extremenetworks.com/ExtremeCloud_IQ_NEW_25_11_0_User_Guide.pdf (Retrieved: 2026-08-10T17:08:26Z)
[33] Extreme Networks (blog). "Extreme Achieves ISO 27001 Certification for ExtremeCloud IQ". https://www.extremenetworks.com/resources/blogs/extreme-achieves-iso-iec-27001-certification-extremecloud-iq (Retrieved: 2026-08-10T17:08:26Z)
[34] Extreme Networks. "Leveraging Stealth Networking to Facilitate PCI-Compliance (solution brief)". https://www.extremenetworks.com/resources/solution-brief/leveraging-stealth-networking-to-facilitate-pci-compliance (Retrieved: 2026-08-10T17:08:26Z)
[35] Extreme Networks. "Zero Trust Security Made Simple: The Extreme Platform ONE Advantage". https://www.extremenetworks.com/resources/report/zero-trust-security-made-simple-extreme-platform-one-advantage (Retrieved: 2026-08-10T17:08:26Z)
[36] The Tolly Group / Extreme Networks. "ExtremeCloud IQ Site Engine Interoperability Evaluation by Tolly (report page)". https://www.extremenetworks.com/resources/report/interoperability-extremecloud-iq-site-engine (Retrieved: 2026-08-10T17:08:26Z)
[37] Extreme Networks. "Integration of ExtremeCloud IQ - Site Engine with ServiceNow (solution brief)". https://www.extremenetworks.com/resources/solution-brief/integration-of-extremecloud-iq-site-engine-with-servicenow (Retrieved: 2026-08-10T17:08:26Z)
[38] Extreme Networks (GitHub). "ExtremeCloud IQ OpenAPI Specification (GitHub README)". https://github.com/ExtremeNetworks/ExtremeCloudIQ-OpenAPI-Specification (Retrieved: 2026-08-10T17:08:26Z)
[39] Extreme Networks (GitHub). "Ansible Collection for Fabric Engine (GitHub README)". https://github.com/ExtremeNetworks/ansible_collections.extreme.fe (Retrieved: 2026-08-10T17:08:26Z)
[40] Extreme Networks. "Industrial Switches (ISW) Series product page". https://www.extremenetworks.com/products/switches/industrial-switches/isw-series (Retrieved: 2026-08-10T17:08:26Z)
[41] Extreme Networks (documentation). "ExtremeCloud IQ v25.2.0 CoPilot Deployment Guide - Welcome". https://documentation.extremenetworks.com/ExtremeCloud%20IQ%20v25.2.0%20CoPilot%20Deployment%20Guide/ExtremeCloud_IQ/XIQ_CoPilot_Deployment_Guide/topics/welcome_to_extremecloud_iq_copilot_container.shtml (Retrieved: 2026-08-10T17:08:26Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 33
- **Sources reviewed:** 41 (kept: 41, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 4, third_party_review: 1, vendor_blog: 4, vendor_doc: 32
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
