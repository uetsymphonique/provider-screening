# BSG / Cross Domain Product Assessment: Waterfall Security Solutions - Waterfall Bidirectional Security Gateway

**Product ID:** `waterfall-bidirectional-security-gateway`
**Version reference:** WF-500 v2.0 / WF-600 vF (Common Criteria-certified configurations, 2023-2025); Axle software platform
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:37:12.152001+00:00
**Total evidence items collected:** 64
**Total distinct sources:** 33

---

## 1. Overview

Waterfall Security Solutions is a vendor of hardware-enforced unidirectional security gateways (USGs) for OT/ICS perimeters. The "Bidirectional Security Gateway" assessed here is not a separate product SKU: bidirectional data flow is delivered by deploying pairs of USGs - an outbound gateway replicating OT servers to the enterprise network and an independent inbound gateway replicating external servers into the plant [2] - plus Secure Bypass/FLIP modules that temporarily, or on schedule, reverse the one-way hardware for remote support and updates [9, 29]. The product is a protocol-break guard of the Cross Domain Solution class, not an industrial firewall: TX/RX appliances joined by a fiber-optic laser/photocell link pass only a proprietary one-way protocol, and IP routing never crosses the boundary [19, 25]. Deployment shapes span 1U rack-mount appliances (WF-500, WF-600), DIN-rail and DiodeCore/VM options, with 1–10 Gbps throughput and optional/standard HA [14, 16]. Certified configurations hold Common Criteria EAL4+ under the Dutch NSCIB and Singapore CSA schemes [17, 18].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 7     | 5                | 2      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 10    | 0                | 0      | 10  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 5 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | high | - | The TX host terminates all communications inside the OT network and is not a router; only a proprietary one-way protocol passes over the laser/photocell link, so no TCP/IP session or IP routing crosses the boundary. Bidirectional data access is delivered by replicating servers through paired inbound/outbound gateways. [1], [2], [3], [6], [16], [19], [23], [24], [25] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | high | - | The gateway is a TX/RX appliance pair separated by a physical divider with no electrical connection between sides, linked only by a fiber-optic cable carrying laser-LED light to a photoelectric cell on the RX side. [14], [19], [25], [33] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | - | Inbound traffic is blocked at the hardware level, not by an allow-list: nothing on the external side can send traffic into the OT network and even administrators cannot misconfigure the product to allow it. Reverse flows only occur via physically-controlled mechanisms such as the FLIP's scheduled reversal. [1], [11], [19], [23], [25] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | - | The WF-600 runs a proprietary 'Waterfall OS' and the certified diode modules implement all security functionality in hardware, but no explicit hardening mode (microkernel/SELinux) is documented. TX/RX agent hosts run standard PC operating systems, and a 2025 CVE describes OS command injection in the WF-500 TX Host administration WebUI. [16], [19], [26] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No source describes cryptographic signing/stamping of data before session re-initiation; the architecture replicates data rather than re-initiating sessions.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No CDR (content disarm & reconstruction) of Office/PDF/image/CAD formats documented in vendor material.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No macro/script/DDE/embedded-object removal documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (Vendor documents only AV-signature updater connectors (Kaspersky, Norton, OPSWAT), not inline multi-engine scanning of payloads.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM schema validation documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label (IFC) based filtering documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (Waterfall Central documents hiding sensitive data in logs; no content-based DLP (keywords/IDs/regex) documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography scanning of images documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | File-transfer connectors (SFTP, FTP/FTPS, SMB/CIFS/NFS, TFTP, folder mirroring) are documented, but no content-cleaning of transferred files is evidenced. [3], [5], [14] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | - | The connector library includes OPC UA, Modbus, DNP3, IEC 60870-5-104, ICCP, BACnet and MQTT connectors that replicate OT data across the gateway; the WF-500 datasheet and certified Security Target likewise list Modbus, DNP3, ICCP, IEC 60870-5-104 and OPC variants. [1], [3], [14], [19] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | - | Database connectors replicate Microsoft SQL Server, Oracle, MySQL and PostgreSQL data; query-whitelisting proxy behavior is not documented since the connectors replicate rather than proxy queries. [3], [14] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Video/audio stream transfer, multicast streams and syslog TCP/UDP relays are documented; RTSP-specific video proxying and CEF log format are not explicitly documented. [3], [14], [24] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | high | 1000 Mbps | Standard throughput is 1 Gbps per TX/RX pair ('1Gbps standard throughput, multi-Gbps with several TX/RX pairs'), and the WF-600 platform offers 1-10 Gbps options. [2], [14], [16], [27], [31] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No latency figures are published in datasheets, brochures, Security Targets or third-party material; the product replicates data rather than forwarding packets.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | High availability is documented as a standard WF-600 option ('no single point of failure') and an optional WF-500 configuration, but no switchover time in milliseconds is published. [14], [16], [27], [32] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | - | The Secure Bypass unit physically disconnects after a pre-programmed period (typically 30-90 minutes) or on power failure, restoring unidirectional state; the unidirectional hardware itself has no inbound path that a denial-of-service flood could force open. [1], [9], [25], [29] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (Management runs through the web-based UI (Axle), but no role separation (system admin / policy admin / auditor) is documented in public material.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Gateway software emulates syslog devices and ships connectors for FortiSIEM, Splunk, IBM QRadar, ArcSight, Microsoft Sentinel and other SIEM platforms; CEF format and TLS-encrypted log transport are not explicitly documented. [3], [13], [14], [24] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | - | Vendor documents compliance enablement for NERC CIP, IEC 62443, NIST SP 800-82, NRC 5.71, CFATS, ISO and ANSSI; out-of-box compliance report templates are not documented. [1], [10], [15] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | - | WF-500 v2.0 and WF-600 vF hold Common Criteria EAL4+ certificates (EAL4 augmented with AVA_VAN.5, ALC_DVS.2 and ALC_FLR.2) under the Dutch NSCIB and Singapore CSA schemes. Vendor and integrator pages additionally claim ANSSI CSPN, NITES Singapore, Korean KC and Israel NISA. [4], [17], [18], [21], [22], [28] |

---

## 4. Notable Strengths

- **Hardware-enforced protocol break (items 1.1, 1.2):** The TX host terminates all communications and is not a router; only a proprietary one-way protocol crosses the fiber-optic laser/photocell link, so no TCP/IP session or IP routing traverses the boundary [1, 19, 25].
- **Default-deny by construction, fail-safe bypass (items 1.3, 4.4):** Nothing on the external side can send traffic into the OT network and administrators cannot misconfigure the product to allow it; the Secure Bypass unit physically disconnects after a pre-programmed period or on power failure, restoring unidirectional state [1, 25, 29].
- **Broad OT protocol and connector coverage (items 3.1, 3.2, 3.3, 3.4):** The connector library covers OPC UA, Modbus, DNP3, IEC 60870-5-104, MQTT, SQL Server/Oracle/PostgreSQL, SFTP/FTP/SMB file transfer, video/audio streams and syslog relays [3, 14].
- **Throughput headroom (item 4.1):** 1 Gbps standard throughput per TX/RX pair with 1–10 Gbps options on the WF-600 platform [14, 16, 27].
- **Independent certification (item 5.4):** WF-500 v2.0 and WF-600 vF hold Common Criteria EAL4+ certificates (EAL4 augmented with AVA_VAN.5, ALC_DVS.2, ALC_FLR.2) under the Dutch NSCIB and Singapore CSA schemes, confirmed via the Common Criteria portal [17, 18, 21, 22].

## 5. Notable Gaps / Risks

- **No content inspection or CDR (items 2.1–2.7):** The gateway performs protocol break and server replication, but no CDR, multi-engine AV scanning, schema validation, security-label filtering, DLP or anti-steganography is documented; buyers needing content sanitization must pair it with separate tools or a CDR-capable CDS.
- **Processing latency not specified (item 4.2):** No latency figures are published anywhere in the material reviewed, and the replication architecture is not a packet-forwarding design, so the ≤10 ms realtime-latency requirement is unverifiable.
- **HA switchover time unspecified (item 4.3):** HA is offered (standard on WF-600, optional on WF-500) but no failover time in milliseconds is published, so the ≤100 ms requirement is unverified.
- **No RBAC role separation documented (item 5.1):** Management runs through the web-based Axle UI, but separation of system-admin / policy-admin / auditor roles is not documented in public material.
- **Management-plane CVE on record (item 1.4):** CVE-2025-41265 (OS command injection in the WF-500 TX Host administration WebUI) shows the agent/management plane runs general-purpose OS components; hardening claims cover only the diode hardware itself [26].

## 6. Evidence Quality Notes

Thirteen of 24 items are backed by ≥ 2 source_types. The core architecture items (1.1–1.3) are triangulated across vendor pages/datasheets, the Common Criteria Security Targets, and independent sources (Tenable's deployment guide, Fortinet's solution brief), and item 5.4 rests on certification_registry sources (Common Criteria portal certificate PDFs, the CSA Singapore product list, the sec-certs tracker) plus vendor/integrator claims - hence high confidence on those items. Items 1.4, 3.1, 3.2, 3.3, 3.4, 4.3 and 5.3 rely on vendor documentation and/or reseller pages only, which caps confidence at medium; item 4.4 also relies on vendor material, including the NIST-hosted RFI response which is vendor-authored (a filing, not an independent assessment).

Items 2.1–2.7, 1.5, 4.2 and 5.1 are marked unknown because no source discusses these capabilities - absence of evidence, not evidence of absence; the Security Target explicitly delegates traffic filtering to the IT environment (OE.FILTER_LOW), consistent with no in-gateway content inspection. One credibility note: the DiodeGate article (a competitor blog) contains an uncorroborated "2022 Gartner study" statistic and was used only for the basic TX/RX architecture description, which the Security Target independently confirms; the industrialcyber.co article could not be staged (Cloudflare challenge) and was therefore not cited.

---

## Bibliography

[1] Waterfall Security Solutions. "Unidirectional Security Gateways (product page)". https://waterfall-security.com/technology-and-products/unidirectional-security-gateways/ (Retrieved: 2026-08-11T08:22:18Z)
[2] Waterfall Security Solutions. "Inbound / Outbound Gateways (product page)". https://waterfall-security.com/technology-and-products/remote-access/inbound-outbound-gateways/ (Retrieved: 2026-08-11T08:22:18Z)
[3] Waterfall Security Solutions. "Technology and products (connector library)". https://waterfall-security.com/technology-and-products/ (Retrieved: 2026-08-11T08:22:22Z)
[4] Waterfall Security Solutions. "Unidirectional Technology (product page)". https://waterfall-security.com/technology-and-products/unidirectional-technology/ (Retrieved: 2026-08-11T08:22:51Z)
[5] Waterfall Security Solutions. "Unidirectional Security Gateways - Absolute protection from external network attacks (introduction)". https://waterfall-security.com/wp-content/uploads/Unidirectional-Gateway-Introduction.pdf (Retrieved: 2026-08-11T08:22:51Z)
[6] Waterfall Security Solutions. "The Story of Waterfall Security & Unidirectional Gateway Technology (company profile)". https://waterfall-security.com/wp-content/uploads/Company-Profile_Waterfall-Security.pdf (Retrieved: 2026-08-11T08:22:51Z)
[7] Waterfall Security Solutions. "Waterfall WF-500 Unidirectional Gateway (product page)". https://waterfall-security.com/technology-and-products/wf-500/ (Retrieved: 2026-08-11T08:23:05Z)
[8] Waterfall Security Solutions. "Waterfall WF-600 Unidirectional Gateway (product page)". https://waterfall-security.com/technology-and-products/wf-600/ (Retrieved: 2026-08-11T08:23:05Z)
[9] Waterfall Security Solutions. "Secure Remote Access OT - Waterfall SBP (product page)". https://waterfall-security.com/technology-and-products/remote-access/wf-sbp/ (Retrieved: 2026-08-11T08:22:38Z)
[10] Waterfall Security Solutions. "WF-RSV Remote Screen View (product page)". https://waterfall-security.com/technology-and-products/remote-access/wf-rsv/ (Retrieved: 2026-08-11T08:22:38Z)
[11] Waterfall Security Solutions. "WF Flip Unidirectional Gateway (product page)". https://waterfall-security.com/technology-and-products/remote-access/wf-flip/ (Retrieved: 2026-08-11T08:25:48Z)
[12] Waterfall Security Solutions. "Waterfall Central (product page)". https://waterfall-security.com/technology-and-products/wf-central/ (Retrieved: 2026-08-11T08:25:48Z)
[13] Waterfall Security Solutions. "HERA Hardware-Enforced Remote Access (product page)". https://waterfall-security.com/technology-and-products/hera/ (Retrieved: 2026-08-11T08:24:25Z)
[14] Waterfall Security Solutions. "Unidirectional Security Gateway WF-500 Data Sheet". https://waterfall-security.com/wp-content/uploads/WF-500_Datasheet.pdf (Retrieved: 2026-08-11T08:27:15Z)
[15] Waterfall Security Solutions. "WF-500 Product Brochure". https://waterfall-security.com/wp-content/uploads/2023/11/WF-500-Brochure-digital.pdf (Retrieved: 2026-08-11T08:24:25Z)
[16] Waterfall Security Solutions. "WF-600 Product Brochure". https://waterfall-security.com/wp-content/uploads/2023/09/WF-600-Brochure.pdf (Retrieved: 2026-08-11T08:28:33Z)
[17] Common Criteria Portal / Cyber Security Agency of Singapore. "Common Criteria Certificate - Waterfall Unidirectional Security Gateway WF-600 Version F (CSA_CC_25005)". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/WF-600%20CC%20Certificate%20v2.1.pdf (Retrieved: 2026-08-11T08:25:14Z)
[18] Common Criteria Portal / TUV Rheinland Nederland (NSCIB). "Common Criteria Certificate CC-23-0618820 - Waterfall Unidirectional Security Gateway WF-500 Version 2.0". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/NSCIB-CC-23-0618820-cert.pdf (Retrieved: 2026-08-11T08:25:14Z)
[19] Waterfall Security Solutions (Common Criteria Security Target). "Security Target - Waterfall Unidirectional Security Gateway WF-500 Version 2.0". https://www.commoncriteriaportal.org/files/epfiles/NSCIB-CC-0618820-STv3.pdf (Retrieved: 2026-08-11T08:27:15Z)
[20] Waterfall Security Solutions (Common Criteria Security Target). "Security Target - Waterfall Unidirectional Security Gateway WF-600 Version F". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/NSCIB-CC-2400089-01-ST.pdf (Retrieved: 2026-08-11T08:28:33Z)
[21] Cyber Security Agency of Singapore (CSA). "Waterfall WF-500 version 2 - Singapore Common Criteria Scheme Certified Product List". https://www.csa.gov.sg/our-programmes/certification-and-labelling-schemes/singapore-common-criteria-scheme/product-list/waterfall-wf-500-version-2/ (Retrieved: 2026-08-11T08:27:15Z)
[22] sec-certs.org. "Waterfall WF-500 version 2 - Common Criteria certificate tracker". https://sec-certs.org/cc/89dadb4ce1a88313/ (Retrieved: 2026-08-11T08:29:58Z)
[23] Tenable, Inc.. "Waterfall Architecture and Data Flow - Tenable NNM Deployment Guide". https://docs.tenable.com/network-monitor/deployment/Content/WaterfallArchitecture.htm (Retrieved: 2026-08-11T08:27:15Z)
[24] Fortinet, Inc.. "Fortinet and Waterfall Security Solution (solution brief)". https://www.fortinet.com/content/dam/fortinet/assets/alliances/asb-fortinet-waterfall-joint-solution.pdf (Retrieved: 2026-08-11T08:23:15Z)
[25] Waterfall Security Solutions (filing hosted by NIST). "Waterfall Security Solutions Response to NIST RFI: Developing a Framework to Improve Critical Infrastructure Cybersecurity". https://www.nist.gov/document/040813waterfallsecuritypdf (Retrieved: 2026-08-11T08:23:15Z)
[26] SentinelOne Vulnerability Database. "CVE-2025-41265: Waterfall WF-500 Firmware RCE Vulnerability". https://www.sentinelone.com/vulnerability-database/cve-2025-41265/ (Retrieved: 2026-08-11T08:27:21Z)
[27] Carahsoft Technology Corp.. "Waterfall Security Solutions Government Products". https://www.carahsoft.com/waterfall-security/products (Retrieved: 2026-08-11T08:27:21Z)
[28] INTEC. "Waterfall Security Unidirectional Gateways (integrator page)". https://www.intec.gr/en/what-we-do/cybersecurity/waterfall-security-unidirectional-gateways (Retrieved: 2026-08-11T08:29:17Z)
[29] Waterfall Security Solutions. "Access my OT networks, safely (solution page)". https://waterfall-security.com/solutions/by-need/access-my-ot-networks-safely/ (Retrieved: 2026-08-11T08:28:33Z)
[30] Waterfall Security Solutions. "Waterfall Secure Bypass (SBP) Brochure". https://waterfall-security.com/wp-content/uploads/Waterfall-for-Secure-Bypass.pdf (Retrieved: 2026-08-11T08:28:33Z)
[31] PR Newswire APAC / Waterfall Security Solutions. "Waterfall Security Announces New WF-600 Unidirectional Security Gateway (press release)". https://en.prnasia.com/releases/apac/waterfall-security-announces-new-wf-600-unidirectional-security-gateway-396974.shtml (Retrieved: 2026-08-11T08:28:51Z)
[32] New York Tech Media. "Waterfall Security Solutions launches WF-600 Unidirectional Security Gateway". https://nytech.media/waterfall-security-solutions-launches-wf-600-unidirectional-security-gateway/ (Retrieved: 2026-08-11T08:28:51Z)
[33] DiodeGate. "What is Waterfall Security? (technology article)". https://www.diodegate.com/articles/what-is-waterfall-security/ (Retrieved: 2026-08-11T08:23:15Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 33 (kept: 33, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** pdf: 12, web: 21
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
