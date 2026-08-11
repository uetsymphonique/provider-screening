# BSG / Cross Domain Product Assessment: Sophos Ltd. — Sophos RED / XGS Gateway (Sophos Firewall on XGS Series + SD-RED)

**Product ID:** `sophos-red-xgs-gateway`
**Version reference:** Sophos Firewall OS (SFOS) 20.0/21.x/22.0 admin guide documentation; XGS Series hardware from entry XGS 88 to flagship XGS 8500; Sophos Firewall datasheet edition 2026-04-01
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T16:30:00Z
**Total evidence items collected:** 42
**Total distinct sources:** 19

---

## 1. Overview

Sophos Firewall running on XGS Series appliances is a standard enterprise next-generation firewall (NGFW) that the vendor presents as the center of a consolidated network security platform; the product family also includes SD-RED (Remote Ethernet Device) hardware that connects branch offices to the firewall over secure encrypted tunnels [1][2][5]. Sophos positions the platform as a zone-based stateful firewall with deep packet inspection, TLS 1.3 inspection, IPS, web and application control, VPN, and SD-WAN, deployable as hardware appliances, virtual machines, or cloud instances [2]. It is not a cross-domain solution or protocol-break guard: no session-termination architecture, content disarm and reconstruction, dual-board hardware isolation, or security-label flow control is described in the reviewed material [1][2][19]. The firewall is managed locally or from Sophos Central, supports HA in active-passive and active-active modes [7], and carries FIPS 140-3 (Level 1) and Common Criteria EAL4 certifications [9][10][11]. This assessment therefore treats the product as an enterprise/edge NGFW and marks CDS-specific checklist items not applicable on the documented product category.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 1                | 5      | 0   |
| partial          | 5     | 0                | 5      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 16 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Sophos documents the XGS Series as next-generation firewall appliances with a zone-based stateful firewall, and SD-RED as remote Ethernet devices that build secure encrypted tunnels to the firewall; no protocol-break or TCP/IP session-termination guard architecture is described.
- **1.2:** The XGS Series is documented as single appliances built around a high-speed CPU plus a dedicated Xstream Flow Processor for hardware acceleration; no dual processing-board or FPGA/shared-memory isolation design is described.
- **1.5:** No internal cryptographic stamping of cleaned data before session re-initiation is documented; the product is a stateful firewall/VPN platform rather than a guard architecture.
- **2.1:** No content disarm & reconstruction of Office/PDF/image/CAD files is documented; Sophos' file analysis executes files in a secure cloud-based sandbox to observe behavior, which is malware detonation rather than CDR.
- **2.4:** No XML/JSON/FIXM/AIXM schema validation is documented; the product is a firewall rather than a guard with a content-validation engine.
- **2.5:** No security-label-based information flow control on files is documented; the product is a firewall rather than a classified-data guard.
- **2.7:** No anti-steganography detection or removal capability for image files is documented; the product is a firewall rather than a CDS guard.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Sophos documents the XGS Series as next-generation firewall appliances with a zone-based stateful firewall, and SD-RED as remote Ethernet devices that build secure encrypted tunnels to the firewall; no protocol-break or TCP/IP session-termination guard architecture is described. [1], [2], [5], [19] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The XGS Series is documented as single appliances built around a high-speed CPU plus a dedicated Xstream Flow Processor for hardware acceleration; no dual processing-board or FPGA/shared-memory isolation design is described. [1], [2] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | A fixed 'Drop all' firewall rule (ID #0) at the bottom of the rule table drops traffic matching no firewall rule, and best-practice guidance directs admins to avoid ANY-to-ANY rules and only allow authenticated users to reach the internet. The NSS Labs group test coverage reports the firewall passing all firewall policy and application control tests. [13], [14], [17], [19] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | The datasheet documents hardening across kernel and user portals with containerization and isolation of trust boundaries, and the admin guide describes a hardened, containerized VPN portal; no microkernel or SELinux-strict-mode claim is made. [2], [17] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | No internal cryptographic stamping of cleaned data before session re-initiation is documented; the product is a stateful firewall/VPN platform rather than a guard architecture. [1], [2], [19] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | No content disarm & reconstruction of Office/PDF/image/CAD files is documented; Sophos' file analysis executes files in a secure cloud-based sandbox to observe behavior, which is malware detonation rather than CDR. [2], [19] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No macro/script removal or embedded-object sanitization of files is documented in the reviewed sources.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Supported | medium | — | The admin guide states the firewall offers scanning by two antivirus engines (Sophos and Avira) and that dual-antivirus SMTP policies run the primary engine then the secondary engine; the datasheet notes the entry-level XGS 88 lacks dual AV scanning, implying other models support it. [2], [16] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | No XML/JSON/FIXM/AIXM schema validation is documented; the product is a firewall rather than a guard with a content-validation engine. [2], [19] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label-based information flow control on files is documented; the product is a firewall rather than a classified-data guard. [2], [19] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | — | Policy-based DLP is documented in the Email Protection module - it can automatically trigger encryption or block/notify based on sensitive data in emails leaving the organization; no general web-traffic DLP with custom keyword/ID-number/regex patterns is documented. [2] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No anti-steganography detection or removal capability for image files is documented; the product is a firewall rather than a CDS guard. [2], [19] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | Malware scanning for web, email and FTP traffic, plus TLS-decrypting HTTPS inspection via the web proxy, are documented; no SFTP or SMB/NFS file-transfer proxy with content cleaning is documented. [2], [19] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found (No OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT industrial protocol proxy is documented in the reviewed sources.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented; syslog is outbound-only to a configured server.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 2000 Mbps | The entry-level XGS 88 is rated 9.9 Gbps firewall throughput and 2 Gbps threat-protection throughput in the 2026 datasheet (the 2024 edition lists threat protection as 2,000 Mbps), so even the all-services figure exceeds the 1 Gbps threshold. [2], [3] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.006 ms | Firewall latency (64-byte UDP) is documented as 6 microseconds for the XGS 2100, i.e. 0.006 ms, well below the 10 ms threshold. [2] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Not Supported | medium | 4000 ms | HA active-passive and active-active modes with session failover for forwarded TCP/NAT, UDP/ICMP and VPN traffic are documented, but failover detection defaults to 16 missed heartbeat packets at 250 ms intervals, about 4 seconds (derived from the two documented defaults), far above the 100 ms requirement. [7], [8], [12] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (DoS & spoof protection policies are documented, but no explicit fail-close behavior of the boundary under hardware DoS/overload is documented.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Role-based administrator access with a default super administrator and custom administrator accounts is documented; a documented three-way split of system admin, policy admin and security auditor roles is not found. [15], [17] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | — | Syslog export supports TLS-encrypted log transmission to a configured server in standard-syslog or device-standard formats, and the hardening guide directs admins to forward logs to a SIEM of their choice. [6], [17] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | Compliance report templates are documented for HIPAA, GLBA, SOX, FISMA, PCI, NERC CIP v3 and CIPA, plus cloud-based pre-packaged compliance reports; templates for the checklist's named NIST SP 800-82, IEC 62443 or ISO 27001 frameworks are not in that documented set. [2], [18] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | — | NIST CMVP lists the Sophos Cryptographic Module as FIPS 140-3 Level 1 validated (certificate 4925, active) and FIPS 140-2 validated (certificate 4100, tested on SFOS 18.5 on XGS 3100), and BSI issued Common Criteria certificate BSI-DSZ-CC-1016-2020 for Sophos Firewall OS 17.0 at EAL 4 augmented by ALC_FLR.3. The admin guide states SFOS 20.0 MR1+ uses FIPS-certified modules with FIPS mode supported on XGS Series hardware. [4], [9], [10], [11] |

---

## 4. Notable Strengths

- **Enforced default-deny (item 1.3):** an uneditable Drop-all rule (ID #0) at the bottom of the firewall rule table drops any traffic that matches no rule, and guidance directs admins to avoid ANY-to-ANY rules [14][19].
- **Dual-engine antivirus scanning (item 2.3):** the firewall documents scanning by two antivirus engines (Sophos and Avira) with dual-antivirus SMTP policies running primary then secondary engine [16].
- **Throughput and latency headroom (items 4.1, 4.2):** the entry-level XGS 88 is rated 9.9 Gbps firewall and 2 Gbps threat-protection throughput, and the XGS 2100 documents 6 microsecond (0.006 ms) 64-byte UDP firewall latency [2].
- **TLS-encrypted log export to SIEM (item 5.2):** syslog transmission to a configured server can be encrypted with TLS, and the hardening guide recommends forwarding logs to a SIEM [6][17].
- **Independent certifications (item 5.4):** NIST CMVP lists the Sophos Cryptographic Module as FIPS 140-3 Level 1 validated (certificate 4925, active) and FIPS 140-2 validated (certificate 4100), and BSI certified Sophos Firewall OS 17.0 under Common Criteria at EAL 4 augmented by ALC_FLR.3 [9][10][11].

## 5. Notable Gaps / Risks

- **HA failover time (item 4.3):** documented failover detection defaults to 16 missed heartbeat packets at 250 ms intervals, about 4 seconds - far above the 100 ms requirement; a faster-tuned deployment would need vendor-published sub-second data to change this verdict [8].
- **No OT/ICS protocol proxy (item 3.2):** no OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT industrial proxy is documented, which is load-bearing for OT boundary deployments.
- **DLP is email-scoped (item 2.6):** policy-based DLP is documented only in the Email Protection module, with no web-traffic DLP for custom keywords, ID numbers, or regex patterns [2].
- **Compliance templates miss the named frameworks (item 5.3):** built-in templates cover HIPAA, GLBA, SOX, FISMA, PCI, NERC CIP v3 and CIPA, but not NIST SP 800-82, IEC 62443 or ISO 27001 [18].
- **RBAC without a documented three-role split (item 5.1):** role-based administration with a super administrator and custom administrators is documented, but no explicit system-admin / policy-admin / auditor separation [15][17].
- **Fail-close under DoS unverified (item 4.4):** DoS and spoof protection policies exist, but no documented fail-close behavior of the boundary under hardware overload; this should be clarified with the vendor for fail-safe requirements.

## 6. Evidence Quality Notes

Evidence consists of 42 grounded entries drawn from 19 staged sources: three vendor datasheets (2024 and 2026 Sophos Firewall editions plus XGS technical specifications), twelve Sophos admin-guide pages, and four independent or registry sources (NIST CMVP certificates 4100 and 4925, the BSI/Common Criteria portal certificate, and eG Innovations' Sophos HA documentation). Item 5.4 is triangulated across three independent registries plus vendor documentation and is the only item rated high confidence; items 1.3 and 4.3 additionally draw on third-party material (NSS Labs group-test coverage syndicated on Yahoo Finance, and eG Innovations), while the remaining functional verdicts rest on vendor-only sources, so confidence is capped at medium per the project rules.

No contradictions were found between sources: the 2024 and 2026 datasheet editions agree on XGS 88 performance (9.9 Gbps firewall, 2,000 Mbps threat protection), and the admin guide and datasheets align on HA modes, syslog/TLS, and the two-antivirus-engine architecture. Two caveats: the NSS Labs article is a vendor press release syndicated by a news outlet and is treated as corroboration of NGFW behavior rather than primary evidence, and the 4.3 numeric value (4000 ms) is arithmetic derived from two documented defaults (16 missed heartbeats x 250 ms) because Sophos publishes no switchover-time figure.

---

## Bibliography

[1] Sophos Ltd.. "Sophos XGS Series Technical Specifications (entry desktop models)". https://www.vox.co.za/wp-content/uploads/2025/03/Sophos-XGSSeries-Datasheet.pdf (Retrieved: 2026-08-11T16:00:00Z)
[2] Sophos Ltd.. "Sophos Firewall brochure/datasheet (2026-04-01)". https://www.firewallcompany.com/wp-content/uploads/2026/04/sophos-firewall-br.pdf (Retrieved: 2026-08-11T16:00:00Z)
[3] Sophos Ltd.. "Sophos Firewall brochure/datasheet (2024)". https://cdn.blueally.com/enterpriseav/datasheets/sophos-firewall-br-2024.pdf (Retrieved: 2026-08-11T16:00:00Z)
[4] Sophos Ltd.. "FIPS 140-3 Level 1 - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Certifications/FIPS/ (Retrieved: 2026-08-11T16:00:00Z)
[5] Sophos Ltd.. "RED tunnels and provisioning - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/21.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Network/Interfaces/REDInterfaces/REDInterfaceOverview/ (Retrieved: 2026-08-11T16:00:00Z)
[6] Sophos Ltd.. "Add a syslog server - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/22.0/help/en-us/webhelp/onlinehelp/AdministratorHelp/SystemServices/LogSettings/SyslogServerAdd/ (Retrieved: 2026-08-11T16:00:00Z)
[7] Sophos Ltd.. "About high availability - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/21.0/help/en-us/webhelp/onlinehelp/HighAvailablityStartupGuide/AboutHA/ (Retrieved: 2026-08-11T16:00:00Z)
[8] Sophos Ltd.. "Failover - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/21.0/help/en-us/webhelp/onlinehelp/HighAvailablityStartupGuide/AboutHA/HAFailover/ (Retrieved: 2026-08-11T16:00:00Z)
[9] NIST CSRC. "NIST CMVP Certificate #4100 - Sophos Cryptographic Module (FIPS 140-2)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4100 (Retrieved: 2026-08-11T16:00:00Z)
[10] NIST CSRC. "NIST CMVP Certificate #4925 - Sophos Cryptographic Module (FIPS 140-3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4925 (Retrieved: 2026-08-11T16:00:00Z)
[11] BSI (German Federal Office for Information Security). "BSI Common Criteria certificate BSI-DSZ-CC-1016-2020 - Sophos Firewall OS Version 17.0". https://www.commoncriteriaportal.org/files/epfiles/1016c_pdf.pdf (Retrieved: 2026-08-11T16:00:00Z)
[12] eG Innovations. "Sophos High Availability test - eG Innovations monitoring documentation". https://docs.eginnovations.com/Sophos-Firewall/Sophos-High-Availability-Test.htm (Retrieved: 2026-08-11T16:00:00Z)
[13] Yahoo Finance (press syndication). "Sophos XG Firewall Rated Among Highest Performing Products by NSS Labs in its Next-Generation Firewall Group Test Report". https://finance.yahoo.com/news/sophos-xg-firewall-rated-among-130000355.html (Retrieved: 2026-08-11T16:00:00Z)
[14] Sophos Ltd.. "Security management and best practices - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/20.0/help/en-us/webhelp/onlinehelp/StartupHelp/SecurityBestPractices/RuleBestPractice/ (Retrieved: 2026-08-11T16:00:00Z)
[15] Sophos Ltd.. "Device access - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/21.5/help/en-us/webhelp/onlinehelp/AdministratorHelp/Administration/DeviceAccess/ (Retrieved: 2026-08-11T16:00:00Z)
[16] Sophos Ltd.. "General settings (MTA mode) - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/22.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Email/GeneralSettings/MTAMode/GeneralSettingsMTAMode/ (Retrieved: 2026-08-11T16:00:00Z)
[17] Sophos Ltd.. "Hardening your Sophos Firewall - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/20.0/Help/en-us/webhelp/onlinehelp/StartupHelp/SecurityBestPractices/SecurityHardening/ (Retrieved: 2026-08-11T16:00:00Z)
[18] Sophos Ltd.. "Compliance reports - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/21.5/help/en-us/webhelp/onlinehelp/AdministratorHelp/Reports/Compliance/ (Retrieved: 2026-08-11T16:00:00Z)
[19] Sophos Ltd.. "Firewall rules - Sophos Firewall admin guide". https://docs.sophos.com/nsg/sophos-firewall/21.5/help/en-us/webhelp/onlinehelp/AdministratorHelp/RulesAndPolicies/FirewallRules/ (Retrieved: 2026-08-11T16:00:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 19 (kept: 19, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 4, web: 15
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
