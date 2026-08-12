# BSG / Cross Domain Product Assessment: HMS Networks (Anybus) — Anybus Industrial Security Gateway (Anybus Defender family)

**Product ID:** `anybus-industrial-security-gateway`
**Version reference:** Anybus Defender firmware 2.5.2 / User Manual 2.5.2 (PRO); models ABD1004-NATFW (Compact 1004), ABD4002/6004/6024 (-NATFW/-DPIFW/-PROFW)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:25:45Z
**Total evidence items collected:** 43
**Total distinct sources:** 16

---

## 1. Overview

The product assessed under the screening-list name "Anybus Industrial Security Gateway" is the Anybus Defender family from HMS Networks (Anybus brand): ruggedized DIN-rail industrial network security appliances spanning the Compact 1004 (4x 10/100 Mbit ports, ABD1004-NATFW) and the 4002/6004/6024 (and 6000/8000 series) with Gigabit Ethernet and SFP interfaces, sold in NAT/FW, DPI/FW and PRO/FW license tiers [1][4][5][8]. The vendor positions the lineup as industrial firewalls for OT networks - "a suite of industrial network security appliances designed to safeguard critical infrastructures" - with primary use cases of ISA/IEC 62443-3-3 network segmentation, NAT with traffic filtering, and deep packet inspection on industrial protocols [15][16]. It is therefore a firewall/DPI/VPN appliance class product, not a protocol-break cross-domain guard: item 1.1 is marked not_supported because the documented NAT/routing/bridging datapath contradicts session-terminating protocol break [1][5][15], while the remaining CDS-only checklist items (1.2, 1.5, 2.1, 2.4, 2.5, 2.7) are marked unknown for lack of any specific supporting or excluding evidence. Documented deployment shapes include zone segmentation between IT and OT, transparent layer-2 bridging (bridge mode) for HMI/PLC traffic inspection, OT-SDWAN VPN (WireGuard, OpenSSL, IPsec), and active-standby high availability on 6000/8000 series with PRO licenses [1][10][11].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 6 items backed by ≥ 2 source_types; 9 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | — | HMS documents the Anybus Defender as featuring NAT, Routing, DPI and VPN functionality, and trade press confirms Network Address Translation with traffic filtering for network segmentation -- an affirmative IP-routing/NAT datapath that excludes a protocol-break architecture terminating TCP/IP sessions at the boundary. [1], [15] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No dual processing board or FPGA/shared-memory hardware isolation design is documented; datasheets describe enclosure form factor (rugged fan-less housing, DIN-rail mount, port configuration) only, not internal board architecture.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | The stateful firewall blocks all traffic that does not match a rule by default: the support article states removing all rules still blocks traffic until an explicit allow rule is created, and the manual documents default block rules and a 'Blocking Unknown Traffic' DPI option. Note that only the WAN ships with a secure default profile; the LAN interface ships open by default. [8], [12] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | Secure boot and RSA-encrypted, device-uniquely-paired project configurations are documented as 'security by design', and the manual exposes kernel-hardening controls such as kernel page-table isolation (Meltdown mitigation). No explicit hardened-OS / microkernel / SELinux-strict-mode claim is made. [5], [8] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No internal cryptographic stamping of cleaned data before session re-initiation is documented for this product.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No content disarm & reconstruction of Office/PDF/image/CAD files is documented; the documented inspection engines are NAT/routing, DPI and VPN, which do not address file-content sanitization.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No file-content inspection, macro/script removal or embedded-object sanitization is documented for this network firewall.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No multi-engine antivirus scanning of payload is documented; the documented inspection engines are the industrial-protocol DPI and Snort/Suricata IDS/IPS.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No XML/JSON/FIXM/AIXM schema validation capability is documented for this product.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No security-label-based information flow control on files is documented for this product.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No keyword/regex-based data-leakage detection on traffic content is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No anti-steganography detection/removal capability for image files is documented for this product.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | FTP pass-through with an FTP-Helper application-level gateway that dynamically opens negotiated data ports (active and passive) is documented. No content-cleaning file-transfer proxy for SFTP/SMB/NFS or HTTPS content cleaning is documented. [13] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The industrial DPI engine supports EtherNet/IP, Modbus TCP and Siemens S7 (Classic/Plus) with packet-capture-learned whitelist/blacklist profiles and a 'Blocking Unknown Traffic' option; support for OPC UA, IEC 60870-5-104, DNP3 or MQTT is not documented. [4], [8], [11] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented; syslog appears only as outbound log export to a remote server.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | Interface speeds are documented (Gigabit Ethernet on 4000/6000/8000 series, 10/100 Mbit on the Compact 1004), but no firewall/DPI throughput figure in Mbps is published in the datasheets or manual, so the >= 1000 Mbps requirement cannot be verified numerically. [4], [5], [8] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet-processing latency figure is documented in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Active-standby high availability with real-time state-table synchronization is documented for the 6000/8000 series on PRO licenses, described as 'real-time failover' and 'seamless failover'; no switchover time in ms is published, so the <= 100 ms requirement cannot be verified numerically. [4], [8], [10] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No explicit fail-close behavior of the firewall under DoS/overload is documented.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Group/role-based access control with permission inheritance, LDAP and RADIUS authentication servers, and MFA via RADIUS-backed OTP is documented. A dedicated three-way separation of system admin, policy admin and auditor roles is not documented. [8], [14] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Outbound syslog to a remote server is documented (plus email/Telegram/Pushover notifications and an SNMP daemon with traps); TLS-encrypted syslog/CEF delivery to a SIEM is not explicitly documented. [8] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | The vendor positions the lineup for network segmentation 'in line with ISA/IEC 62443-3-3' and cites NIS2-driven requirements; no ready-made NIST SP 800-82 or ISO 27001 compliance report templates are documented. [15], [16] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | The datasheets and EU Declaration of Conformity list CE, RoHS, WEEE, EMC, RCM, UKCA (plus UL for the Compact 1004) and EMC standards (IEC/EN 61326-1, CISPR 11, FCC/IC Class A); no Common Criteria, FIPS 140-3 or national cryptographic certification is listed. [4], [5], [9] |

---

## 4. Notable Strengths

- **Default-deny stateful firewall (1.3):** Traffic is blocked unless explicitly allowed - the support article states that removing all rules still blocks all traffic until an allow rule is created [12], and the manual documents default block rules and a "Blocking Unknown Traffic" DPI option [8].
- **Industrial-protocol deep packet inspection (3.2):** An inline DPI engine inspects EtherNet/IP, Modbus TCP and Siemens S7 (Classic/Plus) and can auto-learn whitelist/blacklist rules from packet captures [8][4].
- **Active-standby high availability (4.3):** Two 6000/8000-series units can run in active-standby with real-time state-table synchronization for "seamless failover" on PRO licenses [10][4][8].
- **Role- and group-based administration (5.1):** Users map to groups with role-based permissions, LDAP/RADIUS authentication servers are supported, and MFA via RADIUS-backed OTP is documented [8][14].
- **Monitoring integrations (5.2):** Remote syslog export, email/Telegram/Pushover notifications and an SNMP daemon with traps are documented in the manual [8].

## 5. Notable Gaps / Risks

- **Throughput figure unpublished (4.1):** Interface speeds are Gigabit (10/100 Mbit only on the Compact 1004), but no firewall/DPI throughput in Mbps is published in the datasheets or manual, so the >= 1000 Mbps requirement cannot be verified [4][5][8].
- **HA switchover time unpublished (4.3):** HA is described qualitatively as "real-time"/"seamless" failover, but no switchover time in ms is documented, so the <= 100 ms requirement cannot be verified [10][4].
- **No security-product certifications (5.4):** Documented certifications are CE, RoHS, WEEE, EMC, RCM, UKCA (plus UL for the Compact 1004) and EMC standards IEC/EN 61326-1, CISPR 11, FCC/IC Class A; no Common Criteria, FIPS 140-3 or national cryptographic certification is listed [4][5][9].
- **LAN interface ships open by default (1.3):** Only the WAN ships with a secure default profile; the LAN interface is documented as open until a rule set is applied [8].
- **No content-level inspection (2.2, 2.3, 2.6):** No file sanitization, multi-engine AV scanning or DLP capability is documented, so malicious file payloads are not inspected; OT protocol coverage is limited to EtherNet/IP, Modbus TCP and S7 (no OPC UA, IEC 60870-5-104, DNP3 or MQTT documented) [8].

## 6. Evidence Quality Notes

The assessment rests on 16 staged sources and 43 evidence entries, every quote verified verbatim against the staged artifacts (0 fabricated, 0 unverifiable under verify_citation_grounding.py --strict --require-staged). Twelve items are backed by >= 2 source types, but the source base is heavily HMS-authored: the datasheets [4][5][6][7], User Manual v2.5.2 [8], product pages [1][2][3], EU DoC [9] and support-portal articles [10][11][12][13][14] are all vendor material, so all non-unknown verdicts are capped at medium confidence. The two independent-looking trade-press articles (Design World [15], Process and Control Today [16]) are syndications of the same HMS launch announcement and were retrieved through the Google Translate proxy because both origin sites block direct fetching; only item 5.3 relies exclusively on them. Items 4.1 and 4.3 are qualitative partials because the vendor publishes interface speeds and "seamless failover" language but no numeric throughput or switchover figures.

No outright contradictions were found. One nuance was handled explicitly: the out-of-box configuration ships the WAN with a secure default profile while the LAN interface is open [8], which coexists with the documented default-block firewall engine behavior (removing all rules still blocks traffic until an allow rule is created [12]); item 1.3 was anchored to the documented engine behavior with the default-profile nuance recorded in the notes/gaps rather than either extreme.

---

## Bibliography

[1] HMS Networks. "Anybus Defender 6024 - PRO/FW product page". https://www.hms-networks.com/p/abd6024-profw-anybus-defender-6024-pro-fw (Retrieved: 2026-08-11T09:20:23Z)
[2] HMS Networks. "Anybus Defender Compact 1004 - NAT/FW product page". https://www.hms-networks.com/p/abd1004-natfw-anybus-defender-compact-1004-nat-fw (Retrieved: 2026-08-11T09:20:27Z)
[3] HMS Networks. "Network security products - HMS Networks listing page". https://www.hms-networks.com/network-security-products (Retrieved: 2026-08-11T09:20:30Z)
[4] HMS Networks. "Anybus Defender 6024 - PRO/FW datasheet". https://media.hms-networks.com/image/upload/v1747766420/Documents/Generated_Datasheets/Production/en/hms-ABD6024-PROFW-en-Anybus-Defender-6024---PROFW.pdf (Retrieved: 2026-08-11T09:20:36Z)
[5] HMS Networks. "Anybus Defender Compact 1004 - NAT/FW datasheet". https://media.hms-networks.com/image/upload/v1747955607/Documents/Generated_Datasheets/Production/en/hms-ABD1004-NATFW-en-Anybus-Defender-Compact-1004---NATFW.pdf (Retrieved: 2026-08-11T09:20:37Z)
[6] HMS Networks. "Anybus Defender 4002 - PRO/FW datasheet". https://media.hms-networks.com/image/upload/v1747766513/Documents/Generated_Datasheets/Production/en/hms-ABD4002-PROFW-en-Anybus-Defender-4002---PROFW.pdf (Retrieved: 2026-08-11T09:20:41Z)
[7] HMS Networks. "Anybus Defender 6004 - PRO/FW datasheet". https://media.hms-networks.com/image/upload/v1747766709/Documents/Generated_Datasheets/Production/en/hms-ABD6004-PROFW-en-Anybus-Defender-6004---PROFW.pdf (Retrieved: 2026-08-11T09:20:41Z)
[8] HMS Networks. "Anybus Defender Documentation - User Manual v2.5.2 (PRO)". https://secdocs.anybus.com/defender/docs/2.5.2/assets/anybus-defender-manual-pro.pdf (Retrieved: 2026-08-11T09:20:44Z)
[9] HMS Networks. "EU Declaration of Conformity - Defender 6024 PRO/FW (ABD6024-PROFW)". https://hmsnetworks.blob.core.windows.net/nlw/docs/default-source/products/anybus/certificates/eu-declaration-of-conformity---defender-6024-profw.pdf (Retrieved: 2026-08-11T09:21:03Z)
[10] HMS Networks. "Anybus Defender High Availability Mode - HMS Support Portal article". https://support.hms-networks.com/hc/en-us/articles/32481452602130-Anybus-Defender-High-Availability-Mode (Retrieved: 2026-08-11T09:21:23Z)
[11] HMS Networks. "How to use the Anybus Defender in Bridge Mode - HMS Support Portal article". https://support.hms-networks.com/hc/en-us/articles/33619365802642-How-to-use-the-Anybus-Defender-in-Bridge-Mode-as-a-switch-with-firewall-functions (Retrieved: 2026-08-11T09:21:09Z)
[12] HMS Networks. "Why is the Anybus Defender 6024 blocking public pings... - HMS Support Portal article". https://support.hms-networks.com/hc/en-us/articles/29002454748562-Why-is-the-Anybus-Defender-6024-blocking-public-pings-even-without-rules-or-restrictions-active (Retrieved: 2026-08-11T09:21:32Z)
[13] HMS Networks. "Configure Anybus Defender Compact for NAT & FTP - HMS Support Portal article". https://support.hms-networks.com/hc/en-us/articles/36665475870610-Configure-Anybus-Defender-Compact-for-NAT-FTP (Retrieved: 2026-08-11T09:21:38Z)
[14] HMS Networks. "Secure Admin Access to Anybus Defender (MFA) - HMS Support Portal article". https://support.hms-networks.com/hc/en-us/articles/34980475862162-Secure-Admin-Access-to-Anybus-Defender-MFA (Retrieved: 2026-08-11T09:22:17Z)
[15] Design World / WTWH Media. "HMS Networks launches the Anybus Defender industrial security appliances lineup - Design World (retrieved via Google Translate proxy; origin blocks direct fetch)". https://translate.google.com/translate?sl=auto&tl=en&u=https%3A%2F%2Fwww.designworldonline.com%2Fhms-networks-launches-the-anybus-defender-industrial-security-appliances-lineup%2F&client=at&prev=search&hl=en (Retrieved: 2026-08-11T09:22:22Z)
[16] Process and Control Today. "HMS Networks launches the Anybus Defender industrial security appliances lineup - Process and Control Today (retrieved via Google Translate proxy; origin blocks direct fetch)". https://translate.google.com/translate?sl=auto&tl=en&u=https%3A%2F%2Fwww.pandct.com%2Fnews%2Fhms-networks-launches-the-anybus-defender-industrial-security-appliances-lineup&client=at&prev=search&hl=en (Retrieved: 2026-08-11T09:22:32Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 16 (kept: 16, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 6, web: 10
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
