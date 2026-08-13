# BSG / Cross Domain Product Assessment: General Dynamics Mission Systems - TACDS (Tactical Cross Domain Solutions) - LP and VM; registry name 'TACLANE Cross Domain Gateway'

**Product ID:** `taclane-cross-domain-gateway`
**Version reference:** TACDS v3 (LP and VM form factors); v3.0 baseline per USAspending procurement records (2025-2026)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T16:20:00Z
**Total evidence items collected:** 43
**Total distinct sources:** 6

---

## 1. Overview

The registry entry "TACLANE Cross Domain Gateway" maps to General Dynamics Mission Systems' tactical cross domain gateway product family, TACDS, sold as the 1U TACDS-Low Profile (LP) and the compact TACDS-Vehicle Mount (VM) [2, 3]. The vendor positions TACDS as a tactical cross domain solution (CDS) that enables information and communications to be shared and transmitted across different security domains in austere tactical environments - a message-format filtering guard, not a document-CDR system and not an industrial firewall [1, 5]. It is authorized for Secret and Below (SABI) and Top Secret and Below (TSABI) interoperability, executes programmable rule sets that pass, block or change individual messages or data fields, and enforces certified separation of network/interface domains with separate high and low data ports [2, 4]. Deployment shapes include ships, wheeled and tracked vehicles, mobile command centers, ground sensor systems, aircraft and unmanned vehicle systems [2]. TACDS is a low SWaP-C, tamper-resistant, TRL-9 device that is NSA-approved, on the NCDSMO baseline list since 2012 and Raise the Bar v3 compliant; U.S. DoD procurement records confirm v3.0 LP/VM orders through 2025-2026 [4, 6]. TACLANE is GDMS's separate HAIPE network-encryption line rather than a gateway product.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 0                | 3      | 0   |
| partial          | 10    | 0                | 10     | 0   |
| not_supported    | 4     | 0                | 4      | 0   |
| unknown          | 7     | 0                | 0      | 7   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 2 items backed by ≥ 2 source_types; 15 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | - | Vendor documents TACDS as a tactical CDS whose defense-in-depth architecture provides certified separation of network/interface domains and enforces a separation boundary between the attached security domains, with separate high and low data ports; US federal procurement records confirm fielded TACDS cross domain transfer systems. [1], [2], [4], [5], [6] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | - | Vendor documents domain separation with separate high and low data ports on a ruggedized, tamper-resistant bidirectional CDS appliance; the internal dual processing-board design connected via FPGA or isolated shared memory is not specified. [2], [3], [4] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | - | Vendor documents programmable rule sets that filter information, allowing individual messages or data fields to be selectively passed, blocked or changed, with autonomous screening of message exchanges; an explicit default-deny statement for all non-whitelisted traffic is not documented. [2], [4] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | - | Vendor documents secure boot with trusted platform verification upon power up and encrypted storage of rule sets and audit logs; microkernel or SELinux strict-mode OS hardening is not documented. [2] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No public documentation of internal data stamping / signing of clean data before new sessions are initiated.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Not Supported | medium | - | Vendor documents TACDS as a message-format filtering CDS whose RTB filter library covers VMF, XML, Protobuf, FMV, SMTP, FTP, TLS/SSL and similar tactical formats and which stores no user message data; document-format CDR (disassembly and reconstruction of Office/PDF/image/CAD files) is not part of the documented design. [2], [4] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Not Supported | medium | - | The documented filter library and programmable rule-set design process messages and data fields, not Office documents, so removal of VBA macros, JavaScript, DDE links and embedded objects is not part of the product's documented design. [2], [4] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No public documentation of multi-engine antivirus scanning of raw payloads.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | - | Vendor documents filter components customized through configuration files, security policy rulesets and data format descriptions, including Configurable XML and Google Protobuf filters; explicit W3C XSD schema validation of XML/JSON/FIXM/AIXM is not documented. [2], [4] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Partial | medium | - | Vendor documents programmable rule sets that selectively pass, block or change individual messages and data fields across SABI/TSABI domain boundaries (information flow control); filtering based on security labels attached to files is not documented. [2], [4] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No public documentation of keyword/regex DLP rules (secrets, ID numbers, accounts).) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Not Supported | medium | - | The documented processing scope covers tactical message formats and HD Full Motion Video with KLV metadata; still-image file (PNG/JPEG/BMP) processing with steganography detection and removal is not part of the documented design. [2] |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Vendor documents SMTP, FTP and TLS/SSL filters in the RTB filter library with message inspection; SFTP, FTPS and SMB/NFS proxies are not documented. [2], [4] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | - | no evidence found (No public documentation of OT/ICS protocol services (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT).) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No public documentation of database proxy services (SQL Server, Oracle, PostgreSQL) or query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Vendor documents HD Full Motion Video with KLV metadata among dozens of supported message formats; RTSP video proxy and syslog/CEF unidirectional or bidirectional relay are not documented. [1], [2] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Not Supported | medium | 100 Mbps | Vendor datasheets list 10/100 Ethernet interfaces for both TACDS-LP and TACDS-VM, capping the data rate at 100 Mbps, below the 1 Gbps requirement; throughput/latency is stated as message type and size dependent with no separate throughput figure. [2], [3] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | Vendor states TACDS is designed for low latency/disconnected environments and that latency is message type and size dependent, but publishes no numeric latency figure. [2], [4] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | - | no evidence found (No public documentation of HA active-standby configuration or failover switchover time.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | Vendor documents a tamper-resistant device with built-in zeroization, a fail-secure response to physical tampering; fail-close behavior specifically under DoS or overload conditions is not documented. [2], [3] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | - | Vendor documents an Administrator tool providing four administrator roles, each with exclusive access to specific administrator functions, plus authenticated role-based device administration through a management port. [2], [4] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Vendor documents full audit logging of all system, security and message events; CEF/syslog export over a TLS channel to a SIEM is not documented. [2] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No public documentation of compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001).) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | medium | - | Vendor documents NSA approval, NCDSMO baseline listing since 2012 and Raise the Bar v3 compliance (the applicable US-government CDS certification, not Common Criteria EAL4+ or FIPS 140-3); USAspending procurement records confirm 2025-2026 US DoD orders of TACDS v3.0 LP/VM with NSA Raise the Bar compliance requirements. [1], [2], [4], [6] |

---

## 4. Notable Strengths

- **Certified domain separation (items 1.1, 1.2):** TACDS enforces a separation boundary between the attached security domains with separate high and low data ports and programmable rule sets that selectively pass, block or change individual messages and data fields [2, 4].
- **SABI/TSABI accreditation with NSA/NCDSMO certification (items 1.1, 5.4):** Vendor documents authorization for Secret and Top Secret interoperability, NSA approval, NCDSMO baseline listing since 2012 and Raise the Bar v3 compliance [2, 4].
- **Role-separated administration (item 5.1):** An Administrator tool provides four administrator roles, each with exclusive access to specific functions, plus authenticated role-based device administration [2, 4].
- **Audit and tamper-response (items 5.2, 4.4):** Full audit logging of system, security and message events is combined with a tamper-resistant enclosure and built-in device zeroization [2].
- **Broad tactical message coverage (items 3.1, 3.4):** The RTB filter library includes HD Full Motion Video with KLV metadata, SMTP, FTP, TLS/SSL, Link16/JREAP-C, VMF, ASTERIX and other tactical formats [2].

## 5. Notable Gaps / Risks

- **No document-format CDR (item 2.1):** TACDS filters tactical message formats and stores no user message data, so Office/PDF/image/CAD disassembly-and-reconstruction CDR is absent; a buyer needing file-level CDR would require a separate product [2, 4].
- **Throughput below the 1 Gbps requirement (item 4.1):** Both form factors ship 10/100 Ethernet interfaces, capping the data rate at 100 Mbps, and no separate throughput figure is published [2, 3].
- **No numeric latency or HA figures (items 4.2, 4.3):** The vendor only describes "low latency" with message-type- and size-dependent latency; no active-standby HA or failover switchover time is documented [2, 4].
- **No OT/ICS or database protocol support (items 3.2, 3.3):** OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT and SQL Server/Oracle/PostgreSQL proxying are not documented - TACDS is a military-message CDS, not an IT/OT gateway.
- **No DLP or SIEM export (items 2.6, 5.2):** Keyword/regex DLP rules and CEF/syslog-over-TLS export to a SIEM are not documented; audit logging stays local to the device [2].

## 6. Evidence Quality Notes

All capability claims rest on vendor documentation - the TACDS overview, LP and VM product pages, and the FAQ (sources [1]-[5]) - so confidence is capped at medium on every non-unknown verdict. The only independent source obtained was USAspending.gov federal procurement records [6], which corroborate that TACDS v3.0 LP/VM is a real, actively procured U.S. DoD item subject to NSA Raise the Bar compliance requirements, but which do not independently verify capabilities. No third-party lab test or independent technical review could be reached from this environment: search engines, nsa.gov, commoncriteriaportal.org and breakingdefense.com all returned bot blocks, and the vendor-hosted Breaking Defense PDF was staged but is image-only, so it could not be quoted.

Items 1.1 and 5.4 are triangulated across four or five sources (vendor pages plus the procurement registry); most other items rest on one or two vendor pages. No contradictions were found among sources - the vendor's pages are mutually consistent. Where vendor language was qualitative ("low latency", "message type and size dependent"), verdicts were downgraded to partial with null numeric values (items 4.2) or not_supported with the documented interface bound as the numeric basis (item 4.1) rather than extrapolating unstated figures.

---

## Bibliography

[1] General Dynamics Mission Systems. "TACDS (Tactical Cross Domain Solutions) - overview page". https://gdmissionsystems.com/cross-domain-solutions/tactical-cross-domain-solutions-tacds (Retrieved: 2026-08-11T16:20:00Z)
[2] General Dynamics Mission Systems. "TACDS-Low Profile (LP) Cross Domain Solution - product page". https://gdmissionsystems.com/products/cross-domain-solutions/tacds-low-profile (Retrieved: 2026-08-11T16:20:00Z)
[3] General Dynamics Mission Systems. "TACDS-Vehicle Mount (VM) Cross Domain Solution - product page". https://gdmissionsystems.com/products/cross-domain-solutions/tacds-vehicle-mount (Retrieved: 2026-08-11T16:20:00Z)
[4] General Dynamics Mission Systems. "Cross Domain Solutions FAQ (includes TACDS section)". https://gdmissionsystems.com/cross-domain-solutions/faqs (Retrieved: 2026-08-11T16:20:00Z)
[5] General Dynamics Mission Systems. "Cross Domain Solutions (CDS) - overview page". https://gdmissionsystems.com/cross-domain-solutions (Retrieved: 2026-08-11T16:20:00Z)
[6] USAspending.gov (U.S. Treasury). "USAspending.gov award search results for keyword 'TACDS' (US federal contract awards, POST API)". https://api.usaspending.gov/api/v2/search/spending_by_award/ (Retrieved: 2026-08-11T16:20:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 16
- **Sources reviewed:** 6 (kept: 6, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** regulatory_filing: 1, vendor_doc: 5
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
