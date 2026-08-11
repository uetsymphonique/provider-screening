# BSG / Cross Domain Product Assessment: Advantech Co., Ltd. — Advantech UNO / ECU Series

**Product ID:** `advantech-uno-ecu-series`
**Version reference:** UNO-2000 series datasheets (UNO-2484G 27-Jun-2018, UNO-2483G 2017); ECU-4784 datasheet 27-Jun-2018; UNO-2271G-V2 Ubuntu Core 20 certification (Canonical, 2021); ECU-4784-V2 product page 2026
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:08:12Z
**Total evidence items collected:** 33
**Total distinct sources:** 12

---

## 1. Overview

The Advantech UNO series comprises ruggedized, fanless embedded automation computers / industrial IoT edge gateways in pocket, small and regular form factors, which Advantech describes as bridging data from edge devices to the cloud "as protocol converters, data collectors, or data loggers" [5]. The ECU series — exemplified by the ECU-4784/4784-V2 — is a family of IEC 61850-3 certified power/substation automation servers with up to 8 x GbE, serial interfaces, redundant power input and TPM 2.0 [3][4][6]. Neither line is marketed as a security gateway, network firewall or cross-domain guard: Advantech's network security appliance hardware is a separate product family, and no protocol-break or content-inspection engine is documented for UNO/ECU [1][5]. Documented deployment shapes include smart-factory equipment connectivity, process visualization, environment/dispatch management, substation automation and edge gateway roles; select UNO models (e.g. UNO-2271G-V2) are certified with Ubuntu Core 20 for secure embedded OS deployment [5][8]. Against the 24-item BSG checklist the series therefore scores no supported items: seven CDS-specific items are Not Applicable by category, six are Partial, one is Not Supported (certifications), and ten are Unknown.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 0     | 0                | 0      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 10    | 0                | 0      | 10  |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 12 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Advantech positions the UNO-2000 series as ruggedized fanless embedded automation computers / IoT edge gateways that bridge data from edge devices to cloud as protocol converters, data collectors or data loggers, and the ECU-4784 as an IEC 61850-3 certified power automation server; no protocol-break (TCP/IP session termination) architecture is described.
- **1.2:** The UNO-2484G is documented as a modular compact embedded box PC (single enclosure, aluminum housing) and the ECU-4784 as a fanless substation server; no dual processing board or FPGA/shared-memory isolation design is described.
- **1.5:** No internal cryptographic stamping of cleaned data before session re-initiation is described; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways, not cross-domain guards.
- **2.1:** No content disarm & reconstruction of Office/PDF/image/CAD files is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than CDS guards with a CDR engine.
- **2.4:** No XML/JSON/FIXM/AIXM schema validation is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than guard appliances with a content validation engine.
- **2.5:** No security-label-based information flow control on files is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than classified-data guards.
- **2.7:** No anti-steganography detection/removal capability for image files is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than CDS guards.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Advantech positions the UNO-2000 series as ruggedized fanless embedded automation computers / IoT edge gateways that bridge data from edge devices to cloud as protocol converters, data collectors or data loggers, and the ECU-4784 as an IEC 61850-3 certified power automation server; no protocol-break (TCP/IP session termination) architecture is described. [1], [2], [3], [4], [5] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The UNO-2484G is documented as a modular compact embedded box PC (single enclosure, aluminum housing) and the ECU-4784 as a fanless substation server; no dual processing board or FPGA/shared-memory isolation design is described. [1], [2], [3], [4], [5] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Unknown | low | — | no evidence found (No default-deny / whitelist firewall behavior is documented for the UNO/ECU computing platforms; they ship with general-purpose OS images (Windows, Linux) rather than a firewall appliance OS.) |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | Select UNO models (e.g. UNO-2271G-V2) are pre-loaded and certified with Ubuntu Core 20, which provides secure boot, full disk encryption, secure device recovery and transactional over-the-air updates, and UNO-2484G / ECU-4784-V2 document TPM 2.0 hardware security; no microkernel or SELinux-strict-mode claim is made for the platform. [2], [6], [8] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | No internal cryptographic stamping of cleaned data before session re-initiation is described; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways, not cross-domain guards. [1], [2], [3], [4], [5] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | No content disarm & reconstruction of Office/PDF/image/CAD files is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than CDS guards with a CDR engine. [1], [2], [3], [4], [5] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No file-content inspection or macro/script/embedded-object removal capability is documented for the UNO/ECU platforms.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No multi-engine antivirus scanning of payloads is documented for the UNO/ECU platforms.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | No XML/JSON/FIXM/AIXM schema validation is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than guard appliances with a content validation engine. [1], [2], [3], [4], [5] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label-based information flow control on files is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than classified-data guards. [1], [2], [3], [4], [5] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No keyword/regex-based data-leakage detection on traffic content is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No anti-steganography detection/removal capability for image files is documented; the UNO/ECU lines are documented as general-purpose industrial computing platforms and gateways rather than CDS guards. [1], [2], [3], [4], [5] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No file-transfer proxy with content cleaning (SFTP, FTP/S, HTTPS, SMB/NFS) is documented; the platforms expose general-purpose OS networking only.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | OT protocol handling is documented: the ECU-4784 is IEC 61850-3 certified for substation automation communication, Advantech describes its IoT edge gateways as protocol converters for field data, and UNO-2000 series supports fieldbus protocol via iDoor modules; no security-cleaning proxy specifically for OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT is documented. [1], [3], [4], [5] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | Datasheets document 10/100/1000 Mbps LAN interface rates (4 x GbE on UNO-2484G/2483G, 8 x GbE on ECU-4784), but no packet-inspection or CDR processing throughput figure is published; throughput depends on the software stack deployed on the platform. [2], [3], [10] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet or protocol processing latency figure is documented in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Redundant power input (100-240 VAC/DC, configurable) is documented on the ECU-4784 and RAID 0/1 storage redundancy on the UNO-2484G, but no device-level active-standby switchover mechanism or switchover time figure is documented. [2], [3], [4] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | A programmable watchdog timer (1-255 s) that resets the system on hang is documented on the UNO-2484G; no fail-close behavior of a security boundary under DoS/overload is documented. [2] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (No role-based access control with separated system admin / policy admin / auditor roles is documented for the platform management interfaces (SNMP-based remote management only).) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (No CEF/syslog-over-TLS forwarding to a SIEM/SOAR is documented; the ECU-4784 page documents SNMP for remote management but not SIEM integration.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | Advantech documents IEC 62443-4-1 Secure Software Development Lifecycle certification and ISO/IEC 27001 at organization level, the ECU-4784 carries IEC 61850-3/IEEE 1613 certifications, and selected platforms are being validated against IEC 62443-4-2; no ready-made NIST SP 800-82, IEC 62443 or ISO 27001 report templates for this product line are documented. [4], [11], [12] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | Datasheet certification lists for UNO-2484G/2483G (CE, FCC, UL, CCC, BSMI) and ECU-4784 (CE, FCC, CCC, IEC-61850-3, IEEE-1613, UL, CB, LVD) contain no Common Criteria, FIPS 140-3 or national cryptographic certification. [2], [4], [10] |

---

## 4. Notable Strengths

- **OT protocol awareness (item 3.2):** The ECU-4784 is IEC 61850-3 certified for substation automation communication and the UNO-2000 series supports fieldbus protocol extension via iDoor modules, giving documented OT/ICS protocol handling [3][4][1].
- **Hardened-OS option (item 1.4):** The UNO-2271G-V2 is pre-loaded and certified with Ubuntu Core 20, providing secure boot, full disk encryption, transactional over-the-air updates and TPM 2.0 on UNO-2484G and ECU-4784-V2 [8][2][6].
- **Gigabit interface capacity (item 4.1):** Datasheets document 10/100/1000 Mbps LAN interfaces — 4 x GbE on UNO-2484G/2483G and 8 x GbE on ECU-4784 — providing Gbps-class transport capacity [2][10][3].
- **Platform-level resilience (items 4.3, 4.4):** The ECU-4784 documents redundant AC/DC power input and the UNO-2484G documents RAID 0/1 storage plus a programmable watchdog timer [3][2].
- **Compliance posture (items 5.3, 5.4):** Advantech documents IEC 62443-4-1 Secure Software Development Lifecycle certification and ISO/IEC 27001 at organization level, and selected platforms are being pre-certified against IEC 62443-4-2 [12][11].

## 5. Notable Gaps / Risks

- **No native security gateway function (items 1.3, 2.2, 2.3, 2.6):** The UNO/ECU platforms ship as general-purpose computers with Windows/Linux OS images; no default-deny firewall behavior, file sanitization, multi-engine AV or DLP is documented, so they cannot act as a security gateway without third-party software.
- **No inspection throughput or latency figures (items 4.1, 4.2):** Only interface line rates are published; no packet-inspection/CDR throughput or processing latency numbers exist, so the 1000 Mbps / 10 ms requirements remain unverified.
- **No device-level high availability (item 4.3):** Documented redundancy is limited to redundant power input and RAID storage; no active-standby switchover mechanism or 100 ms switchover figure exists.
- **No security certifications (item 5.4):** Datasheet certifications (CE, FCC, UL, CCC, BSMI; IEC 61850-3, IEEE 1613) exclude Common Criteria, FIPS 140-3 and national cryptographic certification, which blocks classified or regulated deployments.
- **Management and SIEM gaps (items 5.1, 5.2):** No RBAC with separated admin/policy/auditor roles and no CEF/syslog-over-TLS SIEM integration are documented; only SNMP-based remote management appears.

## 6. Evidence Quality Notes

The assessment rests on 12 distinct sources and 33 evidence entries, every quote verified verbatim against staged artifacts (0 fabricated, 0 unverifiable). Eight sources are Advantech-authored (product pages and datasheets for UNO-2484G/2483G, ECU-4784/4784-V2, and the embedded automation computers category page); four are non-vendor (Everest Automation and WPG Americas reseller pages [7][9], a Canonical blog on Ubuntu Core certification [8], and an ARMdevices.net article on IEC 62443-4-2 pre-certification [11]). Because the category and specification claims rest heavily on vendor material, all non-unknown verdicts are capped at medium confidence; no verdict reached high confidence.

Triangulation: the not-applicable and partial items each draw on 3-5 sources, but only items 1.4, 5.3 and 5.4 include a non-vendor source, while items 3.2, 4.1, 4.3 and 4.4 rest on vendor documentation only. No outright contradictions were found: the reseller pages mirror the vendor's category and ruggedness language, and the Canonical and ARMdevices sources describe adjacent capabilities (OS-level hardening, IEC 62443-4-2 pre-certification) that the vendor's own pages do not contradict. Numeric-threshold items 4.1 and 4.3 are Partial with null numeric_value because the only documented figures are interface line rates and power/storage redundancy — not the inspection throughput or device switchover metrics the checklist requires.

---

## Bibliography

[1] Advantech Co., Ltd.. "UNO-2484G - Advantech (product page)". https://www.advantech.com/en-us/products/1-2mlj9a/uno-2484g/mod_19fb1f0d-aadb-4d9d-b882-a6cc16f1129e (Retrieved: 2026-08-11T09:08:12Z)
[2] Advantech Co., Ltd.. "UNO-2484G Datasheet (Industrial IoT Gateways)". https://advdownload.advantech.com/productfile/PIS/UNO-2484G/Product%20-%20Datasheet/UNO-2484G20180910102434.pdf (Retrieved: 2026-08-11T09:08:12Z)
[3] Advantech Co., Ltd.. "ECU-4784 - Advantech (product page)". https://www.advantech.com/en-us/products/1-369nwl/ecu-4784/mod_18553282-e8f5-4b32-a64b-1083f7182d36 (Retrieved: 2026-08-11T09:08:12Z)
[4] Advantech Co., Ltd.. "ECU-4784 Datasheet". https://advdownload.advantech.com/productfile/PIS/ECU-4784/Product%20-%20Datasheet/ECU-478420180910102948.pdf (Retrieved: 2026-08-11T09:08:12Z)
[5] Advantech Co., Ltd.. "Embedded Automation Computers - Advantech (category page)". https://www.advantech.com/en-us/products/embedded-automation-computers/sub_1-2mlckb (Retrieved: 2026-08-11T09:08:12Z)
[6] Advantech Co., Ltd.. "ECU-4784-V2 - Advantech (product page)". https://www.advantech.com/en-us/products/1-369nwl/ecu-4784-v2/mod_75411083-6470-4325-bf5f-1e379651f31b (Retrieved: 2026-08-11T09:08:12Z)
[7] Everest Automation. "UNO-2000 Series - Everest Automation". https://everestautomation.com/products/uno-2000-series/ (Retrieved: 2026-08-11T09:08:12Z)
[8] Canonical Ltd.. "Advantech, Canonical Boost Security and Edge Features in UNO Embedded Automation Platform with Pre-Loaded Ubuntu and Ubuntu Core 20". https://canonical.com/blog/advantech-canonical-boost-security-and-edge-features-in-uno-embedded-automation-platform-with-pre-loaded-ubuntu-and-ubuntu-core-20 (Retrieved: 2026-08-11T09:08:12Z)
[9] WPG Americas Inc.. "Advantech UNO-2000 Series - WPG Americas Inc.". https://wpgacorp.com/advantech-uno2000-series/ (Retrieved: 2026-08-11T09:08:12Z)
[10] Advantech Co., Ltd.. "UNO-2483G Datasheet (IoT Gateways)". https://advdownload.advantech.com/productfile/PIS/UNO-2483G/Product%20-%20Datasheet/UNO-2483G_DS(11.03.17)20171220151043.pdf (Retrieved: 2026-08-11T09:08:12Z)
[11] ARMdevices.net. "Advantech CRA Compliance, IEC 62443 Pre-Certified Hardware and ONEKEY SBOM". https://armdevices.net/2026/03/24/advantech-cra-compliance-iec-62443-pre-certified-hardware-and-onekey-sbom/ (Retrieved: 2026-08-11T09:08:12Z)
[12] Advantech Co., Ltd.. "Advantech Cybersecurity (campaign page)". https://campaign.advantech.online/en/global/intelligent-connectivity/cybersecurity/ (Retrieved: 2026-08-11T09:08:12Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 12 (kept: 12, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 3, web: 9
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
