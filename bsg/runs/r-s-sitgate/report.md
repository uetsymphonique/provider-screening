# BSG / Cross Domain Product Assessment: Rohde & Schwarz Cybersecurity (Rohde & Schwarz SIT GmbH) — R&S SITGate

**Product ID:** `r-s-sitgate`
**Version reference:** SITGate Next-Generation Firewall Product Brochure v02.00 (S100/M200/M400/L500/L800, 2014); SIT-Ind flyer 02.00 (2012)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:45:00+00:00
**Total evidence items collected:** 27
**Total distinct sources:** 7

---

## 1. Overview

R&S SITGate is a security gateway product of Rohde & Schwarz Cybersecurity (formerly Rohde & Schwarz SIT GmbH, Berlin). Public documentation - the 2012 SIT product flyer and the 2014 "R&S SITGate Next-Generation Firewall" product brochure - positions it as a next-generation firewall (models S100/M200/M400/L500/L800, 1U/2U rack appliances with 6-16 Ethernet ports) that applies positive application-based validation: traffic is analyzed per transaction and only data that is fully validated and understood is transmitted [1, 2, 4]. Crypto Museum independently describes it as a "secure firewall," formerly a Siemens product [5], and it was still advertised as the "SITGate L500 Next Generation Firewall" in 2015-2016 [6, 7]. The vendor's current website no longer lists SITGate and no current-generation (2020+) documentation could be retrieved, so this assessment reflects the documented 2012-2016 firewall-class product, not a protocol-break guard or data diode.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 0                | 2      | 0   |
| partial          | 3     | 0                | 3      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 12    | 0                | 0      | 12  |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 8 items backed by ≥ 2 source_types; 5 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Vendor documentation positions SITGate as a next-generation firewall and Crypto Museum lists it as a secure firewall (formerly a Siemens product), not a protocol-break guard or data diode; the brochure documents a stateful firewall with application detection rather than session termination with IP routing cut.
- **1.2:** As a firewall-class appliance documented in standard 1U/2U form factors with Ethernet ports, SITGate has no documented dual processing-board design connected via FPGA or isolated shared memory; the two-node guard architecture this item describes is not part of its category.
- **1.5:** SITGate's documented architecture is a firewall that inspects and forwards traffic; no guard-style internal control core that cryptographically stamps clean data before re-initiating sessions is part of that category.
- **2.1:** SITGate is documented as a firewall-class product, so format-level content disarm and reconstruction (CDR) of Office/PDF/image/CAD files is outside its documented function; only inline malware screening of downloaded files in the data stream is described.
- **2.4:** Schema validation of XML/JSON/FIXM/AIXM structures is a guard/CDS-specific capability; SITGate is documented as a firewall-class product and no schema-check function is part of its documented category.
- **2.5:** Filtering based on security labels attached to files is a guard/CDS-specific capability; SITGate is documented as a firewall-class product with user/group-based rules, not security-label (IFC) filtering.
- **2.7:** Anti-steganography detection in image files is a guard/CDS-specific capability; SITGate is documented as a firewall-class product and no image steganography scanning is part of its documented category.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Vendor documentation positions SITGate as a next-generation firewall and Crypto Museum lists it as a secure firewall (formerly a Siemens product), not a protocol-break guard or data diode; the brochure documents a stateful firewall with application detection rather than session termination with IP routing cut. [1], [2], [5], [6], [7] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | As a firewall-class appliance documented in standard 1U/2U form factors with Ethernet ports, SITGate has no documented dual processing-board design connected via FPGA or isolated shared memory; the two-node guard architecture this item describes is not part of its category. [1], [5] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | The vendor describes positive application-based validation in which only data that is fully validated and understood can be transmitted, and documents whitelist/blacklist support with immediate blocking of protocol violations. [1], [2], [3] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No hardening details (hardened OS, microkernel, SELinux strict mode) are documented in the flyer or product brochure.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | SITGate's documented architecture is a firewall that inspects and forwards traffic; no guard-style internal control core that cryptographically stamps clean data before re-initiating sessions is part of that category. [1], [5] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | SITGate is documented as a firewall-class product, so format-level content disarm and reconstruction (CDR) of Office/PDF/image/CAD files is outside its documented function; only inline malware screening of downloaded files in the data stream is described. [1], [3], [5] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No removal of VBA macros, Javascript, DDE links or embedded objects is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | Downloaded documents and files are screened inline for malware using protection based on Bitdefender antimalware technology; parallel scanning with two or more antivirus engines is not documented. [3] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | Schema validation of XML/JSON/FIXM/AIXM structures is a guard/CDS-specific capability; SITGate is documented as a firewall-class product and no schema-check function is part of its documented category. [1], [5] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | Filtering based on security labels attached to files is a guard/CDS-specific capability; SITGate is documented as a firewall-class product with user/group-based rules, not security-label (IFC) filtering. [1], [5] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (HTTPS analysis is described as exposing threats and unauthorized data leaks, but no content-based DLP (keywords, national ID numbers, account numbers, custom regex) is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | Anti-steganography detection in image files is a guard/CDS-specific capability; SITGate is documented as a firewall-class product and no image steganography scanning is part of its documented category. [1], [5] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | TLS/SSL/HTTPS connections can be analyzed despite encryption and downloaded files are screened for malware inline in the data stream; explicit SFTP/FTP/SMB/NFS proxy modes with content cleaning are not documented. [3] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found (No OT/ICS protocol support (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) is documented in the product material reviewed.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No database protocol proxy (SQL Server, Oracle, PostgreSQL) with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | The vendor spec sheet lists UTM throughput (IPS, AV and web filter enabled) of 1 Gbit/s on the M400, 2 Gbit/s on the L500 and 3 Gbit/s on the L800, so the family sustains at least 1 Gbps of real inspection throughput on mid/high models; CDR inspection throughput is not applicable to this firewall class. [4] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No processing latency figures are published in the brochure or spec sheet.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found (No HA active-standby configuration or failover switchover time is documented.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (The product blocks hazardous or unauthorized use and protocol violations, but no explicit fail-close state under DoS/overload is documented.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (Management is documented as a web-browser configuration UI; no separation of system admin / policy admin / auditor roles is documented.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (A reporting feature is mentioned in the brochure, but no SIEM/SOAR integration (CEF/Syslog over TLS) is documented.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No compliance report templates for NIST SP 800-82, IEC 62443 or ISO 27001 are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | — | The vendor states its SIT products have been approved by the German Federal Office for Information Security (BSI); no specific Common Criteria EAL4+ or FIPS 140-3 certificate for SITGate was identified in the public material reviewed. [1] |

---

## 4. Notable Strengths

- **Positive validation / default-deny posture (item 1.3):** SITGate analyzes every network transaction and only transmits data that is fully validated and understood; whitelisting and blacklisting are supported and connections showing protocol violations are blocked immediately [1, 2, 3].
- **Inline content security (items 2.3, 3.1):** Downloaded files are screened for malware in the data stream using Bitdefender-based technology with no file-size restriction, and TLS/SSL/HTTPS traffic can be analyzed despite encryption [3].
- **Inspection throughput headroom (item 4.1):** The mid/high models sustain real inspection (UTM: IPS, AV, web filter enabled) throughput of 1-3 Gbit/s (M400/L500/L800), meeting the >= 1 Gbps requirement on those models [4].
- **Vendor-documented national approval (item 5.4):** Rohde & Schwarz SIT states its products are approved by the German Federal Office for Information Security (BSI); no product-specific Common Criteria certificate was identified in public material [1].

## 5. Notable Gaps / Risks

- **Product availability risk (overall):** SITGate no longer appears on the vendor's website and every located source dates from 2012-2016; buyers should verify current availability, support, and product form before further evaluation.
- **No protocol-break or CDS architecture (items 1.1, 1.2, 2.1):** SITGate is a firewall, not a guard or data diode; deployments requiring session termination at a boundary, dual-board hardware isolation, or content disarm and reconstruction need a different product class.
- **No OT/ICS, database, or realtime-stream protocol support documented (items 3.2, 3.3, 3.4):** OPC UA/Modbus/DNP3 proxies, SQL query-whitelisting proxies, and RTSP/syslog relays are absent from the documented feature set.
- **Latency, HA, and fail-close behavior unspecified (items 4.2, 4.3, 4.4):** no processing-latency figures, HA switchover times, or DoS fail-close behavior are published, so the <= 10 ms and <= 100 ms requirements are unverifiable.
- **Management and integration gaps (items 5.1, 5.2, 5.3):** no RBAC role separation (system/policy/auditor), SIEM/CEF/Syslog integration, or compliance-report templates are documented.

## 6. Evidence Quality Notes

Only 7 distinct sources were collected, of which 6 are vendor-authored or vendor-advertising material (the 2012 flyer, three brochure pages, and two vendor advertisements reproduced in independent publications); Crypto Museum is the sole independent source, used to confirm the product category. No Common Criteria registry entry, analyst report, independent lab test, or third-party deployment reference could be located. Consequently every non-unknown verdict rests on vendor documentation and is capped at medium confidence, and 12 of 24 items are unknown because the documented feature set simply does not cover them.

The dominant limitation is vintage: all evidence dates from 2012-2016 and the product is no longer listed on the vendor's website. Search engines (DuckDuckGo, Bing, Google, Ecosia, Yahoo, Mojeek) blocked automated access from this network and the Wayback Machine returned HTTP 429 for the entire run, so current product pages, newer brochures, and the BSI Common Criteria registry could not be retrieved; a re-run from a different network should re-check product status and certifications before relying on the not_applicable categorization. No contradictions between sources were found - every source consistently describes SITGate as a firewall.

---

## Bibliography

[1] Rohde & Schwarz SIT GmbH. "Protect your know-how - Encryption & IT security by Rohde & Schwarz SIT (flyer, includes R&S SITGate description)". https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_brochures_and_datasheets/pdf_1/SIT-Ind_fly_e.pdf (Retrieved: 2026-08-11T09:20:00Z)
[2] Rohde & Schwarz SIT GmbH. "R&S SITGate Next-Generation Firewall - Product Brochure v02.00, page 2 (At a glance)". https://www.yumpu.com/en/document/view/11199934/rsrsitgate-next-generation-firewall-rohde-schwarz-sit/2 (Retrieved: 2026-08-11T09:20:00Z)
[3] Rohde & Schwarz SIT GmbH. "R&S SITGate Next-Generation Firewall - Product Brochure v02.00, page 4 (Benefits and key features)". https://www.yumpu.com/en/document/view/11199934/rsrsitgate-next-generation-firewall-rohde-schwarz-sit/4 (Retrieved: 2026-08-11T09:20:00Z)
[4] Rohde & Schwarz SIT GmbH. "R&S SITGate Next-Generation Firewall - Product Brochure v02.00, page 6/7 (Specifications in brief)". https://www.yumpu.com/en/document/view/11199934/rsrsitgate-next-generation-firewall-rohde-schwarz-sit/6 (Retrieved: 2026-08-11T09:20:00Z)
[5] Crypto Museum. "Rohde & Schwarz (Crypto Museum manufacturer index, R&S SITGate entry)". https://www.cryptomuseum.com/crypto/rs/index.htm (Retrieved: 2026-08-11T09:20:00Z)
[6] The Security Times / ICCT. "The Security Times - Challenges (February 2016), Rohde & Schwarz advertisement page listing SITGate L500 Next Generation Firewall". https://icct.nl/sites/default/files/import/publication/ST_Feb2016_double_page.pdf (Retrieved: 2026-08-11T09:20:00Z)
[7] Bayernkurier (CSU). "Bayernkurier (February 2015), Rohde & Schwarz advertisement page listing SITGate L500 Next Generation Firewall". https://csu-schweinheim.de/wp-content/uploads/2015/02/Bayernkurier.pdf (Retrieved: 2026-08-11T09:20:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 16
- **Sources reviewed:** 7 (kept: 7, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** pdf: 3, web: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
