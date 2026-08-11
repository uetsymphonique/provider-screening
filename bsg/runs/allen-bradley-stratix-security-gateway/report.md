# BSG / Cross Domain Product Assessment: Rockwell Automation — Allen-Bradley Stratix Security Gateway

**Product ID:** `allen-bradley-stratix-security-gateway`
**Version reference:** Stratix 5900 Security Gateway (runs Cisco IOS 15.6(3)M1 per ICS-CERT advisory coverage)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:35:00Z
**Total evidence items collected:** 12
**Total distinct sources:** 9

---

## 1. Overview

The Allen-Bradley Stratix 5900 Security Gateway is an industrial firewall/security gateway that Rockwell Automation sells as part of the Allen-Bradley Stratix networking portfolio, which is the Rockwell side of the Cisco-Rockwell Converged Plantwide Ethernet (CPwE) partnership [2]. Independent coverage places the Stratix 5900 in the Stratix security appliance family that Cisco documents as an Industrial Security Appliance based on Cisco ASA security software with FirePOWER Services, i.e. a stateful firewall/VPN/threat-detection platform rather than a protocol-break guard [1]; a third-party integration video titles the device a "cell zone firewall" [4]. ICS-CERT-based reporting confirms the unit runs Cisco IOS 15.6(3)M1, a Cisco router/firewall-class operating system [6]. Because the vendor's own product page and datasheet could not be retrieved from this environment (rockwellautomation.com and literature.rockwellautomation.com returned HTTP 403), capability verdicts are anchored to the reachable Cisco-partner, third-party, and certification-registry sources: guard-specific items are marked not applicable, while protocol, performance, and management details remain unknown pending vendor documentation.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 0     | 0                | 0      | 0   |
| partial          | 2     | 0                | 1      | 1   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 8     | 0                | 8      | 0   |

**Evidence quality:** 2 items backed by ≥ 2 source_types; 1 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Third-party and Cisco-partner sources characterize the Stratix 5900 as an industrial firewall: a third-party video titles it a 'cell zone firewall', ICS-CERT-based reporting lists it as a Cisco IOS 15.6(3)M1 device, and Cisco documents the Stratix security appliance family as ASA+FirePOWER-based. No protocol-break or session-termination architecture is documented or marketed for this product.
- **1.2:** The same category evidence identifies the Stratix 5900 as a firewall-class Cisco IOS device; no dual processing-board/FPGA or shared-memory isolation architecture is documented for it.
- **1.5:** The Stratix 5900 is a firewall-class device per the category sources; no internal data-stamping/session-re-initiation core of the kind found in guards is documented for it.
- **2.1:** The product category is industrial firewall/security gateway (cell-zone firewall with Cisco ASA/FirePOWER-based security software), not a content-sanitizing CDS. No content disarm and reconstruction engine is documented for it.
- **2.2:** Document-level macro/script removal (VBA, JavaScript, DDE, embedded objects) is a CDR content-sanitization capability that is not applicable to this firewall-class product per the category evidence.
- **2.4:** XML/JSON/FIXM/AIXM schema validation is a CDS document-processing capability not applicable to this firewall-class product per the category evidence.
- **2.5:** No security-label-based information flow control is documented for this firewall-class product; the category sources do not describe label-aware filtering.
- **2.7:** Anti-steganography detection in image files is a CDS guard capability not applicable to this firewall-class product per the category evidence.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Third-party and Cisco-partner sources characterize the Stratix 5900 as an industrial firewall: a third-party video titles it a 'cell zone firewall', ICS-CERT-based reporting lists it as a Cisco IOS 15.6(3)M1 device, and Cisco documents the Stratix security appliance family as ASA+FirePOWER-based. No protocol-break or session-termination architecture is documented or marketed for this product. [1], [4], [6] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The same category evidence identifies the Stratix 5900 as a firewall-class Cisco IOS device; no dual processing-board/FPGA or shared-memory isolation architecture is documented for it. [4], [6] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | low | — | Cisco-partner documentation describes the Stratix security appliance family (ASA+FirePOWER-based) as providing access control and consistent policy enforcement across OT/IT infrastructure, which is the mechanism for default-deny filtering. An explicit whitelist-only/default-deny statement specific to the Stratix 5900 was not found in reachable sources. [1] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | ICS-CERT-based reporting documents that the Stratix 5900 runs Cisco IOS 15.6(3)M1, a purpose-built network operating system rather than a general-purpose OS. Microkernel or SELinux-strict-mode hardening of the OS is not documented in reachable sources. [6] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | The Stratix 5900 is a firewall-class device per the category sources; no internal data-stamping/session-re-initiation core of the kind found in guards is documented for it. [4], [6] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | The product category is industrial firewall/security gateway (cell-zone firewall with Cisco ASA/FirePOWER-based security software), not a content-sanitizing CDS. No content disarm and reconstruction engine is documented for it. [1], [4], [6] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | N/A | medium | — | Document-level macro/script removal (VBA, JavaScript, DDE, embedded objects) is a CDR content-sanitization capability that is not applicable to this firewall-class product per the category evidence. [4], [6] |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No vendor documentation reachable to verify multi-AV integration.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | XML/JSON/FIXM/AIXM schema validation is a CDS document-processing capability not applicable to this firewall-class product per the category evidence. [4], [6] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | No security-label-based information flow control is documented for this firewall-class product; the category sources do not describe label-aware filtering. [4], [6] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No vendor documentation reachable to verify DLP.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | Anti-steganography detection in image files is a CDS guard capability not applicable to this firewall-class product per the category evidence. [4], [6] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | — | no evidence found |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Unknown | low | — | no evidence found |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Unknown | low | — | no evidence found |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (ICS-CERT reporting covers DoS vulnerabilities but not the device's fail-safe state behavior.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (Cisco-partner material discusses SIEM ingestion for Cisco Cyber Vision telemetry from Stratix switches, not the 5900 gateway itself.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Not Supported | medium | — | The authoritative registries contain no certification for the Stratix 5900 or its Cisco-based platform: ISASecure's IEC 62443-4-2 list covers only the Stratix 5200/5800 switches, and the Common Criteria portal and NIST CMVP list Cisco certifications only for other firewall platforms (e.g. FTD EAL4+, ASA on FPR 1000 Series). No CC EAL4+, FIPS 140-3, or national crypto certification for this product was found. [7], [8], [9] |

---

## 4. Notable Strengths

- **Cell-zone firewall positioning for OT segmentation (item 1.1, 1.3):** The Stratix 5900 is positioned as a cell-zone firewall, and Cisco documents the Stratix security appliance family as providing access control and consistent policy enforcement across OT/IT infrastructure [1, 4].
- **Cisco-based, patch-coordinated security platform (item 1.4):** The unit runs Cisco IOS 15.6(3)M1, a purpose-built network operating system whose vulnerabilities are patched in coordinated Rockwell/Cisco advisories, per ICS-CERT-based reporting [6].
- **IEC 62443 ecosystem for the Stratix portfolio (item 5.4 context):** Sibling Stratix 5200/5800 switches carry ISASecure IEC 62443-4-2 CSA Level 2 certification, and CPwE designs are the reference architecture for ISA/IEC 62443 zone-based segmentation [2, 7].
- **Default-off IPsec posture in the appliance family (item 1.3 context):** ICS-CERT advisory coverage notes the IPsec feature on the Stratix security appliance line is disabled by default, an example of a conservative default security posture [5].

## 5. Notable Gaps / Risks

- **OT protocol handling unverified (item 3.2):** No reachable source documents OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, or MQTT proxy behavior for the Stratix 5900; buyers relying on ICS protocol inspection must confirm against Rockwell's current literature.
- **Throughput, latency, and HA figures unavailable (items 4.1, 4.2, 4.3):** No numeric firewall throughput, processing latency, or failover time was found in any reachable source, so the checklist thresholds cannot be evaluated without the vendor datasheet or independent tests.
- **No certification found in authoritative registries (item 5.4):** The Common Criteria portal, NIST CMVP, and ISASecure registries list no certification for the Stratix 5900 or its platform (ISASecure covers only the Stratix 5200/5800 switches); a FIPS 140-3, Common Criteria, or IEC 62443 requirement would need explicit vendor confirmation.
- **Fail-safe behavior unverified (item 4.4):** ICS-CERT reporting documents DoS vulnerabilities in Stratix devices running Cisco software but not the gateway's fail-close behavior under DoS.
- **Management and operations evidence gap (items 5.1, 5.2, 5.3):** RBAC role separation, real-time SIEM log export, and compliance report templates are undocumented in reachable sources.

## 6. Evidence Quality Notes

This assessment was severely source-constrained: rockwellautomation.com, literature.rockwellautomation.com, and cisco.com returned HTTP 403 (Akamai) from this environment, web.archive.org and archive.ph returned persistent HTTP 429, and most search engines were bot-blocked, so no vendor datasheet, user manual, or archived product page could be staged. Discovery was limited to Marginalia, Google News RSS, and direct domain probing. Consequently only 12 evidence quotes across 9 staged sources were available, and every staged quote was verified verbatim by verify_citation_grounding.py (12/12 grounded, 0 fabricated, 0 unverifiable). No item was triangulated across three or more independent source types; item 5.4 draws on three independent certification registries (negative findings), while the category and capability claims behind items 1.1-2.x rest on Cisco partner blogs (vendor_blog), Security Affairs/ICS-CERT coverage, and one independent integration video.

Sources were consistent rather than contradictory — none suggested the Stratix 5900 is anything other than a Cisco-based industrial firewall. Confidence is capped at medium for every non-unknown verdict because no analyst report or independent lab test was reachable; a procurement decision should re-verify throughput, OT-protocol support, HA behavior, and certification claims against Rockwell's current Stratix 5900 datasheet and user manual before treating any partial or unknown verdict as resolved.

---

## Bibliography

[1] Cisco Systems, Inc.. "Security + Performance = Key Trends at Automation Fair". https://blogs.cisco.com/manufacturing/rockwell-automations-automation-fair-recap (Retrieved: 2026-08-11T09:35:00Z)
[2] Cisco Systems, Inc.. "A blueprint for the modern industrial network from Cisco and Rockwell Automation". https://blogs.cisco.com/industrial-iot/delivering-secure-industrial-connectivity-at-rockwell-automation-fair-2021 (Retrieved: 2026-08-11T09:35:00Z)
[3] Cisco Systems, Inc.. "How Visibility-Driven Segmentation is Redefining the OT Security Starting Line". https://blogs.cisco.com/industrial-iot/how-visibility-driven-segmentation-is-redefining-the-ot-security-starting-line (Retrieved: 2026-08-11T09:35:00Z)
[4] YouTube. "9 Stratix 5900 Cell Zone Firewall Video (Elvatron S.A.)". https://www.youtube.com/watch?v=GsVMgZkRM1Y (Retrieved: 2026-08-11T09:35:00Z)
[5] Security Affairs. "Rockwell Automation fixes multiple DoS flaws in Stratix Switch introduced by Cisco Software". https://securityaffairs.com/83477/security/rockwell-patches-stratix-flaws.html (Retrieved: 2026-08-11T09:35:00Z)
[6] Security Affairs. "Cisco IOS vulnerabilities open Rockwell Industrial Switches to attacks". https://securityaffairs.com/62347/breaking-news/cisco-ios-flaws-rockwell.html (Retrieved: 2026-08-11T09:35:00Z)
[7] ISA Security Compliance Institute (ISASecure). "IEC 62443-4-2 Certified Components (CSA/EDSA)". https://isasecure.org/end-users/iec-62443-4-2-certified-components (Retrieved: 2026-08-11T09:35:00Z)
[8] Common Criteria Portal. "Certified Products (Common Criteria portal registry)". https://www.commoncriteriaportal.org/products/certified_products.csv (Retrieved: 2026-08-11T09:35:00Z)
[9] NIST Computer Security Resource Center. "Cryptographic Module Validation Program - Validated Modules (NIST CMVP)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search/all (Retrieved: 2026-08-11T09:35:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 9 (kept: 9, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 3, third_party_review: 3, vendor_blog: 3
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
