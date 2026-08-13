# BSG / Cross Domain Product Assessment: Owl Cyber Defense - Owl ReCon / Owl Talon Bidirectional Gateway

**Product ID:** `owl-recon-owl-talon-bidirectional-gateway`
**Version reference:** ReCon (D026 V4, 11-29-22), ReCon 2U (D129 V1, 08-24-23), Owl Talon One: Bidirectional (D137 V1, 4-30-2025), Owl Talon Torrent 1U (11-13-2025), IXD Tera (D086 V5, 10-4-2024)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:29:21Z
**Total evidence items collected:** 54
**Total distinct sources:** 10

---

## 1. Overview

Owl Cyber Defense's bidirectional gateway family combines two hardware-enforced one-way data diode paths inside a single appliance to create a secure round-trip, bidirectional channel between networks at different security levels [1, 2]. The product line spans the legacy ReCon / ReCon 2U - two completely independent data diodes in one 1U/2U enclosure - and Owl Talon One: Bidirectional, which pairs two independent 1U diode paths on OnLogic MK100 hardware; Owl's current bidirectional-capable industrial cross domain appliance is IXD Tera, and the vendor directs ReCon buyers to IXD because ReCon is no longer generally available for commercial sale and is sold exclusively through Dell [1, 3]. The vendor positions the family as a cross domain solution / protocol-break guard - a fusion of content filtering, NGFW-style data-flow restriction, and hardware-enforced diode separation - not a standard firewall [9]. Deployment shapes include remote access, remote command and control, remote monitoring, safety-system isolation, SCADA data replication and secure file transfer between OT and IT networks, in 1U/2U rack-mount form factors [2, 3, 5].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 4                | 4      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 11 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | high | - | The ReCon datasheet states there is no direct pass-through of TCP/IP traffic, and the certified XDE Radium diode's destination FPGA rebuilds packet headers for pre-defined destinations, i.e. TCP/IP sessions are terminated and reconstructed at the boundary; Talon One: Bidirectional pairs two one-way diodes for round-trip communication. [3], [5], [10] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | high | - | ReCon/ReCon 2U house two completely independent one-way data-diode paths in a single enclosure, Talon One: Bidirectional uses two independent 1U diode paths, and the certified XDE Radium module is built around two FPGAs plus an optical/digital isolator. [3], [5], [10] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | - | ReCon restricts session initiation so TCP/IP connections originate only from the trusted source side with a fixed destination IP, the XDE Radium configuration utility defines source/destination whitelisted connections, and IXD documents whitelisting/blacklisting of commands and file types. [5], [7], [10] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | Talon One and Talon Torrent datasheets list SELinux enforcement, a STIG-compliant OS, BIOS password and disk encryption (Torrent adds TPM binding), and the IXD appliance runs RHEL with SELinux in enforcing mode. [3], [4], [7] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No source describes cryptographic signing/stamping of transferred data inside the gateway.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No full content disarm & reconstruction of Office/PDF/image/CAD formats is documented for ReCon/Talon; IXD documents content inspection/filtering but not parse-and-rebuild CDR.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No evidence of macro/script (VBA, JavaScript, DDE) removal in transferred files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No antivirus engine integration is documented for the gateway family.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | - | Owl's current IXD bidirectional cross-domain appliance documents content inspection with XML schema validation and normalizes/filters data against schemas; JSON, FIXM and AIXM schema checking are not documented. [7] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (Information-flow control is described, but not filtering based on security labels attached to files.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No keyword/regex data-loss-prevention filtering (secrets, IDs, accounts) is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography detection/removal is documented for image files.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | ReCon documents FTPS and Talon One supports SFTP, while the IXD use case covers one-way SFTP file transfer and bidirectional HTTPS communications; SMB/NFS proxying with content cleaning is not documented. [3], [5], [9] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | - | ReCon/ReCon 2U support DNP3, Ethernet/IP, IEC-104 and ICCP for SCADA/process-control traffic, and Talon One adds OPC DA/A&E, OPC UA and MQTT. [2], [3] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | - | ReCon documents MS SQL database replication, and the IXD appliance supports bidirectional database communications with an Oracle TNS adapter; PostgreSQL and SQL query whitelisting are not documented. [5], [9] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Talon One: Bidirectional supports Remote Desktop bidirectionally plus Remote Screen View, Syslog and SNMP traps one-way, and Owl markets its diodes for streaming logs/telemetry to SOC/SIEMs; RTSP video proxying is not documented for this gateway. [3], [8] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | The Talon One: Bidirectional datasheet specifies up to 1 Gbps max throughput (the OTO card transfers one-way at up to 1 Gbps), meeting the >=1000 Mbps requirement; the one-way Talon Torrent variant reaches 10 Gbps. [3], [7] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | Owl describes Talon Torrent as low-latency/ultra-low-latency, but publishes no numeric latency figure, so the <=10 ms requirement cannot be verified. [4], [8] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | The Talon Torrent datasheet lists High Availability support as Coming Soon, while Owl's current IXD bidirectional appliance is marketed as high availability with redundancy and failover; no switchover time is published, so the <=100 ms no-session-loss requirement is unverified. [4], [7], [9] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | - | The Common Criteria report documents fail-secure behavior for the XDE Radium diode: any major component failure stops data flow entirely and power loss drops all buffered data, preventing unintended flow past the TSF. [10] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | - | ReCon/ReCon 2U provide separate administration for the source and destination sides with a menu-driven interface that restricts command-line access; separation of system-admin, policy-admin and auditor roles is not documented. [5], [6] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Talon One supports Syslog and SNMP traps for log/telemetry export, and Owl markets its diodes for streaming logs to SOC/SIEMs; CEF-formatted logs over a TLS-encrypted channel are not documented. [3], [8] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | - | The Owl XDE Radium v1.3 diode (core of Talon One) holds Common Criteria EAL4+ (EAL4 augmented with AVA_VAN.4), certified 2022-09-19 under the Swedish CSEC scheme with CCRA/SOGIS/EA-MLA recognition, and ReCon 2U is listed as EAL4+ Certified in its datasheet. [3], [6], [10] |

---

## 4. Notable Strengths

- **Protocol-break architecture (items 1.1, 1.2, 1.3):** ReCon explicitly documents no direct TCP/IP pass-through with restricted session initiation from the trusted source side only, built on two independent hardware data-diode paths with whitelisted connections [5, 10].
- **Hardened platform and fail-secure behavior (items 1.4, 4.4):** Talon One and Talon Torrent ship with SELinux enforcement, a STIG-compliant OS, BIOS password and disk encryption, and the certified XDE Radium diode fails closed - any major component failure stops data flow entirely [3, 4, 10].
- **Broad OT/ICS and database protocol support (items 3.2, 3.3):** DNP3, Ethernet/IP, IEC-104, ICCP, OPC DA/A&E, OPC UA and MQTT, plus MS SQL database replication, cover SCADA and historian use cases [2, 3, 5].
- **1 Gbps bidirectional throughput (item 4.1):** Talon One: Bidirectional is rated up to 1 Gbps max throughput, meeting the ≥ 1000 Mbps requirement; the one-way Talon Torrent variant reaches 10 Gbps [3, 7].
- **EAL4+ certification with registry confirmation (item 5.4):** The XDE Radium diode core holds Common Criteria EAL4+ (EAL4 + AVA_VAN.4), certified 2022-09-19 under the Swedish CSEC scheme with CCRA/SOGIS/EA-MLA recognition, and ReCon 2U is listed as EAL4+ Certified [3, 6, 10].

## 5. Notable Gaps / Risks

- **High availability not yet delivered (item 4.3):** The Talon datasheet lists HA support as "Coming Soon" and no switchover time is published anywhere, so the ≤ 100 ms active-standby requirement is unmet for the gateway family; the IXD appliance's HA claims also lack a failover-time figure [4, 7, 9].
- **No CDR / AV / label-based filtering evidence (items 2.1–2.3, 2.5–2.7):** Content disarm & reconstruction, multi-AV scanning, security-label IFC, DLP keyword filtering and anti-steganography are not documented for ReCon/Talon; only the IXD appliance covers XML schema validation and content filtering [7].
- **Product lifecycle risk (ReCon):** ReCon is no longer generally available for commercial sale and is exclusive to Dell, so buyers of the named product must evaluate IXD Tera or Talon One: Bidirectional as the current path [1].
- **Latency and SIEM integration details unpublished (items 4.2, 5.2):** Only qualitative "low latency" language is available with no millisecond figure, and log export is documented as Syslog/SNMP without the CEF-over-TLS channel the requirement asks for [3, 8].
- **Role-based administration is partial (item 5.1):** Separate source/destination administration exists, but system-admin / policy-admin / auditor role separation is not documented [5, 6].

## 6. Evidence Quality Notes

Evidence was collected from 10 staged sources: 9 vendor sources (product pages and datasheets for ReCon, ReCon 2U, Talon One: Bidirectional, Talon Torrent and IXD Tera, plus the Owl data-diode product page) and 1 independent registry source (the Common Criteria certification report for the XDE Radium v1.3 diode, CSEC2021009). Four items (1.1, 1.2, 1.3, 5.4) reach high confidence by triangulating vendor datasheets against the certification registry; all other non-unknown items rely on vendor documentation only and are capped at medium confidence per the project's validator rule.

No source contradictions were observed - the certification report corroborates the vendor's architectural claims (packet-header rebuild, whitelisted connections, fail-secure behavior) rather than conflicting with them. Items marked unknown (1.5, 2.1–2.3, 2.5–2.7, 5.3) reflect genuine absence of evidence in the staged material, not confirmed non-support; the CDR/AV/label/DLP/steganography gaps would need OEM documentation or a lab evaluation to resolve. The main weakness is vendor-centricity: with only one independent registry source, performance, latency and protocol-behavior claims remain unverified by third-party testing.

---

## Bibliography

[1] Owl Cyber Defense. "ReCon Secure Bi-Directional Network Communication | Owl Cyber Defense". https://owlcyberdefense.com/product/recon/ (Retrieved: 2026-08-11T08:29:21Z)
[2] Owl Cyber Defense. "ReCon 2U - Secure Round Trip, Bidirectional Communication | Owl Cyber Defense". https://owlcyberdefense.com/product/recon-2u/ (Retrieved: 2026-08-11T08:29:21Z)
[3] Owl Cyber Defense. "Owl Talon One: Bidirectional Data Diode - Data Sheet (D137, V1, 4-30-2025)". https://owlcyberdefense.com/product/owl-talon-one-bidirectional/ (Retrieved: 2026-08-11T08:29:21Z)
[4] Owl Cyber Defense. "Owl Talon Torrent 1U Data Diode - Data Sheet (11-13-2025)". https://owlcyberdefense.com/product/owl-talon-torrent-1u/ (Retrieved: 2026-08-11T08:29:21Z)
[5] Owl Cyber Defense. "ReCon Data Sheet - Secure Bi-Directional Data Diode Communication (D026, V4, 11-29-22)". https://owlcyberdefense.com/wp-content/uploads/2019/05/19-OWL-0105-Data-Sheet-Redesign-ReCon-V4.pdf (Retrieved: 2026-08-11T08:29:21Z)
[6] Owl Cyber Defense. "ReCon 2U Data Sheet - Secure Bidirectional Communications (D129, V1, 08-24-23)". https://owlcyberdefense.com/wp-content/uploads/2023/08/23-OWL-0354-Recon-2U-Datasheet-V1-3.pdf (Retrieved: 2026-08-11T08:29:21Z)
[7] Owl Cyber Defense. "IXD Tera - Industrial Cross Domain Solution Data Sheet (D086, V5, 10-4-2024)". https://owlcyberdefense.com/wp-content/uploads/2021/05/21-OWL-0108-IXD-Data-Sheet-V6.pdf (Retrieved: 2026-08-11T08:29:21Z)
[8] Owl Cyber Defense. "Owl Data Diodes: Hardware-Enforced & Protocol Aware | Owl Cyber Defense". https://owlcyberdefense.com/products/data-diode-products/ (Retrieved: 2026-08-11T08:29:21Z)
[9] Owl Cyber Defense. "Industrial Cross Domain Solutions for OT Threat Detection - IXD Tera | Owl Cyber Defense". https://owlcyberdefense.com/product/industrial-cross-domain/ (Retrieved: 2026-08-11T08:29:21Z)
[10] Swedish Certification Body for IT Security (CSEC). "Certification Report - Owl XDE Radium v1.3 (CSEC2021009), Swedish Certification Body for IT Security". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/Certification%20Report%20-%20Owl%20XDE%20Radium%20v13.pdf (Retrieved: 2026-08-11T08:29:21Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 10 (kept: 10, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 5, government: 1, web: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
