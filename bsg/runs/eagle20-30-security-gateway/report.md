# BSG / Cross Domain Product Assessment: Hirschmann (Belden) — EAGLE20/30 Security Gateway (EAGLE20-0400 / EAGLE30-0402 Industrial Firewalls)

**Product ID:** `eagle20-30-security-gateway`
**Version reference:** HiSecOS 3.0 (Product Bulletin PB00044AG, 2015); models EAGLE20-0400 / EAGLE30-0402
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:10:00Z
**Total evidence items collected:** 34
**Total distinct sources:** 7

---

## 1. Overview

The Hirschmann EAGLE20/30 Security Gateway (EAGLE20-0400 and EAGLE30-0402) is a ruggedized multiport industrial firewall from Belden's Hirschmann line, running the Hirschmann Security Operating System (HiSecOS) [1, 2]. Belden positions it as an "Industrial Firewall, Router, Transparent (Bridging)" device: a stateful inspection firewall with NAT, static and OSPF routing, IPSec VPN, and deep packet inspection for OPC Classic and Modbus traffic, deployed as a DIN-rail appliance with up to eight ports (Fast Ethernet, Gigabit Ethernet SFP, and SHDSL) [2, 4]. It is a standard firewall-class product for segmenting industrial networks at IT/OT boundaries: its documented "Router" categorization and NAT/routing feature set contradict a protocol-break architecture (item 1.1), and no evidence confirms or excludes the other guard-specific checklist items, which are rated unknown [2, 4]. Target applications include automobile and machine building, process automation, transportation, water/wastewater, and oil and gas networks [2].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 6     | 0                | 6      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 16    | 0                | 0      | 16  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 4 items backed by ≥ 2 source_types; 7 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | — | Hirschmann datasheets categorize the EAGLE20/30 as "Industrial Firewall, Router, Transparent (Bridging)" and document IP masquerading, 1:1 NAT, Double-NAT and Destination NAT -- an IP-routing/NAT architecture that forwards traffic rather than terminating sessions and removing IP routing. [2], [4] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | — | no evidence found (No dual-processing-board hardware isolation design (FPGA or isolated shared memory) is documented.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | Vendor documents rule-based forwarding in which packets are evaluated against configured firewall rules and only safe packets continue while unwanted packets are discarded, supported by Firewall Learning Mode and ACL filtering. [1], [2] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | Vendor documents IEEE 1686-compliant configuration with security audit trails and password-policy user management, but no hardened-OS/microkernel/SELinux-strict approach; NVD records HiSecOS vulnerabilities affecting EAGLE20/30 (CVE-2020-6994 buffer overflow, CVE-2018-25236 management authentication bypass). [2], [6], [7] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No internal cryptographic stamping of cleaned data prior to session re-initiation is documented.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (The documented Deep Packet Inspection covers OPC and Modbus protocol traffic; no file-level CDR (Office/PDF/Image/CAD reconstruction) capability is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No public documentation of VBA macro / JavaScript / DDE link / embedded object removal from Office or PDF files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No public documentation of multi-engine antivirus scanning of raw payloads.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No XML/JSON/FIXM/AIXM schema-validation engine is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No security-label-based information flow control on files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No public documentation of keyword/regex-based DLP rules for secrets, ID numbers or accounts.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No anti-steganography detection/removal capability for image files is documented.) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No public documentation of SFTP/FTP(S)/HTTPS/SMB/NFS file-transfer proxies with content cleaning; documented HTTPS/SSH/SFTP support is for device management.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | Vendor documents deep packet inspection for OPC (OPC Classic Enforcer software level) and Modbus on the EAGLE20/30; OPC UA, IEC 60870-5-104, DNP3 and MQTT industrial proxying are not documented for this model. [1], [2] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No public documentation of SQL Server / Oracle / PostgreSQL database proxying or query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No public documentation of RTSP video proxying or unidirectional/bidirectional syslog/CEF relay services through the gateway.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | — | no evidence found (Vendor documents port types (4x 10/100 on EAGLE20-0400; plus 2x FE/GE SFP on EAGLE30-0402) but publishes no firewall/CDR inspection throughput figure; the EAGLE40 successor markets 1 Gb/s bandwidth.) |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No public latency figure for packet/protocol processing.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Vendor documents VRRP router redundancy with a tracking framework to reduce downtime, but publishes no switchover time, so the <=100 ms failover-without-session-loss threshold cannot be verified. [2], [3] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | Vendor documents DoS protection and ingress storm protection as firewall features; an explicit fail-close boundary lock on hardware overload is not documented. [2] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | Vendor documents role-based access control, local/central user management via RADIUS and IEEE 1686-compliant audit trails with password policies; the checklist's three-role separation (system admin / policy admin / auditor) is not enumerated. [2] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Vendor documents syslog output, audit-trail log file, SNMPv1/2/3 and traps for configuration changes; CEF-format real-time log export over a TLS-encrypted channel to a SIEM is not documented. [2] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No public documentation of compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001).) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | — | no evidence found (No Common Criteria (EAL4+), FIPS 140-3 or national crypto certification located for EAGLE20/30; the ISASecure IEC 62443-4-2 CSA Level 1 registry lists the EAGLE4007 model of the successor EAGLE40 line, not the EAGLE20/30.) |

---

## 4. Notable Strengths

- **Rule-based allow/deny forwarding (item 1.3):** packets are evaluated against configured rules and only safe packets continue, with Firewall Learning Mode offering one-click rule creation [2, 1].
- **OT protocol inspection (item 3.2):** HiSecOS provides deep packet inspection for OPC (OPC Classic Enforcer) and Modbus, with dedicated software levels for each protocol [2].
- **Router redundancy for uptime (item 4.3):** VRRP with a tracking framework is documented to reduce downtime on the firewall [2, 3].
- **Overload defence features (item 4.4):** DoS protection and ingress storm protection are built into the stateful inspection engine [2].
- **Access control and auditability (items 5.1, 5.2):** role-based access control, RADIUS user management, IEEE 1686-compliant audit trails, and syslog/SNMP monitoring with configuration-change traps are documented [2].

## 5. Notable Gaps / Risks

- **No published inspection throughput (item 4.1):** no firewall/CDR inspection throughput figure is published for the EAGLE20/30, and the documented 10/100 Mbps Ethernet ports on the EAGLE20-0400 cap its wire rate below the >= 1 Gbps requirement, so 4.1 stays unknown [2].
- **VRRP failover time unquantified (item 4.3):** VRRP redundancy is documented but no switchover time or session-preservation behaviour is published, leaving the <= 100 ms target unverified [2, 3].
- **Fail-close behaviour undocumented (item 4.4):** DoS protection is documented, but an explicit fail-close boundary lock under sustained overload is not [2].
- **OS hardening unverified (item 1.4):** no hardened-OS/microkernel/SELinux-strict approach is documented, and NVD records EAGLE20/30 HiSecOS vulnerabilities (CVE-2020-6994 buffer overflow, CVE-2018-25236 management authentication bypass) [6, 7].
- **No security certification for this model (item 5.4):** no Common Criteria (EAL4+), FIPS 140-3 or national crypto certification is documented for the EAGLE20/30; the ISASecure IEC 62443-4-2 CSA Level 1 listing covers the successor EAGLE4007 model of the EAGLE40 line [5].

## 6. Evidence Quality Notes

All 24 items were assessed, with 14 non-unknown verdicts grounded in 34 evidence entries drawn from 7 sources. No item reached three independent source types: vendor documentation (product page [1], product bulletin [2], flyer [3], category listing [4]) backs every non-unknown verdict, and the only non-vendor sources secured were the two NVD vulnerability records [6, 7] and the ISASecure certification registry [5]. All public search engines, the Common Criteria portal, CISA.gov and the Wayback Machine were blocked or unreachable from the research environment, so no independent lab review or analyst report could be located; confidence is capped at medium for all non-unknown items per the vendor-only rule.

The product-class determination (firewall/router rather than CDS guard) rests on two independent vendor statements — the product bulletin describes the device as "Industrial Firewall, Router, Transparent (Bridging)" with full NAT and routing [2], and the firewalls category page lists it identically [4] — which grounds the not_supported verdict on item 1.1 (IP-routing architecture contradicts protocol break); the remaining guard-specific items (1.2, 1.5, 2.1, 2.4, 2.5, 2.7) have no documented fact either way and are rated unknown rather than not_applicable. The only evidence tension is on item 1.4: vendor documentation emphasises IEEE 1686-compliant security configuration and audit [2], while NVD documents HiSecOS vulnerabilities affecting the EAGLE20/30 [6, 7]; because no hardened-OS/microkernel/SELinux claim exists to reconcile with that vulnerability history, the item is rated partial rather than supported.

---

## Bibliography

[1] Belden Inc.. "EAGLE20/30 — Hirschmann EAGLE20/30 Multiport Industrial Firewall System (product page)". https://www.belden.com/products/industrial-networking-cybersecurity/cybersecurity/firewalls/eagle20-30 (Retrieved: 2026-08-11T09:10:00Z)
[2] Belden Inc.. "EAGLE20/30 Industrial Firewalls with HiSecOS 3.0 Software — Product Bulletin PB00044AG (2015)". https://assets.belden.com/m/7dfe1ce866fbd95a/original/Eagle20-30-Industrial-Firewalls-Hisecos-Software-Hirschmann-2015-11.pdf (Retrieved: 2026-08-11T09:10:00Z)
[3] Belden Inc.. "EAGLE20/30 Industrial Firewalls with HiSecOS 3.0 — Flyer (2020)". https://assets.belden.com/m/7c1c5dae8fe11b55/original/Eagle-20-30-Industrial-Firewalls-Flyer-Hirschmann-2020-01.pdf (Retrieved: 2026-08-11T09:10:00Z)
[4] Belden Inc.. "Firewalls — Belden industrial firewall product category page (EAGLE20/30 product listing)". https://www.belden.com/products/industrial-networking-cybersecurity/cybersecurity/firewalls (Retrieved: 2026-08-11T09:10:00Z)
[5] ISA Security Compliance Institute (ISASecure). "ISASecure IEC 62443-4-2 Certified Components registry (Hirschmann EAGLE4007 entry)". https://isasecure.org/end-users/iec-62443-4-2-certified-components (Retrieved: 2026-08-11T09:10:00Z)
[6] NIST National Vulnerability Database. "NVD entry CVE-2020-6994 — HiOS/HiSecOS buffer overflow affecting EAGLE20/30 (HiSecOS <= 03.2.00)". https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2020-6994 (Retrieved: 2026-08-11T09:10:00Z)
[7] NIST National Vulnerability Database. "NVD entry CVE-2018-25236 — HiOS/HiSecOS HTTP(S) management authentication bypass (EAGLE included)". https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2018-25236 (Retrieved: 2026-08-11T09:10:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 7 (kept: 7, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, third_party_review: 2, vendor_datasheet: 2, vendor_doc: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
