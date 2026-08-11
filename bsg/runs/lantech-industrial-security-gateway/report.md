# BSG / Cross Domain Product Assessment: Lantech Communications — Lantech Industrial Security Gateway

**Product ID:** `lantech-industrial-security-gateway`
**Version reference:** Anchored to the documented Lantech security product families matching the BSG.csv product description (encryption + bidirectional filtering for transport/energy): OS5 security switches (software datasheet v2.7, May 2026), industrial multifunction VPN routers, T(P)GS-3208GF router switch (datasheet v1.6), and the LFW professional firewall appliance series. No SKU is marketed under the exact name 'Industrial Security Gateway'.
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:45:00Z
**Total evidence items collected:** 42
**Total distinct sources:** 9

---

## 1. Overview

Lantech Communications (Taiwan, founded 1986) is an industrial networking vendor, not a cross-domain-guard manufacturer: the documented portfolio comprises ruggedized managed Ethernet switches (OS5 / OS4 / OS3 / OS2PRO platforms), security switches, industrial multifunction 4G/Wi-Fi VPN routers, router-switch hybrids such as the T(P)GS-3208GF, and the legacy LFW professional firewall appliance line [3, 6, 8]. No device is marketed under the exact name "Industrial Security Gateway" on the vendor's current site, its live legacy pages, or archived 2016-2022 snapshots; the BSG.csv entry is therefore assessed against the security gateway-class families that match its description (encryption and bidirectional filtering for transportation and energy): the OS5 security switch platform with IEC 62443-4-2 SL-2 cybersecurity, the VPN routers with Layer-4 firewall and Modbus gateway, and the LFW stateful-inspection firewall appliances [1, 6, 8]. Deployment shapes documented include DIN-rail industrial switching, EN50155 rolling-stock and IP54/IP67 vehicle applications, and LTE multi-WAN VPN meshes for rail, ITS, smart-city and energy networks [6, 7].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 13 items backed by ≥ 2 source_types; 15 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Lantech markets industrial Ethernet switches, security switches and multifunction VPN routers with a stateful inspection firewall appliance line; no protocol-break (TCP/IP session termination) guard architecture exists.
- **1.2:** Vendor documents industrial switches, security switches and multifunction VPN routers/firewall appliances; no dual-board protocol-break isolation is described anywhere in the product line.
- **1.5:** Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope.
- **2.1:** No content disarm & reconstruction engine is documented; the products are switches, VPN routers and a stateful inspection firewall appliance.
- **2.4:** Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope.
- **2.5:** Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope.
- **2.7:** Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Lantech markets industrial Ethernet switches, security switches and multifunction VPN routers with a stateful inspection firewall appliance line; no protocol-break (TCP/IP session termination) guard architecture exists. [3], [6], [8] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | Vendor documents industrial switches, security switches and multifunction VPN routers/firewall appliances; no dual-board protocol-break isolation is described anywhere in the product line. [2], [3], [8] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Unknown | low | — | no evidence found (No source documents a default-deny / whitelist-only forwarding policy; firewall and ACL behavior is not described in the gathered documentation.) |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | — | OS5 documents secure boot with signature verification, SSH hardening per BSI TR-02102-4, memory purging, a hardware security IC, and IEC 62443-4-2 SL2 security measures; no microkernel/SELinux strict-mode OS is claimed. [1], [4], [8] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope. [3], [6] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | No content disarm & reconstruction engine is documented; the products are switches, VPN routers and a stateful inspection firewall appliance. [3], [6], [8] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No file-content inspection or macro/script removal capability is documented for any Lantech device.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No antivirus engine integration is documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope. [3], [6] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope. [2], [3] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No data-loss-prevention (keyword/regex) filtering is documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | Vendor documents only industrial switches, security switches and multifunction VPN routers/firewall appliances; no guard/CDS architecture exists in the documented portfolio, so this guard-specific capability is out of scope. [3], [8] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | — | no evidence found (No file-transfer protocol proxy with content cleaning (SFTP/FTP/S/HTTPS/SMB/NFS) is documented.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | Routers embed a Modbus gateway (Modbus RTU/ASCII to Modbus TCP) and the T(P)GS-3208GF can act as an MQTT publisher or broker; OPC UA, IEC 60870-5-104 and DNP3 proxies are not documented. [6], [7] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No SQL Server / Oracle / PostgreSQL database proxy is documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | — | no evidence found (No RTSP video proxy or Syslog/CEF unidirectional/bidirectional relay is documented.) |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | The T(P)GS-3208GF datasheet documents a 20 Gbps switching fabric (back-plane), but no CDR or firewall inspection throughput figure is published, so the >=1000 Mbps inspection-throughput threshold cannot be confirmed. [7] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No processing-latency figure is published for any Lantech security gateway/switch device.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | G.8032 ring self-heal recovery below 20ms and sub-50ms fault recovery are documented on OS5 switches, and VRRP gateway redundancy on routers; no active-standby switchover time with session preservation is specified. [4], [6], [7] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Supported | medium | — | OS5 security switch documents fail-close Island Mode that isolates the network boundary on breach detection, plus DDoS attack protection; OS5 and T(P)GS-3208GF list prevention of DDoS/DoS attacks. [1], [4], [7] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | OS5 documents RBAC separating read-only and read-write privileges with audit trails; separation of System Admin, Policy Admin and Auditor roles is not explicitly described. [1] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | OS5 supports Syslog and Syslog over TLS plus a remote system log server; no explicit SIEM/SOAR integration or CEF-format export is documented. [1], [4] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | OS5 can generate machine-readable reports of current security settings for compliance and auditing; no NIST SP 800-82 / IEC 62443 / ISO 27001 report templates are documented. [1] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | — | OS5 generation products hold IEC 62443-4-2 SL2 certification (Cert. No. FRCyber10275, Bureau Veritas LCIE) and IEC 62443-4-1 development-lifecycle certification (FRCyber10088), corroborated by distributor Arcobel; no Common Criteria EAL4+, FIPS 140-3 or national crypto certification is documented. [3], [4], [5], [9] |

---

## 4. Notable Strengths

- **IEC 62443-4-2 SL-2 certification (item 5.4):** OS5 generation products hold IEC 62443-4-2 Security Level 2 certification (Certificate No. FRCyber10275 issued by Bureau Veritas LCIE) plus IEC 62443-4-1 development-lifecycle certification (FRCyber10088), corroborated by partner-distributor Arcobel [5, 3, 9].
- **Fail-close and DDoS resilience (item 4.4):** the OS5 security switch documents Island Mode / Fail Close that isolates the network boundary on breach detection, with DDoS attack protection listed across the OS5 datasheet and the T(P)GS-3208GF [1, 4, 7].
- **Hardened platform (item 1.4):** secure boot with signature verification, SSH hardening per BSI TR-02102-4, memory purging, a hardware security IC, and 90+ IEC 62443-4-2 security measures are documented on the OS5 platform [1, 4].
- **OT protocol reach (item 3.2):** routers embed a Modbus RTU/ASCII-to-TCP gateway and the T(P)GS-3208GF can act as an MQTT publisher or broker [6, 7].
- **Fast ring failover (item 4.3):** G.8032 ring self-heal recovery below 20 ms and sub-50 ms fault recovery are documented for OS5 switches and the router-switch line [4, 7].

## 5. Notable Gaps / Risks

- **Product identity (scope):** no Lantech device is marketed as "Industrial Security Gateway", so the buyer must pin the requirement to a concrete family (OS5 security switch vs. multifunction VPN router vs. LFW firewall) and verify the exact SKU before procurement [3, 6].
- **No inspection-throughput spec (item 4.1):** only switching-fabric figures (e.g. 20 Gbps back-plane on T(P)GS-3208GF) are published; no firewall/CDR inspection throughput per model, so the >=1000 Mbps threshold cannot be confirmed [7].
- **No latency figures (item 4.2):** no processing-latency specification is published for any Lantech security gateway-class device.
- **No active-standby switchover spec (item 4.3):** ring-based recovery (<20 ms) and VRRP are documented, but no <=100 ms session-preserving active-standby switchover time [4, 6, 7].
- **Content-security gap (items 2.2, 2.3, 2.6, 3.1):** no CDR, multi-AV, DLP or file-transfer cleaning exists on the documented platform; buyers requiring file sanitization or whitelist-protocol database proxying must select a different product class.
- **SIEM/audit depth (items 5.2, 5.3):** Syslog over TLS and machine-readable security reports are documented, but no CEF/SOAR integration or named NIST/IEC/ISO report templates [1, 4].

## 6. Evidence Quality Notes

Every non-unknown verdict (16 items) rests on vendor-authored material: solution pages, product pages, the company profile, two current datasheets (OS5 software v2.7; T(P)GS-3208GF v1.6), a 2026 certification press release, and the 2011 LFW-1003 firewall datasheet. Only item 5.4 additionally cites a non-vendor host (Arcobel, a partner-distributor whose article mirrors the vendor's certification announcement), so no fully independent lab, analyst or registry source was obtained; discovery was constrained because major search engines bot-blocked this environment and the wayback machine rate-limited direct access. Per the project rule, all vendor-only verdicts are confidence-capped at medium. Multiple items were triangulated across 2-4 vendor sources (e.g. 4.4 uses the security-switch page, the OS5 datasheet and the T(P)GS-3208GF datasheet; 4.3 uses the OS5 datasheet, the T(P)GS datasheet and the router page), and no contradictions between sources were found.

Two transparency caveats apply. First, the Arcobel page is Cloudflare-protected and could not be fetched as raw HTML; it was staged manually from the r.jina.ai reader rendering, which is flagged in the artifact manifest. Second, the exact "Industrial Security Gateway" SKU could not be located on the current site, the live legacy pages, or archived 2016-2022 snapshots, so the assessment anchors to the documented security gateway-class families; the 8 "unknown" verdicts reflect genuine absence of published evidence, not confirmed absence of capability, and are the items a follow-up with the vendor should prioritize.

---

## Bibliography

[1] Lantech Communications Global, Inc.. "Security Switch (Lantech OS5 Security Switch solution page)". https://lantechcom.webflow.io/solutions/security-switch (Retrieved: 2026-08-11T09:14:42Z)
[2] Lantech Communications Global, Inc.. "Layer 2 / Layer 3 OS5 Switches (product page)". https://lantechcom.webflow.io/products/layer3-os5-switches (Retrieved: 2026-08-11T09:14:45Z)
[3] Lantech Communications Global, Inc.. "About Us (company profile, product lines, certifications)". https://lantechcom.webflow.io/about-us (Retrieved: 2026-08-11T09:14:45Z)
[4] Lantech Communications Global, Inc.. "Lantech OS5 Management Functions - Software Datasheet, Version 2.7 (8 pp.)". https://cdn.prod.website-files.com/698a4b8e853115b2b57d592e/6a041085e6f08617b8bf7eb8_D-OS5_2.7.pdf (Retrieved: 2026-08-11T09:41:51Z)
[5] Lantech Communications Global, Inc.. "Press release: Lantech successfully obtained the IEC 62443-4-2 international certification (March 25, 2026, 4 pp.)". https://www.lantechcom.tw/global/eng/news-events/2026-03-25-Lantech-successfully-obtained-the-IEC-62443-4-2-international-certification%5BEN%5D.pdf (Retrieved: 2026-08-11T09:41:52Z)
[6] Lantech Communications Global, Inc.. "Multifunction Routers (industrial / EN50155 multifunction VPN routers)". https://www.lantechcom.tw/global/eng/software-router.html (Retrieved: 2026-08-11T09:35:02Z)
[7] Lantech Communications Global, Inc.. "T(P)GS-3208GF PoE Managed Ethernet Router Switches - Datasheet Version 1.6 (6 pp.)". https://www.lantechcom.tw/global/eng/download/datasheet/D-T(P)GS-3208GF.pdf (Retrieved: 2026-08-11T09:41:56Z)
[8] Lantech Communications Europe GmbH. "Lantech Professional Firewall Series LFW-1003 - Datasheet Version 1.0 (2 pp.)". https://cdn.pressebox.de/a/9077f571afa62f73/attachments/0598439.attachment/filename/D-LFW-1003.pdf (Retrieved: 2026-08-11T09:41:57Z)
[9] Arcobel B.V.. "Lantech OS5 Achieves IEC 62443-4-2 SL2 Certification (Arcobel partner news)". https://arcobel.com/arcobel_nl/lantech-os5-iec-62443-4-2-industrial-cybersecurity-certification (Retrieved: 2026-08-11T09:37:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 17
- **Sources reviewed:** 9 (kept: 9, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 4, web: 5
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
