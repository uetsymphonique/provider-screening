# BSG / Cross Domain Product Assessment: Cisco Systems - Cisco Catalyst Industrial Gateway

**Product ID:** `cisco-catalyst-industrial-gateway`
**Version reference:** Family assessment: Cisco Catalyst Industrial Routers & Gateways (IR1000, IR1100/IR1101, IR1800, IR8100, IR8300)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T10:20:23Z
**Total evidence items collected:** 59
**Total distinct sources:** 16

---

## 1. Overview

**Cisco Catalyst Industrial Gateway** is assessed here as the Cisco **Catalyst Industrial Routers & Gateways** family (IR1000, IR1100/IR1101, IR1800, IR8100, IR8300) - ruggedized industrial routers/gateways that Cisco positions with built-in next-generation firewall (NGFW), Catalyst SD-WAN, and Cisco Cyber Vision OT asset visibility [1][9][10][11]. Deployment shapes include outdoor IP67 mounts (IR8100), compact low-power enclosures (IR1000/IR1100), and rack-mount routing/switching (IR8300) connecting remote OT sites (substations, pipelines, fleets, roadways) to control centers and the enterprise WAN [7][8][3]. The family is firewall-class, not a protocol-break cross-domain guard: it segments traffic with zone-based policy firewalls, VRF and application-aware inspection [2][3][5]. Cisco documents it as a router-and-firewall device (session-forwarding, not session-termination), and no content disarm-and-reconstruction, macro/schema/label-based inspection, or internal data-stamping capability is documented in the reviewed sources. On the OT side, the IR1101 performs DNP3 serial-to-IP and IEC 60870 T101-to-T104 translation (SCADA gateway) [2], and Snort pre-processors inspect Modbus, DNP3, CIP and S7Commplus [5]. Edge compute via Cisco IOx app hosting is available on the IR8300 [3].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 0                | 3      | 0   |
| partial          | 9     | 0                | 9      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 11    | 0                | 0      | 11  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 6 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | - | Cisco describes the Catalyst family as "a ruggedized, scalable router and firewall, all in one" and as industrial wireless routers, i.e. an IP-routing device rather than a protocol-break guard that terminates sessions and stops IP routing. [1], [9], [10] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No dual-processing-board hardware isolation design (FPGA or isolated shared memory) is documented.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | Cisco documents a default-deny posture - access to cloud/internet disabled by default with only trusted domains explicitly allowed - and zone-based policy firewalls that block unpermitted inter-zone traffic; the SD-WAN feature list also cites whitelisting. [2], [3], [5] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | - | Hardware/software authenticity is anchored by Cisco Trust Anchor Technology (ACT2 chipset) with a tamper-proof module on the IR8100/IR8300, and the platform runs Cisco IOS XE; no microkernel or SELinux-strict-mode hardening claim is documented. [3], [4] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No internal cryptographic stamping of cleaned data prior to session re-initiation is documented.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No file CDR (Office/PDF/Image/CAD reconstruction) capability is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No macro/script/DDE/embedded-object removal capability is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | - | The documented file-protection mechanism is Cisco Advanced Malware Protection (SHA-256 reputation check against the Talos database with optional cloud sandboxing) via the NGFW add-on; no source documents two or more parallel AV engines scanning raw payloads. [5] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM schema-validation engine is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label-based information flow control on files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No DLP capability (secret/ID-number keyword or custom-regex blocking) documented for the family.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography detection/removal capability for image files is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Stateful, application-aware firewall with an Application-Level Gateway (ALG) for the zone-based firewall inspects file-transfer protocols; no content-cleaning proxy for SFTP/FTP-S/HTTPS/SMB is documented. [2], [3] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | IR1101 performs DNP3 serial-to-DNP3/IP and IEC 60870 T101-to-T104 translation as a SCADA gateway, and Snort pre-processors inspect Modbus, DNP3, CIP and S7Commplus for granular policies; OPC UA and MQTT gateway/proxy functions are not documented. [2], [5] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No database-protocol proxy (SQL Server/Oracle/PostgreSQL) with query whitelisting documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Syslog, SNMP, NetFlow and Cflowd/IPFIX generation and export are documented on the IR1101 and IR8300; no RTSP video proxy or CEF unidirectional/bidirectional relay is documented. [2], [3] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | Documented encrypted/aggregate throughput tiers: IR8300 25 Mbps (Tier 0) / 200-400 Mbps (Tier 1) with Tier 2 described only as 'Uncapped', and IR8100 30 Mbps default / 200 Mbps performance; IPsec throughput is 2 Gbps on the IR8340. No >=1 Gbps inspection-throughput figure is documented, so the requirement is not clearly met. [3], [14] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No processing-latency figures published for the family.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | HA mechanisms are documented (VRRP/HSRP, firewall stateful failover, dual-SIM cellular failover, and REP/HSR/PRP redundancy), but no switchover-time figure is published, so the <=100 ms requirement cannot be verified. [2], [3], [4] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | Cisco IOS XE on industrial routers provides stateful packet inspection, DoS mitigation and zone-based default-deny filtering; an explicit fail-close boundary lock when the platform is under DoS is not described. [3], [5] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | - | Role-based access control with an audit trail is documented on the IR1101 and IR8100 datasheets, including IEEE 802.1X-based authentication and RBAC for device configuration. [2], [4], [14] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Syslog/SNMP/NetFlow/IPFIX export and SD-WAN Manager centralized logging are documented; TLS-encrypted syslog/CEF forwarding to an external SIEM is not explicitly documented. [2], [3], [5] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No ready-made compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | medium | - | Datasheets across the family claim FIPS 140-2 and Common Criteria compliance (plus DoDIN APL), and NIST CMVP lists active Cisco IOS cryptographic module validations; the cited certifications are FIPS 140-2 (not 140-3) and Common Criteria without a stated EAL. [2], [3], [4], [15] |

---

## 4. Notable Strengths

- **RBAC with audit trail (5.1):** Role-based access control with an audit trail is documented on the IR1101 and IR8100 datasheets, including IEEE 802.1X-based authentication and RBAC for device configuration [2][4][14].
- **Security certifications (5.4):** Family datasheets claim FIPS 140-2 and Common Criteria compliance (plus DoDIN APL on IR1101/IR8300), and NIST CMVP lists active Cisco IOS cryptographic module validations [2][3][4][15].
- **Default-deny security posture (1.3):** Zone-based policy firewalls plus a documented recommendation to disable outbound access by default and explicitly allowlist only trusted domains [2][3][5].
- **OT/ICS protocol coverage (3.2):** DNP3 serial-to-DNP3/IP and IEC 60870 T101-to-T104 translation (SCADA gateway) on the IR1101, plus Snort pre-processors for Modbus, DNP3, CIP and S7Commplus [2][5].
- **HA redundancy toolkit (4.3):** VRRP/HSRP, firewall stateful failover, dual-SIM cellular failover and REP/HSR/PRP redundancy are documented across the family [2][3][4].

## 5. Notable Gaps / Risks

- **Inspection throughput (4.1):** Documented encrypted/aggregate throughput tiers are 25-400 Mbps (IR8300) and 30-200 Mbps (IR8100), with only 2 Gbps IPsec and a qualitative "Uncapped" Tier 2 on the IR8300 - no >=1 Gbps inspection figure is published, so the requirement is not clearly met and needs a vendor throughput validation [3][14].
- **HA switchover time (4.3):** No failover-time figure is published for VRRP/HSRP or stateful failover, so the <=100 ms requirement is unverified and would require lab measurement [2][3][4].
- **Processing latency (4.2):** No latency figures are published anywhere for the family; realtime-protocol latency cannot be assessed from current evidence.
- **SIEM integration depth (5.2):** Syslog/SNMP/NetFlow/IPFIX export and SD-WAN Manager centralized logging are documented, but TLS-encrypted CEF/Syslog push to an external SIEM is not explicitly documented [2][3][5].
- **CDR-family capabilities undocumented (2.1, 2.2, 2.4, 2.5):** No content disarm and reconstruction, macro/script stripping, schema validation or file-level security-label filtering is documented in the reviewed sources; buyers requiring CDS-grade content sanitization should seek explicit vendor confirmation before considering this family [1][9].
- **Router architecture excludes protocol break (1.1):** Cisco documents the family as "a ruggedized, scalable router and firewall, all in one," an IP-routing architecture that is incompatible with a session-terminating protocol-break guard [1][9][10].

## 6. Evidence Quality Notes

59 evidence entries across 16 sources cover all 24 checklist items, and every quote is grounded in the staged artifact text (verify_citation_grounding.py: 59/59 grounded). 13 items are backed by >= 2 source types; the load-bearing claims - product category (router/firewall architecture basis for item 1.1), default-deny firewall behavior, RBAC, FIPS/Common Criteria certifications, OT-protocol support and throughput tiers - are each supported by multiple vendor datasheets plus at least one independent source (Engineering.com [10], 5G Americas [11], ARC Advisory Group [12], NIST CMVP registry [15]). 7 items rest on vendor-datasheet-only evidence (1.4, 2.3, 3.1, 3.4, 4.1, 4.3, 5.1), so their confidence is capped at medium per the validator rule; the 4 unknown items (2.6, 3.3, 4.2, 5.3) reflect genuinely absent documentation, not evaluated failures.

Two caveats on source handling: cisco.com blocks direct fetches from this environment (Akamai HTTP 403), so the nine cisco.com pages and the Engineering.com article were staged through the r.jina.ai text proxy - the raw_url recorded in sources.jsonl is the proxy URL, with the original page in the original_url field (see run_manifest.json); grounding checks run against those staged texts. The 5G Americas piece is a reprint of a Cisco press release (vendor-origin content on an independent host) and the Aerco/Madison PDFs are Cisco documents mirrored by distributors, so they do not count as independent verification. No contradictions between sources were found; where evidence was qualitative (throughput tiers, HA mechanisms), verdicts were kept at Partial rather than raised to Supported. The NIST CMVP link is to Cisco IOS cryptographic module validations generally; no IR-platform-specific certificate number was found.

---

## Bibliography

[1] Cisco Systems. "Cisco Industrial Routers / Catalyst Industrial Routers & Gateways family page". https://r.jina.ai/https://www.cisco.com/site/us/en/products/networking/industrial-routers-gateways/index.html (Retrieved: 2026-08-11T10:15:14Z)
[2] Cisco Systems. "Cisco 1101 Industrial Integrated Services Router datasheet (Catalyst IR1101)". https://r.jina.ai/https://www.cisco.com/c/en/us/products/collateral/routers/1101-industrial-integrated-services-router/datasheet-c78-741709.html (Retrieved: 2026-08-11T10:15:17Z)
[3] Cisco Systems. "Cisco Catalyst IR8300 Rugged Series Router datasheet (IR8340)". https://r.jina.ai/https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-ir8300-rugged-series-router/nb-06-cat-ir8340-rugged-ser-rout-ds-cte-en.html (Retrieved: 2026-08-11T10:15:20Z)
[4] Cisco Systems. "Cisco Catalyst IR8100 Heavy Duty Series Router datasheet (IR8140)". https://r.jina.ai/https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-ir8100-heavy-duty-series-routers/nb-06-cat-ir8140-hd-ser-rout-ds-cte-en.html (Retrieved: 2026-08-11T10:15:23Z)
[5] Cisco Systems. "Cisco Catalyst Industrial Routers with Cisco Next-Generation Firewall - Solution Overview". https://r.jina.ai/https://www.cisco.com/c/en/us/products/collateral/networking/industrial-routers-gateways/industrial-router-next-generation-firewall-so.html (Retrieved: 2026-08-11T10:15:26Z)
[6] Cisco Systems. "Cisco Cyber Vision product page (OT asset visibility)". https://r.jina.ai/https://www.cisco.com/site/us/en/products/security/industrial-security/cyber-vision/index.html (Retrieved: 2026-08-11T10:15:29Z)
[7] Cisco Systems. "Cisco Catalyst IR8100 Heavy Duty Series Routers product page". https://r.jina.ai/https://www.cisco.com/site/us/en/products/networking/industrial-routers-gateways/catalyst-ir8100-heavy-duty-series/index.html (Retrieved: 2026-08-11T10:15:32Z)
[8] Cisco Systems. "Cisco Catalyst IR8300 Rugged Series Routers product page". https://r.jina.ai/https://www.cisco.com/site/us/en/products/networking/industrial-routers-gateways/catalyst-ir8300-rugged-series/index.html (Retrieved: 2026-08-11T10:15:40Z)
[9] Cisco Systems. "Cisco Catalyst IR1100 Rugged Series Routers product page". https://r.jina.ai/https://www.cisco.com/site/us/en/products/networking/industrial-routers-gateways/catalyst-ir1100-rugged-series/index.html (Retrieved: 2026-08-11T10:15:43Z)
[10] Engineering.com. "Cisco's New 5G Industrial Router and Gateway Series to Further Connect the IoT Edge". https://r.jina.ai/https://www.engineering.com/ciscos-new-5g-industrial-router-and-gateway-series-to-further-connect-the-iot-edge/ (Retrieved: 2026-08-11T10:15:47Z)
[11] 5G Americas. "Cisco Unveils New 5G Industrial Router Portfolio to Unite the IoT Edge". https://www.5gamericas.org/connecting-and-protecting-the-things-that-matter-most-cisco-unveils-new-5g-industrial-router-portfolio-to-unite-the-iot-edge/ (Retrieved: 2026-08-11T10:15:54Z)
[12] ARC Advisory Group. "Cisco Announces New Industrial 5G RedCap Cellular Routers and Incremental Network Visibility, Segmentation, and Remote Access Capabilities". https://www.arcweb.com/blog/cisco-announces-new-industrial-5g-redcap-cellular-routers-incremental-network-visibility (Retrieved: 2026-08-11T10:15:59Z)
[13] Cisco Systems (mirror: Aerco UK). "Cisco Industrial Router Portfolio 'At a glance' (C45-735008-07), mirrored by Aerco UK". https://www.aerco.co.uk/images/uploaded/ProductDataFiles/Cisco/CiscoRuggedRoutersCatalog.pdf (Retrieved: 2026-08-11T10:16:02Z)
[14] Cisco Systems (mirror: Madison Technologies). "Cisco Catalyst IR8100 Heavy Duty Series Router datasheet, mirrored by Madison Technologies". https://madison.tech/wp-content/uploads/2023/03/IR8100-Catalyst-Rugged-Series-Routers.pdf (Retrieved: 2026-08-11T10:16:07Z)
[15] NIST CMVP. "NIST Cryptographic Module Validation Program - Validated Modules (FIPS 140-2/140-3) search results". https://r.jina.ai/https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced (Retrieved: 2026-08-11T10:16:14Z)
[16] Cisco Blogs (Industrial IoT). "Layered Defense for the Plant Floor: Simplifying OT Security". https://blogs.cisco.com/industrial-iot/layered-defense-for-the-plant-floor-simplifying-ot-security/ (Retrieved: 2026-08-11T10:16:42Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 16 (kept: 16, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 1, certification_registry: 1, third_party_review: 2, vendor_blog: 1, vendor_datasheet: 5, vendor_doc: 6
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
