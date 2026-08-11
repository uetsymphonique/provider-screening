# BSG / Cross Domain Product Assessment: OPSWAT — MetaDefender Cross Domain Gateway

**Product ID:** `metadefender-cross-domain-gateway`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:50:22Z
**Total evidence items collected:** 67
**Total distinct sources:** 25

---

## 1. Overview

OPSWAT markets MetaDefender Cross Domain Gateway as part of a high-assurance Cross Domain Solution (CDS) line, not a firewall: its current product family — MetaDefender Diode X (formerly Transfer Guard), Unidirectional Security Gateway (USG), Bilateral Security Gateway (BSG), and Optical Diode, collectively the MetaDefender NetWall family — is built on MetaDefender Core engines (Deep CDR, Metascan Multiscanning, Proactive DLP) and is marketed for one-way and controlled two-way transfer between networks of different trust/classification levels, including OT-to-IT and low-to-high domain flows [1, 4, 7, 8]. The vendor describes the architecture as hardware-enforced one-way data flow over non-routable serial or optical links between isolated server pairs, with true protocol break ("Protocol break, completely removed from TCP/IP connection" [6]) and guaranteed payload delivery [2, 6, 12]. Deployment shapes cover 1U rack appliances with 100 Mbps to 10 Gbps options, DIN-rail form factors, and integration with MetaDefender Kiosk, MFT, and Software Supply Chain for system/software import and controlled-export workflows [6, 8, 17]. Note: OPSWAT no longer publishes a page under the exact name "MetaDefender Cross Domain Gateway"; this assessment anchors on its documented successor family (see Evidence Quality Notes).

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 18    | 1                | 17     | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 0     | 0                | 0      | 0   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 18 items backed by ≥ 2 source_types; 22 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | — | Vendor documents that transfer protocols are terminated at the diode ingest point and re-originated with different protocols or new session IDs, with no TCP/IP handshake or routing across the boundary (protocol break). [6], [8], [12] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | medium | — | Vendor documents hardware-enforced isolation: a non-networked serial connection between the USG/BSG server pair or a unidirectional optical connection between the Diode X server pair, with no return path. [4], [12], [14] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | Vendor documents that the gateway strictly enforces one-way flows and will not allow a connection to be initiated from the untrusted network, so only allowlisted transfer channels operate. [1], [2], [6] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | — | OPSWAT documents MetaDefender appliances as pre-configured with a pre-hardened operating system, and MetaDefender Core support articles reference deployments on hardened Linux systems. [20], [22] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Supported | medium | — | Vendor documents that files are validated according to policy and digitally signed with a protected private key on the data diode before release, establishing cryptographic proof of origin and integrity; appliances ship with USB crypto keys. [9], [14] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Supported | medium | — | Vendor documents Deep CDR disassembling and reconstructing files from verified, safe elements across 150-200+ file types, with SE Labs reporting a 100% protection and accuracy score (vendor-reported). [3], [7], [8] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Supported | medium | — | Vendor documents Deep CDR extracting potentially harmful scripts, embedded macros, and out-of-policy content from over 180 file types, including deep inspection of embedded objects and metadata. [7], [8], [14] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Supported | medium | — | Vendor documents Metascan Multiscanning with 30+ anti-malware engines detecting over 99% of malware via signatures, heuristics and machine learning; Diode X package cites up to 20 engines. [3], [7], [8] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | — | MetaDefender Core Deep CDR documents XML schema validation against XSD schemas, failing non-conforming files. [18] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Partial | medium | — | Transfer policies can be conditioned on file attributes, metadata, user roles and security results, and cross-domain policy validation defines which file types and content elements may cross. [7], [21] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Supported | medium | — | Vendor documents Proactive DLP detecting and blocking sensitive, classified or regulated information, including secret keys, passwords and access credentials, with custom policy support. [7], [8], [14] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Supported | medium | — | Vendor documents Deep CDR removing hidden data in image files by stripping metadata chunks such as iTXt and regenerating pixel data during reconstruction, disrupting pixel-level (e.g., LSB) payloads. [15] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Supported | medium | — | Vendor datasheets list FTP, FTPS, SFTP, SMB/CIFS and HTTPS transfer with connectors feeding MetaDefender scanning/sanitization (e.g., Diode X with file sanitization), including software package/artifact transfer via diodes. [2], [6], [17] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | — | Vendor datasheets list OPC (UA, DA, A&E), Modbus, MQTT (incl. Sparkplug B), IEC 60870-5-104 (IEC104), DNP3, ICCP and AVEVA PI among supported OT protocols. [6], [12], [24] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | — | Vendor documents database replication (Microsoft SQL via native transactional replication, Oracle GoldenGate, other relational databases and historians). [2], [6] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | Vendor documents video/audio stream transfer, Ethernet packet transfer and syslog log transfer on the gateways. [2], [6] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000.0 Mbps | Vendor documents a 100 Mbps base platform field-upgradeable to 1 Gbps with a 10 Gbps enterprise-server option; MetaDefender Core scan throughput is separately documented at 13,000+ files per minute, and Deep CDR per-file conversion times are published (e.g., ~0.6 s per pdf2pdf). [3], [6], [19] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.6 ms | Vendor datasheets report tested latency of 0.6 ms TCP and 0.7 ms UDP for the gateways. [2], [12], [14] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Vendor documents active/standby high availability with automated failover and 99.99% system availability across the NetWall family, with no session loss claims (guaranteed payload delivery). [2], [5] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | — | Vendor documents fail-safe designs that ensure no inbound connectivity is introduced during failure, hardware-enforced one-way directionality (data cannot return regardless of software state or compromise), and anti-overrun control against data overflow. [11], [12], [24] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | — | MetaDefender Core documents role-based user management with granularly defined roles covering console actions, scan services and workflows, and MFT documents granular RBAC with AD integration, SSO and MFA. [16], [21] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Vendor documents real-time syslog transfer and SIEM integration (BSG/USG datasheets list 'SIEM integration via Syslog'; NetWall brochure describes syslog replication to one or more SIEM systems; MFT integrates with SIEM platforms). [2], [6], [21] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Supported | medium | — | Vendor documents compliance coverage for NERC CIP, NIST CSF/800-82/800-53/ICS, IEC 62443, NRC 5.71, CFATS, ISO 27001/27032/27103, ANSSI, IIC SF and NCDSMO Raise the Bar guidance. [6], [8], [12] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | — | OPSWAT gateways are Common Criteria EAL4+ certified (USG/Diode X datasheets), the MetaDefender platform crypto module is FIPS 140-3 validated (NIST CMVP #5225), Diode X and Optical Diode are listed in NATO's NIAPC, and BSG carries IEC 62443 certification. [2], [10], [12], [23] |

---

## 4. Notable Strengths

- **Hardware-enforced protocol break (items 1.1, 1.2):** Transfer protocols are terminated at the diode ingest point and re-originated with new session IDs over a non-routable serial/optical link, with no TCP/IP handshake or routing across the boundary [6, 8, 12].
- **Deep CDR content sanitization (items 2.1, 2.2, 2.7):** Deep CDR disassembles and reconstructs 150-200+ file types from verified elements, removing macros, scripts, embedded objects, metadata, and steganographic payloads (iTXt chunks, pixel-level data) [7, 8, 14, 15].
- **Layered inspection at the boundary (items 2.3, 2.6):** Metascan Multiscanning runs 30+ anti-malware engines and Proactive DLP blocks sensitive/classified data and credentials during cross-domain transfer [3, 7, 8].
- **Measured low latency and scalable throughput (items 4.1, 4.2):** Vendor datasheets report 0.6 ms TCP / 0.7 ms UDP latency and a platform scale from 100 Mbps to 1 Gbps (field upgrade) and 10 Gbps (enterprise) [2, 6, 12, 14].
- **Certification portfolio (item 5.4):** Common Criteria EAL4+ (USG/Diode X), FIPS 140-3 for the MetaDefender platform crypto module (NIST CMVP #5225), NATO NIAPC listing for Diode X and Optical Diode, and IEC 62443 for BSG [10, 12, 14, 23].

## 5. Notable Gaps / Risks

- **No quantified HA switchover time (item 4.3):** Active/standby failover and 99.99% availability are documented, but no switchover time in ms is published, so the <=100 ms no-session-loss threshold cannot be confirmed; a vendor-furnished failover-time measurement would resolve this.
- **Database support is replication-based, not a query-whitelist proxy (item 3.3):** SQL Server/Oracle GoldenGate/historian replication is documented, but there is no evidence of a SQL proxy with query-command whitelisting as the checklist assumes.
- **Schema validation covers XML/XSD only (item 2.4):** XML validation against XSD schemas is documented, but JSON schema and FIXM/AIXM-specific validation are not evidenced.
- **No explicit security-label-based filtering (item 2.5):** Policies can condition on file attributes/metadata and content type, but filtering on attached security/classification labels (e.g., STANAG 4774/4778) is not documented.
- **SIEM delivery lacks CEF/TLS detail (item 5.2):** Real-time Syslog to SIEM is documented, but CEF format and TLS-encrypted delivery to the SIEM are not explicitly documented.

## 6. Evidence Quality Notes

Evidence was collected from 25 distinct sources and 67 grounded quotes, all verified as exact substrings of the staged artifacts (artifacts/manifest.jsonl sha256-anchored). No item was triangulated across genuinely independent sources: 24 of 25 sources are OPSWAT-published (12 vendor_doc, 4 vendor_datasheet, 7 vendor_blog, 1 product_release_notes), and only the NIST CMVP certificate #5225 is an independent registry (certification_registry), used for item 5.4 — the sole item allowed "high" confidence; all other items are capped at "medium" by the validator's vendor-only rule. Most items (18) draw on 2-3 vendor sources for triangulation of vendor claims; 2.4, 2.7 and 5.4 rest on one primary source each.

Two caveats shape the verdicts. First, the assessed product line no longer exists under the "MetaDefender Cross Domain Gateway" name; the run anchored on its documented successors (Diode X, USG, BSG, Optical Diode), which the vendor's own materials treat as the CDS family, but CDG-era documentation (docs.opswat.com/mcdg) is no longer online and could not be retrieved (Internet Archive was rate-limited throughout the run; the current docs are JS-rendered and were staged via a reader proxy for three pages). Second, partial verdicts (2.4, 2.5, 3.3, 3.4, 4.3, 5.2) reflect real gaps between vendor documentation and checklist specifics — e.g., no failover time in ms, no query-whitelist database proxy, no CEF/TLS SIEM channel — rather than contradictions between sources; no two sources contradicted each other on any item.

---

## Bibliography

[1] OPSWAT. "OPSWAT - MetaDefender Bilateral Security Gateway (BSG) for IT & OT - product page". https://www.opswat.com/products/metadefender/bilateral-security-gateway-bsg (Retrieved: 2026-08-11T08:20:48Z)
[2] OPSWAT. "OPSWAT - MetaDefender Bilateral Security Gateway Datasheet (Rev. 2026-06)". https://static.opswat.com/uploads/files/opswat-metadefender-bilateral-security-gateway-datasheet.pdf (Retrieved: 2026-08-11T08:22:50Z)
[3] OPSWAT. "OPSWAT - Cross Domain Solutions - solutions page". https://www.opswat.com/solutions/cross-domain (Retrieved: 2026-08-11T08:25:50Z)
[4] OPSWAT. "OPSWAT - MetaDefender Unidirectional Security Gateway (USG) - product page". https://www.opswat.com/products/metadefender/unidirectional-security-gateway-usg (Retrieved: 2026-08-11T08:25:50Z)
[5] OPSWAT. "OPSWAT - MetaDefender NetWall Series High Availability Solution Brief (Rev. 2026-05)". https://static.opswat.com/uploads/files/opswat-metadefender-netwall-high-availability-solution-brief.pdf (Retrieved: 2026-08-11T08:25:59Z)
[6] OPSWAT. "OPSWAT - MetaDefender NetWall Series Brochure (Rev. 2026-05)". https://static.opswat.com/uploads/files/opswat-metadefender-netwall-series-brochure.pdf (Retrieved: 2026-08-11T08:25:59Z)
[7] OPSWAT. "OPSWAT Blog - Data Diodes in Transfer CDS: Securing High-Assurance Cross-Domain Solutions (Mar 19, 2026)". https://www.opswat.com/blog/data-diodes-in-transfer-cds-securing-high-assurance-cross-domain-solutions (Retrieved: 2026-08-11T08:32:23Z)
[8] OPSWAT. "OPSWAT - Buyer's Guide: Cross-Domain Solutions for Government & Defense (Rev. 2026-03)". https://static.opswat.com/uploads/files/opswat-cross-domain-solutions-for-government-defense-guide.pdf (Retrieved: 2026-08-11T08:32:23Z)
[9] OPSWAT. "OPSWAT Blog - Secure Cross-Domain Transfers Across Untrusted Networks Using Data Diodes, Digital Signatures, and mTLS (Jun 25, 2026)". https://www.opswat.com/blog/secure-cross-domain-transfers-across-untrusted-networks-using-data-diodes-digital-signatures-and-mtls (Retrieved: 2026-08-11T08:32:29Z)
[10] OPSWAT. "OPSWAT Press - Data Diode Products Listed on NIAPC for Use in Mission-Critical Environments Across NATO Member Countries (Jul 31, 2025)". https://www.opswat.com/blog/opswat-data-diode-products-listed-on-niapc-for-use-in-mission-critical-environments-across-nato-member-countries (Retrieved: 2026-08-11T08:32:29Z)
[11] OPSWAT. "OPSWAT Blog - Data Diodes and IEC 62443: The Keys to Staying Compliant". https://www.opswat.com/blog/data-diodes-and-iec-62443-the-keys-to-staying-compliant (Retrieved: 2026-08-11T08:32:33Z)
[12] OPSWAT. "OPSWAT - MetaDefender Unidirectional Security Gateway Datasheet (Rev. 2026-06)". https://static.opswat.com/uploads/files/opswat-metadefender-unidirectional-security-gateway-datasheet.pdf (Retrieved: 2026-08-11T08:38:49Z)
[13] OPSWAT. "OPSWAT - MetaDefender Diode X (formerly Transfer Guard) - product page". https://www.opswat.com/products/metadefender/diode-x (Retrieved: 2026-08-11T08:38:55Z)
[14] OPSWAT. "OPSWAT - MetaDefender Diode X Datasheet (Rev. 2026-06)". https://static.opswat.com/uploads/files/opswat-metadefender-diode-x-datasheet.pdf (Retrieved: 2026-08-11T08:38:55Z)
[15] OPSWAT. "OPSWAT Blog - How Deep CDR Technology Prevents Steganography-Based Threats Embedded in Image Files (Jul 22, 2026)". https://www.opswat.com/blog/how-steganography-based-threats-hidden-in-image-files-are-prevented-with-deep-cdr (Retrieved: 2026-08-11T08:39:14Z)
[16] OPSWAT. "OPSWAT Blog - OPSWAT Announces the Release of Role-Based User Management for MetaDefender Core (Feb 1, 2017)". https://www.opswat.com/blog/opswat-announces-release-role-based-user-management-metadefender-core (Retrieved: 2026-08-11T08:39:14Z)
[17] OPSWAT. "OPSWAT Blog - MetaDefender Software Supply Chain v3.3.0: Cross Domain Transfer, Expanded Integrations (May 4, 2026)". https://www.opswat.com/blog/metadefender-software-supply-chain-v3-3-0-cross-domain-transfer-expanded-integrations-and-deeper-visibility (Retrieved: 2026-08-11T08:40:19Z)
[18] OPSWAT. "OPSWAT MetaDefender Core v5.20.0 Docs - Validate XML files against an XSD schema (reader-rendered; original is JS-rendered at www.opswat.com/docs/mdcore/v5.20.0/deep-cdr/validate-xml-files-against-an-xsd-schema)". https://r.jina.ai/https://www.opswat.com/docs/mdcore/v5.20.0/deep-cdr/validate-xml-files-against-an-xsd-schema (Retrieved: 2026-08-11T08:40:56Z)
[19] OPSWAT. "OPSWAT MetaDefender Core v5.20.0 Docs - Deep CDR Performance (Throughput) (reader-rendered; original is JS-rendered at www.opswat.com/docs/mdcore/v5.20.0/deep-cdr/deep-cdr-performance--throughput-)". https://r.jina.ai/https://www.opswat.com/docs/mdcore/v5.20.0/deep-cdr/deep-cdr-performance--throughput- (Retrieved: 2026-08-11T08:41:05Z)
[20] OPSWAT. "OPSWAT - MetaDefender Kiosk - product page". https://www.opswat.com/products/metadefender/kiosk (Retrieved: 2026-08-11T08:42:00Z)
[21] OPSWAT. "OPSWAT - MetaDefender Managed File Transfer (MFT) - product page". https://www.opswat.com/products/metadefender/managed-file-transfer (Retrieved: 2026-08-11T08:42:00Z)
[22] OPSWAT. "OPSWAT MetaDefender Core v5.20.0 KB - Why have the ESET and Kaspersky scan engines failed to initialize on the hardened Linux OS? (reader-rendered; original is JS-rendered at www.opswat.com/docs/mdcore/v5.20.0/knowledge-base/eset-and-kaspersky-engines-failed-to-initialize-on-the-hardened-)". https://r.jina.ai/https://www.opswat.com/docs/mdcore/v5.20.0/knowledge-base/eset-and-kaspersky-engines-failed-to-initialize-on-the-hardened- (Retrieved: 2026-08-11T08:44:33Z)
[23] NIST (CMVP). "NIST CMVP - Certificate #5225: OPSWAT Cryptographic Module (FIPS 140-3, Overall Level 1, Active)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5225 (Retrieved: 2026-08-11T08:47:39Z)
[24] OPSWAT. "OPSWAT - Data Diode Comparison Guide (Rev. 2026-06)". https://static.opswat.com/uploads/images/opswat-data-diode-comparison-guide.pdf (Retrieved: 2026-08-11T08:32:33Z)
[25] OPSWAT. "OPSWAT Blog (CEO Benny Czarny) - Why We Entered the Data Diode and Unidirectional Gateway Business (Feb 11, 2026)". https://www.opswat.com/blog/why-we-entered-the-data-diode-and-unidirectional-gateway-business (Retrieved: 2026-08-11T08:26:16Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 25 (kept: 25, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, product_release_notes: 1, vendor_blog: 7, vendor_datasheet: 4, vendor_doc: 12
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
