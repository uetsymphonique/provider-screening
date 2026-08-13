# Product Assessment: ABB - ABB Ability Security Gateway

**Product ID:** `abb-ability-security-gateway`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 2
**Assessed at:** 2026-08-11T09:35:00Z
**Total evidence items collected:** 7
**Total distinct sources:** 4

---

## 1. Overview

No ABB product named "ABB Ability Security Gateway" could be found in any indexed source. Exact-phrase searches on DuckDuckGo, Bing, Startpage (Google index) and Yandex return zero results; the ABB Library download-center search API returns no document with that title; and no page for the product exists on abb.com (the URL that would host it, new.abb.com/abb-ability/cybersecurity/security-gateway, now soft-redirects to the ABB homepage). ABB's actual cyber security offering is a portfolio of consultancy, technology and services - ABB Ability Cyber Security Assess, Protect and Workplace [1] - with no hardware security-gateway appliance listed. The closest-named ABB gateway products, the ABB Ability Edge Industrial Gateway [4] and the Connectivity Edge Gateway EGW-02 [2], are IoT data gateways (LTE/Wi-Fi connectivity, cloud data collection) for electrification and drive equipment, not bidirectional security gateways or firewalls; ABB's "Security and Service Gateway" appears only as an architecture component of the ABB Service Platform for remote service access [3]. Because no documentation of the named product exists, all 24 checklist items are recorded as unknown (absence of evidence), and the BSG vendor list entry should be treated as a product-identification error pending correction.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 0     | 0                | 0      | 0   |
| partial          | 0     | 0                | 0      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 24    | 0                | 0      | 24  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 0 items backed by ≥ 2 source_types; 0 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Unknown | low | - | no evidence found (No documentation exists for a product named 'ABB Ability Security Gateway' (product identification failure, see run_manifest assumption asm_00000001); a protocol-break architecture is therefore not evidenced.) |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no dual-board / FPGA / shared-memory isolation design is documented anywhere.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no default-deny / whitelist behavior is documented.) |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | - | no evidence found (No product documentation exists for this product name; no hardened-OS / microkernel / SELinux claim is documented.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no internal data stamping is documented.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no CDR capability for Office/PDF/image/CAD is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no macro/script/DDE/embedded-object removal is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no multi-AV integration is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no XML/JSON/FIXM/AIXM schema validation is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no security-label-based filtering (IFC) is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no DLP keyword/pattern blocking is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No product documentation exists for this product name; no anti-steganography engine is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no file-transfer protocol proxy (SFTP/FTP/HTTPS/SMB/NFS) is documented.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no OT/ICS protocol support (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) is documented.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no database protocol proxy (SQL Server/Oracle/PostgreSQL) is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no realtime stream relay (RTSP/Syslog/CEF) is documented.) |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | - | no evidence found (No product documentation exists for this product name; no throughput figure is published.) |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no latency figure is published.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no HA failover behavior or switchover time is published.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no fail-close/DoS self-defense behavior is documented.) |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no RBAC role separation is documented.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no SIEM/SOAR log export (CEF/Syslog over TLS) is documented.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | - | no evidence found (No product documentation exists for this product name; no Common Criteria / FIPS / national crypto certification is documented (ABB's actual EGW-02 gateway carries IEC 62443-4-2 SL2, but that is a different product).) |

---

## 4. Notable Strengths

No checklist item (1.1-5.4) could be verified as supported for a product named "ABB Ability Security Gateway", because no documentation of such a product exists. The following facts about ABB's actual products are documented for context, but apply to different products than the one named in the vendor list:

- **ABB's actual gateway hardware is certified (item 5.4 context):** the Connectivity Edge Gateway EGW-02 is "certified for IEC 62443-4-2 SL2" and uses hardware-based key-material encryption [2] - relevant if the intended product was ABB's EGW-02 or Edge Industrial Gateway rather than a security gateway.
- **ABB's cyber security portfolio is real and active (portfolio context):** ABB offers an end-to-end OT security portfolio across consultancy, technology and services [1], so ABB does have security capability to sell - just not under the name "ABB Ability Security Gateway".

## 5. Notable Gaps / Risks

- **Product identification failure (all items):** no ABB product named "ABB Ability Security Gateway" could be located in any indexed source or in the ABB Library; all 24 checklist items are therefore unknown. The vendor-list entry must be corrected to a real ABB product (e.g. ABB Ability Edge Industrial Gateway, Connectivity Edge Gateway EGW-02) or dropped before any procurement decision, otherwise the comparison matrix will show a phantom product.
- **No BSG-class capability evidence (items 1.1-5.4):** even ABB's closest real gateways are IoT data gateways, not protocol-break guards, CDR engines or industrial NGFWs [2, 4], so a buyer needing a Bidirectional Security Gateway should not expect ABB's current gateway line to supply it.
- **Portfolio pages do not substitute for product documentation (items 1.4, 2.3, 4.x, 5.x):** ABB's cyber security portfolio pages [1, 3] describe services and reference architectures, not appliance-level capabilities such as hardened OS, multi-AV scanning, throughput, latency, HA failover or certifications; these items would remain unresolvable even for ABB's real products without their device manuals.

## 6. Evidence Quality Notes

Zero checklist items are backed by evidence: all 24 are unknown by design, because the anti-fabrication contract requires unknown (never not_supported or not_applicable) when no product documentation exists. Four vendor sources were staged and cited for the identification finding itself - the ABB Ability Cyber Security Portfolio page [1], the Connectivity Edge Gateway EGW-02 product page [2], the ABB Ability Cyber Security Services Portfolio brochure [3], and the ABB Ability Edge Industrial Gateway User Manual [4] - all of which are vendor-authored, so the finding is corroborated across multiple ABB channels (marketing pages, download-center brochure, technical manual) but not by any independent third-party source.

The identification methodology used five independent search systems (DuckDuckGo, Bing, Startpage/Google, Yandex, and the ABB Library discovery API) plus direct probing of abb.com site structure; exact-phrase searches for "ABB Ability Security Gateway" and "ABB Security Gateway" returned zero results on every engine. No sources contradicted each other - every located ABB source consistently describes ABB's gateways as IoT data gateways and its cyber security offering as services/software. The verdicts are chosen as unknown rather than not_applicable because no source establishes the named product's category (the prerequisite for not_applicable per the GUIDE), and rather than not_supported because no source evaluates and rejects a capability. Recommended follow-up: confirm the intended ABB product with the vendor-list owner, then re-run this assessment against the correct product_id.

---

## Bibliography

[1] ABB. "ABB Ability™ Cyber Security Portfolio". https://new.abb.com/industrial-software/cyber-security-portfolio (Retrieved: 2026-08-11T09:19:00Z)
[2] ABB. "Connectivity Edge Gateway - EGW-02". https://www.abb.com/global/en/areas/motion/drives/connectivity/iot-connectivity-solutions/connectivity-edge-gateway-egw-02 (Retrieved: 2026-08-11T09:19:03Z)
[3] ABB AG. "ABB Ability™ Cyber Security Services Portfolio (German edition)". https://search.abb.com/library/Download.aspx?DocumentID=9AKK108469A1537&LanguageCode=de&DocumentPartId=&Action=Launch (Retrieved: 2026-08-11T09:19:22Z)
[4] ABB. "ABB Ability™ Edge Industrial Gateway - User Manual". https://search.abb.com/library/Download.aspx?DocumentID=9AKK107991A7743&DocumentRevisionId=C (Retrieved: 2026-08-11T09:19:31Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 4 (kept: 4, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** vendor_datasheet: 2, vendor_doc: 2
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
