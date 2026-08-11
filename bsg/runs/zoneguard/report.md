# BSG / Cross Domain Product Assessment: Advenica AB — ZoneGuard (SecuriCDS ZoneGuard PE250)

**Product ID:** `zoneguard`
**Version reference:** ZoneGuard PE250 appliance; product sheet Doc. no. 20277 v1.5 (2025), Protocol Guide Doc. no. 21846 v1.0
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:50:00Z
**Total evidence items collected:** 28
**Total distinct sources:** 8

---

## 1. Overview

Advenica ZoneGuard is a bidirectional Cross Domain Solution (CDS) security gateway that validates and filters information exchanged between security domains [1]. Advenica positions it as an information-exchange product rather than a network-oriented firewall [6]; the PE250 is a pre-configured 1U 19-inch appliance, and the same software stack can be hosted as a virtual machine [1]. The gateway performs a protocol break with full message inspection, enforces information-level allowlisting per customer policy, and leaves an audit trail [1, 3]. Service modules cover HTTP(S)/SOAP, email (SMTP/POP3) and file transfer (FTP, SFTP, SMB, NFS) [3, 4], with customised protocol services available on request [2]. Advenica describes ZoneGuard as a data loss and intrusion prevention solution with CDR capabilities through information transformation [3], targeting defence, authority, critical-infrastructure and enterprise customers; a Swedish government deployment at Trafikverket is documented [8]. The vendor holds Common Criteria EAL4+ certification on its DD1G data diode and EU/national approvals on other product lines, but no ZoneGuard-specific certification is published [5, 7].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 0                | 5      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 10 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | — | Vendor documents that ZoneGuard performs a protocol break with full message inspection to reduce the attack surface of the boundary gateway. [1], [3] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | — | Vendor documents separation technology on a dedicated pre-configured 1U appliance for exchange between two separate systems, but the internal dual processing-board design connected via FPGA or isolated shared memory is not specified. [1], [3] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | Vendor documents information-level allowlisting in which only information permitted by the defined policy is transferred and all other information is denied. [1], [2], [3], [8] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No public documentation of the underlying OS hardening approach (hardened OS, microkernel or SELinux strict mode).) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No public documentation of internal data stamping/signing of clean data before new sessions are initiated.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | — | Vendor claims CDR capabilities through transformation of information with byte-level file finger printing and information-centric content inspection; the checklist's format coverage (Office, PDF, image, CAD) is not enumerated. [2], [3] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No public documentation of macro/script removal (VBA, JavaScript, DDE links, embedded objects).) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No public documentation of multi-engine antivirus scanning of raw payloads.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | — | Vendor documents XML validation against XSD schemas for HTTP(S)/SOAP traffic; JSON, FIXM and AIXM schema validation is not documented. [1], [2] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No public documentation of filtering based on security labels attached to files.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | — | Vendor positions ZoneGuard as a data loss and intrusion prevention solution with HTTP-method, range and signature filtering plus byte-level file validation; keyword/regex-based DLP rules (secrets, ID numbers, accounts) are not explicitly documented. [1], [3] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No public documentation of steganography detection or removal in image files.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Supported | medium | — | File Transfer service supports FTP, SFTP, SMB and NFS and Web App integration covers HTTP/HTTPS and SOAP, all under full message inspection with byte-level validation; FTP/S is not separately enumerated. [3], [4] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found (No public documentation of OT/ICS protocol services (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT).) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No public documentation of database proxy services (SQL Server, Oracle, PostgreSQL) or query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | Syslog and SNMP output is documented for active device monitoring; RTSP video proxy and syslog/CEF relay services through the gateway are not documented. [3] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 10000 Mbps | Vendor datasheet specifies 2x 10 Gbit SFP+ network interfaces running at 10 Gbit Ethernet wire speed (10,000 Mbps) on the ZoneGuard PE250. [1], [3], [6] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No public latency figure documented for packet/protocol processing.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found (No public documentation of HA active-standby configuration or failover switchover time.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No public documentation of fail-close behaviour under DoS or overload conditions.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | — | Vendor documents a role-based administration system with separation of duties. [1], [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Vendor documents Syslog and SNMP for active device monitoring; CEF format and TLS-encrypted log export to a SIEM are not documented. [3] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No public documentation of compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001).) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | — | no evidence found (No public evidence of Common Criteria (EAL4+), FIPS 140-3 or national crypto certification for ZoneGuard specifically.) |

---

## 4. Notable Strengths

- **Protocol break with full message inspection (item 1.1):** the vendor documents a protocol break and 100% message inspection that reduce the attack surface of the boundary gateway [1, 3].
- **Information-level allowlisting / default-deny (item 1.3):** only information permitted by the defined policy is transferred; all other information is denied, down to information level [1, 2, 3].
- **File transfer and web application protocol coverage (item 3.1):** FTP, SFTP, SMB and NFS plus HTTP/HTTPS and SOAP run under full message inspection with byte-level validation [3, 4].
- **High interface throughput (item 4.1):** 2x 10 Gbit SFP+ network interfaces at 10 Gbit Ethernet wire speed (10,000 Mbps) [3, 6].
- **Role-based administration with separation of duties (item 5.1):** management is role-based with separation of duties and full audit trail capabilities [1, 3].

## 5. Notable Gaps / Risks

- **No published security certification (item 5.4):** no Common Criteria, FIPS or national crypto certification is documented for ZoneGuard; the vendor's CC EAL4+ certificate covers only the DD1G data diode and other approvals cover other product lines [5, 7]. This is a material gap for high-assurance buyers; resolving it requires the vendor to publish a ZoneGuard-specific certificate or evaluation report.
- **CDR format coverage unverified (item 2.1):** CDR via information transformation is claimed, but disassembly/reconstruction of Office, PDF, image and CAD formats is not documented [3].
- **No HA or latency figures (items 4.2, 4.3):** no processing-latency value and no active-standby failover/switchover-time documentation is public; both metrics are rated unknown.
- **Fail-close behaviour undocumented (item 4.4):** no public description of how the gateway behaves (fail-open vs fail-close) under DoS or overload conditions.
- **No OT/ICS protocol services (item 3.2):** OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 and MQTT are not listed among supported services despite the file transfer service being positioned for ICS/SCADA use [2]; only customised protocol services are offered.

## 6. Evidence Quality Notes

All 11 non-unknown verdicts rest on vendor-published material (product pages, PE250 datasheet, protocol guide, press releases), so confidence is capped at medium across the board; 7 items are backed by at least two distinct source types, and item 1.3 is backed by four vendor sources including a named government customer announcement [1, 2, 3, 8]. The only non-vendor source staged is the Common Criteria portal registry [7], used here for certification context: item 5.4 is rated unknown because the registry lists no ZoneGuard entry, and the vendor's certifications page names certifications for other product lines only [5]. Attempts to locate independent lab tests or third-party reviews were blocked by search-engine anti-bot defenses in this environment, so the assessment likely understates coverage for items 4.2, 4.3, 4.4 and 5.4, which are rated unknown even though the non-public customer documentation may contain figures (latency, failover, fail-safe behaviour). No source contradictions surfaced; the vendor corpus is internally consistent. Quotes were verified verbatim against the staged artifact texts (28/28 grounded).

---

## Bibliography

[1] Advenica AB. "ZoneGuard (Data Guards) - product page". https://advenica.com/products-and-solutions/data-guards/zoneguard/ (Retrieved: 2026-08-11T08:50:00Z)
[2] Advenica AB. "ZoneGuard Services - product page". https://advenica.com/products-and-solutions/data-guards/zoneguard-services/ (Retrieved: 2026-08-11T08:50:00Z)
[3] Advenica AB. "SecuriCDS ZoneGuard PE250 - Product Sheet (Doc. no. 20277 v1.5)". https://advenica.com/media/fwyokwby/20277v1-5productsheet_securicdszoneguardpe250-1-20250327-085032.pdf (Retrieved: 2026-08-11T08:50:00Z)
[4] Advenica AB. "Protocol Guide - Protocol support for Advenica ZoneGuard (Doc. no. 21846 v1.0)". https://advenica.com/media/ufypysaj/protocolguide_zoneguard.pdf (Retrieved: 2026-08-11T08:50:00Z)
[5] Advenica AB. "Certifications & Approvals". https://advenica.com/certifications-approvals/ (Retrieved: 2026-08-11T08:50:00Z)
[6] Advenica AB. "Advenica launches ZoneGuard PE250 - a new and unique Security Gateway with high security (press release)". https://advenica.com/about-us/news-and-press/advenica-launches-zoneguard-pe250-a-new-and-unique-security-gateway-with-high-security/ (Retrieved: 2026-08-11T08:50:00Z)
[7] Common Criteria Recognition Arrangement (CCRA). "Common Criteria Portal - Certified Products search for vendor 'Advenica'". https://www.commoncriteriaportal.org/products/index.cfm?txtCertificationName=Advenica (Retrieved: 2026-08-11T08:50:00Z)
[8] Advenica AB. "The Swedish Transport Administration (Trafikverket) signs a three year agreement with Advenica and places an initial ZoneGuard order of 1.9 MSEK (press release)". https://advenica.com/about-us/news-and-press/the-swedish-transport-administration-trafikverket-signs-a-three-year-agreement-with-advenica-and-place-an-initial-zoneguard-order-of-1-9-msek/ (Retrieved: 2026-08-11T08:50:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 8 (kept: 8, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 1, certification_registry: 1, vendor_datasheet: 2, vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
