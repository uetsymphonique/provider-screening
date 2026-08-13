# Microsegmentation Product Assessment: Zscaler - Zscaler Zero Trust Exchange

**Product ID:** `zscaler-zero-trust-exchange`
**Version reference:** n/a
**Assessment mode:** standard
**Checklist version:** 1
**Assessed at:** 2026-08-10T21:30:00Z
**Total evidence items collected:** 98
**Total distinct sources:** 45

---

## 1. Overview

Zscaler Zero Trust Exchange (ZTE) is a cloud-native SASE/SSE platform that delivers security and connectivity from more than 160 globally distributed data centers rather than on-premises appliances [2, 13]. Its microsegmentation capabilities span three components: ZPA (Zscaler Private Access), which brokers one-to-one user-to-app and app-to-app connections without placing users or workloads on the network [3, 12]; Zscaler Microsegmentation, a host-based workload segmentation product (built on the Edgewise acquisition) that enforces process-level, identity-based policy in public clouds and data centers [1, 9, 33]; and agentless OT/IoT Segmentation, which isolates devices into segments of one using /32 host isolation [4]. Policy is built on user-defined tags, cloud attributes, and identity rather than IP/VLAN [6, 32, 38], and AI generates segmentation and app-segment recommendations from live traffic [10, 11]. The platform is FedRAMP authorized at moderate and high levels, ISO 27001 certified, and runs a FIPS 140-2/140-3 validated cryptographic stack [25, 26, 45]. Zscaler positions ZTE as an architectural replacement for firewalls and VPNs across users, workloads, and IoT/OT [2].

---

## 2. Verdict Summary

**Counts across 33 checklist items:**

| Verdict          | Count | Confidence: high | medium | low |
|------------------|-------|------------------|--------|-----|
| supported        | 14    | 1                | 13     | 0   |
| partial          | 16    | 0                | 16     | 0   |
| not_supported    | 1     | 0                | 1      | 0   |
| unknown          | 2     | 0                | 0      | 2   |
| not_applicable   | 0     | 0                | 0      | 0   |

**Evidence quality:** 16 items backed by ≥ 2 source_types; 29 items backed by vendor_doc only (confidence capped at medium per validator rule).

---

## 3. Per-Item Verdicts

### Category 1 - Visibility & Mapping

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 1.1 | Tự động khám phá luồng dữ liệu thời gian thực (Real-time Auto-discovery). | Supported | medium | - | Zscaler Microsegmentation and Workload Discovery services discover cloud resources (VPCs, subnets, VMs/EC2) and applications in near-real time using cloud-native tags and attributes, and ZPA automatically discovers and catalogs private applications. [9], [11], [12], [32], [35], [40] |
| 1.2 | Hiển thị sơ đồ kết nối trực quan theo App, Environment, Role, Process. | Partial | medium | - | An interactive application map and application dependency maps show matched flows between application resources, and autonomous segmentation visualizes which user groups can access which applications; the views are not organized by the full App/Environment/Role/Process model the checklist requires. [9], [10], [11], [12] |
| 1.3 | Lưu trữ lịch sử luồng kết nối ít nhất 90 ngày để truy vết forensic. | Supported | medium | 180 days | Zero Trust Cloud Standard includes global real-time interactive reporting with a 6-month window, and the Advanced Plus edition adds an NSS log feed with log recovery, exceeding the 90-day flow-history retention requirement. [10] |
| 1.4 | Hiển thị lỗ hổng phần mềm (Vulnerability/CVE Context) trực tiếp trên map. | Unknown | low | - | no evidence found (No staged source shows vulnerability or CVE context displayed on the microsegmentation map or application views.) |
| 1.5 | Phát hiện các luồng kết nối ẩn, luồng không tiêu chuẩn (Unrecognized Traffic). | Supported | medium | - | Flow inventory records 5-tuple details with application names, OT/IoT segmentation baselines authorized versus unauthorized access, and autonomous user-to-app segmentation surfaces unaccounted-for shadow IT and rogue applications. [4], [9], [12], [33], [42] |

### Category 2 - Policy Management

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 2.1 | Tạo chính sách dựa trên Tag/Label/Identity (không phụ thuộc IP/VLAN). | Supported | medium | - | Security policies can be built on user-defined tags, cloud attributes, and identity: ZPA access is determined by identity and context rather than IP address, and Zero Trust Cloud collects cloud metadata (tags, labels, attributes) for policy groups. [6], [10], [12], [32], [38] |
| 2.2 | Hỗ trợ gợi ý chính sách tự động bằng AI/Machine Learning (Rule Recommendation). | Supported | medium | - | Automated policy recommendations and AI-generated app-segment suggestions are produced from live traffic analysis by machine-learning models in both ZPA autonomous user-to-app segmentation and Zscaler Microsegmentation. [1], [10], [11], [12] |
| 2.3 | Chế độ Mô phỏng / Giả lập Chính sách (Policy Simulation / Dry-run). | Partial | medium | - | Autonomous user-to-app segmentation proves a recommendation's impact (e.g., the projected reduction in exposed users) before it is committed as policy; a general traffic-replay or dry-run simulation engine for all policies is not documented. [42] |
| 2.4 | Khả năng khôi phục chính sách tức thì (Instant 1-Click Rollback). | Unknown | low | - | no evidence found (No staged source documents instant one-click rollback of a previously published segmentation/access policy; Client Connector rollback is documented only for agent updates.) |
| 2.5 | Hỗ trợ chính sách phân cấp (Inherited & Hierarchical Rules). | Partial | medium | - | Application Zones and Appzones scope policy rules to application zones or environments, providing hierarchical policy organization; inherited rule hierarchies are not documented. [9], [10] |

### Category 3 - Architecture & Support

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 3.1 | Hỗ trợ đa dạng OS: Windows Server (2003-2022), Linux RHEL/CentOS/Ubuntu, AIX, Solaris. | Partial | medium | - | Zscaler Microsegmentation agents support Windows and Linux, and ZPA components list Windows 8+, Linux, macOS, ChromeOS, iOS, and Android; AIX and Solaris are not documented as supported. [9], [10], [12] |
| 3.2 | Hỗ trợ Container / Kubernetes / OpenShift native isolation. | Supported | medium | - | Host-based microsegmentation supports Kubernetes on Amazon EKS and Google GKE, and the ZPA App Connector can be deployed on OpenShift and Docker. [10], [12], [20], [39] |
| 3.3 | Hỗ trợ cả giải pháp Agent-based và Agentless/Network Integration. | Supported | medium | - | ZPA offers both client-based (Zscaler Client Connector) and clientless browser access, OT/IoT Segmentation is agentless, and microsegmentation documentation describes agent-based enforcement with network-based fallback for out-of-scope systems. [4], [12], [34] |
| 3.4 | Tương thích môi trường cách ly hoàn toàn không có Internet (Air-gapped Network). | Not Supported | medium | - | Zscaler's own material argues against air-gapped operation, and the ZPA business-continuity architecture requires the Private Cloud Controller to continuously synchronize with the Zero Trust Exchange cloud, so a fully isolated network with no internet is not supported. [14], [22], [24] |
| 3.5 | Khả năng mở rộng (Scalability) lên tới trên 50,000 Workloads tập trung. | Partial | medium | n/a (qualitative) | ZPA Public Service Edges handle millions of concurrent users across 160+ PoPs and the platform processes more than 500 billion transactions per day, but no workload-count figure such as 50,000 is published. [12], [13] |

### Category 4 - Performance & Impact

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 4.1 | Mức độ tiêu tốn tài nguyên Agent: CPU < 1%. | Partial | medium | n/a (qualitative) | Zscaler Client Connector and microsegmentation agents are described only as 'lightweight'; no CPU-usage percentage is published. [7] |
| 4.2 | Mức độ tiêu tốn tài nguyên Agent: RAM < 100MB. | Partial | medium | n/a (qualitative) | Agents are described only as 'lightweight' (e.g., 'Lightweight agents can be installed on common operating systems'); no RAM footprint figure is published. [9] |
| 4.3 | Không làm tăng độ trễ mạng (< 0.1ms network latency). | Partial | medium | n/a (qualitative) | ZPA is described as providing secure, low-latency access on a Zscaler cloud designed for high availability and low latency, but no sub-0.1 ms latency figure is published. [23], [30] |
| 4.4 | Agent Fail-safe: Nếu Agent lỗi hoặc crash, giao tiếp mạng giữ nguyên không bị gián đoạn. | Partial | medium | - | ZPA Business Continuity Mode keeps zero-trust policies enforced and access available when the Zscaler cloud is unreachable, and the Client Connector is documented to protect endpoints during disconnection; behavior after a workload-agent crash is not documented. [7], [14] |
| 4.5 | Cài đặt và cập nhật Agent không yêu cầu Reboot Server. | Partial | medium | - | Client Connector supports silent auto-install of the client and certificates, and microsegmentation agents are upgraded in groups via version profiles; no explicit statement that installs and updates require no server reboot. [7], [9] |

### Category 5 - Integration & Automation

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 5.1 | Full RESTful API hỗ trợ 100% chức năng quản trị. | Partial | medium | - | OneAPI provides a single, consistent control plane for ZIA, ZPA, ZDX, ZCC, and ZTC, and programmable interfaces (Zscaler APIs, Terraform, CloudFormation) automate deployments; 100% coverage of administrative functions is not explicitly stated. [10], [16], [19] |
| 5.2 | Tích hợp sẵn với SIEM/SOAR (Splunk, QRadar, Sentinel) qua Syslog/CEF/API. | Supported | high | - | Log Streaming Service and Cloud NSS stream logs natively into Splunk and Microsoft Sentinel (including SOAR playbooks), QRadar is listed among supported SIEM integrations, and LSS streams user activity to SIEM. [12], [16], [17], [27], [43] |
| 5.3 | Tích hợp CMDB (ServiceNow) để đồng bộ hóa thông tin nhãn (Tags). | Partial | medium | - | ServiceNow integrations cover rapid app onboarding for segmentation and ITSM/SOAR workflows, but direct CMDB tag/label synchronization is not explicitly documented. [11], [19], [41] |
| 5.4 | Tích hợp CI/CD Pipeline (Jenkins, GitLab, Terraform) cho DevSecOps. | Supported | medium | - | Zero Trust Cloud environments can be declared as code with the Terraform provider and deployed through CI/CD pipelines, with CloudFormation and Azure Resource Manager templates provided out of the box. [19], [36] |

### Category 6 - Security & Compliance

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 6.1 | Kiểm soát truy cập sâu tới cấp độ Tiến trình (Process-level enforcement). | Supported | medium | - | Workload identities extend down to the subprocess level, the workload segmentation agent generates process-level software fingerprints, and Zero Trust Cloud collects process-level metadata from VM and container environments. [10], [33], [36] |
| 6.2 | Tích hợp Threat Intelligence & Đánh lừa (Honeypot/Deception detection). | Supported | medium | - | Zscaler Deception deploys decoys, lures, and honeypot-style decoys across endpoints, clouds, and applications (integrated with Client Connector and ZPA), and the platform ingests more than 500 trillion daily threat-intelligence signals. [2], [5] |
| 6.3 | Báo cáo tuân thủ có sẵn theo chuẩn: PCI-DSS, NIST 800-207, ISO 27001, IEC 62443. | Partial | medium | - | PCI DSS 4.0 and ISO 27001 compliance are documented, NIST 800-207 zero trust architecture is addressed, and IEC 62443 alignment is described via ZPA; a formal IEC 62443 compliance report or certification is not evidenced. [26], [29], [30], [31] |
| 6.4 | Mã hóa dữ liệu truyền giữa Agent và Controller (TLS 1.3 / Mutual Auth). | Partial | medium | - | The Client Connector establishes a permanent TLS connection to the ZPA Service Edge, and the platform supports TLS 1.3 encryption of traffic in transit; explicit mutual-TLS between agent and controller is not documented in the staged sources. [12], [29] |

### Category 7 - High Availability

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 7.1 | Kiến trúc Cụm Controller hỗ trợ High Availability (Active-Active / Active-Passive). | Supported | medium | - | ZPA is documented as a highly available and resilient cloud service with automatic load-based user-to-service-edge redirection, delivered from more than 160 globally distributed data centers. [13], [14] |
| 7.2 | Nếu Controller mất kết nối hoàn toàn, Agent trên Host vẫn tiếp tục thực thi Policy (Autonomous Mode). | Supported | medium | - | With Private Cloud Controllers and Business Continuity Mode, ZPA enforces authentication and zero-trust policies and continues user access even when the Zscaler cloud is unreachable. [12], [14] |
| 7.3 | Hỗ trợ sao lưu và khôi phục thảm họa (Disaster Recovery site sync). | Supported | medium | - | The Private Cloud Controller continuously synchronizes configuration and policies with the Zscaler cloud, and a business-continuity/disaster-recovery offering maintains access during black swan events. [12], [14] |

### Category 8 - Standards Certification

| ID  | Requirement | Verdict | Conf | Value | Evidence |
|-----|-------------|:-------:|:----:|-------|----------|
| 8.1 | Đạt chứng nhận an ninh quốc tế: FIPS 140-2/140-3, Common Criteria EAL4+. | Partial | medium | - | NIST CMVP lists Zscaler FIPS 140-2 validated modules (Zscaler Crypto Module #3159, Zscaler Mobile Cryptographic Module #3154) and a FIPS 140-3 validated module (#5080 Zscaler Java Crypto Module); no Common Criteria EAL4+ certification is evidenced. [45] |
| 8.2 | Chứng nhận tương thích phần mềm công nghiệp từ Siemens, Honeywell, ABB (cho OT). | Partial | medium | - | Zscaler and Siemens jointly deliver zero-trust OT access with the ZPA App Connector running on Siemens SCALANCE LPE and sold through Siemens' industrial security channel; Honeywell and ABB integrations are not evidenced. [22], [23] |

---

## 4. Notable Strengths

- **Identity- and tag-based policy model (items 2.1, 2.2):** Policies are built on user-defined tags, cloud attributes, and identity via Workload Groups and ZPA access policies, with AI-generated segmentation recommendations derived from live traffic analysis [6, 10, 32, 38].
- **Process-level enforcement (items 1.5, 6.1):** Workload identities extend to the subprocess level, so unverified software is blocked from communicating and unaccounted-for applications are surfaced [33, 36].
- **Real-time discovery and mapping (items 1.1, 1.2):** Workload Discovery and ZPA app discovery surface cloud resources and applications in near real time, with interactive application maps and dependency maps [9, 11, 35, 40].
- **SIEM/SOAR and Infrastructure-as-Code integrations (items 5.2, 5.4):** Cloud NSS and Log Streaming Service stream logs natively to Splunk, Microsoft Sentinel, and QRadar with SOAR playbooks, and Terraform providers plus CloudFormation/ARM templates enable CI/CD-driven deployments [16, 17, 19, 36, 43].
- **Resilient cloud architecture (items 7.1, 7.2, 7.3):** ZPA is documented as a highly available cloud service with automatic load-based redirection, and Business Continuity Mode with Private Cloud Controllers keeps policy enforced and access available when the Zscaler cloud is unreachable [12, 14].

## 5. Notable Gaps / Risks

- **No documented policy dry-run or rollback (items 2.3, 2.4):** Only AI recommendation impact-preview is documented; no general policy simulation engine or one-click rollback of published segmentation/access policies was found in staged sources.
- **Unverified agent resource and latency figures (items 4.1, 4.2, 4.3):** CPU, RAM, and latency are only described qualitatively ("lightweight", "low latency"); no published numbers meet the <1% CPU, <100MB RAM, or <0.1ms thresholds.
- **Limited legacy OS and workload-scale evidence (items 3.1, 3.5):** AIX/Solaris support is undocumented, and no workload-count figure (e.g., 50,000) is published - only concurrent-user and transaction volume scale.
- **No air-gapped deployment (item 3.4):** The platform is cloud-delivered and its business-continuity architecture requires the Private Cloud Controller to continuously synchronize with the Zero Trust Exchange, ruling out fully isolated networks [14, 24].
- **Missing certification breadth (items 8.1, 8.2):** No Common Criteria EAL4+ certification is evidenced, and only Siemens (not Honeywell or ABB) OT compatibility is documented [22, 23, 45].

## 6. Evidence Quality Notes

This run collected 98 evidence entries across 45 staged sources (6 PDF datasheets, 20 vendor blogs, 16 vendor product/press pages, and 3 independent sources). Only 2 of 33 items are backed by non-vendor sources: item 5.2 (technologymatch.com third-party review, which independently lists Splunk/QRadar/Sentinel log forwarding) and item 8.1 (the NIST CMVP registry, which lists three Zscaler FIPS 140-2/140-3 validated modules). Wikipedia supplied background only and was not load-bearing for any verdict. Because the remaining 31 items rest on vendor documentation, confidence is capped at medium across those items per the validator's vendor-only rule.

Sources were mutually consistent; the judgements below are worth noting. Item 3.4 (air-gapped) is rated not_supported from Zscaler's own anti-air-gap positioning plus the documented cloud-sync requirement of Business Continuity Mode, rather than from silence. Numeric items 4.1, 4.2, 4.3, and 3.5 were downgraded to partial with numeric_value null because only qualitative language exists. Item 1.3 is rated supported on the Zero Trust Cloud 6-month interactive reporting window (180 days). The main limitation is that help.zscaler.com product documentation (a JS-rendered SPA) was unreachable in this environment, so items like 1.4 (CVE context) and 2.4 (policy rollback) remain unknown for lack of evidence rather than confirmed absence; re-running with the vendor docs staged could resolve them.

---

## Bibliography

[1] Zscaler, Inc.. "Zero Trust Microsegmentation | Zscaler". https://www.zscaler.com/products-and-solutions/microsegmentation (Retrieved: 2026-08-10T13:45:13Z)
[2] Zscaler, Inc.. "The Zscaler Zero Trust Exchange Platform". https://www.zscaler.com/products-and-solutions/zero-trust-exchange-zte (Retrieved: 2026-08-10T13:45:13Z)
[3] Zscaler, Inc.. "Zscaler Private Access (ZPA) - ZTNA". https://www.zscaler.com/products-and-solutions/zscaler-private-access (Retrieved: 2026-08-10T13:45:18Z)
[4] Zscaler, Inc.. "OT/IoT Segmentation: Eliminate Lateral Movement with Zero Trust". https://www.zscaler.com/products-and-solutions/zero-trust-device-segmentation (Retrieved: 2026-08-10T13:45:18Z)
[5] Zscaler, Inc.. "Advanced Deception Technology Solutions | Zscaler". https://www.zscaler.com/products-and-solutions/deception-technology (Retrieved: 2026-08-10T13:45:18Z)
[6] Zscaler, Inc.. "Zero Trust Cloud Workload Protection". https://www.zscaler.com/products/zscaler-workload-segmentation (Retrieved: 2026-08-10T13:45:18Z)
[7] Zscaler, Inc.. "Zscaler Client Connector | Platform". https://www.zscaler.com/products-and-solutions/zscaler-client-connector (Retrieved: 2026-08-10T13:45:25Z)
[8] Zscaler, Inc.. "Zscaler Internet Access - SSE". https://www.zscaler.com/products/zscaler-internet-access (Retrieved: 2026-08-10T13:45:25Z)
[9] Zscaler, Inc.. "Data Sheet: Zscaler Microsegmentation". https://www.zscaler.com/resources/data-sheets/advantages-of-using-zscaler-for-microsegmentation.pdf (Retrieved: 2026-08-10T13:47:02Z)
[10] Zscaler, Inc.. "Data Sheet: Zero Trust Cloud". https://www.zscaler.com/resources/data-sheets/zero-trust-cloud.pdf (Retrieved: 2026-08-10T13:47:02Z)
[11] Zscaler, Inc.. "At-a-Glance: Zscaler AI-Powered App Segmentation". https://www.zscaler.com/resources/data-sheets/zscaler-ai-powered-app-segmentation.pdf (Retrieved: 2026-08-10T13:47:02Z)
[12] Zscaler, Inc.. "Data Sheet: Zscaler Private Access". https://www.zscaler.com/resources/data-sheets/zscaler-private-access.pdf (Retrieved: 2026-08-10T13:47:06Z)
[13] Zscaler, Inc.. "At-a-Glance: Zscaler Zero Trust Exchange". https://www.zscaler.com/resources/data-sheets/zscaler-zero-trust-exchange-at-a-glance.pdf (Retrieved: 2026-08-10T13:47:06Z)
[14] Zscaler, Inc.. "At-a-Glance: Business Continuity for Zscaler Private Access". https://www.zscaler.com/resources/solution-briefs/zpa-business-continuity-aag.pdf (Retrieved: 2026-08-10T13:47:06Z)
[15] Zscaler, Inc.. "Zscaler Secures Cloud Workloads with the Zero Trust Exchange". https://www.zscaler.com/blogs/company-news/zscaler-secures-cloud-workloads-zscaler-zero-trust-exchange (Retrieved: 2026-08-10T13:47:41Z)
[16] Zscaler, Inc.. "Achieve True Zero Trust with Zscaler and Splunk". https://www.zscaler.com/blogs/company-news/achieve-true-zero-trust-zscaler-and-splunk (Retrieved: 2026-08-10T13:47:42Z)
[17] Zscaler, Inc.. "Introducing Zscaler and Microsoft Sentinel's New SIEM & SOAR Capabilities". https://www.zscaler.com/blogs/product-insights/elevating-cybersecurity-zscaler-and-microsoft-sentinel (Retrieved: 2026-08-10T13:47:46Z)
[18] Zscaler, Inc.. "Introducing Zscaler and ServiceNow: Protect More, Work Smarter". https://www.zscaler.com/blogs/product-insights/introducing-zscaler-and-servicenow-protect-more-work-smarter (Retrieved: 2026-08-10T13:47:41Z)
[19] Zscaler, Inc.. "Introducing Zscaler Zero Trust Cloud Terraform Provider". https://www.zscaler.com/blogs/product-insights/introducing-zscaler-zero-trust-cloud-terraform-provider (Retrieved: 2026-08-10T13:47:43Z)
[20] Zscaler, Inc.. "Deploy App Connector on Red Hat OpenShift". https://www.zscaler.com/innovations/deploy-app-connector-red-hat-openshift (Retrieved: 2026-08-10T13:47:46Z)
[21] Zscaler, Inc.. "Enhanced Cloud Security Policies for Kubernetes". https://www.zscaler.com/innovations/enhanced-cloud-security-policies-kubernetes (Retrieved: 2026-08-10T13:47:48Z)
[22] Zscaler, Inc.. "Siemens Now Sells Zscaler for IoT/OT for Industrial Security". https://www.zscaler.com/blogs/company-news/zscaler-iot-ot-now-sold-siemens-industrial-security (Retrieved: 2026-08-10T13:47:53Z)
[23] Zscaler, Inc.. "Siemens and Zscaler Partner to Extend Zero Trust Security to the Industrial Edge for Smart Factories". https://www.zscaler.com/blogs/company-news/siemens-and-zscaler-partner-extend-zero-trust-security-industrial-edge-smart (Retrieved: 2026-08-10T13:47:55Z)
[24] Zscaler, Inc.. "From Air Gaps to Always Connected: The Uptime Challenge Security Must Solve". https://www.zscaler.com/blogs/company-news/air-gaps-always-connected-uptime-challenge-security-must-solve (Retrieved: 2026-08-10T13:47:56Z)
[25] Zscaler, Inc.. "Zscaler's Entire Zero Trust Exchange Platform FedRAMP Authorized". https://www.zscaler.com/blogs/company-news/zscaler-s-entire-zero-trust-exchange-platform-fedramp-authorized (Retrieved: 2026-08-10T13:47:58Z)
[26] Zscaler, Inc.. "Press Release: Zscaler Achieves ISO 27001 Certification for its Cloud Security Service". https://www.zscaler.com/press/zscaler-achieves-iso-27001-certification-its-cloud-security-service (Retrieved: 2026-08-10T13:48:47Z)
[27] Zscaler, Inc.. "Zscaler FedRAMP Platforms: Hyperscaling Compliance and Security". https://www.zscaler.com/privacy-compliance/customer-compliance/fedramp (Retrieved: 2026-08-10T13:48:49Z)
[28] Zscaler, Inc.. "Press Release: Zscaler Completes SOC 2, Type II Certification". https://www.zscaler.com/press/zscaler-completes-soc-2-type-ii-certification (Retrieved: 2026-08-10T13:48:51Z)
[29] Zscaler, Inc.. "SASE Solutions for PCI DSS 4.0 Compliance & Enhanced Security". https://www.zscaler.com/privacy-compliance/customer-compliance/pci-dss (Retrieved: 2026-08-10T13:48:10Z)
[30] Zscaler, Inc.. "What Is IEC 62443? Definition, Breakdown & Methodology". https://www.zscaler.com/zpedia/what-is-iec-62443 (Retrieved: 2026-08-10T13:48:11Z)
[31] Zscaler, Inc.. "Bringing NIST Special Publication 800-207 down to Earth". https://www.zscaler.com/blogs/cxo-insights/abstraction-action-bringing-nist-special-publication-800-207-down-earth (Retrieved: 2026-08-10T13:48:14Z)
[32] Zscaler, Inc.. "How to Enable User-Defined Tags". https://www.zscaler.com/blogs/product-insights/how-enable-user-defined-tags-identity-securing-cloud-workloads (Retrieved: 2026-08-10T13:48:10Z)
[33] Zscaler, Inc.. "Identity-Based Microsegmentation is Foundational to Cloud Security". https://www.zscaler.com/blogs/product-insights/identity-based-microsegmentation-foundational-cloud-security-don-t-get (Retrieved: 2026-08-10T13:48:11Z)
[34] Zscaler, Inc.. "Microsegmentation 101". https://www.zscaler.com/blogs/product-insights/microsegmentation-101 (Retrieved: 2026-08-10T13:48:14Z)
[35] Zscaler, Inc.. "Innovations Simplify Cloud Workload Security". https://www.zscaler.com/blogs/product-insights/new-zero-trust-innovations-radically-simplify-cloud-workload-security (Retrieved: 2026-08-10T13:48:16Z)
[36] Zscaler, Inc.. "Securing Workloads in Multicloud Environments with the Zscaler Zero Trust Exchange". https://www.zscaler.com/blogs/product-insights/securing-workloads-multi-cloud-environments-zscalers-zero-trust-exchange (Retrieved: 2026-08-10T13:51:08Z)
[37] Zscaler, Inc.. "Zero Trust Meets Multicloud: A Guide to Secure Workload Segmentation". https://www.zscaler.com/blogs/product-insights/zero-trust-meets-multicloud-guide-secure-workload-segmentation (Retrieved: 2026-08-10T13:51:10Z)
[38] Zscaler, Inc.. "Modernizing Cloud Workload Policies: Using Tags and Attributes with ZPA". https://www.zscaler.com/blogs/product-insights/modernizing-cloud-workload-policies-using-tags-and-attributes-zscaler (Retrieved: 2026-08-10T13:51:12Z)
[39] Zscaler, Inc.. "At Zenith Live 2026, Zero Trust Cloud Takes Workload Security Further". https://www.zscaler.com/blogs/product-insights/zenith-live-2026-zero-trust-cloud-takes-workload-security-further (Retrieved: 2026-08-10T13:51:14Z)
[40] Zscaler, Inc.. "Innovations to Accelerate Adoption of Zero Trust in Public Cloud Workloads". https://www.zscaler.com/blogs/product-insights/innovations-accelerate-adoption-zero-trust-public-cloud-workloads (Retrieved: 2026-08-10T13:53:44Z)
[41] Zscaler, Inc.. "Press Release: Zscaler and ServiceNow Integrate to Offer Enterprise Cloud Data Control and Fast Threat Detection and Response". https://www.zscaler.com/press/zscaler-and-servicenow-integrate-offer-enterprise-cloud-data-control-and-fast-threat (Retrieved: 2026-08-10T13:51:59Z)
[42] Zscaler, Inc.. "AI for Segmentation: The Limits of AI Policy Optimizers and Private Access Co-Pilots". https://www.zscaler.com/blogs/product-insights/ai-segmentation-limits-ai-policy-optimizers-and-private-access-co-pilots (Retrieved: 2026-08-10T13:52:02Z)
[43] Technology Match. "What is Zscaler, How it Works, and What it Does for IT Leaders". https://technologymatch.com/blog/what-is-zscaler-how-it-works-and-what-it-does-for-it-leaders (Retrieved: 2026-08-10T13:51:08Z)
[44] Wikipedia. "Zscaler - Wikipedia". https://en.wikipedia.org/wiki/Zscaler (Retrieved: 2026-08-10T13:45:25Z)
[45] NIST Cryptographic Module Validation Program. "NIST CMVP Validated Modules search (q=zscaler)". https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules/search?SearchMode=Advanced&q=zscaler (Retrieved: 2026-08-10T13:53:17Z)

---

## Appendix A - Methodology

- **Research mode used:** standard
- **Queries executed:** 12
- **Sources reviewed:** 45 (kept: 45, discarded for low credibility: n/a (not tracked))
- **Source_types distribution:** certification_registry: 1, community: 1, third_party_review: 1, vendor_blog: 20, vendor_datasheet: 6, vendor_doc: 16
- **Verify script results:** see validate_assessment.py output for this run

## Appendix B - Machine-readable outputs

Companion files in this run directory:
- `assessment.json` - canonical verdict store (validated against `schemas/assessment.schema.json`)
- `sources.jsonl`, `evidence.jsonl`, `claims.jsonl` - inherited from deep-research skill
- `run_manifest.json` - research config and provenance
