# BSG / Cross Domain Product Assessment: Lancs Networks — BSGW Secure Gateway

**Product ID:** `bsgw-secure-gateway`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:31:29Z
**Total evidence items collected:** 26
**Total distinct sources:** 11

---

## 1. Overview

BSGW Secure Gateway (Cổng bảo mật hai chiều BSGW) is a bidirectional security gateway developed by Lancs Networks, a Vietnamese network-technology vendor, and is positioned as a cross-domain solution for secure data transmission between secure and unsecure (IT/OT) network layers, leveraging Data Diode and USGW technology [1, 2]. The solution comprises three components: Gateway A, the single connection point to the untrusted external network; Core Processors that convert network protocols into product-specific protocols and back; and Gateway B, the connection point to the protected network [1, 2]. Both gateways integrate Zero Trust authentication, firewall policies, IDS/IPS, anti-virus and VPN transport [2]. The product family is built on the company's in-house core technologies — the Lancs NOS network operating system, Lancs FPGA packet-processing platform and Lancs Trust authentication technology — which also underpin the wider LINKSAFE ecosystem [4, 5, 6, 8]. Public documentation is thin: two short product pages, company technology pages and news items; no datasheet, admin guide or independent test report was located.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 9     | 0                | 9      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 14    | 0                | 0      | 14  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 1 items backed by ≥ 2 source_types; 9 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | — | The BSGW Core Processor converts network protocols into product-specific protocols and back, and the vendor positions the solution as leveraging Data Diode and USGW technology, indicating a protocol-break architecture between Gateway A and B. No IP-routing path between the two gateways is described. [1], [2] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | — | The BSGW solution is a three-component design with Gateway A (untrusted side) and Gateway B (protected side) as separate connection points linked through Core Processors, and the platform uses Lancs FPGA packet-processing technology. A two-board design connected via FPGA or isolated shared memory is not explicitly documented. [1], [5] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | Both BSGW gateways authenticate every connection (Zero Trust) and apply firewall policies, consistent with an allow-by-policy posture, but an explicit whitelist-only default-deny of all unlisted packets/protocols is not documented. [1], [2] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | Lancs security products, including the BSGW platform, run on the proprietary in-house Lancs NOS operating system that provides full network and security features, per the vendor and independent coverage. Microkernel or SELinux-strict-mode hardening is not documented. [4], [8], [11] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No mention of internal data stamping or signing of clean data before session initiation is made anywhere in the staged BSGW or platform pages.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No CDR / disarm-and-reconstruct capability for Office, PDF, image or CAD formats is documented; the product page lists only anti-virus among content-inspection features.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No macro, script, DDE-link or embedded-object removal is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | The BSGW page documents an anti-virus capability on both Gateway A and Gateway B for handling malicious external content, but no antivirus engine count or parallel multi-engine scanning is specified. [1], [2] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No XML/JSON/FIXM/AIXM schema validation is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No security-label-based information flow control is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No DLP keyword/regex blocking is documented for BSGW; the vendor offers a separate LINKSAFE DLP product not described as part of BSGW.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No anti-steganography capability for PNG/JPEG/BMP is documented.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No file-transfer protocol support (SFTP, FTP/S, HTTPS, SMB/NFS proxy) is documented for BSGW.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | BSGW is positioned for secure data transmission between secure/unsecure (IT/OT) network layers, but no specific OT/ICS protocol support (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) is documented. [1] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No database protocol proxying (SQL Server, Oracle, PostgreSQL) is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No realtime stream relay (RTSP video proxy, Syslog/CEF relay) is documented.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | The only quantitative bandwidth figures are for the underlying Lancs FPGA platform (10 Mbps-200 Gbps network interface) and the shared-memory IP core (up to ~2 T Gbps); the vendor publishes no BSGW product-level throughput, so the >=1000 Mbps requirement is unverified. [5], [7] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | The vendor claims very low packet-forwarding latency for the Lancs FPGA platform (200 Gbps with extremely low latency) and 16 ns/192 ns core latency for the shared-memory IP core, but no BSGW product-level processing latency is published. [5], [7] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found (No HA active-standby configuration or switchover time is documented.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No fail-safe/fail-close behavior under denial-of-service is documented.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Gateway A and Gateway B are configured through different management systems and administrators, providing administrative separation between the two security domains. Role-based separation of system admin, policy admin and auditor is not documented. [1], [2], [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (No SIEM/SOAR log export (CEF/Syslog over TLS) is documented for BSGW; a separate LINKSAFE SIEM product exists in the vendor ecosystem but BSGW integration is not described.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | The vendor reports applying ISO 9001:2015 and ISO/IEC 27001:2013 across its operations, covering the ISO 27001 element of the requirement at organizational level. Product-level compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) are not documented. [10] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | — | no evidence found (No Common Criteria, FIPS 140-3 or national cryptographic ('Chứng nhận Cơ yếu') certification was found in public registries (Common Criteria portal and NIST CMVP searched, no entries); company-level ISO/IEC 27001:2013 adoption is reported but is not one of the required product certifications.) |

---

## 4. Notable Strengths

- **Protocol-break architecture (item 1.1):** Core Processors convert network protocols into product-specific protocols and back between Gateway A and Gateway B, and the vendor cites Data Diode/USGW heritage, matching the defining mechanism of a bidirectional security gateway [1, 2].
- **Dual security-domain design (items 1.2, 5.1):** Gateway A (untrusted) and Gateway B (protected) are separate connection points managed by different administrators and management systems, providing strong domain separation [1, 2, 3].
- **Zero Trust posture (item 1.3):** every connection is authenticated on both gateways, and the vendor's Lancs Trust technology (SmartCard/Token authentication on Lancs NOS) is the Zero-Trust basis of its security products [2, 6].
- **In-house technology stack (items 1.4, 4.1):** the platform runs on Lancs' proprietary Lancs NOS and FPGA-based packet processing (10 Mbps-200 Gbps interface bandwidth), a self-developed core stack that reduces third-party software dependency [4, 5, 8].
- **Content-inspection baseline (item 2.3):** anti-virus handling of malicious external content is included on both gateways [1, 2].

## 5. Notable Gaps / Risks

- **Deep-inspection engine undocumented (items 2.1, 2.2, 2.4, 2.7):** no CDR, macro-removal, schema validation or anti-steganography capability is published; a buyer needing content disarm of Office/PDF files would require vendor confirmation.
- **No protocol matrix (items 3.1, 3.2, 3.3, 3.4):** only a generic IT/OT positioning is given; OPC UA, Modbus, IEC 60870-5-104, DNP3, SFTP, database or realtime-stream proxying are all unverified [1].
- **Throughput and latency unquantified at product level (items 4.1, 4.2):** quantitative figures exist only for the underlying FPGA platform and shared-memory IP core [5, 7]; no BSGW datasheet figure exists, so a >=1 Gbps throughput or <=10 ms latency commitment cannot be confirmed.
- **HA and fail-safe behavior undocumented (items 4.3, 4.4):** no active-standby switchover time or fail-close behavior under denial-of-service is described.
- **Certifications thin (item 5.4):** no Common Criteria, FIPS 140-3 or national cryptographic certification was found in public registries; only organizational ISO 9001/27001 adoption is reported [10].

## 6. Evidence Quality Notes

Evidence is dominated by vendor documentation: 9 of 11 staged sources are vendor pages (product pages, core-technology pages, vendor news), and only two are independent media — the Tạp chí Khoa học và Công nghệ Việt Nam article [8] and the Báo Khoa học & Phát triển article, which is a vendor-hosted reprint [9]. No analyst reports, lab tests, certification-registry entries or procurement records mentioning BSGW were found; checks of the Common Criteria portal and NIST CMVP returned no Lancs entries. Consequently no item reaches high confidence: 1 item is supported (1.1) and 9 are partial, all at medium confidence, and 14 items are unknown for absence of evidence rather than demonstrated absence of capability.

Items 1.4, 4.1 and 4.2 were partially triangulated — the NOS/FPGA platform claims are corroborated by independent coverage [8, 9] and the VNCERT working-session report [11] — but the capabilities those claims feed (hardened OS, product-level throughput and latency) remain unverified at product level, so those verdicts were kept partial rather than promoted to supported. No contradictions between sources were observed; the dominant limitation is silence, not conflict. A full BSGW datasheet, admin guide or a vendor technical Q&A would be required to move the 14 unknown items forward.

---

## Bibliography

[1] Lancs Networks. "Giải pháp Gateway Bảo mật hai chiều BSGW". https://lancsnet.com/giai-phap-gateway-bao-mat-hai-chieu-bsgw/ (Retrieved: 2026-08-11T08:27:52Z)
[2] Lancs Networks. "Bidirectional Security Gateways BSDW Solution". https://lancsnet.com/bidirectional-security-gateways-bsdw-solution/ (Retrieved: 2026-08-11T08:27:58Z)
[3] Lancs Networks. "Bidirectional Security Gateways BSDW Solution (English site)". https://en.lancsnet.com/bidirectional-security-gateways-bsdw-solution/ (Retrieved: 2026-08-11T08:27:58Z)
[4] Lancs Networks. "Hệ Điều Hành LANCS NOS". https://lancsnet.com/he-dieu-hanh-lancs-nos/ (Retrieved: 2026-08-11T08:28:00Z)
[5] Lancs Networks. "Công Nghệ LANCS FPGA". https://lancsnet.com/cong-nghe-lancs-fpga/ (Retrieved: 2026-08-11T08:28:00Z)
[6] Lancs Networks. "Công Nghệ LANCS TRUST". https://lancsnet.com/cong-nghe-lancs-trust/ (Retrieved: 2026-08-11T08:28:00Z)
[7] Lancs Networks. "Lancs Shared Memory IPCore". https://lancsnet.com/lancs-shared-memory-ipcore-2/ (Retrieved: 2026-08-11T08:28:01Z)
[8] Tạp chí Khoa học và Công nghệ Việt Nam. "Tích hợp công nghệ FPGA, ARM và PUF, Lancs Networks từng bước tự chủ công nghệ mạng". https://vjst.vn/tich-hop-cong-nghe-fpga-arm-va-puf-lancs-networks-tung-buoc-tu-chu-cong-nghe-mang-69281.html (Retrieved: 2026-08-11T08:28:04Z)
[9] Báo Khoa học & Phát triển Việt Nam (reprinted by Lancs Networks). "Lancs Networks dùng FPGA để giải quyết bài toán an ninh mạng (reprint of Báo Khoa học & Phát triển)". https://lancsnet.com/lancs-networks-dung-fpga-de-giai-quyet-bai-toan-an-ninh-mang/ (Retrieved: 2026-08-11T08:28:05Z)
[10] Lancs Networks. "Tổng Cục Tiêu chuẩn Đo lường Chất lượng tham quan Lancs Networks: ISO 9001:2015 & ISO/IEC 27001:2013". https://lancsnet.com/tong-cuc-tieu-chuan-do-luong-chat-luong-tham-quan-va-lam-viec-voi-lancs-networks-ve-viec-ap-dung-he-thong-quan-ly-chat-luong-va-an-toan-thong-tin-iso-90012015-iso-iec-270012013/ (Retrieved: 2026-08-11T08:28:05Z)
[11] Lancs Networks. "Lancs Networks làm việc với Trung tâm Ứng cứu khẩn cấp không gian mạng Việt Nam (VNCERT/CC)". https://lancsnet.com/trien-vong-dong-gop-cua-cong-nghe-viet-cho-hoat-dong-dam-bao-an-toan-an-ninh-mang-quoc-gia-lancs-networks-lam-viec-voi-trung-tam-ung-cuu-khan-cap-khong-gian-mang-viet-nam/ (Retrieved: 2026-08-11T08:28:05Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** ['site:lancsnet.com BSGW', 'lancsnet.com/?s=BSGW', 'lancsnet.com/?s=data+diode', 'lancsnet.com/?s=USGW', '"Lancs Networks" BSGW (Google News RSS, Bing RSS)', '"BSGW" "Secure Gateway" (Google News RSS)', 'vjst.vn search: Lancs', 'NIST CMVP validated modules vendor=Lancs', 'Common Criteria portal vendor=Lancs']
- **Sources reviewed:** 11 (kept: 11, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 2, vendor_doc: 9
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
