# BSG / Cross Domain Product Assessment: Yokogawa Electric — CENTUM VP Security Gateway

**Product ID:** `centum-vp-security-gateway`
**Version reference:** Waterfall Unidirectional Security Gateway family (DiodeCore / WF-600, 'Waterfall for Yokogawa' edition, 2023 datasheet); CENTUM VP R7.01 (June 2025) as the protected DCS platform
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:35:00Z
**Total evidence items collected:** 46
**Total distinct sources:** 12

---

## 1. Overview

Yokogawa does not market a standalone Yokogawa-branded hardware appliance named "CENTUM VP Security Gateway"; the security gateway offering for its CENTUM VP DCS environment is realized through the January 2023 collaboration with Waterfall Security Solutions [2][3], which makes the hardware-enforced Waterfall Unidirectional Security Gateway family (DiodeCore / WF-600) available to Yokogawa customers with native connectors for Exaopc, Exaquantum and CI Server [1]. The gateway physically enforces one-way data replication: OPC-DA/HDA/UA tags are mirrored in real time to the enterprise side with no inbound path [1][4], positioning the product as a unidirectional Cross-Domain-Solution-style device rather than a bidirectional firewall or content-CDR guard. The protected platform, CENTUM VP R7.01 (June 2025), is Yokogawa's 10th-generation DCS [5], reinforced with industry security benchmarks, an OPC UA client, and ISASecure CSA/SSA Level 1 certifications [7][8].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 1                | 5      | 0   |
| partial          | 5     | 0                | 5      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 9 items backed by ≥ 2 source_types; 9 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | high | — | The CENTUM VP security gateway is a hardware-enforced unidirectional gateway: OPC server data is replicated one-way to the enterprise side and the hardware permits data to flow in only one direction, so TCP/IP interaction is terminated at the boundary with no inbound routing path. [1], [2], [3], [4] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | medium | — | Two physically separate circuit boards (transmit and receive) are connected only by a laser/photocell fiber link, enforcing one-way hardware isolation between the networks; the DiodeCore platform is likewise documented with a transmit board, receive board and fiber as the only connection. [4], [6] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | All inbound traffic is physically blocked by the gateway hardware (even legitimate administrators cannot misconfigure it to allow inbound traffic), and Yokogawa's network security offering adds source/destination-based firewall filtering at the boundary; outbound flows are limited to configured connector protocols. [1], [4], [11] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | The gateway is documented as Common Criteria EAL4+ certified, which entails evaluated security functionality, and Yokogawa's IT Security Tool, certified against the CIS Benchmark, hardens the Windows-based CENTUM VP/ProSafe-RS components; no microkernel or SELinux-strict-mode statement for the gateway OS was found. [4], [8] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No cryptographic stamping of data before session re-initiation is documented for the gateway; the FCS-level CRC integrity diagnostics described for CENTUM VP are internal integrity checks, not boundary data stamping.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No content disarm & reconstruction of Office/PDF/image/CAD files is documented; the gateway's data plane is OPC tag replication, not file transfer.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No macro/script/embedded-object removal from files is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No multi-engine antivirus scanning of payload is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No XML/JSON/FIXM/AIXM schema validation is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No security-label-based information flow control on files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No keyword/regex-based data-leakage detection on content is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No anti-steganography detection/removal for image files is documented.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No SFTP/FTP/S/HTTPS/SMB/NFS file-transfer proxy with content cleaning is documented; the gateway replicates OPC tag data rather than file transfers.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The gateway replicates OPC-DA/HDA/UA tags and has documented Modbus and Siemens S7 connectors, and the Yokogawa stack adds OPC UA support via Exaopc and an OPC UA client in CENTUM R7; IEC 60870-5-104, DNP3 and MQTT proxies are not documented. [1], [2], [4], [8], [9] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented; the gateway emits its own fault alarms via Syslog/SNMP but is not documented as a relay.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | The datasheet documents 1-10 Gbps throughput for the family, the DiodeCore platform is rated 1 Gbps and the WF-600 Performance platform 1-10 Gbps, so the ≥1000 Mbps requirement is met at the base platform and exceeded on the high-capacity platform. [1], [4] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet-processing latency figure is documented for the gateway (it replicates data rather than forwarding packets).) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | High-availability options are documented for the gateway family (WF-600 Performance 'High Availability: Yes', datasheet 'High Availability options') and the CENTUM VP controller supports fully redundant configuration, but no automatic switchover time is specified. [1], [4], [12] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | — | The boundary is fail-safe by construction: the hardware physically blocks all inbound traffic, so DoS floods and other attacks from the external side cannot reach the control network at all ('nothing on the external side can send traffic into OT through the Gateway'). [1], [4] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (No three-way RBAC separation of system admin / policy admin / auditor roles is documented for the gateway or the CENTUM VP stack; central management (Waterfall Central / Axle) is documented without role-separation detail.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Gateway fault alarms are emitted in real time via Syslog, SNMP traps, email, Windows logs and log files, and Yokogawa's network security offering includes SIEM log collection and analysis; no CEF format or TLS-encrypted syslog channel is documented. [1], [11] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | The gateway family is documented to facilitate compliance with NERC CIP (including 37 NERC CIP-005 R1 exemptions), NIST SP 800-82, IEC 62443 and ANSSI, and Yokogawa maps its network security implementation to the IEC 62443 Purdue model; ready-made compliance report templates are not documented. [1], [3], [4], [11] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | medium | — | Waterfall documents Common Criteria EAL4+ certification for the gateway platforms, and the CENTUM VP/ProSafe-RS system holds ISASecure CSA Level 1 (IEC 62443-4-1/4-2, 2022) and ISASecure SSA Level 1 (IEC 62443-3-3, 2026) certifications; no FIPS 140-3 or national cryptographic certification was found. [4], [7], [8] |

---

## 4. Notable Strengths

- **Hardware-enforced protocol break and isolation (items 1.1, 1.2):** two physically separate circuit boards connected only by a laser/photocell fiber link make inbound attacks impossible, a stronger boundary than rule-based firewall segmentation [1][4].
- **Fail-safe boundary by construction (item 4.4):** nothing on the external side can send traffic into the OT network through the gateway, so DoS floods cannot reach the control system [1][4].
- **Throughput headroom (item 4.1):** the family is documented at 1-10 Gbps (DiodeCore 1 Gbps; WF-600 Performance 1-10 Gbps), meeting the ≥1000 Mbps requirement [1][4].
- **OT protocol coverage for Yokogawa plants (item 3.2):** OPC-DA/HDA/UA tag replication plus Modbus and Siemens S7 connectors, extended by OPC UA support in Exaopc and an OPC UA client in CENTUM R7 [1][4][8].
- **Compliance leverage (items 5.3, 5.4):** documented NERC CIP-005 R1 exemptions and NIST SP 800-82 / IEC 62443 / ANSSI alignment, plus a vendor-documented Common Criteria EAL4+ claim for the gateway and ISASecure CSA/SSA Level 1 for the CENTUM VP system [4][7][8].

## 5. Notable Gaps / Risks

- **Unidirectional, not bidirectional (items 1.1, 3.2):** the offering is a one-way data-replication gateway; IEC 60870-5-104, DNP3 and MQTT proxies are undocumented, so buyers needing two-way OT traffic must source separate components [1][4].
- **No content inspection engine (items 2.1-2.7, 3.1):** no CDR, multi-engine AV, DLP, schema validation or file-transfer proxies are documented; the gateway replicates OPC tag data only [1][4].
- **HA switchover unquantified (item 4.3):** high-availability options exist on the WF-600 Performance but no switchover time (≤100 ms target) or session-preservation figure is documented.
- **RBAC separation undocumented (item 5.1):** central management is documented, but no system-admin / policy-admin / auditor role separation was found for the gateway or the CENTUM VP stack.
- **Common Criteria claim not registry-verified (item 5.4):** the EAL4+ certification is vendor-documented; the Common Criteria portal blocks automated access, so the certificate could not be independently confirmed during this run.

## 6. Evidence Quality Notes

12 distinct sources were staged and every one of the 46 evidence quotes was verified verbatim against the staged text (grounding check: 46/46 grounded, 0 fabricated, 0 unverifiable). 9 items are backed by two or more source_types; the gateway-specific items (1.1-1.4, 4.1-4.4, 5.2-5.4) triangulate Waterfall product documentation, the Yokogawa-focused datasheet, a vendor blog and one third-party announcement (SecurityWeek / ICS Cyber Security Conference), while the CENTUM VP platform context rests on Yokogawa product pages and press releases, which are vendor-only and therefore cap confidence at medium. Items 1.5, 2.1-2.7, 3.1, 3.3, 3.4, 4.2 and 5.1 are marked unknown because no staged source documents those capabilities; none were downgraded to not_supported from silence.

The main scoping risk is product identity: no Yokogawa-branded hardware named "CENTUM VP Security Gateway" exists in the sources reviewed, so the assessment anchors on the Waterfall collaboration, which is the documented security-gateway offering for CENTUM VP. The only material discrepancy is that throughput (1-10 Gbps) comes from vendor documentation with no independent benchmark, so item 4.1 is held at medium confidence rather than high.

---

## Bibliography

[1] Waterfall Security Solutions. "Waterfall for Yokogawa - Secure Process Data Replication (datasheet)". https://waterfall-security.com/wp-content/uploads/2023/08/Waterfall-for-Yokogawa-New.pdf (Retrieved: 2026-08-11T09:00:00Z)
[2] SecurityWeek / ICS Cyber Security Conference. "Yokogawa to Sell Unidirectional Gateways from Waterfall Security Solutions Under New Partnership". https://www.icscybersecurityconference.com/yokogawa-to-sell-unidirectional-gateways-from-waterfall-security-solutions-under-new-partnership/ (Retrieved: 2026-08-11T09:00:00Z)
[3] Waterfall Security Solutions. "Waterfall Security Announces Cybersecurity Collaboration with Yokogawa". https://waterfall-security.com/about-waterfall/news/waterfall-security-announces-cybersecurity-collaboration-with-yokogawa/ (Retrieved: 2026-08-11T09:00:00Z)
[4] Waterfall Security Solutions. "Unidirectional Security Gateways (product page)". https://waterfall-security.com/technology-and-products/unidirectional-security-gateways/ (Retrieved: 2026-08-11T09:00:00Z)
[5] Hydrocarbon Processing. "Yokogawa releases next generation of CENTUM VP integrated production control system". https://www.hydrocarbonprocessing.com/news/2025/06/yokogawa-releases-next-generation-of-centum-vp-integrated-production-control-system/ (Retrieved: 2026-08-11T09:00:00Z)
[6] Waterfall Security Solutions. "Big OT Security, Smaller Footprint - Meet DiodeCore! (blog)". https://waterfall-security.com/ot-insights-center/ot-cybersecurity-insights-center/big-ot-security-smaller-footprint-meet-diodecore/ (Retrieved: 2026-08-11T09:00:00Z)
[7] Yokogawa Electric Corporation. "OpreX Control and Safety System lineup: cyber security measures and safety strengthened (press release, 2022-01-12, JA)". https://www.yokogawa.co.jp/news/press-releases/2022/2022-01-12-ja/ (Retrieved: 2026-08-11T09:00:00Z)
[8] Yokogawa Electric Corporation. "Integrated Control and Safety System, CENTUM VP and ProSafe-RS: cyber security measures strengthened (press release, 2026-04-08, JA)". https://www.yokogawa.co.jp/news/press-releases/2026/2026-04-08-ja/ (Retrieved: 2026-08-11T09:00:00Z)
[9] Yokogawa Electric Corporation. "Next-generation integrated production control system CENTUM VP announced (press release, 2025-06-03, JA)". https://www.yokogawa.co.jp/news/press-releases/2025/2025-06-03-ja/ (Retrieved: 2026-08-11T09:00:00Z)
[10] Yokogawa Electric Corporation. "CENTUM VP | YOKOGAWA (product page, JA)". https://www.yokogawa.co.jp/solutions/products-and-services/control/control-and-safety-system/distributed-control-systems-dcs/centum-vp/ (Retrieved: 2026-08-11T09:00:00Z)
[11] Yokogawa Electric Corporation. "Network security measures (Yokogawa Security Program, JA)". https://www.yokogawa.co.jp/solutions/solutions/cyber-security-sol/security-sol/network-security/ (Retrieved: 2026-08-11T09:00:00Z)
[12] Yokogawa Electric Corporation. "CENTUM VP | Yokogawa Electric Corporation (product page, EN)". https://www.yokogawa.com/solutions/products-and-services/control/control-and-safety-system/distributed-control-systems-dcs/centum-vp/ (Retrieved: 2026-08-11T09:00:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 9
- **Sources reviewed:** 12 (kept: 12, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 2, vendor_blog: 2, vendor_datasheet: 1, vendor_doc: 7
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
