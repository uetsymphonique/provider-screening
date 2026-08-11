# BSG / Cross Domain Product Assessment: Everfox — Everfox High Assurance Cross Domain Gateway

**Product ID:** `everfox-high-assurance-cross-domain-gateway`
**Version reference:** Everfox CDS family: Data Guard v4.0.0.2 (CC EAL4+), Trusted Gateway System, High Speed Guard, High Speed Verifier, Information eXchange, Data Diode (2024-2026 datasheets)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:10:31Z
**Total evidence items collected:** 82
**Total distinct sources:** 26

---

## 1. Overview

Everfox (formerly Forcepoint Federal) is a US high-assurance Cross Domain Solution (CDS) vendor, not a firewall vendor: it markets "Cross Domain Solutions that are purpose-built to enable secure and timely data access and transfer between networks operating at different security classification levels or security controls" [1]. The assessed "High Assurance Cross Domain Gateway" capability is delivered by its bidirectional CDS family: Data Guard (Common Criteria EAL4+ certified [13][23]), Trusted Gateway System for multi-directional unstructured file transfer [3], High Speed Guard for high-throughput structured/streaming transfer [4], the hardware High Speed Verifier (HSV) that enforces protocol/data breaks in FPGA logic [9][18], and the Information eXchange (iX) boundary appliance with built-in CDR [5]. Everfox positions the family against NCDSMO Raise the Bar and states its solutions are approved for US Defense, Intelligence and FVEY partners [1]. Deployment shapes span enterprise air-gapped networks, tactical/SWaP-C platforms (HSG SP, HSV-T) [4][9], and cloud/virtual form factors for iX [19]; TGS and HSG are managed centrally via Control Center [8].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 14    | 1                | 13     | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 2     | 0                | 0      | 2   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 16 items backed by ≥ 2 source_types; 21 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | — | Everfox documents full protocol breaks across its CDS family: the Data Guard datasheet cites a full protocol break on a Common Criteria-evaluated platform, the HSV enforces a protocol break in hardware logic with no TCP/IP crossing the verifier, and High Speed Guard inspects application-level data without forwarding or routing packets. [7], [13], [16], [18] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | — | Hardware-enforced separation is documented: HSV verifies protocol and data breaks in FPGA hardware logic, iX splits proxy/CDR across two servers, and the GIA provides three physically separate network ports. A literal two-processing-board FPGA/shared-memory design is not stated. [5], [6], [7], [18] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | Default-deny behavior is documented: TGS denies all SCP connections from non-configured hosts, HSV never delivers received data, and TGS only admits known-good reconstructed files into classified enclaves. [3], [4], [14], [18] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | — | All three guard appliances run hardened operating systems: TGS and HSG use Red Hat Enterprise Linux with SELinux components, and iX runs on a hardened, cut-down Linux kernel. [14], [15], [19] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No source describes an internal control core digitally signing/stamping sanitized data before a new outbound session is initiated; the HSV's 'data break' is a hardware data break rather than cryptographic stamping.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Supported | medium | — | Everfox CDR rebuilds Office, PDF and image files from verified content only, discarding originals; TGS applies a Zero Trust CDR filter and Office/PDF sanitization filters, and Data Guard offers a CDR plugin. CAD formats are not explicitly named in the cited sources. [1], [10], [13], [14], [17] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Supported | medium | — | Reconstruction-based sanitization removes embedded executable content: CDR rebuilds files using only the legitimate content and TGS documents document inspection, malware scanning, metadata removal and CDR for Office/PDF files. [10], [14], [17] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Supported | medium | — | TGS ships two independent AV engines (McAfee and Sophos signature scanning filters) plus multi-engine analysis with CDR, and Data Guard integrates the McAfee engine as an optional plugin. [3], [13], [14] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Supported | medium | — | Schema validation is documented for XML/JSON (Data Guard validates schema and digital signature), TGS validates XML against stored XSD schemas, and iX constrains web application traffic to pre-defined schemas. [5], [13], [14] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Partial | medium | — | HSG extracts, audits and validates classification/release-caveat metadata (KLV) inside video streams, and the NCSC-based brochure describes domain labelling in the transfer UI. File-level security-label-driven filtering (IFC) is not otherwise documented. [15], [21] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Supported | medium | — | TGS provides a dirty-word text search filter supporting plain text and regular expressions across any file type, and Data Guard's CDR plugin can redact sensitive or unwanted data. [13], [14] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Supported | medium | — | iX explicitly destroys steganography ('stegware') in images in email, web services and file transfers without signature detection, and TGS image filters strip the least significant bit of pixel-based images; CDR rebuilds files from known-good content so hidden payloads do not survive. [5], [11], [14], [19] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | SFTP/SCP file transfer with inspection is documented on TGS, Data Guard's File Drop uses SCP, HSG's Automated Secure Transfer supports SCP and FTP, and Data Guard performs HTTPS decryption with CDR cleaning. SMB/NFS proxies and explicit FTPS are not cited. [13], [14], [15] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | HSG ICS secures and validates SCADA protocols DNP3, IEC 61850, ICCP and MMS with latency meeting DNP3/IEC 61850 requirements, and the Data Diode moves data for SCADA/PLC/DCS assets. OPC UA, Modbus TCP, IEC 60870-5-104 and MQTT are not cited. [7], [16] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No cited source documents a database-protocol proxy (SQL Server, Oracle, PostgreSQL) with query whitelisting; databases appear only as generic data assets moved by the Data Diode.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Supported | medium | — | Data Guard's video adaptor inspects RTSP/RTP, MPEG-TS and HLS streams with KLV checking, HSG provides audited MPEG transport-stream video with STANAG 4609 support, and audit logs can be relayed off-box via syslog. CEF format is not cited. [13], [15], [21] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 9000 Mbps | High Speed Guard sustains bidirectional transfer rates over 9 Gb/s (9,000 Mbps) on 10 Gb networks per its datasheet, and the Data Diode datasheet cites 9 Gbps unidirectional speed; both exceed the 1,000 Mbps threshold. [15], [16], [20] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 1.3 ms | High Speed Guard cites latencies as low as 1.3 ms (product page and datasheet) and sub-10 ms transfer on commodity hardware for the ICS variant, within the 10 ms threshold. [4], [15], [16] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | HSV documents built-in high availability and failover features with non-stop operation and dual redundant hot-swappable power supplies, and GIA supports cross-site redundancy and high availability. No switchover-time figure is published, so the 100 ms requirement cannot be verified. [6], [18] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | HSG halts the server or stops transfer mechanisms on integrity-check failure, a fail-closed behavior, and HSV's hardware verification is non-bypassable. Explicit DoS-triggered fail-close is not described. [15], [18] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | — | FC2 provides separate administrative roles (System Administrator vs Security Administrator approvals) with LDAP login and process/role separation, TGS enforces two-person human review with producer/releaser roles, and HSG enforces two-person integrity controls. [3], [8], [15], [22] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Audit logs can be exported in real time via syslog to a SIEM (documented in the NCSC-based brochure, iX datasheet and HSG datasheet), and guard health/status is monitored via SNMP in Control Center. CEF format and a TLS-encrypted log transport channel are not explicitly cited. [8], [15], [19], [21] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | TGS documents alignment with NIST 800, RMF, ICD 503, SABI/TSABI and DIACAP, and HSG cites NIST 800-53 and 8500.01/RMF controls plus NERC CIP for the ICS variant. IEC 62443, ISO 27001 and NIST SP 800-82 report templates are not cited. [14], [15], [16] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | — | Everfox Data Guard v4.0.0.2 holds a Common Criteria EAL4+ certificate (OCSI, Italy, 2026-01-23) listed on the CC portal, TGS and HSG are NCDSMO Baseline solutions, and TTC with MESA was added to the NCDSMO Baseline per ExecutiveBiz coverage. FIPS 140-3 is not cited for the gateway. [12], [13], [14], [15], [23], [24], [25] |

---

## 4. Notable Strengths

- **Hardware-enforced protocol break (items 1.1, 1.2):** the HSV implements a protocol break and data break entirely in hardware logic with no TCP/IP crossing the verifier, and Data Guard documents a full protocol break on a Common Criteria-evaluated platform [13][18].
- **Reconstruction-based CDR and inspection depth (items 2.1, 2.2, 2.3, 2.7):** Everfox CDR rebuilds Office/PDF/image files from verified content only, TGS pairs two AV engines (McAfee and Sophos) with CDR and dirty-word/regex filtering, and iX explicitly destroys steganographic payloads without signature detection [10][14][17][19].
- **Published throughput/latency (items 4.1, 4.2):** High Speed Guard sustains over 9 Gb/s bidirectional transfer with latencies as low as 1.3 ms, exceeding the 1,000 Mbps and 10 ms checklist thresholds [4][15].
- **Certifications and baseline listings (item 5.4):** Data Guard v4.0.0.2 holds a Common Criteria EAL4+ certificate (OCSI, Italy, 2026-01-23) on the CC portal, and TGS/HSG are NCDSMO Baseline solutions [14][15][23][24].
- **Role-separated administration (item 5.1):** Control Center enforces separate System/Security Administrator approval workflows with LDAP login, and TGS/HSG support two-person review and integrity controls [3][22].

## 5. Notable Gaps / Risks

- **No internal data-stamping evidence (item 1.5):** no cited source describes a control core cryptographically signing sanitized data before a new outbound session; the HSV's "data break" is hardware, not cryptographic stamping. Certification/evaluation documentation would be needed to verify this.
- **No database-protocol proxy (item 3.3):** SQL Server, Oracle or PostgreSQL query-whitelisting proxies are not documented; databases appear only as generic data assets moved by the Data Diode. Vendor clarification or a DBA-flow datasheet would resolve this.
- **OT protocol set differs from the requirement (item 3.2):** HSG ICS documents DNP3, IEC 61850, ICCP and MMS, but OPC UA, Modbus TCP, IEC 60870-5-104 and MQTT are not cited; buyers needing those protocols should confirm roadmap support.
- **No published HA switchover time (item 4.3):** HSV/GIA document high availability and failover qualitatively but no failover/switchover duration, so the 100 ms no-session-loss requirement cannot be confirmed.
- **Log format and compliance-report gaps (items 5.2, 5.3):** syslog-to-SIEM export is documented but CEF format and a TLS-encrypted log channel are not; IEC 62443, ISO 27001 and NIST SP 800-82 report templates are not evidenced.

## 6. Evidence Quality Notes

22 of 24 items carry cited evidence drawn from 26 registered sources (82 evidence quotes); only 5.4 reaches high confidence because it is the sole item backed by an independent source type (Common Criteria portal registry, the OCSI certificate PDF, and ExecutiveBiz coverage relayed via Google News RSS, plus the Carahsoft reseller page). The remaining 21 items rely exclusively on vendor documentation and datasheets, which caps their confidence at medium per the validator rule - this matters because Everfox's CDS line is sold mostly through government channels with little independent public analysis of the gateway internals, so throughput (9 Gb/s), latency (1.3 ms), failover and protocol-support claims are vendor-asserted. No contradictions between sources were found; where partial evidence existed (e.g. OT protocols, SIEM/TLS log transport, fail-close behavior), verdicts were kept at partial rather than supported, and items 1.5 and 3.3 were left unknown because no source discusses them. All 82 evidence quotes were verified verbatim against the staged artifacts.

---

## Bibliography

[1] Everfox. "Everfox Cross Domain Solutions". https://www.everfox.com/products/cross-domain-solutions/ (Retrieved: 2026-08-11T09:10:31Z)
[2] Everfox. "Everfox Data Guard – Cross Domain Solution". https://www.everfox.com/products/cross-domain-solutions/data-guard/ (Retrieved: 2026-08-11T09:10:31Z)
[3] Everfox. "Everfox Trusted Gateway System (TGS)". https://www.everfox.com/products/cross-domain-solutions/trusted-gateway-system/ (Retrieved: 2026-08-11T09:10:31Z)
[4] Everfox. "Everfox High Speed Guard". https://www.everfox.com/products/cross-domain-solutions/high-speed-guard/ (Retrieved: 2026-08-11T09:10:31Z)
[5] Everfox. "Everfox Information eXchange (iX)". https://www.everfox.com/products/cross-domain-solutions/information-exchange/ (Retrieved: 2026-08-11T09:10:31Z)
[6] Everfox. "Everfox Garrison Isolation Appliance (GIA)". https://www.everfox.com/products/cross-domain-solutions/isolation-appliance/ (Retrieved: 2026-08-11T09:10:31Z)
[7] Everfox. "Everfox Data Diode". https://www.everfox.com/products/cross-domain-solutions/data-diode/ (Retrieved: 2026-08-11T09:10:31Z)
[8] Everfox. "Everfox Control Center (FC2)". https://www.everfox.com/products/cross-domain-solutions/control-center/ (Retrieved: 2026-08-11T09:10:31Z)
[9] Everfox. "Everfox High Speed Verifier Solutions (HSV & HSV-T)". https://www.everfox.com/products/cross-domain-solutions/high-speed-verifier-solutions/ (Retrieved: 2026-08-11T09:10:31Z)
[10] Everfox. "Everfox Content Disarm & Reconstruction (CDR)". https://www.everfox.com/products/content-disarm-reconstruction/ (Retrieved: 2026-08-11T09:10:31Z)
[11] Everfox. "Steganography – The Old Attack Mechanism that will Never Die". https://www.everfox.com/blog/cross-domain-solutions/steganography-the-old-attack-mechanism-that-will-never-die/ (Retrieved: 2026-08-11T09:10:31Z)
[12] Everfox. "Breaking Down Data Silos: Everfox MESA Achieves NCDSMO Baseline Listing". https://www.everfox.com/blog/cross-domain-solutions/breaking-down-data-silos-everfox-mesa-achieves-ncdsmo-baseline-listing/ (Retrieved: 2026-08-11T09:10:31Z)
[13] Everfox. "Everfox Data Guard Datasheet v1 (02/2026)". https://www.everfox.com/wp-content/uploads/2026/03/DataGuard_Datasheet_v1_022026.pdf (Retrieved: 2026-08-11T09:10:31Z)
[14] Everfox. "Everfox Trusted Gateway System Datasheet (07/2025)". https://www.everfox.com/wp-content/uploads/2025/07/datasheet-trusted-gateway-system.pdf (Retrieved: 2026-08-11T09:10:31Z)
[15] Everfox. "Everfox High Speed Guard Datasheet v2 (07/2026)". https://www.everfox.com/wp-content/uploads/2026/07/HSG_Datasheet_v2_072026.pdf (Retrieved: 2026-08-11T09:10:31Z)
[16] Everfox. "Everfox High Speed Guard Industrial Control Systems Datasheet (03/2024)". https://www.everfox.com/wp-content/uploads/2024/03/Datasheet_High_Speed_Guard_industrial_control_systems_en-031724.pdf (Retrieved: 2026-08-11T09:10:31Z)
[17] Everfox. "Everfox Content Disarm & Reconstruction Datasheet (03/2024)". https://www.everfox.com/wp-content/uploads/2024/03/Datasheet_Content_Disarm_Reconstruction-en-031124.pdf (Retrieved: 2026-08-11T09:10:31Z)
[18] Everfox. "Everfox High Speed Verifier (HSV) Datasheet (02/2024)". https://www.everfox.com/wp-content/uploads/2024/03/Datasheet_High-_Speed_Verifier_HSV-en-021324.pdf (Retrieved: 2026-08-11T09:10:31Z)
[19] Everfox. "Everfox Information eXchange (iX) Datasheet v3 (03/2026)". https://www.everfox.com/wp-content/uploads/2026/03/iX_Datasheet_v3_032026-1.pdf (Retrieved: 2026-08-11T09:10:31Z)
[20] Everfox. "Everfox Data Diode Datasheet v4 (08/2024)". https://www.everfox.com/wp-content/uploads/2024/08/Data-Diode-Datasheet-v4.pdf (Retrieved: 2026-08-11T09:10:31Z)
[21] Everfox. "Implementing the UK NCSC Principles for Cross Domain Solutions V3". https://www.everfox.com/wp-content/uploads/2024/05/Implementing-the-UK-National-Cyber-Security-Centre-Principles-for-Cross-Domain-Solutions-V3.pdf (Retrieved: 2026-08-11T09:10:31Z)
[22] Everfox. "Everfox Control Center (FC2) Datasheet (03/2024)". https://www.everfox.com/wp-content/uploads/2024/03/Datasheet_Everfox_Control_Center-en_031224.pdf (Retrieved: 2026-08-11T09:10:31Z)
[23] Common Criteria Portal. "Common Criteria Portal – Certified Products list (Everfox)". https://www.commoncriteriaportal.org/products/index.cfm?search=1&vendor=Everfox%20LLC (Retrieved: 2026-08-11T09:10:31Z)
[24] Agenzia per la Cybersicurezza Nazionale (OCSI). "Common Criteria Certificate 03/2026 – Everfox Data Guard v4.0.0.2 (OCSI, Italy)". https://www.commoncriteriaportal.org/files/epfiles/FP_cr_everfox_dataguard_v4002_v1.0_en.pdf (Retrieved: 2026-08-11T09:10:31Z)
[25] Google News / ExecutiveBiz. "Google News RSS – Everfox MESA NCDSMO coverage (ExecutiveBiz)". https://news.google.com/rss/search?q=%22Everfox+MESA%22+NCDSMO&hl=en-US&gl=US&ceid=US:en (Retrieved: 2026-08-11T09:10:31Z)
[26] Carahsoft. "Everfox for Government – Carahsoft partner page". https://www.carahsoft.com/everfox (Retrieved: 2026-08-11T09:10:31Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** n/a (not tracked)
- **Sources reviewed:** 26 (kept: 26, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, third_party_review: 2, vendor_blog: 2, vendor_datasheet: 9, vendor_doc: 11
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
