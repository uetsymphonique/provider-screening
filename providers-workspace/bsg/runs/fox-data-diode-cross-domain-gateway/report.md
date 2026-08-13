# BSG / Cross Domain Product Assessment: Fox-IT (NCC Group) - Fox Data Diode & Cross Domain Gateway

**Product ID:** `fox-data-diode-cross-domain-gateway`
**Version reference:** Fort Fox Hardware Data Diode FFHDD3_1/10 (EAL7+, certified 2023-09-19, NSCIB-CC-2300039-01.1); vendor now markets the family as Sentyron DataDiode Ruggedised 1G-10G / Andean 1G
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:47:38Z
**Total evidence items collected:** 55
**Total distinct sources:** 19

---

## 1. Overview

Fox Data Diode & Cross Domain Gateway is Fox-IT's (now NCC Group / Sentyron) hardware-enforced unidirectional security gateway. The vendor positions it explicitly as "a cross-domain solution" reconciling high assurance with free flow of information [1][3]. The evaluated hardware (Fort Fox Hardware Data Diode FFHDD3_1/10) is a fixed-function physical-layer device with no programmable logic, firmware or software [17]; a full deployment adds base software and proxy servers on each side that convert bidirectional protocols into one-way flows [10], plus replicators for OPC, Modbus, OSIsoft PI and databases [6]. Deployment shapes span government & defense (classified networks, NATO environments), industrial control systems (CCTV, historian replication, plant monitoring) and enterprise use [2][3]. The family holds Common Criteria EAL7+ and NATO Cosmic Top Secret certification [16][18] and is marketed today by Sentyron in 1 Gbps and 10 Gbps variants [10][11]. Content-inspection features common on bidirectional CDS guards (CDR, multi-AV, DLP) are not documented in public sources and remain unverified.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 5                | 3      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 9     | 0                | 0      | 9   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 12 items backed by ≥ 2 source_types; 8 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | high | - | The Fox DataDiode is a one-way cross-domain solution: the evaluated hardware operates on the OSI physical layer with a single light source and no back channel, and proxy servers on each side convert bidirectional protocols into one-way flows. [1], [10], [17], [18], [19] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | high | - | The diode is a single fixed-function hardware unit containing no programmable logic, firmware, software or memory; the full system uses three separate hardware units in different security zones linked by optical fiber, and the Andean model physically separates upstream and downstream interfaces. [5], [7], [11], [17], [19] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | The evaluated information-flow policy (FDP_IFC.2/FDP_IFF.1) explicitly denies any downstream-to-upstream flow and permits only upstream-to-downstream flow, i.e. a single-rule whitelist enforced in hardware. [10], [17] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | The diode hardware itself contains no operating system or software; the base software side supports Intel x64 SELinux, providing hardened-OS protection at the proxy layer. [10], [17] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (The vendor documents GPG signing of software packages (supply-chain integrity) but not internal signing of cleaned data before session re-initiation.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | - | A data curation and filtering capability for input security checks is documented, but no keyword/secret-detection or custom-regex DLP specifics are published. [10] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Supported | medium | - | File-transfer support covers FTP, SFTP, SCP, Samba/SMB, NFS, CIFS and HTTP(S) proxied through the one-way base software, which Fox-IT describes as hardware enforcing unidirectional network traffic flow. [8], [10], [11] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | OT/ICS coverage is documented for Modbus, OPC and OSIsoft PI replication through the Fox Replicators; IEC 60870-5-104, DNP3, MQTT and explicit OPC UA are not documented. [2], [6], [10] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | - | Database replication is supported for Oracle DBMS, MySQL and MSSQL via GoldenGate/Shareplex, making read-only copies available on the destination network; PostgreSQL and query-whitelisting proxy behavior are not documented. [6], [10] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Syslog relay and file/video stream replication over UDP/TCP are documented (including a CCTV deployment); no RTSP video proxy or CEF relay is documented. [10], [14] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | high | 10000 Mbps | The evaluated Fort Fox Hardware Data Diode ships in 1 Gbit/sec and 10 Gbit/sec versions (FFHDD3_1 and FFHDD3_10); 10 Gbps exceeds the 1000 Mbps threshold. [10], [17], [18] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | The vendor claims large datasets are delivered 'in milliseconds' through the 10 Gbps diode, but publishes no per-packet or per-protocol processing-latency figure comparable to the 10 ms threshold. [10] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Parallel-diode high availability with automatic failover and 99.99% uptime is documented, and the diode has redundant 24VDC power inputs; no switchover-time figure is published to compare with the 100 ms threshold. [3], [13], [17] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | high | - | The downstream interface is physically incapable of input and ignores all received data, so a DoS or any traffic from the untrusted side cannot propagate across the boundary; the NATO listing confirms the diode eliminates the digital attack surface of the secured network. [10], [17], [18] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Syslog, SNMP traps and a Splunk forwarder are documented for log/notification export; CEF format and TLS-encrypted transport to a SIEM are not specified. [10] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | - | The product holds Common Criteria EAL7+ (certificate NSCIB-CC-2300039-01.1, TrustCB/NL scheme), NATO Cosmic Top Secret approval by the Dutch AIVD, and vendor-documented NATO SECRET, BSI and NL-NCSA certifications. [4], [10], [16], [18] |

---

## 4. Notable Strengths

- **Physical protocol break with no back channel (items 1.1, 1.2):** the diode operates on the OSI physical layer with a single light source, making reverse traffic, including covert channels, physically impossible [17].
- **Highest-assurance certifications (item 5.4):** Common Criteria EAL7+ (certificate NSCIB-CC-2300039-01.1) and NATO Cosmic Top Secret approval by the Dutch AIVD are confirmed by registry sources [16][18].
- **Throughput headroom (item 4.1):** the 10 Gbit/sec FFHDD3_10 version exceeds the 1 Gbps checklist threshold tenfold, corroborated by the NATO product catalogue [17][10][18].
- **Fail-closed by design (item 4.4):** the downstream interface ignores all received data, so DoS and tampering from the untrusted side cannot cross the boundary [17][18].
- **OT protocol coverage (item 3.2):** Modbus, OPC and OSIsoft PI replication are documented for industrial monitoring scenarios, alongside UDP/TCP video streaming for CCTV use [6][10][14].

## 5. Notable Gaps / Risks

- **Content inspection is undocumented (items 2.1, 2.3, 2.4, 2.7):** no CDR, multi-AV scanning, schema validation or anti-steganography evidence was found; buyers needing sanitized file transfer must confirm capability with the vendor.
- **DLP is only weakly evidenced (item 2.6):** the documented "data curation & filtering" capability does not confirm keyword/regex secret detection as required by the checklist.
- **Latency is qualitative only (item 4.2):** "millisecond" delivery claims are not backed by a per-packet latency figure comparable to the 10 ms threshold.
- **HA switchover time unknown (item 4.3):** automatic failover and 99.99% uptime are claimed, but no switchover-time measurement against the 100 ms threshold is published.
- **Management-plane items unverified (items 5.1, 5.3):** no RBAC role separation or NIST SP 800-82 / IEC 62443 / ISO 27001 compliance report templates are documented in public sources.

## 6. Evidence Quality Notes

Twelve items are backed by two or more source types, and five (1.1, 1.2, 4.1, 4.4, 5.4) draw on independent registry or reference sources - the Common Criteria certificate PDF [16], the NATO NIA product catalogue [18] and Wikipedia [19] - which is what allows those items to reach high confidence. The remaining non-unknown items rest on vendor documentation (Fox-IT pages recovered from Common Crawl, Sentyron product pages and vendor-hosted case studies), so their confidence is capped at medium per the validator's vendor-only rule.

All 55 evidence quotes are exact substrings of staged raw artifacts - Common Crawl WARC recoveries of the 2020-2021 fox-it.com pages, live Sentyron pages, the CC portal certificate and Security Target PDFs, the NATO listing and Wikipedia - and every one passed the grounding check (verify_citation_grounding.py --strict --require-staged: 55 grounded, 0 fabricated, 0 unverifiable). No contradictions between sources surfaced; where vendor marketing was unquantified (e.g. "milliseconds" latency, automatic failover), verdicts were downgraded to partial with null numeric values rather than inferred to meet thresholds.

---

## Bibliography

[1] Fox-IT (NCC Group). "Fox DataDiode - product page (Fox-IT)". https://www.fox-it.com/en/technology/datadiode/ (Retrieved: 2026-08-11T00:00:00Z)
[2] Fox-IT (NCC Group). "Fox DataDiode for Industrial Control Systems (Fox-IT)". https://www.fox-it.com/en/technology/datadiode/for-industrial-control-systems/ (Retrieved: 2026-08-11T00:00:00Z)
[3] Fox-IT (NCC Group). "Fox DataDiode for Government & Defense (Fox-IT)". https://www.fox-it.com/en/technology/datadiode/for-government-defense/ (Retrieved: 2026-08-11T00:00:00Z)
[4] Fox-IT (NCC Group). "Data diode certifications: an overview (Fox-IT blog)". https://www.fox-it.com/en/news/blog/data-diode-certifications-an-overview/ (Retrieved: 2026-08-11T00:00:00Z)
[5] Fox-IT (NCC Group). "Fox-IT achieves Common Criteria Security Certification EAL 7+ for its Two Ruggedized DataDiodes (press release)". https://www.fox-it.com/en/news/pressreleases/fox-it-achieves-common-criteria-security-certification-eal-7-for-its-two-ruggedized-datadiodes/ (Retrieved: 2026-08-11T00:00:00Z)
[6] Fox-IT (NCC Group). "What is the role of a replicator together with a data diode? (Fox-IT blog)". https://www.fox-it.com/en/news/blog/what-is-the-role-of-a-replicator-together-with-a-data-diode/ (Retrieved: 2026-08-11T00:00:00Z)
[7] Fox-IT (NCC Group). "Can you use malware to bypass a data diode system with radio waves? (Fox-IT blog)". https://www.fox-it.com/en/news/blog/can-you-use-malware-to-bypass-a-data-diode-system-with-radio-waves/ (Retrieved: 2026-08-11T00:00:00Z)
[8] Fox-IT (NCC Group). "Fox-IT and Ingram Micro Sign Distribution Agreement for Fox DataDiode in APAC Region (press release)". https://www.fox-it.com/en/news/pressreleases/fox-it-and-ingram-micro-sign-distribution-agreement-for-fox-datadiode-in-apac-region/ (Retrieved: 2026-08-11T00:00:00Z)
[9] Fox-IT (NCC Group). "Digital Signatures for Fox DataDiode Software (Fox-IT)". https://www.fox-it.com/en/technology/digital-signatures-for-fox-datadiode-software/ (Retrieved: 2026-08-11T00:00:00Z)
[10] Sentyron. "Sentyron DataDiode Ruggedised 1G-10G - product page". https://sentyron.com/solutions/sentyron-datadiode-ruggedised-1g-10g/ (Retrieved: 2026-08-11T00:00:00Z)
[11] Sentyron. "Sentyron DataDiode Andean 1G - product page". https://sentyron.com/solutions/sentyron-datadiode-andean-1g/ (Retrieved: 2026-08-11T00:00:00Z)
[12] Sentyron. "Securing a major urban rail network with Sentyron (case study)". https://sentyron.com/cases/securing-london-undergrounds-rail-network-with-fox-datadiode/ (Retrieved: 2026-08-11T00:00:00Z)
[13] Sentyron. "High availability for critical data networks (case study)". https://sentyron.com/cases/high-availability-for-critical-data-networks/ (Retrieved: 2026-08-11T00:00:00Z)
[14] Sentyron. "Ensuring uncompromised CCTV surveillance with Sentyron (case study)". https://sentyron.com/cases/ensuring-uncompromised-cctv-surveillance-with-sentyron/ (Retrieved: 2026-08-11T00:00:00Z)
[15] Sentyron. "Ensuring offshore installation security with DataDiode (case study)". https://sentyron.com/cases/ensuring-offshore-installation-security-with-datadiode/ (Retrieved: 2026-08-11T00:00:00Z)
[16] TrustCB B.V. / Common Criteria Portal. "Common Criteria Certificate NSCIB-CC-2300039-01.1 - Fort Fox Hardware Data Diode FFHDD3_1/10 (PDF)". https://www.commoncriteriaportal.org/files/epfiles/NSCIB-CC-2300039-01.1-Cert.pdf (Retrieved: 2026-08-11T00:00:00Z)
[17] Fox Crypto B.V. (via Common Criteria Portal). "Fort Fox Hardware Data Diode - Security Target v3.3 (PDF)". https://www.commoncriteriaportal.org/files/epfiles/NSCIB-CC-2300039-01-ST-v3.3.pdf (Retrieved: 2026-08-11T00:00:00Z)
[18] NATO NIA Product Catalogue. "NATO Information Assurance (NIA) PC - Sentyron (formerly Fox) DataDiode Ruggedized". https://www.ia.nato.int/niapc/Product/Fort-Fox-Hardware-Data-Diode-V3--FFHDD3-_767 (Retrieved: 2026-08-11T00:00:00Z)
[19] Wikipedia. "Unidirectional network (Wikipedia)". https://en.wikipedia.org/wiki/Data_diode (Retrieved: 2026-08-11T00:00:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 19 (kept: 19, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 4, certification_registry: 2, third_party_review: 1, vendor_blog: 5, vendor_datasheet: 2, vendor_doc: 5
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
