# BSG / Cross Domain Product Assessment: Schneider Electric - ConneXium Security Gateway (ConneXium Industrial Firewall family, TCSEFE: TCSEFEA23F3F22 / TCSEFEC23F3F21 / TCSEFEC23FCF21)

**Product ID:** `connexium-security-gateway`
**Version reference:** ConneXium Tofino Industrial Firewall / Industrial Firewall-Router; TCSEFEC Web-based Interface Reference Manual S1B64648 02/2012; ConneXium catalog July 2018; Modicon Networking catalog DIA6ED2140903EN v6.0 07/2026
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:45:00Z
**Total evidence items collected:** 29
**Total distinct sources:** 8

---

## 1. Overview

The ConneXium Security Gateway is Schneider Electric's industrial (OT) network security gateway line, sold within the ConneXium Ethernet family and carried by the current Modicon Networking catalog as "ConneXium Industrial Firewalls" - the Tofino-based TCSEFE family (TCSEFEA23F3F22 Tofino Industrial Firewall TX/TX; TCSEFEC23F3F21 / TCSEFEC23FCF21 Industrial Firewall/Router) [1][3]. Schneider positions the line as "security for automation systems by restricting access to the network, allowing only authorized devices, types of communications and services" [7] - i.e. a ruggedized industrial firewall/router with stateful packet inspection, NAT, IPSec VPN and DoS protection, not a cross-domain guard with a protocol break [2][4][6]. Deployment shapes are DIN-rail security perimeters between automation zones, run in transparent bridge mode or routed mode, with redundant power supplies and router-redundancy options [3][4]. Identity caveat: the exact "Security Gateway 2xxx" SKU (TCSEGMC23F3F0) is end-of-life - its se.com page redirects to all-products - and the family is being phased out (TCSEFEC23F3F21 documented as discontinued 07 Jan 2021, end-of-service 28 Feb 2021; end of commercialization 1 Dec 2027 per the se.com page) [4][6].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 5     | 0                | 5      | 0   |
| not_supported    | 3     | 0                | 3      | 0   |
| unknown          | 15    | 0                | 0      | 15  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 6 items backed by ≥ 2 source_types; 8 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | - | The reference manual documents Stateful Packet Inspection (the firewall transmits data packets from external to internal network only when requested by an internal subscriber) and the product page documents switchover between bridge mode and route mode -- packet-forwarding architectures, not a protocol-break design that terminates and re-originates sessions. [2], [6] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No dual-processing-board hardware isolation design (FPGA or isolated shared memory) is documented.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | The stateful packet inspection firewall transmits unsolicited inbound traffic only for connections requested from inside and drops other data packets, with an explicit drop-everything rule on the external interface; firewall rules can be applied per packet or per frame. [2], [3], [6] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | - | no evidence found (No hardened-OS / microkernel / SELinux-strict-mode claim for the device OS was found in the reviewed sources.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No internal cryptographic stamping of cleaned data prior to session re-initiation is documented.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No file CDR (Office/PDF/Image/CAD reconstruction) capability is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No file-content inspection, macro/script removal or embedded-object sanitization is documented for this packet-level firewall.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No multi-engine antivirus scanning of payload is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM schema-validation engine is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label-based information flow control on files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No keyword/regex-based data-leakage detection on traffic content is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography detection/removal capability for image files is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | - | no evidence found (No file-transfer proxy with content cleaning (SFTP, FTP/S, HTTPS, SMB/NFS) is documented; SFTP appears only as a device file-management channel, and FTP/TFTP/SFTP appear only as packet-filter port services.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | The Tofino firewall integrates a Modbus/TCP Enforcer with optional OSI Layer-7 modules for EtherNet/IP, OPC, DNP3, IEC 60870-5-104 and GOOSE, and a community question confirms deep packet inspection for Modbus TCPIP; OPC UA and MQTT industrial proxying are not documented. [1], [3], [8] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | - | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented; a syslog client exists but is not a relay.) |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Not Supported | medium | 100 Mbps | All documented variants provide 10/100BASE-TX (or 10BASE-T/100BASE-TX) copper ports, which caps the achievable throughput at 100 Mbps, below the 1000 Mbps threshold; no higher throughput figure is documented. [1], [4], [5] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No packet/DPI processing latency figure is documented; a Schneider Community question about DPI latency impact went unanswered.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Router Redundancy is documented: two firewalls form a virtual firewall and the redundant firewall takes over on detected error, with redundant power supplies and transparent network-coupling redundancy also listed; no switchover time figure is published, so the <=100 ms failover-without-session-loss threshold cannot be verified. [2], [3], [4] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | DoS prevention is documented as per-second rate limits for TCP connections, ping and ARP floods with optional log entries; an explicit fail-close boundary lock on hardware overload is not documented. [2], [3], [5] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | - | Role-based access control is documented (read-only user role vs read/write admin role, with RADIUS group authentication for the user firewall); the checklist's three-role separation of system admin, policy admin and auditor is not documented. [2], [3], [5] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Event messages are forwarded to a configured syslog server (default port 514) and syslog protocol support plus SNMP traps are listed as cybersecurity features; CEF-format real-time log export over a TLS-encrypted channel to a SIEM is not documented. [2], [3], [5] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No ready-made NIST SP 800-82 / IEC 62443 / ISO 27001 compliance report templates are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | - | The documented certification set for the firewall family covers industrial EMC/safety approvals (CE, UL, RCM, DNV, UL 508, CSA C22.2 No 213/214, UL 1604, EN/IEC 61131-2, EN/IEC 60950, Germanischer Lloyd, FCC 47 CFR Part 15, IEC 61850-3, IEEE 1613, Class I Div 2); no Common Criteria, FIPS 140-3 or national cryptographic certification appears in the documented certification lists. [1], [3], [4] |

---

## 4. Notable Strengths

- **Default-deny stateful inspection (items 1.3, 4.4):** the SPI packet filter forwards unsolicited external traffic only for connections requested from inside and drops the rest via a documented "drop everything" rule on the external interface, with per-second DoS flood rate limits for TCP, ping and ARP traffic [2][6].
- **Industrial protocol deep packet inspection (item 3.2):** a built-in Modbus/TCP enforcer plus optional OSI Layer-7 modules for EtherNet/IP, OPC, DNP3, IEC 60870-5-104 and GOOSE give application-layer policing of OT traffic, with community confirmation of Modbus TCPIP DPI [1][3][8].
- **Active-standby redundancy (item 4.3):** router redundancy combines two firewalls into a virtual firewall whose redundant partner takes over on detected error, backed by state-table synchronisation and redundant power supplies [2][3][4].
- **Management and logging basics (items 5.1, 5.2):** role-based access (read-only user vs read-write admin), RADIUS group authentication, syslog forwarding and SNMP traps are documented in the manual and datasheets [2][3][5].

## 5. Notable Gaps / Risks

- **Throughput ceiling (item 4.1):** every documented variant is a 2-port 10/100BASE-TX device (100 Mbps), far below the 1 Gbps checklist threshold, so the line cannot serve as a high-bandwidth boundary [4][5].
- **End-of-life product line (overall):** TCSEFEC23F3F21 is documented discontinued (07 Jan 2021, end-of-service 28 Feb 2021) and the se.com page lists end of commercialization 1 Dec 2027; a buyer must confirm spares, firmware and support runway before selection, and the "Security Gateway 2xxx" SKU itself is already de-listed [4][6].
- **Unverifiable HA and fail-safe behavior (items 4.3, 4.4):** no switchover time is published (the <=100 ms failover-without-session-loss threshold is unverifiable) and no explicit fail-close boundary lock under hardware overload is documented - only DoS rate limiting [2].
- **No SIEM-over-TLS export (item 5.2):** syslog is forwarded over the plain RFC 3164 protocol (default port 514); CEF-format export over a TLS-encrypted channel is not documented [2].
- **Uncovered content-inspection capabilities (items 2.2, 2.3, 2.6, 3.1, 3.3, 3.4, 5.3):** no file/macro sanitisation, multi-engine AV, DLP, file-transfer/database/video-stream proxies or compliance report templates are documented for this packet-level firewall - all currently unknown, not confirmed absent.

## 6. Evidence Quality Notes

All 24 items were assessed from 8 distinct sources, every one vendor-documented: three Schneider catalogs/manuals (ConneXium Connecting Ethernet Devices catalog 2018, TCSEFEC Web-based Interface Reference Manual 2012, Modicon Networking catalog 2026), two Schneider product datasheets (one mirrored by the RMS Online reseller), two se.com pages (product and range) and one Schneider Community thread. Only item 3.2 draws on a non-documentation source (community), and no item is backed by an independent analyst/lab source, so confidence is capped at medium throughout and no verdict is high-confidence. No independent source was locatable: all public search engines, archive.org and the major distributor sites rate-limited or blocked this environment during the run, and the exact "Security Gateway 2xxx" SKU is de-indexed, so the assessment anchors to the documented ConneXium firewall family with the identity caveat recorded in the overview and run manifest.

The sources were mutually consistent - catalog, manual and datasheets agree on product category (Ethernet TCP/IP firewall), 2x 10/100 ports, security features and certifications - so no contradictions required adjudication. The main judgment calls were: item 1.1 is rated not_supported on the documented Stateful Packet Inspection / bridge-or-route-mode packet-forwarding architecture, which is incompatible with a protocol-break design; items 1.2, 1.5, 2.1, 2.4, 2.5 and 2.7 have no documented fact either confirming or excluding the capability and are rated unknown rather than not_applicable; and the numeric-threshold items were rated from the documented numbers (4.1 not_supported at 100 Mbps because the ports are 10/100; 4.3 partial because router redundancy is documented but no switchover time is published).

---

## Bibliography

[1] Schneider Electric. "ConneXium - Connecting Ethernet devices - Catalog (July 2018)". https://iportal.se.com/Contents/docs/CONNEXIUM%20CONNECTING%20ETHERNET%20DEVICES_CATALOG.PDF (Retrieved: 2026-08-11T09:40:00Z)
[2] Schneider Electric. "ConneXium TCSEFEC Industrial Firewall - Web-based Interface Reference Manual (S1B64648, 02/2012)". https://archive.org/download/manualzilla-id-5677278/5677278.pdf (Retrieved: 2026-08-11T09:40:00Z)
[3] Schneider Electric. "Modicon Networking: Connecting Ethernet devices - Catalog (DIA6ED2140903EN, v6.0, July 2026)". https://download.se.com/files?p_Doc_Ref=DIA6ED2140903EN&p_enDocType=Catalog&p_File_Name=DIA6ED2140903EN.pdf (Retrieved: 2026-08-11T09:40:00Z)
[4] RMS Online (Schneider Electric product data). "TCSEFEC23F3F21 ConneXium Industrial Firewall product datasheet (Schneider data mirrored by RMS Online, 30 May 2024)". https://rmsonline.co.za/wp-content/uploads/2024/06/tcsefec23f3f21.pdf (Retrieved: 2026-08-11T09:40:00Z)
[5] Schneider Electric. "Product data sheet - TCSEFEA23F3F22 ConneXium Tofino Firewall TX/TX (Sep 21, 2020)". https://iportal.se.com/Contents/docs/SQD-TCSEFEA23F3F22_DATASHEET.PDF (Retrieved: 2026-08-11T09:40:00Z)
[6] Schneider Electric. "TCSEFEC23F3F21 - firewall, Modicon Networking, industrial firewall, 2 ports for copper - Schneider Electric USA product page". https://www.se.com/us/en/product/TCSEFEC23F3F21/firewall-modicon-networking-industrial-firewall-2-ports-for-copper/ (Retrieved: 2026-08-11T09:40:00Z)
[7] Schneider Electric. "Connexium Industrial Firewalls - Automation System Security - Schneider Electric USA product range page". https://www.se.com/us/en/product-range/1106-connexium-industrial-firewalls/ (Retrieved: 2026-08-11T09:40:00Z)
[8] Schneider Electric Community. "Schneider Electric Community thread: ConneXium Firewalls with deep packet inspection (Modicon PAC Forum)". https://community.se.com/t5/Modicon-PAC-Forum/ConneXium-Firewalls-with-deep-packet-inspection/td-p/257250 (Retrieved: 2026-08-11T09:40:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 34
- **Sources reviewed:** 8 (kept: 8, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 5, web: 3
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
