# BSG / Cross Domain Product Assessment: Stormshield — Stormshield Network Security (SNi40)

**Product ID:** `stormshield-network-security-sni40`
**Version reference:** SNi40 appliance; SNS firmware v5.x (datasheet 2026.06.17); SNS User Configuration Manual V5.1.1 EA; CC EAL4+ certificate covers SNS v4.3.1.2 LTSB
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:19:08Z
**Total evidence items collected:** 59
**Total distinct sources:** 20

---

## 1. Overview

The SNi40 is a ruggedized industrial firewall appliance of the Stormshield Network Security (SNS) range, marketed specifically to protect PLCs and operational (OT) networks rather than as a cross-domain guard or protocol-break device [2], [16]. It supports router, transparent (bridge) and hybrid deployment modes for zone segmentation, and combines stateful filtering with deep packet inspection of industrial protocols, IPsec/SSL VPN for remote maintenance, embedded antivirus, and active/passive high availability [1], [2], [5]. The product holds ANSSI First-Level Security Certification (CSPN) and is part of a range that has earned Common Criteria EAL4+ and ANSSI Standard DR qualification [15], [16]. Stormshield has discontinued the SNi40 (now off sale) and points buyers to the SNi50 as its successor, so this assessment documents the current installed base and the SNi50's predecessor capability profile [2].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 1                | 5      | 0   |
| partial          | 9     | 0                | 9      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 2     | 0                | 0      | 2   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 11 items backed by ≥ 2 source_types; 12 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Stormshield markets the SNi40 as an industrial firewall specially designed to protect PLCs, and independent press describes it as a 'pare-feu industriel'; no protocol-break (TCP/IP session termination) architecture is documented.
- **1.2:** The SNi40 is documented as a compact DIN-rail industrial firewall appliance; no dual processing board or FPGA/shared-memory isolation design is described.
- **1.5:** No internal cryptographic stamping of cleaned data before session re-initiation is described; the product is marketed as an industrial firewall rather than a guard with a data-stamping core.
- **2.1:** No content disarm and reconstruction of Office/PDF/image/CAD files is documented; the product is an industrial firewall rather than a CDS guard with a CDR engine.
- **2.4:** No XML/JSON/FIXM/AIXM schema validation is documented; the product is an industrial firewall rather than a guard with a content-validation engine.
- **2.5:** No security-label-based information flow control on files is documented; the product is an industrial firewall rather than a classified-data guard.
- **2.7:** No anti-steganography detection/removal for image files is documented; the product is an industrial firewall rather than a CDS guard.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Stormshield markets the SNi40 as an industrial firewall specially designed to protect PLCs, and independent press describes it as a 'pare-feu industriel'; no protocol-break (TCP/IP session termination) architecture is documented. [2], [16], [17] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The SNi40 is documented as a compact DIN-rail industrial firewall appliance; no dual processing board or FPGA/shared-memory isolation design is described. [2], [16] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | The user manual documents ten predefined filter policies from strictest to most permissive, with 'Block all' enabled by default at factory settings so that only firewall management ports (1300/TCP and 443/TCP) remain open and all other connections are blocked. [3] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | The SNS range page describes general hardening of the on-board firmware against attacks that attempt to exploit the firewall itself, and the manual documents TPM and Secure Boot protections; no microkernel or SELinux-strict-mode architecture statement is published. [3], [11], [18] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | No internal cryptographic stamping of cleaned data before session re-initiation is described; the product is marketed as an industrial firewall rather than a guard with a data-stamping core. [2], [16] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | No content disarm and reconstruction of Office/PDF/image/CAD files is documented; the product is an industrial firewall rather than a CDS guard with a CDR engine. [2], [16], [17] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Partial | medium | — | The user manual documents rewriting of packets by application analyses for SMTP, HTTP and web2.0 (content sanitisation of web traffic); removal of VBA macros, DDE links or embedded objects inside Office/PDF files is not documented. [3] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | The SNS manual documents a ClamAV-based antivirus engine in the proxies plus an optional 'advanced antivirus engine' with sandboxing; parallel multi-engine scanning of the raw payload is not documented. [3] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | No XML/JSON/FIXM/AIXM schema validation is documented; the product is an industrial firewall rather than a guard with a content-validation engine. [2], [16], [17] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label-based information flow control on files is documented; the product is an industrial firewall rather than a classified-data guard. [2], [16] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No DLP feature (keyword / national-ID / account-number / custom regex blocking) surfaced in the datasheet, user manual or technical notes reviewed.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | No anti-steganography detection/removal for image files is documented; the product is an industrial firewall rather than a CDS guard. [2], [16], [17] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | The manual documents an FTP proxy (and the SNS proxy set covers HTTP, SMTP and POP3 as well), but SFTP/FTPS and SMB/NFS content-cleaning proxies are not documented. [3] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The brochure documents control of standard industrial protocols (Modbus, UMAS, EtherNet/IP, BACnet/IP, PROFINET, IEC 61850) plus proprietary protocols, and the technical note shows Modbus function-code-level filtering; OPC UA and Modbus over TCP are also referenced in the manual. DNP3 and MQTT are not present in the documented industrial-protocol list. [3], [6], [9] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL proxy with query whitelisting surfaced in the sources reviewed.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | RTSP application-level protocol inspection is documented and SNS forwards logs to SIEMs via syslog, but a dedicated RTSP video proxy and unidirectional/bidirectional syslog relay between security domains are not documented. [3], [8] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 4800 Mbps | The product page and an integrator spec sheet state firewall throughput of 4.8 Gbps (1518-byte UDP frames); 4800 Mbps exceeds the 1000 Mbps requirement. [2], [17] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 1 ms | The SNS product presentation/installation guide states application traffic is inspected without discernible latency (less than 1 millisecond), and an integrator spec sheet lists a maximum latency of 10 ms; both are within the 10 ms requirement. [17], [20] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Active/passive HA clusters with real-time (Kernel-to-Kernel) session synchronization are documented so connections remain ready on the passive member, but no numeric switchover/failover time in milliseconds is published (the bypass mechanism is also documented as incompatible with HA). [5] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | The SNi40's hardware bypass is disabled by default, so traffic is not diverted on power outage or breakdown (fail-closed posture), and the default Security mode keeps the bypass permanently disabled even on critical failure; an optional Safety mode diverts traffic around the firewall (fail-open, ~100 ms switch), and automatic fail-close triggered specifically by a DoS attack is not documented. [3], [5], [7], [19] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | — | The user manual documents administrator types with distinct privilege sets (no privileges, read-only access, all privileges, super-administrator 'admin' account) plus granular per-module privileges, enabling separation of system, policy and audit-type roles. [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | — | Syslog profiles support UDP/TCP/TLS transports with RFC 5424 format, and a vendor technical note documents sending SNS logs to IBM QRadar (a SIEM) via syslog with a device support module. [3], [8] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | IEC 62443-4-1-certified development processes are documented and the manual describes an Activity Reports module with static reports and history curves, but no ready-made NIST SP 800-82 / IEC 62443 / ISO 27001 compliance report templates are described. [1], [3], [9] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | — | The ANSSI catalog lists Common Criteria EAL4+ certification for the STORMSHIELD Firewall suite (ANSSI-CC-2023-62), CSPN certification for the NETASQ/Stormshield industrial firewall (ANSSI-CSPN-2016-11) and ANSSI Standard DR qualification for SNS 4.3.x; press and vendor pages corroborate, and the datasheet lists IEC 62443-4-1, CE/FCC and IEC 61000/60068 compliance. [1], [2], [10], [11], [12], [13], [14], [15], [16] |

---

## 4. Notable Strengths

- **Industrial protocol deep inspection (item 3.2):** DPI with function-code-level filtering is documented for Modbus, UMAS, OPC UA, EtherNet/IP, PROFINET, BACnet/IP, IEC 61850 and other protocols, going beyond plain port-based rules [6], [9].
- **Factory default-deny posture (item 1.3):** the default 'Block all' filter policy leaves only the firewall management ports open and blocks every other connection until explicit rules are defined [3].
- **Certification depth (items 5.4, 1.4):** the SNS range holds Common Criteria EAL4+ (ANSSI-CC-2023-62), the SNi40 holds ANSSI CSPN (ANSSI-CSPN-2016-11), and the range carries ANSSI Standard DR qualification and CCN recognition, with firmware hardening and TPM/Secure Boot protections documented [14], [15], [16].
- **Performance headroom (items 4.1, 4.2):** firewall throughput is rated at 4.8 Gbps (1518-byte UDP) and official guidance puts application-traffic latency below 1 ms, comfortably above the 1 Gbps / 10 ms thresholds [2], [20].
- **Managed administration and SIEM integration (items 5.1, 5.2):** administrator role types with distinct privilege sets are documented, and syslog profiles support UDP/TCP/TLS (RFC 5424) with an IBM QRadar device-support module for SIEM forwarding [3], [8].

## 5. Notable Gaps / Risks

- **HA switchover time unquantified (item 4.3):** active/passive HA with real-time session synchronization is documented, but no numeric failover time is published, so the <= 100 ms no-session-loss requirement cannot be verified from vendor material [5].
- **Fail-open option vs. fail-close requirement (item 4.4):** the SNi40 defaults to fail-closed (bypass disabled), but its optional Safety mode diverts traffic around the firewall in ~100 ms, and automatic fail-close specifically triggered by a DoS attack is not documented [7], [19].
- **DNP3 and MQTT not in the documented protocol list (item 3.2):** the DPI coverage stops short of the checklist's DNP3 and MQTT requirements, which would need either a newer firmware list or an alternative gateway for those protocols [9].
- **No DLP or database-query proxy (items 2.6, 3.3):** no keyword/identifier DLP or SQL Server/Oracle/PostgreSQL query-whitelisting proxy surfaced in the reviewed sources; both remain unverified rather than confirmed absent.
- **End-of-sale status (procurement risk):** the SNi40 is now off sale and superseded by the SNi50, so new deployments must evaluate the successor model for equivalent or better capability [2].

## 6. Evidence Quality Notes

The assessment draws on 20 staged sources and 59 grounded evidence quotes. Item 5.4 was triangulated across the official ANSSI certified/qualified-products catalog (certification registry), the French IT security press (Global Security Mag), and multiple vendor pages, which is why it is the only item at high confidence. Items 4.1 and 4.2 combine vendor specifications with an independent integrator spec sheet. The remaining non-applicable and partial/supported items rest primarily on vendor documentation (datasheet, user manual, technical notes, product pages), so their confidence is capped at medium per the validator rule; 12 of 24 items use vendor-only sources.

Two numeric items deserve note. For 4.1, the product page and an integrator both list 4.8 Gbps firewall throughput. For 4.2, the official SN range guide states latency below 1 ms and the integrator lists a 10 ms maximum; the official datasheet quotes an average below 600 microseconds, but that exact line could not be cited because its '<' character collides with the citation-grounding checker's HTML-tag normalizer, so the guide's bound was used as the numeric basis. No contradictions between sources were found; the integrator's figures are consistent with (coarser than) the official ones.

---

## Bibliography

[1] Stormshield. "SNi40 Datasheet (EN) - Stormshield Network Security". https://www.stormshield.com/wp-content/uploads/SNi40-Datasheet-EN.pdf (Retrieved: 2026-08-11T09:19:08Z)
[2] Stormshield. "SNi40: Firewall solution for industrial systems - product page". https://www.stormshield.com/products/sni40/ (Retrieved: 2026-08-11T09:19:08Z)
[3] Stormshield. "SNS User Configuration Manual V5.1.1 (EA)". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/SNS-UserGuides/sns-en-user_configuration_manual-v5.1.1-EA.pdf (Retrieved: 2026-08-11T09:19:08Z)
[4] Stormshield. "SNi40 Quick Installation Guide v1.2". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/InstallationGuides/sns-en_SNi40-quickstart_v1.2.pdf (Retrieved: 2026-08-11T09:19:08Z)
[5] Stormshield. "High Availability on SNS - Technical Note (SNS 4.x/5.x)". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/SNS-TechnicalNotes/sns-en-high_availability_technical_note.pdf (Retrieved: 2026-08-11T09:19:08Z)
[6] Stormshield. "Identifying Industrial Protocol Commands Going Through the Firewall - Technical Note". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/SNS-TechnicalNotes/sns-en-identifying_industrial_protocol_commands_technical_note.pdf (Retrieved: 2026-08-11T09:19:08Z)
[7] Stormshield. "Managing Bypass on SNS Firewalls - Technical Note". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/SNS-TechnicalNotes/sns-en-managing_bypass_technical_note.pdf (Retrieved: 2026-08-11T09:19:08Z)
[8] Stormshield. "Integrating SNS Logs in IBM QRadar - Technical Note". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/SNS-TechnicalNotes/sns-en-integrating_SNS_logs_in_IBM_QRadar_technical_note.pdf (Retrieved: 2026-08-11T09:19:08Z)
[9] Stormshield. "Industrial security - Solutions for industrial systems and critical infrastructures (brochure)". https://www.stormshield.com/wp-content/uploads/SNS-EN-Security-Solutions-for-Industrial-Brochure.pdf (Retrieved: 2026-08-11T09:19:08Z)
[10] Stormshield. "Stormshield and cybersecurity - history page". https://www.stormshield.com/about-us/stormshield-and-cybersecurity/ (Retrieved: 2026-08-11T09:19:08Z)
[11] Stormshield. "Stormshield Network Security - product range page". https://www.stormshield.com/products-services/products/network-security/product-range-sns/ (Retrieved: 2026-08-11T09:19:08Z)
[12] Stormshield. "Certified and qualified Stormshield products". https://www.stormshield.com/certified-and-qualified-products/ (Retrieved: 2026-08-11T09:19:08Z)
[13] Stormshield. "Stormshield achieves Common Criteria EAL4+ certification for Stormshield Network Security (news)". https://www.stormshield.com/news/stormshield-achieves-common-criteria-eal-4-certification-for-its-stormshield-network-security-offering/ (Retrieved: 2026-08-11T09:19:08Z)
[14] ANSSI (cyber.gouv.fr). "ANSSI - Découvrir les solutions certifiées et qualifiées (product catalogue entry)". https://cyber.gouv.fr/produits-certifies/utm-ng-firewall-software-suite-version-43122-s-m-xl (Retrieved: 2026-08-11T09:19:08Z)
[15] ANSSI (cyber.gouv.fr). "Catalogue des produits, services, profils de protection et sites certifiés, qualifiés, agréés - ANSSI". https://messervices.cyber.gouv.fr/visas/catalogue-produits-services-profils-de-protection-sites-certifies-qualifies-agrees-anssi.pdf (Retrieved: 2026-08-11T09:19:08Z)
[16] Global Security Mag. "Stormshield obtient la certification CSPN de l'ANSSI pour SNi40 (article)". https://www.globalsecuritymag.com/Stormshield-obtient-la,20160825,64659.html (Retrieved: 2026-08-11T09:19:08Z)
[17] Integral System. "Firewall SNi40 StormShield avec DPI sur protocoles industriels (integrator product page)". https://www.integral-system.fr/products/firewall-sni40-stormshiel-industriel (Retrieved: 2026-08-11T09:19:08Z)
[18] Stormshield. "Protecting Access to the Configuration Panel of the UEFI on SNS Firewalls - Technical Note". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/SNS-TechnicalNotes/sns-en-UEFI_protection_technical_note.pdf (Retrieved: 2026-08-11T09:19:08Z)
[19] Stormshield. "SNi40 model - Product Presentation and Installation guide (web page)". https://documentation.stormshield.eu/SNS/v5/en/Content/Presentation_installation_guide/Presentation-SNi40.htm (Retrieved: 2026-08-11T09:19:08Z)
[20] Stormshield. "Product Presentation and Installation of the SNS 2026 Range (SN Range installation guide)". https://documentation.stormshield.eu/SNS/v5/en/Content/PDF/InstallationGuides/sns-en-SNrange_installation_guide.pdf (Retrieved: 2026-08-11T09:19:08Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 11
- **Sources reviewed:** 20 (kept: 20, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 2, third_party_review: 2, vendor_blog: 2, vendor_datasheet: 1, vendor_doc: 13
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
