# BSG / Cross Domain Product Assessment: Lanner Electronics Inc. — Lanner ICS Security Gateway (ICS-P570 family)

**Product ID:** `lanner-ics-security-gateway`
**Version reference:** ICS-P570 datasheet rev V.1-2023.2,16 (2023); Lanner 'Industrial Edge' brochure Volume 25.1 (C) 2025; ICS-P570 User Manual v1.2 released 2023-12-14 (referenced, not staged)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:21:00Z
**Total evidence items collected:** 24
**Total distinct sources:** 9

---

## 1. Overview

Lanner Electronics is a Taiwanese hardware-platform manufacturer, and the assessed "Lanner ICS Security Gateway" is the ICS-P570, the flagship of Lanner's ICS (Industrial Cyber Security) gateway family; the assessment also draws family-level evidence from the sibling ICS-P371, LEC-6041 and ICS-P770/P550 platforms [1][2][6][8]. Lanner positions the ICS-P570 as an IEC 61850-3 wide-temperature industrial cybersecurity gateway "designed to protect communication in both IT and OT domains" [1][2], and its rugged industrial cyber security platforms as conducting protocol filtering, packet inspection, whitelisting and network traffic monitoring for ICS/SCADA networks [6]; the LEC-6041 is described as a rugged firewall [4]. The product is therefore a ruggedized industrial firewall/gateway hardware platform, not a cross-domain guard: the seven guard/CDS-specific checklist items (1.1, 1.2, 1.5, 2.1, 2.4, 2.5, 2.7) are marked unknown because no such capability is documented (product class alone does not establish a specific excluding fact). Deployment shapes documented include power substations, factory automation, railway and other harsh OT environments, on DIN-rail or wall mount, with dual DC power, TPM 2.0, LAN bypass and -40 to 70 C operation [1][2][5]. No bundled security software stack, throughput/latency figures, or HA failover design are documented in the reviewed sources; the security functions are described at platform level only [1][6].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 0     | 0                | 0      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 17    | 0                | 0      | 17  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 3 items backed by ≥ 2 source_types; 4 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Unknown | low | — | no evidence found (No TCP/IP protocol-break architecture is documented; the product is described only as an industrial firewall-class gateway.) |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No dual processing-board / FPGA / isolated shared-memory hardware isolation design is documented.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | The vendor documents that its industrial cyber security platforms are designed to conduct protocol filtering, packet inspection, white-listing and network traffic monitoring, and describes the LEC-6041 as a rugged firewall; however, no explicit default-deny enforcement or whitelist policy mechanism is documented for the ICS-P570. [4], [6] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No hardened-OS / microkernel / SELinux-strict-mode claim is documented; the datasheet lists Linux kernel driver support only.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No internal data-stamping / signing core for clean data before session re-initiation is documented.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No content disarm and reconstruction (CDR) of Office/PDF/Image/CAD files is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No file-content inspection or macro/script/embedded-object removal is documented for this firewall-class platform.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | The vendor's IEC brochure lists Antivirus/Malware scanning among the capabilities of its IIoT Network Security Gateway line within the Industrial OT Security Appliances family; no number of antivirus engines or parallel-scan implementation is documented. [6] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No XML/JSON/FIXM/AIXM W3C schema validation capability is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No security-label-based information flow control attached to files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | — | The vendor lists DLP/SIEM among the capabilities of its IIoT network security gateway line; no secret-keyword / ID-regex / customizable-pattern detection details are documented. [6] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No anti-steganography / hidden-data detection or removal engine for image files is documented.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No SFTP/FTP/S/HTTPS/SMB/NFS file-transfer proxy with content cleaning is documented.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The vendor documents that its rugged industrial cyber security platforms provide protection for ICS/SCADA networks with protocol filtering and lists Industrial UTM/Firewall/DPI and ICS/SCADA cyber security among target applications; no specific OT protocols (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) are named. [6] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | — | no evidence found (No processing/CDR inspection throughput figure is documented; the datasheet only specifies Ethernet link speeds (100M/1G/2.5Gbps on RJ45, 1Gbps on SFP).) |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet-processing or realtime-protocol latency figure is documented in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found (No active-standby failover or session-preserving switchover is documented for the ICS-P570; dual DC power input is documented but is power redundancy, not HA failover.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | The datasheet documents one pair of LAN bypass ports and a software-programmable watchdog timer for system reset, indicating availability-oriented failure handling; no fail-close boundary lockdown under DoS is documented. [1], [2] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (No role-based administration separation (system admin / policy admin / auditor) is documented.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | The vendor lists DLP/SIEM among the capabilities of its IIoT network security gateway line; no CEF/syslog log format or encrypted TLS transport details are documented. [6] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No NIST SP 800-82 / IEC 62443 / ISO 27001 compliance report templates are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | The datasheet, reseller listing and industry releases document FCC/CE Class A, UL (IEC-62368), IEC 61850-3 and IEEE 1613 as the product's certifications; no Common Criteria, FIPS 140-3 or national cryptographic certification is documented. [1], [5], [6], [7], [8] |

---

## 4. Notable Strengths

- **Documented firewall-class design (item 1.3):** Lanner documents its industrial OT security platforms as designed for protocol filtering, packet inspection, whitelisting and network traffic monitoring, and describes the LEC-6041 as a rugged firewall, establishing a legitimate industrial-NGFW product category rather than a guard [4][6].
- **OT-environment ruggedness and IEC 61850-3 / IEEE 1613 certification (items 5.4):** The ICS-P570 is certified to IEC 61850-3 and IEEE 1613 with FCC/CE Class A and UL (IEC-62368), covering substation and harsh-environment deployment [1][5].
- **Hardware-level resilience features (item 4.4):** The datasheet documents one pair of LAN bypass ports, a software-programmable watchdog timer, dual DC power input and -40 to 70 C operation, indicating availability-oriented failure handling [1][2].
- **Platform-level security functions (items 2.3, 2.6, 3.2, 5.2):** Lanner's brochure lists Antivirus/Malware scanning and DLP/SIEM among its IIoT network security gateway capabilities and targets Industrial UTM/Firewall/DPI for ICS/SCADA, indicating the intended security workload [6].

## 5. Notable Gaps / Risks

- **No documented default-deny policy engine (item 1.3):** Whitelisting is claimed only as a design capability of the platform family; no explicit default-deny enforcement, firewall rule engine or policy mechanism is documented for the ICS-P570 - resolution requires the vendor's (or a partner's) firewall software documentation.
- **No inspection performance figures (items 4.1, 4.2):** No processing throughput or latency values are documented anywhere; the datasheet only specifies Ethernet link speeds (up to 2.5 Gbps RJ45 / 1 Gbps SFP), which is not inspection throughput [1].
- **No HA failover design (item 4.3):** Only dual DC power input is documented; there is no active-standby failover or session-preserving switchover for the ICS-P570.
- **No management-plane evidence (items 5.1, 5.2, 5.3):** RBAC role separation, SIEM log transport (CEF/Syslog over TLS) and compliance-report templates are not documented; DLP/SIEM appears only as a marketing capability list [6].
- **No Common Criteria / FIPS certification (item 5.4):** The documented certification set is IEC 61850-3, IEEE 1613, UL and FCC/CE only; no Common Criteria, FIPS 140-3 or national cryptographic certification exists for this product [1][5].

## 6. Evidence Quality Notes

The assessment rests on 9 staged sources: the official ICS-P570 datasheet (Arrow static mirror of the Lanner PDF) [1], Lanner's IEC brochure [6], three marugged.com product-page mirrors [2][3][4], a Westward Sales reseller listing [5], and three industry/press items (Enlit Asia, Automation.com, PRWeb) [7][8][9]. Only items 1.3, 4.4 and 5.4 are now triangulated across multiple sources (the guard/CDS items previously listed here are now unknown with no cited evidence), but no item reaches high confidence: the reseller and press pages largely republish vendor-originated copy, so confidence is capped at medium for all non-unknown verdicts even where the validator would permit higher. Items 2.3, 2.6, 3.2 and 5.2 rest on the single vendor brochure [6], which lists capabilities (Antivirus/Malware, DLP/SIEM, protocol filtering) without implementation detail; they are therefore Partial rather than Supported.

The vendor's official site (lannerinc.com) is Cloudflare-protected and web.archive.org returned HTTP 429 throughout the run, so the live product page could not be staged; marugged.com hosts a full mirror of it (Overview, Use Case, Specifications, Order Information), and the Arrow-hosted datasheet is the official PDF. The 17 unknown items reflect genuine absence of documentation for this hardware platform - no throughput, latency, HA, RBAC, SIEM-log, compliance-report or file-inspection content exists in any staged source - rather than evaluated-and-failed claims. The main source contradiction is terminological: marugged's ICS-P570 page says "ICS-P371 is compliant with IEC 61850-3" inside the ICS-P570 description (a copy error repeated from the sibling page); the datasheet and both the ICS-P570 and ICS-P371 spec tables confirm both models carry IEC 61850-3/IEEE 1613, so the verdicts are unaffected.

---

## Bibliography

[1] Lanner Electronics Inc.. "ICS-P570 IEC 61850-3 Wide Temperature Industrial Cybersecurity Gateway - Datasheet (V.1-2023.2,16)". https://static6.arrow.com/aropdfconversion/ce30c77af7518d703d2bd68989ac9961db80e992/ics-p570_dm.pdf (Retrieved: 2026-08-11T09:04:59Z)
[2] marugged.com (Mid-Atlantic Rugged Systems). "ICS-P570 - IEC 61850-3 Wide Temperature Industrial Cybersecurity Gateway (product page mirror)". https://marugged.com/ics-p570/ (Retrieved: 2026-08-11T08:58:44Z)
[3] marugged.com (Mid-Atlantic Rugged Systems). "ICS-P371 - Industrial Cyber Security Gateway (product page mirror)". https://marugged.com/ics-p371/ (Retrieved: 2026-08-11T09:08:05Z)
[4] marugged.com (Mid-Atlantic Rugged Systems). "LEC-6041 - Wide Temperature ICS Cyber Security Gateway / Rugged Firewall (product page mirror)". https://marugged.com/lec-6041/ (Retrieved: 2026-08-11T09:08:05Z)
[5] Westward Sales. "Lanner ICS-P570 Industrial Security Appliance Powered by AMD Ryzen Processor (reseller listing)". https://westwardsales.com/lanner-ics-p570-cyber-security-gateway (Retrieved: 2026-08-11T08:56:08Z)
[6] Lanner Electronics Inc.. "Industrial Edge - Rugged Edge Computing and OT Security Appliances for Critical Infrastructure (brochure Vol 25.1)". https://cdn.asp.events/CLIENT_CL_EE_E92EC48A_9F42_8E1E_7106D5CAFEEF513B/sites/enlit-europe-2025/media/libraries/exhibitor-brochures/66745-iec-brochure.pdf (Retrieved: 2026-08-11T09:15:17Z)
[7] Enlit Asia. "Lanner to Showcase IEC 61850-3 Certified Substation Computers at Enlit Europe 2025 (exhibitor press release)". https://www.enlit-asia.com/exhibitor-press-releases/lanner-to-showcase-iec-61850-3-certified-substation-computers-at-enlit-europe-2025 (Retrieved: 2026-08-11T09:19:25Z)
[8] Automation.com / ISA. "Lanner Unveils IEC 61850-3 Certified Industrial Computer ICS-P770 Powered by Intel Xeon 6 Processor (industry news)". https://www.automation.com/article/lanner-industrial-computer-ics-intel-xeon (Retrieved: 2026-08-11T09:19:34Z)
[9] PRWeb / PR Newswire. "Lanner Unveils IEC 61850-Certified AI-Enabled Rugged Computer and Industrial Switch at DISTRIBUTECH 2026 (press release)". https://www.prweb.com/releases/lanner-unveils-iec-61850-certified-ai-enabled-rugged-computer-and-industrial-switch-at-distributech-2026-302674756.html (Retrieved: 2026-08-11T09:19:43Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 11
- **Sources reviewed:** 9 (kept: 9, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** article: 1, brochure: 1, datasheet: 1, documentation: 4, press_release: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
