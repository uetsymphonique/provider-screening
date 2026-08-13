# BSG / Cross Domain Product Assessment: Toshiba Corporation - Toshiba Industrial Security Gateway (Waterfall Unidirectional Security Gateway)

**Product ID:** `toshiba-industrial-security-gateway`
**Version reference:** Line-up: WF-600, WF-500C, WF-500S (also WF-500SPLIT, Waterfall for IDS); Toshiba gateway pages retrieved 2026-08-11; Toshiba whitepaper 2020.03; Toshiba Solutions leaflet 2019-06; English leaflet 2020-10; Common Criteria certificate for Waterfall WF-500 version 2 issued 2023-05-16
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:20:00Z
**Total evidence items collected:** 58
**Total distinct sources:** 15

---

## 1. Overview

The Toshiba Industrial Security Gateway is the Toshiba-branded distribution of the Waterfall Unidirectional Security Gateway, a hardware-enforced data diode developed by Waterfall Security Solutions Ltd., for which Toshiba states it is the sales agent [1]. Toshiba positions it as the OT/IT boundary security appliance for critical infrastructure - nuclear power, electric power, rail, petrochemical and water sectors - where the control network must keep sending data outward while no traffic, data, command or packet may return [1], [5]. The gateway is therefore a cross-domain-solution-class product (a protocol-break unidirectional gateway), not a conventional firewall: a laser on the transmitter board drives a photocell on the receiver board over an optical link, making reverse communication physically impossible [5], [9]. Deployment shapes are appliance-based: the all-in-one WF-500C and WF-600 (1U, up to 10G interfaces), the modular WF-500S with external agent servers, the chassis-split WF-500SPLIT, and the Waterfall for IDS variant [2], [3], [4], [7]. Connectors replicate historians, databases, files and syslog/SNMP feeds to the business network one-way [5], [7].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 7     | 4                | 3      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 11    | 0                | 0      | 11  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 4 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | high | - | Toshiba markets the product as a data diode / unidirectional security gateway that enforces a physical one-way optical link; the TX unit has only a laser emitter and the RX unit only a photocell, so reverse (RX-to-TX) communication is physically impossible and no TCP/IP session can be re-initiated from the receiving network. [1], [5], [9], [12], [14] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | high | - | The sender and receiver are separate hardware units: a laser on one circuit board drives a photocell on a second board; the WF-500C encloses both sides in one chassis with an internal partition and the WF-500SPLIT uses separate chassis, so the two processing sides are physically isolated. [3], [5], [7], [9] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | - | The hardware is physically unable to send any information back into the source network: no data, command, protocol or packet can flow in from the external side, and even a misconfigured or compromised gateway cannot open an inbound path - only whitelisted connectors replicate data outward. [5], [9], [11], [15] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | - | no evidence found (No hardened-OS / microkernel / SELinux-strict-mode claim was found; gateway security functions are implemented in hardware with agent software hosted on general-purpose Windows/Linux servers per distributor documentation.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No documentation of cryptographic stamping/signing of data before session re-initiation was found in the staged sources.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No content disarm & reconstruction (CDR) capability is documented; the security model is one-way server replication rather than content re-generation, but no source explicitly states the absence of CDR.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No evidence of VBA macro, JavaScript, DDE-link or embedded-object removal in transferred files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No multi-engine antivirus scanning of transferred payloads is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM W3C-schema validation capability is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label / information-flow-control filtering based on file labels is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No DLP keyword/regex data-loss prevention capability is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography detection/removal capability for image files is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | File-transfer connectors replicate files and folders one-way over FTP, TFTP, SFTP, FTPS, RCP and remote CIFS folders; no content-cleaning (disarm) step is documented, so the item is only partially met. [5], [7] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | - | Industrial protocol connectors cover OPC (DA/HDA/A&E/UA), DNP3, ICCP, Modbus, IEC 60870-5-104 and MQTT replication, per the Toshiba whitepaper/leaflets and corroborated by distributor documentation. [1], [5], [7], [11], [14] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | - | Database connectors replicate Microsoft SQL Server, Oracle, MySQL, Postgres and SAP data to the receiving network; query-whitelisting proxy behavior is not documented, so the item is only partially met. [5], [7] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | SYSLOG, SNMP and SIEM feed relays (Splunk, McAfee ESM, HP ArcSight) plus SMTP/TCP/UDP/TimeSync/NTP/multicast IT connectors are documented for one-way delivery; RTSP video proxying and CEF-format relay are not documented, so the item is only partially met. [1], [5] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | Toshiba rates the WF-400 and WF-500C models at 1 Gbps and the WF-600 at 1-10 Gbps with 10GBASE-T/10G fiber interfaces, and an integrator lists 1 Gbps standard throughput; the 1 Gbps (1000 Mbps) rating meets the >=1000 Mbps threshold. [2], [6], [9], [15] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No processing-latency figure is published in any staged source.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | HA/redundancy is documented: duplicated WF-500S appliances and agents, optional HA configurations, Toshiba ClusterPerfect clustering and dual redundant power supplies; no switchover time (e.g. <=100 ms) is published, so the numeric requirement cannot be verified. [4], [7], [8], [9], [15] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | - | The unidirectional hardware is a physical constraint with no inbound path, so denial-of-service against the OT side is impossible - nothing on the external side can send traffic into the OT network through the gateway, and no software misconfiguration can open the boundary. [5], [9] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (No documentation of separation between system-admin, policy-admin and security-auditor roles was found.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Realtime SYSLOG/SNMP log transfer to SIEM connectors (Splunk, McAfee ESM, HP ArcSight) and SIEM/SOAR/SOC deployments are documented; CEF format and a TLS-encrypted log channel are not explicitly documented, so the item is only partially met. [1], [5], [14] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | - | The gateway is documented as enabling compliance with NRC RG 5.71, NIST 800-53/800-82, NERC CIP, IEC 62443, CFATS, ISO and ANSSI; vendor-supplied out-of-box compliance report templates are not documented, so the item is only partially met. [5], [9], [15] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | - | The Singapore Common Criteria Scheme certifies Waterfall WF-500 version 2 (the gateway family sold by Toshiba) at EAL4+ augmented with AVA_VAN.5, ALC_DVS.2 and ALC_FLR.2 (issued 16 May 2023, category Boundary Protection Devices and Systems), and Waterfall and its distributors also cite Common Criteria EAL4+ for the family. [9], [10], [13], [14], [15] |

---

## 4. Notable Strengths

- **Hardware-enforced protocol break (items 1.1, 1.2):** the TX unit carries only a laser emitter and the RX unit only a photocell, so no TCP/IP session can be re-initiated from the receiving network; sender and receiver live on separate boards, with an internal partition in the WF-500C and separate chassis in the WF-500SPLIT [5], [9], [3].
- **Default-deny by physics (item 1.3):** nothing on the external side can send traffic into the OT network through the gateway, and even a misconfigured or compromised device cannot open an inbound path [5], [9], [11].
- **Broad OT protocol coverage (items 3.2, 3.4):** connectors replicate OPC (DA/HDA/A&E/UA), DNP3, ICCP, Modbus, IEC 60870-5-104 and MQTT, plus SYSLOG/SNMP and SIEM feeds (Splunk, McAfee ESM, HP ArcSight) [5], [7], [1].
- **Rated throughput (item 4.1):** the WF-400/WF-500C are rated at 1 Gbps and the WF-600 at 1-10 Gbps with 10GBASE-T and 10G fiber options, meeting the >=1000 Mbps threshold [6], [9], [15].
- **Common Criteria certification (item 5.4):** the Singapore Common Criteria Scheme certifies Waterfall WF-500 version 2 at EAL4+ augmented with AVA_VAN.5, ALC_DVS.2 and ALC_FLR.2, category Boundary Protection Devices and Systems, issued 16 May 2023 [13].

## 5. Notable Gaps / Risks

- **No content processing / CDR (items 2.1-2.7):** no evidence exists of CDR, macro removal, multi-AV, schema validation, DLP or anti-steganography - the gateway replicates data without content disarm, so buyers needing file sanitization must add a separate product.
- **No published latency or HA switchover time (items 4.2, 4.3):** no processing-latency figure exists and HA is documented only qualitatively (duplicated WF-500S appliances and agents, ClusterPerfect, dual PSUs); the <=10 ms latency and <=100 ms failover requirements cannot be verified [4], [7], [8], [9].
- **SIEM integration is partial (item 5.2):** realtime syslog/SNMP/SIEM connectors are documented, but CEF format and a TLS-encrypted log channel are not [5], [1].
- **Compliance reporting is partial (item 5.3):** standards alignment (NRC RG 5.71, NIST 800-53/800-82, NERC CIP, IEC 62443) is documented, but out-of-box compliance report templates are not [5], [9].
- **Management-evidence gaps (items 5.1, 1.4):** no RBAC role separation and no hardened-OS/microkernel claim is documented; security functions are implemented in hardware, but agent OS hardening is unverified [9], [15].

## 6. Evidence Quality Notes

Six items (1.1, 1.2, 1.3, 3.2, 4.1, 5.4) were triangulated across Toshiba documentation, the original vendor's (Waterfall Security Solutions) pages and at least one non-vendor source - Terilogy, INTEC or the Singapore Common Criteria Scheme registry - which is what allows the high-confidence verdicts on 1.1, 1.2, 1.3 and 5.4 [13], [14], [15]. Four items (3.1, 3.3, 3.4, 4.4) rest on vendor-only documentation and are therefore capped at medium confidence; the remaining eleven items are unknown for lack of any published evidence rather than documented absence, per the anti-fabrication contract. No source contradicted another; the main caveat is that Toshiba's primary material is Japanese-language, and the 1 Gbps throughput figure is a vendor model rating rather than an independent test result, so numeric claims should be re-validated against a certified configuration (WF-500 v2) datasheet before procurement.

---

## Bibliography

[1] Toshiba Corporation. "データダイオード Waterfall 一方向セキュリティゲートウェイ (Toshiba Industrial Security Gateway product page)". https://www.global.toshiba/jp/products-solutions/security-ict/gateway.html (Retrieved: 2026-08-11T09:05:00Z)
[2] Toshiba Corporation. "WF-600 model page - Waterfall Unidirectional Security Gateway (Toshiba)". https://www.global.toshiba/jp/products-solutions/security-ict/gateway/wf-600.html (Retrieved: 2026-08-11T09:05:00Z)
[3] Toshiba Corporation. "WF-500C model page - Waterfall Unidirectional Security Gateway (Toshiba)". https://www.global.toshiba/jp/products-solutions/security-ict/gateway/wf-500c.html (Retrieved: 2026-08-11T09:05:00Z)
[4] Toshiba Corporation. "WF-500S model page - Waterfall Unidirectional Security Gateway (Toshiba)". https://www.global.toshiba/jp/products-solutions/security-ict/gateway/wf-500s.html (Retrieved: 2026-08-11T09:05:00Z)
[5] Toshiba Digital Solutions Corporation. "制御システムセキュリティ対策の勘所 - Waterfall whitepaper (Toshiba Digital Solutions)". https://www.global.toshiba/content/dam/toshiba/jp/products-solutions/security-ict/gateway/download/pdf/whitepaper_waterfall.pdf (Retrieved: 2026-08-11T09:05:00Z)
[6] Toshiba Solutions Corporation. "データダイオード Waterfall 一方向セキュリティゲートウェイ leaflet (Toshiba Solutions)". https://www.toshiba-sol.co.jp/pfsol/gateway/pdf/waterfall_leaflet1906.pdf (Retrieved: 2026-08-11T09:05:00Z)
[7] Toshiba Digital Solutions Corporation. "Data Diode Solution - Waterfall Unidirectional Security Gateway leaflet EN (Toshiba Digital Solutions)". https://www.toshiba-sol.co.jp/pfsol/gateway/pdf/Waterfall%20Leaflet_EN_202010.pdf (Retrieved: 2026-08-11T09:05:00Z)
[8] Toshiba Corporation. "DiGiTAL T-SOUL Vol.25: 制御システムの最新セキュリティ対策 (Toshiba article)". https://www.global.toshiba/jp/company/digitalsolution/articles/tsoul/25/005.html (Retrieved: 2026-08-11T09:05:00Z)
[9] Waterfall Security Solutions Ltd.. "Unidirectional Security Gateways - product page (Waterfall Security Solutions)". https://waterfall-security.com/technology-and-products/unidirectional-security-gateways/ (Retrieved: 2026-08-11T09:05:00Z)
[10] Waterfall Security Solutions Ltd.. "Waterfall for Intrusion Detection Systems - product page". https://waterfall-security.com/technology-and-products/wf-ids/ (Retrieved: 2026-08-11T09:05:00Z)
[11] Waterfall Security Solutions Ltd.. "Data Diode and Unidirectional Gateways (Waterfall blog)". https://waterfall-security.com/data-diode-and-unidirectional-gateways/ (Retrieved: 2026-08-11T09:05:00Z)
[12] Waterfall Security Solutions Ltd. (hosted by NIST). "Waterfall Security Solutions Response to NIST RFI: Developing a Framework to Improve Critical Infrastructure Cybersecurity (Docket 130208119-3119-01)". https://www.nist.gov/document/040813waterfallsecuritypdf (Retrieved: 2026-08-11T09:05:00Z)
[13] Cyber Security Agency of Singapore. "Singapore Common Criteria Scheme Certified Product List - Waterfall WF-500 version 2". https://www.csa.gov.sg/our-programmes/certification-and-labelling-schemes/singapore-common-criteria-scheme/product-list/waterfall-wf-500-version-2/ (Retrieved: 2026-08-11T09:05:00Z)
[14] Terilogy Corporation. "データダイオード「Unidirectional Security Gateways」(Terilogy Waterfall page)". https://www.terilogy.com/waterfall/index.html (Retrieved: 2026-08-11T09:05:00Z)
[15] INTEC (Intracom Telecom). "Waterfall Security Unidirectional Gateways (INTEC page)". https://www.intec.gr/en/what-we-do/cybersecurity/waterfall-security-unidirectional-gateways (Retrieved: 2026-08-11T09:05:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 15 (kept: 15, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification registry: 1, datasheet: 2, regulatory filing: 1, third-party distributor page: 1, third-party integrator page: 1, vendor article: 1, vendor blog: 1, vendor product page: 6, whitepaper: 1
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
