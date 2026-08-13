# BSG / Cross Domain Product Assessment: Terafence - Terafence V-Gate (gateway family: Vsecure 20/50, A4Gate, TFG121, MBsecure+, OPC Air-Gap)

**Product ID:** `terafence-v-gate`
**Version reference:** Gateway family as documented on terafence.com (2022-03 datasheets; TFG121 technical brief; MBsecure v2018 manual)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T16:00:00Z
**Total evidence items collected:** 49
**Total distinct sources:** 22

---

## 1. Overview

Terafence is an Israeli data-diode / unidirectional-gateway vendor. The provider-list entry "V-Gate" has no literal product of that name on terafence.com and is assessed here as the vendor's gateway family (Vsecure 20/50 video gateway, A4Gate, TFG121 file-transfer and email-relay, MBsecure+ Modbus gateway, OPC air-gap unit), all built on a proprietary FPGA core that has no OS, IP or MAC address on the security hardware and two accompanying CPUs for protocol termination [1, 6]. The vendor positions the family as enforcing one-way data flow with galvanic separation between OT/IT, PLC/HMI or camera/control-center segments [1, 14, 17]. Independent coverage - a JETRO regional report (2023) [20], a Permian Basin Oil & Gas Magazine feature [21] and a CRI Middleware stock-market disclosure on the Okinawa defense-facility deployment [22] - confirms deployments protecting IoT/OT assets and surveillance cameras. Deployment shapes are inline hardware units between network segments of different classification, rated at 1 Gbps throughput [12, 17]. It is neither a bidirectional protocol-break CDS nor a standard NGFW: content sanitization (CDR) is positioned as separate servers air-gapped by the diodes [10].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 2                | 6      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 10 items backed by ≥ 2 source_types; 13 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | high | - | Vendor documents the gateway as a protocol proxy that terminates TCP/IP sessions on both ends and moves raw data between two unidirectional sides whose core has no IP address, OS or CPU, with galvanic separation like a data diode for OPC. Independent coverage corroborates physical-layer data-direction control that blocks external attack traffic on Vsecure. [1], [6], [17], [21], [22] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | medium | - | Vendor documents Board A/B processing sides with two accompanying CPUs and hardware-based data-flow control on a proprietary FPGA chip providing galvanic separation; the a4Gate spec lists separate board A and board B CPUs. [1], [4], [14], [17] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | - | Vendor documents allowlist behavior: only configured HMI addresses are served and all other requests are dropped, with complete blocking of information flow and no return path once a direction is set. Independent coverage states Vsecure blocks all external attack traffic while maintaining video delivery. [1], [12], [19], [22] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | Vendor documents hardened Linux on the accompanying CPUs of TFG121/OPC/Vsecure units and states the core security hardware has no OS, MAC or IP address, with security layers split across hardware (L1-2), Linux (L3-4) and software (L5-7). [12], [14], [17] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No public documentation of internal data stamping/signing of clean data before new sessions are initiated.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Not Supported | medium | - | The vendor's technical brief states the unit acts as a protocol proxy moving raw data between two unidirectional sides without storage, and its CDR/XDR article describes deploying separate CDR servers with air gaps on both sides rather than in-unit disassembly and reconstruction of Office/PDF/image/CAD files. [10], [17] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No public documentation of macro/script removal (VBA, JavaScript, DDE links, embedded objects).) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No public documentation of multi-engine antivirus scanning of raw payloads.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No public documentation of XML/JSON/FIXM/AIXM schema validation.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No public documentation of filtering based on security labels attached to files.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No public documentation of keyword/regex DLP rules (secrets, ID numbers, accounts).) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No public documentation of steganography detection or removal in image files.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | The file-transfer gateway supports SMB/SAMBA, SFTP and HTTP/S upload with mixed-protocol operation, and the platform table lists SMB/FTP/SFTP transfer; the unit forwards raw data without content sanitization. [7], [11] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | - | Vendor documents Modbus (RTU over TCP/IP, up to 247 devices), IEC-104, MQTT, OPC DA/UA and conversion of 350 vendor-specific PLC protocols to OPC/UA tags across the TFG121, OPC and MBsecure units. [5], [6], [14], [17], [18] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | - | The platform protocol table lists MS-SQL replication across the gateway; no Oracle or PostgreSQL proxy and no query whitelisting is documented. [11] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Supported | medium | - | Vendor documents RTSP CCTV live streaming and syslog forwarding (TCP/UDP) through the TFG121 gateway and lists RTSP/Onvif and syslog in the platform protocol table. [11], [17] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | Vendor datasheets state 1 Gbps data throughput across TFG121, OPC and Vsecure units, meeting the 1000 Mbps requirement. [12], [14], [17] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.03 ms | The MBsecure datasheet cites near-zero average latency of 30 microseconds through the unit, equivalent to 0.03 ms, and the a4Gate page states zero induced latency, both within the 10 ms limit. [4], [18] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Vendor mentions HA unit redundancy (MBsecure), optional unit clustering (Vsecure) and redundant power inputs (TFG121), but publishes no failover switchover time, so the 100 ms requirement cannot be verified. [12], [17], [18] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | The IEC 62443 SL2 assessment quote states the solution exposes no service and is considered immune to direct attacks with a physical data-diode protection level; an explicit fail-close boundary lockout under overload is not documented, and Vsecure's self-resurrection is listed as a future release. [9], [12] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (No public documentation of role separation between system admin, policy admin and auditor.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Vendor documents syslog forwarding (TFG121) and syslog support (MBsecure) for log export; CEF format and a TLS-encrypted log channel to a SIEM are not documented. [5], [17] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No public documentation of compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001).) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | - | Vendor documents an IEC 62443-4-2 SL2 security-level assessment for the TFG121 performed under an ISA/IEC 62443 specialist's supervision, plus CE/FCC Class B and MIL-STD-810F marks; no Common Criteria (EAL4+), FIPS 140-3 or national cryptographic certification is documented. [9], [16], [17] |

---

## 4. Notable Strengths

- **FPGA hardware isolation with protocol break (items 1.1, 1.2):** the core security hardware has no IP address, OS or CPU; sessions are terminated on both ends and raw data moved one-way between two unidirectional sides, corroborated by independent coverage of the Vsecure camera deployment [1, 6, 17, 22].
- **Default-deny / allowlist behavior (item 1.3):** only configured HMI addresses are served and all other requests are dropped, with no return path once a direction is set [19].
- **OT/ICS protocol breadth (item 3.2):** Modbus (up to 247 devices), IEC-104, MQTT, OPC DA/UA and conversion of 350 vendor-specific PLC protocols to OPC/UA tags across the family [6, 17, 18].
- **Throughput and latency (items 4.1, 4.2):** 1 Gbps data throughput on TFG121/OPC/Vsecure units and 30-microsecond average latency through the MBsecure unit [12, 17, 18].
- **Real-world deployment validation (items 5.4, 1.1):** IEC 62443-4-2 SL2 assessment of the TFG121 plus documented deployments at Okinawa defense facilities and a US building-security company [9, 22].

## 5. Notable Gaps / Risks

- **No in-unit CDR (item 2.1):** the diode forwards raw data between two sides; the vendor's own article positions CDR/XDR servers as separate components with air gaps on both sides, so Office/PDF/image/CAD disassembly-reconstruction must be added externally [10, 17].
- **HA failover time unpublished (item 4.3):** only qualitative HA mentions (unit redundancy, optional unit clustering, redundant power) exist; no switchover figure is published to verify the 100 ms requirement [12, 17, 18].
- **Management and compliance gaps (items 5.1, 5.3):** no role-based separation of system admin / policy admin / auditor and no compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) are documented.
- **Certification gap (item 5.4):** no Common Criteria (EAL4+), FIPS 140-3 or national cryptographic certification is documented; the IEC 62443-4-2 SL2 mark is a vendor-reported assessment rather than an accredited-body certification [9, 16, 17].
- **Nine items unknown (1.5, 2.2-2.7, 5.1, 5.3):** no public evidence of internal data stamping, macro/script removal, multi-AV scanning, schema validation, security-label IFC, DLP keyword rules, anti-steganography, RBAC or compliance reports - the vendor publishes no admin guides for the newer units that would clarify these.

## 6. Evidence Quality Notes

Ten items are backed by two or more source types and thirteen rely on vendor documentation alone (confidence capped at medium by the validator). Three independent sources were located and staged: a JETRO regional report (2023) [20] confirming the company's cybersecurity-for-IoT positioning, a Permian Basin Oil & Gas Magazine article quoting Terafence on the Vsecure camera hardware buffer [21], and a CRI Middleware disclosure (TSE-listed partner) describing the Vsecure deployment at Okinawa defense facilities [22]. Items 1.1 and 1.3 reach high confidence by triangulating vendor architecture claims with the CRI disclosure's physical-layer direction control and attack-traffic blocking; all other items stay at medium. No source contradictions were found; the closest is the a4Gate variant pairing a Windows 10 IoT Enterprise board with an Ubuntu board, which is recorded as a gap under item 1.4 rather than contradicting the hardened-Linux claims of the TFG121/OPC/Vsecure units.

Two caveats shape this assessment. First, "V-Gate" is not a literal Terafence product name, so each item's evidence is drawn from whichever family member documents the capability (e.g. latency from the MBsecure datasheet, throughput from TFG121/OPC/Vsecure, protocols from the TFG121 brief); the assessment should be read as covering the family, not a single SKU. Second, search-engine access is blocked from this environment, so third-party discovery relied on outbound links from terafence.com; no independent lab test or penetration report was found, and the IEC 62443 SL2 result is vendor-reported.

---

## Bibliography

[1] Terafence. "Technology - hardware FPGA isolation (product family technology page)". https://terafence.com/technology/ (Retrieved: 2026-08-11T16:00:00Z)
[2] Terafence. "About Terafence - Unidirectional Gateway and Data Diode". https://terafence.com/about-terafence-cybersecurity/ (Retrieved: 2026-08-11T16:00:00Z)
[3] Terafence. "Terafence Vsecure 20/50 - product page". https://terafence.com/product/terafence-vsecure-20-50/ (Retrieved: 2026-08-11T16:00:00Z)
[4] Terafence. "A4Gate - Terafence inside - product page". https://terafence.com/product/a4gate-terafence-inside/ (Retrieved: 2026-08-11T16:00:00Z)
[5] Terafence. "TF MBsecure+ - product page". https://terafence.com/product/terafence-mbsecure/ (Retrieved: 2026-08-11T16:00:00Z)
[6] Terafence. "OPC for Air Gapped Networks - product page". https://terafence.com/product/opc-for-air-gapped-networks/ (Retrieved: 2026-08-11T16:00:00Z)
[7] Terafence. "Terafence File Transfer - TFG121 - product page". https://terafence.com/product/terafence-file-transfer-tfg121/ (Retrieved: 2026-08-11T16:00:00Z)
[8] Terafence. "Terafence Email-Relay - TFG121 - product page". https://terafence.com/product/terafence-email-relay-tfg121/ (Retrieved: 2026-08-11T16:00:00Z)
[9] Terafence. "Terafence TFG obtained the Security Level Assessment IEC62443-4-2, SL2 (news)". https://terafence.com/news/terafence-tfg-obtained-the-security-level-assessment-iec62443-4-2-sl2/ (Retrieved: 2026-08-11T16:00:00Z)
[10] Terafence. "Terafence for CDR/XDR File Cleansing Architecture (news)". https://terafence.com/news/terafence-for-cdr-xdr-file-cleansing-architecture/ (Retrieved: 2026-08-11T16:00:00Z)
[11] Terafence. "Terafence for OT/IT Convergence - platform protocol table". https://terafence.com/terafence-for-ot-it-convergence/ (Retrieved: 2026-08-11T16:00:00Z)
[12] Terafence. "Terafence Vsecure 20|50 - Data Sheet". https://terafence.com/wp-content/uploads/2022/03/Terafence-Vsecure-Data-Sheet.pdf (Retrieved: 2026-08-11T16:00:00Z)
[13] Terafence. "Terafence Vsecure 20|50 - Technical Brief". https://terafence.com/wp-content/uploads/2022/03/Terafence-Vsecure-Technical-Brief30.pdf (Retrieved: 2026-08-11T16:00:00Z)
[14] Terafence. "Terafence OPC Solutions for Air Gapped Networks (A4GATE) - datasheet". https://terafence.com/wp-content/uploads/2022/03/Terafence-OPC-Solutions-A4GATE-copy.pdf (Retrieved: 2026-08-11T16:00:00Z)
[15] Terafence. "Terafence File Transfer for Air Gapped Networks (TFG121) - datasheet". https://terafence.com/wp-content/uploads/2022/03/Terafence-File-Transfer-Solutions-TFG121-copy.pdf (Retrieved: 2026-08-11T16:00:00Z)
[16] Terafence. "Terafence Email-Relay for Air Gapped Networks (TFG121) - datasheet". https://terafence.com/wp-content/uploads/2022/03/Terafence-Email-Relay-Solutions-TFG121.pdf (Retrieved: 2026-08-11T16:00:00Z)
[17] Terafence. "Terafence TFG-121 - Technical Brief". https://terafence.com/wp-content/uploads/2022/03/Terafence-TFG121-Technical-Brief88.pdf (Retrieved: 2026-08-11T16:00:00Z)
[18] Terafence. "Terafence MBsecure+ - datasheet". https://terafence.com/wp-content/uploads/2019/01/Terafence-TF_MBsecure-1.pdf (Retrieved: 2026-08-11T16:00:00Z)
[19] Terafence. "Terafence MBsecure - Installation and Configuration Manual". https://terafence.com/wp-content/uploads/2019/01/TF_MBsecure-Installation-and-Configuration-Manual.pdf (Retrieved: 2026-08-11T16:00:00Z)
[20] JETRO (Japan External Trade Organization). "JETRO Regional Report - Israel SUS Overseas Strategy (Terafence interview, 13 June 2023)". https://www.jetro.go.jp/biz/areareports/2023/c30350a2e0d6dca0.html (Retrieved: 2026-08-11T16:00:00Z)
[21] PBO (Permian Basin Oil and Gas Magazine). "The Keys to the Castle - Permian Basin Oil and Gas Magazine (Terafence Vsecure coverage)". https://pboilandgasmagazine.com/the-keys-to-the-castle/ (Retrieved: 2026-08-11T16:00:00Z)
[22] CRI Middleware Co., Ltd. (TSE Mothers 3698). "CRI Middleware news release: Terafence Vsecure adopted at Okinawa defense facilities (2021-06-01)". https://assets.minkabu.jp/news/article_media_content/urn:newsml:tdnet.info:20210601436314/140120210601436314.pdf (Retrieved: 2026-08-11T16:00:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 15
- **Sources reviewed:** 22 (kept: 22, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 3, vendor_blog: 2, vendor_datasheet: 7, vendor_doc: 10
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
