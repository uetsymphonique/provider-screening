# BSG / Cross Domain Product Assessment: Nozomi Networks — Nozomi Networks Guardian (OT/ICS network monitoring sensor; listed as 'Guardian Security Gateway' in the BSG provider list)

**Product ID:** `guardian-security-gateway`
**Version reference:** N2OS 26.4.0 (2026); Guardian sensor hardware NSG-HS/NSG-H/NSG-M/NS1/ruggedized/virtual series
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:30:00+00:00
**Total evidence items collected:** 62
**Total distinct sources:** 24

---

## 1. Overview

Nozomi Networks does not market a product named "Guardian Security Gateway"; the BSG provider-list entry corresponds to the Nozomi Networks Guardian sensor, an OT/ICS and IoT network monitoring product. Guardian is positioned as a passive network security sensor, not a cross domain solution or a filtering gateway: it observes copies of traffic from mirrored SPAN ports or TAPs to build asset inventory, baseline behavior, and detect anomalies and threats, without injecting packets or forwarding traffic between domains [1], [23]. The vendor's own description is that "The Nozomi Guardian security sensor passively observes and analyzes local network traffic" [1], and an Enel case study calls the technology "non-intrusive" [22]. Deployment shapes are hardware appliances (NSG-HS/NSG-H/NSG-M/NS1/ruggedized), virtual machines, containers, and embedded Siemens platforms, managed by the on-prem Central Management Console or the cloud Vantage platform [1], [6]. Because the product is a monitoring sensor rather than a protocol-break guard or industrial firewall, the checklist's gateway- and CDS-specific items are predominantly not applicable.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 0                | 2      | 0   |
| partial          | 5     | 0                | 5      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 12    | 2                | 10     | 0   |

**Evidence quality:** 8 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Nozomi markets Guardian as a passive network security sensor, not a security gateway: it observes mirrored traffic on SPAN ports or taps and forwards no traffic between domains, so a protocol-break boundary function is not part of its architecture.
- **1.3:** Guardian is passive-only: it does not filter or block any packets and is positioned for environments that prohibit active querying, so whitelist-based default-deny forwarding is not applicable to a sensor that forwards no traffic.
- **1.5:** Guardian has no control core that signs internal data before re-initiating sessions; as a passive monitoring sensor it does not implement internal data stamping.
- **2.1:** Guardian performs passive packet inspection of mirrored traffic only; no content disarm and reconstruction (CDR) of Office, PDF, image, or CAD files is documented for the sensor.
- **2.2:** The sensor can reconstruct monitored files for analysis (quarantine) but does not strip macros, scripts, DDE links, or embedded objects from files; no file-sanitization capability is documented.
- **2.4:** Guardian parses network protocols but provides no W3C-schema validation of XML, JSON, FIXM, or AIXM files; the checklist's schema-validation capability is CDS-specific and not part of the passive sensor.
- **2.5:** No information-flow control based on security labels attached to files is documented; the sensor does not filter data by classification label.
- **2.7:** No image-file processing or anti-steganography scanning is documented; the passive sensor does not analyze image content.
- **3.1:** Guardian parses file-transfer protocols such as FTP/FTPS and SMB passively but provides no file-transfer proxy with content cleaning; proxying is not part of the monitoring-sensor architecture.
- **3.3:** Guardian parses database protocols such as SQL Server and Oracle TNS passively but provides no database proxy with query whitelisting; proxying is outside the sensor's architecture.
- **4.1:** Guardian performs no CDR, so no CDR inspection throughput exists; the vendor instead documents passive monitoring throughput up to 6 Gbps on the largest appliance (NSG-HS 3500), with 'up to' caveats depending on the analyzed traffic.
- **4.4:** Guardian sits transparently on mirrored ports and is designed not to disrupt traffic; as a passive sensor with no boundary enforcement, fail-close behavior under DoS is not applicable.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | high | — | Nozomi markets Guardian as a passive network security sensor, not a security gateway: it observes mirrored traffic on SPAN ports or taps and forwards no traffic between domains, so a protocol-break boundary function is not part of its architecture. [1], [5], [22], [23] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No documentation of dual processing boards, FPGA, or isolated shared-memory links was found; hardware specs document redundant power supplies and RAID-1 storage only.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | N/A | medium | — | Guardian is passive-only: it does not filter or block any packets and is positioned for environments that prohibit active querying, so whitelist-based default-deny forwarding is not applicable to a sensor that forwards no traffic. [1], [23] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | Guardian runs on the dedicated Nozomi Networks Operating System (N2OS), which supports a FIPS-140-2-approved cryptography module, and the vendor describes the platform as hardened. No hardening standard (e.g., SELinux strict mode or microkernel design) is documented. [15], [16], [20] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | Guardian has no control core that signs internal data before re-initiating sessions; as a passive monitoring sensor it does not implement internal data stamping. [1] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | high | — | Guardian performs passive packet inspection of mirrored traffic only; no content disarm and reconstruction (CDR) of Office, PDF, image, or CAD files is documented for the sensor. [1], [5], [23] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | N/A | medium | — | The sensor can reconstruct monitored files for analysis (quarantine) but does not strip macros, scripts, DDE links, or embedded objects from files; no file-sanitization capability is documented. [1], [17] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No embedded third-party antivirus engines are documented; Guardian's malware detection uses its own signature/YARA-based engine, and no parallel multi-AV scanning of raw payloads is described.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | Guardian parses network protocols but provides no W3C-schema validation of XML, JSON, FIXM, or AIXM files; the checklist's schema-validation capability is CDS-specific and not part of the passive sensor. [1] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No information-flow control based on security labels attached to files is documented; the sensor does not filter data by classification label. [1] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No DLP capability (secret keywords, national ID numbers, account data, custom regex blocking) is documented in the public material reviewed.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No image-file processing or anti-steganography scanning is documented; the passive sensor does not analyze image content. [1] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | N/A | medium | — | Guardian parses file-transfer protocols such as FTP/FTPS and SMB passively but provides no file-transfer proxy with content cleaning; proxying is not part of the monitoring-sensor architecture. [8], [23] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | Guardian performs protocol-aware deep packet inspection of the checklist's OT protocols (Modbus TCP/RTU, DNP3, IEC 60870-5-104, OPC UA, MQTT) plus many others, but only passively - it provides no industrial proxy or content-cleaning function. [3], [8], [22], [23] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | N/A | medium | — | Guardian parses database protocols such as SQL Server and Oracle TNS passively but provides no database proxy with query whitelisting; proxying is outside the sensor's architecture. [8], [23] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | Guardian passively captures and forwards syslog events (alerts, health, audit) to SIEM endpoints and parses RTSP traffic, but it provides no RTSP video proxy; the syslog/CEF relay is unidirectional to the SIEM. [8], [17], [19] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | N/A | medium | — | Guardian performs no CDR, so no CDR inspection throughput exists; the vendor instead documents passive monitoring throughput up to 6 Gbps on the largest appliance (NSG-HS 3500), with 'up to' caveats depending on the analyzed traffic. [1], [3] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No processing-latency figures for the sensor are published in the vendor documentation or third-party material reviewed.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found (No active-standby failover with a switchover-time specification is documented; the only high-availability reference found describes CMC-to-CMC data replication, not session-preserving failover.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | N/A | medium | — | Guardian sits transparently on mirrored ports and is designed not to disrupt traffic; as a passive sensor with no boundary enforcement, fail-close behavior under DoS is not applicable. [1], [23] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | — | Guardian management supports group-based RBAC with per-section permissions, admin groups, and zone/node filters, and Vantage defines default roles including Admin, functional Operators, and read-only Observer/Superobserver with access scoped by organization, tag, or site. [17], [24] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | — | Guardian ships CEF and syslog forwarders (with a TLS option and CA-certificate validation) that push alerts, health, and audit events to SIEM endpoints, plus a QRadar app and integrations for Splunk, ArcSight, LogRhythm, Exabeam, and Swimlane. [3], [13], [17], [23] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | The vendor documents compliance support with an ISA/IEC 62443 mapping guide (parts 2-1 and 3-3) and automation/demonstration of NERC CIP compliance; report templates for NIST SP 800-82 or ISO 27001 specifically are not documented. [9], [10] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | — | Guardian's cryptographic library completed FIPS 140-2 validation testing from NIST (2022 press release) and N2OS supports a FIPS-140-2-approved cryptography module, while the trust center lists ISO 27001 and SOC 2 Type II organizational certifications; no FIPS 140-3 or Common Criteria certification is documented. [3], [11], [15], [16] |

---

## 4. Notable Strengths

- **Broad OT/ICS protocol inspection (item 3.2):** Guardian decodes Modbus TCP/RTU, DNP3, IEC 60870-5-104, OPC UA, MQTT and many other protocols down to field level, although strictly passively [8], [23].
- **SIEM/SOAR integration (item 5.2):** CEF and syslog forwarders with a TLS encryption option plus a QRadar app and integrations for Splunk, ArcSight, LogRhythm, Exabeam and Swimlane push alerts, health and audit events to SOC tooling [17], [13], [3].
- **Role/group-based administration (item 5.1):** management supports group-based RBAC with per-section permissions, zone and node filters, and Vantage default roles (Admin, Operators, Observer/Superobserver) scoped by organization, tag or site [17], [24].
- **FIPS 140-2 validated cryptography (item 5.4):** the Guardian cryptographic library completed FIPS 140-2 validation testing from NIST, and N2OS supports a FIPS-140-2-approved cryptography module [15], [16].
- **Regulatory compliance support (item 5.3):** the vendor publishes an ISA/IEC 62443 (parts 2-1, 3-3) mapping guide and documents NERC CIP compliance automation [9], [10].

## 5. Notable Gaps / Risks

- **Product class mismatch for a BSG procurement (items 1.1, 2.1, 3.1-3.4, 4.1, 4.4):** Guardian is a passive monitoring sensor and provides none of the gateway functions the checklist requires (protocol break, CDR, proxying, fail-close, CDR throughput), so it cannot serve as a Bidirectional Security Gateway; buyers needing a BSG should select a different product.
- **No FIPS 140-3 or Common Criteria certification (item 5.4):** only FIPS 140-2 (2022) and organizational ISO 27001/SOC 2 attestations are documented, which may fall short of EAL4+/FIPS 140-3 requirements [15], [11].
- **Unknowns for HA-reliant or low-latency use (items 4.2, 4.3):** no processing-latency figures and no active-standby failover with a switchover-time specification are published; the only HA reference is CMC-to-CMC data replication.
- **No hardware isolation evidence (item 1.2):** dual processing boards or FPGA/shared-memory isolation between processing elements are not documented, only redundant power and RAID storage [3].
- **Missing file-security capabilities (items 2.3, 2.6):** no multi-AV scanning of payloads or DLP (keyword/ID/regex blocking) is documented, so content-level protection cannot be assumed.

## 6. Evidence Quality Notes

24 sources were staged (17 web pages, 7 PDFs). Category-establishing items (1.1, 2.1, 3.2) were triangulated across the vendor product page, the product-overview datasheet, one independent technical blog (Techclick) and a vendor-hosted Enel case study; 8 items draw on at least two source types. However, 11 items rest on vendor documentation only, which caps their confidence at medium per the project's validator rule — including the two supported items (5.1, 5.2), whose documentation is detailed but single-party. The only genuinely independent source is the Techclick blog, so "high" confidence is reserved for the two category items (1.1, 2.1) where the passive-sensor classification is corroborated across all four sources.

No contradictions between sources were found; the dominant pattern is absence rather than disagreement. Unknown verdicts (1.2, 2.3, 2.6, 4.2, 4.3) reflect that the capabilities are simply not addressed in any public material reviewed — they were not marked not_supported because no source states their absence. One naming discrepancy is flagged: no Nozomi source uses the name "Guardian Security Gateway", and this assessment was scoped to the Guardian sensor as the closest real product, which is itself a material finding for the buyer.

---

## Bibliography

[1] Nozomi Networks. "Guardian Sensor | OT Network Monitoring (product page)". https://www.nozominetworks.com/platform/guardian (Retrieved: 2026-08-11T08:56:08Z)
[2] Nozomi Networks. "Guardian Product Overview (resource page)". https://www.nozominetworks.com/resources/guardian-product-overview (Retrieved: 2026-08-11T08:56:08Z)
[3] Nozomi Networks. "Technical Specifications & Protocols (platform page)". https://www.nozominetworks.com/platform/technical-specifications (Retrieved: 2026-08-11T08:56:58Z)
[4] Nozomi Networks. "Guardian Specifications Sheet (resource page)". https://www.nozominetworks.com/resources/specifications-sheet-guardian-sensors (Retrieved: 2026-08-11T08:56:58Z)
[5] Nozomi Networks. "Nozomi Networks Guardian Sensor Product Overview (PDF)". https://cdn.prod.website-files.com/645a4534705010e2cb244f50/65b101b7dc27996910aa56dc_Nozomi-Networks-Guardian-Sensor-Product-Overview.pdf (Retrieved: 2026-08-11T08:56:58Z)
[6] Nozomi Networks. "Nozomi Central Management Console (product page)". https://www.nozominetworks.com/platform/central-management-console (Retrieved: 2026-08-11T08:57:16Z)
[7] Nozomi Networks. "Nozomi Networks Protocol Support List (resource page)". https://www.nozominetworks.com/resources/protocol-support-list (Retrieved: 2026-08-11T08:57:16Z)
[8] Nozomi Networks. "Nozomi Networks Guardian Supported Protocol List (PDF)". https://cdn.prod.website-files.com/645a4534705010e2cb244f50/69a1139bfcf928505516333a_Nozomi-Networks-Protocol-Support-List.pdf (Retrieved: 2026-08-11T08:57:23Z)
[9] Nozomi Networks. "Applying the ISA/IEC 62443 Standards for IACS Security (page)". https://www.nozominetworks.com/compliance/isa-iec-62443-standards (Retrieved: 2026-08-11T08:57:30Z)
[10] Nozomi Networks. "NERC CIP compliance for NA Electric Utilities (page)". https://www.nozominetworks.com/compliance/nerc-cip (Retrieved: 2026-08-11T08:57:31Z)
[11] Nozomi Networks. "Nozomi Networks Trust Center (page)". https://www.nozominetworks.com/trust-center (Retrieved: 2026-08-11T08:58:00Z)
[12] Nozomi Networks. "Nozomi Networks Support (page)". https://www.nozominetworks.com/support (Retrieved: 2026-08-11T08:58:00Z)
[13] Nozomi Networks. "The Nozomi Networks App for QRadar (partner page)". https://www.nozominetworks.com/partners/ibm-qradar (Retrieved: 2026-08-11T08:58:49Z)
[14] Nozomi Networks. "Technology Alliance Ecosystem (page)". https://www.nozominetworks.com/technology-alliance-ecosystem (Retrieved: 2026-08-11T08:58:49Z)
[15] Nozomi Networks. "Nozomi Networks Is FIPS Compliant (press release)". https://www.nozominetworks.com/press-release/nozomi-networks-achieves-fips-compliance (Retrieved: 2026-08-11T09:01:04Z)
[16] Nozomi Networks (technicaldocs). "Federal Information Processing Standards (N2OS docs)". https://technicaldocs.nozominetworks.com/products/n2os/topics/fips/c_fips_3.html (Retrieved: 2026-08-11T09:01:05Z)
[17] Nozomi Networks (technicaldocs). "Guardian Administrator Guide v26.4.0 (PDF)". https://technicaldocs.nozominetworks.com/out/pdf-output/Guardian-Administrator%20Guide.pdf (Retrieved: 2026-08-11T09:01:16Z)
[18] Nozomi Networks (technicaldocs). "Guardian User Guide v26.4.0 (PDF)". https://technicaldocs.nozominetworks.com/out/pdf-output/Guardian-User%20Guide.pdf (Retrieved: 2026-08-11T09:01:22Z)
[19] Nozomi Networks (technicaldocs). "N2OS Configuration-Reference Guide v26.4.0 (PDF)". https://technicaldocs.nozominetworks.com/out/pdf-output/N2OS%20Configuration-Reference%20Guide.pdf (Retrieved: 2026-08-11T09:01:30Z)
[20] Nozomi Networks (technicaldocs). "Federal Information Processing Standards - Reference Guide (PDF)". https://technicaldocs.nozominetworks.com/out/pdf-output/Federal%20Information%20Processing%20Standards-Reference%20Guide.pdf (Retrieved: 2026-08-11T09:02:26Z)
[21] Nozomi Networks (technicaldocs). "N2OS v26.4.0 Release Highlights (docs)". https://technicaldocs.nozominetworks.com/products/n2os/release-notes/26.4.0/r_n2os_release_highlights.html (Retrieved: 2026-08-11T09:02:44Z)
[22] Nozomi Networks (Enel case study). "Enel Secures their Global Power Generation Network (case study)". https://www.nozominetworks.com/resources/enel-secures-global-power-generation-network (Retrieved: 2026-08-11T09:02:59Z)
[23] Techclick. "Nozomi Guardian Sensor - Passive DPI, Asset Discovery (Techclick blog)". https://ai.techclick.in/blog_nozomi_guardian_deep_dive (Retrieved: 2026-08-11T09:03:10Z)
[24] Nozomi Networks (technicaldocs). "Vantage Administrator Guide (PDF)". https://technicaldocs.nozominetworks.com/out/pdf-output/Vantage-Administrator%20Guide.pdf (Retrieved: 2026-08-11T09:04:04Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 24 (kept: 24, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** html: 17, pdf: 7
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
