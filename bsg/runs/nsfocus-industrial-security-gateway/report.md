# BSG / Cross Domain Product Assessment: NSFOCUS (NSFOCUS Technologies, Inc. / 绿盟科技) — NSFOCUS Industrial Security Gateway (NSFOCUS ISG)

**Product ID:** `nsfocus-industrial-security-gateway`
**Version reference:** NSFOCUS ISG V2.0 per IPv6 Ready Logo registry entry 02-C-002610 (approved 2023-05-03); Chinese product page 绿盟工业防火墙 ISG
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:22:34Z
**Total evidence items collected:** 30
**Total distinct sources:** 4

---

## 1. Overview

The NSFOCUS Industrial Security Gateway (NSFOCUS ISG) is a next-generation industrial firewall and border-protection product for OT networks, positioned by the vendor as an industrial firewall (绿盟工业防火墙 ISG) rather than a cross domain solution; its case studies deploy it as 工业安全网关 (Industrial Security Gateway) [1]. The IPv6 Ready Logo registry independently lists the product as "NSFOCUS Industrial Security Gateway" V2.0, describing it as "a next-generation border protection product specially designed for industrial enterprises" [2, 3]. It performs single-pass deep parsing of industrial protocols (OPC, Modbus, MQTT, DNP3, IEC61850 MMS, Siemens S7, Ethernet IP, IEC104) with simultaneous industrial virus scanning, intrusion prevention, access control, content filtering and DoS protection [1, 2]. Deployment shapes are virtual-wire, transparent and hybrid modes with static/policy routing, SNAT/DNAT and IPsec VPN [1]; the appliance uses industrial-grade, fanless, wide-temperature, redundant-power hardware with hardware redundancy and load balancing [1]. NSFOCUS's guard/isolation architecture lives in a separate product line (SIES security isolation and information exchange system) [4], confirming the ISG is a ruggedized industrial firewall, not a protocol-break guard.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 1                | 1      | 0   |
| partial          | 4     | 0                | 4      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 17    | 0                | 0      | 17  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 2 items backed by ≥ 2 source_types; 5 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | — | The vendor documents static/policy routing, SNAT/DNAT and IPSec VPN on the ISG, so the datapath forwards IP between interfaces rather than terminating every session at the boundary. Protocol-break session termination is therefore absent. [1] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No public documentation describes a dual processing-board design connected via FPGA or isolated shared memory.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | The ISG supports a self-learning industrial-protocol whitelist used as its security policy, with five-tuple filtering and IP-MAC binding. [1] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No public documentation of the underlying OS hardening approach (hardened OS, microkernel or SELinux strict mode).) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No public documentation describes an internal control core that cryptographically stamps clean data before re-initiating sessions.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No public documentation describes content disarm and reconstruction (CDR) of Office, PDF, image or CAD files.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No public documentation describes removal of VBA macros, JavaScript, DDE links or embedded objects from files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | The ISG documents built-in industrial virus scanning/filtering with 9 million-plus virus signatures, and the registry description confirms virus detection, intrusion prevention and content filtering; the number of independent antivirus engines scanning raw payloads is not specified. [1], [2] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No public documentation describes schema validation of XML, JSON, FIXM or AIXM structures.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No public documentation describes information-flow control based on security labels attached to files.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (Only generic content filtering is documented; keyword/regex DLP for secrets, ID numbers or accounts is not specified.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No public documentation describes detection or removal of hidden data in image files (PNG, JPEG, BMP).) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No file-transfer proxy services (SFTP, FTPS, HTTPS, SMB/NFS with content cleaning) documented; only HTTP/FTP/Telnet application-layer access control is listed.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | high | — | The ISG performs deep parsing and value-level control of OPC, Modbus, MQTT, DNP3, IEC61850 MMS, Siemens S7, Ethernet IP and IEC104, and the IPv6 Ready registry independently confirms analysis and control of more than 20 industrial protocols. [1], [2] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No database proxy services (SQL Server, Oracle, PostgreSQL) or query whitelisting documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF relay service documented for the ISG.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | The vendor documents a single-channel parallel-processing architecture that keeps the device stable and efficient at high forwarding rates with all security features enabled, but publishes no numeric throughput figure; the 1 Gbps threshold cannot be confirmed. [1] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No processing/realtime protocol latency figure published for the ISG.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | The vendor documents industrial-grade hardware with redundant power, hardware redundancy and load balancing, and a high-availability feature set on the rail on-board variant, but publishes no active-standby failover switchover time. [1] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | The ISG documents DoS protection alongside intrusion prevention, virus filtering and content filtering; the explicit fail-close boundary behaviour under DoS or overload is not specified. [1] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (No documentation of role separation between system admin, policy admin and security auditor.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (No documentation of CEF/syslog log export over TLS to a SIEM for the ISG.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) documented; the product page targets Chinese 等保2.0 and 工信部 compliance frameworks instead.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | — | no evidence found (Documented approvals are Chinese/railway (公安部 enhanced-grade sales license, State Grid EPRI enhanced test report, EN50155/EN45545, EMC); no Common Criteria (EAL4+), FIPS 140-3 or national crypto certification found, and no NSFOCUS entry appears in the Common Criteria portal product list.) |

---

## 4. Notable Strengths

- **Industrial protocol deep parsing (item 3.2):** deep parsing and value-level control of OPC, Modbus, MQTT, DNP3, IEC61850 MMS, Siemens S7, Ethernet IP and IEC104, independently corroborated by the IPv6 Ready registry entry confirming analysis and control of more than 20 industrial protocols [1, 2].
- **Whitelist-based default-deny (item 1.3):** a self-learning industrial-protocol whitelist serves as the security policy, with five-tuple filtering and IP-MAC binding [1].
- **Built-in threat defense (items 2.3, 4.4):** industrial virus scanning and filtering (9 million-plus signatures), intrusion prevention, content filtering and DoS protection are documented on the vendor page and in the registry description [1, 2].
- **Industrial-grade hardware and HA features (item 4.3):** fanless, wide-temperature, redundant-power design with hardware redundancy, load balancing and soft/hardware bypass, plus a high-availability feature set on the rail on-board variant [1].
- **Flexible deployment (supporting item 3.2 context):** virtual-wire, transparent and hybrid modes with static/policy routing, SNAT/DNAT and IPsec VPN for OT boundary insertion [1].

## 5. Notable Gaps / Risks

- **No numeric throughput or latency figures (items 4.1, 4.2):** the vendor publishes only qualitative performance language ("high forwarding rates with all security features enabled"), so the 1 Gbps throughput and 10 ms latency requirements are unverified; resolving this requires the product datasheet or admin guide [1].
- **No active-standby switchover time (item 4.3):** hardware redundancy, load balancing and high-availability features are documented, but the <=100 ms session-preserving failover target is not quantified [1].
- **Management-layer capabilities undocumented (items 5.1, 5.2, 5.3):** role separation between system/policy/auditor admin, CEF/syslog export over TLS to a SIEM, and NIST SP 800-82 / IEC 62443 / ISO 27001 report templates are not described in the public sources; the product page instead targets Chinese 等保2.0 and 工信部 compliance frameworks.
- **Certification set does not match the checklist (item 5.4):** documented approvals are Chinese/railway (公安部 enhanced-grade sales license, State Grid EPRI enhanced test report, EN50155/EN45545, EMC) [1]; no Common Criteria EAL4+, FIPS 140-3 or national crypto certification was found, and no NSFOCUS entry appears in the Common Criteria portal product list.
- **Fail-close semantics unspecified (item 4.4):** DoS protection is documented, but the explicit fail-close boundary behaviour under DoS or overload is not described [1].

## 6. Evidence Quality Notes

Four sources were staged: two vendor pages (the ISG product page [1] and the SIES product page [4]) and two independent IPv6 Ready Logo registry artifacts (the ISG's logo entry 02-C-002610 [2] and the vendor-wide approved-list search [3]). Items 2.3 and 3.2 are triangulated across at least two source types (vendor_doc + certification_registry), while items 1.1, 1.3, 4.1, 4.3 and 4.4 rest on vendor documentation alone, so confidence is capped at medium for them; only item 3.2 reaches high confidence because the independent registry directly corroborates the 20-plus protocol claim [1, 2]. The registry entry independently confirms the exact product name ("NSFOCUS Industrial Security Gateway"), version V2.0, the approval date (2023-05-03) and the product's category, and no contradiction between the vendor page and the registry surfaced. The assessment likely understates items 1.4, 4.2, 5.1, 5.2, 5.3 and 5.4, where the vendor's admin guide or datasheet (not publicly accessible: bbs.nsfocus.com requires SSO login and nsfocusglobal.com is Cloudflare-protected, with the Wayback Machine rate-limiting this environment) would contain the relevant figures. All 30 evidence quotes were verified verbatim against the staged artifact texts (30/30 grounded).

---

## Bibliography

[1] NSFOCUS (绿盟科技). "绿盟工业防火墙 ISG - 工业互联网安全产品 (NSFOCUS Industrial Firewall ISG product page)". https://www.nsfocus.com.cn/html/2019/199_1008/59.html (Retrieved: 2026-08-11T09:22:34Z)
[2] IPv6 Forum / IPv6 Ready Logo Committee. "IPv6 Ready Logo Program - Approved List - Logo 02-C-002610 (NSFOCUS Industrial Security Gateway V2.0)". https://www.ipv6ready.org/db/index.php/public/logo/02-C-002610/ (Retrieved: 2026-08-11T09:22:34Z)
[3] IPv6 Forum / IPv6 Ready Logo Committee. "IPv6 Ready Logo Program Approved List - search results for vendor NSFOCUS". https://www.ipv6ready.org/db/index.php/public/search/?vn=NSFOCUS&do=1 (Retrieved: 2026-08-11T09:22:34Z)
[4] NSFOCUS (绿盟科技). "绿盟安全隔离与信息交换系统 SIES (NSFOCUS Security Isolation and Information Exchange System product page)". https://www.nsfocus.com.cn/html/2020/197_0102/101.html (Retrieved: 2026-08-11T09:22:34Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 4 (kept: 4, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, vendor_doc: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
