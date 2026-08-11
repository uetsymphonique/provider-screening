# BSG / Cross Domain Product Assessment: Red Lion Controls (HMS Networks) — FlexEdge Intelligent Gateway (FlexEdge Intelligent Edge Automation Platform)

**Product ID:** `flexedge-intelligent-gateway`
**Version reference:** DA50A / DA70A series hardware with Crimson 3.2 software (Linux-based FlexEdge OS); assessed from HMS Networks product pages (2026), FlexEdge brochure (2025) and 2020-2024 independent coverage
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:20:00Z
**Total evidence items collected:** 45
**Total distinct sources:** 11

---

## 1. Overview

Red Lion's FlexEdge (DA50A/DA70A series) is a ruggedized industrial edge gateway/router platform that HMS Networks markets as the "FlexEdge Intelligent Edge Automation Platform", powered by Crimson 3.2 configuration software on a Linux-based operating system [6]. The vendor positions it as an all-in-one protocol converter, router and cellular gateway with field-unlockable software editions (networking gateway, protocol gateway, advanced IIoT gateway, automation controller) [1, 2]. The networking-gateway edition - the class assessed here - provides a stateful firewall, ACLs, packet filtering, NAT, routing, IP fallback, VPN (OpenVPN, IPsec, GRE) and RADIUS authentication [1, 2]. Hardware is DIN-rail mountable, rated -40 to 75 deg C with UL Class 1 Div 2, ATEX/IECEx and ABS certifications, and accepts up to three plug-and-play communications sleds (cellular, Wi-Fi, Ethernet, serial, USB) [2, 3, 5]. Deployment shapes include machine-level IIoT connectivity (MQTT/OPC UA to cloud), secure remote access, protocol conversion between legacy PLCs, and data logging/visualization [6, 10]. It is an industrial edge gateway, not a cross-domain guard or protocol-break device.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 0     | 0                | 0      | 0   |
| partial          | 6     | 1                | 5      | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 7     | 1                | 6      | 0   |

**Evidence quality:** 14 items backed by ≥ 2 source_types; 9 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** HMS/Red Lion positions FlexEdge as a ruggedized industrial edge gateway/router platform (networking-gateway edition with firewall, VPN, NAT and routing) and a protocol converter, not a cross-domain guard; no TCP/IP session-termination or protocol-break architecture is described.
- **1.2:** FlexEdge is documented as a single DIN-rail unit with a modular communications-sled design (up to three sleds) and on-board I/O; no dual processing-board or FPGA/shared-memory isolation architecture is described.
- **1.5:** No internal cryptographic stamping of cleaned data before session re-initiation is documented; the product is marketed as a networking/protocol gateway and automation controller, not a guard that re-initiates sessions on sanitized content.
- **2.1:** No content disarm & reconstruction of Office/PDF/image/CAD files is documented; the product converts protocols and moves data between OT and IT systems rather than acting as a CDS guard with a CDR engine.
- **2.4:** No XML/JSON/FIXM/AIXM schema validation is documented; the product is a protocol-conversion gateway, not a guard with a content validation engine.
- **2.5:** No security-label-based information flow control on files is documented; the product is a networking/protocol gateway rather than a classified-data guard.
- **2.7:** No anti-steganography detection/removal capability for image files is documented; the product is a firewall/gateway that connects PLCs and moves data rather than a CDS guard.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | high | — | HMS/Red Lion positions FlexEdge as a ruggedized industrial edge gateway/router platform (networking-gateway edition with firewall, VPN, NAT and routing) and a protocol converter, not a cross-domain guard; no TCP/IP session-termination or protocol-break architecture is described. [1], [2], [6], [10] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | FlexEdge is documented as a single DIN-rail unit with a modular communications-sled design (up to three sleds) and on-board I/O; no dual processing-board or FPGA/shared-memory isolation architecture is described. [1], [2], [3] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | A stateful firewall with access control lists (ACL) and packet filtering is documented on the brochure and product page, alongside encrypted communication and RADIUS authentication; an explicit default-deny whitelist policy for all non-listed packets/protocols is not stated in the reviewed sources. [2], [3], [4] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (Press coverage states FlexEdge runs a Linux-based OS combined with Crimson 3.2, but no hardened-OS / microkernel / SELinux-strict-mode claim for the device OS was found.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | No internal cryptographic stamping of cleaned data before session re-initiation is documented; the product is marketed as a networking/protocol gateway and automation controller, not a guard that re-initiates sessions on sanitized content. [1], [2] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | No content disarm & reconstruction of Office/PDF/image/CAD files is documented; the product converts protocols and moves data between OT and IT systems rather than acting as a CDS guard with a CDR engine. [2], [3] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No file-content inspection, macro/script removal or embedded-object sanitization is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No multi-engine antivirus scanning of payload is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | No XML/JSON/FIXM/AIXM schema validation is documented; the product is a protocol-conversion gateway, not a guard with a content validation engine. [1], [2] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label-based information flow control on files is documented; the product is a networking/protocol gateway rather than a classified-data guard. [1], [2] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No keyword/regex-based data-leakage detection on traffic content is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No anti-steganography detection/removal capability for image files is documented; the product is a firewall/gateway that connects PLCs and moves data rather than a CDS guard. [1], [10] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | Crimson documents syncing data to FTP servers and MS SQL Server, but no SFTP/FTP/S/HTTPS/SMB/NFS proxy with content cleaning is documented. [2], [8] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | high | — | OPC UA, MQTT, J1939 and CAN connectivity, plus conversion of up to 20 protocols from 300+ drivers, are documented across HMS pages and independent coverage; Modbus TCP, DNP3 and IEC 60870-5-104 proxy support are not named in the reviewed sources. [1], [9], [10] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | — | SQL Server connectivity via Crimson SQL Sync (data push to MS SQL Server) is documented on the brochure and product pages; no SQL Server/Oracle/PostgreSQL proxy with query whitelisting is documented. [2], [3], [8] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Not Supported | medium | 100 Mbps | Documented Ethernet connectivity is 10/100BaseT(X) Fast Ethernet ('Dual 10/100TX Ethernet communications sled'); the DA50A base unit lists 2x RJ45 with no gigabit rating and no throughput figure is published, so the platform's link rate is below the 1000 Mbps threshold. [3], [5], [11] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet-processing or realtime protocol latency figure is documented in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | IP fallback between WAN paths and dual-SIM cellular sleds are documented in the feature matrix and brochure, indicating automatic connectivity failover; no active-standby switchover time or session-preservation figure is published, so the <= 100 ms requirement is unverified. [1], [2] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No explicit fail-close behavior of the firewall under DoS/overload is documented.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Multi-user authentication via RADIUS, LDAP and password policies is documented; no explicit separation of system-admin, policy-admin and auditor roles is documented. [1], [2], [3], [4] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (No syslog/CEF export to a SIEM over an encrypted channel is documented in the reviewed sources.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No NIST SP 800-82 / IEC 62443 / ISO 27001 compliance report templates are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | Documented certifications are safety/environmental (UL Hazardous Class 1 Div 2, ATEX/IECEx, ABS, CE, cUL, UKCA, RoHS); no Common Criteria, FIPS 140-3 or national cryptographic certification is listed. [2], [3], [7] |

---

## 4. Notable Strengths

- **OT protocol conversion breadth (3.2):** Crimson converts up to 20 protocols from 300+ drivers, with documented OPC UA, MQTT, J1939 and CAN connectivity; a Sealed Air deployment at the ARC Industry Forum used the FlexEdge DA50N to normalize PackML/OPC UA data from multiple PLC brands [1, 9, 10].
- **Firewall and VPN network security (1.3):** a stateful firewall with ACL and packet filtering, VPN tunnels (OpenVPN, IPsec, GRE) and encrypted communication are documented across the brochure and product pages [1, 2].
- **Multi-factor authentication integration (5.1):** RADIUS authentication, LDAP and password policies are documented, enabling enterprise directory integration for device access [2, 3].
- **Rugged, hazard-area-rated hardware (4.x environment):** a -40 to 75 deg C DIN-rail platform with UL Class 1 Div 2, ATEX/IECEx and ABS certifications supports deployment in harsh and marine OT environments [2, 3, 7].
- **Field-upgradeable software editions (1.1):** a networking gateway can be upgraded in the field to a protocol gateway or IIoT controller without new hardware [2, 6].

## 5. Notable Gaps / Risks

- **No gigabit throughput (4.1):** documented Ethernet is 10/100BaseT(X) Fast Ethernet, so the platform cannot meet the >= 1000 Mbps requirement if high-bandwidth traffic must pass the gateway [5].
- **HA is connectivity failover, not active-standby (4.3):** IP fallback and dual-SIM cellular sleds are documented, but no sub-100 ms switchover time or session-preservation claim exists; the <= 100 ms requirement is unverified [1, 2].
- **No file-content sanitization or AV scanning (2.2, 2.3):** no macro/script removal, embedded-object cleaning or multi-engine antivirus scanning is documented - forwarded content is not inspected at the file level.
- **No SIEM log export documented (5.2):** no syslog/CEF forwarding to a SIEM over an encrypted channel is documented, limiting audit and SOC integration.
- **No security certifications (5.4):** documented certifications are safety/environmental (UL Hazardous, ATEX/IECEx, ABS, CE, cUL, UKCA, RoHS); there is no Common Criteria, FIPS 140-3 or national cryptographic certification [2, 3, 7].

## 6. Evidence Quality Notes

Fourteen of 24 items are backed by at least two source types; items 1.1, 3.2, 5.4 and the category basis for the seven not_applicable verdicts are corroborated by independent sources (Automation.com/ISA press coverage 2020-2024 and an ARC Industry Forum deployment writeup), which allows high confidence on 1.1 and 3.2. Nine items (1.4, 2.2, 2.3, 2.6, 3.4, 4.2, 4.4, 5.2, 5.3) are unknown because the reviewed public material never discusses the capability; the vendor's user manual and the retired DA50D datasheet on redlion.net could not be retrieved this run (the site has migrated to HMS Networks and both web archives rate-limited requests), so manual-level claims such as syslog forwarding, firewall default policy and role separation could not be verified.

Items 1.2, 1.3, 1.5, 2.1, 2.4, 2.5, 2.7, 4.1, 4.3 and 5.1 rest on vendor documentation only, capping confidence at medium per the validator rule; 4.1's numeric verdict (100 Mbps) derives from the vendor's own "Dual 10/100TX Ethernet communications sled" specification. One minor discrepancy exists: the HMS platform page says Crimson converts "up to 20 protocols simultaneously" while the DA50A page says "converts 10 protocols"; the platform-level figure was used with the broader driver count (300+). The ARC article names a "FlexEdge DA50N" while HMS pages list DA50A/DA70A; both were treated as the same FlexEdge platform family.

---

## Bibliography

[1] HMS Networks (Red Lion). "FlexEdge | Products | HMS Networks". https://www.hms-networks.com/flexedge (Retrieved: 2026-08-11T09:20:00Z)
[2] HMS Networks (Red Lion). "Red Lion FlexEdge Brochure (Industrial Network Controller and Edge Gateway)". https://media.hms-networks.com/image/upload/v1746532105/Documents/Brochures/Red_Lion_FlexEdge_Brochure.pdf (Retrieved: 2026-08-11T09:20:00Z)
[3] HMS Networks (Red Lion). "FlexEdge Advanced IIoT Gateway 1-Sled — Product page & technical specifications". https://www.hms-networks.com/p/da50a0bnn0000030-flexedge-advanced-iiot-gateway-1-sled (Retrieved: 2026-08-11T09:20:00Z)
[4] HMS Networks (Red Lion). "FlexEdge Networking Gateway 1-Sled — Product page & technical specifications". https://www.hms-networks.com/p/da50a0bnn0000010-flexedge-networking-gateway-1-sled (Retrieved: 2026-08-11T09:20:00Z)
[5] HMS Networks (Red Lion). "DA Series FlexEdge Dual Fast Ethernet Sled — Product page". https://www.hms-networks.com/p/das00pn1ee200000-da-series-flexedge-dual-fast-ethernet-sled (Retrieved: 2026-08-11T09:20:00Z)
[6] Automation.com (ISA). "Red Lion's FlexEdge Intelligent Edge Automation Platform Integrates IT and OT". https://www.automation.com/article/red-lion-flexedge-intelligent-edge-automation (Retrieved: 2026-08-11T09:20:00Z)
[7] Automation.com (ISA). "Red Lion's Entire FlexEdge Intelligent Edge Automation Platform Receives American Bureau of Shipping (ABS) Certification". https://www.automation.com/article/red-lion-flexedge-intelligent-edge-automation-abs (Retrieved: 2026-08-11T09:20:00Z)
[8] Automation.com (ISA). "Red Lion's New HDMI Feature Boosts Productivity with Real-Time Visual Awareness". https://www.automation.com/article/red-lion-hdmi-feature-productivity-visual-aware (Retrieved: 2026-08-11T09:20:00Z)
[9] Automation.com (ISA). "Red Lion Launches Strain Gauge Modules and J1939 and CAN Protocol Sleds for the FlexEdge Platform". https://www.automation.com/article/red-lion-strain-gauge-modules-j1939-can-protocol (Retrieved: 2026-08-11T09:20:00Z)
[10] Automation.com (ISA). "Remote Multivendor Digital Packaging Machine Services at the 27th Annual ARC Industry Forum". https://www.automation.com/article/remote-multivendor-digital-packaging-machine-arc (Retrieved: 2026-08-11T09:20:00Z)
[11] HMS Networks (Red Lion). "FlexEdge Networking Gateway 3-Sled — Product page & technical specifications". https://www.hms-networks.com/p/da70a0gnnnnnn010-flexedge-networking-gateway-3-sled-1-rs-232-2-rs-485-ports (Retrieved: 2026-08-11T09:20:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 11 (kept: 11, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 5, vendor_datasheet: 1, vendor_doc: 5
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
