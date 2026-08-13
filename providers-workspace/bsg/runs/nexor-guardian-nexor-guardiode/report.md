# BSG / Cross Domain Product Assessment: Nexor - Nexor Guardian / Nexor GuarDiode

**Product ID:** `nexor-guardian-nexor-guardiode`
**Version reference:** Guardian 3.1 / GuarDiode 3.0+ (File Edition 4)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:31:07Z
**Total evidence items collected:** 54
**Total distinct sources:** 22

---

## 1. Overview

Nexor is a privately held UK vendor (Nottingham, founded 1989) specialising in high-assurance Cross Domain Solutions (CDS) for government, defence and critical national infrastructure [21]. The assessed line pairs Nexor Guardian, a bidirectional data guard, with Nexor GuarDiode, a managed data diode that combines guard, managed-proxy and hardware-diode technologies [1, 2]. Both are positioned as protocol-break guards rather than industrial firewalls: proxy servers strip traffic-control data and re-emit payloads across the boundary, and the diode hardware physically enforces one-way flow [4, 13]. GuarDiode ships in File, Camera and Edge/Slim variants and integrates EAL7-certified OEM diode hardware, with an NCSC CAPS-approved Oakdoor option [2, 14, 22]. Deployment shapes include physical appliances, a 1U slim form factor, virtual Guardian deployments, and G-Cloud 14 procurement [1, 2, 18]. Content inspection and Content Disarm and Reconstruction (CDR) are central to both products, with the Purifile engine removing macros, links and other active content before transfer [2, 14].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 6     | 0                | 6      | 0   |
| partial          | 12    | 0                | 12     | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 6     | 0                | 0      | 6   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 13 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | - | Protocol break is documented: proxy servers strip traffic-control data and re-emit payloads on the far side of the diode, and guards are described as full application-layer proxies that terminate and re-originate traffic. [4], [11], [13] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | - | Hardware-enforced isolation is documented via sealed tamper-evident optical diode hardware that physically terminates one direction of the link and separates upstream/downstream proxy servers. [2], [3] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | Validation is default-deny: only authorised data that meets the security policy passes, and anything that fails is held back, quarantined or rejected. [1], [2], [12] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | Nexor appliances run Red Hat Enterprise Linux with a custom SELinux policy that confines processes to the guard path, and GuarDiode 3.0 moved to RHEL 7. [8], [10] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No source describes digital signing of validated data before the guard initiates new outbound sessions.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | - | CDR is a documented core capability on Guardian and GuarDiode (Purifile engine) that strips risky elements and rebuilds content in a safe format. [1], [2], [14] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Supported | medium | - | GuarDiode CDR removes macros, links and other active content from files before transmission, corroborated by a partner blog. [2], [14], [20] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | - | Optional third-party security software and virus scanning are documented within GuarDiode's content-checking framework. [2], [8], [19] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | - | Guard checks are documented to include schema compliance and conformance of data to the configured security policy. [11], [12] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Supported | medium | - | Security labelling is listed as a Guardian feature and security-label checks are described as a configurable guard check. [1], [12] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | - | Data loss prevention is a named G-Cloud feature, and policy-driven redaction filters that block or quarantine sensitive content are documented. [2], [14], [18] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No source describes detection or removal of hidden data inside image files (steganography).) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Proxy support is documented for UDP, TCP, FTP and Samba/SMB, with multiple application protocols listed on the G-Cloud service. [2], [13], [18] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | - | no evidence found (No OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT industrial proxy support is documented.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No SQL Server, Oracle or PostgreSQL database proxy with query whitelisting is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Live and recorded camera stream viewing (GuarDiode Camera) and UDP/TCP stream-edition relays are documented, and a case study covers real-time monitoring-data streaming. [2], [8], [16] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | Nexor data diode models are offered at 1 Gbps and 10 Gbps at wire speed, and the vendor claims high throughput even with deep content inspection. [2], [3], [19] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | Only qualitative 'low latency' and 'high data processing speeds' claims are documented, including with deep content inspection. [2], [19] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Guardian 3.1 supports active-passive HA with resilient auto-replication and uninterrupted data streams during equipment or power failure. [1], [7] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | Data failing validation is held back, quarantined or rejected (fail-closed content handling), and the diode exposes no management interface for remote attack. [1], [3], [12] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (No separation of System Admin, Policy Admin and Security Auditor roles is documented.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | All GuarDiode transfers are logged and auditable with real-time system-status visibility. [2], [7] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No NIST SP 800-82, IEC 62443 or ISO 27001 compliance report templates are documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | medium | - | GuarDiode is marketed with CC EAL7+ and NCSC CAPS-aligned configurations; the EAL7 certificate (NSCIB-CC-2300039-01) covers the OEM Fox Crypto Fort Fox diode hardware used in File Edition 4, and company-level ISO 27001 is certified. [2], [14], [18], [21], [22] |

---

## 4. Notable Strengths

- **Protocol break and hardware-enforced one-way flow (items 1.1, 1.2):** proxies strip traffic-control data and re-emit payloads across a physically terminated, tamper-evident optical link, eliminating any IP-level return path [3, 4, 13].
- **Default-deny validation (item 1.3):** only data that meets the security policy passes; anything failing is held back, quarantined or rejected [1, 2, 12].
- **CDR and active-content removal (items 2.1, 2.2):** the Purifile-based CDR strips risky elements and rebuilds content in a safe format, removing macros and links, corroborated by a partner blog [1, 2, 14, 20].
- **Security labelling and redaction-based DLP (items 2.5, 2.6):** security-label checks and policy-driven redaction/quarantine filters are documented features, with data loss prevention a named G-Cloud capability [1, 12, 14, 18].
- **Certification posture (item 5.4):** GuarDiode is marketed with Common Criteria EAL7+ and NCSC CAPS-aligned configurations; the EAL7 certificate covers the Fox Crypto Fort Fox diode hardware inside File Edition 4, and the company holds ISO 27001 [2, 18, 21, 22].

## 5. Notable Gaps / Risks

- **No published performance numbers (items 4.1, 4.2, 4.3):** CDR-path throughput, processing latency and HA switchover time are only described qualitatively, so the >=1 Gbps CDR throughput, <=10 ms latency and <=100 ms failover requirements cannot be confirmed; a technical specification sheet exists but is only available on request [2, 7, 19].
- **No OT/ICS protocol proxies (item 3.2):** OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 and MQTT proxy support is not documented anywhere in the public material; the diode is only described generically for ICS/SCADA telemetry use cases.
- **No database proxy (item 3.3):** SQL Server, Oracle or PostgreSQL proxying with query whitelisting is not documented.
- **RBAC and compliance reporting undocumented (items 5.1, 5.3):** no evidence of System Admin / Policy Admin / Auditor role separation or NIST SP 800-82 / IEC 62443 / ISO 27001 report templates.
- **SIEM and anti-steganography gaps (items 5.2, 2.7):** transfers are logged and auditable but CEF/Syslog-over-TLS export to a SIEM is not confirmed, and no hidden-data-in-image detection is described.

## 6. Evidence Quality Notes

All 24 checklist items were assessed in standard mode using 22 distinct staged sources and 54 evidence entries, every one of which is grounded verbatim in the staged artifact text (citation-grounding check: 54/54 grounded, 0 fabricated, 0 unverifiable). Thirteen items are backed by at least two source types; the strongest triangulation is on item 5.4, which combines the vendor claim with the NSCIB certificate, Wikipedia, the G-Cloud listing and a vendor release note. Non-vendor sources (Wikipedia [21], Sentyron blog [20], the UK G-Cloud registry [18], and the TrustCB/NSCIB certificate [22]) were used where available, but most items still rest on vendor pages and blogs, which is why confidence is capped at medium throughout - no item reached high confidence under the validator rule.

One nuance shaped the 5.4 verdict: the EAL7 certificate found in the Common Criteria registry is issued to Fox Crypto B.V. for the Fort Fox Hardware Data Diode, the OEM hardware that Nexor integrates into GuarDiode File Edition 4, and no current Nexor-branded product appears in the registry [22]; the Nexor-branded EAL7 claim comes from the vendor and Wikipedia [2, 21]. No contradictions between sources were found. The main limitation is quantitative: the vendor publishes no millisecond or per-path Mbps figures for the guard/CDR processing path, so items 4.1-4.3 remain partial rather than supported.

---

## Bibliography

[1] Nexor. "Nexor Guardian - Data Guard". https://www.nexor.com/guardian (Retrieved: 2026-08-11T08:20:43Z)
[2] Nexor. "Nexor GuarDiode - Managed Data Diode". https://www.nexor.com/guardiode (Retrieved: 2026-08-11T08:20:43Z)
[3] Nexor. "Nexor Data Diode - One Way Data Flow". https://www.nexor.com/data-diode (Retrieved: 2026-08-11T08:20:58Z)
[4] Nexor. "Nexor Data Diode FAQs". https://www.nexor.com/data-diode-faqs (Retrieved: 2026-08-11T08:23:48Z)
[5] Nexor. "Cyber Security Solutions". https://www.nexor.com/solutions (Retrieved: 2026-08-11T08:27:22Z)
[6] Nexor. "Our Accreditations". https://www.nexor.com/about/our-accreditations (Retrieved: 2026-08-11T08:21:01Z)
[7] Nexor. "Press Release - Guardian 3.1 - High Availability". https://www.nexor.com/blog/guardian3-1-high-availability (Retrieved: 2026-08-11T08:23:17Z)
[8] Nexor. "GuarDiode 3.0 Press Release". https://www.nexor.com/blog/guardiode-3-0-press-release (Retrieved: 2026-08-11T08:23:17Z)
[9] Nexor. "Discover the power of Nexor GuarDiode: tailored cross domain security solutions". https://www.nexor.com/blog/discover-the-power-of-nexor-guardiode-tailored-cross-domain-security-solutions (Retrieved: 2026-08-11T08:23:19Z)
[10] Nexor. "Securing the Guard". https://www.nexor.com/blog/securing-the-guard (Retrieved: 2026-08-11T08:23:42Z)
[11] Nexor. "What is the difference between a Guard and a Gateway?". https://www.nexor.com/blog/guard-or-gateway (Retrieved: 2026-08-11T08:23:44Z)
[12] Nexor. "File transfers for a data guard: automate or manually review?". https://www.nexor.com/blog/file-transfers-data-guard (Retrieved: 2026-08-11T08:23:46Z)
[13] Nexor. "Securing sensitive data transfers: Unlocking the potential of data diodes and proxies". https://www.nexor.com/blog/securing-sensitive-data-transfers-unlocking-the-potential-of-data-diodes-and-proxies (Retrieved: 2026-08-11T08:24:52Z)
[14] Nexor. "Introducing Nexor GuarDiode File Edition 4: Secure Collaboration Made Simple". https://www.nexor.com/blog/introducing-nexor-guardiode-file-edition-4-secure-collaboration-made-simple (Retrieved: 2026-08-11T08:24:55Z)
[15] Nexor. "Secure Remote Video Control (Case Study, European Defence Ministry)". https://www.nexor.com/knowledge-hub/case-studies/secure-remote-video-control (Retrieved: 2026-08-11T08:23:49Z)
[16] Nexor. "Network Monitoring (Case Study, UK Government Agency)". https://www.nexor.com/knowledge-hub/case-studies/network-monitoring (Retrieved: 2026-08-11T08:23:42Z)
[17] Nexor. "Secure and Efficient Manual Release of Files Across Networks (Case Study)". https://www.nexor.com/knowledge-hub/case-studies/files-transfer-secure-networks (Retrieved: 2026-08-11T08:23:46Z)
[18] UK Crown Commercial Service / Digital Marketplace. "Nexor GuarDiode - Digital Marketplace (G-Cloud 14)". https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/152043636001857 (Retrieved: 2026-08-11T08:24:30Z)
[19] Nexor. "Nexor GuarDiode - Service Definition Document (G-Cloud 14)". https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/92446/152043636001857-service-definition-document-2022-05-18-0938.pdf (Retrieved: 2026-08-11T08:28:19Z)
[20] Sentyron. "Making secure collaboration possible with the Nexor GuarDiode File Edition 4". https://sentyron.com/making-secure-collaboration-possible-with-the-nexor-guardiode-file-edition-4/ (Retrieved: 2026-08-11T08:24:31Z)
[21] Wikipedia. "Nexor (Wikipedia)". https://en.wikipedia.org/wiki/Nexor (Retrieved: 2026-08-11T08:24:52Z)
[22] TrustCB / NSCIB. "Fort Fox Hardware Data Diode FFHDD3_1/10 - NSCIB Common Criteria Certificate NSCIB-CC-2300039-01". https://www.commoncriteriaportal.org/nfs/ccpfiles/files/epfiles/NSCIB-CC-2300039-01-Cert.pdf (Retrieved: 2026-08-11T08:28:04Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 22 (kept: 22, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** case_study: 3, certification_registry: 1, regulatory_filing: 1, third_party_review: 2, vendor_blog: 8, vendor_doc: 7
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
