# BSG / Cross Domain Product Assessment: Lockheed Martin - Radiant Mercury

**Product ID:** `radiant-mercury`
**Version reference:** Fourth-generation deployment as of Feb 2015 (trade press); active RADMERC IDIQ N0003919D0006, period of performance 2019-09-01 to 2029-08-31
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:30:00Z
**Total evidence items collected:** 17
**Total distinct sources:** 4

---

## 1. Overview

Radiant Mercury is a cross-domain solution (CDS) software application developed by Lockheed Martin and primarily deployed by the US Navy, designed to allow communications between higher-level classified networks and lower-level, unclassified networks [4]. A reference source describes it as a software application, developed under contract to the Navy, that automatically sanitizes and downgrades formatted classified documents according to user-defined rules [1]. Trade press positions it as a guard that enables secure sharing of sensitive data between classified and unclassified security domains, supports simultaneous data flows to hundreds of channels, interfaces with major C4ISR systems, and has been deployed at more than 400 sites for the US and allied partners since the fourth generation began fielding in 2015 [2]. US federal procurement records show the product remains an active Navy program under the single-award RADMERC indefinite-delivery/indefinite-quantity contract N0003919D0006 (Lockheed Martin, base-and-all-options value $134,242,344, period of performance 2019-09-01 to 2029-08-31) [3]. No Lockheed Martin product page or datasheet is currently published, and the majority of the checklist's capability-level items are not documented in open sources.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 14    | 0                | 0      | 14  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 0 items backed by ≥ 2 source_types; 0 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Partial | medium | - | Sources establish Radiant Mercury as a cross-domain solution that automatically sanitizes and downgrades classified documents and allows secure sharing between classified and unclassified security domains. An explicit protocol-break architecture (TCP/IP session termination with IP routing disabled at the boundary) is not documented in open sources. [1], [2], [4] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No public documentation of hardware isolation architecture (dual processing boards, FPGA or isolated shared-memory link).) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | - | Trade press reports that Radiant Mercury guards classified data from unauthorised access while allowing authorised personnel to retrieve sensitive information, and a reference source documents operation according to user-defined rules. An explicit default-deny whitelist mode for packets and protocols is not documented. [1], [2] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | - | no evidence found (No public documentation of the underlying OS hardening approach (hardened OS, microkernel or SELinux strict mode).) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No public documentation of internal signing/stamping of clean data before new sessions are initiated.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | - | A reference source documents that Radiant Mercury automatically sanitizes and downgrades formatted classified documents, decreasing processing time and eliminating human error. The checklist's format coverage (DOCX/XLSX, PDF, image, CAD) is not enumerated. [1] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No public documentation of macro/script removal (VBA, JavaScript, DDE links, embedded objects).) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No public documentation of multi-engine antivirus scanning of raw payloads.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | - | A reference source documents structured-format header processing for NITF imagery files. W3C-schema validation of XML, JSON, FIXM or AIXM is not documented. [1] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Partial | medium | - | A reference source documents that Radiant Mercury screening depends on security labels in NITF file headers accurately representing image classification. Label-based filtering for other file types is not documented. [1] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | - | A reference source documents automated sanitization and redaction of classified documents driven by user-defined rules. Keyword/regex DLP patterns for secrets, ID numbers or accounts are not specified. [1] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Not Supported | medium | - | A reference source states that Radiant Mercury cannot examine image content itself, so data hidden in image pixels would pass through screening untouched. No anti-steganography engine is documented. [1] |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Trade press reports support for simultaneous data flows to hundreds of channels and most transport, network and data link protocols. Specific file-transfer protocols (SFTP, FTP/S, HTTPS, SMB/NFS) with content cleaning are not enumerated. [2] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | - | no evidence found (No public documentation of OT/ICS protocol services (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT).) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No public documentation of database proxy services (SQL Server, Oracle, PostgreSQL) or query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Trade press reports hundreds of simultaneous channels and interfaces with major C4ISR systems. RTSP video proxy and syslog/CEF unidirectional or bidirectional relay are not documented. [2] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | - | no evidence found (No published bandwidth/throughput figure (Mbps) for CDR or data processing.) |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No published latency figure for packet/protocol processing.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | - | no evidence found (No public documentation of HA active-standby configuration or failover switchover time.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | - | no evidence found (No public documentation of fail-close behaviour under DoS or overload conditions.) |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (No public documentation of role-based administration with separated system-admin/policy-admin/auditor roles.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | - | no evidence found (No public documentation of real-time CEF/Syslog log export over TLS to a SIEM/SOAR.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No public documentation of compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001).) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | medium | - | Trade press reports that Radiant Mercury is accredited to the highest levels of protection in the US and approved for top secret and secret interoperability by the Unified Cross Domain Services Management Office (UCDSMO, now NCDSMO). Common Criteria EAL4+, FIPS 140-3 or national crypto certification is not documented. [2] |

---

## 4. Notable Strengths

- **Established cross-domain guard role (items 1.1, 1.3):** multiple independent sources establish Radiant Mercury as a CDS that sanitizes and downgrades classified documents and guards classified data from unauthorised access between security domains [1, 2, 4].
- **Automated document sanitization / downgrade (items 2.1, 2.6):** the product automates sanitization and downgrade of formatted classified documents per user-defined rules, decreasing processing time and eliminating human error [1].
- **Security-label-driven screening (item 2.5):** a reference source documents that Radiant Mercury screening is driven by security labels in NITF file headers representing image classification [1].
- **US DoD accreditation and approval (item 5.4):** trade press reports Radiant Mercury is accredited to the highest levels of protection in the US and approved for top secret and secret interoperability by the UCDSMO (now NCDSMO) [2].
- **Long-running, funded Navy program (supportability):** the active RADMERC IDIQ (2019-2029, $134M ceiling) demonstrates continued government support and maintenance [3].

## 5. Notable Gaps / Risks

- **Protocol-break architecture unconfirmed (item 1.1):** open sources establish the CDS role but never document explicit TCP/IP session termination with IP routing disabled, so the guard's protocol-break posture cannot be verified from public material.
- **No performance figures published (items 4.1, 4.2, 4.3):** no throughput, latency, or HA failover numbers exist in open sources; the only quantitative claim is qualitative "hundreds of channels" [2].
- **Anti-steganography explicitly absent in documented version (item 2.7):** a reference source states Radiant Mercury cannot examine image content, so data hidden in image pixels passes through screening [1]; any buyer requirement for image-level steganography detection is unmet by the documented version.
- **Large evidence gap on inspection and management capabilities (items 2.2, 2.3, 3.2, 3.3, 5.1-5.3):** macro/script removal, multi-AV, OT/ICS and database protocols, RBAC and SIEM integration are not documented in open sources and are all rated unknown.
- **No format-level CDR enumeration (item 2.1):** sanitization of formatted documents is documented, but coverage of specific Office/PDF/image/CAD formats is not, which is load-bearing for document-transfer use cases.

## 6. Evidence Quality Notes

No item reached three independent sources. Item 1.1 is the only one triangulated across multiple sources (GlobalSecurity, Shephard Media and Wikipedia [1, 2, 4]); all other evaluated items rest on a single source - mostly the dated GlobalSecurity reference entry (items 2.1, 2.4, 2.5, 2.6, 2.7) or the 2015 Shephard trade-press article (items 1.3, 3.1, 3.4, 5.4). Notably, no vendor documentation was available at all: Lockheed Martin's current site has no Radiant Mercury page, so unlike most other runs in this project there are no vendor_doc/vendor_datasheet sources and no vendor-only confidence cap applies. All confidence is capped at medium because each claim depends on a single secondary source and the GlobalSecurity entry describes the 1990s-era version (page last modified 2011).

The sources do not contradict each other - Wikipedia derives directly from the other two - but they are of different vintages and specificity, which is why verdicts for items like 2.7 (not_supported) and 1.1 (partial) are qualified in their notes: the explicit statements in the sources apply to the documented version, and newer generations (fourth generation fielded in 2015 [2]) may behave differently. The USAspending award record [3] is high-confidence procurement evidence that the program is active through 2029 but carries no capability information, so it appears in the bibliography and overview rather than as item-level evidence.

---

## Bibliography

[1] GlobalSecurity.org. "RADIANT MERCURY [RM]". https://www.globalsecurity.org/intell/systems/radiant_mercury.htm (Retrieved: 2026-08-11T08:55:55Z)
[2] Shephard Media. "US Navy awards Radiant Mercury support contract". https://www.shephardmedia.com/news/digital-battlespace/us-navy-awards-radiant-mercury-support-contract/ (Retrieved: 2026-08-11T08:56:01Z)
[3] USAspending.gov (U.S. Department of the Treasury). "Award detail - CONT_IDV_N0003919D0006_9700 (RADIANT MERCURY (RADMERC))". https://api.usaspending.gov/api/v2/awards/CONT_IDV_N0003919D0006_9700/ (Retrieved: 2026-08-11T09:07:24Z)
[4] Wikipedia. "Radiant Mercury - Wikipedia". https://en.wikipedia.org/wiki/Radiant_Mercury (Retrieved: 2026-08-11T09:12:54Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 4 (kept: 4, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** regulatory_filing: 1, third_party_review: 3
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
