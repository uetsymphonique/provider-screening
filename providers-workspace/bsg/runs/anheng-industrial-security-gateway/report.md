# BSG / Cross Domain Product Assessment: DBAPPSECurity (杭州安恒信息技术股份有限公司, Hangzhou Anheng Information Technology Co., Ltd.) - Anheng Industrial Security Gateway (安恒工业防火墙 / DBAPPSECurity Industrial Firewall)

**Product ID:** `anheng-industrial-security-gateway`
**Version reference:** Industrial Firewall appliance family (models 1004 DIN-rail / 1006 / 2006 rack per third-party listing); product manual edition 2025 (安恒信息产品手册); product page accessed 2026-08-11
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:17:04Z
**Total evidence items collected:** 38
**Total distinct sources:** 5

---

## 1. Overview

The product under review is DBAPPSECurity's (Hangzhou Anheng Information Technology Co., Ltd.) industrial boundary gateway, marketed in Chinese as 工业防火墙 (Industrial Firewall) and matching the "Anheng Industrial Security Gateway" entry in the screening list. The vendor positions it as a boundary-protection security device for industrial control networks (ICS/IIoT) that combines software and hardware, with explicit deployment shapes including isolation between the MES layer and the office information network (工控网络和信息网络边界隔离), isolation between different networks, between control-zone regions, and in front of critical control devices such as PLC/DCS/RTU [1], [3]. Architecturally it is a firewall-class product - stateful inspection combined with deep packet inspection (DPI), supporting routing, transparent and mixed deployment modes, VLAN, and IPv4/IPv6 dual stack [1] - not a protocol-break cross domain guard; the vendor also markets a separate industrial isolation-and-information-exchange system (工业网闸) for data-exchange between different security levels [2].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 14    | 0                | 0      | 14  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 1 items backed by ≥ 2 source_types; 10 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | - | Vendor documentation states the firewall supports routing and transparent (bridge) deployment modes using stateful inspection plus DPI for access control -- an affirmative pass-through/forwarding datapath that excludes a protocol-break architecture terminating TCP/IP sessions at the boundary. [1] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (Internal board architecture is not published in reviewed vendor documentation.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | Vendor documents both blacklist and whitelist access-control modes with instruction-level filtering that intercepts illegal operation commands, so whitelist (default-deny) enforcement is available. [1], [3] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | - | no evidence found (Hardened-OS details are not published in the reviewed product page, product manual or knowledge-center article.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (Internal data-stamping mechanism is not published in reviewed vendor documentation.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (CDR capability is not published in reviewed vendor documentation.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (Macro/script-stripping is not documented for this product.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | - | Vendor documents a built-in industrial ISP rule library with industrial-protocol virus filtering and an AV capability; the number of concurrently running antivirus engines is not specified. [1], [2], [3] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (Schema-validation capability is not published in reviewed vendor documentation.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (IFC/label-based filtering is not published in reviewed vendor documentation.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | - | Vendor capability map lists keyword filtering and file filtering on the firewall; specific sensitive-data patterns (confidential keywords, ID numbers, accounts) and custom regex rules are not documented. [2] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (Anti-steganography capability is not published in reviewed vendor documentation.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Vendor capability map lists HTTP(s) and FTP among protocols the firewall parses, with file and keyword filtering; SFTP and SMB/NFS proxy with content cleaning are not documented. [2] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | Vendor documents deep parsing of OPC, MODBUS/TCP, IEC104 (IEC 60870-5-104), DNP3, S7 and Ethernet/IP at instruction/address/range level; OPC UA and MQTT industrial proxy are not explicitly documented for this product. [1], [2], [3], [5] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | - | Vendor lists SQL among protocols the firewall recognizes in its capability map; database-proxy operation with query whitelisting (SQL Server/Oracle/PostgreSQL) is not documented. [2] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | - | no evidence found (Realtime-stream protocol support is not published in reviewed vendor documentation.) |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | - | no evidence found (Vendor publishes no Mbps throughput for this product (interface speeds are not inspection throughput).) |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No latency figure (ms) located.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Vendor documents active-standby hot standby with redundant power and BYPASS; no failover switchover time is published. [1], [2], [3] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | Vendor documents anomalous-packet defense, attack protection and self-protection capabilities; explicit fail-close behavior under DoS is not documented (documented hardware-fault BYPASS is fail-open). [1], [2], [3] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (Administration role model is not published in reviewed vendor documentation.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Vendor capability map lists SIEM (with situational-awareness and big-data platforms) as log-integration destinations and the management platform collects logs centrally; CEF/syslog-over-TLS transport is not explicitly documented. [1], [2] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (Compliance-report templates not documented in reviewed sources.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | - | no evidence found (Only company-level industrial-security credentials appear on the vendor solution page (industrial info-security testing/assessment agency capability certificate (Level 3); industrial info-security emergency-service support unit certificate); no product certification registry entry found.) |

---

## 4. Notable Strengths

- **Whitelist default-deny with instruction-level enforcement (item 1.3):** the firewall supports black/whitelist access-control modes and its instruction-level filtering intercepts illegal operation commands and unknown device access, giving whitelist (default-deny) posture [1], [3].
- **Deep industrial protocol parsing (item 3.2):** OPC, Modbus TCP, IEC 60870-5-104, DNP3, S7 and Ethernet/IP are parsed in real time down to instruction, address-range and value-range granularity [1], [2], [3].
- **Industrial-hardened inspection features (items 2.3, 4.4):** a built-in industrial ISP rule library provides industrial-protocol virus filtering, IP/MAC binding, attack protection, anomalous-packet defense and self-protection [1], [2].
- **High-availability design (item 4.3):** redundant power, software/hardware-fault BYPASS, dual-machine hot standby and load balancing are documented for business continuity [1], [2], [3].
- **Content inspection hooks (item 2.6):** the capability map includes URL, file and keyword filtering, providing basic content-level inspection on top of ACL/NAT/routing functions [2].

## 5. Notable Gaps / Risks

- **No published throughput figure (item 4.1):** the vendor publishes no Mbps processing-throughput number for the industrial firewall, so the >= 1000 Mbps requirement cannot be verified; a datasheet or independent lab test would resolve this.
- **No published latency figure (item 4.2):** no realtime-protocol processing latency (ms) is documented anywhere in the reviewed sources.
- **HA failover time unquantified (item 4.3):** dual-machine hot standby is documented but the <= 100 ms switchover requirement is not addressed; the vendor states no session-preservation or switchover timing.
- **No product-level certification located (item 5.4):** no Common Criteria, FIPS 140-3 or national commercial-cryptography certification entry was found for the industrial firewall - only company-level industrial-security credentials (testing/assessment agency capability certificate Level 3, emergency-service support unit certificate) [4]; a certification registry entry or vendor certificate statement would close this.
- **Several management/compliance items undocumented (items 5.1, 5.3):** RBAC role separation and compliance-report templates (NIST SP 800-82, IEC 62443, ISO 27001) are not covered in any reviewed vendor documentation; SIEM forwarding transport (CEF/syslog over TLS, item 5.2) is also only implied by the capability map [2].

## 6. Evidence Quality Notes

Four items were triangulated across three or more sources (2.3, 3.2, 4.3, 4.4; 3.2 across four), while the rest rest on one or two sources; all 38 evidence quotes were verified as exact substrings of the staged artifacts by verify_citation_grounding.py (0 fabricated, 0 unverifiable). Every cited source is vendor-authored: the product page, the official product manual PDF (industrial firewall section), the vendor knowledge-center article, and one B2B marketplace listing (afzhan.com / 智慧城市网) that mirrors vendor-provided text and is tagged vendor_datasheet. No independent test-lab report, analyst note, or certification-registry entry for this product could be located - general search engines were bot-blocked in this environment and only a reader proxy over DuckDuckGo returned results - so confidence is capped at medium on all non-unknown items per the vendor-only rule.

The sources did not contradict each other; the marketplace mirror reproduces the vendor's own wording. The main evidence limitation is the absence of quantitative data (throughput, latency, failover time) and of any product-level certification statement, which forced unknown verdicts on 4.1, 4.2, 5.4 and several management items. Item 1.1 (protocol-break architecture) was rated not_supported because the vendor documentation states the firewall supports routing and transparent deployment modes with stateful inspection + DPI access control [1], a pass-through datapath that contradicts session-terminating protocol break; the remaining guard-specific items (1.2, 1.5, 2.1, 2.4, 2.5, 2.7) were rated unknown because the same documentation establishes the firewall category but states no specific fact for or against those capabilities. The product's Chinese documentation is the authoritative source and was quoted verbatim.

---

## Bibliography

[1] 杭州安恒信息技术股份有限公司 (DBAPPSECurity). "工业防火墙（Industrial Firewall）- 产品页". https://www.dbappsecurity.com.cn/product/cloud141.html (Retrieved: 2026-08-11T09:16:27Z)
[2] 杭州安恒信息技术股份有限公司 (DBAPPSECurity). "安恒信息产品手册（工业防火墙章节，第90页）". https://www.dbappsecurity.com.cn/ajax/download.aspx?id=122473&name=59714E0AFAFDE0D6183C74C813EBA6BE (Retrieved: 2026-08-11T09:16:27Z)
[3] 杭州安恒信息技术股份有限公司 (DBAPPSECurity). "知识中心：工业防火墙（守护工业控制系统的安全防线）". https://www.dbappsecurity.com.cn/content/details6068_122689.html (Retrieved: 2026-08-11T09:16:27Z)
[4] 杭州安恒信息技术股份有限公司 (DBAPPSECurity). "工业信息安全解决方案（荣誉资质）". https://www.dbappsecurity.com.cn/solution/index674.html (Retrieved: 2026-08-11T09:16:27Z)
[5] 杭州安恒信息技术股份有限公司 (via afzhan.com / 智慧城市网). "工业防火墙 - 杭州安恒信息技术股份有限公司（智慧城市网/环保在线商铺产品页）". https://www.afzhan.com/st212942/product_12453005.html (Retrieved: 2026-08-11T09:16:27Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 5 (kept: 5, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** vendor_datasheet: 1, vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
