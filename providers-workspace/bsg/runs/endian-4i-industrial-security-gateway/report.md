# BSG / Cross Domain Product Assessment: Endian S.r.l. - Endian 4i Industrial Security Gateway (4i Edge V / Edge X / Edge XL / Edge Software)

**Product ID:** `endian-4i-industrial-security-gateway`
**Version reference:** EndianOS 4i 6.9 (reference manual 6.9, datasheets © 2025); hardware models Endian 4i Edge V, Edge X, Edge XL
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T17:00:00Z
**Total evidence items collected:** 51
**Total distinct sources:** 18

---

## 1. Overview

The Endian 4i is a family of ruggedized industrial security gateways - the Edge V, Edge X and Edge XL hardware appliances plus an Edge Software/virtual edition - that run the EndianOS 4i operating system and are aimed at OT/ICS environments such as manufacturing, renewable energy and critical infrastructure [1], [2], [12]. The vendor positions the product as an industrial security gateway, not a protocol-break cross domain solution: the 6.9 reference manual documents an iptables-based stateful firewall, and the documented feature set centres on zone-based microsegmentation, NAT, IPsec/OpenVPN remote access, an nDPI-based application-control/IPS engine and Docker edge computing [6], [5], [15]. Deployment shapes include ruggedized DIN-rail, wall-mount or desktop appliances with extended temperature ranges and 4G/WiFi connectivity options, or EndianOS 4i installed on customer x86 hardware or a virtual machine [1], [12], [4]. Gateways integrate with the Endian Switchboard for centralized remote access, session management and permission control [2], [15].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 0                | 3      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 5     | 0                | 5      | 0   |
| unknown          | 10    | 0                | 0      | 10  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 1 items backed by ≥ 2 source_types; 14 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | - | The reference manual documents an iptables-based firewall with dedicated port-forwarding, source-NAT and 'incoming routed traffic' modules, i.e. an IP-routed/NAT datapath rather than a TCP/IP session-terminating protocol-break architecture. [6] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (The 4i Edge XL hardware spec (ARM SoC, 2 GB RAM, 16 GB storage, 5x GbE ports) does not describe internal board layout; no dual processing-board FPGA/shared-memory isolation design is documented.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | The firewall manual documents an implicit DROP rule that blocks every packet not matched by a rule, with everything else forbidden by default except system rules; a pre-configured whitelist of common outbound services (HTTP/HTTPS/FTP/DNS/ICMP) exists for the GREEN zone. [5], [6] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | Endian describes EndianOS as a hardened Linux-based operating system that powers the 4i gateways, running the Linux 6.6 LTS kernel; hardening specifics such as SELinux or a microkernel are not documented. [5], [12], [16] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Not Supported | medium | - | The documented datapath is an iptables-based routed/NAT firewall (port forwarding, source NAT, incoming routed traffic), not a session-terminating protocol-break funnel, so there is no internal control core that could gate re-initiation of a new session on a data-stamp. [6] |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No content disarm and reconstruction (CDR) engine that disassembles and rebuilds Office/PDF/image/CAD files is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No vendor documentation found describing macro/VBA/script removal from transferred files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Not Supported | medium | - | The vendor's feature matrix marks antivirus filtering and the Bitdefender anti-malware engine as EndianOS UTM-only with an empty EndianOS 4i column; no antivirus engine at all is documented for the 4i, so the two-plus-engine multi-AV requirement is not met. [5] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM schema validation capability is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label-based information flow control for transferred files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No vendor documentation found describing data-loss-prevention (keyword/regex) filtering of transferred content.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography engine for hidden data in image files is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Not Supported | medium | - | The 4i reference manual documents only a DNS proxy and the feature matrix marks HTTP/HTTPS proxy functionality as EndianOS UTM-only; no content-cleaning file-transfer proxy (SFTP, FTP/S, HTTPS, SMB/NFS) is documented for the 4i. [5], [9] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | Application-control/DPI detection and policy enforcement for Modbus, DNP3, Siemens S7, OPC-UA, Profinet and BACnet is documented for EndianOS 4i, but proxy support for IEC 60870-5-104 and MQTT industrial traffic is not described. [10], [13] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No vendor documentation found describing SQL Server/Oracle/PostgreSQL database proxying with query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | - | no evidence found (No vendor documentation found describing an RTSP video proxy or syslog/CEF unidirectional/bidirectional relay.) |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 3000 Mbps | The Endian 4i Edge XL and Edge X datasheets list firewall throughput of 3 Gbit/s (3,000 Mbps) with 300,000 concurrent sessions, measured under ideal test conditions with multiple flows; the figure exceeds the 1,000 Mbps requirement. [2], [3] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No vendor documentation found publishing packet/protocol processing latency figures.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Active-passive high availability (keepalived/VRRP) with up to three nodes is documented and described as a seamless failover where the slave immediately becomes master, but no switchover time in milliseconds is published. [5], [14] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | DoS/SYN-ICMP flood protection and inline IPS blocking are documented for the 4i; an explicit fail-close behavior of the gateway boundary under sustained DoS is not described. [5], [18] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | - | Web-UI user roles (Administrator, Viewer) with a single GUI profile are documented for the 4i, and the platform whitepaper describes role-based access with least-privilege permissions; a three-way separation of system admin, policy admin and auditor is not documented. [7], [16] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Remote syslog forwarding over UDP or TCP is documented in the logs manual, but CEF format and TLS-encrypted syslog transport to a SIEM are not documented. [5], [8] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | - | Endian documents technical alignment of the Secure Digital Platform with IEC 62443-3-2/3-3 (security zones and conduits, access control, encryption), but no ready-made compliance report templates for NIST SP 800-82, IEC 62443 or ISO 27001 are documented. [11], [17] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | - | The vendor documents IEC 62443-4-2/3-3 SL2 compliance with a security certification from TG alpha and hardware certifications CE/UKCA/FCC/RoHS, and states it does not offer certifications; no Common Criteria EAL4+, FIPS 140-3 or national cryptographic certification is documented for the 4i. [2], [11], [16] |

---

## 4. Notable Strengths

- **Default-deny firewall (item 1.3):** the 4i firewall applies an implicit DROP rule so any packet not matched by a rule is automatically blocked, with everything else forbidden by default except system rules [6].
- **Firewall throughput (item 4.1):** the Edge X and Edge XL datasheets list 3 Gbit/s firewall throughput with 300,000 concurrent sessions, comfortably exceeding the 1 Gbps checklist threshold [2], [3].
- **OT protocol visibility (item 3.2):** the nDPI-based application-control engine detects and can enforce policies on Modbus, DNP3, Siemens S7, OPC-UA, Profinet and BACnet traffic [10], [13].
- **Hardened Linux platform (item 1.4):** Endian documents EndianOS as a hardened Linux-based operating system running the Linux 6.6 LTS kernel across the 4i range [12], [16], [5].
- **Resilience features (items 4.3, 4.4):** active-passive HA clustering (keepalived/VRRP, up to 3 nodes) with seamless failover is documented, alongside DoS/SYN-ICMP flood protection and inline IPS blocking [14], [5].

## 5. Notable Gaps / Risks

- **No CC/FIPS/national cryptographic certification (item 5.4):** the datasheet enumerates CE, UKCA, FCC and RoHS and the vendor states it does not offer certifications; only a vendor-claimed IEC 62443-4-2/3-3 SL2 certification (TG alpha) is documented, so buyers requiring Common Criteria EAL4+, FIPS 140-3 or a national crypto certificate would need to verify or rule the product out [2], [11], [16].
- **No antivirus engine on the 4i (item 2.3):** the vendor's feature matrix marks antivirus filtering and the Bitdefender engine as UTM-only, leaving the 4i without the multi-AV inspection the checklist requires [5].
- **No content-cleaning file-transfer proxies (item 3.1):** the 4i documents only a DNS proxy; SFTP/FTP/S/HTTPS/SMB-NFS proxying with content cleaning is not available [9], [5].
- **Unquantified latency and failover (items 4.2, 4.3):** no processing-latency figure is published and HA is only described qualitatively ("seamless", "immediately"), so the ≤ 10 ms latency and ≤ 100 ms switchover requirements cannot be confirmed from vendor material [14].
- **Partial management separation (items 5.1, 5.2):** user roles are limited to Administrator/Viewer with a single GUI profile - no three-way system-admin/policy-admin/auditor split - and SIEM forwarding is plain syslog over UDP/TCP without CEF format or TLS transport [7], [8].

## 6. Evidence Quality Notes

All 18 cited sources are vendor-published (product pages, three datasheets, the 4i Edge X 6.9 reference manual, help-center KB articles, two whitepapers and a press release), because every general search engine attempted from this environment (Bing, DuckDuckGo, Startpage, Mojeek, Ecosia, Yandex, SearX instances, Reddit, Marginalia, Yep) returned anti-bot blocks or empty results - the same constraint documented in earlier BSG runs. As a result every item is capped at medium confidence by the validator's vendor-only rule, and no independent lab test, analyst report or certification-registry entry could be triangulated. Within the vendor corpus, 14 items draw on 2-3 distinct sources and 8 items span 2 or more source types (datasheet vs. manual vs. whitepaper); single-source items (2.3, 3.1, 4.4) rest on the vendor's own UTM-vs-4i feature matrix, whose explicit "-" marks for the 4i column are the basis for the not_supported verdicts on 2.3 and 3.1 (documented absence, not silence).

One internal tension exists on certifications: the 2023 press release describes the 4i as "certifiable to the IEC 62443 standard", the whitepaper claims the Secure Digital Platform "complies with IEC 62443 4-2, 3-3 at SL2" with "the security certification from TG alpha", and the IEC 62443 compliance page states "Endian does not offer consulting services or certifications". The 5.4 verdict (not_supported) does not depend on resolving that tension: none of the documented certifications - IEC 62443 SL2, CE, UKCA, FCC, RoHS - is on the checklist's required list (Common Criteria EAL4+, FIPS 140-3, national cryptographic certification), and the vendor's own datasheet explicitly enumerates which certifications the hardware holds. Items 2.2, 2.6, 3.3, 3.4 and 4.2 remain unknown because no staged vendor text mentions macro/script removal, DLP, database proxies, RTSP/syslog relays or latency figures.

---

## Bibliography

[1] Endian S.r.l.. "OT Security Gateway | For Industrial Environments (OT) - product page". https://www.endian.com/en/secure-digital-platform/security-gateways/for-ot-environment/ (Retrieved: 2026-08-11T17:00:00Z)
[2] Endian S.r.l.. "Endian 4i Edge XL - Datasheet". https://cms.endian.com/media/download/endian_4i_edge_xl_datasheet_en.pdf (Retrieved: 2026-08-11T17:00:00Z)
[3] Endian S.r.l.. "Endian 4i Edge X - Datasheet". https://cms.endian.com/media/download/endian_4i_edge_x_datasheet_en.pdf (Retrieved: 2026-08-11T17:00:00Z)
[4] Endian S.r.l.. "Endian 4i Edge Software - Datasheet". https://cms.endian.com/media/download/endian_4i_edge_software_datasheet_en.pdf (Retrieved: 2026-08-11T17:00:00Z)
[5] Endian S.r.l.. "EndianOS Full Feature List (UTM vs 4i)". https://www.endian.com/en/secure-digital-platform/security-gateways/endianos/full-feature-list/ (Retrieved: 2026-08-11T17:00:00Z)
[6] Endian S.r.l.. "4i Edge X 6.9 Reference Manual - The Firewall Menu". https://docs.endian.com/6.9/4i/firewall.html (Retrieved: 2026-08-11T17:00:00Z)
[7] Endian S.r.l.. "4i Edge X 6.9 Reference Manual - The System Menu". https://docs.endian.com/6.9/4i/system.html (Retrieved: 2026-08-11T17:00:00Z)
[8] Endian S.r.l.. "4i Edge X 6.9 Reference Manual - The Logs and Reports Menu". https://docs.endian.com/6.9/4i/logs.html (Retrieved: 2026-08-11T17:00:00Z)
[9] Endian S.r.l.. "4i Edge X 6.9 Reference Manual - The Proxy Menu". https://docs.endian.com/6.9/4i/proxy.html (Retrieved: 2026-08-11T17:00:00Z)
[10] Endian S.r.l.. "EndianOS 6.8.0 Release Notes (help center KB article)". https://help.endian.com/hc/en-us/articles/26826434972573-EndianOS-6-8-0-Release-Notes (Retrieved: 2026-08-11T17:00:00Z)
[11] Endian S.r.l.. "IEC 62443 Compliance for OT Systems - product page". https://www.endian.com/en/solutions/compliance/iec-62443-compliance/ (Retrieved: 2026-08-11T17:00:00Z)
[12] Endian S.r.l.. "Endian 4i Hardware - product page". https://www.endian.com/en/secure-digital-platform/security-gateways/for-ot-environment/hardware/ (Retrieved: 2026-08-11T17:00:00Z)
[13] Endian S.r.l.. "EndianOS - Secure Operating System for IT & OT - product page". https://www.endian.com/en/secure-digital-platform/security-gateways/endianos/ (Retrieved: 2026-08-11T17:00:00Z)
[14] Endian S.r.l.. "How to Configure High Availability (help center KB article)". https://help.endian.com/hc/en-us/articles/34699049062301-How-to-Configure-High-Availability (Retrieved: 2026-08-11T17:00:00Z)
[15] Endian S.r.l.. "Press release: IoT Security Gateway as software and virtual solution (Endian 4i Edge)". https://www.endian.com/en/resources/communication/press-releases/iot-security-gateway-as-software-and-virtual-solution/ (Retrieved: 2026-08-11T17:00:00Z)
[16] Endian S.r.l.. "Why Endian is secure - architecture of the Secure Digital Platform (whitepaper)". https://cms.endian.com/media/download/what_makes_endian_secure_rz_en.pdf (Retrieved: 2026-08-11T17:00:00Z)
[17] Endian S.r.l.. "How the Endian Secure Digital Platform helps to Achieve IEC 62443 Compliance (whitepaper)". https://cms.endian.com/media/download/endian_iec-62443-compliance_whitepaper_en.pdf (Retrieved: 2026-08-11T17:00:00Z)
[18] Endian S.r.l.. "4i Edge X 6.9 Reference Manual - The Services Menu". https://docs.endian.com/6.9/4i/services.html (Retrieved: 2026-08-11T17:00:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** ['endian.com site crawl: product page, hardware page, feature list, IEC 62443 page, whitepapers, press releases', 'docs.endian.com 6.9/4i reference manual: firewall, system, logs, proxy, services', 'help.endian.com Zendesk API: article search (modbus/OPC UA/HA/syslog/62443) + direct article fetch (6.8.0 release notes, HA configuration)', "cms.endian.com datasheet/whitepaper PDFs (Edge X, Edge XL, Edge Software, 'Why Endian is secure', IEC 62443 whitepaper)", 'Search-engine attempts (Bing, DuckDuckGo lite/html, Startpage, Mojeek, Ecosia, Yandex, SearX instances, Reddit, Marginalia, Yep) - all blocked or empty from this environment', 'ISASecure IEC 62443-4-2 certified-components registry check (no Endian entry found; used only as a gap note, not cited as evidence)']
- **Sources reviewed:** 18 (kept: 18, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** vendor_blog: 1, vendor_datasheet: 3, vendor_doc: 14
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
