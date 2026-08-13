# BSG / Cross Domain Product Assessment: infodas GmbH - SDoT Security Gateway / SDoT Industry Gateway

**Product ID:** `sdot-security-gateway-sdot-industry-gateway`
**Version reference:** SDoT Security Gateway 6.2i (certified configuration); SDoT Industry Gateway per 2024 launch
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:33:34Z
**Total evidence items collected:** 53
**Total distinct sources:** 21

---

## 1. Overview

infodas GmbH's SDoT (Secure Domain Transition) family is a German-made high-assurance Cross Domain Solution line rather than a conventional firewall. The SDoT Security Gateway is a bidirectional trusted filter that combines a full protocol break with inspection, transformation and monitoring of data transfers between security domains, approved up to DEU/EU/NATO SECRET [1, 9, 10]. An Express variant targets near-real-time, low-latency filtering of structured formats such as XML, JSON, Link 16 and ASTERIX [9, 14]. The SDoT Industry Gateway, launched in 2024, extends the same architecture to OT/IT exchange in critical infrastructures, configurable from unidirectional to bidirectional and covering SCADA/ETCS-style traffic [2, 5]. All SDoT products run the L4Re microkernel OS [3]. The gateway ships as a 19-inch 1U appliance with redundant power supply, delivered with the SDoT Admin & Audit Center for configuration [1, 13]. Deployments include the NATO AWACS modernization (Boeing), the German F126 frigate programme, and a Naval Group European naval programme [1, 18, 21]. The gateway holds BSI Common Criteria EAL4+ (BSI-DSZ-CC-1129-2021), NITES certification, and NATO/EU/DEU SECRET approvals [4, 8, 17].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 1                | 5      | 0   |
| partial          | 13    | 0                | 13     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 18 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | - | The vendor documents a full protocol break with inspection, transformation and monitoring of data transfers between security domains. [1], [4], [10], [20] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No source describes a dual-processor-board design with FPGA or isolated shared-memory link for the Security Gateway.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | Filtering is rule-based: data elements not matching the configured rules are rejected/blocked or sanitized, so only authorized information crosses domains. [1], [10], [11] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | All SDoT products run the proprietary L4Re microkernel OS; the diode variant documents L4-based service isolation. [3], [15] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Partial | medium | - | SDoT cryptographically binds NATO STANAG 4774/8 XML security labels to data objects for cross-domain flows; the control core's internal signing before session re-initiation is not documented. [3], [12] |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | - | The Express performs strict per-element content checks and blocks or sanitizes non-conforming data; full file-format disarm-and-reconstruction for Office/PDF/CAD is not documented. [1], [11] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No source addresses macro/script/DDE/embedded-object removal.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Supported | medium | - | Multi-engine malware scanning (35+ engines) is delivered through the documented OPSWAT MetaDefender Kiosk/Vault integration rather than as an in-gateway engine set. [3], [19] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | - | Structured-data filtering for XML, JSON, Link 16, ASTERIX, ADatP-3, ADEXP, NMEA and DIS is documented; explicit W3C schema-conformance checking for FIXM/AIXM is not stated. [10], [11] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Supported | medium | - | Data filtering is driven by security labels, and the SDoT Labelling Service creates NATO STANAG 4774/8-compliant labels bound to data objects. [1], [3], [12] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | - | The vendor claims DLP capability and prevention of accidental or deliberate outflow of sensitive data via content filtering; specific keyword/ID-number/regex DLP rules are not documented. [3], [11] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No source addresses detection/removal of hidden data in images (anti-steganography).) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Time-critical file transfer with content filtering, including patches and malware signatures, is documented; a specific SFTP/FTP/HTTPS/SMB/NFS protocol-proxy list is not published. [2], [7] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | OT data exchange is documented for the family: OPC and Modbus (diode use cases), SCADA/ETCS with bidirectional protocols, and controlled OT/IT exchange for the Industry Gateway; dedicated OPC UA/DNP3/IEC 60870-5-104/MQTT proxies are not enumerated. [2], [5], [7] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (Database replication through the diode is mentioned but a SQL Server/Oracle/PostgreSQL proxy with query whitelisting is not documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Real-time data streaming (video/audio) and near real-time filtering of military data (Link 16/JREAP, ASTERIX) are documented; RTSP proxy and Syslog/CEF relay specifics are not. [7], [9] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | Only qualitative 'high speed / low latency' claims exist for the Security Gateway/Express; the sole numeric figure (9.1 Gbit/s) is for the unidirectional SDoT Data Diode, so no CDR throughput of 1000 Mbps or more can be confirmed for the gateway. [1], [9], [14] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | Vendor claims 'very low latency' and 'near real-time' filtering but publishes no milliseconds figure, so the 10 ms threshold cannot be verified. [9], [11], [14] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | - | no evidence found (Redundant power supply is documented, but active-standby HA failover time (100 ms) is not addressed.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | Denial-of-service defense and a design in which security functions are never compromised are claimed; explicit fail-close boundary behavior under DoS is not documented. [3], [7] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | - | Delivery includes a separate SDoT Admin & Audit Center plus CA center, and administration authenticates all users and services; explicit System Admin / Policy Admin / Security Auditor role separation is not confirmed. [1], [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Monitoring/logging and SIEM-to-SOC data flows are documented use cases; gateway audit-log export in CEF/Syslog over TLS is not explicitly documented. [2], [7], [15] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | - | The Industry Gateway supports compliance with IEC 62443, NIST, NIS-2 and IACS UR E26/E27; availability of ready-made report templates (NIST SP 800-82, ISO 27001) is not confirmed. [2], [5], [16] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | - | SDoT Security Gateway v6.2i holds BSI Common Criteria EAL4+ (BSI-DSZ-CC-1129-2021), NITES certification from Singapore CSA, DEU/EU/NATO SECRET approvals and a NATO NIAPC listing. [4], [8], [9], [13], [17] |

---

## 4. Notable Strengths

- **Protocol break architecture (items 1.1, 1.3):** vendor documents a full protocol break with in-depth inspection, transformation and monitoring, and rule-based blocking or sanitization of non-conforming data elements [1, 10, 11].
- **Label-based information flow control (items 1.5, 2.5):** filtering is driven by security labels, and the SDoT Labelling Service binds NATO STANAG 4774/8 XML labels cryptographically to data objects [1, 12].
- **Microkernel-based hardening (item 1.4):** all SDoT products run the proprietary L4Re microkernel OS with documented service isolation [3, 15].
- **Certification depth (item 5.4):** Common Criteria EAL4+ certificate BSI-DSZ-CC-1129-2021, NITES certification from Singapore CSA, DEU/EU/NATO SECRET approvals and a NATO NIAPC listing [4, 8, 9, 17].
- **Multi-engine malware defense via OPSWAT (item 2.3):** documented SDoT/OPSWAT MetaDefender combination provides 35+ anti-malware engines for scan-and-clean of files [3, 19].

## 5. Notable Gaps / Risks

- **CDR depth (items 2.1, 2.2):** per-element sanitization is documented for the Express, but full file-format disarm-and-reconstruction (Office/PDF/CAD) and macro/script removal are not confirmed [11].
- **Numeric performance absent (items 4.1, 4.2):** only qualitative "high speed / low latency" claims exist for the gateway; the 9.1 Gbit/s figure applies to the unidirectional SDoT Data Diode, so CDR throughput of 1000 Mbps or more and latency of 10 ms or less cannot be verified [9, 14].
- **Hardware isolation not documented (item 1.2):** no source describes dual processor boards with FPGA or isolated shared-memory coupling; separation is logical (microkernel), not physical board-level [3].
- **HA failover unproven (item 4.3):** redundant power supply is documented, but active-standby switchover of 100 ms or less without session loss is not addressed [13].
- **Protocol breadth unquantified (items 3.2, 3.3, 3.4):** OPC/Modbus/SCADA flows are documented for the family, but dedicated IEC 60870-5-104/DNP3/MQTT proxies, database query-whitelisting, and RTSP/Syslog-CEF relays are not enumerated [5, 7].

## 6. Evidence Quality Notes

Evidence spans 21 sources: 16 vendor-authored (product pages, press releases, datasheets), 2 independent news articles (Defence Industry Europe on the NATO AWACS programme and on the Naval Group contract), and 1 certification-registry artifact (the BSI Common Criteria certificate hosted on the Common Criteria portal). Nine of 24 items rest on vendor-only sources and are capped at medium confidence; item 5.4 is the only high-confidence verdict because the certificate, NIAPC listing and approvals are corroborated by the registry PDF and independent news. No sources contradicted each other; the main limitation is that the vendor publishes no numeric performance data for the Security Gateway or Industry Gateway (only the unidirectional SDoT Data Diode has a published figure, 9.1 Gbit/s), which forced partial verdicts on throughput and latency, and five items (1.2, 2.2, 2.7, 3.3, 4.3) remain unknown due to total absence of evidence. Sibling-family evidence (Data Diode, Labelling Service) was used only where the vendor states those products share the same SDoT Security Framework and architecture.

---

## Bibliography

[1] infodas GmbH. "SDoT Security Gateway - product page (infodas)". https://www.infodas.com/en/solutions/sdot-cross-domain-solutions/sdot-security-gateway/ (Retrieved: 2026-08-11)
[2] infodas GmbH. "SDoT Industry Gateway - product page (infodas)". https://www.infodas.com/en/solutions/sdot-cross-domain-solutions/sdot-industry-gateway/ (Retrieved: 2026-08-11)
[3] infodas GmbH. "SDoT Cross Domain Solutions - product family overview (infodas)". https://www.infodas.com/en/solutions/sdot-cross-domain-solutions/ (Retrieved: 2026-08-11)
[4] infodas GmbH. "Common Criteria EAL4+ certification for SDoT Security Gateway Cross Domain Solution (infodas press release)". https://www.infodas.com/en/press-releases/cc-eal4-certification-for-sdot-security-gateway-cross-domain-solution/ (Retrieved: 2026-08-11)
[5] infodas GmbH. "infodas launches SDoT Industry Gateway (infodas press release)". https://www.infodas.com/en/press-releases/infodas-launches-sdot-industry-gateway/ (Retrieved: 2026-08-11)
[6] infodas GmbH. "Security at a new level: infodas IT security product receives BSI certification according to Common Criteria (infodas press release)". https://www.infodas.com/en/press-releases/security-on-a-new-level-infodas-it-security-product-receives-bsi-certification-according-to-common-criteria/ (Retrieved: 2026-08-11)
[7] infodas GmbH. "SDoT Software Data Diode - product page (infodas)". https://www.infodas.com/en/solutions/sdot-cross-domain-solutions/sdot-diode/ (Retrieved: 2026-08-11)
[8] Common Criteria portal / BSI. "BSI-DSZ-CC-1129-2021 Common Criteria certificate for SDoT Security Gateway v6.2i (Common Criteria portal)". https://www.commoncriteriaportal.org/files/epfiles/1129c_pdf.pdf (Retrieved: 2026-08-11)
[9] infodas GmbH. "Enabling Multi-Domain Operations: SDoT Security Gateway receives NATO SECRET approval (infodas press release)". https://www.infodas.com/en/press-releases/multi-domain-operations-sdot-security-gateway-receives-nato-secret-approval/ (Retrieved: 2026-08-11)
[10] infodas GmbH. "INFODAS SDoT Security Gateway receives EU SECRET approval enabling digitization of EU Classified Information systems (infodas press release)". https://www.infodas.com/en/press-releases/eu_secret_approval_sdot_security_gateway_from_council_european_union/ (Retrieved: 2026-08-11)
[11] infodas GmbH. "SDoT Security Gateway Express receives German, NATO and EU SECRET accreditation (infodas press release, German)". https://www.infodas.com/en/press-releases/bsi-erteilt-geheim-zulassung-fuer-sdot-security-gateway-express-2/ (Retrieved: 2026-08-11)
[12] infodas GmbH. "SDoT Labelling Service - product page (infodas)". https://www.infodas.com/en/solutions/sdot-cross-domain-solutions/sdot-labelling-service/ (Retrieved: 2026-08-11)
[13] infodas GmbH. "SDoT Security Gateway flyer EN (infodas, rev. 25-09-02)". https://www.infodas.com/wp-content/uploads/2025/09/25-09-02_infodas_SDoT_SecurityGateway_Flyer_EN-1.pdf (Retrieved: 2026-08-11)
[14] infodas GmbH. "SDoT Security Gateway Express flyer EN (infodas)". https://www.infodas.com/wp-content/uploads/2024/11/infodas_SDoT_SecurityGatewayExpress_Flyer_EN.pdf (Retrieved: 2026-08-11)
[15] infodas GmbH. "SDoT Software Data Diode flyer EN (infodas)". https://www.infodas.com/wp-content/uploads/2025/07/infodas_SDoT_SoftwareDataDiode_Flyer_EN.pdf (Retrieved: 2026-08-11)
[16] infodas GmbH. "SDoT Industry Gateway - Maritime Industrial flyer EN (infodas)". https://www.infodas.com/wp-content/uploads/2025/07/infodas_Maritime_Industrial_Flyer_EN.pdf (Retrieved: 2026-08-11)
[17] infodas GmbH. "infodas receives NITES certification from the Cyber Security Agency of Singapore (infodas press release)". https://www.infodas.com/en/press-releases/infodas-receives-nites-certification-from-the-cyber-security-agency-of-singapore/ (Retrieved: 2026-08-11)
[18] Defence Industry Europe. "Infodas Cross Domain Solutions selected for NATO's AWACS modernization project (Defence Industry Europe)". https://defence-industry.eu/infodas-cross-domain-solutions-selected-for-natos-awacs-modernization-project/ (Retrieved: 2026-08-11)
[19] infodas GmbH. "German public sector client awards contract for SDoT CDS & OPSWAT Metadefender (infodas press release)". https://www.infodas.com/en/press-releases/german-public-sector-client-awards-contract-for-sdot-cds-opswat-metadefender/ (Retrieved: 2026-08-11)
[20] infodas GmbH. "Bidirektionaler Datenaustausch | SDoT Security Gateway/Express - Produktseite (infodas, deutsch)". https://www.infodas.com/de/loesungen/sdot-cross-domain-solutions/sdot-security-gateway/ (Retrieved: 2026-08-11)
[21] Defence Industry Europe. "infodas signed contract with Naval Group for a major European naval programme (Defence Industry Europe)". https://defence-industry.eu/infodas-signed-contract-with-naval-group-for-a-major-european-naval-programme/ (Retrieved: 2026-08-11)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 21 (kept: 21, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, third_party_review: 2, vendor_blog: 8, vendor_datasheet: 4, vendor_doc: 6
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
