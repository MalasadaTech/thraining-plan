# CTI Analyst Proficiency Matrix

**Skill Levels**
- **3** = Apprentice (Note: CTI Analyst 3-level is expected to already have solid foundational knowledge and competence)
- **5** = Journeyman (independent)
- **7** = Craftsman / Senior (can train others)

**Proficiency Codes**
- Knowledge: A (Facts) → B (Principles) → C (Analysis) → D (Evaluation)
- Task Performance: 1 (Extremely Limited) → 2 (Partially Proficient) → 3 (Competent) → 4 (Highly Proficient)
- Task Knowledge: a (Nomenclature) → b (Procedures) → c (Operating Principles) → d (Advanced Theory)

**Baseline for CTI Analyst**
- Knowledge items generally start at **B**
- Task items generally start at **3c**
- Section **0** is the shared intro (same codes as SOC, Hunter, and DE), not CTI-primary work

---

## 0 Front door

Everyone. Taught before SOC. Same idea on the SOC, hunter, and DE sheets. Not site policy.

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 0.1 | How this course is laid out | K | A | B | B | Course map. Not CTI-primary. |
| 0.2 | What a SOC is | K | A | B | B | Shared intro. Not CTI-primary; do not start at B/3c. |
| 0.3 | Jobs in one sentence | K | A | B | B | CTI is one desk among several. |
| 0.4 | How work can move | K | A | B | B | RFI and enrich are named, not taught. |
| 0.4.1 | Given a step in the flow, name the next hand-off and whose product it is | T | 1a | 2b | 2b | Name the hand-off. Do not invent a PIR or ticket. No 4d. |
| 0.5 | Where the jobs lightly overlap | K | A | B | B | Same evidence, different product. |

---

## 0.6 Frameworks (shared floor)

Taught in `00` before SOC. Advanced CTI application is **2.7**. Codes match combined.

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 0.6.1.1 | MITRE ATT&CK | K | B | C | C | Shared floor. Raised application is 2.7.1. |
| 0.6.1.2 | Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence | T | 3c | 4c | 4c | Map + cite. Not 2.7 product. |
| 0.6.2.1 | Diamond Model | K | B | C | C | Shared floor. Advanced fill is 2.7.2. |
| 0.6.2.2 | Apply the Diamond Model to an incident or set of indicators | T | 3c | 4c | 4d | Weakest vertex. 7-level when vertices compete. |
| 0.6.3.1 | Cyber Kill Chain | K | B | C | C | Shared floor. Advanced staging is 2.7.3. |
| 0.6.3.2 | Identify the Kill Chain stage of observed activity | T | 3c | 4c | 4c | Stage + reject neighbor. |

---

## 2.1 Core Intelligence Concepts

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.1.1 | Difference between data, information, and intelligence | K | B | C | C | Foundation. CTI 3 should already know the distinction at a principles level. |
| 2.1.1.1 | Correctly categorize examples as data, information, or intelligence | T | 3c | 4c | 4c | Direct application of 2.1.1. Competent at 3-level. |
| 2.1.2 | Intelligence lifecycle | K | B | C | C | CTI 3 should understand stages and purpose at a principles level. |
| 2.1.2.1 | Identify the lifecycle stage of an activity and describe the flow | T | 3c | 4c | 4c | Practical mapping of work to the lifecycle. |
| 2.1.3 | Intelligence types (strategic, operational, tactical, technical) | K | B | C | C | Raised baseline. 5/7 analyze which type a problem needs. |
| 2.1.3.1 | Classify an intelligence product or requirement by type | T | 3c | 4c | 4c | Direct application of 2.1.3. |
| 2.1.4 | Intelligence requirements and Priority Intelligence Requirements (PIRs) | K | B | C | C | CTI 3 should already understand principles of PIRs. Higher levels analyze and refine them. |
| 2.1.4.1 | Develop or refine intelligence requirements | T | 3c | 4c | 4d | Core skill. 7-level can apply advanced judgment and align with strategic needs. |
| 2.1.4.2 | Translate stakeholder questions into clear intelligence requirements | T | 3c | 4c | 4d | High-value analytical skill that improves with seniority. |
| 2.1.4.3 | Explain how a given requirement drives analytic work | T | 3c | 4c | 4c | Ties requirements to collection and production. |
| 2.1.5 | Ensuring intelligence is actionable | K | B | C | C | CTI 3 should know what “actionable” means and why products fail. |
| 2.1.5.1 | Evaluate whether a piece of intelligence is actionable and explain why | T | 3c | 4c | 4d | Judgment-heavy; 7-level applies advanced criteria. |
| 2.1.6 | Tailoring output to the audience | K | B | C | C | Raised baseline. Production depth continues in 2.11. |
| 2.1.6.1 | Adjust an intelligence product for a specified audience | T | 3c | 4c | 4d | Communication skill that improves with seniority. |
| 2.1.7 | Attribution (purpose, confidence, types) | K | B | C | C | CTI 3 should understand principles and limits of attribution. |
| 2.1.7.1 | Assess attribution statements for confidence and supporting evidence | T | 3c | 4c | 4d | Analytic judgment expected to deepen at 7-level. |
| 2.1.8 | Collection sources and methods (OSINT, commercial, internal) | K | B | C | C | Expands the collection stage of the lifecycle and how requirements drive collection. |
| 2.1.8.1 | Identify appropriate collection source classes for a given requirement | T | 3c | 4c | 4c | Direct application of 2.1.8. |
| 2.1.8.2 | Plan collection against an intelligence requirement | T | 3c | 4c | 4d | Planning skill; local request process is 2.12.4. |

---

## 2.2 Analytic Tradecraft

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.2.1 | Estimative language | K | B | C | C | CTI 3 should already use estimative terms at a principles level. |
| 2.2.1.1 | Use and interpret estimative language in analytic judgments | T | 3c | 4c | 4c | Daily writing skill. Highly proficient by 5-level. |
| 2.2.2 | Structured analytic techniques | K | B | C | C | Raised baseline (ACH, key assumptions check, and when to use them). |
| 2.2.2.1 | Apply a structured analytic technique and select the right one for a scenario | T | 3c | 4c | 4d | Advanced tradecraft; 7-level applies theory and teaches others. |
| 2.2.3 | Admiralty Code / source reliability and information credibility | K | B | C | C | CTI 3 should know both scales and how they combine. |
| 2.2.3.1 | Assign Admiralty Code ratings and evaluate source reliability and credibility | T | 3c | 4c | 4d | Critical CTI skill. 7-level applies advanced source-evaluation theory. |
| 2.2.4 | Cognitive biases and mitigation | K | B | C | C | Raised baseline. |
| 2.2.4.1 | Identify cognitive bias in a judgment and apply a mitigation technique | T | 3c | 4c | 4d | Judgment-heavy; deepens at 7-level. |

---

## 2.3 Tools

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.3.1 | Internal threat intelligence platform | K | B | C | C | CTI 3 should understand purpose, navigation, and how the TIP supports work. |
| 2.3.1.1 | Search, retrieve, and use the internal TIP for enrichment or analysis | T | 3c | 4c | 4d | Core platform skill. 7-level develops more sophisticated workflows. |
| 2.3.2 | External tools (VirusTotal, AnyRun, Silent Push, URLScan) | K | B | C | C | Shared floor: purpose and when to pick. Platform depth is 2.9. |
| 2.3.2.1 | Select the appropriate external tool for a given enrichment or analysis need | T | 3c | 4c | 4d | Select on the shared floor. Advanced pivot is 2.9. |

---

## 2.4 File Similarity & Hashing Techniques

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.4.1 | Hashing and similarity concepts (imphash, ssdeep, TLSH, code-signing certificates) | K | B | C | C | CTI 3 should understand purpose and use case of each. |
| 2.4.1.1 | Use file similarity hashes to identify related samples | T | 3c | 4c | 4d | Practical pivoting skill; 7-level applies advanced matching judgment. |
| 2.4.1.2 | Extract and interpret certificate / code-signing information from a file | T | 3c | 4c | 4c | Direct application of 2.4.1. |

---

## 2.5 RDAP / WHOIS

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.5.1 | RDAP and WHOIS concepts | K | B | C | C | Purpose, differences, and fields useful for enrichment and attribution. |
| 2.5.1.1 | Query RDAP/WHOIS and interpret fields for enrichment or attribution | T | 3c | 4c | 4c | Competent at 3-level; highly proficient thereafter. |

---

## 2.6 Advanced DNS

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.6.1 | Advanced DNS concepts (SOA and other records of intel value) | K | B | C | C | How advanced DNS supports enrichment and infrastructure analysis. |
| 2.6.1.1 | Interpret an SOA record and use advanced DNS data to enrich or pivot | T | 3c | 4c | 4d | 7-level applies more advanced infrastructure-analysis judgment. |

---

## 2.7 Frameworks

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.7.1 | MITRE ATT&CK for CTI analysis and reporting | K | B | C | C | Raised baseline; advanced application vs SOC 0.6. |
| 2.7.1.1 | Map activity or reports to MITRE ATT&CK | T | 3c | 4c | 4c | Practical mapping skill. |
| 2.7.2 | Diamond Model application in CTI | K | B | C | C | Same knowledge progression. |
| 2.7.2.1 | Apply the Diamond Model to an intelligence problem | T | 3c | 4c | 4d | Analytical application skill. |
| 2.7.3 | Cyber Kill Chain in intelligence analysis | K | B | C | C | Same knowledge progression. |
| 2.7.3.1 | Identify the Kill Chain stage of observed or reported activity | T | 3c | 4c | 4c | Direct application of 2.7.3. |
| 2.7.4 | Defender’s ThreatMesh Framework (DTF) for infrastructure discovery | K | B | C | C | Purpose, PTA/P components, and relationship to other frameworks. |
| 2.7.4.1 | Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor | T | 3c | 4c | 4d | Distinct local framework; 7-level refines distinctive vs weak pivot. |
| 2.7.4.2 | Use a selected DTF pivot to guide the next enrichment or lookup | T | 3c | 4c | 4d | Ties DTF IDs to 2.8 lookup work. |
| 2.7.4.3 | Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain | T | 3c | 4c | 4c | Required outline task. |

---

## 2.8 Enrichment & Analysis

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.8.1 | Identifying additional adversary infrastructure from seed indicators | K | B | C | C | Pivoting concepts and common data sources. |
| 2.8.1.1 | Pivot from a seed indicator to additional adversary infrastructure | T | 3c | 4c | 4d | Core operational skill. 7-level develops advanced enrichment workflows. |
| 2.8.2 | Extracting applicable TTPs from intelligence reports | K | B | C | C | How to find TTPs and judge applicability to the environment. |
| 2.8.2.1 | Extract applicable TTPs from an intelligence report | T | 3c | 4c | 4d | Higher-value analytical task. |
| 2.8.3 | IOC handling and enrichment concepts | K | B | C | C | Supports 2.8.1; raised baseline. |
| 2.8.3.1 | Enrich and pivot on IOCs using internal and external tools | T | 3c | 4c | 4d | Same family as 2.8.1.1. |
| 2.8.3.2 | Link analysis and campaign tracking | T | 3c | 4c | 4d | Supports infrastructure and TTP enrichment; not a separate outline unit. |
| 2.8.4 | Threat relevance and organizational impact | K | B | C | C | Whether a finding matters here, not only whether it is technically interesting. |
| 2.8.4.1 | Assess threat relevance and potential impact to the organization | T | 3c | 4c | 4d | Judgment-heavy “so what” of enrichment and TTP applicability. |

---

## 2.9 Platform-Specific Skills

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.9.1 | VirusTotal (Relations and Behavior tabs) | K | B | C | C | Relations for infrastructure; Behavior for host/network events. |
| 2.9.1.1 | Use VirusTotal Relations and Behavior to pivot and extract events | T | 3c | 4c | 4d | Platform depth beyond 2.3. |
| 2.9.2 | AnyRun | K | B | C | C | Search by tag/IP/domain/hash; review for actionable intel. |
| 2.9.2.1 | Search and review AnyRun submissions for actionable intelligence | T | 3c | 4c | 4c | Competent at 3-level. |
| 2.9.3 | Silent Push | K | B | C | C | Core capabilities and pivoting. |
| 2.9.3.1 | Enrich an indicator and pivot in Silent Push | T | 3c | 4c | 4d | 7-level applies more advanced pivot paths. |
| 2.9.4 | URLScan | K | B | C | C | Capabilities and how to read results for intel value. |
| 2.9.4.1 | Submit or retrieve a URLScan result and extract actionable intelligence | T | 3c | 4c | 4c | Direct application of 2.9.4. |

---

## 2.10 Common STIX Objects

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.10.1 | Core STIX objects | K | B | C | C | Indicator, Observed Data, Malware, Attack Pattern, Threat Actor, Intrusion Set, Campaign, CoA, Identity, Relationship, Sighting. |
| 2.10.1.1 | Identify and label common STIX objects in a report | T | 3c | 4c | 4c | Required outline task. |
| 2.10.2 | How STIX objects are used in intelligence production | K | B | C | C | Structuring for sharing and automation; linking objects. |
| 2.10.2.1 | Create STIX-aligned relationships and explain a threat scenario | T | 3c | 4c | 4d | 7-level designs more complex object graphs. |
| 2.10.2.2 | Create and validate STIX objects | T | 3c | 4c | 4d | Technical production skill carried from the prior matrix. |
| 2.10.2.3 | Use TAXII for sharing and consumption of intelligence | T | 3c | 4c | 4c | Supports outline “sharing and automation”; not a separate outline heading. |

---

## 2.11 Intelligence Production & Dissemination

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.11.1 | Creating finished intelligence products | K | B | C | C | Types, structure, required elements, quality standards. |
| 2.11.1.1 | Draft a finished product and evaluate it against standards | T | 3c | 4c | 4d | Core production skill. Quality increases with seniority. |
| 2.11.1.2 | Produce a threat actor profile | T | 3c | 4c | 4d | Finished-product form of 2.1.7 attribution. 7-level produces more nuanced profiles. |
| 2.11.2 | Disseminating intelligence to the correct audiences | K | B | C | C | Audience, approved methods, handling caveats and markings. |
| 2.11.2.1 | Select audience and method and apply correct handling markings | T | 3c | 4c | 4c | Operational dissemination skill. |
| 2.11.2.2 | Tailor products to different audiences (technical, leadership, etc.) | T | 3c | 4c | 4d | Builds on 2.1.6 / 2.1.6.1. |
| 2.11.2.3 | Disseminate intelligence products through approved channels | T | 3c | 4c | 4c | Highly proficient by 5-level. |
| 2.11.3 | Handling RFIs | K | B | C | C | Purpose, lifecycle, evaluate / prioritize / respond. |
| 2.11.3.1 | Evaluate, prioritize, and produce a response to an RFI | T | 3c | 4c | 4d | Judgment-heavy customer-facing task. |

---

## 2.12 Site-Specific CTI Knowledge and Tasks

| # | Item | Type | CTI 3 | CTI 5 | CTI 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 2.12.1 | Local intelligence requirements and priorities | K | B | C | C | Current local PIRs and how they drive analytic focus. |
| 2.12.1.1 | Identify current local priorities and align analytic work to them | T | 3c | 4c | 4c | Must be competent from 3-level up. |
| 2.12.2 | Local production and approval processes | K | B | C | C | Workflow, reviews, and approval authorities. |
| 2.12.2.1 | Follow the local process for requesting collection or producing and approving products | T | 3c | 4c | 4c | Site ticket/process. Planning the collection itself is 2.1.8.2. |
| 2.12.2.2 | Document and archive intelligence products according to local standards | T | 3c | 4c | 4c | Same as prior site-specific archive task. |
| 2.12.3 | Local dissemination channels and customers | K | B | C | C | Primary customers and approved channels. |
| 2.12.3.1 | Disseminate a product using the correct local channels and customers | T | 3c | 4c | 4c | Direct application of 2.12.3. |
