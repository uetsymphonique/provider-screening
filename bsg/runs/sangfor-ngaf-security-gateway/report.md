# BSG / Cross Domain Product Assessment: Sangfor Technologies — Sangfor NGAF Security Gateway (Athena NGFW / NSF series)

**Product ID:** `sangfor-ngaf-security-gateway`
**Version reference:** NGAF firmware 8.0.x family (datasheet throughput measured on 8.0.107; CyberRatings tested AF8.0.47.1004 EN R1)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T16:20:00Z
**Total evidence items collected:** 37
**Total distinct sources:** 15

---

## 1. Overview

Sangfor NGAF is a converged next-generation firewall appliance line (NSF hardware series plus virtual vNGAF) that the vendor now markets as "Sangfor Athena NGFW" (previously "Network Secure") [1]. The product page and NGAF brochure position it as an enterprise perimeter NGFW integrating firewall, IPS, antivirus, AI-based malware inspection (Engine Zero), cloud threat intelligence and sandboxing (Neural-X), a next-generation web application firewall, and SD-WAN in one appliance [1][3]. It is not marketed as a cross-domain solution or protocol-break guard, so the guard-specific checklist items are treated as not applicable rather than unverified. Deployments cover routed, transparent/bridge, virtual-wire, bypass and hybrid modes, in physical and virtual form factors, with centralized management via Platform-X / Sangfor Central Manager [2][3]. Independent validation comes from CyberRatings.org Enterprise Firewall tests ("Recommended" in 2023 and 2024) [4][5] and Gartner Magic Quadrant recognition (Visionary, 2022) [10].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 4     | 0                | 4      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 3 items backed by ≥ 2 source_types; 18 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Sangfor markets the product as a next-generation firewall using DPI-based inspection, not a protocol-break cross-domain guard; no TCP/IP session-termination with IP-routing separation is claimed.
- **1.2:** The vendor positions Athena NGFW as a standard next-generation firewall appliance; no dual-board FPGA/shared-memory isolation architecture is documented.
- **1.5:** Product category is a standard NGFW; no internal cryptographic data-stamping of sanitized content before new-session initiation is documented.
- **2.1:** The product is marketed as an NGFW, not a CDS/guard; content is inspected and malware removed from files, but no 100% content disarming and reconstruction (CDR) engine for Office/PDF/image/CAD formats is documented.
- **2.4:** No W3C-schema structural validation of XML/JSON/FIXM/AIXM documents is documented; the product category is NGFW rather than a CDS content-validation engine.
- **2.5:** No security-label (IFC)-based filtering of files is documented; the product category is NGFW.
- **2.7:** No anti-steganography inspection of image files is documented; the product category is NGFW.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Sangfor markets the product as a next-generation firewall using DPI-based inspection, not a protocol-break cross-domain guard; no TCP/IP session-termination with IP-routing separation is claimed. [1] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The vendor positions Athena NGFW as a standard next-generation firewall appliance; no dual-board FPGA/shared-memory isolation architecture is documented. [1] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | Vendor documents rule-based access control that allows or denies traffic per policy with first-match processing, but an explicit default-deny whitelist-only posture for unmatched traffic is not stated. [1], [2], [3] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No public documentation of the underlying OS hardening approach (hardened OS, microkernel or SELinux strict mode); the vendor's own advisory documents web-stack vulnerabilities (e.g. CVE-2023-30802) fixed in later firmware.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | Product category is a standard NGFW; no internal cryptographic data-stamping of sanitized content before new-session initiation is documented. [1] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | The product is marketed as an NGFW, not a CDS/guard; content is inspected and malware removed from files, but no 100% content disarming and reconstruction (CDR) engine for Office/PDF/image/CAD formats is documented. [1] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (File filtering and malware removal are documented, but no macro/script removal capability (VBA, JavaScript, DDE links, embedded objects) is described.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Supported | medium | — | Vendor documents multiple gateway malware-inspection engines (signature AV, AI-based Engine Zero, Neural-X cloud sandbox and threat intelligence) inspecting HTTP, HTTPS, FTP, SMB, SMTP, POP3 and IMAP payloads. [2], [3] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | No W3C-schema structural validation of XML/JSON/FIXM/AIXM documents is documented; the product category is NGFW rather than a CDS content-validation engine. [1] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label (IFC)-based filtering of files is documented; the product category is NGFW. [1] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Supported | medium | — | Vendor documents data-leakage detection and prevention over customizable sensitive-information types including identity-card numbers, bank/credit-card numbers and phone numbers, plus file-download control. [3] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No anti-steganography inspection of image files is documented; the product category is NGFW. [1] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | FTP, HTTPS and SMB traffic are documented for inspection (malware scanning with SSL decryption and an FTP ALG), but SFTP and NFS proxying with content cleaning are not documented. [2] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found (Only IoT asset discovery and a dedicated IoT IPS signature database are documented; no OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT industrial protocol proxy is described.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (IPS/WAF protect against database exploits and SQL injection at the web layer, but no SQL Server/Oracle/PostgreSQL protocol proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | RTSP is supported via an application-layer gateway (ALG) and logs are exported in CEF to multiple syslog servers, but explicit unidirectional/bidirectional relay semantics are not documented. [2] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 19000 Mbps | Datasheet lists NGFW throughput of 19 Gbps (19,000 Mbps) for the NSF-7100A-I with firewall, application control and IPS enabled, exceeding the 1 Gbps requirement; CyberRatings measured a rated throughput of 5,782 Mbps on the NGAF 5300. [2], [7] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No processing or forwarding latency figure is published in the datasheet, brochure, or press material.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Active-Active/Active-Standby HA with hardware bypass is documented with failover time 'less than 1 second', a qualitative figure that does not demonstrate the 100 ms switchover target. [2], [3] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | Device-level DoS/DDoS protection is documented and hardware bypass (fail-open on hardware failure) is provided; an explicit fail-close boundary lockout under DoS is not documented. [2], [3] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | — | Vendor documents role-based admin authorization with default roles of security admin, system admin, and audit admin. [2] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | CEF-format syslog export to multiple target servers and RESTful APIs for third-party SIEM/SOC integration are documented, but TLS encryption of the syslog transport channel is not explicitly stated. [2] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | A built-in report center with scheduled PDF security reports is documented, but compliance-standard report templates (NIST SP 800-82, IEC 62443, ISO 27001) are not mentioned. [2], [3] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | — | The product holds ICSA Labs firewall certification (2021) and independent CyberRatings 'Recommended' ratings, but no Common Criteria or FIPS 140-3 entry appears in the official registries, and no national cryptographic certification was found. [1], [2], [4], [14], [15] |

---

## 4. Notable Strengths

- **Multi-engine malware inspection (items 2.3, 2.6):** the datasheet and brochure document signature AV, the AI-based Engine Zero, and Neural-X cloud sandbox/threat intelligence inspecting HTTP, HTTPS, FTP, SMB, SMTP, POP3 and IMAP payloads, plus data-leakage detection over customizable sensitive-data types such as identity-card, bank-card and phone numbers [2][3].
- **RBAC admin separation (item 5.1):** default roles of security admin, system admin and audit admin are documented on the NSF-7100A-I datasheet, matching the requirement's separation of system, policy and auditor roles [2].
- **Inspection throughput (item 4.1):** the NSF-7100A-I datasheet rates NGFW throughput at 19 Gbps (19,000 Mbps) with firewall, application control and IPS enabled, an order of magnitude above the 1 Gbps requirement; CyberRatings measured a 5,782 Mbps rated throughput on the NGAF 5300 [2][7].
- **Independent security-effectiveness validation (item 5.4):** CyberRatings.org awarded "Recommended" ratings in its 2023 and 2024 Enterprise Firewall tests of the Sangfor NGAF 5300, and ICSA Labs endorsed the product in 2021 [4][1].
- **HA and device self-protection (items 4.3, 4.4):** Active-Active/Active-Standby HA with hardware bypass and device-level DoS/DDoS attack protection are documented on the datasheet and brochure [2][3].

## 5. Notable Gaps / Risks

- **No explicit default-deny posture documented (item 1.3):** access control is rule-based with first-match processing; a whitelist-only default-deny mode is not stated, so buyers should verify default handling of unmatched traffic in a lab.
- **HA failover does not demonstrate the 100 ms target (item 4.3):** the vendor documents failover "less than 1 second"; if session-preserving sub-100 ms switchover is required, a measured failover test against the requirement is needed.
- **No processing-latency figure published (item 4.2):** realtime protocol latency of 10 ms or less is unverified; no datasheet, brochure or press material states a forwarding/processing latency.
- **No OT/ICS or database protocol proxying documented (items 3.2, 3.3):** only IoT asset discovery and a dedicated IoT IPS signature database are described; OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT and SQL Server/Oracle/PostgreSQL proxy support are absent from public documentation.
- **Certification shortfall versus the checklist (item 5.4):** ICSA Labs and CyberRatings recognition is documented, but no Common Criteria or FIPS 140-3 entry appears in the official registries and no national cryptographic certification was found; the required certifications would need to be obtained or re-scoped.

## 6. Evidence Quality Notes

Fifteen distinct sources were staged and 37 evidence quotes were extracted; every quote was verified as an exact substring of the staged artifact text by the grounding check, including two full-list registry pages (NIST CMVP, Common Criteria portal). Independent, non-vendor sources were obtained for this product: the CyberRatings.org 2023 Q2 and 2024 Q2 Enterprise Firewall report pages and the two certification registries, despite all general search engines returning anti-bot blocks in this environment (discovery proceeded by direct site navigation of the vendor sitemap/news, cyberratings.org resource library, and the registries).

Only three items (1.3, 4.1, 5.4) are backed by two or more source types; the remaining feature-level verdicts rest on the vendor product page, datasheet and brochure, so confidence is capped at medium across the board. No direct contradictions were found between sources; the throughput figures differ (19 Gbps datasheet NGFW-mix versus 5,782 Mbps CyberRatings rated throughput) because they are measured under different inspection stacks and traffic profiles, which the 4.1 note reflects. Registry absence was used only where the registry is the complete official list (no Sangfor entries in CMVP or the CC certified-products list), supporting the 5.4 partial verdict as absence from authoritative registries rather than vendor silence.

---

## Bibliography

[1] Sangfor Technologies. "Sangfor Athena NGFW – AI-Powered Next Generation Firewall (product page)". https://www.sangfor.com/cybersecurity/sangfor-athena-foundation/next-generation-firewall-ngfw (Retrieved: 2026-08-11T09:11:51Z)
[2] Sangfor Technologies. "Athena NGFW NSF-7100A-I Datasheet (2026-05)". https://www.sangfor.com/sites/default/files/2026-05/Athena-NGFW-Datasheet-NSF-7100A-I.pdf (Retrieved: 2026-08-11T09:11:51Z)
[3] Sangfor Technologies. "Sangfor NGAF Next Generation Firewall Brochure (NGAF_BR_P_NGAF-Brochure_20240319)". https://www.sangfor.com/sites/default/files/2024-03/NGAF_BR_P_NGAF-Brochure_20240319.pdf (Retrieved: 2026-08-11T09:11:51Z)
[4] CyberRatings.org. "2023 Q2 Enterprise Firewall Report – Sangfor (CyberRatings.org)". https://cyberratings.org/resources/2023-q2-enterprise-firewall-report-sangfor/ (Retrieved: 2026-08-11T09:11:51Z)
[5] CyberRatings.org. "2024 Q2 Enterprise Firewall Report – Sangfor (CyberRatings.org)". https://cyberratings.org/resources/2024-q2-enterprise-firewall-report-sangfor/ (Retrieved: 2026-08-11T09:11:51Z)
[6] Innotel (Sangfor distributor). "Sangfor NGAF – Sản phẩm khuyến nghị sử dụng của CyberRatings.org (Innotel distributor blog)". https://sangfor.com.vn/sangfor-ngaf-san-pham-khuyen-nghi-su-dung-cua-cyberrating-org.html (Retrieved: 2026-08-11T09:11:51Z)
[7] Sangfor Technologies. "Sangfor NGAF Achieves Recommended Rating in CyberRatings.org's Enterprise Firewall Test (press release)". https://www.sangfor.com/news-and-press-release/sangfor-ngaf-achieves-recommended-rating-in-2023-cyberratings-enterprise-firewall-test (Retrieved: 2026-08-11T09:11:51Z)
[8] Sangfor Technologies. "Sangfor NGAF Receives AAA Rating from CyberRatings (press release)". https://www.sangfor.com/news-and-press-release/sangfor-ngaf-receives-aaa-rating-cyberratings (Retrieved: 2026-08-11T09:11:51Z)
[9] Sangfor Technologies. "Sangfor Recommended Again in CyberRatings.org 2024 Enterprise Firewall Test (press release)". https://www.sangfor.com/news-and-press-release/sangfor-recommended-again-cyberratingsorg-2024-enterprise-firewall-test (Retrieved: 2026-08-11T09:11:51Z)
[10] Sangfor Technologies. "Sangfor Named as a Visionary in 2022 Gartner Magic Quadrant for Network Firewalls (press release)". https://www.sangfor.com/news-and-press-release/visionary-2022-gartner-magic-quadrant-for-network-firewalls (Retrieved: 2026-08-11T09:11:51Z)
[11] Sangfor Technologies. "IDC Latest Report: Sangfor Next-Generation Firewall Ranked 1st in China (press release)". https://www.sangfor.com/news-and-press-release/idc-latest-report-sangfor-next-generation-firewall-ranked-1st-china (Retrieved: 2026-08-11T09:11:51Z)
[12] Sangfor Technologies. "Sangfor Releases Major Update for NGAF 8.0.26 with Advanced Malware Protection (blog)". https://www.sangfor.com/blog/cybersecurity/sangfor-releases-major-update-ngaf-8-0-26-advanced-malware-protection (Retrieved: 2026-08-11T09:11:51Z)
[13] Sangfor Technologies. "Official Advisory on Reported Vulnerabilities in Sangfor NGAF". https://www.sangfor.com/news-and-press-release/official-advisory-on-reported-vulnerabilities-sangfor-ngaf (Retrieved: 2026-08-11T09:11:51Z)
[14] NIST CSRC. "NIST CMVP – Validated Cryptographic Modules (full list incl. FIPS 140-1/2/3)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all (Retrieved: 2026-08-11T09:11:51Z)
[15] Common Criteria Portal. "Common Criteria Portal – Certified Products (full list)". https://www.commoncriteriaportal.org/products/index.cfm (Retrieved: 2026-08-11T09:11:51Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 15 (kept: 15, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, third_party_review: 2, vendor_blog: 7, vendor_datasheet: 2, vendor_doc: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
