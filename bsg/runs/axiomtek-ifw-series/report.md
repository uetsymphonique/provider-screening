# BSG / Cross Domain Product Assessment: Axiomtek Co., Ltd. — Axiomtek IFW Series (IFW320 / IFW330 industrial firewalls)

**Product ID:** `axiomtek-ifw-series`
**Version reference:** IFW320 datasheet (2017, catalog pp. 383-384); IFW330 datasheet (2017, pp. 385-386); IFW320 User's Manual Version A1 (January 2015); IFW330 series User's Manual
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:08:34Z
**Total evidence items collected:** 53
**Total distinct sources:** 10

---

## 1. Overview

The Axiomtek IFW series is a DIN-rail-mountable industrial firewall appliance line marketed by Axiomtek (Taiwan) for protecting automation and remote-monitoring networks, with two members assessed here: the IFW320 (1 WAN / 1 LAN) and the IFW330 (2 WAN / 1 LAN plus a configurable WAN/DMZ port) [1], [2]. Axiomtek positions both as all-in-one Firewall/NAT/VPN appliances with stateful packet inspection, DoS protection, IDP/BotNet prevention and industrial protocol management (EtherCAT, Ethernet/IP, Lonworks, Profinet, Modbus, DNP) [1], [7]. The product is an industrial firewall, not a cross-domain guard: no protocol-break or content-disarm architecture is documented, and Axiomtek's current IT/OT portfolio is built around firewall/VPN/UTM cybersecurity gateways (iNA110, iNA200), indicating the IFW generation has been superseded [10]. Deployment shapes include DIN-rail and wall mounting in oil/gas, water/wastewater, power and factory automation segments [1], [7]. The IFW320 User's Manual VA1 (January 2015) documents configuration, policy, HA, logging and administration; both manuals and the 2017 datasheets are the primary evidence base for this assessment [3], [4].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 2     | 0                | 2      | 0   |
| unknown          | 7     | 0                | 0      | 7   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 11 items backed by ≥ 2 source_types; 8 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Axiomtek markets the IFW320/IFW330 as all-in-one industrial firewall/NAT/VPN appliances based on stateful packet inspection, and its current IT/OT portfolio is positioned around firewall/VPN/UTM security gateways; no TCP/IP session termination or protocol-break architecture is described, so the protocol-break requirement does not apply to this product class.
- **1.2:** The IFW320 is documented as a single DIN-rail appliance built on one Intel Atom E3815 processor with two GbE ports; no dual processing board or FPGA/shared-memory isolation design is described, consistent with an industrial firewall rather than a guard.
- **1.5:** No internal cryptographic stamping of data before session re-initiation is described; the product is positioned as an industrial firewall appliance, not a CDS guard with data stamping.
- **2.1:** No content disarm and reconstruction of Office/PDF/image/CAD files is documented; inspection is packet-level (stateful inspection, IDP, anti-virus on WEB/FTP transfers) rather than a CDR engine, consistent with the firewall product class.
- **2.4:** No XML/JSON/FIXM/AIXM schema validation is documented; the product is an industrial firewall rather than a content-validating guard.
- **2.5:** No security-label-based information flow control on files is documented; the product is an industrial firewall rather than a classified-data guard.
- **2.7:** No anti-steganography detection or removal for image files is documented; the product is an industrial firewall rather than a CDS guard.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Axiomtek markets the IFW320/IFW330 as all-in-one industrial firewall/NAT/VPN appliances based on stateful packet inspection, and its current IT/OT portfolio is positioned around firewall/VPN/UTM security gateways; no TCP/IP session termination or protocol-break architecture is described, so the protocol-break requirement does not apply to this product class. [1], [2], [6], [7], [10] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The IFW320 is documented as a single DIN-rail appliance built on one Intel Atom E3815 processor with two GbE ports; no dual processing board or FPGA/shared-memory isolation design is described, consistent with an industrial firewall rather than a guard. [1], [2], [6], [7] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | The IFW320/IFW330 manuals document a policy-based stateful firewall in which packets not meeting any policy criteria are not permitted to pass, and the datasheet lists URL and IP whitelist modes; forwarding is rule/whitelist driven rather than implicitly permissive. [1], [3], [4] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No hardened-OS / microkernel / SELinux-strict-mode claim for the device firmware was found in the datasheets or manuals; the manuals reference only generic IP-stack/kernel behavior.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | No internal cryptographic stamping of data before session re-initiation is described; the product is positioned as an industrial firewall appliance, not a CDS guard with data stamping. [1], [2], [6], [7] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | No content disarm and reconstruction of Office/PDF/image/CAD files is documented; inspection is packet-level (stateful inspection, IDP, anti-virus on WEB/FTP transfers) rather than a CDR engine, consistent with the firewall product class. [1], [2], [6], [7] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No macro/script removal or embedded-object sanitization for files is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | The manuals document a WEB/FTP anti-virus filter applied per policy that filters viruses in files transferred over WEB and FTP; no parallel multi-engine (2+) antivirus scanning of raw payload is documented. [3], [4] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | No XML/JSON/FIXM/AIXM schema validation is documented; the product is an industrial firewall rather than a content-validating guard. [1], [2], [6], [7] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label-based information flow control on files is documented; the product is an industrial firewall rather than a classified-data guard. [1], [2], [6], [7] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No keyword/regex-based data-leakage detection on traffic content is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No anti-steganography detection or removal for image files is documented; the product is an industrial firewall rather than a CDS guard. [1], [2], [6], [7] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | The manual's pre-defined service list includes SFTP, FTP and HTTPS as policy-filterable TCP services, and a WEB/FTP anti-virus filter applies to transferred files; no SMB/NFS proxy with content cleaning is documented. [3] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The datasheets and manual document industrial protocol management for EtherCAT, Ethernet/IP, Lonworks, Profinet, Modbus and DNP (IFW330 also lists ICE); no OPC UA, IEC 60870-5-104 or MQTT industrial proxy is documented. [1], [2], [3], [7] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented; remote syslog appears only as a log-forwarding client.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Not Supported | medium | 500 Mbps | The IFW320 datasheet specifies 500 Mbps data throughput and the IFW330 datasheet specifies 500 Mbps NAT throughput; the CTIMES launch article and the IPC Station listing repeat the 500 Mbps maximum, below the 1000 Mbps threshold. [1], [2], [5], [7], [9] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet processing latency figure is published in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | The manuals document active/standby HA in which a Backup firewall is promoted to Master with transparent failover when the Master fails, and the IFW330 adds dual-WAN redundancy; no switchover time in milliseconds is published, so the <=100 ms requirement cannot be verified. [3], [4] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | The devices document DoS protection with SYN/ICMP/UDP attack detection and configurable source/destination IP blocking, plus anomaly-based auto-blocking of IPs until an administrator unlocks them; an explicit fail-close of the entire boundary under hardware overload is not documented. [1], [3], [4] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | The manual documents an 'admin' superuser plus sub-administrators granted Read, Write or All privileges, with read-only sub-administrators unable to change settings, and user authentication via local accounts, AD or POP3; a dedicated three-way system-admin/policy-admin/auditor role separation is not documented. [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | The manuals document forwarding all security-function logs to an external syslog server via the Remote Syslog Server setting, plus SNMP monitoring and per-event audit logs; CEF format and a TLS-encrypted log channel to a SIEM are not documented. [3], [4] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No ready-made NIST SP 800-82 / IEC 62443 / ISO 27001 compliance report templates are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | The datasheets list CE, FCC Part 18, UL 60950-1 (compliance) and UL 508 (compliance) certifications for the IFW320/IFW330; none of the checklist's required certifications (Common Criteria, FIPS 140-3 or national cryptographic certification) appears in the documented list. [1], [2] |

---

## 4. Notable Strengths

- **Policy-based default-deny firewall (item 1.3):** The IFW320/IFW330 manuals document that packets not meeting any configured policy criteria are not permitted to pass, with URL and IP whitelist modes available [1], [3], [4].
- **Industrial protocol awareness (item 3.2):** Protocol management covers Modbus, DNP, EtherCAT, PROFINET, Ethernet/IP and Lonworks, letting the firewall filter fieldbus traffic without a CDS guard [1], [2], [3].
- **Active/standby HA with transparent failover (item 4.3):** Two devices elect a new Master on failure with transparent failover, and the IFW330 adds dual-WAN redundancy [3], [4].
- **DoS protection and anomaly auto-blocking (item 4.4):** SYN/ICMP/UDP attack detection with configurable IP blocking, plus anomaly-based auto-blocking of IPs until administrator unlock [3].
- **Role-based administration and external logging (items 5.1, 5.2):** Admin plus sub-administrator Read/Write/All privilege model with AD/POP3 user authentication, and security-function logs forwardable to an external syslog server [3].

## 5. Notable Gaps / Risks

- **Throughput below threshold (item 4.1):** Documented data/NAT throughput is 500 Mbps, half the checklist's 1000 Mbps minimum, so the series cannot meet a 1 Gbps inspection requirement [1], [2], [7].
- **HA switchover time unquantified (item 4.3):** Transparent failover is documented but no switchover time in milliseconds is published, so the <= 100 ms requirement cannot be verified and may not hold with session preservation [3], [4].
- **No OPC UA / IEC 60870-5-104 / MQTT proxies (item 3.2):** Industrial protocol support covers Modbus/DNP/Profinet-class fieldbuses but not the OPC UA, IEC 60870-5-104 or MQTT application proxies the checklist asks for [1], [2].
- **No high-assurance certifications (item 5.4):** The documented certifications (CE, FCC Part 18, UL 60950-1, UL 508) include neither Common Criteria, FIPS 140-3 nor a national cryptographic certification [1], [2].
- **Legacy product status:** The IFW generation no longer appears in Axiomtek's current IT/OT portfolio, which lists iNA110/iNA200 DIN-rail cybersecurity gateways instead, so new deployments face obsolescence and firmware-support risk [10].

## 6. Evidence Quality Notes

Evidence was staged from the official IFW320/IFW330 datasheets (2017), the IFW320 User's Manual VA1 (January 2015, archived copy) and the IFW330 series User's Manual (reseller-hosted copy), with corroboration from a CTIMES launch article, distributor/reseller listings (Mouser, IPC Station, nt-rt.ru) and Axiomtek's current IT/OT portfolio page. Items 1.1, 2.1, 2.4, 2.5, 2.7 and 4.1 are triangulated across vendor documentation and at least one independent source (CTIMES, IPC Station); items 1.3, 2.3, 3.1, 4.3, 4.4, 5.1 and 5.2 rest on vendor documentation only (datasheets/manuals), so their confidence is capped at medium per the validator rule. The seven items marked unknown (1.4, 2.2, 2.6, 3.3, 3.4, 4.2, 5.3) have no supporting evidence in any staged source; they were not upgraded to not_supported because no source affirmatively documents the capability's absence (with the exception of 5.4, where the documented certification list rules out the required certifications). No contradictions between sources were found — the datasheet figures (500 Mbps throughput, certification list, protocol list) are consistent across the official documents, the CTIMES article and the reseller listings.

---

## Bibliography

[1] Axiomtek Co., Ltd.. "IFW320 Robust Industrial Firewall Appliance - datasheet (Industrial Firewall Systems, pp. 383-384)". https://www.axiomtek.com/download/spec/ifw320.pdf (Retrieved: 2026-08-11T09:08:33Z)
[2] Axiomtek Co., Ltd.. "IFW330 Industrial Firewall Appliance with 2 WAN and 1 LAN - datasheet (Industrial Firewall Systems, pp. 385-386)". https://www.axiomtek.com/download/spec/ifw330.pdf (Retrieved: 2026-08-11T09:08:33Z)
[3] Axiomtek Co., Ltd. (via Internet Archive). "IFW320 Industrial Firewall Appliance User's Manual, Version A1 (January 2015)". https://archive.org/download/manualzilla-id-5843532/5843532.pdf (Retrieved: 2026-08-11T09:08:33Z)
[4] Axiomtek Co., Ltd. (via Westward Sales). "IFW330 series Industrial Firewall Appliance User's Manual". https://westwardsales.com/product/product/download?product_id=3705&download_id=936 (Retrieved: 2026-08-11T09:08:33Z)
[5] Axiomtek Co., Ltd. (via Mouser Electronics). "IFW320 Robust Industrial Firewall Appliance - datasheet (Mouser-hosted copy)". https://www.mouser.com/datasheet/2/618/ifw320-1381070.pdf (Retrieved: 2026-08-11T09:08:33Z)
[6] Axiomtek Co., Ltd. (via NT-RT, Russia). "IFW330 / IFW320 datasheet compilation (nt-rt.ru distributor copy)". https://axiomtek.nt-rt.ru/images/manuals/IFW3XX.pdf (Retrieved: 2026-08-11T09:08:33Z)
[7] CTIMES (Taiwan tech media). "Axiomtek Robust Industrial Firewall Appliance - IFW320 (CTIMES article, published Apr 22 2015)". https://en.ctimes.com.tw/DispArt.asp?O=HJZ4M8H7YMVARA00PS&U=RC (Retrieved: 2026-08-11T09:08:33Z)
[8] IPC Station. "AXIOMTEK IFW330 - product page (IPC Station reseller)". https://www.ipcstation.net/axiomtek/ifw330 (Retrieved: 2026-08-11T09:08:33Z)
[9] IPC Station. "AXIOMTEK IFW320 - product page (IPC Station reseller)". https://www.ipcstation.net/axiomtek/ifw320 (Retrieved: 2026-08-11T09:08:33Z)
[10] Axiomtek Co., Ltd.. "IT/OT Network Security - Axiomtek product portfolio page". https://www.axiomtek.com/it-ot/ (Retrieved: 2026-08-11T09:08:33Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 10 (kept: 10, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 6, web: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
