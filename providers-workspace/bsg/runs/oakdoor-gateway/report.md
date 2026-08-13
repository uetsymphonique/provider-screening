# BSG / Cross Domain Product Assessment: Oakdoor (PA Consulting) - Oakdoor Gateway

**Product ID:** `oakdoor-gateway`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T08:46:43.107583+00:00
**Total evidence items collected:** 44
**Total distinct sources:** 29

---

## 1. Overview

Oakdoor, part of PA Consulting (a UK consultancy; Oakdoor founded 2021 per the BSG provider list), markets the Oakdoor Gateway as a single-box bidirectional data gateway: it combines an Import Diode and an Export Diode - hardware data diodes implementing the UK NCSC "Safely Importing Data" and "Safely Exporting Data" patterns - with two integrated servers on either side for application-specific processing [1]. The vendor positions it as a hardware-enforced Cross Domain Solution, not a firewall: the boundary provides a protocol break (connections terminate either side of the data diodes), hardware-enforced syntax verification and software-configured semantic verification [25]. Documented deployment shapes include defence and security [7], critical national infrastructure (controlled two-way remote management) [6], IT/OT [14], SOC/SIEM [11], cloud [8] and financial services [9]. The Gateway is the bidirectional member of a product family that also includes 1G and 10G diodes [2]; the Enterprise Diode is NCSC CAPS-approved and on the US NCDSMO Diode List per vendor and press reporting [3][26]. Certification claims are vendor-reported and corroborated by third-party coverage [27][28]; no registry entry was independently reachable during this assessment.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 0                | 3      | 0   |
| partial          | 9     | 0                | 7      | 2   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 12    | 0                | 0      | 12  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 11 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | - | Vendor states the Oakdoor Gateway terminates connections either side of the data diodes (protocol break) and that imported IP frames are deconstructed in hardware and reconstructed as new packets, with content wrapped in known-good protocol headers before release into the high domain. [2], [19], [20], [25] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | - | Vendor documents the Gateway as an import/export diode pair with two integrated servers on either side and hardware-enforced unidirectional flow that cannot be bypassed without physically modifying the device. The specific dual-processing-board interconnect (FPGA or isolated shared memory) is not explicitly specified, so the exact hardware-isolation scheme is unconfirmed. [1], [3], [20], [21] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | Vendor states the diodes allow only defined, approved or specified types of structured data to pass and implement pre-defined security and authentication protocols, i.e. whitelist-style default-deny of data types. [8], [9], [16], [19], [20] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | low | - | Vendor describes hardware-implemented security-enforcing functions whose instruction set is restricted and which require physical access for reprogramming, plus state-machine SEFs that cannot be changed or compromised. No hardened OS / microkernel / SELinux claim for the integrated servers is published. [1], [2], [21] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Partial | low | - | The Gateway processing pipeline (Figure 4 of the Mind the Gap white paper) includes sanitisation, verification, transform, sign and release-authorisation stages, and software updates are released only after hash and digital-signature checks. No prose claim about cryptographically stamping clean data before each new session is published. [18], [25] |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (Vendor documents structural/content inspection ('Data structure inspection ensures that only structured data can pass') but no file-format disarm and reconstruction (DOCX/XLSX/PDF/Image/CAD) is described in the reviewed sources.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No mention of macro/script (VBA, JavaScript, DDE, embedded object) removal in the reviewed sources.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No multi-engine antivirus scanning is documented; vendor contrasts its diodes with devices that bundle 'virus screening' but does not describe any AV integration.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Partial | medium | - | Vendor documents hardware-enforced syntax verification and software-configured semantic verification of message protocols and structured data. W3C-schema validation of XML/JSON/FIXM/AIXM is not explicitly claimed. [3], [15], [25] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (Data-type filtering is documented but no classification/security-label-based information flow control is described.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No DLP keyword/regex capability is described in the reviewed sources.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography detection/removal capability is described in the reviewed sources.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | Vendor states Oakdoor products enable one- or two-way file transfer and protocol exchanges between segregated networks, and documents importing large unstructured binary files such as software updates. Specific protocols (SFTP, FTP/S, HTTPS, SMB/NFS proxy) are not enumerated. [18], [19], [26] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | - | Vendor documents one-way and controlled two-way data transfer between OT and IT networks and in critical national infrastructure, including real-time sensor monitoring data. No specific ICS protocols (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) are named. [6], [14], [17] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No database protocol proxy (SQL Server/Oracle/PostgreSQL with query whitelisting) is described in the reviewed sources.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | Vendor documents real-time transfer and inspection of SIEM/event logs into the SOC via data diodes. RTSP video proxy and CEF/Syslog relay formats are not explicitly named. [10], [11], [15], [19] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | Vendor publishes 1 Gbit/s and 10 Gbit/s diode line rates with content verification at full line rate, but no end-to-end Oakdoor Gateway throughput figure is published, so the >= 1000 Mbps Gateway CDR threshold is unconfirmed. [3], [5], [15] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | - | no evidence found (No packet/real-time processing latency figure is published in the reviewed sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | - | no evidence found (No HA active-standby or failover switchover capability/time is documented in the reviewed sources.) |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | - | no evidence found (Vendor claims the diode is impervious to software-based attacks because security functions are implemented in hardware and cannot be bypassed without physical modification, but no explicit fail-close response to DoS/overload is documented.) |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found (A dedicated management interface for remote configuration/audit/update is documented, but no role separation (system admin / policy admin / security auditor) is described.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Vendor documents real-time SIEM log transfer and inspection into the SOC via data diodes as a primary use case. CEF/Syslog format over TLS is not explicitly stated. [10], [11], [15] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No compliance-report templates (NIST SP 800-82, IEC 62443, ISO 27001) are mentioned in the reviewed sources.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | medium | - | Vendor states its diode platforms are NCSC CAPS approved (UK scheme for products handling classified information, described as superseding Common Criteria EAL testing) and that the Enterprise Diode is on the US NCDSMO Diode List. Claims are corroborated by third-party coverage but no registry entry was independently located. [3], [4], [5], [7], [26], [27] |

---

## 4. Notable Strengths

- **Protocol break at the boundary (1.1):** The Gateway terminates connections either side of the data diodes and deconstructs/reconstructs IP frames in hardware, blocking protocol-based attacks [1][20][25].
- **Hardware-enforced isolation (1.2):** An import/export diode pair with two integrated servers on either side; flow control cannot be bypassed without physically modifying the device [1][3].
- **Default-deny data filtering (1.3):** Only defined, approved or specified types of structured data pass, with pre-defined security and authentication protocols; browse-down allows only verified bitmap images into the high side [19][20][9][16].
- **National certifications (5.4):** Diode platforms are NCSC CAPS approved and the Enterprise Diode is on the US NCDSMO Diode List; the vendor states CAPS testing supersedes Common Criteria EAL [3][4][26][27].
- **Content verification pipeline (2.4):** Hardware-enforced syntax verification plus software-configured semantic verification of message protocols and structured data [15][25].

## 5. Notable Gaps / Risks

- **No CDR capability (2.1):** No file-format disarm and reconstruction (DOCX/XLSX/PDF/Image/CAD) is documented; the described inspection is structural/content-level, so buyers needing full CDR should ask whether the integrated servers run format-reconstruction modules.
- **Large undocumented surface (2.2, 2.3, 2.5, 2.6, 2.7, 3.3, 4.2, 4.3, 4.4, 5.1, 5.3):** macro/script removal, multi-engine AV, security-label IFC, DLP, anti-steganography, database proxy, processing latency, HA failover time, fail-close behavior, RBAC role separation and compliance report templates are not described in public sources; verdicts are unknown pending vendor documentation or a technical demo.
- **No end-to-end Gateway throughput (4.1):** 1 Gbit/s and 10 Gbit/s diode line rates are published, but no Gateway-level throughput figure exists, so the >= 1000 Mbps CDR threshold is unconfirmed.
- **Qualitative protocol support (3.1, 3.2, 3.4):** File transfer, IT/OT and SIEM log use cases are documented, but specific protocols (SFTP/FTP/S/HTTPS/SMB, OPC UA/Modbus/IEC 60870-5-104/DNP3/MQTT, RTSP/CEF/Syslog) are not named in any source reviewed.

## 6. Evidence Quality Notes

Seven items (1.1-1.4, 1.5-adjacent pipeline, 3.1, 5.4) draw on two or more source_types; the remaining supported/partial items rest on vendor documentation only (vendor_doc or vendor_blog), which is why all confidence values are capped at medium (or low where the mapping to the requirement is indirect). No item reached three or more genuinely independent sources: the only non-vendor material is the Nexor partnership announcement [27], Consultancy.uk coverage [28] and the techUK interview [29], all of which corroborate the product family, the 10G launch and the CAPS status but provide no independent lab testing or registry verification.

No contradictions between sources were found - vendor pages are internally consistent across product, insight and use-case pages, and third-party coverage repeats rather than disputes vendor claims. Where evidence was thin, verdicts were deliberately held at partial (qualitative claims) or unknown (metric absent), and item 5.4 was kept at medium confidence because the certification claims, while consistently repeated by vendor and press sources, could not be checked against a public registry during this run.

---

## Bibliography

[1] Oakdoor (PA Consulting). "Oakdoor Gateway | Oakdoor". https://oakdoor.io/products/oakdoor-gateway (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[2] Oakdoor (PA Consulting). "Cyber Security Hardware | Cross Domain Solutions | Oakdoor". https://oakdoor.io/ (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[3] Oakdoor (PA Consulting). "Oakdoor Enterprise Diode | Oakdoor". https://oakdoor.io/products/oakdoor-enterprise-diode (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[4] Oakdoor (PA Consulting). "Oakdoor 1G Diode | Oakdoor". https://oakdoor.io/products/oakdoor-1g-diode (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[5] Oakdoor (PA Consulting). "1G Data Diodes | Oakdoor". https://oakdoor.io/1g-data-diodes (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[6] Oakdoor (PA Consulting). "Critical national infrastructure | Oakdoor". https://oakdoor.io/industries/critical-national-infrastructure (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[7] Oakdoor (PA Consulting). "Cyber Security Solutions for Defence Industry | Oakdoor". https://oakdoor.io/industries/defence-and-security (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[8] Oakdoor (PA Consulting). "Cyber Security Solutions for Cloud Providers | Oakdoor". https://oakdoor.io/industries/cloud (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[9] Oakdoor (PA Consulting). "Cyber Security Solutions for Financial Services | Oakdoor". https://oakdoor.io/industries/financial-services (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[10] Oakdoor (PA Consulting). "Use Cases | Oakdoor". https://oakdoor.io/use-cases (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[11] Oakdoor (PA Consulting). "Protecting your SOC/SIEM infrastructure with Oakdoor | Oakdoor". https://oakdoor.io/use-cases/protect-soc-siem (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[12] Oakdoor (PA Consulting). "Securing your software updates with Oakdoor | Oakdoor". https://oakdoor.io/use-cases/secure-software-updates (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[13] Oakdoor (PA Consulting). "Enabling secure browse-down with Oakdoor | Oakdoor". https://oakdoor.io/use-cases/secure-browse-down (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[14] Oakdoor (PA Consulting). "Protecting your IT/OT infrastructure with Oakdoor | Oakdoor". https://oakdoor.io/use-cases/protect-it-ot (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[15] Oakdoor (PA Consulting). "Protecting your SOC/SIEM infrastructure with Oakdoor Hardware Security Solutions". https://d10edd1ik1f4q2.cloudfront.net/assets/ctas/Oakdoor-Protecting-SOC-SIEM-Infrastructure.pdf (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[16] Oakdoor (PA Consulting). "Enabling secure browse-down with Oakdoor Hardware Security Solutions". https://d10edd1ik1f4q2.cloudfront.net/assets/ctas/Oakdoor-Enabling-Secure-Browse-Down.pdf (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[17] Oakdoor (PA Consulting). "Protecting your IT/OT infrastructure with Oakdoor Hardware Security Solutions". https://d10edd1ik1f4q2.cloudfront.net/assets/ctas/Oakdoor-Protecting-IT-OT-Infrastructure.pdf (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[18] Oakdoor (PA Consulting). "Securing your software updates with Oakdoor Hardware Security Solutions". https://d10edd1ik1f4q2.cloudfront.net/assets/ctas/Oakdoor-Securing-Software-Updates.pdf (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[19] Oakdoor (PA Consulting). "What are Cross Domain Solutions (CDS)?". https://oakdoor.io/insights/what-is-a-cross-domain-solution-cds (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[20] Oakdoor (PA Consulting). "What is a data diode?". https://oakdoor.io/insights/what-is-a-data-diode (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[21] Oakdoor (PA Consulting). "Understanding hardware-enforced security and the role of data diodes". https://oakdoor.io/insights/understanding-hardware-enforced-security-and-the-role-of-data-diodes (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[22] Oakdoor (PA Consulting). "Oakdoor announces the launch of Enterprise Diode". https://oakdoor.io/insights/oakdoor-part-of-pa-consulting-launches-new-10g-enterprise-diode (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[23] Oakdoor (PA Consulting). "Oakdoor partners with Nexor to advance high assurance security solutions". https://oakdoor.io/insights/oakdoor-partners-with-nexor-to-advance-high-assurance-security-solutions (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[24] Oakdoor (PA Consulting). "Mind the Gap | Oakdoor". https://oakdoor.io/mind-the-gap (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[25] Gallagher Security & Oakdoor (PA Consulting). "Mind the Gap: Mitigating the risk of data flow from the perimeter to the core". https://www2.paconsulting.com/rs/526-HZE-833/images/Gallagher-and-Oakdoor-whitepaper.pdf (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[26] PA Consulting. "Oakdoor, part of PA Consulting, launches new 10G Enterprise Diode". https://www.paconsulting.com/newsroom/oakdoor-launches-new-10g-enterprise-diode-12-march-2025 (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[27] Nexor. "Nexor Announces Strategic Partnership with Oakdoor, part of PA Consulting, to Advance High Assurance Security Solutions". https://www.nexor.com/blog/nexor-announces-strategic-partnership-with-oakdoor-part-of-pa-consulting-to-advance-high-assurance-security-solutions (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[28] Consultancy.uk. "PA Consulting helps launch high-speed data diode". https://www.consultancy.uk/news/39679/pa-consulting-helps-launch-high-speed-data-diode (Retrieved: 2026-08-11T08:46:43.032688+00:00)
[29] techUK. "Talking 5 with Cyber Security Member Oakdoor". https://www.techuk.org/resource/talking-5-with-cyber-security-member-oakdoor.html (Retrieved: 2026-08-11T08:46:43.032688+00:00)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 29 (kept: 29, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** third_party_review: 3, vendor_blog: 6, vendor_doc: 20
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
