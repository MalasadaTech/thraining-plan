# Defensive Cyber Operations

**SOC, Cyber Threat Intelligence, Threat Hunting, and Detection Engineering**

**MalasadaTech Training Plan – First Edition**  
**v0.2 Review Draft · Build date: 2026-10-05**  
Source snapshot date: 2026-10-05.

Defensive work depends on more than recognizing a suspicious value. An analyst needs to explain what happened, decide which questions remain, and give the next person enough evidence to act. This book follows that work from shared foundations through SOC investigation, Cyber Threat Intelligence, Threat Hunting, and Detection Engineering.

The chapters combine technical examples with the decisions those examples support. You will read endpoint and network evidence, evaluate intelligence, develop scoped hunts, and consider how findings become maintained detection coverage.

## How to Use This Book

Read the shared foundations first, then follow the role tracks in order. Chapter numbers match the curriculum so you can return to a particular lesson during practice. The opening and closing chapters of each track provide orientation and integration. Multi-lesson subunits also include short advance-organizer introductions and end-state summaries so you can preview the structure before reading closely; the final course summary reconnects all four roles.

Use **Preview → Predict → Read → Confirm**: preview a subunit introduction and its end-state summary, predict how the lessons fit together, read the detail, then return to the summary to check your understanding.

At a worked example, pause before the explanation. Describe the observation in your own words, identify what remains unknown, and name the next useful question. Use the knowledge checks to test that reasoning. They are learner exercises; this manuscript does not add an instructor answer key.

Estimated times are retained from the course as planning guides. The CTI platform chapters use two passes: first retrieve and describe evidence, then return for interpretation during the relevant enrichment method. Their estimates cover both passes together. Use the example cards and records printed in the lessons where available. Controlled CSV/Python assets required by the embedded hunt and detection-validation practicals are included under their owning lessons. The external-platform pivot practical still requires approved live/public platform access or authorized training accounts; this book does not provide platform accounts.

Examples distinguish course facts from local operating requirements. Where a chapter asks for a local priority, approval path, sensor configuration, or response clock, obtain that information from the responsible organization. Classroom examples provide practice rather than an operating policy.

Callouts identify their purpose in plain language. **A12 Case Study** marks the recurring case; **Example** introduces a worked observation or decision; **Key Point**, **Evidence Boundary**, and **Remember** emphasize the reasoning to retain. **Knowledge Check** introduces questions for practice. Detailed role ratings and task mappings are collected in [Appendix B](#appendix-b--proficiency-mapping).

## The Course-Wide Learning Model

**Observe → Understand → Search → Improve Coverage → Observe Again**

The SOC investigates observed activity. CTI evaluates evidence against an intelligence requirement. Threat Hunting tests questions beyond the original alert. Detection Engineering decides how to improve and maintain coverage. Each role contributes a different product to the same defensive workflow.

> **Key Point:** Describe what the evidence shows first. Then decide what it means.

A useful product carries its observations, reasoning, scope, uncertainty, and next decision together. As you read, ask what another analyst could verify from the product and what they would still need to establish.

> **Evidence Boundary:** Keep an observed event separate from an assessment of its meaning. Explain the additional evidence needed for a stronger conclusion.

## Meet A12: The Recurring Case Study

A12 is a fictional incident at **Dixon, Yamada, & Associates (DYA)**, a law firm. Its recurring starting point is **WS-JLEE**, a workstation in Building C associated with the account **jlee**. Those names help you recognize the same case as the work moves between roles.

You will encounter the evidence progressively. The shared foundations introduce the environment and responsibilities; later chapters examine the case from the SOC, CTI, Threat Hunting, and Detection Engineering perspectives. Work with the evidence supplied for each exercise, and distinguish a proposed follow-up from an established finding.

> **A12 Case Study:** A12 is the recurring case study used throughout this book. You will encounter its evidence progressively as you move through SOC, CTI, Threat Hunting, and Detection Engineering. The complete case study is available in [Appendix A](#appendix-a--the-complete-a12-case-study) after the main course.

## Contents

- [Part I — Shared Foundations](#part-i--shared-foundations)
  - [0.1 — How this course is laid out](#01--how-this-course-is-laid-out)
  - [0.2 — What a SOC is](#02--what-a-soc-is)
  - [0.3 — Jobs in one sentence](#03--jobs-in-one-sentence)
  - [0.4 — How work can move](#04--how-work-can-move)
  - [0.5 — Where the jobs lightly overlap](#05--where-the-jobs-lightly-overlap)
  - [0.6 – Shared Analytical Frameworks: Introduction](#06--shared-analytical-frameworks-introduction)
  - [0.6.1 — MITRE ATT&CK](#061--mitre-attck)
  - [0.6.2 — Diamond Model](#062--diamond-model)
  - [0.6.3 — Cyber Kill Chain](#063--cyber-kill-chain)
  - [0.6 – Shared Analytical Frameworks: Summary](#06--shared-analytical-frameworks-summary)
  - [0.7 — External tools](#07--external-tools)
  - [0.8 — Environment / signal flow](#08--environment--signal-flow)
  - [0.9 — Common Initial Access Paths](#09--common-initial-access-paths)
  - [0.10 — Shared Foundations Section Summary](#010--shared-foundations-section-summary)
- [Part II — SOC Analyst](#part-ii--soc-analyst)
  - [1.0 — SOC Analyst Fundamentals: How the 1.x Block Fits Together](#10--soc-analyst-fundamentals-how-the-1x-block-fits-together)
  - [1.1 – Endpoint Activity: Introduction](#11--endpoint-activity-introduction)
  - [1.1.1 — Endpoint activity (the map)](#111--endpoint-activity-the-map)
  - [1.1.2 — Process Activity](#112--process-activity)
  - [1.1.3 — File System Activity](#113--file-system-activity)
  - [1.1.4 — Network Activity (Endpoint)](#114--network-activity-endpoint)
  - [1.1.5 — Registry Activity](#115--registry-activity)
  - [1.1.6 — Image and Driver Load Activity](#116--image-and-driver-load-activity)
  - [1.1 – Endpoint Activity: Summary](#11--endpoint-activity-summary)
  - [1.2 – Zeek Network Evidence: Introduction](#12--zeek-network-evidence-introduction)
  - [1.2.1 — Zeek Concepts](#121--zeek-concepts)
  - [1.2.2 — Conn Engine](#122--conn-engine)
  - [1.2.3 — DNS Engine](#123--dns-engine)
  - [1.2.4 — TLS Engine](#124--tls-engine)
  - [1.2.5 — HTTP Engine](#125--http-engine)
  - [1.2.6 — SMTP Engine](#126--smtp-engine)
  - [1.2.7 — Files Engine](#127--files-engine)
  - [1.2.8 — Weird Engine](#128--weird-engine)
  - [1.2 – Zeek Network Evidence: Summary](#12--zeek-network-evidence-summary)
  - [1.3 – Detection Rules: Introduction](#13--detection-rules-introduction)
  - [1.3.1 — SIGMA Rules](#131--sigma-rules)
  - [1.3.2 — Suricata Rules](#132--suricata-rules)
  - [1.3.3 — YARA Rules](#133--yara-rules)
  - [1.3.4 — SIEM Rules](#134--siem-rules)
  - [1.3 – Detection Rules: Summary](#13--detection-rules-summary)
  - [1.4 – Alert Investigation and Assessment: Introduction](#14--alert-investigation-and-assessment-introduction)
  - [1.4.1 — Alert Context and Investigation](#141--alert-context-and-investigation)
  - [1.4.2 — Alert Classification](#142--alert-classification)
  - [1.4.3 — Common False Positive Causes](#143--common-false-positive-causes)
  - [1.4.4 — Common Alert Categorizations](#144--common-alert-categorizations)
  - [1.4.5 — SLA / Response Time Goals](#145--sla--response-time-goals)
  - [1.4 – Alert Investigation and Assessment: Summary](#14--alert-investigation-and-assessment-summary)
  - [1.5 – Reporting and Notification: Introduction](#15--reporting-and-notification-introduction)
  - [1.5.1 — Report Types](#151--report-types)
  - [1.5.2 — Reporting Timeline Requirements](#152--reporting-timeline-requirements)
  - [1.5.3 — Notification and Distribution](#153--notification-and-distribution)
  - [1.5 – Reporting and Notification: Summary](#15--reporting-and-notification-summary)
  - [1.6 — SOC Analyst Section Summary](#16--soc-analyst-section-summary)
- [Part III — Cyber Threat Intelligence](#part-iii--cyber-threat-intelligence)
  - [2.0 — Cyber Threat Intelligence: How the 2.x Block Fits Together](#20--cyber-threat-intelligence-how-the-2x-block-fits-together)
  - [2.1 – Intelligence Foundations and Requirements: Introduction](#21--intelligence-foundations-and-requirements-introduction)
  - [2.1.1 — Difference between data, information, and intelligence](#211--difference-between-data-information-and-intelligence)
  - [2.1.2 — Intelligence lifecycle](#212--intelligence-lifecycle)
  - [2.1.3 — Intelligence Types](#213--intelligence-types)
  - [2.1.4 — Intelligence Requirements](#214--intelligence-requirements)
  - [2.1.5 — RFI Intake and Prioritization](#215--rfi-intake-and-prioritization)
  - [2.1.6 — Ensuring Intelligence Is Actionable](#216--ensuring-intelligence-is-actionable)
  - [2.1.7 — Tailoring Output to the Audience](#217--tailoring-output-to-the-audience)
  - [2.1.8 — Attribution](#218--attribution)
  - [2.1.9 — Collection Sources and Methods](#219--collection-sources-and-methods)
  - [2.1 – Intelligence Foundations and Requirements: Summary](#21--intelligence-foundations-and-requirements-summary)
  - [2.2 – Analytical Tradecraft: Introduction](#22--analytical-tradecraft-introduction)
  - [2.2.1 — Estimative language](#221--estimative-language)
  - [2.2.2 — Structured Analytic Techniques](#222--structured-analytic-techniques)
  - [2.2.3 — Admiralty Code](#223--admiralty-code)
  - [2.2.4 — Cognitive Biases and Mitigation](#224--cognitive-biases-and-mitigation)
  - [2.2 – Analytical Tradecraft: Summary](#22--analytical-tradecraft-summary)
  - [2.3 – Analytical Frameworks: Introduction](#23--analytical-frameworks-introduction)
  - [2.3.1 — MITRE ATT&CK for CTI Analysis and Reporting](#231--mitre-attck-for-cti-analysis-and-reporting)
  - [2.3.2 — Diamond Model Application in CTI](#232--diamond-model-application-in-cti)
  - [2.3.3 — Cyber Kill Chain in Intelligence Analysis](#233--cyber-kill-chain-in-intelligence-analysis)
  - [2.3 – Analytical Frameworks: Summary](#23--analytical-frameworks-summary)
  - [2.4 – CTI Tools and Platforms: Introduction](#24--cti-tools-and-platforms-introduction)
  - [2.4.1 — Internal Threat Intelligence Platform](#241--internal-threat-intelligence-platform)
  - [2.4.2 — Selecting Platforms for CTI Work](#242--selecting-platforms-for-cti-work)
  - [2.4.3 — VirusTotal Relations and Behavior](#243--virustotal-relations-and-behavior)
  - [2.4.4 — ANY.RUN](#244--anyrun)
  - [2.4.5 — Silent Push](#245--silent-push)
  - [2.4.6 — urlscan.io](#246--urlscanio)
  - [2.4 – CTI Tools and Platforms: Summary](#24--cti-tools-and-platforms-summary)
  - [2.5 – Technical Enrichment and Discovery: Introduction](#25--technical-enrichment-and-discovery-introduction)
  - [2.5.1 — IOC Handling and Enrichment Concepts](#251--ioc-handling-and-enrichment-concepts)
  - [2.5.2 — Hashing and Similarity Concepts](#252--hashing-and-similarity-concepts)
  - [2.5.3 — RDAP and WHOIS Concepts](#253--rdap-and-whois-concepts)
  - [2.5.4 — Advanced DNS Concepts](#254--advanced-dns-concepts)
  - [2.5.5 — Identifying Additional Adversary Infrastructure from Seed Indicators](#255--identifying-additional-adversary-infrastructure-from-seed-indicators)
  - [2.5.6 — MalasadaTech Defender's ThreatMesh Framework (DTF)](#256--malasadatech-defenders-threatmesh-framework-dtf)
  - [2.5.7 — Correlation, Link Analysis, and Campaign Tracking](#257--correlation-link-analysis-and-campaign-tracking)
  - [2.5 – Technical Enrichment and Discovery: Summary](#25--technical-enrichment-and-discovery-summary)
  - [2.6 – Threat Assessment and Organizational Significance: Introduction](#26--threat-assessment-and-organizational-significance-introduction)
  - [2.6.1 — Extracting Applicable TTPs from Intelligence Reports](#261--extracting-applicable-ttps-from-intelligence-reports)
  - [2.6.2 — Threat Relevance and Organizational Impact](#262--threat-relevance-and-organizational-impact)
  - [2.6 – Threat Assessment and Organizational Significance: Summary](#26--threat-assessment-and-organizational-significance-summary)
  - [2.7 – Intelligence Production and Dissemination: Introduction](#27--intelligence-production-and-dissemination-introduction)
  - [2.7.1 — Core STIX Objects](#271--core-stix-objects)
  - [2.7.2 — How STIX Objects Are Used in Intelligence Production](#272--how-stix-objects-are-used-in-intelligence-production)
  - [2.7.3 — Creating Finished Intelligence Products](#273--creating-finished-intelligence-products)
  - [2.7.4 — RFI Responses and Closure](#274--rfi-responses-and-closure)
  - [2.7.5 — Disseminating Intelligence to the Correct Audiences](#275--disseminating-intelligence-to-the-correct-audiences)
  - [2.7 – Intelligence Production and Dissemination: Summary](#27--intelligence-production-and-dissemination-summary)
  - [2.8 – Local Application: Introduction](#28--local-application-introduction)
  - [2.8.1 — Local Intelligence Requirements and Priorities](#281--local-intelligence-requirements-and-priorities)
  - [2.8.2 — Local Production and Approval Processes](#282--local-production-and-approval-processes)
  - [2.8.3 — Local Dissemination Channels and Customers](#283--local-dissemination-channels-and-customers)
  - [2.8 – Local Application: Summary](#28--local-application-summary)
  - [2.9 — Cyber Threat Intelligence Section Summary](#29--cyber-threat-intelligence-section-summary)
- [Part IV — Threat Hunting](#part-iv--threat-hunting)
  - [3.0 — Threat Hunting: How the 3.x Block Fits Together](#30--threat-hunting-how-the-3x-block-fits-together)
  - [3.1 — Purpose of Threat Hunting](#31--purpose-of-threat-hunting)
  - [3.2 – Hunt Methodology: Introduction](#32--hunt-methodology-introduction)
  - [3.2.1 — Hunt Types](#321--hunt-types)
  - [3.2.2 — Hunt Development Concepts](#322--hunt-development-concepts)
  - [3.2 – Hunt Methodology: Summary](#32--hunt-methodology-summary)
  - [3.3.1 — Tool Capabilities for Hunting](#331--tool-capabilities-for-hunting)
  - [3.4 – CTI as Hunt Input: Introduction](#34--cti-as-hunt-input-introduction)
  - [3.4.1 — Assessing CTI for Hunting Value](#341--assessing-cti-for-hunting-value)
  - [3.4.2 — Extracting Hunt Leads from CTI](#342--extracting-hunt-leads-from-cti)
  - [3.4.3 — STIX as Hunt Input](#343--stix-as-hunt-input)
  - [3.4 – CTI as Hunt Input: Summary](#34--cti-as-hunt-input-summary)
  - [3.5.1 — Using MITRE ATT&CK for Hunt Planning](#351--using-mitre-attck-for-hunt-planning)
  - [3.6 – Attacker Techniques for Hunting: Introduction](#36--attacker-techniques-for-hunting-introduction)
  - [3.6.1 — Persistence Techniques](#361--persistence-techniques)
  - [3.6.2 — Privilege Escalation Techniques](#362--privilege-escalation-techniques)
  - [3.6.3 — Hunt for a Specific Persistence or Privilege-Escalation Technique](#363--hunt-for-a-specific-persistence-or-privilege-escalation-technique)
  - [3.6 – Attacker Techniques for Hunting: Summary](#36--attacker-techniques-for-hunting-summary)
  - [3.7 – Local Hunt Control and Outputs: Introduction](#37--local-hunt-control-and-outputs-introduction)
  - [3.7.1 — Hunt Control and Lead Management](#371--hunt-control-and-lead-management)
  - [3.7.2 — Hunt Documentation Standards](#372--hunt-documentation-standards)
  - [3.7.3 — Hunt Outputs and Hand-off](#373--hunt-outputs-and-hand-off)
  - [3.7 – Local Hunt Control and Outputs: Summary](#37--local-hunt-control-and-outputs-summary)
  - [3.8 — Threat Hunting Section Summary](#38--threat-hunting-section-summary)
- [Part V — Detection Engineering](#part-v--detection-engineering)
  - [4.0 — Detection Engineering: How the 4.x Block Fits Together](#40--detection-engineering-how-the-4x-block-fits-together)
  - [4.1 — What Detection Engineering Owns](#41--what-detection-engineering-owns)
  - [4.2 — Making a Detection Sound and Meeting Shop Requirements](#42--making-a-detection-sound-and-meeting-shop-requirements)
  - [4.3 — Nominations from SOC, Hunt, and CTI](#43--nominations-from-soc-hunt-and-cti)
  - [4.4 — Tune Requests from SOC](#44--tune-requests-from-soc)
  - [4.5 — Hunt and Intel Packages](#45--hunt-and-intel-packages)
  - [4.6 — Detection Lifecycle](#46--detection-lifecycle)
  - [4.7 — Sensor and Data Availability for Detection](#47--sensor-and-data-availability-for-detection)
  - [4.8 — Site-Specific Detection Engineering Knowledge](#48--site-specific-detection-engineering-knowledge)
  - [4.9 — Detection Engineering Section Summary](#49--detection-engineering-section-summary)
- [Part VI — Course Conclusion](#part-vi--course-conclusion)
  - [Course Summary – Bringing the Defensive Workflow Together](#course-summary--bringing-the-defensive-workflow-together)
- [Appendix A — The Complete A12 Case Study](#appendix-a--the-complete-a12-case-study)
- [Appendix B — Proficiency Mapping](#appendix-b--proficiency-mapping)
- [Glossary](#glossary)
- [Acronyms and Technical Abbreviations](#acronyms-and-technical-abbreviations)
- [Consolidated References and Further Reading](#consolidated-references-and-further-reading)

## Part I — Shared Foundations

Begin with the work the four defensive roles share: understanding the environment, recognizing evidence, and handing useful products to the next analyst. These foundations give the later technical lessons a common purpose.

### 0.1 — How this course is laid out

**Estimated Time:** 15 minutes

#### Why This Matters

This course follows the work of SOC analysts, CTI analysts, threat hunters, and detection engineers. Understanding its structure will help you see why a topic appears where it does and how the later lessons build on what you have already learned. Everyone begins with the same introductory material so that the four roles share a common vocabulary.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe the course sequence and explain why the shared lessons come first.
2. Explain why detections precede alert investigation and identify where the SOC track ends.
3. Explain how an RFI connects the course example to the CTI track.

#### How the course progresses

The introductory lessons explain the setting, the roles, and how their work connects. They are followed by four shared topics: frameworks, external tools, the organization's environment, and common initial-access paths. These topics support every role, so they are taught before the SOC material.

The four role tracks then follow this order:

| Track | What the sequence introduces |
|---|---|
| SOC analyst | Understand observations and detections, investigate alerts, and report findings. |
| CTI analyst | Develop answers to intelligence questions using evidence and context. |
| Threat hunter | Search for relevant activity and examine gaps in what detections reveal. |
| Detection engineer | Develop and maintain detections that use what the organization has learned. |

This sequence lets you encounter the same work from several perspectives. Each track develops the responsibilities introduced in the shared lessons.

#### Why detections come before alert work

Within the SOC track, you first learn what a detection is and what activity it is intended to identify. That background helps you interpret an alert when you later investigate one. The SOC track ends with reporting in module 1.5.

A Request for Information, or **RFI**, provides the teaching connection into CTI. An analyst may have a question that remains after investigating an alert; the CTI track explains how intelligence work develops an answer. Later modules explain the local procedures used to request and deliver that work.

#### Using the shared examples

The course uses a fictional company and adversary, introduced in the next lesson. Reusing the same setting makes it easier to focus on the new concept in each module. After the lessons, a companion story brings the work together as one incident.

When applying the material at work, obtain the site's own procedures and environment details. The role-specific lessons explain where those local requirements enter the workflow.

#### Knowledge Check

1. What do learners complete before the four role tracks, and why are those topics shared?
2. Why does the SOC track teach detections before alert investigation, and where does that track end?
3. How does an RFI connect the SOC and CTI parts of this course?

#### Summary

The course begins with shared foundations and then follows SOC, CTI, Hunt, and Detection Engineering. Its ordering helps you understand the evidence and products that later work depends on. The fictional setting and companion story connect the lessons, while local procedures are introduced where they are needed.

### 0.2 — What a SOC is

**Estimated Time:** 15–20 minutes

#### Why This Matters

A Security Operations Center, or **SOC**, is an organizational function that monitors for suspicious activity, investigates what it finds, and coordinates the start of a response. Understanding that purpose gives you a common starting point for the roles and handoffs in this course.

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of a SOC.
2. Explain why several roles contribute to security operations.
3. Identify DYA and PRD as the course setting and distinguish that setting from local procedures.

#### What a SOC contributes

Security tools produce observations and alerts, but someone must interpret them. The SOC brings together people, processes, and technology to assess what the available evidence means and determine what attention an event requires.

For example, an alert may identify unusual activity on a workstation. An analyst reviews the available context, records a finding, and routes the work when further action is needed. The details of that investigation are developed in the SOC track. Here, the important connection is that monitoring leads to an assessment and an appropriate response.

#### How a team supports that purpose

Several functions contribute to security operations. SOC analysts, incident responders, intelligence analysts, hunters, and detection engineers may work together even when they report to different teams. Their responsibilities connect through the evidence they share and the work they request from one another.

A SOC can operate with staff in one location, across multiple locations, or through a service arrangement. For this course, focus on what the function accomplishes. The next lesson introduces the responsibilities that may sit within or alongside it.

#### The setting used in this course

**Dixon, Yamada, & Associates (DYA)** is the fictional law firm used in the lessons. **Pink River Dolphin (PRD)** is the fictional vendor tracking label used in the scenario. These names let later examples refer to a consistent setting without introducing a new organization each time.

The scenario supplies facts for teaching. Your employer's procedures, approval paths, and system details must come from your employer. When a lesson presents evidence, use the evidence supplied at that point; seeing a vendor tracking label does not establish who caused a particular event.

#### Knowledge Check

1. What does a SOC contribute after a security tool produces an alert?
2. Why can several roles contribute to a SOC investigation even if they belong to different teams?
3. What are DYA and PRD, and where should you obtain the procedures used at your workplace?

#### Summary

A SOC monitors and investigates activity so the organization can respond appropriately. Several roles contribute to that purpose, and their arrangement varies by organization. DYA and PRD provide a consistent fictional setting for learning how the work connects.

#### References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.

### 0.3 — Jobs in one sentence

**Estimated Time:** 15–20 minutes

#### Why This Matters

Security work often begins with an alert or a question, then involves people with different responsibilities. Knowing the purpose of each role helps you recognize who can carry the work forward and what result to expect. This lesson gives you a short description of each role used in the course.

#### Learning Objectives

By the end of this module, you will be able to:

1. Summarize each role’s responsibility in one sentence.
2. Identify IR and firewall / IA as supporting functions introduced for handoffs.

#### The roles and their responsibilities

| Role | Core responsibility in this course |
|---|---|
| **SOC analyst** | Investigates an alert, records the finding, and starts the appropriate handoffs. |
| **Incident response (IR)** | Coordinates containment and recovery when incident handling is required. |
| **CTI analyst** | Answers intelligence questions, adds context, and examines related adversary activity or infrastructure. |
| **Threat hunter** | Searches for relevant activity that existing alerts may have missed, using an intelligence package or a hypothesis. |
| **Detection engineer (DE)** | Develops, tests, and maintains detections using identified needs and findings. |
| **Firewall / Information Assurance (IA) function** | Evaluates and implements blocking changes through the organization's authorized process. |

These descriptions identify the main contribution of each role. An organization may assign those responsibilities to teams with different names or combine several responsibilities in one position.

#### Recognizing the work being requested

A **Request for Information (RFI)** asks for information or analysis needed to answer a question. In this course's workflow, it is directed to CTI. A question arising from an alert is one reason for an RFI; other intelligence needs can also produce requests.

Consider a question about the role of a suspicious domain. CTI may develop an answer about that role. If the organization decides to restrict access to the domain, the function responsible for blocking evaluates and carries out that change. If the finding reveals activity worth detecting in the future, DE considers the detection need. The shared domain connects the work, while the requested outcome identifies the responsibility.

#### What the course develops

The four role tracks develop SOC analysis, CTI, hunting, and detection engineering. Incident response and firewall / IA responsibilities are included so learners understand the handoffs, while detailed training for those functions sits outside this course.

For now, aim to explain each role clearly in one sentence. That short description should convey the responsibility and intended result. The following lessons show how those results connect and how responsibilities can overlap.

#### Knowledge Check

1. Describe each of the six roles in one sentence.
2. Which two supporting functions are introduced for handoffs rather than developed as full tracks, and what does each contribute?
3. How does a detection engineer’s responsibility differ from a request to block a domain?

#### Summary

Identify a responsibility by the work requested and the result it should produce. The six roles introduced here support connected parts of security operations; the course develops four of them in depth and explains the other two as handoff destinations.

#### References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.

### 0.4 — How work can move

**Estimated Time:** 20–25 minutes

#### Why This Matters

An investigation can create several kinds of follow-on work. Some work addresses the incident already in progress, while other work improves understanding or future detection. Following one possible workflow helps you identify who receives a request and what they are expected to produce.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe one possible workflow after an alert is triaged.
2. Explain how intelligence findings can support blocking, hunting, and detection work.
3. Given a step in the workflow, identify the receiving role and the product it owns.

#### From an alert to response and a question

An analyst begins by triaging an alert: reviewing the available evidence, determining its significance, and deciding what handling it needs. In the course example, the finding warrants an incident-response handoff and leadership notification. The analyst also identifies a question for CTI and sends an RFI.

These activities may proceed in parallel. Immediate response does not have to wait for every intelligence question to be answered. Which findings require escalation and who must be notified are matters for the organization's own procedures.

#### How the intelligence work branches

CTI evaluates the question, adds relevant context, and develops an answer. That work may identify related infrastructure or behaviors worth examining elsewhere.

| Finding or product | Recipient and intended result |
|---|---|
| Infrastructure supported for blocking consideration | The firewall / IA function evaluates a blocking change under local procedures. |
| An intelligence package with a question and searchable leads | Hunters search for relevant activity and report their findings and gaps. |
| That same package with useful detection opportunities | DE assesses whether existing detections meet the need and whether a rule should be written or tuned. |

Related infrastructure is initially a candidate to evaluate. Its relationship to a known indicator supplies a lead; the evidence and operational context determine whether a blocking recommendation is justified. The same infrastructure may also be useful in a hunt, depending on the question and available telemetry.

#### Naming the next handoff

When given a point in this workflow, describe the receiving role and the work it owns. For example, a hunt team receiving a package owns the search and the resulting findings. DE receiving that package owns the assessment of detection coverage and any resulting rule work. Depending on the environment, that work may involve Microsoft Defender for Endpoint (MDE) analytics or rule formats such as Sigma, YARA, and Suricata.

An effective handoff makes the requested outcome understandable. The course introduces that responsibility before teaching the detailed formats. Your site's processes determine where the request is recorded, who accepts it, and how the result is returned.

#### Knowledge Check

1. In the escalated course example, what can the analyst do after triage while CTI works on an RFI?
2. CTI has evidence supporting consideration of a domain block. Who receives that work, and what product does that function own?
3. The same intelligence package goes to Hunt and DE. What result should each produce?

#### Summary

A single alert can lead to response, notification, intelligence analysis, hunting, and detection work. Identify each handoff by its purpose and the product the receiving role owns. The example explains how the responsibilities connect while leaving local routing and approval procedures to the organization.

#### References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.

### 0.5 — Where the jobs lightly overlap

**Estimated Time:** 15–20 minutes

#### Why This Matters

Several analysts may examine the same host, log, or domain while working toward different outcomes. Understanding those outcomes helps you collaborate without losing track of who is responsible for the remaining work. In this lesson, a **product** means the result a role is expected to deliver.

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain how shared evidence can support different role-specific products.
2. Distinguish a handoff request from the work needed to complete it.
3. Explain why responsibilities remain distinct when one person performs several roles.

#### Shared evidence and different products

| Role | Product developed from the evidence |
|---|---|
| SOC analyst | A finding that supports closing or escalating an alert. |
| CTI analyst | An intelligence answer that explains the evidence's significance for a question. |
| Threat hunter | Search findings, their scope, and relevant gaps or limitations. |
| Detection engineer | A tested detection or a justified change to detection coverage. |

For example, a domain found in an alert may help SOC establish what the host contacted. CTI may examine the domain's role in the activity. A hunter may search for other hosts that contacted it, while DE considers whether the associated behavior warrants a detection. Each role can reuse the earlier evidence and reasoning while developing the product it owes.

#### What a request contributes

An RFI communicates a question and the context needed to begin answering it. The CTI analyst still has to evaluate the evidence and develop the answer. Similarly, an intelligence package can prepare a hunter to search, while the hunter still needs to execute the search and explain the results.

When passing work, be clear about what has already been established and what the recipient is being asked to do. This prevents a request from being mistaken for completed analysis and helps the receiving role build on work already done.

#### When one person fills several roles

In a smaller organization, the same person may investigate an alert and later perform intelligence or detection work. The responsibilities still matter because the purpose and completion criteria change as that person moves between tasks.

For example, documenting why an alert was escalated does not answer every intelligence question about the activity. The analyst can use the same evidence, but should make the additional question, reasoning, and result clear. Distinguishing the products helps others understand what is complete and what still needs attention.

#### Knowledge Check

1. SOC and CTI examine the same domain. How could their products differ?
2. What remains to be done when CTI receives an RFI?
3. Why distinguish roles when one person performs both alert investigation and hunting?

#### Summary

Collaboration works best when shared evidence is paired with clear responsibilities. A request prepares the next task, and each role develops a result suited to its purpose. Those distinctions remain useful when a single person performs several roles.

#### References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.

### 0.6 – Shared Analytical Frameworks: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Defenders need shared ways to describe behavior, relationships, and intrusion progression. These three frameworks provide common structures that will reappear later in the SOC, CTI, threat-hunting, and Detection Engineering tracks.

#### Connect to What You Already Know

Earlier shared-foundation lessons introduced the defensive roles and how work moves among them. This subunit gives those roles common ways to organize and communicate what they observe.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **0.6.1 – MITRE ATT&CK** | Recognize tactics and techniques as a shared vocabulary for adversary behavior. |
| **0.6.2 – Diamond Model** | Recognize Adversary, Capability, Infrastructure, and Victim as connected features of an intrusion event. |
| **0.6.3 – Cyber Kill Chain** | Recognize the seven stages as a way to discuss intrusion progression. |

#### What to Watch For

- Focus on the question each framework helps organize rather than trying to choose one framework for every problem.
- Keep the framework tied to the evidence; labels and boxes do not create facts that are not present.
- Treat incomplete information as normal. A useful model can remain partially unresolved.

#### Expected End State

By the end of this subunit, you should be able to:

- explain the basic purpose of ATT&CK, the Diamond Model, and the Cyber Kill Chain;
- describe the different question each framework helps organize;
- recognize that the same evidence can be viewed through more than one framework without becoming different evidence;
- preserve uncertainty instead of forcing a complete-looking model.

#### How to Preview This Subunit

Read this introduction, then skim the [0.6 Summary](#06--shared-analytical-frameworks-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 0.6.1 — MITRE ATT&CK

**Estimated Time:** 15–20 minutes

#### Why This Matters

ATT&CK gives analysts a shared vocabulary for describing adversary behavior. A useful mapping connects that vocabulary to evidence, so another analyst can understand why the label fits. This lesson introduces the matrix and shows how to support one mapping from an observed event.

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose and structure of ATT&CK.
2. Distinguish a tactic, technique, and sub-technique.
3. Map one observed behavior, cite the supporting evidence, and choose the better-supported mapping when two nearby ATT&CK labels appear plausible.

#### Reading the matrix

The [Enterprise ATT&CK matrix](https://attack.mitre.org/matrices/enterprise/) organizes behavior by tactics, techniques, and sub-techniques.

| Element | Meaning | Example |
|---|---|---|
| Tactic | The goal the behavior serves. | Execution |
| Technique | A way to achieve a goal. | T1059 — Command and Scripting Interpreter |
| Sub-technique | A more specific form of a technique. | T1059.001 — PowerShell |

Tactics appear as columns. Techniques and their sub-techniques describe behaviors within that structure. The matrix helps you find a relevant description; the description and your evidence determine whether a mapping is supported.

#### Building an evidence-supported mapping

Suppose a process event records `wscript.exe` starting `powershell.exe`, and the command-line field contains an encoded PowerShell command. The event supports **Execution / T1059.001 — PowerShell** because it shows the PowerShell interpreter being invoked to run commands. The parent process and command line provide the evidence to cite.

A short mapping could read: “Execution / T1059.001 — PowerShell; the process event shows `wscript.exe` launching `powershell.exe` with an encoded command.” Include the event reference or relevant fields in the actual record so the reader can check your reasoning.

The broader T1059 label describes the interpreter family. When the evidence identifies PowerShell, the sub-technique gives a more precise description.

#### Choosing between plausible mappings

Sometimes two ATT&CK labels can both seem reasonable at first glance. The useful question is not simply whether a label can be made to fit; it is which mapping best describes the observed behavior at the level of specificity the evidence supports.

Suppose a registry event shows `reg.exe` creating value `Updater` under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` and pointing it to `%TEMP%\update.exe`. Two labels may come to mind:

- **T1112 – Modify Registry** describes registry modification broadly.
- **T1547.001 – Registry Run Keys / Startup Folder** specifically describes use of a Run key for boot or logon autostart execution.

If you must choose the primary mapping for this event, **T1547.001** is better supported because the observed registry location is itself a Run key and the event records a value being configured there. T1112 describes the generic mechanism, but it is less specific to what this event shows.

If the event only showed an unspecified registry value being changed, without evidence that the key was a Run/Startup persistence location, **T1112** would be the safer mapping. The evidence determines how specific the mapping can be.

#### Keeping the conclusion within the evidence

This event alone does not establish Command and Control: it contains no evidence of communication with an external controller. That behavior might appear in another event and support an additional mapping. More than one mapping can be appropriate when each has evidence.

An ATT&CK label also does not establish that an event is malicious. Administrators use PowerShell for legitimate tasks. The mapping describes behavior; assessing its significance requires context such as the command, user, parent process, and surrounding activity.

#### Knowledge Check

1. How do a tactic, technique, and sub-technique differ?
2. A process event shows `wscript.exe` launching `powershell.exe` with an encoded command. Give a supported mapping, identify the evidence, and explain whether the same event establishes Command and Control or malicious intent.
3. A registry event shows `reg.exe` creating a value under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`. Between T1112 and T1547.001, which should be the primary mapping, and why? When would T1112 be the safer choice?

#### Summary

ATT&CK provides names for behavior. A useful mapping identifies the tactic and technique or sub-technique, cites the supporting evidence, and explains why the label fits. When two labels look plausible, choose the one whose specificity is best supported by the observed behavior, and keep additional conclusions tied to additional evidence.

#### References and Further Reading

- [MITRE ATT&CK — Enterprise matrix](https://attack.mitre.org/matrices/enterprise/) — Explore the matrix structure.
- [MITRE ATT&CK — PowerShell (T1059.001)](https://attack.mitre.org/techniques/T1059/001/) — Read the behavior description used in the example.
- [MITRE ATT&CK — Modify Registry (T1112)](https://attack.mitre.org/techniques/T1112/) — Compare the broader registry-modification behavior.
- [MITRE ATT&CK — Registry Run Keys / Startup Folder (T1547.001)](https://attack.mitre.org/techniques/T1547/001/) — Compare the more specific Run-key persistence behavior.

### 0.6.2 — Diamond Model

**Estimated Time:** 15 minutes

#### Why This Matters

The Diamond Model helps you organize what is known about an intrusion event and identify useful questions about what is missing. Its four vertices keep the activity, the systems involved, and the responsible party visible in one view.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe the four Diamond Model vertices.
2. Organize a simple event using the available evidence.
3. Identify the weakest-supported vertex and explain the evidence gap.

#### The four vertices

| Vertex | Question it helps answer |
|---|---|
| Adversary | Who is responsible for the activity? |
| Capability | What tools or techniques were used? |
| Infrastructure | What systems or services enabled the activity? |
| Victim | Who or what was targeted or affected? |

The model connects these elements within an event. For example, an adversary may use a capability through infrastructure against a victim. An investigation may begin with evidence for only some of those elements.

#### Organizing a small example

Suppose an endpoint event shows PowerShell running on a workstation, and a related network event records that process contacting a domain identified in the investigation as suspicious.

| Vertex | What can be recorded | Basis or limitation |
|---|---|---|
| Adversary | Unknown. | These events do not identify the responsible party. |
| Capability | PowerShell execution. | The endpoint process event records the interpreter. |
| Infrastructure | The contacted domain, provisionally associated with the activity. | The network event establishes contact; the domain's role still needs assessment. |
| Victim | The observed workstation. | The endpoint and network records identify the host. |

This organizes the observations without treating contact as proof that the domain is attacker-controlled. More evidence may refine the domain's role or the assessment of the event.

#### Using gaps to guide a question

The weakest-supported vertex highlights a gap in the available evidence. In this example, the adversary vertex is unknown. A vendor's actor label may suggest a lead, but evaluating attribution requires the evidence and reasoning behind that label.

The next question should also serve the investigation's purpose. If the immediate concern is whether other workstations contacted the domain, checking that exposure may be more useful than attempting attribution. The model helps you see gaps and choose a relevant question; it does not require every vertex to be completed before action can continue.

#### Knowledge Check

1. Name the four Diamond Model vertices and what each describes.
2. How would you organize the PowerShell and domain-contact example?
3. Which vertex is weakest in the example, and must it be resolved first?

#### Summary

The Diamond Model organizes an event around adversary, capability, infrastructure, and victim. Populate it from evidence, mark uncertainty, and use the gaps to develop questions that matter to the investigation.

#### References and Further Reading

- [Sergio Caltagirone — The Diamond Model](https://www.activeresponse.org/the-diamond-model/) — Author resource for the model introduced by Caltagirone, Pendergast, and Betz in 2013.

### 0.6.3 — Cyber Kill Chain

**Estimated Time:** 15 minutes

#### Why This Matters

The Cyber Kill Chain provides a way to discuss progression through an intrusion. It helps analysts place an observed event in a larger sequence and consider where defensive action could interrupt that sequence. The available evidence may show only part of the activity.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe the purpose and seven stages of the Cyber Kill Chain.
2. Assign a stage to a simple observed event and explain the evidence.
3. Distinguish observed progression from unestablished activity.

#### The seven stages

| Stage | What it describes |
|---|---|
| Reconnaissance | Gathering information about a target. |
| Weaponization | Preparing a malicious payload or delivery package. |
| Delivery | Transmitting the malicious material to the target. |
| Exploitation | Exploiting a vulnerability to enable the attack. |
| Installation | Establishing a malicious implant or foothold. |
| Command and Control | Communicating with infrastructure used to direct the compromised system. |
| Actions on Objectives | Carrying out the attacker's intended outcome. |

The sequence is a model for reasoning about an intrusion. Real activity can repeat stages, take different paths, or leave stages unobserved. Use the model to explain what the evidence shows while keeping those limits visible.

#### Placing an observed event

> **Scenario status: Separate classroom example — not A12.**

Suppose an email record shows that a message containing `shipping-notice.js` was delivered to a mailbox. For this example, separate analysis has established that the attachment is malicious. The email record supports **Delivery** because it shows the malicious material reaching the target.

The record does not show how the attachment was prepared, whether anyone opened it, or whether it established a foothold. Those are questions for other evidence. The `.js` extension alone would not establish maliciousness; the example's stated analysis supplies that context.

#### Explaining a stage assignment

A useful stage assignment includes the stage, the event supporting it, and any uncertainty that affects interpretation. For example: “Delivery: the email record shows the malicious attachment reached the mailbox; execution has not been established.”

ATT&CK, the Diamond Model, and the Cyber Kill Chain answer different questions. ATT&CK names behavior, the Diamond Model organizes the elements of an event, and the Kill Chain describes progression. Together they help analysts explain activity without requiring every observation to prove an entire intrusion.

#### Knowledge Check

1. Name the seven Cyber Kill Chain stages and explain what the model helps analysts describe.
2. An email record confirms delivery of an attachment established as malicious. Which stage is supported, and why?
3. Does that delivery record establish exploitation or installation? What would you say in the finding?

#### Summary

The Cyber Kill Chain describes intrusion progression in seven stages. Assign a stage from the observed event, explain the supporting evidence, and leave unobserved activity open for investigation.

#### References and Further Reading

- [Lockheed Martin — Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — Original model and supporting resources.

### 0.6 – Shared Analytical Frameworks: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Behavior → relationships → progression**. ATT&CK emphasizes behavior, the Diamond Model emphasizes relationships, and the Cyber Kill Chain emphasizes progression.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- explain the basic purpose of ATT&CK, the Diamond Model, and the Cyber Kill Chain;
- describe the different question each framework helps organize;
- recognize that the same evidence can be viewed through more than one framework without becoming different evidence;
- preserve uncertainty instead of forcing a complete-looking model.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **0.6.1 – MITRE ATT&CK** | Recognize tactics and techniques as a shared vocabulary for adversary behavior. |
| **0.6.2 – Diamond Model** | Recognize Adversary, Capability, Infrastructure, and Victim as connected features of an intrusion event. |
| **0.6.3 – Cyber Kill Chain** | Recognize the seven stages as a way to discuss intrusion progression. |

#### Check Your Understanding

Ask yourself:

1. Which framework would you reach for first if your question is primarily about adversary behavior?
2. How can the Diamond Model remain useful when one of its core features is unknown?
3. Why can the same observation appear in more than one framework without becoming independent evidence?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **0.7 – External Tools**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 0.7 — External tools

**Estimated Time:** 20 minutes

#### Why This Matters

External analysis services can help answer questions about files, domains, IP addresses, and web pages. Choosing a useful service starts with the question you need to answer and the input you have. Their capabilities overlap, and results still need interpretation in the context of the investigation.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe the questions VirusTotal, ANY.RUN, Silent Push, and urlscan.io can help answer.
2. Choose a suitable service and input for a simple investigation question.
3. Explain a relevant interpretation limit and distinguish a lookup from a new submission.

#### Matching the tool to the question

| Service | Useful starting question | Typical contribution |
|---|---|---|
| VirusTotal | What is already known about this file or indicator? | Reputation results, existing analyses, relationships, and passive DNS information where available. |
| ANY.RUN | What does this file or URL do in an interactive analysis environment? | Observed process, file, and network activity from an execution or browsing session. |
| Silent Push | What DNS history and infrastructure relationships can help investigate this domain or IP address? | DNS records, historical observations, and infrastructure pivots. |
| urlscan.io | What does this web page load or redirect to in a browser visit? | Requests, redirects, contacted hosts, and a screenshot from the scan. |

Use the input and available workflow to refine the choice. A file hash can locate an existing report, but a new sandbox execution requires an actual file or another supported input such as a URL. A URL analysis and a DNS-history lookup answer different questions even when both involve the same domain. Access to particular results or features can depend on the service and account.

#### Interpreting what comes back

Suppose a suspicious email links to a website. A reputation lookup can supply existing context. A browser scan may show that the page redirects to another host, while DNS history may reveal earlier infrastructure. Each result adds evidence about a different part of the question.

A detection count is a set of vendor assessments, not a final verdict. No detections may reflect limited knowledge rather than safety. A sandbox run records behavior under the conditions of that run; timing, interaction, or evasion may affect what appears. DNS relationships can reveal leads, but shared hosting does not establish common ownership or a common adversary. A browser scan captures a particular visit, and the page may behave differently for another user or at another time.

In your finding, state what the service observed and how it contributes to your question. Preserve the report reference and relevant time so another analyst can assess the result.

#### Choosing a suitable lookup or submission

Searching for an existing report and submitting new material are different actions. Before uploading a file or submitting a URL, follow the organization's approved process and check the workflow's visibility settings. Files can contain sensitive information, and URLs can include credentials, tokens, or internal names.

Visibility differs by service and mode. VirusTotal offers a separate private-scanning workflow; standard submissions should not be assumed private. urlscan.io distinguishes public, unlisted, and private scans, and unlisted scans remain accessible to certain vetted users. Confirm the current service documentation and your approved configuration when handling organizational material.

The appropriate choice combines the analytical question, the available input, and permission to use the service in that way.

#### Knowledge Check

1. You need to see the redirects and resources loaded during a browser visit. Which service is a suitable starting point, and why?
2. You have only a file hash. Can you run a new file execution in a sandbox from that alone?
3. A domain has no detections and shares an IP address with a malicious domain. What can you conclude, and what should you check before submitting its URL?

#### Summary

Choose an external service by the question, input, and available capability. Interpret results as evidence with limits, preserve their context, and use an approved submission workflow when providing new material.

#### References and Further Reading

- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching) — Existing reports, relationships, and passive DNS searches.
- [VirusTotal — Private scanning](https://docs.virustotal.com/docs/private-scanning) — Separate private-scanning workflow.
- [ANY.RUN — Features](https://any.run/features/) — Interactive analysis capabilities and supported inputs.
- [Silent Push — Passive DNS lookups](https://help.silentpush.com/docs/perform-passive-dns-scans-and-record-specific-lookups) — DNS history and record-specific investigation.
- [urlscan.io — FAQ](https://urlscan.io/docs/faq/) — Scan behavior and visibility options.

### 0.8 — Environment / signal flow

**Estimated Time:** 15–20 minutes

#### Why This Matters

An event becomes easier to interpret when you understand where it occurred and how activity normally moves through the organization. Environment orientation connects a host or account to its role, its access paths, and the evidence available along those paths.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe the seven environment areas used for orientation.
2. Identify which areas are relevant to a simple investigation question.
3. Distinguish the environment area relevant to a question from a related area, including traffic paths versus sensor coverage.

#### Building a useful environment picture

| Area | What to establish | Why it matters |
|---|---|---|
| Egress | How systems reach external networks, including proxies and other gateways. | Helps locate outbound activity and the controls it crosses. |
| Segments and data flow | Major network or workload boundaries and expected paths between them. | Helps distinguish expected communication from activity needing explanation. |
| Email | How messages enter, are processed, and reach users. | Helps locate delivery evidence and relevant email controls. |
| Edge firewalls and chokepoints | Where traffic is filtered or concentrated. | Identifies useful control and observation points. |
| Third-party access and federation | How external organizations or identities receive access and what that access permits. | Helps explain access paths and responsibility for relevant records. |
| Crown jewels | Systems, services, or information whose loss would have high impact. | Helps prioritize investigation according to organizational consequence. |
| PCAP and sensors | Where packet capture or other sensors exist and what they actually retain. | Establishes which activity may be observable and at what detail. |

These categories organize questions for the local environment. Use maintained diagrams, service documentation, and system owners to establish the actual design. The fictional course setting does not supply a complete production architecture.

#### Tracing an event through the environment

Suppose an alert reports that a workstation contacted an external domain. Begin by establishing the workstation's segment and the expected egress path. Then identify the relevant gateway or proxy and ask what records are available for the time in question. If packet capture is needed, confirm whether a sensor covered that path and retained the traffic.

This sequence separates three questions: where traffic could travel, where it could be observed, and what evidence is actually available. A diagram may show a gateway even when its logs were not enabled or retained. A sensor may cover one segment without seeing another.

#### Recording useful gaps and next questions

If the expected evidence is missing, record the visibility gap and identify the owner or documentation needed to resolve it. An absence of logs does not establish that the activity did not occur. It may reflect routing, collection, access, or retention limits.

Also connect the affected system to its purpose and importance. A third-party account accessing a critical service raises questions about the authorized access method, scope, and responsible owner. Understanding those relationships helps you ask a focused question and choose an appropriate next step.

#### Knowledge Check

1. Which environment areas would help you investigate a workstation contacting an external domain?
2. You know the expected egress path but need to determine whether packet-level evidence exists. Which environment area should you check, and how does it differ from egress?
3. How do third-party access and crown jewels help orient an investigation?

#### Summary

Environment orientation helps you connect an event to expected paths, organizational importance, and available evidence. Use the seven areas to ask focused questions, verify the actual environment, and make visibility gaps clear.

#### References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — Further reading on organizing SOC responsibilities and understanding the environment. The course workflow is an instructional example, not a mandated organizational design.

### 0.9 — Common Initial Access Paths

**Estimated Time:** 25–35 minutes

#### Why This Matters

Module 0.8 gave you the terrain: email paths, Internet-facing systems, remote access, third-party trust, network routes, and the places evidence may be collected. Initial access asks a different question: **how might an adversary first gain, or try to gain, a foothold through that terrain?**

The useful skill is separating an **entry-path hypothesis** from evidence that the path actually succeeded; memorizing attack names is secondary to that reasoning. A phishing message can be delivered without being opened. A vulnerable web server can receive exploit traffic without being compromised. A successful VPN login proves that an account was used, but it does not by itself prove the user was an adversary.

As you read, predict what evidence would move each example from *possible path* to *supported initial access*. The course principle still applies: **Describe what the evidence shows first. Then decide what it means.**

#### Learning Objectives

By the end of this module, you will be able to:

1. Recognize common initial-access paths and connect them to the environment areas introduced in 0.8.
2. Distinguish exposure or delivery from an access attempt, successful access, and later execution.
3. Given a short scenario, identify the most defensible initial-access path—or leave it unresolved—and name the next evidence that would test the hypothesis.

#### Initial access is an objective, not a verdict

MITRE ATT&CK uses **Initial Access** for techniques adversaries use to gain their first foothold in an environment. The tactic includes paths such as phishing, drive-by compromise, exploitation of public-facing applications, valid accounts, external remote services, trusted relationships, and supply-chain compromise.

That vocabulary helps describe *how access could occur*. It does not remove the need to prove what happened in the case in front of you. The same observation can sit at different points in the evidence progression:

**Exposure or delivery → interaction / access attempt → successful access → later execution or follow-on behavior**

For example, a malicious attachment in a mailbox establishes delivery. A process event showing the attachment launching code establishes something later in the chain. The first observation should not be rewritten as the second merely because the analyst expects one to lead to the other.

ATT&CK and the Cyber Kill Chain may both help describe the same incident from different angles. ATT&CK Initial Access names adversary entry techniques. The Kill Chain asks about progression such as Delivery and Exploitation. Use the framework that answers the question you are asking and keep the underlying observations visible.

#### Common entry paths

| Entry-path family | What it can look like | Evidence that may support it | Important boundary |
|---|---|---|---|
| **Phishing / malspam** | Attachment, link, or message delivered through email or another service | Message headers, gateway records, attachment/link metadata, click/open records, endpoint process/file evidence | Delivery does not prove the user opened it, code ran, or access succeeded. |
| **Public-facing exploitation** | Exploit attempt against an Internet-facing application, API, appliance, or service | WAF/app/service logs, exploit request, error/response patterns, vulnerable version context, resulting process/session/file changes | A CVE or vulnerable version establishes exposure; an exploit request establishes an attempt; neither alone proves compromise. |
| **Drive-by / watering hole / malicious web path** | User visits adversary-controlled or compromised web content; malvertising or search/SEO poisoning may steer the user there | Browser/proxy/DNS/HTTP records, redirect chain, downloaded content, exploit response, endpoint browser-child processes or files | A visit or redirect does not prove exploitation. SEO poisoning or malvertising often explains how the user was steered; map the actual access behavior supported by evidence. |
| **Valid account / external remote service** | VPN, webmail, cloud, remote desktop, Citrix, SSH, or another externally reachable service is used with an account | Authentication logs, MFA events, device/source context, session creation, remote-service records, authorization/context from the account owner | A successful login proves account use. It does not by itself establish that the account was stolen or the session was malicious. |
| **Trusted relationship / supply chain** | Third-party access, trusted identity, dependency, software update, or delivery mechanism is abused | Third-party/session records, software/update provenance, build/dependency evidence, package history, affected-version context | The existence of a trust path or dependency is exposure context. Evidence must connect that path to the actual intrusion. |

These families are a practical map rather than an exhaustive catalog. Real incidents can combine them. A phishing link can send a user to a malicious website; a compromised vendor account can use an external remote service; a watering-hole page can exploit a browser vulnerability. When paths overlap, describe each observed step rather than forcing the incident into one label too early.

#### Match the question to the evidence source

Module 0.8 introduced where activity may travel and where evidence may exist. Initial-access reasoning turns that orientation into a collection question.

| Hypothesis | Useful evidence sources |
|---|---|
| Phishing or malspam delivered the first artifact | Mail/security gateway, message trace, mailbox metadata, URL/attachment handling, endpoint file/process evidence |
| Internet-facing exploitation provided access | Public-facing application/service logs, WAF/reverse proxy, authentication/session records, process/file activity on the server, vulnerability/patch context |
| A web path led to client compromise | Proxy/DNS/HTTP, browser history where authorized, redirect/download records, endpoint process/file activity |
| A valid account or remote service was used | Identity provider, VPN/remote service, MFA, device/source context, account-owner validation, resulting session activity |
| A trusted third party or supply chain was involved | Third-party identity/session records, software/update/dependency provenance, vendor reporting, local installation/execution evidence |

The next source should answer the uncertainty you actually have. If you already know a message was delivered, another copy of the mail header may add little. The next useful question may be whether the user interacted with the message or whether an endpoint process followed it.

#### Work from evidence strength

A useful initial-access statement has four parts:

1. **Observation:** what the source actually recorded.
2. **Reasoning:** why that observation supports one path more than another.
3. **Bounded conclusion:** the strongest claim the evidence supports now.
4. **Next test:** the evidence that would strengthen, reject, or replace the hypothesis.

> **Scenario status: Separate classroom example — not A12.**

Example:

> The mail gateway recorded delivery of a message containing `shipping-notice.js` to the user. This supports phishing or malspam as a possible delivery path. The record does not establish that the attachment was opened or executed. Check endpoint file/process evidence and user-interaction telemetry for the message time before concluding that phishing produced host activity.

Another example:

> The VPN recorded a successful login for a valid employee account from an unfamiliar source. This establishes that the account authenticated through the remote service. Whether the session represents adversary access remains unresolved until authorization, MFA/device context, and resulting session activity are checked.

The bounded conclusion is useful because it tells the next analyst both what is known and what work remains.

#### A12: keep the entry path unresolved

At this point in the course, A12 is used to establish one shared-foundation fact: **suspicious activity will later be investigated on WS-JLEE, but the entry path is not known**.

Detailed A12 process, network, and registry observations are intentionally introduced later in the SOC track. Nothing available in the shared-foundation view establishes phishing, a malicious web path, public-facing exploitation, valid-account or remote-service abuse, or a trusted-third-party/supply-chain path.

The canonical case supplies no mail record tying the activity to phishing, no browser chain proving a drive-by path, no public-facing exploitation record, no authentication record establishing account-based entry, and no third-party or supply-chain evidence connecting those paths to A12.

So the defensible initial-access conclusion is:

> **A12 initial access remains unresolved.**

Leaving the path unresolved is the analytical answer supported by the current evidence. If reconstructing the entry path became important, the analyst would choose the next source based on the hypotheses being tested—for example mail/message records, browser/proxy history, identity/remote-access logs, or other case-relevant evidence.

#### Knowledge Check

1. A mail gateway shows a malicious attachment was delivered, but you have no endpoint evidence yet. What initial-access conclusion can you support, and what remains unproven?
2. An Internet-facing application is vulnerable to a CVE and receives a request matching a published exploit pattern. What additional evidence would you want before concluding the exploit provided access?
3. For A12, no canonical mail, browser, public-facing exploit, authentication, or third-party record establishes how access began. What is the correct conclusion, and what evidence would you seek next?

#### By This Point, You Should Be Able To…

You should now be able to recognize the major initial-access families, connect them to likely evidence sources, and place an observation at the correct point in the evidence progression. Most importantly, you should be comfortable leaving the entry path unresolved when the available evidence does not establish it, while still naming the next evidence that would make the hypothesis testable.

#### References and Further Reading

- [MITRE ATT&CK — Initial Access (TA0001)](https://attack.mitre.org/tactics/TA0001/)
- [CISA — #StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — Includes common initial-access vectors and advanced social-engineering examples such as SEO/search poisoning.
- [MITRE ATT&CK — Phishing (T1566)](https://attack.mitre.org/techniques/T1566/)
- [MITRE ATT&CK — Drive-by Compromise (T1189)](https://attack.mitre.org/techniques/T1189/)
- [MITRE ATT&CK — Exploit Public-Facing Application (T1190)](https://attack.mitre.org/techniques/T1190/)
- [MITRE ATT&CK — Valid Accounts (T1078)](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK — External Remote Services (T1133)](https://attack.mitre.org/techniques/T1133/)
- [MITRE ATT&CK — Trusted Relationship (T1199)](https://attack.mitre.org/techniques/T1199/)
- [MITRE ATT&CK — Supply Chain Compromise (T1195)](https://attack.mitre.org/techniques/T1195/)

### 0.10 — Shared Foundations Section Summary

**Estimated Time:** 15–20 minutes  

#### Purpose

The 0.x block gave every learner the same foundation before the role-specific tracks begin.

You learned:

- how the course is organized;
- what a SOC is;
- what the major defensive roles produce;
- how work can move between those roles;
- where responsibilities overlap;
- how ATT&CK, the Diamond Model, and the Cyber Kill Chain help organize activity;
- what external research tools can and cannot tell you;
- how the local environment and signal flow affect what evidence is available;
- how common initial-access paths differ and how to keep delivery, access attempts, successful access, and later execution separate.

This summary reconnects those topics before you begin 1.x.

A simple way to remember the 0.x block is:

**Course map → Roles → Handoffs → Frameworks → Tools → Environment → Initial Access**

These foundations support every later track.

#### What You Can Now Do

You should now be able to:

- explain how the course progresses from shared foundations into SOC, CTI, hunting, and Detection Engineering;
- describe the purpose of a SOC without reducing it to one tool or queue;
- state the primary product expected from each defensive role;
- identify a reasonable next handoff when one role reaches the limit of its current task;
- explain why two roles can examine the same evidence while producing different outputs;
- use ATT&CK, the Diamond Model, and the Cyber Kill Chain for different analytic purposes;
- treat external platform results as evidence or leads rather than automatic truth;
- describe major environment paths and recognize that traffic path, collection point, and actual visibility are different concepts.

The goal is shared language.

Later tracks will add depth.

#### The 0.x Block at a Glance

| Unit | Core idea retained |
|---|---|
| **0.1 – Course Layout** | Understand the teaching sequence and why shared foundations come first. |
| **0.2 – What a SOC Is** | Understand the SOC as a defensive function that receives, investigates, coordinates, and communicates security work. |
| **0.3 – Jobs in One Sentence** | Recognize the primary purpose and product of SOC, CTI, hunting, and Detection Engineering roles. |
| **0.4 – How Work Can Move** | Follow a piece of defensive work from one role to another when the question changes. |
| **0.5 – Where Jobs Overlap** | Understand that several roles may inspect the same evidence while producing different products. |
| **0.6 – Frameworks** | Use ATT&CK, the Diamond Model, and the Cyber Kill Chain as different ways to organize what you know. |
| **0.7 – External Tools** | Understand the broad capabilities and limits of public/external research platforms. |
| **0.8 – Environment / Signal Flow** | Relate hosts, users, network paths, critical assets, access paths, and sensors to the evidence you can actually observe. |
| **0.9 – Common Initial Access Paths** | Identify the most defensible entry-path hypothesis from evidence, preserve uncertainty, and name what would test it. |

#### One A12 Story Across the Shared Foundations

The A12 scenario can show why the 0.x material matters before any role-specific lesson begins.

Suppose the SOC receives an alert involving `WS-JLEE`.

At this point in the course, the shared foundations intentionally keep the case spoiler-light:

- suspicious activity involving `WS-JLEE` will enter the SOC track;
- A12's initial-access mechanism remains unresolved;
- the detailed process, network, and registry observations are introduced later in 1.x when learners are expected to interpret them.

Several defensive roles may eventually become involved as new evidence and questions emerge.

##### SOC

The SOC asks:

> What happened on this system, how serious is it, and what needs to happen now?

Its product may be:
- an investigated alert;
- an incident record;
- an escalation;
- an RFI to another team.

##### CTI

CTI may ask:

> What is known about the infrastructure, behavior, malware, campaign, or threat activity connected to this case?

Its product is an assessed intelligence answer or package—not simply a list of search results.

##### Threat Hunting

Hunting may ask:

> Does this same or related behavior exist elsewhere in the environment?

Its product is a bounded hunt result, including findings, limitations, and follow-on gaps.

##### Detection Engineering

Detection Engineering may ask:

> Should this behavior become maintained automatic coverage, and if so, how?

Its product is maintained detection capability rather than only a query.

The same A12 evidence can appear in all four workflows.

The **question and product** are what change.

#### Follow the Question When Work Moves

A handoff should happen because the next question belongs to another function—not merely because another team exists.

For example:

> **Scenario status: Separate classroom example — not A12.**

> SOC investigates suspicious activity and asks whether external infrastructure is known.

That becomes an intelligence question.

> CTI identifies a distinctive procedure and asks whether it appears elsewhere internally.

That can become a hunt lead.

> Hunting finds the procedure on additional hosts and discovers that no analytic covers it.

That can become Detection Engineering work.

> Detection Engineering deploys a validated analytic.

Future activity may generate a SOC alert.

This generic workflow shows how the work can become a loop without asserting that those downstream outcomes occurred in A12.

The course teaches the roles separately so you can understand their responsibilities, but real defensive work often moves back and forth.

#### Same Evidence, Different Product

This is one of the most important ideas from 0.x.

A domain such as `example-update.test` might appear in:

- a SOC case;
- a CTI infrastructure assessment;
- a hunt query;
- a detection rule.

That does not make the four products interchangeable.

Similarly, one analyst may wear two roles.

The analyst still needs to know which product they are producing at that moment.

A useful question is:

> **What decision or downstream action is this product supposed to support?**

That often tells you which role's work you are doing.

#### Keep the Frameworks Distinct

The frameworks introduced in 0.6 help organize different kinds of reasoning.

##### MITRE ATT&CK

ATT&CK helps describe **adversary behavior**.

Ask:

> What behavior or technique does the evidence support?

##### Diamond Model

The Diamond Model helps organize relationships among:

- adversary;
- capability;
- infrastructure;
- victim.

Ask:

> Which vertices are supported, and what relationships can we investigate?

An incomplete diamond is still useful. Missing information should remain missing until evidence supports it.

##### Cyber Kill Chain

The Cyber Kill Chain helps reason about **progression through an intrusion**.

Ask:

> Which stage does the available evidence support?

Leave stages unfilled when the evidence does not support them.

##### One event can support more than one framework view

The frameworks are not competing answers.

They organize the same evidence for different analytic purposes.

#### External Tools Provide Evidence, Not Authority

External research platforms can help with:

- file relationships;
- sandbox behavior;
- passive DNS;
- infrastructure context;
- URL or web observations;
- reputation and prior reporting.

But a platform result should still be interpreted.

Examples:

> A sandbox observed a process behavior.

This means the behavior was observed in that sandbox execution.

Interpret it as evidence from that sandbox execution; separate confirmation is needed before applying the behavior to every copy or to the local environment.

> Passive DNS shows a historical domain-to-IP relationship.

This provides historical infrastructure context.

It does not by itself prove common ownership or malicious operation.

> A vendor labels infrastructure as malicious.

That is a source claim to evaluate, not a substitute for analysis.

Later CTI and hunt lessons will develop these distinctions in more depth.

#### How Network Paths, Collection Points, and Visibility Relate

Module 0.8 introduced the environment because evidence depends on both **where activity travels** and **where the organization can observe it**. Those are related questions, but they are not the same question.

**Traffic path** describes where activity moves through the environment.

**Collection point** describes where a sensor or log source has an opportunity to observe part of that activity.

**Visibility** describes what evidence is actually collected, retained, parsed, and available to the analyst.

A connection may cross a network segment without a sensor recording the detail you need. A sensor may be present but lack the relevant field, and an important host may sit outside a particular telemetry population. When an investigation reaches an evidence gap, trace these three layers before deciding what the absence means.

This relationship becomes increasingly important in SOC investigation, threat hunting, and Detection Engineering.

#### Concepts That Stay Distinct as the Course Progresses

The shared foundations introduced several ideas that will appear repeatedly in later tracks. Keeping their purposes clear will make the more technical material easier to organize.

##### A defensive role is defined by its purpose and product

A SOC may rely heavily on a SIEM, CTI may rely on a TIP, hunting may use a query language, and Detection Engineering may author Sigma rules. Those tools support the work; they do not define the role.

When you are unsure which role's work you are doing, ask what question you are answering and what product or decision the work is meant to support.

##### Shared evidence can support different responsibilities

Two roles may inspect the same process event, domain, or network record while answering different questions. Shared access to the evidence does not make the products interchangeable.

The useful distinction is ownership of the **question, judgment, and downstream action**.

##### A handoff changes who is best positioned to answer the next question

Passing a bounded question to another function does not mean the original team stops caring about the case. It means the work has reached a question that another role is better equipped to answer.

A good handoff preserves the evidence, the reasoning already completed, the uncertainty, and the decision the receiving team needs to make.

##### Frameworks organize evidence; they do not supply missing facts

ATT&CK, the Diamond Model, and the Cyber Kill Chain give analysts useful structures for behavior, relationships, and progression. Their labels become meaningful only when the underlying evidence supports them.

An incomplete framework view is acceptable when the evidence is incomplete.

##### External research creates leads and context that still need local confirmation

A sandbox result, passive-DNS relationship, reputation score, or vendor assessment can sharpen an investigation. It describes what that source observed or assessed.

Whether the same activity occurred in the organization's environment still depends on local evidence.

##### Network topology tells you where traffic could be observed; telemetry tells you what was actually visible

Knowing that traffic traversed a device or segment does not guarantee that the required evidence was collected there. Visibility depends on sensor placement, configuration, retention, parsing, and population coverage.

This is why later lessons treat a missing observation as an evidence question rather than immediately treating it as proof that the activity did not occur.

#### Integrated Review Exercise

Use this spoiler-light A12 starting card:

> **Host:** `WS-JLEE`  
> **Known:** suspicious activity will be investigated in 1.x; the initial-access mechanism is unresolved  
> **Deferred:** detailed process, network, and registry observations are introduced later in the SOC track

For each item below, state the most appropriate role or concept.

##### Immediate host/case investigation
Who owns the first operational investigation?

##### External infrastructure question
If later evidence introduces an external domain or IP that needs threat context, which function should assess it?

##### Enterprise-wide search
If later evidence produces a supported behavior or infrastructure lead, which function should search for related activity elsewhere?

##### Durable analytic coverage
If later evidence identifies reusable behavior that may need maintained coverage, which function should evaluate it?

##### Behavior framework
Which framework is best suited to naming the adversary behavior?

##### Relationship framework
Which framework helps organize adversary, capability, infrastructure, and victim relationships?

##### Intrusion progression
Which framework helps reason about stages of an intrusion?

##### External platform result
What should you call it before internal evidence confirms local occurrence?

##### Initial-access path
The A12 evidence begins with suspicious host activity, but the course supplies no mail, browser, public-facing exploit, authentication, or third-party record proving how access began. What is the correct initial-access conclusion, and what evidence would you seek next?

##### Missing sensor coverage
Why can the existence of a network path not prove you had visibility into the activity?

A strong answer should explain **why**, not only name the role or framework.

#### Shared-Foundations Readiness Checklist

Before beginning 1.x, you should be comfortable saying:

- [ ] I understand the course sequence and the purpose of each major role track.
- [ ] I can explain what a SOC does at a high level.
- [ ] I can distinguish the primary products of SOC, CTI, hunting, and Detection Engineering.
- [ ] I can identify when a question should become a handoff.
- [ ] I understand that the same evidence can support different role-specific products.
- [ ] I can explain the different purposes of ATT&CK, Diamond, and Kill Chain.
- [ ] I can preserve uncertainty when a framework element is unsupported.
- [ ] I treat external-tool results as evidence or leads that require interpretation.
- [ ] I can distinguish network/data flow from actual sensor visibility.
- [ ] I can identify a defensible initial-access hypothesis from evidence and leave the path unresolved when the evidence does not establish it.
- [ ] I understand that later lessons will deepen these concepts rather than replace them.

If one of these is weak, revisit the corresponding 0.x module.

#### Bridge Into 1.x SOC

The shared foundation is now complete.

The course next narrows from:

> **How does defensive work fit together?**

to:

> **What does the evidence actually show?**

The SOC track begins with the observations closest to daily alert investigation:

- endpoint activity;
- network activity;
- detection logic;
- alert investigation;
- reporting and handoff.

The shared role, framework, tool, and environment concepts from 0.x remain in the background throughout that work.

#### Summary

The 0.x block created the common language used by every later role:

**Course map → Roles → Handoffs → Frameworks → Tools → Environment → Initial Access**

The most important idea to carry forward is:

> **Follow the evidence, know which question you are answering, and know which product the next defender needs.**

## Part II — SOC Analyst

The shared foundations now become an investigation. Read endpoint and network records closely, work out what an alert actually detected, and communicate a finding another analyst can use. Keep the observation separate from the conclusion as the evidence develops.

> **A12 Case Study:** Follow the evidence available at this stage of the case. The uninterrupted narrative appears in [Appendix A](#appendix-a--the-complete-a12-case-study).

### 1.0 — SOC Analyst Fundamentals: How the 1.x Block Fits Together

**Estimated Time:** 10–15 minutes  

#### Learning Objectives

By the end of this introduction, you will be able to:

1. Explain the purpose of the 1.x SOC block and how its five units fit together.
2. Follow the basic SOC evidence flow from an observation to an alert decision and a handoff.
3. Recognize what each unit is responsible for teaching before you begin the detailed lessons.

#### What the SOC Block Is Building Toward

The SOC analyst's job begins with **evidence**.

A host runs a process. A file appears. A workstation connects to an address. A network sensor records a request. A detection fires because some part of that activity matched logic someone wrote.

The analyst's job is to turn those separate observations into a defensible answer:

> **What happened, what does the evidence support, and what should happen next?**

The 1.x block teaches that process in layers.

You will start by learning how to read the evidence itself. Then you will learn how detections describe what they are looking for. After that, you will investigate alerts, classify what the detection did, and turn the result into a report or handoff another team can use.

A simple mental model is:

**Observe → Detect → Investigate → Communicate**

#### The Five Units

| Unit | Main question | What you learn |
|---|---|---|
| **1.1 – Endpoint** | What happened on the host? | Process, file, host-network, registry, and image/driver activity |
| **1.2 – Zeek** | What happened on the wire? | Connections, DNS, TLS, HTTP, SMTP, files, and protocol anomalies |
| **1.3 – Detection** | What activity was the detection logic designed to match? | Sigma, Suricata, YARA, and SIEM rule fundamentals |
| **1.4 – Alerts** | What does this alert mean after we investigate it? | Context, classification, false-positive causes, categorization, and response-time goals |
| **1.5 – Reporting** | How does the result leave the SOC? | Report type, reporting timelines, notification, and distribution |

Each unit answers a different question. Together they form one workflow.

#### Start With the Evidence

The most important habit in this block is to separate **what the sensor recorded** from **what you conclude from it**.

For example:

> **Scenario status: Separate classroom example — not A12.**

- Endpoint telemetry may show a script interpreter launching PowerShell.
- Network telemetry may show the same workstation making an HTTP request.
- A detection may alert on one of those patterns.

Those observations can support an investigation, but each source tells you something different.

The endpoint event can tell you **which process** acted.

The network event can tell you **what crossed the wire**.

The detection tells you **which pattern matched**.

The analyst combines those pieces without making any one source say more than it actually recorded.

That evidence discipline will repeat throughout the course.

#### One Activity, Several Views

The classroom A12 scenario is intentionally reused across the 1.x block, but its detailed evidence is revealed progressively.

At this orientation point, keep only the case frame:

1. Suspicious activity involving `WS-JLEE` enters the SOC track.
2. 1.1 will introduce the relevant host observations.
3. 1.2 will add network observations.
4. 1.3 will show how detection logic describes what it is designed to match.
5. 1.4 will investigate and assess the resulting alert context.
6. 1.5 will turn the supported result into a usable report or handoff.

Do not fill in later A12 process, network, or registry facts before the lesson that introduces them. Different lessons will revisit the same case from different viewpoints as the evidence becomes available.

##### In 1.1

You may ask:

> Which process ran?  
> Which file was created?  
> Which process opened the network connection?

##### In 1.2

You may ask:

> Which host initiated the connection?  
> What DNS name was requested?  
> What URI appeared in HTTP?  
> Was a file observed on the wire?

##### In 1.3

You may ask:

> What exactly would this rule match?  
> Which fields or byte patterns make the rule fire?

##### In 1.4

You may ask:

> What context is still missing?  
> Was the detection correct?  
> If it was noisy, why?  
> What kind of activity was this?

##### In 1.5

You may ask:

> Is this an incident report or a request for information?  
> When is it due?  
> Who receives it, and through which approved path?

The incident has not changed. The **question** has.

#### Host Evidence and Network Evidence Complement Each Other

Two evidence sources appear repeatedly in 1.x:

**Endpoint telemetry** sees activity from the host's point of view.

It can often tell you:
- which process ran;
- which user context was involved;
- which process created a file;
- which process initiated a network connection.

**Network telemetry** sees activity from the wire's point of view.

It can often tell you:
- which addresses communicated;
- which DNS name was requested;
- which HTTP method or URI appeared;
- which TLS properties were visible;
- which file or protocol artifact crossed the monitored connection.

Neither view is automatically better. They answer different questions.

A strong investigation uses the source that can actually support the statement you need to make.

#### Detections Are Leads Into Evidence

A detection alert is not the entire investigation.

A rule says:

> **This pattern matched.**

The analyst still needs to determine:
- what the underlying events show;
- what context is missing;
- whether the activity is actually the behavior the rule was intended to identify;
- whether the result should be escalated, closed, tuned, or handed to another team.

That is why the course teaches raw evidence before alert classification.

You should understand the event before deciding what the alert means.

#### The SOC Produces a Usable Handoff

The final SOC product is not simply “I looked at the alert.”

Someone else may need the result:
- incident response;
- CTI;
- threat hunting;
- detection engineering;
- a local operational or leadership customer.

A useful SOC handoff preserves:
- the important observations;
- the analyst's conclusion;
- the evidence that supports it;
- important gaps or uncertainty;
- the question or action the next team needs to address.

The 1.x block therefore ends with reporting and distribution rather than with the alert itself.

#### What You Need to Remember Before 1.1

You do not need to memorize Sysmon event IDs, Zeek fields, Sigma syntax, or alert categories yet.

For now, remember the flow:

> **1.1:** Read the host.  
> **1.2:** Read the wire.  
> **1.3:** Read the detection.  
> **1.4:** Investigate and assess the alert.  
> **1.5:** Communicate the result.

Each later module will add the detail needed to perform that step.

#### Orientation Check

1. Which unit teaches you which **process** opened a network connection?
2. Which unit teaches you what an HTTP request looked like **on the wire**?
3. Why does the course teach endpoint and network evidence before alert classification?
4. What is the final purpose of 1.5?

#### Summary

The 1.x SOC block teaches a complete evidence-to-handoff workflow.

You will learn to read host and network evidence, understand what detection logic matched, investigate the resulting alert, and communicate a defensible result.

The recurring discipline is simple:

> **Describe what the evidence shows first. Then decide what it means.**

### 1.1 – Endpoint Activity: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Endpoint telemetry records what programs, files, network connections, registry changes, and loaded components did on a host. SOC analysts need to recognize which evidence type can answer a question and how to combine several event types into a defensible picture of host activity.

#### Connect to What You Already Know

The SOC orientation introduced the evidence-to-handoff workflow. This subunit begins the evidence side of that workflow by showing what endpoint records can reveal and where each record type has limits.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.1.1 – Endpoint Activity** | Build the map of endpoint evidence types and the questions they can answer. |
| **1.1.2 – Process Activity** | Interpret process creation, parent-child relationships, command lines, users, and execution context. |
| **1.1.3 – File System Activity** | Interpret file creation, modification, deletion, paths, and hashes. |
| **1.1.4 – Network Activity (Endpoint)** | Connect outbound or inbound network activity to the host and, where available, the initiating process. |
| **1.1.5 – Registry Activity** | Interpret registry changes as host configuration and persistence evidence when the relevant keys and values are present. |
| **1.1.6 – Image and Driver Load Activity** | Interpret loaded modules and drivers as additional execution and trust context. |

#### What to Watch For

- Match the question to the endpoint evidence type most likely to answer it.
- Preserve what a field actually says; an event can show that something happened without proving intent or maliciousness.
- Combine events by host, user, process, time, and other shared context rather than treating each record as a complete incident by itself.

#### Expected End State

By the end of this subunit, you should be able to:

- identify the major endpoint evidence types and the questions each can answer;
- read common process, file, network, registry, image, and driver-load fields in context;
- connect related endpoint events without overstating what any one event proves;
- recognize when missing telemetry limits the conclusion.

#### How to Preview This Subunit

Read this introduction, then skim the [1.1 Summary](#11--endpoint-activity-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 1.1.1 — Endpoint activity (the map)

**Estimated Time:** 15–20 minutes

#### Why This Matters

Endpoint evidence helps you describe activity on a device. Recognizing the kind of activity first makes it easier to choose the right fields and explain what the event establishes. The next five lessons build that skill one activity type at a time.

#### Learning Objectives

By the end of this module, you will be able to:

1. Recognize the five endpoint activity types.
2. Classify a short description by its recorded operation.
3. Explain why source and collection coverage matter when interpreting an event.

#### Five kinds of endpoint activity

An event is a recorded observation. A log can contain many events, and a SIEM may display each event as a row. Collection settings determine which observations are recorded.

| Activity type | What the event concerns | Example |
|---|---|---|
| Process | A program starts, ends, or accesses another process. | A script interpreter launches PowerShell. |
| File | A file operation such as creation, rename, modification, reading, or deletion, where collected. | A process writes a file under Temp. |
| Registry | A Windows registry key or value changes. | A process sets a Run-key value. |
| Host-network | A connection or DNS operation observed by the endpoint. | PowerShell connects to a remote IP address. |
| Image / driver load | A module loads into a process, or a driver loads into the kernel. | A program loads a DLL. |

One sequence can generate several event types. Each observation adds a different part of the account.

#### Recognizing the observation

“A file named `update.dll` was created” describes file activity. “PowerShell loaded `update.dll`” describes image-load activity. The filename is shared, but the recorded operation differs. A creation event alone leaves loading or execution unestablished.

Likewise, a process-start event can explain how a program began, while a related host-network event can identify a connection associated with it. Linking the events develops the sequence without asking one record to prove everything.

#### Understanding the source

Sysmon and Microsoft Defender for Endpoint (MDE) can provide overlapping endpoint observations. Their event types, fields, and collection coverage differ, so translating between them requires checking the actual schema. They should not be treated as interchangeable copies of the same dataset.

Zeek observes network traffic at a sensor. Its native connection records generally identify network endpoints rather than the operating-system process that opened a socket. Endpoint and network evidence complement one another when host identity, timing, and the observed flow can be connected.

#### Knowledge Check

1. Name the five activity types and give an example of each.
2. How does a file-create event differ from an image-load event for the same DLL?
3. Why should you check the schema when moving from Sysmon to MDE?

#### Summary

Identify the recorded operation, then use the fields and coverage of its source to describe it. Related events can build a fuller sequence while retaining what each observation actually establishes.

#### References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — Advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables)

### 1.1.2 — Process Activity

**Estimated Time:** 25–30 minutes

#### Why This Matters

A process event helps answer which program ran, what started it, and under which account. Reading those relationships carefully gives the investigation a stronger starting point than relying on the executable name alone.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret process creation, termination, and access events.
2. Describe a process event using its recorded fields and limitations.
3. Create or modify a query for a specific process pattern.

#### Reading a process event

| Detail | What to examine |
|---|---|
| Operation | Sysmon 1 records process creation, 5 termination, and 10 process access. These are different operations. |
| Process identity | Image path, PID, event time, and a stable process identifier where available. PIDs can be reused. |
| Command line | Recorded arguments explain how the program was invoked; they may be incomplete or attacker-controlled. |
| Parent and account | Parent fields and user context help explain the launch relationship. In an MDE creation event, `InitiatingProcess*` describes the initiating process. |
| Integrity and elevation | Use recorded integrity and token information to assess execution context. An empty field leaves a gap. |
| Hash and original filename | Identify the file and its embedded metadata. MDE uses `ProcessVersionInfoOriginalFileName`; a name or trusted hash alone does not establish benign use. |

`DeviceProcessEvents` provides process creation and related observations. Use its in-portal schema to confirm event types rather than assuming every Sysmon operation has a direct equivalent there. For process access, describe the recorded source and target; opening a handle alone does not establish injection.

#### Working through the example

The supplied creation event records `wscript.exe` launching `powershell.exe -enc …` as `jlee`. A supported description is: “Script Host launched PowerShell with an encoded-command argument under the recorded account `jlee`.” The parent, command line, and account fields support the sentence.

The abbreviated command line does not show the decoded instructions. It also does not establish a hidden window: that needs an appropriate argument or other evidence. Record the event reference and time so another analyst can recover the source. A legitimate PowerShell binary can be used for either authorized or malicious activity.

#### Creating a focused process query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceProcessEvents
| where Timestamp > ago(1d)
| where ActionType == "ProcessCreated"
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName =~ "wscript.exe"
| where ProcessCommandLine contains "-enc"
| project Timestamp, DeviceName, AccountName, ProcessCommandLine,
          InitiatingProcessCommandLine, ProcessId, SHA1, SHA256
```

The filters search for the three observed characteristics together. `contains` performs a substring search; this teaching example can match longer text and does not cover every spelling or form of PowerShell invocation. Review the returned command lines before interpreting a match. To create a query for a different parent, change the initiating-process predicate and explain how the result set changes.

#### Knowledge Check

1. What distinguishes Sysmon events 1, 5, and 10?
2. Describe the supplied wscript-to-PowerShell event and identify one unknown.
3. Modify the query to look for the same PowerShell pattern started by cscript.exe. What changes?

#### Summary

A useful process description connects the operation, program, command line, parent, and account to recorded evidence. A focused query expresses the chosen pattern and makes its coverage limits clear.

#### References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

### 1.1.3 — File System Activity

**Estimated Time:** 25–30 minutes

#### Why This Matters

File events help establish what happened to an object on an endpoint and which process performed the operation. Keeping the operation, path, and initiating process together helps distinguish a file arriving from that file later being used.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret file operations, paths, hashes, and initiating processes.
2. Describe a file event without inferring execution.
3. Create or modify a query for a specific file operation.

#### Reading file operations

| Detail | Interpretation |
|---|---|
| Create or overwrite | Sysmon 11 records file creation or overwrite. The record does not by itself distinguish every prior state of the path. |
| Rename or move | A source may record a new name or location, with previous path/name fields where available. |
| Delete | Sysmon 23 records deletion with archiving; 26 records deletion without archiving. A deletion record concerns that operation, not permanent absence afterward. |
| Modify or read | Coverage depends on the source and configuration; these operations are not comprehensively represented by Sysmon 11/23/26. |
| Path and extension | Identify the target object. An extension is a name, not proof of content or execution. |
| Hash | Use a recorded hash when available. Sysmon 11 does not supply a file hash; MDE hash population varies. |
| Initiator | Sysmon `Image` or MDE `InitiatingProcess*` identifies the process associated with the file operation. |

MDE `DeviceFileEvents` includes file operations such as creation, modification, rename, and deletion where collected. Check the supported actions and previous-name fields in the schema. An absent record could reflect coverage or retention rather than absence of activity.

#### Working through the example

For this separate field-reading example, a supplied Sysmon 11 event uses the familiar classroom host `WS-JLEE`. It records `Image=wscript.exe` and `TargetFilename=C:\Users\jlee\AppData\Local\Temp\update.exe`, with no hash field. Describe it as: “Sysmon recorded Script Host creating or overwriting `update.exe` at the Temp path; this event supplies no file hash.”

This practice record is not evidence that A12's HTTP request successfully transferred the file. The event does not establish that `update.exe` ran. To investigate execution, look for a related process event using the host, time, path, and any available identity evidence. Treat that as an additional observation rather than adding it to the file event's meaning.

#### Creating a focused file query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceFileEvents
| where Timestamp > ago(1d)
| where ActionType == "FileCreated"
| where InitiatingProcessFileName =~ "wscript.exe"
| where FolderPath contains @"\Temp\"
| where FileName endswith ".exe"
| project Timestamp, DeviceName, ActionType, FolderPath, FileName,
          InitiatingProcessCommandLine, SHA1, SHA256
```

This searches for executable-named file creations associated with Script Host under a Temp path. The name filter does not inspect the bytes. A rename question needs the appropriate rename action and available previous/current path fields, rather than treating file creation as a rename.

#### Knowledge Check

1. What does Sysmon 11 establish, and does it prove execution?
2. Describe the supplied event when its hash is unavailable.
3. Modify the query to search for DLL-named files and explain the limitation.

#### Summary

File evidence describes an operation on a path by an associated process. Use the available identity fields, preserve coverage gaps, and query the operation that answers the investigation question.

#### References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

### 1.1.4 — Network Activity (Endpoint)

**Estimated Time:** 25–30 minutes

#### Why This Matters

Endpoint network events connect network activity to a process on a device. That process context can help explain a connection that a network sensor sees only as traffic between addresses.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret endpoint network addresses, operations, direction, names, and process context.
2. Describe the supplied event with its evidence limits.
3. Create or modify a query for specific endpoint network activity.

#### Reading the endpoint view

| Detail | What it contributes |
|---|---|
| Local and remote address/port | MDE `LocalIP`, `LocalPort`, `RemoteIP`, and `RemotePort` identify the endpoints. Local/remote alone does not establish who initiated. |
| Protocol and operation | Read the protocol and `ActionType` to distinguish the recorded connection outcome. |
| Direction | Sysmon 3 `Initiated` helps identify whether the process initiated the connection; interpret direction using the source's semantics. |
| Process | Sysmon `Image` or MDE `InitiatingProcess*` associates the activity with a process. |
| Name information | Sysmon 22 `QueryName` records DNS queries when collected. MDE `RemoteUrl` may contain a URL or FQDN; a blank field does not establish that DNS was unused. |

Sysmon 3 concerns network connections; Sysmon 22 concerns DNS queries. MDE uses `DeviceNetworkEvents` for network connections and related observations. Its table and action coverage should be checked locally. A DNS lookup and a subsequent connection are separate observations.

#### Working through the example

**Separate classroom record — not A12.** The values below are training-only and should not be merged into the recurring case.

A supplied MDE event records `ConnectionSuccess`, `Protocol=Tcp`, `RemoteIP=198.51.100.44`, `RemotePort=443`, and initiating process `powershell.exe` with command line `powershell.exe -enc …`. `RemoteUrl` is blank.

A supported description is: “The endpoint recorded a successful TCP connection associated with PowerShell to the remote endpoint `198.51.100.44:443`; no remote URL or FQDN is recorded.” The port alone does not establish HTTPS or Command and Control. The abbreviated command does not establish hidden-window execution. Use source-specific direction evidence before adding “outbound” to the finding.

#### Creating a focused network query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceNetworkEvents
| where Timestamp > ago(1d)
| where ActionType == "ConnectionSuccess"
| where InitiatingProcessFileName =~ "powershell.exe"
| where RemoteIP == "198.51.100.44" and RemotePort == 443
| project Timestamp, DeviceName, Protocol, LocalIP, LocalPort,
          RemoteIP, RemotePort, RemoteUrl, InitiatingProcessCommandLine
```

This looks for successful connections associated with PowerShell to the specified endpoint. It is an exact destination search for the example, not a general detector for malicious PowerShell. A DNS question instead calls for a DNS-capable source and its query-name field.

#### Knowledge Check

1. What does endpoint network evidence add to a native Zeek connection record?
2. What can you say about the supplied TCP/443 event when RemoteUrl is blank?
3. How would you modify the query to find the same destination used by any process?

#### Summary

Endpoint network evidence helps connect a process to a recorded network operation. Describe the outcome, endpoints, protocol, and available names, then use a focused query to investigate the chosen pattern.

#### References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceNetworkEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicenetworkevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

### 1.1.5 — Registry Activity

**Estimated Time:** 25–30 minutes

#### Why This Matters

Registry events record changes to Windows configuration. Reading the key, value name, value data, and initiating process separately helps explain exactly what changed and what follow-up evidence would be useful.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret registry structure and create, set, delete, and rename operations.
2. Describe a registry change and its evidence limits.
3. Create or modify a query for specific registry operations.

#### Reading the registry structure

A hive is a top-level registry area. A key provides a path, and a value within that key has a name, type, and data. `HKLM` concerns machine configuration. `HKCU` refers to the current user's hive; records may instead identify that user's hive under `HKU\<SID>`. Preserve the SID and resolve its account context when needed.

| Operation or field | What to read |
|---|---|
| Create/delete | Sysmon 12 records creation or deletion of registry objects; read the event's operation detail. |
| Set value | Sysmon 13 records a value being set, with details subject to the value type and logging behavior. |
| Rename | Sysmon 14 records key or value rename. |
| MDE fields | `DeviceRegistryEvents`: `RegistryKey`, `RegistryValueName`, `RegistryValueData`, `ActionType`, and `InitiatingProcess*`. |
| Locations | Run/RunOnce and service configuration keys can be relevant to startup behavior. Location alone does not establish malicious persistence. |

If value data is blank, distinguish an absent or uncollected value from a genuinely empty value where the source permits it. Otherwise state that the available record does not resolve the distinction.

#### Working through the example

The supplied event records PowerShell setting value `Updater` under the user's `Software\Microsoft\Windows\CurrentVersion\Run` key to `C:\Users\jlee\AppData\Local\Temp\update.exe`.

Describe the configuration change: “PowerShell set the user's Run value `Updater` to the recorded Temp executable path.” This can configure a startup action, but the event does not establish that the file exists, that a later logon ran it, or that the change was unauthorized. Those questions require supporting file, process, and authorization context.

#### Creating a focused registry query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceRegistryEvents
| where Timestamp > ago(1d)
| where ActionType == "RegistryValueSet"
| where InitiatingProcessFileName =~ "powershell.exe"
| where RegistryKey endswith @"\Software\Microsoft\Windows\CurrentVersion\Run"
| where RegistryValueName =~ "Updater"
| project Timestamp, DeviceName, RegistryKey, RegistryValueName,
          RegistryValueData, InitiatingProcessCommandLine
```

The key suffix and value-name predicates focus the search on this configuration change. Confirm how your source represents hive paths. Removing the value-name predicate broadens the search to other values under that Run key; it does not automatically cover RunOnce or all startup mechanisms.

#### Knowledge Check

1. How do a key, value name, and value data differ?
2. Describe the supplied Updater change and one thing it leaves unknown.
3. Modify the query to find any value set by PowerShell under the same Run key.

#### Summary

A registry finding should identify the operation, key, named value, available data, and initiating process. This makes the configuration change clear while leaving later behavior and authorization to additional evidence.

#### References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceRegistryEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceregistryevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

### 1.1.6 — Image and Driver Load Activity

**Estimated Time:** 25–30 minutes

#### Why This Matters

An image-load event shows a module being loaded into a process. A driver-load event concerns code loaded into the kernel. Understanding the difference helps you describe the execution context without confusing a file on disk with a recorded load.

#### Learning Objectives

By the end of this module, you will be able to:

1. Distinguish user-mode image loads from kernel driver loads.
2. Describe load paths, process context, hashes, and signature evidence.
3. Create or modify a query for specific image or driver load activity.

#### Reading image and driver loads

| Detail | Interpretation |
|---|---|
| User-mode image load | Sysmon 7: `Image` identifies the process and `ImageLoaded` the module. MDE `DeviceImageLoadEvents` concerns DLL loads. |
| Kernel driver load | Sysmon 6 records the loaded driver. It does not provide a user-mode parent-process relationship equivalent to event 7. |
| Path and hash | Identify the loaded object using the available path and hashes. A .sys extension by itself does not prove a kernel load. |
| Signature | Interpret signature fields for the loaded object where supplied. Missing is different from explicitly unsigned, and signed does not mean harmless. |
| Coverage | Image-load collection can be high volume and selectively enabled. Confirm collection and retention before interpreting an absence. |

In MDE, fields prefixed `InitiatingProcess` describe the initiating process; they should not be mistaken for the loaded DLL's identity or signing status. A loaded-object SHA1/SHA256, when available, concerns the object named by the event.

#### Working through the example

A Sysmon 7 event records `Image=powershell.exe`, `ImageLoaded=C:\Users\jlee\AppData\Local\Temp\update.dll`, and `Signed=false`.

A supported description is: “PowerShell loaded the DLL at the recorded Temp path; Sysmon reports the loaded object as unsigned.” The load, path, and reported signature state warrant examination in context. They do not alone establish how the DLL arrived, what code it executed, or whether the activity was malicious. A related file event may explain arrival, while process and other evidence may explain subsequent behavior.

#### Creating a focused image-load query

The following KQL example illustrates the requested search. Confirm the table, fields, and supported `ActionType` values in your environment before using it. Adjust the time range to the investigation.

```kusto
DeviceImageLoadEvents
| where Timestamp > ago(1d)
| where InitiatingProcessFileName =~ "powershell.exe"
| where FolderPath contains @"\Temp\"
| where FileName endswith ".dll"
| project Timestamp, DeviceName, FolderPath, FileName, SHA1, SHA256,
          InitiatingProcessFileName, InitiatingProcessCommandLine
```

This searches for DLL loads associated with PowerShell from Temp paths. It does not filter for unsigned DLLs because no loaded-object signature field has been assumed. A kernel-driver question calls for verified driver-load telemetry, such as Sysmon 6, and a query mapped to that source.

For a driver-specific question, this separate KQL example assumes a classroom `SysmonEvents` table with normalized `TimeGenerated`, `EventID`, `Computer`, and `ImageLoaded` columns:

```kusto
SysmonEvents
| where TimeGenerated > ago(1d)
| where EventID == 6
| where ImageLoaded endswith @"\trainingdriver.sys"
| project TimeGenerated, Computer, ImageLoaded
```

It finds recorded driver loads for the specified path suffix; it does not determine whether that driver is safe. Map the table and parsed fields to the actual Sysmon ingestion schema.

#### Knowledge Check

1. How do Sysmon 6 and 7 differ?
2. Describe the supplied event and distinguish missing signature data from Signed=false.
3. Modify the query for DLLs loaded by rundll32.exe. Does it become a driver-load query?

#### Summary

Image and driver events describe different kinds of loads. Identify the loaded object, execution context, and available signature evidence, then search the source that actually records the operation of interest.

#### References and Further Reading

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft — DeviceImageLoadEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceimageloadevents-table)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

### 1.1 – Endpoint Activity: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Host question → relevant event type → field interpretation → cross-event context → bounded conclusion**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- identify the major endpoint evidence types and the questions each can answer;
- read common process, file, network, registry, image, and driver-load fields in context;
- connect related endpoint events without overstating what any one event proves;
- recognize when missing telemetry limits the conclusion.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.1.1 – Endpoint Activity** | Build the map of endpoint evidence types and the questions they can answer. |
| **1.1.2 – Process Activity** | Interpret process creation, parent-child relationships, command lines, users, and execution context. |
| **1.1.3 – File System Activity** | Interpret file creation, modification, deletion, paths, and hashes. |
| **1.1.4 – Network Activity (Endpoint)** | Connect outbound or inbound network activity to the host and, where available, the initiating process. |
| **1.1.5 – Registry Activity** | Interpret registry changes as host configuration and persistence evidence when the relevant keys and values are present. |
| **1.1.6 – Image and Driver Load Activity** | Interpret loaded modules and drivers as additional execution and trust context. |

#### Check Your Understanding

Ask yourself:

1. If you need to know which process opened a network connection, which endpoint evidence is most useful?
2. Why is a file hash useful context without automatically proving that the file is malicious?
3. What shared context can help you determine whether process, file, and registry events belong to the same activity?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **1.2 – Zeek Network Evidence: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 1.2 – Zeek Network Evidence: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Zeek turns observed network traffic into protocol-aware logs. The analyst skill is learning which log answers which question, how related records connect, and what the sensor can and cannot tell you about activity it observed.

#### Connect to What You Already Know

Endpoint evidence showed what a host recorded locally. Zeek adds a network-sensor view, which can confirm, complement, or fail to observe parts of the same activity depending on where the sensor sits and what protocols are visible.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.2.1 – Zeek Concepts** | Understand Zeek records, timestamps, UIDs, sensors, and evidence boundaries. |
| **1.2.2 – Conn Engine** | Use connection summaries to establish who talked to whom, when, and how much. |
| **1.2.3 – DNS Engine** | Use DNS records to understand name-resolution activity and answers. |
| **1.2.4 – TLS Engine** | Use TLS metadata to interpret encrypted-session context without assuming visibility into encrypted content. |
| **1.2.5 – HTTP Engine** | Use HTTP records to inspect requests and responses when HTTP is visible. |
| **1.2.6 – SMTP Engine** | Use SMTP records to understand mail-flow activity visible to the sensor. |
| **1.2.7 – Files Engine** | Use file-analysis records to connect transferred files with network activity when extraction or hashing is available. |
| **1.2.8 – Weird Engine** | Use protocol anomalies as investigative context rather than automatic proof of malicious activity. |

#### What to Watch For

- Start with the network question, then choose the log that contains the relevant protocol evidence.
- Use shared identifiers such as Zeek UIDs and timing to connect records across logs.
- Keep sensor placement, encryption, logging configuration, and protocol visibility in mind before interpreting a missing field or missing record.

#### Expected End State

By the end of this subunit, you should be able to:

- select the Zeek log that best answers a network-investigation question;
- interpret the core evidence each major Zeek log provides;
- connect related network records using shared context;
- explain how sensor visibility and protocol limits affect what Zeek can establish.

#### How to Preview This Subunit

Read this introduction, then skim the [1.2 Summary](#12--zeek-network-evidence-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 1.2.1 — Zeek Concepts

**Estimated Time:** 15–20 minutes

#### Why This Matters

Network-sensor evidence describes traffic visible at an observation point. Zeek turns that traffic into structured records that analysts can search and connect. Understanding how those records are produced helps you choose the right log and recognize when additional evidence is needed.

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain Zeek’s purpose and the role of analyzers and scripts.
2. Distinguish network-sensor records from endpoint evidence.
3. Explain when PCAP can verify or expand a logged observation.

#### How traffic becomes a log

Zeek is a network analysis framework. Protocol analyzers interpret observed traffic, and scripts use events from that analysis to create logs and other outputs. This course uses “engine” as an introductory label for these analysis and logging components; it is not a claim that every log comes from a separate protocol engine.

Connection records summarize flows. Protocol logs describe observations such as DNS transactions, TLS handshakes, HTTP requests, and SMTP transactions. File analysis records observed content, while weird records describe unexpected conditions encountered during analysis. These records expose different aspects of activity that a SIEM can make searchable.

#### Relating Zeek to endpoint evidence

A native Zeek record generally identifies network endpoints, times, and protocol details. An endpoint record may identify the responsible operating-system process. To connect them, examine the host/address relationship, time, ports, protocol, and available identifiers.

The sensor's placement matters. Traffic outside its view, encrypted content, packet loss, and configuration choices can limit what Zeek records. A missing protocol log therefore needs a coverage explanation before it can support a conclusion about the activity.

#### When packet capture helps

A packet capture (PCAP) contains captured packets rather than only the fields selected for a log. If retained for the relevant flow, it may help verify a parsed value, examine a header, or recover visible content omitted from the log.

For example, a connection log identifies two endpoints, but an available cleartext HTTP capture may reveal the requested URI. An encrypted capture may still leave application content unreadable. Capture availability, completeness, and decryption context determine what can be added. Request the relevant time and flow through the site's collection process and explain the question the capture is intended to answer.

#### Knowledge Check

1. How do analyzers and scripts contribute to Zeek logs?
2. What can endpoint evidence add to a Zeek connection record?
3. When would PCAP add information, and when might it not?

#### Summary

Zeek supplies structured observations from network traffic. Choose a log according to the question, account for the sensor’s view, and use retained PCAP when it can add relevant evidence.

#### References and Further Reading

- [Zeek — Log files](https://docs.zeek.org/en/master/reference/zeekscript/log-files.html)
- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)

### 1.2.2 — Conn Engine

**Estimated Time:** 25–30 minutes

#### Why This Matters

A connection record gives you a network-level starting point: the endpoints, transport, and progress Zeek observed. That description helps you select the related protocol records without assigning a purpose to the traffic too early.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret connection endpoints, state, history, and identifiers.
2. Describe a connection using the supplied evidence.
3. Create or modify a query for specific connection activity.

#### Reading connection fields

| Field | Meaning |
|---|---|
| `uid` | Connection identifier used to relate records from the same Zeek observation context. |
| `id.orig_h`, `id.orig_p` | Originator address and port from the sensor's view. |
| `id.resp_h`, `id.resp_p` | Responder address and port. |
| `proto`, `service` | Transport and identified application service when available. Port alone does not establish service. |
| `conn_state` | A summary of observed connection progress. Interpret it for the protocol. |
| `history` | Encoded observations; case distinguishes the originator and responder sides. |

For the TCP examples, `SF` indicates normal establishment and termination; `S0` indicates an attempt with no reply observed; `REJ` indicates rejection. In history, letters such as S, H, F, and R concern SYN, SYN-ACK, FIN, and reset observations, with lowercase representing the responder. An originator can be external to your network. Partial capture can limit what the state tells you.

#### Working through the example

The supplied record shows originator `192.0.2.10:51000`, responder `203.0.113.88:443`, `proto=tcp`, `conn_state=SF`, and `uid=CTrain1`.

Describe it as: “Zeek observed a TCP connection from `192.0.2.10:51000` to `203.0.113.88:443` with normal establishment and termination.” The addresses, ports, protocol, and state support that description. Look for `CTrain1` in relevant protocol logs to learn more. The record alone does not identify a process, establish HTTPS, or prove a malicious purpose.

#### Creating a focused connection query

This KQL teaching example assumes an ingested table named `ZeekConn`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekConn
| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88"
| where ['id.resp_p'] == 443 and proto == "tcp"
| where conn_state == "SF"
| project TimeGenerated, uid, ['id.orig_h'], ['id.orig_p'],
          ['id.resp_h'], ['id.resp_p'], conn_state, history
```

The query selects the specified responder, port, transport, and state. Change the state to `S0` to investigate attempts for which the sensor observed no response; the results would not establish why a response was absent.

#### Knowledge Check

1. How do originator and responder differ from internal and external?
2. Describe the supplied record and name the pivot identifier.
3. Modify the query for unanswered attempts and explain the limit.

#### Summary

A connection finding describes the endpoints, transport, and observed progress. Use the connection identifier to seek related records and keep explanations of purpose or failure tied to additional evidence.

#### References and Further Reading

- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html)

### 1.2.3 — DNS Engine

**Estimated Time:** 25–30 minutes

#### Why This Matters

DNS evidence connects a question about a name to the response observed on the network. Distinguishing the resolver from the returned address helps prevent a common error when moving from a lookup to a connection investigation.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret DNS question, response, record type, and endpoints.
2. Describe a DNS observation and distinguish it from later communication.
3. Create or modify a query for specific DNS activity.

#### Reading a DNS transaction

| Field | Meaning |
|---|---|
| `query` | The requested name. |
| `qtype_name` | The requested record type. |
| `answers` | Observed answer values, which may contain addresses or names. |
| `rcode_name` | Response code, where recorded, useful when interpreting an empty answer. |
| `id.orig_h` | The querying endpoint visible to the sensor. |
| `id.resp_h` | The DNS server contacted, often a recursive resolver. |
| `uid` | Connection identifier for related records; multiple DNS transactions may share it. |

A requests an IPv4 address; AAAA an IPv6 address; MX a mail exchanger; NS a name server; TXT text data; and CNAME a canonical-name alias. A response can include an alias chain. The responder address is the server asked, while returned addresses belong in the answer data. A blank answer needs interpretation using the response code and capture context.

#### Working through the example

The example records `192.0.2.10` asking resolver `192.0.2.53` for an A record for `update.example`, with `answers=["203.0.113.88"]` and `rcode_name=NOERROR`.

A supported description is: “The observed client asked `192.0.2.53` for the IPv4 address of `update.example` and received `203.0.113.88`.” A subsequent connection to that address would be separate evidence. If the observed client is itself a resolver, additional records may be needed to identify the original endpoint behind the request.

#### Creating a focused DNS query

This KQL teaching example assumes an ingested table named `ZeekDns`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekDns
| where TimeGenerated > ago(1d)
| where query =~ "update.example" and qtype_name == "A"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          query, qtype_name, answers, rcode_name
```

This selects questions for one name and record type. To include IPv6 questions, use `qtype_name in ("A", "AAAA")`. Compare actual answer values and response codes rather than assuming every matching question received an address.

#### Knowledge Check

1. Where do you find the DNS server and the returned address?
2. Describe the example and explain whether it proves a connection to the answer.
3. Modify the query for both IPv4 and IPv6 questions for the same name.

#### Summary

A DNS description identifies the observed client, resolver, question, type, and response. It supplies a lead for subsequent activity rather than proving that the client contacted the returned address.

#### References and Further Reading

- [Zeek — dns.log](https://docs.zeek.org/en/current/reference/logs/dns.html)

### 1.2.4 — TLS Engine

**Estimated Time:** 25–30 minutes

#### Why This Matters

TLS can conceal application content while leaving some handshake information visible. Reading that information carefully helps describe the observed session without treating a hostname, certificate, or fingerprint as a verdict.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret SNI, certificate information, optional fingerprints, version, cipher, and endpoints.
2. Describe TLS activity using the observed establishment state.
3. Create or modify a query for specific TLS activity.

#### Reading TLS evidence

Zeek records TLS information in `ssl.log`; the name is historical.

| Field or feature | Interpretation |
|---|---|
| `server_name` | Observed Server Name Indication (SNI), when visible. It is distinct from a certificate subject. |
| `subject`, `issuer` | Certificate identity fields where available; detailed certificate records may be linked through `x509.log`. |
| `version`, `cipher` | Observed TLS negotiation details. |
| `established` | Zeek's indication that the TLS session was successfully established. Version and cipher alone should not substitute for that assessment. |
| JA3 / JA3S | Optional client/server fingerprints when the deployment collects them. A shared fingerprint does not uniquely identify malware. |
| Endpoint fields and `uid` | Identify the observed connection and related records. |

Encryption, TLS version, encrypted Client Hello, capture quality, and configuration affect visibility. A blank SNI or certificate field does not establish that no name or certificate existed. TLS 1.3 can conceal certificate details from a passive sensor.

#### Working through the example

A record shows `192.0.2.10` communicating with `203.0.113.88:443`, a recorded TLS version and cipher, `established=true`, and no `server_name`.

Describe it as: “Zeek reports an established TLS session between the supplied endpoints with the recorded version and cipher; SNI is unavailable in this record.” If `established` were absent, limit the conclusion to the observed handshake details. Even an established session does not reveal the encrypted HTTP path or prove the application's purpose.

#### Creating a focused TLS query

This KQL teaching example assumes an ingested table named `ZeekTls`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekTls
| where TimeGenerated > ago(1d)
| where ['id.resp_h'] == "203.0.113.88" and ['id.resp_p'] == 443
| where established == true
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          server_name, version, cipher, established
```

This searches for established TLS sessions to the example endpoint. To ask about a hostname instead, use `server_name =~ "update.example"`; that query only finds records where the name is visible and populated.

#### Knowledge Check

1. How does SNI differ from the certificate subject?
2. What supports calling the example an established TLS session?
3. Modify the query to search for visible SNI update.example and explain a blind spot.

#### Summary

TLS records describe the visible handshake and session state. State which names, certificate details, and fingerprints are available, and keep encrypted application behavior separate from those observations.

#### References and Further Reading

- [Zeek — ssl.log](https://docs.zeek.org/en/current/reference/logs/ssl.html)
- [Zeek — x509.log](https://docs.zeek.org/en/current/reference/logs/x509.html)

### 1.2.5 — HTTP Engine

**Estimated Time:** 25–30 minutes

#### Why This Matters

An HTTP record helps explain what a client requested and what response status the sensor observed. Separating request details, server response, and any transferred content makes the resulting account more precise.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret HTTP method, host, URI, User-Agent, response status, and endpoints.
2. Describe the request and response without inventing content or execution.
3. Create or modify a query for specific HTTP activity.

#### Reading HTTP fields

| Field | Meaning |
|---|---|
| `method` | Request method, such as GET, POST, PUT, or HEAD. |
| `host` | Recorded HTTP Host header; it is distinct from the destination IP. |
| `uri` | Requested URI, commonly a path and query. |
| `user_agent` | A client-supplied identification string, which can be changed or spoofed. |
| `status_code` | Observed response status. A 200 response does not establish benignness or execution. |
| Endpoint fields, `uid`, `trans_depth` | Connection context and the transaction's position within it. |

Host and URI help reconstruct the requested resource, but a complete URL also needs a supported scheme and any relevant port. Preserve missing components explicitly. Zeek needs visibility into HTTP content to parse it; encrypted HTTPS normally requires appropriate decryption visibility for comparable HTTP fields. The log does not supply the full body by default.

#### Working through the example

**Separate classroom HTTP record — not A12.** These values exist only to teach field interpretation and query scope.

The supplied record shows `GET /package.bin` from `192.0.2.10` to `198.51.100.60:8080`, `status_code=200`, and no recorded Host or User-Agent.

A supported description is: “The client requested `/package.bin` with GET from the supplied destination on port 8080 and received HTTP status 200; Host and User-Agent are unavailable in this record.” The path name does not establish the returned bytes. File-analysis records or retained content may help determine what was transferred, while endpoint evidence can address whether a file was saved or executed.

#### Creating a focused HTTP query

This KQL teaching example assumes an ingested table named `ZeekHttp`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekHttp
| where TimeGenerated > ago(1d)
| where method == "GET" and uri == "/package.bin"
| where ['id.resp_h'] == "198.51.100.60" and ['id.resp_p'] == 8080
| project TimeGenerated, uid, ['id.orig_h'], host, uri,
          user_agent, status_code
```

The equality test matches exactly `/package.bin`; it will not include a URI with an added query string. A substring or carefully scoped path expression changes that behavior. Choose the comparison that answers the stated question and explain the extra results it permits.

#### Knowledge Check

1. How do the Host header, destination IP, and URI differ?
2. What does the example establish, and does it prove package.bin ran?
3. Would uri == "/package.bin" match /package.bin?id=1? How could you broaden it?

#### Summary

An HTTP finding connects the request, response status, and endpoints. Preserve missing headers and distinguish a requested path from transferred content or endpoint execution.

#### References and Further Reading

- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)

### 1.2.6 — SMTP Engine

**Estimated Time:** 25–30 minutes

#### Why This Matters

SMTP records describe mail transactions visible to a network sensor. They help identify envelope addresses and selected headers while leaving mailbox delivery, user action, and attachment behavior to other evidence.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret SMTP envelope addresses, subject, Message-ID, and endpoints.
2. Describe a transaction without assuming delivery or user action.
3. Create or modify a query for specific SMTP activity.

#### Reading a mail transaction

| Field | Meaning |
|---|---|
| `mailfrom` | Envelope sender supplied during the SMTP transaction. This differs from the displayed From header. |
| `rcptto` | Envelope recipients, potentially more than one. |
| `subject` | Recorded Subject header when available. |
| `msg_id` | Message-ID header when available; useful context, not a file hash or guaranteed unique identity. |
| Endpoint fields and `uid` | The communicating systems and connection context. |

These values describe the observed transaction and claims within it. A familiar sender name or subject does not authenticate the sender. Encryption, including a STARTTLS transition, may limit which portions the sensor can parse. A missing header can reflect absence in the message, collection limits, or parsing visibility.

#### Working through the example

The supplied transaction records envelope sender `sender@example.net`, recipient `jlee@example.org`, subject `Invoice`, and Message-ID `<train-1@example.net>` between two mail systems.

Describe it as: “Zeek observed an SMTP transaction with the recorded envelope sender and recipient, subject `Invoice`, and the supplied Message-ID.” Without a relevant acceptance result or delivery record, avoid claiming successful mailbox delivery. The transaction also does not establish that the user opened the message or that its attachment was malicious.

#### Creating a focused SMTP query

This KQL teaching example assumes an ingested table named `ZeekSmtp`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekSmtp
| where TimeGenerated > ago(1d)
| where mailfrom =~ "sender@example.net"
| where subject contains "Invoice"
| project TimeGenerated, uid, ['id.orig_h'], ['id.resp_h'],
          mailfrom, rcptto, subject, msg_id
```

This selects transactions using an envelope sender and subject substring. For a recipient search, first confirm whether `rcptto` was ingested as an array or string and use the appropriate membership operation. Sender or subject matches remain leads requiring context.

#### Knowledge Check

1. How does mailfrom differ from a displayed From header?
2. Describe the example without claiming mailbox delivery.
3. Modify the query for the same sender regardless of subject.

#### Summary

SMTP evidence describes the observed mail transaction and selected headers. Use it to develop a precise lead while keeping delivery, user action, and attachment behavior tied to their own evidence.

#### References and Further Reading

- [Zeek — smtp.log](https://docs.zeek.org/en/current/reference/logs/smtp.html)

### 1.2.7 — Files Engine

**Estimated Time:** 25–30 minutes

#### Why This Matters

Zeek file analysis connects observed network content to the flow that carried it. It can help explain a download or attachment, while the available fields also show whether hashes or extracted bytes exist for further examination.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret file names, MIME types, hashes, direction, and connection identifiers.
2. Describe observed file content without assuming endpoint creation.
3. Create or modify a query using the file-log schema actually available.

#### Reading file-analysis records

| Field or representation | What it contributes |
|---|---|
| `fuid` | File-analysis identifier; this is different from a connection UID. |
| `filename`, `mime_type` | A supplied filename when available and an assessment of content type. These may disagree. |
| `md5`, `sha1`, `sha256` | Hashes when the relevant analysis is enabled and values are available. |
| Current `uid`, endpoint fields, `is_orig` | Connection context; `is_orig=false` indicates the responder supplied the content, and true indicates the originator. |
| Legacy `tx_hosts`, `rx_hosts`, `conn_uids` | Sender/receiver sets and connection identifiers in older or compatibility-enabled schemas. Check which representation your feed uses. |
| Completeness and extraction fields | Observed/missing byte information and extraction details help assess what was actually available. |

A `files.log` record does not guarantee that Zeek saved a file to disk or captured its complete content. Extraction and hashing are configuration-dependent. A network file observation also does not establish an endpoint filesystem path.

#### Working through the example

**Separate classroom file-analysis record — not A12.** It intentionally pairs with the separate HTTP training record from 1.2.5.

Suppose a record identifies executable-type content with `mime_type=application/x-dosexec`, `fuid=FTrain1`, `uid=CTrain1`, originator `192.0.2.10`, responder `198.51.100.60`, and `is_orig=false`. A related HTTP record associates it with `/package.bin`.

The supported account is that Zeek observed executable-type content supplied by the responder to the originator in that HTTP context. Use `CTrain1` for the connection and `FTrain1` for file references such as an HTTP `resp_fuids` entry. In a legacy record, `tx_hosts` and `rx_hosts` supply direction and `conn_uids` supplies the connection pivot. State separately whether a hash, complete bytes, or an extracted object is available.

#### Creating a focused file-analysis query

This KQL teaching example assumes an ingested table named `ZeekFiles`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekFiles
| where TimeGenerated > ago(1d)
| where mime_type == "application/x-dosexec"
| where ['id.resp_h'] == "198.51.100.60" and is_orig == false
| project TimeGenerated, fuid, uid, ['id.orig_h'], ['id.resp_h'],
          mime_type, is_orig
```

This example uses the current endpoint/direction representation and selects executable-type content sent by the specified responder. A legacy feed needs equivalent membership tests against `tx_hosts` and suitable `conn_uids` output. Searching hashes requires a populated hash column; the file-analysis identifier is not a substitute for a hash.

#### Knowledge Check

1. How do fuid and uid differ?
2. Who supplied the content when is_orig=false in the example, and does it establish a Temp file on the host?
3. Modify the query for files supplied by the originator and identify the legacy equivalent.

#### Summary

File-analysis records describe observed network content and its connection context. Check the schema, direction, completeness, and available hashes or extracted bytes before choosing the next pivot.

#### References and Further Reading

- [Zeek — files.log](https://docs.zeek.org/en/current/reference/logs/files.html)

### 1.2.8 — Weird Engine

**Estimated Time:** 20–25 minutes

#### Why This Matters

A weird record reports an unexpected condition encountered by Zeek. It is useful because it points to traffic or visibility worth examining, but its meaning depends on the named condition and the surrounding evidence.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret a weird type, notice flag, endpoints, and available UID.
2. Describe the reported condition from the sensor’s viewpoint.
3. Create or modify a query for a specific weird condition.

#### Reading an unexpected condition

| Field | What to examine |
|---|---|
| `name` | The specific unexpected condition reported by Zeek. |
| Endpoint fields | Connection endpoints when the condition is associated with a connection. |
| `uid` | Related connection identifier when available. |
| `notice` | Whether the condition also resulted in a notice under the applicable policy. |
| `addl` | Additional explanatory detail when supplied. |

Weird records may reflect unusual protocol behavior, malformed traffic, sensor visibility gaps, or other analysis conditions. Some do not have a complete connection context. Use the recorded type to develop a question rather than treating “weird” as a severity or malware label.

#### Working through the example

The example records `name=data_before_established`, responder `203.0.113.88:8080`, and `uid=CTrain1`.

A supported description is: “Zeek reported data before it had observed an established TCP connection for the supplied flow.” This wording preserves the sensor's viewpoint: it does not prove that the endpoints themselves skipped a handshake. Examine the connection history and, if available, the relevant packets to understand whether traffic behavior or incomplete visibility explains the record.

#### Creating a focused weird query

This KQL teaching example assumes an ingested table named `ZeekWeird`, a datetime `TimeGenerated` column, and columns retaining the Zeek field names shown below. These are classroom table names, not built-in Zeek or SIEM tables. Map names and data types to your ingestion schema before use.

```kusto
ZeekWeird
| where TimeGenerated > ago(1d)
| where name == "data_before_established"
| where ['id.resp_h'] == "203.0.113.88"
| project TimeGenerated, uid, name, ['id.orig_h'], ['id.resp_h'],
          ['id.resp_p'], notice
```

The query selects a named condition at the example destination. If the record has no UID, use the available endpoints and time to seek context, acknowledging a less certain correlation. A resulting lead can justify investigation even before an incident determination is possible.

#### Knowledge Check

1. What does a weird record establish?
2. Describe data_before_established without overstating what happened at the endpoints.
3. How would you broaden the query to that condition across all destinations, and what would you use to investigate matches?

#### Summary

A weird record supplies a named condition and any available connection context. Use it to ask a focused follow-up question and separate the sensor’s observation from an explanation of its cause.

#### References and Further Reading

- [Zeek — weird.log and notice.log](https://docs.zeek.org/en/current/reference/logs/weird-and-notice.html)

### 1.2 – Zeek Network Evidence: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Network question → protocol/log selection → related records → visibility check → network conclusion**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- select the Zeek log that best answers a network-investigation question;
- interpret the core evidence each major Zeek log provides;
- connect related network records using shared context;
- explain how sensor visibility and protocol limits affect what Zeek can establish.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.2.1 – Zeek Concepts** | Understand Zeek records, timestamps, UIDs, sensors, and evidence boundaries. |
| **1.2.2 – Conn Engine** | Use connection summaries to establish who talked to whom, when, and how much. |
| **1.2.3 – DNS Engine** | Use DNS records to understand name-resolution activity and answers. |
| **1.2.4 – TLS Engine** | Use TLS metadata to interpret encrypted-session context without assuming visibility into encrypted content. |
| **1.2.5 – HTTP Engine** | Use HTTP records to inspect requests and responses when HTTP is visible. |
| **1.2.6 – SMTP Engine** | Use SMTP records to understand mail-flow activity visible to the sensor. |
| **1.2.7 – Files Engine** | Use file-analysis records to connect transferred files with network activity when extraction or hashing is available. |
| **1.2.8 – Weird Engine** | Use protocol anomalies as investigative context rather than automatic proof of malicious activity. |

#### Check Your Understanding

Ask yourself:

1. Which Zeek log would you start with to establish the basic endpoints and duration of a connection?
2. Why can a TLS log describe an encrypted session without revealing the application content inside it?
3. What does a shared UID allow you to do during an investigation?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **1.3 – Detection Rules: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 1.3 – Detection Rules: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

SOC analysts encounter detection logic written for different evidence layers. Understanding the rule language helps you explain why an alert fired, recognize what data the rule depends on, and make bounded changes without confusing a match with a completed investigation.

#### Connect to What You Already Know

The endpoint and Zeek subunits established the evidence that detections can evaluate. This subunit shows how several common rule types express conditions over that evidence.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.3.1 – SIGMA Rules** | Read and modify portable detection logic that describes log-event conditions. |
| **1.3.2 – Suricata Rules** | Read and modify network-signature logic over packet or protocol evidence. |
| **1.3.3 – YARA Rules** | Read and modify pattern-matching logic for files, memory, or other scanned content. |
| **1.3.4 – SIEM Rules** | Read and modify analytic logic in the local query/detection environment. |

#### What to Watch For

- Identify the evidence layer before interpreting the rule.
- Separate rule conditions from the investigative conclusion that follows a match.
- When modifying a rule, understand which condition changes and what new activity the change would include or exclude.

#### Expected End State

By the end of this subunit, you should be able to:

- explain what evidence each rule family is designed to evaluate;
- read the main parts of SIGMA, Suricata, YARA, and SIEM detection logic;
- describe why a rule matched without equating the match with maliciousness;
- make or assess a simple rule change while preserving its intended detection purpose.

#### How to Preview This Subunit

Read this introduction, then skim the [1.3 Summary](#13--detection-rules-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 1.3.1 — SIGMA Rules

**Estimated Time:** 25–30 minutes

#### Why This Matters

Sigma expresses a detection idea in a shareable format. Reading its source, field tests, and condition helps you understand what a matching event actually proves and what must be mapped before the rule can run in a local platform.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret a Sigma rule’s purpose, structure, field tests, and condition.
2. Describe the events a rule would match.
3. Create or modify a basic rule and explain its translation to a local query.

#### Understanding the rule structure

A basic Sigma rule uses YAML. The `title` describes the rule, `logsource` identifies the required telemetry, and `detection` contains named selections and a condition. Metadata such as status, references, and false-positive notes helps readers assess the proposal; it does not replace matching logic.

Within a selection, different field tests are normally combined with AND. A list of values for one field is normally OR unless a modifier changes that behavior. Modifiers such as `endswith`, `contains`, and `re` express suffix, substring, or regular-expression tests. Read the condition to see how selections combine.

Sigma can describe many kinds of log sources, not only endpoint logs. Conversion requires a supported backend and field/logsource mappings appropriate to the target platform.

#### Reading a basic proposal

```yaml
title: Training PowerShell Encoded Argument From Script Host
status: experimental
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
    ParentImage|endswith: '\wscript.exe'
    CommandLine|contains: '-enc'
  condition: selection
falsepositives:
  - Authorized automation using the same invocation pattern
level: medium
```

This teaching rule selects a Windows process-creation event whose image ends in `powershell.exe`, whose parent ends in `wscript.exe`, and whose command line contains `-enc`. All three tests must match.

The substring test may include longer arguments or incidental text and can miss other invocation forms. A match establishes the selected pattern, not malicious intent. The experimental status and false-positive note make the proposal's maturity and a plausible benign explanation visible.

#### Modifying and translating the idea

To include both Script Host programs, change the parent selection to a list:

```yaml
    ParentImage|endswith:
      - '\wscript.exe'
      - '\cscript.exe'
```

The list allows either parent while retaining the PowerShell image and command-line tests. In an MDE process-creation query, the corresponding fields are `FileName`, `InitiatingProcessFileName`, and `ProcessCommandLine`; preserve the intended suffix/filename and substring semantics when translating.

A useful proposal explains expected matches, a relevant nonmatch, and known limitations. The course's SOC workflow sends basic rule proposals to Detection Engineering for review and testing under local change procedures.

#### Knowledge Check

1. What do logsource, selections, and condition contribute?
2. Describe exactly what the teaching rule matches and one limitation.
3. Modify the rule to allow wscript.exe or cscript.exe as parent. Does the command-line test still apply?

#### Summary

Sigma makes detection logic shareable. Explain the source, tests, and condition, preserve their meaning during translation, and propose changes with clear expected behavior and limitations.

#### References and Further Reading

- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)
- [Sigma — Conditions](https://sigmahq.io/docs/basics/conditions.html)

### 1.3.2 — Suricata Rules

**Estimated Time:** 25–30 minutes

#### Why This Matters

Suricata rules express conditions to inspect in network traffic. Reading the protocol, direction, and inspection buffer helps explain why a signature matched and whether its meaning agrees with the analyst’s description.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret rule action, header, options, and text/hex/regex matching.
2. Describe a rule’s traffic and match conditions.
3. Create or modify a basic rule and relate a hit to other network evidence.

#### Understanding header and options

A rule begins with an action, followed by protocol, source address/port, direction, destination address/port, and options. This lesson uses the `alert` action. Options include the message, signature identifier (`sid`), revision (`rev`), and match conditions.

`content` can represent literal text or bytes, such as `content:"|4d 5a|";`. A `pcre` expression can match variable text, but its scope and performance need care. Sticky buffers such as `http.method`, `http.uri`, `http.user_agent`, and `tls.sni` select which parsed data subsequent tests inspect.

`$HOME_NET` and `$EXTERNAL_NET` are configured variables. Their actual values determine scope; `$EXTERNAL_NET` is not necessarily defined as the complement of `$HOME_NET`. Confirm them when explaining a rule's direction.

#### Reading a basic proposal

```suricata
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"TRAINING HTTP update path"; flow:established,to_server; http.method; content:"GET"; bsize:3; http.uri; content:"/update.exe"; sid:1000001; rev:1;)
```

The rule alerts on established client-to-server HTTP traffic matching the configured network variables, an exact three-byte GET method, and a normalized URI containing `/update.exe`. The URI content test is a substring: `/folder/update.exe` also fits. This is a classroom example, and its SID is illustrative; operational proposals need an unused identifier from local practice.

A matching Zeek HTTP record may provide request context if Zeek observed and parsed the same traffic. Correlate time and the five-tuple (source/destination IPs and ports plus protocol), accounting for sensor location and translation. A Suricata hit does not guarantee a Zeek record exists.

#### Modifying the matching scope

If the intended target is exactly `/update.exe`, add `bsize:11;` after its URI content test. This excludes longer normalized URI strings, including query strings. If those should be included, the proposal needs a different, explicitly described condition.

A raw `content:"GET"` test on general TCP traffic searches for bytes without the HTTP-method context. Choosing the protocol buffer makes the intent clearer and reduces unrelated matches. For each modification, explain a match and a nonmatch, then pass the proposal for review and testing.

#### Knowledge Check

1. What do the header and sticky buffer each control?
2. Does the example match /folder/update.exe? Explain.
3. Modify the URI test for exactly /update.exe and name an excluded request.

#### Summary

A clear Suricata proposal identifies the traffic scope and the exact buffer and pattern inspected. Explain what matches, what does not, and what related network evidence could add.

#### References and Further Reading

- [Suricata — Rule format](https://docs.suricata.io/en/latest/rules/intro.html)
- [Suricata — HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html)

### 1.3.3 — YARA Rules

**Estimated Time:** 25–30 minutes

#### Why This Matters

YARA examines content supplied to a scanner, such as a file or process memory. Understanding what bytes and conditions a rule tests helps you distinguish a content match from a filename, log entry, or conclusion about maliciousness.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret YARA structure, text/hex/regex patterns, and conditions.
2. Describe what a rule matches in its intended input.
3. Create or modify a basic file rule and explain file-versus-memory limits.

#### Understanding the rule structure

A YARA rule has a name and a required `condition`. Optional `meta` entries describe it, while a `strings` section defines named text, hexadecimal, or regular-expression patterns used by the condition. Not every valid rule needs strings or metadata.

Text such as `"update.exe" ascii nocase` matches that content without case sensitivity. Hexadecimal `{ 4D 5A }` matches the bytes MZ. A regex such as `/update\.(exe|dll)/ nocase` allows alternatives. Conditions can combine patterns with AND/OR, positions such as `$mz at 0`, a count such as `#name >= 2`, or a file-size test.

The scanner must receive the relevant bytes. A network file log that names a hash is not the same input as an extracted file.

#### Reading a basic file rule

```yara
rule Training_Update_Marker
{
    meta:
        description = "Teaching example: MZ prefix and update.exe string"
    strings:
        $mz = { 4D 5A }
        $name = "update.exe" ascii nocase
    condition:
        $mz at 0 and $name and filesize < 5MB
}
```

The rule matches files smaller than 5 MB whose first two bytes are MZ and whose content includes `update.exe`. It does not test the filesystem name. MZ is consistent with a DOS/PE-style header but alone does not validate a complete PE file. The string is intentionally simple for teaching and is not a distinctive malware-family signature.

A benign file could satisfy every condition. Explain a hit as a content match and use additional analysis to determine its significance.

#### Modifying a rule and choosing the input

To require two occurrences of the example name, replace `$name` with `#name >= 2` in the condition. This changes a measurable property of the content; it still does not make the rule a reliable maliciousness verdict.

File and process-memory scans have different semantics. `filesize` is undefined during a process-memory scan, and offsets in memory are virtual addresses rather than file-relative positions. Adapt and test a rule for its intended input instead of assuming a file rule will work unchanged in memory. The basic proposal here remains a file rule for review by Detection Engineering.

#### Knowledge Check

1. What does the teaching rule match, and does the filename itself matter?
2. Modify the rule to require two occurrences of the name.
3. Why should the same rule not be assumed to work as intended on process memory?

#### Summary

A YARA description explains the supplied input, patterns, and condition. Basic modifications should have predictable matching behavior, and file versus memory use requires attention to input semantics.

#### References and Further Reading

- [YARA — Writing rules](https://yara.readthedocs.io/en/stable/writingrules.html)
- [YARA — Command-line input options](https://yara.readthedocs.io/en/stable/commandline.html)

### 1.3.4 — SIEM Rules

**Estimated Time:** 25–30 minutes

#### Why This Matters

A saved detection combines search logic with operating settings that determine when and how an alert is created. Reading both parts explains what an alert represents and helps turn a query into a reviewable detection proposal.

#### Learning Objectives

By the end of this module, you will be able to:

1. Identify the source, logic, timing, trigger, and output of a saved detection.
2. Explain what a rule would match and what would create an alert.
3. Create a basic proposal from known log fields or a Sigma rule.

#### Understanding the detection proposal

| Component | What to specify |
|---|---|
| Name and purpose | The activity the detection is intended to identify. |
| Source | Required table, event types, and populated fields. |
| Logic | Matching predicates and any grouping, count, or threshold. |
| Lookback | How far back each run searches. |
| Frequency | How often it runs; distinct from lookback. |
| Output | Evidence and entity fields needed to investigate a result. |
| Alert behavior | How matches become alerts and how repeated matches are handled. |

A basic rule can filter one table; joining multiple sources is not required. A broad search may be useful for exploration, but a detection proposal should explain why the returned activity warrants attention and how much routine activity it may include.

#### Reading a worked proposal

**Name:** PowerShell encoded argument from Script Host. **Classroom schedule:** run every five minutes with a five-minute lookback. **Trigger:** one or more matching events. **Output:** event and host identifiers plus the command-line context below. Grouping and duplicate handling remain settings to confirm in the target platform.

```kusto
DeviceProcessEvents
| where Timestamp > ago(5m)
| where ActionType == "ProcessCreated"
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName =~ "wscript.exe"
| where ProcessCommandLine contains "-enc"
| project Timestamp, DeviceId, DeviceName, ReportId, AccountName,
          ProcessCommandLine, InitiatingProcessCommandLine
```

This KQL illustrates the three-field process pattern. It requires the supported MDE source and action. The simplified schedule may miss late-arriving data; a deployable rule needs appropriate lookback, timing, and duplicate handling. It has not been validated against a live tenant.

#### Creating or translating a basic rule

From log fields, choose the operation and predicates that express the target behavior, then specify schedule, trigger, and outputs. From Sigma, map `logsource` to the appropriate table/event and preserve the meaning of selections and condition. Translation is more than renaming fields.

Choose comparison operators according to the question. In KQL, `contains` is a substring operation, `has` is term-based, and `=~` is case-insensitive equality. A literal asterisk inside `contains` is not a general wildcard. Other SIEM languages have different wildcard and regex rules. Use regex when its additional pattern control is needed and describe the intended matches.

For example, broadening the parent predicate to `InitiatingProcessFileName in~ ("wscript.exe", "cscript.exe")` includes either Script Host program while retaining the other conditions. Submit the proposal with a matching and nonmatching example for review.

#### Knowledge Check

1. How do lookback and run frequency differ?
2. Describe the example’s matching logic and trigger.
3. Create a modified proposal that permits both Script Host parents. What besides the predicate should it specify?

#### Summary

A SIEM detection proposal connects clear logic to a source, schedule, trigger, and useful output. Preserve matching semantics when translating Sigma and review timing and alert behavior before deployment.

#### References and Further Reading

- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators)
- [Microsoft — Custom detection rules](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)

### 1.3 – Detection Rules: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Evidence source → rule conditions → match → investigation → tuning or change when justified**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- explain what evidence each rule family is designed to evaluate;
- read the main parts of SIGMA, Suricata, YARA, and SIEM detection logic;
- describe why a rule matched without equating the match with maliciousness;
- make or assess a simple rule change while preserving its intended detection purpose.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.3.1 – SIGMA Rules** | Read and modify portable detection logic that describes log-event conditions. |
| **1.3.2 – Suricata Rules** | Read and modify network-signature logic over packet or protocol evidence. |
| **1.3.3 – YARA Rules** | Read and modify pattern-matching logic for files, memory, or other scanned content. |
| **1.3.4 – SIEM Rules** | Read and modify analytic logic in the local query/detection environment. |

#### Check Your Understanding

Ask yourself:

1. Why does knowing the evidence layer matter before you interpret a detection rule?
2. What is the difference between explaining why a rule matched and deciding what the matched activity means?
3. When you change one condition in a rule, what should you consider about the activity the rule will now include or exclude?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **1.4 – Alert Investigation and Assessment: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 1.4 – Alert Investigation and Assessment: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

An alert is a starting point for investigation, not the finished judgment. SOC analysts need to gather context, determine what the evidence establishes, classify the result, understand common causes of benign matches, place the work in the right operational category, and meet response-time expectations.

#### Connect to What You Already Know

Detection lessons showed how analytic logic produces matches. This subunit begins with that fired object and develops the investigation and decision-making that turn a match into an operational SOC result.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.4.1 – Alert Context and Investigation** | Gather the host, user, process, file, network, and other context needed to understand the alert. |
| **1.4.2 – Alert Classification** | Classify the investigated alert using evidence and the detection expectation. |
| **1.4.3 – Common False Positive Causes** | Recognize why legitimate activity can satisfy detection conditions. |
| **1.4.4 – Common Alert Categorizations** | Place investigated activity into the operational categories used for routing and reporting. |
| **1.4.5 – SLA / Response Time Goals** | Apply the relevant response-time goal and understand which event starts the clock. |

#### What to Watch For

- Distinguish what the alert says from what investigation adds.
- Tie classification to the relevant detection expectation and checked evidence, not to intuition alone.
- Keep categorization, priority, and timing connected to the actual operational requirement.

#### Expected End State

By the end of this subunit, you should be able to:

- identify the context needed to investigate an alert;
- classify an alert using the available evidence and the expected detection outcome;
- explain common reasons legitimate activity may match a detection;
- apply the appropriate category and response-time expectation without confusing separate clocks.

#### How to Preview This Subunit

Read this introduction, then skim the [1.4 Summary](#14--alert-investigation-and-assessment-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 1.4.1 — Alert Context and Investigation

**Estimated Time:** 30 minutes

#### Why This Matters

An alert is the starting point for an investigation. Before deciding what it means, establish what evidence it contains, what logic produced it, and what related records can add. This makes the eventual finding traceable to observations rather than to the alert title alone.

#### Learning Objectives

By the end of this module, you will be able to:

1. Identify present and missing alert context, including an approved lookup of an available indicator.
2. Explain the alert configuration and trace its actual upstream detection path.
3. Select related endpoint logs and describe what they add or fail to add.
4. Select related PCAP for a network question and describe its contribution or availability limit.

#### Establishing context and detection lineage

For the course process alert, record the host, account, event time, alert time, rule name/version, and the matched process fields. Separate facts already present from questions still open. The example shows `wscript.exe` launching PowerShell with an encoded-command argument as `jlee`; the decoded behavior and authorization are not yet supplied.

Read the configuration and explain what would fire: the process-created event must satisfy the image, parent, and command-line predicates, together with the rule's trigger settings. Trace the actual upstream path. A SIEM-only example is endpoint event → ingested table → SIEM rule → alert. A network example could be Suricata signature → Suricata alert ingested into the SIEM → correlation rule → SIEM alert. Use rule IDs and source references to establish which path applies.

#### Adding relevant evidence

| Evidence source | How to use it | What to record |
|---|---|---|
| Related endpoint events | Select the host and relevant time, then correlate process identity, paths, account, and operation. | What each event adds and any unresolved gap. |
| VirusTotal lookup | Look up an available hash, IP, or domain through the approved workflow. | The exact indicator, report reference/time, relevant result, and interpretation limit. |
| Related PCAP | Request retained traffic for a relevant flow, time range, and sensor. | What becomes visible beyond the alert, or why the capture cannot answer the question. |

A file event for `invoice.vbs` may add a path and initiating process; its mere proximity in time does not establish causation. A lookup with no known detections or no report does not establish safety. Keep public submission handling consistent with module 0.7.

For a process-only alert, first determine whether a related network question and flow exist. Distinguish “not relevant to the current question,” “not collected or retained,” and “searched but no related packets found.” These are different outcomes. Encryption may leave application content unavailable even when a capture exists.

#### Working through a reviewable finding

For the supplied classroom process alert, a useful initial record could state:

- **Present:** host `WS-JLEE`, account `jlee`, the creation event, Script Host parent, and encoded-command argument.
- **Logic:** the SIEM rule selects that three-field pattern; the lineage is endpoint event → table → rule → alert.
- **Added endpoint evidence:** a supplied file event records `invoice.vbs` at a Temp path. Its relationship to the launch should be supported by the path and process context.
- **Lookup:** if a hash or IP becomes available, record the actual lookup result or that the lookup is still pending. No real service result is supplied by this example.
- **PCAP:** no related flow is supplied yet, so identify the network question before requesting traffic.
- **Still open:** decoded command behavior, authorization, and any related execution or communication.

For a separate network example, retained cleartext HTTP packets can add `/update.exe` when the alert contained only IP and port. Record that contribution and the packet/time reference. The result should show how the additional evidence changes understanding.

#### Knowledge Check

1. For the process example, identify what context is present and missing, then explain the SIEM rule configuration and upstream event-to-alert path.
2. You have a related hash and a file event. What should collection and a VirusTotal lookup contribute, and what would each still leave unresolved?
3. A network alert has IP/port only. What would you request from PCAP, and how would you document an unavailable capture?

#### Summary

An investigation record should explain the alert’s evidence, logic, and lineage, then show what related endpoint records, lookups, and packets contribute. Clear unresolved questions make the next decision easier to support.

#### References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching)
- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html)

### 1.4.2 — Alert Classification

**Estimated Time:** 20–25 minutes

#### Why This Matters

Classification compares a detection result with an assessed condition. Keeping those two questions separate helps you distinguish a useful alert, a false alarm, and activity that was missed. Each label needs evidence about both the activity and the detection outcome.

#### Learning Objectives

By the end of this module, you will be able to:

1. Define TP, FP, TN, and FN against an explicit target condition.
2. Classify supplied cases and cite activity evidence and detection outcome.
3. Recognize uncertainty and the evidence needed to establish a false negative.

#### Defining what counts as positive

First state the condition being evaluated. For this lesson, the target condition is malicious or unauthorized activity within the stated detection requirement. A positive result means the relevant detection alerted; a negative result means it did not alert within the defined scope and time.

| Label | Detection result | Assessed target condition |
|---|---|---|
| True positive (TP) | Alerted. | Present. |
| False positive (FP) | Alerted. | Absent. |
| True negative (TN) | Did not alert. | Absent. |
| False negative (FN) | Did not alert. | Present and within the expected detection requirement. |

A rule can correctly match a technical behavior that is authorized. Some products label this “informational/expected activity” or a benign positive. Apply the local platform's definitions and explain your basis. When evidence is insufficient, record an unresolved assessment instead of forcing a benign or malicious label.

#### Classifying evidence-supported examples

| Supplied classroom case | Classification and reason |
|---|---|
| The Script Host/PowerShell rule alerts; follow-up evidence confirms the command performed unauthorized activity within the rule's intended scope. | TP: the alert and assessed target condition are both present. |
| An overly broad threat rule alerts on interactive `Get-Help`; the activity is verified as authorized helpdesk use. | FP against this lesson's threat condition: an alert occurred but the target condition is absent. |
| Verified ordinary browsing is within the evaluation sample and the relevant detector produces no alert. | TN: the target condition and alert are both absent. |
| A download is independently confirmed malicious and within required coverage; relevant logs show it occurred, but a checked alert record shows no alert during the evaluated period. | FN: the required target condition occurred without the expected alert. |

The command-line pattern alone does not confirm maliciousness. Likewise, `/update.exe` plus an empty queue does not by itself establish an FN: you need the maliciousness assessment, coverage expectation, and a reliable check for the relevant alert.

#### Writing the classification and evidence

Record the label, the condition being assessed, the evidence supporting that assessment, and the detection outcome. For an FN, include the checked rule/source, time range, and whether the necessary telemetry reached the detection system. If the source was absent, identify the visibility failure rather than automatically blaming rule logic.

TN and FN usually arise from reviewing activity beyond fired alerts, such as a scoped test, related evidence, or a hunt. An alert queue alone cannot establish that all unalerted activity was benign. Classification should remain revisable when new evidence changes the assessment.

#### Knowledge Check

1. Classify the four supplied cases and cite both sides of each decision.
2. Does confirmed wscript-to-encoded-PowerShell behavior alone establish a malicious true positive?
3. What is needed before calling an unalerted download a false negative?

#### Summary

Classify the detection outcome against an explicit, evidence-supported target condition. Preserve uncertainty, use local disposition definitions, and investigate misses using both activity evidence and the expected coverage.

#### References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Microsoft — Alert classification playbooks](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-playbooks)

### 1.4.3 — Common False Positive Causes

**Estimated Time:** 20–25 minutes

#### Why This Matters

Once an alert is assessed as a false positive, the explanation can help reduce repeated unnecessary work. A useful recommendation connects the benign activity to the logic that matched and proposes a specific change with an understood effect on coverage.

#### Learning Objectives

By the end of this module, you will be able to:

1. Recognize analyst/tool activity and overly broad logic as common causes.
2. Identify a supported cause for a supplied false positive.
3. Propose a specific change and explain its coverage tradeoff.

#### Recognizing two common causes

| Cause class | Example | Direction for a proposal |
|---|---|---|
| Analyst or tool activity | An authorized scanner or documented test/replay produces the observed pattern. | Separate test traffic or narrowly identify the approved activity. |
| Untuned or overly broad logic | A threat rule matches every PowerShell process, including verified helpdesk use. | Align predicates or thresholds with the intended threat condition. |

These two classes organize the lesson; they are not an exhaustive operational taxonomy. They can overlap. A scanner is not automatically benign merely because it is organization-owned, and an accurate behavior match may be classified as expected activity by the local product. Begin with the established assessment and authorization evidence.

#### Working through a recommendation

For a threat rule that matches any PowerShell process, verified interactive `Get-Help` is routine activity. If the intended requirement is specifically encoded PowerShell from Script Host, propose the image, parent, and command-line predicates that express that requirement. Explain that this narrows coverage and does not detect every form of PowerShell misuse.

For a documented packet replay that causes production alerts, propose using a designated test path or a narrowly scoped test-traffic treatment tied to the verified source and period. A blanket exclusion of all scanner or analyst activity can hide unexpected activity from those systems.

#### Making the change reviewable

A concise recommendation should include the cause class, supporting evidence, the exact proposed change, and an expected match and nonmatch. For example: “Overly broad logic: the rule matched authorized help commands. For the Script Host requirement, add the parent and encoded-argument tests; a matching script-host launch should remain visible, while ordinary interactive help should not match.”

Detection Engineering reviews the proposal, checks representative legitimate and suspicious cases, and manages changes under local procedures. If the evidence does not fit either taught cause, describe the observed cause and uncertainty without forcing a category.

#### Knowledge Check

1. What are the two cause classes taught here, and can they overlap?
2. For verified Get-Help noise on an any-PowerShell threat rule, propose a change tied to the Script Host requirement.
3. Why is excluding every event from a scanner a weak recommendation?

#### Summary

Explain why the benign activity matched, then propose a concrete change tied to the detection requirement. Review its effect on expected matches and missed activity before it is applied.

#### References and Further Reading

- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)
- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html)

### 1.4.4 — Common Alert Categorizations

**Estimated Time:** 20–25 minutes

#### Why This Matters

An activity category tells the next analyst what kind of behavior or access the evidence supports. It serves a different purpose from TP/FP classification, which evaluates a detection result. Clear category reasoning helps avoid overstating an attacker’s access.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe the syllabus activity categories and their local use.
2. Assign a supported category to a supplied event.
3. Explain why a plausible adjacent category is less supported.

#### Using the course categories

These are the syllabus categories, not a universal taxonomy. Use the definitions and labels adopted by your organization when applying them at work.

| Category | Evidence that supports it | Useful distinction |
|---|---|---|
| Scanning / reconnaissance | Probing intended to discover hosts, services, or other information. | Compare discovery activity with a failed access attempt. |
| Root-level access | Evidence of privileged control, such as root, SYSTEM, or relevant elevated administrative execution. | A service account or service process is not automatically privileged. |
| User-level access | Evidence of activity within a standard or non-elevated user execution context. | A suspicious command does not itself establish elevation. |
| Unsuccessful activity | Evidence that an access or exploitation attempt failed. | Distinguish the attempted action from a discovery probe. |
| Other (local) | An applicable category defined by the organization. | Use its actual definition rather than inventing a local label. |

Activities may be mixed or incompletely observed. Choose the category supported for the described activity and explain uncertainty or additional categories according to local practice.

#### Comparing similar cases

A separate classroom PowerShell example (not A12) runs under `labuser` with a recorded Medium integrity, non-elevated context. That supports user-level activity for this event. It does not prove that the account lacks every administrative membership or that no privileged activity occurred elsewhere.

If another supplied event establishes SYSTEM execution, privileged activity is supported for that event. A process name or “service” label alone is insufficient to make that change.

A pattern of probing many ports with no supplied authentication attempt supports scanning/reconnaissance. A documented failed login supports unsuccessful access activity. An HTTP 401 alone can be part of normal authentication, so corroborate an actual failed access attempt before categorizing a sequence on that basis.

#### Writing a justified category

Write the category, cite the supporting operation or privilege evidence, and explain why a plausible alternative is less supported. For example: “User-level activity: this process ran in the supplied non-elevated user context. The event supplies no privileged execution supporting root-level access.”

This comparison is a reasoning check. It does not require all possible categories to be mutually exclusive. An ATT&CK mapping may add a behavior description, while the local activity category continues to serve its own reporting purpose.

#### Knowledge Check

1. Name the four syllabus categories and explain how Other is used.
2. Categorize the supplied non-elevated labuser event and explain why root-level is unsupported.
3. How would you distinguish a port sweep from a failed login, and why is HTTP 401 alone insufficient?

#### Summary

Choose an activity category from the observed behavior and access context. Explain the evidence and a plausible alternative, and use local definitions for mixed activity or additional categories.

#### References and Further Reading

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)

### 1.4.5 — SLA / Response Time Goals

**Estimated Time:** 20–25 minutes

#### Why This Matters

Response-time goals help ensure an alert receives attention and reaches an appropriate next state. Keeping each goal’s start point and completion event explicit makes overdue work visible without encouraging premature closure.

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the start and close/escalate clocks and their origins.
2. Calculate which response-time goal is at risk or breached.
3. Record a supported closure or escalation against the correct clock.

#### Understanding the two classroom clocks

An SLA can contain several commitments. This lesson focuses on two response-time goals, called clocks for convenience. The numbers and start points below are classroom assumptions, not workplace requirements.

| Clock | Starts at | Completed by | Classroom goal |
|---|---|---|---|
| Start | Alert creation. | Recorded beginning of investigation. | 15 minutes. |
| Close / escalate | Beginning of investigation. | Supported closure or documented escalation. | 45 minutes. |

Before investigation begins, the start clock is running and the second clock has not started in this model. Afterward, preserve whether the start goal was met or breached while tracking close/escalate. Real procedures may use different origins, severity tiers, pauses, or deadlines; consult them rather than transferring these numbers directly.

#### Calculating status from timestamps

Use one stated time zone and a complete date where needed. Compute the due time from the defined origin before deciding which clock needs attention.

| Supplied facts | Calculation | Status |
|---|---|---|
| Created 14:00; untouched at 14:18. | Start due 14:15; elapsed 18 minutes. | Start breached by 3 minutes. |
| Created 13:20; started 13:28; open at 14:20. | Start took 8 minutes. Close/escalate due 14:13; elapsed 52 minutes since start. | Start met; close/escalate breached by 7 minutes. |

A goal is breached after its deadline. Before the deadline, it may be at risk if the remaining work is unlikely to finish in time. State the evidence for that forecast. If only the start timestamp is supplied, the earlier start-goal result cannot be reconstructed without creation time.

#### Recording the appropriate action

For the first example, begin the investigation and record `started | start breached | 14:18`, with the creation time and due time retained. For the second, record a supported closure if the work is complete, or document escalation, the reason, receiving owner, and time if further handling is needed.

A classroom escalation line could be `escalated | close/escalate breached | 14:20 | unresolved investigation; duty lead notified`. Escalation records a transfer or request for attention; local procedure determines whether acceptance is also required. A breached goal remains breached after the action. Keep the investigation finding and the timing record consistent.

#### Knowledge Check

1. Created 14:00 and untouched at 14:18: which clock applies, when was it due, and what is the first action?
2. Created 13:20, started 13:28, and open at 14:20: calculate both clock results.
3. Write an appropriate record for the second case if the investigation still needs the duty lead’s help.

#### Summary

Identify the applicable clock, calculate its due time, and record the action actually taken. Preserve both timing status and investigation state, using the organization’s definitions outside the classroom.

#### References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

### 1.4 – Alert Investigation and Assessment: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Alert → context → evidence assessment → classification/category → response timing and handoff**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- identify the context needed to investigate an alert;
- classify an alert using the available evidence and the expected detection outcome;
- explain common reasons legitimate activity may match a detection;
- apply the appropriate category and response-time expectation without confusing separate clocks.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.4.1 – Alert Context and Investigation** | Gather the host, user, process, file, network, and other context needed to understand the alert. |
| **1.4.2 – Alert Classification** | Classify the investigated alert using evidence and the detection expectation. |
| **1.4.3 – Common False Positive Causes** | Recognize why legitimate activity can satisfy detection conditions. |
| **1.4.4 – Common Alert Categorizations** | Place investigated activity into the operational categories used for routing and reporting. |
| **1.4.5 – SLA / Response Time Goals** | Apply the relevant response-time goal and understand which event starts the clock. |

#### Check Your Understanding

Ask yourself:

1. What additional context would you seek before deciding what a process alert means?
2. Why is a disliked or noisy alert not automatically a false positive?
3. What must you identify before calculating whether an SLA or response-time goal was met?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **1.5 – Reporting and Notification: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 1.5 – Reporting and Notification: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

SOC work becomes useful to the rest of the organization when the right product reaches the right audience on time. Reporting is therefore part of the investigation workflow, not an afterthought.

#### Connect to What You Already Know

The alert subunit ended with an assessed result, operational category, and response-time expectations. This subunit focuses on how that result becomes a report, notification, request, or handoff.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **1.5.1 – Report Types** | Choose the product type that matches the purpose of the communication. |
| **1.5.2 – Reporting Timeline Requirements** | Apply the timing requirement associated with the product or event. |
| **1.5.3 – Notification and Distribution** | Route the product to the correct recipients through the approved channel. |

#### What to Watch For

- Choose the product from the question and audience, not from habit.
- Keep the reporting clock tied to the event that actually starts it.
- Treat recipient, awareness, and channel choices as part of the product design.

#### Expected End State

By the end of this subunit, you should be able to:

- select an appropriate SOC report or request type for the communication need;
- identify the timing requirement and its correct start point;
- route the product to the appropriate recipients through the approved channel;
- separate the contents needed by different audiences instead of sending one undifferentiated report to everyone.

#### How to Preview This Subunit

Read this introduction, then skim the [1.5 Summary](#15--reporting-and-notification-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 1.5.1 — Report Types

**Estimated Time:** 20–25 minutes

#### Why This Matters

Report selection begins with the purpose of the communication. An incident report records a case and supports response, while an RFI asks a question needed by the work. The same incident can require both products.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe incident reports, RFIs, and local report types.
2. Select the type suited to a supplied reporting purpose.
3. Explain why a plausible alternative serves a different purpose.

#### Choosing the product by purpose

| Type | Primary purpose | Useful comparison |
|---|---|---|
| Incident report | Records an incident or supported suspected incident for handling under local criteria. | An RFI asks for information rather than replacing the incident record. |
| Request for Information (RFI) | States a question and needed information or analysis, with relevant context. | It can link to an existing case without creating a duplicate incident. |
| Other (local) | Meets a reporting purpose defined by the organization. | Use the actual type and instructions applicable to that purpose. |

An RFI may go to CTI or another responsible function. In this course, a question requiring intelligence analysis provides the connection into the CTI track. The type describes the requested product, while routing procedures determine the recipient and channel.

#### Working through the course case

For this example, assume the investigation of case `A12` on `WS-JLEE` has met the organization's criteria for a suspected incident and IR handoff. The supporting case record includes the Script Host/PowerShell activity and the evidence for that escalation decision. The command pattern alone is not the incident determination.

The product recording the case for response is an incident report. If the analyst also needs CTI to assess the role of a related domain or file, an RFI can state that question and link to A12. The RFI has a separate purpose even if the system stores it within the same case record.

#### Explaining the choice

State the selected type and explain the purpose that makes it appropriate. For example: “RFI: A12 already records the incident, and this product asks CTI to assess the domain's role. It should link to A12 so CTI can use the existing evidence.”

Conversely, when the task is to record and hand off the supported incident itself, select the incident report. The presence of unanswered questions does not prevent reporting a suspected incident under local criteria. This lesson focuses on choosing the product; the next lessons connect it to a deadline and an approved route.

#### Knowledge Check

1. How do an incident report and an RFI differ?
2. A12 is already open and CTI is asked to assess a related domain. Which type fits, and why?
3. If a suspected incident meets reporting criteria but attribution is unknown, should the incident record wait for the RFI answer?

#### Summary

Select the report type by the work it must accomplish. Record the supported incident and use linked RFIs for additional questions, following the organization’s definitions for other products.

#### References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)

### 1.5.2 — Reporting Timeline Requirements

**Estimated Time:** 20–25 minutes

#### Why This Matters

Reporting deadlines keep useful information moving while an investigation continues. A submission deadline and a blocker-escalation deadline can run at the same time, so recording their separate start points helps you act on both.

#### Learning Objectives

By the end of this module, you will be able to:

1. Describe submission and blocker-escalation clocks.
2. Calculate applicable deadlines from supplied timestamps.
3. Distinguish an at-risk deadline from one already breached.

#### Understanding the classroom reporting clocks

The following times are classroom assumptions, separate from the alert-response clocks in 1.4.5. Operational and contractual requirements must come from the organization's current procedures.

| Clock | Origin | Classroom limit |
|---|---|---|
| Submit incident report | Decision that an incident report is required. | 30 minutes. |
| Submit RFI | The information question arises. | 60 minutes. |
| Escalate for more information | A blocker prevents completion without help from another function. | 15 minutes. |

A blocker does not pause the submission clock in this example. Escalating the blocker and submitting an available preliminary report may both be needed, according to the applicable process. Other local report types may have their own deadlines.

#### Calculating overlapping deadlines

| Supplied situation | Due time and status |
|---|---|
| RFI question at 13:30; unsent at 14:40. | RFI due 14:30; breached by 10 minutes. |
| Incident-report decision at 14:00; blocked at 14:10; still blocked at 14:28. | Blocker escalation due 14:25; breached by 3 minutes. Incident report due 14:30; 2 minutes remain. |

In the second example, the submission deadline has not passed, but it is at risk because the blocker remains with little time available. Name both clocks and their status. The overdue escalation deserves immediate action while the submission obligation remains visible.

#### Recording the timing decision

Use a record that makes the report type, origin, due time, current state, and next action clear. For the blocked incident example: “Incident report due 14:30; blocker escalation due 14:25 and overdue at 14:28. Escalate the missing-information need now and coordinate the available submission under the reporting procedure.”

Keep actual timestamps when actions occur. An escalation does not retroactively meet a missed deadline, and completing an alert does not automatically submit its report. Use a consistent time zone and dates when the work crosses midnight.

#### Knowledge Check

1. When does each classroom reporting clock begin?
2. Calculate the RFI status for a 13:30 question still unsent at 14:40.
3. At 14:28, an incident report was required at 14:00 and blocked at 14:10. Identify both deadlines and the next action.

#### Summary

Track submission by report type and escalation from the time a blocker arises. When both apply, retain both due times and act on the blocker without losing the submission requirement.

#### References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

### 1.5.3 — Notification and Distribution

**Estimated Time:** 20–25 minutes

#### Why This Matters

A report becomes useful when it reaches the responsible people through a channel that supports the work. A notification chart connects the product to recipients, leadership awareness, and the approved means of delivery.

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret a notification chart’s recipients, awareness requirements, and channels.
2. Route a supplied report using the chart.
3. Explain why an alternative route does not meet the stated requirements.

#### Reading a notification chart

The chart below is a classroom example, not a universal routing policy.

| Product | Work recipients | Leadership awareness | Approved classroom channel |
|---|---|---|---|
| Incident report | SOC queue and IR. | Yes, through the duty SOC lead. | The case-system ticket. |
| RFI | The named responsible team, such as CTI, Hunt, or IT. | No routine separate notification unless requested or required. | Ticket or approved RFI form. |

“Leadership awareness” identifies the relevant leadership role and purpose; it does not automatically mean contacting the most senior executive. Real routing may depend on severity, incident type, sensitivity, and local agreements. Use the actual chart and escalation path when applying the lesson.

#### Routing the course examples

For the first IR handoff of supported case A12, route the incident record to the SOC queue and IR through the case-system ticket and provide awareness to the duty SOC lead. Include a clear link or reference to the evidence and work being handed off.

For an RFI asking CTI to assess the related domain, name CTI as the recipient and use the ticket or approved RFI form. Under this classroom chart, no separate leadership notification is routinely required. If leadership requested the answer or another policy applies, record that requirement.

Personal SMS, private chat, and personal email are outside the approved classroom routes. The issue is whether the chosen path provides the required access, record, and handling—not the mere fact that a tool is called chat or email.

#### Making the handoff traceable

A concise routing record names the recipients, leadership-awareness decision, approved channel, and reason a proposed alternative does not satisfy the chart. For example: “A12 incident report → SOC queue and IR; duty SOC lead informed; case-system ticket. A private message to one responder does not place the case in the required queue.”

Follow local requirements for acceptance, acknowledgement, or urgent supplementary notification. Keep the official record aligned with the action taken so another analyst can see who owns the next step. This completes the SOC reporting sequence; the CTI track develops how an intelligence question becomes an answer.

#### Knowledge Check

1. What does a notification chart tell you?
2. Route the first A12 incident handoff using the classroom chart and reject an unsuitable alternative.
3. Route the CTI RFI and explain when the leadership decision could change.

#### Summary

Use the notification chart to route the product, provide appropriate leadership awareness, and preserve a traceable handoff. The approved route connects the completed SOC work to the next responsible function.

#### References and Further Reading

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center)

### 1.5 – Reporting and Notification: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Assessed result → product type → timing → recipients/channel → handoff**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- select an appropriate SOC report or request type for the communication need;
- identify the timing requirement and its correct start point;
- route the product to the appropriate recipients through the approved channel;
- separate the contents needed by different audiences instead of sending one undifferentiated report to everyone.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **1.5.1 – Report Types** | Choose the product type that matches the purpose of the communication. |
| **1.5.2 – Reporting Timeline Requirements** | Apply the timing requirement associated with the product or event. |
| **1.5.3 – Notification and Distribution** | Route the product to the correct recipients through the approved channel. |

#### Check Your Understanding

Ask yourself:

1. How does an incident report differ in purpose from an RFI?
2. Why is the start event for a reporting clock as important as the allowed duration?
3. What should determine whether leadership, IR, CTI, or another team receives a product?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **1.6 – SOC Analyst Section Summary**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 1.6 — SOC Analyst Section Summary

**Estimated Time:** 15–20 minutes  

#### Purpose

Module 1.0 introduced the SOC block as an evidence-to-handoff workflow.

Module 1.6 closes that loop.

By this point, you have learned how to read endpoint evidence, interpret network evidence, understand what detection logic matched, investigate and assess alerts, and communicate the result through the correct reporting path.

The summary returns to the same model:

**Endpoint evidence → Network evidence → Detection logic → Alert investigation → Reporting / handoff**

Or more simply:

**Observe → Detect → Investigate → Communicate**

#### What You Can Now Do

The 1.x block is designed to give you a complete SOC foundation.

You should now be able to:

- describe host activity from endpoint telemetry;
- describe network activity from Zeek without claiming visibility the sensor does not have;
- explain what basic detection logic is designed to match;
- investigate an alert beyond its title;
- classify what the detection did;
- identify likely false-positive causes without confusing cause with classification;
- distinguish activity category from TP/FP/TN/FN;
- track the correct response and reporting timelines;
- choose the correct report or request;
- route the result through the approved handoff path.

The important skill is not memorizing isolated fields.

It is being able to connect the evidence into a defensible operational story.

#### The 1.x Block at a Glance

| Unit | Core skill retained |
|---|---|
| **1.1 – Endpoint** | Explain what happened on the host and which process, user, file, registry, network, or image/driver activity was involved. |
| **1.2 – Zeek** | Explain what happened on the wire and what the network sensor can—and cannot—support. |
| **1.3 – Detection** | Read basic Sigma, Suricata, YARA, and SIEM logic and explain what causes the rule to match. |
| **1.4 – Alerts** | Gather context, investigate, classify, identify false-positive causes, categorize activity, and manage response-time goals. |
| **1.5 – Reporting** | Choose the right report or request, identify the applicable timeline, and route it through the approved path. |

These are not separate jobs.

They are stages of one SOC workflow.

#### A12 End to End

The A12 scenario shows how the pieces fit together.

##### Step 1 – Endpoint evidence

On `WS-JLEE`, endpoint telemetry shows:

- `wscript.exe` launches PowerShell;
- the PowerShell command is encoded;
- additional file, registry, or network activity may appear around the same time.

The endpoint view answers questions such as:

> Which process ran?  
> Which user context was involved?  
> Which process touched the file or registry?  
> Which process initiated a network connection?

The evidence should be described before deciding what it means.

##### Step 2 – Network evidence

Zeek or other network telemetry shows activity such as:

- the host communicates with external infrastructure;
- a DNS lookup occurs;
- an HTTP request includes `/update.exe`;
- a TLS or connection record supplies additional context.

The network view answers a different set of questions:

> Which systems communicated?  
> What protocol activity was visible?  
> Which name, URI, or transferred artifact appeared on the wire?

The network sensor normally cannot tell you which local process opened the connection.

That fact comes from endpoint telemetry.

##### Step 3 – Detection logic

A rule fires because observed data matches its conditions.

The analyst should be able to explain:

> **What part of the event caused this detection to match?**

For example:
- encoded PowerShell;
- a specific URI;
- a byte/string pattern;
- a field combination in SIEM data.

A detection match tells you that the rule condition was satisfied.

It does not, by itself, prove maliciousness.

##### Step 4 – Alert investigation

Now combine the available context.

The analyst asks:

- What actually happened?
- Which observations support the conclusion?
- What evidence is still missing?
- Does the activity fit expected behavior?
- Does the alert need escalation?
- Is there a tuning or coverage issue?

The alert title is the starting point, not the final answer.

##### Step 5 – Assessment

Several different labels may be required.

Keep them separate.

**Detection classification**
- True Positive
- False Positive
- True Negative
- False Negative

**Activity category**
- scanning/reconnaissance
- user-level access
- root-level access
- unsuccessful activity
- another locally defined category

**False-positive cause**
- analyst/tool activity
- overly broad or untuned logic
- another locally recognized explanation

These answer different questions.

##### Step 6 – Reporting and handoff

The investigation now becomes something another team can use.

For A12, that may include:

**Incident report**
> Record the suspected or confirmed security case and hand it to IR through the approved workflow.

**RFI**
> Ask CTI, hunt, IT, or another team a bounded question needed to continue the case.

The report or request should preserve:
- important observations;
- the analyst's conclusion;
- evidence supporting the conclusion;
- important uncertainty or gaps;
- what the next team needs to do or answer.

#### Distinctions That Keep a SOC Assessment Precise

Several SOC concepts sit close together in the workflow. Keeping the question behind each one clear prevents a correct observation from turning into an unsupported conclusion.

##### Observations and conclusions require different levels of support

> `wscript.exe` launched encoded PowerShell.

is a direct observation from the process evidence.

> The host is compromised.

is a broader conclusion. It may eventually be justified, but it requires additional evidence and reasoning. A strong investigation shows the path from the observation to the conclusion instead of treating them as equivalent statements.

##### Endpoint and network telemetry answer different questions

Endpoint telemetry can often identify the process, user, file, registry activity, and host-local context. Network telemetry can describe the connection or protocol transaction visible to the sensor.

When the two views are correlated, preserve which source supplied each field. That makes the finding reviewable and prevents host-only context from being silently attributed to a network sensor, or vice versa.

##### A detection match establishes that the logic matched; investigation establishes what the activity means

When a rule fires, the analyst knows that the event satisfied the rule's conditions. Classification requires the next layer of evidence: whether the assessed target condition was actually present.

This is why a rule match can justify investigation without automatically proving maliciousness.

##### Detection classification and activity category answer different questions

**TP / FP / TN / FN** describe the relationship between the detection outcome and the assessed target condition.

A category such as **user-level access**, **root-level access**, or **scanning/reconnaissance** describes the kind of activity observed.

An investigation may need both labels because neither one replaces the other.

##### Classification and false-positive cause are separate judgments

Calling an alert a **False Positive** answers whether the alert represented the target condition being evaluated.

Explaining that benign helpdesk activity or overly broad logic caused the match answers **why** the false positive occurred. Separating those questions makes tuning recommendations more useful.

##### Alert-response and reporting timelines may start from different events

The alert queue may have a response-time goal while an incident report or RFI has a separate submission clock. Track the trigger, due time, and current state for the specific obligation you are measuring.

##### Incident reports and RFIs carry different products

An incident report records and routes the security case. An RFI asks another team a bounded question needed to advance the work.

They can exist beside one another because the case and the unanswered question are related but different products.

##### A correct recipient still requires an approved delivery path

Knowing who needs the information is only part of a handoff. Sensitive operational information also needs to move through the approved channel so handling, accountability, and recordkeeping are preserved.

#### Integrated Review Exercise

Use this evidence card:

> **Host:** `WS-JLEE`  
> **User:** `jlee`  
> **Endpoint:** `wscript.exe` launches encoded PowerShell  
> **Network:** the host requests `/update.exe` from external infrastructure  
> **Detection:** an analytic fires on the encoded PowerShell pattern  
> **Gap:** available evidence does not yet establish whether `/update.exe` was successfully downloaded and executed

Write a short SOC handoff using this structure:

##### Host evidence
What does endpoint telemetry establish?

##### Network evidence
What does network telemetry establish?

##### Detection
What caused the analytic to match?

##### Assessment
What can you defensibly conclude now?

##### Remaining gap
What important question remains unanswered?

##### Report / handoff
What record or request should carry the result forward?

A strong answer should preserve the difference between **observed behavior** and **what remains unproven**.

#### SOC Readiness Checklist

Before moving into 2.x, you should be comfortable saying:

- [ ] I can describe process, file, registry, endpoint-network, and image/driver activity from evidence.
- [ ] I can explain what Zeek observed without assigning it host-process visibility it does not have.
- [ ] I can explain what a basic detection rule is designed to match.
- [ ] I can investigate an alert beyond its title or severity label.
- [ ] I can distinguish TP/FP/TN/FN from activity categorization.
- [ ] I can distinguish a false positive from the reason it occurred.
- [ ] I can identify which alert or reporting timeline applies.
- [ ] I can choose an incident report versus an RFI.
- [ ] I can identify the correct consumer and approved handoff path.
- [ ] I can state what the evidence does **not** establish.

If one of these is weak, return to the corresponding unit before moving forward.

#### Bridge Into 2.x CTI

The SOC establishes what happened locally as far as the available evidence allows.

Sometimes that is enough to close or escalate the case.

Other times the SOC reaches a question that needs intelligence work.

For example:

> What is known about this domain?  
> Has this infrastructure appeared in other reporting?  
> Which threat activity uses this behavior?  
> Is this pattern relevant to our environment?

That is where 2.x begins.

The SOC provides the observations and the question.

CTI adds context, evaluates sources, enriches the evidence, answers intelligence requirements, and produces assessed intelligence.

The **RFI** is one practical bridge between the two functions.

#### Summary

The 1.x SOC block taught one complete operational flow:

**Observe → Detect → Investigate → Communicate**

You can now move from raw endpoint and network evidence to an investigated alert and a usable handoff.

Keep one principle with you into every later track:

> **Describe what the evidence shows first. Then decide what it means.**

## Part III — Cyber Threat Intelligence

An investigation often leaves a question that additional collection and analysis can answer. CTI begins with that requirement, then develops an assessment whose reasoning and limitations remain visible. The sequence is **Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**. The eight units below follow the current course organization.

> **A12 Case Study:** Follow the evidence available at this stage of the case. The uninterrupted narrative appears in [Appendix A](#appendix-a--the-complete-a12-case-study).

### 2.0 — Cyber Threat Intelligence: How the 2.x Block Fits Together

**Estimated Time:** 10–15 minutes  

#### Learning Objectives

By the end of this introduction, you will be able to:

1. Explain how the reorganized 2.x CTI block moves from an intelligence question to an assessed answer.
2. Describe the role of tradecraft, frameworks, platforms, enrichment, assessment, and production in that workflow.
3. Recognize why platform results and enrichment records are inputs to analysis rather than finished intelligence.

#### What the CTI Block Is Building Toward

CTI begins with a question.

That question may come from leadership, a standing intelligence requirement, a SOC case, a threat hunt, or another defensive function.

The analyst's job is to turn available evidence into an answer that is:

- relevant to the requirement;
- grounded in identifiable sources;
- explicit about uncertainty;
- useful to a decision or next action.

A useful mental model for the 2.x block is:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

The analyst does more than gather information.

The analyst decides what the evidence supports.

#### The Eight Units

| Unit | Main question | What you learn |
|---|---|---|
| **2.1 – Intelligence Foundations and Requirements** | What question are we answering? | Data vs information vs intelligence, lifecycle, requirements, RFI intake, actionability, audience, attribution, and collection sources |
| **2.2 – Analytical Tradecraft** | How do we reason carefully about incomplete evidence? | Estimative language, structured techniques, source/information evaluation, and bias mitigation |
| **2.3 – Analytical Frameworks** | How can we organize what we know? | ATT&CK, Diamond Model, and Cyber Kill Chain as analytic structures |
| **2.4 – CTI Tools and Platforms** | Which source or platform should answer this lookup? | Internal TIP use, question-driven platform selection, VirusTotal, ANY.RUN, Silent Push, and urlscan.io |
| **2.5 – Technical Enrichment and Discovery** | What additional technical relationships can we test? | IOC lifecycle, file similarity, RDAP/WHOIS, DNS, infrastructure pivots, DTF, correlation, and link analysis |
| **2.6 – Threat Assessment and Organizational Significance** | Does this matter here? | Applicable TTPs, visibility, relevance, and plausible organizational impact |
| **2.7 – Intelligence Production and Dissemination** | How do we package and deliver the supported answer? | STIX, finished intelligence, RFI response/closure, and dissemination |
| **2.8 – Local Application** | How does this organization actually run CTI? | Local requirements, production/approval process, and dissemination channels |

Each unit answers a different part of the same intelligence requirement.

#### Start With the Requirement

Suppose the SOC asks CTI about A12:

> **What is known about the update domain, and does available evidence support that it delivered `update.exe` during the incident?**

That question creates a requirement.

Before searching, the analyst should understand:

- what is being asked;
- who needs the answer;
- what decision the answer will support;
- what is already known;
- what evidence would materially change the answer.

This keeps collection focused.

Without a requirement, enrichment can easily become endless browsing.

#### Collection Is Question-Driven

Different sources answer different questions.

For example:

- an internal TIP may show prior reports or sightings;
- VirusTotal may expose file relationships, detections, or behavior;
- ANY.RUN may show one sandbox execution;
- Silent Push may provide passive-DNS or infrastructure context;
- urlscan.io may provide a web-scan observation.

The important question is not:

> Which tools have I not checked yet?

It is:

> Which source can answer the next unresolved question?

That is why the reorganized course teaches **platform selection before deep enrichment**.

#### Platforms Use Two Passes

The 2.4 platform lessons introduce retrieval and interpretation boundaries.

Later 2.5 method lessons use those platforms again when the analyst needs a specific enrichment technique.

Think of the two passes as:

##### First pass – Retrieve correctly

Understand:
- what object you are querying;
- what the platform can return;
- what the observation time/source means;
- what the result cannot prove.

##### Second pass – Use the result analytically

Apply the result to:
- file similarity;
- infrastructure discovery;
- DNS/registration analysis;
- correlation;
- campaign tracking.

The platform is not the method.

It supports the method.

#### Enrichment Creates Candidate Relationships

Enrichment can reveal:

- related files;
- historical DNS;
- registration context;
- certificates;
- domains;
- IP addresses;
- infrastructure characteristics;
- behavioral artifacts.

Those findings often begin as **candidate relationships**.

For example:

> Two domains share an uncommon nameserver during overlapping periods.

That may justify further analysis.

It does not automatically prove:
- common ownership;
- common malicious control;
- a campaign;
- actor attribution.

Correlation in 2.5.7 tests whether individual findings form a stronger supported relationship.

#### Assessment Asks What Matters Here

Technical enrichment is not the end of CTI.

The analyst must determine whether the finding matters to the organization.

Keep these questions separate:

**Applicability**  
> Can this behavior occur in our environment?

**Visibility**  
> Can our telemetry observe it?

**Relevance**  
> Does it meaningfully intersect our mission, assets, technologies, or exposure?

**Impact**  
> If true here, what plausible consequence follows?

A finding can be applicable but not visible.

It can be visible but low relevance to the current requirement.

The distinctions keep the assessment useful.

#### Production Turns Analysis Into a Usable Answer

The final product should answer the original requirement.

That may include:

- a direct RFI response;
- a finished intelligence product;
- STIX objects for structured representation;
- a handoff to hunting or Detection Engineering;
- an explicit follow-up requirement when evidence remains incomplete.

The product should separate:

- supported facts;
- analytical judgments;
- confidence/uncertainty;
- unresolved gaps;
- recommended or requested next action.

The answer should be no broader than the evidence supports.

#### One A12 CTI Flow

A12 can move through the whole 2.x block.

##### Requirement

> Did the update domain likely support payload delivery, and what related activity matters to DYA?

##### Collect

Retrieve:
- internal TIP context;
- public reporting;
- file/platform observations;
- infrastructure records.

##### Evaluate

Preserve:
- source;
- observation/reporting time;
- provenance;
- source reliability/information credibility;
- uncertainty.

##### Enrich

Investigate:
- file relationships;
- registration;
- DNS;
- infrastructure;
- related domains/IPs.

##### Correlate

Test whether the findings support:
- a candidate relationship;
- a stronger activity-set/campaign assessment;
- or only weak/shared-provider coincidence.

##### Assess

Determine:
- which TTPs apply;
- whether they are visible;
- why the finding matters locally;
- plausible impact.

##### Produce

Write the evidence-based answer and represent structured objects when useful.

##### Disseminate

Deliver the answer to the correct audience and record closure or follow-up.

#### What You Need to Remember Before 2.1

You do not need to memorize every platform field or enrichment technique yet.

Remember the workflow:

> **Know the question.**  
> **Collect only what helps answer it.**  
> **Preserve provenance.**  
> **Treat pivots as candidates until tested.**  
> **Assess significance, not just technical interest.**  
> **Answer the requirement directly.**

#### Orientation Check

1. Why does the reorganized track teach platform selection before deep enrichment?
2. What is the difference between a platform result and finished intelligence?
3. A shared nameserver links two domains. What can you record before stronger corroboration exists?
4. Why are applicability and visibility separate questions?
5. What should the finished product return to at the end of the workflow?

#### Summary

The 2.x CTI block moves from a question to a supported answer:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

The recurring discipline is:

> **Preserve the evidence, make the judgment explicit, and answer the requirement—not the tool.**

### 2.1 – Intelligence Foundations and Requirements: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

CTI work begins with a question that matters to a decision maker and ends with a supported answer. This subunit establishes the concepts that keep collection, analysis, and production connected to that requirement.

#### Connect to What You Already Know

The CTI orientation introduced the intelligence workflow. This subunit provides the vocabulary and requirement discipline needed before deeper tradecraft, framework use, platforms, and enrichment.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **2.1.1 – Data, Information, and Intelligence** | Distinguish observations and organized facts from the judged answer that addresses a requirement. |
| **2.1.2 – Intelligence Lifecycle** | Understand intelligence as a cycle of direction, collection, processing, analysis, dissemination, and feedback. |
| **2.1.3 – Intelligence Types** | Recognize common intelligence types and how they serve different decisions and audiences. |
| **2.1.4 – Intelligence Requirements** | Translate an information need into a bounded intelligence requirement. |
| **2.1.5 – RFI Intake and Prioritization** | Receive, clarify, prioritize, and route a request for intelligence. |
| **2.1.6 – Ensuring Intelligence Is Actionable** | Connect the answer to a decision, action, or next step the customer can use. |
| **2.1.7 – Tailoring Output to the Audience** | Match detail, language, and format to the audience and decision need. |
| **2.1.8 – Attribution** | Keep actor or cluster judgments proportional to the available sourcing and evidence. |
| **2.1.9 – Collection Sources and Methods** | Select and describe sources based on what the requirement needs and what each source can provide. |

#### What to Watch For

- Keep the intelligence requirement visible as the reason for collection and analysis.
- Distinguish collected material from the judgment that answers the customer question.
- Make audience, actionability, sourcing, and attribution strength part of the answer rather than afterthoughts.

#### Expected End State

By the end of this subunit, you should be able to:

- distinguish data, information, and intelligence in a real workflow;
- explain how requirements drive the intelligence lifecycle and collection choices;
- receive and bound an RFI around the decision it needs to support;
- tailor a supported answer to the correct audience while preserving uncertainty and sourcing.

#### How to Preview This Subunit

Read this introduction, then skim the [2.1 Summary](#21--intelligence-foundations-and-requirements-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 2.1.1 — Difference between data, information, and intelligence

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Define data, information, and intelligence, and explain how context and analysis develop recorded observations into an assessment.
2. Categorize an example as data, information, or intelligence and explain your reasoning.

#### Key Concepts

CTI analysts work with material in many forms: individual indicators, logs, incident notes, and published reports. Each can contribute to an investigation, but they provide different kinds of understanding. Recognizing what a piece of material tells you helps you decide what work is still needed before you can use it to answer someone's question.

In this lesson, we use three terms to explain that development: **data**, **information**, and **intelligence**.

| Term | Meaning in this lesson | What the analyst contributes |
|---|---|---|
| **Data** | Individual recorded values or observations, such as an IP address, a timestamp, or a file hash. | Identifies what was recorded and where it came from. |
| **Information** | Data organized and placed in context so that it describes an event or situation. | Connects relevant observations to explain who did what, when, and where. |
| **Intelligence** | An assessment developed by evaluating information to answer a relevant question and support a decision. | Explains what the evidence means, why that conclusion is supported, and what uncertainty remains. |

##### Adding context

An IP address by itself gives you very little to work with. You need to know where it appeared and what was happening at the time. It might identify the destination of a workstation's connection, an address returned by a DNS lookup, or an indicator copied from a report.

As you establish those relationships, you develop information that describes the situation. For example, connecting an address to a particular workstation, request, and incident gives another analyst enough context to understand why you are examining it.

##### Developing an assessment

Analysis begins with the question you need to answer. You examine the relevant information, consider how reliable and complete it is, and decide which explanation the evidence supports. That conclusion is an **analytic judgment**. Explaining the reasoning allows the recipient to understand how you reached it and how much weight to place on it.

Intelligence can help someone decide what to investigate, what to prioritize, or whether a threat matters to their organization. It may include a recommended action, but its value also comes from improving the recipient's understanding of the situation.

##### Following one example

Consider the course's A12 incident. The question is: **What role did the update domain play in the activity on WS-JLEE?** A payload host is a server used to deliver a file involved in the attack.

**Start with data.** You encounter the address `203.0.113.88`. On its own, the address tells you neither what the workstation did nor how the address relates to the incident.

**Develop information.** The incident records connect WS-JLEE to that address, and the HTTP log records a request to the update domain for `/update.exe`. You can now describe the observed activity: the workstation requested a file from that destination during the incident. This is useful context, although the request alone does not establish that the file was successfully delivered or executed.

**Develop intelligence.** You evaluate that request alongside the suspicious process activity already associated with A12. You consider whether the destination served a role in delivering the payload and explain the limits of that interpretation:

> We assess that the update domain was likely used for attempted payload delivery in A12. The workstation requested `/update.exe` from that destination during the suspicious activity. These observations support investigating the domain's delivery role, but they do not establish that the requested file was successfully downloaded or executed.

The assessment adds an explanation of the domain's likely role and identifies what still needs to be established. That helps the investigator decide what evidence to seek next. The reasoning behind the conclusion is what makes this an assessment; the phrase “we assess” simply signals that a judgment is being expressed.

##### Communicating uncertainty

You will often need to provide an assessment before every question has been resolved. Explain what the evidence supports and where it leaves room for other explanations. In the example, the request supports a possible delivery role, while successful delivery and execution remain separate questions.

Being clear about those limits helps the recipient use the assessment appropriately. Later lessons develop the language used to express likelihood and confidence.

##### Recognizing the difference in practice

When reviewing an item, ask what work it contains. Does it present a recorded value, connect observations into a meaningful description, or evaluate evidence to answer a question? Look for the context and reasoning that support your choice. A single report may contain all three, so classify the particular statement you are examining.

#### Knowledge Check

1. You receive only the address `203.0.113.88`. How would you categorize it, and what context would you seek to understand its relevance?
2. A log shows that WS-JLEE requested `/update.exe` from the update domain during A12. Explain why this is information and identify one conclusion the request alone cannot establish.
3. Review the assessment in the worked example. What analysis does it add to the observations, and how does its uncertainty affect the investigator's next step?

#### Summary

Data provides the recorded observations from which you begin. Adding context develops information that describes a situation. Evaluating that information against a relevant question produces an intelligence assessment that explains the evidence's significance and supports a decision. A useful assessment makes its reasoning and remaining uncertainty clear enough for another person to use.

#### Related Reading

- [1.5 — Reporting](#15--reporting-and-notification-introduction)
- [2.1.2 — Intelligence lifecycle](#212--intelligence-lifecycle)
- [2.1.4 — Intelligence requirements](#214--intelligence-requirements)
- [2.2.1 — Estimative language](#221--estimative-language)
- [2.7.3 — Creating Finished Intelligence Products](#273--creating-finished-intelligence-products)

#### References and Further Reading

[ODNI, ICD 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf): supports the guidance on distinguishing evidence from judgments and explaining uncertainty. The three-part teaching model and classroom example above are instructional explanations, not quoted definitions from the directive.

### 2.1.2 — Intelligence lifecycle

**Estimated Time:** 20–25 minutes  

#### Learning Objectives

By the end of this module, you will be able to:

1. Name the six stages of the intelligence lifecycle and explain the purpose of each.
2. Place a given activity in the appropriate stage and explain why the lifecycle can return to an earlier stage.

#### Key Concepts

The intelligence lifecycle is a way to organize the work required to turn a question into an answer that someone can use. It helps an analyst recognize what kind of work is happening now, what should happen next, and when new evidence or feedback requires another pass through part of the process.

The stages are often drawn as a circle because intelligence work rarely moves through them once and stops. An analyst may discover during analysis that an important piece of evidence is missing and return to collection. A recipient may receive an assessment and ask a follow-up question, which begins another round of planning.

This course uses six stages:

| Stage | Purpose | Typical analyst work |
|---|---|---|
| **Planning and Direction** | Define the question and determine what is needed to answer it. | Clarify the request, identify the decision or information need, and determine what evidence would be useful. |
| **Collection** | Gather material relevant to the question. | Obtain records, logs, reporting, samples, or other needed observations. |
| **Processing and Exploitation** | Prepare collected material so it can be examined and compared. | Extract, normalize, organize, translate, enrich, or store relevant material in a usable form. |
| **Analysis and Production** | Evaluate the available information and develop the answer. | Compare evidence, test interpretations, identify gaps and uncertainty, and communicate an analytic judgment. |
| **Dissemination** | Deliver the intelligence to the people who need it in a usable form. | Provide the assessment through the appropriate report, briefing, ticket, platform, or other approved channel. |
| **Evaluation and Feedback** | Determine whether the intelligence answered the need and what should happen next. | Learn how the recipient used the answer, identify remaining questions, and refine future work. |

##### Connecting the lifecycle to the previous lesson

Module 2.1.1 focused on the difference between data, information, and intelligence. Those concepts help explain what happens inside parts of the lifecycle, but they are not the lifecycle stages themselves.

Collection often gives the analyst recorded observations. Processing and exploitation makes those observations easier to understand and compare. Analysis and production evaluates the available information against a question and develops an intelligence assessment. Planning, dissemination, and feedback organize the work around that analytical development.

The boundaries are useful for understanding the work, but real investigations may overlap stages. For example, an analyst may process a newly collected log and immediately notice a gap that requires another collection step.

##### What “exploitation” means here

In **Processing and Exploitation**, exploitation means making collected material usable for analysis. Depending on the source, that could include extracting indicators from a report, parsing a file, translating text, normalizing timestamps, or organizing records in a threat intelligence platform (TIP). It does not refer to exploiting a computer system.

##### Following one question through the lifecycle

Continue with the A12 investigation from the previous lesson. SOC asks CTI:

**What role did the update domain play in the activity on WS-JLEE?**

**Planning and Direction.** The analyst clarifies the question and identifies what would help answer it. Useful evidence might include the workstation's network activity, domain-resolution records, relevant incident notes, and any other observations that connect the destination to the suspicious activity.

**Collection.** The analyst gathers the records needed for the question. For example, the analyst obtains the relevant HTTP and DNS activity associated with WS-JLEE and the A12 time frame.

**Processing and Exploitation.** The analyst prepares the collected material for use. Relevant fields may be extracted, timestamps normalized, and the domain, IP address, request path, and source host organized so that the activity can be compared across the incident.

**Analysis and Production.** The analyst evaluates the processed information against the original question. In the A12 example, the request for `/update.exe` during the suspicious activity supports an assessment that the update domain likely played a role in attempted payload delivery, while successful download and execution remain unresolved.

**Dissemination.** The assessment is delivered to SOC in a form and channel they can use. The important point is that the recipient receives the analytic answer and its supporting limits, rather than simply receiving the raw indicators that contributed to it.

**Evaluation and Feedback.** SOC may confirm that the assessment answered the immediate question, or it may identify another need. For example, the next question could be whether the requested file actually reached the workstation or executed. That feedback gives the analyst a new or refined question and starts another pass through the lifecycle.

##### Why the lifecycle loops

The lifecycle is not a one-way assembly line. Each stage can reveal something that changes the work that follows.

Suppose the analyst reaches analysis and realizes that the available records show an HTTP request but do not show whether the transfer completed. The appropriate response is to identify that evidence gap and seek additional material that could address it. The work returns to collection because the analysis has shown what is still missing.

Feedback creates the same kind of loop. A useful assessment often answers one question while revealing the next. The lifecycle gives the team a common way to describe that movement without treating every return to an earlier stage as a failure or restart.

##### Recognizing the stage in practice

When classifying an activity, focus on **what work is being performed**, not the tool, team name, or folder where the work happens. Adding an indicator to a TIP could be processing if the analyst is organizing collected material. Evaluating that indicator alongside other evidence to answer a question is analysis. Sending the resulting assessment to the recipient is dissemination.

The same platform can therefore support several lifecycle stages. The stage is determined by the purpose of the activity.

#### Knowledge Check

1. An analyst has collected HTTP and DNS records for A12 and is extracting the domain, IP address, timestamps, and request path into a consistent format for comparison. Which lifecycle stage is this, and what makes it different from analysis?
2. During analysis, the analyst realizes the available records cannot establish whether `/update.exe` was successfully downloaded. What should happen next in the lifecycle, and why?
3. SOC receives the assessment about the update domain and asks whether the requested file executed on WS-JLEE. Which lifecycle stage produced that new need, and how does it affect the flow?

#### Summary

The intelligence lifecycle organizes the work required to move from a question to a useful answer. Planning defines the need, collection gathers relevant material, processing prepares it, analysis develops the assessment, dissemination delivers it, and evaluation determines whether the need was met and what comes next.

The stages provide structure, but the process is iterative. Analysis can reveal new collection needs, and feedback can create the next question. Recognizing the purpose of the work at each point helps analysts decide what should happen next.

#### Related Reading

- [2.1.1 — Data, information, and intelligence](#211--difference-between-data-information-and-intelligence)
- [2.1.3 — Intelligence types](#213--intelligence-types)
- [2.1.4 — Intelligence requirements](#214--intelligence-requirements)
- [2.1.7 — Tailoring output to the audience](#217--tailoring-output-to-the-audience)
- [2.1.9 — Collection sources](#219--collection-sources-and-methods)
- [2.7.3 — Creating Finished Intelligence Products](#273--creating-finished-intelligence-products)

### 2.1.3 — Intelligence Types

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the four intelligence types used in this course: **strategic**, **operational**, **tactical**, and **technical**.
2. Classify an intelligence product or requirement by type and explain the decision need that makes that classification appropriate.

#### Key Concepts

Intelligence types help describe the **kind of decision or understanding** a product is intended to support. Two products can discuss the same threat and still be different types because their readers are trying to answer different questions.

The useful starting point is therefore not the length of the report or the amount of technical detail. Ask: **What question is this product trying to answer, and what decision will the recipient make with the answer?**

This course uses four types:

| Type | Primary decision need | Typical focus |
|---|---|---|
| **Strategic** | How should leadership understand or change organizational risk, priorities, or posture? | Longer-term implications, trends, business or mission risk, resource and policy decisions |
| **Operational** | How should defenders understand and manage an operation, campaign, incident set, or hunt over time? | Campaign activity, sequencing, targeting patterns, operational priorities, coordination across days or weeks |
| **Tactical** | What should a defender do about the activity in front of them? | Immediate defensive decisions, response actions, techniques, and near-term handling |
| **Technical** | What concrete artifacts or technical characteristics can analysts detect, validate, or pivot on? | Domains, IP addresses, hashes, paths, protocol details, malware characteristics, and other observables |

These categories are a teaching model. In practice, organizations and vendors sometimes use the labels differently. When you work in a specific environment, use its definitions consistently. The important skill is recognizing the **decision level** the product is serving.

##### Type follows the question

A requirement and the product that answers it usually share the same primary type because the requirement defines the decision need.

Consider several possible questions related to A12:

- **Technical:** What domains, IP addresses, file names, and request paths are associated with the activity?
- **Tactical:** What should SOC or IR do now with WS-JLEE and the update domain?
- **Operational:** How is the A12 activity unfolding, and what should defenders prioritize across the investigation over the next several days?
- **Strategic:** Does the broader threat represented by this activity materially change organizational risk, defensive priorities, or investment decisions?

The same incident can contribute evidence to all four questions, but the questions require different analysis. A single A12 observation may be enough to support a technical or tactical answer while being only one input to a broader strategic assessment.

##### Technical and tactical are related, but not interchangeable

This is a common source of confusion. A technical observable tells you **what can be identified or detected**. A tactical product tells a defender **how to respond to or handle activity**.

For example:

- `203.0.113.88` and `GET /update.exe` are technical observations.
- “Investigate connections from WS-JLEE to the update domain and preserve the associated file and process evidence” is tactical guidance.

The technical evidence may enable the tactical decision, but the observable itself is not the response action.

##### Operational and strategic differ in the decision horizon

Operational intelligence helps a team manage an ongoing body of activity: a campaign, incident set, hunt, or adversary operation. It is concerned with how the activity is unfolding and what defenders should prioritize across that effort.

Strategic intelligence steps farther back. It helps leadership understand implications for risk, posture, resources, or policy. A lengthy report is not automatically strategic, and a short assessment can still be strategic if it answers a leadership-level risk question.

Time horizon can be a useful clue, but it is not the definition. The **decision being supported** is the stronger indicator.

##### Relationship to the lifecycle

Module 2.1.2 described the stages of intelligence work. A lifecycle **stage** tells you what kind of work is happening; an intelligence **type** tells you what kind of decision the resulting requirement or product supports.

You can collect technical observables while working on a tactical or operational requirement. Likewise, a strategic product still passes through planning, collection, processing, analysis, dissemination, and feedback.

#### Knowledge Check

1. A 40-page report containing mostly domains, hashes, and malware configuration details is automatically strategic because it is long. True or false? Explain.
2. A requirement asks, “What should IR do now with WS-JLEE and the update domain?” Which intelligence type best fits the requirement, and why?
3. Explain the difference between a **technical** product that lists the A12 observables and a **tactical** product that uses those observables to guide a responder.

#### Summary

Intelligence type is determined primarily by the **question and decision need**, not by report length or technical complexity. Strategic intelligence supports leadership-level risk and posture decisions; operational intelligence supports management of campaigns and ongoing activity; tactical intelligence supports near-term defensive action; and technical intelligence describes concrete artifacts and characteristics analysts can detect or pivot on.

When the boundary is unclear, ask what the recipient needs to decide. That usually reveals the type more reliably than the format of the product.

#### Related Reading

- [2.1.2 — Intelligence lifecycle](#212--intelligence-lifecycle)
- [2.1.4 — Intelligence requirements](#214--intelligence-requirements)
- [2.1.7 — Tailoring output to the audience](#217--tailoring-output-to-the-audience)
- [2.7.3 — Creating Finished Intelligence Products](#273--creating-finished-intelligence-products)

### 2.1.4 — Intelligence Requirements

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain why intelligence requirements exist and distinguish a **Priority Intelligence Requirement (PIR)** from other requirements.
2. Refine a stakeholder question into a clear intelligence requirement and explain how that requirement directs collection and analysis.

#### Key Concepts

An intelligence requirement gives the work a **purpose**. It tells the analyst what question needs to be answered so collection and analysis can be focused on the evidence that matters.

Without a clear requirement, analysts can easily collect everything that looks interesting, follow every possible pivot, and still have no reliable way to know when the original need has been answered.

A useful requirement therefore connects three things:

1. **The question** — what needs to be known.
2. **The decision or need** — why the answer matters to the stakeholder.
3. **The scope** — what subject, environment, and time window the work should cover.

A requirement should be specific enough to guide work while leaving room for the analyst to determine what evidence is needed. It normally should not dictate a particular tool or source unless the source itself is part of the requirement.

##### Priority is not the same as duration

A **Priority Intelligence Requirement (PIR)** is an intelligence requirement that leadership or the program has identified as especially important. The word *priority* describes its relative importance.

Other labels describe different characteristics of a requirement:

- A **standing requirement** remains active over time until it is changed or retired.
- An **ad-hoc requirement** addresses a one-time or event-driven need, often created by an incident or Request for Information (RFI).

These labels are not mutually exclusive. A standing requirement can also be a PIR if leadership prioritizes it. An ad-hoc requirement can also become a priority if the situation warrants it.

The key point is that **not every requirement is a PIR**. Use the organization's published priorities rather than inventing PIR numbers or labels.

##### Refining a stakeholder question

Stakeholders often begin with a question that makes sense conversationally but is too broad to guide analysis.

For example:

> “Are we seeing them?”

That question leaves several things unclear. Who is “them”? What activity counts as “seeing” them? In what environment and during what period?

In the A12 context, a more useful requirement might be:

> **What role did the update domain play in the activity on WS-JLEE during A12?**

This version gives the analyst an object to investigate, a defined case, and a relationship to establish. It is still broad enough for the analyst to determine what evidence is needed.

A more narrowly scoped follow-on requirement could ask:

> **Was the update domain used to deliver `/update.exe` to WS-JLEE during the A12 time window?**

The right level of specificity depends on the stakeholder's actual need. The analyst's job is to make the question clear enough that the team knows what evidence would answer it.

##### How requirements drive collection and analysis

Once the question is clear, it shapes the work.

For the A12 requirement, the analyst might need:

- network records showing WS-JLEE's requests to the domain;
- DNS records connecting the domain to an address;
- host evidence showing whether the requested file appeared; and
- incident context needed to interpret those observations.

The requirement also helps control scope. A sibling domain discovered during enrichment may be interesting, but if it does not help answer the current question, it can be documented for later rather than allowed to derail the analysis.

That does not mean analysts ignore unexpected evidence. It means they can distinguish **evidence needed for the current requirement** from **new information that may justify a separate or refined requirement**.

##### Requirements and intelligence types

Module 2.1.3 introduced strategic, operational, tactical, and technical intelligence. A requirement can be classified the same way because the requirement defines the type of answer the stakeholder needs.

For example, “What should IR do now with WS-JLEE?” is a tactical requirement. “Does this threat materially change organizational risk?” is strategic. The requirement sets the direction before collection begins.

##### Connect the requirement to local priorities

Before starting real collection, consult the current local priorities described in [2.8.1](#281--local-intelligence-requirements-and-priorities). Identify the mission, assets, and decision that make the question relevant. This early relevance check bounds the work; the fuller applicability and impact assessment follows the evidence in 2.6.

#### Knowledge Check

1. Every intelligence requirement is a PIR. True or false? Explain what makes a PIR different.
2. A stakeholder asks, “Are we seeing them?” Identify two things you would clarify before treating that as an intelligence requirement.
3. Using A12, write a clearer requirement for the update domain and name one piece of evidence that would help answer it and one interesting pivot that could reasonably be deferred if it does not help answer the question.

#### Summary

An intelligence requirement defines the question the work exists to answer. A clear requirement identifies the information need, connects it to a decision, and provides enough scope to guide collection and analysis.

A PIR is a requirement that has been **prioritized** by leadership or the program. Standing and ad-hoc describe how a requirement persists or arises; they do not automatically determine priority.

Good requirements focus the work without prescribing every analytical step. They help the analyst decide what evidence matters now, what can wait, and when the answer is sufficient for the stakeholder's need.

#### Related Reading

- [2.1.3 — Intelligence types](#213--intelligence-types)
- [2.1.6 — Ensuring intelligence is actionable](#216--ensuring-intelligence-is-actionable)
- [2.1.9 — Collection sources and methods](#219--collection-sources-and-methods)
- [2.8.1 — Local intelligence requirements and PIRs](#281--local-intelligence-requirements-and-priorities)

### 2.1.5 — RFI Intake and Prioritization

**Estimated Time:** 15–20 minutes

#### Learning Objectives

1. Capture a bounded RFI with its decision need, scope, deadline, and handling context.
2. Evaluate answerability, identify missing evidence, and justify priority or routing using local policy.

#### Key Concepts

An **RFI — Request for Information** is a request for an answer or information that another consumer needs.

The RFI is not automatically:
- a new incident;
- a Priority Intelligence Requirement;
- a new collection campaign;
- a request to write everything known about the actor.

Its first job is to define **what the requestor needs answered**.

##### Receive

Capture enough information to understand the request.

Useful intake fields include:

- requestor / customer;
- question;
- why the answer is needed or what decision it supports;
- needed-by time, if relevant;
- scope or time window;
- handling restrictions;
- related incident/report/reference.

Local forms and queue fields belong to site-specific policy in 2.8; the course does not invent them.

##### Evaluate

Ask:

- Is the question clear and bounded?
- Do we already have an answer?
- What evidence would answer it?
- What evidence do we currently have?
- What is missing?
- Is CTI the right owner, or should the request be routed elsewhere?
- Does the request duplicate an existing requirement or product?

If the question is unclear, clarification may be the correct next action.

If the question cannot yet be answered, identify the gap rather than inventing a conclusion.

##### Prioritize

Priority should reflect the local policy, but the analyst can recognize common drivers:

- active incident or operational decision;
- time sensitivity;
- mission/customer importance;
- dependency: another team cannot proceed without the answer;
- effort and available evidence;
- existing standing priorities.

The classroom rule is simple:

> A bounded RFI supporting an active incident normally takes precedence over routine background reading.

That is a teaching scenario, not a universal queue SLA.

##### A12 intake decision

The request asks: **Was the update domain the host that successfully delivered the payload in A12?** The requester needs to distinguish an attempted transfer from a completed one.

Record the requester and needed-by time from the actual request; clarify them if missing. Scope the work to WS-JLEE, the update domain, `/update.exe`, and the A12 time window. Reference the existing case rather than opening a second incident merely because an RFI arrived.

Available evidence establishes a request for `/update.exe`, but not successful download or execution. The question is clear; the evidence is incomplete. Record the missing transfer or host-file evidence and identify the appropriate source or owner. In this classroom scenario, the active incident gives the request priority over routine background research, subject to the site's actual rules.

##### Carry the requirement forward

Use a short intake record:

`requester | question | decision/use | needed-by | scope | handling | case | evidence available | gap | priority/routing rationale`

This record directs collection in [2.1.9](#219--collection-sources-and-methods). Keep it with the evidence through the course; you will answer the same question in [2.7.4 – RFI Responses and Closure](#274--rfi-responses-and-closure). Obtain actual local priorities from [2.8.1](#281--local-intelligence-requirements-and-priorities) before applying this workflow at work.

#### Knowledge Check

1. Why is an RFI not automatically a PIR or a new incident?
2. The A12 request asks whether delivery succeeded, but you only have a request record. What should intake record?
3. What would you clarify if the requester asks only, “Are we seeing them?”

#### Summary

A clear RFI establishes the question, its purpose, and its limits. Record evidence gaps and priority before collection begins.

### 2.1.6 — Ensuring Intelligence Is Actionable

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the characteristics that make intelligence **actionable** for a recipient and common reasons a product fails that test.
2. Evaluate a piece of intelligence and explain whether the recipient can use it to make a timely decision or take a meaningful next step.

#### Key Concepts

Intelligence becomes actionable when the recipient can **use the assessment to make a decision or take a meaningful next step**. The standard is not simply whether the product is interesting, accurate, or technically detailed. The question is whether it helps the intended recipient do something useful in the context of the requirement.

Actionability depends on the relationship among the requirement, the assessment, the recipient, and the timing. A useful way to evaluate a product is to ask five questions:

| Question | What to look for |
|---|---|
| **Does it answer the requirement?** | The product addresses the question the work was intended to answer. |
| **Is the recipient clear?** | The person or team who can use the answer is identifiable. |
| **Is the next decision or action specific enough?** | The product gives the recipient enough information to decide what to investigate, contain, prioritize, collect, or monitor. |
| **Is it timely?** | The answer arrives while the decision can still be made or influenced. |
| **Are the judgment and limits clear?** | The recipient can distinguish what the evidence supports from what remains uncertain. |

These are not a universal five-box policy. They are a practical test for this course: can the intended consumer use the intelligence responsibly and in time?

##### Actionable does not always mean “issue a command”

An intelligence product can be actionable without telling the recipient exactly which button to press. Sometimes the useful next step is to investigate, collect additional evidence, change a priority, or decide that no immediate response is warranted.

For example, an assessment that the update domain likely supported attempted payload delivery could be actionable if it gives IR a reason to preserve relevant evidence and examine whether the file transfer completed. The value comes from improving the decision, not from adding a directive for its own sake.

##### Why products fail the test

Common failure modes include:

- **The product answers a different question.** The reporting may be interesting but unrelated to the requirement.
- **The recipient cannot tell what the significance is.** A list of indicators may be useful data, but without context or judgment it may not tell anyone what to do with it.
- **The language is too vague.** “Be aware” or “monitor” may sound cautious but can leave the recipient without a meaningful next step.
- **The answer arrives too late.** A correct assessment can lose operational value after the relevant decision window closes.
- **The product hides uncertainty.** A recipient may act too aggressively or too cautiously if the limits of the judgment are unclear.

##### Compare two A12 products

Consider the requirement from the previous lesson:

**What role did the update domain play in the activity on WS-JLEE during A12?**

A product such as this gives the recipient something useful:

> We assess that the update domain likely supported attempted payload delivery during A12. WS-JLEE requested `/update.exe` from that destination during the suspicious activity. IR should preserve and review the associated network, file, and process evidence to determine whether the transfer completed and whether the file executed.

Why is this actionable?

- It answers the requirement by explaining the domain's likely role.
- It identifies IR as a recipient who can use the answer.
- It gives a concrete next investigative step.
- It preserves the uncertainty around successful delivery and execution.

Now compare:

> New malicious activity has been reported. Be aware and monitor as needed.

That statement does not identify the relevant requirement, environment, evidence, or meaningful next decision. The problem is not that the wording is short; the problem is that the recipient cannot tell what the statement means for their situation.

##### Actionability depends on the recipient and requirement

A product that is actionable for IR may not be actionable for leadership. IR can work host, file, and process details; leadership may need the risk implication, priority, and decision point instead. Module 2.1.7 addresses that tailoring in more detail.

Likewise, “actionable for a hunter” is a narrower question addressed later in the hunting curriculum. A product can support an IR decision even if it does not contain everything a hunter would need to build a hunt.

#### Knowledge Check

1. “Be aware and monitor as needed” is actionable intelligence because it tells the recipient to monitor. True or false? Explain.
2. Name three questions you can ask when evaluating whether an intelligence product is actionable.
3. Review the A12 assessment above. Identify the requirement it answers, the recipient who can act, the next step it supports, and one uncertainty the recipient still needs to keep in mind.

#### Summary

Actionable intelligence helps a specific recipient make a timely decision or take a meaningful next step. It should answer the requirement, make the significance clear, provide enough specificity for use, arrive in time, and communicate the limits of the judgment.

A product does not become actionable merely because it contains indicators or an instruction. The important test is whether the recipient can use the assessment responsibly in the situation the requirement was meant to address.

#### Related Reading

- [2.1.4 — Intelligence requirements](#214--intelligence-requirements)
- [2.1.7 — Tailoring output to the audience](#217--tailoring-output-to-the-audience)
- [2.1.1 — Data, information, and intelligence](#211--difference-between-data-information-and-intelligence)
- [3.4.1 — Assessing CTI for hunt value](#341--assessing-cti-for-hunting-value)

### 2.1.7 — Tailoring Output to the Audience

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain why **audience analysis** should happen before an intelligence product is written or delivered.
2. Adjust the **content**, **format**, and **level of detail** of an intelligence product for a specified audience while preserving the underlying facts and analytic judgment.

#### Key Concepts

An intelligence product is useful only if the intended reader can understand it and use it for the decision they own. The same assessment may therefore need to be presented differently to leadership, SOC, IR, threat hunters, or detection engineers.

Tailoring does **not** mean changing the evidence or softening the judgment to match what a reader wants to hear. It means deciding which parts of the same underlying analysis each audience needs, how much detail they can use, and what format makes the decision easiest to understand.

Before writing, ask:

- **Who is the consumer?**
- **What decision or action do they own?**
- **What do they already know?**
- **Which facts, caveats, and details do they need in order to use the assessment correctly?**

##### Three things you adjust

| Element | What it means |
|---|---|
| **Content** | Which facts, implications, and supporting details the reader needs for their decision |
| **Format** | The shape of the product: short summary, paragraph, table, technical appendix, briefing, or other appropriate form |
| **Level of detail** | How much technical depth, evidence, and supporting context the reader needs |

The underlying evidence and analytic judgment should remain consistent across versions. Tailoring changes the **presentation and emphasis**, not the truth of the assessment.

##### Follow the same A12 assessment for two audiences

Use the assessment developed earlier in the course:

> We assess that the update domain likely supported attempted payload delivery during A12. WS-JLEE requested `/update.exe` from that destination during the suspicious activity. Successful download and execution remain unresolved.

A leadership version might say:

> **A12 involved suspicious PowerShell activity on WS-JLEE and an external domain that likely supported attempted payload delivery. IR has the affected host; the immediate evidence gap is whether the requested file was successfully delivered or executed.**

This version preserves the assessment and uncertainty while emphasizing impact, ownership, and the decision-relevant gap. Leadership usually does not need every path, hash, or request field in the main line.

An IR / SOC version could retain more technical detail:

> **WS-JLEE requested `/update.exe` from the update domain during the A12 activity. CTI assesses the domain likely supported attempted payload delivery. Review the related network, file, and process evidence to determine whether the transfer completed and whether the file executed.**

This version emphasizes the host, request path, evidence, and next investigative step because those details are directly useful to the technical consumer.

##### Same facts does not mean identical wording

Good tailoring may change the order of information, the amount of supporting evidence, the terminology, and the prominence of caveats.

For leadership, the analyst may lead with the implication and decision point. For IR, the analyst may lead with the affected host and evidence. For a hunter, the analyst may emphasize behavioral patterns and observables. The assessment should still be traceable back to the same evidence and judgment.

##### Avoid two opposite errors

**Too much detail:** A leadership product can become harder to use when the main message is buried under hashes, file paths, raw logs, or platform-specific fields.

**Too little detail:** A technical team may be unable to act if the product reduces everything to a one-line “so what” without the host, artifacts, behavior, or evidence they need.

Tailoring is therefore a balance between **relevance and sufficiency**. Give the reader enough to make the right decision without forcing them to reconstruct the analysis from irrelevant detail.

##### Tailoring and dissemination are related, but different

Tailoring concerns the **content and presentation** of the product. Dissemination also includes how and where the product is delivered. Later modules cover channels and finished-product mechanics in more depth.

#### Knowledge Check

1. Tailoring means changing the analytic judgment so that it is more acceptable to leadership. True or false? Explain.
2. What three elements of a product can you adjust for a specified audience?
3. Using the A12 assessment, write one short leadership version and list two additional details you would retain or add for IR / SOC.

#### Summary

Audience analysis begins with the consumer's decision. Once you know who will use the product and what they need to do, you can adjust the content, format, and level of detail without changing the underlying evidence or analytic judgment.

Leadership usually needs implications, ownership, and decision-relevant uncertainty. Technical consumers usually need more of the host, behavior, artifact, and evidence detail that allows them to investigate or respond.

The goal is not to make every reader see the same words. The goal is to make every reader receive the **same supported assessment in a form they can use correctly**.

#### Related Reading

- [2.1.6 — Ensuring intelligence is actionable](#216--ensuring-intelligence-is-actionable)
- [2.1.8 — Attribution](#218--attribution)
- [2.7.5 — Dissemination channels](#275--disseminating-intelligence-to-the-correct-audiences)
- [1.5 — SOC reporting and routing](#15--reporting-and-notification-introduction)

### 2.1.8 — Attribution

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose and challenges of attribution and distinguish an **activity group or cluster** from a stronger claim about **nation-state sponsorship**.
2. Evaluate an attribution statement by comparing the confidence claimed with the evidence actually presented.

#### Key Concepts

Attribution is the analytical work of connecting observed activity to a responsible **cluster, actor, organization, or sponsor** at a level the evidence can support.

The purpose is not simply to attach the most specific name possible. A useful attribution helps defenders understand which body of activity they are dealing with so they can connect reporting, compare behaviors, prioritize collection, and make better defensive decisions.

A well-calibrated attribution claim should answer two questions:

1. **What level of attribution is being claimed?**
2. **How strongly does the available evidence support that claim?**

##### Different levels of attribution require different evidence

This course emphasizes two levels:

| Level | What the claim means |
|---|---|
| **Activity group / cluster** | Multiple observations are judged to belong to the same body of activity based on shared infrastructure, malware, behavior, targeting, or other characteristics. |
| **Nation-state sponsorship** | The activity is judged to be sponsored, directed, or conducted on behalf of a government. This is a stronger claim about who stands behind the cluster. |

Analysts can defend against an activity cluster without knowing which government, company, or individual ultimately controls it. In many cases, the cluster-level judgment is both useful and better supported than a sponsor-level claim.

##### Why attribution is difficult

Cyber evidence is often indirect and reusable. Several conditions make over-attribution easy:

- **Shared infrastructure:** Multiple customers or actors may use the same hosting provider, IP range, cloud service, VPN, or compromised server.
- **Malware and tool reuse:** Code, loaders, scripts, and public tools can be copied or purchased by unrelated actors.
- **False flags and deception:** An actor can deliberately imitate another group or plant misleading artifacts.
- **Vendor naming differences:** Two vendors may use different names for overlapping activity, or one name may cover activity that another vendor splits into several clusters.
- **Limited or one-sided reporting:** A public report may omit the evidence that led to a vendor's conclusion.

Because of these challenges, a label is not the same thing as evidence. A report title such as “PRD APT” tells you how that source tracks the activity; by itself, it does not prove government sponsorship.

##### Confidence describes the strength of support

This lesson uses a simplified classroom scale:

- **Low confidence:** The judgment has limited support, depends heavily on one source or weakly discriminating evidence, or has substantial plausible alternatives.
- **Medium confidence:** Multiple relevant lines of evidence support the judgment, but important gaps or plausible alternatives remain.
- **High confidence:** Several strong, substantially independent lines of evidence converge on the judgment and plausible alternatives are limited.

Use your organization's published confidence framework when one exists. These definitions are a teaching aid, not a replacement for local analytic standards.

Confidence is about **how well the evidence supports the judgment**. It is different from likelihood language such as “likely” or “almost certainly,” which is covered later in Module 2.2.1.

##### Assess the claim, not the label

Consider this statement:

> “The vendor report calls the actor PRD APT, so A12 is a high-confidence nation-state operation.”

Break the statement apart:

- **Claimed attribution level:** nation-state sponsorship.
- **Claimed confidence:** high.
- **Evidence presented:** a vendor tracking label.

The evidence shown in the statement does not justify the claim. The label may support the fact that the vendor tracks an activity cluster under that name, but it does not independently establish a government sponsor or high confidence.

A stronger analysis would either provide the additional evidence that supports the sponsor-level judgment or narrow the claim to the level the available evidence can defend.

##### Use A12 without overreaching

The A12 case includes suspicious PowerShell activity, an update domain, and related network observations. Those facts can help analysts compare the incident to other activity and may contribute to clustering.

They do not, by themselves, establish nation-state sponsorship. If a vendor has already attributed similar activity to a government, that vendor assessment can be considered as one source—but the analyst should still distinguish **the vendor's claim** from **the evidence available in the current analysis**.

This distinction allows the analyst to say something useful without pretending to know more than the evidence supports.

#### Knowledge Check

1. A vendor's use of an “APT” name is, by itself, sufficient for high-confidence nation-state attribution. True or false? Explain.
2. What is the difference between attributing activity to an **activity group / cluster** and attributing it to a **nation-state sponsor**?
3. Assess this statement: “A vendor PDF calls the actor PRD APT, so this is high-confidence nation-state activity.” Identify the attribution level claimed, the confidence claimed, and what additional support would be needed before accepting that conclusion.

#### Summary

Attribution should be as specific as the evidence allows—not as specific as the analyst can imagine. Activity-group attribution connects observations to a body of related activity. Nation-state attribution makes a stronger claim about sponsorship and therefore requires stronger support.

When evaluating an attribution statement, separate the **claim**, the **confidence**, and the **evidence**. Vendor labels, infrastructure, malware, and behavior can all contribute, but none should be treated as proof without considering alternative explanations and the independence of the evidence.

The most useful attribution is often the one the analyst can defend clearly and update as better evidence becomes available.

#### Related Reading

- [2.1.7 — Tailoring output to the audience](#217--tailoring-output-to-the-audience)
- [2.1.9 — Collection sources and methods](#219--collection-sources-and-methods)
- [2.2.1 — Estimative language](#221--estimative-language)
- [2.7.3.2 — Actor profiles](#273--creating-finished-intelligence-products)

### 2.1.9 — Collection Sources and Methods

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the three source classes used in this course: **OSINT**, **commercial**, and **internal**.
2. Select appropriate source classes for a requirement and build a short collection plan that identifies collection order, the first action, and reasonable limits on scope.

#### Key Concepts

An intelligence requirement tells the analyst **what needs to be known**. Collection planning decides **where to look for the evidence that can answer it**.

Module 2.1.2 described Collection as a lifecycle stage—the work of gathering relevant material. This lesson looks inside that stage and asks which broad class of source is most appropriate for the question.

This course uses three source classes:

| Source class | What it includes | Especially useful when the requirement asks... |
|---|---|---|
| **OSINT** | Public reporting, public repositories, public DNS and registration data, open research, public malware or security reporting | What is publicly known about the threat, infrastructure, technique, or campaign? |
| **Commercial** | Paid threat-intelligence services, premium sandboxing or enrichment, vendor reporting, licensed datasets | What additional enrichment or vendor-held context can supplement open and internal evidence? |
| **Internal** | SIEM, EDR, network telemetry, tickets, incident records, internal threat-intelligence platforms, hunt results, internal logs | What is happening in **our** environment, and what evidence do **we** have? |

The classes can be combined. A mature collection effort often uses more than one. The important question is not “Which class is best?” in the abstract. It is **which source is most likely to reduce uncertainty about this requirement, given what is already available**.

##### Collection order follows the requirement

Suppose the requirement asks:

> **What role did the update domain play in the activity on WS-JLEE during A12?**

Because the question concerns activity in the organization's own environment, internal evidence should usually be an early collection priority. Relevant internal sources might include HTTP and DNS telemetry, host evidence, and incident records.

Public or commercial sources may still add useful context. They could show whether the domain has appeared in other reporting, whether it has related infrastructure, or whether vendors have seen similar activity. But that external context cannot replace the internal evidence needed to answer what happened on WS-JLEE.

Now consider a different requirement:

> **What public reporting exists about this delivery technique and the infrastructure associated with it?**

For that question, OSINT or commercial reporting may be the logical starting point. The requirement changes the collection order.

##### A short collection plan

A collection plan in this lesson does not need to be a formal document. It should show that the analyst has connected the requirement to a deliberate set of collection actions.

A useful short plan includes:

1. **Requirement:** What question are you answering?
2. **Source class and order:** Which class or classes should be checked first, and why?
3. **First collection action:** What specific evidence will you seek first?
4. **Limits or stop conditions:** What will you defer, avoid, or revisit only if the first collection does not answer the requirement?

For the A12 requirement, a short plan might look like this:

- **Requirement:** Determine the update domain's role in the activity on WS-JLEE.
- **First class:** Internal, because the question is about observed activity in our environment.
- **First action:** Review the relevant HTTP, DNS, and host evidence for the A12 window.
- **Next class if needed:** OSINT or commercial sources to add external context about the domain or delivery pattern.
- **Limit:** Record unrelated infrastructure pivots, but defer them unless they help answer the current requirement or justify a follow-on requirement.

This structure prevents habitual collection. The analyst is not automatically starting with a favorite platform or collecting every available pivot.

##### Source quality and access still matter

Selecting a source class is only the beginning. Within any class, sources vary in reliability, timeliness, coverage, and accessibility.

An analyst should consider:

- whether the source can actually answer the question;
- how current and complete the source is;
- whether the organization has lawful and authorized access;
- whether another source can corroborate an important claim; and
- whether the expected value of the collection justifies the time and effort.

Later modules go deeper into specific tools and local collection-request processes. In this lesson, the goal is to build the habit of selecting sources **because they answer the requirement**, not because they are familiar or convenient.

##### Plan for the evidence gap, not for the tool

A weak plan says, “Open the TIP and search the domain.”

A stronger plan says, “Use internal telemetry first to determine whether WS-JLEE resolved and contacted the domain during A12; if the internal evidence leaves the domain's broader role unclear, use public or commercial reporting to add external context.”

The stronger plan explains what the collection is meant to establish. The tool can change without changing the analytical purpose.

##### Use the local collection process

Carry forward the intake record from [2.1.5](#215--rfi-intake-and-prioritization). Before requesting collection or using an external service, confirm the actual approval and handling requirements described in [2.8.2](#282--local-production-and-approval-processes). Do not infer authorization from the availability of a tool.

#### Knowledge Check

1. The Collection lifecycle stage and a collection source class are the same thing. True or false? Explain the difference.
2. A requirement asks, “What happened with this domain on our network during A12?” Which source class should usually be an early priority, and why?
3. Write a short collection plan for the A12 update-domain requirement that includes the first source class, the first collection action, one possible follow-on class, and one reasonable scope limit.

#### Summary

Collection planning connects an intelligence requirement to the evidence most likely to answer it. This course groups sources into OSINT, commercial, and internal classes, and those classes can be combined as needed.

The requirement determines the order. Questions about the organization's own environment usually require internal evidence early; questions about the public threat landscape may begin with OSINT or commercial reporting.

A good collection plan explains **what evidence is needed and why**, not merely which tool the analyst intends to open. It also defines reasonable limits so interesting pivots do not replace the question the team is supposed to answer.

#### Related Reading

- [2.1.8 — Attribution](#218--attribution)
- [2.1.2 — Intelligence lifecycle](#212--intelligence-lifecycle)
- [2.1.4 — Intelligence requirements](#214--intelligence-requirements)
- [2.8.2.1 — Local collection requests](#282--local-production-and-approval-processes)
- 0.7 / 2.4 / 2.4 – Tool survey, TIP, and platform depth

### 2.1 – Intelligence Foundations and Requirements: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Requirement → collection → evaluation/analysis → answer → dissemination → feedback**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- distinguish data, information, and intelligence in a real workflow;
- explain how requirements drive the intelligence lifecycle and collection choices;
- receive and bound an RFI around the decision it needs to support;
- tailor a supported answer to the correct audience while preserving uncertainty and sourcing.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **2.1.1 – Data, Information, and Intelligence** | Distinguish observations and organized facts from the judged answer that addresses a requirement. |
| **2.1.2 – Intelligence Lifecycle** | Understand intelligence as a cycle of direction, collection, processing, analysis, dissemination, and feedback. |
| **2.1.3 – Intelligence Types** | Recognize common intelligence types and how they serve different decisions and audiences. |
| **2.1.4 – Intelligence Requirements** | Translate an information need into a bounded intelligence requirement. |
| **2.1.5 – RFI Intake and Prioritization** | Receive, clarify, prioritize, and route a request for intelligence. |
| **2.1.6 – Ensuring Intelligence Is Actionable** | Connect the answer to a decision, action, or next step the customer can use. |
| **2.1.7 – Tailoring Output to the Audience** | Match detail, language, and format to the audience and decision need. |
| **2.1.8 – Attribution** | Keep actor or cluster judgments proportional to the available sourcing and evidence. |
| **2.1.9 – Collection Sources and Methods** | Select and describe sources based on what the requirement needs and what each source can provide. |

#### Check Your Understanding

Ask yourself:

1. What makes an intelligence requirement more useful than a broad topic request?
2. Why is collected reporting not automatically a finished intelligence answer?
3. How can the same underlying analysis be tailored differently for two audiences without changing the evidence?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **2.2 – Analytical Tradecraft: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 2.2 – Analytical Tradecraft: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Analytical tradecraft helps an intelligence analyst make judgments that are transparent, reviewable, and appropriately uncertain. The goal is not to remove uncertainty; it is to reason through it in a disciplined way.

#### Connect to What You Already Know

The foundations subunit established the requirement, collection, and audience. This subunit focuses on how the analyst evaluates sources, structures reasoning, communicates probability, and reduces avoidable bias while answering that requirement.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **2.2.1 – Estimative Language** | Express probability and uncertainty with consistent estimative terms. |
| **2.2.2 – Structured Analytic Techniques** | Use structured methods to expose assumptions, alternatives, and evidence relationships. |
| **2.2.3 – Admiralty Code** | Evaluate source reliability separately from information credibility. |
| **2.2.4 – Cognitive Biases and Mitigation** | Recognize common analytical biases and apply practical mitigation techniques. |

#### What to Watch For

- Separate source reliability from the credibility of a specific piece of information.
- Use estimative language for the judgment, while keeping confidence and sourcing visible as separate ideas.
- Choose structured techniques and bias mitigations because they improve a real analytical decision, not because the method itself is the product.

#### Expected End State

By the end of this subunit, you should be able to:

- use consistent estimative language to communicate probabilistic judgments;
- evaluate source reliability and information credibility as separate dimensions;
- apply structured techniques to test assumptions or alternatives;
- recognize common cognitive biases and choose a mitigation that improves the analysis.

#### How to Preview This Subunit

Read this introduction, then skim the [2.2 Summary](#22--analytical-tradecraft-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 2.2.1 — Estimative language

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain why estimative language is used and interpret the classroom likelihood terms.
2. Write an analytic judgment using a likelihood term and distinguish likelihood from confidence in the supporting evidence.

#### Key Concepts

Analysts often have to make a judgment before every uncertainty has been resolved. Estimative language gives the reader a consistent way to understand **how probable the analyst believes a claim is**. Instead of leaving the reader to interpret vague phrases such as “could be” or “we believe,” the analyst uses a term with an agreed meaning.

This course uses the following classroom scale:

| Term | Meaning in this lesson |
|---|---|
| **Almost certainly** | Near certain; you would be surprised if it were not true. |
| **Highly likely** | Very probable. |
| **Likely** | More probable than not. |
| **Even chance** | About as likely as not. |
| **Unlikely** | More probable that it is not true. |
| **Highly unlikely** | Very improbable. |
| **Remote** | Very little chance. |

These terms are a teaching scale for this course. An organization may publish its own terminology or probability ranges; when it does, analysts should use that standard consistently rather than inventing their own percentages.

##### Likelihood and confidence answer different questions

A likelihood term describes **the probability of the judgment**. Confidence describes **how strongly the available evidence and reasoning support that judgment**. They can appear together because they communicate different things.

For example:

> We assess that the update domain was **likely** used for attempted payload delivery in A12, with **medium confidence**.

“Likely” tells the reader how probable the analyst judges the delivery role to be. “Medium confidence” tells the reader how much weight to place on that judgment given the quality, quantity, and consistency of the supporting evidence.

A judgment can therefore have a relatively high likelihood while still carrying limited confidence if the evidence base is thin. Keeping the two ideas separate prevents the reader from treating strong wording as a substitute for strong evidence.

##### Why vague possibility words are not enough

Words such as *could*, *may*, and *might* can be useful in ordinary writing, but by themselves they usually say only that something is possible. They do not tell the reader whether the analyst sees the explanation as remote, evenly balanced, or likely.

Suppose the analyst writes:

> The update domain could have been used for attempted payload delivery in A12.

The reader still has to guess how strongly the analyst favors that explanation. Compare it with:

> The update domain was **likely** used for attempted payload delivery in A12.

The second sentence communicates the probability judgment more precisely while preserving the same claim about attempted delivery. The HTTP request during suspicious activity supports that interpretation; successful transfer and execution remain unresolved. Changing the likelihood term changes how probable the analyst judges the claim to be, rather than adding evidence of a completed transfer.

##### Interpreting the term in context

An estimative term modifies the claim it is attached to. In the statement “It is **remote** that the traffic represents ordinary browsing,” *remote* means the analyst judges ordinary browsing to have very low likelihood. It does not mean the analyst has no evidence or has refused to make a judgment.

The underlying reasoning still matters. Estimative language communicates the strength of the judgment; it does not replace the evidence and analysis that support it.

#### Knowledge Check

1. Why are “likely” and “high confidence” not interchangeable?
2. A report says, “The update domain could be related to A12.” What important information is missing from that wording?
3. Write one A12 judgment using a classroom likelihood term and, if appropriate, a separate confidence statement.

#### Summary

Estimative language makes analytic uncertainty easier for readers to understand and compare. A likelihood term communicates how probable the analyst judges a claim to be. Confidence communicates how strongly the evidence and reasoning support that judgment. Using both deliberately gives the reader more information than vague possibility language alone.

#### Related Reading

- [2.1.8 — Attribution confidence](#218--attribution)
- [2.1.9 — Collection sources](#219--collection-sources-and-methods)
- [2.2.2 — Structured analytic techniques](#222--structured-analytic-techniques)
- [2.2.3 — Admiralty Code](#223--admiralty-code)

#### References and Further Reading

[ODNI, ICD 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf): supports clear expression of uncertainty, likelihood, and confidence in analytic judgments. The classroom scale above is an instructional scale rather than a quoted ODNI probability table.

### 2.2.2 — Structured Analytic Techniques

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain why structured analytic techniques are useful and choose between a **Key Assumptions Check** and **Analysis of Competing Hypotheses (ACH)** for a given problem.
2. Apply the selected technique to a short analytic problem and explain what it reveals about the judgment.

#### Key Concepts

Analysts rarely begin with a completely blank mind. A first explanation may already feel plausible, a vendor report may supply a convenient label, or a familiar pattern may shape what the analyst expects to find. Structured analytic techniques provide a deliberate way to examine that reasoning before the preferred explanation becomes the conclusion by default.

The point of a structured technique is not extra paperwork. It is to make part of the reasoning visible and testable so another analyst can understand what was challenged and why the judgment changed—or did not change.

This lesson uses two techniques:

| Technique | Best fit | Core question |
|---|---|---|
| **Key Assumptions Check** | One or more assumptions are carrying the judgment. | What are we treating as true, and what happens if that assumption is weak or false? |
| **Analysis of Competing Hypotheses (ACH)** | Two or more plausible explanations remain live. | Which evidence is most consistent or inconsistent with each explanation, and which evidence actually distinguishes among them? |

##### Key Assumptions Check

An assumption is something the analysis relies on without directly establishing it. Some assumptions are reasonable and necessary; the risk comes when an important assumption remains invisible.

A compact Key Assumptions Check can be done in four steps:

1. State the draft judgment.
2. Identify the assumptions that must be true for that judgment to hold.
3. Ask what evidence supports each assumption and what would weaken or break it.
4. Decide whether the judgment still holds if a critical assumption changes.

Consider an attribution claim: a vendor report labels the activity “PRD APT,” and the draft assessment treats that label as proof of who conducted the activity. A Key Assumptions Check makes the hidden step explicit:

**Assumption:** the vendor tracking name identifies the actual sponsor of the activity.

Once stated, the analyst can test it. A tracking label may identify a cluster of activity without establishing government sponsorship. The exercise does not automatically prove the draft wrong; it shows exactly what additional evidence the conclusion depends on.

##### Analysis of Competing Hypotheses

ACH is useful when the analyst has multiple plausible explanations and wants to avoid evaluating evidence only through the favorite one.

A compact classroom ACH can be done in four steps:

1. State the competing hypotheses.
2. List the important evidence relevant to them.
3. Compare how well each item fits—or conflicts with—each hypothesis.
4. Give extra attention to **diagnostic evidence**: evidence that helps distinguish one hypothesis from another.

For A12, consider:

- **H1:** the update domain was being used for payload delivery.
- **H2:** the request was ordinary browsing or software activity unrelated to the incident.

The request for `/update.exe` on port `8080` during the suspicious activity is harder to reconcile with H2 than with H1. That makes it useful because it helps discriminate between the explanations. The analyst should still consider what evidence would weaken H1 rather than simply counting how many facts appear to support it.

##### Choosing the technique

Use a Key Assumptions Check when the main risk is an untested premise inside the current judgment. Use ACH when the problem is better represented as competing explanations that need to be compared against the same evidence.

The techniques can be used together in real analysis, but the learning objective here is to choose the method that best addresses the immediate reasoning problem and apply it deliberately.

#### Knowledge Check

1. A draft judgment depends on the assumption that a vendor tracking name identifies a government sponsor. Which technique is the better first fit, and why?
2. An analyst has two plausible explanations for an A12 network request. Which technique is the better fit, and what kind of evidence should receive the most attention?
3. In the A12 ACH example, explain why `/update.exe` over port `8080` during suspicious activity is more useful than simply saying “the domain appeared in the case.”

#### Summary

Structured analytic techniques make important parts of the analyst's reasoning visible and testable. A Key Assumptions Check examines the premises carrying a judgment. ACH compares multiple plausible explanations and pays particular attention to evidence that distinguishes among them. The method should match the reasoning problem the analyst needs to test.

#### Related Reading

- [2.2.1 — Estimative language](#221--estimative-language)
- [2.2.3 — Admiralty Code](#223--admiralty-code)
- [2.2.4 — Cognitive biases](#224--cognitive-biases-and-mitigation)
- [2.1.8 — Attribution](#218--attribution)

### 2.2.3 — Admiralty Code

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Evaluate **source reliability** (A–F) separately from **information credibility** (1–6).
2. Combine the two ratings into an Admiralty Code and explain what the pair communicates.

#### Key Concepts

When analysts receive reporting, two questions need to stay separate:

1. **How reliable is this source generally?**
2. **How credible is this particular piece of information?**

A source with a strong history can still provide a weak or unconfirmed claim. A source whose reliability is unknown can occasionally provide information that later proves correct. The Admiralty Code keeps those judgments separate by assigning a **letter** to the source and a **number** to the information.

##### The two scales

| Source reliability | Information credibility |
|---|---|
| **A** – Completely reliable | **1** – Confirmed by other sources |
| **B** – Usually reliable | **2** – Probably true |
| **C** – Fairly reliable | **3** – Possibly true |
| **D** – Not usually reliable | **4** – Doubtful |
| **E** – Unreliable | **5** – Improbable |
| **F** – Reliability cannot be judged | **6** – Truth cannot be judged |

A complete rating combines the two, such as **B2**.

The letter and number answer different questions. **B2** means the source is usually reliable and this particular information is assessed as probably true. The source's history does not automatically make the information confirmed, and the apparent plausibility of one claim does not automatically make the source highly reliable.

##### How to think about source reliability

Source reliability should be based on what is known about the source over time: its access, record of accurate reporting, consistency, and the degree to which its reliability can actually be evaluated.

The source category alone is not enough. “Internal,” “commercial,” or “OSINT” does not automatically map to a particular letter. For example, an internal sensor with a well-understood collection function and a strong history may merit a different rating from a newly deployed sensor whose behavior has not yet been validated.

##### How to think about information credibility

Information credibility concerns the specific claim. Relevant considerations include corroboration, consistency with independently observed facts, plausibility, directness of the reporting, and whether contradictory evidence exists.

A **1** requires confirmation by other sources. A single report from a trusted source does not become a 1 merely because the source has a high reliability rating.

##### F and 6 mean different things

**F** means the analyst cannot judge the reliability of the source. **6** means the analyst cannot judge the truth of the information. Those conditions often appear together, but they are still separate judgments.

For example, an anonymous public post with no history and a claim that cannot be corroborated might reasonably be rated **F6**. If later independent evidence confirms the claim, the information rating could change even though the original source's reliability remains unknown.

##### Worked examples

Suppose a sensor has an established record that supports a **B** source rating. It reports a connection that is independently confirmed by host evidence. The combined rating would be **B1**: usually reliable source, information confirmed by another source.

Now consider an unsigned public post from an unknown author making a claim that cannot be checked against any other evidence. The source reliability may be **F**, and the information credibility may be **6**. The rating communicates uncertainty about both dimensions without pretending they are the same uncertainty.

The number in an Admiralty rating is not an estimative-likelihood term. “Probably true” on the credibility scale and “likely” in an analytic judgment belong to different systems and answer different questions.

#### Knowledge Check

1. Why does a highly reliable source not automatically make a particular claim confirmed?
2. A source is usually reliable, and another independent source confirms the specific claim. What Admiralty rating fits that scenario, and what does it mean?
3. An anonymous source has no reliability history, and the claim cannot be corroborated or evaluated. What rating is reasonable, and why?

#### Summary

The Admiralty Code separates the reliability of the source from the credibility of the information. The letter describes the source; the number describes the particular claim. Keeping the two ratings independent prevents a trusted source from turning every claim into confirmed information and prevents one plausible claim from becoming a blanket endorsement of the source.

#### Related Reading

- [2.2.1 — Estimative language](#221--estimative-language)
- [2.2.2 — Structured analytic techniques](#222--structured-analytic-techniques)
- [2.2.4 — Cognitive biases](#224--cognitive-biases-and-mitigation)
- [2.1.8 — Attribution confidence](#218--attribution)

### 2.2.4 — Cognitive Biases and Mitigation

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Recognize **confirmation bias**, **anchoring**, and **availability bias** in an analytic judgment and explain how each can distort the product.
2. Select and apply a structured mitigation that gives the judgment a meaningful opportunity to change.

#### Key Concepts

Cognitive biases are predictable shortcuts in human judgment. Analysts cannot eliminate them by simply deciding to “be objective.” The practical goal is to recognize where a judgment is vulnerable and use a process that forces the reasoning to encounter evidence or alternatives it might otherwise ignore.

This lesson focuses on three biases:

| Bias | What happens | Risk to the product |
|---|---|---|
| **Confirmation bias** | The analyst gives more attention to evidence that fits the favored explanation and discounts evidence that does not. | Alternatives receive an unfair test and the judgment becomes harder to revise. |
| **Anchoring** | An early label, number, or explanation has too much influence on later reasoning. | New evidence is interpreted around the first frame instead of being allowed to change it. |
| **Availability bias** | Recent, vivid, or memorable examples come to mind more easily and feel more representative than they are. | A new event is treated like the last memorable incident without enough shared evidence. |

The task is to identify the **effect on the judgment**, not diagnose the personality or motives of the person who wrote it.

##### Confirmation bias

Suppose an analyst already favors the idea that the update domain was a payload host. If the analyst records every suspicious detail supporting that idea but ignores evidence of legitimate software activity, confirmation bias can strengthen the conclusion without actually strengthening the analysis.

A useful mitigation is **ACH** because it requires the analyst to compare the same evidence against competing explanations and look deliberately for evidence that is inconsistent with the favored one.

##### Anchoring

Suppose the first report calls the cluster “PRD APT.” Later analysis begins with the unstated assumption that the vendor tracking name identifies a government sponsor. The first label has become an anchor.

A **Key Assumptions Check** can expose the dependency: “vendor label = actual sponsor.” Once written down, the analyst can ask what evidence supports that assumption and what would cause it to fail.

##### Availability bias

Suppose the analyst recently worked A12 and then sees a new incident involving PowerShell. Because A12 is vivid and easy to recall, the analyst may prematurely treat the new event as related even when there is no shared infrastructure, file, host, or other meaningful linkage.

A useful mitigation is to make the comparison explicit. ACH can compare “related to A12” against “unrelated activity,” while a Key Assumptions Check can test the premise that superficial similarity implies common origin.

##### Mitigation is a process, not a pep talk

“Be more objective,” “keep an open mind,” or “avoid bias” are good intentions, but they do not create a repeatable test. A mitigation should change what the analyst **does** with the reasoning.

The two methods already taught in Module 2.2.2 are sufficient for this lesson:

- **Key Assumptions Check:** expose a premise carrying the judgment and test how fragile it is.
- **ACH:** compare competing explanations against the same evidence and seek evidence that discriminates among them.

The goal is not to prove that the first judgment was wrong. The goal is to give it a fair opportunity to change if the evidence does not support it.

#### Knowledge Check

1. Why is “be more objective” not a sufficient bias mitigation?
2. A vendor tracking name is introduced early and later evidence is interpreted around it. Which bias is most directly illustrated, and what mitigation would help?
3. A new PowerShell incident is assumed to be A12-related mainly because A12 was the analyst's most recent case. Which bias is illustrated, and how could the analyst test that assumption?

#### Summary

Confirmation bias favors evidence that fits the current explanation. Anchoring gives the first frame too much influence. Availability makes vivid or recent examples feel more representative than they are. Effective mitigation changes the analyst's process by exposing assumptions or comparing alternative explanations, giving the judgment a real chance to move when the evidence warrants it.

#### Related Reading

- [2.2.2 — Structured analytic techniques](#222--structured-analytic-techniques)
- [2.2.3 — Admiralty Code](#223--admiralty-code)
- [2.1.8 — Attribution](#218--attribution)
- [2.4.1 — Internal threat intelligence platform](#241--internal-threat-intelligence-platform)

### 2.2 – Analytical Tradecraft: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Evaluate sources → structure reasoning → test alternatives → express the judgment and uncertainty clearly**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- use consistent estimative language to communicate probabilistic judgments;
- evaluate source reliability and information credibility as separate dimensions;
- apply structured techniques to test assumptions or alternatives;
- recognize common cognitive biases and choose a mitigation that improves the analysis.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **2.2.1 – Estimative Language** | Express probability and uncertainty with consistent estimative terms. |
| **2.2.2 – Structured Analytic Techniques** | Use structured methods to expose assumptions, alternatives, and evidence relationships. |
| **2.2.3 – Admiralty Code** | Evaluate source reliability separately from information credibility. |
| **2.2.4 – Cognitive Biases and Mitigation** | Recognize common analytical biases and apply practical mitigation techniques. |

#### Check Your Understanding

Ask yourself:

1. Why should source reliability and information credibility be evaluated separately?
2. When is a structured analytic technique useful instead of simply adding process?
3. What is the difference between expressing probability and describing how much confidence you have in the judgment?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **2.3 – Analytical Frameworks: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 2.3 – Analytical Frameworks: Introduction

**Estimated Time:** 5–10 minutes  

#### Why This Subunit Matters

Analytical frameworks help you organize evidence so that another analyst can understand **what happened, how the pieces relate, and where the activity fits in a larger intrusion**. They are most useful when they make reasoning easier to inspect—not when they replace the evidence or make a conclusion sound stronger than the source material supports.

In the previous subunit, Analytical Tradecraft, you focused on how to evaluate information, express uncertainty, structure analysis, and reduce bias. This subunit builds on that discipline by giving you three different ways to organize the evidence you have already evaluated.

The important question is not, “Which framework is best?” It is:

> **Which framework helps answer the analytical question in front of me?**

#### What You Will Learn

The three frameworks in this subunit look at different aspects of the same activity.

| Lesson | Main question | What the framework contributes |
|---|---|---|
| **2.3.1 – MITRE ATT&CK for CTI** | What behavior does the evidence demonstrate? | A shared vocabulary for mapping observed or reported behavior to supported tactics, techniques, and sub-techniques. |
| **2.3.2 – Diamond Model** | What entities and relationships make up this intrusion event? | A way to organize Adversary, Capability, Infrastructure, and Victim while keeping uncertain vertices visible. |
| **2.3.3 – Cyber Kill Chain** | Where does the supported activity fit in attack progression? | A way to describe progression while leaving unsupported stages unresolved. |

You may use more than one framework on the same evidence because each one answers a different question.

#### Connect to What You Already Know

From **2.2 Analytical Tradecraft**, you already have several habits that matter here:

- evaluate the quality and credibility of the information before relying on it;
- separate what the evidence directly supports from what you infer;
- use estimative language when a judgment is probabilistic;
- make uncertainty visible rather than hiding it;
- watch for analytical shortcuts and cognitive bias.

Those habits continue to apply when a framework gives you convenient labels or boxes. A framework can organize a judgment, but it does not create evidence that was not present before.

#### What to Watch For

As you work through the three lessons, pay particular attention to these ideas.

##### The analytical question should drive the framework

ATT&CK, the Diamond Model, and the Cyber Kill Chain are not interchangeable. Each highlights a different dimension of the activity. Start with the question you need to answer, then select the framework that helps organize that question.

##### A framework label does not strengthen weak evidence

A technique ID, Diamond vertex, or Kill Chain stage can make an analysis look precise. The precision is useful only when the underlying evidence supports it.

##### Unknown or unresolved is a valid analytical result

You do not need to fill every Diamond vertex, assign every Kill Chain stage, or map every plausible ATT&CK technique. An unresolved field can tell the reader exactly where the evidence becomes thin.

##### The same evidence can support different views without becoming different evidence

For example, a PowerShell process can be:

- mapped to an ATT&CK behavior;
- described as part of the Capability vertex in a Diamond;
- considered in the context of attack progression for the Kill Chain.

Those are different analytical views of the same underlying observation.

#### Expected End State

By the end of this subunit, you should be able to:

- select a framework based on the analytical question you are trying to answer;
- map observed or reported behavior to ATT&CK while preserving the supporting evidence;
- populate a Diamond Model event without filling uncertain vertices with guesses;
- assign Cyber Kill Chain stages only when the surrounding evidence supports the stage;
- explain how the three frameworks complement one another without treating any of them as proof by themselves.

#### How to Preview This Subunit

Before reading the individual lessons closely:

1. read this introduction;
2. read the **2.3 Analytical Frameworks Summary**;
3. skim the headings, tables, examples, and emphasized terms in the three lessons.

Try to predict which framework you would use for each kind of analytical question. Then return to the summary after the detailed reading and check whether your answers have become more precise.

### 2.3.1 — MITRE ATT&CK for CTI Analysis and Reporting

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Map behavior from a report or activity set to an ATT&CK tactic and the most specific technique or sub-technique supported by the evidence.
2. Explain the evidence for the mapping and distinguish it from a nearby ATT&CK choice that would require evidence the product does not contain.

#### Key Concepts

MITRE ATT&CK gives analysts a shared vocabulary for describing adversary behavior. In a CTI product, the value of an ATT&CK mapping is not the ID by itself. The value comes from showing **which observed or reported behavior supports the mapping**.

A useful mapping starts with the evidence and moves to ATT&CK—not the other way around.

| ATT&CK element | Question it answers |
|---|---|
| **Tactic** | Why is the adversary performing this behavior at this point? |
| **Technique** | What general method is being used? |
| **Sub-technique** | What more specific implementation of the technique is supported? |
| **Procedure / evidence** | What concrete command, event, report sentence, or observation shows the behavior in this case? |

The [MITRE ATT&CK Enterprise knowledge base](https://attack.mitre.org/) is the authoritative reference for current tactic, technique, and sub-technique definitions.

##### Map the behavior you actually have

Consider:

`wscript.exe` → `powershell.exe -enc ...`

The observable behavior is PowerShell execution. ATT&CK defines **T1059.001 – PowerShell** under the **Execution** tactic.

A strong CTI mapping is:

> **Execution / T1059.001 PowerShell** — supported by `powershell.exe -enc` launched by `wscript.exe`.

Reference: [MITRE ATT&CK – T1059.001 PowerShell](https://attack.mitre.org/techniques/T1059/001/)

The mapping does not need to guess what the PowerShell process might do later. If there is no callback in the evidence, there is no reason to add a Command and Control behavior merely because PowerShell *can* be used for C2.

##### Use the most specific supported technique

If the evidence clearly identifies PowerShell, use **T1059.001** rather than stopping at the broader parent **T1059 Command and Scripting Interpreter**.

That does not mean “always choose the longest ID.” It means choose the most specific technique the evidence supports.

If a report only says “a command interpreter was used” and does not identify which one, the parent technique may be the defensible mapping.

##### Map separate behaviors separately

One activity set can contain several behaviors.

Suppose the evidence shows:

1. `powershell.exe -enc ...`
2. the host successfully downloaded `/update.exe` from an external system.

The first behavior supports **T1059.001 PowerShell**.

The second can support **T1105 – Ingress Tool Transfer** when the evidence establishes that a tool or file was transferred from an external system into the compromised environment.

Reference: [MITRE ATT&CK – T1105 Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)

An HTTP request name alone is weaker evidence than a confirmed transfer. If all you know is that a request for `/update.exe` occurred, say exactly that. A response, file creation, or other transfer evidence makes the T1105 mapping stronger.

##### A nearby technique may look plausible for the wrong reason

The best way to resolve close choices is to compare the ATT&CK definition with the behavior in the product.

For example:

- `powershell.exe -enc` → **T1059.001**
- confirmed external file transfer → **T1105**
- HTTP alone does not make something a command interpreter
- PowerShell alone does not make something Command and Control

The question is always: **what behavior does this evidence demonstrate?**

##### Cite the evidence with the mapping

A reusable CTI mapping should preserve enough evidence that another analyst can review the decision.

A simple format is:

`Tactic | ATT&CK ID | Technique | Evidence`

Example:

`Execution | T1059.001 | PowerShell | powershell.exe -enc launched by wscript.exe`

This makes the ATT&CK line useful to threat hunting, detection engineering, and future analysis because the ID remains tied to the observation that produced it.

#### Knowledge Check

1. `wscript.exe` launches `powershell.exe -enc`. What tactic and ATT&CK sub-technique are supported, and what evidence would you cite?
2. A report says only that the host requested `/update.exe`. What additional evidence would make **T1105 Ingress Tool Transfer** a stronger mapping?
3. Why is “choose the most specific supported technique” better guidance than either always using the parent technique or always choosing the most detailed ID available?

#### Summary

ATT&CK mapping is evidence-bound behavior classification.

Start with the report or activity, identify the behavior, use the most specific ATT&CK technique or sub-technique the evidence supports, and preserve the evidence beside the ID. A nearby technique belongs in the product only when its own behavioral definition is actually demonstrated.

#### Related Reading

- [2.5.4 — Advanced DNS](#254--advanced-dns-concepts)
- [2.3.2 — Diamond Model for CTI](#232--diamond-model-application-in-cti)
- [0.6.1 — ATT&CK shared-floor introduction](#061--mitre-attck)
- [3.5 — Hunt planning with ATT&CK](#351--using-mitre-attck-for-hunt-planning)
- [2.6.1 — TTP applicability to the environment](#261--extracting-applicable-ttps-from-intelligence-reports)

#### References and Further Reading

- [MITRE ATT&CK](https://attack.mitre.org/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)
- [T1105 – Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/)

### 2.3.2 — Diamond Model Application in CTI

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Populate the four Diamond Model core features from a report or activity set using evidence.
2. Identify which vertex is least developed and explain how that uncertainty constrains the intelligence product.

#### Key Concepts

The Diamond Model treats an intrusion **event** as relationships among four core features:

- **Adversary**
- **Capability**
- **Infrastructure**
- **Victim**

The original paper describes these features as the core of an intrusion event and uses the edges between them to support analysis, correlation, and discovery.

Reference: [The Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/)

##### The four vertices

| Vertex | CTI question |
|---|---|
| **Adversary** | Who is responsible for or associated with the activity, at the level the evidence supports? |
| **Capability** | What capability, malware, tool, exploit, or method is being used? |
| **Infrastructure** | What infrastructure enables or carries the activity? |
| **Victim** | Who or what is being targeted or affected? |

A Diamond does not become invalid because one vertex is unknown. Incomplete knowledge is normal in intrusion analysis.

##### Apply the model to A12

For the A12 activity set:

- `wscript.exe` launches encoded PowerShell;
- A12 includes a request for `/update.exe`; that path is a **candidate payload name**, not an established transferred or executed sample;
- the update domain and `203.0.113.88` appear in the infrastructure;
- `WS-JLEE` / `jlee` are the affected victim assets.

A defensible Diamond is:

| Vertex | A12 fill |
|---|---|
| **Adversary** | Unknown / unresolved activity cluster |
| **Capability** | Encoded PowerShell; requested `/update.exe` as a candidate payload name |
| **Infrastructure** | Update domain; `203.0.113.88` |
| **Victim** | `WS-JLEE`; `jlee`; DYA |

The **Adversary** vertex is the least developed.

That is useful analytical information. It tells the writer that the product can describe capability, infrastructure, and victim with more specificity than it can describe who is behind the activity.

##### Vendor tracking names require source qualification

A vendor name such as “PRD APT” can be useful context if a source attributes the activity that way. But a tracking label is not automatically the same thing as independently established adversary identity.

A careful product can say:

> Vendor X tracks similar activity as “PRD APT.”

That preserves provenance.

It is stronger than silently changing the Diamond vertex to:

> Adversary = PRD APT

unless the product's own evidence and sourcing justify that conclusion.

This distinction keeps the Diamond useful as an analytical model rather than turning it into a place to copy labels.

##### Relationships matter as much as the boxes

The Diamond Model is not just four fields. The edges represent relationships that analysts can test and pivot across.

For example:

- capability ↔ infrastructure: Which infrastructure delivered or controlled this capability?
- infrastructure ↔ victim: Which victim interacted with this infrastructure?
- adversary ↔ capability: What evidence connects this capability to an activity cluster?
- adversary ↔ infrastructure: What evidence links the infrastructure to the same cluster?

Those relationships often reveal where the next intelligence question should go.

##### Classroom “weakest vertex”

This course uses **weakest vertex** as a practical checkpoint: identify which core feature has the least evidentiary support.

That phrase is a classroom aid, not a new fifth Diamond component. Its purpose is to make the analyst state where the model is least complete and avoid filling the gap with a guess.

#### Knowledge Check

1. What are the four core Diamond Model features?
2. In A12, why is the Adversary vertex less developed than Capability, Infrastructure, and Victim?
3. A vendor report calls the activity “PRD APT.” How can you preserve that information without presenting the vendor label as independently proven adversary identity?

#### Summary

The Diamond Model organizes an intrusion event around Adversary, Capability, Infrastructure, and Victim—and the relationships among them.

Use evidence to populate each vertex. Leave a vertex unresolved when the evidence is unresolved. In this course, naming the least-developed vertex helps keep uncertainty visible instead of completing the model with speculation.

#### References and Further Reading

- [The Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/)

### 2.3.3 — Cyber Kill Chain in Intelligence Analysis

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Use the seven Cyber Kill Chain stages to describe attack progression in an intelligence product.
2. Assign a stage only when the observed or reported activity supports that stage and explain when the evidence is insufficient to distinguish between stages.

#### Key Concepts

Lockheed Martin's Cyber Kill Chain describes seven stages adversaries progress through in a successful intrusion:

1. **Reconnaissance**
2. **Weaponization**
3. **Delivery**
4. **Exploitation**
5. **Installation**
6. **Command and Control**
7. **Actions on Objectives**

References:
- [Lockheed Martin – Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [Lockheed Martin overview PDF](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)

The value of the framework in CTI is to describe **progression that the evidence supports**. It is not a requirement to fill all seven stages.

##### What each stage means

| Stage | Evidence that can support it |
|---|---|
| **Reconnaissance** | Target research, scanning, or other preparation focused on understanding the victim. |
| **Weaponization** | Building or pairing exploit and payload before delivery. Often described in external reporting rather than victim telemetry. |
| **Delivery** | Transmitting the weapon or payload to the target environment. |
| **Exploitation** | Triggering exploitation or executing the delivered mechanism to gain code execution/access. |
| **Installation** | Installing or establishing malware, an implant, persistence, or other foothold on the victim. |
| **Command and Control** | Establishing or using a channel that allows adversary control/communication. |
| **Actions on Objectives** | Performing the intended mission effect, such as collection, theft, disruption, or destruction. |

##### Use Surrounding Context to Assign the Stage

A process event such as:

`wscript.exe` → `powershell.exe -enc ...`

shows execution. By itself, it does **not** necessarily tell you whether the Cyber Kill Chain role is Exploitation, Installation, or part of a later stage.

The surrounding context matters.

Examples:

- malicious script arrives by email → **Delivery**
- user/script execution triggers malicious code → may support **Exploitation**
- a payload is written and persistence is established → **Installation**
- the implant begins periodic callbacks → **Command and Control**

The framework is describing the role of the activity in the intrusion, not simply the name of the process.

##### A Download Supports Delivery More Directly Than Installation

For a separate progression exercise, suppose a record shows a successful download of `/update.exe`. This adds a hypothetical transfer condition for practice; successful transfer remains unresolved in the canonical A12 case.

That can support **Delivery** of a follow-on payload into the victim environment.

It supports **Installation** only when there is evidence that the payload was installed, established, or otherwise placed as the intrusion's foothold.

If the download occurs over an established control channel, it may also occur during Command and Control, but the file-transfer event itself does not prove the control relationship.

##### Gaps are valuable

If the product supports Delivery and Command and Control but contains no evidence of Reconnaissance or Weaponization, leave those stages unfilled.

That tells the reader something important about the evidence base.

The Kill Chain should help answer:

> Which parts of the progression do we actually know?

—not—

> Which stages probably happened because every attack has a beginning?

##### Worked progression example

For a separate hypothetical progression example, suppose reporting contains:

- phishing email with `invoice.vbs` → **Delivery**
- user launches the script and malicious code executes → **Exploitation**
- malware writes a persistent implant → **Installation**
- implant checks in to the update domain every 60 seconds → **Command and Control**

A CTI product can list those supported stages and leave Reconnaissance, Weaponization, and Actions on Objectives unresolved if they are not in the evidence.

#### Knowledge Check

1. Why should an intelligence product not list all seven Kill Chain stages by default?
2. A host successfully downloads `/update.exe`, but there is no evidence it executes or persists. Which stage is best supported, and which stage would require more evidence?
3. `wscript.exe` launches encoded PowerShell. Why is the process event alone not enough to declare “Installation”?

#### Summary

The Cyber Kill Chain describes attack progression, but stage assignment depends on context.

List only the stages the evidence supports. A delivery event does not automatically establish installation; code execution does not automatically establish persistence; network traffic does not automatically establish command and control.

Unobserved stages are useful gaps, not blanks that need to be filled.

#### References and Further Reading

- [Lockheed Martin – Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [Cyber Kill Chain overview PDF](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)

### 2.3 – Analytical Frameworks: Summary

**Estimated Time:** 5–10 minutes  

#### What This Subunit Built

The three frameworks in this subunit give you complementary ways to organize adversary activity. **ATT&CK classifies supported behavior. The Diamond Model organizes entities and relationships. The Cyber Kill Chain organizes supported progression.**

The skill is not simply remembering the names of the frameworks. It is recognizing which analytical question each one helps answer, then keeping the framework tied to the evidence that justified the mapping.

#### By This Point, You Should Be Able To

- explain the different analytical purpose of ATT&CK, the Diamond Model, and the Cyber Kill Chain;
- choose a framework based on the question you need to answer;
- map behavior to the most specific ATT&CK technique or sub-technique the evidence supports;
- populate Adversary, Capability, Infrastructure, and Victim from available evidence while leaving unresolved vertices unresolved;
- use the Cyber Kill Chain to describe supported attack progression without filling missing stages by assumption;
- preserve the evidence and uncertainty behind every framework mapping.

#### How the Pieces Fit Together

| Analytical question | Framework | Useful output | Evidence boundary to preserve |
|---|---|---|---|
| **What behavior does the evidence demonstrate?** | MITRE ATT&CK | Supported tactic / technique / sub-technique tied to the observation | A plausible technique is not a supported technique until the behavior in its definition is demonstrated. |
| **What entities and relationships make up the event?** | Diamond Model | Adversary, Capability, Infrastructure, Victim, and the relationships among them | An unknown vertex can remain unknown; a vendor label or candidate relationship does not automatically establish identity. |
| **Where does this activity fit in intrusion progression?** | Cyber Kill Chain | Supported stage or stages of the intrusion | A process, download, or network event needs surrounding context before it proves a particular stage. |

One piece of evidence may appear in all three views, but the framework does not change what the evidence itself says.

#### Integrated A12 Example

Consider several facts already used in the A12 training scenario:

- `wscript.exe` launches encoded PowerShell on **WS-JLEE**;
- the update domain and `203.0.113.88` are associated with the activity;
- the affected victim includes **WS-JLEE** / `jlee`;
- the adversary identity remains unresolved.

Each framework organizes those facts differently.

##### ATT&CK

The observed PowerShell behavior supports **T1059.001 – PowerShell** because the process evidence directly shows PowerShell execution.

The mapping remains tied to the process observation. It does not, by itself, prove what the PowerShell process did afterward.

##### Diamond Model

The same activity can populate parts of the Diamond:

- **Victim:** `WS-JLEE` / `jlee` / DYA
- **Capability:** encoded PowerShell and other supported tooling or behavior
- **Infrastructure:** the supported update-domain infrastructure
- **Adversary:** unresolved at the level currently supported by the evidence

The incomplete Adversary vertex is useful because it shows where the analysis has less support.

##### Cyber Kill Chain

The process chain alone does not tell you exactly which Kill Chain stage the activity represents. Stage assignment depends on the role the behavior played in the surrounding intrusion.

This is why the Kill Chain lesson asks you to use context rather than translating a process name directly into a stage.

#### A Practical Selection Rule

When you are deciding which framework to use, start with the question:

- **Behavior?** Start with ATT&CK.
- **Entities and relationships?** Start with the Diamond Model.
- **Progression?** Start with the Cyber Kill Chain.

You may use more than one when the intelligence problem needs more than one view.

#### Check Your Understanding

Ask yourself:

1. If two analysts map the same PowerShell event differently, can I explain which ATT&CK definition the evidence actually supports?
2. If the infrastructure and victim are well established but the actor is not, can I leave the Diamond adversary vertex unresolved and explain why?
3. If I observe a file download but do not know whether the payload executed or persisted, can I explain why I should not automatically call the activity Installation?
4. Can I explain why using three frameworks on one activity does not create three independent pieces of evidence?

If you can answer those questions clearly, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next subunit, **2.4 CTI Tools and Platforms**, shifts from organizing evidence to retrieving and examining it in the systems analysts use for CTI work.

The framework lessons give you analytical questions to ask. The platform lessons help you obtain and inspect information that may answer those questions. The same evidence-first rule still applies: **the platform returns information; the analyst decides what that information supports.**

### 2.4 – CTI Tools and Platforms: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

CTI platforms help analysts retrieve reports, relationships, infrastructure context, and sandbox observations. The analyst still has to choose the source that fits the question, preserve provenance, and understand what the platform result does and does not establish.

#### Connect to What You Already Know

The framework subunit focused on organizing evidence. This subunit shifts to the systems used to retrieve and inspect information that may become evidence for later enrichment and analysis.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **2.4.1 – Internal Threat Intelligence Platform** | Use the organization’s internal TIP as a starting point for available intelligence, relationships, and local context. |
| **2.4.2 – Selecting Platforms for CTI Work** | Choose a platform based on the analytical question and artifact type. |
| **2.4.3 – VirusTotal Relations and Behavior** | Retrieve file, URL, domain, IP, relation, and behavior context while preserving what each result represents. |
| **2.4.4 – ANY.RUN** | Use existing sandbox reports or authorized analysis to inspect observed file and network behavior. |
| **2.4.5 – Silent Push** | Use DNS and infrastructure context to support later infrastructure analysis. |
| **2.4.6 – urlscan.io** | Use web-scan results to inspect page, request, hosting, and related web infrastructure context. |

#### What to Watch For

- Let the question and artifact type drive platform selection.
- Distinguish an existing report lookup from submitting a new sample, URL, or artifact for analysis.
- Preserve source, timestamp, and result context so later analytical claims remain reviewable.
- Treat platform relationships as leads or evidence inputs whose analytical meaning is established later.

#### Expected End State

By the end of this subunit, you should be able to:

- choose among the available platforms based on the intelligence question and artifact;
- retrieve and interpret the main kinds of results each platform provides;
- distinguish lookup, enrichment, and new submission workflows;
- preserve platform evidence and limitations for the later enrichment and assessment steps.

#### How to Preview This Subunit

Read this introduction, then skim the [2.4 Summary](#24--cti-tools-and-platforms-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 2.4.1 — Internal Threat Intelligence Platform

**Estimated Time:** 20–25 minutes

#### Starting point

Use an existing case object to learn retrieval, provenance, and relationships. Select the correct object type using the TIP's labels; detailed STIX object construction is taught later in [2.7.1–2.7.2](#271--core-stix-objects). Confirm the site's access and handling rules before a live lookup.

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose and core functions of an internal threat intelligence platform (TIP), including how it supports enrichment, analysis, and production.
2. Search for an indicator or report, interpret what the platform returns, and use the result to support enrichment or analysis.

#### Key Concepts

A threat intelligence platform helps an organization organize the intelligence it already holds so analysts can find prior reporting, indicators, relationships, and observations before starting the same work again.

The word **internal** describes the organization's platform or workspace. It does not mean every item inside it came from an internal source. A TIP may contain material produced by the organization alongside commercial reporting, open-source reporting, imported indicators, and analyst-created relationships. The practical question is: **what has our organization already recorded about this object or topic?**

That makes the TIP useful at several points in the intelligence workflow.

| Function | What it helps the analyst do |
|---|---|
| **Store** | Preserve indicators, reports, notes, relationships, and sightings or observations. |
| **Search and retrieve** | Find existing objects and prior context related to a hash, IP address, domain, report, or other intelligence object. |
| **Relate** | Connect an observation or report to objects already in the platform when the evidence supports that relationship. |
| **Support production** | Reuse relevant internal context and cite what the organization already knows in an assessment or report. |

##### Search the object you actually have

A useful TIP search begins with the value and object type in front of you. If you have a domain, search for that domain as a domain object. If you have a file hash, search the appropriate hash value or file object.

This sounds simple, but it matters. An empty result only means something if the search was performed correctly. Searching the wrong object type, using a partial value when the platform expects an exact value, or overlooking alternate representations can create a false impression that the TIP contains nothing.

When a matching object exists, open it and examine the context already attached to it. Useful questions include:

- Where did this object come from?
- When was it added or last updated?
- What reports or observations are linked to it?
- Has the organization recorded a sighting or other relevant observation?
- What relationships are explicitly supported?
- Is any of the information stale, superseded, or source-limited?

The goal is not merely to find a hit. It is to understand what the hit actually tells you.

##### A hit adds context; it does not automatically prove the current case

Suppose you search the A12 update domain and find an existing TIP object. The object may contain a prior report, a related IP address, or an earlier organizational observation.

That information can enrich the current analysis, but the analyst still has to determine whether the older context applies to the present activity. A prior association is evidence to consider, not automatic proof that the same relationship still holds.

This is especially important when the object contains older reporting, vendor attribution, or relationships created for a different incident.

##### A miss is also information—but only about the TIP

If the search returns no matching object, record that result accurately: **no matching object found in the TIP** or **not found in TIP**, depending on local practice.

That result means the platform did not return a match under the search you performed. It does **not** mean the indicator is benign, new to the internet, or absent from every organizational data source.

A TIP miss may identify an intelligence gap or simply show that the platform has not yet captured the relevant context. The next step depends on the requirement: the analyst may need to check internal telemetry, an external source, or another collection path.

##### How the TIP supports enrichment, analysis, and production

**Enrichment** uses the platform to recover context already held by the organization: prior reporting, relationships, notes, source information, or observations.

**Analysis** compares that context with the current evidence. The analyst asks whether the existing relationships still fit the current case, whether the TIP adds useful corroboration, and what remains unresolved.

**Production** incorporates relevant TIP context into the finished assessment with enough provenance that another analyst can understand where the information came from. If the TIP search produced no match, that can also be recorded when it matters to the analytic story.

##### Following one A12 lookup

Assume you are examining the update domain from A12.

1. **Search:** Query the domain using the correct object type or field.
2. **Retrieve:** Open the matching object if one exists and review its sources, dates, relationships, and observations.
3. **Evaluate:** Decide which of that context is relevant to the A12 question and which relationships still require independent support.
4. **Use:** Incorporate supported context into the analysis, or record that no matching object was found.
5. **Relate when justified:** If the current evidence establishes a new observation or relationship, record it according to the platform's workflow rather than creating unsupported links.

A TIP is most useful when it helps the analyst reuse organizational knowledge without confusing **stored context** with **proven fact**.

#### Knowledge Check

1. You find an older TIP object for the A12 update domain that links it to a prior report. What should you check before treating that relationship as relevant to the current incident?
2. You search the correct domain object and the TIP returns no match. What does that result tell you, and what does it *not* tell you?
3. A file hash appears in a current investigation and the TIP contains a matching object with prior notes and a sighting. Explain how the TIP result can support enrichment and analysis without automatically deciding the current case.

#### Summary

The internal TIP is the organization's intelligence workspace for preserving and reusing context. Search the object you actually have, inspect the provenance and relationships behind any match, and use only the context that the evidence supports.

A TIP hit adds context; it does not automatically prove the current assessment. A TIP miss means no matching object was returned—it does not mean benign. Used carefully, the platform reduces duplicated work and makes prior organizational knowledge available to enrichment, analysis, and production.

#### Related Reading

- [2.2.4 — Cognitive biases and mitigation](#224--cognitive-biases-and-mitigation)
- [2.5.2 — File similarity and hashing techniques](#252--hashing-and-similarity-concepts)
- [0.7 — External tool survey](#07--external-tools)
- [2.4 — CTI Tools and Platforms](#24--cti-tools-and-platforms-introduction)
- [2.7 — STIX / structured intelligence authoring](#27--intelligence-production-and-dissemination-introduction)

### 2.4.2 — Selecting Platforms for CTI Work

**Estimated Time:** 10–15 minutes

#### Learning Objectives

1. Select a source for a defined CTI question and explain what the lookup can establish.
2. Capture an evidence record that preserves the object, source, time, result, and limitation.

#### Key Concepts

The introductory tool survey explained what the external tools are for. Here you choose a source for a specific intelligence question and carry its result into an evidence record.

Start with the requirement from 2.1 and an existing case value. Check what the internal TIP already holds, then use another source when it can answer a remaining question. Local handling restrictions determine whether a value can be submitted outside the organization; retrieving an existing public report and uploading an internal file are different actions.

| Question | Useful starting point | Record |
|---|---|---|
| What do we already know about this value? | Internal TIP | Linked reports, sightings, provenance, and time. |
| What does a known sample relate to, and what behavior was observed? | VirusTotal; ANY.RUN for available sandbox reports | Exact object/report, relationships or events, report time, and limitations. |
| What infrastructure associations were observed over time? | Silent Push; registration sources for registration questions | Record type, returned relationship, observation window, and source. |
| What did a recorded browser visit load or contact? | urlscan.io | Scan context, redirects, requests, destinations, and relevant time. |

##### Official platform references

Use these pages to confirm platform capabilities and terminology. Local handling rules still determine whether a case value may be submitted to an external service.

- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching)
- [ANY.RUN — Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/)
- [Silent Push — DNS Data](https://help.silentpush.com/docs/dns-data)
- [urlscan.io — Quickstart](https://docs.urlscan.io/guides/quickstart)

A tool result answers a narrower question than “Is everything related malicious?” A sandbox record describes the observed execution; a recorded browser visit describes that visit; a missing result reflects the queried source's coverage.

##### First pass through the platforms

For 2.4.3–2.4.6, retrieve a provided report or use an supplied static result. Identify the object, the report or observation time, one relevant field, and one limitation. Record:

`question | seed/object | source/report | query/observation time | result | meaning | next question`

Detailed interpretation returns with the method lessons. Work through VirusTotal and ANY.RUN evidence with file and behavioral analysis, Silent Push with DNS and infrastructure methods, and urlscan.io with web-infrastructure relationships. This keeps platform familiarity ahead of the exercise while putting interpretation beside the concepts it requires.

##### Stop when the question is answered

Do not visit every platform by default. Continue when a specific uncertainty could change the assessment. Preserve a result even when it is inconclusive, and explain what the next source is expected to add.

#### Knowledge Check

1. How does a CTI lookup differ from simply checking every available tool?
2. Which source would you start with for historical domain-to-IP observations, and what time context would you retain?
3. Why does access to an external platform not automatically authorize uploading a case file?

#### Summary

Choose a source for a defined question, preserve provenance and time, and continue only when another lookup can improve the answer.

### 2.4.3 — VirusTotal Relations and Behavior

**Estimated Time:** 20–25 minutes

#### How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an provided result, identify the retrieved file/report identity, report time, and one relationship or observed event, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.2](#252--hashing-and-similarity-concepts):** return to the detailed concepts, worked example, and knowledge check below when studying file relationships and sandbox behavior. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

#### Learning Objectives

By the end of this module, you will be able to:

1. Use VirusTotal relationship data to identify objects connected to a seed and select candidates for further enrichment.
2. Use VirusTotal behavior reports to extract sandbox-observed process, file, registry, and network activity while preserving the difference between an observed event and an analytic conclusion.

#### Key Concepts

VirusTotal organizes information around **objects** such as files, URLs, domains, and IP addresses. It also records **relationships** between objects—for example, a file related to a URL, a domain related to URLs, or a file related to other files.

Reference: [VirusTotal – Relationships](https://docs.virustotal.com/reference/relationships)

The course uses the familiar **Relations** view and **Behavior** view. The important distinction is analytical:

- **Relations** answers: *what other objects are linked to this seed in VirusTotal?*
- **Behavior** answers: *what did one or more sandbox reports observe this file doing?*

Neither answer automatically means “confirmed adversary infrastructure” or “confirmed behavior in our environment.”

##### Relations: linked objects, not automatic ownership

A relationship can expose useful candidates such as:

- contacted domains or IPs;
- URLs associated with a file;
- dropped or related files;
- other objects connected through VirusTotal's dataset.

VirusTotal's API documentation describes relationships as links or dependencies between objects.

A useful analyst statement is:

> VirusTotal relates the seed file to `198.51.100.77`; investigate whether that relationship is relevant to A12.

That is stronger than:

> `198.51.100.77` is adversary infrastructure because VirusTotal shows it.

The second statement skips the required contextual evaluation.

##### Behavior: sandbox observations

VirusTotal can contain multiple behavior reports for a file from sandbox systems. Behavior data may include:

- processes;
- files opened, created, or written;
- registry activity;
- network activity;
- loaded modules;
- ATT&CK technique associations.

Reference: [VirusTotal – File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)

A behavior report describes what that sandbox observed under its particular environment and execution conditions. Malware may behave differently across sandboxes, operating systems, time periods, network conditions, or execution paths.

So:

> Sandbox report observed `sync-client.exe` contacting `198.51.100.77:8080`.

is evidence.

It is not the same as:

> Every execution of `sync-client.exe` will contact that address.

##### Different sandboxes can produce different observations

If VirusTotal contains multiple behavior reports, compare them rather than assuming one report is complete.

A behavior absent from one sandbox report may be:
- genuinely absent;
- dependent on environment or timing;
- gated by anti-analysis logic;
- missed because execution ended early.

“Not observed” is narrower than “does not occur.”

##### Separate classroom card — not A12

This training-only card is **not canonical A12**. A12 does not provide a recovered `update.exe` sample, a SHA256, or VirusTotal behavior. The supplied values below exist only to practice Relations/Behavior interpretation.

Seed: SHA256 for `sync-client.exe`

The classroom card shows:

**Relations**
- contacted IP: `198.51.100.77`

**Behavior**
- process: `sync-client.exe` started;
- file: write under a Temp path;
- network: connection to `198.51.100.77:8080`;
- no registry Run-key event shown.

Defensible outputs:

> **Relationship candidate:** VirusTotal links the file to `198.51.100.77`.

> **Sandbox observation:** the behavior report recorded a connection to `198.51.100.77:8080`.

> **Registry:** no Run-key event is shown on this card.

Do not add `login-prd.net` or an `Updater` Run key unless the card actually contains it.

##### Detection labels are context, not the lesson output

Vendor detection counts and labels can be useful context, but they are not substitutes for Relations or Behavior evidence.

This lesson focuses on:
- linked objects;
- sandbox-observed events;
- evidence boundaries.

#### Knowledge Check

1. VirusTotal relates a file to an IP. What does that establish, and what still needs analysis?
2. A Behavior report does not show a registry persistence event. Can you conclude the file never uses registry persistence? Why or why not?
3. From the separate classroom card, write one valid Relations finding and one valid Behavior finding.

#### Summary

VirusTotal Relations provides linked objects that can become enrichment candidates. Behavior reports provide sandbox observations.

Treat both as evidence with provenance. A relationship is not automatic adversary ownership, and a sandbox event is not automatically universal behavior.

#### References and Further Reading

- [VirusTotal – Relationships](https://docs.virustotal.com/reference/relationships)
- [VirusTotal – File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)

### 2.4.4 — ANY.RUN

**Estimated Time:** 20–25 minutes

#### How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an provided result, identify the report identity, sample hash, and one process/file/network event, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.2](#252--hashing-and-similarity-concepts):** return to the detailed concepts, worked example, and knowledge check below when studying sandbox evidence and file context. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

#### Learning Objectives

By the end of this module, you will be able to:

1. Search ANY.RUN threat-intelligence data using a known IOC or relevant event field.
2. Review the linked sandbox evidence and extract process, file, registry, network, or other observations that can support analysis without treating a tag or verdict as ground truth.

#### Key Concepts

ANY.RUN combines interactive sandbox analysis with threat-intelligence lookup across sandbox research sessions.

Current ANY.RUN documentation supports single-IOC searches for values such as:
- URL;
- MD5, SHA1, SHA256;
- IP address;
- domain.

Its lookup capability can also search event fields and combine indicators/events.

References:
- [ANY.RUN Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)

##### Search from evidence you already have

The safest starting point is a seed already connected to your investigation.

Examples:
- SHA256 of `sync-client.exe`;
- `198.51.100.77`;
- update domain;
- a specific process command line from reporting.

This keeps enrichment tied to the requirement instead of browsing labels until an interesting family appears.

##### Review the session, not just the tag

A malware-family tag, threat name, or malicious verdict is useful metadata, but the analysis should be grounded in the session evidence.

Useful evidence can include:
- process tree and command line;
- contacted domains, IPs, and URLs;
- dropped or modified files;
- registry modifications;
- mutexes;
- Suricata/signature events;
- other recorded sandbox events.

A tag such as `lumma_stealer` is a **classification claim produced by the service**. Preserve it as provenance:

> ANY.RUN labels the session as `lumma_stealer`.

That is different from independently concluding:

> This is definitively Lumma Stealer.

##### Sandbox evidence is conditional

Like any sandbox, ANY.RUN observes behavior in a particular environment and execution.

Malware can change behavior because of:
- execution path;
- network availability;
- timing;
- user interaction;
- anti-analysis checks;
- operating-system or software differences.

So the correct evidence language is:

> The analyzed session observed...

—not—

> The malware always...

##### What makes an extract useful?

The best extracts are concrete enough to feed the next analytic or defensive step.

Example:

> ANY.RUN session observed `powershell.exe` launching with an encoded command.

or:

> ANY.RUN session observed a request to `/client.bin` on `sync-gateway.example`.

Those can inform:
- TTP analysis;
- infrastructure enrichment;
- hunt leads;
- further sandbox comparison.

A generic verdict such as “malicious” contains less operational detail.

##### Separate classroom card — not A12

This training-only sandbox card is **not canonical A12**. A12 does not provide a recovered `update.exe` hash or a sandbox execution. Use this card only to practice session-evidence interpretation.

Search seed: SHA256 for `sync-client.exe`

Suppose the card shows:
- process: `sync-client.exe`;
- child process: `powershell.exe`;
- contacted IP: `198.51.100.77`;
- dropped file: `stage.dat`;
- no check-in POST shown.

Valid output:

> ANY.RUN session observed `sync-client.exe` spawning PowerShell and contacting `198.51.100.77`.

If a check-in POST is absent from the card:

> No check-in POST is shown on this classroom result.

Do not reconstruct one from the broader course story.

#### Knowledge Check

1. Why is a malware-family tag weaker evidence than a concrete process or network event from the session?
2. Name two IOC types and two event types ANY.RUN can be used to search or investigate.
3. A classroom result has no check-in POST. What can you say, and what should you avoid claiming?

#### Summary

Search from a known IOC or relevant event field. Review the linked sandbox evidence. Preserve service labels as attributed metadata, and base your analysis on concrete events where possible.

Sandbox output describes what happened in that session—not every possible execution.

#### References and Further Reading

- [ANY.RUN Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)

### 2.4.5 — Silent Push

**Estimated Time:** 20–25 minutes

#### How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an provided result, identify the queried seed, returned record type, and observation window, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.4](#254--advanced-dns-concepts):** return to the detailed concepts, worked example, and knowledge check below when studying DNS records and historical relationships. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

#### Learning Objectives

By the end of this module, you will be able to:

1. Use Silent Push passive-DNS data to enrich a domain or IP with historical DNS observations.
2. Pivot from a seed to candidate infrastructure using record-specific PADNS relationships while considering time, hosting density, and distinctiveness.

#### Key Concepts

Silent Push provides passive-DNS and infrastructure intelligence that can help analysts examine how domains and IP addresses have been associated over time.

References:
- [Silent Push – DNS Data](https://help.silentpush.com/docs/dns-data)
- [Silent Push – Passive DNS and Record-Specific Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups)

Current Silent Push documentation supports forward and reverse PADNS lookups across record types including A, AAAA, CNAME, MX, NS, TXT, and SOA.

##### Passive DNS is historical observation

Authoritative DNS tells you what a zone publishes when queried.

**Passive DNS (PADNS)** stores observations of DNS relationships seen over time.

That lets an analyst ask questions such as:
- Which IPs has this domain resolved to?
- Which domains have been observed on this IP?
- Which domains share a nameserver?
- How did those relationships change over time?

A PADNS association means the relationship was **observed by the provider's data collection**. It is not proof that the relationship existed everywhere or for the entire time window.

##### Time matters

Infrastructure changes.

A domain that resolved to one address in January may resolve somewhere else in October.

When comparing two objects, record or consider:
- first/last seen;
- overlapping time window;
- whether the relationship is historical or current;
- whether the hosting environment is shared.

Two domains using the same IP five years apart are a weaker relationship than two suspicious domains co-resolving to a rare IP during the same campaign window.

##### Forward and reverse pivots

**Forward-style question**
> What addresses or DNS answers have been observed for this domain?

**Reverse-style question**
> What domains or records have been observed pointing to this address or server?

Silent Push also supports record-specific queries, so the analyst can pivot on more than just A records.

##### Density and shared hosting matter

An IP with hundreds or thousands of unrelated domains is less distinctive than an address hosting a small, suspicious cluster.

Likewise, a common managed nameserver is weaker evidence than a rare nameserver associated with a tight group of domains.

Silent Push can help identify candidate relationships, but **provider data does not remove the need for contextual judgment**.

##### A12 Case Study: Worked Example

Seed: `203.0.113.88`

Classroom result shows:
- update domain observed on the IP during the A12 period;
- `login-prd.net` observed on the same IP during an overlapping period;
- many unrelated hosts elsewhere in the larger cloud range.

A defensible result is:

> Silent Push PADNS shows the update domain and `login-prd.net` associated with `203.0.113.88` during overlapping time periods; `login-prd.net` is a candidate related domain.

A weak conclusion is:

> The entire `203.0.113.0/24` belongs to the actor.

##### Enrich first, then pivot

A useful workflow:

1. Query the seed.
2. Review observed record relationships and time.
3. Identify candidate related objects.
4. Ask how common the shared value is.
5. Compare additional records or independent sources.
6. Promote the relationship only as strongly as the evidence supports.

#### Knowledge Check

1. What is the difference between authoritative DNS and passive DNS?
2. Why does overlapping time matter when two domains share an IP?
3. Silent Push shows `login-prd.net` on the same IP as the update domain during the same period. What is the strongest first conclusion?

#### Summary

Silent Push helps reconstruct historical DNS relationships and find candidate infrastructure.

Use time, hosting density, record type, and distinctiveness to judge the relationship. A PADNS association is evidence of an observed DNS relationship—not automatic proof of common ownership.

#### References and Further Reading

- [Silent Push – DNS Data](https://help.silentpush.com/docs/dns-data)
- [Silent Push – Passive DNS and Record-Specific Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups)

### 2.4.6 — urlscan.io

**Estimated Time:** 20–25 minutes

#### How to use this platform guide

**Orientation now (about 5 minutes):** retrieve an provided result, identify the scan URL/time, visited page, and one request or redirect, and state one limitation. The first pass is about finding and recording evidence.

**Application with [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators):** return to the detailed concepts, worked example, and knowledge check below when studying web-infrastructure relationships. The lesson's total estimated time includes both passes; this is one lesson delivered in two parts. Complete its platform performance check during the application pass.

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain what a urlscan.io result captures about one browser scan of a URL.
2. Retrieve or interpret a scan result and extract page, redirect, requested-host, IP, certificate, and response evidence without treating one scan as permanent truth about the site.

#### Key Concepts

urlscan.io loads a URL in a browser environment and records information about that scan.

The Result API includes data such as:
- submitted and final URL;
- page title;
- primary IP;
- whether the page redirected;
- requested domains, IPs, and URLs;
- HTTP requests/responses;
- certificate information;
- screenshot and DOM when stored;
- service verdicts.

References:
- [urlscan.io API Documentation](https://urlscan.io/docs/api/)
- [urlscan.io Result API Reference](https://urlscan.io/docs/result/)

##### One scan is one observation

A urlscan result describes **that scan at that time under that scan environment**.

Web content can vary by:
- time;
- geography;
- cookies/session state;
- user agent;
- authentication;
- server-side logic;
- anti-bot or anti-analysis behavior.

Therefore:

> The scan observed a redirect to `example-login.test`.

is defensible.

> The URL always redirects there.

requires more evidence.

##### Requested hosts are useful pivot candidates

The browser may contact many domains and IP addresses while rendering a page.

Those can include:
- first-party infrastructure;
- CDNs;
- analytics;
- advertising;
- fonts;
- third-party scripts;
- malicious payload or redirect infrastructure.

A requested host should therefore be **classified before being treated as adversary infrastructure**.

The fact that a page loaded Google Fonts, a CDN, or common analytics does not make those services part of the malicious campaign.

##### Redirect chain is often more useful than the screenshot

A screenshot tells you what the rendered page looked like.

The redirect and request data can show:
- where the browser started;
- where it ended;
- which intermediate URLs were visited;
- which infrastructure delivered content.

For infrastructure analysis, those machine-readable relationships may be more useful than the visual appearance alone.

##### Search existing scans before submitting

urlscan's documentation recommends searching for existing scans before resubmitting.

A classroom course can safely work from static result cards without sending live organizational URLs to an external service.

If live submission is ever used operationally, **scan visibility matters**. urlscan supports visibility settings, and analysts should follow organizational policy before submitting sensitive, internal, tokenized, or otherwise private URLs.

Reference: [urlscan.io API Documentation – Submission and visibility](https://urlscan.io/docs/api/)

##### Separate classroom example — not A12

This static result is **training-only**. Its redirect/page/contact details are not facts of A12.

Suppose the result card shows:

- tasked URL: `https://sync-gateway.example/start`;
- final URL: `/download`;
- title: `Software Update`;
- requested host: `cdn-lab.example`;
- primary IP: `198.51.100.77`;
- redirect occurred;
- screenshot stored.

Valid observations:

> The scan redirected from the submitted URL to `/download`.

> The scan contacted `cdn-lab.example` and `198.51.100.77`.

> The rendered page title was `Software Update`.

These facts become candidates for enrichment. They do not by themselves prove that every host contacted is adversary-owned or that every visitor receives the same page.

#### Knowledge Check

1. Why should one urlscan result be described as an observation rather than permanent truth about a URL?
2. A page requests a common analytics domain and a rare host from the supplied classroom card. Should both automatically become adversary infrastructure? Why or why not?
3. Name three useful fields or evidence types you can extract from a urlscan result.

#### Summary

urlscan records one browser scan of a URL.

Use page metadata, redirects, requested domains/IPs/URLs, responses, certificates, screenshot, and DOM as evidence from that scan. Classify third-party dependencies before promoting them to adversary infrastructure, and follow organizational policy before submitting sensitive URLs.

#### References and Further Reading

- [urlscan.io API Documentation](https://urlscan.io/docs/api/)
- [urlscan.io Result API Reference](https://urlscan.io/docs/result/)
- [urlscan.io Quickstart](https://docs.urlscan.io/guides/quickstart)

### 2.4 – CTI Tools and Platforms: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Question → platform choice → retrieval/submission decision → result capture → evidence boundary → later analysis**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- choose among the available platforms based on the intelligence question and artifact;
- retrieve and interpret the main kinds of results each platform provides;
- distinguish lookup, enrichment, and new submission workflows;
- preserve platform evidence and limitations for the later enrichment and assessment steps.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **2.4.1 – Internal Threat Intelligence Platform** | Use the organization’s internal TIP as a starting point for available intelligence, relationships, and local context. |
| **2.4.2 – Selecting Platforms for CTI Work** | Choose a platform based on the analytical question and artifact type. |
| **2.4.3 – VirusTotal Relations and Behavior** | Retrieve file, URL, domain, IP, relation, and behavior context while preserving what each result represents. |
| **2.4.4 – ANY.RUN** | Use existing sandbox reports or authorized analysis to inspect observed file and network behavior. |
| **2.4.5 – Silent Push** | Use DNS and infrastructure context to support later infrastructure analysis. |
| **2.4.6 – urlscan.io** | Use web-scan results to inspect page, request, hosting, and related web infrastructure context. |

#### Teaching / Workflow Note

The individual platform lessons use a two-pass model: first learn retrieval and evidence boundaries here; apply the platforms again during the relevant 2.5 enrichment methods.

#### Check Your Understanding

Ask yourself:

1. Why is platform selection better driven by the question than by whichever tool an analyst knows best?
2. What is the difference between looking up an existing sandbox report and detonating a new sample?
3. Why should a platform relation be preserved with provenance before it is promoted into an analytical relationship?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **2.5 – Technical Enrichment and Discovery: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 2.5 – Technical Enrichment and Discovery: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Technical enrichment turns a seed indicator or artifact into additional context and candidate relationships. The challenge is to discover useful connections without treating every shared property as proof that two objects belong to the same adversary activity.

#### Connect to What You Already Know

The platform subunit showed where analysts retrieve technical context. This subunit focuses on the analytical methods that use those results: indicator handling, file similarity, registration, DNS, infrastructure pivoting, DTF, and correlation.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **2.5.1 – IOC Handling and Enrichment Concepts** | Track indicators, provenance, confidence, scope, and lifecycle decisions during enrichment. |
| **2.5.2 – Hashing and Similarity Concepts** | Use exact hashes and similarity relationships to connect or differentiate files without overstating equivalence. |
| **2.5.3 – RDAP and WHOIS Concepts** | Use registration and allocation data as infrastructure context with appropriate ownership limits. |
| **2.5.4 – Advanced DNS Concepts** | Use DNS records and historical patterns to understand infrastructure relationships and changes. |
| **2.5.5 – Identifying Additional Adversary Infrastructure from Seed Indicators** | Pivot from a seed through distinctive shared characteristics and evaluate candidate infrastructure. |
| **2.5.6 – MalasadaTech Defender's ThreatMesh Framework (DTF)** | Organize justified infrastructure pivots without mixing them with unrelated file or behavior relationships. |
| **2.5.7 – Correlation, Link Analysis, and Campaign Tracking** | Correlate multiple supported relationships while keeping candidate links, activity sets, campaigns, and attribution distinct. |

#### What to Watch For

- Track the seed, pivot, shared characteristic, provenance, and reason the relationship may be meaningful.
- Distinguish exact matches, similarity, co-hosting, shared registration, shared DNS, and other relationship types.
- Treat a candidate pivot as a question to corroborate, not as automatic proof of common control.
- Keep file/behavior pivots separate from infrastructure-only DTF relationships when their evidentiary logic differs.

#### Expected End State

By the end of this subunit, you should be able to:

- manage indicators and enrichment results with provenance and lifecycle context;
- use file, registration, DNS, and infrastructure evidence to generate defensible pivots;
- distinguish candidate relationships from corroborated relationships and broader campaign judgments;
- apply DTF to justified infrastructure relationships while keeping other pivot types separate.

#### How to Preview This Subunit

Read this introduction, then skim the [2.5 Summary](#25--technical-enrichment-and-discovery-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 2.5.1 — IOC Handling and Enrichment Concepts

**Estimated Time:** 15–20 minutes

#### Learning Objectives

1. Distinguish an observable from an operational IOC and choose retain, enrich, review/expire, or reject.
2. Record a question-driven enrichment lookup with provenance and label any resulting pivot as a candidate.

#### Key Concepts

Analysts work with technical values such as hashes, domains, IP addresses, URLs, filenames, and certificates.

Those values are **observables**: technical facts that can be recorded and related to higher-level intelligence.

An observable becomes operationally useful as an **indicator / IOC** when the analyst has enough context to associate it with suspicious or malicious activity and use it for detection, investigation, enrichment, or tracking.

The distinction matters because **not every observable is malicious**.

The STIX 2.1 standard makes a similar distinction:
- Cyber-observable Objects represent observed technical facts.
- An Indicator contains a detection pattern intended to identify suspicious or malicious activity.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

##### IOC is a practical course term

Operational teams often use **IOC** broadly for malicious or suspicious technical indicators such as hashes, domains, IPs, and URLs.

This course uses that familiar term, but keeps the evidence boundary visible:

> `203.0.113.88` is an observable value.

It becomes a useful IOC when the case/reporting connects that address to the activity strongly enough for an operational purpose.

##### Four lifecycle decisions

| Decision | Meaning |
|---|---|
| **Retain / keep** | Evidence and provenance support continuing to use the indicator. |
| **Enrich** | Gather context that may change confidence, scope, relationships, or utility. |
| **Review / expire** | A previously valid indicator has aged, changed ownership, lost relevance, or reached the end of its useful validity. |
| **Reject / do not promote** | The candidate never had enough specificity or malicious context to become a useful IOC. |

This makes an important distinction:

A shared cloud `/24` containing one malicious address is usually **too broad to promote as an IOC**.

That is different from expiring a domain that was previously a strong indicator but is no longer useful.

STIX Indicators explicitly support `valid_from` and optional `valid_until`, reinforcing the idea that indicator utility can have a time window. See the [STIX 2.1 specification](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html), which defines Indicator validity with `valid_from` and optional `valid_until`.

##### Preserve provenance

For each retained indicator, keep enough context to answer:

- What is the value and type?
- What source connected it to malicious/suspicious activity?
- When was it observed or reported?
- What case, report, malware, or activity does it relate to?
- How confident are we in that relationship?
- Is the indicator still useful?

A raw value without provenance is easy to misuse later.

##### Enrichment should answer a question

A useful enrichment record states:

`object | source/tool | field or relationship sought | result | analytic meaning`

Example:

> `invoice.vbs SHA256 | internal TIP | prior sightings / linked reports | none found | no prior TIP context`

Then, if needed:

> `invoice.vbs SHA256 | public malware repository | detections / metadata | ... | adds external context`

The purpose is not to touch every tool. It is to retrieve information that could change the analysis.

##### A first enrichment record

Start with a value already in the case. State what you need to learn, select the source, and retain the result with its provenance. If a lookup reveals another object, record it as a candidate and explain the relationship; the later method lessons teach how to test that lead.

For A12, a TIP lookup with no matching hash means **no matching TIP result was returned**. It does not establish that the file is benign or absent from the environment. An external lookup should answer a defined remaining question and comply with the site's handling rules.

Preserve this enrichment record through the following lessons. Use [2.5.7 – Correlation and Link Analysis](#257--correlation-link-analysis-and-campaign-tracking) to combine the resulting evidence into a supported activity-set or campaign assessment.

#### Knowledge Check

1. Why is a raw IP address not automatically an IOC?
2. One bad IP sits inside a busy cloud /24. Should you promote the whole range, expire it, or reject it as too broad?
3. A TIP lookup returns no matching hash. Write the result and identify what should guide the next lookup.

#### Summary

Keep provenance, manage validity, and enrich to answer a question. Preserve candidate relationships for testing in the following method lessons.

#### References and Further Reading

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### 2.5.2 — Hashing and Similarity Concepts

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain what **imphash**, **ssdeep**, and **TLSH** measure and use similarity results to identify samples that merit further comparison.
2. Extract and interpret **code-signing** information from a file without treating the signature as proof of trust or attribution.

#### Key Concepts

A cryptographic hash such as **SHA256** is useful when you need to know whether two files are exactly the same. Change the file and the SHA256 changes.

Threat intelligence often asks a different question: **is this new sample similar enough to another sample that it deserves comparison?**

Similarity techniques help analysts find candidates for that next step. They do not, by themselves, prove that two files belong to the same malware family, came from the same actor, or perform the same behavior.

This lesson uses three similarity techniques plus code-signing information:

| Technique | What it represents | How to interpret it |
|---|---|---|
| **imphash** | A hash derived from the ordered imports of a Windows PE file. | The same value means the files have the same normalized import structure under the algorithm. That can be a useful pivot, but it is not proof of common authorship or family. |
| **ssdeep** | A context-triggered piecewise or “fuzzy” hash based on file content. | Comparison produces a score from 0–100. Higher scores indicate greater similarity, but the score is not a percentage probability and does not prove relationship. |
| **TLSH** | A locality-sensitive hash that summarizes byte-level characteristics of sufficiently complex input. | Comparison produces a difference score. Lower values indicate greater similarity; 0 indicates extremely close or identical input under the comparison. |
| **Code-signing** | Digital-signature and certificate information attached to the file. | Identifies the signing publisher/certificate identity and helps verify file integrity. It does not prove the software is benign or that the named signer authored the malicious activity. |

##### imphash: a structural pivot

Windows PE files record imported libraries and functions. **imphash** derives a value from that ordered import information.

If two files have the same imphash, they share the import structure represented by the algorithm. That can be useful for finding samples that may have been built from similar source, a common builder, or a common packing process.

The important word is **may**. Mandiant's original description of imphash explicitly notes that matching values are useful for triage and discovery but should not be treated as a single point of attribution. Simple utilities, common packers, or shared builders can produce the same value across otherwise unrelated activity.

A matching imphash is therefore a **lead for comparison**, not a finished family judgment.

##### ssdeep: higher means more similar

**ssdeep** compares fuzzy signatures and returns a match score from 0 to 100. A higher score means the files share more matching structure according to the algorithm.

For classroom exercises, this course may use **50 or higher** as a simple threshold for selecting samples to examine further. That number is a teaching convenience, not a universal operational cutoff. The official ssdeep guidance warns that a match does not itself establish that two files are related; analysts should inspect the matching files and context.

Think of the result as:

> “These samples are similar enough to deserve comparison.”

—not—

> “These samples are definitely the same malware family.”

##### TLSH: lower means more similar

**TLSH** works in the opposite direction. Its comparison output is a **difference score**: lower values indicate greater similarity.

For classroom exercises, this course may use **30 or lower** as a simple threshold for selecting close candidates. As with ssdeep, operational thresholds should be calibrated to the corpus and use case rather than treated as universal policy.

Do not read a TLSH value as a percentage. A distance of 30 does not mean “30% similar.”

##### Similarity is evidence for a pivot, not the conclusion

Suppose `sync-client.exe` has a different SHA256 from a newly discovered file.

That tells you the files are not byte-identical.

Now suppose:
- they share an imphash;
- ssdeep reports a strong similarity score; or
- TLSH reports a small difference.

Those results justify deeper comparison. Useful next questions include:

- Do the files share imports, strings, configuration structure, or embedded resources?
- Do they communicate with related infrastructure?
- Do they exhibit similar behavior?
- Are the similarities better explained by a common packer or builder?
- Do multiple independent features point to the same relationship?

The strongest analytic statement is usually not “same family because the hash matched.” It is “the similarity result identified a candidate relationship that is supported—or not supported—by additional evidence.”

##### Code-signing: inspect the signature, certificate, and status

Code-signing information provides another useful dimension of file analysis.

For a signed Windows file, useful fields include:
- **signer / subject** — the identity represented by the signing certificate;
- **issuer** — the certificate authority or intermediate that issued the certificate;
- **validity period** — the certificate's not-before and not-after dates;
- **signature status** — whether the signature and certificate chain validate in the context of the system performing the check.

Microsoft Authenticode is designed to identify the software publisher and verify that signed code has not been modified since signing. That is valuable evidence, but it does not mean “signed = safe.” Certificates can be stolen, abused, revoked, expired, or used to sign unwanted software.

Likewise, **unsigned** means the file does not contain a usable code-signing signature under the check you performed. It does not mean the file is malicious, and it does not establish attribution.

##### Separate worked example — not A12

The files in this exercise are **training-only samples, not A12 evidence**. Canonical A12 does not supply a recovered `update.exe` sample or similarity hashes.

You compare a new PE file with `sync-client.exe`.

- SHA256 differs → the files are not byte-identical.
- imphash matches → they share the import structure represented by imphash.
- ssdeep score is 68 → the classroom exercise treats this as a strong similarity candidate.
- TLSH distance is 24 → the classroom exercise also treats this as a close candidate.
- the new file is signed by a certificate whose subject and issuer are visible → record those facts and verify signature status.

A reasonable conclusion is:

> The new sample is sufficiently similar to `sync-client.exe` to justify deeper comparison. The shared imphash and strong fuzzy-hash similarity support a possible relationship, but additional behavioral or structural evidence is needed before assigning a malware-family or actor relationship.

That statement uses the similarity evidence without asking it to prove more than it can.

##### Paired platform application

Return to [VirusTotal](#243--virustotal-relations-and-behavior) and [ANY.RUN](#244--anyrun). Retrieve a provided seed-file report, compare an exact hash with a similarity lead, and record one observed behavioral or structural feature that supports or weakens the proposed relationship. Preserve the report conditions and source/time. A similarity lead and an observed sandbox event answer different questions.

Keep the result with the enrichment record started in [2.5.1](#251--ioc-handling-and-enrichment-concepts).

#### Knowledge Check

1. Two PE files have the same imphash but different SHA256 values. What does the imphash match tell you, and what does it *not* establish?
2. ssdeep returns 72 while TLSH returns a difference of 22 for two samples. How do you interpret the direction of each score, and what should you do before calling the files related?
3. `sync-client.exe` is unsigned. What did you learn from that result, and what conclusions would go beyond the evidence?

#### Summary

Identity hashes answer **same file**. Similarity techniques help answer **which files deserve comparison**.

imphash describes PE import structure. ssdeep uses a higher-is-closer match score. TLSH uses a lower-is-closer difference score. None of them proves malware family or attribution on its own.

Code-signing information identifies the signing certificate and publisher claim and can support integrity checks. Signed does not automatically mean safe, and unsigned does not automatically mean malicious.

#### Related Reading

- [2.4.1 — Internal TIP](#241--internal-threat-intelligence-platform)
- [2.5.3 — RDAP / WHOIS](#253--rdap-and-whois-concepts)
- [1.2.7 — MD5 / SHA identity hashing](#127--files-engine)
- [2.4 — CTI Tools and Platforms](#24--cti-tools-and-platforms-introduction)
- [2.1.8 — Attribution](#218--attribution)

#### References and Further Reading

- [Mandiant, **Tracking Malware with Import Hashing**](https://cloud.google.com/blog/topics/threat-intelligence/tracking-malware-import-hashing) — explains imphash construction, uses, and limitations as a discovery and triage pivot.
- [ssdeep project documentation](https://ssdeep-project.github.io/ssdeep/usage.html) — explains fuzzy-hash comparison scores and how higher scores represent greater similarity.
- [Trend Micro, **TLSH**](https://github.com/trendmicro/tlsh) — documents TLSH as a fuzzy-matching technique and its lower-is-more-similar difference score.
- [Microsoft, **Authenticode Digital Signatures**](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode) — explains publisher identity and signed-code integrity.

### 2.5.3 — RDAP and WHOIS Concepts

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain what RDAP and legacy WHOIS registration data are used for and how the two access methods differ.
2. Query a domain or IP registration record, extract useful fields, and interpret those fields without turning registration data into unsupported attribution.

#### Key Concepts

Registration data helps an analyst answer questions such as:

- Which registrar maintains this domain?
- Which registry or Regional Internet Registry (RIR) is authoritative for the record?
- What nameservers are listed?
- When was the domain registered or last changed?
- Which organization is listed for an IP network?
- Which contact or entity information is publicly available?

Those facts are useful for enrichment, but registration data has an important limit: **it tells you what the registration system records about the name or network block. It does not, by itself, tell you who is operating malicious activity through that infrastructure.**

##### RDAP is the modern structured protocol

The **Registration Data Access Protocol (RDAP)** is the modern IETF-standard protocol for retrieving registration data. RDAP uses HTTP/HTTPS and structured JSON responses, which makes fields easier for software and analysts to interpret consistently.

For generic top-level domains (gTLDs), ICANN made RDAP the definitive source for registration data on **January 28, 2025**, replacing the contractual requirement for registrar and registry WHOIS services.

**WHOIS** is the older registration-data protocol defined around free-text responses over TCP port 43. WHOIS still exists in some registries, RIRs, tools, archives, and operational environments, so analysts should understand how to read it. But it should be treated as a **legacy access method**, not as the preferred modern standard.

| Feature | RDAP | Legacy WHOIS |
|---|---|---|
| Transport | HTTP / HTTPS | TCP port 43 |
| Response | Structured JSON | Primarily free text |
| Field consistency | Defined object structure | Varies by server and operator |
| Modern role | Preferred / standardized registration access | Legacy and environment-dependent |
| Useful to analysts | Easier parsing, links, notices, events, entities | Historical familiarity and fallback where still offered |

##### Registration roles are not interchangeable

Several names can appear in a registration record, and they describe different roles.

**Registry** — operates the authoritative database for a top-level domain or address-registration system.

**Registrar** — the company through which a domain registration is managed.

**Registrant / entity** — the person or organization associated with the registration when that information is available.

**RIR / network holder** — the organization to which an IP address range is registered or allocated.

These are not actor labels. A registrar can serve millions of unrelated customers. A cloud provider can hold the IP block used by many unrelated tenants.

##### Useful domain fields

For a domain, useful RDAP/WHOIS fields commonly include:

- **registrar**;
- **domain status**;
- **registration / creation date**;
- **last changed / updated date**;
- **expiration date**, when exposed;
- **nameservers**;
- **entities / contacts**, when public;
- **remarks and notices**, which may explain redaction or policy.

If contact information is redacted or unavailable, record that accurately. **Redacted registration data is not the same thing as an empty lookup.** Other fields may still provide useful context.

##### Useful IP-network fields

For an IP address, an RDAP lookup can lead to the registered network object. Useful fields may include:

- start and end address or CIDR/netblock;
- network handle or name;
- organization / entity;
- registration service;
- country or administrative metadata when present;
- remarks, notices, and abuse contacts.

If `203.0.113.88` falls inside a network registered to **Example Cloud**, the defensible statement is:

> The address is within a network registered to Example Cloud.

That is not the same as:

> Example Cloud conducted the activity.

Hosting and cloud providers routinely host unrelated customers.

##### Nameservers are useful context, not automatic clustering proof

Nameservers can be useful pivots, especially when they are unusual or appear alongside other shared infrastructure. But the evidentiary value depends on **distinctiveness**.

Two domains using the same large managed-DNS provider may tell you very little. Two domains sharing a rare nameserver pair, a rare address, similar registration timing, and other independent characteristics present a stronger case for further investigation.

Treat a shared nameserver as a **candidate pivot**, not a finished attribution.

##### Worked example: the A12 update domain

Suppose the RDAP record for the update domain shows:

- registrar: Example Registrar;
- nameservers: `ns1.cdn-test.net` and `ns2.cdn-test.net`;
- registration event: a recent creation date;
- registrant details: not publicly disclosed.

A useful enrichment line would be:

> RDAP lists Example Registrar and the nameservers `ns1.cdn-test.net` and `ns2.cdn-test.net`; registrant details are not publicly disclosed.

That statement preserves what the record actually says.

If another domain, `login-prd.net`, uses the same nameserver pair, that is a reason to examine the domain more closely. It is not enough by itself to call the domains the same infrastructure cluster or attribute them to the same actor.

##### Worked example: the A12 IP

Suppose an RDAP lookup for `203.0.113.88` returns a network object covering `203.0.113.0/24` and identifies **Example Cloud** as the network holder.

Useful enrichment:

> `203.0.113.88` is within `203.0.113.0/24`, a network registered to Example Cloud.

Evidence boundary:

> The registration establishes the network holder, not the operator of the specific malicious activity and not ownership of the entire block by the threat actor.

##### Paired platform application

Return to [platform selection](#242--selecting-platforms-for-cti-work). Use an approved registration service or the supplied registration record. Identify the entity role, relevant dates, and redacted or unavailable fields. Record one useful lead and one conclusion the registration data cannot support.

Keep the result with the enrichment record started in [2.5.1](#251--ioc-handling-and-enrichment-concepts).

#### Knowledge Check

1. Why is RDAP generally preferable to legacy WHOIS for modern registration-data access?
2. A domain's registrant information is redacted, but the registrar, nameservers, and registration events are present. What useful intelligence remains?
3. `203.0.113.88` belongs to a network registered to a cloud provider. What can you state from that record, and what would be unsupported attribution?

#### Summary

RDAP and WHOIS provide registration data, not actor identity. RDAP is the modern structured protocol; WHOIS is a legacy access method that may still appear in some environments.

Extract the fields that are actually present, preserve redaction as a fact, and distinguish registrar, registrant, and network holder from the operator of malicious activity. Registration data is most useful when it becomes one line of evidence in a larger enrichment or infrastructure analysis.

#### Related Reading

- [2.5.2 — Hashing and similarity concepts](#252--hashing-and-similarity-concepts)
- [2.5.4 — Advanced DNS](#254--advanced-dns-concepts)
- [0.7 — External tool survey](#07--external-tools)
- [2.1.8 — Attribution](#218--attribution)

#### References and Further Reading

- [ICANN — Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en) — explains the January 2025 gTLD transition to RDAP as the definitive registration-data source.
- [RFC 9082 — RDAP Query Format](https://www.rfc-editor.org/rfc/rfc9082.html) — defines RDAP query structure.
- [RFC 9083 — RDAP JSON Responses](https://www.rfc-editor.org/rfc/rfc9083.html) — defines the structured JSON response model.
- [RFC 3912 — WHOIS Protocol Specification](https://www.rfc-editor.org/rfc/rfc3912.html) — documents the legacy WHOIS protocol.

### 2.5.4 — Advanced DNS Concepts

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Interpret the key fields of an **SOA** record, especially MNAME, RNAME, and SERIAL.
2. Use authoritative DNS records such as NS, MX, TXT, and SRV to enrich a domain and identify **candidate pivots** without treating shared infrastructure as proof of common ownership or control.

#### Key Concepts

This lesson focuses on **authoritative DNS data**: records published for a DNS zone.

That is different from:
- a Zeek `dns` log showing that a host made a DNS query;
- passive DNS history showing how resolutions changed over time; or
- registration data from RDAP.

Authoritative DNS tells you what the zone currently publishes. Those records can expose infrastructure relationships worth investigating, but the strength of the relationship depends on how distinctive the shared record is.

##### SOA: the zone's authority record

The **Start of Authority (SOA)** record contains management parameters for a zone.

[RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html) defines several fields. This lesson focuses on three:

| Field | Meaning | Analytic use |
|---|---|---|
| **MNAME** | Domain name of the name server that is the original or primary source of data for the zone. | Identifies the server named as the zone's primary source in the SOA record. |
| **RNAME** | Domain-name encoding of the mailbox of the person responsible for the zone. | Provides an administrative/responsible mailbox value. |
| **SERIAL** | Unsigned 32-bit version number of the zone data. | Helps identify that the published zone version changed; it is not a file hash or guaranteed timestamp. |

The full SOA also contains REFRESH, RETRY, EXPIRE, and MINIMUM fields, which control aspects of zone transfer and caching behavior.

##### Reading RNAME correctly

RNAME is written in DNS-name form rather than ordinary email notation.

For a simple value such as:

`hostmaster.cdn-test.net.`

the conventional mailbox rendering is:

`hostmaster@cdn-test.net`

The conversion can involve escaped dots in more complicated local parts, so treat the field as a DNS-encoded mailbox rather than assuming every dot has the same meaning.

RNAME tells you the mailbox published in the SOA record. It does not prove that the mailbox owner is the malicious operator.

##### SERIAL is a version, not a clock

The SOA SERIAL is the zone's version number. Operators often choose serial formats that resemble dates, but DNS does not require the serial to be a timestamp.

A changed serial can support the statement:

> The zone version changed between the two observations.

It cannot automatically support:

> The domain was modified at exactly the date encoded in this number.

The serial is also not a cryptographic hash.

##### Other DNS records that support enrichment

| Record | What it represents | Potential intelligence value |
|---|---|---|
| **NS** | Authoritative name servers for a zone or delegation. | Candidate pivot to other names using the same distinctive DNS infrastructure. |
| **MX** | Mail exchanger for the domain. | Can expose related mail-host infrastructure. |
| **TXT** | Arbitrary published text. | Unique verification tokens or unusual strings may provide pivots; common SaaS tokens may be weak signals. |
| **SRV** | Location of a named service, including target host and port. | Can expose additional hostnames associated with a service. |
| **A / AAAA** | IPv4 / IPv6 address for a hostname. | Useful infrastructure context, but shared hosting can make the relationship weak. |
| **CNAME** | Alias pointing to a canonical name. | Can reveal hosting or service-provider relationships. |

NS, A/AAAA, and other record meanings are defined in the core DNS specifications, including [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) and [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html). SRV is defined in [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782.html).

##### Shared DNS records create candidates, not automatic siblings

Suppose the A12 update domain and `login-prd.net` share:

- `ns1.cdn-test.net`;
- `ns2.cdn-test.net`; and
- A record `203.0.113.88`.

That is useful. But the correct first conclusion is:

> `login-prd.net` is a candidate related domain because it shares multiple DNS infrastructure features with the update domain.

The strength of that relationship depends on context.

If the nameservers belong to a huge managed-DNS provider and the IP is shared hosting, the overlap may be weak. If the nameserver pair is rare, the address is unusual, registration timing is similar, and additional records also match, the case becomes stronger.

DNS pivots are most reliable when **multiple independent, distinctive features converge**.

##### Keep Infrastructure Claims at the Scope the DNS Evidence Supports

If two domains resolve to `203.0.113.88`, that supports a relationship involving that address at the observed time.

It does not establish that the threat actor controls all of `203.0.113.0/24`.

The previous RDAP lesson may tell you who the network is registered to. DNS tells you which address the name publishes or resolves to. Neither fact alone establishes ownership of the larger block by the actor.

##### A practical pivot workflow

Start with the A12 update domain.

1. **Read the SOA.** Record MNAME, RNAME, SERIAL, and any relevant timing fields.
2. **Collect useful records.** NS, A/AAAA, CNAME, MX, TXT, or SRV as appropriate.
3. **Normalize the values.** Compare hostnames, addresses, and tokens consistently.
4. **Identify candidate pivots.** Look for other names sharing distinctive values.
5. **Ask how common the feature is.** A public DNS provider is weaker than rare infrastructure.
6. **Corroborate.** Combine DNS with registration data, timing, internal telemetry, passive DNS, or other evidence before asserting shared control.

This workflow turns DNS into a disciplined source of hypotheses rather than a shortcut to ownership claims.

##### Paired platform application

Return to [Silent Push](#245--silent-push). Compare a supplied authoritative record with a passive-DNS result. Record the type, value, source, and query/observation time, then identify a candidate relationship whose time window is relevant.

Keep the result with the enrichment record started in [2.5.1](#251--ioc-handling-and-enrichment-concepts).

#### Knowledge Check

1. What do MNAME, RNAME, and SERIAL mean in an SOA record?
2. The SOA serial changes from one observation to the next. What can you safely infer, and what should you avoid assuming?
3. Two domains share the same NS pair and A address. What is a defensible first conclusion, and what additional questions determine whether the relationship is strong?

#### Summary

Authoritative DNS records describe the zone and the services it publishes.

SOA MNAME identifies the named primary source of zone data, RNAME encodes the responsible mailbox, and SERIAL is the zone version. NS, A/AAAA, CNAME, MX, TXT, and SRV records can expose useful infrastructure relationships.

Shared DNS values are **pivots**, not automatic proof of common ownership. Stronger infrastructure analysis comes from combining distinctive DNS overlaps with independent registration, timing, telemetry, or historical evidence.

#### Related Reading

- [2.5.3 — RDAP / WHOIS](#253--rdap-and-whois-concepts)
- [2.3.1 — ATT&CK for CTI](#231--mitre-attck-for-cti-analysis-and-reporting)
- [1.2.3 — Zeek DNS / DGA](#123--dns-engine)
- [0.7 — External tool survey / passive DNS](#07--external-tools)
- [2.5.5 — Infrastructure pivoting](#255--identifying-additional-adversary-infrastructure-from-seed-indicators)

#### References and Further Reading

- [RFC 1034 — Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html) — explains zones, authoritative servers, and NS/SOA roles.
- [RFC 1035 — Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html) — defines SOA fields and core DNS resource records.
- [RFC 2782 — A DNS RR for Specifying the Location of Services (SRV)](https://www.rfc-editor.org/rfc/rfc2782.html) — defines SRV records.

### 2.5.5 — Identifying Additional Adversary Infrastructure from Seed Indicators

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Pivot from a known seed to a **candidate** infrastructure object and write a concise hop sentence that preserves the shared evidence.
2. Judge whether the shared characteristic is distinctive enough to pursue and identify the source class that would support the next enrichment step.

#### Key Concepts

Infrastructure pivoting begins with a **seed**: a domain, IP address, certificate, hostname, or other infrastructure object already connected to the intelligence problem.

A pivot uses one characteristic of that seed to find another object worth investigating.

The key word is **candidate**. A shared nameserver, address, certificate field, or page characteristic can reveal potentially related infrastructure, but the pivot itself does not prove common ownership or adversary control.

##### The hop sentence

This course records one pivot with:

`seed | shared characteristic | candidate | why the relationship is worth pursuing`

Example:

> `update-domain | uncommon NS pair ns1/ns2.cdn-test.net | login-prd.net | same uncommon authoritative NS pair; corroborate with registration and DNS history`

This sentence captures the reasoning without requiring the DTF PTA/P identifiers taught in 2.5.6.

##### Distinctiveness matters

Not every shared value has the same evidentiary weight.

**Stronger candidate pivots** tend to involve characteristics that are:
- relatively uncommon;
- specific enough to identify a small set of infrastructure;
- observed close in time; or
- supported by more than one independent feature.

**Weaker pivots** often involve:
- large public DNS providers;
- CDN or shared-hosting addresses;
- broad cloud netblocks;
- common certificate issuers;
- generic HTTP titles.

The right question is not simply, “Do these objects share something?”

It is:

> **How surprising is it that unrelated infrastructure would share this characteristic?**

##### Common source classes

| Source class | Useful pivot information |
|---|---|
| **Registration / RDAP** | Registrar, registration events, nameservers, public entities |
| **Authoritative DNS** | NS, A/AAAA, CNAME, MX, TXT, SOA values |
| **Passive / historical DNS** | Other names associated with an address or changes over time |
| **TLS certificate data** | SAN names, subject, issuer, serial/fingerprint, validity |
| **HTTP / application data** | Titles, favicons, resources, headers, page fingerprints |

The detailed mechanics belong to the earlier or later tool lessons. Here, the analyst selects the source class that can test the pivot.

For registration context, see the [ICANN RDAP transition guidance](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en). For authoritative DNS semantics, see [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html).

##### Worked A12 example

Seed: A12 update domain  
Known address: `203.0.113.88`  
Known nameservers: `ns1.cdn-test.net`, `ns2.cdn-test.net`

Candidate: `login-prd.net`

If `login-prd.net` shares the same uncommon NS pair, that is a reasonable candidate hop.

If it also resolves to the same address during the relevant time window, the relationship becomes more interesting because two different features converge.

A defensible hop sentence is:

> `update-domain | uncommon NS pair + same observed A | login-prd.net | multiple shared infrastructure features; investigate further`

That is stronger than:

> `203.0.113.88 is inside 203.0.113.0/24, so the whole /24 is adversary infrastructure.`

The second statement expands one observation into ownership of a shared range without enough evidence.

##### One hop should lead to a testable next step

After writing the hop, identify what would strengthen or weaken it.

Examples:
- shared NS → search for other domains using that NS and compare registration timing;
- shared IP → check historical DNS and hosting density;
- shared certificate SAN → inspect whether the certificate is unique or mass-issued;
- shared HTTP title → determine whether the title is distinctive or generic.

The purpose of the pivot is not to collect an ever-growing graph. It is to generate a **defensible candidate relationship** that the next lookup can test.

##### Paired platform application

Return to [Silent Push](#245--silent-push) and [urlscan.io](#246--urlscanio). Use the retained DNS result and a supplied browser-scan result to propose one infrastructure hop. Separate page-controlled or distinctive features from common third-party services. Record the seed, shared characteristic, candidate, reason to pursue, and next lookup.

Keep the result with the enrichment record started in [2.5.1](#251--ioc-handling-and-enrichment-concepts).

#### Knowledge Check

1. What four parts belong in the course's hop sentence?
2. The update domain and `login-prd.net` share a large public DNS provider. Is that enough to call them related infrastructure? What would make the relationship stronger?
3. Why is “same `/24`” weaker than “same uncommon NS pair plus same observed A address” in the A12 example?

#### Summary

A pivot starts with a known seed and produces a candidate.

Record the seed, the shared characteristic, the candidate, and why the relationship deserves investigation. Weight the pivot by **distinctiveness**, and use the next lookup to test whether the relationship survives scrutiny.

#### References and Further Reading

- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework) – the formal pivot-ID framework taught in 2.5.6.
- [ICANN – Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en)
- [RFC 1035 – Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html)

### 2.5.6 — MalasadaTech Defender's ThreatMesh Framework (DTF)

**Estimated Time:** 25–30 minutes

#### Build on the previous pivot

Bring the hop record from [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators). Keep the existing evidence and distinctiveness assessment; this lesson adds a valid PTA/P-ID and uses that classification to select the next lookup. File-similarity and behavioral relationships remain separate from the infrastructure-focused DTF record.

#### Learning Objectives

1. Explain DTF's purpose and select a valid Pivot Tactic (PTA) and Pivot (P) from a known-bad infrastructure seed.
2. Use the pivot's shared characteristic to identify a candidate, assess whether the relationship is distinctive enough to pursue, and name the next enrichment step.
3. Explain how DTF complements ATT&CK, Diamond, and the Cyber Kill Chain.

#### Key Concepts

The **Defender's ThreatMesh Framework (DTF)** organizes ways defenders can pivot from known malicious infrastructure to discover additional candidate infrastructure.

The framework is inspired by ATT&CK's matrix structure, but its job is different: **DTF is about discovery pivots, not adversary behavior**.

References:
- [Defender's ThreatMesh Framework repository](https://github.com/MalasadaTech/defenders-threatmesh-framework)
- [Current DTF matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)

##### Pivot tactics and pivots

The current DTF matrix contains four Pivot Tactics:

| Pivot Tactic | Name | Examples of pivot families |
|---|---|---|
| **PTA0001** | Domain | Registration, domain characteristics, DNS |
| **PTA0002** | IP | Reverse lookup, proximity, AS |
| **PTA0003** | SSL | Issuer, SAN, certificate timing |
| **PTA0004** | Application | HTTP title, embedded code, resources |

Under each tactic are specific Pivot IDs.

Examples confirmed in the current matrix:

- **P0101.010 – Registration: Name Server**
- **P0103.003 – DNS: IP Address**
- **P0103.004 – DNS: SOA RName**
- **P0202 – Proximity**

Use the IDs that actually exist in the framework rather than inventing a code for an interesting idea.

##### Classify the existing A12 hops

Use the candidate relationships already evaluated in 2.5.5. Add the DTF classification without changing the strength of the evidence:

| Existing hop | DTF classification | What the classification adds |
|---|---|---|
| Update domain → shared `ns1.cdn-test.net` → `login-prd.net` | **PTA0001 / P0101.010 – Registration: Name Server** | Names the characteristic used to discover the candidate. |
| Update domain → shared `203.0.113.88` → candidate domain | **PTA0001 / P0103.003 – DNS: IP Address** | Names the DNS-address pivot so another analyst can reproduce it. |

A framework code labels the discovery method. It does not upgrade a candidate into confirmed adversary infrastructure. Carry forward the hosting context, timing, and corroboration assessment from the previous lesson.

##### Proximity is not automatically wrong

**P0202 – Proximity** is a valid DTF pivot.

The problem is not the pivot itself. The problem is using it without considering hosting context.

For example:

- checking nearby IPs around a known dedicated adversary server may be productive;
- declaring an entire busy cloud `/24` adversary-owned because one bad IP appears inside it is not supported.

So the classroom `/24` example is **rejected as a strong relationship**, not because P0202 is an invalid pivot, but because shared-cloud proximity is too weak in that scenario.

##### The pivot should name the next lookup

The selected pivot should lead naturally to a next enrichment action.

| DTF pivot | Useful next step |
|---|---|
| **P0101.010 – Name Server** | Search domain/passive-DNS data for other domains using the same NS; optionally enrich the NS's registrable domain with RDAP. |
| **P0103.003 – DNS: IP Address** | Search passive DNS or domain intelligence for other names associated with the address. |
| **P0103.004 – DNS: SOA RName** | Search for other zones publishing the same distinctive RNAME and compare additional DNS/registration features. |
| **P0202 – Proximity** | Examine nearby addresses only when network context makes adjacency meaningful. |

The DTF line records **why** you pivoted. The next lookup tests whether the candidate relationship survives further scrutiny.

##### DTF complements the other frameworks

| Framework | Primary question |
|---|---|
| **ATT&CK** | What adversary behavior is being performed? |
| **Diamond Model** | What are the Adversary, Capability, Infrastructure, and Victim relationships in this event? |
| **Cyber Kill Chain** | Where does supported activity sit in attack progression? |
| **DTF** | What infrastructure characteristic can we pivot on to discover additional candidates? |

They can all describe different aspects of the same investigation without replacing one another.

##### A concise DTF record

A practical format is:

`seed | PTA | P-ID | shared characteristic | candidate | why this is worth pursuing | next lookup`

Example:

`update-domain | PTA0001 | P0101.010 | ns1.cdn-test.net | login-prd.net | uncommon NS overlap | search other domains using NS`

That is enough for another analyst to understand and repeat the pivot.

#### Knowledge Check

1. The update domain and `login-prd.net` share `ns1.cdn-test.net`. Which DTF PTA/P-ID describes the pivot, and what determines whether the relationship is strong?
2. Two suspicious names resolve to the same `203.0.113.88`. Which DTF pivot applies, and what is a useful next lookup?
3. Why is rejecting the entire shared-cloud `/24` different from saying **P0202 Proximity** is an invalid pivot?

#### Summary

DTF gives defenders a repeatable vocabulary for infrastructure discovery.

Use a real PTA/P-ID, preserve the characteristic that produced the candidate, evaluate how distinctive that characteristic is, and name the next lookup that will test the relationship.

A pivot discovers **candidates**. Corroborating evidence turns candidates into defensible infrastructure relationships.

#### References and Further Reading

- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework)
- [DTF Matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md)

### 2.5.7 — Correlation, Link Analysis, and Campaign Tracking

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Combine enrichment records into evidence-backed links while testing alternative explanations.
2. Distinguish a candidate relationship, an activity-set or campaign assessment, and actor attribution.

#### Key Concepts

Enrichment produces individual observations and candidate relationships. Correlation asks whether those findings form a coherent pattern; link analysis records the relationships and the evidence behind them. Campaign tracking adds a time-bounded assessment of related activity.

Bring forward the records from file, registration, DNS, infrastructure-pivoting, and DTF lessons. Keep each original source and observation time visible as you combine them.

##### A link is a claim about a relationship

Useful evidence may include a distinctive infrastructure characteristic, matching malware configuration, certificate fingerprint, co-occurrence in an incident, or a repeated temporal pattern. A shared vendor tracking name is source context; it is not, by itself, technical evidence connecting two objects.

Record each proposed link as:

`object A | relationship | object B | source and observation time | supporting evidence | alternative explanation | assessment / next check`

Two tools repeating the same upstream report do not necessarily provide two independent confirmations. Check provenance before counting corroboration.

##### Combine evidence at the strength it supports

For A12, the update domain and `login-prd.net` share an uncommon nameserver and an IP during an overlapping period. This supports a candidate infrastructure relationship. The shared fields should be evaluated together with hosting context and any independent registration, certificate, or behavioral evidence.

A busy shared cloud range remains a weak link. Similar files can support a separate file-family hypothesis, but similarity alone does not establish common infrastructure control. Record file and behavioral relationships alongside infrastructure relationships without forcing them into DTF, which remains infrastructure-focused.

| Evidence state | Defensible record |
|---|---|
| One shared field with unresolved common-provider explanation | Candidate link requiring further evaluation. |
| Several distinctive, time-relevant findings with documented sources | A stronger assessed relationship, with remaining limitations stated. |
| Evidence of coordinated activity against a common objective over time | A campaign hypothesis with its scope, basis, confidence, and competing explanations. |

The third conclusion requires activity evidence. A graph of related domains alone does not establish the campaign's objective or responsible actor.

##### Maintain the assessment as evidence changes

Keep the activity-set or campaign label separate from actor attribution. Record what the label covers, the time window, supporting and contradicting evidence, and why the assessment changed. Revisit stale indicators through the lifecycle decisions in [2.5.1](#251--ioc-handling-and-enrichment-concepts).

When a relationship no longer holds, update the assessment without erasing the historical observation. Use [2.1.8 – Attribution](#218--attribution) when evaluating a claim of actor identity, and carry the supported findings into the organizational assessment in 2.6.

#### Knowledge Check

1. Two reports repeat the same upstream nameserver finding. Do they provide two independent confirmations?
2. The A12 domains share a rare NS and time-overlapping IP. What can you record, and what would justify a stronger campaign claim?
3. A similar file and a domain share a vendor actor label. Is that sufficient to link them to the same actor?

#### Summary

Promote relationships only as far as the evidence supports. Keep candidate links, campaign assessments, and actor attribution distinct.

#### References and Further Reading

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### 2.5 – Technical Enrichment and Discovery: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Seed → enrich → pivot → test distinctiveness/context → corroborate → relationship → broader correlation when supported**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- manage indicators and enrichment results with provenance and lifecycle context;
- use file, registration, DNS, and infrastructure evidence to generate defensible pivots;
- distinguish candidate relationships from corroborated relationships and broader campaign judgments;
- apply DTF to justified infrastructure relationships while keeping other pivot types separate.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **2.5.1 – IOC Handling and Enrichment Concepts** | Track indicators, provenance, confidence, scope, and lifecycle decisions during enrichment. |
| **2.5.2 – Hashing and Similarity Concepts** | Use exact hashes and similarity relationships to connect or differentiate files without overstating equivalence. |
| **2.5.3 – RDAP and WHOIS Concepts** | Use registration and allocation data as infrastructure context with appropriate ownership limits. |
| **2.5.4 – Advanced DNS Concepts** | Use DNS records and historical patterns to understand infrastructure relationships and changes. |
| **2.5.5 – Identifying Additional Adversary Infrastructure from Seed Indicators** | Pivot from a seed through distinctive shared characteristics and evaluate candidate infrastructure. |
| **2.5.6 – MalasadaTech Defender's ThreatMesh Framework (DTF)** | Organize justified infrastructure pivots without mixing them with unrelated file or behavior relationships. |
| **2.5.7 – Correlation, Link Analysis, and Campaign Tracking** | Correlate multiple supported relationships while keeping candidate links, activity sets, campaigns, and attribution distinct. |

#### Check Your Understanding

Ask yourself:

1. What information should travel with a pivot so another analyst can review why it was made?
2. Why can two domains sharing an IP be a useful lead without proving common control?
3. What additional evidence would you want before promoting several candidate links into a broader activity-set or campaign assessment?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **2.6 – Threat Assessment and Organizational Significance: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 2.6 – Threat Assessment and Organizational Significance: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

External intelligence becomes operationally useful when the analyst explains what applies to the organization and why it matters. This requires separating what an adversary is reported to do from whether the organization is exposed, visible, relevant, or likely to experience meaningful impact.

#### Connect to What You Already Know

Technical enrichment established evidence and relationships. This subunit turns that material toward the organization by extracting applicable behavior and evaluating its significance.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **2.6.1 – Extracting Applicable TTPs from Intelligence Reports** | Identify reported behaviors that plausibly apply to the organization and preserve the source evidence for each TTP. |
| **2.6.2 – Threat Relevance and Organizational Impact** | Assess why the threat matters to the organization, including exposure, relevance, potential impact, and important visibility limits. |

#### What to Watch For

- Keep **applicability**, **visibility**, **relevance**, and **impact** as separate analytical questions.
- Tie applicable TTPs to actual reporting rather than to a framework label alone.
- Explain organizational significance in terms of assets, exposure, mission, decisions, and consequences that the available evidence supports.

#### Expected End State

By the end of this subunit, you should be able to:

- extract TTPs from reporting and explain why they may apply to the organization;
- separate applicability from whether the organization can observe the behavior;
- assess relevance and potential impact without turning possibility into certainty;
- state the organizational significance in a form that supports a decision or next action.

#### How to Preview This Subunit

Read this introduction, then skim the [2.6 Summary](#26--threat-assessment-and-organizational-significance-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 2.6.1 — Extracting Applicable TTPs from Intelligence Reports

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Extract concrete adversary behaviors from an intelligence report rather than copying an IOC list or unsupported ATT&CK table.
2. Evaluate whether each behavior is **applicable to the environment**, then assess **visibility separately** so a telemetry gap is not mistaken for non-applicability.

#### Key Concepts

A report may contain dozens of ATT&CK IDs, indicators, malware names, and narrative claims. The analyst's job is to extract the behaviors that matter to the local environment.

A **TTP** describes how an adversary operates. A hash, IP address, or domain is an observable/indicator, not a TTP.

ATT&CK is the reference vocabulary for the behaviors in this lesson:
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)

##### Start with the behavior, not the printed ID

A report line such as:

> The malware launched encoded PowerShell with `-enc`.

contains a concrete procedure.

If the report also labels it **T1059.001**, the analyst can verify that mapping against ATT&CK. If the vendor's ID is missing or questionable, the mapping exercise belongs to 2.3.1.

This lesson asks a different question:

> **Does this behavior apply to our environment?**

##### Applicability and visibility are separate filters

This course treats them as two distinct questions.

###### Applicability

A behavior is applicable when the environment contains the systems, services, access paths, or conditions needed for the behavior to occur.

Useful checks include:

- **Platform:** Do we run the affected operating system, application, identity system, cloud service, or device type?
- **Exposure / path:** Can the behavior reach or execute against something we actually operate?
- **Preconditions:** Are the required features or configuration present?

###### Visibility

If the behavior is applicable, ask whether current telemetry can observe it.

Visibility can be:

- **Visible** – existing telemetry can support hunting/detection.
- **Partially visible** – some evidence exists but important fields are missing.
- **Not currently visible** – the behavior can happen here, but the required telemetry is absent.

A visibility gap does **not** make the TTP non-applicable.

It means:

> applicable behavior + collection/telemetry gap

That distinction prevents the organization from ignoring a real exposure merely because current tools cannot see it.

##### Classroom environment

DYA is a law firm with Windows workstations. `WS-JLEE` is a Windows user workstation.

Example:

**Report behavior:** encoded PowerShell / T1059.001  
**Applicability:** yes — Windows workstations are present.  
**Visibility:** assess separately based on available process/script/PowerShell telemetry.

MITRE lists PowerShell as a Windows technique under Execution. See [T1059.001](https://attack.mitre.org/techniques/T1059/001/).

Example:

**Report behavior:** destructive action against an OT historian appliance  
**Applicability:** no, if DYA does not operate OT historian systems.  
**Visibility:** not evaluated because the required platform is absent.

##### A simple extraction table

| Report behavior | ATT&CK reference | Applicable? | Why? | Visibility |
|---|---|---|---|---|
| Encoded PowerShell | T1059.001 | Yes | Windows endpoints present | Visible / partial / gap |
| OT historian wipe | Report-specific | No | No OT historian environment | N/A |
| ESXi-only behavior | Relevant ATT&CK technique | No if no ESXi | Required platform absent | N/A |

This keeps three decisions separate:
1. What behavior did the report describe?
2. Can it occur here?
3. Can we currently observe it?

##### Validate Vendor ATT&CK Mappings Against the Reported Behavior

A vendor's technique list can be useful, but the local extract should remain tied to the report's actual procedures.

If the report lists an ID with no described behavior, mark it for validation rather than treating it as a finished local TTP extract.

The most useful output is a short set of behaviors with clear applicability and visibility status—not the longest possible ATT&CK list.

#### Knowledge Check

1. Why are applicability and visibility separate questions?
2. Encoded PowerShell appears in a report. DYA runs Windows, but current telemetry cannot capture PowerShell command lines. Is the TTP applicable? What else should be recorded?
3. A report describes an ESXi-only technique, and DYA has no ESXi systems. How should it be handled?

#### Summary

Extract behaviors from the report first.

Then ask **applicability**: can this behavior occur in the environment?

Only after that ask **visibility**: can current telemetry observe it?

A visibility gap is not the same thing as non-applicability. Keep the distinction visible so collection gaps can be addressed instead of silently removing relevant behavior from the intelligence package.

#### References and Further Reading

- [MITRE ATT&CK](https://attack.mitre.org/)
- [MITRE ATT&CK Enterprise Matrix](https://attack.mitre.org/matrices/enterprise/)
- [T1059.001 – PowerShell](https://attack.mitre.org/techniques/T1059/001/)

### 2.6.2 — Threat Relevance and Organizational Impact

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Assess whether a threat finding is relevant to the organization's mission, assets, technologies, and exposure.
2. Describe the plausible organizational consequence if the finding is true while keeping evidence, uncertainty, and decision context visible.

#### Key Concepts

Intelligence becomes useful to an organization when the analyst explains **why the finding matters here**.

A technically interesting threat can still have low local relevance if the organization does not use the affected platform, expose the vulnerable service, operate the targeted mission, or possess the asset type in question.

This lesson separates two questions:

##### Relevance

> **Does this finding meaningfully intersect our environment or mission?**

Useful relevance checks include:

- **Mission:** Does the threat affect something important to what the organization does?
- **Assets / identities:** Do we have the kinds of users, systems, data, applications, or services involved?
- **Platform / technology:** Do we run the affected technology?
- **Exposure / path:** Is there a realistic way the behavior or infrastructure could reach us?
- **Observed evidence:** Have we already seen related activity internally?

##### Impact

> **If this finding is true here, what could change for the organization?**

Impact should describe a plausible consequence tied to the finding.

Examples:
- compromised user workstation;
- credential exposure;
- interruption of a business service;
- loss of sensitive client data;
- additional IR workload;
- need to isolate or patch an exposed system.

The impact statement should not become a dramatic worst-case story unless the evidence supports that escalation.

##### Relevance, applicability, visibility, and impact are different

These concepts sit near one another, but they answer different questions.

| Concept | Question |
|---|---|
| **TTP applicability (2.6.1)** | Can this behavior occur in our environment? |
| **Visibility** | Can our current telemetry observe the applicable behavior? |
| **Threat relevance** | Does the finding intersect our mission, assets, technology, or exposure in a meaningful way? |
| **Impact** | What plausible organizational consequence follows if the finding is true here? |

A finding can be technically applicable but low relevance to the current requirement.

A finding can also be highly relevant while visibility is poor.

##### Worked A12 example

Finding:

- encoded PowerShell on `WS-JLEE`;
- request to the update domain;
- Windows user workstation in DYA.

**Relevance:**

> The finding is relevant because DYA operates Windows user workstations and the behavior was observed on `WS-JLEE`.

**Impact:**

> If the update-domain activity represents payload delivery, the affected user workstation may require containment and further examination to determine whether a payload was successfully transferred or executed.

Notice what the impact statement does **not** claim:
- that payload execution is already proven;
- that the entire organization is compromised;
- that a nation-state conducted the activity.

The impact remains proportional to the evidence.

##### Example of low relevance

A report describes wiping an industrial-control historian.

If DYA does not operate that technology, the finding may be:

> **Low / not currently relevant to this environment** because the required OT historian platform is absent.

That conclusion can change if the environment changes or if the report contains another behavior that does apply.

##### Relevance should be requirement-aware

A finding can be relevant to the environment but still outside the immediate intelligence requirement.

For example, `login-prd.net` may be a useful infrastructure lead while the current requirement asks only whether the update domain delivered `update.exe` during A12.

The analyst can preserve the lead without allowing it to derail the current answer.

That is how relevance supports prioritization without erasing useful intelligence.

#### Knowledge Check

1. What is the difference between TTP applicability and threat relevance?
2. A behavior is applicable to Windows, but current telemetry cannot see it. Does that make the threat irrelevant? Why or why not?
3. For A12, write one relevance sentence and one impact sentence that stay within the evidence.

#### Summary

Relevance answers **does this matter here?**

Impact answers **what plausible consequence follows if it is true here?**

Keep those judgments tied to mission, assets, technology, exposure, and observed evidence. Preserve uncertainty rather than turning a relevant finding into a larger crisis than the evidence supports.

### 2.6 – Threat Assessment and Organizational Significance: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Reported behavior → applicability → visibility/exposure → relevance → potential impact → decision support**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- extract TTPs from reporting and explain why they may apply to the organization;
- separate applicability from whether the organization can observe the behavior;
- assess relevance and potential impact without turning possibility into certainty;
- state the organizational significance in a form that supports a decision or next action.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **2.6.1 – Extracting Applicable TTPs from Intelligence Reports** | Identify reported behaviors that plausibly apply to the organization and preserve the source evidence for each TTP. |
| **2.6.2 – Threat Relevance and Organizational Impact** | Assess why the threat matters to the organization, including exposure, relevance, potential impact, and important visibility limits. |

#### Check Your Understanding

Ask yourself:

1. Why can a TTP be applicable even when current telemetry cannot observe it?
2. What is the difference between a threat being relevant and a specific impact being certain to occur?
3. What organizational context makes a technical TTP assessment more useful to a decision maker?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **2.7 – Intelligence Production and Dissemination: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 2.7 – Intelligence Production and Dissemination: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Analysis becomes an intelligence product when the supported judgment is represented clearly, answers the requirement, and reaches the audience that can use it. Structured formats such as STIX can help represent objects and relationships, but they do not replace the analytical judgment.

#### Connect to What You Already Know

The earlier CTI subunits established requirements, tradecraft, evidence, enrichment, and organizational significance. This subunit turns that work into structured and finished products, closes RFIs, and delivers the result.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **2.7.1 – Core STIX Objects** | Recognize the main STIX objects used to represent indicators, malware, infrastructure, relationships, and other intelligence concepts. |
| **2.7.2 – STIX in Intelligence Production** | Use STIX objects and relationships to represent supported intelligence without treating the schema as proof. |
| **2.7.3 – Creating Finished Intelligence Products** | Build a product around the requirement, evidence, judgment, uncertainty, and customer decision. |
| **2.7.4 – RFI Responses and Closure** | Answer the bounded RFI, document gaps or caveats, and close the request appropriately. |
| **2.7.5 – Disseminating Intelligence to the Correct Audiences** | Deliver the product to the audiences and channels appropriate to the decision and sensitivity. |

#### What to Watch For

- Keep **representation** separate from **judgment**: STIX describes supported objects and relationships; the analyst still explains what they mean.
- Use the original requirement as the test for whether the product is complete enough to answer the question.
- Tailor detail and dissemination to the audience while preserving the same underlying evidence and caveats.

#### Expected End State

By the end of this subunit, you should be able to:

- represent core intelligence objects and relationships using STIX concepts;
- create a finished product that connects evidence, judgment, uncertainty, and the customer requirement;
- respond to and close an RFI with a bounded answer and documented gaps;
- disseminate the product to the correct audiences through appropriate channels.

#### How to Preview This Subunit

Read this introduction, then skim the [2.7 Summary](#27--intelligence-production-and-dissemination-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 2.7.1 — Core STIX Objects

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Recognize the **eleven STIX 2.1 object types selected for this course** and explain what each represents.
2. Given a line from a report, choose the most appropriate course object type and explain the evidence boundary behind that choice.

#### Key Concepts

**STIX**—Structured Threat Information Expression—is a standardized language for representing cyber threat and observable information.

This course uses **STIX 2.1**, the current OASIS standard used by the curriculum.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

STIX contains more object types than this lesson teaches. The eleven below are a **course-selected working set**, chosen because they appear repeatedly in CTI production and the later training modules.

##### The course's eleven object types

| Object | What it represents |
|---|---|
| **Indicator** | A pattern that can detect suspicious or malicious activity. |
| **Observed Data** | A record that cyber-observable data was seen during a time window. |
| **Malware** | Malicious code, whether represented as a family or an instance. |
| **Attack Pattern** | A type of adversary behavior, technique, or method. |
| **Threat Actor** | An individual, group, or organization believed to operate with malicious intent. |
| **Intrusion Set** | A grouped set of adversarial behaviors/resources believed to share common properties and often a common operator. |
| **Campaign** | A set of malicious activities occurring over a period of time against targets. |
| **Course of Action** | An action intended to prevent, mitigate, or respond to malicious activity. |
| **Identity** | A person, organization, group, system, or other entity identity. |
| **Relationship** | A typed relationship connecting STIX objects. |
| **Sighting** | An assertion that a STIX Domain Object was seen. |

Other valid STIX 2.1 types include Infrastructure, Tool, Vulnerability, Report, Note, Grouping, Location, Incident, Malware Analysis, and others. Their absence from this course list does **not** mean they are invalid STIX objects.

##### Indicator is not the same as a raw observable

A common beginner mistake is to treat every hash, IP address, or domain as an **Indicator**.

STIX separates the concepts more carefully.

An **Indicator** contains a detection pattern.

Example:

`[file:hashes.'SHA-256' = 'abc123...']`

That pattern can be used to look for matching activity.

A raw file, IP address, domain, process, or registry key is represented with a **STIX Cyber-observable Object (SCO)** such as File, IPv4 Address, Domain Name, Process, or Windows Registry Key.

An **Observed Data** object can then record that one or more of those SCOs were observed during a particular time window.

So:

- **File SCO:** the file/hash value itself.
- **Observed Data:** records that the file was observed.
- **Indicator:** a pattern used to detect activity matching that file/hash.

Reference: [STIX 2.1 – Observed Data and Cyber-observable Objects](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

##### Sighting is another distinct concept

A **Sighting** states that a STIX Domain Object was seen.

For example, an organization may record that an Indicator was sighted in its environment.

STIX can also attach:
- **Observed Data** describing what was actually seen;
- an **Identity or Location** describing where/who saw it.

This makes Sighting different from both Observed Data and a generic Relationship.

##### Identity does not mean “the attacker”

Identity is a neutral entity object.

It can represent:
- an organization;
- a person;
- a group;
- a system;
- a class of entities.

For example:

- **DYA** → Identity (organization)
- **WS-JLEE** → could be modeled as an Identity with `identity_class: system` when the production design needs a system identity

Neither is automatically a Threat Actor.

Likewise, a vendor tracking name such as **PRD APT** should not automatically become a Threat Actor object merely because the report contains a name. The analyst should first determine what the source actually claims and what object type the evidence supports.

##### Threat Actor and Intrusion Set are not interchangeable

**Threat Actor** focuses on the malicious actor entity.

**Intrusion Set** focuses on a set of adversarial behaviors/resources believed to share common properties and often a common operator.

Many intelligence providers use tracking labels before real-world identity is established. Depending on the underlying evidence and modeling approach, an Intrusion Set may be more appropriate than claiming a known Threat Actor.

The lesson does not force either object when the evidence is insufficient.

##### Attack Pattern represents behavior

MITRE ATT&CK techniques can be represented as **Attack Pattern** objects in STIX.

Example:

> Encoded PowerShell / T1059.001 → Attack Pattern

That object represents the behavior—not the process event, hash, or victim.

##### Relationship and Sighting are STIX Relationship Objects

Most of the course list above are **STIX Domain Objects (SDOs)**.

**Relationship** and **Sighting** are **STIX Relationship Objects (SROs)**.

This distinction matters because Sighting has its own specific fields, including `sighting_of_ref`; it is not simply a Relationship with a verb such as `sighting-of`.

#### Knowledge Check

1. Are the eleven objects in this lesson the only valid object types in STIX 2.1? Explain.
2. A report records that a file with a particular SHA256 was seen on a host. How are the raw file, the observation, and a detection pattern conceptually different in STIX?
3. Why should a vendor tracking name not automatically become a Threat Actor object?

#### Summary

STIX 2.1 gives analysts a structured vocabulary for threat and observable information.

The eleven types in this module are a **course subset**, not the entire STIX object model.

Keep these three distinctions especially clear:

- observable data is not automatically an Indicator;
- Sighting is not generic Relationship;
- Identity or a vendor label is not automatically Threat Actor.

#### References and Further Reading

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
- [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)

### 2.7.2 — How STIX Objects Are Used in Intelligence Production

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Build a small STIX-aligned graph using valid relationship types and Sightings to express a threat scenario.
2. Recognize the key required fields needed for common STIX 2.1 objects used in the classroom example.
3. Explain how TAXII 2.1 Collections exchange STIX objects and distinguish a **STIX Bundle** from a **TAXII Envelope**.

#### Key Concepts

STIX becomes useful when separate facts are structured and connected so people and tools can interpret the same threat model consistently.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

##### Relationships give the graph meaning

A STIX **Relationship** object connects a source object to a target object with a `relationship_type`.

Common specification-defined relationships used in this course include:

| Source | Relationship | Target example |
|---|---|---|
| Indicator | **indicates** | Malware or Attack Pattern |
| Indicator | **based-on** | Observed Data |
| Malware | **uses** | Attack Pattern |
| Threat Actor / Intrusion Set / Campaign | **uses** | Malware or Attack Pattern |
| Threat Actor / Intrusion Set / Campaign | **targets** | Identity |
| Course of Action | **mitigates** | Attack Pattern, Indicator, Malware, Tool, Vulnerability |

STIX also permits `related-to` and can permit custom relationships. For this course, use a specification-defined relationship when one clearly fits. A vague or custom verb should not be used to hide uncertainty.

##### Sighting is not a Relationship verb

**Sighting** is its own STIX Relationship Object.

It uses:
- `sighting_of_ref` → the STIX Domain Object that was sighted;
- optional `observed_data_refs` → raw observation context;
- optional `where_sighted_refs` → Identity or Location describing who/where saw it.

Reference: [STIX 2.1 – Sighting](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

This means a host sighting should not be modeled as:

`relationship_type: sighting-of`

That is not the STIX 2.1 Sighting model.

##### Build the A12 graph with defensible semantics

Assume the classroom scenario has:

- an Indicator pattern for the SHA256 of `invoice.vbs`;
- Malware object for the malicious `invoice.vbs` sample/family if the analysis supports modeling it as Malware;
- Attack Pattern for **T1059.001 PowerShell**;
- Identity for **DYA**;
- optionally an Identity representing **WS-JLEE** as a system;
- Observed Data describing the file/process observation.

A defensible graph might include:

1. **Indicator → indicates → Malware**
2. **Malware → uses → Attack Pattern T1059.001**
3. **Indicator → based-on → Observed Data**
4. **Sighting** of the Indicator, with Observed Data attached and DYA or WS-JLEE represented through `where_sighted_refs` when that modeling decision is appropriate

This is more precise than claiming:

> The invoice hash indicates PowerShell because PowerShell happened somewhere in the same incident.

STIX permits Indicator → indicates → Attack Pattern, but the analyst should still ensure the detection pattern genuinely detects evidence of that Attack Pattern. Relationship validity in the schema does not automatically make the analytic claim sound.

##### Required fields depend on object type

Most STIX Domain Objects and STIX Relationship Objects use common required fields such as:

- `type`
- `spec_version`
- `id`
- `created`
- `modified`

But each object can have additional required properties.

Examples:

**Indicator** requires, among other properties:
- `pattern`
- `pattern_type`
- `valid_from`

**Relationship** requires:
- `relationship_type`
- `source_ref`
- `target_ref`

**Sighting** requires:
- `sighting_of_ref`

**Observed Data** requires observation fields such as:
- `first_observed`
- `last_observed`
- `number_observed`
- `object_refs` in the STIX 2.1 model

Validation therefore means more than checking that every object has the five common fields.

Reference: [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)

##### A Bundle is a container—not a relationship

A **STIX Bundle** is a transient container holding arbitrary STIX Objects.

The specification explicitly states that objects are **not considered related merely because they appear in the same Bundle**.

Reference: [STIX 2.1 – Bundle Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

A Bundle can be convenient for packaging objects in a file or message, but the semantic links still come from Relationship, Sighting, embedded references, and the objects themselves.

##### TAXII is the exchange protocol

**TAXII 2.1** is an application-layer protocol for exchanging cyber threat intelligence over HTTPS.

Reference: [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)

A **Collection** is a logical repository of CTI objects exposed by a TAXII server.

A TAXII client can:
- GET objects from a Collection;
- POST objects to a writable Collection.

##### TAXII Envelopes and STIX Bundles Serve Different Purposes

TAXII and STIX define different layers of the exchange, so their container concepts should remain distinct.

TAXII 2.1 uses a **TAXII Envelope** as the transport wrapper when STIX objects are exchanged through Collection endpoints. A **STIX Bundle** is a separate STIX container that can group STIX objects independently of TAXII.

This means a STIX Bundle can be used outside TAXII, while a TAXII exchange does not require every set of objects to be represented as a STIX Bundle.

A useful mental model is:

- **STIX objects** → the intelligence content
- **STIX Relationship/Sighting** → the semantic connections
- **STIX Bundle** → optional transient STIX container
- **TAXII Collection** → logical exchange repository
- **TAXII Envelope** → transport wrapper used by TAXII endpoints

##### Classroom TAXII exercise

The classroom collection name `dya-cti` is fictional.

The skill is to explain:

> A TAXII client with read access could retrieve STIX objects from the `dya-cti` Collection.

and, if write permission existed:

> A client could add valid STIX objects to the Collection.

The lesson does not require standing up a server.

#### Knowledge Check

1. Why does putting two STIX objects in the same Bundle not establish that they are related?
2. Which required Indicator field is missing from the old shortcut list of `type`, `spec_version`, `id`, `created`, and `modified`?
3. Explain the difference among a STIX Bundle, a TAXII Collection, and a TAXII Envelope.

#### Summary

STIX production is graph construction, not merely JSON packaging.

Use precise relationships, model Sightings with the Sighting object, validate the required fields for each object type, and remember that Bundle membership does not create semantic relationships.

TAXII 2.1 provides the exchange mechanism. Collections hold/expose CTI, and TAXII Envelopes wrap STIX objects in Collection exchanges.

#### References and Further Reading

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
- [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)
- [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)

### 2.7.3 — Creating Finished Intelligence Products

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Draft a short finished intelligence product that answers a requirement and evaluate it against clear analytic standards.
2. Produce a concise actor or activity profile that distinguishes what is known, what is assessed, and what remains unresolved.

#### Key Concepts

A **finished intelligence product** is the usable result of analysis: it answers a defined question with evidence-based judgments and enough context for the intended customer to understand what matters.

A list of indicators, a TIP export, or a STIX bundle may support the product, but none is automatically a finished analytic product.

##### Product type follows the question

Common classroom product types include:

| Product | Best fit |
|---|---|
| **Assessment** | A judged answer to a specific intelligence question. |
| **Activity / actor profile** | A structured description of a tracked cluster or actor, including behavior, infrastructure, targeting, confidence, and gaps. |
| **RFI response** | A bounded answer to a Request for Information. Intake and priority are taught in 2.1.5; response and closure are taught in 2.7.4. |

The product should match the requirement rather than trying to combine every format into one document.

##### A compact finished-product structure

A short CTI product should normally make these elements easy to find:

1. **Requirement / question** – What are we answering?
2. **Key judgment** – What do we assess?
3. **Evidence / source basis** – What observations and reporting support the judgment?
4. **Uncertainty / confidence** – How strong is the evidence and what remains unknown?
5. **Relevance / implications** – Why does this matter to the customer or decision?

That structure is a classroom implementation of broader analytic-tradecraft principles rather than a claim that every organization must use these exact headings.

##### Quality is more than formatting

ODNI's **ICD 203 – Analytic Standards** provides a useful reference for evaluating analytic products. Among other tradecraft expectations, it emphasizes:

- describing source quality and credibility;
- explaining uncertainty;
- distinguishing underlying information from assumptions and judgments;
- considering alternatives when relevant;
- demonstrating customer relevance and implications;
- using clear and logical reasoning.

References:
- [ODNI – ICD 203, Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
- [ODNI – Objectivity and Analytic Standards](https://www.dni.gov/index.php/how-we-work/objectivity)

This course applies those ideas to CTI without pretending the classroom format is an official IC template.

##### Facts and judgments should remain distinguishable

A useful product makes it possible for the reader to see what was **observed** and what the analyst **assesses**.

For A12:

**Observed**
- `WS-JLEE` requested `/update.exe` from the update domain during suspicious activity.
- Encoded PowerShell occurred on the workstation.

**Judgment**
> We assess that the update domain was **likely** used for attempted payload delivery in A12.

**Uncertainty**
> Available evidence does not establish that `/update.exe` was successfully downloaded or executed.

That is stronger tradecraft than writing:

> The domain was the payload host.

because the latter removes an important evidence boundary.

##### The “so what” should be proportional

The product should explain why the judgment matters without escalating beyond the evidence.

For A12:

> The domain should remain in scope for the A12 investigation and retrospective review because the workstation requested a payload-like path from it during the suspicious activity.

That tells the consumer why the judgment matters without claiming enterprise-wide compromise or actor identity.

##### Activity profile before actor identity

A profile does not require a real-world nation-state attribution.

When identity is unresolved, profile the **activity cluster** you can support.

A concise A12 profile could contain:

- **Tracking scope:** A12-associated activity cluster
- **Observed behavior:** encoded PowerShell; request for `/update.exe`
- **Infrastructure:** update domain / `203.0.113.88`; distinctive DNS characteristics where supported
- **Victim:** `WS-JLEE` / DYA
- **Assessment:** likely attempted payload delivery
- **Attribution:** unresolved
- **Gaps:** successful download/execution not established

If a vendor calls similar activity “PRD APT,” preserve that as source-attributed context rather than silently changing “Attribution: unresolved” into a country or government actor.

##### Evaluate the draft against the question

A useful review asks:

- Does the product actually answer the requirement?
- Can the reader distinguish evidence from judgment?
- Is uncertainty explicit?
- Are major claims traceable to source/evidence?
- Are alternatives or important gaps acknowledged?
- Is the relevance or implication clear?
- Is attribution no stronger than the evidence?

A polished document that fails those questions is still analytically weak.

#### Demonstration Exercise — Non-A12 Threat Actor Profile

This exercise is **not part of A12**. It uses a separate training-only evidence set so you can practice the approved threat-actor-profile task without inventing attribution for the recurring case.

##### Training evidence set: SILVER KITE

You are supporting a fictional regional manufacturer. Four independent reports over six months describe the same tracked actor, **SILVER KITE**, with the following corroborated characteristics:

- repeatedly targets aerospace and advanced-manufacturing organizations in the United States and Japan;
- obtains initial access through spearphishing attachments and exploitation of externally exposed VPN appliances;
- uses PowerShell for discovery and staging, then deploys a custom backdoor consistently identified in the supplied reporting as **KiteDoor**;
- creates scheduled tasks for persistence and commonly archives collected engineering documents before exfiltration;
- uses short-lived VPS infrastructure registered through multiple providers;
- has targeted organizations for technical drawings, proprietary manufacturing data, and program documentation;
- two high-confidence sources attribute the activity to the same named actor, while **no supplied evidence supports a government sponsor, nationality, or legal identity**.

##### Required output

Produce a concise threat actor profile that includes:

1. **Tracking identity and scope** — what SILVER KITE represents and the reporting period.
2. **Targeting** — sectors/regions and the information apparently sought.
3. **Observed behavior** — the major access, execution, persistence, collection, and exfiltration behaviors supported by the evidence.
4. **Infrastructure/tooling** — what is known and what remains too weak to claim.
5. **Key judgments and confidence** — at least one analytic judgment with its evidence basis.
6. **Attribution boundary and gaps** — explicitly state what the supplied evidence does **not** establish.

Then evaluate your draft against the finished-product standards taught above: requirement fit, evidence-versus-judgment separation, uncertainty, traceability, relevance, and bounded attribution.

**Demonstration note:** producing the profile demonstrates task `2.7.3.2`. When you draft it as a finished product and evaluate it against the standards above, the same event can also produce evidence for `2.7.3.1`. The evaluator records each task separately under the qualification/sign-off standard; lesson completion alone is not automatic sign-off.

#### Knowledge Check

1. Why is a TIP export or IOC list not automatically a finished intelligence product?
2. Name four elements that should be easy to find in a short finished product.
3. Write a three-line A12 activity profile that keeps attribution unresolved and preserves the download/execution evidence gap.

#### Summary

A finished intelligence product is a judged answer to a requirement, not a data dump.

Make the question, judgment, source basis, uncertainty, and relevance easy to see. Evaluate the product for analytic quality as well as presentation quality.

When actor identity is unresolved, profile the activity cluster you can defend rather than inventing attribution.

#### References and Further Reading

- [ODNI – ICD 203, Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
- [ODNI – Objectivity and Analytic Standards](https://www.dni.gov/index.php/how-we-work/objectivity)

### 2.7.4 — RFI Responses and Closure

**Estimated Time:** 15–20 minutes

#### Learning Objectives

1. Write a direct RFI response that separates the supported answer from unresolved evidence gaps.
2. Check the response against the original requirement and record closure or agreed follow-up.

#### Key Concepts

Return to the intake record from [2.1.5](#215--rfi-intake-and-prioritization). Check whether the question, deadline, or handling constraints changed during the work. If they did, clarify and record the change with the requester.

The assessment in 2.6 now supports a direct answer. A response can be brief when the question is narrow; it does not need to become a full actor profile.

Answer the question that was asked.

A useful response normally includes:

- direct answer / key judgment;
- evidence basis;
- uncertainty or limitation;
- relevant next implication or unresolved requirement.

Do not make the recipient search through a long actor history to find a two-sentence answer.

##### Complete the A12 RFI

**Question:**
> Was the update domain the host that successfully delivered the payload in A12?

**Evidence available:**
- `WS-JLEE` requested `/update.exe` from the update domain during suspicious activity.
- The update domain resolves to the infrastructure already associated with the case.
- Available evidence does not establish successful download or execution of `/update.exe`.

**Response:**
> We assess the update domain was **likely used for attempted payload delivery** in A12. `WS-JLEE` requested `/update.exe` from that destination during the suspicious activity, but available evidence does not establish that the file was successfully downloaded or executed.

That response answers the question while preserving the evidence boundary.

##### When the RFI cannot be fully answered

A useful partial response can say:

> Current evidence is insufficient to determine whether the payload was successfully delivered. Confirmation would require response/file-transfer evidence or a resulting file/artifact on the host.

That is better than filling the gap with confidence language unsupported by the evidence.

##### Close the loop

An RFI is complete when the requestor receives:
- the answer available now;
- the uncertainty/gaps;
- any agreed follow-up.

If a new question emerges, record it as a new/follow-on requirement rather than silently expanding the original RFI forever.

Confirm the response uses the approved audience and channel in [2.7.5](#275--disseminating-intelligence-to-the-correct-audiences), and archive the answer and agreed follow-up through the local process in [2.8.2](#282--local-production-and-approval-processes).

#### Knowledge Check

1. Write a two-sentence A12 response that distinguishes attempted payload delivery from successful delivery.
2. What should a useful response contain when evidence cannot fully answer the question?
3. How should you handle a new question that arises when the requester receives the answer?

#### Summary

Answer the original question as far as the evidence allows. Preserve uncertainty and record closure or the next agreed requirement.

### 2.7.5 — Disseminating Intelligence to the Correct Audiences

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Select the audience, approved dissemination method, and appropriate sharing designation/instructions for a finished product.
2. Tailor the level of detail for technical and leadership audiences without changing the underlying judgment.
3. Explain why TLP markings and organizational channel/handling rules are related but separate controls.

#### Key Concepts

Dissemination is the step where a finished product reaches the people who need it through a method the organization authorizes.

Three decisions should remain separate:

1. **Audience** – Who needs the information for a decision or action?
2. **Channel / method** – Which approved system or workflow should carry it?
3. **Sharing / handling rules** – Who may receive or redistribute it?

The correct audience on an unapproved channel is still poor dissemination.

##### TLP is a sharing protocol, not a classification system

The **Traffic Light Protocol (TLP) 2.0** provides standardized markings for how cybersecurity information may be shared.

Reference:
- [FIRST – Traffic Light Protocol](https://www.first.org/tlp/)
- [FIRST – TLP 2.0 Definitions and Usage Guidance](https://www.first.org/tlp/docs/tlp-a4.pdf)

TLP does **not** replace:
- classification markings;
- legal restrictions;
- contractual controls;
- privacy rules;
- organizational data-handling policy.

Use the actual local marking/handling scheme when one exists.

##### Correct TLP 2.0 meanings

| Marking | Sharing boundary |
|---|---|
| **TLP:RED** | Individual recipients only; no further disclosure. |
| **TLP:AMBER+STRICT** | Need-to-know sharing **within the recipient's organization only**. |
| **TLP:AMBER** | Need-to-know sharing within the recipient's organization **and its clients**. |
| **TLP:GREEN** | Sharing within the defined community; not public channels. |
| **TLP:CLEAR** | May be shared without TLP restriction, subject to applicable rules/procedures and copyright. |

The old classroom shorthand “TLP:AMBER = organization only” is incorrect under TLP 2.0. Organization-only sharing is **TLP:AMBER+STRICT**.

FIRST also permits accompanying instructions when the originator needs to clarify or further constrain sharing.

Reference: [FIRST – TLP Use Cases](https://www.first.org/tlp/use-cases)

##### Classroom handling card

For the A12 exercise, assume:

- technical incident details are **TLP:AMBER+STRICT**;
- the organization requires the product to travel through either the approved incident-management system or approved CTI channel;
- personal SMS, unapproved personal chat, and public posting are not approved dissemination methods.

These are **classroom workflow assumptions**, not live DYA or user-organization policy.

##### Tailoring changes detail, not truth

The technical and leadership versions can contain different levels of detail while preserving the same key judgment and uncertainty.

**Technical / IR version**
- `WS-JLEE`
- `/update.exe`
- update domain / IP
- relevant timestamps
- evidence caveat
- next investigative need

**Leadership version**
> We assess a suspicious external domain was likely used for attempted payload delivery to a user workstation. IR has the affected host in scope; available evidence does not yet establish successful payload execution.

The leadership version removes unnecessary technical detail without changing:
- **likely**
- **attempted payload delivery**
- the unresolved execution gap

##### Minimize sensitive detail when the audience does not need it

Tailoring is not only about readability.

It can also reduce unnecessary exposure of:
- hostnames;
- usernames;
- hashes;
- internal paths;
- client identifiers;
- investigative methods.

Only include detail the audience needs for its decision.

##### Additional sharing instructions

A TLP marking may be accompanied by specific instructions when appropriate and authorized.

Example:

> TLP:AMBER+STRICT — Do not redistribute outside the incident-response and CTI teams without originator approval.

Local policy still governs whether and how such instructions are used.

#### Knowledge Check

1. Under TLP 2.0, which marking restricts sharing to the recipient's organization only?
2. Why are TLP marking and approved dissemination channel separate decisions?
3. Give one detail that belongs in the IR version of A12 but can be omitted from a leadership awareness version without changing the judgment.

#### Summary

Good dissemination aligns **audience, approved channel, and sharing rules**.

TLP 2.0 controls information-sharing boundaries; it is not a substitute for classification, privacy, legal, contractual, or organizational handling requirements.

Tailor detail for the audience, but preserve the judgment and uncertainty.

#### References and Further Reading

- [FIRST – Traffic Light Protocol](https://www.first.org/tlp/)
- [FIRST – TLP 2.0 Definitions and Usage Guidance](https://www.first.org/tlp/docs/tlp-a4.pdf)
- [FIRST – TLP Use Cases](https://www.first.org/tlp/use-cases)

### 2.7 – Intelligence Production and Dissemination: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Supported evidence/judgment → structured representation where useful → finished answer → RFI closure → dissemination**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- represent core intelligence objects and relationships using STIX concepts;
- create a finished product that connects evidence, judgment, uncertainty, and the customer requirement;
- respond to and close an RFI with a bounded answer and documented gaps;
- disseminate the product to the correct audiences through appropriate channels.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **2.7.1 – Core STIX Objects** | Recognize the main STIX objects used to represent indicators, malware, infrastructure, relationships, and other intelligence concepts. |
| **2.7.2 – STIX in Intelligence Production** | Use STIX objects and relationships to represent supported intelligence without treating the schema as proof. |
| **2.7.3 – Creating Finished Intelligence Products** | Build a product around the requirement, evidence, judgment, uncertainty, and customer decision. |
| **2.7.4 – RFI Responses and Closure** | Answer the bounded RFI, document gaps or caveats, and close the request appropriately. |
| **2.7.5 – Disseminating Intelligence to the Correct Audiences** | Deliver the product to the audiences and channels appropriate to the decision and sensitivity. |

#### Teaching / Workflow Note

STIX remains a two-lesson sequence inside this subunit before the course moves into finished products, RFI closure, and dissemination.

#### Check Your Understanding

Ask yourself:

1. Why does encoding a relationship in STIX not prove that the relationship is analytically correct?
2. What should determine whether an RFI response is complete enough to close?
3. How can you tailor a product for different audiences without changing the underlying judgment?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **2.8 – Local Application: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 2.8 – Local Application: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Good CTI tradecraft still has to operate inside a real organization. Local priorities, approval processes, repositories, customer lists, and dissemination channels determine how the generic workflow is actually executed.

#### Connect to What You Already Know

The preceding CTI subunits developed the full analytical workflow. This final subunit asks the learner to map that workflow to the documents, authorities, and channels used in the local environment.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **2.8.1 – Local Intelligence Requirements and Priorities** | Identify the organization’s actual intelligence priorities and the documents or authorities that define them. |
| **2.8.2 – Local Production and Approval Processes** | Identify where products are created, reviewed, approved, stored, and versioned locally. |
| **2.8.3 – Local Dissemination Channels and Customers** | Identify local customers, channels, handling expectations, and feedback paths. |

#### What to Watch For

- Use actual local documents and procedures where available rather than inventing a generic policy.
- Distinguish course examples from authoritative local requirements.
- Map each generic CTI step to the real owner, system, approval point, and customer used by the organization.

#### Expected End State

By the end of this subunit, you should be able to:

- locate or identify the organization’s intelligence requirements and priorities;
- describe the local production, review, approval, and storage path;
- identify the correct local customers and dissemination channels;
- recognize which parts of the CTI workflow are universal tradecraft and which are site-specific implementation.

#### How to Preview This Subunit

Read this introduction, then skim the [2.8 Summary](#28--local-application-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 2.8.1 — Local Intelligence Requirements and Priorities

**Estimated Time:** 15–20 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Locate and verify the shop's **current intelligence requirements and priorities** using the authoritative local source.
2. Align analytic work to a stated local requirement and clearly identify when the current priority list has not yet been obtained.

#### Key Concepts

Earlier modules taught how intelligence requirements work. This module asks a different question:

> **What priorities are actually in force in this organization today?**

That answer cannot come from a generic textbook or this classroom scenario. It must come from the shop's own authoritative source.

A new analyst should learn three things early:

1. **Where the current priority list lives**
2. **Who owns or maintains it**
3. **How to tell that the copy is current**

The source might be a formal requirements document, a team workspace, a program plan, a briefing deck, or another locally approved system. The specific source is site-dependent.

##### Current means current

Requirements and priorities change.

A copy from last quarter may still be useful background, but it should not automatically be treated as the list governing today's work.

Before aligning analysis to a requirement, verify:
- the effective date or version;
- whether the list has been superseded;
- the owning role or authority;
- whether the requirement is active, standing, deferred, or retired, if the local process uses those states.

##### PIRs are one kind of local priority structure

Some organizations use **Priority Intelligence Requirements (PIRs)**. Others may use:
- intelligence requirements;
- standing requirements;
- leadership priorities;
- mission priorities;
- collection or analytic priorities.

The important point is not the label. The analyst needs the **authoritative list that governs local work**.

Module 2.1.4 taught what a PIR and intelligence requirement are. This module teaches how to orient yourself to the local implementation.

##### Align work only when the connection is explicit

Suppose A12 is an active incident involving a Windows workstation.

That makes A12 operationally important, but it does not automatically make A12 a PIR.

To say that A12 analysis supports a local requirement, you should be able to point to the actual requirement.

Example:

> **Local requirement:** Assess malicious use of scripting interpreters on enterprise Windows endpoints.  
> **A12 alignment:** The incident includes encoded PowerShell on `WS-JLEE`, so the analysis directly supports this requirement.

Without the local requirement list, the correct status is:

> **Current priority alignment not yet verified.**

That statement is more useful than assigning an invented PIR number because it tells the team exactly what onboarding information is still missing.

##### Record the source of the priority

When practical, preserve:
- requirement or priority title/ID;
- authoritative source;
- version/effective date;
- owner;
- how the current analytic task supports it.

This makes later review easier when priorities change.

##### A practical onboarding note

A new analyst could maintain a small orientation entry:

| Item | Local answer |
|---|---|
| Authoritative priority source | ______ |
| Owner / maintainer | ______ |
| Current version / effective date | ______ |
| Review cadence | ______ |
| How work is mapped to a requirement | ______ |

The blanks are intentional. They are filled from the real shop, not from classroom fiction.

#### Knowledge Check

1. Why is an old priority list not automatically sufficient for current alignment?
2. A12 is an active incident, but you have not seen the current requirement list. What should you record about priority alignment?
3. What information should you capture about the authoritative local priority source?

#### Summary

Site-specific priority work begins by locating the authoritative local source and confirming that it is current.

Then map analytic work to the stated requirement it actually supports.

When that source has not yet been obtained, record the gap clearly instead of filling it with a classroom assumption.

#### Related Reading

- [2.1.5 – RFI Intake and Prioritization](#215--rfi-intake-and-prioritization)
- [2.7.4 – RFI Responses and Closure](#274--rfi-responses-and-closure)
- [2.1.4 — Intelligence requirements](#214--intelligence-requirements)
- [2.1.9 — Collection planning](#219--collection-sources-and-methods)
- [2.8.2 — Local production and approval](#282--local-production-and-approval-processes)

### 2.8.2 — Local Production and Approval Processes

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Locate and explain the shop's local workflow for collection requests, product review, approval, release, and archival.
2. Follow the known process for a product or collection request and clearly identify any workflow element that has not yet been obtained.

#### Key Concepts

A finished analytic draft is not automatically an official product.

Organizations normally have local steps that determine:
- how additional collection is requested;
- who reviews a product;
- who can approve or release it;
- how changes are resolved;
- where the official version is recorded and retained.

The names of those steps, tools, and roles are local.

This module teaches how to **orient yourself to that process**.

##### Build a local workflow map

A useful orientation map answers:

| Workflow question | Local answer |
|---|---|
| How is a collection request submitted? | ______ |
| Who receives / triages it? | ______ |
| Who reviews analytic products? | ______ |
| What review standards/checklist are used? | ______ |
| Who is authorized to approve/release? | ______ |
| Where is the authoritative copy stored? | ______ |
| How are revisions/version history recorded? | ______ |
| What metadata must be preserved? | ______ |

The blanks are completed from the real shop process.

##### Collection planning and collection requesting are different

Module 2.1.9 taught collection planning:
- what information is needed;
- which source class may provide it;
- what scope is appropriate.

This module addresses the **local mechanism used to request or coordinate that collection**.

Example:

> **Analytic need:** determine whether `/update.exe` was successfully transferred.  
> **Collection requirement:** obtain response/file-transfer or host-artifact evidence.  
> **Local request path:** use the shop's approved collection-request workflow.

The first two can be reasoned about generically. The last one must be learned locally.

##### Review is not the same as approval

A reviewer may:
- check sourcing;
- challenge reasoning;
- check analytic standards;
- verify handling/markings;
- edit for clarity.

An approval authority is the role empowered by local policy to release or make the product official.

Some shops combine those roles; others separate them.

The analyst should learn the actual local arrangement rather than assume one universal model.

##### Archive the authoritative version

The official product should be stored according to local standards.

Useful questions include:
- Which repository is authoritative?
- Is the draft also retained?
- How are revisions numbered?
- Are source notes stored with the product or separately?
- What handling/retention rules apply?
- How is superseded content identified?

This matters because future analysts need to know which version was actually released.

##### When the local process is not yet known

Use explicit onboarding status:

> **Local production/approval path not yet verified.**

Then identify the missing element:

> Need current review/approval workflow and authoritative archive location from the team lead/process owner.

That is more useful than inventing a Jira queue, ticket name, or folder because the statement tells the team exactly what the analyst still needs to learn.

##### A12 walkthrough

Suppose the A12 assessment is drafted.

Before release, the analyst should be able to answer:

1. Who reviews this kind of product?
2. Which standard/checklist applies?
3. Who approves/releases it?
4. Which channel/repository receives the official copy?
5. How is the final version recorded?

If those answers are not known, the product may be analytically complete while the **production workflow is not yet complete**.

#### Knowledge Check

1. What is the difference between collection planning and the local collection-request process?
2. Why should review authority and approval authority be learned separately?
3. You have a finished A12 draft but do not know the official archive location. What should you record?

#### Summary

Local production is an orientation-and-follow-through skill.

Learn the collection-request path, review process, approval authority, release step, versioning, and authoritative archive.

When part of the workflow has not yet been obtained, identify that gap precisely so it can be closed.

#### Reference Model

This module intentionally relies on the organization's **local production, approval, records, and collection-request procedures** as the source of truth.

### 2.8.3 — Local Dissemination Channels and Customers

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Locate the authoritative local customer/channel map and identify the primary internal and external consumers the CTI function actually supports.
2. Select the correct local dissemination path for a product, or clearly identify that the required customer/channel mapping has not yet been obtained.

#### Key Concepts

Module 2.7.5 taught the general dissemination problem:

- Who needs the product?
- Which approved channel should carry it?
- What sharing/handling restrictions apply?

This module asks for the **local answers**.

Every CTI team has an operating context:
- internal customers;
- possibly external customers or partners;
- approved systems/channels;
- recurring products;
- escalation or urgent-notification paths;
- restrictions on what can be shared with each audience.

A new analyst should learn that map early.

##### Customer means an established intelligence consumer

A customer is not simply anyone who might find the information interesting.

The local customer map should tell you which roles, teams, leaders, partner organizations, or other authorized recipients the CTI function is expected to support.

Examples of categories that may exist locally:
- SOC;
- incident response;
- threat hunting;
- detection engineering;
- vulnerability management;
- leadership;
- mission/business units;
- external partners.

These are examples only. The actual list must come from the local organization.

##### Map product → customer → channel

A useful orientation table looks like:

| Product / use | Primary customer | Approved channel | Handling notes |
|---|---|---|---|
| Urgent incident intelligence | ______ | ______ | ______ |
| Routine CTI assessment | ______ | ______ | ______ |
| Leadership awareness | ______ | ______ | ______ |
| Hunt-support package | ______ | ______ | ______ |
| External partner share | ______ | ______ | ______ |

The blanks are filled from the site's authoritative customer/channel guidance.

##### Channel is more than convenience

A channel may be approved because it provides:
- access control;
- auditability;
- retention;
- classification/handling support;
- ticket linkage;
- version control;
- notification to the right group.

That is why “the right person” does not automatically make an unofficial personal channel acceptable.

##### External sharing needs explicit authorization

If the organization supports external customers or partners, learn:
- who they are;
- what products may be shared;
- which channel is approved;
- what marking/handling rules apply;
- whether additional approval is required.

Do not assume an external partner from familiarity or prior collaboration.

##### A12 Case Study: Worked Example

Suppose the A12 assessment is approved and ready for dissemination.

Before sending, the analyst should identify from the local map:

1. Which internal customer owns the immediate operational decision?
2. Is there a separate leadership customer?
3. What approved channel is used for each?
4. What handling/sharing instructions apply?
5. Does any external party receive the product?

If the local customer/channel map has not been provided, record:

> **Local dissemination path not yet verified.**

Then identify the missing source/owner rather than selecting a convenient recipient from the classroom scenario.

##### Keep 2.7.5 and 2.8.3 connected

**2.7.5** taught the general dissemination method and TLP concepts.

**2.8.3** supplies the organization-specific customer names, channels, and routing rules.

The general model helps you ask the right questions. The local map provides the actual answer.

#### Knowledge Check

1. Why is “someone who might like the report” not enough to make them a CTI customer?
2. What four fields belong in a useful local product/customer/channel map?
3. The A12 product is approved, but you have never been shown the customer/channel map. What should you record?

#### Summary

Local dissemination requires an authoritative map of **who the CTI function serves and how each product is sent**.

Learn the customer, channel, and handling path for the products you produce.

When the map is missing, record that onboarding gap explicitly instead of substituting a convenient recipient or personal channel.

This completes the **2.8 Local Application subunit**.

#### Reference Model

This module intentionally relies on the organization's **local customer, dissemination, handling, and partner-sharing guidance** as the source of truth.

### 2.8 – Local Application: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Generic CTI tradecraft → local priorities → local production/approval → local dissemination → feedback**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- locate or identify the organization’s intelligence requirements and priorities;
- describe the local production, review, approval, and storage path;
- identify the correct local customers and dissemination channels;
- recognize which parts of the CTI workflow are universal tradecraft and which are site-specific implementation.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **2.8.1 – Local Intelligence Requirements and Priorities** | Identify the organization’s actual intelligence priorities and the documents or authorities that define them. |
| **2.8.2 – Local Production and Approval Processes** | Identify where products are created, reviewed, approved, stored, and versioned locally. |
| **2.8.3 – Local Dissemination Channels and Customers** | Identify local customers, channels, handling expectations, and feedback paths. |

#### Teaching / Workflow Note

Use actual local documents and procedures for the site-specific walkthrough; course examples are not authoritative local policy.

#### Check Your Understanding

Ask yourself:

1. Which local document tells you what intelligence questions or priorities matter most?
2. Where does your organization require a product to be reviewed or approved before dissemination?
3. Why should a training example never be treated as proof of a local ticket, channel, or approval requirement?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **2.9 – Cyber Threat Intelligence Section Summary**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 2.9 — Cyber Threat Intelligence Section Summary

**Estimated Time:** 15–20 minutes  

#### Purpose

Module 2.0 introduced the CTI workflow:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

Module 2.9 closes that loop.

By this point, you have learned how to define intelligence requirements, evaluate evidence, use structured tradecraft, select platforms, enrich technical objects, test relationships, assess local significance, produce intelligence, answer RFIs, and disseminate the result.

This summary reconnects those skills into one requirement-to-answer workflow.

#### What You Can Now Do

You should now be able to:

- distinguish data, information, and intelligence;
- identify the customer, requirement, and decision context;
- intake and prioritize an RFI;
- choose collection sources based on the question;
- preserve provenance and distinguish independent reporting from repeated upstream claims;
- use estimative language and structured techniques without hiding uncertainty;
- evaluate source reliability and information credibility;
- recognize and mitigate common analytic biases;
- use ATT&CK, Diamond, and Kill Chain to organize evidence appropriately;
- select CTI platforms based on the lookup required;
- manage observables/IOCs through retain, enrich, review/expire, or reject decisions;
- perform file, RDAP/WHOIS, DNS, and infrastructure enrichment;
- keep DTF infrastructure pivots separate from file and behavioral relationships;
- correlate evidence while testing alternative explanations;
- distinguish a candidate relationship, campaign/activity-set assessment, and actor attribution;
- assess applicability, visibility, relevance, and impact separately;
- represent intelligence in STIX when useful;
- produce a finished intelligence answer;
- close an RFI or document follow-up;
- disseminate through the correct audience and local process.

The important skill is not producing more enrichment.

It is producing a supported answer.

#### The 2.x Block at a Glance

| Unit | Core skill retained |
|---|---|
| **2.1 – Foundations and Requirements** | Define the question, customer, collection need, and desired intelligence outcome. |
| **2.2 – Analytical Tradecraft** | Make disciplined judgments from incomplete or conflicting evidence. |
| **2.3 – Frameworks** | Organize adversary behavior, relationships, and intrusion progression without manufacturing missing facts. |
| **2.4 – Tools and Platforms** | Select the right source for the question and preserve the result as an evidence record. |
| **2.5 – Enrichment and Discovery** | Test technical relationships and combine evidence into stronger or weaker links. |
| **2.6 – Assessment** | Determine what applies, what is visible, why the finding matters locally, and plausible impact. |
| **2.7 – Production and Dissemination** | Turn analysis into structured and finished products that answer the requirement. |
| **2.8 – Local Application** | Follow the organization's real requirements, approval process, customers, and dissemination channels. |

#### A12 End to End

A12 can demonstrate the entire CTI workflow.

##### Step 1 – Intake the requirement

SOC asks:

> **What is known about the update domain, and does available evidence support that it delivered `update.exe` during A12?**

Capture:
- customer;
- question;
- priority;
- existing evidence;
- desired answer;
- deadline/follow-up expectations.

##### Step 2 – Separate data, information, and intelligence

Examples:

**Data**  
> DNS response, hash, IP, sandbox process event.

**Information**  
> The domain resolved to an IP during the incident window.

**Intelligence**  
> An assessed answer explaining what the relationship means for A12 and how strongly the evidence supports it.

##### Step 3 – Apply tradecraft

Evaluate:
- source provenance;
- reliability;
- credibility;
- uncertainty;
- alternative explanations;
- possible bias.

Do not treat two reports repeating the same upstream source as independent corroboration.

##### Step 4 – Organize with frameworks

Use:
- ATT&CK to organize behavior;
- Diamond Model to organize adversary/capability/infrastructure/victim relationships;
- Kill Chain to reason about intrusion progression.

Frameworks help structure analysis.

They do not fill evidence gaps.

##### Step 5 – Select the source

Choose platforms based on the unresolved question.

For example:
- internal TIP for prior local/contextual knowledge;
- VirusTotal for file relations/behavior/context;
- ANY.RUN for sandbox execution evidence;
- Silent Push for passive-DNS/infrastructure context;
- urlscan.io for observed web behavior.

Record:
- object;
- source;
- time;
- result;
- limitation.

##### Step 6 – Enrich and pivot

Use the appropriate method:

- IOC lifecycle;
- file similarity;
- registration/RDAP;
- advanced DNS;
- infrastructure pivoting;
- DTF identifiers for infrastructure relationships;
- correlation/link analysis.

Preserve file and behavioral pivots as their own evidence rather than forcing them into an infrastructure-only framework.

##### Step 7 – Correlate

Suppose the update domain and another domain share:

- an uncommon nameserver;
- a time-overlapping IP;
- additional supporting context.

Record a candidate relationship first.

A stronger campaign/activity-set claim requires stronger, time-relevant activity evidence.

Actor attribution requires still more.

##### Step 8 – Assess organizational significance

For each relevant behavior/finding, separate:

**Applicability**  
> Can it occur here?

**Visibility**  
> Can we observe it?

**Relevance**  
> Does it intersect our mission/assets/technology/exposure?

**Impact**  
> What plausible consequence follows if true here?

This converts technical findings into organizational intelligence.

##### Step 9 – Produce the answer

A strong RFI response might say:

> Available evidence supports the assessment that the update domain was used for attempted payload delivery in A12. `WS-JLEE` requested `/update.exe` from that destination during the suspicious activity, but current evidence does not establish successful transfer or execution of the file.

The answer:
- addresses the question;
- identifies what is supported;
- preserves the unresolved gap.

##### Step 10 – Disseminate and close

Deliver through the approved audience/channel.

Then record:
- requirement answered;
- confidence/limitations;
- follow-up agreed;
- new requirement if needed.

#### Concepts to Keep Separate During CTI Analysis

The CTI workflow contains several closely related concepts. The distinctions below matter because each one changes what the analyst is justified in claiming or doing next.

##### Data, information, and intelligence build on one another

**Data** are recorded observations or values. **Information** adds context that explains how those observations relate. **Intelligence** adds an assessed answer to a relevant question or requirement.

The transition is not created by renaming the artifact. It comes from adding context, analysis, and decision relevance.

##### The requirement directs collection

The requirement defines the question and the decision the work is meant to support. Collection obtains the evidence needed to answer it.

Starting with the requirement helps the analyst choose sources deliberately instead of allowing an interesting tool result to redefine the task.

##### Source reliability and information credibility are separate judgments

A source with a strong historical record can still provide a weak or poorly supported claim. An unfamiliar source can still provide information that is technically verifiable.

Evaluate the source and the specific information independently, then explain how those judgments affect the assessment.

##### Platform output becomes intelligence through analysis

A sandbox event, passive-DNS record, detection count, TIP relationship, or web scan is evidence with provenance. Its significance depends on the question, surrounding evidence, and interpretation.

The analyst's job is to explain what the platform result supports and where its limitations begin.

##### An observable becomes an operational IOC through context and purpose

A hash, IP, domain, URL, or filename is first a technical observable. Promoting it into an IOC requires enough suspicious or malicious context, provenance, specificity, validity, and operational purpose to justify using it defensively.

This is also why lifecycle decisions such as retain, enrich, review/expire, and reject are evidence-dependent.

##### A pivot candidate needs corroboration before it becomes a supported relationship

A shared nameserver, address, certificate field, or page characteristic can justify another lookup. The initial overlap is a reason to investigate, not proof of common control or malicious purpose.

Use distinctiveness, time relevance, hosting context, and independent evidence to decide whether the relationship strengthens.

##### Candidate relationships, campaign assessments, and attribution require progressively stronger evidence

A candidate link can be recorded early. A campaign or activity-set assessment requires a coherent pattern of related activity. Attribution adds the still stronger judgment about who is responsible.

Keeping those levels separate allows the analysis to mature without promoting a tentative relationship beyond the evidence.

##### DTF is used for infrastructure relationships

The Defender's ThreatMesh Framework organizes justified infrastructure pivots. File similarity and behavioral relationships remain useful evidence, but they should be recorded alongside the infrastructure analysis rather than forced into an infrastructure-only model.

##### Applicability, visibility, relevance, and impact answer different organizational questions

**Applicability** asks whether the behavior can occur in the environment.

**Visibility** asks whether current telemetry can observe it.

**Relevance** asks whether the finding materially intersects the organization's mission, assets, technology, or exposure.

**Impact** asks what plausible organizational consequence follows if the finding is true here.

Because these questions are different, they can legitimately produce different answers.

##### STIX represents intelligence; the representation does not establish the claim

STIX provides a structured way to describe objects and relationships. The represented assertion still needs evidence, provenance, and appropriate confidence.

A well-formed STIX relationship is useful for exchange and reuse, but formatting cannot substitute for analysis.

##### Enrichment supports the finished answer

A large set of lookups, pivots, and graphs may be valuable working material. The finished intelligence product selects the evidence that answers the requirement and explains its significance.

The goal is not to show every action the analyst performed; it is to deliver a supported answer.

##### RFI intake and RFI response are different stages of the same requirement

Module 2.1.5 captures, clarifies, prioritizes, and assigns the question. Module 2.7.4 returns to that requirement with the supported answer, uncertainty, and closure or agreed follow-up.

Keeping both stages visible makes it possible to judge whether the analysis actually answered what the requester needed.

#### Integrated Review Exercise

Use this **hypothetical CTI practice card built from the A12 case**. The supplied enrichment and visibility details are exercise conditions rather than additional canonical A12 facts:

> **Requirement:** Determine what role the update domain played and whether available evidence establishes successful payload delivery.  
> **Case evidence:** encoded PowerShell on `WS-JLEE`; HTTP request for `/update.exe` to the update domain  
> **Enrichment:** `login-prd.net` shares an uncommon nameserver pair and an overlapping observed IP with the update domain  
> **Environment:** Windows workstations are present; process visibility is partial on one endpoint population  
> **Evidence gap:** successful transfer or execution of `update.exe` is not established

Write a short intelligence answer using:

##### Requirement
What question are you answering?

##### Evidence
Which observations materially support the answer?

##### Relationship assessment
What can you say about the infrastructure relationship?

##### Applicability / visibility
Which behavior applies, and what can or cannot be seen?

##### Relevance / impact
Why does the finding matter locally?

##### Judgment
What does the evidence support?

##### Gap
What remains unresolved?

##### Closure / follow-up
Is the RFI answered, or is a new requirement needed?

A strong answer should not let the amount of enrichment exceed the strength of the evidence.

#### CTI Readiness Checklist

Before moving into 3.x, you should be comfortable saying:

- [ ] I can distinguish data, information, and intelligence.
- [ ] I can define the customer and intelligence requirement before collecting.
- [ ] I can intake and prioritize an RFI.
- [ ] I can preserve provenance and evaluate source/reporting quality.
- [ ] I can use estimative language without hiding uncertainty.
- [ ] I can test alternative explanations and recognize bias.
- [ ] I can use ATT&CK, Diamond, and Kill Chain for their appropriate purposes.
- [ ] I can choose a CTI platform based on the question.
- [ ] I can record platform results with time/source/limitations.
- [ ] I can manage observable/IOC lifecycle decisions.
- [ ] I can perform file, registration, DNS, and infrastructure enrichment.
- [ ] I can keep file/behavioral and infrastructure pivots conceptually separate.
- [ ] I can distinguish a candidate link, stronger activity-set/campaign assessment, and attribution.
- [ ] I can separate applicability, visibility, relevance, and impact.
- [ ] I can produce an evidence-based answer rather than an enrichment dump.
- [ ] I can close an RFI or identify a follow-up requirement.
- [ ] I can follow the local production, approval, and dissemination process.

If one area is weak, return to the corresponding 2.x unit.

#### Bridge Into 3.x Threat Hunting

CTI can answer:

> **What does the available intelligence tell us about the threat?**

That answer may create a new internal question:

> **Does this behavior or related activity exist elsewhere in our environment?**

That is where threat hunting begins.

CTI should hand hunting:
- the behavior/procedure;
- relevant indicators and observables;
- infrastructure context;
- provenance;
- uncertainty;
- applicability/visibility notes;
- the reason the lead matters.

Hunting then converts that intelligence into a bounded internal search.

#### Summary

The 2.x block taught one complete intelligence workflow:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

A strong intelligence product does not show everything the analyst found.

It shows what the evidence supports, why it matters, and what remains uncertain.

Keep one principle with you into 3.x:

> **The value of CTI is the supported answer—not the number of tools, indicators, or pivots used to reach it.**

## Part IV — Threat Hunting

An assessment can suggest behavior worth searching for beyond the original incident. Hunting turns that lead into a bounded question, tests it against available telemetry, and produces a finding with a clear handoff. Follow **Question → Hypothesis → Evidence → Refine → Finding → Handoff**.

> **A12 Case Study:** Follow the evidence available at this stage of the case. The uninterrupted narrative appears in [Appendix A](#appendix-a--the-complete-a12-case-study).

### 3.0 — Threat Hunting: How the 3.x Block Fits Together

**Estimated Time:** 10–15 minutes  

#### Learning Objectives

By the end of this introduction, you will be able to:

1. Explain the purpose of the 3.x threat-hunting block and how its seven units fit together.
2. Follow the basic hunt loop from a question to a finding and handoff.
3. Explain why hunt conclusions must remain bounded by the scope and telemetry actually tested.

#### What the Threat-Hunting Block Is Building Toward

Threat hunting begins when a security team has a reason to ask a question that existing alerts have not already answered well enough.

That reason may come from:
- an active incident;
- CTI;
- an anomaly;
- a testable hypothesis;
- a known detection or visibility gap.

The hunter turns that starting signal into a bounded search.

A simple mental model for the 3.x block is:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

The goal is not simply to run a query.

The goal is to produce a defensible answer:

> **What did we search, what did we find, what could we not see, and what should happen next?**

#### The Seven Units

| Unit | Main question | What you learn |
|---|---|---|
| **3.1 – Purpose** | Why hunt at all? | How hunting complements alerts, incident response, CTI, and detection engineering |
| **3.2 – Methodology** | What exactly are we testing? | Hunt types, hypotheses, scope, priority, and distinctive patterns |
| **3.3 – Online Tools** | What external evidence can sharpen the hunt? | Use external tools to develop leads that can become internal searches |
| **3.4 – CTI for Hunters** | Which intelligence is useful for hunting? | Assess CTI, extract hunt leads, and convert structured intelligence into search inputs |
| **3.5 – Framework Application** | How does ATT&CK help organize the hunt? | Map behavior and use ATT&CK to support planning without replacing the hypothesis |
| **3.6 – Attacker Techniques** | How do we hunt a specific behavior? | Build technique-focused searches for persistence, privilege escalation, and related procedures |
| **3.7 – Site-Specific Hunt Operations** | How does this shop control, document, and route hunts? | Local initiation, documentation, completion, and handoff requirements |

Each unit adds something different to the same hunt.

#### Hunting Starts With a Question

A hunt is easier to reason about when the question is explicit.

For the A12 scenario, an active incident might create the question:

> **Are there additional workstations with A12-style persistence?**

That is more useful than:

> Hunt persistence.

The first question tells the hunter what problem needs to be tested.

The second only names a topic.

#### Turn the Question Into a Testable Hypothesis

The question becomes a hunt when the hunter states what evidence should exist if the activity is present.

For example:

> If A12-style persistence exists on additional Windows user workstations, we expect to observe Run-key values pointing to `update.exe` or closely related payloads in user-writable paths.

Now the hunt can define:
- the population;
- the time window;
- the telemetry required;
- useful exclusions;
- what counts as a meaningful candidate.

This is the core of 3.2.

#### Evidence Comes From More Than One Place

A hunt may use:

**Internal telemetry**
- registry events;
- process events;
- file events;
- endpoint network activity;
- Zeek or other network telemetry.

**CTI**
- behaviors;
- procedures;
- infrastructure;
- indicators;
- structured STIX objects.

**External research tools**
- sandbox observations;
- passive DNS;
- file relationships;
- web-scan results.

The hunter's job is to turn those inputs into **internal search logic**.

An external platform result does not prove that the same behavior occurred locally.

It gives the hunter a reason to look.

#### Refine the Search as Evidence Appears

A hunt rarely ends with the first query.

Suppose a broad search for Run-key values pointing into `%TEMP%` returns hundreds of results.

The hunter may refine using:
- value name;
- target filename;
- signer information;
- parent process;
- time relationship to other events;
- known-good software exclusions.

That refinement is analysis.

The goal is not to eliminate every benign result before searching. The goal is to make the candidate set specific enough to investigate without filtering away the behavior you are trying to find.

#### A Hunt Can Produce Several Kinds of Findings

A hunt does not succeed only when it finds another compromised host.

Useful outcomes include:

- additional affected hosts or accounts;
- suspicious candidates needing incident review;
- a reusable behavioral pattern;
- a **detection gap**;
- a **visibility gap**;
- a new intelligence lead;
- evidence that the searched-for behavior was **not found within the tested scope and available visibility**.

That last phrase matters.

A negative hunt does not prove:

> This behavior does not exist anywhere.

It supports:

> We did not find this behavior in the population, time window, and telemetry that we actually tested.

#### Different Findings Go to Different Owners

The hunt output may contain several different problems.

For example:

| Hunt finding | Likely next owner category |
|---|---|
| Additional compromised host | SOC / Incident Response |
| Behavior visible but no analytic covers it | Detection Engineering |
| Required telemetry missing | Telemetry / platform owner |
| New infrastructure or actor question | CTI |
| New suspicious pattern worth another hunt | Hunt lead-management process |

The actual team names and workflows are local and are taught in 3.7.

The important idea is that the hunt does not have to solve every downstream problem itself.

#### Hypothetical A12-Based Hunt Loop

Canonical A12 reaches a hunt package, but the case does **not** specify the completed hunt result, additional affected-host count, visibility-gap count, or detection-coverage outcome.

The sequence below is a **hypothetical practice extension based on A12 behavior**. Its result counts are exercise conditions used to show the full 3.x workflow; they are **not canonical A12 facts**.

##### Question

> Are there additional hosts with A12-style persistence?

##### Hypothesis

> If the persistence exists elsewhere, registry telemetry should show Run values pointing to the same or closely related payload pattern.

##### Evidence

Search:
- registry modification telemetry;
- related process/file events;
- CTI-derived artifacts where useful.

##### Refine

Separate:
- exact `Updater → %TEMP%\update.exe`;
- related suspicious Run-value patterns;
- approved software/updaters.

##### Finding

Hypothetical practice result:

- 2 additional hosts with the exact persistence pattern;
- 7 hosts lack the registry telemetry needed to test the hypothesis;
- no current analytic covers the exact behavior.

##### Handoff

- affected hosts → SOC / IR;
- detection gap → Detection Engineering;
- telemetry gap → platform/telemetry owner;
- new infrastructure lead → CTI.

That is a complete **practice** hunt story. Do not carry the invented host counts or coverage result back into canonical A12.

#### What You Need to Remember Before 3.1

You do not need to know every ATT&CK technique, query language, or external platform yet.

Remember the loop:

> **Ask a bounded question.**  
> **State what evidence should exist.**  
> **Search the data you actually have.**  
> **Refine without losing the behavior.**  
> **Report what you found and what you could not see.**  
> **Route the outcome to the right owner.**

#### Orientation Check

1. Why is “hunt persistence” weaker than a bounded hunt question?
2. What does an external sandbox or passive-DNS result provide to a hunter?
3. A hunt returns no matches on 18 hosts, but 7 additional hosts lack the required telemetry. What can the hunter conclude?
4. Why might one hunt produce handoffs to SOC/IR, CTI, Detection Engineering, and a telemetry owner?

#### Summary

The 3.x block teaches a complete hunt workflow:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

Threat hunting searches beyond what current alerts have already surfaced, but every conclusion must remain tied to the scope and visibility actually tested.

A good hunt does more than find threats. It creates reusable defensive knowledge and makes gaps visible.

### 3.1 — Purpose of Threat Hunting

**Estimated Time:** 20–25 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain why threat hunting exists alongside alerting, incident response, CTI, and detection engineering.
2. Distinguish **uncovered activity**, a **detection gap**, a **visibility gap**, and a true **false negative**.

#### Key Concepts

Threat hunting searches deliberately for suspicious or malicious activity that has **not already been adequately surfaced by existing controls**.

That makes hunting complementary to the SOC rather than a replacement for it. The SOC responds to alerts and cases that are already visible. A hunt asks a broader question:

> What relevant activity could exist in the environment even though no useful alert brought it to us?

A good hunt can produce several kinds of value:

- previously unknown affected hosts or accounts;
- evidence that an incident is broader than first understood;
- a reusable behavioral pattern;
- a **detection gap** for detection engineering;
- a **visibility gap** for telemetry owners;
- a new intelligence lead for CTI;
- evidence that the searched-for behavior was not found **within the tested scope and available visibility**.

##### Four concepts that should stay separate

| Concept | Meaning |
|---|---|
| **Uncovered activity** | Relevant activity that was not already surfaced by an alert or case. |
| **Detection gap** | The needed telemetry exists, but current detections do not adequately cover the behavior. |
| **Visibility gap** | The telemetry needed to test the behavior is missing or insufficient. |
| **False negative** | A control that was expected to detect the activity failed to produce the expected detection. |

The distinction matters.

If HTTP telemetry shows `GET /update.exe` but the organization has **no detection designed to alert on that behavior**, the absence of an alert is a **coverage/detection gap**, not automatically a false negative.

If an existing analytic was explicitly designed to detect that exact behavior and the event satisfied its conditions but no alert was generated, then the event may represent a **false negative**.

##### A12 Case Study: Worked Example

The original A12 case began with a process alert on `WS-JLEE`.

Additional telemetry shows:

- `GET /update.exe` to `203.0.113.88:8080`;
- HKCU Run value `Updater` pointing to `%TEMP%\update.exe`.

A hunt can ask whether similar artifacts appear on **other hosts**.

Possible outcomes:

- more affected hosts are found;
- registry telemetry exists but no analytic covers the pattern → **detection gap**;
- some host classes do not collect registry telemetry → **visibility gap**;
- an existing rule should have alerted on the exact event but failed → investigate a possible **false negative**.

The hunt output should preserve these distinctions instead of describing every unalerted event as a failed detection.

#### Knowledge Check

1. Why is threat hunting complementary to the SOC rather than a replacement for it?
2. What is the difference between a detection gap and a visibility gap?
3. HTTP telemetry contains `GET /update.exe`, but no analytic is designed to alert on that pattern. Is the missing alert automatically a false negative? Explain.

#### Summary

Threat hunting searches beyond what existing alerts have already surfaced.

Its value is not limited to finding compromise. Hunts also expose coverage and visibility gaps and generate reusable defensive knowledge.

Call something a **false negative** only when a control was expected to detect it and failed.

### 3.2 – Hunt Methodology: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Threat hunting becomes repeatable when the hunter can choose an appropriate hunt type and turn a question into a bounded plan with a hypothesis, scope, evidence sources, and stopping conditions.

#### Connect to What You Already Know

The hunt-purpose lesson established why hunting exists and how it differs from routine alert response. This subunit focuses on how to design the search before opening tools.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **3.2.1 – Hunt Types** | Choose a hunt type based on the starting evidence, question, and objective. |
| **3.2.2 – Hunt Development** | Turn the objective into a hypothesis, look-fors, scope, telemetry plan, and documented execution approach. |

#### What to Watch For

- Choose the hunt type from the evidence and question rather than from a preferred tool.
- Keep the hypothesis testable and the scope bounded enough to produce an interpretable result.
- Identify the telemetry needed before execution so a missing result can be interpreted correctly.

#### Expected End State

By the end of this subunit, you should be able to:

- distinguish the major hunt types and select one for a realistic starting condition;
- write or assess a testable hunt hypothesis;
- define scope, look-fors, and telemetry needed to evaluate the hypothesis;
- recognize when a hunt design is too broad or underspecified to produce a useful finding.

#### How to Preview This Subunit

Read this introduction, then skim the [3.2 Summary](#32--hunt-methodology-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 3.2.1 — Hunt Types

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Explain the four hunt types used by this course and the **initiating signal** for each.
2. Given a seed, identify the primary hunt type and state the question or look-for it should produce.

#### Key Concepts

There is no single universal industry taxonomy for hunt types. This course uses four labels because they help explain **what caused the hunt to begin**.

| Course hunt type | Primary initiating signal | A12 example |
|---|---|---|
| **Intel-driven** | CTI provides a behavior, observable, indicator, or procedure worth searching locally. | CTI reports the update domain or a distinctive Run-key procedure. |
| **Hypothesis-driven** | The hunter begins with a testable proposition about what should be visible if an activity is occurring. | “If A12-style persistence exists elsewhere, we should see a Run value pointing into a user-writable Temp path.” |
| **Reactive** | A known incident or confirmed finding creates a need to determine wider scope or related activity. | After A12, search the estate for the same or related persistence and payload artifacts. |
| **Anomaly-based** | An unusual pattern or deviation from baseline becomes the starting lead. | Rare outbound `:8080` requests for `/update.exe` on hosts without an associated alert. |

##### The categories can overlap

A reactive hunt can also use intelligence. An intel-driven hunt should still have a testable question. An anomaly can later be linked to a known actor.

For this course, classify the hunt by its **primary starting signal**.

That prevents a taxonomy debate from becoming more important than the hunt itself.

##### Every hunt should become testable

Even when the hunt does not begin as “hypothesis-driven,” it should eventually be expressed as a question or expectation that evidence can support or fail to support.

Examples:

**Intel-driven**
> CTI reports the `Updater` Run value. Do other user workstations contain the same value/path relationship?

**Reactive**
> A12 affected one workstation. Are the same or closely related artifacts present elsewhere during the incident window?

**Anomaly-based**
> Several hosts made rare `:8080` requests for `/update.exe`. Is the pattern associated with the A12 activity set or a benign application?

##### Preparation is not execution

This lesson prepares you to recognize the initiating signal, classify the primary hunt type, and form the first testable question. Those are required planning skills, but they do **not** by themselves satisfy a task whose approved verb is **execute**.

For `3.2.1.1`–`3.2.1.4`, execution means you actually run the hunt against supplied or approved telemetry and record the scope, query/search, results, gaps, and bounded finding.

Use the [Hunt Execution Practical](#hunt-execution-practical--controlled-telemetry) to demonstrate the four execution tasks. The detailed hunt-development model is taught next in 3.2.2.

#### Knowledge Check

1. Why can one hunt reasonably fit more than one category?
2. CTI publishes a distinctive persistence procedure and you decide to look for it locally. Which course type best describes the initiating signal?
3. An active A12 investigation asks hunting to determine whether other hosts are affected. Which type is primary, and what question would you ask?

#### Summary

The four course hunt types describe the **primary reason the hunt starts**.

They are useful labels, not rigid boxes. Regardless of type, the hunt should become a bounded, testable search.

#### Hunt Execution Practical — Controlled Telemetry

**Purpose:** demonstrate the operational verbs in `3.2.1.1`–`3.2.1.4` and `3.6.3` with one reusable dataset. This is a **separate training scenario**, not canonical A12.

##### Inputs

Use [hunt-execution-practical.csv](#lab-asset--hunt-execution-practicalcsv). The dataset represents a fictional organization, **Blue Heron Manufacturing (BHM)**.

Run the searches with a tool that actually filters or queries the supplied data: a spreadsheet filter, command-line tool, Python, a notebook, or an approved training SIEM. **Do not satisfy the practical by only reading the table and describing what you would search.**

For every execution, preserve:

1. initiating signal / hunt type;
2. scope and time window;
3. exact query or filter used;
4. returned rows / hosts;
5. telemetry or interpretation gaps;
6. bounded finding and next action.

##### Practical A — Intel-driven hunt (`3.2.1.1`)

**Seed intelligence:** CTI reports that suspicious activity may use domain `cdn-sync.example` and Run value name `Updater`.

Execute a local search for both observables, identify matching hosts, then decide whether a broader behavior search is justified. Record which results are exact matches and which are only related candidates.

##### Practical B — Hypothesis-driven hunt (`3.2.1.2`)

**Hypothesis:** If unauthorized persistence is using user-writable temporary directories, recent Run-key modifications should reference executables under a user's `AppData\Local\Temp` path more often on affected hosts than on ordinary workstations.

Execute a search for the condition. Review all returned rows rather than assuming every Temp-path Run key is malicious. Use signature/context fields to separate suspicious results from the benign near-neighbor.

##### Practical C — Reactive hunt (`3.2.1.3`)

**Incident seed:** `BHM-WKS-07` is the known affected host.

Execute an estate search for exact and related artifacts from that host. Identify any additional hosts that merit incident scoping and state which evidence created the relationship. Do not claim compromise where the evidence only creates a candidate lead.

##### Practical D — Anomaly-based hunt (`3.2.1.4`)

**Anomaly seed:** outbound HTTP traffic on destination port `8080` is rare in the workstation population.

Execute a search for port `8080`, group or compare the results by destination/process/path, and determine which results can be explained as approved activity versus which remain suspicious. A rare event is a lead, not a verdict.

##### Practical E — Technique-focused hunt (`3.6.3`)

Execute **two** searches for ATT&CK `T1547.001` behavior:

1. **Exact-observed layer:** Run value `Updater` or exact Temp updater paths.
2. **Behavior-broadened layer:** Run-key values that launch executables from user-writable temporary locations.

Compare the returned hosts. Explain what the exact layer misses, what the broadened layer adds, and why the broadened result set requires contextual review.

##### Evaluator evidence

The evaluator should observe the learner actually execute the filters/queries and retain the query text or filter criteria. A satisfactory result includes:

- correct scope and use of the initiating signal;
- reproducible query/filter logic;
- accurate identification of returned hosts/events;
- explicit handling of benign near-neighbors and visibility limits;
- findings bounded to the supplied evidence;
- a defensible next action.

At higher proficiency, expect efficient query refinement, explanation of false-positive/false-negative risk, and adaptation when the first search is too narrow or too broad. Qualification/sign-off remains a separate evaluator action under the course standard.

##### Lab Asset — hunt-execution-practical.csv

Embedded from `/thraining-plan/labs/hunt-execution-practical.csv` for this controlled practical.

```csv
timestamp,host,event_source,event_type,user,process,command_line,registry_path,registry_value_name,registry_value_data,file_path,dst_domain,dst_ip,dst_port,url_path,signature_status,note
2026-09-14T08:12:03Z,BHM-WKS-07,endpoint,process,mkim,wscript.exe,wscript.exe invoice.vbs,,,,,,,,,signed,reactive seed host
2026-09-14T08:12:08Z,BHM-WKS-07,endpoint,process,mkim,powershell.exe,powershell.exe -NoP -EncodedCommand JAB3AGM...,,,,,,,,,signed,encoded PowerShell child
2026-09-14T08:13:20Z,BHM-WKS-07,registry,registry_set,mkim,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,Updater,C:\Users\mkim\AppData\Local\Temp\updater.exe,,,,,,,run key to user-writable temp
2026-09-14T08:14:01Z,BHM-WKS-07,network,http,mkim,powershell.exe,,,,,,,cdn-sync.example,198.51.100.44,8080,/update.exe,,rare external 8080
2026-09-14T08:15:10Z,BHM-WKS-07,file,file_create,mkim,powershell.exe,,,,,C:\Users\mkim\AppData\Local\Temp\updater.exe,,,,,unsigned,temp executable created
2026-09-14T09:41:02Z,BHM-WKS-12,registry,registry_set,ajones,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,Updater,C:\Users\ajones\AppData\Local\Temp\updater.exe,,,,,,,exact Updater pattern
2026-09-14T09:42:16Z,BHM-WKS-12,network,http,ajones,updater.exe,,,,,,,cdn-sync.example,198.51.100.44,8080,/update.exe,unsigned,same infrastructure/path
2026-09-14T09:42:50Z,BHM-WKS-12,file,file_create,ajones,updater.exe,,,,,C:\Users\ajones\AppData\Local\Temp\updater.exe,,,,,unsigned,related file
2026-09-15T11:05:44Z,BHM-WKS-19,registry,registry_set,rpatel,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,OneDriveUpdate,C:\Users\rpatel\AppData\Local\Temp\syncsvc.exe,,,,,,,variant temp Run key
2026-09-15T11:06:31Z,BHM-WKS-19,network,http,rpatel,syncsvc.exe,,,,,,,updates-cdn.example,203.0.113.74,8080,/pkg.bin,unsigned,variant infrastructure
2026-09-15T11:07:09Z,BHM-WKS-19,file,file_create,rpatel,syncsvc.exe,,,,,C:\Users\rpatel\AppData\Local\Temp\syncsvc.exe,,,,,unsigned,variant temp executable
2026-09-14T07:01:11Z,BHM-WKS-03,registry,registry_set,lchen,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,OneDrive,C:\Program Files\Microsoft OneDrive\OneDrive.exe /background,,,,,,,Microsoft,common benign Run key
2026-09-14T07:02:03Z,BHM-WKS-04,registry,registry_set,sgarcia,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,Teams,C:\Program Files\Microsoft\Teams\current\Teams.exe --processStart Teams.exe,,,,,,,Microsoft,common benign Run key
2026-09-15T12:30:00Z,BHM-WKS-22,network,http,svc_backup,backupagent.exe,,,,,,,backup-gw.internal,10.20.30.40,8080,/health,signed,approved internal backup service
2026-09-15T12:31:00Z,BHM-WKS-23,network,http,svc_backup,backupagent.exe,,,,,,,backup-gw.internal,10.20.30.40,8080,/health,signed,same approved service
2026-09-15T15:10:21Z,BHM-WKS-31,network,http,dnguyen,java.exe,,,,,,,telemetry.vendor.example,192.0.2.80,8080,/metrics,signed,approved vendor telemetry
2026-09-16T08:55:18Z,BHM-WKS-44,registry,registry_set,hlee,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,AcmeUpdater,C:\Users\hlee\AppData\Local\Temp\AcmeSetup\acme-update.exe,,,,,,,Acme Software LLC,near-neighbor temp Run key; signed vendor
2026-09-16T08:55:32Z,BHM-WKS-44,file,file_create,hlee,acme-update.exe,,,,,C:\Users\hlee\AppData\Local\Temp\AcmeSetup\acme-update.exe,,,,,Acme Software LLC,benign signed updater
2026-09-16T08:56:01Z,BHM-WKS-44,network,https,hlee,acme-update.exe,,,,,,,updates.acme.example,192.0.2.55,443,/v3/check,Acme Software LLC,benign updater traffic
2026-09-16T10:02:19Z,BHM-WKS-52,endpoint,process,kwhite,powershell.exe,powershell.exe Get-Service | Where-Object {$_.Status -eq 'Running'},,,,,,,,,signed,administrative PowerShell
2026-09-16T10:04:29Z,BHM-WKS-53,registry,registry_set,jcooper,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,PrinterHelper,C:\Program Files\PrinterCo\helper.exe,,,,,,,PrinterCo,benign Run key
2026-09-17T03:14:05Z,BHM-SRV-02,network,http,svc_app,appsvc.exe,,,,,,,api.partner.example,192.0.2.140,8080,/api/status,signed,server app expected 8080
2026-09-17T05:20:50Z,BHM-WKS-58,registry,registry_set,mross,,,HKCU\Software\Microsoft\Windows\CurrentVersion\Run,UpdaterService,C:\Users\mross\AppData\Roaming\Updater\svc.exe,,,,,,,unsigned,rare Run key but not Temp
2026-09-17T05:21:30Z,BHM-WKS-58,network,https,mross,svc.exe,,,,,,,cloud-storage.example,203.0.113.120,443,/sync,unsigned,needs review; no exact CTI match
```

### 3.2.2 — Hunt Development Concepts

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Write a testable hunt hypothesis and define a scope that states population, time window, and telemetry.
2. Prioritize the hunt and identify a **distinctive/discriminating pattern** suitable for internal search.

#### Key Concepts

A hunt becomes useful when another hunter can understand **what is being tested, where it will be tested, why it matters now, and what evidence would be meaningful**.

This course captures that in four core fields:

| Field | Purpose |
|---|---|
| **Hypothesis** | A proposition that evidence can support or fail to support. |
| **Scope** | Population, time window, telemetry, and important exclusions. |
| **Priority** | Why this hunt should consume time now. |
| **Distinctive pattern** | The behavior or artifact that makes the search selective enough to investigate. |

##### Hypothesis

A good hypothesis is not a topic such as “hunt persistence.”

It connects a condition to expected evidence.

> If A12-style persistence exists on additional user workstations, we expect to observe Run-key values pointing to `update.exe` or closely related payloads in user-writable paths.

That statement can produce findings, or it can produce no findings within the tested scope.

##### Scope

Scope should make a negative result interpretable.

For example:

- **Population:** managed Windows user workstations
- **Window:** previous 14 days
- **Telemetry:** registry modification + file/process telemetry
- **Exclusions:** known software-deployment systems or approved updater paths, where appropriate

“Entire enterprise, all time, every log” is not automatically better. It often makes the search expensive and the result harder to interpret.

##### Priority

Useful priority factors include:

- active incident or mission need;
- strength and freshness of the lead;
- local applicability;
- available telemetry;
- likely defensive value;
- search cost and analyst capacity;
- existing detection coverage.

ATT&CK mapping can support priority later, but an ATT&CK tactic name is not a priority score by itself.

##### Distinctive pattern

The curriculum calls this a “unique pattern,” but in practice **distinctive** or **discriminating** is the better idea.

`Updater` alone may be useful if rare locally. A stronger pattern can combine:

- Run-key location;
- value name;
- user-writable target path;
- uncommon parent process;
- file/signing context.

The goal is not perfect uniqueness. The goal is enough specificity to separate a manageable set of candidates from normal activity.

##### Visibility comes before interpretation

A hunt that depends on registry modification data cannot produce a meaningful “not found” result on systems where registry telemetry is absent.

Document that limitation in scope.

#### Knowledge Check

1. Why is “hunt persistence” not a sufficient hypothesis?
2. What four core fields does this course use to develop a hunt?
3. Write a scoped A12 hypothesis using user workstations, a 14-day window, and registry/file telemetry.

#### Summary

Develop the hunt before running the search.

A useful hunt has a testable hypothesis, bounded scope, defensible priority, and a distinctive pattern grounded in telemetry you actually have.

### 3.2 – Hunt Methodology: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Question → hunt type → hypothesis → scope/look-fors → telemetry → execute/refine**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- distinguish the major hunt types and select one for a realistic starting condition;
- write or assess a testable hunt hypothesis;
- define scope, look-fors, and telemetry needed to evaluate the hypothesis;
- recognize when a hunt design is too broad or underspecified to produce a useful finding.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **3.2.1 – Hunt Types** | Choose a hunt type based on the starting evidence, question, and objective. |
| **3.2.2 – Hunt Development** | Turn the objective into a hypothesis, look-fors, scope, telemetry plan, and documented execution approach. |

#### Check Your Understanding

Ask yourself:

1. What should determine whether a hunt is hypothesis-driven, intel-driven, retrospective, or anomaly-focused?
2. What makes a hunt hypothesis testable rather than merely interesting?
3. Why should telemetry availability be checked before interpreting a negative hunt result?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **3.3 – Online Tools for Threat Hunting**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 3.3.1 — Tool Capabilities for Hunting

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Use VirusTotal, ANY.RUN, urlscan.io, and Silent Push outputs to identify hunt-relevant pivots.
2. Convert an external finding into a precise **internal query plan** that names the local data source, fields, value, and time window.

#### Key Concepts

External tools provide **context and candidates**. Internal telemetry tells you whether the activity occurred in your environment.

| Tool | Hunt-relevant strength | Important limit |
|---|---|---|
| **VirusTotal** | Object relationships and sandbox behavior can expose related files, domains, IPs, processes, files, registry, and network events. | A relationship or sandbox event is external evidence, not proof it occurred internally. |
| **ANY.RUN** | TI Lookup can search IOCs and sandbox event fields such as processes, registry activity, commands, mutexes, and network events. | A threat label or one sandbox session is not the internal hunt result. |
| **urlscan.io** | A scan can expose redirects, requested domains/IPs/URLs, page metadata, certificates, and HTTP artifacts. | One browser scan is time/environment specific and may include unrelated third-party services. |
| **Silent Push** | Passive DNS can expose historical domain/IP and other DNS relationships. | Provider-observed PADNS associations require time and hosting-density context. |

##### Supporting documentation

- [VirusTotal Relationships](https://docs.virustotal.com/reference/relationships)
- [VirusTotal File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)
- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)
- [Silent Push DNS Data](https://help.silentpush.com/docs/dns-data)
- [urlscan Result API](https://urlscan.io/docs/result/)

##### What makes a good hunt lead?

A hunt lead should be **internally queryable** and retain enough context to avoid becoming a blind IOC search.

Examples:

- destination `203.0.113.88`, TCP port `8080`, URI `/update.exe`;
- registry value `Updater` under a Run key, pointing to a user-writable path;
- a dropped filename plus parent process or hash;
- a rare domain paired with an observed time window.

A detection count, verdict label, or screenshot can provide context but is not itself the internal search.

##### Convert the finding into an internal query plan

Write:

1. **Local data source** – e.g., Zeek `http.log`, EDR process events, registry telemetry.
2. **Fields** – the fields that express the lead.
3. **Values/relationship** – the exact artifact or behavior.
4. **Time window / population** – where and when to search.
5. **Expected review context** – what would make a hit interesting or benign.

Example:

> **Data source:** Zeek HTTP telemetry  
> **Predicate:** `id.resp_h = 203.0.113.88`, `id.resp_p = 8080/tcp`, `uri = /update.exe`  
> **Window:** A12 window ± 14 days across user-workstation traffic  
> **Review:** identify originating hosts, repeated requests, response metadata, and associated file/process evidence.

Those are **field constraints**, not a claim that Zeek itself has a universal query language. The exact SIEM syntax depends on where your Zeek data is stored.

##### Preserve external-source provenance

Phrase the lead as:

> VirusTotal behavior report observed...

or:

> Silent Push PADNS associated...

Then ask whether internal telemetry contains the same or related activity.

##### Platform use must be demonstrated separately

This lesson teaches what the four platforms can contribute and how to turn their results into internal hunt leads. That preparation does **not** by itself satisfy `3.3.1.1`, whose approved verb is **perform**.

Use the [External Tool Pivot Practical](#external-tool-pivot-practical--virustotal-anyrun-urlscanio-and-silent-push) to demonstrate actual searching and pivoting in VirusTotal, ANY.RUN, urlscan.io, and Silent Push. The practical requires preserved provenance and a local test derived from each platform result.

#### Knowledge Check

1. Why is a VirusTotal relationship useful but not proof of internal activity?
2. What four or five elements make an external finding into a good internal query plan?
3. Convert `203.0.113.88:8080` + `/update.exe` into a Zeek/SIEM field predicate and scope.

#### Summary

External tools generate context and candidates. Hunting converts them into precise internal tests.

Carry forward the artifact **and** its context, then search the local telemetry that can actually answer the question.

#### External Tool Pivot Practical — VirusTotal, ANY.RUN, urlscan.io, and Silent Push

**Purpose:** demonstrate task `3.3.1.1` by actually querying and pivoting in the four named external platforms. Planning a query or interpreting a screenshot does not by itself demonstrate this task.

##### Delivery model

This is an evaluator-led practical. The evaluator supplies one approved seed per platform at delivery time so the exercise does not depend on stale public results. The seed may be a hash, domain, IP, URL, or other object appropriate to the platform and the learner's access level.

Use an approved training account, free/public access where permitted, or another authorized account. Do not submit sensitive organizational artifacts to public services merely to complete the exercise.

For every platform, preserve:

1. seed value and timestamp;
2. query/search used;
3. at least one pivot performed;
4. result object or report identifier/URL when policy permits;
5. one hunt-relevant lead extracted from the result;
6. provenance wording that identifies the external source;
7. the internal telemetry/data source and field relationship you would use to test the lead locally.

##### Station A — VirusTotal

Use the supplied seed to perform a search, inspect relevant relationships and/or behavior, pivot to a related object, and extract one lead that could be tested internally.

A valid result shows more than the seed lookup: the learner must use a relationship, behavior, or other supported pivot and explain why the resulting object is a candidate rather than proof of internal occurrence.

##### Station B — ANY.RUN

Use the supplied seed in the available search/TI workflow, review the returned submission or TI context, pivot through at least one behavior or related observable, and extract a hunt lead. Preserve the relevant submission/report identifier when allowed.

##### Station C — urlscan.io

Retrieve or search for the supplied URL/domain result, inspect request/redirect/infrastructure artifacts, pivot to one related object or result, and identify a lead that can be represented as local HTTP/DNS/TLS fields.

##### Station D — Silent Push

Use the supplied seed to inspect passive-DNS or related infrastructure context, perform at least one infrastructure pivot, and record the time/hosting-density context needed before using the result as a hunt lead.

##### Required final output

Create a four-row evidence table with one row per platform:

| Platform | Seed | Query/pivot | Extracted lead | Provenance statement | Internal test |
|---|---|---|---|---|---|

The internal test should name the local source, fields/relationship, and time/population. It does not have to prove the activity occurred; the purpose is to convert an external candidate into a precise local test.

##### Evaluator criteria

A satisfactory demonstration requires the learner to actually use all four platforms and preserve enough evidence to reproduce the reasoning. The evaluator should confirm:

- the learner performed a real search/query and at least one pivot in each platform;
- the pivot selected is supported by what the platform actually shows;
- the learner does not turn an external relationship/verdict into proof of local activity;
- the extracted lead is internally queryable;
- provenance, time, and infrastructure-sharing context are preserved where relevant;
- the local test is precise enough to hand to a hunter/SIEM user.

At higher proficiency, expect better pivot selection, faster recognition of weak/common-infrastructure relationships, and adaptation when the first pivot is unproductive. Qualification/sign-off remains a separate evaluator action under the course standard.

### 3.4 – CTI as Hunt Input: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

CTI can give hunters behaviors, observables, infrastructure, and relationships worth searching for, but not every intelligence statement is a usable hunt lead. The hunter has to assess the intelligence, extract testable elements, and preserve the difference between what the source claims and what local telemetry can verify.

#### Connect to What You Already Know

The methodology and tools lessons established how hunts are designed and executed. This subunit focuses on turning external or internal intelligence into bounded local search inputs.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **3.4.1 – Assessing CTI for Hunting** | Decide whether intelligence is relevant, specific, timely, and observable enough to support a hunt. |
| **3.4.2 – Extracting Hunt Leads** | Extract behaviors, artifacts, observables, and relationships that can become testable hunt leads. |
| **3.4.3 – STIX as Hunt Input** | Read STIX objects and relationships as structured inputs while returning to the underlying evidence and observables for the actual hunt. |

#### What to Watch For

- Separate the intelligence judgment from the local search condition you can actually test.
- Prefer behavior and observable detail that maps to available telemetry over actor-name awareness alone.
- Use STIX as a representation of intelligence, not as a substitute for understanding the underlying objects and relationships.

#### Expected End State

By the end of this subunit, you should be able to:

- assess whether a CTI product is suitable for a hunt;
- extract concrete hunt leads from intelligence without copying unsupported claims into the hypothesis;
- translate structured STIX content into useful local hunt inputs;
- state what local telemetry can confirm, refute, or leave unresolved.

#### How to Preview This Subunit

Read this introduction, then skim the [3.4 Summary](#34--cti-as-hunt-input-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 3.4.1 — Assessing CTI for Hunting Value

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Evaluate whether a CTI report can support a useful local hunt.
2. Classify the next step as **hunt**, **awareness/monitor**, or **coordinate/hand off**, and explain the reason.

#### Key Concepts

A report is hunt-worthy when it can produce a **local, testable question with enough visibility and enough incremental value to justify the search**.

Five quick checks help:

1. **Applicability** – Does the environment contain the relevant platform, service, user population, or exposure?
2. **Testability** – Does the report contain a behavior, procedure, artifact, or relationship that can become a question?
3. **Visibility** – Do we have telemetry capable of testing that question?
4. **Scope** – Can the search be bounded to a reasonable population and time window?
5. **Incremental value** – Will hunting add something beyond work already adequately covered by an active response or existing analytic?

##### Three practical dispositions

| Disposition | When it fits |
|---|---|
| **Hunt** | A relevant, testable question exists; telemetry and scope are sufficient; broader discovery can add value. |
| **Awareness / monitor** | The report is useful context but does not currently support a useful local search. |
| **Coordinate / hand off** | The immediate next action belongs to IR, SOC, DE, or another function; hunting may still support later if a broader search question remains. |

The third category is not “IR touched the hash, therefore hunting stops.”

During an active incident, a reactive hunt can be especially valuable for finding additional affected systems. Coordination matters because containment and evidence preservation may take priority over an independent search on the same hosts.

##### A12 Case Study: Worked Examples

**Hunt**
> Report describes Run-key persistence and `/update.exe`; registry and HTTP telemetry exist; the question is whether related artifacts exist on additional workstations.

**Awareness / monitor**
> Report describes a platform the organization does not operate, with no applicable procedure elsewhere in the report.

**Coordinate / hand off**
> A specific endpoint shows confirmed active compromise requiring containment. IR owns immediate response. Hunting coordinates with IR and may run an estate-wide search for related behavior.

##### Hunt-worthiness is not the same as “interesting”

Actor reputation, severity language, or a long ATT&CK appendix do not create a hunt by themselves.

The hunter needs a test.

#### Knowledge Check

1. What five checks help determine hunt-worthiness?
2. Why does an active IR case not automatically mean “do not hunt”?
3. A report gives a locally applicable Run-key procedure, registry telemetry exists, and no detection covers it. Which disposition fits and why?

#### Summary

Assess CTI for **local testability and value**, not just threat severity.

Hunt when a bounded question and visibility exist. Monitor when the report cannot support a useful local search. Coordinate when another operational function owns the immediate action.

### 3.4.2 — Extracting Hunt Leads from CTI

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Extract hunt-suitable procedures, behaviors, observables, and indicators from a CTI report.
2. Evaluate each candidate lead for provenance, applicability, distinctiveness, validity, and local visibility, then state the hunt question it supports.

#### Key Concepts

A CTI report becomes hunt input only after the hunter translates it into **searchable local evidence**.

##### What to extract

**Procedures / behaviors**
- Run-key persistence pointing into a user-writable path;
- encoded PowerShell spawned by a script interpreter;
- scheduled task creation with an unusual action;
- HTTP request to a campaign-specific path.

**Observables / indicators**
- hash;
- domain/IP/URL;
- filename/path;
- registry value;
- certificate;
- user-agent or protocol trait.

**Context**
- platform;
- time period;
- target population;
- parent/child relationship;
- expected role in the intrusion.

Context often determines whether the lead is useful.

##### Evaluate each candidate lead

Ask:

1. **Provenance** – Where did the claim/value come from?
2. **Local applicability** – Can this exist in our environment?
3. **Distinctiveness** – Will it reduce normal activity to a reviewable set?
4. **Validity / timeliness** – Is the relationship still relevant to the question?
5. **Visibility** – Do we have telemetry that can test it?

##### Old does not automatically mean expired

A SHA256 from 2019 does not become invalid merely because it is old. A file hash can remain useful for retrospective search indefinitely.

An indicator should be treated as expired/invalid when its source or context says its useful validity ended, ownership changed, the pattern no longer represents the threat, or a defined validity window ended.

Age affects priority and expected yield. It is not an automatic expiration rule.

##### Missing telemetry is a gap, not a reason to erase the lead

If a report provides a strong persistence procedure but the environment lacks registry telemetry:

- keep the procedure as relevant intelligence;
- mark it **not currently executable as a hunt lead**;
- record the **visibility gap**.

That preserves the defensive requirement.

##### A12 extraction

**Keep procedure**
> HKCU Run value `Updater` → `%TEMP%\update.exe`

**Keep observable**
> `GET /update.exe` to `203.0.113.88:8080`

**Keep context**
> Windows user workstations; incident time window

**Weak/broad candidate**
> Entire `203.0.113.0/24` without evidence of common control

**Hunt question**
> Are A12-related persistence or payload-delivery artifacts present on additional Windows user workstations during the scoped time window?

#### Knowledge Check

1. Why is a 2019 hash not automatically “expired”?
2. What should you do with a strong CTI procedure that is locally applicable but not observable with current telemetry?
3. From the A12 slice, give one procedure, one observable, and one hunt question.

#### Summary

Extract more than IOC lists. Preserve procedures, observables, and the context that makes them meaningful.

Evaluate leads for applicability, distinctiveness, validity, and visibility. If visibility is missing, record the gap rather than deleting the intelligence.

### 3.4.3 — STIX as Hunt Input

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Identify STIX objects and references that can supply hunt-relevant evidence.
2. Convert STIX content into a local hunt lead without assuming that every object—or every object in the same Bundle—is directly searchable.

#### Key Concepts

STIX gives CTI a structured way to represent threat and observable information. Hunters consume that structure; they do not need to author it in this lesson.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

##### Objects with direct hunt value

| STIX content | Hunt use |
|---|---|
| **Indicator** | Parse the pattern into observable fields/values that local telemetry can search. Check validity and context. |
| **Observed Data + referenced SCOs** | Identify the file, IP, domain, process, registry key, or other observable that was actually recorded. |
| **Attack Pattern** | Use the named behavior as a hunt seed when locally applicable and visible. |
| **Sighting** | Understand that an SDO was reported as seen; inspect `observed_data_refs` and where it was sighted when available. |
| **Relationship** | Preserve why objects are connected (`indicates`, `uses`, `based-on`, etc.) so the lead keeps its analytic context. |

##### Context objects are useful without being direct queries

**Malware**, **Threat Actor**, **Intrusion Set**, and **Campaign** can help prioritize or group a hunt, but the object name itself may not be searchable in local telemetry.

A STIX Malware object does **not inherently contain a file hash**. File hashes are represented through cyber-observable objects or Indicator patterns/observations linked to the malware.

That distinction prevents a hunter from expecting every `malware` object to produce an IOC automatically.

##### Bundle membership has no semantic meaning

Two objects are not related merely because they appear in the same STIX Bundle.

Use explicit Relationships, Sightings, embedded references, and object properties to understand the graph.

##### A12 Case Study: Worked Example

Suppose a classroom package contains:

- `indicator` pattern for `203.0.113.88`;
- `attack-pattern` for T1547.001;
- `observed-data` referencing a File and Process;
- `relationship` tying the Indicator to Malware;
- a `sighting` with supporting Observed Data.

A hunter can derive:

> Search internal network telemetry for the IP during the relevant window, and search registry/file telemetry for the T1547.001 procedure described by the related report/observations.

The actor or malware name can help prioritize the search. The actual local query comes from the observable pattern and behavior.

#### Knowledge Check

1. Why does a STIX Malware object not automatically give you a file hash?
2. Which STIX object is most likely to contain a machine-readable detection pattern?
3. Why should a hunter inspect Relationships rather than assume objects in the same Bundle are connected?

#### Summary

Use STIX structure to preserve **what the lead is and why it is related**.

Indicator patterns and observed cyber-observables often provide direct query material. Attack Patterns provide behavior. Context objects provide scope and priority.

#### References and Further Reading

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### 3.4 – CTI as Hunt Input: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**CTI product → suitability check → extract leads → map to telemetry → hunt hypothesis/search**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- assess whether a CTI product is suitable for a hunt;
- extract concrete hunt leads from intelligence without copying unsupported claims into the hypothesis;
- translate structured STIX content into useful local hunt inputs;
- state what local telemetry can confirm, refute, or leave unresolved.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **3.4.1 – Assessing CTI for Hunting** | Decide whether intelligence is relevant, specific, timely, and observable enough to support a hunt. |
| **3.4.2 – Extracting Hunt Leads** | Extract behaviors, artifacts, observables, and relationships that can become testable hunt leads. |
| **3.4.3 – STIX as Hunt Input** | Read STIX objects and relationships as structured inputs while returning to the underlying evidence and observables for the actual hunt. |

#### Check Your Understanding

Ask yourself:

1. What makes an intelligence report hunt-worthy instead of merely useful for awareness?
2. How does a behavioral lead differ from repeating an actor label in a query?
3. Why should a hunter inspect the objects and evidence behind a STIX relationship before using it as a search condition?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **3.5 – Framework Application in Hunting**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 3.5.1 — Using MITRE ATT&CK for Hunt Planning

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Map the behavior a hunt will test—or has found—to the most specific ATT&CK technique/sub-technique supported by evidence.
2. Use that mapping to describe detection/visibility gaps and support hunt priority without treating ATT&CK as a scoring system.

#### Key Concepts

ATT&CK gives the hunt a shared behavioral vocabulary.

Reference: [MITRE ATT&CK](https://attack.mitre.org/)

##### Map the behavior this hunt is testing

Do not map every technique associated with a named actor.

Map:

> the procedure or behavior this hunt is searching for

to:

> the most specific ATT&CK technique/sub-technique the evidence supports.

##### Technique and tactic are related but not identical

One ATT&CK technique can support more than one tactic.

For example, [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/) is currently associated with both **Persistence** and **Privilege Escalation**.

The A12 HKCU Run value executes in the logged-on user's context. In that scenario, the supported use is **Persistence**. Nothing in the Run-key observation by itself establishes higher privileges.

So the hunt mapping is:

> **Persistence / T1547.001 – Registry Run Keys / Startup Folder**

The same technique could support a different tactic in another context when the evidence demonstrates that role.

##### Use ATT&CK for coverage analysis

After mapping the hunt, ask:

**Visibility**
> Do we collect telemetry that can observe this procedure on the in-scope systems?

**Detection**
> If the telemetry exists, does an analytic meaningfully cover the behavior?

Examples:

- registry data absent on a host class → **visibility gap**;
- registry data present but no analytic covers suspicious Run-key changes → **detection gap**.

##### ATT&CK supports priority; it does not determine it

Hunt priority also depends on:

- active incident/mission relevance;
- strength and freshness of the lead;
- local applicability;
- visibility;
- current detection coverage;
- expected defensive value;
- analyst/search cost.

A technique being mapped to Persistence does not make it automatically higher priority than another hunt.

#### Knowledge Check

1. Why should you map the behavior being hunted instead of every technique associated with an actor?
2. T1547.001 is associated with more than one tactic. Why is **Persistence** the relevant tactic for the A12 HKCU Run example?
3. Registry telemetry exists but no analytic covers suspicious Run-key changes. Which gap is that?

#### Summary

Map the hunt's **actual behavior** to ATT&CK.

Use context to choose the relevant tactic when a technique spans more than one. Then use the mapping to reason about visibility and detection coverage.

ATT&CK informs priority; it does not replace operational judgment.

#### References and Further Reading

- [MITRE ATT&CK](https://attack.mitre.org/)
- [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)

### 3.6 – Attacker Techniques for Hunting: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

Technique knowledge helps hunters turn broad adversary behaviors into concrete, observable search ideas. The useful level is specific enough to map to telemetry and distinguish suspicious patterns from the large amount of legitimate activity that may use the same mechanism.

#### Connect to What You Already Know

The framework-application lesson showed how ATT&CK and other models can structure a hunt. This subunit applies that thinking to technique families that frequently produce huntable host evidence.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **3.6.1 – Persistence** | Recognize persistence mechanisms and narrow them into observable patterns suitable for hunting. |
| **3.6.2 – Privilege Escalation** | Recognize privilege-escalation behaviors and the host context needed to search for them meaningfully. |
| **3.6.3 – Hunt-Specific Technique Development** | Turn a named technique into a unique pattern, bounded scope, and evidence-backed hunt line. |

#### What to Watch For

- Move from a broad tactic or technique name to a concrete observable pattern.
- Use environment and baseline context to distinguish common administrative behavior from a hunt-worthy pattern.
- Keep the hunt scope narrow enough that the result answers a question rather than producing an unbounded list of matches.

#### Expected End State

By the end of this subunit, you should be able to:

- identify concrete persistence and privilege-escalation behaviors that can produce hunt leads;
- translate a technique into a specific observable pattern and telemetry requirement;
- bound the search by scope, time, assets, users, or other relevant context;
- explain why hunting an entire tactic is usually less useful than testing a specific behavioral hypothesis.

#### How to Preview This Subunit

Read this introduction, then skim the [3.6 Summary](#36--attacker-techniques-for-hunting-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 3.6.1 — Persistence Techniques

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Recognize common Windows persistence mechanisms in host telemetry.
2. Identify the fields that demonstrate the mechanism while separating **technique recognition** from a judgment that the activity is malicious.

#### Key Concepts

Persistence is how an adversary maintains access or recurring execution across interruptions such as logon, reboot, process termination, or other changes in session state.

This lesson focuses on several Windows mechanisms hunters commonly encounter.

##### Registry Run keys and Startup Folder

MITRE ATT&CK: [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)

Useful evidence includes:

- exact registry path;
- value name;
- value data/target path;
- process/user that created or modified it;
- file metadata for the target.

A12:

> `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`  
> `Updater = %TEMP%\update.exe`

That supports **user-context persistence** because Windows can execute the referenced program at logon.

It does not, by itself, establish privilege escalation.

##### Scheduled Tasks

MITRE ATT&CK: [T1053.005 – Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)

Useful evidence includes:

- task name/path;
- trigger;
- action/command;
- principal/account;
- creator/modifier;
- creation/update time.

A scheduled task can be used for **Execution, Persistence, or Privilege Escalation** depending on how it is configured and used. Classification should follow the observed role.

##### Windows Services

MITRE ATT&CK: [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)

Useful evidence includes:

- service name;
- image path;
- start type;
- service account;
- creator/modifier;
- whether the binary/path is expected.

Services can support persistence and can also result in elevated execution when the necessary prerequisites are present.

##### Other recurring mechanisms

Examples include:

- WMI event subscriptions;
- logon scripts;
- Winlogon modifications;
- other boot/logon autostart locations.

Name the mechanism the telemetry supports rather than forcing every recurring execution into “Run key.”

##### Recognizing a technique does not mean declaring malware

Legitimate software uses persistence mechanisms every day.

A vendor updater in a known path can legitimately create an autorun.

Hunting asks what makes the instance suspicious:
- unusual creator;
- user-writable target;
- rare value/task/service name;
- unsigned or unexpected binary;
- timing around an incident;
- unexpected account or host population.

#### Knowledge Check

1. What fields make a Run-key persistence observation reviewable?
2. Why can a scheduled task map to more than one ATT&CK tactic?
3. Does a legitimate updater that creates a Run key stop being a persistence mechanism? Explain.

#### Summary

Recognize the mechanism first; judge suspiciousness second.

Registry autoruns, Startup folders, scheduled tasks, services, and other recurring mechanisms all need the fields that show **what will run, when, and under which context**.

#### References and Further Reading

- [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)
- [T1053.005 – Scheduled Task](https://attack.mitre.org/techniques/T1053/005/)
- [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)

### 3.6.2 — Privilege Escalation Techniques

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Recognize evidence that a process or actor obtained a higher security context than it previously had.
2. Distinguish the **elevation outcome** from the specific technique used to achieve it.

#### Key Concepts

Privilege escalation occurs when an actor obtains a higher level of effective privilege than the context it previously controlled.

Seeing a process run as **SYSTEM** may establish an elevated outcome. It does **not automatically tell you how the elevation happened**.

That method/evidence distinction is the core of this lesson.

##### UAC bypass

MITRE ATT&CK: [T1548.002 – Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)

Evidence should support the bypass mechanism—for example:

- use of an auto-elevated component;
- associated registry/protocol/COM abuse or other known bypass mechanism;
- high-integrity child/result;
- absence of normal consent where that matters to the technique.

`fodhelper.exe` followed by an elevated child can be suspicious, but the process name alone is not enough to prove a UAC bypass.

##### Access Token Manipulation

MITRE ATT&CK: [T1134 – Access Token Manipulation](https://attack.mitre.org/techniques/T1134/)

Useful evidence can include:

- token duplication or impersonation operations from EDR/API telemetry;
- source and target security contexts;
- creation of a process using a manipulated token;
- linkage to a privileged token source.

A user process followed by a SYSTEM child does **not by itself prove token theft**. It proves that the child ran in a higher context; the method remains unresolved until token-manipulation evidence supports it.

##### Windows Service abuse

MITRE ATT&CK: [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)

Services can execute as SYSTEM. If an adversary with sufficient rights creates/modifies a service and uses it to move from a lower effective context to SYSTEM, the service activity can contribute to privilege escalation.

Preserve:
- who created/modified it;
- image path;
- service account;
- resulting process context.

##### Exploitation for Privilege Escalation

MITRE ATT&CK: [T1068 – Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)

Evidence should connect:
- vulnerable component/driver or exploit behavior;
- exploitation activity;
- resulting higher privilege.

A SYSTEM process appearing after a crash or driver load is not enough by itself to name a specific exploit.

##### Outcome first, method second

A useful analytic sequence is:

1. What was the original security context?
2. What higher context appeared?
3. What telemetry explains **how** the transition occurred?
4. Is the technique specific enough to name, or is the method unresolved?

##### A12 boundary

The A12 HKCU Run value is evidence of user-context persistence. It does not establish a privilege change.

#### Knowledge Check

1. A user-context process launches a SYSTEM child. What can you say immediately, and what remains unresolved?
2. What additional evidence would help support Access Token Manipulation?
3. Why is `fodhelper.exe` alone insufficient to prove UAC bypass?

#### Summary

Recognize the privilege change, then require method-specific evidence before naming the escalation technique.

High privilege is an **outcome**. Token manipulation, UAC bypass, service abuse, and exploitation are **methods**.

#### References and Further Reading

- [T1548.002 – Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/)
- [T1134 – Access Token Manipulation](https://attack.mitre.org/techniques/T1134/)
- [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/)
- [T1068 – Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/)

### 3.6.3 — Hunt for a Specific Persistence or Privilege-Escalation Technique

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Turn one named persistence or privilege-escalation technique into a bounded, telemetry-backed hunt.
2. Distinguish the ATT&CK technique from the **procedure-level pattern** that makes the hunt selective.

#### Key Concepts

“Hunt persistence” is too broad.

A useful hunt names:

1. **Technique** – the behavioral category.
2. **Procedure/pattern** – what this threat actually did, or the behavior variant you intend to test.
3. **Scope** – population, time, telemetry.
4. **Expected evidence** – fields/events that would make a hit reviewable.

##### A12 Case Study: Worked Example

**Technique**
> [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)

**Relevant tactic/context**
> Persistence

**Observed procedure**
> HKCU Run value `Updater` → `%TEMP%\update.exe`

**Exact-observed hunt**
> Search user workstations for Run value `Updater` or the exact target path during the scoped window.

**Behavior-broadened hunt**
> Search for newly created/modified Run values that launch executables from user-writable Temp locations, then prioritize rare value names, unusual creators, unsigned files, and hosts related to A12.

The first search has high specificity but may miss variants.

The second can find variants but produces more benign candidates.

A mature hunt can use both layers.

##### Wrong-class avoidance

A task that runs as SYSTEM is not automatically “privilege escalation.” The hunt should require evidence that the actor moved from a lower context to a higher one and, if naming a specific escalation method, evidence supporting that method.

##### Hunt line

A concise hunt line can be:

> **T1547.001 / Persistence** — Windows user workstations, previous 14 days, registry + file telemetry; search exact `Updater → %TEMP%\update.exe` first, then broaden to rare Run values launching from user-writable Temp paths.

That hunt line is specific enough to **prepare an executable search**, but writing the line is not the same as executing the mapped task.

To demonstrate `3.6.3`, run both the exact-observed and behavior-broadened layers in [Practical E of the Hunt Execution Practical](#hunt-execution-practical--controlled-telemetry). Record the query/filter, returned hosts, benign near-neighbor, gaps, and bounded finding.

#### Knowledge Check

1. What is the difference between an ATT&CK technique and the procedure-level pattern used by the hunt?
2. What trade-off exists between exact-observed and behavior-broadened hunts?
3. Write an A12 T1547.001 hunt line with scope and telemetry.

#### Summary

Hunt one named technique through a procedure-level pattern.

Start exact when intelligence gives you exact evidence; broaden deliberately when you want variants. Keep the scope and required telemetry explicit.

#### References and Further Reading

- [T1547.001 – Registry Run Keys / Startup Folder](https://attack.mitre.org/techniques/T1547/001/)

### 3.6 – Attacker Techniques for Hunting: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Technique → concrete behavior → observable pattern → telemetry → bounded hunt line**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- identify concrete persistence and privilege-escalation behaviors that can produce hunt leads;
- translate a technique into a specific observable pattern and telemetry requirement;
- bound the search by scope, time, assets, users, or other relevant context;
- explain why hunting an entire tactic is usually less useful than testing a specific behavioral hypothesis.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **3.6.1 – Persistence** | Recognize persistence mechanisms and narrow them into observable patterns suitable for hunting. |
| **3.6.2 – Privilege Escalation** | Recognize privilege-escalation behaviors and the host context needed to search for them meaningfully. |
| **3.6.3 – Hunt-Specific Technique Development** | Turn a named technique into a unique pattern, bounded scope, and evidence-backed hunt line. |

#### Check Your Understanding

Ask yourself:

1. What information turns “hunt persistence” into a testable search idea?
2. Why can an administrative mechanism be useful to hunt without being inherently malicious?
3. What scope information helps keep a technique-based hunt interpretable?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **3.7 – Local Hunt Control and Outputs: Introduction**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 3.7 – Local Hunt Control and Outputs: Introduction

**Estimated Time:** 5–10 minutes

#### Why This Subunit Matters

A technically sound hunt still has to fit the organization’s control process. Hunters need to know how work is authorized or queued, where the investigation is documented, and how findings, gaps, and handoffs are delivered to the teams that act on them.

#### Connect to What You Already Know

The preceding hunt lessons established purpose, methodology, tools, CTI inputs, framework use, and technique development. This final subunit maps that generic hunt workflow to the local operating environment.

#### What You Will Learn

| Lesson | What it contributes |
|---|---|
| **3.7.1 – Hunt Control** | Identify how hunts are initiated, authorized, prioritized, tracked, and closed locally. |
| **3.7.2 – Hunt Documentation** | Document the question, scope, evidence, queries, results, gaps, and decisions so the work can be reviewed or continued. |
| **3.7.3 – Hunt Outputs** | Package findings, detection gaps, intelligence feedback, IR handoffs, and other outputs for the correct downstream owner. |

#### What to Watch For

- Use the organization’s actual control path rather than inventing a generic ticket or approval chain.
- Document enough evidence and reasoning that another hunter can reproduce or continue the work.
- Separate the hunt finding from the downstream action: IR, CTI, Detection Engineering, and other owners may each receive a different product from the same hunt.

#### Expected End State

By the end of this subunit, you should be able to:

- identify the local process used to initiate, authorize, track, and close hunts;
- document a hunt so its scope, evidence, queries, and conclusions are reviewable;
- route findings and gaps to the correct downstream owner;
- distinguish universal hunt tradecraft from site-specific control and documentation requirements.

#### How to Preview This Subunit

Read this introduction, then skim the [3.7 Summary](#37--local-hunt-control-and-outputs-summary). After that, scan the lesson headings, tables, emphasized terms, and callouts before reading the lessons closely.

Use the preview to predict how the lessons fit together. Return to the summary after the detailed reading and compare the expected end state with what you can now explain or do.

### 3.7.1 — Hunt Control and Lead Management

**Estimated Time:** 15–20 minutes

#### Learning Objectives

1. Locate the site's authoritative process for initiating, controlling, pausing/stopping, and changing the scope of a hunt.
2. Explain how out-of-scope hunt leads are recorded, triaged, and assigned locally.

#### Key Concepts

The hunt methodology learned in 3.2 tells you **how to formulate a hunt**.

This module asks:

> How does this organization authorize and govern one?

Those answers are local.

##### Build the local governance map

| Question | Local answer |
|---|---|
| Who may initiate a hunt? | ______ |
| What prerequisites/approval are required? | ______ |
| Where is the hunt opened/tracked? | ______ |
| Who can expand or narrow scope? | ______ |
| Who can pause/stop a hunt? | ______ |
| What triggers escalation to incident response? | ______ |
| Where do out-of-scope leads go? | ______ |
| Who owns lead triage/deduplication? | ______ |

The blanks are filled from the real shop process.

##### Why hunt control matters

A query can affect:

- analyst time;
- search infrastructure;
- regulated/sensitive data;
- live incident handling;
- other teams' workload.

A scope change from 50 user workstations to the entire enterprise may be operationally significant even when the query itself is harmless.

##### Lead management prevents uncontrolled scope growth

A hunt often discovers something interesting that does not answer the current hypothesis.

Instead of silently expanding the hunt forever:

1. record the lead;
2. preserve why it matters and the evidence/source;
3. follow the local triage/ownership process;
4. decide whether it becomes a follow-on hunt, CTI question, detection task, or incident lead.

##### Missing local process

Use an explicit onboarding status:

> **Local hunt-governance path not yet verified.**

Then identify the missing owner/source.

That is actionable because it tells the team what still needs to be learned.

#### Knowledge Check

1. Why might expanding a hunt's scope require local authorization?
2. What should happen to an interesting finding that is outside the current hunt scope?
3. What should you record if the local hunt-control process has not been provided?

#### Summary

Local hunt control defines how hunts become official, how scope changes are governed, and how follow-on leads are managed.

Learn the authoritative process and use it.

#### Reference Model

This module intentionally relies on the organization's local hunt-governance process.

### 3.7.2 — Hunt Documentation Standards

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Locate the local hunt documentation standard and authoritative repository.
2. Document a hunt using the required local fields, evidence/query retention rules, and versioning method.

#### Key Concepts

The 3.2.2 hunt card teaches the **reasoning needed to develop a hunt**.

The organization's hunt record answers a different question:

> What must be preserved so another analyst can understand, reproduce, review, and close this hunt here?

##### Learn the local documentation map

| Question | Local answer |
|---|---|
| What fields are mandatory? | ______ |
| Where is the authoritative hunt record stored? | ______ |
| How are hypothesis/scope changes recorded? | ______ |
| How are queries or notebooks retained? | ______ |
| What evidence/results must be attached or linked? | ______ |
| How are data sources and time windows recorded? | ______ |
| How are gaps and limitations captured? | ______ |
| How are revisions/version history handled? | ______ |
| What status/closure fields are required? | ______ |

These are orientation questions, not a substitute template.

##### Reproducibility matters

A future analyst should be able to answer:

- What was the hypothesis?
- What population and time window were searched?
- Which telemetry was available?
- Which query/version was run?
- What exclusions or filters were applied?
- What findings were reviewed?
- What limitations affect the result?

A screenshot of a dashboard rarely provides all of that.

##### Separate scratch work from the official record

Personal notes can help an analyst think. The local standard decides what must become part of the authoritative hunt record.

The official record should preserve enough evidence and reasoning to support:
- review;
- hand-off;
- follow-on hunting;
- detection engineering;
- later lessons learned.

##### Missing standard

Use:

> **Local hunt documentation standard not yet verified.**

Then identify the missing repository/form/process owner.

#### Knowledge Check

1. How does the 3.2.2 hunt card differ from the local official hunt record?
2. Name four things that support reproducibility.
3. What should you record if you do not know the authoritative hunt repository?

#### Summary

Document hunts where the organization says the authoritative record lives.

Preserve the hypothesis, scope, telemetry, query/evidence, findings, limitations, and version history required by the local standard.

#### Reference Model

This module intentionally relies on the organization's local hunt documentation and records standard.

### 3.7.3 — Hunt Outputs and Hand-off

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Locate the site's definition of a complete hunt output and the local hand-off map.
2. Produce the required package and route each finding to the locally authorized consumer.

#### Key Concepts

A hunt is not complete merely because the query finished.

The organization decides what the finished hunt must contain and which teams receive which outcomes.

##### Common output categories

A local output standard may require some combination of:

- hypothesis and scope;
- queries/data sources used;
- findings and affected hosts/accounts;
- evidence and confidence/limitations;
- **detection gaps**;
- **visibility gaps**;
- reusable search logic;
- follow-on hunt leads;
- recommended hand-offs or actions.

These are examples, not a universal local checklist.

##### Findings can require different consumers

A useful hand-off map may distinguish outcomes such as:

| Finding type | Possible consumer category |
|---|---|
| Active/suspected compromise | SOC / IR |
| Detection coverage gap | Detection engineering or equivalent |
| New infrastructure / intelligence question | CTI |
| Missing telemetry | Telemetry/platform owner |
| Out-of-scope investigative lead | Local lead-management process |

The actual team names, queues, and approval paths are site-specific.

##### Preserve the evidence boundary

A hunt package should make clear:

- what was observed;
- what was inferred;
- what scope was searched;
- what telemetry was unavailable;
- whether additional hosts were found;
- whether a negative result is limited by visibility.

##### Hypothetical A12-based output example

Canonical A12 does **not** specify the completed hunt result. The following is a **practice-only extension based on A12 behavior**; the host counts, visibility gap, detection gap, and follow-on lead are exercise conditions rather than canonical A12 facts.

A finished practice hunt might report:

- 2 additional hosts with the exact `Updater → %TEMP%\update.exe` persistence pattern;
- 18 hosts searched with complete registry visibility;
- 7 hosts without the required registry telemetry;
- no existing analytic covering the exact pattern;
- a follow-on lead involving a different Run-value name pointing to a user-writable path.

The **practice results** remain the same regardless of which local team receives each part. The local hand-off map determines who owns response, detection improvement, visibility remediation, and follow-on intelligence.

##### Missing local list/map

Use:

> **Local hunt output requirements / hand-off path not yet verified.**

Then identify the owner/source needed to close that onboarding gap.

#### Knowledge Check

1. Why is “the query finished” not enough to call the hunt complete?
2. Which two gap types should a hunt output distinguish?
3. A hunt finds active compromise, a detection gap, and missing registry telemetry. Why might those outcomes have different consumers?

#### Summary

A finished hunt communicates findings, scope, evidence, gaps, and follow-on work in the form required locally.

Then route each outcome through the organization's authorized hand-off map.

This completes the **3.7 local hunt operations subunit**.

#### Reference Model

This module intentionally relies on the organization's local hunt-output and hand-off standard.

### 3.7 – Local Hunt Control and Outputs: Summary

**Estimated Time:** 5–10 minutes

#### What This Subunit Built

**Hunt question → local control → documented execution → finding/gap → handoff and closure**.

The purpose of this summary is to help you check whether the individual lessons have combined into a usable mental model rather than a list of separate facts.

#### By This Point, You Should Be Able To

- identify the local process used to initiate, authorize, track, and close hunts;
- document a hunt so its scope, evidence, queries, and conclusions are reviewable;
- route findings and gaps to the correct downstream owner;
- distinguish universal hunt tradecraft from site-specific control and documentation requirements.

#### How the Pieces Fit Together

| Lesson | Role in the larger model |
|---|---|
| **3.7.1 – Hunt Control** | Identify how hunts are initiated, authorized, prioritized, tracked, and closed locally. |
| **3.7.2 – Hunt Documentation** | Document the question, scope, evidence, queries, results, gaps, and decisions so the work can be reviewed or continued. |
| **3.7.3 – Hunt Outputs** | Package findings, detection gaps, intelligence feedback, IR handoffs, and other outputs for the correct downstream owner. |

#### Check Your Understanding

Ask yourself:

1. Where does your organization record who authorized or prioritized a hunt?
2. What information must be documented so another hunter can reproduce the work?
3. How can one hunt produce separate outputs for IR, CTI, and Detection Engineering?

If you can answer those questions clearly and explain the reasoning behind your answers, you have the mental model this subunit is intended to build.

#### Where This Leads Next

The next learning unit is **3.8 – Threat Hunting Section Summary**. Carry the model from this subunit forward rather than treating the boundary as a reset; later lessons will reuse the evidence, terminology, and decisions introduced here.

### 3.8 — Threat Hunting Section Summary

**Estimated Time:** 15–20 minutes  

#### Purpose

Module 3.0 introduced threat hunting as a bounded analytical loop:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

Module 3.8 closes that loop.

By this point, you have learned why hunting exists, how different hunts begin, how to develop a hunt, how CTI and external research become hunt inputs, how ATT&CK supports planning, how to hunt specific techniques, and how a finished hunt is documented and routed.

This summary reconnects the pieces into one defensible hunt process.

#### What You Can Now Do

You should now be able to:

- explain why hunting exists alongside alerting and incident response;
- distinguish an intel-driven, hypothesis-driven, reactive, and anomaly-based starting signal;
- turn a topic into a testable hypothesis;
- define population, time window, telemetry, exclusions, and priority;
- identify a distinctive behavior or artifact worth searching;
- use external research and CTI to sharpen an internal search;
- distinguish a CTI lead from proof of local occurrence;
- use ATT&CK to organize behavior without allowing the framework to replace the hunt question;
- recognize persistence and privilege-escalation evidence without overstating the technique used;
- document the search so another hunter can understand or reproduce it;
- separate findings, detection gaps, visibility gaps, and follow-on leads;
- hand different outcomes to the correct downstream owner.

The important skill is not running a large number of queries.

It is producing a bounded answer that another defender can understand and act on.

#### The 3.x Block at a Glance

| Unit | Core skill retained |
|---|---|
| **3.1 – Purpose** | Explain why hunting searches beyond what existing alerts have already surfaced. |
| **3.2 – Methodology** | Convert a starting signal into a hypothesis, scope, priority, and distinctive search pattern. |
| **3.3 – Online Tools** | Use external evidence to sharpen leads and build an internal query plan. |
| **3.4 – CTI for Hunters** | Assess intelligence for hunt value and extract behaviors, indicators, procedures, and structured inputs. |
| **3.5 – Framework Application** | Use ATT&CK to organize the behavior and support hunt planning without replacing the evidence. |
| **3.6 – Attacker Techniques** | Translate technique knowledge into specific huntable observations while preserving method/evidence boundaries. |
| **3.7 – Site-Specific Operations** | Follow the local process for hunt control, documentation, completion, and handoff. |

Together, these units answer one question:

> **How do we search deliberately for relevant activity that existing controls have not already answered well enough?**

#### A12 End to End

The A12 scenario can show the entire hunt workflow.

##### Step 1 – Starting signal

The original incident identified suspicious activity on `WS-JLEE`.

Available evidence included:
- encoded PowerShell;
- a request for `/update.exe`;
- a Run-key persistence pattern such as `Updater → %TEMP%\update.exe`.

The incident creates a reasonable hunt question:

> **Are there additional Windows workstations with the same or closely related persistence behavior?**

This is primarily a **reactive** starting signal because an active/known incident created the need to determine wider scope.

The hunt may still use CTI and a formal hypothesis. The course labels describe the primary starting signal, not mutually exclusive boxes.

##### Step 2 – Hypothesis

Turn the question into an expectation:

> If A12-style persistence exists on additional managed Windows user workstations, we expect to observe Run-key values pointing to `update.exe` or closely related payloads in user-writable paths.

That statement can be supported or fail to be supported by evidence.

##### Step 3 – Scope

Define what the result will actually mean.

Example:

- **Population:** managed Windows user workstations
- **Window:** previous 14 days
- **Telemetry:** registry modification plus process/file telemetry
- **Important exclusions:** approved updater/software-management patterns where known

A negative result is only meaningful for systems and time periods where the required telemetry is available.

##### Step 4 – Search pattern

Start with the distinctive behavior.

Examples:

- Run-key modification;
- target path in `%TEMP%` or another user-writable location;
- value or filename relationship;
- related process/file context.

Do not assume the exact value name is the only possible variant.

Use exact artifacts when useful, then expand carefully into behavioral relationships.

##### Step 5 – CTI and external research

CTI or an external platform may provide:
- related hashes;
- infrastructure;
- filenames;
- process behavior;
- registry artifacts;
- additional procedures.

Those findings sharpen the hunt.

They do **not** prove that the same artifact or behavior occurred internally.

The hunter still needs local evidence.

##### Step 6 – ATT&CK and technique reasoning

The Run-key pattern can be mapped to the appropriate ATT&CK technique when the observed behavior supports it.

Keep three levels separate:

- **Technique:** the ATT&CK behavior category
- **Procedure:** how the activity was carried out in this case
- **Local observation:** the specific registry/process/file evidence you actually saw

The framework helps organize the hunt. It does not replace the hypothesis or evidence.

##### Step 7 – Refine the candidates

Suppose the first query returns many Run-key entries.

Refine using context such as:
- target path;
- filename;
- signer;
- parent/process relationship;
- timing;
- known-good software.

The goal is to reduce the candidate set without filtering away the behavior you are trying to find.

##### Step 8 – Findings

The canonical A12 story does not specify the hunt outcome. For practice, suppose a hunt produced the following result:

- 2 additional hosts show the exact `Updater → %TEMP%\update.exe` pattern;
- 3 other hosts show related Run-key behavior needing review;
- 18 hosts were searched with complete required telemetry;
- 7 hosts lack the registry telemetry needed to test the hypothesis;
- no current analytic appears to cover the exact behavior.

This produces several different findings.

##### Step 9 – Handoff

The hunt does not have to solve every downstream problem itself.

Possible routing:

| Finding | Downstream owner category |
|---|---|
| Additional affected hosts | SOC / Incident Response |
| No existing analytic for the behavior | Detection Engineering |
| Missing registry telemetry | Telemetry / platform owner |
| New infrastructure or intelligence question | CTI |
| Related unexplained pattern | Follow-on hunt / lead-management process |

The actual local team names and queues come from the site's hunt-governance process.

#### Distinctions That Keep a Hunt Reviewable

Hunting combines intelligence, hypotheses, telemetry, and search logic. The concepts below stay useful when each one is tied to the question it is meant to answer.

##### Hunt type describes the starting signal, not the whole design

**Reactive**, **intel-driven**, **hypothesis-driven**, and **anomaly-based** describe how a hunt primarily begins.

Regardless of the starting signal, a reviewable hunt still needs a testable question, bounded scope, required telemetry, search logic, and a documented result.

##### A topic becomes a hypothesis when it predicts evidence

> Hunt persistence

names an area of interest.

> If A12-style persistence exists elsewhere, we expect to observe Run values pointing into user-writable paths

creates an expectation that can be tested. The second form tells the hunter what evidence would support or weaken the idea.

##### CTI creates a lead; local telemetry establishes local occurrence

A sandbox observation, passive-DNS result, indicator, or STIX object can give the hunter a reason to search. It does not establish that the activity occurred inside the organization.

The hunt connects the external lead to local evidence within a defined population and time window.

##### Indicators and behaviors support different kinds of searching

An exact hash, domain, or IP can provide a precise match. A behavior or procedure can survive infrastructure or file changes and support a broader search.

Good hunts often use both: exact artifacts for precision and behavior for durability.

##### ATT&CK names the technique; the hunt needs the observable procedure

ATT&CK gives the team a shared behavior category. The hunt still needs the specific procedure, fields, and telemetry pattern that can be tested locally.

Technique mapping helps organize the question; the procedure makes it searchable.

##### Detection gaps and visibility gaps require different fixes

A **detection gap** exists when the required telemetry is available but current analytics do not adequately cover the behavior.

A **visibility gap** exists when the telemetry needed to test or detect the behavior is absent or insufficient.

The first points toward analytic coverage. The second points toward collection, ingestion, parsing, or population coverage.

##### Unalerted activity becomes a false negative only when an expected detector failed

The absence of an alert can reveal a coverage question, but a confirmed false negative requires an established expectation that a control should have detected the target condition and evidence that the required telemetry reached that control.

This prevents the hunt from labeling every previously unalerted finding as a detection failure.

##### A privileged outcome does not identify the privilege-escalation method by itself

Observing a process running as SYSTEM can establish a high-privilege state when the context supports that comparison. Identifying token theft, UAC bypass, or another specific escalation method requires evidence of how that state was reached.

##### A negative hunt result is bounded by what was actually tested

A defensible result says:

> **Not found within the tested population, time window, and available telemetry.**

That statement preserves the scope of the search. It does not imply that the activity cannot exist elsewhere in the enterprise or outside the observable period.

#### Integrated Review Exercise

Use this **hypothetical practice card based on A12 behavior**. These results extend the case for the exercise and are not canonical A12 outcomes:

> **Seed:** A12 incident  
> **Known behavior:** Run-key persistence pointing to `%TEMP%\update.exe`  
> **Population:** managed Windows user workstations  
> **Window:** 14 days  
> **Telemetry:** registry + process/file events  
> **Results:** 2 exact matches, 3 related candidates, 18 fully visible hosts, 7 hosts missing registry telemetry, no known analytic covering the exact pattern

Write a short hunt summary using:

##### Hunt question
What are you trying to determine?

##### Hypothesis
What evidence should exist if the behavior is present?

##### Scope
Which population, time window, and telemetry were tested?

##### Findings
What did the hunt actually observe?

##### Limitations
What could the hunt not determine?

##### Gaps
Which findings are detection gaps versus visibility gaps?

##### Handoff
Which outcomes belong to SOC/IR, DE, CTI, telemetry owners, or follow-on hunting?

A strong answer should make the boundaries of the conclusion obvious.

#### Threat-Hunting Readiness Checklist

Before moving into 4.x, you should be comfortable saying:

- [ ] I can explain why hunting exists alongside alerts and incident response.
- [ ] I can identify the primary starting signal for a hunt without treating hunt types as rigid boxes.
- [ ] I can turn a topic into a testable hypothesis.
- [ ] I can define population, time window, telemetry, and important exclusions.
- [ ] I can identify a distinctive pattern worth searching.
- [ ] I can turn CTI or external research into an internal query plan.
- [ ] I can distinguish external intelligence from local evidence.
- [ ] I can use ATT&CK to organize behavior without replacing the hypothesis.
- [ ] I can preserve the difference between a technique and the observed procedure.
- [ ] I can distinguish detection gaps, visibility gaps, and possible false negatives.
- [ ] I can write a negative result that is bounded by scope and visibility.
- [ ] I can document the hunt so another hunter can understand what was tested.
- [ ] I can route different findings to different downstream owners.

If one of these is weak, return to the corresponding 3.x unit before moving forward.

#### Bridge Into 4.x Detection Engineering

A hunt can discover activity, but some findings are really questions about **durable coverage**.

For example:

> We can find this A12 persistence behavior manually.  
> Should the organization detect it automatically in the future?

That is where Detection Engineering enters.

The hunter provides:
- the observed behavior;
- evidence;
- scope;
- useful search logic;
- benign context;
- limitations.

Detection Engineering determines whether to:
- reuse existing coverage;
- modify an existing analytic;
- create new coverage;
- or decide that another control is more appropriate.

The hunt identifies defensive knowledge.

DE turns appropriate knowledge into maintained detection capability.

#### Summary

The 3.x block taught one complete hunt loop:

**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

A defensible hunt tells the reader:
- what was tested;
- where and when it was tested;
- what evidence was available;
- what was found;
- what could not be seen;
- what should happen next.

Keep one principle with you into 4.x:

> **A hunt result is only as broad as the scope and visibility that produced it.**

## Part V — Detection Engineering

Investigation and hunting can reveal a need for better coverage. Detection Engineering evaluates that need and maintains the resulting capability through **Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**. The decision may be to change existing coverage, add coverage, or explain why no new rule is justified.

> **A12 Case Study:** Follow the evidence available at this stage of the case. The uninterrupted narrative appears in [Appendix A](#appendix-a--the-complete-a12-case-study).

### 4.0 — Detection Engineering: How the 4.x Block Fits Together

**Estimated Time:** 10–15 minutes  

#### Learning Objectives

By the end of this introduction, you will be able to:

1. Explain the purpose of the 4.x Detection Engineering block and how its eight units fit together.
2. Follow the detection lifecycle from a defensive need to maintained production coverage.
3. Explain why a detection is more than rule syntax and why its effectiveness depends on both logic and telemetry.

#### What the Detection Engineering Block Is Building Toward

Detection Engineering turns recurring defensive needs into **maintained detection capability**.

A SOC analyst may notice a noisy alert.  
A threat hunter may discover behavior that no analytic covers.  
CTI may identify a procedure worth monitoring.  
An existing analytic may stop working because the data changed.

Detection Engineering takes those needs and decides what durable coverage should exist.

A simple mental model for the 4.x block is:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

The goal is not simply to write a query.

The goal is to maintain a detection that:
- addresses a real defensive need;
- uses telemetry that actually exists;
- behaves as intended;
- reaches production through the local process;
- remains useful as the environment changes.

#### The Eight Units

| Unit | Main question | What you learn |
|---|---|---|
| **4.1 – What DE Owns** | Which work belongs to Detection Engineering? | Detection lifecycle ownership, nominations, rule-authoring boundaries, and enforcement/control ownership |
| **4.2 – Sound Detections** | How do we know the analytic is actually good? | Logic, data requirements, positive testing, benign controls, and validation |
| **4.3 – Nominations** | How does new detection work enter the lifecycle? | Turning SOC, hunt, and CTI needs into reviewable DE inputs |
| **4.4 – Tune Requests** | What do we do when a live analytic needs attention? | Tune, exception, replace, leave, or retire decisions |
| **4.5 – Hunt and Intel Packages** | How do findings become coverage decisions? | Reuse existing coverage, modify it, or create new detection work |
| **4.6 – Detection Lifecycle** | How does coverage stay useful over time? | Deployment, monitoring, maintenance, change, replacement, and retirement |
| **4.7 – Sensors and Data** | Can the detection actually see what it needs? | Collection, ingestion, parsing, population coverage, timeliness, and logic dependencies |
| **4.8 – Site-Specific DE** | How does this organization run DE in production? | Local requirements, review, approval, deployment, rollback, and authoritative repositories |

Each unit addresses a different part of the same lifecycle.

#### Start With the Defensive Need

Detection work should begin with a problem worth solving.

For the A12 scenario:

> **We need durable visibility for encoded PowerShell behavior similar to what occurred on `WS-JLEE`.**

That is enough to begin DE review.

The nominator does not need to arrive with:
- a production-ready Sigma rule;
- a final KQL query;
- the exact exclusion list;
- deployment instructions.

Those are engineering decisions.

The first DE question is:

> **What behavior needs coverage, and do we already cover it adequately?**

#### Reuse Coverage Before Creating More

A new rule is only one possible answer.

When a nomination arrives, DE should consider:

1. Does an existing analytic already cover this behavior?
2. Could an existing analytic be safely expanded or tuned?
3. Is a new analytic justified?
4. Is the need better handled by another control or workflow?
5. Is the required telemetry even available?

This prevents the detection library from becoming a pile of overlapping rules that all try to solve the same problem.

#### A Rule Is Not Yet a Detection Capability

Writing valid syntax is only one step.

A production detection also needs evidence that:

- the target behavior causes the analytic to match;
- representative benign activity does not match unnecessarily;
- required fields and telemetry are present;
- the analytic works on the intended population;
- changes and exclusions do not remove the target behavior;
- the rule can be maintained after deployment.

That is why 4.x follows the 1.3 rule lessons rather than duplicating them.

**1.3** teaches how rules work.

**4.x** teaches how detections are operated as a capability.

#### Validation Tests Both Logic and Data

Suppose DE builds an analytic for encoded PowerShell.

A useful validation asks:

##### Positive test

> Does known target behavior match?

##### Benign-control test

> Does representative normal PowerShell activity remain outside the detection when appropriate?

##### Data test

> Does the production data path actually provide the process and command-line fields the analytic expects?

A rule can be perfectly written and still be ineffective if the required data is absent or mapped differently.

#### Deployment Is Not the End

A detection changes once it enters production.

You may discover:
- benign software generates large alert volume;
- adversary behavior changes;
- field mappings change;
- a sensor stops covering part of the population;
- another analytic makes the old one redundant;
- a narrow exception suppresses something it should not.

That is why the lifecycle continues:

**Deploy → Monitor → Tune/Change → Revalidate → Replace/Retire when appropriate**

A detection that nobody maintains is not durable coverage.

#### A Silent Detection Has More Than One Possible Explanation

If a rule does not fire, several explanations are possible:

- the target behavior did not occur;
- the logic does not match it;
- the event was not collected;
- the event never reached the platform;
- parsing changed;
- the required field is empty;
- the relevant host population is not covered;
- the event arrived outside the analytic's time window.

The engineer therefore asks:

> **Did the behavior occur, did the data arrive correctly, and would the logic match that data?**

This prevents a silent rule from being interpreted automatically as proof that the environment is clean.

#### Detection Engineering Has Adjacent Owners

Detection Engineering works closely with:
- SOC;
- threat hunting;
- CTI;
- telemetry/platform owners;
- incident response;
- control/enforcement owners.

The course keeps those responsibilities visible.

For example:

> **Create durable analytic coverage** → Detection Engineering

> **Investigate this host** → SOC / IR

> **Block this IP at the firewall** → locally authorized enforcement/control owner

> **Fix missing process telemetry** → telemetry/platform owner

The exact team names and approval paths are local and are taught in 4.8.

#### Hypothetical A12-Based Detection Lifecycle

Canonical A12 reaches a **Detection Engineering coverage review**. It does **not** specify whether DE builds or changes an analytic, validates it, deploys it, monitors it, or later retires it.

The sequence below is a **hypothetical practice extension based on A12 behavior** so you can see the complete 4.x lifecycle without turning those downstream steps into A12 facts.

##### Need

For this practice extension, assume hunting reports recurring encoded PowerShell and a persistence pattern. That assumed hunt result is an exercise condition, not a canonical A12 outcome.

##### Coverage Decision

DE checks whether existing analytics already cover the behavior.

##### Build / Change

DE creates or modifies the appropriate analytic.

##### Validate

Test:
- target behavior;
- benign controls;
- required data;
- intended host population.

##### Deploy

Use the local review, approval, and release process.

##### Monitor

Review alert quality, data health, and whether the analytic continues to provide the intended coverage.

##### Improve

Tune narrow benign conditions, update logic when behavior changes, or replace the analytic when a better design exists.

##### Retire

Remove or supersede the analytic when it no longer provides enough value.

That is a complete **practice** detection-engineering story. The canonical A12 case still stops at coverage review.

#### What You Need to Remember Before 4.1

You do not need to know every rule format, deployment pipeline, or local approval process yet.

Remember the lifecycle:

> **Start with the need.**  
> **Decide what coverage should exist.**  
> **Build or change the analytic.**  
> **Validate the behavior and the data.**  
> **Deploy through the local process.**  
> **Monitor and maintain it.**  
> **Replace or retire it when that becomes the better defensive choice.**

#### Orientation Check

1. Why is a syntactically valid rule not automatically a production-ready detection?
2. A hunter provides a strong behavior description but no rule. Can DE begin work from that?
3. A detection does not fire during a replay. Name two explanations other than “the behavior did not happen.”
4. Why might DE modify or reuse an existing analytic instead of creating a new one?

#### Summary

The 4.x block teaches the full lifecycle of **maintained detection capability**:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

Detection Engineering is not only rule authoring. It connects defensive needs to reliable, tested, maintainable coverage—and keeps that coverage working as behavior, telemetry, and the environment change.

### 4.1 — What Detection Engineering Owns

**Estimated Time:** 15–20 minutes

#### Learning Objectives

By the end of this module, you will be able to:

1. Explain what Detection Engineering owns across the lifecycle of a detection.
2. Route a piece of work to **DE**, a **nominator**, **rule-authoring instruction (1.3)**, or the locally authorized **enforcement/control owner**.

#### Key Concepts

Detection Engineering turns recurring defensive needs into **maintained detection capability**.

That is broader than writing a query. A detection only provides lasting value when someone owns what happens after the first draft: review, validation, deployment, tuning, change, health checks, and retirement.

For this course, DE owns the **detection lifecycle**:

- create or accept new detection work;
- change and tune existing detections;
- validate behavior and data requirements;
- deploy through the local process;
- maintain coverage as data and adversary behavior change;
- retire or replace detections that no longer provide value.

##### Four adjacent kinds of work

| Work | Primary responsibility in this course |
|---|---|
| **Detection lifecycle** | DE evaluates, validates, deploys, maintains, changes, and retires detection logic. |
| **Nomination** | SOC, hunt, or CTI identifies a need and gives DE enough context to review it. |
| **Rule-authoring mechanics (1.3)** | How a Sigma, SIEM, IDS, YARA, or other rule is expressed and interpreted. |
| **Enforcement / blocking / containment** | The locally authorized owner of firewall, EDR-prevention, isolation, or other control action. |

The fourth boundary is an **operating-model decision**, not a universal law. Some organizations give DE authority over prevention controls; others separate detection from enforcement. In this course, treat a request such as “block this IP at the firewall” as an enforcement request and route it to the authorized control owner unless the local policy says DE owns that action.

##### A nomination does not need to arrive production-ready

SOC, hunters, and CTI often see the defensive need before they know the final detection logic.

A useful nomination can begin as:

> We observed encoded PowerShell during A12 and want durable visibility for similar execution.

DE then evaluates:
- what behavior should be detected;
- which telemetry can support it;
- whether an existing analytic already covers it;
- what implementation and testing are required.

A rough nomination is not “bad DE work.” It is **input to DE work**.

##### Detection Engineering is not only syntax

Module 1.3 teaches how a rule works.

The 4.x track is about **operating detections as a capability**:
- intake;
- design;
- validation;
- deployment;
- monitoring;
- tuning;
- lifecycle decisions;
- feedback to the nominator.

That distinction prevents the team from treating a syntactically valid query as a finished detection.

##### A12 Case Study: Worked Examples

**“We need durable detection for encoded PowerShell similar to A12.”**  
→ **Nomination / DE lifecycle work**

**“How do I express this condition in Sigma?”**  
→ **1.3 rule-authoring mechanics**

**“This live analytic is firing on our backup process.”**  
→ **DE tune/change work**

**“Block `203.0.113.88` at the firewall.”**  
→ **Enforcement/control-owner request under the course operating model**

#### Knowledge Check

1. Why is Detection Engineering broader than writing a rule?
2. A hunter sends a rough behavior description with hunt evidence but no rule. Is that enough to enter DE review?
3. Why should “block this IP” be routed according to the local control-ownership model rather than treated automatically as a DE deployment?

#### Summary

Detection Engineering owns **maintained detection capability**, not just rule syntax.

SOC, hunt, and CTI can nominate work before the final analytic exists. DE turns the need into a validated, deployable, maintainable detection—or explains why a new detection is not the right answer.

Enforcement actions follow the organization's control-ownership model.

### 4.2 — Making a Detection Sound and Meeting Shop Requirements

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Define the behavior a detection should recognize and state **positive, negative, and data-availability test expectations** before deployment.
2. Check the actual local requirements list without confusing an external rule format with shop policy.
3. Close the loop with the nominator by recording the disposition and any important change to the original need.

#### Key Concepts

A detection is ready for production because its **behavior, data assumptions, and test results are understood**—not merely because the query parses.

For this course, a sound detection should answer three questions:

1. **What should match?**
2. **What similar activity should not match?**
3. **What data must exist for the analytic to work?**

##### Positive tests: what must fire

Use one or more known examples of the intended behavior.

For A12, if the analytic is designed around suspicious encoded PowerShell, a positive test should reproduce or safely emulate the relevant process/command behavior and verify that the detection matches the expected fields.

A positive test demonstrates:

> Under these test conditions, the analytic recognized the behavior it was designed to detect.

It does not prove that every future variation will be detected.

##### Negative tests: what must not fire

Test realistic benign or near-neighbor activity.

Examples:
- a sanctioned administration script;
- a backup process that resembles part of the malicious pattern;
- a legitimate PowerShell command without the suspicious combination the analytic requires.

The goal is not “zero false positives forever.” The goal is to understand the boundary between:
- intended detection;
- expected benign activity;
- acceptable review volume.

Sigma's documentation explicitly treats false-positive context and filters as part of detection engineering. See:
- [Sigma Rules – false positives and rule metadata](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)
- [Sigma Filters](https://sigmahq.io/docs/meta/)

##### Data-availability test: can the analytic actually see its inputs?

A correct logical condition still fails if the required data is missing, delayed, parsed differently, or absent on part of the environment.

Before deployment, verify:
- required log/event source exists;
- required fields are populated;
- field normalization matches the analytic;
- the intended host/user/network population is covered;
- the data arrives within the timeframe the analytic expects.

The Sigma log-source guidance illustrates the same principle: detection logic must be applied to the correct logs and fields. See [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html).

##### Test the behavior, not only the exact IOC

Behavior-focused validation is more durable than replaying one exact malicious value.

The Center for Threat-Informed Defense recommends continuous adversary emulation as a way to validate whether real adversary behaviors are observable and detected in the environment. See [CTID – Continuous Emulation as Detection Validation](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/).

That does not mean every rule needs a full red-team exercise. It means the test should represent the **behavioral claim** the detection is making.

##### Shop requirements are local

External formats can show common metadata categories, but they do not define your organization's deployment policy.

For example, Sigma supports fields such as IDs, status, description, references, log source, false-positive notes, level, and tags. See [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html).

Your shop may require some, all, or different fields.

At this point in the course, learn the method but do **not** pretend you already have the authoritative local list. Module 4.8 teaches you how to locate and verify that source.

After 4.8, return to [Part B of the Detection Validation Practical](#detection-validation-practical--draft-analytic-test) with the **verified local list** and mark:
- met;
- missing;
- not applicable, if the real local process permits it.

Until that local source is available, `4.2.2` is taught/prepared but not qualification-complete.

##### Close the loop

A close-the-loop note should tell the nominator what happened to the need.

Useful dispositions include:

- **Shipped** – detection deployed.
- **Changed** – the original idea was modified; explain the meaningful change.
- **Sent back** – additional information is needed.
- **Retired / superseded** – the work or existing analytic no longer remains active.

Example:

> **Changed:** We kept the encoded-PowerShell behavior but removed the host-specific IOC so the analytic can detect similar execution across workstations. Positive and benign-control tests passed. Deployment follows the local change path.

That feedback is more useful than simply writing “done.”

##### Demonstrate validation by running the draft

The three-test model above is preparation. Task `4.2.1` requires you to **test** a draft/change, so you must execute the analytic against controlled or approved evidence and evaluate the result.

Use the [Detection Validation Practical](#detection-validation-practical--draft-analytic-test). It supplies target behavior, benign near-neighbor behavior, and a deliberate data-path problem. Run the draft, preserve the output, and make a justified **PASS / CHANGE / FAIL-HOLD** decision.

#### Knowledge Check

1. What three categories of test expectation should be clear before deployment?
2. Why can a logically correct detection still fail operationally?
3. A Sigma field exists in the public specification. Does that automatically make it a mandatory local field?

#### Summary

Sound detection engineering tests the intended behavior, realistic non-target behavior, and the data path that makes the analytic possible.

External formats can inform design, but the organization's actual requirements list determines what is required locally.

Close the loop so the nominator knows whether the original defensive need was shipped, changed, sent back, or superseded.

#### References and Further Reading

- [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)
- [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)
- [Sigma Filters](https://sigmahq.io/docs/meta/)
- [Center for Threat-Informed Defense – Continuous Emulation as Detection Validation](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/)

#### Detection Validation Practical — Draft Analytic Test

**Purpose:** demonstrate `4.2.1` with an actual controlled test, then provide the handoff point for `4.2.2` after local onboarding in 4.8. This is a separate training scenario, not canonical A12.

##### Inputs

- [de-validation-practical.csv](#lab-asset--de-validation-practicalcsv)
- [de-validation-runner.py](#lab-asset--de-validation-runnerpy)

The draft analytic claims to detect suspicious encoded PowerShell launched by `wscript.exe`. The supplied runner implements **draft v1**. It is intentionally imperfect so the learner has evidence to evaluate rather than a guaranteed pass.

Run from the repository root or equivalent working directory, for example:

```bash
python labs/de-validation-runner.py labs/de-validation-practical.csv
```

Use an approved equivalent query environment if Python is not available. The requirement is to actually execute the draft logic against the controlled evidence, not merely inspect the rows.

##### Part A — Test the draft (`4.2.1`)

1. **Positive/intended behavior:** identify which supplied events are expected to match the behavioral claim.
2. **Benign near-neighbor:** verify that the approved deployment and non-encoded PowerShell cases do not match.
3. **Data path:** identify any event where required fields are missing or incomplete.
4. Run the draft and preserve the output.
5. Compare actual results with the expected classes.
6. Make one decision: **PASS**, **CHANGE**, or **FAIL / HOLD**. Justify it from the evidence.

A strong answer notices that a syntactically valid draft can still need change because a supported encoded-command variant is missed and because one sensor does not populate a required parent field.

###### Required validation record

Record:

- draft/version tested;
- exact command/query run;
- intended positive results;
- benign-control results;
- false positives / false negatives;
- data-path gaps;
- decision;
- specific change or scoping action, if needed.

##### Part B — Local requirement check (`4.2.2`)

Do **not** complete this part from fictional DYA/BHM policy. After 4.8, obtain the **verified local shop requirement list** or an authorized local simulation. Then mark each applicable requirement as met, missing, or not applicable if local policy allows that state.

Attach that checklist to the same validation record. If the real local list is unavailable, record an onboarding/qualification gap rather than inventing requirements.

##### Part C — Close the loop (`4.2.3`)

Write a short note to the nominator that states:

- disposition: shipped / changed / sent back / held / superseded, as appropriate;
- what changed from the original need;
- validation result and important limitation;
- next owner/action.

##### Evaluator criteria

For `4.2.1`, the evaluator should observe the learner actually execute the test and interpret the results. A satisfactory demonstration includes target, benign near-neighbor, and data-path evidence plus a justified pass/change/fail decision.

For `4.2.2`, qualification requires the verified **real local** requirements artifact or an authorized local simulation after 4.8. The training dataset cannot substitute for local policy.

At higher proficiency, expect the learner to isolate why a case was missed, propose a bounded rule/data-path correction, rerun where practical, and explain residual coverage limitations. Qualification/sign-off remains a separate evaluator action under the course standard.

##### Lab Asset — de-validation-practical.csv

Embedded from `/thraining-plan/labs/de-validation-practical.csv` for this controlled practical.

```csv
event_id,host,sensor,process,parent_process,command_line,telemetry_complete,expected_class,note
DV-001,BHM-WKS-07,EDR-A,powershell.exe,wscript.exe,powershell.exe -NoProfile -EncodedCommand JAB3AGM...,true,target_should_match,intended suspicious behavior with complete telemetry
DV-002,BHM-WKS-12,EDR-A,powershell.exe,ccmexec.exe,powershell.exe -NoProfile -EncodedCommand SQBUACA...,true,benign_should_not_match,approved software deployment near-neighbor
DV-003,BHM-WKS-15,EDR-A,powershell.exe,wscript.exe,powershell.exe Get-Process,true,benign_should_not_match,same parent/child but no encoded command
DV-004,BHM-WKS-21,EDR-B,powershell.exe,,powershell.exe -NoProfile -EncodedCommand JABjAGw...,false,target_data_gap,target-like behavior but parent_process missing on EDR-B
DV-005,BHM-WKS-25,EDR-A,cmd.exe,explorer.exe,cmd.exe /c whoami,true,irrelevant_should_not_match,unrelated command shell
DV-006,BHM-WKS-29,EDR-A,powershell.exe,wscript.exe,powershell.exe -NoP -enc JABlAG4...,true,target_should_match,encoded PowerShell using short -enc switch
```

##### Lab Asset — de-validation-runner.py

Embedded from `/thraining-plan/labs/de-validation-runner.py` for this controlled practical.

```python
#!/usr/bin/env python3
"""Controlled detection-validation runner for training only."""
import csv, sys

path = sys.argv[1] if len(sys.argv) > 1 else "de-validation-practical.csv"

def draft_detection(row):
    # Draft v1 intentionally recognizes only the long -EncodedCommand form.
    return (
        row["process"].lower() == "powershell.exe"
        and row["parent_process"].lower() == "wscript.exe"
        and "-encodedcommand" in row["command_line"].lower()
    )

rows = list(csv.DictReader(open(path, newline="")))
print("event_id expected actual telemetry result")
false_negatives = []
false_positives = []
data_gaps = []
for row in rows:
    actual = draft_detection(row)
    expected_target = row["expected_class"].startswith("target")
    if row["telemetry_complete"].lower() != "true":
        data_gaps.append(row["event_id"])
    if expected_target and not actual and row["telemetry_complete"].lower() == "true":
        false_negatives.append(row["event_id"])
    if (not expected_target) and actual:
        false_positives.append(row["event_id"])
    print(row["event_id"], row["expected_class"], "MATCH" if actual else "NO_MATCH", row["telemetry_complete"])

print("\nSummary")
print("false_negatives:", ", ".join(false_negatives) or "none")
print("false_positives:", ", ".join(false_positives) or "none")
print("data_path_gaps:", ", ".join(data_gaps) or "none")
```

### 4.3 — Nominations from SOC, Hunt, and CTI

**Estimated Time:** 15–20 minutes

#### Learning Objectives

1. Explain what makes a detection nomination **clear enough to review** without requiring the nominator to design the final analytic.
2. Review a nomination as **accept**, **send back**, or **reject/route elsewhere**, and state what the nominator still owes versus what DE will finish.

#### Key Concepts

A nomination is the point where another defensive function says:

> We have evidence of a recurring defensive need. Please evaluate whether detection engineering should address it.

SOC, hunt, and CTI can all nominate.

The nominator does **not** need to arrive with production-ready logic. DE is the team expected to turn a clear defensive need into a sound, maintainable analytic when a new detection is appropriate.

##### Minimum: need + evidence pointer

For this course, a nomination is clear enough to review when it names:

1. **The need** – what behavior or gap should be addressed.
2. **The evidence/context pointer** – where DE can inspect the case, hunt package, report, or other source that supports the need.

Helpful additional information may include:
- affected platform/population;
- representative event or observable;
- suspected ATT&CK technique;
- relevant telemetry;
- a draft rule, if the nominator already has one.

Those additions improve the handoff but are not a reason to force SOC, hunt, or CTI to perform DE's design work.

##### Three review outcomes

###### Accept for work

Use when the defensive need and supporting context are clear enough to evaluate.

Accept does not mean:

> We promise to deploy the nominator's exact idea.

It means DE owns the next engineering decision:
- reuse an existing detection;
- modify one;
- create a new one;
- determine that no durable analytic is justified.

###### Send back

Use when the request may belong to DE but the evidence is too incomplete to evaluate.

State exactly what is missing.

Example:

> Please add the hunt-package reference and one representative registry event showing the `Updater` value. The need is clear, but we cannot validate the required telemetry from the current nomination.

###### Reject / route elsewhere

Use when the request is not a detection-engineering need.

Examples:
- investigate this host;
- isolate this endpoint;
- block this IP;
- explain Sigma syntax for a training exercise.

Route it to the appropriate local owner rather than treating “reject” as “the problem does not matter.”

##### A12 Case Study: Worked Examples

**Nomination:**
> Need durable coverage for suspicious creation of HKCU Run values pointing into user-writable temporary paths. Evidence: A12 hunt package.

→ **Accept for work.**

**Nomination:**
> Need a detection for “something suspicious.” No case/report/hunt reference.

→ **Send back** for clearer need and evidence.

**Request:**
> Isolate `WS-JLEE`.

→ **Route to IR/containment owner**, not DE design work.

#### Knowledge Check

1. What two items are the minimum classroom bar for a reviewable nomination?
2. A hunt package states the need and contains representative evidence but no drafted rule. Accept or send back?
3. What is the difference between sending a nomination back and routing it elsewhere?

#### Summary

A nomination should be **clear enough to review**, not ready to deploy.

The nominator owes the defensive need and evidence/context. DE owns the engineering work that determines whether the right answer is a new analytic, a change, reuse of existing coverage, or no new rule.

### 4.4 — Tune Requests from SOC

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Review a SOC request concerning a **live detection** and choose **tune, exception/filter, replace, leave, or retire** with supporting evidence.
2. Distinguish detection-tuning work from investigation, containment, blocking, or other operational requests.

#### Key Concepts

A tune request begins with a detection that is **already live**.

SOC has operational evidence that something about the current analytic may need attention:
- excessive benign volume;
- a known blind spot;
- missing context;
- a pattern the current logic handles poorly;
- an old analytic that may no longer provide value.

That makes tuning different from a **new nomination**.

Whether the organization uses a separate queue, ticket type, or shared workflow is local. The important conceptual distinction is the **work type**, not the existence of a separate “inbox.”

##### A reviewable tune request

Useful inputs include:

- the live detection/rule ID or name;
- representative alert/case examples;
- the observed problem;
- what SOC believes should behave differently;
- a pointer to the investigation or case where the problem was observed.

If evidence is missing, send the request back with a precise ask.

##### Five engineering outcomes

| Outcome | Use when |
|---|---|
| **Tune** | Adjust logic while preserving the detection's purpose. |
| **Exception / filter** | Exclude a narrow, understood benign condition. |
| **Replace** | A different analytic design should supersede the live rule. |
| **Leave** | Evidence shows the rule is behaving as intended and the alert burden is justified. |
| **Retire** | The rule no longer provides enough value to remain active. |

##### Exceptions create blind spots if they are too broad

A filter should be as narrow as the benign condition permits.

After adding an exception, rerun the **positive test** from 4.2. A filter that removes the noise but also suppresses the malicious/target behavior is not a successful tune.

Sigma supports filters as a formal mechanism for excluding matching events, but a filter's existence does not make the exclusion safe. See [Sigma Filters](https://sigmahq.io/docs/meta/).

##### “Noisy” is evidence to investigate—not an automatic reason to disable

Ask:
- What benign population is producing the volume?
- Is the target behavior still valuable?
- Can the benign pattern be distinguished?
- Does the rule need broader redesign?
- Is the operational cost still justified?

A rule can be noisy and still deserve to remain active while DE works on a safer improvement.

##### Requests that are not tuning

**“Investigate why this host ran PowerShell.”**  
→ investigation workflow

**“Isolate this endpoint.”**  
→ IR/containment owner

**“Block this IP.”**  
→ enforcement/control owner

**“Create a new analytic for behavior we do not cover.”**  
→ nomination/new detection work

Route those requests instead of trying to turn them into tune outcomes.

#### Knowledge Check

1. What makes a tune request different from a nomination?
2. Why should an exception/filter be followed by a positive re-test?
3. SOC says “this rule is noisy; investigate the host.” Is that a tune request?

#### Summary

Tune requests use operational evidence from a **live detection**.

Choose tune, narrow exception, replace, leave, or retire based on what the evidence shows. Re-test after change, especially after adding exclusions.

Investigation, containment, and blocking are separate operational workflows.

#### References and Further Reading

- [Sigma Filters](https://sigmahq.io/docs/meta/)

### 4.5 — Hunt and Intel Packages

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Review a hunt or CTI package as engineering input and decide whether it supports **reuse**, **change**, **add**, or **no new rule**.
2. Separate durable detection opportunities from time-bounded indicators and enforcement/blocking actions.

#### Key Concepts

A hunt or CTI package is evidence and analysis that can inform Detection Engineering.

It is **not automatically a finished detection**.

DE's first question should be:

> What durable defensive capability, if any, does this package justify?

##### Start with existing coverage

Before creating a new analytic, determine whether the need is already covered.

Possible outcomes:

1. **Reuse existing coverage** – the package maps to an analytic that already addresses the behavior.
2. **Change existing coverage** – a live analytic is close but needs improvement.
3. **Add new coverage** – a meaningful gap exists and a new analytic is justified.
4. **No new rule** – the package is useful but does not justify a detection change.

The original task mapping groups this as add/change/no-new-rule; **reuse** is the check that can lead to “no new rule” because coverage already exists.

##### Package evidence can include several layers

A package may contain:
- observed procedures;
- ATT&CK techniques;
- IOCs;
- behavioral artifacts;
- affected platforms;
- scope and timing;
- hunt findings;
- known visibility gaps;
- supporting sources.

DE should use the **behavioral and environmental context**, not only the IOC list.

##### Exact indicators can be useful without being durable

A hash, domain, IP, or URL can support:
- retrospective search;
- short-lived monitoring;
- correlation;
- an enforcement action by the appropriate control owner.

But an exact IOC is not automatically a durable detection.

Ask:
- How long is this indicator likely to remain useful?
- Can the adversary rotate it easily?
- Does it reveal a more durable procedure?
- Is an existing behavioral analytic already stronger?

For A12, `203.0.113.88` may be useful as evidence or short-term context. A behavioral analytic around suspicious encoded PowerShell or unusual user-level autorun creation may survive infrastructure rotation better.

##### Route Infrastructure Findings According to the Defensive Need

A package may contain candidate related infrastructure.

That does not mean:
- every related IP/domain should become a detection rule;
- every candidate should be blocked;
- a shared cloud range should be treated as malicious.

Enforcement decisions go through the locally authorized control process.

Detection Engineering should focus on what the package says about **detectable behavior and defensible context**.

##### Feedback to the package producer

A useful DE response can say:

> **Change existing coverage:** The package's Run-key procedure is partially covered, but the current analytic does not distinguish user-writable payload paths. We will test a change around that behavioral condition. Exact infrastructure remains short-lived context rather than the primary detection logic.

That closes the loop and explains what DE learned from the package.

#### Knowledge Check

1. Why should DE check existing coverage before creating a new rule?
2. Does an exact IOC automatically deserve a durable detection?
3. A package contains a broad shared-hosting `/24`. Should DE convert the whole range into a detection or block list?

#### Summary

Treat hunt and CTI packages as **engineering input**.

Start with existing coverage, then decide whether to reuse, change, add, or make no detection change.

Use exact indicators when they are operationally useful, but prefer durable behavior when the evidence supports it. Enforcement/blocking follows the local control process.

### 4.6 — Detection Lifecycle

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Review a live detection and choose **modify, retire/replace, or leave** based on value, performance, data availability, and redundancy.
2. Evaluate whether an external block or control change actually removes the detection's remaining value.

#### Key Concepts

Detection lifecycle management asks a recurring question:

> Does this analytic still provide enough defensive value, with acceptable operational cost and valid data, to remain in its current form?

A live detection can become less useful because:
- adversary behavior changes;
- the data source changes;
- a replacement analytic provides better coverage;
- benign activity changes;
- the rule becomes redundant;
- a control prevents some of the activity;
- the original threat-specific context expires.

None of those conditions automatically tells you the answer. They trigger a review.

##### Three course decisions

| Decision | Meaning |
|---|---|
| **Modify** | Keep the capability, but change logic, data assumptions, context, or implementation. |
| **Retire / replace** | Remove this analytic from active use because a replacement or changed environment makes the old rule unnecessary/unsupported. |
| **Leave** | The current analytic remains useful and its operational burden is acceptable. |

##### Evaluate more than “is the threat still active?”

Useful review factors include:

- **Coverage value:** What meaningful behavior does the analytic detect?
- **Performance:** Is alert quality/volume acceptable?
- **Data health:** Are the required logs and fields still available?
- **Redundancy:** Does another analytic now provide equal or better coverage?
- **Durability:** Does the rule depend on a short-lived condition?
- **Operational cost:** Is the analyst burden proportionate to the value?
- **Replacement path:** If retiring, what coverage remains?

A campaign ending does not automatically make a behavioral detection obsolete if the behavior is useful across other threats.

##### Data-source change can mean modify—not immediate retirement

If the old sensor/log path disappears but equivalent evidence exists elsewhere, the right answer may be:

> Modify/migrate the analytic to the supported data source.

Retirement is appropriate when the detection can no longer operate and no replacement path justifies keeping it active.

##### Lifecycle status in rule formats is not your local lifecycle policy

Sigma defines rule-status values including `stable`, `test`, `experimental`, `deprecated`, and `unsupported`. See [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html).

Those values demonstrate that rules can have explicit lifecycle state, but your organization's production lifecycle may use different statuses and approvals.

##### A block does not automatically eliminate detection value

Suppose an IP is blocked at the firewall.

Ask:
- Does the detection recognize only that IP?
- Can the same behavior occur through other infrastructure?
- Does detecting attempted access still provide useful evidence?
- Does the block apply to every path/population?
- Is the rule useful for verifying attempted activity or control bypass?

If the analytic was only a one-to-one alert on that exact object and the object is permanently blocked everywhere, retirement may be reasonable.

If the analytic detects a broader behavior or can reveal attempts around the control, it may still earn its keep.

##### Document the reason

A lifecycle decision should be reproducible.

Examples:

> **Modify:** existing encoded-PowerShell analytic remains valuable, but the log schema changed and the field mapping must be updated.

> **Retire/replace:** old hash-only analytic is redundant with the new behavioral analytic and no longer adds useful coverage.

> **Leave:** rule continues to detect a meaningful behavior with acceptable alert quality; the associated IP block does not remove the broader detection value.

#### Knowledge Check

1. Why does “campaign ended” not automatically mean “retire the detection”?
2. A required log source disappears but equivalent telemetry now exists elsewhere. What lifecycle action may be appropriate?
3. An IP was blocked. Name two questions you should ask before retiring the matching analytic.

#### Summary

Lifecycle decisions balance **coverage value, performance, data, redundancy, durability, and operational cost**.

Modify when the capability still matters but needs change. Retire or replace when the analytic no longer earns its place. Leave it when it remains useful.

A block is one input to that decision—not an automatic retirement command.

#### References and Further Reading

- [Sigma Rules Specification – status and lifecycle metadata](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)

### 4.7 — Sensor and Data Availability for Detection

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Given “the detection never fired,” distinguish a **logic problem**, a **data-path problem**, a **coverage problem**, or a combination.
2. Explain why absent or unhealthy telemetry limits the conclusion you can draw from a silent detection.

#### Key Concepts

A detection can only evaluate evidence that reaches it in the expected form.

When a rule is silent, the problem may be:
- the target behavior did not occur;
- the analytic logic missed it;
- the required data was not collected;
- data was collected but not transported;
- parsing/normalization changed;
- required fields were empty;
- the analytic did not cover the relevant host/user/network population;
- data arrived too late for the analytic's time logic.

That is why **“no alert” is not enough to explain what happened.**

##### Think in a data path

A practical DE check moves through:

1. **Source / sensor** – was the underlying event recorded?
2. **Transport / ingestion** – did the event reach the platform?
3. **Parsing / normalization** – are the expected fields present and mapped?
4. **Coverage** – was the relevant host/user/network path actually monitored?
5. **Timeliness** – did the data arrive within the analytic window?
6. **Logic** – would the rule match the resulting event?

This is a troubleshooting model, not a requirement that DE administer every platform in the chain.

##### “Dead” and “blind” are useful shorthand but incomplete

A sensor may be:
- **down** – no data;
- **blind to the target population** – it is healthy but does not cover the needed host/path;
- **degraded** – data arrives partially or late;
- **semantically broken** – events arrive but required fields/parsing changed.

The last two cases matter because a dashboard can say “sensor healthy” while the analytic still cannot operate correctly.

##### Current ATT&CK terminology

MITRE ATT&CK changed its defensive model in **ATT&CK v18 (October 2025)**: the old **Data Sources** objects were deprecated, and ATT&CK now emphasizes **Detection Strategies** and platform-specific **Analytics** with explicit log-source information.

References:
- [MITRE ATT&CK – Analytics](https://attack.mitre.org/analytics/)
- [MITRE ATT&CK – Data Sources deprecation notice](https://attack.mitre.org/datasources/)

This course still uses the ordinary phrase **data source** in the generic engineering sense: the telemetry/log evidence a detection needs. Do not confuse that everyday phrase with ATT&CK's deprecated Data Source object type.

##### External rule requirements are data assumptions

Sigma log sources similarly express what type of logs an analytic expects. A mismatch can make a valid rule ineffective. See [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html).

The engineering skill is to connect:

> detection logic → required fields → required telemetry → covered population

##### A12 Case Study: Worked Example

Suppose the encoded-PowerShell analytic does not fire during a safe replay.

Check:

- Was process creation captured on the test host?
- Does the event include the expected command-line field?
- Did the pipeline parse that field under the name the rule expects?
- Did the event arrive in time?
- Does the analytic include that host population?
- Does the condition match the replayed command?

If process events never arrived, you have a **visibility/data-path problem**.

If the event is present with the required fields but the condition misses it, you have a **logic problem**.

If both are wrong, fix both.

##### Missing telemetry narrows the conclusion

If the endpoint sensor was absent for the relevant period, you can say:

> We lack the endpoint telemetry required to determine whether this analytic would have matched the activity on that host.

You cannot say:

> The activity did not happen.

That distinction protects later investigation and coverage reporting.

#### Knowledge Check

1. Name three places in the data path that can break a detection even when the rule logic is correct.
2. What is the difference between a healthy sensor and usable detection data?
3. ATT&CK deprecated its old Data Sources objects. Does that mean detection engineers no longer need to understand the telemetry their analytics depend on?

#### Summary

A silent detection can be a **behavior, logic, data, coverage, parsing, or timing** problem.

Trace the data path before concluding the rule failed—or that the activity never occurred.

Detection Engineering needs to understand telemetry dependencies even when another team administers the sensors and pipelines.

#### References and Further Reading

- [MITRE ATT&CK – Analytics](https://attack.mitre.org/analytics/)
- [MITRE ATT&CK – Data Sources deprecation notice](https://attack.mitre.org/datasources/)
- [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)

### 4.8 — Site-Specific Detection Engineering Knowledge

**Estimated Time:** 20–25 minutes

#### Learning Objectives

1. Locate and verify the organization's current detection requirements and production standards.
2. Map the local **review → test → approve → deploy → monitor → change/retire** path, including who owns each decision.
3. Follow the verified process and clearly identify any onboarding element that has not yet been obtained.

#### Key Concepts

The previous modules taught Detection Engineering tradecraft that transfers between organizations.

This module asks:

> **How does this organization actually run that work?**

The answer must come from the current local standards and process owners.

##### Part 1: the local detection requirements list

A mature local standard may address categories such as:
- required metadata;
- naming/ID conventions;
- ownership;
- references;
- ATT&CK mapping;
- severity/priority;
- required data sources;
- test evidence;
- known benign/false-positive context;
- runbook/triage guidance;
- version/change information.

Those are **examples of categories**, not a field list for DYA or your organization.

For comparison, public formats such as Sigma define their own metadata and rule-status fields. See [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html). Your local organization may adopt, extend, or ignore parts of that format.

What matters in this lesson is locating the **actual local list**.

##### Verify that the list is current

Capture:
- authoritative location;
- owner/maintainer;
- version/effective date;
- supersession or review cadence;
- which platforms/use cases it applies to.

A copied checklist with no owner or version may be useful background but is not enough to confidently describe current policy.

##### Complete the deferred 4.2.2 local-requirements demonstration

Module 4.2 taught the method for checking a detection against shop requirements, but it deliberately did not invent a local checklist. Now that you have located and verified the real requirements source, return to [Part B of the Detection Validation Practical](#detection-validation-practical--draft-analytic-test).

Using the same validation record from 4.2:

1. identify the authoritative local requirements source, owner, and version/effective date;
2. mark each applicable requirement **met**, **missing**, or the locally authorized equivalent;
3. cite the evidence for each status;
4. record any requirement you cannot evaluate because a local artifact, authority, or data source is still unavailable.

This is the practical demonstration for task `4.2.2`. If the verified local list is unavailable, record an onboarding/qualification gap rather than substituting Sigma fields or fictional DYA policy.

##### Part 2: the local lifecycle path

Map how a detection becomes official:

| Step | Local answer |
|---|---|
| Intake / nomination | ______ |
| Engineering owner | ______ |
| Test/staging method | ______ |
| Reviewer | ______ |
| Approval authority | ______ |
| Deployment mechanism | ______ |
| Monitoring / post-deploy validation | ______ |
| Tune/change path | ______ |
| Rollback/disable authority | ______ |
| Retirement / replacement path | ______ |
| Authoritative repository / source control | ______ |

The blanks are the learning objective. Fill them from the real shop.

##### Review, approval, deployment, and rollback are different decisions

One person or system may perform several of these locally, but the concepts should remain clear:

- **Review:** Is the analytic technically and analytically sound?
- **Approval:** Who is authorized to make the production decision?
- **Deployment:** How does the change reach production?
- **Rollback/disable:** Who can reverse the change when it causes a problem?
- **Retirement:** How is the old detection formally removed/superseded?

That distinction becomes important during urgent changes and production failures.

##### Source control and deployment platform may be different

A detection may be authored/stored in:
- a version-controlled repository;
- a content-management platform;
- a SIEM/EDR console;
- an internal detection-as-code pipeline.

The authoritative source must be known.

Otherwise, two engineers can edit different copies and both believe they changed production.

##### When local information is missing

Use precise onboarding status.

Examples:

> **Local required metadata list not yet verified.**

> **Deployment approval authority not yet verified.**

> **Rollback path not yet verified.**

This is more useful than inventing a “change board” or ticket because it tells the team exactly which operating fact still needs to be supplied.

##### A12 onboarding exercise

Assume DE has built and validated an A12-related analytic.

Before production, the learner should be able to identify:

1. Which local required fields/test evidence must be present?
2. Who reviews it?
3. Who approves it?
4. How is it deployed?
5. How is post-deploy health checked?
6. Who can roll it back?
7. Where is the authoritative version stored?
8. How will future tune/retire decisions be recorded?

If those answers are not known, the analytic may be technically ready while the **production process is not yet ready**.

#### Knowledge Check

1. Why is a public Sigma specification not the same thing as your organization's local deployment standard?
2. Name four roles/steps you should identify in the local lifecycle path.
3. You know how to deploy a rule but do not know who can approve or roll it back. What should you record?

#### Summary

Site-specific DE knowledge is an **orientation and governance** skill.

Find the current requirements list, its owner and version, and the real review/deploy/change/retire path.

Follow verified local process. When a piece is missing, identify that specific onboarding gap so the organization can close it.

This completes the **4.8 site-specific Detection Engineering module**.

#### References and Further Reading

- [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html) – an example external rule format; not a substitute for local policy.

### 4.9 — Detection Engineering Section Summary

**Estimated Time:** 15–20 minutes  

#### Purpose

Module 4.0 introduced Detection Engineering as a lifecycle:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

Module 4.9 closes that loop.

By this point, you have learned what DE owns, how new work enters, how detections are validated, how live analytics are tuned, how hunt and CTI findings become coverage decisions, how telemetry affects detection behavior, and how the local organization governs production changes.

This summary reconnects the pieces into one maintained detection capability.

#### What You Can Now Do

You should now be able to:

- explain what Detection Engineering owns across a detection lifecycle;
- distinguish a nomination from rule-authoring help, tuning work, investigation, and enforcement;
- evaluate whether an existing analytic already satisfies a defensive need;
- decide whether to reuse, modify, create, replace, leave, or retire coverage;
- identify the telemetry and fields a detection depends on;
- validate target behavior with positive tests;
- use benign controls and exclusions without silently removing the behavior you need to detect;
- distinguish an analytic-logic problem from a data-path, parsing, population, or timing problem;
- monitor a detection after deployment;
- revalidate after tuning or environmental changes;
- document the local review, approval, deploy, rollback, and retirement path.

The important skill is not producing the largest rule library.

It is maintaining reliable defensive coverage.

#### The 4.x Block at a Glance

| Unit | Core skill retained |
|---|---|
| **4.1 – What DE Owns** | Separate detection-lifecycle work from nominations, rule-authoring mechanics, investigation, and enforcement. |
| **4.2 – Sound Detections** | Validate behavior, benign controls, and required telemetry before calling an analytic production-ready. |
| **4.3 – Nominations** | Turn SOC, hunt, or CTI needs into reviewable detection work without requiring the nominator to engineer the rule. |
| **4.4 – Tune Requests** | Evaluate live analytics and choose tune, exception, replace, leave, or retire based on evidence. |
| **4.5 – Hunt and Intel Packages** | Convert findings into a coverage decision while checking existing analytics first. |
| **4.6 – Detection Lifecycle** | Maintain, monitor, change, replace, and retire detections over time. |
| **4.7 – Sensors and Data** | Trace collection, ingestion, parsing, population coverage, timeliness, and analytic logic when coverage fails. |
| **4.8 – Site-Specific DE** | Follow the organization's actual review, approval, deployment, rollback, source-control, and retirement process. |

Together, these units answer one question:

> **How do we turn a defensive need into reliable coverage that remains useful over time?**

#### A12 End to End

One A12 analytic can demonstrate the complete 4.x lifecycle.

##### Step 1 – Need

Threat hunting identifies recurring encoded PowerShell behavior and finds that current controls do not provide adequate coverage.

A useful nomination might say:

> **Need durable visibility for A12-style encoded PowerShell execution on managed Windows endpoints.**

The nomination does not need to include the final production rule.

##### Step 2 – Coverage decision

Before building anything new, DE asks:

- Do we already detect this behavior?
- Is existing coverage reliable on the relevant population?
- Could an existing analytic be safely extended?
- Is a new analytic necessary?
- Is detection the right defensive response?

The objective is coverage—not rule count.

##### Step 3 – Build or change

If a new or changed analytic is justified, DE translates the behavior into logic.

The implementation might use:
- process image;
- command-line content;
- parent/child relationships;
- additional context that improves discrimination.

The exact query language is secondary to the detection requirement.

##### Step 4 – Validate

A production candidate should answer three questions.

###### Positive test

> Does known A12-style target behavior match?

###### Benign-control test

> Does representative normal PowerShell behavior remain outside the match when appropriate?

###### Data test

> Do the production data path and target population provide the process and command-line fields the analytic expects?

A syntactically valid rule can fail any of these tests.

##### Step 5 – Deploy

Use the verified local process:

**review → approval → deployment → post-deploy validation**

Know:
- who reviews;
- who approves;
- how the change reaches production;
- where the authoritative version lives;
- who can roll it back.

##### Step 6 – Monitor

After deployment, evaluate:
- alert quality;
- expected event volume;
- missed target behavior;
- data health;
- population coverage;
- operational burden.

Deployment is the beginning of production ownership—not the end.

##### Step 7 – Improve

Suppose backup software generates benign encoded PowerShell.

DE may consider a narrow exception.

Before accepting it, confirm that the exception:
- removes the known benign case;
- preserves A12-style target behavior;
- does not create an unnecessarily broad blind spot.

Then re-run the positive test.

##### Step 8 – Troubleshoot silence

Suppose a safe replay occurs and the analytic does not fire.

Trace the path:

1. Was the source event recorded?
2. Did it reach the platform?
3. Were fields parsed correctly?
4. Was the test host in the covered population?
5. Did the data arrive in time?
6. Would the analytic logic match the resulting event?

The issue may be logic, data, coverage, timing—or more than one.

##### Step 9 – Lifecycle decision

Later, DE may decide to:
- leave the analytic unchanged;
- tune it;
- replace it with a stronger behavioral design;
- combine it with overlapping coverage;
- retire it when it no longer provides enough value.

Retirement should be an engineering decision, not simply a reaction to age.

#### Distinctions That Keep Detection Engineering Focused on Coverage

Detection Engineering receives requests from many parts of the defensive workflow. The following distinctions help the engineer identify the actual problem before deciding to change a rule.

##### A nomination identifies a defensive need; DE turns it into a coverage decision

SOC, Hunt, and CTI can identify behavior that deserves review and provide an evidence pointer. They do not need to deliver a finished production detection.

DE evaluates the need, checks existing coverage and data, and determines whether engineering work is warranted.

##### Valid syntax is only one requirement for production readiness

A query that parses correctly may still be analytically weak, poorly tested, unsupported by production telemetry, operationally noisy, or difficult to maintain.

Production readiness comes from the combination of sound logic, usable data, validation, deployment controls, and ongoing ownership.

##### A new defensive need does not always require a new rule

Before creating coverage, check whether an existing analytic already addresses the behavior or can be safely extended.

Reuse or modification can provide better coverage with less duplication and a smaller maintenance burden.

##### Tune requests and new nominations enter the lifecycle at different points

A **tune request** concerns a live analytic whose behavior needs adjustment.

A **nomination** introduces a new or newly recognized defensive need that DE must evaluate.

Both require evidence, but the engineering question is different.

##### An exception succeeds only when it fixes the benign condition without losing the target behavior

Removing a noisy benign case is not enough. Re-run the positive test after the exception and confirm that the intended malicious or unauthorized behavior is still detected.

This makes tuning a validation problem rather than simply a reduction in alert volume.

##### Detection gaps and data gaps require different engineering responses

If the required telemetry exists but current analytics do not adequately cover the behavior, the problem is detection/coverage.

If the required telemetry is missing, malformed, delayed, or absent from part of the target population, the problem is visibility or the data path.

Trace the data before changing analytic logic.

##### A silent analytic has several possible explanations

No alert may mean the target behavior did not occur. It can also reflect logic failure, collection or ingestion failure, parsing changes, population gaps, or late data.

A trustworthy conclusion about silence comes from checking the path from source event through analytic evaluation.

##### Detection and enforcement are different defensive controls

Detection asks whether the organization should create durable visibility or alerting for a behavior.

Blocking, containment, prevention, and other enforcement actions belong to the control owners defined by the organization. The same evidence may inform both decisions without making them the same function.

##### Deployment begins production ownership

Once an analytic reaches production, DE still owns monitoring, maintenance, tuning, revalidation, and eventual replacement or retirement.

The lifecycle continues because telemetry, environments, adversary behavior, and operational needs change.

#### Integrated Review Exercise

Use this **hypothetical Detection Engineering practice card based on A12 behavior**. The deployment result below is an exercise condition, not a canonical A12 outcome:

> **Need:** durable detection for A12-style encoded PowerShell  
> **Existing coverage:** partial; current analytic misses some variants  
> **Telemetry:** process image + command line available on most managed Windows endpoints  
> **Test:** target replay matches new logic  
> **Benign issue:** approved backup tooling also uses encoded PowerShell  
> **Coverage issue:** one endpoint group is missing command-line telemetry  
> **Production result:** analytic deployed after validation

Write a short DE lifecycle summary using:

##### Defensive need
What behavior needs durable coverage?

##### Coverage decision
Reuse, modify, or create? Why?

##### Validation
What positive, benign-control, and data tests are required?

##### Limitation
What population or telemetry problem remains?

##### Production action
How should deployment and rollback be controlled?

##### Follow-up
What should DE monitor or revalidate after deployment?

A strong answer should distinguish the **analytic design problem** from the **telemetry problem**.

#### Detection Engineering Readiness Checklist

Before completing the course, you should be comfortable saying:

- [ ] I can explain what DE owns across a detection lifecycle.
- [ ] I can distinguish nominations, tunes, rule-authoring help, investigation, and enforcement.
- [ ] I check existing coverage before proposing a new analytic.
- [ ] I can identify the behavior and telemetry a detection depends on.
- [ ] I can define a positive validation test.
- [ ] I can define a benign-control test.
- [ ] I can test whether required data reaches the analytic in the expected form.
- [ ] I can evaluate an exception without creating an uncontrolled blind spot.
- [ ] I can troubleshoot a silent detection across logic and the data path.
- [ ] I can separate missing detection coverage from missing telemetry.
- [ ] I understand that deployment begins production ownership.
- [ ] I can justify tune, leave, replace, or retire decisions with evidence.
- [ ] I can identify the local review, approval, deployment, rollback, and source-of-truth process.

If one of these is weak, return to the corresponding 4.x unit.

#### Closing the Defensive Loop

The course has now connected four defensive functions.

**SOC** observes and investigates activity.

**CTI** adds context and develops assessed intelligence.

**Threat Hunting** searches deliberately for related or insufficiently surfaced behavior.

**Detection Engineering** turns appropriate defensive knowledge into maintained coverage.

The relationship is cyclical.

A detection can create a SOC alert.

SOC can identify a new question.

CTI or hunt can expand that question.

The result can become new or improved detection coverage.

Then the cycle begins again.

#### Summary

The 4.x block taught the lifecycle of maintained detection capability:

**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

A strong detection program does not measure success by how many rules exist.

It measures whether useful coverage is:
- grounded in a real defensive need;
- supported by available data;
- validated;
- operationally usable;
- maintained as conditions change.

Keep one final principle:

> **A detection is a maintained capability, not a finished query.**

This completes the **4.x Detection Engineering block**.

## Part VI — Course Conclusion

Bring the role-specific work back together. The final chapter traces how an observation becomes an assessment, a search, and a coverage decision—and how those decisions shape the next observation.

### Course Summary – Bringing the Defensive Workflow Together

**Estimated Time:** 20–25 minutes  

#### Purpose

This course began by separating four defensive functions so their questions, methods, and products would remain clear:

- Security Operations
- Cyber Threat Intelligence
- Threat Hunting
- Detection Engineering

The final lesson reconnects them.

A simple course-wide model is:

**Observe → Understand → Search → Improve Coverage → Observe Again**

Mapped to the course:

**0.x – Shared Foundations**  
Understand the environment, roles, handoffs, frameworks, tools, and visibility.

**1.x – SOC**  
Observe and investigate what happened.

**2.x – CTI**  
Turn a requirement and collected evidence into assessed intelligence.

**3.x – Threat Hunting**  
Search deliberately for related or insufficiently surfaced activity.

**4.x – Detection Engineering**  
Turn appropriate defensive knowledge into maintained detection capability.

These functions are not a one-way pipeline. They form a feedback loop.

#### The Course at a Glance

| Section | Central question | Primary outcome |
|---|---|---|
| **0.x – Shared Foundations** | How does defensive work fit together? | Common vocabulary and operating context |
| **1.x – SOC** | What happened, and what should happen next? | Investigated alert, case, report, or handoff |
| **2.x – CTI** | What does the evidence mean, why does it matter, and what answer does the requirement support? | Assessed intelligence and an evidence-based response |
| **3.x – Threat Hunting** | Does this or related activity exist elsewhere? | Bounded hunt findings and defensive gaps |
| **4.x – Detection Engineering** | Should this behavior become maintained automatic coverage? | Validated and maintained detection capability |

The roles may overlap in practice, but their questions and products remain different.

#### One A12 Story Across the Entire Course

The A12 scenario demonstrates how evidence can move through the whole defensive system.

##### 0.x – Establish the Shared Context

Before anyone investigates, the team needs common language.

Learners identify:

- which role owns which question;
- how work can move between roles;
- how ATT&CK, Diamond Model, and Kill Chain organize different parts of the evidence;
- which external tools can provide useful observations;
- where important systems, access paths, and sensors sit in the environment.

This foundation prevents later analysts from confusing a tool with a function or a network path with actual visibility.

##### 1.x – SOC: Observe and Investigate

An alert involving `WS-JLEE` leads to evidence such as:

- `wscript.exe` launching encoded PowerShell;
- external communication;
- a request for `/update.exe`;
- persistence-related registry activity.

The SOC establishes what the available endpoint and network evidence supports.

It separates:

- observation from conclusion;
- detection match from maliciousness;
- known facts from unanswered questions.

The SOC may create an incident record and identify a bounded question that requires another function.

##### 2.x – CTI: Answer the Intelligence Requirement

The SOC sends an RFI such as:

> **What is known about the update domain, and does available evidence support that it delivered `update.exe` during A12?**

The reorganized CTI workflow begins with that requirement:

**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

###### Define the requirement

CTI identifies:

- the customer;
- the exact question;
- priority and deadline;
- existing evidence;
- what decision the answer will support.

###### Apply analytical tradecraft

The analyst preserves:

- source and provenance;
- source reliability;
- information credibility;
- uncertainty;
- alternative explanations;
- possible cognitive bias.

Two reports that repeat the same upstream source are not automatically two independent confirmations.

###### Use frameworks to organize the evidence

CTI may use:

- **ATT&CK** to organize behavior;
- **Diamond Model** to organize adversary, capability, infrastructure, and victim relationships;
- **Cyber Kill Chain** to reason about intrusion progression.

The framework organizes what is known. It does not fill missing facts.

###### Select platforms based on the question

The analyst chooses the source that can answer the next unresolved question.

Examples:

- internal TIP for prior context;
- VirusTotal for file relations or behavior;
- ANY.RUN for sandbox execution evidence;
- Silent Push for passive-DNS and infrastructure context;
- urlscan.io for observed web behavior.

The 2.x platform lessons intentionally use two passes:

1. **Retrieve correctly** and understand what the platform result can establish.
2. **Use the result analytically** during the appropriate enrichment method.

The platform is not the analysis.

###### Enrich and discover relationships

CTI may use:

- IOC lifecycle decisions;
- file similarity;
- RDAP/WHOIS;
- advanced DNS;
- infrastructure pivots;
- the infrastructure-focused DTF;
- correlation and link analysis.

An enrichment result usually begins as a candidate relationship.

For example:

> The update domain and `login-prd.net` share an uncommon nameserver and a time-overlapping IP.

That may support a candidate or stronger assessed infrastructure relationship depending on the rest of the evidence.

It does not automatically prove a campaign or actor attribution.

###### Assess organizational significance

The analyst keeps four questions separate:

**Applicability**
> Can this behavior occur in our environment?

**Visibility**
> Can our telemetry observe it?

**Relevance**
> Does this finding meaningfully intersect our mission, assets, technology, or exposure?

**Impact**
> If the finding is true here, what plausible consequence follows?

###### Produce and close the RFI

The final response returns to the original question.

For example:

> We assess that the update domain was likely used for attempted payload delivery in A12. WS-JLEE requested `/update.exe` from that destination during suspicious activity, but current evidence does not establish successful transfer or execution of the file.

The response separates:

- supported evidence;
- analytical judgment;
- uncertainty;
- unresolved gaps;
- agreed follow-up.

CTI then disseminates through the correct local channel and records closure or a new requirement.

##### 3.x – Threat Hunting: Search Beyond the Original Case

The intelligence answer can create a new internal question:

> **Does this or related behavior exist elsewhere in the environment?**

The hunter develops:

- a bounded question;
- a testable hypothesis;
- population;
- time window;
- telemetry requirements;
- distinctive patterns.

CTI indicators, procedures, infrastructure, and behavioral artifacts become hunt inputs.

They do not become proof of local occurrence until local evidence supports them.

The hunt may produce:

- additional affected hosts;
- related suspicious candidates;
- a detection gap;
- a visibility gap;
- a new intelligence lead.

A negative result remains bounded:

> The behavior was not found within the tested population, time window, and available telemetry.

##### 4.x – Detection Engineering: Create Durable Coverage

A useful hunt or intelligence finding may create a new defensive need:

> **We need durable visibility for this behavior.**

Detection Engineering first asks whether existing coverage already satisfies that need.

If not, DE may:

- modify existing logic;
- create new logic;
- validate target behavior;
- test representative benign activity;
- verify required telemetry;
- deploy through the local process;
- monitor production performance;
- tune, replace, or retire the analytic later.

The result is not merely a query.

It is maintained detection capability.

##### Back to the SOC

When the behavior occurs again, the improved analytic may generate an alert.

The SOC now begins with better visibility than it had during the original A12 case.

That completes the defensive feedback loop:

**SOC → CTI → Threat Hunting → Detection Engineering → SOC**

Real operations can enter, skip, repeat, or reverse parts of this loop. The important point is that evidence and questions move between specialized functions.

#### The Most Important Principle: Preserve the Evidence Boundary

Every section of this course returned to the same discipline:

> **Describe what the evidence shows before deciding what it means.**

Examples:

**Observation**

> `wscript.exe` launched PowerShell with an encoded command.

**Assessment**

> The activity is suspicious and consistent with the behavior under investigation.

The assessment may be reasonable, but it is not the same thing as the observation.

The same boundary applies across the course:

- SOC should not turn an alert label into proof of maliciousness.
- CTI should not turn a platform result or source claim into established fact.
- Hunting should not turn an external lead into proof of local occurrence.
- DE should not turn a matching condition into proof that the underlying activity is malicious.

Good defensive work preserves the boundary.

#### Questions Should Drive Tools

The course introduced many technologies and platforms:

- endpoint and SIEM telemetry;
- Zeek;
- Sigma;
- Suricata;
- YARA;
- threat-intelligence platforms;
- VirusTotal;
- ANY.RUN;
- Silent Push;
- urlscan.io;
- STIX;
- ATT&CK.

Each tool provides a capability.

None replaces the question.

A useful analyst asks:

- What am I trying to determine?
- Which source can answer that question?
- What exactly did the source observe?
- When?
- What are the limitations?
- What other evidence would change the conclusion?

This is why the reorganized CTI track explicitly teaches **platform selection before deep enrichment**.

The goal is not to touch every available tool.

The goal is to retrieve the evidence needed for the next analytical decision.

#### Frameworks Organize Evidence; They Do Not Create It

The course used several frameworks for different purposes.

**MITRE ATT&CK** helps describe adversary behavior.

**Diamond Model** helps organize relationships among adversary, capability, infrastructure, and victim.

**Cyber Kill Chain** helps reason about progression through an intrusion.

**DTF** helps organize infrastructure-focused pivots.

**STIX** helps represent and exchange structured CTI.

Each framework has a scope.

For example, file-similarity and behavioral relationships may support an assessment without belonging inside an infrastructure-focused DTF representation.

An incomplete model is preferable to a complete model built on assumptions.

#### Claim Strength Should Follow Evidence Strength

This principle is especially visible in the reorganized CTI section.

A shared nameserver may support a **candidate relationship**.

Several distinctive, time-relevant observations may support a **stronger assessed relationship**.

Evidence of coordinated activity over time may support an **activity-set or campaign assessment**.

Actor attribution requires still more evidence.

The analyst should not skip levels simply because the next label is more satisfying.

The same discipline applies elsewhere:

- a rule match is not automatically malicious;
- SYSTEM execution does not automatically prove a privilege-escalation method;
- an unalerted behavior is not automatically a false negative;
- no hunt results do not prove enterprise absence.

#### Visibility and Coverage Are Different Problems

This distinction connects SOC, CTI, hunting, and Detection Engineering.

##### Applicability

Can the behavior occur in the environment?

##### Visibility gap

The behavior can occur, but the evidence needed to observe or test it is missing or insufficient.

Examples:

- registry telemetry is not collected;
- a network segment lacks the required sensor;
- parsing removed a needed field.

##### Detection gap

The required telemetry exists, but current analytics do not adequately cover the behavior.

##### Relevance

Does the finding matter to the organization's mission, assets, technologies, or exposure?

These questions are related, but they are not interchangeable.

A relevant, applicable behavior can still have poor visibility.

A visibility problem normally requires collection, sensor, ingestion, or data-quality work.

A detection problem requires analytic coverage.

#### Negative Results Have Boundaries

Several parts of the course taught the same idea in different forms.

A SOC analyst cannot conclude that an event did not occur simply because the expected log is absent.

A CTI analyst cannot conclude that an object is benign because a TIP returned no match.

A hunter cannot conclude that the enterprise is clean because a query returned zero results.

A detection engineer cannot conclude that behavior did not happen because a rule remained silent.

A stronger statement is:

> **We did not observe the behavior within the scope and visibility available to us.**

Good conclusions state their boundaries.

#### Same Evidence, Different Product

One artifact can support several different workflows.

A domain may appear in:

- a SOC investigation;
- a CTI evidence record or assessment;
- a threat-hunt query;
- a detection analytic.

The evidence has not changed.

The **question and product** have.

Ask:

> **What decision is this work supposed to support?**

That question helps identify which role's product you are creating.

#### Handoffs Are Part of the Work

No defensive function needs to solve every problem itself.

A useful handoff communicates:

- what was observed;
- what was assessed;
- the supporting evidence;
- important uncertainty;
- what question or action remains.

Examples:

**SOC → CTI**

> What is known about this infrastructure and its relationship to the observed behavior?

**CTI → Hunt**

> This procedure appears applicable and relevant. Determine whether it exists elsewhere internally.

**Hunt → Detection Engineering**

> The behavior is visible and repeatable, but current analytics do not adequately cover it.

**Detection Engineering → SOC**

> This behavior now has validated production coverage and associated triage guidance.

A handoff is not abandonment.

It is how specialized defensive work becomes a coordinated capability.

#### Local Process Matters

The course teaches transferable tradecraft, but real organizations determine:

- priorities;
- customers;
- intelligence requirements;
- approval authorities;
- reporting requirements;
- hunt-control processes;
- deployment workflows;
- handling rules;
- authoritative repositories;
- sensor ownership;
- escalation paths;
- dissemination channels.

When local information is unknown, identify the specific missing operating fact.

Do not replace missing organizational knowledge with a plausible classroom workflow.

Generic tradecraft tells you **what questions to ask**.

Local policy tells you **how this organization answers them**.

#### Course Readiness Checklist

By the end of the course, you should be comfortable saying:

- [ ] I can distinguish an observation from an analytical judgment.
- [ ] I understand what endpoint and network evidence can and cannot establish.
- [ ] I can explain why a detection matched without treating the alert as automatic proof of maliciousness.
- [ ] I can identify when a SOC question should become an RFI or other handoff.
- [ ] I can distinguish data, information, and intelligence.
- [ ] I can define an intelligence requirement before collecting.
- [ ] I can evaluate source reliability, information credibility, uncertainty, and alternative explanations.
- [ ] I can choose a CTI platform based on the question rather than tool availability.
- [ ] I can distinguish a platform result, enrichment pivot, assessed relationship, campaign assessment, and attribution.
- [ ] I can separate applicability, visibility, relevance, and impact.
- [ ] I can produce an evidence-based RFI response and identify closure or follow-up.
- [ ] I can turn intelligence or an incident into a bounded hunt hypothesis.
- [ ] I can define hunt scope, telemetry, and limitations.
- [ ] I can distinguish a detection gap from a visibility gap.
- [ ] I can express a negative finding within the scope that was actually tested.
- [ ] I can turn a useful defensive finding into a Detection Engineering nomination.
- [ ] I can distinguish rule syntax from production-ready detection capability.
- [ ] I can validate detection behavior, benign controls, and telemetry dependencies.
- [ ] I understand that detections require monitoring, tuning, maintenance, and eventual retirement.
- [ ] I can identify when work belongs to another defensive function and provide a usable handoff.
- [ ] I know when an answer depends on local organizational policy rather than generic tradecraft.

Weakness in one area is not a reason to restart the course.

Use the section summaries to identify which track or lesson to revisit.

#### What the Course Was Really Teaching

The course included many technologies, frameworks, and technical details.

Those support a smaller set of durable habits.

##### Start with a clear question

Know what you are trying to determine.

##### Use evidence appropriate to that question

Different sensors, sources, platforms, and frameworks answer different questions.

##### Preserve provenance

Know where the evidence came from, when it was observed, and whether multiple sources are truly independent.

##### Preserve uncertainty

Say what is known, what is assessed, and what remains unresolved.

##### Keep scope visible

A conclusion is only as strong as the population, time window, visibility, and evidence behind it.

##### Keep claim strength proportional

A candidate link should remain a candidate until stronger evidence justifies promotion.

##### Produce something another defender can use

Analysis becomes operationally valuable when it supports a decision, action, or next question.

##### Improve the system when you learn something

An investigation can produce an intelligence requirement.

Intelligence can produce a hunt.

A hunt can expose a detection or visibility gap.

Detection Engineering can turn that lesson into better future coverage.

That is how defensive operations learn.

#### Final Course Model

The course began with separate roles.

It ends with one connected defensive system:

**Observe → Understand → Search → Improve Coverage → Observe Again**

Or, expressed through the role tracks:

**SOC → CTI → Threat Hunting → Detection Engineering → SOC**

The cycle is not rigid and the roles are not silos.

What connects them is disciplined use of evidence, appropriately bounded judgments, and clear handoffs.

> **Follow the evidence. Answer the question in front of you. Preserve what remains uncertain. Give the next defender something they can use.**

## Appendix A — The Complete A12 Case Study

Read this complete case after the main course to see how the same evidence moves between SOC, CTI, Threat Hunting, and Detection Engineering. The canonical narrative is reproduced here, with book navigation adapted from its source links.

### A12 — Following the Evidence Across Four Defensive Roles

Dixon, Yamada, & Associates (**DYA**) is the fictional law firm used throughout this course. In Building C, the workstation **WS-JLEE** (`10.10.8.40`) is associated with `jlee` / `BUILDINGC\jlee`. The investigation involving that workstation is **A12**. A vendor report uses the tracking label **Pink River Dolphin (PRD)**; that name tells us how the vendor describes activity, while the identity of the actor responsible for this case remains unresolved.

You have already encountered parts of A12 in the lessons. This retelling brings them together so you can follow how an observation becomes an investigation, an intelligence question, a hunt lead, and a detection-coverage review. As you read, watch what each role receives, how it reasons from that evidence, and what the next person needs to continue. The case becomes more useful through these handoffs even when some questions remain unanswered.

Before reading closely, skim the nine stages and the closing product table. Try to predict where the evidence supports an observation, where an analyst must make an assessment, and where another source would be needed. Return to the table afterward and check whether you can explain why each product has a different purpose.

One question stays open from the beginning: **how access first occurred**. The case later shows `invoice.vbs` in a Temp path and the process activity that followed, but those observations do not identify the entry mechanism. A phishing message, malicious web path, public-facing exploit, valid-account session, or trusted-third-party path would require its own supporting evidence. Treat those as hypotheses unless the case supplies that evidence.

#### 1. Start with the process event behind the alert

The first record in the SOC queue is a SIEM alert for `wscript.exe` launching `powershell.exe -enc ...` on **WS-JLEE** as `jlee`. The rule has matched a process pattern involving an encoded-command argument. An analyst can verify that pattern from the recorded fields and explain why the rule selected the event.

Understanding the match is the beginning of the investigation. The encoded argument alone leaves the command's behavior and authorization unresolved. Several other useful details, including a related destination, URI, and file hash, are absent from the initial alert. Their absence tells the analyst what additional evidence to seek before drawing a broader conclusion about the activity.

The analyst records the host, account, time, rule identity, parent process, and child command line, then traces how the alert was produced. In this example, endpoint telemetry reaches an ingested table, the SIEM rule evaluates the event, and the SIEM creates the alert. Tracing that path makes it possible to connect the alert to the actual logic and data that produced it. A Suricata stage would belong in a different detection path only if the source records showed one.

The next collection step follows the question. At this stage the analyst needs related host records. Packet capture may become useful once a network flow and a question about that flow have been identified.

#### 2. Add context while keeping the classification open

The analyst collects related endpoint records for **WS-JLEE** and the case time window. The broader case includes `wscript.exe` running `invoice.vbs` from a Temp path and launching encoded PowerShell. A file event supplies the `invoice.vbs` artifact and a hash. Endpoint network telemetry associates the PowerShell process with an outbound connection to `203.0.113.88:8080`.

Zeek adds the protocol view: an HTTP `GET` request with Host `prd-updates.net` and URI `/update.exe`. Correlating the host, time, and connection context allows the analyst to read these records together while retaining what each source actually observes.

| Source | What it contributes | Question still open |
|---|---|---|
| Process evidence | The Script Host–PowerShell chain and recorded command-line context | What was authorized, and what did the encoded command do? |
| File evidence | Temp `invoice.vbs` and its recorded hash | What does further analysis establish about the file? |
| Endpoint network evidence | A process-associated connection to `203.0.113.88:8080` | What was exchanged over that connection? |
| Zeek HTTP evidence | A request to `prd-updates.net` for `/update.exe` | Did a response transfer the file, and did the file execute? |

Retained packets, if available, could help answer a specific traffic question. The analyst would record which flow and time were examined and what the packets added. The case does not supply a packet-capture result that confirms transfer, so the request remains the established network observation.

The file hash also provides a possible enrichment starting point. An approved VirusTotal lookup would preserve the exact queried value, report reference, time, and result. For this case, the record is **lookup result not supplied**. There is no supplied service verdict to interpret as either malicious or benign, and no live lookup was performed for this publication.

A hash could also locate an existing ANY.RUN report. That retrieval can be useful without possessing a sample for a new detonation. Submitting a file for a new run is a separate workflow with its own input and handling requirements. The analyst chooses between those actions by asking which result could resolve the current uncertainty.

The combined evidence gives the analyst a reason to investigate and escalate, while the **malicious/unauthorized target-condition assessment remains unresolved**. A true-positive label would require evidence of that condition in addition to the rule match. Preserving the unresolved classification lets another analyst see both the suspicious pattern and the work still needed to assess it.

There is also no supplied alert specifically for the `/update.exe` request. This raises a **coverage question**. Establishing a false negative would require the assessed target condition, an expectation that a detector should cover it, evidence that the necessary telemetry reached that detector, and a checked alert outcome for the relevant scope and time. Those conditions have not been established here, so the case carries the question forward for review.

#### 3. Give incident response and leadership the products they need

SOC opens the incident record and routes the affected host to **Sam** in Incident Response. The handoff includes the observed process chain, related file and network records, and the questions that remain open. Sam can work from those observations while further analysis continues.

The leadership update has a narrower purpose. It can explain that **WS-JLEE**, associated with `jlee`, generated a suspicious Script Host–PowerShell alert and that investigation identified Temp `invoice.vbs`. Detailed hashes, registry paths, and subsequent enrichment belong in the technical record where the receiving analysts can use them. Selecting detail by audience makes the update easier to act on without weakening the evidence retained in the case.

The course uses classroom response clocks and approved-ticket examples to teach timely routing. Actual deadlines, recipients, and approval paths come from the learner's organization. A12 demonstrates why those routes matter without assigning DYA a complete operating policy.

Escalation and analytical certainty answer different questions. The observed activity can warrant response while the team continues to establish authorization, delivery, and scope. Recording that uncertainty in the handoff helps Sam understand the basis for the referral.

#### 4. Turn the network question into a bounded RFI

SOC now has enough context to ask CTI a focused question:

> **Was the update domain the host that successfully delivered the payload in A12?**

**Jordan** owns this Request for Information, or **RFI**. The existing incident supplies the scope: WS-JLEE, the update domain, `/update.exe`, and the relevant case window. The question asks CTI to distinguish an attempted retrieval from a successful delivery.

At intake, Jordan can explain why the question matters and identify the missing evidence. The HTTP request supports an attempted retrieval, while confirmation of delivery would require response, transfer, or resulting host-artifact evidence. The requester and Jordan clarify the needed-by time and any handling restrictions through the actual request process.

Because the question supports an active incident, the classroom example gives it priority over routine background reading, subject to the organization's priorities. That reasoning establishes a useful next action without inventing a universal queue rule. If analysis later raises a separate question about infrastructure control or actor identity, it can be recorded as a follow-on requirement with its own scope.

#### 5. Answer the RFI with a judgment the evidence can support

Jordan evaluates the request alongside the suspicious host activity. Requesting an executable-looking resource from the associated destination during that activity supports an assessment of the domain's likely delivery role. Successful transfer and execution remain separate questions because the supplied records do not show those outcomes.

A useful response is:

> We assess that the update domain was **likely used for attempted payload delivery** in A12. WS-JLEE requested `/update.exe` from that destination during the suspicious activity, but current evidence does not establish successful transfer or execution of the file.

The answer gives the requester an assessment now and identifies what additional evidence would be needed to answer the successful-delivery question fully. “Likely” expresses the probability of the assessed role. Any confidence statement should separately explain the strength and limitations of the sources supporting that judgment.

Frameworks help Jordan make the reasoning easier to inspect. ATT&CK provides a behavioral description for the observed PowerShell execution through **T1059.001 – PowerShell**. The mapping describes the observed behavior; the authorization assessment still depends on the investigation. Mapping **T1105 – Ingress Tool Transfer** would require evidence of transfer beyond the request currently available.

The Diamond Model organizes the entities and relationships:

| Vertex | Supported A12 content |
|---|---|
| **Victim** | WS-JLEE, `jlee`, and DYA |
| **Capability** | Encoded PowerShell; `/update.exe` as the requested candidate payload name |
| **Infrastructure** | `prd-updates.net` and `203.0.113.88` |
| **Adversary** | Unresolved; PRD remains a vendor tracking label rather than an independently established actor identity |

The unfilled adversary identity helps the reader see where attribution would require further evidence. The Cyber Kill Chain offers another view, focused on progression, but assigning a stage still requires evidence of the role the activity played. A process launch or request cannot establish every later stage simply because the names suggest an attack sequence.

Jordan returns the bounded answer with its evidence and remaining collection need. That closes the communication loop for the answer available now while allowing any agreed follow-up to remain visible.

#### 6. Use infrastructure overlap to generate a testable candidate

CTI can also enrich the destination already associated with A12. Registration and DNS information identify the nameserver pair `ns1.cdn-test.net` and `ns2.cdn-test.net`. The supplied SOA RNAME is `hostmaster.cdn-test.net`, which provides zone-contact context. These fields help the analyst choose further lookups; their presence alone does not identify the responsible actor.

A second name, **`login-prd.net`**, shares the uncommon nameserver pair and the observed A address `203.0.113.88` during the relevant period. The overlap is specific enough to investigate as **candidate related infrastructure**. Its value comes from the shared features, their timing, and the question they make testable.

A concise record is:

| Seed | Shared characteristics | Candidate | Next analytical step |
|---|---|---|---|
| `prd-updates.net` | Uncommon NS pair and the same observed A address during the relevant period | `login-prd.net` | Compare registration and DNS history, hosting context, and independent evidence that could strengthen or weaken the relationship |

Several objects can share a provider or service without sharing an operator. The next lookup therefore tests that alternative alongside the possible operational connection. Common control would require corroboration; an activity-set or campaign assessment would additionally need evidence of related activity. Actor attribution is a further judgment with its own evidentiary burden.

The address also sits inside **Example Cloud's `203.0.113.0/24`**. The allocation tells the analyst about the hosting range, but one case address gives too little specificity to treat all neighboring addresses as A12 infrastructure. The range is **rejected as too broad for promotion**. Expiration would describe a different lifecycle situation in which a previously valid indicator had lost its usefulness.

The result of this enrichment is a documented candidate and a next question. The record retains both the observed overlap and the limits of the relationship claim so later analysis can revise it without losing its history.

#### 7. Let the protective-control owner evaluate the candidate

The candidate may be relevant to a protective-control decision because the organization is investigating activity involving related infrastructure. CTI packages the object, shared characteristics, relevant observation period, and uncertainty for the function responsible for those controls. Depending on the organization, that may be a firewall team or an Information Assurance function.

The receiving owner applies local thresholds and considers the consequences of blocking, monitoring, or taking no action. CTI's contribution is the assessment and its basis; the control owner's contribution is the authorized operational decision. Keeping both visible prevents the candidate from quietly becoming a confirmed malicious destination as it moves through a ticket.

The canonical case leaves the final control action unspecified. Sam continues to own the host response, and Jordan's intelligence record remains available to support the decision. The same evidence can later inform detection work without turning a control request into a completed detection change.

#### 8. Build a hunt around the observed registry configuration

Threat Hunting uses the case to ask whether related behavior or artifacts appear elsewhere in the environment. At this stage, the course brings forward registry evidence that was not required to explain the initial process alert: PowerShell set the current-user Run value **`Updater`** to **`%TEMP%\update.exe`**.

That observation establishes a configured persistence mechanism. The target file's existence, its successful launch, and persistence taking effect remain unresolved. This distinction gives the hunter a concrete search lead while keeping the result of that configuration open.

A bounded hypothesis could be:

> If related A12 persistence configurations exist on other user workstations, we expect to find the `Updater` Run value pointing to `%TEMP%\update.exe`, or related case artifacts, within the selected time window.

The hunter begins with the observed value and target path, then may broaden deliberately to relevant variants. Registry and file telemetry determine what the search can test. `invoice.vbs` and the domain/address/request pattern provide additional case leads, with matches evaluated in their own context. A filename or registry-value hit is a candidate for investigation before it becomes a finding of another affected host.

ATT&CK's **T1547.001 – Registry Run Keys / Startup Folder** helps describe the technique associated with the configuration. The practical hunt still needs a defined population, time window, evidence sources, and reviewable results. Those details make it possible for another hunter to repeat the work and understand the limits of a negative result.

The package records the question, scope, look-fors, telemetry, findings if established, and visibility or coverage questions. Any new evidence of affected hosts would go to the incident-response process. A12 leaves the hunt's host count and search results unspecified, so the handoff preserves the question and available evidence without implying that an outbreak has been found.

#### 9. Give Detection Engineering a need and an evidence pointer

The case and hunt package provide **a need and an evidence pointer** for Detection Engineering: assess whether current coverage adequately addresses the relevant behavior, using the documented process, registry, and network observations. A completed production rule is not required from the nominator; DE first evaluates the coverage question.

The engineer checks whether an existing analytic can be reused, whether the necessary telemetry reaches the detection system, and whether the requested behavior falls within the intended coverage. This review can distinguish a gap in analytic logic from a collection or visibility problem. It can also show that the current coverage is already adequate.

| Possible review result | Reasoning that would support it |
|---|---|
| **Reuse or no new rule** | Existing coverage already addresses the need adequately. |
| **Change** | An existing analytic needs a supported improvement. |
| **Add** | The behavior warrants detection and available telemetry can support coverage that is currently missing. |
| **Data or visibility gap** | The needed evidence is absent, incomplete, or not reaching the detection system. |
| **Route to another owner** | The requested outcome concerns blocking, containment, or another function. |

The unalerted request remains a question within that review, rather than a pre-established false negative. If the review later establishes the required target condition, coverage expectation, telemetry, and failed alert outcome, the classification can be updated with that basis.

The case ends with the package available for this coverage review. It supplies no completed review outcome, deployed analytic, validation result, eradication, or final incident resolution. Keeping that endpoint explicit allows the later engineering lessons to explore possible follow-through without presenting their practice conditions as events that happened in A12.

#### What you should be able to explain afterward

The same observations support several products because the roles need to answer different questions. Each handoff should preserve the evidence and reasoning while making the next decision clear.

| Role | Question carried forward | Product at this point in A12 |
|---|---|---|
| **SOC** | What happened, what remains uncertain, and who needs the case? | Investigation record, incident route, concise leadership update, and RFI |
| **CTI** | What role did the destination likely play, and what relationship is worth testing? | Attempted-delivery assessment, explicit transfer/execution gap, and candidate infrastructure record |
| **Threat Hunting** | Where else could the supported behavior or artifacts appear within a bounded scope? | Search hypothesis and package retaining its evidence, scope, and unresolved results |
| **Detection Engineering** | Is a coverage change justified, and can the available data support it? | Need and evidence pointer for coverage/visibility review; outcome still open |
| **Incident Response** | What host-response work is required? | Continued ownership of the affected host by Sam |
| **Protective-control owner** | Does the candidate justify an action under local policy? | Evidence for a control review; action still open |

By this point, you should be able to trace the observations through those products, explain why the RFI answer stops at attempted delivery, and distinguish a useful hunt or infrastructure lead from a confirmed finding. You should also be able to name the additional evidence needed for a TP, an FN, successful transfer, or a stronger infrastructure relationship.

The course principle applies throughout: **Describe what the evidence shows first. Then decide what it means.** A clear account of what remains uncertain gives the next analyst a reliable place to continue.

#### Related course reading

- [Alert context and investigation — 1.4.1](#141--alert-context-and-investigation) and [classification — 1.4.2](#142--alert-classification).
- [RFI intake — 2.1.5](#215--rfi-intake-and-prioritization) and [response and closure — 2.7.4](#274--rfi-responses-and-closure).
- [Analytical frameworks — 2.3](#23--analytical-frameworks-introduction), [ANY.RUN — 2.4.4](#244--anyrun), and [IOC handling — 2.5.1](#251--ioc-handling-and-enrichment-concepts).
- [Infrastructure pivots — 2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators) and [correlation — 2.5.7](#257--correlation-link-analysis-and-campaign-tracking).
- [Technique-focused hunting — 3.6.3](#363--hunt-for-a-specific-persistence-or-privilege-escalation-technique) and [DE package review — 4.5](#45--hunt-and-intel-packages).

## Appendix B — Proficiency Mapping

These are the course’s existing proficiency requirements. Role ratings, task identifiers, and mapped knowledge and performance statements are retained from the student guides. The three ratings in a role entry correspond to the course’s 3-, 5-, and 7-level progression. The qualification rules below describe this curriculum’s model.

### Reading the Proficiency Codes

### Skill Levels (3/5/7)

| Level | Title              | Description |
|-------|--------------------|-------------|
| **3** | Apprentice         | Entry-level. Can perform tasks with detailed guidance and supervision. Must never work a shift alone. Must be trained/supervised by at least a 7-level. |
| **5** | Journeyman         | Fully qualified. Can perform tasks independently under normal conditions. May work a shift alone. |
| **7** | Craftsman / Senior | Advanced. Can perform complex/non-standard tasks, troubleshoot, adapt techniques, train others, and set standards. Qualified to supervise and train 3-levels. |

**Special Note:**  
- **1-level** (pre-apprentice / trainee) is never authorized to work on shift.

---

### Proficiency Codes (USAF CFETP Style)

#### Task Performance Levels
| Code | Definition |
|------|------------|
| **1** | Can do simple parts of the task. Needs to be told or shown how to do most of the task. **(Extremely Limited)** |
| **2** | Can do most parts of the task. Needs help only on hardest parts. **(Partially Proficient)** |
| **3** | Can do all parts of the task. Needs only a spot check of completed work. **(Competent)** |
| **4** | Can do the complete task quickly and accurately. Can tell or show others how to do the task. **(Highly Proficient)** |

#### Task Knowledge Levels
| Code | Definition |
|------|------------|
| **a** | Can name parts, tools, and simple facts about the task. **(Nomenclature)** |
| **b** | Can determine step-by-step procedures for doing the task. **(Procedures)** |
| **c** | Can identify why and when the task must be done and why each step is needed. **(Operating Principles)** |
| **d** | Can predict, isolate, and resolve problems about the task. **(Advanced Theory)** |

#### Subject Knowledge Levels
| Code | Definition |
|------|------------|
| **A** | Can identify basic facts and terms about the subject. **(Facts)** |
| **B** | Can identify relationship of basic facts and state general principles about the subject. **(Principles)** |
| **C** | Can analyze facts and principles and draw conclusions about the subject. **(Analysis)** |
| **D** | Can evaluate conditions and make proper decisions about the subject. **(Evaluation)** |

---

### How Codes Are Written

Examples:
- `3c` = Competent performance + understands operating principles
- `2b` = Partially proficient + knows procedures
- `4d` = Highly proficient + advanced theory
- `B`  = Subject knowledge at the Principles level
- `3c / B` = Both a task code and a subject knowledge code apply

---

### Instruction, Demonstration, and Qualification

The proficiency codes above describe the **required end-state performance**, not merely lesson completion.

Use the three-state model in [Qualification Demonstration and Sign-Off Standard](qualification-demonstration-signoff-standard.md):

> **Taught / Prepared → Demonstrated → Qualified / Signed Off**

- A lesson or knowledge check can prepare a learner for a task without proving the mapped task-performance level.
- A **Task (`T`)** row requires observable performance before qualification sign-off.
- The smallest honest demonstration should prove the verb in the requirement; not every task needs a full lab.
- Local/site-specific tasks require the real approved local process or an authorized local simulation.
- The working crosswalk for all current task rows is [qualification-evidence-map.md](qualification-evidence-map.md).

Do not reinterpret a matrix verb such as **execute**, **perform**, **test**, **produce**, **disseminate**, or **follow** as a weaker planning/discussion exercise merely because the lesson is concept-first.

---

### Manning & Qualification Rules (Quick Reference)

- **1-level**: Never on shift
- **3-level**: Never alone on shift; must be supervised by ≥ 7-level
- **5-level**: May work alone
- **7-level**: May supervise and train 3-levels

### Chapter Mappings

#### Mapping — 0.1 — How this course is laid out

[Return to chapter](#01--how-this-course-is-laid-out)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (front door)  
**Proficiency Focus:**  
- SOC: 0.1 A / B / B  
- Hunter: 0.1 A / B / B  
- CTI: 0.1 A / B / B  
- DE: 0.1 A / B / B  
**Mapped Proficiency Items:**
- K: 0.1 – How this course is laid out

#### Mapping — 0.2 — What a SOC is

[Return to chapter](#02--what-a-soc-is)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.2 A / B / B  
- Hunter: 0.2 A / B / B  
- CTI: 0.2 A / B / B  
- DE: 0.2 A / B / B  
**Mapped Proficiency Items:**
- K: 0.2 – What a SOC is

#### Mapping — 0.3 — Jobs in one sentence

[Return to chapter](#03--jobs-in-one-sentence)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.3 A / B / B  
- Hunter: 0.3 A / B / B  
- CTI: 0.3 A / B / B  
- DE: 0.3 A / B / B  
**Mapped Proficiency Items:**
- K: 0.3 – Jobs in one sentence

#### Mapping — 0.4 — How work can move

[Return to chapter](#04--how-work-can-move)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- Hunter: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- CTI: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
- DE: 0.4 A / B / B ; 0.4.1 1a / 2b / 2b  
**Mapped Proficiency Items:**
- K: 0.4 – How work can move
- T: 0.4.1 – Given a step in the flow, name the next hand-off and whose product it is

#### Mapping — 0.5 — Where the jobs lightly overlap

[Return to chapter](#05--where-the-jobs-lightly-overlap)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.5 A / B / B  
- Hunter: 0.5 A / B / B  
- CTI: 0.5 A / B / B  
- DE: 0.5 A / B / B  
**Mapped Proficiency Items:**
- K: 0.5 – Where the jobs lightly overlap

#### Mapping — 0.6.1 — MITRE ATT&CK

[Return to chapter](#061--mitre-attck)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.1.1 A / B / C ; 0.6.1.2 2b / 3c / 4c  
- Hunter: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- CTI: 0.6.1.1 B / C / C ; 0.6.1.2 3c / 4c / 4c  
- DE: 0.6.1.1 A / B / B ; 0.6.1.2 1a / 2b / 2b  
**Mapped Proficiency Items:**
- K: 0.6.1.1 – MITRE ATT&CK
- T: 0.6.1.2 – Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence

#### Mapping — 0.6.2 — Diamond Model

[Return to chapter](#062--diamond-model)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.2.1 A / B / C ; 0.6.2.2 2b / 3c / 4c  
- Hunter: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- CTI: 0.6.2.1 B / C / C ; 0.6.2.2 3c / 4c / 4d  
- DE: 0.6.2.1 A / B / B ; 0.6.2.2 1a / 2b / 2b  
**Mapped Proficiency Items:**
- K: 0.6.2.1 – Diamond Model
- T: 0.6.2.2 – Apply the Diamond Model to an incident or set of indicators

#### Mapping — 0.6.3 — Cyber Kill Chain

[Return to chapter](#063--cyber-kill-chain)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.6.3.1 A / B / C ; 0.6.3.2 2b / 3c / 4c  
- Hunter: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- CTI: 0.6.3.1 B / C / C ; 0.6.3.2 3c / 4c / 4c  
- DE: 0.6.3.1 A / B / B ; 0.6.3.2 1a / 2b / 2b  
**Mapped Proficiency Items:**
- K: 0.6.3.1 – Cyber Kill Chain
- T: 0.6.3.2 – Identify the Kill Chain stage of observed activity

#### Mapping — 0.7 — External tools

[Return to chapter](#07--external-tools)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
- Hunter: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- CTI: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- DE: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 0.7 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)
- T: 0.7.1 – Select the appropriate external tool for a given enrichment or analysis need

#### Mapping — 0.8 — Environment / signal flow

[Return to chapter](#08--environment--signal-flow)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.8 A / B / C ; 0.8.1 2b / 3c / 4c  
- Hunter: 0.8 B / C / C ; 0.8.1 2b / 3c / 4c  
- CTI: 0.8 A / B / B ; 0.8.1 1a / 2b / 3c  
- DE: 0.8 A / B / B ; 0.8.1 2b / 3c / 4c  
**Mapped Proficiency Items:**
- K: 0.8 – Environment / signal flow
- T: 0.8.1 – Identify which kind of fact applies and why it is not the adjacent kind

#### Mapping — 0.9 — Common Initial Access Paths

[Return to chapter](#09--common-initial-access-paths)

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared foundations)  
**Proficiency Focus:**  
- SOC: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- Hunter: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- CTI: 0.9 A / B / C ; 0.9.1 2b / 3c / 4c  
- DE: 0.9 A / B / B ; 0.9.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 0.9 – Common initial access paths
- T: 0.9.1 – Identify the most defensible initial-access path from supplied evidence, preserve uncertainty, and name the next evidence needed

#### Mapping — 0.10 — Shared Foundations Section Summary

[Return to chapter](#010--shared-foundations-section-summary)

**Target Audience:** SOC Analyst, CTI Analyst, Threat Hunter, Detection Engineer  
**Module Type:** Section summary — no proficiency mapping

#### Mapping — 1.0 — SOC Analyst Fundamentals: How the 1.x Block Fits Together

[Return to chapter](#10--soc-analyst-fundamentals-how-the-1x-block-fits-together)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Module Type:** Orientation — no proficiency mapping

#### Mapping — 1.1.1 — Endpoint activity (the map)

[Return to chapter](#111--endpoint-activity-the-map)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.1.1.1 – Endpoint activity (the map)
- T: 1.1.1.2 – Given a one-line description, name the activity type

#### Mapping — 1.1.2 — Process Activity

[Return to chapter](#112--process-activity)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.2.1 A / B / C ; 1.1.2.2 2b / 3c / 4c ; 1.1.2.3 2b / 3c / 4c  
- Hunter: 1.1.2.1 A / B / B ; 1.1.2.2 1a / 2b / 3c ; 1.1.2.3 1a / 2b / 3c  
- CTI: 1.1.2.1 A / A / A ; 1.1.2.2 1a / 1a / 1a ; 1.1.2.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.1.2.1 – Process activity concepts
- T: 1.1.2.2 – Analyze a process event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.2.3 – Create a SIEM query to detect specific process activity

#### Mapping — 1.1.3 — File System Activity

[Return to chapter](#113--file-system-activity)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.3.1 A / B / C ; 1.1.3.2 2b / 3c / 4c ; 1.1.3.3 2b / 3c / 4c  
- Hunter: 1.1.3.1 A / B / B ; 1.1.3.2 1a / 2b / 3c ; 1.1.3.3 1a / 2b / 3c  
- CTI: 1.1.3.1 A / A / A ; 1.1.3.2 1a / 1a / 1a ; 1.1.3.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.1.3.1 – File system activity concepts
- T: 1.1.3.2 – Analyze a file event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.3.3 – Create a SIEM query to detect specific file operations

#### Mapping — 1.1.4 — Network Activity (Endpoint)

[Return to chapter](#114--network-activity-endpoint)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.4.1 A / B / C ; 1.1.4.2 2b / 3c / 4c ; 1.1.4.3 2b / 3c / 4c  
- Hunter: 1.1.4.1 A / B / B ; 1.1.4.2 1a / 2b / 3c ; 1.1.4.3 1a / 2b / 3c  
- CTI: 1.1.4.1 A / A / A ; 1.1.4.2 1a / 1a / 1a ; 1.1.4.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.1.4.1 – Network activity (endpoint) concepts
- T: 1.1.4.2 – Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.4.3 – Create a SIEM query to detect specific endpoint network activity

#### Mapping — 1.1.5 — Registry Activity

[Return to chapter](#115--registry-activity)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.5.1 A / B / C ; 1.1.5.2 2b / 3c / 4c ; 1.1.5.3 2b / 3c / 4c  
- Hunter: 1.1.5.1 A / B / B ; 1.1.5.2 1a / 2b / 3c ; 1.1.5.3 1a / 2b / 3c  
- CTI: 1.1.5.1 A / A / A ; 1.1.5.2 1a / 1a / 1a ; 1.1.5.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.1.5.1 – Registry activity concepts
- T: 1.1.5.2 – Analyze a registry event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.5.3 – Create a SIEM query to detect specific registry operations

#### Mapping — 1.1.6 — Image and Driver Load Activity

[Return to chapter](#116--image-and-driver-load-activity)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.6.1 A / B / C ; 1.1.6.2 2b / 3c / 4c ; 1.1.6.3 2b / 3c / 4c  
- Hunter: 1.1.6.1 A / B / B ; 1.1.6.2 1a / 2b / 3c ; 1.1.6.3 1a / 2b / 3c  
- CTI: 1.1.6.1 A / A / A ; 1.1.6.2 1a / 1a / 1a ; 1.1.6.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.1.6.1 – Image and driver load activity concepts
- T: 1.1.6.2 – Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred
- T: 1.1.6.3 – Create a SIEM query to detect specific image or driver load activity

#### Mapping — 1.2.1 — Zeek Concepts

[Return to chapter](#121--zeek-concepts)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.1.1 A / B / C  
- Hunter: 1.2.1.1 B / C / C  
- CTI: 1.2.1.1 A / B / B  
**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts

#### Mapping — 1.2.2 — Conn Engine

[Return to chapter](#122--conn-engine)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.2.1 A / B / C ; 1.2.2.2 2b / 3c / 4c ; 1.2.2.3 2b / 3c / 4c  
- Hunter: 1.2.2.1 B / C / C ; 1.2.2.2 3c / 4c / 4c ; 1.2.2.3 3c / 4c / 4c  
- CTI: 1.2.2.1 A / A / B ; 1.2.2.2 1a / 1a / 2b ; 1.2.2.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

#### Mapping — 1.2.3 — DNS Engine

[Return to chapter](#123--dns-engine)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

#### Mapping — 1.2.4 — TLS Engine

[Return to chapter](#124--tls-engine)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

#### Mapping — 1.2.5 — HTTP Engine

[Return to chapter](#125--http-engine)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C ; 1.2.5.2 2b / 3c / 4c ; 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C ; 1.2.5.2 3c / 4c / 4c ; 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B ; 1.2.5.2 1a / 2b / 3c ; 1.2.5.3 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

#### Mapping — 1.2.6 — SMTP Engine

[Return to chapter](#126--smtp-engine)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C ; 1.2.6.2 2b / 3c / 4c ; 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C ; 1.2.6.2 3c / 4c / 4c ; 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B ; 1.2.6.2 1a / 1a / 2b ; 1.2.6.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

#### Mapping — 1.2.7 — Files Engine

[Return to chapter](#127--files-engine)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.7.1 A / B / C ; 1.2.7.2 2b / 3c / 4c ; 1.2.7.3 2b / 3c / 4c  
- Hunter: 1.2.7.1 B / C / C ; 1.2.7.2 3c / 4c / 4c ; 1.2.7.3 3c / 4c / 4c  
- CTI: 1.2.7.1 A / A / B ; 1.2.7.2 1a / 1a / 2b ; 1.2.7.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.2.7.1 – Files engine
- T: 1.2.7.2 – Analyze a Zeek files log and accurately describe what occurred
- T: 1.2.7.3 – Create a SIEM query to detect specific file transfer activity

#### Mapping — 1.2.8 — Weird Engine

[Return to chapter](#128--weird-engine)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C ; 1.2.8.2 2b / 3c / 4c ; 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C ; 1.2.8.2 3c / 4c / 4c ; 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A ; 1.2.8.2 1a / 1a / 1a ; 1.2.8.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log and accurately describe what occurred
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

#### Mapping — 1.3.1 — SIGMA Rules

[Return to chapter](#131--sigma-rules)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.1.1 A / B / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 1a / 2b / 3c  
- Hunter: 1.3.1.1 B / C / C ; 1.3.1.2 2b / 3c / 4c ; 1.3.1.3 2b / 3c / 4c  
- CTI: 1.3.1.1 A / B / B ; 1.3.1.2 1a / 2b / 3c ; 1.3.1.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.3.1.1 – SIGMA rules
- T: 1.3.1.2 – Analyze an existing SIGMA rule and describe what it detects
- T: 1.3.1.3 – Create or modify a basic SIGMA rule

#### Mapping — 1.3.2 — Suricata Rules

[Return to chapter](#132--suricata-rules)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.2.1 A / B / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 1a / 2b / 3c  
- Hunter: 1.3.2.1 B / C / C ; 1.3.2.2 2b / 3c / 4c ; 1.3.2.3 2b / 3c / 4c  
- CTI: 1.3.2.1 A / B / B ; 1.3.2.2 1a / 2b / 3c ; 1.3.2.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.3.2.1 – Suricata rules
- T: 1.3.2.2 – Analyze an existing Suricata rule and describe what it detects
- T: 1.3.2.3 – Create or modify a basic Suricata rule

#### Mapping — 1.3.3 — YARA Rules

[Return to chapter](#133--yara-rules)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.3.1 A / B / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 1a / 2b / 3c  
- Hunter: 1.3.3.1 B / C / C ; 1.3.3.2 2b / 3c / 4c ; 1.3.3.3 2b / 3c / 4c  
- CTI: 1.3.3.1 A / B / B ; 1.3.3.2 1a / 2b / 3c ; 1.3.3.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.3.3.1 – YARA rules
- T: 1.3.3.2 – Analyze an existing YARA rule and describe what it detects
- T: 1.3.3.3 – Create or modify a basic YARA rule

#### Mapping — 1.3.4 — SIEM Rules

[Return to chapter](#134--siem-rules)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.3.4.1 A / B / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 1a / 2b / 3c  
- Hunter: 1.3.4.1 B / C / C ; 1.3.4.2 2b / 3c / 4c ; 1.3.4.3 2b / 3c / 4c  
- CTI: 1.3.4.1 A / B / B ; 1.3.4.2 1a / 2b / 3c ; 1.3.4.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.3.4.1 – SIEM rules
- T: 1.3.4.2 – Analyze an existing SIEM rule and describe what it detects
- T: 1.3.4.3 – Create a basic SIEM detection rule from log fields or a SIGMA rule

#### Mapping — 1.4.1 — Alert Context and Investigation

[Return to chapter](#141--alert-context-and-investigation)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.1.1 A / B / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- Hunter: 1.4.1.1 B / C / C ; 1.4.1.2 2b / 3c / 4c ; 1.4.1.3 2b / 3c / 4c ; 1.4.1.4 2b / 3c / 4c ; 1.4.1.5 2b / 3c / 4c ; 1.4.1.6 2b / 3c / 4c  
- CTI: 1.4.1.1 A / A / B ; 1.4.1.2 1a / 1a / 2b ; 1.4.1.3 1a / 1a / 2b ; 1.4.1.4 1a / 1a / 2b ; 1.4.1.5 1a / 1a / 1a ; 1.4.1.6 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.4.1.1 – Alert context and investigation
- T: 1.4.1.2 – Review an alert and identify which context is present and which is missing (include VirusTotal on a hash, IP, or domain you have)
- T: 1.4.1.3 – Review the alert configuration and explain what would fire
- T: 1.4.1.4 – Trace an alert to its upstream detection logic and name each hop
- T: 1.4.1.5 – Collect related endpoint logs and state what they add (or fail to add)
- T: 1.4.1.6 – Collect related PCAP and state what it adds versus the alert fields

#### Mapping — 1.4.2 — Alert Classification

[Return to chapter](#142--alert-classification)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

#### Mapping — 1.4.3 — Common False Positive Causes

[Return to chapter](#143--common-false-positive-causes)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.3.1 A / B / C ; 1.4.3.2 2b / 3c / 4c  
- Hunter: 1.4.3.1 B / C / C ; 1.4.3.2 2b / 3c / 4c  
- CTI: 1.4.3.1 A / A / B ; 1.4.3.2 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 1.4.3.1 – Common false positive causes
- T: 1.4.3.2 – Given a false positive, identify the cause class and what you would change

#### Mapping — 1.4.4 — Common Alert Categorizations

[Return to chapter](#144--common-alert-categorizations)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C ; 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C ; 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A ; 1.4.4.2 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.4.4.1 – Common alert categorizations
- T: 1.4.4.2 – Assign a category to an alert and justify why it is not the adjacent category

#### Mapping — 1.4.5 — SLA / Response Time Goals

[Return to chapter](#145--sla--response-time-goals)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.5.1 A / B / C ; 1.4.5.2 2b / 3c / 4c ; 1.4.5.3 2b / 3c / 4c  
- Hunter: 1.4.5.1 A / B / B ; 1.4.5.2 1a / 2b / 3c ; 1.4.5.3 1a / 2b / 3c  
- CTI: 1.4.5.1 A / A / A ; 1.4.5.2 1a / 1a / 1a ; 1.4.5.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 1.4.5.1 – Service Level Agreements / Response Time Goals
- T: 1.4.5.2 – Given timestamps, identify whether the start clock or the close/escalate clock is at risk
- T: 1.4.5.3 – Close or escalate an alert and record it against the correct clock

#### Mapping — 1.5.1 — Report Types

[Return to chapter](#151--report-types)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C ; 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C ; 1.5.1.2 2b / 3c / 4c  
- CTI: 1.5.1.1 B / C / C ; 1.5.1.2 3c / 4c / 4c  
**Mapped Proficiency Items:**
- K: 1.5.1.1 – Report types
- T: 1.5.1.2 – Identify the correct report type for a given situation and why it is not the adjacent type

#### Mapping — 1.5.2 — Reporting Timeline Requirements

[Return to chapter](#152--reporting-timeline-requirements)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C ; 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 A / B / B ; 1.5.2.2 2b / 3c / 4c  
- CTI: 1.5.2.1 B / C / C ; 1.5.2.2 3c / 4c / 4c  
**Mapped Proficiency Items:**
- K: 1.5.2.1 – Reporting timeline requirements
- T: 1.5.2.2 – Given timestamps, identify which report timeline applies and whether it is at risk

#### Mapping — 1.5.3 — Notification and Distribution

[Return to chapter](#153--notification-and-distribution)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C ; 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B ; 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C ; 1.5.3.2 3c / 4c / 4c  
**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

#### Mapping — 1.6 — SOC Analyst Section Summary

[Return to chapter](#16--soc-analyst-section-summary)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Module Type:** Section summary — no proficiency mapping

#### Mapping — 2.0 — Cyber Threat Intelligence: How the 2.x Block Fits Together

[Return to chapter](#20--cyber-threat-intelligence-how-the-2x-block-fits-together)

**Target Audience:** CTI Analyst (primary); SOC Analyst, Threat Hunter (secondary)  
**Module Type:** Orientation — no proficiency mapping

#### Mapping — 2.1.1 — Difference between data, information, and intelligence

[Return to chapter](#211--difference-between-data-information-and-intelligence)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.1 B / C / C ; 2.1.1.1 3c / 4c / 4c  
- Hunter: 2.1.1 A / B / B ; 2.1.1.1 1a / 2b / 3c  
- SOC: 2.1.1 A / A / A ; 2.1.1.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.1 – Difference between data, information, and intelligence
- T: 2.1.1.1 – Correctly categorize examples as data, information, or intelligence

#### Mapping — 2.1.2 — Intelligence lifecycle

[Return to chapter](#212--intelligence-lifecycle)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.2 B / C / C ; 2.1.2.1 3c / 4c / 4c  
- Hunter: 2.1.2 A / B / B ; 2.1.2.1 1a / 2b / 3c  
- SOC: 2.1.2 A / A / A ; 2.1.2.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.2 – Intelligence lifecycle
- T: 2.1.2.1 – Identify the lifecycle stage of an activity and describe the flow

#### Mapping — 2.1.3 — Intelligence Types

[Return to chapter](#213--intelligence-types)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.3 B / C / C ; 2.1.3.1 3c / 4c / 4c  
- Hunter: 2.1.3 A / B / B ; 2.1.3.1 1a / 2b / 3c  
- SOC: 2.1.3 A / A / A ; 2.1.3.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.3 – Intelligence types (strategic, operational, tactical, technical)
- T: 2.1.3.1 – Classify an intelligence product or requirement by type

#### Mapping — 2.1.4 — Intelligence Requirements

[Return to chapter](#214--intelligence-requirements)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.4 B / C / C ; 2.1.4.1 3c / 4c / 4d ; 2.1.4.2 3c / 4c / 4d ; 2.1.4.3 3c / 4c / 4c  
- Hunter: 2.1.4 A / B / B ; 2.1.4.1 1a / 2b / 3c ; 2.1.4.2 1a / 2b / 3c ; 2.1.4.3 1a / 2b / 3c  
- SOC: 2.1.4 A / A / B ; 2.1.4.1 1a / 1a / 1a ; 2.1.4.2 1a / 1a / 1a ; 2.1.4.3 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.4 – Intelligence requirements and Priority Intelligence Requirements (PIRs)
- T: 2.1.4.1 – Develop or refine intelligence requirements
- T: 2.1.4.2 – Translate stakeholder questions into clear intelligence requirements
- T: 2.1.4.3 – Explain how a given requirement drives analytic work

#### Mapping — 2.1.5 — RFI Intake and Prioritization

[Return to chapter](#215--rfi-intake-and-prioritization)

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.1.5 B / C / C ; 2.1.5.1 3c / 4c / 4d  
- Hunter: 2.1.5 A / A / B ; 2.1.5.1 1a / 1a / 2b  
- SOC: 2.1.5 A / A / A ; 2.1.5.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.5 – RFI intake and prioritization
- T: 2.1.5.1 – Receive, evaluate, and prioritize an RFI

#### Mapping — 2.1.6 — Ensuring Intelligence Is Actionable

[Return to chapter](#216--ensuring-intelligence-is-actionable)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.6 B / C / C ; 2.1.6.1 3c / 4c / 4d  
- Hunter: 2.1.6 A / B / B ; 2.1.6.1 1a / 2b / 3c  
- SOC: 2.1.6 A / A / B ; 2.1.6.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.6 – Ensuring intelligence is actionable
- T: 2.1.6.1 – Evaluate whether a piece of intelligence is actionable and explain why

#### Mapping — 2.1.7 — Tailoring Output to the Audience

[Return to chapter](#217--tailoring-output-to-the-audience)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.7 B / C / C ; 2.1.7.1 3c / 4c / 4d  
- Hunter: 2.1.7 A / B / B ; 2.1.7.1 1a / 2b / 3c  
- SOC: 2.1.7 A / A / B ; 2.1.7.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.1.7 – Tailoring output to the audience
- T: 2.1.7.1 – Adjust an intelligence product for a specified audience

#### Mapping — 2.1.8 — Attribution

[Return to chapter](#218--attribution)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.8 B / C / C ; 2.1.8.1 3c / 4c / 4d  
- Hunter: 2.1.8 A / B / B ; 2.1.8.1 1a / 2b / 3c  
- SOC: 2.1.8 A / A / A ; 2.1.8.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.8 – Attribution (purpose, confidence, types)
- T: 2.1.8.1 – Assess attribution statements for confidence and supporting evidence

#### Mapping — 2.1.9 — Collection Sources and Methods

[Return to chapter](#219--collection-sources-and-methods)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.9 B / C / C ; 2.1.9.1 3c / 4c / 4c ; 2.1.9.2 3c / 4c / 4d  
- Hunter: 2.1.9 A / B / B ; 2.1.9.1 1a / 1a / 2b ; 2.1.9.2 1a / 1a / 2b  
- SOC: 2.1.9 A / A / B ; 2.1.9.1 1a / 1a / 1a ; 2.1.9.2 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.1.9 – Collection sources and methods (OSINT, commercial, internal)
- T: 2.1.9.1 – Identify appropriate collection source classes for a given requirement
- T: 2.1.9.2 – Plan collection against an intelligence requirement

#### Mapping — 2.2.1 — Estimative language

[Return to chapter](#221--estimative-language)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.1 B / C / C ; 2.2.1.1 3c / 4c / 4c  
- Hunter: 2.2.1 A / B / B ; 2.2.1.1 1a / 2b / 3c  
- SOC: 2.2.1 A / A / A ; 2.2.1.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.2.1 – Estimative language
- T: 2.2.1.1 – Use and interpret estimative language in analytic judgments

#### Mapping — 2.2.2 — Structured Analytic Techniques

[Return to chapter](#222--structured-analytic-techniques)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.2 B / C / C ; 2.2.2.1 3c / 4c / 4d  
- Hunter: 2.2.2 A / B / B ; 2.2.2.1 1a / 2b / 3c  
- SOC: 2.2.2 A / A / A ; 2.2.2.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.2.2 – Structured analytic techniques
- T: 2.2.2.1 – Apply a structured analytic technique and select the right one for a scenario

#### Mapping — 2.2.3 — Admiralty Code

[Return to chapter](#223--admiralty-code)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.3 B / C / C ; 2.2.3.1 3c / 4c / 4d  
- Hunter: 2.2.3 A / B / B ; 2.2.3.1 1a / 2b / 3c  
- SOC: 2.2.3 A / A / B ; 2.2.3.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.2.3 – Admiralty Code / source reliability and information credibility
- T: 2.2.3.1 – Assign Admiralty Code ratings and evaluate source reliability and credibility

#### Mapping — 2.2.4 — Cognitive Biases and Mitigation

[Return to chapter](#224--cognitive-biases-and-mitigation)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.4 B / C / C ; 2.2.4.1 3c / 4c / 4d  
- Hunter: 2.2.4 A / B / B ; 2.2.4.1 1a / 2b / 3c  
- SOC: 2.2.4 A / A / A ; 2.2.4.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.2.4 – Cognitive biases and mitigation
- T: 2.2.4.1 – Identify cognitive bias in a judgment and apply a mitigation technique

#### Mapping — 2.3.1 — MITRE ATT&CK for CTI Analysis and Reporting

[Return to chapter](#231--mitre-attck-for-cti-analysis-and-reporting)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4c  
- Hunter: 2.3.1 B / C / C ; 2.3.1.1 3c / 4c / 4c  
- SOC: 2.3.1 A / B / B ; 2.3.1.1 2b / 3c / 4c  
**Mapped Proficiency Items:**
- K: 2.3.1 – MITRE ATT&CK for CTI analysis and reporting
- T: 2.3.1.1 – Map activity or reports to MITRE ATT&CK

#### Mapping — 2.3.2 — Diamond Model Application in CTI

[Return to chapter](#232--diamond-model-application-in-cti)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.2 B / C / C ; 2.3.2.1 3c / 4c / 4d  
- Hunter: 2.3.2 B / C / C ; 2.3.2.1 3c / 4c / 4d  
- SOC: 2.3.2 A / B / B ; 2.3.2.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 2.3.2 – Diamond Model application in CTI
- T: 2.3.2.1 – Apply the Diamond Model to an intelligence problem

#### Mapping — 2.3.3 — Cyber Kill Chain in Intelligence Analysis

[Return to chapter](#233--cyber-kill-chain-in-intelligence-analysis)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.3 B / C / C ; 2.3.3.1 3c / 4c / 4c  
- Hunter: 2.3.3 B / C / C ; 2.3.3.1 3c / 4c / 4c  
- SOC: 2.3.3 A / B / B ; 2.3.3.1 2b / 3c / 4c  
**Mapped Proficiency Items:**
- K: 2.3.3 – Cyber Kill Chain in intelligence analysis
- T: 2.3.3.1 – Identify the Kill Chain stage of observed or reported activity

#### Mapping — 2.4.1 — Internal Threat Intelligence Platform

[Return to chapter](#241--internal-threat-intelligence-platform)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.1 B / C / C ; 2.4.1.1 3c / 4c / 4d  
- Hunter: 2.4.1 A / B / B ; 2.4.1.1 1a / 2b / 3c  
- SOC: 2.4.1 A / A / B ; 2.4.1.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.4.1 – Internal threat intelligence platform
- T: 2.4.1.1 – Search, retrieve, and use the internal TIP for enrichment or analysis

#### Mapping — 2.4.2 — Selecting Platforms for CTI Work

[Return to chapter](#242--selecting-platforms-for-cti-work)

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.4.2 B / C / C ; 2.4.2.1 3c / 4c / 4d  
**Mapped Proficiency Items:**
- K: 2.4.2 – Selecting platforms for CTI work
- T: 2.4.2.1 – Select a source and record a question-driven CTI lookup

#### Mapping — 2.4.3 — VirusTotal Relations and Behavior

[Return to chapter](#243--virustotal-relations-and-behavior)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.3 B / C / C ; 2.4.3.1 3c / 4c / 4d  
- Hunter: 2.4.3 B / C / C ; 2.4.3.1 3c / 4c / 4d  
- SOC: 2.4.3 A / B / B ; 2.4.3.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 2.4.3 – VirusTotal Relations and Behavior
- T: 2.4.3.1 – Use Relations and Behavior to pivot and extract events

#### Mapping — 2.4.4 — ANY.RUN

[Return to chapter](#244--anyrun)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.4 B / C / C ; 2.4.4.1 3c / 4c / 4c  
- Hunter: 2.4.4 A / B / B ; 2.4.4.1 2b / 3c / 4c  
- SOC: 2.4.4 A / A / B ; 2.4.4.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.4.4 – ANY.RUN
- T: 2.4.4.1 – Search and review ANY.RUN submissions for actionable intelligence

#### Mapping — 2.4.5 — Silent Push

[Return to chapter](#245--silent-push)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.5 B / C / C ; 2.4.5.1 3c / 4c / 4d  
- Hunter: 2.4.5 A / B / B ; 2.4.5.1 2b / 3c / 4c  
- SOC: 2.4.5 A / A / B ; 2.4.5.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.4.5 – Silent Push
- T: 2.4.5.1 – Enrich an indicator and pivot in Silent Push

#### Mapping — 2.4.6 — urlscan.io

[Return to chapter](#246--urlscanio)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.4.6 B / C / C ; 2.4.6.1 3c / 4c / 4c  
- Hunter: 2.4.6 A / B / B ; 2.4.6.1 2b / 3c / 4c  
- SOC: 2.4.6 A / A / B ; 2.4.6.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.4.6 – URLScan
- T: 2.4.6.1 – Submit or retrieve a URLScan result and extract actionable intelligence

#### Mapping — 2.5.1 — IOC Handling and Enrichment Concepts

[Return to chapter](#251--ioc-handling-and-enrichment-concepts)

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.5.1 B / C / C ; 2.5.1.1 3c / 4c / 4d  
- Hunter: 2.5.1 B / C / C ; 2.5.1.1 3c / 4c / 4d  
- SOC: 2.5.1 A / B / B ; 2.5.1.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 2.5.1 – IOC handling and enrichment concepts
- T: 2.5.1.1 – Enrich and pivot on IOCs using internal and external tools

#### Mapping — 2.5.2 — Hashing and Similarity Concepts

[Return to chapter](#252--hashing-and-similarity-concepts)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.2 B / C / C ; 2.5.2.1 3c / 4c / 4d ; 2.5.2.2 3c / 4c / 4c  
- Hunter: 2.5.2 A / B / B ; 2.5.2.1 1a / 2b / 3c ; 2.5.2.2 1a / 2b / 3c  
- SOC: 2.5.2 A / A / B ; 2.5.2.1 1a / 1a / 2b ; 2.5.2.2 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.5.2 – Hashing and similarity concepts
- T: 2.5.2.1 – Use file similarity hashes to identify related samples
- T: 2.5.2.2 – Extract and interpret certificate / code-signing information from a file

#### Mapping — 2.5.3 — RDAP and WHOIS Concepts

[Return to chapter](#253--rdap-and-whois-concepts)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.3 B / C / C ; 2.5.3.1 3c / 4c / 4c  
- Hunter: 2.5.3 A / B / B ; 2.5.3.1 2b / 3c / 4c  
- SOC: 2.5.3 A / A / B ; 2.5.3.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.5.3 – RDAP and WHOIS concepts
- T: 2.5.3.1 – Query RDAP/WHOIS and interpret fields for enrichment or attribution

#### Mapping — 2.5.4 — Advanced DNS Concepts

[Return to chapter](#254--advanced-dns-concepts)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.4 B / C / C ; 2.5.4.1 3c / 4c / 4d  
- Hunter: 2.5.4 B / C / C ; 2.5.4.1 2b / 3c / 4c  
- SOC: 2.5.4 A / A / B ; 2.5.4.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.5.4 – Advanced DNS concepts (SOA and other records of intelligence value)
- T: 2.5.4.1 – Interpret an SOA record and use advanced DNS data to enrich or pivot

#### Mapping — 2.5.5 — Identifying Additional Adversary Infrastructure from Seed Indicators

[Return to chapter](#255--identifying-additional-adversary-infrastructure-from-seed-indicators)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.5 B / C / C ; 2.5.5.1 3c / 4c / 4d  
- Hunter: 2.5.5 B / C / C ; 2.5.5.1 3c / 4c / 4d  
- SOC: 2.5.5 A / B / B ; 2.5.5.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 2.5.5 – Identifying additional adversary infrastructure from seed indicators
- T: 2.5.5.1 – Pivot from a seed indicator to additional adversary infrastructure

#### Mapping — 2.5.6 — MalasadaTech Defender's ThreatMesh Framework (DTF)

[Return to chapter](#256--malasadatech-defenders-threatmesh-framework-dtf)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.6 B / C / C ; 2.5.6.1 3c / 4c / 4d ; 2.5.6.2 3c / 4c / 4d ; 2.5.6.3 3c / 4c / 4c  
- Hunter: 2.5.6 A / B / B ; 2.5.6.1 1a / 2b / 3c ; 2.5.6.2 1a / 2b / 3c ; 2.5.6.3 1a / 2b / 3c  
- SOC: 2.5.6 A / A / B ; 2.5.6.1 1a / 1a / 2b ; 2.5.6.2 1a / 1a / 2b ; 2.5.6.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.5.6 – Defender’s ThreatMesh Framework (DTF) for infrastructure discovery
- T: 2.5.6.1 – Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor
- T: 2.5.6.2 – Use a selected DTF pivot to guide the next enrichment or lookup
- T: 2.5.6.3 – Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain

#### Mapping — 2.5.7 — Correlation, Link Analysis, and Campaign Tracking

[Return to chapter](#257--correlation-link-analysis-and-campaign-tracking)

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.5.7 B / C / C ; 2.5.7.1 3c / 4c / 4d  
- Hunter: 2.5.7 B / C / C ; 2.5.7.1 1a / 2b / 3c  
- SOC: 2.5.7 A / B / B ; 2.5.7.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.5.7 – Correlation, link analysis, and campaign tracking
- T: 2.5.7.1 – Link analysis and campaign tracking

#### Mapping — 2.6.1 — Extracting Applicable TTPs from Intelligence Reports

[Return to chapter](#261--extracting-applicable-ttps-from-intelligence-reports)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- Hunter: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- SOC: 2.6.1 A / B / B ; 2.6.1.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 2.6.1 – Extracting applicable TTPs from intelligence reports
- T: 2.6.1.1 – Extract applicable TTPs from an intelligence report

#### Mapping — 2.6.2 — Threat Relevance and Organizational Impact

[Return to chapter](#262--threat-relevance-and-organizational-impact)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.2 B / C / C ; 2.6.2.1 3c / 4c / 4d  
- Hunter: 2.6.2 B / C / C ; 2.6.2.1 2b / 3c / 4c  
- SOC: 2.6.2 A / B / B ; 2.6.2.1 1a / 2b / 3c  
**Mapped Proficiency Items:**
- K: 2.6.2 – Threat relevance and organizational impact
- T: 2.6.2.1 – Assess threat relevance and potential impact to the organization

#### Mapping — 2.7.1 — Core STIX Objects

[Return to chapter](#271--core-stix-objects)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.1 B / C / C ; 2.7.1.1 3c / 4c / 4c  
- Hunter: 2.7.1 B / C / C ; 2.7.1.1 2b / 3c / 4c  
- SOC: 2.7.1 A / B / B ; 2.7.1.1 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.7.1 – Core STIX objects
- T: 2.7.1.1 – Identify and label common STIX objects in a report

#### Mapping — 2.7.2 — How STIX Objects Are Used in Intelligence Production

[Return to chapter](#272--how-stix-objects-are-used-in-intelligence-production)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d ; 2.7.2.2 3c / 4c / 4d ; 2.7.2.3 3c / 4c / 4c  
- Hunter: 2.7.2 B / C / C ; 2.7.2.1 2b / 3c / 4c ; 2.7.2.2 2b / 3c / 4c ; 2.7.2.3 2b / 3c / 4c  
- SOC: 2.7.2 A / B / B ; 2.7.2.1 1a / 1a / 2b ; 2.7.2.2 1a / 1a / 2b ; 2.7.2.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.7.2 – How STIX objects are used in intelligence production
- T: 2.7.2.1 – Create STIX-aligned relationships and explain a threat scenario
- T: 2.7.2.2 – Create and validate STIX objects
- T: 2.7.2.3 – Use TAXII for sharing and consumption of intelligence

#### Mapping — 2.7.3 — Creating Finished Intelligence Products

[Return to chapter](#273--creating-finished-intelligence-products)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.3 B / C / C ; 2.7.3.1 3c / 4c / 4d ; 2.7.3.2 3c / 4c / 4d  
- Hunter: 2.7.3 A / B / B ; 2.7.3.1 1a / 2b / 3c ; 2.7.3.2 1a / 2b / 3c  
- SOC: 2.7.3 A / A / B ; 2.7.3.1 1a / 1a / 2b ; 2.7.3.2 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.7.3 – Creating finished intelligence products
- T: 2.7.3.1 – Draft a finished product and evaluate it against standards
- T: 2.7.3.2 – Produce a threat actor profile

#### Mapping — 2.7.4 — RFI Responses and Closure

[Return to chapter](#274--rfi-responses-and-closure)

**Target Audience:** CTI Analyst (primary); Threat Hunter and SOC Analyst (supporting context)  
**Proficiency Focus:**  
- CTI: 2.7.4 B / C / C ; 2.7.4.1 3c / 4c / 4d  
- Hunter: 2.7.4 A / A / B ; 2.7.4.1 1a / 1a / 2b  
- SOC: 2.7.4 A / A / A ; 2.7.4.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.7.4 – RFI responses and closure
- T: 2.7.4.1 – Produce an evidence-based RFI response and close or record follow-up

#### Mapping — 2.7.5 — Disseminating Intelligence to the Correct Audiences

[Return to chapter](#275--disseminating-intelligence-to-the-correct-audiences)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.5 B / C / C ; 2.7.5.1 3c / 4c / 4c ; 2.7.5.2 3c / 4c / 4d ; 2.7.5.3 3c / 4c / 4c  
- Hunter: 2.7.5 A / B / B ; 2.7.5.1 1a / 2b / 3c ; 2.7.5.2 1a / 2b / 3c ; 2.7.5.3 1a / 2b / 3c  
- SOC: 2.7.5 A / A / B ; 2.7.5.1 1a / 1a / 2b ; 2.7.5.2 1a / 1a / 2b ; 2.7.5.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 2.7.5 – Disseminating intelligence to the correct audiences
- T: 2.7.5.1 – Select audience and method and apply correct handling markings
- T: 2.7.5.2 – Tailor products to different audiences
- T: 2.7.5.3 – Disseminate intelligence products through approved channels

#### Mapping — 2.8.1 — Local Intelligence Requirements and Priorities

[Return to chapter](#281--local-intelligence-requirements-and-priorities)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4c  
- Hunter: 2.8.1 A / A / B ; 2.8.1.1 1a / 1a / 2b  
- SOC: 2.8.1 A / A / A ; 2.8.1.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.8.1 – Local intelligence requirements and priorities
- T: 2.8.1.1 – Identify current local priorities and align analytic work to them

#### Mapping — 2.8.2 — Local Production and Approval Processes

[Return to chapter](#282--local-production-and-approval-processes)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4c ; 2.8.2.2 3c / 4c / 4c  
- Hunter: 2.8.2 A / A / B ; 2.8.2.1 1a / 1a / 2b ; 2.8.2.2 1a / 1a / 2b  
- SOC: 2.8.2 A / A / A ; 2.8.2.1 1a / 1a / 1a ; 2.8.2.2 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.8.2 – Local production and approval processes
- T: 2.8.2.1 – Follow the local process for requesting collection or producing and approving products
- T: 2.8.2.2 – Document and archive intelligence products according to local standards

#### Mapping — 2.8.3 — Local Dissemination Channels and Customers

[Return to chapter](#283--local-dissemination-channels-and-customers)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4c  
- Hunter: 2.8.3 A / A / B ; 2.8.3.1 1a / 1a / 2b  
- SOC: 2.8.3 A / A / A ; 2.8.3.1 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 2.8.3 – Local dissemination channels and customers
- T: 2.8.3.1 – Disseminate a product using the correct local channels and customers

#### Mapping — 2.9 — Cyber Threat Intelligence Section Summary

[Return to chapter](#29--cyber-threat-intelligence-section-summary)

**Target Audience:** CTI Analyst (primary); SOC Analyst, Threat Hunter (secondary)  
**Module Type:** Section summary — no proficiency mapping

#### Mapping — 3.0 — Threat Hunting: How the 3.x Block Fits Together

[Return to chapter](#30--threat-hunting-how-the-3x-block-fits-together)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Module Type:** Orientation — no proficiency mapping

#### Mapping — 3.1 — Purpose of Threat Hunting

[Return to chapter](#31--purpose-of-threat-hunting)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Mapped Proficiency Items:**

- K: 3.1.1 – Purpose of Threat Hunting
- T: 3.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 3.1.1.2 – Identify examples of activity that existing controls might miss

#### Mapping — 3.2.1 — Hunt Types

[Return to chapter](#321--hunt-types)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.1 B / C / C ; 3.2.1.1–3.2.1.4 3c / 4c / 4c  
- SOC: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
- CTI: 3.2.1 A / B / B ; 3.2.1.1–3.2.1.4 1a / 1a / 2b  
**Mapped Proficiency Items:**

- K: 3.2.1 – Hunt types
- T: 3.2.1.1 – Execute an intel-driven hunt
- T: 3.2.1.2 – Execute a hypothesis-driven hunt
- T: 3.2.1.3 – Execute a reactive hunt
- T: 3.2.1.4 – Execute an anomaly-based hunt

#### Mapping — 3.2.2 — Hunt Development Concepts

[Return to chapter](#322--hunt-development-concepts)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.2.2 B / C / C ; 3.2.2.1–3.2.2.3 3c / 4c / 4d  
- SOC: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 1a / 2b  
- CTI: 3.2.2 A / B / B ; 3.2.2.1–3.2.2.3 1a / 2b / 3c  
**Mapped Proficiency Items:**

- K: 3.2.2 – Hunt development concepts
- T: 3.2.2.1 – Develop and document a hunt hypothesis
- T: 3.2.2.2 – Scope and prioritize a hunt
- T: 3.2.2.3 – Identify unique patterns or behaviors suitable for hunting

#### Mapping — 3.3.1 — Tool Capabilities for Hunting

[Return to chapter](#331--tool-capabilities-for-hunting)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c  
**Mapped Proficiency Items:**

- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Perform advanced querying and pivoting in VirusTotal, ANY.RUN, urlscan.io, and Silent Push
- T: 3.3.1.2 – Extract actionable hunting leads from external tool results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

#### Mapping — 3.4.1 — Assessing CTI for Hunting Value

[Return to chapter](#341--assessing-cti-for-hunting-value)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.1 B / C / C ; 3.4.1.1 3c / 4c / 4d  
- SOC: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
- CTI: 3.4.1 A / B / B ; 3.4.1.1 1a / 2b / 3c  
**Mapped Proficiency Items:**

- K: 3.4.1 – Assessing CTI for hunting value
- T: 3.4.1.1 – Triage a CTI report: hunt / don't hunt / hand off, and say why

#### Mapping — 3.4.2 — Extracting Hunt Leads from CTI

[Return to chapter](#342--extracting-hunt-leads-from-cti)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.2 B / C / C ; 3.4.2.1–3.4.2.3 3c / 4c / 4d  
- SOC: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
- CTI: 3.4.2 A / B / B ; 3.4.2.1–3.4.2.2 1a / 2b / 3c ; 3.4.2.3 1a / 1a / 2b  
**Mapped Proficiency Items:**

- K: 3.4.2 – Extracting hunt leads from CTI
- T: 3.4.2.1 – Extract hunt-suitable TTPs from a CTI report
- T: 3.4.2.2 – Extract hunt-suitable artifacts (IOCs, patterns, behaviors)
- T: 3.4.2.3 – State the hunt question those leads support

#### Mapping — 3.4.3 — STIX as Hunt Input

[Return to chapter](#343--stix-as-hunt-input)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.3 B / C / C ; 3.4.3.1 3c / 4c / 4c ; 3.4.3.2 3c / 4c / 4d  
- SOC: 3.4.3 A / A / B ; 3.4.3.1 1a / 1a / 2b ; 3.4.3.2 1a / 1a / 2b  
- CTI: 3.4.3 A / B / B ; 3.4.3.1 1a / 2b / 3c ; 3.4.3.2 1a / 1a / 2b  
**Mapped Proficiency Items:**

- K: 3.4.3 – STIX as hunt input
- T: 3.4.3.1 – Identify hunt-relevant objects in a report or bundle
- T: 3.4.3.2 – Turn those objects into hunt leads

#### Mapping — 3.5.1 — Using MITRE ATT&CK for Hunt Planning

[Return to chapter](#351--using-mitre-attck-for-hunt-planning)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 3c / 4c / 4d  
- SOC: 3.5.1 A / B / B ; 3.5.1.1–3.5.1.2 1a / 2b / 3c ; 3.5.1.3 1a / 1a / 2b  
- CTI: 3.5.1 B / C / C ; 3.5.1.1 3c / 4c / 4c ; 3.5.1.2–3.5.1.3 2b / 3c / 4c  
**Mapped Proficiency Items:**

- K: 3.5.1 – Using MITRE ATT&CK for hunt planning and coverage analysis
- T: 3.5.1.1 – Map a hunt plan or hunt findings to MITRE ATT&CK
- T: 3.5.1.2 – Use ATT&CK to identify detection or visibility gaps
- T: 3.5.1.3 – Use ATT&CK to support hunt prioritization

#### Mapping — 3.6.1 — Persistence Techniques

[Return to chapter](#361--persistence-techniques)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.1 B / C / C ; 3.6.1.1 3c / 4c / 4c  
- SOC: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
- CTI: 3.6.1 A / B / B ; 3.6.1.1 1a / 2b / 3c  
**Mapped Proficiency Items:**

- K: 3.6.1 – Persistence techniques
- T: 3.6.1.1 – Recognize persistence techniques in logs or telemetry

#### Mapping — 3.6.2 — Privilege Escalation Techniques

[Return to chapter](#362--privilege-escalation-techniques)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.2 B / C / C ; 3.6.2.1 3c / 4c / 4c  
- SOC: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
- CTI: 3.6.2 A / B / B ; 3.6.2.1 1a / 2b / 3c  
**Mapped Proficiency Items:**

- K: 3.6.2 – Privilege escalation techniques
- T: 3.6.2.1 – Recognize privilege escalation techniques in logs or telemetry

#### Mapping — 3.6.3 — Hunt for a Specific Persistence or Privilege-Escalation Technique

[Return to chapter](#363--hunt-for-a-specific-persistence-or-privilege-escalation-technique)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.6.3 3c / 4c / 4d  
- SOC: 3.6.3 1a / 1a / 2b  
- CTI: 3.6.3 1a / 1a / 2b  
**Mapped Proficiency Items:**

- T: 3.6.3 – Hunt for specific persistence or privilege escalation techniques

#### Mapping — 3.7.1 — Hunt Control and Lead Management

[Return to chapter](#371--hunt-control-and-lead-management)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.1 B / C / C ; 3.7.1.1 3c / 4c / 4c  
- SOC: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
- CTI: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
**Mapped Proficiency Items:**

- K: 3.7.1 – Hunt control and lead management
- T: 3.7.1.1 – Follow the local process for initiating and controlling a hunt

#### Mapping — 3.7.2 — Hunt Documentation Standards

[Return to chapter](#372--hunt-documentation-standards)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.2 B / C / C ; 3.7.2.1 3c / 4c / 4c  
- SOC: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
- CTI: 3.7.2 A / A / B ; 3.7.2.1 1a / 1a / 2b  
**Mapped Proficiency Items:**

- K: 3.7.2 – Hunt documentation standards
- T: 3.7.2.1 – Document a hunt according to local standards

#### Mapping — 3.7.3 — Hunt Outputs and Hand-off

[Return to chapter](#373--hunt-outputs-and-hand-off)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.3 B / C / C ; 3.7.3.1 3c / 4c / 4c  
- SOC: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
- CTI: 3.7.3 A / A / B ; 3.7.3.1 1a / 1a / 2b  
**Mapped Proficiency Items:**

- K: 3.7.3 – Hunt outputs and hand-off
- T: 3.7.3.1 – Produce required hunt outputs and perform proper hand-off

#### Mapping — 3.8 — Threat Hunting Section Summary

[Return to chapter](#38--threat-hunting-section-summary)

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Module Type:** Section summary — no proficiency mapping

#### Mapping — 4.0 — Detection Engineering: How the 4.x Block Fits Together

[Return to chapter](#40--detection-engineering-how-the-4x-block-fits-together)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Module Type:** Orientation — no proficiency mapping

#### Mapping — 4.1 — What Detection Engineering Owns

[Return to chapter](#41--what-detection-engineering-owns)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.1 B / C / C ; 4.1.1 3c / 4c / 4c  
- SOC: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- Hunter: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
- CTI: 4.1 A / B / B ; 4.1.1 1a / 2b / 2b  
**Mapped Proficiency Items:**
- K: 4.1 – What DE owns
- T: 4.1.1 – Sort work to DE, nominator, 1.3, or block/control owner

#### Mapping — 4.2 — Making a Detection Sound and Meeting Shop Requirements

[Return to chapter](#42--making-a-detection-sound-and-meeting-shop-requirements)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.2 B / C / C ; 4.2.1 3c / 4c / 4d ; 4.2.2 3c / 4c / 4c ; 4.2.3 3c / 4c / 4c  
- SOC: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- Hunter: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- CTI: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 4.2 – Making a detection sound and meeting shop requirements
- T: 4.2.1 – Test a draft or change: what must fire and what must not
- T: 4.2.2 – Mark which shop requirements are met and which are still missing
- T: 4.2.3 – Write the close-the-loop note to the nominator

#### Mapping — 4.3 — Nominations from SOC, Hunt, and CTI

[Return to chapter](#43--nominations-from-soc-hunt-and-cti)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.3 B / C / C ; 4.3.1 3c / 4c / 4d  
- SOC: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- Hunter: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
- CTI: 4.3 A / B / B ; 4.3.1 1a / 2b / 2b  
**Mapped Proficiency Items:**
- K: 4.3 – Nominations from SOC, hunt, and CTI
- T: 4.3.1 – Review a nomination and say who finishes what

#### Mapping — 4.4 — Tune Requests from SOC

[Return to chapter](#44--tune-requests-from-soc)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.4 B / C / C ; 4.4.1 3c / 4c / 4d ; 4.4.2 3c / 4c / 4c  
- SOC: 4.4 A / B / B ; 4.4.1 1a / 2b / 3c ; 4.4.2 1a / 2b / 2b  
- Hunter: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
- CTI: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 4.4 – Tune requests from SOC
- T: 4.4.1 – Pick tune / exception / replace / leave / retire and cite why
- T: 4.4.2 – Reject/route a request that is investigation, block, or IR containment

#### Mapping — 4.5 — Hunt and Intel Packages

[Return to chapter](#45--hunt-and-intel-packages)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.5 B / C / C ; 4.5.1 3c / 4c / 4d ; 4.5.2 3c / 4c / 4c  
- SOC: 4.5 A / A / B ; 4.5.1 1a / 1a / 2b ; 4.5.2 1a / 1a / 2b  
- Hunter: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
- CTI: 4.5 A / B / B ; 4.5.1 1a / 2b / 3c ; 4.5.2 1a / 2b / 2b  
**Mapped Proficiency Items:**
- K: 4.5 – Hunt and intel packages
- T: 4.5.1 – Review a package: one add, one change, or no new rule
- T: 4.5.2 – Reject turning the package into a block list

#### Mapping — 4.6 — Detection Lifecycle

[Return to chapter](#46--detection-lifecycle)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.6 B / C / C ; 4.6.1 3c / 4c / 4d ; 4.6.2 3c / 4c / 4d  
- SOC: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- Hunter: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
- CTI: 4.6 A / A / B ; 4.6.1 1a / 1a / 2b ; 4.6.2 1a / 1a / 2b  
**Mapped Proficiency Items:**
- K: 4.6 – Detection lifecycle
- T: 4.6.1 – Call modify / retire / leave and cite the reason
- T: 4.6.2 – Given a block, decide whether the matching rule still earns its keep

#### Mapping — 4.7 — Sensor and Data Availability for Detection

[Return to chapter](#47--sensor-and-data-availability-for-detection)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.7 A / B / B ; 4.7.1 2b / 3c / 3c ; 4.7.2 2b / 3c / 3c  
- SOC: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- Hunter: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- CTI: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 4.7 – Sensor availability and performance
- T: 4.7.1 – Given “the rule never fired,” check the rule, the sensor/data path, or both
- T: 4.7.2 – Reject treating missing telemetry as proof the activity did not happen

#### Mapping — 4.8 — Site-Specific Detection Engineering Knowledge

[Return to chapter](#48--site-specific-detection-engineering-knowledge)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.8.1 B / C / C ; 4.8.1.1 3c / 4c / 4c ; 4.8.2 B / C / C ; 4.8.2.1 3c / 4c / 4c ; 4.8.2.2 3c / 4c / 4c  
- SOC: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1–4.8.2.2 1a / 1a / 1a  
- Hunter: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1–4.8.2.2 1a / 1a / 1a  
- CTI: 4.8.1 A / A / A ; 4.8.1.1 1a / 1a / 1a ; 4.8.2 A / A / A ; 4.8.2.1–4.8.2.2 1a / 1a / 1a  
**Mapped Proficiency Items:**
- K: 4.8.1 – Local detection requirements
- T: 4.8.1.1 – Align to the local requirements list
- K: 4.8.2 – Local review, deploy, and retire paths
- T: 4.8.2.1 – Follow the local path
- T: 4.8.2.2 – Distinguish verified local policy from an assumed or invented workflow

#### Mapping — 4.9 — Detection Engineering Section Summary

[Return to chapter](#49--detection-engineering-section-summary)

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Module Type:** Section summary — no proficiency mapping

#### Mapping — Course Summary – Bringing the Defensive Workflow Together

[Return to chapter](#course-summary--bringing-the-defensive-workflow-together)

**Target Audience:** SOC Analyst, CTI Analyst, Threat Hunter, Detection Engineer  
**Module Type:** Course synthesis — no proficiency mapping

## Glossary

Definitions summarize how terms are used in this course. Follow the chapter link for the fuller explanation and evidence limits.

**Activity set.** A grouping of activity supported by assessed connections. Shared infrastructure can suggest a candidate relationship before it supports this grouping. See [2.5.7](#257--correlation-link-analysis-and-campaign-tracking).

**Admiralty Code.** A notation that evaluates source reliability separately from the credibility of the information it provides. See [2.2.3](#223--admiralty-code).

**Alert.** A detection-generated item for investigation. The match identifies the rule’s condition; the investigation establishes what that activity means. See [1.4.1](#141--alert-context-and-investigation).

**Applicability.** Whether a reported behavior could operate against the organization’s technology or environment. See [2.6.1](#261--extracting-applicable-ttps-from-intelligence-reports).

**Attribution.** An assessment connecting activity to an actor or responsible entity, with the supporting evidence and uncertainty stated. See [2.1.8](#218--attribution).

**Candidate relationship.** A connection worth testing through further evidence. A shared characteristic alone does not establish common control or malicious activity. See [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators).

**Collection.** Obtaining information from selected sources to answer an intelligence requirement, while preserving provenance and limitations. See [2.1.9](#219--collection-sources-and-methods).

**Confidence.** A judgment about the strength of the evidence and reasoning supporting an assessment. It is distinct from the likelihood of the assessed proposition. See [2.2.1](#221--estimative-language).

**Correlation.** Comparing observations and relationships in context to determine which connections the evidence supports. See [2.5.7](#257--correlation-link-analysis-and-campaign-tracking).

**Data.** Recorded observations or values before sufficient context has been added to explain their relevance. See [2.1.1](#211--difference-between-data-information-and-intelligence).

**Detection lifecycle.** The work of deciding on coverage, building or changing it, validating, deploying, monitoring, and improving or retiring it. See [4.6](#46--detection-lifecycle).

**Detection nomination.** A proposed detection need with an evidence pointer that DE can evaluate and develop. See [4.3](#43--nominations-from-soc-hunt-and-cti).

**Diamond Model.** A framework connecting adversary, capability, infrastructure, and victim within the evidence available for an event. See [2.3.2](#232--diamond-model-application-in-cti).

**Dissemination.** Delivering intelligence to the appropriate recipients through approved channels with its handling requirements and context intact. See [2.7.5](#275--disseminating-intelligence-to-the-correct-audiences).

**Enrichment.** Adding context and relationships to a seed to answer a defined question, rather than accumulating unrelated tool results. See [2.5.1](#251--ioc-handling-and-enrichment-concepts).

**Estimative language.** Words used to express the assessed likelihood of a proposition while keeping that likelihood distinct from confidence. See [2.2.1](#221--estimative-language).

**Evidence boundary.** The limit of what the available observation establishes. A further conclusion needs additional evidence or an explicitly qualified assessment. See [2.1.1](#211--difference-between-data-information-and-intelligence).

**False negative.** Malicious or unauthorized activity that should have been detected under an established expectation but was missed; the classification needs supporting evidence. See [1.4.2](#142--alert-classification).

**False positive.** An alert assessed as firing on benign or authorized activity rather than the malicious or unauthorized condition under investigation. See [1.4.2](#142--alert-classification).

**Finished intelligence.** An assessed product organized for a recipient’s decision, with reasoning, evidence, uncertainty, and relevant implications. See [2.7.3](#273--creating-finished-intelligence-products).

**Handoff.** Passing a usable product to its next owner, including evidence, scope, uncertainty, and the action or decision needed. See [0.4](#04--how-work-can-move).

**Hash.** A value used to identify or compare file content. An exact hash match and a similarity result answer different questions. See [2.5.2](#252--hashing-and-similarity-concepts).

**Hunt hypothesis.** A testable expectation about activity and the evidence that should be observable within a defined scope. See [3.2.2](#322--hunt-development-concepts).

**IOC handling.** Managing indicators through their usefulness, evidence, relationships, and lifecycle, including keeping, linking, rejecting, or expiring them as appropriate. See [2.5.1](#251--ioc-handling-and-enrichment-concepts).

**Impact.** The organizational consequence if the assessed activity affects relevant assets or operations. See [2.6.2](#262--threat-relevance-and-organizational-impact).

**Information.** Observations connected with context so they describe a meaningful situation. See [2.1.1](#211--difference-between-data-information-and-intelligence).

**Intelligence.** An evaluation of information that answers a relevant question and explains the evidence’s significance for a decision. See [2.1.1](#211--difference-between-data-information-and-intelligence).

**Intelligence requirement.** A defined question or information need that directs collection and analysis toward a decision. See [2.1.4](#214--intelligence-requirements).

**Likelihood.** How probable the analyst assesses a proposition to be, expressed separately from confidence in that assessment. See [2.2.1](#221--estimative-language).

**Pivot.** Using a seed’s characteristic to discover another candidate object and recording why that relationship is worth pursuing. See [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators).

**Procedure.** The specific implementation or pattern of behavior that makes a technique observable and a hunt selective. See [3.6.3](#363--hunt-for-a-specific-persistence-or-privilege-escalation-technique).

**Provenance.** The source and context needed to trace an observation, including the object or report and relevant time. See [2.4.2](#242--selecting-platforms-for-cti-work).

**RFI closure.** Providing a usable answer with reasoning and limitations, delivering it to the requester, and recording the response and follow-up status. See [2.7.4](#274--rfi-responses-and-closure).

**RFI intake.** Receiving and evaluating a question, clarifying the decision and scope, and assigning ownership and priority. See [2.1.5](#215--rfi-intake-and-prioritization).

**Relevance.** Why a threat finding matters to this organization given its assets, exposure, and circumstances. See [2.6.2](#262--threat-relevance-and-organizational-impact).

**Sandbox observation.** Behavior recorded during a particular controlled execution. It does not automatically establish behavior in the local environment. See [2.4.4](#244--anyrun).

**Seed.** The known starting object for an enrichment or infrastructure-discovery question. See [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators).

**Sensor visibility.** What a sensor and its placement, configuration, and available fields can observe within the relevant scope. See [4.7](#47--sensor-and-data-availability-for-detection).

**Structured analytic technique.** A repeatable way to organize reasoning, expose assumptions, or compare alternatives. See [2.2.2](#222--structured-analytic-techniques).

**Threat hunting.** A bounded, evidence-driven search that tests a question beyond the work owed by an existing alert investigation. See [3.1](#31--purpose-of-threat-hunting).

**True positive.** An alert supported by evidence of the malicious or unauthorized condition being evaluated, not merely by a successful rule match. See [1.4.2](#142--alert-classification).

**Tune request.** A request to change an existing detection, supported by evidence of its current behavior and the desired improvement. See [4.4](#44--tune-requests-from-soc).

**Visibility gap.** A limit in available telemetry that prevents the intended observation; it is distinct from a detection missing activity it could observe. See [3.1](#31--purpose-of-threat-hunting).

## Acronyms and Technical Abbreviations

This list covers the recurring operational vocabulary. Product and framework names retain the meaning used in the course; identifiers such as ATT&CK technique IDs and DTF pivot IDs are explained in their chapters.

| Term | Course meaning | Chapter |
|---|---|---|
| ACH | Analysis of Competing Hypotheses | [2.2.2](#222--structured-analytic-techniques) |
| API | Application programming interface; used here for platform access and exchange | [2.7.2](#272--how-stix-objects-are-used-in-intelligence-production) |
| APT | Advanced persistent threat; an actor label still requires evidence | [2.1.8](#218--attribution) |
| AS | Autonomous system; an IP-infrastructure pivot context | [2.5.6](#256--malasadatech-defenders-threatmesh-framework-dtf) |
| ATT&CK | MITRE’s adversary-behavior knowledge base | [0.6.1](#061--mitre-attck) |
| CDN | Content delivery network; shared services affect infrastructure interpretation | [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators) |
| CTI | Cyber Threat Intelligence | [2.0](#20--cyber-threat-intelligence-how-the-2x-block-fits-together) |
| DE | Detection Engineering | [4.0](#40--detection-engineering-how-the-4x-block-fits-together) |
| DLL | Dynamic-link library; image-load and side-loading context | [1.1.6](#116--image-and-driver-load-activity) |
| DNS | Domain Name System | [1.2.3](#123--dns-engine) |
| DTF | Defender’s ThreatMesh Framework | [2.5.6](#256--malasadatech-defenders-threatmesh-framework-dtf) |
| DYA | Dixon, Yamada, & Associates; the fictional organization in A12 | [0.8](#08--environment--signal-flow) |
| EDR | Endpoint detection and response | [4.2](#42--making-a-detection-sound-and-meeting-shop-requirements) |
| FIRST | Publisher of the Traffic Light Protocol guidance cited by this course | [2.7.5](#275--disseminating-intelligence-to-the-correct-audiences) |
| FN | False negative | [1.4.2](#142--alert-classification) |
| FP | False positive | [1.4.2](#142--alert-classification) |
| FQDN | Fully qualified domain name | [2.5.4](#254--advanced-dns-concepts) |
| HKCU | HKEY_CURRENT_USER; current-user registry hive | [1.1.5](#115--registry-activity) |
| HKLM | HKEY_LOCAL_MACHINE; machine-wide registry hive | [1.1.5](#115--registry-activity) |
| HKU | HKEY_USERS; registry hives by user security identifier | [1.1.5](#115--registry-activity) |
| HTTP | Hypertext Transfer Protocol | [1.2.5](#125--http-engine) |
| HTTPS | HTTP protected by TLS | [1.2.4](#124--tls-engine) |
| IA | Information Assurance; a blocking-owner example in A12 | [0.3](#03--jobs-in-one-sentence) |
| ICANN | Organization cited for registration and RDAP transition guidance | [2.5.3](#253--rdap-and-whois-concepts) |
| ICD | Intelligence Community Directive; used in references to ICD 203 | [2.1.1](#211--difference-between-data-information-and-intelligence) |
| IOC | Indicator of compromise | [2.5.1](#251--ioc-handling-and-enrichment-concepts) |
| IP | Internet Protocol; addresses identify network endpoints in the examples | [1.1.4](#114--network-activity-endpoint) |
| IR | Incident Response | [0.3](#03--jobs-in-one-sentence) |
| JSON | JavaScript Object Notation; structured representation used in STIX examples | [2.7.2](#272--how-stix-objects-are-used-in-intelligence-production) |
| KQL | Kusto Query Language | [1.1.2](#112--process-activity) |
| MDE | Microsoft Defender for Endpoint | [1.1.2](#112--process-activity) |
| NIST | National Institute of Standards and Technology; source of incident-response references | [1.5.1](#151--report-types) |
| NS | DNS nameserver record | [2.5.4](#254--advanced-dns-concepts) |
| OASIS | Standards organization publishing the STIX and TAXII specifications cited here | [2.7.2](#272--how-stix-objects-are-used-in-intelligence-production) |
| ODNI | Office of the Director of National Intelligence; source of ICD 203 | [2.1.1](#211--difference-between-data-information-and-intelligence) |
| OSINT | Open-source intelligence | [2.1.9](#219--collection-sources-and-methods) |
| OT | Operational technology | [2.6.2](#262--threat-relevance-and-organizational-impact) |
| PADNS | Passive DNS; the abbreviation used in the course’s Silent Push guide | [2.4.5](#245--silent-push) |
| PCAP | Packet capture | [1.4.1](#141--alert-context-and-investigation) |
| PIR | Priority Intelligence Requirement | [2.1.4](#214--intelligence-requirements) |
| PRD | Pink River Dolphin; a vendor label in the fictional case, not proven attribution | [2.1.8](#218--attribution) |
| PTA | Pivot Tactic in DTF | [2.5.6](#256--malasadatech-defenders-threatmesh-framework-dtf) |
| RDAP | Registration Data Access Protocol | [2.5.3](#253--rdap-and-whois-concepts) |
| RFC | Request for Comments; the technical documents cited for DNS and related protocols | [2.5.4](#254--advanced-dns-concepts) |
| RFI | Request for Information | [2.1.5](#215--rfi-intake-and-prioritization) |
| RIR | Regional Internet Registry | [2.5.3](#253--rdap-and-whois-concepts) |
| SAN | Subject Alternative Name; certificate field used in infrastructure pivots | [2.5.6](#256--malasadatech-defenders-threatmesh-framework-dtf) |
| SCO | STIX Cyber-observable Object | [2.7.1](#271--core-stix-objects) |
| SID | Security identifier in registry context; signature identifier in a Suricata rule | [1.1.5](#115--registry-activity) |
| SIEM | Security information and event management | [1.3.4](#134--siem-rules) |
| SLA | Service-level agreement; the course distinguishes different response clocks | [1.4.5](#145--sla--response-time-goals) |
| SMTP | Simple Mail Transfer Protocol | [1.2.6](#126--smtp-engine) |
| SNI | Server Name Indication | [1.2.4](#124--tls-engine) |
| SOA | Start of Authority; DNS record | [2.5.4](#254--advanced-dns-concepts) |
| SOC | Security Operations Center | [0.2](#02--what-a-soc-is) |
| SSL | Certificate-oriented label retained in DTF’s SSL pivot tactic; see the framework context | [2.5.6](#256--malasadatech-defenders-threatmesh-framework-dtf) |
| STIX | Structured Threat Information Expression | [2.7.1](#271--core-stix-objects) |
| TAXII | Trusted Automated Exchange of Intelligence Information | [2.7.2](#272--how-stix-objects-are-used-in-intelligence-production) |
| TCP | Transmission Control Protocol | [1.2.2](#122--conn-engine) |
| TIP | Threat Intelligence Platform | [2.4.1](#241--internal-threat-intelligence-platform) |
| TLP | Traffic Light Protocol | [2.7.5](#275--disseminating-intelligence-to-the-correct-audiences) |
| TLS | Transport Layer Security | [1.2.4](#124--tls-engine) |
| TN | True negative | [1.4.2](#142--alert-classification) |
| TP | True positive | [1.4.2](#142--alert-classification) |
| TTP | Tactics, techniques, and procedures | [2.6.1](#261--extracting-applicable-ttps-from-intelligence-reports) |
| UAC | User Account Control | [3.6.2](#362--privilege-escalation-techniques) |
| UID | Unique identifier; Zeek uses a connection uid to link related records | [1.2.1](#121--zeek-concepts) |
| URI | Uniform Resource Identifier; used for the requested resource in HTTP records | [1.2.5](#125--http-engine) |
| URL | Uniform Resource Locator | [2.4.6](#246--urlscanio) |
| VT | VirusTotal | [0.7](#07--external-tools) |
| CFETP | Career Field Education and Training Plan; the proficiency legend uses this style | [Appendix B](#appendix-b--proficiency-mapping) |
| USAF | United States Air Force; named in the source proficiency-code legend | [Appendix B](#appendix-b--proficiency-mapping) |

**Other technical notation.** DNS record labels (`A`, `AAAA`, `CNAME`, `MX`, `TXT`, `SRV`, `RNAME`, and `SERIAL`) are covered in [2.5.4](#254--advanced-dns-concepts). File identifiers and similarity names (`MD5`, `SHA1`, `SHA256`, `ssdeep`, and `TLSH`) are covered in [2.5.2](#252--hashing-and-similarity-concepts). `JA3` is discussed with TLS evidence in [1.2.4](#124--tls-engine). Zeek `uid` and file identifiers are explained in [1.2.1](#121--zeek-concepts) and [1.2.7](#127--files-engine). Sigma and YARA are rule-language names; see [1.3.1](#131--sigma-rules) and [1.3.3](#133--yara-rules).

## Consolidated References and Further Reading

The following list preserves the course’s linked sources, with one entry per exact URL and links back to the chapters that use it. Chapter-level references remain beside their explanations. URLs are reproduced from the curriculum; their live availability and current platform interfaces have not been independently revalidated for this Markdown edition.

### activeresponse.org

- [Sergio Caltagirone — The Diamond Model](https://www.activeresponse.org/the-diamond-model/) — used in [0.6.2](#062--diamond-model).

### any.run

- [ANY.RUN — Features](https://any.run/features/) — used in [0.7](#07--external-tools).
- [ANY.RUN — Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/) — used in [2.4.2](#242--selecting-platforms-for-cti-work), [2.4.4](#244--anyrun).

### attack.mitre.org

- [Enterprise ATT&CK matrix](https://attack.mitre.org/matrices/enterprise/) — used in [0.6.1](#061--mitre-attck), [2.6.1](#261--extracting-applicable-ttps-from-intelligence-reports).
- [MITRE ATT&CK — PowerShell (T1059.001)](https://attack.mitre.org/techniques/T1059/001/) — used in [0.6.1](#061--mitre-attck), [2.3.1](#231--mitre-attck-for-cti-analysis-and-reporting), [2.6.1](#261--extracting-applicable-ttps-from-intelligence-reports).
- [MITRE ATT&CK — Modify Registry (T1112)](https://attack.mitre.org/techniques/T1112/) — used in [0.6.1](#061--mitre-attck).
- [MITRE ATT&CK — Registry Run Keys / Startup Folder (T1547.001)](https://attack.mitre.org/techniques/T1547/001/) — used in [0.6.1](#061--mitre-attck), [3.5.1](#351--using-mitre-attck-for-hunt-planning), [3.6.1](#361--persistence-techniques), [3.6.3](#363--hunt-for-a-specific-persistence-or-privilege-escalation-technique).
- [MITRE ATT&CK — Initial Access (TA0001)](https://attack.mitre.org/tactics/TA0001/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK — Phishing (T1566)](https://attack.mitre.org/techniques/T1566/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK — Drive-by Compromise (T1189)](https://attack.mitre.org/techniques/T1189/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK — Exploit Public-Facing Application (T1190)](https://attack.mitre.org/techniques/T1190/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK — Valid Accounts (T1078)](https://attack.mitre.org/techniques/T1078/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK — External Remote Services (T1133)](https://attack.mitre.org/techniques/T1133/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK — Trusted Relationship (T1199)](https://attack.mitre.org/techniques/T1199/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK — Supply Chain Compromise (T1195)](https://attack.mitre.org/techniques/T1195/) — used in [0.9](#09--common-initial-access-paths).
- [MITRE ATT&CK Enterprise knowledge base](https://attack.mitre.org/) — used in [2.3.1](#231--mitre-attck-for-cti-analysis-and-reporting), [2.6.1](#261--extracting-applicable-ttps-from-intelligence-reports), [3.5.1](#351--using-mitre-attck-for-hunt-planning).
- [MITRE ATT&CK – T1105 Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105/) — used in [2.3.1](#231--mitre-attck-for-cti-analysis-and-reporting).
- [T1053.005 – Scheduled Task](https://attack.mitre.org/techniques/T1053/005/) — used in [3.6.1](#361--persistence-techniques).
- [T1543.003 – Windows Service](https://attack.mitre.org/techniques/T1543/003/) — used in [3.6.1](#361--persistence-techniques), [3.6.2](#362--privilege-escalation-techniques).
- [T1548.002 – Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002/) — used in [3.6.2](#362--privilege-escalation-techniques).
- [T1134 – Access Token Manipulation](https://attack.mitre.org/techniques/T1134/) — used in [3.6.2](#362--privilege-escalation-techniques).
- [T1068 – Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/) — used in [3.6.2](#362--privilege-escalation-techniques).
- [MITRE ATT&CK – Analytics](https://attack.mitre.org/analytics/) — used in [4.7](#47--sensor-and-data-availability-for-detection).
- [MITRE ATT&CK – Data Sources deprecation notice](https://attack.mitre.org/datasources/) — used in [4.7](#47--sensor-and-data-availability-for-detection).

### cisa.gov

- [CISA — #StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide) — used in [0.9](#09--common-initial-access-paths).

### cloud.google.com

- [Mandiant, **Tracking Malware with Import Hashing**](https://cloud.google.com/blog/topics/threat-intelligence/tracking-malware-import-hashing) — used in [2.5.2](#252--hashing-and-similarity-concepts).

### csrc.nist.gov

- [NIST SP 800-61 Rev. 3 — Incident response recommendations](https://csrc.nist.gov/pubs/sp/800/61/r3/final) — used in [1.4.5](#145--sla--response-time-goals), [1.5.1](#151--report-types), [1.5.2](#152--reporting-timeline-requirements), [1.5.3](#153--notification-and-distribution).

### ctid.mitre.org

- [CTID – Continuous Emulation as Detection Validation](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/) — used in [4.2](#42--making-a-detection-sound-and-meeting-shop-requirements).

### dni.gov

- [ODNI, ICD 203 — Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) — used in [2.1.1](#211--difference-between-data-information-and-intelligence), [2.2.1](#221--estimative-language), [2.7.3](#273--creating-finished-intelligence-products).
- [ODNI – Objectivity and Analytic Standards](https://www.dni.gov/index.php/how-we-work/objectivity) — used in [2.7.3](#273--creating-finished-intelligence-products).

### docs.oasis-open.org

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html) — used in [2.5.1](#251--ioc-handling-and-enrichment-concepts), [2.5.7](#257--correlation-link-analysis-and-campaign-tracking), [2.7.1](#271--core-stix-objects), [2.7.2](#272--how-stix-objects-are-used-in-intelligence-production), [3.4.3](#343--stix-as-hunt-input).
- [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html) — used in [2.7.1](#271--core-stix-objects), [2.7.2](#272--how-stix-objects-are-used-in-intelligence-production).
- [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html) — used in [2.7.2](#272--how-stix-objects-are-used-in-intelligence-production).

### docs.suricata.io

- [Suricata — Rule format](https://docs.suricata.io/en/latest/rules/intro.html) — used in [1.3.2](#132--suricata-rules).
- [Suricata — HTTP keywords](https://docs.suricata.io/en/latest/rules/http-keywords.html) — used in [1.3.2](#132--suricata-rules).

### docs.urlscan.io

- [urlscan.io — Quickstart](https://docs.urlscan.io/guides/quickstart) — used in [2.4.2](#242--selecting-platforms-for-cti-work), [2.4.6](#246--urlscanio).

### docs.virustotal.com

- [VirusTotal — Searching](https://docs.virustotal.com/docs/searching) — used in [0.7](#07--external-tools), [1.4.1](#141--alert-context-and-investigation), [2.4.2](#242--selecting-platforms-for-cti-work).
- [VirusTotal — Private scanning](https://docs.virustotal.com/docs/private-scanning) — used in [0.7](#07--external-tools).
- [VirusTotal – Relationships](https://docs.virustotal.com/reference/relationships) — used in [2.4.3](#243--virustotal-relations-and-behavior), [3.3.1](#331--tool-capabilities-for-hunting).
- [VirusTotal – File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours) — used in [2.4.3](#243--virustotal-relations-and-behavior), [3.3.1](#331--tool-capabilities-for-hunting).

### docs.zeek.org

- [Zeek — Log files](https://docs.zeek.org/en/master/reference/zeekscript/log-files.html) — used in [1.2.1](#121--zeek-concepts).
- [Zeek — conn.log](https://docs.zeek.org/en/current/reference/logs/conn.html) — used in [1.2.1](#121--zeek-concepts), [1.2.2](#122--conn-engine).
- [Zeek — dns.log](https://docs.zeek.org/en/current/reference/logs/dns.html) — used in [1.2.3](#123--dns-engine).
- [Zeek — ssl.log](https://docs.zeek.org/en/current/reference/logs/ssl.html) — used in [1.2.4](#124--tls-engine).
- [Zeek — x509.log](https://docs.zeek.org/en/current/reference/logs/x509.html) — used in [1.2.4](#124--tls-engine).
- [Zeek — http.log](https://docs.zeek.org/en/current/reference/logs/http.html) — used in [1.2.5](#125--http-engine), [1.4.1](#141--alert-context-and-investigation).
- [Zeek — smtp.log](https://docs.zeek.org/en/current/reference/logs/smtp.html) — used in [1.2.6](#126--smtp-engine).
- [Zeek — files.log](https://docs.zeek.org/en/current/reference/logs/files.html) — used in [1.2.7](#127--files-engine).
- [Zeek — weird.log and notice.log](https://docs.zeek.org/en/current/reference/logs/weird-and-notice.html) — used in [1.2.8](#128--weird-engine).

### first.org

- [FIRST – Traffic Light Protocol](https://www.first.org/tlp/) — used in [2.7.5](#275--disseminating-intelligence-to-the-correct-audiences).
- [FIRST – TLP 2.0 Definitions and Usage Guidance](https://www.first.org/tlp/docs/tlp-a4.pdf) — used in [2.7.5](#275--disseminating-intelligence-to-the-correct-audiences).
- [FIRST – TLP Use Cases](https://www.first.org/tlp/use-cases) — used in [2.7.5](#275--disseminating-intelligence-to-the-correct-audiences).

### github.com

- [Trend Micro, **TLSH**](https://github.com/trendmicro/tlsh) — used in [2.5.2](#252--hashing-and-similarity-concepts).
- [Defender's ThreatMesh Framework](https://github.com/MalasadaTech/defenders-threatmesh-framework) — used in [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators), [2.5.6](#256--malasadatech-defenders-threatmesh-framework-dtf).
- [Current DTF matrix](https://github.com/MalasadaTech/defenders-threatmesh-framework/blob/main/matrix.md) — used in [2.5.6](#256--malasadatech-defenders-threatmesh-framework-dtf).

### help.silentpush.com

- [Silent Push — Passive DNS lookups](https://help.silentpush.com/docs/perform-passive-dns-scans-and-record-specific-lookups) — used in [0.7](#07--external-tools).
- [Silent Push — DNS Data](https://help.silentpush.com/docs/dns-data) — used in [2.4.2](#242--selecting-platforms-for-cti-work), [2.4.5](#245--silent-push), [3.3.1](#331--tool-capabilities-for-hunting).
- [Silent Push – Passive DNS and Record-Specific Lookups](https://help.silentpush.com/v1/docs/perform-passive-dns-scans-and-record-specific-lookups) — used in [2.4.5](#245--silent-push).

### icann.org

- [ICANN — Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en) — used in [2.5.3](#253--rdap-and-whois-concepts), [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators).

### intelligence.any.run

- [ANY.RUN TI Lookup Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf) — used in [2.4.4](#244--anyrun), [3.3.1](#331--tool-capabilities-for-hunting).

### learn.microsoft.com

- [Microsoft — Sysmon events](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) — used in [1.1.1](#111--endpoint-activity-the-map), [1.1.2](#112--process-activity), [1.1.3](#113--file-system-activity), [1.1.4](#114--network-activity-endpoint), [1.1.5](#115--registry-activity), [1.1.6](#116--image-and-driver-load-activity).
- [Microsoft — Advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables) — used in [1.1.1](#111--endpoint-activity-the-map).
- [Microsoft — DeviceProcessEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceprocessevents-table) — used in [1.1.2](#112--process-activity).
- [Microsoft — KQL string operators](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators) — used in [1.1.2](#112--process-activity), [1.1.3](#113--file-system-activity), [1.1.4](#114--network-activity-endpoint), [1.1.5](#115--registry-activity), [1.1.6](#116--image-and-driver-load-activity), [1.2.5](#125--http-engine), [1.3.4](#134--siem-rules).
- [Microsoft — DeviceFileEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicefileevents-table) — used in [1.1.3](#113--file-system-activity).
- [Microsoft — DeviceNetworkEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-devicenetworkevents-table) — used in [1.1.4](#114--network-activity-endpoint).
- [Microsoft — DeviceRegistryEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceregistryevents-table) — used in [1.1.5](#115--registry-activity).
- [Microsoft — DeviceImageLoadEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-deviceimageloadevents-table) — used in [1.1.6](#116--image-and-driver-load-activity).
- [Microsoft — Custom detection rules](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) — used in [1.3.4](#134--siem-rules).
- [Microsoft — Investigate and classify alerts](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts) — used in [1.4.1](#141--alert-context-and-investigation), [1.4.2](#142--alert-classification), [1.4.3](#143--common-false-positive-causes).
- [Microsoft — Alert classification playbooks](https://learn.microsoft.com/en-us/defender-xdr/alert-classification-playbooks) — used in [1.4.2](#142--alert-classification).
- [Microsoft, **Authenticode Digital Signatures**](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode) — used in [2.5.2](#252--hashing-and-similarity-concepts).

### lockheedmartin.com

- [Lockheed Martin — Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) — used in [0.6.3](#063--cyber-kill-chain), [2.3.3](#233--cyber-kill-chain-in-intelligence-analysis).
- [Lockheed Martin overview PDF](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf) — used in [2.3.3](#233--cyber-kill-chain-in-intelligence-analysis).

### mitre.org

- [MITRE — 11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) — used in [0.2](#02--what-a-soc-is), [0.3](#03--jobs-in-one-sentence), [0.4](#04--how-work-can-move), [0.5](#05--where-the-jobs-lightly-overlap), [0.8](#08--environment--signal-flow), [1.4.4](#144--common-alert-categorizations), [1.5.1](#151--report-types), [1.5.3](#153--notification-and-distribution).

### rfc-editor.org

- [RFC 9082 — RDAP Query Format](https://www.rfc-editor.org/rfc/rfc9082.html) — used in [2.5.3](#253--rdap-and-whois-concepts).
- [RFC 9083 — RDAP JSON Responses](https://www.rfc-editor.org/rfc/rfc9083.html) — used in [2.5.3](#253--rdap-and-whois-concepts).
- [RFC 3912 — WHOIS Protocol Specification](https://www.rfc-editor.org/rfc/rfc3912.html) — used in [2.5.3](#253--rdap-and-whois-concepts).
- [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html) — used in [2.5.4](#254--advanced-dns-concepts), [2.5.5](#255--identifying-additional-adversary-infrastructure-from-seed-indicators).
- [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) — used in [2.5.4](#254--advanced-dns-concepts).
- [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782.html) — used in [2.5.4](#254--advanced-dns-concepts).

### sigmahq.io

- [Sigma — Rule basics](https://sigmahq.io/docs/basics/rules.html) — used in [1.3.1](#131--sigma-rules), [1.3.4](#134--siem-rules), [1.4.3](#143--common-false-positive-causes).
- [Sigma — Conditions](https://sigmahq.io/docs/basics/conditions.html) — used in [1.3.1](#131--sigma-rules).
- [Sigma Rules – false positives and rule metadata](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html) — used in [4.2](#42--making-a-detection-sound-and-meeting-shop-requirements), [4.6](#46--detection-lifecycle), [4.8](#48--site-specific-detection-engineering-knowledge).
- [Sigma Filters](https://sigmahq.io/docs/meta/) — used in [4.2](#42--making-a-detection-sound-and-meeting-shop-requirements), [4.4](#44--tune-requests-from-soc).
- [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html) — used in [4.2](#42--making-a-detection-sound-and-meeting-shop-requirements), [4.7](#47--sensor-and-data-availability-for-detection).

### ssdeep-project.github.io

- [ssdeep project documentation](https://ssdeep-project.github.io/ssdeep/usage.html) — used in [2.5.2](#252--hashing-and-similarity-concepts).

### threatintel.academy

- [The Diamond Model of Intrusion Analysis](https://www.threatintel.academy/diamond/) — used in [2.3.2](#232--diamond-model-application-in-cti).

### urlscan.io

- [urlscan.io — FAQ](https://urlscan.io/docs/faq/) — used in [0.7](#07--external-tools).
- [urlscan.io API Documentation](https://urlscan.io/docs/api/) — used in [2.4.6](#246--urlscanio).
- [urlscan.io Result API Reference](https://urlscan.io/docs/result/) — used in [2.4.6](#246--urlscanio), [3.3.1](#331--tool-capabilities-for-hunting).

### yara.readthedocs.io

- [YARA — Writing rules](https://yara.readthedocs.io/en/stable/writingrules.html) — used in [1.3.3](#133--yara-rules).
- [YARA — Command-line input options](https://yara.readthedocs.io/en/stable/commandline.html) — used in [1.3.3](#133--yara-rules).
