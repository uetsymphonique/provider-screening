# BSG / Cross Domain Product Assessment: BAE Systems — BAE Systems Cross Domain Solution

**Product ID:** `bae-systems-cross-domain-solution`
**Version reference:** XTS Guard 7 (launched 2019; 2025 product page), XTS Diode, Data Diode Solution, XTS IRIS Large Scale Enterprise (UK CAPS, June 2024), Secure Voice and Video Gateway, STOP 8.8.2 (Common Criteria, 15 Sept 2023)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T10:20:46Z
**Total evidence items collected:** 47
**Total distinct sources:** 21

---

## 1. Overview

BAE Systems markets its Cross Domain Solution as a high-assurance CDS family, not a firewall: it covers multi-directional guards, one-way transfer (OWT) devices, and hardware CDS appliances built on the proprietary STOP high-assurance GPOS [7]. The core guard, XTS Guard 7, enables secure sharing between networks of varying security classifications and enclaves, is NSA/NCDSMO Raise-the-Bar compliant, and ships in enterprise, small-form-factor and ruggedized (XTS-Hercules with Crystal Group) chassis [3][7]. The family also includes the XTS Diode and Data Diode Solution OWT devices - the Data Diode Solution is Common Criteria EAL 7+ certified and NCDSMO baseline approved [10] - and the XTS IRIS hardware appliance family, whose Large Scale Enterprise platform passes 160 Gbps wire-speed with FPGA processing blades [2][4]. The Secure Voice and Video Gateway (SVG) provides hardware-enforced real-time VoIP/VTC streaming between domains [19]. BAE reports hundreds of deployments across the DoD, intelligence community, coalition partners and foreign militaries [7]. Certifications and registrations span UK CAPS (XTS IRIS and SVG, June 2024) [2], Common Criteria (STOP 8.8.2, GPOS PP 4.2.1, September 2023; Data Diode EAL 7+) [6][10], and the NATO IA product catalogue (XTS Diode) [17].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 3                | 2      | 0   |
| partial          | 11    | 0                | 11     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 5 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | — | XTS Guard 7 is a multi-directional guard whose kernel-enforced STOP OS maintains security-domain separation, and the XTS IRIS hardware platform removes general-purpose operating systems from the data path; the Data Diode converts data into sequenced UDP packets at the boundary with no return path, i.e. sessions are terminated and reconstructed rather than routed. [1], [4], [5], [10] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | — | Hardware-based isolation is documented: XTS IRIS hosts security controls on FPGA processing blades and the Data Diode is a fibre-optic hardware device connecting two domain-attached servers with no shared software stack; a specific dual-independent-processing-board design is not stated for the guard SKUs. [4], [5], [8] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | The RTB-compliant guards support a fixed protocol set with deep content filtering, described as ensuring 'your data (and nothing else)' is transferred, which implies allow-list behaviour; explicit default-deny/whitelist-only documentation was not found. [1], [4], [13] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | high | — | XTS Guard is built on the STOP Secure Trusted Operating Program, a 64-bit GPOS designed around mandatory access control policies that cannot be disabled, and STOP 8.8.2 was Common Criteria certified against the GPOS PP 4.2.1 in September 2023. [1], [6], [9] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No source describes cryptographic signing/stamping of transferred data before session re-initiation inside the gateway.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | — | Deep content inspection with file-sanitization filters covering SMTP, XML, common office files, imagery and chat is documented, and RTB compliance requires filtering/sanitizing/decomposing data; a full parse-and-rebuild CDR guarantee for all Office/PDF/image/CAD formats is not claimed. [1], [13], [20] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Partial | medium | — | File-sanitization and deep content inspection filters for common office files are documented, which remove dangerous content; explicit removal of VBA macros, JavaScript, DDE links or embedded objects is not itemized. [1], [20] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | XTS Guard 7 ships redundant native anti-virus filters and supports plug-in of multiple content filters; the number of concurrently scanning AV engines (2+) is not specified. [1], [7] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | — | Schema validation and redundant native XML filters are documented for XTS Guard 7; JSON, FIXM and AIXM schema conformance is not specified. [1], [7] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (Multi-enclave and multi-compartment controlled information sharing is documented, but per-file security-label (IFC) filtering is not described.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No data-loss-prevention keyword/regex filtering is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No anti-steganography engine is documented.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | XTS Guard 7 supports SFTP, SMTP, DSG, UDP, TCP and HTTP/s transfer with content inspection, and the Data Diode provides SMTP and file-transfer applications; FTP/S and SMB/NFS proxies are not documented. [1], [5], [7] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found (No OT/ICS protocol proxies (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) are documented.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No database protocol proxies (SQL Server, Oracle, PostgreSQL) are documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | The Secure Voice and Video Gateway provides hardware-enforced real-time VoIP/VTC streaming between domains, and the XTS Diode streams ISR data over UDP/TCP; RTSP video proxy or syslog/CEF relay specifics are not documented. [8], [19] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | high | 160000 Mbps | The XTS IRIS Large Scale Enterprise platform is specified at 160 Gbps wire-speed throughput, while the XTS Diode is rated up to 40 Gbps (10 Gb/s per its datasheet); both exceed the 1 Gbps requirement. [2], [4], [15], [21] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 10 ms | The XTS Diode datasheet specifies latency below 10 ms and the XTS Tactical Guard is described as low latency; the value 10 ms is used as the documented upper bound. [7], [12] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | 6000 ms | The Data Diode Solution's High Availability Library performs automatic failover in less than six seconds (6000 ms), which does not meet the 100 ms switchover requirement. [10] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No explicit fail-closed behaviour under DoS or hardware attack is documented for the guard family.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | XTS Guard 7 enforces multiple mandatory access controls and role-based policies at the kernel level with advanced administration and auditing; separation of System Admin / Policy Admin / Auditor roles is not explicitly documented. [1], [7] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | The XTS Diode datasheet documents audit log files with syslog export and SNMP traps (v1 and v3); CEF format and TLS-encrypted log transport to a SIEM are not specified. [5], [12] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No compliance-report templates for NIST SP 800-82, IEC 62443 or ISO 27001 are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | — | The Data Diode Solution is Common Criteria EAL 7+ certified and NCDSMO baseline approved; STOP 8.8.2 is CC-certified (GPOS PP 4.2.1, Sept 2023); XTS IRIS and the SVG passed the UK CAPS evaluation (June 2024); the XTS Diode was the first device named RTB-compliant by NCDSMO/NSA and XTS Guard 7 is NCDSMO-listed. [2], [6], [10], [11], [16], [17], [18] |

---

## 4. Notable Strengths

- **Hardware-based, RTB-compliant architecture (items 1.1, 1.2, 1.4):** XTS Guard 7 runs on the kernel-enforced STOP OS, and the XTS IRIS platform hosts security controls on FPGA processing blades with no general-purpose OS in the data path [1][4].
- **Certification depth (item 5.4):** Common Criteria EAL 7+ for the Data Diode Solution [10], CC-certified STOP 8.8.2 (GPOS PP 4.2.1) [6], UK CAPS for XTS IRIS and SVG [2], and XTS Diode named the first RTB-compliant device by NCDSMO/NSA [17].
- **Wire-speed throughput (item 4.1):** XTS IRIS Large Scale Enterprise is specified at 160 Gbps [2], with the XTS Diode rated up to 40 Gbps [21] - far above the 1 Gbps requirement.
- **Deep content inspection with plug-in filters (items 2.1, 2.3, 2.4):** anti-virus, schema/XML validation and file-sanitization filters are native, with a simple API for additional content filters [1][7].
- **Real-time media and streaming (item 3.4):** the SVG delivers hardware-enforced VoIP/VTC between domains [19], and the XTS Diode streams ISR data over UDP/TCP [8].

## 5. Notable Gaps / Risks

- **HA switchover time (item 4.3):** the documented HAL failover for the Data Diode Solution is under six seconds, far above the 100 ms requirement [10] - a shortfall to confirm against the specific SKU.
- **OT/ICS protocol support (item 3.2):** no OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT proxies are documented anywhere in the public material, so industrial-zone deployments remain unverified.
- **IFC, DLP and anti-steganography (items 2.5, 2.6, 2.7):** multi-enclave/multi-compartment sharing is described, but per-file security-label filtering, DLP keyword/regex blocking, and steganography detection are not documented.
- **Explicit default-deny (item 1.3):** allow-list behaviour is implied by the RTB design and the fixed protocol set, but is not documented in those words; a buyer needing a written whitelist-only guarantee should request the security target.
- **Database and file-protocol breadth (items 3.3, 3.1):** no SQL/Oracle/PostgreSQL proxies are documented, and FTP/S and SMB/NFS are absent from the documented protocol list (SFTP/SMTP/HTTP/s are covered) [7].

## 6. Evidence Quality Notes

13 of 24 items are backed by at least 2 source_types, and the 3 high-confidence items (1.4, 4.1, 5.4) each combine a non-vendor source (certification registries, trade press, or independent comparison) with vendor material. Items 3.4, 4.2, 4.3 and 5.2 rest on vendor-only material (product pages and NATO-hosted datasheets), so their confidence is capped at medium per the validator rule. 8 items (1.5, 2.5, 2.6, 2.7, 3.2, 3.3, 4.4, 5.3) are marked unknown: no public BAE documentation covers internal data stamping, security-label IFC, DLP, anti-steganography, OT/ICS or database protocol proxies, fail-close behaviour, or compliance-report templates - absence of evidence, not evidence of absence.

The main cross-source tension is throughput across SKUs and document revisions: the XTS Diode is quoted at 10 Gb/s in its datasheet [12], 32-40 Gbps by Iron Bow and the NATO catalogue [17][21], and the XTS IRIS Large Scale Enterprise at 160 Gbps [2][4]; these reflect different product lines rather than contradictions, so item 4.1 cites the flagship XTS IRIS figure with the diode range noted. Domain counts for XTS Guard 7 also differ between 2019 press coverage (up to 28 [13]) and the current product page (22 enterprise [7]); the current vendor figure is attributed. Vendor pages on baesystems.com are bot-protected and were staged via a rendering proxy, with two vendor datasheets staged from the NATO IA portal; all 47 quoted evidence fragments were verified verbatim against staged text by verify_citation_grounding.py.

---

## Bibliography

[1] Iron Bow Technologies. "Strengthening Military Cross Domain Solutions with XTS Guard 7 (Iron Bow TechSource)". https://ironbow.com/techsource/strengthening-military-cross-domain-solutions-with-xts-guard-7 (Retrieved: 2026-08-11T10:20:06Z)
[2] Military Embedded Systems. "Cross domain solution from BAE Systems passes UK CAPS evaluation". https://militaryembedded.com/avionics/computers/cross-domain-solution-from-bae-systems-passes-uk-caps-evaluation (Retrieved: 2026-08-11T10:20:06Z)
[3] Crystal Group. "Secure Connectivity at the Edge: BAE Systems & Crystal Group Join Forces (XTS-Hercules)". https://www.crystalrugged.com/crystal-group-collaborates-with-bae-systems-on-new-cross-domain-solution-for-commercial-market/ (Retrieved: 2026-08-11T10:20:06Z)
[4] ASDNews / BAE Systems PLC. "BAE Newest Cross Domain Solution Passes UK CAPS Evaluation (BAE Systems press release reprint)". https://www.asdnews.com/news/defense/2024/06/20/bae-newest-cross-domain-solution-passes-uk-caps-evaluation (Retrieved: 2026-08-11T10:20:06Z)
[5] BAE Systems Insyte / NATO IA. "Data Diode datasheet (BC283008.02.v06) - Interactive Link Data Diode ILL301, hosted on NATO IA portal". https://www.ia.nato.int/DocumentGenerator/repository/version/9bb63c9c-9984-4ec4-bb8c-90a29004d679/BAE-System-Data-Diode---EAL-7-Manufacturer (Retrieved: 2026-08-11T10:20:06Z)
[6] Canadian Centre for Cyber Security (CCCS) / CC Portal. "Common Criteria Certification Report - BAE Systems STOP 8.8.2 (15 September 2023, Canadian Centre for Cyber Security)". https://www.commoncriteriaportal.org/files/epfiles/553-EWA%20CR%20v1.0.pdf (Retrieved: 2026-08-11T10:20:06Z)
[7] BAE Systems. "Cross Domain Solutions: XTS Guard 7 - BAE Systems product page". https://www.baesystems.com/en-us/product/xts-guard-7 (Retrieved: 2026-08-11T10:20:06Z)
[8] BAE Systems. "Cross Domain Solutions: XTS Diode - BAE Systems product page". https://www.baesystems.com/en-us/product/xts-diode (Retrieved: 2026-08-11T10:20:06Z)
[9] BAE Systems. "Cross Domain Solutions: STOP High Assurance GPOS - BAE Systems product page". https://www.baesystems.com/en-us/product/stop (Retrieved: 2026-08-11T10:20:06Z)
[10] BAE Systems. "Cross Domain Solutions: Data Diode Solution - BAE Systems product page". https://www.baesystems.com/en-us/product/data-diode-solution (Retrieved: 2026-08-11T10:20:06Z)
[11] BAE Systems. "Cybersecurity Cross Domain Solutions portfolio - BAE Systems product page". https://www.baesystems.com/en-us/product/cybersecurity-products-portfolio (Retrieved: 2026-08-11T10:20:06Z)
[12] BAE Systems / NATO IA. "XTS Diode One Way Transfer Solution datasheet (c. 2022), hosted on NATO IA portal". https://www.ia.nato.int/DocumentGenerator/repository/version/7d356b69-8ff3-4cd3-aef1-709d5514b763/XTS-Diode (Retrieved: 2026-08-11T10:20:06Z)
[13] Help Net Security. "BAE Systems' XTS Guard 7 provides secure access to geospatial imagery and data". https://www.helpnetsecurity.com/2019/08/20/xts-guard-7/ (Retrieved: 2026-08-11T10:20:06Z)
[14] Defence Online. "BAE Systems launches XTS Guard 7 cyber security solution". https://www.defenceonline.co.uk/2019/08/29/bae-systems-xts-guard-7/ (Retrieved: 2026-08-11T10:20:06Z)
[15] Network Critical. "Top 7 Data Diodes for Government and Defense Networks (vendor comparison, 2026)". https://www.networkcritical.com/blogs/data-diodes-for-government-and-defense-networks (Retrieved: 2026-08-11T10:20:06Z)
[16] NSA NCDSMO. "National Cross Domain Strategy & Management Office (NCDSMO) - NSA page". https://www.nsa.gov/Cybersecurity/Partnership/National-Cross-Domain-Strategy-Management-Office/ (Retrieved: 2026-08-11T10:20:06Z)
[17] NATO IA (NIAPC). "NATO Information Assurance Product Catalogue (NIAPC) entry: BAE Systems XTS Diode". https://www.ia.nato.int/niapc/Product/https---www.baesystems.com-en-us-product-xts-diode_836 (Retrieved: 2026-08-11T10:20:06Z)
[18] NCSC UK. "CAPS Assisted Products - Introduction (UK National Cyber Security Centre)". https://www.ncsc.gov.uk/schemes/caps-assisted-products/introduction (Retrieved: 2026-08-11T10:20:06Z)
[19] BAE Systems. "Cross Domain Solutions: Secure Voice and Video Communications (SVG) - BAE Systems product page". https://www.baesystems.com/en/product/cross-domain-solutions-secure-voice-and-video-communications (Retrieved: 2026-08-11T10:20:06Z)
[20] CMI Inc.. "XTS Guard - CMI Cybersecurity Solutions (BAE Systems channel partner page)". https://cmi-inc.ca/wordpress/xts-guard/ (Retrieved: 2026-08-11T10:20:06Z)
[21] Iron Bow Technologies. "Revolutionizing Data Transfer Security in Military Operations with XTS Diode One Way Transfer (Iron Bow TechSource)". https://ironbow.com/techsource/revolutionizing-data-transfer-security-in-military-operations-with-xts-diode-one-way-transfer (Retrieved: 2026-08-11T10:20:06Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 21 (kept: 21, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 2, government: 4, web: 15
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
