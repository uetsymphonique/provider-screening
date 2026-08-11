# BSG / Cross Domain Product Assessment: Radiflow — iSEG Industrial Security Gateway

**Product ID:** `iseg-industrial-security-gateway`
**Version reference:** iSEG RF-1031 (2021 datasheet) / iSEG RF-3180 (April 2022 datasheet)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T10:30:00Z
**Total evidence items collected:** 34
**Total distinct sources:** 13

---

## 1. Overview

Radiflow's iSEG is a family of ruggedized industrial secure gateways — currently marketed as the RF-1031 for small remote sites and the RF-3180 for remote sites and substations — that combine a whitelist-based, distributed deep-packet-inspection (DPI) firewall for SCADA protocols (Modbus TCP, IEC 101/104, DNP3, S7) with IPsec VPN over landline and cellular links and an Authentication Proxy Access (APA) for user-identity-based remote access [1, 2, 3, 4]. The vendor positions the family as an OT security gateway for M2M and H2M traffic at field locations, not as a cross-domain guard or protocol-break solution: the devices route L3 traffic (static routing, OSPF, RIPv2, VRRP), perform NAT, and enforce firewall rules at every port rather than terminating and re-originating sessions [1, 3, 4, 8]. An ARC Advisory Group review likewise describes iSEG secure gateways as providing "local protection and access management for remote substations and other industrial sites" [10]. Typical deployment shapes are DIN-rail gateways at substations, storage tanks and other harsh-environment sites, managed centrally with the iSIM tool and integrated into Radiflow's iSID/CIARA monitoring and risk-management platform [3, 5, 9].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 1     | 0                | 1      | 0   |
| partial          | 11    | 0                | 8      | 3   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 5     | 0                | 0      | 5   |
| not_applicable   | 7     | 0                | 7      | 0   |

**Evidence quality:** 6 items backed by ≥ 2 source_types; 17 items backed by vendor_doc only (confidence capped at medium per validator rule).

**Not-applicable items:**
- **1.1:** Vendor datasheets, the vendor blog and an ARC Advisory Group review position iSEG as a DPI SCADA firewall and ruggedized gateway with L3 routing (OSPF, RIPv2, VRRP) and NAT, not a protocol-break guard that terminates and re-originates TCP/IP sessions.
- **1.2:** The datasheet describes a single ruggedized DIN-rail appliance (IP30, fanless, 1.4 kg), an industrial gateway form factor with no dual processing-board / FPGA-isolated architecture, consistent with its firewall category.
- **1.5:** The product category is an in-line DPI firewall/gateway; the vendor does not describe a guard-style internal signing funnel that stamps data before re-initiating sessions.
- **2.1:** iSEG validates SCADA protocol packets (source, destination, protocol, content) rather than files, and no content disarm and reconstruction of Office/PDF/image documents is offered, consistent with its firewall category.
- **2.4:** The policy engine operates on SCADA protocol fields through profile-based rules rather than XML/JSON/FIXM/AIXM schema validation; the product is a firewall, not a message-schema gateway.
- **2.5:** Filtering is whitelist/policy-based at the packet level; security-label-based information flow control attached to files is not part of the DPI firewall design.
- **2.7:** iSEG inspects protocol packets, not image files, and no anti-steganography file sanitization capability is described, consistent with the firewall category.

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | N/A | medium | — | Vendor datasheets, the vendor blog and an ARC Advisory Group review position iSEG as a DPI SCADA firewall and ruggedized gateway with L3 routing (OSPF, RIPv2, VRRP) and NAT, not a protocol-break guard that terminates and re-originates TCP/IP sessions. [4], [8], [10] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | N/A | medium | — | The datasheet describes a single ruggedized DIN-rail appliance (IP30, fanless, 1.4 kg), an industrial gateway form factor with no dual processing-board / FPGA-isolated architecture, consistent with its firewall category. [4] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | — | Both iSEG datasheets describe a whitelist-based distributed DPI firewall installed at every port that validates each SCADA packet and forwards only what its rules allow, with Monitoring and Enforcement modes for non-whitelisted traffic. [2], [4], [8] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | low | — | The datasheet documents OS image encryption and a Safe Mode for the gateway software, but no microkernel or SELinux-style hardening claims are made. [4] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | N/A | medium | — | The product category is an in-line DPI firewall/gateway; the vendor does not describe a guard-style internal signing funnel that stamps data before re-initiating sessions. [4] |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | N/A | medium | — | iSEG validates SCADA protocol packets (source, destination, protocol, content) rather than files, and no content disarm and reconstruction of Office/PDF/image documents is offered, consistent with its firewall category. [4] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No evidence found on macro/script (VBA, Javascript, DDE) removal.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | — | no evidence found (No evidence of multi-engine antivirus scanning in iSEG.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | N/A | medium | — | The policy engine operates on SCADA protocol fields through profile-based rules rather than XML/JSON/FIXM/AIXM schema validation; the product is a firewall, not a message-schema gateway. [4] |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | N/A | medium | — | Filtering is whitelist/policy-based at the packet level; security-label-based information flow control attached to files is not part of the DPI firewall design. [3] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No evidence of DLP (keyword/pattern blocking) functionality.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | N/A | medium | — | iSEG inspects protocol packets, not image files, and no anti-steganography file sanitization capability is described, consistent with the firewall category. [4] |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | low | — | The datasheet lists TFTP/SFTP client capability for management transfers (config/OS), but no FTP/S, HTTPS, SMB/NFS file-transfer proxy with content cleaning is documented. [2] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | DPI firewalling is documented for Modbus TCP, IEC 60870-5-104, DNP3 and Siemens S7 (plus IEC 101 serial gateway) and confirmed in a field deployment case study; OPC UA and MQTT are not mentioned in the staged datasheets. [2], [4], [8], [9] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | — | no evidence found (No evidence of SQL Server/Oracle/PostgreSQL proxy with query whitelisting.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | low | — | Syslog export is listed in the gateway's management feature set, but no RTSP video proxy or CEF-format relay is documented. [4] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Partial | medium | n/a (qualitative) | The datasheet states line-rate L2/L3 switching throughput but publishes no quantified firewall/DPI inspection throughput in Mbps, so the >=1000 Mbps requirement cannot be confirmed. [4] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | A switching latency below 10 microseconds is documented for the L2/L3 fabric, but DPI/security processing latency for realtime protocols is not separately quantified. [4] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | VRRP redundancy is documented for the RF-3180 and iSIM supports configuration backup for failover gateways, but no switchover time in milliseconds is published. [3], [4] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | — | The gateway automatically blocks abnormal activity and isolates affected sub-networks upon anomaly detection and includes a failsafe output relay for critical alarms; an explicit fail-close boundary lock under DoS overload is not described. [4] |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | — | User authorization levels (iSIM) and user/task-based access control via Authentication Proxy Access are documented; explicit separation of system-admin, policy-admin and auditor roles is not evidenced. [2], [5], [8] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | — | Syslog and SNMPv1/v2c/v3 export are documented on the gateway and the Radiflow suite makes its enriched data available to external SIEMs; CEF format and TLS-encrypted syslog transport are not confirmed. [4], [6] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | — | iSEG is positioned as a NERC CIP v6 enabler via its Authentication Proxy Access, and the Radiflow platform (CIARA) produces IEC 62443-aligned hardening plans and compliance reports; iSEG-native report templates for NIST SP 800-82 or ISO 27001 are not documented. [4], [7] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | — | no evidence found (No Common Criteria / FIPS 140-3 / national crypto certification found; the RF-3180 datasheet instead documents IEC 61850-3, IEEE 1613, EN 50121-4 and IEC 61000-4 utility/EMC conformance.) |

---

## 4. Notable Strengths

- **Whitelist-based default-deny firewall (item 1.3):** Both iSEG datasheets describe a whitelist-based distributed DPI firewall installed at every port for serial and Ethernet traffic, with Monitoring and Enforcement modes — non-whitelisted traffic is not forwarded [2, 4].
- **Deep protocol inspection for major SCADA protocols (item 3.2):** DPI firewalling is documented for Modbus TCP, IEC 60870-5-104, DNP3 and Siemens S7, and a petroleum-storage field deployment confirms iSEG 3180 gateways inspecting SCADA traffic at each tank [2, 4, 9].
- **Remote-access control with NERC CIP framing (items 5.1, 5.3):** The built-in APA grants authenticated users time-and-device-scoped access with full logging, and the gateway is positioned as a NERC CIP v6 enabler [2, 4, 8].
- **Ruggedized field deployment and utility standards conformance (item 4.4, 5.4 context):** The RF-3180 operates at -40C to 75C, is DIN-rail mountable and carries IEC 61850-3, IEEE 1613, EN 50121-4 and IEC 61000-4 conformance, with automatic blocking and isolation of anomalous activity [4].
- **Management ecosystem (items 5.1, 5.2):** iSIM provides central management with user-authorization levels, and the Radiflow suite feeds enriched operational data to external SIEMs [5, 6].

## 5. Notable Gaps / Risks

- **No quantified throughput or latency figures (items 4.1, 4.2):** The RF-3180 datasheet states line-rate L2/L3 switching throughput and sub-10-microsecond switching latency but publishes no firewall/DPI inspection throughput in Mbps or protocol processing latency, so the >=1000 Mbps and <=10 ms requirements cannot be verified from public documentation [4].
- **HA switchover time not specified (item 4.3):** VRRP redundancy is documented, but no failover/switchover time is published, leaving the <=100 ms requirement unverifiable [3, 4].
- **OPC UA and MQTT not evidenced (item 3.2):** DPI coverage is limited to Modbus TCP, IEC 101/104, DNP3 and S7; organizations standardizing on OPC UA or MQTT at the gateway would need vendor confirmation [2, 4].
- **No Common Criteria / FIPS / national crypto certification (item 5.4):** No evidence of CC EAL4+, FIPS 140-3 or a national cryptographic certification was found; the datasheets document utility/EMC conformance (IEC 61850-3, IEEE 1613) instead [4].
- **CDR-class capabilities absent by design (items 2.1, 2.2, 2.3, 2.6):** As a protocol DPI firewall the product offers no file content disarm/reconstruction, macro removal, multi-AV scanning or DLP — buyers needing file sanitization must pair it with a separate guard/CDR product [4].

## 6. Evidence Quality Notes

Thirteen distinct sources were cited across 34 evidence entries. Only one item (3.2, protocol support) is triangulated across four sources (two datasheets, a vendor blog and a field case study); most other non-unknown items rest on one or two vendor datasheets. Six items are backed by >= 2 source_types, and no item achieved "high" confidence — the evidence base is dominated by vendor documentation (4 datasheets, 4 product pages, 2 vendor blogs). The only non-vendor sources are a vendor-hosted ARC Advisory Group review summary [10], a vendor case study [9], and third-party press quoting Radiflow's CEO [12]; none of these independently tests the gateway's performance or security claims, which is why numeric-threshold and performance items stayed at "partial" rather than being upgraded.

No direct contradictions between sources were found; the datasheets (2021 RF-1031, April 2022 RF-3180) are consistent with the current family page and blog. The main evidence-quality limitation is age and scope: the published datasheets predate the current product line, legacy model datasheets (RF-1074/1120/1180) are no longer on the vendor site and could not be retrieved from archives during this run, and the vendor site was partially protected by bot filters, so some pages (e.g. the original ARC article) were only reachable via vendor-hosted summaries.

---

## Bibliography

[1] Unknown. "iSEG RF-1031 Secure Gateway - product page". https://radiflow.com/products/iseg/ (Retrieved: 2026-08-11T10:00:00Z)
[2] Unknown. "iSEG RF-1031 Secure Gateway - Product Datasheet". https://www.radiflow.com/wp-content/uploads/iSEG-RF-1031-new-data-sheet.pdf (Retrieved: 2026-08-11T10:00:00Z)
[3] Unknown. "Secure Gateways - family page (iSEG RF-3180, RF-1031, iSIM)". https://www.radiflow.com/products/secure-gateways/ (Retrieved: 2026-08-11T10:00:00Z)
[4] Unknown. "iSEG RF-3180 Secure Gateway - Product Datasheet". https://www.radiflow.com/wp-content/uploads/RF-DS-iSEG-3180-APR22.pdf (Retrieved: 2026-08-11T10:00:00Z)
[5] Unknown. "iSIM Industrial Service Management Tool - Datasheet". https://www.radiflow.com/wp-content/uploads/iSIM-2022.pdf (Retrieved: 2026-08-11T10:00:00Z)
[6] Unknown. "iSID Industrial Threat Detection System - Brochure". https://www.radiflow.com/wp-content/uploads/iSID-Brochure-WEB.pdf (Retrieved: 2026-08-11T10:00:00Z)
[7] Unknown. "CIARA OT Risk Management platform - product page". https://www.radiflow.com/products/ot-risk-managment/ (Retrieved: 2026-08-11T10:00:00Z)
[8] Unknown. "Securing Remote Access in OT Enterprises - Radiflow blog". https://www.radiflow.com/blog/securing-remote-access-in-ot-enterprises/ (Retrieved: 2026-08-11T10:00:00Z)
[9] Unknown. "Case study: Securing Petroleum Storage Tanks in Southeast Asia". https://www.radiflow.com/case-studies/securing-petroleum-storage-tanks-in-southeast-asia/ (Retrieved: 2026-08-11T10:00:00Z)
[10] Unknown. "ARC Advisory Group review of Radiflow solutions (vendor-hosted summary)". https://www.radiflow.com/news/arc-advisory-group-reviews-radiflows-solutions-concludes-that-radiflow-can-help-companies-close-ot-security-gaps/ (Retrieved: 2026-08-11T10:00:00Z)
[11] Unknown. "Cyberthreats Built Right into Your OT Environment - guest article by Radiflow CEO on Automation.com". https://www.automation.com/en-us/articles/july-2024/cyberthreats-built-ot-environment (Retrieved: 2026-08-11T10:00:00Z)
[12] Unknown. "Is critical infrastructure prepared for OT ransomware? - The Register". https://www.theregister.com/2024/02/02/critical_infrastructure_ot_ransomware/ (Retrieved: 2026-08-11T10:00:00Z)
[13] Unknown. "iSID Visibility and Anomaly Detection - product page". https://www.radiflow.com/products/ot-visibility-and-anomaly-detection/ (Retrieved: 2026-08-11T10:00:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** Radiflow iSEG product pages and datasheets (RF-1031, RF-3180, iSIM, iSID, CIARA); Radiflow blog: remote access / iSEG DPI firewall positioning; Case study: iSEG 3180 petroleum storage tanks SE Asia; ARC Advisory Group review (vendor-hosted summary); Third-party press: The Register OT ransomware; Automation.com guest article; Registry checks: Common Criteria portal, ISASecure, NIST CMVP (no Radiflow entries found); Wayback Machine CDX queries for legacy iSEG datasheets (rate-limited, not retrieved)
- **Sources reviewed:** 13 (kept: 13, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** analyst_report: 1, case_study: 1, third_party_review: 1, vendor_blog: 2, vendor_datasheet: 4, vendor_doc: 4
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
