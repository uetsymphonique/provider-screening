# BSG / Cross Domain Product Assessment: Phoenix Contact GmbH & Co. KG - FL MGUARD Industrial Security Gateway (FL MGUARD Security-Router family)

**Product ID:** `fl-mguard-industrial-gateway`
**Version reference:** FL MGUARD Security-Router family: 2102 (1357828), 2105 (1357850), 4102 PCI (1441187), 4102 PCIE (1357842), 4302 (1357840), 4305 (1357875); firmware 10.5.x per TUV Rheinland certificate 968/CSP 1029.00/25; IEC 62443-4-2 security manual um_de/en_mguard_62443-4-2; catalog pages/datasheet retrieved 2026-08-11
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:40:00Z
**Total evidence items collected:** 35
**Total distinct sources:** 13

---

## 1. Overview

FL MGUARD is Phoenix Contact's industrial security router family: DIN-rail appliances combining a stateful-inspection firewall, IPsec VPN, NAT and routing for IT/OT network segmentation and secure remote maintenance [4, 12]. The current line (FL MGUARD 2102/2105, 4102 PCI/PCIE, 4302, 4305) is documented on the vendor's catalog pages as "Security-Router" products with 10/100/1000 Mbps Ethernet ports, an SD-card slot and an extended temperature range; the FL MGUARD Device Manager (DM) software provides central device management [4, 10]. Phoenix Contact positions the family as industrial firewalls/security routers rather than protocol-break cross-domain guards: the vendor category page describes "security routers and industrial firewalls" that allow only wanted traffic [12], and an independent open-source tool description calls the mGuard series "a family of firewall/router devices" [9]. The seven guard/CDS-specific checklist items (1.1, 1.2, 1.5, 2.1, 2.4, 2.5, 2.7) are therefore scored not_supported where the documented firewall/router datapath logically excludes the capability (1.1, 1.5) and unknown where the reviewed sources simply do not document it (1.2, 2.1, 2.4, 2.5, 2.7). Certifications found include IEC 62443-4-2 (TUV Rheinland certificate 968/CSP 1029.00/25) and UL 61010-1/2-201 [7, 8]; no Common Criteria, FIPS 140-3, or national cryptographic certification was found.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 1                | 0      | 0   |
| partial          | 4     | 0                | 4      | 0   |
| not_supported    | 3     | 0                | 3      | 0   |
| unknown          | 16    | 0                | 0      | 16  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 1 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | - | Vendor documents the FL MGUARD 2102 as a 'Simple stateful inspection firewall' security router; an independent tool description calls the mGuard series 'a family of firewall/router devices'. A firewall/router forwards traffic at the network layer rather than terminating sessions in a protocol-break architecture. [4], [9] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No documentation of the processing-board architecture or FPGA/shared-memory isolation was found; being a stateful-inspection firewall/router does not establish whether dual processing boards exist.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | - | A CERT@VDE advisory states the incoming IPv4 packet filter 'blocks all incoming traffic by default', and the vendor describes allowing only wanted data traffic while blocking unauthorized access attempts, with IP-spoofing, DoS and SYN-flood protection. [1], [4], [12] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | - | no evidence found (No hardened-OS, microkernel or SELinux-strict-mode documentation was found; NVD/CERT@VDE records show vulnerabilities in the web-based management of older firmware (e.g. CVE-2022-3480), but absence of hardening documentation alone drives the unknown verdict.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Not Supported | medium | - | FL MGUARD is documented as a stateful-inspection firewall/security router that forwards and filters traffic rather than terminating sessions; with no protocol-break session re-initiation, there is no internal control core that signs clean data before a new session. [4], [9] |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No content disarm and reconstruction (CDR) of Office, PDF, image or CAD files is documented; the documented function set is packet/flow-level firewall filtering, which does not establish CDR absence.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No macro/script removal or file-sanitization capability for VBA, JavaScript, DDE or embedded objects is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No multi-engine antivirus scanning of payloads is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No W3C-schema validation of XML/JSON/FIXM/AIXM structures is documented; the documented filtering is by MAC/IP address, port and protocol.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label-based information flow control on files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No DLP capability (secret keywords, identity numbers, account data, custom regex) is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography detection/removal for image files (PNG, JPEG, BMP) is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | - | no evidence found (No file-transfer protocol proxy with content cleaning (SFTP, FTP/S, HTTPS, SMB/NFS) is documented; IPsec VPN tunnels carry arbitrary TCP/UDP traffic.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | - | no evidence found (Vendor documents filtering by MAC and IP addresses, ports and protocols, but no OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT application-layer proxy is described in the staged sources.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No SQL Server, Oracle or PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | - | no evidence found (Remote syslog logging to an external server is documented, but no RTSP video proxy or syslog/CEF unidirectional/bidirectional relay function is described.) |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Not Supported | medium | 940 Mbps | Vendor datasheets document maximum firewall throughput of 940 Mbps (router mode, default firewall rules, unidirectional) for both FL MGUARD 2102 and 4305, below the 1,000 Mbps threshold; 'Gigabit wire speed' in the product description refers to the 1 Gbps port speed. [4], [5], [6] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No packet/application processing latency figure is documented.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | - | no evidence found (No device-level HA or active/standby failover is documented; the 4305 page notes only a redundant DC power supply input.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | Vendor documents DoS and SYN-flood protection for incoming traffic and states unauthorized access attempts are blocked; a CERT@VDE advisory records a management-interface DoS in firmware below 8.9.0, and explicit fail-close behavior of the data path under overload is not documented. [2], [4], [12] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | - | A CERT@VDE advisory documents Admin and Super Admin roles in the web-based management with different access rights (an Admin cannot access LDAP settings); a distinct Auditor role is not documented. [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | The 2102 page documents remote syslog logging to an external server and the Device Manager provides central device management; encrypted CEF/Syslog transport to a SIEM is not documented. [3], [4], [10] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | - | FL MGUARD is product-certified to IEC 62443-4-2 under TUV Rheinland certificate 968/CSP 1029.00/25 with an IEC 62443-4-1 development process, plus UL 61010-1/2-201 approval; no Common Criteria, FIPS 140-3 or national cryptographic certification was found in the cited sources. [4], [6], [7], [8], [11] |

---

## 4. Notable Strengths

- **Default-deny firewall (item 1.3):** The incoming IPv4 packet filter blocks all incoming traffic by default, with allowlist-style operation and DoS/SYN-flood protection [1, 4, 12].
- **Vendor-documented security certification (items 5.4, 1.3):** Product certified to IEC 62443-4-2 by TUV Rheinland (968/CSP 1029.00/25) under an IEC 62443-4-1 development process, plus UL 61010-1/2-201 approval [7, 8, 11].
- **VPN-based remote maintenance (items 3.1, 1.1):** IPsec VPN with up to 250 tunnels on the 4305, X.509v3/RSA/PSK authentication and AES-128/192/256 encryption, used with mGuard Secure Cloud for field remote servicing [5, 6, 9].
- **Central management and logging (items 5.2, 5.1):** Remote syslog logging to external servers and the Device Manager for central configuration of several thousand appliances [4, 10, 3].

## 5. Notable Gaps / Risks

- **Throughput below checklist threshold (item 4.1):** Maximum documented firewall throughput is 940 Mbps (router mode, default rules, unidirectional) for both the 2102 and 4305, below the 1,000 Mbps requirement; a model with >=1 Gbps sustained inspection throughput would be required for this use case [4, 5, 6].
- **No device-level HA failover (item 4.3):** No active/standby failover with session preservation is documented, only a redundant DC power input on the 4305; uninterrupted gateway operation cannot be assumed [5].
- **No OT/ICS application-layer protocol filtering (item 3.2):** Filtering is documented at MAC/IP-address, port and protocol level; no OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT proxy is described [6].
- **Management-plane DoS history (item 4.4):** A CERT@VDE advisory records an unauthenticated HTTPS-flood denial of service of the management interface in firmware below 8.9.0, and explicit fail-close behavior of the data path under overload is not documented [2].
- **Requested certifications absent (item 5.4):** IEC 62443-4-2 and UL certifications exist, but no Common Criteria, FIPS 140-3, or national cryptographic certification was found in the staged sources [7, 8].

## 6. Evidence Quality Notes

Twelve of 24 items are backed by two or more source types; item 4.1 relies on vendor documentation only (product pages plus the catalog datasheet), which is why its confidence is capped at medium. Items 1.3, 4.4, 5.1 and 5.2 draw on CERT@VDE advisories (independent security disclosures coordinated by a certification body), and item 5.4 draws on TUV Rheinland and UL certificates, giving at least one non-vendor source to 12 items. No item was triangulated across three fully independent vendors or labs, because general web search engines were bot-blocked from this environment and independent reviews of FL MGUARD could not be located.

One material contradiction was handled: the vendor describes "Gigabit wire speed" for the 4305 while the same datasheet specifies max firewall throughput of 940 Mbps (unidirectional, default rules); the explicit throughput figure was used for item 4.1, with wire speed treated as port capability. VDE-2023-010 documents a UDP-packet bypass of MAC filter rules in stealth mode while confirming the default IPv4 packet filter was not compromised; item 1.3 therefore remains supported with the caveat recorded in gaps. The sixteen unknown verdicts (1.2, 1.4, 2.1-2.7, 3.1-3.4, 4.2, 4.3, 5.3) reflect genuine absence of evidence in the staged material - latency, HA failover, OT-protocol proxies, CDR/DLP and compliance-report capabilities are simply not documented in the pages, datasheet, certificates or advisories reviewed; consulting the full mGuard user manual and firmware release notes could resolve several of these.

---

## Bibliography

[1] CERT@VDE (VDE Association for Electrical, Electronic & Information Technologies). "PHOENIX CONTACT: FL MGUARD affected by two vulnerabilities (VDE-2023-010)". https://cert.vde.com/en/advisories/VDE-2023-010/ (Retrieved: 2026-08-11T09:35:00Z)
[2] CERT@VDE (VDE Association for Electrical, Electronic & Information Technologies). "PHOENIX CONTACT: Denial-of-Service vulnerability in mGuard product family (VDE-2022-051)". https://cert.vde.com/en/advisories/VDE-2022-051/ (Retrieved: 2026-08-11T09:35:00Z)
[3] CERT@VDE (VDE Association for Electrical, Electronic & Information Technologies). "PHOENIX CONTACT: XSS and memory-leak in FL MGUARD 1102/1105 (VDE-2021-046)". https://cert.vde.com/en/advisories/VDE-2021-046/ (Retrieved: 2026-08-11T09:35:00Z)
[4] Phoenix Contact GmbH & Co. KG. "FL MGUARD 2102 - Router - 1357828 (product page)". https://www.phoenixcontact.com/en-us/products/router-fl-mguard-2102-1357828 (Retrieved: 2026-08-11T09:35:00Z)
[5] Phoenix Contact GmbH & Co. KG. "FL MGUARD 4305 - Router - 1357875 (product page)". https://www.phoenixcontact.com/en-us/products/router-fl-mguard-4305-1357875 (Retrieved: 2026-08-11T09:35:00Z)
[6] Phoenix Contact GmbH & Co. KG. "FL MGUARD 4305 - Router - 1357875 (catalog datasheet PDF)". https://www.phoenixcontact.com/en-us/products/router-fl-mguard-4305-1357875?type=pdf (Retrieved: 2026-08-11T09:35:00Z)
[7] UL LLC. "UL Mark Safety Scheme Certificate (UL-US-L238705-1D1-32300202-3) for FL MGUARD". https://www.phoenixcontact.com/product/product/MTM1Nzg3NQ/downloads/8347185?_realm=us&_locale=en-US (Retrieved: 2026-08-11T09:35:00Z)
[8] TUV Rheinland Industrie Service GmbH. "TUV Rheinland Cybersecurity Certificate revision list, Cert. No. 968/CSP 1029.00/25 (FL MGUARD)". https://www.phoenixcontact.com/product/product/MTM1Nzg3NQ/downloads/11221426?_realm=us&_locale=en-US (Retrieved: 2026-08-11T09:35:00Z)
[9] GitHub (GriffinPlus). "GriffinPlus/mguard-config-tool README - a tool for handling ATV/ECS configuration files for the mGuard security router family". https://raw.githubusercontent.com/GriffinPlus/mguard-config-tool/master/README.md (Retrieved: 2026-08-11T09:35:00Z)
[10] Phoenix Contact GmbH & Co. KG. "FL MGUARD DM UNLIMITED - Software - 2981974 (product page)". https://www.phoenixcontact.com/en-us/products/device-parameterization-fl-mguard-dm-unlimited-2981974 (Retrieved: 2026-08-11T09:35:00Z)
[11] Phoenix Contact GmbH & Co. KG. "Industrial security - industry page (PHOENIX CONTACT)". https://www.phoenixcontact.com/en-us/industries/industrial-security (Retrieved: 2026-08-11T09:35:00Z)
[12] Phoenix Contact GmbH & Co. KG. "Industrial routers and cybersecurity - product category page (PHOENIX CONTACT)". https://www.phoenixcontact.com/en-us/products/industrial-communication/industrial-routers-and-cybersecurity (Retrieved: 2026-08-11T09:35:00Z)
[13] NIST. "NVD CVE search API results for keyword 'FL MGUARD' (5 CVEs)". https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=FL%20MGUARD&resultsPerPage=20 (Retrieved: 2026-08-11T09:35:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 13 (kept: 13, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, regulatory_filing: 1, third_party_review: 4, vendor_datasheet: 1, vendor_doc: 5
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
