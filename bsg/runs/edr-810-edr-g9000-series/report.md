# BSG / Cross Domain Product Assessment: Moxa Inc. — EDR-810 / EDR-G9000 Series (EDR-810, EDR-G902, EDR-G903 industrial secure routers)

**Product ID:** `edr-810-edr-g9000-series`
**Version reference:** EDR-810 firmware v5.12.x; EDR-G902/G903 firmware v5.7.x; datasheets updated Jun 27, 2025; Industrial Secure Router User's Manual Edition 4.0 (April 2018)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:20:00Z
**Total evidence items collected:** 53
**Total distinct sources:** 12

---

## 1. Overview

The EDR-810, EDR-G902 and EDR-G903 are Moxa's industrial secure routers: all-in-one firewall/NAT/VPN devices that combine a stateful inspection firewall, VPN (IPsec, OpenVPN, L2TP), routing, and - on the EDR-810 - a managed Layer 2 switch, for protecting remote control and monitoring networks in water, oil and gas, and factory automation applications [1][2]. Moxa positions the family as firewall/VPN secure routers providing an electronic security perimeter for critical cyber assets, not as cross-domain guards or protocol-break devices [2][1]. The family supports Modbus TCP/UDP deep packet inspection and Quick Automation Profile filtering for common fieldbus protocols including IEC 60870-5-104, DNP, EtherNet/IP, PROFINET, EtherCAT, FOUNDATION Fieldbus and LonWorks [1][2][3][4]. All three series are end-of-life: Moxa's product pages list the EDR-8010, EDR-G9004 and EDR-G9010 series as replacements [5][6][7]. Deployment shapes are DIN-rail mounted industrial routers with dual DC power inputs and wide-temperature (-40 to 75 C) variants, typically placed at the IT/OT boundary or between remote sites over public networks [1][3].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 0     | 0                | 0      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 11 items backed by ≥ 2 source_types; 15 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Moxa positions the EDR-810, EDR-G902 and EDR-G903 as all-in-one industrial firewall/NAT/VPN secure routers for Ethernet networks; no TCP/IP session-termination protocol-break architecture is described.
- **1.2:** The devices are documented as industrial secure routers with firewall/NAT/VPN functionality in one unit; no dual processing board or FPGA/shared-memory isolation design is described.
- **1.5:** No internal cryptographic stamping of cleaned data before session re-initiation is described; the product is documented as a firewall/VPN router, not a guard.
- **2.1:** No content disarm and reconstruction (CDR) of Office/PDF/image/CAD files is documented; the product is documented as a firewall/VPN router.
- **2.4:** No XML/JSON/FIXM/AIXM schema validation is documented; the product is documented as a firewall/VPN router rather than a data-sanitizing guard.
- **2.5:** No security-label-based information flow control on files is documented; the product is documented as a firewall/VPN router.
- **2.7:** No anti-steganography detection/removal for image files is documented; the product is documented as a firewall/VPN router.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Moxa positions the EDR-810, EDR-G902 and EDR-G903 as all-in-one industrial firewall/NAT/VPN secure routers for Ethernet networks; no TCP/IP session-termination protocol-break architecture is described. [1], [2] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The devices are documented as industrial secure routers with firewall/NAT/VPN functionality in one unit; no dual processing board or FPGA/shared-memory isolation design is described. [1], [2], [3] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | A stateful inspection firewall with ordered whitelist/blacklist policies and Accept/Drop actions is documented; a global default-deny for traffic not matching any policy is not explicitly stated. [1], [2] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (Vendor documentation does not describe a hardened OS, microkernel, or SELinux strict mode; NVD and Cisco Talos record past web-server command-injection (CVE-2017-12120) and DoS (CVE-2023-4452) vulnerabilities that were fixed in later firmware.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | No internal cryptographic stamping of cleaned data before session re-initiation is described; the product is documented as a firewall/VPN router, not a guard. [1], [2] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | No content disarm and reconstruction (CDR) of Office/PDF/image/CAD files is documented; the product is documented as a firewall/VPN router. [1], [2] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No macro/script removal capability (VBA, JavaScript, DDE links, embedded objects) is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No multi-engine antivirus scanning of raw payloads is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | No XML/JSON/FIXM/AIXM schema validation is documented; the product is documented as a firewall/VPN router rather than a data-sanitizing guard. [1], [2] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label-based information flow control on files is documented; the product is documented as a firewall/VPN router. [1], [2] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No DLP keyword/regex detection for confidential identifiers is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No anti-steganography detection/removal for image files is documented; the product is documented as a firewall/VPN router. [1], [2] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (FTP/HTTP are among the firewall Quick Automation Profiles and FTP NAT ALG is documented, but no content-cleaning file-transfer proxy (SFTP/SMB/NFS) is documented.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | Modbus TCP/UDP deep packet inspection (function-code, UID, and address level) and Quick Automation Profile filtering for IEC 60870-5-104, DNP, EtherNet/IP, PROFINET, EtherCAT, FOUNDATION Fieldbus and LonWorks are documented; the documented protocol set does not include OPC UA or MQTT. [1], [2], [3], [4] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server/Oracle/PostgreSQL database proxy or query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or unidirectional/bidirectional syslog/CEF relay is documented; the device only forwards its own event logs to syslog servers.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Not Supported | medium | 500 Mbps | Datasheets list maximum firewall throughput of 100 Mbps (EDR-810), 300 Mbps (EDR-G902) and 500 Mbps (EDR-G903); the family top-end of 500 Mbps is below the 1 Gbps requirement. [1], [3], [4] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No firewall/VPN processing latency figures are published.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | VRRP-based active/standby redundancy is documented with advertisement interval and preemption delay configured in seconds; no sub-100 ms switchover time is specified. [2] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | DoS/DDoS defense is documented (SYN-flood, ICMP-death, Xmas/NULL scan detection with packet-rate limits that drop abnormal packets); a fail-close lockdown of the entire boundary under DoS is not described. [1], [2], [3] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Two configuration access levels are documented (admin read/write, user read-only) with login/password policy and RADIUS authentication; the three-role system-admin/policy-admin/auditor separation is not provided. [2] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Real-time firewall/VPN/system events are forwarded to up to three syslog servers as UDP packets (default port 514) or to SNMP trap servers; CEF format or TLS-encrypted syslog transport is not documented. [1], [2], [3] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | Documented certifications (UL 508, ATEX/Class I Division 2, DNV/DNV-GL, NEMA TS2, EN 50121-4, IEC 61850-3, IEC 61162-460) do not include Common Criteria EAL4+, FIPS 140-3, or a national cryptographic certification. [1], [3], [4] |

---

## 4. Notable Strengths

- **Industrial-protocol-aware firewall (item 3.2):** Modbus TCP/UDP deep packet inspection at function-code, UID and address level, plus Quick Automation Profiles for IEC 60870-5-104, DNP, EtherNet/IP, PROFINET, EtherCAT, FOUNDATION Fieldbus and LonWorks, give the family genuinely OT-specific filtering [1][2][3][4].
- **Stateful firewall with whitelist/blacklist policies (item 1.3):** ordered Accept/Drop policies per interface direction, with event logging to flash, syslog or SNMP trap, let operators control which fieldbus and IT traffic crosses the boundary [1][2].
- **DoS/DDoS defense (item 4.4):** built-in SYN-flood, ICMP-death, Xmas/NULL scan detection with configurable packet-rate limits drops abnormal packets and activates defense when traffic conditions are abnormal [2][1][3].
- **VRRP redundancy and IPsec VPN (item 4.3):** VRRP active/standby with interface and object-ping tracking, plus IPsec up to AES-256/SHA-256 with X.509 certificates (up to 100 tunnels on the EDR-G903), supports dual-WAN deployments [2][4].
- **Ruggedized and sector certifications (item 5.4 context):** wide-temperature models with UL 508, ATEX/Class I Division 2, DNV/DNV-GL, EN 50121-4, IEC 61850-3 (EDR-G903) and IEC 61162-460 (EDR-810) compliance suit industrial, maritime, rail and substation environments [1][3][4].

## 5. Notable Gaps / Risks

- **Throughput below requirement (item 4.1):** maximum firewall throughput is 500 Mbps (EDR-G903), 300 Mbps (EDR-G902) and 100 Mbps (EDR-810), under the 1 Gbps threshold [1][3][4].
- **HA switchover not shown sub-100 ms (item 4.3):** VRRP is documented with second-granularity advertisement intervals and preemption delay; no session-preserving failover time is claimed [2].
- **Vulnerability history on the web server (item 1.4 context):** CVE-2017-12120 (command injection to root shell, disclosed by Cisco Talos), CVE-2020-28144 and CVE-2023-4452 (remote DoS/reboot) affected the family; fixes shipped in firmware v5.12.29 (EDR-810) and v5.7.21 (EDR-G902/G903) [8][9][10][11].
- **End-of-life status (item 1.1 context):** all three assessed series are phased out and replaced by EDR-8010 / EDR-G9004 / EDR-G9010, which constrains the future security-patching runway for new deployments [5][6][7].
- **No content-security capabilities documented (items 2.2, 2.3, 2.6, 3.1):** macro/script removal, multi-engine AV scanning, DLP, and content-cleaning file-transfer proxies are not documented in the vendor materials reviewed; these items are rated unknown [2].

## 6. Evidence Quality Notes

Of the 24 items, 11 are backed by at least two source types (datasheet plus manual, and for item 3.2 across all three datasheets), while the remaining verdict items rely on a single source type. Capability claims rest entirely on vendor documentation - datasheets v1.7 (EDR-810), v1.2 (EDR-G902), v1.3 (EDR-G903) and the shared Industrial Secure Router User's Manual Edition 4.0 - so confidence is capped at medium per the validator rule; no independent lab tests, analyst reports, or third-party spec reviews of throughput, latency or failover were obtainable (most search engines blocked automated access during this run). The vulnerability history is independently corroborated by the NVD [8] and Cisco Talos [9], cross-checked against Moxa's own advisories MPSA-234880 [10] and MPSA-201002 [11]; the IEC 62443-4-2 press release [12] concerns the successor EDR-G9010/TN-4900 models and is used only as context, never as evidence for the assessed series.

No contradictions were found among the sources: the manual and the three datasheets are consistent (the EDR-G902 and EDR-G903 manuals are byte-identical), and the product pages [5][6][7] agree on end-of-life status. Items rated unknown - 1.4 (hardened OS), 2.2, 2.3, 2.6 (content security), 3.1, 3.3, 3.4 (protocol proxies), 4.2 (latency), 5.3 (compliance reports) - reflect genuine absence of published information rather than evaluated absence; the gaps text on each row records what specifically was sought and not found.

---

## Bibliography

[1] Moxa Inc.. "EDR-810 Series Datasheet (v1.7)". https://cdn-cms-frontdoor-dfc8ebanh6bkb3hs.a02.azurefd.net/getmedia/5524a8f4-ea5a-4adb-8a26-433c92316101/moxa-edr-810-series-datasheet-v1.7.pdf (Retrieved: 2026-08-11T08:56:18Z)
[2] Moxa Inc.. "Industrial Secure Router User's Manual (Edition 4.0, April 2018) - covers EDR-810, EDR-G902, EDR-G903". https://cdn-cms-frontdoor-dfc8ebanh6bkb3hs.a02.azurefd.net/getmedia/a42ef5fd-5103-4efd-99b8-2991b1f9e339/moxa-edr-810-series-manual-v4.0.pdf (Retrieved: 2026-08-11T08:56:47Z)
[3] Moxa Inc.. "EDR-G902 Series Datasheet (v1.2)". https://cdn-cms-frontdoor-dfc8ebanh6bkb3hs.a02.azurefd.net/getmedia/5ff4286e-5332-4ec1-8288-84fc97ac0edc/moxa-edr-g902-series-datasheet-v1.2.pdf (Retrieved: 2026-08-11T08:56:34Z)
[4] Moxa Inc.. "EDR-G903 Series Datasheet (v1.3)". https://cdn-cms-frontdoor-dfc8ebanh6bkb3hs.a02.azurefd.net/getmedia/bc2fc0ee-164c-4dc9-a8d0-6c302d4c7f4e/moxa-edr-g903-series-datasheet-v1.3.pdf (Retrieved: 2026-08-11T08:56:34Z)
[5] Moxa Inc.. "EDR-810 Series - Secure Routers (product page)". https://www.moxa.com/en/products/industrial-network-infrastructure/secure-routers/secure-routers/edr-810-series (Retrieved: 2026-08-11T08:57:01Z)
[6] Moxa Inc.. "EDR-G902 Series - Secure Routers (product page)". https://www.moxa.com/en/products/industrial-network-infrastructure/secure-routers/secure-routers/edr-g902-series (Retrieved: 2026-08-11T08:57:19Z)
[7] Moxa Inc.. "EDR-G903 Series - Secure Routers (product page)". https://www.moxa.com/en/products/industrial-network-infrastructure/secure-routers/secure-routers/edr-g903-series (Retrieved: 2026-08-11T08:57:19Z)
[8] NIST National Vulnerability Database. "NVD API - CVE search for 'EDR-810' (21 results incl. CVE-2017-12120, CVE-2020-28144, CVE-2023-4452)". https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=EDR-810&resultsPerPage=50 (Retrieved: 2026-08-11T09:01:12Z)
[9] Cisco Talos Intelligence Group. "TALOS-2017-0472: Moxa EDR-810 Web Server ping Command Injection Vulnerability (CVE-2017-12120)". https://www.talosintelligence.com/vulnerability_reports/TALOS-2017-0472 (Retrieved: 2026-08-11T09:07:57Z)
[10] Moxa Inc.. "MPSA-234880: EDR-810/G902/G903 Series Web Server Buffer Overflow Vulnerability (CVE-2023-4452)". https://www.moxa.com/en/support/product-support/security-advisory/mpsa-234880-edr-810-g902-g903-series-web-server-buffer-overflow-vulnerability (Retrieved: 2026-08-11T09:01:19Z)
[11] Moxa Inc.. "MPSA-201002: EDR-G903, EDR-G902, and EDR-810 Secure Router Vulnerability (CVE-2020-28144)". https://www.moxa.com/en/support/support/security-advisory/edr-g903-g902-810-secure-router-vulnerability (Retrieved: 2026-08-11T09:08:13Z)
[12] Moxa Inc.. "Moxa Achieves World's First IEC 62443-4-2 Certification for Industrial Secure Routers (press release, Sep 2023)". https://www.moxa.com/en/about-us/news-events/news/2023/moxa-achieves-world-s-first-iec-62443-4-2-certification-for-industrial-secure-routers (Retrieved: 2026-08-11T09:08:08Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 9
- **Sources reviewed:** 12 (kept: 12, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 4, web: 8
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
