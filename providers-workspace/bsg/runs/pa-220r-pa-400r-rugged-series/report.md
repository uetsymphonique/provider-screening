# BSG / Cross Domain Product Assessment: Palo Alto Networks - PA-220R / PA-400R Rugged Series

**Product ID:** `pa-220r-pa-400r-rugged-series`
**Version reference:** PA-220R on PAN-OS 10.0 datasheet (2020); PA-400R Series on PAN-OS 12.1 datasheet (2026); FIPS 140-3 cert #5333 (PAN-OS 10.2) and #5326 (PAN-OS 11.1/11.2); CC VID 11284 (PAN-OS 10.1)
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-11T09:13:48Z
**Total evidence items collected:** 46
**Total distinct sources:** 23

---

## 1. Overview

Palo Alto Networks markets the PA-220R and PA-400R Series as ruggedized, ML-powered next-generation firewalls (NGFWs) that bring next-generation capabilities to industrial applications in harsh environments, such as utility substations, power plants, manufacturing plants, oil and gas facilities, building management systems and healthcare networks [1], [2]. Both families run PAN-OS, the same software that runs all Palo Alto Networks NGFWs, and are positioned for industrial/defense deployments with extended temperature range, fanless passive cooling, DIN-rail/rack/wall mounting, dual DC power and IEC 61850-3 / IEEE 1613 environmental certifications [1], [2]. The PA-400R Series is the current line (PA-410R, PA-450R, PA-455R-5G with optional integrated 5G), rated from 1.4 Gbps to 3.2 Gbps firewall throughput on PAN-OS 12.1, while the older PA-220R is rated 575/540 Mbps on PAN-OS 10.0 [1], [2]. Because the product is a stateful NGFW rather than a protocol-break cross domain guard, the guard/CDS-specific checklist items (1.1, 1.2, 1.5, 2.1, 2.2, 2.4, 2.5, 2.7) are assessed as unknown: the datasheets and reseller listing do not document these capabilities and no specific documented fact excludes them [1], [2], [20].

---

## 2. Verdict Summary

**Counts across 24 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 8     | 1                | 7      | 0   |
| partial          | 7     | 0                | 7      | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 8     | 0                | 0      | 8   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 7 items backed by ≥ 2 source_types; 14 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Architecture & Security

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Kiến trúc Tách biệt Phiên (Protocol Break): Chấm dứt phiên TCP/IP tại phễu ranh giới, ngắt hoàn toàn IP routing. | Unknown | low | - | no evidence found (Product documentation describes the devices as ruggedized ML-powered NGFWs but does not document TCP/IP session-termination (protocol-break) architecture either way.) |
| 1.2 | Cách ly Phần cứng (Hardware Isolation): Thiết kế 2 bo mạch xử lý tách biệt kết nối qua FPGA hoặc Shared Memory cách ly. | Unknown | low | - | no evidence found (Hardware specs document TPM-based secure boot on a single ruggedized appliance, but no documentation describes a dual processing-board design connected via FPGA or isolated shared memory.) |
| 1.3 | Chế độ Default-Deny: Tự động chặn tất cả gói tin/giao thức không nằm trong danh mục White-list. | Supported | medium | - | PAN-OS documentation states the default rules deny all interzone traffic while allowing intrazone traffic, i.e. cross-zone forwarding is whitelist-based, and security policy decisions are made on the application rather than the port. [1], [6] |
| 1.4 | Bảo vệ chống Lỗ hổng OS: Hệ điều hành gia cố siêu cấp (Hardened OS / Microkernel / SELinux Strict Mode). | Supported | medium | - | An independent migration write-up describes PAN-OS as a hardened, closed security-focused operating system; the vendor additionally documents FIPS-CC operational mode, TPM-based secure boot with a hardware root of trust, and PAN-OS Shield management-plane exploit protection. [2], [13], [21], [23] |
| 1.5 | Chữ ký số Nội bộ (Internal Data Stamping): Lõi kiểm soát ký số dữ liệu sạch trước khi cho phép phễu nội khởi tạo phiên mới. | Unknown | low | - | no evidence found (No documentation describes an internal control core that cryptographically stamps clean data before re-initiating sessions.) |

### Category 2 - Inspection & CDR Engine

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Giải phẫu & Tái tạo Nội dung (CDR): Bóc tách và tái tạo 100% các định dạng Office (DOCX, XLSX), PDF, Image, CAD. | Unknown | low | - | no evidence found (No documentation describes content disarm and reconstruction (CDR) of Office, PDF, image or CAD files.) |
| 2.2 | Loại bỏ Macro & Script Độc hại: Xóa bỏ hoàn toàn VBA Macro, Javascript, DDE Links, Embedded Objects trong file. | Unknown | low | - | no evidence found (No documentation describes removal of VBA macros, JavaScript, DDE links or embedded objects from files.) |
| 2.3 | Quét Mã độc Đa nhân (Multi-AV): Tích hợp tối thiểu 2+ Engine Antivirus quét song song payload thô. | Partial | medium | - | Threat Prevention combines antivirus, anti-spyware, IPS and WildFire inline-ML/cloud analysis in a single pass, but the vendor does not document two or more independent antivirus engines scanning raw payload in parallel. [1], [2] |
| 2.4 | Phân tích Cú pháp Schema (Schema Check): Kiểm tra tính hợp lệ của cấu trúc XML, JSON, FIXM, AIXM theo W3C Schema. | Unknown | low | - | no evidence found (No documentation describes schema validation of XML, JSON, FIXM or AIXM structures.) |
| 2.5 | Kiểm soát Luồng Thông tin (IFC): Lọc dữ liệu dựa trên Nhãn An ninh (Security Labels) gắn kèm tập tin. | Unknown | low | - | no evidence found (No documentation describes information-flow control based on security labels attached to files.) |
| 2.6 | Chống Rò rỉ Dữ liệu (DLP): Nhận diện và chặn từ khóa Mật, Mã số CMND, Tài khoản, Regex tùy biến. | Supported | medium | - | Data Filtering profiles with predefined patterns for credit card and social security numbers plus custom regular-expression patterns are documented, and the datasheet describes identification of payload data patterns to thwart data exfiltration. [1], [7] |
| 2.7 | Anti-Steganography Engine: Phát hiện và loại bỏ dữ liệu ẩn giấu bên trong file hình ảnh (PNG, JPEG, BMP). | Unknown | low | - | no evidence found (No documentation describes detection or removal of hidden data in image files (PNG, JPEG, BMP).) |

### Category 3 - Protocol Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ Giao thức File Transfer: SFTP, FTP/S, HTTPS, SMB/NFS Proxy có làm sạch nội dung. | Partial | medium | - | FTP is handled by an application-level gateway and file-transfer applications are identified by App-ID for policy and payload inspection; no SFTP/SMB/NFS content-cleaning proxy in the CDR sense is documented. [1], [14] |
| 3.2 | Hỗ trợ Giao thức OT/ICS: OPC UA, Modbus TCP, IEC 60870-5-104, DNP3, MQTT Industrial Proxy. | Supported | medium | - | App-IDs for Modbus, DNP3, IEC 60870-5-104, OPC UA, MQTT, IEC 61850, EtherNet/IP and Siemens S7 are documented with base- and function-level identifiers, and the OT solution page cites 1070+ OT/ICS App-IDs. [1], [15], [16] |
| 3.3 | Hỗ trợ Giao thức Database: SQL Server, Oracle, PostgreSQL Proxy với khả năng whitelist câu lệnh Query. | Partial | medium | - | Application-level gateway support is documented for MySQL and Oracle/SQLNet/TNS traffic; no SQL-query whitelisting proxy and no SQL Server/PostgreSQL proxy is documented. [14] |
| 3.4 | Hỗ trợ Giao thức Realtime Stream: RTSP Video Proxy, Syslog/CEF Unidirectional/Bidirectional Relay. | Partial | medium | - | An RTSP application-level gateway that opens dynamic pinholes is documented, and firewalls forward logs to external syslog servers; no dedicated unidirectional/bidirectional syslog/CEF relay gateway is documented. [10], [14] |

### Category 4 - Performance & High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Băng thông Xử lý (Throughput): Hỗ trợ băng thông kiểm tra CDR thực tế ≥ 1Gbps (hoặc theo tải dự án). | Supported | medium | 1400 Mbps | The PA-400R Series datasheet lists firewall throughput of 1.4 Gbps (PA-410R) up to 3.2 Gbps (PA-450R/PA-455R-5G), meeting the 1000 Mbps threshold from the entry model upward; the older PA-220R is rated 575/540 Mbps firewall throughput. [1], [2] |
| 4.2 | Độ trễ Xử lý (Processing Latency): Độ trễ xử lý gói tin/giao thức realtime ≤ 10ms. | Partial | medium | n/a (qualitative) | The datasheets describe a single-pass architecture that avoids introducing latency but publish no numeric packet-processing latency in milliseconds, so the 10 ms requirement cannot be confirmed. [1], [2] |
| 4.3 | Khả năng Dự phòng (HA Active-Standby): Tự động chuyển mạch khi sự cố trong thời gian ≤ 100ms không mất session. | Not Supported | medium | 3000 ms | Stateful active/passive and active/active HA with session synchronization is documented, but failover triggers after three consecutive heartbeat losses at a default 1000 ms heartbeat interval, i.e. roughly 3000 ms detection latency, exceeding the 100 ms threshold. [3], [4], [5] |
| 4.4 | Tự vệ khi Quá tải (Fail-Safe State): Tự động khóa ranh giới (Fail-Close) khi phần cứng bị tấn công từ chối dịch vụ DoS. | Partial | medium | - | Zone protection and DoS protection profiles/policy rules that drop flood and reconnaissance traffic are documented, and the firewall can be configured to respond to security violations with maintenance mode; an explicit fail-close boundary lock under overload is not described. [12], [22] |

### Category 5 - Management & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Quản trị Phân quyền (RBAC): Tách biệt vai trò Admin Hệ thống, Admin Policy và Auditor An ninh. | Supported | medium | - | Admin Role profiles grant granular per-functional-area permissions (Enable/Read-Only/Disable) across the Web UI, REST/XML API and CLI, allowing separation of system, policy and audit-type roles. [8] |
| 5.2 | Tích hợp SIEM/SOAR: Đẩy Log thời gian thực dạng CEF/Syslog qua kênh mã hóa TLS tới SIEM. | Supported | medium | - | Log forwarding to external syslog servers over TCP or TLSv1.2 is documented, including CEF-formatted output for ArcSight collection, which satisfies real-time SIEM log push. [9], [10], [11] |
| 5.3 | Báo cáo Tuân thủ (Compliance Report): Có sẵn mẫu báo cáo tuân thủ NIST SP 800-82, IEC 62443, ISO 27001. | Partial | medium | - | The OT solution documents IEC 62443-aligned zoning/segmentation and Strata Cloud Manager claims compliance maintenance with industry and InfoSec standards; ready-made NIST SP 800-82 / IEC 62443 / ISO 27001 report templates are not documented. [2], [16] |
| 5.4 | Chứng nhận Quốc tế / Quốc gia: Đạt chứng nhận Common Criteria (EAL4+), FIPS 140-3 hoặc Chứng nhận Cơ yếu. | Supported | high | - | NIST CMVP lists FIPS 140-3 certificates for PAN-OS 10.2 explicitly including the PA-220R (cert #5333, overall level 2) and for PAN-OS 11.1/11.2 on PA-400 Series hardware (cert #5326); NIAP Common Criteria validation exists for PAN-OS 10.1 NGFWs (VID 11284) under the collaborative Network Device Protection Profile. [13], [17], [18], [19] |

---

## 4. Notable Strengths

- **Industrial protocol coverage (item 3.2):** App-IDs for Modbus, DNP3, IEC 60870-5-104, OPC UA, MQTT, IEC 61850, EtherNet/IP and Siemens S7 are documented with base- and function-level identifiers, and the OT solution cites 1070+ OT/ICS App-IDs [1], [15], [16].
- **Whitelist-based default-deny (item 1.3):** PAN-OS default rules deny all interzone traffic, so cross-zone forwarding is allowed only for traffic matching configured rules [6].
- **Data leakage prevention (item 2.6):** Data Filtering profiles detect credit-card and social-security patterns plus custom regex in transit [7].
- **SIEM integration (item 5.2):** all log types forward to external syslog servers over TCP or TLSv1.2, including CEF-formatted output for ArcSight [9], [10], [11].
- **FIPS 140-3 and Common Criteria certifications (item 5.4):** NIST CMVP lists FIPS 140-3 certificate #5333 explicitly covering the PA-220R (overall level 2), and PAN-OS 10.1 NGFWs hold NIAP Common Criteria validation VID 11284 [17], [18], [19].

## 5. Notable Gaps / Risks

- **HA failover time (item 4.3):** stateful HA is supported, but failover triggers only after three consecutive heartbeat losses at a default 1000 ms interval, roughly 3000 ms detection latency - far above the 100 ms requirement [3], [4], [5].
- **No numeric latency figure (item 4.2):** the single-pass architecture is claimed to avoid introducing latency, but no packet-processing latency in milliseconds is published, so the 10 ms requirement is unconfirmed [1], [2].
- **No multi-vendor AV stacking (item 2.3):** threat prevention bundles antivirus, anti-spyware, IPS and WildFire engines in a single pass, but two or more independent AV engines scanning raw payload in parallel are not documented [1], [2].
- **File-transfer and database proxies limited (items 3.1, 3.3):** FTP and MySQL/Oracle traffic get ALG handling and App-ID policy control, but no SFTP/SMB/NFS content-cleaning proxy and no SQL-query whitelisting exist [14].
- **Entry-level throughput below threshold (item 4.1):** the PA-220R alone is rated 575/540 Mbps firewall throughput and does not meet the 1000 Mbps threshold, though every PA-400R model does [1], [2].
- **Compliance report templates absent (item 5.3):** IEC 62443 alignment is documented for OT segmentation, but ready-made NIST SP 800-82 / IEC 62443 / ISO 27001 report templates are not [2], [16].

## 6. Evidence Quality Notes

The assessment draws on 23 staged sources and 46 grounded evidence entries. Item 5.4 is backed by independent registries (NIST CMVP certificates #5333/#5326 and the NIAP Common Criteria validation report VID 11284) plus vendor docs, giving it the run's only high-confidence verdict [13], [17], [18], [19]. Item 1.4 is triangulated between an independent migration write-up describing PAN-OS as a hardened closed OS and vendor documentation of FIPS-CC mode, TPM secure boot and PAN-OS Shield [2], [13], [21], [23]. The category-establishing evidence for the guard/CDS-specific items (1.1, 1.2, 1.5, 2.1, 2.2, 2.4, 2.5, 2.7), assessed as unknown, combines two vendor datasheets with a third-party reseller listing [1], [2], [20]. The remaining items rest primarily on vendor documentation (datasheets and PAN-OS TechDocs), so their confidence is capped at medium per the project's vendor-only rule; this is the expected posture for a product whose authoritative specification and behavior documentation is vendor-published.

No direct contradictions between sources surfaced. The main judgment calls were: item 4.1 is anchored on the entry PA-400R model (1.4 Gbps) so the ≥1000 Mbps verdict is conservative, with the PA-220R's 575/540 Mbps rating disclosed in the notes rather than conflated; item 4.3 derives a ~3000 ms failover detection time arithmetically from the documented 1000 ms heartbeat interval and three-loss rule, since the vendor does not publish a switchover-time figure; and items 3.1/3.3/3.4 are partial because PAN-OS provides ALG/App-ID handling for FTP, MySQL/Oracle and RTSP but no content-cleaning proxies, query whitelisting or syslog relay gateway.

---

## Bibliography

[1] Palo Alto Networks. "PA-220R Datasheet (PAN-OS 10.0)". https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/pan-os-10-0/pa-220r.pdf (Retrieved: 2026-08-11T09:13:31Z)
[2] Palo Alto Networks. "PA-400R Series Datasheet". https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/pa-400r/pa-400r-series.pdf (Retrieved: 2026-08-11T09:13:31Z)
[3] Palo Alto Networks. "High Availability - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/high-availability (Retrieved: 2026-08-11T09:13:31Z)
[4] Palo Alto Networks. "Failover - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/high-availability/failover (Retrieved: 2026-08-11T09:13:31Z)
[5] Palo Alto Networks. "HA Timers - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/high-availability/ha-timers (Retrieved: 2026-08-11T09:13:31Z)
[6] Palo Alto Networks. "Security Policy - PAN-OS 10.1 Administrator's Guide". https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/policy/security-policy (Retrieved: 2026-08-11T09:13:31Z)
[7] Palo Alto Networks. "Set Up Data Filtering - PAN-OS 10.1 Administrator's Guide". https://docs.paloaltonetworks.com/pan-os/10-1/pan-os-admin/policy/security-profiles/set-up-data-filtering (Retrieved: 2026-08-11T09:13:31Z)
[8] Palo Alto Networks. "Configure an Admin Role Profile - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/firewall-administration/manage-firewall-administrators/configure-an-admin-role-profile (Retrieved: 2026-08-11T09:13:31Z)
[9] Palo Alto Networks. "Configure Log Forwarding - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/monitoring/configure-log-forwarding (Retrieved: 2026-08-11T09:13:31Z)
[10] Palo Alto Networks. "Use Syslog for Monitoring - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/monitoring/use-syslog-for-monitoring (Retrieved: 2026-08-11T09:13:31Z)
[11] Palo Alto Networks. "Common Event Format (CEF) Configuration Guides - TechDocs". https://docs.paloaltonetworks.com/resources/cef (Retrieved: 2026-08-11T09:13:31Z)
[12] Palo Alto Networks. "Zone Protection and DoS Protection - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/zone-protection-and-dos-protection (Retrieved: 2026-08-11T09:13:31Z)
[13] Palo Alto Networks. "Certifications (FIPS-CC mode) - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/certifications (Retrieved: 2026-08-11T09:13:31Z)
[14] Palo Alto Networks. "Application Level Gateways - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/app-id/application-level-gateways (Retrieved: 2026-08-11T09:13:31Z)
[15] Palo Alto Networks. "App-IDs for ICS and SCADA - Support for Industrial Control Systems Protocols and Applications (datasheet)". https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/white-papers/app-ids-for-ics-scada.pdf (Retrieved: 2026-08-11T09:13:31Z)
[16] Palo Alto Networks. "OT Security Solution - Proactive Protection for Industrial Operations". https://www.paloaltonetworks.com/network-security/ot-security-solution (Retrieved: 2026-08-11T09:13:31Z)
[17] NIST Cryptographic Module Validation Program. "NIST CMVP Certificate #5333 - PAN-OS 10.2 running on PA-220, PA-220R, PA-400 Series ... NGFWs". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5333 (Retrieved: 2026-08-11T09:13:31Z)
[18] NIST Cryptographic Module Validation Program. "NIST CMVP Certificate #5326 - PAN-OS 11.1/11.2 running on PA-400 Series ... NGFWs". https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/5326 (Retrieved: 2026-08-11T09:13:31Z)
[19] National Information Assurance Partnership. "NIAP Common Criteria Validation Report VID 11284 - Palo Alto Networks NGFW with PAN-OS 10.1 (CCEVS-VR-VID11284-2022)". https://www.commoncriteriaportal.org/files/epfiles/st_vid11284-vr.pdf (Retrieved: 2026-08-11T09:13:31Z)
[20] Network Devices Inc.. "Palo Alto PA-400R Series Firewalls - reseller product listing". https://networkdevicesinc.com/collections/palo-alto-pa-400r-series-firewalls (Retrieved: 2026-08-11T09:13:31Z)
[21] Medium. "Migrating Palo Alto VM-Series Firewalls from Unmanaged to Managed Disks in Azure". https://medium.com/@JoshuaMichealM1/migrating-palo-alto-vm-series-firewalls-from-unmanaged-to-managed-disks-in-azure-277ed838b191 (Retrieved: 2026-08-11T09:13:31Z)
[22] Palo Alto Networks. "Configure Device Security - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/security-settings/configure-device-security (Retrieved: 2026-08-11T09:13:31Z)
[23] Palo Alto Networks. "Enable PAN-OS Shield - Next-Generation Firewall documentation". https://docs.paloaltonetworks.com/ngfw/administration/security-settings/panos-shield (Retrieved: 2026-08-11T09:13:31Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 14
- **Sources reviewed:** 23 (kept: 23, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** documentation: 18, web: 5
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
