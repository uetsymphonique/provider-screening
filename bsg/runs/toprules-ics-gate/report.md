# BSG / Cross Domain Product Assessment: TOPSEC Technologies (Beijing Topsec Network Security Technology Co., Ltd. / 天融信) — TopRules / ICS Gate (安全隔离与信息交换系统 TopRules; 工控安全隔离与信息交换系统 TopIGap)

**Product ID:** `toprules-ics-gate`
**Version reference:** TopRules8000 (TR-82166), TopRules6000 (TR-62166), TopRules (NR-31616) per ZOL spec pages; TopIGap industrial gateway per Topsec official WeChat article (2021)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:35:00Z
**Total evidence items collected:** 26
**Total distinct sources:** 7

---

## 1. Overview

TOPSEC (天融信, Beijing Topsec) markets the TopRules family as a security isolation and information exchange system (安全隔离与信息交换系统, a GAP/网闸 product class), with the industrial variant 工控安全隔离与信息交换系统 (TopIGap, 工业网闸) positioned as a production-network boundary protection device for industrial internet enterprises [5]. Both variants share a "2+1" architecture of separate inner and outer proxy hosts connected through self-developed FPGA isolation hardware; the vendor describes physical, protocol and content isolation that severs all direct connections between production and non-production networks and ferries only approved business data [4], [5]. ZOL's product database classifies the TopRules8000/6000/NR-31616 appliances as isolation gateways (隔离网闸) with dedicated inner/outer processing units [1], [2], [3]. The TopIGap variant is documented as deployed in petrochemical, rail transit, tobacco, smart manufacturing, coal, metallurgy, water and municipal sectors, supporting IPv4/IPv6 dual-stack operation [5].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 3     | 2                | 1      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 13    | 0                | 0      | 13  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 5 items backed by ≥ 2 source_types; 1 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 — Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | high | — | Vendor material documents a '2+1' architecture in which all direct connections between production and non-production networks are severed and data is ferried via protocol stripping, landing/restoration on inner/outer proxy hosts with dedicated FPGA isolation hardware; ZOL classifies the hardware as an isolation gateway (隔离网闸). [1], [4], [5] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Supported | high | — | The '2+1' design consists of separate inner and outer proxy hosts (documented as 内端机/外端机 units with their own port sets on ZOL spec pages) connected through self-developed FPGA isolation hardware. [1], [4], [5] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Partial | medium | — | Vendor documents severing all direct connections between production and non-production networks and access-controlled ferrying of business data, consistent with whitelist-only forwarding; an explicit default-deny/whitelist policy statement is not present in the staged sources. [5] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Unknown | low | — | no evidence found (No public documentation of the underlying OS hardening approach (hardened OS, microkernel or SELinux strict mode) in the staged sources.) |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | — | no evidence found (No public documentation of internal data stamping/signing of clean data before new sessions are initiated.) |

### Category 2 — Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | — | no evidence found (No public documentation of content disarm & reconstruction (full dissect/rebuild of DOCX, XLSX, PDF, image, CAD formats).) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | — | no evidence found (No public documentation of macro/script removal (VBA, JavaScript, DDE links, embedded objects).) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | — | Virus scanning (病毒查杀) is documented as part of the gateway's content filtering pipeline, and an expandable anti-virus module is listed in the standard configuration; the number of concurrent antivirus engines scanning raw payloads is not specified. [2], [4] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | — | no evidence found (No public documentation of XML/JSON/FIXM/AIXM schema validation against W3C schemas.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | — | no evidence found (No public documentation of filtering based on security labels attached to files (IFC).) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | — | no evidence found (No public documentation of DLP keyword/regex (classified keywords, ID numbers, account numbers) detection and blocking.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | — | no evidence found (No public documentation of steganography detection or removal in image files (PNG, JPEG, BMP).) |

### Category 3 — Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | — | Standard configuration includes secure-browsing, file-transfer, file-sync, mail, VOIP, database-access and database-sync modules plus active/passive file-exchange and unidirectional TCP/UDP transfer modules; the specific protocols (SFTP, FTP/S, HTTPS, SMB/NFS) are not named in the staged sources. [2], [3] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Partial | medium | — | The TopIGap industrial variant is documented as performing deep parsing of industrial protocols and is deployed at production-network boundaries in petrochemical, rail, tobacco, smart-manufacturing, coal, metallurgy, water and municipal sectors; a specific protocol list (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) is not named in the staged sources. [5], [6] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | — | Database access and database sync modules are part of the standard configuration, including unidirectional database sync; the specific DBMS proxies (SQL Server, Oracle, PostgreSQL) and query whitelisting are not documented in the staged sources. [2], [3] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | — | Video exchange and data sync are documented on the TopIGap, and unidirectional TCP/UDP/mail transfer modules are listed in the TopRules6000 standard configuration; RTSP video proxy and Syslog/CEF relay specifics are not documented. [3], [5] |

### Category 4 — Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1000 Mbps | ZOL spec pages document 1 Gbps throughput for TopRules8000 (TR-82166) and 1000 Mbps for TopRules6000 (TR-62166) in the TopRules isolation-gateway family; a separate throughput figure for the TopIGap industrial variant was not published in the staged sources. [1], [3] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Unknown | low | — | no evidence found (No latency figure documented for packet/protocol processing in the staged sources.) |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | The inner and outer units carry dedicated HA ports (TopRules8000 and TopRules6000 spec pages), indicating high-availability support; no failover switchover time is published, so the <=100ms requirement cannot be verified. [1], [3] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | — | no evidence found (No public documentation of fail-close behaviour under DoS or overload conditions.) |

### Category 5 — Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Unknown | low | — | no evidence found (No public documentation of RBAC with separated system-admin, policy-admin and security-auditor roles.) |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Unknown | low | — | no evidence found (No public documentation of realtime CEF/Syslog log export to SIEM over an encrypted channel.) |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | — | no evidence found (No public documentation of compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001).) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Partial | medium | — | TopRules received IPv6 Ready Logo Phase-2 certification (Logo ID 02-C-002002, 2019) and the TopIGap industrial gateway received IPv6 Ready Logo certification 02-C-002223 as the first industrial gateway in the domestic industrial-internet field, with the Topsec vendor holding multiple current Phase-2 registry entries; no Common Criteria (EAL4+), FIPS 140-3 or national cryptographic certification was evidenced in the staged sources. [4], [5], [6], [7] |

---

## 4. Notable Strengths

- **Protocol-break isolation architecture (items 1.1, 1.2):** vendor and independent sources document a "2+1" design with inner/outer proxy hosts, self-developed FPGA isolation hardware and full severing of direct connections between network zones [1], [4], [5].
- **Throughput at the 1 Gbps level (item 4.1):** ZOL spec pages record 1 Gbps (TopRules8000) and 1000 Mbps (TopRules6000) for the family [1], [3].
- **OT boundary positioning with industrial protocol parsing (item 3.2):** the TopIGap industrial gateway is explicitly sold for production-network boundaries with deep industrial protocol parsing, and is deployed across petrochemical, rail, manufacturing, coal and other OT sectors [5].
- **Breadth of exchange modules (items 3.1, 3.3, 3.4):** the standard configuration includes file transfer/sync, mail, VOIP, database access/sync and unidirectional TCP/UDP transfer modules, with video exchange documented on the industrial variant [2], [3], [5].
- **Protocol-conformance certification (item 5.4):** TopRules holds IPv6 Ready Logo Phase-2 (02-C-002002, 2019) and TopIGap was the first domestic industrial gateway with IPv6 Ready Logo (02-C-002223, 2021), with the vendor carrying multiple current Phase-2 registry entries [4], [5], [7].

## 5. Notable Gaps / Risks

- **Unnamed OT protocol list (item 3.2):** no staged source names OPC UA, Modbus TCP, IEC 60870-5-104, DNP3 or MQTT; only qualitative "deep industrial protocol parsing" is documented, so buyers must confirm protocol coverage with the vendor.
- **No latency figure (item 4.2):** processing latency is entirely undocumented, so the realtime <=10ms requirement is unverifiable.
- **HA without switchover time (item 4.3):** dedicated HA ports exist on inner/outer units, but no failover time is published, so the <=100ms requirement cannot be verified.
- **Shallow content-inspection evidence (items 2.1, 2.2, 2.4-2.7):** only virus scanning and content filtering are documented; CDR, macro removal, schema validation, IFC labels, DLP and anti-steganography are all un-evidenced.
- **Certification scope (item 5.4):** certifications found are IPv6 protocol conformance; no Common Criteria (EAL4+), FIPS 140-3 or national cryptographic certification is evidenced.
- **Un-evidenced management features (items 5.1-5.3):** RBAC role separation, SIEM log export and compliance report templates are not documented in any staged source.

## 6. Evidence Quality Notes

Seven sources were staged and grounded: three ZOL spec pages (TopRules8000, TopRules NR-31616, TopRules6000), an ifeng-syndicated IPv6 Ready release, the Topsec official WeChat article on TopIGap, a Sogou WeChat search results page, and the Global IPv6 Testing Center Ready Logo registry. Items 1.1 and 1.2 are triangulated across three sources and two source types (vendor WeChat + ifeng + ZOL) and carry high confidence; items 2.3, 3.1, 3.3, 3.4, 4.1 and 4.3 are corroborated by two ZOL pages (single source type, so confidence stays medium); item 1.3 rests on a single vendor-blog quote and is capped at medium; the thirteen unknown items have no supporting evidence at all. The main vendor-side claims (protocol break, FPGA isolation, industrial protocol parsing) come from the vendor's own WeChat article, which is why confidence is capped at medium there and why the absence of the vendor's product pages (topsec.com.cn is WAF-blocked from this environment and the Wayback Machine was rate-limited for the whole session) is the biggest evidence-quality limitation. No contradictions between sources were found; ZOL's throughput figures are internally consistent (1 Gbps for the 8000, 1000 Mbps for the 6000).

---

## Bibliography

[1] ZOL中关村在线 (Zhongguancun Online). "天融信TopRules8000 (TR-82166) 产品报价与参数 — ZOL中关村在线 (physical security isolation category)". https://detail.zol.com.cn/physicalsecurity_isolation/index1213570.shtml (Retrieved: 2026-08-11T09:12:33Z)
[2] ZOL中关村在线 (Zhongguancun Online). "天融信TopRules (NR-31616) 产品报价与参数 — ZOL中关村在线 (physical security isolation category)". https://detail.zol.com.cn/physicalsecurity_isolation/index1381232.shtml (Retrieved: 2026-08-11T09:21:00Z)
[3] ZOL中关村在线 (Zhongguancun Online). "天融信TopRules6000 (TR-62166) 产品报价与参数 — ZOL中关村在线 (physical security isolation category)". https://detail.zol.com.cn/physicalsecurity_isolation/index1320657.shtml (Retrieved: 2026-08-11T09:21:00Z)
[4] 凤凰网 (ifeng). "天融信安全隔离与信息交换系统TopRules通过IPv6 Ready Logo认证 (ifeng news syndication of BiiGroup Global IPv6 Testing Center release)". https://ishare.ifeng.com/c/s/7sMnx4hCtz5 (Retrieved: 2026-08-11T09:12:36Z)
[5] 天融信科技集团 (Topsec) official WeChat account. "国内首款 | 天融信工业网闸率先通过IPv6 Ready Logo认证，助力工业互联网IPv6应用发展 (Topsec official WeChat article on TopIGap industrial isolation gateway)". https://mp.weixin.qq.com/s?src=11&timestamp=1786439938&ver=6898&signature=fQZrb3TIYex3AupCNBb630W4qvI1nTm8lG5lxMSKNkO395*1nlaxSnR67lYgieD*X49HM*Eft2WCXLqw*bmYDqJbsgIfawumF9MtzZbYtvo*BwJVNE9ly1O80SR7Iidh&new=1 (Retrieved: 2026-08-11T09:18:00Z)
[6] 搜狗 (Sogou) WeChat search. "搜狗微信搜索: '天融信工业网闸' — WeChat article search results page (aggregates Topsec and third-party WeChat articles)". https://weixin.sogou.com/weixin?type=2&query=%E5%A4%A9%E8%9E%8D%E4%BF%A1%E5%B7%A5%E4%B8%9A%E7%BD%91%E9%97%B8 (Retrieved: 2026-08-11T09:24:00Z)
[7] 全球IPv6测试中心 (Global IPv6 Testing Center / BiiGroup). "全球IPv6测试中心 IPv6 Ready Logo 认证查询 — 厂商 'Topsec' 查询结果 (Global IPv6 Testing Center certification registry, vendor-filtered results)". https://www.ipv6ready.org.cn/index.php/readylogo_search/search (Retrieved: 2026-08-11T09:22:00Z)

---

## Appendix A — Methodology

- **Research mode used:** standard
- **Queries executed:** 18
- **Sources reviewed:** 7 (kept: 7, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, third_party_review: 5, vendor_blog: 1
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B — Machine-readable outputs

Companion files in this run directory:
- `assessment.json` — canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` — inherited from deep-research skill
- `run_manifest.json` — research config and provenance
