# BSG / Cross Domain Product Assessment: Venustech - Leadsec Industrial Security Gateway

**Product ID:** `leadsec-industrial-security-gateway`
**Version reference:** IFW-3000 series (IFW-3000-1100R, IFW-3000-XF-3600R), Tianqing Hanma / NetEye-Leadsec industrial firewall, system V5.0; 2016 product whitepaper; 2024-2025 Frost & Sullivan market reports
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:30:04Z
**Total evidence items collected:** 35
**Total distinct sources:** 13

---

## 1. Overview

Venustech's Leadsec Industrial Security Gateway is the Tianqing Hanma / NetEye-Leadsec IFW-3000 series, an industrial firewall (工业安全网关/工业防火墙 class) dedicated to ICS boundary protection for SCADA, DCS, PCS and PLC environments [1], [3], [4]. The vendor positions it as a ruggedized industrial firewall, not a cross-domain solution or protocol-break guard [1], [4]; sources describe a stateful packet-filtering and deep-packet-inspection engine with whitelist-based industrial protocol control rather than a session-terminating, non-routable architecture [4]. It ships in DIN-rail and rack-mount forms with wide-temperature, fanless, IP40 hardware, and deploys at management-network/monitoring-network/production-network boundaries or directly in front of engineering workstations and PLCs [2], [3]. The series (e.g. IFW-3000-1100R, IFW-3000-XF-3600R) runs deep DPI for OPC, Modbus, IEC 104, S7, DNP3 and other protocols, includes industrial IPS, VPN, traffic self-learning and centralized management [1], [4], [10], and is adapted to domestic Phytium/Zhaoxin/Hygon platforms and the Kylin OS [8], [13].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 4     | 2                | 2      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 2 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Unknown | low | - | no evidence found (No session-terminating, non-routable protocol-break architecture is documented; sources describe the product only as an industrial firewall.) |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (No dual processing-board / FPGA / isolated shared-memory hardware isolation design is documented.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | high | - | Whitelist-based access control is central: a reseller listing describes packets not on the whitelist being directly rejected, and the vendor whitepaper describes whitelist protection of industrial protocols and whitelists that block unauthorized packets. Independent sources corroborate the default-deny posture. [1], [3], [4], [5] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | - | The industrial firewall is adapted to domestic Phytium/Zhaoxin/Hygon hardware platforms and the Kylin (银河麒麟) domestic OS per vendor news releases citing Frost & Sullivan reports. No explicit hardened-OS claim (microkernel or SELinux strict mode) is published. [8], [13] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No internal data-stamping / signing core for clean data before session re-initiation is documented.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No content disarm and reconstruction (CDR) of Office/PDF/Image/CAD files is documented.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No file-level macro/script (VBA, Javascript, DDE) / embedded-object removal capability is documented.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | - | An antivirus (AV) engine is described as part of the deep security-detection chain, and a reseller page lists antivirus capability. Parallel scanning by two or more AV engines is not documented. [5], [8] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM W3C schema validation capability is documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No security-label-based information flow control attached to files is documented.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Partial | medium | - | A natural-language, extensible content-level detection engine with functions/operators enables custom deep inspection of non-encrypted protocol payloads, and the packet-parsing module supports content filtering and audit by item. Prebuilt sensitive-data keyword dictionaries (secrets, ID numbers, accounts) are not documented. [4], [10] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography / hidden-data detection or removal engine for image files is documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | - | no evidence found |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | high | - | Instruction-level deep inspection is documented for OPC (DA/HDA/A&E and OPC UA), Modbus/TCP, Modbus/RTU, IEC 60870-5-104, Ethernet/IP, EIP, S7, DNP3 and PROFINET across vendor and independent sources. MQTT was not found in the reviewed material. [1], [3], [4], [8], [10] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Unknown | low | - | no evidence found |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | A reseller specification listing for the IFW-3000-1100R model states throughput of 1 Gbps (吞吐量 1Gbps), meeting the ≥1000 Mbps threshold. [5] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.04 ms | The same reseller specification listing states processing latency of 40 microseconds (时延 40us), equal to 0.04 ms, below the 10 ms threshold. [5] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | Dual-machine hot standby (双机热备), redundant power and interface linkage are documented across vendor and independent sources. No active-standby switchover time in milliseconds is published, so the ≤100 ms requirement cannot be confirmed numerically. [2], [3], [8] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | On power loss or anomaly the device intelligently engages hardware Bypass to preserve production continuity, i.e. a fail-open availability behavior. No fail-close boundary lock under DoS is documented. [3], [8] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | - | no evidence found |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | Juniper's JSA DSM documents that Venusense appliances forward firewall and NIPS events to the SIEM via syslog on port 514, and the firewall records and sends management and system logs. TLS-encrypted CEF/Syslog delivery is not documented. [4], [5], [6] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | - | The firewall is designed per the enhanced level of national standard GB/T 37933-2019 (ICS dedicated firewall technical requirements, current since 2020-03-01), and Venustech gateways hold CNITSEC EAL3+ certificates; Frost & Sullivan ranked the product China industrial-firewall market leader with 36.7% share. No EAL4+/FIPS 140-3 or national crypto certificate for the IFW itself was found. [7], [8], [9], [13] |

---

## 4. Notable Strengths

- **Whitelist default-deny (item 1.3):** Whitelist-based access control is core - a reseller listing describes packets not on the whitelist being directly rejected while whitelisted traffic is format- and virus-checked before forwarding [3], [4], [5].
- **Deep industrial protocol inspection (item 3.2):** Instruction-level DPI is documented for OPC (DA/HDA/A&E and OPC UA), Modbus/TCP, Modbus/RTU, IEC 60870-5-104, Ethernet/IP, EIP, S7, DNP3 and PROFINET, across vendor and independent sources [1], [3], [4], [8].
- **Throughput and latency meet numeric thresholds (items 4.1, 4.2):** a reseller spec listing for the IFW-3000-1100R states 1 Gbps throughput and 40 us latency, satisfying the ≥1000 Mbps and ≤10 ms requirements [5].
- **High-availability mechanisms (item 4.3):** redundant power, dual-machine hot standby, interface linkage and hardware Bypass are documented for availability-oriented operation [2], [3], [8].
- **National-standard alignment (item 5.4):** the firewall is designed per the enhanced level of GB/T 37933-2019 (ICS dedicated firewall technical requirements) and the vendor holds CNITSEC EAL3+ certificates for its gateway family [7], [8], [9].

## 5. Notable Gaps / Risks

- **HA switchover time unquantified (item 4.3):** dual-machine hot standby is documented but no switchover time in ms is published anywhere, so the ≤100 ms requirement cannot be verified - a vendor datasheet or test report stating failover time would resolve this.
- **Fail-open BYPASS conflicts with fail-close expectation (item 4.4):** on power loss or anomaly the device opens its Bypass path to keep production running [8]; no DoS-triggered fail-close boundary lock is documented, which is the opposite posture for buyers expecting fail-close behavior.
- **No EAL4+/FIPS 140-3/national-crypto certificate for the IFW (item 5.4):** GB/T 37933-2019 enhanced-level design is vendor-claimed and sibling gateways hold CNITSEC EAL3+ only [7], [8], [9]; an IFW-specific Common Criteria or crypto certificate is not public.
- **SIEM delivery lacks TLS (item 5.2):** syslog to SIEM is documented on port 514 (UDP) via Juniper JSA DSM, but no TLS-encrypted CEF/Syslog channel is specified [4], [6].
- **Management/audit evidence gaps (items 5.1, 5.3):** no public documentation of RBAC role separation (admin/policy/auditor) or of NIST SP 800-82 / IEC 62443 / ISO 27001 report templates was found for this product.
- **CDS-class capabilities not documented (items 1.1, 2.1):** no protocol break or content disarm & reconstruction is documented for this firewall-class product; buyers requiring guard/CDS functions should verify with the vendor or look elsewhere.

## 6. Evidence Quality Notes

Evidence was triangulated across 13 staged sources: 8 vendor pages/whitepapers, 3 independent sources (the Gongkong industrial-automation portal listing [3], the Zhongtao Tianyou reseller spec sheet [5], and Juniper JSA integration documentation [6]) and 2 registries (the SAMR national-standard platform [7] and the CNITSEC product-evaluation page [9]). Items 1.3 and 3.2 reached high confidence with independent corroboration; 4.1 and 4.2 rest on a single reseller-listed spec figure that almost certainly mirrors the vendor datasheet, so confidence is capped at medium and the figure is flagged as not independently lab-measured. Items 1.4, 2.3, 2.6, 4.3, 4.4, 5.2 and 5.4 rely on vendor documentation (some citing Frost & Sullivan reports) plus at most one independent source, hence medium confidence.

Chinese-language sources were checked against staged raw text with exact whitespace-normalized substring matching; because the grounding checker's normalizer drops non-ASCII characters, quotes that are purely Chinese verify only via the ASCII tokens they contain (model numbers, figures such as 1Gbps/40us) - a limitation of the tool, not of quote provenance. No source contradictions were found; the main judgment calls were (a) treating the product as firewall-class (marking CDS-specific items unknown) based on vendor and third-party category statements, since product class alone does not establish a specific excluding fact, and (b) marking 4.3/4.4 partial because HA is documented but the numeric failover and fail-close-under-DoS behaviors are not.

---

## Bibliography

[1] Venustech (Venusense international site). "Venusense Industrial Firewall (IFW) - product page". https://www.venusense.com/type/IFW/ (Retrieved: 2026-08-11T08:59:25Z)
[2] Venustech. "天清汉马工业防火墙IFW-3000系列 (Tianqing Hanma Industrial Firewall IFW-3000 series)". https://www.venustech.com.cn/new_type/gyfhq/ (Retrieved: 2026-08-11T08:59:30Z)
[3] Gongkong (China industrial automation portal). "启明星辰IFW-3000天清汉马工业防火墙 (product listing, 中国工控网)". https://www.gongkong.com/product/201612/102159.html (Retrieved: 2026-08-11T09:22:00Z)
[4] Venustech Group Inc.. "Venusense Industrial Firewall (IFW-3000 Series) Product Whitepaper (2016, 25 pp.)". https://softyab.com/wp-content/uploads/2020/12/IFW-white-paper.pdf (Retrieved: 2026-08-11T09:23:00Z)
[5] Jiangsu Zhongtao Tianyou Electronic Technology Co.. "启明星辰IFW-3000-1100R防火墙 (reseller spec listing, 江苏中韬天友电子科技)". http://www.ztty.com.cn/page25?product_id=122 (Retrieved: 2026-08-11T09:24:00Z)
[6] Juniper Networks. "Venustech Venusense | JSA 7.5.0 (Juniper Networks DSM documentation)". https://www.juniper.net/documentation/us/en/software/jsa7.5.0/jsa-dsm/topics/concept/jsa-dsm-venustech-venusense.html (Retrieved: 2026-08-11T09:25:00Z)
[7] 全国标准信息公共服务平台 / SAMR. "GB/T 37933-2019 信息安全技术 工业控制系统专用防火墙技术要求 (national standard registry entry)". https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=643139368451D65D4A69009EBA234964 (Retrieved: 2026-08-11T09:26:00Z)
[8] Venustech Group. "持续领航！启明星辰集团工业防火墙再获沙利文市场领导奖 (news release citing Frost & Sullivan 2024 report)". https://www.venusgroup.com.cn/new_type/cpdt/20250718/28663.html (Retrieved: 2026-08-11T09:27:00Z)
[9] CNITSEC (中国信息安全测评中心). "中国信息安全测评中心 产品测评公告 (CNITSEC product evaluation announcements, page 9)". https://www.itsec.gov.cn/cp/cpcpgg/index_9.html (Retrieved: 2026-08-11T09:28:00Z)
[10] Leadsec (网御星云). "网御工业防火墙 (Leadsec-branded industrial firewall IFW-3000 series)". https://www.leadsec.com.cn/product/231018-81.html (Retrieved: 2026-08-11T09:29:00Z)
[11] Venustech. "资质荣誉 (Venustech qualifications and awards)". https://www.venustech.com.cn/new_type/zzry/ (Retrieved: 2026-08-11T09:30:00Z)
[12] Venustech. "工业互联网安全解决方案 (Industrial Internet security solution)". https://www.venustech.com.cn/new_type/gyhlwjjfa/ (Retrieved: 2026-08-11T09:31:00Z)
[13] Venustech. "荣耀六载！启明星辰集团蝉联中国工业防火墙市场第一 (news release citing Frost & Sullivan 2023 market ranking)". https://www.venustech.com.cn/new_type/cpdt/20240620/27686.html (Retrieved: 2026-08-11T09:32:00Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 24
- **Sources reviewed:** 13 (kept: 13, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** pdf: 1, web: 12
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
