# BSG / Cross Domain Product Assessment: Fortinet - FortiGate Rugged Security Gateway

**Product ID:** `fortigate-rugged-security-gateway`
**Version reference:** FortiGate Rugged Series (FGR-50G-5G/60F/60G/70F/70G); datasheet FGR-DAT-R57-20260703; FortiOS 7.4.5 documentation
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:11:51Z
**Total evidence items collected:** 54
**Total distinct sources:** 25

---

## 1. Overview

Fortinet's FortiGate Rugged Security Gateway (Rugged Series models FGR-50G-5G/60F/60G/70F/70G) is a ruggedized industrial next-generation firewall (NGFW) family, not a protocol-break cross-domain guard [1]. The vendor positions it for operational-technology networks: DIN-rail or desktop form factors, redundant 12-125 V DC power, -40 to 75 °C operating range, IP40/IP20 ratings, optional 3G/4G/5G cellular WAN, and IEC 61850-3/IEEE 1613 plus EN 50155 (rolling stock) certification [1][2]. It runs FortiOS, the same OS as the rest of the FortiGate line, with FortiGuard security services (IPS, antivirus, DLP, OT Security Service) and Secure SD-WAN [1][2]. Deployment shapes span IT/OT segmentation per the Purdue model, remote/field sites with cellular WAN, and converged security-fabric topologies with FortiSwitch Rugged [1][2]. All checklist items are assessed against this NGFW class; no staged source documents a protocol break, dual-board hardware isolation, internal data stamping, W3C schema validation, or anti-steganography capability, so those items score unknown or not_supported rather than being exempted (per the checklist's outcome-item rule, product class alone is not grounds for not_applicable) [1].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 10    | 1                | 9      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 18 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Unknown | low | - | no evidence found |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | FortiOS firewall policies are evaluated against traffic parameters and any traffic that does not match a configured policy is denied (implicit default-deny). [8] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | FortiOS is a purpose-built security OS whose firmware, AV and IPS engine files are dually-signed by Fortinet and a third-party CA, and whose executables are protected by real-time file system integrity checking that blocks unauthorized kernel module loading. [20], [21] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | - | FortiOS (proxy-mode antivirus) and the FortiGuard CDR service strip active content from Office, PDF and RTF files in real time to produce sanitized files; coverage of Image/CAD formats and 100% reconstruction is not documented for the Rugged series. [1], [18], [19] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Supported | medium | - | FortiOS CDR strips macros from Microsoft Office documents by default (configurable via the office-macro option), and the FortiGuard CDR service removes all active content including scripts and embedded objects. [18], [19] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | - | Inline malware protection uses the single FortiGuard AV engine with AI heuristic detection and FortiGate Cloud sandboxing; two or more independent AV engines scanning raw payloads in parallel are not documented. [1], [10] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Partial | medium | - | FortiOS DLP profiles can match Microsoft Information Protection (MIP) security labels attached to files and enforce block actions; this is data-loss-prevention label matching rather than domain-to-domain information flow control per security classification. [6] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Supported | medium | - | FortiOS DLP supports credit-card, SSN, keyword, hex and regex data types with block actions, FortiGuard DLP ships 500+ predefined patterns, and the datasheet confirms DLP-based exfiltration blocking. [1], [6], [17] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | FTP proxy and HTTPS/SSL inspection with antivirus cleaning are documented, and CIFS/SMB appears in the protocol-inspection list; SFTP and NFS proxying are not documented. [1], [11], [12] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | - | FortiGuard OT Security Service IPS signatures and DPI cover 80+ OT applications and protocols; the Rugged series also converts IEC 60870-5-101 to IEC 60870-5-104 and Modbus serial to Modbus TCP via Industrial Connectivity, with a documented DNP3 signature dissector. [1], [13], [14], [15] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Not Supported | medium | - | The documented FortiOS protocol-inspection set (HTTP, SMTP, POP3, IMAP, FTP, NNTP, MAPI, DNS, CIFS) includes no SQL Server, Oracle or PostgreSQL proxy, and no database query-whitelisting feature is documented. [11] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | FortiGate sends logs to up to four syslog servers or FortiSIEM devices in CSV or CEF formats (real-time relay confirmed); an RTSP video proxy is not documented in the staged sources. [9] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1500 Mbps | The FGR-70G NGFW throughput (firewall + IPS + application control, per the datasheet's enterprise traffic mix) is 1.5 Gbps, above the 1 Gbps threshold; the product page lists 1.1 Gbps threat-protection throughput for the 70G. [1], [2] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.00582 ms | Datasheet firewall latency for 64-byte UDP packets on the FGR-70G is 5.82 microseconds (0.00582 ms), well below the 10 ms threshold. [1] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | FGCP active-passive HA with session pickup preserves existing TCP sessions across automatic failover, but staged vendor docs give no explicit switchover-time figure, so the ≤100 ms requirement cannot be confirmed numerically. [3], [25] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | - | FortiOS DoS policies detect anomalies such as SYN/UDP/ICMP floods and scans on ingress interfaces and block the anomalous traffic before security policies are evaluated. [5] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | - | FortiOS administrator profiles grant granular per-area permissions (system, policy, log, VPN, etc.), separating a full system admin (super_admin) from lower-level policy and log/audit roles. [7] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Real-time log push to up to four syslog servers or FortiSIEM devices in CSV or CEF format is documented; a TLS-encrypted syslog transport is not documented in the staged sources. [9] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | - | FortiAnalyzer ships compliance report templates including ISO 27001:2022 and an OT (NERC CIP) compliance security rating report; explicit NIST SP 800-82 or IEC 62443 report templates are not named in the template list. [24] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | - | FortiOS 6.4.9/7.0.7/7.2.8 hold Common Criteria EAL4+ certificates (Netherlands scheme), the FortiGate Rugged 60F appears on NIST CMVP certificate #4497 (FIPS 140-2 Level 2), the Rugged series carries IEC 61850-3/IEEE 1613 certification, and Fortinet holds IEC 62443-4-1 ML2 process certification. [1], [16], [22], [23] |

---

## 4. Notable Strengths

- **OT protocol coverage (item 3.2):** FortiGuard OT Security Service signatures plus DPI cover 80+ OT applications/protocols, and the Rugged series adds serial-to-IP conversion for IEC 60870-5-101→104 and Modbus serial→TCP via Industrial Connectivity, with a documented DNP3 signature dissector [1][13][14][15].
- **Performance headroom (items 4.1, 4.2):** FGR-70G NGFW throughput of 1.5 Gbps exceeds the 1 Gbps threshold, and 64-byte UDP firewall latency of 5.82 µs (0.00582 ms) is far below the 10 ms ceiling [1].
- **Defense-in-depth inspection (items 1.3, 2.2, 2.6, 4.4):** implicit default-deny policy evaluation, macro-stripping content disarm for Office/PDF, DLP with credit-card/SSN/regex data types, and DoS anomaly policies that block attack traffic before security policies [5][6][8][19].
- **Certification depth (item 5.4):** FortiOS holds Common Criteria EAL4+ (6.4.9/7.0.7/7.2.8), the Rugged 60F is FIPS 140-2 Level 2 validated (CMVP #4497), and the series carries IEC 61850-3/IEEE 1613 industrial certifications [1][22][23].
- **Hardened, integrity-checked OS (item 1.4):** dually-signed firmware/AV/IPS engine images plus real-time file system integrity checking protect the FortiOS kernel and binaries [20][21].

## 5. Notable Gaps / Risks

- **No quantified HA switchover time (item 4.3):** FGCP active-passive HA with session pickup preserves sessions, but no source documents a ≤100 ms switchover figure, so the numeric threshold is unverified - resolve via a vendor HA benchmark before relying on sub-100 ms failover [3][25].
- **Single-engine antivirus (item 2.3):** inline malware scanning uses one FortiGuard AV engine (plus AI heuristics and cloud sandbox); the checklist's 2+ parallel-engine requirement is not met [1][10].
- **CDR is partial (item 2.1):** content disarm covers Office/PDF/RTF but Image/CAD formats and 100% reconstruction are not documented for the Rugged series; treat CDR as a file-sanitization add-on, not a full guard-engine capability [1][18][19].
- **No database protocol proxy (item 3.3):** the documented FortiOS protocol-inspection set contains no SQL Server/Oracle/PostgreSQL proxy or query whitelisting - sites needing database guard functionality must add a separate product [11].
- **Unverified TLS syslog and RTSP (items 5.2, 3.4):** CEF/syslog push to FortiSIEM is confirmed, but TLS-encrypted syslog transport and RTSP video proxying are not documented in the staged sources [9].

## 6. Evidence Quality Notes

Evidence was staged from 25 sources (22 vendor_doc, 1 vendor_datasheet, 2 certification registries) and 54 grounded quotes; every quote in evidence.jsonl is an exact substring of a persisted artifact. Seven items (2.1, 2.3, 2.6, 3.1, 3.2, 4.1, 5.4) draw on ≥2 source_types. Only item 5.4 reaches high confidence, backed by independent NIST CMVP and Common Criteria Portal registries plus the vendor datasheet [1][22][23]; all other items are vendor-documented and capped at medium by the validator rule.

The main evidence-quality limitation is the absence of independent (non-vendor) sources for feature claims: FortiOS 7.4.5 administration guide pages are authoritative for firewall behavior but vendor-authored, so feature-level verdicts (default-deny, RBAC, DLP, DoS) rest on single-vendor documentation. No source contradictions were found; the closest to tension is CDR availability (FortiOS native vs FortiGuard cloud, model-dependent per datasheet footnote), which is why item 2.1 is partial rather than supported. Items 3.3 and 5.2 were downgraded rather than forced: 3.3 to not_supported based on the vendor's own exhaustive protocol enumeration [11], and 5.2 to partial because TLS-encrypted syslog is not documented anywhere in the staged material [9].

---

## Bibliography

[1] Fortinet. "FortiGate Rugged Series Data Sheet". https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/FortiGate_Rugged_Series.pdf (Retrieved: 2026-08-11T08:55:27Z)
[2] Fortinet. "Fortinet Ruggedized Products (product page)". https://www.fortinet.com/products/rugged (Retrieved: 2026-08-11T08:55:27Z)
[3] Fortinet. "High Availability (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/666376/high-availability (Retrieved: 2026-08-11T08:56:54Z)
[4] Fortinet. "Session pickup (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/955521/session-pickup (Retrieved: 2026-08-11T08:56:54Z)
[5] Fortinet. "DoS policy (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/771644/dos-policy (Retrieved: 2026-08-11T08:56:54Z)
[6] Fortinet. "Basic DLP settings (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/919417/basic-dlp-settings (Retrieved: 2026-08-11T08:57:01Z)
[7] Fortinet. "Administrator profiles (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/294491/administrator-profiles (Retrieved: 2026-08-11T08:57:01Z)
[8] Fortinet. "Firewall policy (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/656084/firewall-policy (Retrieved: 2026-08-11T08:57:01Z)
[9] Fortinet. "Log settings and targets (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/250999/log-settings-and-targets (Retrieved: 2026-08-11T08:58:51Z)
[10] Fortinet. "Antivirus introduction (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/723287/antivirus-introduction (Retrieved: 2026-08-11T08:57:06Z)
[11] Fortinet. "Protocol options (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/5347/protocol-options (Retrieved: 2026-08-11T08:57:06Z)
[12] Fortinet. "FTP proxy (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/556943/ftp-proxy (Retrieved: 2026-08-11T08:57:06Z)
[13] Fortinet. "Industrial Connectivity (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/426842/industrial-connectivity (Retrieved: 2026-08-11T09:01:56Z)
[14] Fortinet. "Application signature dissector for DNP3 (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/896335/application-signature-dissector-for-dnp3 (Retrieved: 2026-08-11T09:02:05Z)
[15] Fortinet. "FortiGuard Operational Technology Security Service (product page)". https://www.fortinet.com/support/support-services/fortiguard-security-subscriptions/industrial-security (Retrieved: 2026-08-11T09:01:48Z)
[16] Fortinet. "Fortinet OT Security Solutions (product page)". https://www.fortinet.com/solutions/ot-security (Retrieved: 2026-08-11T08:57:33Z)
[17] Fortinet. "FortiGuard Data Loss Prevention Service (product page)". https://www.fortinet.com/support/support-services/fortiguard-security-subscriptions/data-loss-prevention (Retrieved: 2026-08-11T08:57:26Z)
[18] Fortinet. "FortiGuard Content Disarm & Reconstruction Service (product page)". https://www.fortinet.com/support/support-services/fortiguard-security-subscriptions/content-disarm-reconstruction (Retrieved: 2026-08-11T08:57:33Z)
[19] Fortinet. "Content disarm and reconstruction (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/788313/content-disarm-and-reconstruction (Retrieved: 2026-08-11T09:01:13Z)
[20] Fortinet. "BIOS-level signature and file integrity checking (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/249947/bios-level-signature-and-file-integrity-checking (Retrieved: 2026-08-11T09:02:59Z)
[21] Fortinet. "Real-time file system integrity checking (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/226732/real-time-file-system-integrity-checking (Retrieved: 2026-08-11T09:02:59Z)
[22] NIST / CMVP. "NIST CMVP Certificate #4497 - FortiGate Next-Generation Firewalls with FortiOS 6.4/7.0". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4497 (Retrieved: 2026-08-11T09:05:11Z)
[23] Common Criteria Portal. "Common Criteria Portal - Certified Products search for FortiOS". https://www.commoncriteriaportal.org/products/index.cfm?search=FortiOS (Retrieved: 2026-08-11T09:05:11Z)
[24] Fortinet. "List of report templates (FortiAnalyzer 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortianalyzer/7.4.5/administration-guide/2854/list-of-report-templates (Retrieved: 2026-08-11T09:03:35Z)
[25] Fortinet. "Failover protection (FortiOS 7.4.5 Administration Guide)". https://docs.fortinet.com/document/fortigate/7.4.5/administration-guide/489324/failover-protection (Retrieved: 2026-08-11T08:57:59Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 25 (kept: 25, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, vendor_datasheet: 1, vendor_doc: 22
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
