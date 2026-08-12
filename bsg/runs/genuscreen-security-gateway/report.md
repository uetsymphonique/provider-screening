# BSG / Cross Domain Product Assessment: GENUA GmbH — genuscreen Security Gateway

**Product ID:** `genuscreen-security-gateway`
**Version reference:** genuscreen 8.0 (BSI-DSZ-CC-1194-2023, cert. 2023); hardware revisions XL 5.0 / L 5.0 / M 5.0 / S 4.1 / XS 2.1; genuscreen Virtual
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:23:33.656172Z
**Total evidence items collected:** 31
**Total distinct sources:** 16

---

## 1. Overview

GENUA genuscreen is a Firewall & VPN-Appliance from GENUA GmbH (Kirchheim, Germany), a German IT-security vendor; the vendor positions it under "Firewalls & Gateways" and "VPN" on its site [1]. It combines a stateful packet filter (with bridging/routing modes, NAT, QoS, GEO-IP filtering and an optional SIP/Session-Border-Controller module) with an IPsec/IKEv2 and SSH-VPN gateway that includes post-quantum key exchange [1][4]. It is not a protocol-break guard or Cross Domain Solution: the BSI certification report describes it as "a distributed stateful packet filter firewall system with VPN capabilities and central configuration" [9]. The product ships in hardware variants XL/L/M/S/XS (rev. 5.0 down to 2.1) plus a virtualized edition (genuscreen Virtual) for hypervisor/cloud deployment [5][7]; all models can be clustered and centrally administered via the genucenter management station [1][11]. Deployment shapes documented include site-to-site VPN meshes, security zones inside LANs, bridging/stealth firewalls, RAS dial-in termination for VPN clients, and VS-NfD/NATO RESTRICTED networks [1][4][8].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 5     | 2                | 3      | 0   |
| partial          | 3     | 0                | 3      | 0   |
| not_supported    | 3     | 0                | 3      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 8 items backed by ≥ 2 source_types; 4 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Not Supported | medium | — | The BSI CC certification report describes the TOE as a distributed stateful packet filter firewall system that filters traffic at the network border; a stateful packet filter forwards traffic under rule/state evaluation and does not terminate every TCP/IP session at a boundary funnel. [4], [9] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Not Supported | medium | — | The BSI CC certification report states the TOE 'consists only of software and documentation', running on standard genuscreen filter appliances plus a separate genucenter management machine; no dual-processing-board, FPGA- or shared-memory-isolated hardware architecture is part of the certified design. [9] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | — | Vendor documentation and three independent reseller/tool pages state that genuscreen permits only explicitly allowed connections and blocks all other requests, i.e. whitelist-style default-deny filtering. [1], [11], [12], [14], [15] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | — | The CC certification report documents that the packet filter runs in the kernel of the OpenBSD operating system, and the datasheet lists privileged separation and sandboxing as enhanced protection. [4], [9] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No macro/script/DDE/embedded-object removal feature is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No multi-engine antivirus scanning of payloads is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Not Supported | medium | — | The datasheet's firewall feature table enumerates the supported filter criteria as IP address, network protocol, port, interface, flags and state only; security-label-based filtering is absent from this exhaustive criteria list. [4] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No DLP keyword/ID/regex filtering is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No file-transfer protocol proxy (SFTP/FTP/SMB/HTTPS) with content cleaning is documented.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found (No OT/ICS protocol support (OPC UA, Modbus, IEC 60870-5-104, DNP3, MQTT) is documented.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No database protocol proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or syslog/CEF relay matching the requirement is documented (a VoIP/SIP relay module exists but is out of scope).) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 37490 Mbps | The hardware datasheet rates the top model (genuscreen XL, rev. 5.0) at 37,490 Mbit/s firewall TCP throughput; the facts sheet quotes up to 19,699 Mbit/s for a single system, with clusters enabling higher performance. [2], [4], [5] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No packet-processing latency figure is published in datasheets, Security Target or third-party material.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Hot standby failover, active-active load balancing and state synchronisation are documented (vendor, CC report, T-Systems case study), but no numeric switchover time in ms is published; only qualitative availability claims were found. [4], [8], [9] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | A DDoS-protection TCP-handshake proxy against SYN floods is documented, but an explicit fail-close state of the boundary under hardware DoS is not described. [4] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | — | The Security Target documents role separation: administrators configure policy, service users run maintenance only, and revisors may only view configuration and audit logs. [9], [10] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Syslog forwarding to external servers is documented, with an optional encrypted (certificate-based) channel, but CEF formatting or a TLS-based real-time push to a named SIEM is not described. [4], [10] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | — | genuscreen 8.0 holds BSI Common Criteria certificate BSI-DSZ-CC-1194-2023 at EAL4+ (augmented by ALC_FLR.2, ASE_TSS.2, AVA_VAN.4, ALC_PAM.1); BSI approval list and NATO NIAPC confirm VS-NfD and NATO RESTRICTED approvals (e.g. BSI-VSA-10937 for v8.6), corroborated by independent reseller/tool pages. [4], [9], [12], [13], [15], [16] |

---

## 4. Notable Strengths

- **Internationally certified security baseline (item 5.4):** genuscreen 8.0 holds BSI Common Criteria certificate BSI-DSZ-CC-1194-2023 at EAL 4+ (augmented by ALC_FLR.2, ASE_TSS.2, AVA_VAN.4, ALC_PAM.1) [9]; the BSI approval list and the NATO NIAPC catalogue independently confirm VS-NfD and NATO RESTRICTED approvals (e.g. BSI-VSA-10937 for version 8.6) [13][16].
- **Default-deny stateful filtering (item 1.3):** the firewall only permits explicitly allowed connections and blocks all other requests; this is stated by the vendor [1][11] and independently by the ECOS, NORLAN and CybersecTools pages [12][14][15].
- **Hardened platform (item 1.4):** the packet filter is implemented in the kernel of the OpenBSD operating system per the certification report, with privileged separation and sandboxing listed as enhanced protection [9][4].
- **High throughput and scale (item 4.1):** the top model is rated at 37,490 Mbit/s firewall TCP throughput, with clustering for more [5][4][2]; installations scale beyond 1,000 systems with central management [1][4].
- **Separation of administrative roles with audit (items 5.1, 5.2):** the Security Target documents distinct administrator, service-user and revisor (audit-view) roles [10][9], and syslog forwarding supports an optional encrypted channel to external log servers [10][4].

## 5. Notable Gaps / Risks

- **No file-content inspection depth (items 2.2, 2.3, 2.6):** no macro/script removal, multi-engine antivirus scanning, or DLP keyword/regex filtering is documented anywhere in the public material reviewed; buyers requiring file-level inspection must add third-party products.
- **No OT/ICS, file-transfer or database protocol proxying (items 3.1, 3.2, 3.3):** genuscreen is a network-layer firewall/VPN; no evidence was found of SFTP/SMB proxies with content cleaning, OPC UA/Modbus/DNP3/104 proxies, or database query whitelisting (GENUA sells a separate industrial firewall, genuwall, outside the reviewed scope).
- **Latency unquantified (item 4.2):** no packet-processing latency figure is published, so the <= 10 ms realtime-protocol requirement cannot be verified from public sources.
- **HA switchover time unquantified (item 4.3):** hot-standby failover, active-active load balancing and state synchronisation are documented [9][4][8], but no failover time in milliseconds is published, so the <= 100 ms requirement remains unverified.
- **Fail-close behavior under DoS not explicit (item 4.4):** a TCP-handshake DDoS/SYN-flood protection proxy is documented [4], but an automatic fail-close state of the boundary under hardware DoS is not described.
- **No compliance report templates (item 5.3):** no NIST SP 800-82 / IEC 62443 / ISO 27001 report templates are documented, though the product itself supports VS-NfD / NATO RESTRICTED compliance via its BSI approvals [9][13].

## 6. Evidence Quality Notes

Sixteen distinct sources and 31 evidence entries support this assessment; every quoted fragment was verified (normalized exact-substring) against the sha256-anchored staged text in artifacts/, and the citation-grounding check reports all 31 entries grounded with zero fabricated or unverifiable quotes. Items 1.3 and 5.4 are triangulated across multiple independent sources (three reseller/tool pages for 1.3; BSI and NATO registries plus ECOS and CybersecTools for 5.4), giving high confidence; items 4.1, 4.3, 1.4, 5.1 and 5.2 combine vendor datasheets/docs with the CC certificate or Security Target. Four items (4.1, 4.4, 5.2 and the 4.3 partial) rest only on vendor documentation, so their confidence is capped at medium per the project contract.

The thirteen "unknown" items (1.5, 2.1, 2.2, 2.3, 2.4, 2.6, 2.7, 3.1-3.4, 4.2, 5.3) reflect genuine absence of documentation in the reviewed material rather than confirmed absence of capability; the vendor publishes a separate industrial firewall (genuwall) and a high-resistance firewall (genugate) that were not in scope. No contradictions were found between sources; the only discrepancy of note is a throughput figure of 37,490 Mbit/s (hardware datasheet, XL rev. 5.0, TCP) versus 19,699 Mbit/s (Facts & Features marketing summary) — both vendor-published, the lower figure likely reflecting a different measurement configuration, and both far above the 1 Gbps checklist threshold. One access caveat: genua.de/genua.eu block direct TLS from the research network, so those pages and PDFs were staged via reader/raw proxies (r.jina.ai, cors.lol) with the original URLs retained as the manifest origin; the Common Criteria portal, BSI, NATO NIAPC, ECOS, NORLAN and CybersecTools were fetched directly.

---

## Bibliography

[1] genua GmbH. "Firewall & VPN-Appliance genuscreen (product page, German)". https://www.genua.de/it-sicherheitsloesungen/firewall-vpn-appliance-genuscreen (Retrieved: 2026-08-11T09:01:54Z)
[2] genua GmbH. "Produktvarianten genuscreen - hardware variants and performance (product page)". https://www.genua.de/it-sicherheitsloesungen/firewall-vpn-appliance-genuscreen/hardware-varianten (Retrieved: 2026-08-11T09:02:18Z)
[3] genua GmbH. "Informationsmaterial genuscreen (download index page)". https://www.genua.de/it-sicherheitsloesungen/firewall-vpn-appliance-genuscreen/informationsmaterial (Retrieved: 2026-08-11T09:02:32Z)
[4] genua GmbH. "genuscreen Facts and Features (Firewall & VPN Appliance) data sheet". https://www.genua.de/fileadmin/Loesungen/Downloads/genuscreen-facts-features.pdf (Retrieved: 2026-08-11T09:04:59Z)
[5] genua GmbH. "genuscreen Hardware Data Sheet (Firewall & VPN Appliance)". https://www.genua.de/fileadmin/Loesungen/Hardware_sheets/genuscreen-hardware.pdf (Retrieved: 2026-08-11T09:06:15Z)
[6] genua GmbH. "genuscreen Salesfolder (Firewall & VPN-Appliance)". https://www.genua.de/fileadmin/Loesungen/Downloads/genuscreen-salesfolder.pdf (Retrieved: 2026-08-11T09:06:19Z)
[7] genua GmbH. "genuscreen Virtual Flyer (Firewall & VPN-Appliance)". https://www.genua.de/fileadmin/Loesungen/Downloads/genuscreen-virtual-flyer.pdf (Retrieved: 2026-08-11T09:06:21Z)
[8] T-Systems International GmbH. "Gemanagtes Security-Netz fuer die HIL Heeresinstandsetzungslogistik GmbH (case study)". https://www.genua.de/fileadmin/Loesungen/Downloads/hil-casestudy.pdf (Retrieved: 2026-08-11T09:07:31Z)
[9] BSI (Bundesamt fuer Sicherheit in der Informationstechnik). "BSI-DSZ-CC-1194-2023 Certification Report - genuscreen 8.0". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/1194a_pdf.pdf (Retrieved: 2026-08-11T09:10:15Z)
[10] genua GmbH (published via Common Criteria Portal). "Security Target BSI-DSZ-CC-1194-2023 - genuscreen 8.0 (genua GmbH)". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/1194b_pdf.pdf (Retrieved: 2026-08-11T09:10:48Z)
[11] genua GmbH. "Firewall & VPN Appliance genuscreen (product page, English)". https://www.genua.eu/it-security-solutions/firewall-vpn-appliance-genuscreen (Retrieved: 2026-08-11T09:15:06Z)
[12] ECOS Technology GmbH. "genua genuscreen - Firewall and VPN appliance (partner product page)". https://www.ecos.de/en/remote-access/genua-genuscreen/ (Retrieved: 2026-08-11T09:14:55Z)
[13] BSI (Bundesamt fuer Sicherheit in der Informationstechnik). "BSI - Liste zugelassener Produkte - genuscreen/genucard (BSI-Schrift 7164)". https://www.bsi.bund.de/SharedDocs/Zulassung/DE/Produkte/genuscreen_genucard_84_BSI-VSA-10828.html (Retrieved: 2026-08-11T09:19:50Z)
[14] NORLAN GmbH. "GENUA GENUSCREEN (reseller product page)". https://norlan.biz/produkt/genua-genuscreen/ (Retrieved: 2026-08-11T09:19:58Z)
[15] CybersecTools. "genuscreen | CybersecTools (product directory entry)". https://cybersectools.com/tools/genuscreen (Retrieved: 2026-08-11T09:20:00Z)
[16] NATO Information Assurance (NIA). "NIAPC - Product Details - genuscreen (virtual) 8.6 (NATO Information Assurance Product Catalogue)". https://www.ia.nato.int/niapc/Product/genuscreen-8.4_885 (Retrieved: 2026-08-11T09:20:39Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 16 (kept: 16, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** pdf: 7, web: 9
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
