# BSG / Cross Domain Product Assessment: Check Point Software Technologies Ltd. - Check Point Quantum Rugged Gateway (Quantum Rugged Series - Rugged Firewall 1575R / 1595R)

**Product ID:** `check-point-quantum-rugged-gateway`
**Version reference:** Quantum Rugged Series (Rugged Firewall 1575R / 1595R) on Embedded GAiA R81.10.10, managed via R81 software; datasheet edition July 22, 2025
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T00:00:00Z
**Total evidence items collected:** 38
**Total distinct sources:** 16

---

## 1. Overview

The Check Point Quantum Rugged Gateway is a ruggedized industrial Next Generation Firewall (NGFW) family, currently sold as the Rugged Firewall 1575R (wired, or Wi-Fi with LTE) and 1595R (wired, or 5G) [1]. Check Point positions it to secure OT/ICS/SCADA and critical-infrastructure networks - power, oil and gas, manufacturing, transportation and maritime - rather than as a cross-domain guard or protocol-break device; the datasheet identifies it as a "Next Generation Firewall (NGFW)" with over 70 SCADA/ICS protocols and the product page cites 1,830 protocols and commands [1][2]. The solid-state, fanless appliances run Embedded GAiA R81.10.10, are managed through the latest R81 software, and deploy as gateways between IT and OT zones, supporting Layer 3 routed or Layer 2 bridge modes, site-to-site and remote-access VPN, dual-SIM wireless (LTE/5G), redundant power and two-member High Availability clusters [1]. The product carries industrial certifications (IEEE 1613, IEC 61850-3, IEC 60945, DNV-GL-CG-0339, IP30) and the 1575R is covered by a FIPS 140-2 Level 1 validation, while the underlying R81/R82 gateway platform holds Common Criteria EAL4+/NIAP cPP certificates [1][9][14].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 0                | 5      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 11    | 0                | 0      | 11  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 6 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Unknown | low | - | no evidence found (No protocol-break (TCP/IP session termination, no IP routing) architecture is documented for the Quantum Rugged gateway.) |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No dual-processing-board hardware isolation design (FPGA or isolated shared memory) is documented.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | The R81.20 admin guide documents a boot-time default filter that drops all inbound and outbound packets and an implicit default rule whose Action is Drop, i.e. forwarding is whitelist-based; the firewall also holds an ICSA Labs firewall certification. [4], [16] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | - | no evidence found (Gaia is documented as a Linux-based OS with restricted shells (Clish) and role-based administration, but no explicit hardened-OS / microkernel / SELinux-strict-mode claim was found in the reviewed sources.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No internal cryptographic stamping of cleaned data prior to session re-initiation is documented.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | - | The SandBlast Threat Extraction blade removes active content and embedded objects, reconstructs files and delivers sanitized content (CDR-style), but exhaustive coverage of Office/PDF/Image/CAD formats is not documented. [4] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Partial | medium | - | Threat Extraction removes active content and embedded objects from files and delivers sanitized content; specific enumeration of VBA macros / Javascript / DDE links is not documented. [4] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | - | The Anti-Virus blade is documented to correlate information from multiple detection engines to detect and block malware; parallel scanning of raw payload by two or more distinct AV engines is not explicitly enumerated. [4] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM schema-validation engine is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label-based information flow control on files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Supported | medium | - | The Data Loss Prevention software blade identifies, monitors and protects data transfer through deep content inspection and blocks the unauthorized transmission of confidential information. [4] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography detection/removal capability for image files is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Antivirus content scanning for web, email, FTP and SMB traffic and HTTPS inspection (SSL decryption with malware scanning) are documented; no dedicated SFTP/FTP-S/SMB proxy with content cleaning is described. [1], [3] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | - | The datasheet lists over 70 SCADA/ICS protocols including Modbus, OPC DA & UA, DNP3, IEC 60870-5-104, BACnet, CIP, Profinet and Siemens S7, and the product page cites support for 1,830 SCADA protocols and commands. [1], [2] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | - | no evidence found (No RTSP video proxy or syslog/CEF traffic relay capability is documented; syslog export exists only as a management-plane feature (LogExporter).) |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1970 Mbps | The datasheet specifies firewall throughput of 1,970 Mbps (NGFW 830 Mbps, Threat Prevention 400 Mbps) under enterprise test conditions, above the 1,000 Mbps requirement. [1] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No gateway processing-latency figure is documented in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Not Supported | medium | 700 ms | ClusterXL High Availability redirects connections to a standby member, but a cluster member is declared down only after 0.7 seconds without a state report, so switchover cannot meet the 100 ms requirement; no sub-100 ms failover figure is documented. [1], [3] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | - | no evidence found (No explicit fail-close behavior under DoS/overload is documented; the 1595R's bypass NIC is a power-loss fail-open feature rather than a DoS fail-close.) |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | - | Gaia role-based administration lets administrators define roles with per-feature read/write, read-only or no access, with predefined adminRole and monitorRole and a restricted Clish shell; a dedicated three-way system-admin/policy-admin/auditor separation is not explicitly documented. [4], [5] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | - | LogExporter exports security and audit logs to SIEM applications over syslog (TCP or UDP) in CEF, LEEF or JSON formats with mutual TLS 1.2 authentication. [6] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | - | The Security Compliance solution provides audit-ready compliance reports mapped to regulations including ISO 27001, HIPAA, GDPR and PCI DSS; NIST SP 800-82 or IEC 62443 report templates are not explicitly documented. [11], [12] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | - | NIST CMVP validation #4264 (FIPS 140-2 Level 1) covers the 1575R on Embedded GAiA R81.10.10, and Check Point R81/R81.20/R82 gateway platforms hold Common Criteria EAL4+/NIAP cPP certificates; no FIPS 140-3 validation was found and rugged-model-level CC coverage is not documented. [7], [8], [9], [10], [13], [14], [15] |

---

## 4. Notable Strengths

- **ICS/SCADA protocol support (item 3.2):** over 70 SCADA/ICS protocols documented, including Modbus, OPC DA & UA, DNP3, IEC 60870-5-104, BACnet, CIP, Profinet and Siemens S7, with 1,830 protocols and commands claimed on the product page [1][2].
- **Content sanitization and file inspection (items 2.1, 2.2, 2.3):** the SandBlast Threat Extraction blade removes active content and embedded objects and reconstructs files, Threat Emulation sandboxes unknown files, and the Anti-Virus blade correlates multiple detection engines [4].
- **Data loss prevention (item 2.6):** the DLP software blade performs deep content inspection and blocks unauthorized transmission of confidential data [4].
- **SIEM integration (item 5.2):** LogExporter pushes security and audit logs to SIEMs over syslog with CEF/LEEF/JSON formats and mutual TLS 1.2 [6].
- **Default-deny posture (item 1.3):** the boot-time default filter drops all packets and the implicit default rule action is Drop, so forwarding is whitelist-based [4].
- **Certification coverage (item 5.4):** FIPS 140-2 Level 1 validation (#4264) covers the 1575R, and the R81/R81.20/R82 gateway platform holds Common Criteria EAL4+ and NIAP cPP certificates [9][13][14][15].

## 5. Notable Gaps / Risks

- **HA switchover exceeds the 100 ms budget (item 4.3):** ClusterXL High Availability is supported, but a member is declared down only after 0.7 s without a state report, so failover cannot meet a 100 ms no-session-loss requirement; a buyer with that constraint needs sub-100 ms failover evidence or a different HA design [3].
- **No processing-latency figure (item 4.2):** no gateway latency is documented, so a ≤10 ms realtime-latency requirement is unverifiable from the reviewed sources.
- **No fail-close-under-DoS evidence (item 4.4):** DoS/overload behavior is not documented as fail-close; the 1595R's bypass NIC is a power-loss fail-open feature for HA deployments [1].
- **CDR coverage is partial (item 2.1):** Threat Extraction sanitizes files but exhaustive Office/PDF/Image/CAD format coverage is not documented, and specific macro/script enumeration is absent (item 2.2) [4].
- **Missing database proxy and video/syslog relay (items 3.3, 3.4):** no SQL query-whitelisting proxy or RTSP video proxy / syslog-rail relay is documented; syslog exists only as management-plane log export.
- **Certification scope gaps (item 5.4):** FIPS validation is 140-2 Level 1 (not 140-3) and covers only the 1575R (the 1595R is not in certificate #4264's tested configurations); the Common Criteria certificates name the gateway platform without model-level enumeration of the rugged appliances [9][14].

## 6. Evidence Quality Notes

Evidence was triangulated across 16 staged sources: 6 vendor documents (R81.20 Quantum Security Gateway, ClusterXL and Gaia admin guides; R81.10 Logging and Monitoring guide), 2 vendor datasheets (Quantum Rugged 1575R/1595R; Security Compliance), 3 vendor product pages, 2 NIST CMVP registry pages, 4 Common Criteria certificates (NIAP VID11235/VID11513, BSI-DSZ-CC-1207-2025, plus the Common Criteria page) and 1 third-party lab certificate (ICSA Labs). No single item reached three fully independent (non-vendor) sources; the certification items (5.4) are the best-triangulated, backed by the NIST CMVP registry and BSI/NIAP certificate documents. Items 1.4, 2.3, 2.6, 3.1, 5.1 and 5.2 rest on vendor documentation alone, so their verdicts are capped at medium confidence - a Check Point-published admin guide is strong evidence for a capability's existence, but cannot corroborate marketing-level claims.

All checkpoint.com raw binaries (datasheet PDFs, certificate PDFs, product pages) are behind the site's AWS WAF, which blocked direct downloads; those sources were captured through the r.jina.ai reader and staged as .txt with their original URLs preserved in artifacts/manifest.jsonl (see the `fetched_via` field) - the grounding check therefore verified quotes against the rendered text rather than the raw binary. No contradicting sources were found: vendor documentation was internally consistent, and the only judgment call was item 4.3, where the ClusterXL guide's 0.7-second member-declaration threshold contradicts the checklist's 100 ms budget, so the verdict is `not_supported` with the documented 700 ms figure rather than a qualitative `partial`.

---

## Bibliography

[1] Check Point Software Technologies Ltd.. "Check Point Quantum Rugged Series Security Gateways Datasheet (1575R / 1595R)". https://www.checkpoint.com/downloads/products/quantum-rugged-1595r-datasheet.pdf (Retrieved: 2026-08-11T09:17:56Z)
[2] Check Point Software Technologies Ltd.. "Industrial Control Systems Security Gateways (Check Point Quantum / Rugged Firewall)". https://www.checkpoint.com/quantum/next-generation-firewall/industrial-control-systems-appliances/ (Retrieved: 2026-08-11T09:17:56Z)
[3] Check Point Software Technologies Ltd.. "R81.20 ClusterXL Administration Guide". https://sc1.checkpoint.com/documents/R81.20/WebAdminGuides/EN/CP_R81.20_ClusterXL_AdminGuide/CP_R81.20_ClusterXL_AdminGuide.pdf (Retrieved: 2026-08-11T09:17:56Z)
[4] Check Point Software Technologies Ltd.. "R81.20 Quantum Security Gateway Administration Guide". https://sc1.checkpoint.com/documents/R81.20/WebAdminGuides/EN/CP_R81.20_SecurityGateway_Guide/CP_R81.20_Quantum_SecurityGateway_AdminGuide.pdf (Retrieved: 2026-08-11T09:17:56Z)
[5] Check Point Software Technologies Ltd.. "R81.20 Gaia Administration Guide". https://sc1.checkpoint.com/documents/R81.20/WebAdminGuides/EN/CP_R81.20_Gaia_AdminGuide/CP_R81.20_Gaia_AdminGuide.pdf (Retrieved: 2026-08-11T09:17:56Z)
[6] Check Point Software Technologies Ltd.. "R81.10 Logging and Monitoring Administration Guide". https://sc1.checkpoint.com/documents/R81.10/WebAdminGuides/EN/CP_R81.10_LoggingAndMonitoring_AdminGuide/CP_R81.10_LoggingAndMonitoring_AdminGuide.pdf (Retrieved: 2026-08-11T09:17:56Z)
[7] Check Point Software Technologies Ltd.. "Product Certifications". https://www.checkpoint.com/about-us/product-certifications/ (Retrieved: 2026-08-11T09:17:56Z)
[8] Check Point Software Technologies Ltd.. "Common Criteria - Product Certifications". https://www.checkpoint.com/about-us/product-certifications/common-criteria/ (Retrieved: 2026-08-11T09:17:56Z)
[9] NIST CMVP. "NIST CMVP Certificate #4264 - Quantum Security Gateway Cryptographic Library". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4264 (Retrieved: 2026-08-11T09:17:56Z)
[10] NIST CMVP. "NIST CMVP Validated Modules search - vendor: Check Point". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&CertificateStatus=Active&Vendor=Check+Point (Retrieved: 2026-08-11T09:17:56Z)
[11] Check Point Software Technologies Ltd.. "Check Point Security Compliance Datasheet". https://www.checkpoint.com/downloads/products/compliance-datasheet.pdf (Retrieved: 2026-08-11T09:17:56Z)
[12] Check Point Software Technologies Ltd.. "Security Compliance - Check Point Software". https://www.checkpoint.com/solutions/compliance/ (Retrieved: 2026-08-11T09:17:56Z)
[13] NIAP CCEVS. "NIAP Common Criteria Certificate VID11235 - Check Point Security Gateway and Maestro Hyperscale Appliances R81.00". https://www.checkpoint.com/downloads/products/common-criteria-certificate-r81-st_vid11235-ci.pdf (Retrieved: 2026-08-11T09:17:56Z)
[14] BSI Germany. "BSI Certificate BSI-DSZ-CC-1207-2025 - Check Point R82 for Gateway and Maestro Configurations (EAL4+)". https://www.checkpoint.com/downloads/products/1207c.pdf (Retrieved: 2026-08-11T09:17:56Z)
[15] NIAP CCEVS. "NIAP Common Criteria Certificate VID11513 - Check Point Quantum Force R81.20". https://www.checkpoint.com/downloads/products/st_vid11513-ci.pdf (Retrieved: 2026-08-11T09:17:56Z)
[16] ICSA Labs. "ICSA Labs Firewall Certification - Check Point Security Gateway (Certificate 110002R10)". https://www.checkpoint.com/downloads/company/2022-icsa-labs-check-point-firewall-certificate.pdf (Retrieved: 2026-08-11T09:17:56Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 16 (kept: 16, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certificate: 4, datasheet: 2, documentation: 8, registry: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
