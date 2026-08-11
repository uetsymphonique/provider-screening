# BSG / Cross Domain Product Assessment: WAGO — WAGO Industrial Security Gateway

**Product ID:** `wago-industrial-security-gateway`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:13:40Z
**Total evidence items collected:** 5
**Total distinct sources:** 4

---

## 1. Overview

The provider list (providers/BSG.csv) describes the WAGO Industrial Security Gateway as a compact industrial security gateway supporting VPN/firewall protection of bidirectional control-cabinet connections, i.e. an industrial network-gateway class product rather than a cross-domain guard. WAGO GmbH & Co. KG is an industrial automation vendor whose published OT-cybersecurity portfolio consists of monitoring, management and analysis software (Cybersecurity Network Sight, Collector, Management, Analysis), industrial Ethernet switches, and security consulting [1, 2]. This assessment could not locate any public product page, datasheet, manual or press material for a product named "Industrial Security Gateway" — wago.com product sitemaps and site search across locales, WAGO press pages, Google News RSS, YouTube and GitHub were all searched on 2026-08-11. The staged sources therefore document WAGO's corporate security posture (IEC 62443-4-1 certified development processes, ISO 27001 ISMS, standards-aligned analysis tooling) [1, 3, 4] rather than the gateway product's own capabilities; 22 of 24 checklist items are rated unknown as a result.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 0     | 0                | 0      | 0   |
| partial          | 2     | 0                | 2      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 22    | 0                | 0      | 22  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 0 items backed by ≥ 2 source_types; 2 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Unknown | low | — | no evidence found (No source documents a protocol-break / TCP-session-termination architecture for the WAGO Industrial Security Gateway; the product itself is undocumented in the sources reviewed.) |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No source documents a dual processing-board design with FPGA or isolated shared-memory link for this product.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Unknown | low | — | no evidence found (No source documents default-deny / whitelist-only forwarding behaviour for this product.) |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No source documents the underlying OS hardening (hardened OS, microkernel or SELinux strict mode) of this product.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No source documents internal signing/stamping of clean data before new sessions are initiated.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No source documents content disarm and reconstruction (CDR) of Office, PDF, image or CAD formats for this product.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No source documents removal of VBA macros, JavaScript, DDE links or embedded objects.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No source documents multi-engine antivirus scanning (2+ engines) of raw payloads.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No source documents XML/JSON/FIXM/AIXM schema validation (W3C Schema) for this product.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No source documents information-flow control based on security labels attached to files.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No source documents DLP detection/blocking of secret keywords, ID numbers, accounts or custom regex for this product.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No source documents steganography detection or removal in image files (PNG, JPEG, BMP).) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No source documents SFTP, FTP/S, HTTPS, SMB/NFS proxy with content cleaning for this product.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found (No source documents OT/ICS protocol support (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) for this product.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No source documents database proxy support (SQL Server, Oracle, PostgreSQL) or query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No source documents RTSP video proxy or syslog/CEF relay services for this product.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | — | no evidence found (No source mentions a processing-throughput figure for this product; numeric threshold (>= 1000 Mbps) cannot be evaluated.) |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No source mentions a processing-latency figure for this product; numeric threshold (<= 10 ms) cannot be evaluated.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found (No source documents HA active-standby configuration or failover switchover time; numeric threshold (<= 100 ms) cannot be evaluated.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No source documents fail-close behaviour under DoS or overload conditions for this product.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (No source documents role-based administration with separated system-admin / policy-admin / auditor roles for this product.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (No source documents CEF/Syslog log export over TLS to a SIEM for this gateway product; the staged sources mention SIEM data export only for the separate Cybersecurity Network Sight/Collector portfolio.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | WAGO documents that its Cybersecurity Analysis platform supports conformity with international standards such as NIST, IEC 62443 and ISO 27001, and that the company operates an ISO 27001-based ISMS. No gateway-specific compliance report template (NIST SP 800-82, IEC 62443, ISO 27001) is documented, and the cited evidence concerns WAGO's analysis platform rather than the Industrial Security Gateway itself. [3] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | — | WAGO documents that its hardware and software development processes are certified per IEC 62443-4-1, with certification granted by TÜV NORD under national DAkkS and international IECEE accreditation. The checklist's named certifications (Common Criteria EAL4+, FIPS 140-3, national cryptographic certification) are not documented for this product. [1], [4] |

---

## 4. Notable Strengths

- **IEC 62443-4-1 certified development process (item 5.4):** WAGO documents that its hardware and software development processes are certified per IEC 62443-4-1, with TÜV NORD accreditation under national DAkkS and international IECEE classes [1, 4] — a genuine security-by-design baseline for any WAGO product, though it is a process certification, not a product-level Common Criteria/FIPS evaluation.
- **Standards-aligned compliance tooling at portfolio level (item 5.3):** WAGO's published materials state its Cybersecurity Analysis platform supports conformity with NIST, IEC 62443 and ISO 27001 frameworks, and that the company operates an ISO 27001-based ISMS [3].
- **Established OT-security portfolio and consulting practice (context for items 5.3, 5.4):** WAGO documents a coherent portfolio of passive network monitoring (Network Sight), encrypted edge data collection (Collector), management/analysis platforms and OT-security consulting for Smart Factory, Smart Building and Smart Energy [1, 2, 3].

## 5. Notable Gaps / Risks

- **Product is undocumented in public sources (items 1.1-5.2):** no product page, datasheet, manual or press material for the WAGO Industrial Security Gateway could be located on 2026-08-11, leaving 22 of 24 checklist items unknown; a vendor datasheet or product page describing the gateway would resolve most of these items.
- **No numeric performance data (items 4.1, 4.2, 4.3):** no throughput, processing-latency or HA failover-switchover figures are published, so the numeric thresholds (>= 1000 Mbps, <= 10 ms, <= 100 ms) cannot be evaluated.
- **No CDS-specific capabilities documented (items 1.1, 1.2, 1.5, 2.1, 2.4, 2.5, 2.7):** protocol break, hardware isolation, internal data stamping, CDR, schema validation, IFC/security labels and anti-steganography are all unknown; if the product is a firewall/VPN-class gateway these may be out of scope, but no citable source establishes that category, so they are not marked not_applicable.
- **Certification is process-level only (item 5.4):** IEC 62443-4-1 covers WAGO's development process rather than a product evaluation; no Common Criteria EAL4+, FIPS 140-3 or national cryptographic certification is documented for this product.
- **Vendor-only evidence base (all non-unknown items):** every piece of evidence is vendor-published; no independent lab test, analyst report or third-party review was locatable.

## 6. Evidence Quality Notes

No checklist item is triangulated across three or more independent sources: the only non-unknown verdicts (5.3, 5.4) rest on WAGO-published pages only, so their confidence is capped at medium by the validator rule, and the remaining 22 items are unknown with no evidence at all. The evidence for 5.3 and 5.4 is corporate/portfolio-level (IEC 62443-4-1 certified development processes, ISO 27001 ISMS, Cybersecurity Analysis conformity support) rather than product-level, and the notes for both items state this explicitly so the reader cannot mistake a company posture statement for a gateway capability claim [1, 3, 4]. Discovery was constrained by the environment: all general web search engines returned anti-bot blocks or empty results, web.archive.org CDX was persistently rate-limited, and the Common Criteria portal rejected automated access, so no certification-registry or third-party source could be staged. This means the assessment likely understates coverage — a WAGO gateway datasheet or a future announcement may well document capabilities that are currently rated unknown. No source contradictions surfaced; the WAGO corpus is internally consistent. All five quoted evidence fragments were verified verbatim against the staged artifact texts (5/5 grounded).

---

## Bibliography

[1] WAGO GmbH & Co. KG. "Cybersecurity in Digitalization | WAGO - OT cybersecurity hub page". https://www.wago.com/global/trends-topics-technologies/topics/cybersecurity (Retrieved: 2026-08-11T09:13:40Z)
[2] WAGO GmbH & Co. KG. "Precise Solutions for Maximum Safety | WAGO - cybersecurity solution portfolio". https://www.wago.com/global/trends-topics-technologies/topics/cybersecurity/custom-solutions (Retrieved: 2026-08-11T09:13:40Z)
[3] WAGO GmbH & Co. KG. "Cyberresilienz staerken - WAGO interview with Dr. Christopher Tebbe and Kilian Froehlich (source: Computer & Automation 09.2024)". https://www.wago.com/de/offene-automatisierung/cyber-security/cyberresilienz-staerken (Retrieved: 2026-08-11T09:13:40Z)
[4] WAGO GmbH & Co. KG. "Optimal Compliance with Security Requirements with WAGO - IEC 62443-4-1 certification statement". https://www.wago.com/global/trends-topics-technologies/topics/cybersecurity/iec (Retrieved: 2026-08-11T09:13:40Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 4 (kept: 4, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
