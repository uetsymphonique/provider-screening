# BSG / Cross Domain Product Assessment: Gatewatcher - Trackwatch (Trackwatch Security Gateway - NDR detection platform / Système de détection qualifié)

**Product ID:** `trackwatch-security-gateway`
**Version reference:** Trackwatch 2.5.X (X>=3) per ANSSI catalogue; current product pages reference the Threat Detection System / Gatewatcher NDR Platform (SENSOR, DETECTION CENTER, DECISION CENTER) as of 2026
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:20:22Z
**Total evidence items collected:** 50
**Total distinct sources:** 19

---

## 1. Overview

The product listed in BSG.csv as "Trackwatch Security Gateway" corresponds to Gatewatcher's Trackwatch network detection and response (NDR) platform, marketed in French as the "Système de détection qualifié" (qualified detection system) and now presented as the Gatewatcher NDR Platform built from SENSOR, DETECTION CENTER and DECISION CENTER components [1][3][5]. Trackwatch is a passive detection sensor: it collects network traffic in bypass via TAPs with no impact on production traffic [1][3], analyzes payloads with static, heuristic and machine-learning engines [3][16], and reconstructs files in transit for detection evidence [10]. French trade press describes Gatewatcher as developing network detection probes ("sondes réseau") sold as appliances or virtual machines, ANSSI-certified and deployed mainly to French critical operators [15]. It is not a bidirectional security gateway or protocol-break cross-domain solution: it neither terminates nor forwards traffic between domains, so the gateway/CDS-specific items in this checklist are marked not_applicable (with category-establishing citations) rather than evaluated as missing capabilities. Version anchor: Trackwatch 2.5.X (X>=3) per the ANSSI catalogue [19].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 2     | 0                | 2      | 0   |
| partial          | 6     | 1                | 5      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 4     | 0                | 0      | 4   |
| not_applicable   | 12    | 0                | 12     | 0   |

**Evidence quality:** 16 items backed by ≥ 2 source_types; 5 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Sources establish Trackwatch as a passive network detection & response sensor deployed in bypass (TAP) with no impact on production traffic; it is not an inline gateway that terminates TCP/IP sessions or breaks routing, so a protocol-break architecture does not apply.
- **1.2:** Sources show Trackwatch ships as standard NDR appliances or virtual machines on a wide range of hardware; the dual-board FPGA/shared-memory guard isolation architecture does not apply to this product category.
- **1.3:** Trackwatch passively collects network traffic and does not forward or block packets, so a whitelist-based default-deny forwarding boundary does not apply to this product category.
- **1.5:** Sources establish Trackwatch as a passive monitoring/detection sensor rather than a guard core that signs clean data before re-initiating sessions; internal data stamping does not apply to this product category.
- **2.1:** Sources establish Trackwatch as a passive NDR sensor that analyzes network traffic; content disarm and reconstruction (CDR) of Office/PDF/image/CAD files is a guard/gateway function that does not apply to this product category.
- **2.2:** Trackwatch is a passive detection sensor and does not transform files; removal of VBA macros, scripts, DDE links or embedded objects from documents is not part of this product category.
- **2.4:** Sources establish Trackwatch as a passive NDR sensor; XML/JSON/FIXM/AIXM schema validation against W3C schemas is a guard/gateway data-checking function that does not apply to this product category.
- **2.5:** Sources establish Trackwatch as a passive NDR sensor; information flow control based on security labels attached to files is a guard/gateway function that does not apply to this product category.
- **2.7:** Sources establish Trackwatch as a passive NDR sensor; an anti-steganography engine for hidden data in images is a guard/gateway function that does not apply to this product category.
- **3.3:** Sources establish Trackwatch as a passive NDR sensor with no database proxy; SQL Server/Oracle/PostgreSQL proxying with query whitelisting is a gateway function that does not apply to this product category.
- **3.4:** Sources establish Trackwatch as a passive NDR sensor; RTSP video proxy and syslog/CEF unidirectional/bidirectional relay are gateway functions that do not apply to this product category.
- **4.4:** Trackwatch sensors operate passively in bypass with no forwarding boundary to lock, and the qualified TAPs are documented as fail-safe in-line designs that keep the network operating on power loss; a fail-close boundary lock under DoS is a gateway function that does not apply to this product category.

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | - | Sources establish Trackwatch as a passive network detection & response sensor deployed in bypass (TAP) with no impact on production traffic; it is not an inline gateway that terminates TCP/IP sessions or breaks routing, so a protocol-break architecture does not apply. [1], [3], [15] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | - | Sources show Trackwatch ships as standard NDR appliances or virtual machines on a wide range of hardware; the dual-board FPGA/shared-memory guard isolation architecture does not apply to this product category. [1], [3], [15] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | N/A | medium | - | Trackwatch passively collects network traffic and does not forward or block packets, so a whitelist-based default-deny forwarding boundary does not apply to this product category. [1], [3], [15] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | Vendor documents that Trackwatch features a hardened operating system, developed with a Secure by Design approach, that resists corruption attempts and reduces the attack surface. [3], [7] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | - | Sources establish Trackwatch as a passive monitoring/detection sensor rather than a guard core that signs clean data before re-initiating sessions; internal data stamping does not apply to this product category. [1], [3], [15] |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | - | Sources establish Trackwatch as a passive NDR sensor that analyzes network traffic; content disarm and reconstruction (CDR) of Office/PDF/image/CAD files is a guard/gateway function that does not apply to this product category. [1], [3], [15] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | N/A | medium | - | Trackwatch is a passive detection sensor and does not transform files; removal of VBA macros, scripts, DDE links or embedded objects from documents is not part of this product category. [1], [3], [15] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Supported | medium | - | Vendor documents that Trackwatch detects malware through file analysis conducted by multiple anti-virus engines, examining up to 6 million files per 24 hours; French press corroborates real-time static/heuristic file analysis. [3], [7], [16] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | - | Sources establish Trackwatch as a passive NDR sensor; XML/JSON/FIXM/AIXM schema validation against W3C schemas is a guard/gateway data-checking function that does not apply to this product category. [1], [3], [15] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | - | Sources establish Trackwatch as a passive NDR sensor; information flow control based on security labels attached to files is a guard/gateway function that does not apply to this product category. [1], [3], [15] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (Closest documented capability is network-level 'alerts in case of critical data exfiltration' in the vendor's OT use case, which is detection, not keyword/regex content DLP blocking.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | - | Sources establish Trackwatch as a passive NDR sensor; an anti-steganography engine for hidden data in images is a guard/gateway function that does not apply to this product category. [1], [3], [15] |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Vendor documents reconstruction of files in transit over HTTP/SMTP/SMB/FTP for detection evidence, but Trackwatch is a passive sensor with no file-transfer proxy or content-cleaning function as the checklist requires. [1], [10] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | Vendor documents threat detection on industrial protocols such as OPC UA, DICOM and S7COM with dedicated IT/OT dashboards, but the product is a passive monitor rather than an industrial protocol proxy, and Modbus TCP/IEC 60870-5-104/DNP3/MQTT proxy support is not documented. [1], [11], [13] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | N/A | medium | - | Sources establish Trackwatch as a passive NDR sensor with no database proxy; SQL Server/Oracle/PostgreSQL proxying with query whitelisting is a gateway function that does not apply to this product category. [1], [3], [15] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | N/A | medium | - | Sources establish Trackwatch as a passive NDR sensor; RTSP video proxy and syslog/CEF unidirectional/bidirectional relay are gateway functions that do not apply to this product category. [1], [3], [15] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | Vendor describes the SENSOR as providing passive, high-performance network traffic collection and Deep Visibility as capturing traffic without compromising performance, but publishes no numeric sustained throughput figure, so the >=1000 Mbps threshold cannot be confirmed. [1], [13] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | Vendor describes real-time and historical network analysis and real-time detection, but publishes no numeric processing latency figure; the product is a passive sensor, so a <=10 ms packet-processing latency cannot be confirmed. [4], [13] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | - | no evidence found (No public documentation of active-standby HA or automatic failover switchover time for Trackwatch sensors or platform components.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | N/A | medium | - | Trackwatch sensors operate passively in bypass with no forwarding boundary to lock, and the qualified TAPs are documented as fail-safe in-line designs that keep the network operating on power loss; a fail-close boundary lock under DoS is a gateway function that does not apply to this product category. [1], [3], [15] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (No public documentation of separate System Admin / Policy Admin / Security Auditor roles for the Trackwatch platform.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Vendor case study documents seamless integration into existing SIEM/EDR/firewall/SOC ecosystems and automated response actions, but CEF/Syslog-over-TLS real-time log export specifics are not publicly documented. [9], [12] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (Vendor positions NIS 2 / DORA compliance support, but no evidence of ready-made compliance report templates for NIST SP 800-82, IEC 62443, or ISO 27001.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | high | - | The official ANSSI catalogue lists Gatewatcher Trackwatch v2.5.3+ with qualification level Elémentaire valid 06/06/2025–28/12/2026 (and qualified GTAP TAPs), corroborated by French press. The item's specifically named certifications (Common Criteria EAL4+, FIPS 140-3, or Vietnam Cơ yếu) are not documented. [8], [15], [16], [19] |

---

## 4. Notable Strengths

- **Hardened detection platform (item 1.4):** Trackwatch ships with a hardened operating system developed under a Secure by Design approach, providing resistance to corruption attempts and a reduced attack surface [3][7].
- **Multi-engine antivirus file analysis (item 2.3):** malware detection runs through multiple anti-virus engines on file analysis, examining up to 6 million files per 24 hours with retro-analysis of flagged files [3][16].
- **OT/ICS protocol detection (item 3.2):** threat detection on industrial protocols such as OPC UA, DICOM and S7COM, with specialized IT and OT monitoring dashboards [11][13].
- **ANSSI qualification (item 5.4):** Trackwatch v2.5.3+ is listed in the official ANSSI catalogue at Elémentaire level, valid 06/06/2025 to 28/12/2026, alongside qualified GTAP optical and copper TAPs [19][15].
- **SOC ecosystem integration (item 5.2):** a vendor case study documents seamless integration with SIEM, EDR, firewall and SOC ecosystems plus automated response actions (host isolation, IP blocking) [12].

## 5. Notable Gaps / Risks

- **Category mismatch with the BSG checklist (items 1.1, 1.2, 2.1, 3.3, 3.4, 4.4):** Trackwatch is a passive NDR sensor, not a bidirectional security gateway; none of the protocol-break, hardware-isolation, CDR, proxy or fail-close-boundary capabilities this checklist targets exist in the product [1][3][15]. A buyer needing a true BSG/CDS must look elsewhere; resolving the gap means confirming at procurement stage whether an inline enforcement variant exists at all.
- **No numeric performance figures (items 4.1, 4.2):** only qualitative claims of "high-performance" collection and "real-time" analysis are published, so the >= 1 Gbps throughput and <= 10 ms latency thresholds cannot be verified [1][13].
- **No HA failover documentation (item 4.3):** no public source describes active-standby redundancy or failover switchover time for the sensor or platform components.
- **RBAC and compliance-reporting evidence absent (items 5.1, 5.3):** no public documentation of System Admin / Policy Admin / Auditor role separation, nor of report templates for NIST SP 800-82, IEC 62443 or ISO 27001 (only NIS 2 / DORA compliance positioning).
- **Certification is national-level only (item 5.4):** the documented ANSSI Elémentaire qualification is a French national product qualification; Common Criteria EAL4+, FIPS 140-3 or Vietnam Cơ yếu certification is not documented [19].

## 6. Evidence Quality Notes

19 sources and 50 evidence entries back this assessment. The twelve not_applicable items rest on category-establishing evidence triangulated across vendor product pages (SENSOR and Threat Detection System) and two independent French trade-press outlets (ChannelNews [15], Silicon.fr [16][17]), i.e. three sources spanning vendor_doc and third_party_review; the same triangulation anchors items 1.4, 2.3, 3.1, 3.2 and 5.4. Items 1.4, 2.3, 3.1, 3.2, 4.1, 4.2 and 5.2 rely on vendor documentation or a vendor-hosted case study for their load-bearing claims, so their confidence is capped at medium even where the underlying claim (e.g. multiple anti-virus engines) is specific; the one authoritative independent source is the ANSSI catalogue PDF [19], which only evidences certification (5.4, rated partial/high). No material contradictions were found: vendor pages and press consistently describe a passive bypass-deployed monitoring sensor. Environmental caveat: all general search engines were bot-blocked and web.archive.org was rate-limited during this pass, and www.gatewatcher.com rejects direct fetches (Cloudflare), so vendor pages were staged via the r.jina.ai reader proxy (raw_url points at the proxy URL that was actually fetched; canonical_locator preserves the original vendor URL). Every evidence quote was verified against the staged text by verify_citation_grounding.py: 50/50 grounded, 0 fabricated, 0 unverifiable.

---

## Bibliography

[1] Gatewatcher. "SENSOR - product page (Gatewatcher NDR Platform)". https://r.jina.ai/https://www.gatewatcher.com/en/product/sensor/ (Retrieved: 2026-08-11T09:19:57Z)
[2] Gatewatcher. "Gatewatcher NDR Platform - product page". https://r.jina.ai/https://www.gatewatcher.com/en/product/gatewatcher-ndr-platform/ (Retrieved: 2026-08-11T09:19:57Z)
[3] Gatewatcher. "Threat Detection System (Trackwatch) - product page". https://r.jina.ai/https://www.gatewatcher.com/en/product/threat-detection-system/ (Retrieved: 2026-08-11T09:19:57Z)
[4] Gatewatcher. "DETECTION CENTER - product page". https://r.jina.ai/https://www.gatewatcher.com/en/product/detection-center/ (Retrieved: 2026-08-11T09:19:57Z)
[5] Gatewatcher. "DECISION CENTER - product page". https://r.jina.ai/https://www.gatewatcher.com/en/product/decision-center/ (Retrieved: 2026-08-11T09:19:57Z)
[6] Gatewatcher. "Certified TAP - product page". https://r.jina.ai/https://www.gatewatcher.com/en/product/certified-tap/ (Retrieved: 2026-08-11T09:19:57Z)
[7] Gatewatcher. "Système de détection qualifié (Trackwatch) - fiche produit". https://r.jina.ai/https://www.gatewatcher.com/product/systeme-de-detection/ (Retrieved: 2026-08-11T09:19:57Z)
[8] Gatewatcher. "TAP qualifié - fiche produit". https://r.jina.ai/https://www.gatewatcher.com/product/tap-qualifie/ (Retrieved: 2026-08-11T09:19:57Z)
[9] Gatewatcher. "Discover the components of the Gatewatcher NDR Platform". https://r.jina.ai/https://www.gatewatcher.com/en/discover-the-components-of-the-gatewatcher-ndr-platform/ (Retrieved: 2026-08-11T09:19:57Z)
[10] Gatewatcher. "Gatewatcher 3-Fold brochure 2026 (EN) - PDF". https://r.jina.ai/https://www.gatewatcher.com/wp-content/uploads/2026/03/GW_3FOLD_EN-2026_Final.pdf (Retrieved: 2026-08-11T09:19:57Z)
[11] Gatewatcher. "Understand IT/OT usage on my network - use case". https://r.jina.ai/https://www.gatewatcher.com/en/use-case/understand-it-ot-usage-on-my-network/ (Retrieved: 2026-08-11T09:19:57Z)
[12] Gatewatcher. "The integration of NDR in the banking sector - customer story". https://r.jina.ai/https://www.gatewatcher.com/en/resource/the-integration-of-network-detection-and-response-ndr-in-the-banking-sector/ (Retrieved: 2026-08-11T09:19:57Z)
[13] Gatewatcher. "Deep Visibility - product page". https://r.jina.ai/https://www.gatewatcher.com/en/product/deep-visibility/ (Retrieved: 2026-08-11T09:19:57Z)
[14] Gatewatcher. "The technological alliance between Gigamon and Gatewatcher". https://r.jina.ai/https://www.gatewatcher.com/en/lalliance-technologique-gigamon-et-gatewatcher/ (Retrieved: 2026-08-11T09:19:57Z)
[15] ChannelNews. "Qui est Gatewatcher, présentée par Macron comme l'une des futures licornes françaises de la cybersécurité ?". https://www.channelnews.fr/qui-est-gatewatcher-presentee-par-macron-comme-lune-des-futures-licornes-francaises-de-la-cybersecurite-101607 (Retrieved: 2026-08-11T09:19:57Z)
[16] Silicon.fr. "Jacques de La Rivière, Gatewatcher : "Nous visons une certification par l'ANSSI prochainement"". https://www.silicon.fr/Thematique/cybersecurite-1371/Breves/Jacques-de-La-Riviere-Gatewatcher-nous-visons-une-certification-par-443747.htm (Retrieved: 2026-08-11T09:19:57Z)
[17] Silicon.fr. "Jacques de la Rivière, Gatewatcher : "Nous avons une approche Best of Breed pour la cybersécurité"". https://www.silicon.fr/Thematique/cybersecurite-1371/Breves/Jacques-de-la-Riviere-Gatewatcher-nous-avons-une-approche-Best-401584.htm (Retrieved: 2026-08-11T09:19:57Z)
[18] ChannelNews. "Gatewatcher renforce son partenariat avec Devensys et Adista du groupe Inherent". https://www.channelnews.fr/gatewatcher-renforce-son-partenariat-avec-devensys-et-adista-du-groupe-inherent-155641 (Retrieved: 2026-08-11T09:19:57Z)
[19] ANSSI. "ANSSI - Catalogue des produits, services, profils de protection et sites certifiés, qualifiés, agréés". https://messervices.cyber.gouv.fr/visas/catalogue-produits-services-profils-de-protection-sites-certifies-qualifies-agrees-anssi.pdf (Retrieved: 2026-08-11T09:19:57Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 19 (kept: 19, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 1, certification_registry: 1, third_party_review: 4, vendor_datasheet: 1, vendor_doc: 12
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
