# BSG / Cross Domain Product Assessment: Fibersystem AB — Fibersystem Secure Gateway (Bidirectional Data Diode 1Gbit family with DDMW middleware)

**Product ID:** `fibersystem-secure-gateway`
**Version reference:** Data Diode Bidirectional 1Gbit 2xAC/2xDC (part nos. 60-00-7563/60-00-7564); datasheet FS24888PA1; Data Diode Middleware DDMW 1.0 (FS17101 v1.0)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:00:00Z
**Total evidence items collected:** 61
**Total distinct sources:** 13

---

## 1. Overview

Fibersystem AB (Stockholm, Sweden) is a TEMPEST/RÖS equipment manufacturer with more than 40 years of fiber-optical cyber security work and certified TEMPEST supplier status to NATO [8][11]. Its "Secure Gateway" listing on the provider matrix matches no product of that exact name on the vendor site; it maps to the vendor's secure hardware gateway family, chiefly the Bidirectional Data Diode 1Gbit (part nos. 60-00-7563/7564, AC or DC power) optionally paired with the Data Diode Middleware (DDMW) 1.0 [1][3]. The product is a hardware-based, fully transparent data diode: it forwards Syslog, NTP broadcast, SNMP traps and UDP traffic in both directions over fiber or copper, with galvanic isolation between completely separated send and receive nodes and no software on the data path [1][2]. Deployment shapes are 1 HU 19-inch rack units with redundant hot-swappable power supplies, card modules for rack integration, and DDMW software nodes for controlled file, stream, mail and UDP transfer between domains [2][3][6]. It is neither an application-layer protocol-break CDS nor a stateful NGFW; the content-inspection checklist items are marked not supported because the documented transparent-hardware category performs no content inspection [1][6].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 0                | 2      | 0   |
| partial          | 10    | 0                | 10     | 0   |
| not_supported    | 9     | 0                | 9      | 0   |
| unknown          | 3     | 0                | 0      | 3   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 14 items backed by ≥ 2 source_types; 14 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | — | Vendor documents the bidirectional diode as a fully hardware-based, galvanically separated device requiring no extra software on its core data path (additional software is needed even for basic mail/FTP/SNMP relay); this is passive physical-layer forwarding, not an active TCP/IP session-terminating protocol-break architecture. [1], [2] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | medium | — | Vendor documents completely isolated send and receive nodes connected by fiber-optic links with galvanic separation between the two networks, corroborated by distributor material; isolation is physical (separate nodes over fiber) rather than dual processing boards over FPGA/shared memory. [1], [2], [12] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | Vendor documents hardware-enforced direction control that eliminates the risk of data flowing in a false direction, with transparent forwarding of all data types; packet- or protocol-level whitelist filtering is not documented for the bidirectional model. [1], [5], [12] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | The diode data path itself is hardware-based with no extra software or OS, so it has no OS-level attack surface to harden; however, DDMW middleware nodes are delivered as software packages for customer-provided common operating systems (Windows/Linux), and no hardening measures (SELinux, microkernel, etc.) are documented for that OS. [1], [3] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Not Supported | medium | — | Vendor documents the diode's core data path as hardware-only with no extra software, so there is no internal control core capable of cryptographically signing 'clean' data or gating a new session before initiation — no session-terminating funnel or signing software exists on the documented data path. [1], [2] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Not Supported | medium | — | Vendor documents the diode's core data path as fully hardware-based, needing no extra software; content disarm and reconstruction requires software-based file parsing and rebuilding, which is documented as absent from the hardware path and not listed among DDMW's software-add-on functions (queue mgmt, logging, mail, FTP, SNMP, SDK). [1], [2] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Not Supported | medium | — | Vendor documents the diode's core path as hardware-only, no extra software; macro/script removal requires software-based document parsing, which is documented as absent from the hardware path and not among DDMW's listed software functions. [1], [2] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Not Supported | medium | — | The diode forwards all data types transparently with a hardware-only path and no additional software; multi-engine antivirus scanning of payloads would require software-based content inspection that the documented data path does not perform. [5], [6] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Not Supported | medium | — | The diode performs no payload inspection - it forwards all data types transparently with a hardware-only path; W3C-schema validation of XML/JSON/FIXM/AIXM structures requires content parsing the documented data path does not perform. [1], [6] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Not Supported | medium | — | The diode performs no content-based filtering - it forwards all data types transparently with a hardware-only path; security-label-based information flow control on files is not present in the documented data path. [1], [6] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Not Supported | medium | — | The diode performs no content inspection, and DDMW middleware documents only hashing-based transfer verification; keyword/regex DLP rules require content inspection the documented data path does not perform. [1], [3], [6] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Not Supported | medium | — | The diode forwards all data types transparently with no image-content analysis; steganography detection/removal requires content inspection the documented data path does not perform. [1], [6] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | Vendor documents file/folder transfer and SMTP proxy via the DDMW middleware plus secure file transfer between networks as a use case; SFTP/FTPS, HTTPS and SMB/NFS proxy support with content cleaning is not documented. [1], [2], [3], [4] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | Vendor documents a SCADA integration interface in the DDMW and industrial-plant use cases (sensor data/valve control) for the bidirectional diode; explicit proxy support for OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT is not documented. [1], [3], [13] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No public documentation of database proxy services (SQL Server, Oracle, PostgreSQL) or query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | Vendor documents native Syslog, NTP broadcast and SNMP trap relay in all modes through the bidirectional diode; RTSP video proxy and CEF-format relay are not documented. [1], [2] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | Vendor datasheet and distributor page specify 1 Gbps data speed on both galvanic/electrical and fiber-optic links (1,000 Mbps); because the device performs no content inspection, this is raw line speed rather than CDR-inspection throughput. [1], [2], [12] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No public latency figure documented for packet/protocol processing.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Vendor documents redundant, hot-swappable power supplies on the 1U rack unit; no active-standby failover switchover time is published, so the ≤100 ms requirement cannot be verified. [1], [12] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | Vendor documents hardware-based direction enforcement that completely eliminates the risk of data flowing in a false direction, plus tamper-protected enclosures with back-channel protection; explicit fail-close behavior under DoS/overload is not documented. [1], [6] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Vendor documents administrative role separation with separated role interfaces and administrator role permissions in the DDMW middleware, corroborated by distributor material; the specific system-admin/policy-admin/auditor role set is not enumerated. [3], [4], [13] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Vendor documents Syslog and SNMP trap output on the diode plus DDMW management interfaces for integration with monitoring systems; CEF format and TLS-encrypted log export to a SIEM are not documented. [1], [2], [3] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No public documentation of compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001).) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | — | Vendor and distributor document TEMPEST Level A (NATO standard)/EMSEC/RÖS U1 certification for the diode family, NATO TEMPEST supplier status, ISO 9001/14001 and CE/RoHS/WEEE compliance; Common Criteria (EAL4+), FIPS 140-3 or national cryptographic certification is not documented. [2], [6], [8], [9], [12] |

---

## 4. Notable Strengths

- **Hardware isolation and direction enforcement (items 1.2, 4.4):** completely isolated send/receive nodes with fiber-optic galvanic separation and a tamper-protected enclosure eliminate any path for data to flow in a false direction [1][2].
- **TEMPEST Level A / RÖS U1 certification (item 5.4):** the diode family is documented as TEMPEST Level A (NATO standard)/EMSEC/RÖS U1 certified, and the company holds NATO TEMPEST supplier status plus ISO 9001/14001 [6][8][9][12].
- **Line-rate throughput (item 4.1):** the datasheet and distributor page specify 1 Gbps data speed on both galvanic/electrical and fiber-optic links [2][12].
- **SCADA/industrial fit (item 3.2):** DDMW documents an integration interface for SCADA applications, and the vendor positions the bidirectional diode for industrial plant sensor and valve-control flows [1][3].
- **Availability features (item 4.3):** redundant, hot-swappable power supplies on the 1U rack unit are documented [1][12].

## 5. Notable Gaps / Risks

- **No content inspection (items 2.1-2.7):** the device is transparent to all data types, so CDR, macro/script removal, multi-AV, schema validation, IFC, DLP and anti-steganography are scored not supported; buyers needing payload sanitization must pair the diode with an external content-inspection solution [1][6].
- **No application-layer protocol break (item 1.1):** TCP/IP sessions are not terminated or inspected, only direction is enforced, so protocol-level filtering is absent [1][2].
- **OT/ICS protocol proxies unverified (item 3.2):** OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 and MQTT proxy support is not documented; only transparent passthrough and SCADA integration interfaces are claimed [3].
- **No SIEM-grade log export (item 5.2):** only Syslog and SNMP traps are documented; CEF format and TLS-encrypted export to a SIEM are not specified [1][3].
- **Unquantified latency and failover (items 4.2, 4.3):** no processing-latency figure and no active-standby switchover time are published, so the ≤10 ms and ≤100 ms requirements cannot be verified [1][12].

## 6. Evidence Quality Notes

All 24 items were assessed from 60 evidence entries across 13 sources; 12 items are backed by at least two source types, and 7 items (1.2, 1.3, 3.2, 4.1, 4.3, 5.1, 5.4) triangulate vendor documentation with the German distributor Systerra's pages. Every non-unknown verdict rests on vendor documentation (product pages, datasheets, blog) or distributor mirrors of it: no independent lab test, analyst report, or certification-registry entry could be located because all general search engines returned bot blocks from this environment, so confidence is capped at medium throughout. The 9 not_supported verdicts (items 1.1, 1.5, 2.1-2.7) therefore depend entirely on the vendor's own transparency/hardware-only design statements, which the grounding check verified verbatim against staged copies.

No source contradictions were found; the only wording divergence is the distributor's DDMW page listing transfer types "messages and streams and UDP" versus the vendor datasheet's "messages, streams and UDP", which was treated as consistent. The three unknown items (3.3 database proxy, 4.2 latency, 5.3 compliance reports) reflect absence of public documentation rather than evaluated absence of capability. Numeric-threshold handling followed the checklist contract: 4.1 uses the published 1 Gbps line speed (1,000 Mbps); 4.2 and 4.3 received no fabricated numbers, with 4.3 rated partial on redundant-power evidence alone.

---

## Bibliography

[1] Fibersystem AB. "Data Diode Bidirectional 1Gbit 2xAC - product page". https://www.fibersystem.com/product/data-diode-bidirectional-1gbit-2xac/ (Retrieved: 2026-08-11T09:00:00Z)
[2] Fibersystem AB. "Data Diode Bidirectional 1Gbit - Datasheet (FS24888PA1)". https://www.fibersystem.com/wp-content/uploads/2026/03/FS24888PA1_Datasheet_Data_Diode_Bidirectional-1Gbit.pdf (Retrieved: 2026-08-11T09:00:00Z)
[3] Fibersystem AB. "Data Diode Middleware 1.0 (DDMW) - product page". https://www.fibersystem.com/product/data-diode-middleware-ddmw/ (Retrieved: 2026-08-11T09:00:00Z)
[4] Fibersystem AB. "Data Diode Middleware DDMW - Datasheet (FS17101 v1.0)". https://www.fibersystem.com/wp-content/uploads/2024/04/FS17101PA1-Datasheet-Datadiode-Middleware-DDMW-1.0.pdf (Retrieved: 2026-08-11T09:00:00Z)
[5] Fibersystem AB. "Product Area: Data Diodes (category page)". https://www.fibersystem.com/product-area/data-diodes/ (Retrieved: 2026-08-11T09:00:00Z)
[6] Fibersystem AB. "Data Diode 1Gbit Secure TEMPEST Level A+ & RÖS U1 - product page". https://www.fibersystem.com/product/data-diode-1gbit-secure-tempest-level-a-ros-u1/ (Retrieved: 2026-08-11T09:00:00Z)
[7] Fibersystem AB. "What is a Data Diode? (white paper / blog)". https://www.fibersystem.com/what-is-a-data-diode/ (Retrieved: 2026-08-11T09:00:00Z)
[8] Fibersystem AB. "Fibersystem is now a certified supplier of TEMPEST equipment to NATO (press release)". https://www.fibersystem.com/fibersystem-is-now-a-certified-supplier-of-tempest-equipment-to-nato/ (Retrieved: 2026-08-11T09:00:00Z)
[9] Fibersystem AB. "ISO Certification 9001 and 14001". https://www.fibersystem.com/iso-certification/ (Retrieved: 2026-08-11T09:00:00Z)
[10] Fibersystem AB. "TEMPEST - what is TEMPEST certification?". https://www.fibersystem.com/tempest/ (Retrieved: 2026-08-11T09:00:00Z)
[11] Fibersystem AB. "About Fibersystem". https://www.fibersystem.com/about-us/ (Retrieved: 2026-08-11T09:00:00Z)
[12] Systerra Computer GmbH (distributor). "Data Diode Bidirectional 1Gbit (Fibersystem) - distributor listing". https://www.systerra.de/Data_Diode_Bidirectional_1Gbit.html (Retrieved: 2026-08-11T09:00:00Z)
[13] Systerra Computer GmbH (distributor). "Fibersystem Data Diode Middleware (DDMW) - distributor listing". https://www.systerra.de/Fibersystem_Data_Diode_Middleware_DDMW.html (Retrieved: 2026-08-11T09:00:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 13 (kept: 13, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 2, vendor_blog: 1, vendor_datasheet: 2, vendor_doc: 8
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
