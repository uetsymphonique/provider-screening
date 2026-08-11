# BSG / Cross Domain Product Assessment: Trend Micro — EdgeIPS Industrial Security Gateway

**Product ID:** `edgeips-industrial-security-gateway`
**Version reference:** EdgeIPS / EdgeIPS Pro firmware 2.1 (announced 2024-10); 2025-edition EdgeIPS family datasheets
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:15:49Z
**Total evidence items collected:** 56
**Total distinct sources:** 20

---

## 1. Overview

Trend Micro's EdgeIPS Industrial Security Gateway is marketed by TXOne Networks, the Trend Micro-Moxa joint venture, as a family of transparent inline industrial intrusion prevention systems (IPS) spanning compact DIN-rail units (EdgeIPS 102/103, EdgeIPS LE 102) and rack-mount Pro platforms (212F, 732, 1048/2096, 2016F/4016F) [1]. The vendor positions it as an operations-first OT security appliance rather than a cross-domain guard: it deploys transparently without IP changes or network redesign, uses Gen3 hardware bypass on every segment to preserve production continuity, and inspects 180+ industrial protocols with L2-L7 deep packet inspection [1, 9]. Deployment shapes include production-cell protection, control-room aggregation, high-speed fiber backbones, and remote/harsh environments, with centralized management through the EdgeOne console [1, 14]. Firmware 2.1 added CPSDR-Networking, asset-centric AI policy learning, and centralized management enhancements [19]. Because the documented category is a transparent inline IPS/security gateway, the guard/CDS-specific checklist items (protocol break, hardware isolation, data stamping, CDR, schema validation, IFC labels, anti-steganography) are marked not applicable [1, 9].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 4     | 0                | 4      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 4     | 0                | 0      | 4   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 10 items backed by ≥ 2 source_types; 19 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Vendor markets EdgeIPS as a transparent inline intrusion prevention system that forwards traffic without IP changes or network redesign; the FAQ confirms it is a transparent device, not a switch, so TCP/IP sessions are not terminated at the boundary as in a protocol-break guard.
- **1.2:** EdgeIPS's documented fail-safe is a Gen3 hardware bypass on every port pair rather than two isolated processing boards linked by FPGA or isolated shared memory; the dual-board isolation architecture of a CDS guard is not part of this product's category.
- **1.5:** EdgeIPS is documented as a transparent inline IPS with DPI on live traffic; internal signing/stamping of sanitized data before re-initiating a session is a guard-architecture mechanism that does not apply to this product category.
- **2.1:** EdgeIPS performs L2-L7 deep packet inspection and signature-based antivirus filtering of live traffic; content disarm and reconstruction (CDR) of files is not documented for this inline IPS category.
- **2.4:** EdgeIPS is a transparent inline IPS, not a schema-validation message gateway; XML/JSON/FIXM/AIXM W3C schema validation is not part of its documented category.
- **2.5:** EdgeIPS filters on protocol allowlists/blocklists and signatures rather than on security labels attached to files; IFC label-based filtering is a guard-domain mechanism that does not apply to this category.
- **2.7:** EdgeIPS is documented as an inline IPS with DPI and signature-based protection; anti-steganography detection in image files is a guard-domain mechanism not applicable to this product category.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Vendor markets EdgeIPS as a transparent inline intrusion prevention system that forwards traffic without IP changes or network redesign; the FAQ confirms it is a transparent device, not a switch, so TCP/IP sessions are not terminated at the boundary as in a protocol-break guard. [1], [9] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | EdgeIPS's documented fail-safe is a Gen3 hardware bypass on every port pair rather than two isolated processing boards linked by FPGA or isolated shared memory; the dual-board isolation architecture of a CDS guard is not part of this product's category. [1], [2] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | OT protocol allowlist/blocklist rules with accept or deny actions are documented, AI-driven baseline allowlists are generated per asset, and the vendor recommends a 'drop' deny action; a blanket default-deny of all non-allowlisted traffic is not explicitly documented. [1], [9], [13] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No public documentation of the underlying OS hardening model (hardened OS / microkernel / SELinux strict mode) was found.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | EdgeIPS is documented as a transparent inline IPS with DPI on live traffic; internal signing/stamping of sanitized data before re-initiating a session is a guard-architecture mechanism that does not apply to this product category. [1] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | EdgeIPS performs L2-L7 deep packet inspection and signature-based antivirus filtering of live traffic; content disarm and reconstruction (CDR) of files is not documented for this inline IPS category. [1], [2] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No documentation of macro/script removal (VBA, JavaScript, DDE links, embedded objects) from files was found.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | Signature-based antivirus scanning of network traffic and of file downloads over HTTP, FTP and SMB is documented; integration of two or more parallel antivirus engines is not documented. [2], [12] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | EdgeIPS is a transparent inline IPS, not a schema-validation message gateway; XML/JSON/FIXM/AIXM W3C schema validation is not part of its documented category. [1] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | EdgeIPS filters on protocol allowlists/blocklists and signatures rather than on security labels attached to files; IFC label-based filtering is a guard-domain mechanism that does not apply to this category. [1], [13] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No data-loss-prevention (keyword/CMND/account/regex) filtering capability was found in the staged documentation.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | EdgeIPS is documented as an inline IPS with DPI and signature-based protection; anti-steganography detection in image files is a guard-domain mechanism not applicable to this product category. [1] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | EdgeIPS Pro scans file downloads over HTTP, FTP and SMB with antivirus profiles and EdgeIPS supports SMB access control; no SFTP/NFS proxy or file content sanitization (cleaning) is documented. [10], [12] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | — | EdgeIPS supports Modbus, EtherNet/IP, CIP, FINS, S7Comm/S7Comm+, SECS/GEM, IEC 61850-MMS, IEC-104, CODESYS and 180+ additional industrial protocols; protocol filter profiles with advanced settings cover DNP3, OPC UA, OPC Classic and PROFINET. [1], [9] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No database proxy (SQL Server/Oracle/PostgreSQL with query whitelisting) evidence was found.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | CEF and LEEF syslog forwarding directly to external syslog servers is documented for EdgeIPS and EdgeIPS Pro; no RTSP video proxy capability is documented. [9], [10] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1800 Mbps | The EdgeIPS Pro 212F datasheet cites 1.8 Gbps+ (IMIX) threat-prevention throughput, and the family scales from 100 Mbps (EdgeIPS LE 102) to 40 Gbps (EdgeIPS Pro 4016F). [1], [2], [3] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.5 ms | The EdgeIPS Pro 212F datasheet cites <500 microseconds average latency under mixed traffic, i.e. 0.5 ms, and the product page states sub-500 microsecond latency. [1], [2] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Gen3 hardware bypass failover with sub-microsecond switchover, HA ports on Pro models, and redundant active-active hot-swappable PSUs are documented; active-standby clustering with session state sync is not explicitly documented, so switchover timing evidence remains qualitative. [1], [2] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Not Supported | medium | — | EdgeIPS fail-safe is documented as hardware bypass that switches to closed bridge mode (short circuit) so traffic continues without inspection on system crash, hang or power loss, and the EdgeIPS 102 datasheet labels the bypass 'Fail Open'; this is the opposite of the fail-close boundary lock required by the checklist. [6], [9] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | The EdgeOne management console supports role-based access control with multiple accounts at distinct permission levels, including System Admin accounts; a strict three-role separation (System Admin / Policy Admin / Security Auditor) is not explicitly documented. [14], [15], [16] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | — | EdgeIPS/EdgeIPS Pro forward CEF and LEEF syslog directly to external syslog servers, and EdgeOne provides SIEM/SOC integration via API with log forwarding. [9], [14], [15] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | IEC 62443 compliance support (zones/conduits network segmentation, IEC 62443-4-1 certified development) and EdgeOne audit logging are documented; no built-in NIST SP 800-82 or ISO 27001 report templates are documented. [1], [14], [17] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | The EdgeIPS Pro 212F datasheet lists only CE, FCC, VCCI, UL, CISPR and RoHS certifications, and the Common Criteria portal contains no EdgeIPS/TXOne entry (Trend Micro's CC-certified products are Deep Security and TippingPoint); IEC 62443-4-1 is a development-process certification, not a product certification of the type required by the checklist. [2], [18], [20] |

---

## 4. Notable Strengths

- **OT protocol depth (item 3.2):** supports Modbus, EtherNet/IP, CIP, FINS, S7Comm/S7Comm+, SECS/GEM, IEC 61850-MMS, IEC-104, CODESYS and 180+ additional industrial protocols, with DNP3, OPC UA, OPC Classic and PROFINET in protocol filter profiles, all without firmware updates [1, 9].
- **Performance headroom (items 4.1, 4.2):** 1.8 Gbps+ IMIX threat-prevention throughput on the Pro 212F up to 40 Gbps on the Pro 4016F, with <500 microseconds average latency across the family [2, 3].
- **Fail-safe production continuity (item 4.3):** Gen3 hardware bypass with sub-microsecond switchover on every segment plus redundant active-active hot-swappable PSUs on rack models [1, 2].
- **SIEM/SOC integration (item 5.2):** CEF/LEEF syslog forwarded directly to external syslog servers, plus EdgeOne SIEM/SOC API integration with log forwarding [9, 14, 15].
- **Protocol allowlist enforcement (item 1.3):** OT protocol allowlist/blocklist policy rules with accept or deny actions, with AI-generated baseline allowlists per asset [13, 1].

## 5. Notable Gaps / Risks

- **Fail-open, not fail-close (item 4.4):** the documented fail-safe is hardware bypass that switches to closed bridge mode (short circuit) on crash, hang, or power loss, so traffic continues without inspection; this is the opposite of the fail-close boundary lock the checklist requires [6, 9].
- **No Common Criteria or FIPS product certification (item 5.4):** datasheets list only CE, FCC, VCCI, UL, CISPR and RoHS, and the Common Criteria portal shows no EdgeIPS/TXOne entry; IEC 62443-4-1 covers the development process, not the product [2, 18, 20].
- **Active-standby HA not documented (item 4.3):** failover evidence is qualitative (hardware-bypass switchover), with no documented session-preserving active-standby cluster meeting the <=100 ms requirement [1, 2].
- **Default-deny not explicit (item 1.3):** allowlist/blocklist rules with deny actions are documented, but a blanket default-deny of all non-allowlisted traffic is not stated [13].
- **File-transfer coverage is partial (item 3.1):** HTTP, FTP and SMB downloads are scanned by antivirus profiles, but no SFTP/NFS proxy or content-sanitization capability is documented [12, 10].

## 6. Evidence Quality Notes

All 20 sources were staged and hash-anchored in artifacts/manifest.jsonl: 19 vendor-published (product page, eight datasheets, six help-center documents, EdgeOne page/datasheet/FAQ, IEC 62443 page, blog, press release) and one independent registry (Common Criteria portal). All 56 evidence quotes are grounded verbatim in the staged text (grounding check: 56/56 grounded, 0 fabricated, 0 unverifiable). Because every capability item rests on vendor documentation only, confidence is capped at medium across the board; the single non-vendor source supports the certification verdict on item 5.4. Items 1.3, 2.3, 3.1, 3.2, 3.4, 4.1, 4.2, 4.3, 4.4, 5.1, 5.2, 5.3 and 5.4 each draw on three or more evidence entries across two or more vendor sources; items 1.1, 1.2, 1.5, 2.1, 2.4, 2.5 and 2.7 rely on category-establishing citations (product page and FAQs) for their not-applicable verdicts.

No source contradictions surfaced; the residual risk is vendor-only sourcing, which the exact-quote grounding and the certification-registry cross-check only partially offset. The fail-open behavior behind item 4.4 is stated consistently across datasheets ("Fail Open", "Fail-Open") and FAQs ("closed bridge mode"), so the not_supported verdict reflects documented design rather than absence of evidence. Numeric-threshold items were handled per contract: 4.1 (1800 Mbps, EdgeIPS Pro 212F) and 4.2 (0.5 ms) are supported with exact published numbers, while 4.3 is partial with null numeric_value because only qualitative (sub-microsecond) failover data is published.

---

## Bibliography

[1] TXOne Networks. "EdgeIPS Family – Product Page (TXOne Networks)". https://www.txone.com/products/network-security/edgeips/ (Retrieved: 2026-08-11T09:15:49Z)
[2] TXOne Networks. "EdgeIPS Pro 212F Datasheet". https://www.txone.com/assets/files/42d512f706e40d116ec065f2146012f169c3f44d.pdf (Retrieved: 2026-08-11T09:15:49Z)
[3] TXOne Networks. "EdgeIPS Pro 2016F/4016F Datasheet". https://www.txone.com/assets/files/eeb88dea9a442e514a45765bfc1d33c2b8fa7dbf.pdf (Retrieved: 2026-08-11T09:15:49Z)
[4] TXOne Networks. "EdgeIPS Pro 1048/2096 Datasheet". https://www.txone.com/assets/files/1ea8e25f536f54652b19f74ccac30fe8dfd92a6d.pdf (Retrieved: 2026-08-11T09:15:49Z)
[5] TXOne Networks. "EdgeIPS 103 Datasheet". https://www.txone.com/assets/files/97cfa4216b5f4db68108ac7c2c019612e8a48f8b.pdf (Retrieved: 2026-08-11T09:15:49Z)
[6] TXOne Networks. "EdgeIPS 102 Datasheet". https://www.txone.com/assets/files/baf0aba7232ec1daec26c5a17796acea2c9a576f.pdf (Retrieved: 2026-08-11T09:15:49Z)
[7] TXOne Networks. "EdgeIPS LE 102 Datasheet". https://www.txone.com/assets/files/1525855243e946243caffc1b7de8d16189f47670.pdf (Retrieved: 2026-08-11T09:15:49Z)
[8] TXOne Networks. "EdgeIPS Pro 732 Datasheet". https://www.txone.com/assets/files/53bcb991c382773a32c19db6e71bcab507e0d2ef.pdf (Retrieved: 2026-08-11T09:15:49Z)
[9] TXOne Networks. "FAQs – EdgeIPS Pro (TXOne Help Center)". https://help.txone.com/docs/faqs-edgeips-pro.md (Retrieved: 2026-08-11T09:15:49Z)
[10] TXOne Networks. "FAQs – EdgeIPS (TXOne Help Center)". https://help.txone.com/docs/faqs-edgeips.md (Retrieved: 2026-08-11T09:15:49Z)
[11] TXOne Networks. "How to Configure Inline & Offline Modes for EdgeIPS & EdgeIPS Pro (TXOne Help Center)". https://help.txone.com/docs/how-to-configure-inline-offline-modes-for-edgeips-edgeips-pro.md (Retrieved: 2026-08-11T09:15:49Z)
[12] TXOne Networks. "How to Configure File Exceptions for EdgeIPS Pro Devices (TXOne Help Center)". https://help.txone.com/docs/how-to-configure-file-exceptions-for-edgeips-pro-devices.md (Retrieved: 2026-08-11T09:15:49Z)
[13] TXOne Networks. "How to Configure Policy Enforcement Monitor & Prevention Modes for Edge Series Devices (TXOne Help Center)". https://help.txone.com/docs/how-to-configure-policy-enforcement-monitor-prevention-modes-for-edge-series-devices.md (Retrieved: 2026-08-11T09:15:49Z)
[14] TXOne Networks. "EdgeOne Management Console – Product Page (TXOne Networks)". https://www.txone.com/products/network-security/edgeone/ (Retrieved: 2026-08-11T09:15:49Z)
[15] TXOne Networks. "EdgeOne Datasheet". https://www.txone.com/assets/files/e511b6eb3606bee34f0a6f6577760c131c8609eb.pdf (Retrieved: 2026-08-11T09:15:49Z)
[16] TXOne Networks. "FAQs – EdgeOne (TXOne Help Center)". https://help.txone.com/docs/faqs-edgeone.md (Retrieved: 2026-08-11T09:15:49Z)
[17] TXOne Networks. "ISA/IEC 62443 Compliance for Industrial Security (TXOne Networks)". https://www.txone.com/compliance/isa-iec-62443/ (Retrieved: 2026-08-11T09:15:49Z)
[18] TXOne Networks. "TXOne Networks Achieves IEC 62443-4-1 Certification (TXOne blog)". https://www.txone.com/resources/blog/iec-62443-4-1-certification-ot-secure-development/ (Retrieved: 2026-08-11T09:15:49Z)
[19] TXOne Networks. "TXOne Networks Expands Edge Series of OT-Native Network Security Appliances (press release)". https://www.txone.com/news/txone-expands-edge-series-ot-native-network-security-appliances/ (Retrieved: 2026-08-11T09:15:49Z)
[20] Common Criteria Portal. "Common Criteria Certified Products list (Common Criteria portal)". https://www.commoncriteriaportal.org/products/index.cfm (Retrieved: 2026-08-11T09:15:49Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 20 (kept: 20, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, vendor_blog: 2, vendor_datasheet: 8, vendor_doc: 9
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
