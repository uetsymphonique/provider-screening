# BSG / Cross Domain Product Assessment: Thales Group — Thales High-Assurance Gateway (X-Arc Cross Domain Solutions, Thales Norway)

**Product ID:** `thales-high-assurance-gateway`
**Version reference:** TSF 401 SW 1.0.0 (SERTIT-127), TSF 201 (SERTIT-130 C), TNOR Guard v1.1.3 (SERTIT-120 C)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:40:00Z
**Total evidence items collected:** 54
**Total distinct sources:** 12

---

## 1. Overview

The provider-list name "Thales High-Assurance Gateway" does not appear verbatim in any public source located during this pass; the real, publicly documented bidirectional Cross Domain Solution family sold by the Thales Group is X-Arc, developed and marketed by Thales Norway AS, which is the subject of this assessment [1], [12]. Thales Norway positions X-Arc explicitly as a Cross Domain Solution, not a firewall: hardware and software products that enable robust, secure bidirectional data transfer between security domains [1], [4]. The family spans the TSF 201/TSF 401 Trusted Security Filters (hardware filtering gateways interconnecting IP networks at different classification levels, with optional diode mode), the X-Arc Guard / TNOR Guard (two-way messaging and content guard covering MMHS, SMTP, XMPP and XML/SOAP), the X-Arc Gateway (combined solution for software-update, alarm and document transfer), the X-Arc Labeler (security labelling, incl. STANAG 4774/4778) and X-Mon (cross domain monitoring) [1], [4], [11]. Deployment shapes documented include data centre operation (TSF 401), tactical vehicles and vessels (TSF 201), and classified/unclassified or air-gapped interconnects (X-Arc Gateway) [2], [3]. TSF 401 is Common Criteria EAL5+ certified (SERTIT-127) and TEMPEST SDIP-27 Level A approved [5], [6].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 7     | 3                | 4      | 0   |
| partial          | 13    | 0                | 10     | 3   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 4     | 0                | 0      | 4   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 14 items backed by ≥ 2 source_types; 7 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | — | SERTIT certification reports describe the X-Arc architecture as a Cross Domain Solution with two separate, independent Red/Black channels; the TNOR Guard acts as a proxy that converts messages to a protocol-independent format and provides no routing between domains. [6], [7], [11] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | — | SERTIT documents the TNOR Guard as software on three separate hardware instances and the TSF 401 filter enforcer as implemented in FPGA with hardware-enforced filtering, but a specific dual-board/FPGA-interconnect topology is not described. [6], [11] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | — | SERTIT and vendor sources document default-deny behavior: the TSF 401 filter defaults to blocking all traffic in both directions until a signed filter is installed, the TSF 201 transfers only rule-compliant datagrams and discards the rest, and the TNOR Guard releases nothing unless policy explicitly allows it. [3], [6], [11] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | — | SERTIT documents the TNOR Guard running on a PikeOS separation-kernel hypervisor with partition isolation, and the TSF 401 with secure boot and self-tests of security-critical functions. [6], [11] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Partial | medium | — | SERTIT documents the TNOR Guard using hardware security modules when signing released information objects and validating digital signatures, and the X-Arc Labeler attaching security labels; the specific internal-stamping-before-session-reinitiation mechanism is not described. [4], [11] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | — | The X-Arc Guard transfers complex data (documents, XML, e-mail, chat) with content checking and automated release decisions, but format-level disarm-and-reconstruct CDR for Office/PDF/Image/CAD is not documented. [1], [4], [11] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No source discusses macro/script removal from files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | low | — | SERTIT notes the TNOR Guard uses external content checker services as part of its release decision, but no antivirus engines or engine count are documented. [11] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | — | The TSF 401 datasheet documents inspection of structured data such as XML, JSON, MQTT and Protobuf and SERTIT documents inspection of protocol parameters and message content; W3C schema conformance for FIXM/AIXM is not explicitly claimed. [2], [6] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Supported | high | — | The X-Arc Guard enforces sharing policy based on security markings of transferred objects, the X-Arc Labeler attaches security labels (incl. STANAG 4774/4778 confidentiality labels per the suite brochure), and SERTIT documents MAC/ABAC on the TNOR Guard. [4], [11] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | low | — | SERTIT documents message-content inspection and content checking as part of the release decision; keyword/pattern DLP (secrets, ID numbers, custom regex) is not specifically described. [6], [11] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No source mentions steganography detection.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | The X-Arc Gateway is documented as a complete solution for transferring software/antivirus updates, alarms and documents/files between domains, and the Guard supports mail, chat, web services and file transfer; specific SFTP/FTP/S/HTTPS/SMB/NFS proxy modes with content cleaning are not enumerated. [1], [4] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The TSF 401 datasheet documents inspection of MQTT among structured protocols; OPC UA, Modbus TCP, IEC 60870-5-104 and DNP3 are not mentioned. [2] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No source documents database proxy support.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | low | — | The TSF 401 datasheet documents IP/TCP/UDP unicast and multicast filtering and Syslog/HTTP remote monitoring; an RTSP video proxy or CEF relay is not documented. [2] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 10000 Mbps | Vendor datasheet and Security Target document the TSF 401 at up to 10 Gb/s per filter channel (full-duplex) and up to 20 Gb/s aggregate with a second channel. [2], [7] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.05 ms | The TSF 401 datasheet documents ~50 µs filter latency and the product page describes low-latency interconnection of security domains. [1], [2] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | SERTIT documents active failover to a redundant interface when the main link fails and the datasheet lists configurable interface redundancy and optional dual power supply, but no switchover-time figure is published. [2], [6] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | The Security Target requires preservation of a secure state on failures (self-test failure, tampering, power loss) and the certification report documents a default all-blocked filter state; explicit fail-close behavior specifically under DoS attack is not described. [6], [7] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | The Security Target documents role-based access control with three operator roles (Operator, Network Operator, Security Operator) and role/password authentication; the specific System Admin / Policy Admin / Security Auditor role split is not documented. [2], [7] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | The TSF 401 datasheet documents centralized management and log collection with Syslog/HTTP remote monitoring and SNMP support, and the Security Target requires a TLS secure channel to the management server; TLS-encrypted syslog/CEF export to a SIEM is not explicitly documented. [2], [7] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No source mentions NIST SP 800-82 / IEC 62443 / ISO 27001 compliance report templates.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | — | SERTIT (Norwegian CC scheme) certifies TSF 401 at EAL5 + ALC_FLR.3 (SERTIT-127), TSF 201 at EAL5 (SERTIT-130 C) and TNOR Guard at EAL4 + ALC_FLR.3 + AVA_VAN.4 (SERTIT-120 C), all with CCRA/SOG-IS mutual recognition; TSF 401 is TEMPEST approved per SDIP-27 Level A and the suite brochure claims CC EAL5+/EAL4+ certification for the Guard. [4], [5], [6], [8], [10] |

---

## 4. Notable Strengths

- **Common Criteria EAL5+ certification across the product line (item 5.4):** TSF 401 (EAL5 + ALC_FLR.3, SERTIT-127), TSF 201 (EAL5, SERTIT-130 C) and TNOR Guard (EAL4 + ALC_FLR.3 + AVA_VAN.4, SERTIT-120 C) are certified under the Norwegian scheme with CCRA/SOG-IS mutual recognition, and TSF 401 is TEMPEST SDIP-27 Level A approved [5], [6], [8], [10].
- **Default-deny and fail-closed posture (items 1.3, 4.4):** the TSF 401 filter defaults to blocking all traffic in both directions until a signed filter definition file is installed, and the Security Target requires preservation of a secure state on self-test failure, tampering or power loss [6], [7].
- **High-assurance separation architecture (items 1.1, 1.2, 1.4):** independent Red/Black channels with an FPGA-implemented filter enforcer, three separate hardware units for the Guard, and a PikeOS separation-kernel hypervisor with partition isolation [6], [11].
- **Policy-driven release with security labels (item 2.5):** the Guard enforces sharing policy based on the security marking of transferred objects, the Labeler attaches STANAG 4774/4778 confidentiality labels, and SERTIT documents MAC/ABAC on the Guard [4], [11].
- **Throughput and latency (items 4.1, 4.2):** up to 10 Gb/s per filter channel (20 Gb/s aggregate with the second channel) at ~50 µs filter latency per the TSF 401 datasheet and Security Target [2], [7].

## 5. Notable Gaps / Risks

- **Content disarm & reconstruction (item 2.1):** content checking and policy-based release are documented, but format-level CDR for Office/PDF/Image/CAD is not; buyers needing deep file sanitisation must verify Guard format handling directly with Thales.
- **Multi-engine antivirus (item 2.3):** only external "content checker services" are referenced in the TNOR Guard certification report; no antivirus engines or engine counts are documented.
- **HA switchover time (item 4.3):** active interface failover and dual power supply are documented, but no switchover-time figure (requirement is ≤ 100 ms) is published.
- **Protocol coverage (items 3.1, 3.2, 3.3, 3.4):** only MQTT is documented among the listed OT/ICS protocols; database proxies, RTSP video proxy and specific file-transfer protocol proxies (SFTP/FTP/S/HTTPS/SMB/NFS) are not documented.
- **Product-name mismatch risk (all items):** the provider-list name "Thales High-Assurance Gateway" appears in no public source; this assessment anchors to the X-Arc family, and the buyer should confirm the exact product, model and version (e.g. TSF 401 SW 1.0.0) in procurement.

## 6. Evidence Quality Notes

Evidence is grounded in 12 staged sources: 3 vendor web pages, 3 vendor datasheets/brochure, and 6 SERTIT (Norwegian Common Criteria scheme) certification pages, certification reports and a Security Target. The certification_registry material is independent of the vendor and corroborates the vendor claims on architecture, filtering behavior, failover and certification. 14 of 24 items are backed by ≥ 2 distinct source_types; the 4 unknown items (2.2 macro/script removal, 2.7 anti-steganography, 3.3 database proxy, 5.3 compliance report templates) have no mention in any staged source and were not inferred from silence. 7 items rest on vendor documentation only (3.1, 3.2, 3.4, 4.1, 4.2, 5.1, 5.2), so their confidence is capped at medium per the validator rule; 4.1 and 4.2 in particular rely on vendor-published performance figures. No staged source contradicted another; where vendor claims lacked independent corroboration (RBAC role naming in 5.1, fail-close specifically under DoS in 4.4, format-level CDR in 2.1), the verdict was kept at partial rather than supported. The NATO NIAPC product page confirming TSF 401 (EAL5+, TEMPEST SDIP-27 Level A) is Cloudflare-blocked from this environment and could not be staged, so it is not cited; SERTIT documentation covers the same facts.

---

## Bibliography

[1] Thales Norway AS. "X-Arc Cross Domain Solutions - product page (Thales Norway)". https://digitaltmesseverktoy.thales.no/products/x-arc (Retrieved: 2026-08-11T09:28:00Z)
[2] Thales Norway AS. "X-Arc TSF 401 - Trusted Security Filter, product sheet". https://framerusercontent.com/assets/nbN4Httszdmbzo3nt5G91wcqkRY.pdf (Retrieved: 2026-08-11T09:25:19Z)
[3] Thales Norway AS. "X-Arc TSF 201 - Trusted Security Filter, datasheet". https://framerusercontent.com/assets/hrR0DmY2edcPTZ5rEdZlj8mDmA.pdf (Retrieved: 2026-08-11T09:25:20Z)
[4] Thales Norway AS. "X-Arc Cross Domain Solutions - product suite brochure (2023-08)". https://framerusercontent.com/assets/tDwHisurLaFVzIzgH7gVCKoQcc.pdf (Retrieved: 2026-08-11T09:25:20Z)
[5] SERTIT - Norwegian Certification Authority for IT Security. "Trusted Security Filter (TSF) 401 - SERTIT certified product page (SERTIT-127)". https://sertit.no/certified-products/trusted-security-filter-tsf-401-article3632-1919.html (Retrieved: 2026-08-11T09:26:08Z)
[6] SERTIT - Norwegian Certification Authority for IT Security. "SERTIT-127 Certification Report - TSF 401 SW 1.0.0 (EAL5, ALC_FLR.3)". https://sertit.no/getfile.php/1314822-1765895275/SERTIT/Sertifikater/2025/127/SERTIT-127%20Certification%20Report.pdf (Retrieved: 2026-08-11T09:26:09Z)
[7] Thales Norway AS. "TSF 401 Security Target Lite, Rev 001 (ST for SERTIT-127)". https://sertit.no/getfile.php/1314825-1765895276/SERTIT/Sertifikater/2025/127/3AQ%2033330%20AAAB%20938%20Security%20Target%20Lite%20TSF%20401%20Ed.%20001.pdf (Retrieved: 2026-08-11T09:28:12Z)
[8] SERTIT - Norwegian Certification Authority for IT Security. "Trusted Security Filter (TSF) 201 - SERTIT certified product page (SERTIT-130 C)". https://sertit.no/certified-products/trusted-security-filter-tsf-201-article3652-1919.html (Retrieved: 2026-08-11T09:26:55Z)
[9] SERTIT - Norwegian Certification Authority for IT Security. "SERTIT-130 Certification Report - TSF 201 (EAL5, ALC_FLR.3)". https://sertit.no/getfile.php/1314979-1770728549/SERTIT/Sertifikater/2026/130/SERTIT-130%20Certification%20Report.pdf (Retrieved: 2026-08-11T09:28:17Z)
[10] SERTIT - Norwegian Certification Authority for IT Security. "TNOR Guard - SERTIT certified product page (SERTIT-120 C)". https://sertit.no/certified-products/tnor-guard-article2842-1919.html (Retrieved: 2026-08-11T09:26:53Z)
[11] SERTIT - Norwegian Certification Authority for IT Security. "SERTIT-120 Certification Report - TNOR Guard v1.1.3 (EAL4, ALC_FLR.3, AVA_VAN.4)". https://sertit.no/getfile.php/1310627-1654589561/SERTIT/Sertifikater/2022/120/SERTIT-120%20CR%20v1.0.pdf (Retrieved: 2026-08-11T09:26:56Z)
[12] Thales Norway AS. "X-Arc - Thales Norway product document portal page". https://products.thales.no/documents/x-arc (Retrieved: 2026-08-11T09:28:01Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 12 (kept: 12, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 6, vendor_datasheet: 3, vendor_doc: 3
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
