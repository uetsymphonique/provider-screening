# BSG / Cross Domain Product Assessment: SVM Technology Limited (DiodeGate) - DiodeGate Security Gateway (DiodeGate-1G / DiodeGate-10G / BitShield-1G / DiodeGate-USB)

**Product ID:** `diodegate-security-gateway`
**Version reference:** Product family: DiodeGate-1G and DiodeGate-10G data diodes, DiodeGate-BitShield 1G inline L2 encryption, DiodeGate-USB; vendor website captured 2026-08-11
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:07:48Z
**Total evidence items collected:** 39
**Total distinct sources:** 11

---

## 1. Overview

DiodeGate is a hardware data diode / unidirectional security gateway product family marketed by SVM Technology Limited, which the vendor's About and Contact pages describe as founded in China with an office in Shenzhen (the provider registry lists European Union as origin, but the vendor's own pages state China) [6, 7]. The family comprises the DiodeGate-1G (up to 1 Gbps) and DiodeGate-10G (up to 10 Gbps) rack data diodes, the BitShield-1G inline Layer-2 AES-256 encryption device, and the DiodeGate-USB read-only USB diode [1, 4, 5]. The vendor positions the products as high-assurance one-way data transfer appliances for confidential networks, aligned with Raise The Bar (RTB) guidelines, supporting one-way, dual one-way (bidirectional via paired diodes), and bi-directional deployments [1]. The 1G/10G devices operate transparently at L2/L3 with hardware allowlist filtering, transmitter-only outgoing optics, hardware ARP/ICMP/syslog, and web/SNMP/LLDP management [2, 3]. Published use cases cover sensor data collection, video streaming, secure system updates, data backup, and event logging [1]. No independent third-party documentation or certification registry entry was located during this pass.

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 4     | 0                | 4      | 0   |
| partial          | 8     | 0                | 8      | 0   |
| not_supported    | 0     | 0                | 0      | 0   |
| unknown          | 12    | 0                | 0      | 12  |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 2 items backed by ≥ 2 source_types; 12 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Supported | medium | - | DiodeGate is marketed as a hardware data diode whose outgoing interface is transmitter-only fiber; reverse data flow is physically restricted, so no response or interaction can return across the boundary. [1], [2], [8], [9] |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Partial | medium | - | Hardware separation is documented via transmit-only optical interfaces and physical blocking of reverse communication; the internal dual-board/FPGA or isolated shared-memory architecture is not described. [2], [3], [8], [9] |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | Operational mode performs hardware allowlist filtering at L2/L3, dropping all packets whose source/destination addresses are not listed (up to 511 rules on the 1G model, 1024 on the 10G). [2], [3] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Partial | medium | - | The vendor states the device runs a trusted operating system that enforces strict separation of roles and processes; no microkernel or SELinux-style hardening details are published. [1] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No documentation of internal data stamping/signing of clean data before new sessions are initiated.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Partial | medium | - | The vendor claims automated inspection with byte-level content sanitization and integrated threat removal, but no per-format CDR engine (Office/PDF/image/CAD reconstruction) is documented. [1] |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No documentation of macro/script (VBA, JavaScript, DDE) removal from files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Unknown | low | - | no evidence found (No multi-engine antivirus scanning of raw payloads documented.) |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No XML/JSON/FIXM/AIXM schema validation documented.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Partial | medium | - | The 10G model handles IPv4 packets carrying mandatory classification labels and is documented as compatible with classification-label protocols; file-level label-based filtering (IFC) is not described. [3] |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Unknown | low | - | no evidence found (No DLP keyword/regex blocking of confidential data documented.) |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No anti-steganography engine for hidden data in images documented.) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Unknown | low | - | no evidence found (No file-transfer protocol proxies (SFTP, FTPS, HTTPS, SMB/NFS) with content cleaning documented.) |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Unknown | low | - | no evidence found (No OT/ICS protocol support (OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT) documented; the devices filter at L2/L3 only.) |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Unknown | low | - | no evidence found (No database protocol proxy (SQL Server, Oracle, PostgreSQL) documented.) |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | The 10G model provides hardware syslog trap and SNMP support on the data plane and video streaming/event logging are listed use cases; no RTSP video proxy or CEF relay is documented. [1], [3] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 9929 Mbps | The DiodeGate-10G datasheet lists tested unidirectional L4 (UDP) throughput of 9929 Mbps at 9216-byte frames (Ixia/Cisco TRex lab), above the 1 Gbps threshold; the 1G model reaches about 998 Mbps L2. [1], [2], [3] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Supported | medium | 0.0001 ms | The DiodeGate-1G datasheet specifies channel latency of no more than 100 ns (0.0001 ms), below the 10 ms threshold; the 10G datasheet states channel delay is not measured. [2], [3] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Partial | medium | n/a (qualitative) | The vendor states high availability with automated failover and seamless unidirectional channel redundancy but publishes no switchover time figure. [1], [3] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Unknown | low | - | no evidence found (No documented fail-close/lockout behavior of the boundary under DoS attack.) |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Partial | medium | - | Management separates an administrative account from a view-only monitoring account and the vendor claims strict role/process separation in the trusted OS; the three-role admin/policy-admin/auditor split is not documented. [1], [3] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Partial | medium | - | The 10G model emits hardware syslog trap messages and supports SNMPv2c, which can feed a SIEM; no TLS-encrypted CEF/Syslog channel to a SIEM is documented. [3] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Unknown | low | - | no evidence found (No compliance report templates (NIST SP 800-82, IEC 62443, ISO 27001) documented.) |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Unknown | low | - | no evidence found (The vendor homepage claims design alignment with Raise The Bar (RTB) guidelines, but no granted certification (Common Criteria, FIPS 140-3, national crypto) is documented; NIST CMVP and Common Criteria portal searches returned no entries for DiodeGate or SVM Technology.) |

---

## 4. Notable Strengths

- **Hardware-enforced unidirectionality (item 1.1):** The outgoing optical interface is transmitter-only and reverse flow is physically restricted, so no response or interaction can return across the boundary [1, 2, 8, 9].
- **Allowlist hardware filtering (item 1.3):** Operational mode drops all packets whose source/destination addresses are not on the configured lists (511 rules on the 1G, 1024 on the 10G) [2, 3].
- **Throughput and latency (items 4.1, 4.2):** The 10G model lists tested unidirectional L4 UDP throughput of 9929 Mbps (Ixia/Cisco TRex lab) and the 1G model publishes channel latency of no more than 100 ns [2, 3].
- **Separation and log export (items 5.1, 5.2):** The 10G separates admin vs view-only monitoring accounts and emits hardware syslog traps with SNMPv2c, giving a basic path for log export toward a SIEM [3].

## 5. Notable Gaps / Risks

- **No certification evidence (item 5.4):** The vendor claims only design alignment with Raise The Bar guidelines; no Common Criteria, FIPS 140-3, or national crypto certification is documented, and NIST CMVP / Common Criteria portal searches returned no entries - a buyer with a certification requirement would need documented certifications before any assurance decision.
- **HA failover time unpublished (item 4.3):** "High availability and automated failover" is claimed without a switchover-time figure, so the ≤ 100 ms requirement cannot be confirmed.
- **No content-inspection depth documented (items 2.1-2.7):** Only generic "byte-level content sanitization" is claimed; no CDR, multi-AV, schema validation, DLP, or anti-steganography detail exists, and the devices filter at L2/L3 only.
- **No application-layer protocol support documented (items 3.1-3.3):** File-transfer, OT/ICS, and database proxies are absent from the documentation; only transparent L2/L3 filtering plus syslog/SNMP is described.
- **Fail-close behavior under DoS undocumented (item 4.4):** No statement describes locking the boundary closed under a denial-of-service attack.

## 6. Evidence Quality Notes

All 24 items rest on vendor-published material only: 11 staged sources (7 product/documentation pages, 4 vendor blog articles), with no independent third-party review, analyst report, or certification registry entry located. General web search engines were blocked or returned only the vendor's own domain for DiodeGate queries; NIST CMVP (basic and advanced) and Common Criteria portal searches for DiodeGate / SVM Technology returned no entries. Confidence is therefore capped at medium for all non-unknown verdicts.

No direct contradictions between sources were found, but two caveats shaped verdicts: the vendor homepage's "Why to choose us" section contains Lorem Ipsum placeholder blocks (excluded from evidence), and the numeric claims come from vendor datasheets tested in a vendor-stated Ixia/Cisco TRex laboratory - 4.1 (9929 Mbps) and 4.2 (100 ns) use those published figures, while 4.3 stays partial because the failover claim is purely qualitative. Items with no documentation at all (1.5, 2.2-2.4, 2.6-2.7, 3.1-3.3, 4.4, 5.3, 5.4) are rated unknown rather than not_supported, per the anti-fabrication contract.

---

## Bibliography

[1] SVM Technology Limited (DiodeGate). "DiodeGate homepage - Reliable Network Data Diode Hardware". https://www.diodegate.com/ (Retrieved: 2026-08-11T09:07:01Z)
[2] SVM Technology Limited (DiodeGate). "DiodeGate-1G - Technical Specifications". https://www.diodegate.com/products/1g (Retrieved: 2026-08-11T09:07:01Z)
[3] SVM Technology Limited (DiodeGate). "DiodeGate-10G - Technical Specifications". https://www.diodegate.com/products/10g (Retrieved: 2026-08-11T09:07:01Z)
[4] SVM Technology Limited (DiodeGate). "DiodeGate-BitShield 1G - Transparent Layer 2 inline encryption". https://www.diodegate.com/products/bit-shield-1g (Retrieved: 2026-08-11T09:07:01Z)
[5] SVM Technology Limited (DiodeGate). "DiodeGate-USB - unidirectional USB data transfer system". https://www.diodegate.com/products/usb (Retrieved: 2026-08-11T09:07:01Z)
[6] SVM Technology Limited (DiodeGate). "About SVM Technology Limited". https://www.diodegate.com/about (Retrieved: 2026-08-11T09:07:01Z)
[7] SVM Technology Limited (DiodeGate). "Contact Us - SVM Technology Limited office details". https://www.diodegate.com/contacts/ (Retrieved: 2026-08-11T09:07:01Z)
[8] SVM Technology Limited (DiodeGate). "Article: What is the Difference Between a Firewall and a Data Diode?". https://www.diodegate.com/articles/what-is-the-difference-between-firewall-and-data-diode/ (Retrieved: 2026-08-11T09:07:01Z)
[9] SVM Technology Limited (DiodeGate). "Article: What is the Difference Between Data Diode and Unidirectional Gateway?". https://www.diodegate.com/articles/data-diode-vs-unidirectional-gateway/ (Retrieved: 2026-08-11T09:07:01Z)
[10] SVM Technology Limited (DiodeGate). "Article: Use Cases Where Data Diodes Can Be Used". https://www.diodegate.com/articles/data-diodes-use-cases/ (Retrieved: 2026-08-11T09:07:01Z)
[11] SVM Technology Limited (DiodeGate). "Article: What Are the Disadvantages of Data Diodes?". https://www.diodegate.com/articles/disadvantages-of-data-diodes/ (Retrieved: 2026-08-11T09:07:01Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 11 (kept: 11, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** vendor_blog: 4, vendor_doc: 7
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
