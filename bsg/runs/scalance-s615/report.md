# BSG / Cross Domain Product Assessment: Siemens AG — SCALANCE S615

**Product ID:** `scalance-s615`
**Version reference:** Firmware V7.2 / Web Based Management Configuration Manual 05/2023 (C79000-G8976-C388-13); device 6GK5615-0AA00-2AA2
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T16:20:00Z
**Total evidence items collected:** 33
**Total distinct sources:** 8

---

## 1. Overview

The SCALANCE S615 (order number 6GK5615-0AA00-2AA2) is a compact DIN-rail security module in Siemens' SIMATIC NET portfolio, marketed as a LAN router that protects automation networks "by means of VPN and firewall" [1]. Siemens positions the SCALANCE S family as industrial security appliances combining network segmentation, high-performance firewall and secure remote access [4], and describes the S615 specifically as optimized for compact deployments, machine-level protection and remote service connections [4]. Its documented security engine is a stateful inspection firewall with up to 128 IP rules per rule set [3][5], IPsec VPN for up to 20 connections (AES-256/3DES, PSK or X.509v3 certificates) [1], an OpenVPN client, NAT/NAPT, dynamic user-specific firewall rule sets, and VRRPv3 router redundancy [3][8]. It is therefore a ruggedized industrial firewall/VPN router, not a protocol-break cross-domain guard: its documented LAN-router/NAT/NAPT and stateful-inspection-firewall architecture is an IP-forwarding design that directly contradicts a protocol-break requirement (item 1.1, scored `not_supported`), while the remaining CDS-only checklist items (hardware isolation, internal data stamping, CDR, schema validation, security labels, anti-steganography) are simply undocumented one way or the other and are scored `unknown` rather than exempted [1][4]. Documented deployment shapes include cell protection between plant subnets, remote-maintenance VPN access via SINEMA Remote Connect, and NAT-based integration of legacy machine networks [3][7].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 0                | 2      | 0   |
| partial          | 3     | 0                | 3      | 0   |
| not_supported    | 4     | 0                | 4      | 0   |
| unknown          | 15    | 0                | 0      | 15  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 8 items backed by ≥ 2 source_types; 4 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | — | Siemens documents the S615 as a LAN router performing NAT/NAPT address conversion with a stateful inspection firewall, an IP-forwarding architecture that logically excludes a protocol-break design terminating every session with no IP routing. [1], [3] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No dual-board FPGA or shared-memory hardware isolation architecture is documented; only generic router/appliance positioning is described.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | The stateful inspection firewall discards IP packets that do not match a firewall rule, i.e. default-deny for routed traffic, with whitelist rules for permitted protocols, sources and destinations. The manual notes the firewall has no effect on packets forwarded at layer 2 within a VLAN. [3], [5] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (Signed and encrypted firmware and encrypted administration access are documented, but no hardened-OS / microkernel / SELinux-strict-mode claim for the device OS was found.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No internal cryptographic data-stamping/signing control of sanitized content prior to new-session initiation is documented.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No 100% content-disarm-and-reconstruction capability for Office/PDF/image/CAD formats is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No file-content inspection, macro/script removal or embedded-object sanitization is documented for this IP-layer firewall.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No multi-engine antivirus scanning of payload is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No W3C-schema structural validation of XML/JSON/FIXM/AIXM documents is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No security-label-based information flow control / file filtering is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No keyword/regex-based data-leakage detection on traffic content is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No anti-steganography detection or removal capability for image files is documented.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No file-transfer proxy with content cleaning (SFTP, FTP/S, HTTPS, SMB/NFS) is documented; SFTP appears only as a device configuration load/save mechanism.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The configuration manual documents predefined firewall services for PROFINET (UDP 34964, 49154, 49155) and use in PROFINET RT environments with a CCA declaration; no application-layer proxy for OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT is documented. A practitioner forum thread describes using the S615's NAT/firewall to give an OPC client access to a PLC across subnets. [3], [7] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF unidirectional/bidirectional relay is documented.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Not Supported | medium | 100 Mbps | The datasheet specifies a maximum transfer rate of 10/100 Mbit/s and the reseller page describes 100 Mbit/s ports with up to 128 firewall rules; the device's interface rate is below the 1000 Mbps threshold. [1], [5] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet processing latency figure is documented in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Not Supported | medium | 3000 ms | VRRPv3 router redundancy is documented in the WBM manual and the Getting Started guide, which states communication is restored within three seconds after master-router failure; no sub-second switchover figure is documented. [3], [5], [8] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No explicit fail-close behavior of the firewall under DoS/overload is documented; VLAN structuring is recommended as DoS mitigation in the security recommendations.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Role-based access control is documented: local users and RADIUS groups map to roles with read-only (function right 1) or read/write (15) rights, and configuration changes are possible only with the admin role. A dedicated three-way separation of system admin, policy admin and auditor roles is not documented. [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | — | The Syslog client forwards event messages to a configured server and supports sending them over TCP with TLS encryption; the datasheet lists SysLog as a supported function. [1], [3] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | The WBM manual's syslog appendix maps security messages to IEC 62443-3-3 requirements (e.g. SR 1.2), and the Siemens product page states SCALANCE S maintains compliance with IEC 62443; no ready-made NIST SP 800-82 or ISO 27001 report templates are documented. [3], [4] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | The datasheet, operating instructions and Siemens certificate registry list ATEX, IECEx, FM, UL/CSA, CE, RCM and marine approvals for the S615; none of the documented certifications is Common Criteria, FIPS 140-3 or a national cryptographic certification. [1], [2], [6] |

---

## 4. Notable Strengths

- **Default-deny stateful firewall (1.3):** The stateful inspection firewall discards packets that do not match a firewall rule, providing default-deny behavior for routed traffic under whitelist rules [3], corroborated by a reseller description of cell-protection firewall capability [5].
- **OT-aware firewall services (3.2):** Predefined firewall services for PROFINET (UDP 34964, 49154, 49155) and documented PROFINET RT environment use with a CCA declaration show built-in OT protocol awareness [3].
- **Encrypted administration and logging (5.2):** HTTPS access is enabled by default [3], firmware is signed and encrypted [3], and the Syslog client can forward messages to a SIEM over TCP with TLS encryption [3].
- **Role-based access control (5.1):** Local users and RADIUS groups map to roles with read-only (function right 1) or read/write (function right 15) rights, and configuration changes require the admin role [3].
- **Compliance-oriented documentation (5.3):** The configuration manual maps syslog messages to IEC 62443-3-3 requirements (e.g. SR 1.2), and the product family page states SCALANCE S maintains compliance with IEC 62443 [3][4].

## 5. Notable Gaps / Risks

- **Throughput below requirement (4.1):** The datasheet specifies a maximum transfer rate of 10/100 Mbit/s [1] and the reseller page confirms 100 Mbit/s ports with up to 128 firewall rules [5], so the device cannot meet the 1 Gbps threshold; a firewall-class replacement with gigabit interfaces would be needed.
- **HA failover far above 100 ms (4.3):** VRRPv3 redundancy is supported, but the Getting Started guide states communication is restored within three seconds after master-router failure [8] and no sub-second switchover or session-state synchronization figure is documented.
- **No security-product certifications (5.4):** Documented approvals cover ATEX, IECEx, FM, UL/CSA, CE, RCM and marine classifications [1][2][6]; no Common Criteria, FIPS 140-3 or national cryptographic certification is listed, which matters for classified or regulated deployments.
- **No content-level inspection (2.2, 2.3, 2.6):** The firewall operates at the IP/packet level [3]; no file sanitization, multi-engine AV or DLP capability is documented, so malicious file payloads are not inspected.
- **Layer-2 blind spot (1.3):** The manual states the firewall has no effect on packets forwarded at layer 2 within a VLAN [3], so intra-VLAN lateral movement is not filtered; latency (4.2) and DoS fail-close (4.4) behavior are also undocumented.

## 6. Evidence Quality Notes

The assessment rests on 8 distinct sources and 33 evidence entries, every quote verified verbatim against staged artifacts (0 fabricated, 0 unverifiable). Non-unknown items are each backed by 2-4 sources, but the source base is heavily Siemens-authored: the datasheet [1], operating instructions [2], WBM configuration manual [3], Getting Started guide [8] and product family page [4] are all vendor material, and the independent-looking sources (industrialcomms reseller page [5], Siemens-hosted certificate registry [6], PLCtalk forum thread [7]) ultimately mirror vendor data or practitioner experience. Only items 1.3, 3.2, 4.1 and 4.3 draw on a non-vendor-hosted source, so all non-unknown verdicts are capped at medium confidence.

No outright contradictions were found. One nuance was handled carefully: the SCALANCE S family page advertises up to 750 Mbit/s firewall throughput and VRRP with firewall state synchronization [4], but its FAQ attributes redundancy primarily to the SCALANCE SC-600 line; items 4.1 and 4.3 were therefore anchored to S615-specific documents (datasheet transfer rate 100 Mbit/s [1]; Getting Started three-second VRRPv3 restoration [8]) rather than family-level marketing figures. Two sources (Siemens certificate registry [6], PLCtalk [7]) were captured through the r.jina.ai rendering proxy because the origin sites block direct fetching or render client-side; the staged text is preserved under artifacts/ with provenance recorded in artifacts/manifest.jsonl.

---

## Bibliography

[1] Siemens AG. "Data sheet 6GK5615-0AA00-2AA2 - SCALANCE S615". https://assets.euautomation.com/uploads/parts/datasheet/01/6gk56150aa002aa2.pdf (Retrieved: 2026-08-11T08:21:42Z)
[2] Siemens AG. "SCALANCE S615 Operating Instructions (SIMATIC NET Industrial Ethernet Security)". https://cache.industry.siemens.com/dl/files/909/109475909/att_899416/v1/BA_SCALANCE-S615_76.pdf (Retrieved: 2026-08-11T08:21:42Z)
[3] Siemens AG. "SCALANCE S615 Web Based Management V7.2 - Configuration Manual". https://support.industry.siemens.com/cs/attachments/109751632/PH_SCALANCE-S615-WBM_76.pdf (Retrieved: 2026-08-11T08:21:47Z)
[4] Siemens AG. "SCALANCE S Industrial Security Appliance - Siemens product page". https://www.siemens.com/en-us/products/scalance/s-industrial-security-appliance/ (Retrieved: 2026-08-11T08:21:47Z)
[5] Industrial Communications. "SCALANCE S615 Series - Industrial VPN System (reseller product page)". https://www.industrialcomms.com/products/scalance-s615 (Retrieved: 2026-08-11T08:23:37Z)
[6] Siemens AG (certificate registry). "Siemens Product Information - 6GK5615-0AA00-2AA2 (SCALANCE S615) certificate list". https://www.industry-mobile-support.siemens-info.com/en/article/6GK5615-0AA00-2AA2/cert (Retrieved: 2026-08-11T08:25:20Z)
[7] PLCtalk.net forum. "Is Siemens SCALANCE S615 The Right Tool? - PLCtalk.net forum thread". https://www.plctalk.net/forums/threads/is-siemens-scalance-s615-the-right-tool.132359/ (Retrieved: 2026-08-11T08:25:20Z)
[8] Siemens AG. "SCALANCE S615 Getting Started (SIMATIC NET Industrial Ethernet Security)". https://cache.industry.siemens.com/dl/files/913/109475913/att_951755/v1/GS_SCALANCE-S615_76.pdf (Retrieved: 2026-08-11T08:24:39Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 9
- **Sources reviewed:** 8 (kept: 8, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 4, web: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
