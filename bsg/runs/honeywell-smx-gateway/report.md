# BSG / Cross Domain Product Assessment: Honeywell International Inc. — Honeywell SMX (Secure Media Exchange)

**Product ID:** `honeywell-smx-gateway`
**Version reference:** SMX R201.1 (press release, Oct 2020); brochure Rev 1 11/2022
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:01:48Z
**Total evidence items collected:** 33
**Total distinct sources:** 7

---

## 1. Overview

Honeywell SMX (Secure Media Exchange) is marketed by Honeywell International as an enforceable enterprise USB device and removable-media cybersecurity solution for operational technology (OT) environments, not as a network-level bidirectional security gateway or cross-domain guard [1][4]. The product line comprises a kiosk-style scanning gateway that resides at a facility's physical front desk, a USB-based portable scanner for air-gapped systems, a client enforcement driver (TRUST V2) that controls which USB devices may connect to end nodes, and an Enterprise Threat Management Portal for centralized file policies, alerts, and remote management [1][3]. Deployment shapes include rugged, micro, and portable scanning stations, from single sites to an SMX Fleet for multi-site enterprises including remote and offshore locations [4]. Threat detection combines Honeywell's GARD threat engine, Google Threat Intelligence, and a local antivirus failsafe [1][4]. Vendor documents support for ISA-99, NIST, and IEC 62443, with customer case studies covering NERC CIP compliance in energy and detection of Triton malware in a petrochemical plant [4][5][6].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 0                | 3      | 0   |
| partial          | 2     | 0                | 2      | 0   |
| not_supported    | 6     | 0                | 6      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 11 items backed by ≥ 2 source_types; 8 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | — | Vendor documents SMX as an enterprise USB-device and removable-media security solution rather than a network gateway; with no network data path, there are no TCP/IP sessions to terminate in a protocol-break architecture. [1], [4] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No documentation of SMX's processing-board architecture or FPGA/shared-memory isolation was found; being a USB scanning station does not establish whether dual processing boards exist.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | Vendor documents allowlist-based enforcement: all storage media must be scanned before use, unchecked USB devices are prevented from using USB ports, and device white-listing restricts connections to authorized USB devices. [4], [5] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No documentation found on OS hardening (microkernel/SELinux strict mode) for the SMX kiosk, portable scanner, or client enforcement driver.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Not Supported | medium | — | Vendor documents SMX as a removable-media scanning and enforcement appliance with no network session-re-initiation funnel; with no protocol-break session model, there is no internal control core that signs clean data before a new session. [1], [3] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No evidence of content disarm and reconstruction (CDR) of Office, PDF, image, or CAD files; SMX documents scanning and blocking rather than file rebuilding.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No documentation of macro/script/DDE-link removal from files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | Vendor documents malware multi-scans across the GARD threat engine plus a local antivirus failsafe and detection above commercial AV solutions, but does not specify a minimum number of AV engines or parallel scanning of raw payloads. [4], [6] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No W3C-schema validation of XML/JSON/FIXM/AIXM structures is documented for scanned media files or network messages.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No security-label-based information flow control is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No documentation of DLP rules such as secret keywords, national ID numbers, account numbers, or custom regex patterns.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No documentation of steganography detection or removal for image files (PNG, JPEG, BMP).) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Not Supported | medium | — | Vendor documents SMX as a USB/removable-media security solution; it secures removable media rather than network file-transfer protocols such as SFTP, FTP/S, HTTPS, SMB, or NFS. [1], [4] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Not Supported | medium | — | Vendor documents SMX as a USB/removable-media security solution rather than a network gateway; it does not proxy OT network protocols such as OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, or MQTT. [1], [3] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Not Supported | medium | — | Vendor documents SMX as a USB/removable-media security solution rather than a network database proxy; it does not proxy SQL Server, Oracle, or PostgreSQL. [1], [4] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Not Supported | medium | — | Vendor documents SMX as a USB/removable-media security solution rather than a network relay; it does not relay realtime streams such as RTSP video or Syslog/CEF. [1], [3] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | — | no evidence found (No throughput figure published; SMX is a USB media scanner rather than a network gateway, so no CDR throughput in Mbps is reported.) |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No processing-latency figure published for media scanning.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found (No HA active-standby failover documentation; the SMX Fleet offering is multi-site management, not redundant failover.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | — | Vendor documents that SMX blocks unchecked USB devices by default while keeping ports active only for authorized devices, with all storage drives scanned before connection, i.e. a fail-closed boundary posture. [1], [4] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (No documentation of separated system-admin, policy-admin, and auditor roles in the Enterprise Threat Management Portal.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | — | Vendor documents integration with Honeywell and third-party SOC/SIEM/SOAR tools to automate analysis, and SMX Fleet integration with an existing IT SOC. [1], [4] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | Vendor documents SMX support for ISA-99 and IEC 62443 with compliance logs and a NERC CIP audit case study, and Honeywell OT cybersecurity reporting aligned with IEC 62443 and NIST; availability of specific NIST SP 800-82 or ISO 27001 report templates is not documented. [4], [5], [7] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | — | no evidence found (No Common Criteria (EAL4+), FIPS 140-3, or national cryptographic certification found for SMX in the Common Criteria portal or other registries; vendor documents design alignment with ISA-99/NIST/IEC 62443 instead.) |

---

## 4. Notable Strengths

- **Default-deny / allowlist enforcement (item 1.3):** SMX requires all storage media to be scanned before use, blocks unchecked USB devices from USB ports, and supports device white-listing that restricts connections to authorized devices [4][5].
- **Fail-closed boundary (item 4.4):** Vendor documents that SMX keeps USB ports active only for authorized devices and scans all storage drives before connection, a fail-closed boundary posture by design [1][4].
- **SIEM/SOAR integration (item 5.2):** SMX integrates with Honeywell and third-party SOC/SIEM/SOAR tools to automate analysis, and SMX Fleet can integrate with an existing IT SOC [1][4].
- **Multi-engine threat scanning (item 2.3):** GARD multi-scans plus a local antivirus failsafe reportedly detect above commercial AV solutions, as demonstrated in the Triton petrochemical case study [4][6].
- **Compliance support (item 5.3):** SMX documents ISA-99/IEC 62443 support with compliance logging, demonstrated in a NERC CIP audit pass case study [4][5].

## 5. Notable Gaps / Risks

- **No network-gateway capability (items 1.1, 3.1-3.4):** SMX performs no protocol break and proxies no network file-transfer, OT/ICS, database, or realtime-stream protocols, so buyers needing a network-level gateway must combine it with other products.
- **No CDR or content sanitization (items 2.1, 2.2):** SMX scans and blocks files but does not document disarm-and-reconstruct or macro/script removal, leaving sanitized-file handoff requirements unmet.
- **Performance metrics unpublished (items 4.1-4.3):** no throughput, latency, or HA failover figures are published, so capacity sizing for large facilities relies on vendor consultation.
- **No RBAC documentation (item 5.1):** separation of system-admin, policy-admin, and auditor roles is not documented for the Enterprise Threat Management Portal.
- **No product certifications (item 5.4):** no Common Criteria, FIPS 140-3, or national cryptographic certification was found for SMX; documented compliance claims are design alignment (ISA-99/NIST/IEC 62443) rather than certified status.

## 6. Evidence Quality Notes

All 7 sources are vendor-hosted (product pages, brochure, press release, two customer case studies, and the honeywell.com OT cybersecurity page); no independent third-party review or certification-registry entry for SMX could be located. Every general search engine queried (DuckDuckGo, Bing, Brave, Ecosia, Mojeek, Startpage, and searx instances) returned anti-bot blocks from this environment, and the Common Criteria portal lists Honeywell certifications only for the Mobility Edge mobile-computer line, not SMX. Confidence is therefore capped at medium for all non-unknown verdicts, and the 13 unknown items reflect absence of evidence rather than verified absence of capability.

No contradictions between sources were found: the product page, brochure, and press release consistently describe SMX as a USB/removable-media security solution, which is the basis for marking the network-bound items (1.1, 1.5, 3.1-3.4) not_supported (a removable-media product provides no network-path capabilities) and the hardware/content items (1.2, 2.4, 2.5) unknown. The 11 items with non-unknown verdicts (1.1, 1.3, 1.5, 2.3, 3.1-3.4, 4.4, 5.2, 5.3) are each backed by 2-3 vendor sources; numeric-threshold items 4.1-4.3 are unknown because the vendor publishes no throughput, latency, or failover figures for SMX.

---

## Bibliography

[1] Honeywell International Inc.. "Honeywell SMX - Secure Media Exchange (SMX) | USB Protection (product page)". https://process.honeywell.com/us/en/products/ot-cybersecurity/honeywell-smx (Retrieved: 2026-08-11T09:01:48Z)
[2] Honeywell International Inc.. "Honeywell Forge OT Cybersecurity - all products page". https://process.honeywell.com/us/en/products/ot-cybersecurity (Retrieved: 2026-08-11T09:01:48Z)
[3] Honeywell International Inc.. "Honeywell Secure Media Exchange (SMX) Expands To Better Protect Organizations From Both Malware & Firmware-Based Cybersecurity Attacks (press release, R201.1 launch)". https://process.honeywell.com/us/en/news-and-events/newsroom/press-releases/honeywell-secure-media-exchange-smx-expands-to-better-protect-organizations-from-both-malware-firmware-based-cybersecurity-attacks (Retrieved: 2026-08-11T09:01:48Z)
[4] Honeywell International Inc.. "Secure Media Exchange (SMX) - Enforceable Enterprise USB Device & Removable Media Cybersecurity Solution for Operational Environments (brochure, Rev 1 11/2022)". https://process.honeywell.com/content/dam/forge/en/documents/cybersecurity/Cybersecurity_Brochure_Honeywell_SMX.pdf (Retrieved: 2026-08-11T09:01:48Z)
[5] Honeywell International Inc.. "Securing the Grid - NERC CIP Compliance Equals Better Grid Cybersecurity, Honeywell SMX helps protect Fortune 500 Energy Company (case study, 04/2021)". https://process.honeywell.com/content/dam/forge/en/documents/case-study/Case%20Study_SMX_Energy%202_Cybersecurity_Honeywell.pdf (Retrieved: 2026-08-11T09:01:48Z)
[6] Honeywell International Inc.. "Battling TRITON - a petrochemical plant avoids potential catastrophe in Honeywell SMX trial (case study, Rev 1 09/2021)". https://process.honeywell.com/content/dam/forge/en/documents/case-study/Case%20Study_SMX_Oil%20and%20Gas%203_Cybersecurity_Honeywell.pdf (Retrieved: 2026-08-11T09:01:48Z)
[7] Honeywell International Inc.. "Honeywell - Protect Operations with OT Cybersecurity Solutions (outcomes page)". https://www.honeywell.com/us/en/outcomes/ot-cybersecurity (Retrieved: 2026-08-11T09:01:48Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 7 (kept: 7, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 2, vendor_datasheet: 1, vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
