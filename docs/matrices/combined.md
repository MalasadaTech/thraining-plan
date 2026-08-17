# Combined Proficiency Matrix  
## SOC Analyst | Threat Hunter | CTI Analyst | Detection Engineer

**Skill Levels**
- **3** = Apprentice
- **5** = Journeyman
- **7** = Craftsman / Senior

**Proficiency Codes**
- Knowledge: A → B → C → D
- Task: 1a → 2b → 3c → 4c / 4d

**Cross-Role Guidance**
- Primary role keeps the detailed ratings developed earlier.
- Non-primary roles receive minimal awareness ratings: **A** (Knowledge) or **1a** (Task) unless the skill has clear shared value.
- "—" means the item is not applicable / no requirement for that role.

Headings use **teaching-unit IDs** (`0.1`, `1.1`, `1.2`, `2.1`, `3.1`, `4.1`, …). Those match the `#` column. Do not assign work by old display numbers (there is no “section 7 = all hunting”).

Section **0** includes Detection Engineer (same codes as the other roles). Sections **1–3** stay three columns until we rate DE on those items. Section **4** has a Detection Engineer column.

---

## 0 How a SOC can operate (all roles)

Shared intro. Same codes for SOC, Hunter, CTI, and DE. Firewall / IA and IR are hand-offs, not scored jobs. DYA / PRD are course fiction, not site policy.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 | DE 3/5/7 |
|---|------|------|-----------|--------------|-----------|----------|
| 0.1 | What a SOC is | K | A / B / B | A / B / B | A / B / B | A / B / B |
| 0.2 | Jobs in one sentence | K | A / B / B | A / B / B | A / B / B | A / B / B |
| 0.3 | How work can move | K | A / B / B | A / B / B | A / B / B | A / B / B |
| 0.4 | Where the jobs lightly overlap | K | A / B / B | A / B / B | A / B / B | A / B / B |
| 0.5 | How this course is laid out | K | A / B / B | A / B / B | A / B / B | A / B / B |
| 0.5.1 | Given a step in the flow, name the next hand-off and whose product it is | T | 1a / 2b / 2b | 1a / 2b / 2b | 1a / 2b / 2b | 1a / 2b / 2b |

---

## 1.1 Endpoint Logs & Telemetry Analysis (Primarily SOC)

Host-observed activity (Sysmon / MDE). Protocol deep-dive is 1.2 Zeek.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.1.1.1 | Endpoint activity (the map) | K | A / B / B | A / B / B | A / A / A |
| 1.1.1.2 | Given a one-line description, name the activity type | T | 1a / 2b / 2b | 1a / 1a / 2b | 1a / 1a / 1a |
| 1.1.2.1 | Process activity concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.2.2 | Analyze a process event (Sysmon or MDE) and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.2.3 | Create a SIEM query to detect specific process activity | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.3.1 | File system activity concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.3.2 | Analyze a file event (Sysmon or MDE) and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.3.3 | Create a SIEM query to detect specific file operations | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.4.1 | Network activity (endpoint) concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.4.2 | Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.4.3 | Create a SIEM query to detect specific endpoint network activity | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.5.1 | Registry activity concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.5.2 | Analyze a registry event (Sysmon or MDE) and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.5.3 | Create a SIEM query to detect specific registry operations | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.6.1 | Image and driver load activity concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.6.2 | Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.6.3 | Create a SIEM query to detect specific image or driver load activity | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

---

## 1.2 Zeek & Network Telemetry (Primarily SOC + Hunter)

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.2.1.1 | Zeek concepts | K | A / B / C | B / C / C | A / B / B |
| 1.2.2.1 | Conn engine | K | A / B / C | B / C / C | A / A / B |
| 1.2.2.2 | Analyze a Zeek conn log and accurately describe what occurred | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.2.3 | Create a SIEM query to detect specific connection activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.3.1 | DNS engine | K | A / B / C | B / C / C | A / B / B |
| 1.2.3.2 | Analyze a Zeek DNS log and accurately describe what occurred | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |
| 1.2.3.3 | Create a SIEM query to detect specific DNS activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |
| 1.2.4.1 | TLS engine | K | A / B / C | B / C / C | A / A / B |
| 1.2.4.2 | Analyze a Zeek TLS log and accurately describe what occurred | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.4.3 | Create a SIEM query to detect specific TLS activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.5.1 | HTTP engine | K | A / B / C | B / C / C | A / B / B |
| 1.2.5.2 | Analyze a Zeek HTTP log and accurately describe what occurred | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |
| 1.2.5.3 | Create a SIEM query to detect specific HTTP activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |
| 1.2.6.1 | SMTP engine | K | A / B / C | B / C / C | A / A / B |
| 1.2.6.2 | Analyze a Zeek SMTP log and accurately describe what occurred | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.6.3 | Create a SIEM query to detect specific SMTP activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.7.1 | Files engine | K | A / B / C | B / C / C | A / A / B |
| 1.2.7.2 | Analyze a Zeek files log and accurately describe what occurred | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.7.3 | Create a SIEM query to detect specific file transfer activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.2.8.1 | Weird engine | K | A / B / C | B / C / C | A / A / A |
| 1.2.8.2 | Analyze a Zeek weird log and accurately describe what occurred | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 1a |
| 1.2.8.3 | Create a SIEM query to detect specific weird activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 1a |

---

## 1.3 Detection Engineering (Primarily SOC)

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.3.1.1 | SIGMA rules | K | A / B / C | B / C / C | A / B / B |
| 1.3.1.2 | Analyze an existing SIGMA rule and describe what it detects | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.3.1.3 | Create or modify a basic SIGMA rule | T | 1a / 2b / 3c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.3.2.1 | Suricata rules | K | A / B / C | B / C / C | A / B / B |
| 1.3.2.2 | Analyze an existing Suricata rule and describe what it detects | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.3.2.3 | Create or modify a basic Suricata rule | T | 1a / 2b / 3c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.3.3.1 | YARA rules | K | A / B / C | B / C / C | A / B / B |
| 1.3.3.2 | Analyze an existing YARA rule and describe what it detects | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.3.3.3 | Create or modify a basic YARA rule | T | 1a / 2b / 3c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.3.4.1 | SIEM rules | K | A / B / C | B / C / C | A / B / B |
| 1.3.4.2 | Analyze an existing SIEM rule and describe what it detects | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.3.4.3 | Create a basic SIEM detection rule from log fields or a SIGMA rule | T | 1a / 2b / 3c | 2b / 3c / 4c | 1a / 1a / 2b |

---

## 1.4 Alert Handling (Primarily SOC)

Five teaching units. Tasks apply the knowledge item they sit under. False-positive *causes* are **1.4.3**, not a second K row under classification. Detection authoring is 1.3.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.4.1.1 | Alert context and investigation | K | A / B / C | B / C / C | A / A / B |
| 1.4.1.2 | Review an alert and identify which context is present and which is missing | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.3 | Review the alert configuration and explain what would fire | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.4 | Trace an alert to its upstream detection logic and name each hop | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.5 | Collect related endpoint logs and state what they add (or fail to add) | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.1.6 | Collect related PCAP and state what it adds versus the alert fields | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.2.1 | Alert classification (TP/FP/TN/FN) | K | A / B / C | B / C / C | A / A / B |
| 1.4.2.2 | Classify given cases as TP, FP, TN, or FN and cite the evidence | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.3.1 | Common false positive causes | K | A / B / C | B / C / C | A / A / B |
| 1.4.3.2 | Given a false positive, identify the cause class and what you would change | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.4.1 | Common alert categorizations | K | A / B / C | B / C / C | A / A / A |
| 1.4.4.2 | Assign a category to an alert and justify why it is not the adjacent category | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.5.1 | Service Level Agreements / Response Time Goals | K | A / B / C | A / B / B | A / A / A |
| 1.4.5.2 | Given timestamps, identify whether the start clock or the close/escalate clock is at risk | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.4.5.3 | Close or escalate an alert and record it against the correct clock | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

---

## 1.5 Frameworks (Shared across all roles)

Three teaching units. Outline tasks nest under each K (`1.5.1` + `1.5.1.1`). Hunt planning with ATT&CK is **2.5**. Actor profiles are **3.11**.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.5.1.1 | MITRE ATT&CK | K | A / B / C | B / C / C | B / C / C |
| 1.5.1.2 | Map an alert or observed activity to MITRE ATT&CK tactics/techniques | T | 2b / 3c / 4c | 3c / 4c / 4c | 3c / 4c / 4c |
| 1.5.2.1 | Diamond Model | K | A / B / C | B / C / C | B / C / C |
| 1.5.2.2 | Apply the Diamond Model to an incident or set of indicators | T | 2b / 3c / 4c | 3c / 4c / 4d | 3c / 4c / 4d |
| 1.5.3.1 | Cyber Kill Chain | K | A / B / C | B / C / C | B / C / C |
| 1.5.3.2 | Identify the Kill Chain stage of observed activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 3c / 4c / 4c |

---

## 1.6 Reporting (Primarily SOC)

Three teaching units. Tasks apply the knowledge they sit under. Shift-change reports are **1.7**. Alert SLA clocks are **1.4.5**.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.6.1.1 | Report types | K | A / B / C | B / C / C | B / C / C |
| 1.6.1.2 | Identify the correct report type for a given situation and why it is not the adjacent type | T | 2b / 3c / 4c | 2b / 3c / 4c | 3c / 4c / 4c |
| 1.6.2.1 | Reporting timeline requirements | K | A / B / C | A / B / B | B / C / C |
| 1.6.2.2 | Given timestamps, identify which report timeline applies and whether it is at risk | T | 2b / 3c / 4c | 2b / 3c / 4c | 3c / 4c / 4c |
| 1.6.3.1 | Notification and distribution | K | A / B / C | A / B / B | B / C / C |
| 1.6.3.2 | Route a report: name recipients, leadership awareness, and the approved channel | T | 2b / 3c / 4c | 2b / 3c / 4c | 3c / 4c / 4c |

---

## 1.7 Shift Change (Primarily SOC)

Two teaching units. Tasks apply the knowledge they sit under. Reporting products are **1.6**. Site-specific ops are **1.8**.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.7.1.1 | Shift changeover process | K | A / B / C | A / B / B | A / A / A |
| 1.7.1.2 | Conduct or participate in a shift changeover | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.7.2.1 | Required content of the changeover report | K | A / B / C | A / B / B | A / A / A |
| 1.7.2.2 | Produce a complete changeover report that includes all required elements | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

---

## 1.8 Site-Specific Operational Knowledge (Mixed)

Five teaching units. Classroom cards are stand-ins. IR process is **1.8.5**, not notes. Reporting products are **1.6**. Shift change is **1.7**.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.8.1.1 | Environment orientation | K | A / B / C | B / C / C | A / B / B |
| 1.8.1.2 | Identify which orientation fact applies and why it is not the adjacent fact | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 2b / 3c |
| 1.8.2.1 | How to download PCAP | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.8.2.2 | What tool to use to view PCAP | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.8.3.1 | How to access required tools and their URLs | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.3.2 | How to request tools to be installed | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.3.3 | How to request access (e.g., SIEM) | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.4.1 | Where and how to save investigation notes | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.5.1 | Follow site-specific incident response processes | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |

---

## 2.1 Purpose of Threat Hunting

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.1.1 | Purpose of Threat Hunting | K | A / B / B | B / C / C | A / B / B |
| 2.1.1.1 | Explain the purpose of threat hunting in the context of the security program | T | 1a / 2b / 3c | 3c / 4c / 4c | 1a / 2b / 3c |
| 2.1.1.2 | Identify examples of activity that existing controls might miss | T | 1a / 2b / 3c | 3c / 4c / 4d | 1a / 2b / 3c |

---

## 2.2 Hunt Methodology

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.2.1 | Hunt types | K | A / B / B | B / C / C | A / B / B |
| 2.2.1.1 | Execute an intel-driven hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.2.1.2 | Execute a hypothesis-driven hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.2.1.3 | Execute a reactive hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.2.1.4 | Execute an anomaly-based hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.2.2 | Hunt development concepts | K | A / B / B | B / C / C | A / B / B |
| 2.2.2.1 | Develop and document a hunt hypothesis | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.2.2.2 | Scope and prioritize a hunt | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.2.2.3 | Identify unique patterns or behaviors suitable for hunting | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 2b / 3c |

---

## 2.3 Online Tools & Enrichment

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.3.1 | Tool capabilities for hunting | K | A / B / B | B / C / C | A / B / B |
| 2.3.1.1 | Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push | T | 1a / 2b / 3c | 3c / 4c / 4d | 2b / 3c / 4c |
| 2.3.1.2 | Extract actionable hunting leads from external tool results | T | 1a / 2b / 3c | 3c / 4c / 4d | 2b / 3c / 4c |
| 2.3.1.3 | Convert external findings into precise internal SIEM or Zeek queries | T | 1a / 2b / 3c | 3c / 4c / 4d | 1a / 2b / 3c |

---

## 2.4 CTI for Hunters

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.4.1 | Assessing CTI for hunting value | K | A / B / B | B / C / C | A / B / B |
| 2.4.1.1 | Triage a CTI report: hunt / don’t hunt / hand off, and say why | T | 1a / 2b / 3c | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.4.2 | Extracting hunt leads from CTI | K | A / B / B | B / C / C | A / B / B |
| 2.4.2.1 | Extract hunt-suitable TTPs from a CTI report | T | 1a / 2b / 3c | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.4.2.2 | Extract hunt-suitable artifacts (IOCs, patterns, behaviors) | T | 1a / 2b / 3c | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.4.2.3 | State the hunt question those leads support | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 1a / 2b |
| 2.4.3 | STIX as hunt input | K | A / A / B | B / C / C | A / B / B |
| 2.4.3.1 | Identify hunt-relevant objects in a report or bundle | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 2b / 3c |
| 2.4.3.2 | Turn those objects into hunt leads | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 1a / 2b |

---

## 2.5 Framework Application for Hunting

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.5.1 | Using MITRE ATT&CK for hunt planning and coverage analysis | K | A / B / B | B / C / C | B / C / C |
| 2.5.1.1 | Map a hunt plan or hunt findings to MITRE ATT&CK | T | 1a / 2b / 3c | 3c / 4c / 4c | 3c / 4c / 4c |
| 2.5.1.2 | Use ATT&CK to identify detection or visibility gaps | T | 1a / 2b / 3c | 3c / 4c / 4d | 2b / 3c / 4c |
| 2.5.1.3 | Use ATT&CK to support hunt prioritization | T | 1a / 1a / 2b | 3c / 4c / 4d | 2b / 3c / 4c |

---

## 2.6 Attacker Techniques

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.6.1 | Persistence techniques | K | A / B / B | B / C / C | A / B / B |
| 2.6.1.1 | Recognize persistence techniques in logs or telemetry | T | 1a / 2b / 3c | 3c / 4c / 4c | 1a / 2b / 3c |
| 2.6.2 | Privilege escalation techniques | K | A / B / B | B / C / C | A / B / B |
| 2.6.2.1 | Recognize privilege escalation techniques in logs or telemetry | T | 1a / 2b / 3c | 3c / 4c / 4c | 1a / 2b / 3c |
| 2.6.3 | Hunt for specific persistence or privilege escalation techniques | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 1a / 2b |

---

## 2.7 Site-Specific Hunt Knowledge and Tasks

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.7.1 | Hunt control and lead management | K | A / A / B | B / C / C | A / A / B |
| 2.7.1.1 | Follow the local process for initiating and controlling a hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.7.2 | Hunt documentation standards | K | A / A / B | B / C / C | A / A / B |
| 2.7.2.1 | Document a hunt according to local standards | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.7.3 | Hunt outputs and hand-off | K | A / A / B | B / C / C | A / A / B |
| 2.7.3.1 | Produce required hunt outputs and perform proper hand-off | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |

---

## 3.1 Core Intelligence Concepts

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.1.1 | Difference between data, information, and intelligence | K | A / A / A | A / B / B | B / C / C |
| 3.1.1.1 | Correctly categorize examples as data, information, or intelligence | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4c |
| 3.1.2 | Intelligence lifecycle | K | A / A / A | A / B / B | B / C / C |
| 3.1.2.1 | Identify the lifecycle stage of an activity and describe the flow | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4c |
| 3.1.3 | Intelligence types (strategic, operational, tactical, technical) | K | A / A / A | A / B / B | B / C / C |
| 3.1.3.1 | Classify an intelligence product or requirement by type | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4c |
| 3.1.4 | Intelligence requirements and Priority Intelligence Requirements (PIRs) | K | A / A / B | A / B / B | B / C / C |
| 3.1.4.1 | Develop or refine intelligence requirements | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.1.4.2 | Translate stakeholder questions into clear intelligence requirements | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.1.4.3 | Explain how a given requirement drives analytic work | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4c |
| 3.1.5 | Ensuring intelligence is actionable | K | A / A / B | A / B / B | B / C / C |
| 3.1.5.1 | Evaluate whether a piece of intelligence is actionable and explain why | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.1.6 | Tailoring output to the audience | K | A / A / B | A / B / B | B / C / C |
| 3.1.6.1 | Adjust an intelligence product for a specified audience | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.1.7 | Attribution (purpose, confidence, types) | K | A / A / A | A / B / B | B / C / C |
| 3.1.7.1 | Assess attribution statements for confidence and supporting evidence | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.1.8 | Collection sources and methods (OSINT, commercial, internal) | K | A / A / B | A / B / B | B / C / C |
| 3.1.8.1 | Identify appropriate collection source classes for a given requirement | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4c |
| 3.1.8.2 | Plan collection against an intelligence requirement | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4d |

---

## 3.2 Analytic Tradecraft

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.2.1 | Estimative language | K | A / A / A | A / B / B | B / C / C |
| 3.2.1.1 | Use and interpret estimative language in analytic judgments | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4c |
| 3.2.2 | Structured analytic techniques | K | A / A / A | A / B / B | B / C / C |
| 3.2.2.1 | Apply a structured analytic technique and select the right one for a scenario | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.2.3 | Admiralty Code / source reliability and information credibility | K | A / A / B | A / B / B | B / C / C |
| 3.2.3.1 | Assign Admiralty Code ratings and evaluate source reliability and credibility | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.2.4 | Cognitive biases and mitigation | K | A / A / A | A / B / B | B / C / C |
| 3.2.4.1 | Identify cognitive bias in a judgment and apply a mitigation technique | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |

---

## 3.3 Tools

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.3.1 | Internal threat intelligence platform | K | A / A / B | A / B / B | B / C / C |
| 3.3.1.1 | Search, retrieve, and use the internal TIP for enrichment or analysis | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.3.2 | External tools (VirusTotal, AnyRun, Silent Push, URLScan) | K | A / B / B | B / C / C | B / C / C |
| 3.3.2.1 | Select the appropriate external tool and perform enrichment or pivoting | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |

---

## 3.4 File Similarity & Hashing Techniques

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.4.1 | Hashing and similarity concepts (imphash, ssdeep, TLSH, code-signing certificates) | K | A / A / B | A / B / B | B / C / C |
| 3.4.1.1 | Use file similarity hashes to identify related samples | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.4.1.2 | Extract and interpret certificate / code-signing information from a file | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4c |

---

## 3.5 RDAP / WHOIS

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.5.1 | RDAP and WHOIS concepts | K | A / A / B | A / B / B | B / C / C |
| 3.5.1.1 | Query RDAP/WHOIS and interpret fields for enrichment or attribution | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |

---

## 3.6 Advanced DNS

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.6.1 | Advanced DNS concepts (SOA and other records of intel value) | K | A / A / B | B / C / C | B / C / C |
| 3.6.1.1 | Interpret an SOA record and use advanced DNS data to enrich or pivot | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |

---

## 3.7 Frameworks

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.7.1 | MITRE ATT&CK for CTI analysis and reporting | K | A / B / B | B / C / C | B / C / C |
| 3.7.1.1 | Map activity or reports to MITRE ATT&CK | T | 2b / 3c / 4c | 3c / 4c / 4c | 3c / 4c / 4c |
| 3.7.2 | Diamond Model application in CTI | K | A / B / B | B / C / C | B / C / C |
| 3.7.2.1 | Apply the Diamond Model to an intelligence problem | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 3.7.3 | Cyber Kill Chain in intelligence analysis | K | A / B / B | B / C / C | B / C / C |
| 3.7.3.1 | Identify the Kill Chain stage of observed or reported activity | T | 2b / 3c / 4c | 3c / 4c / 4c | 3c / 4c / 4c |
| 3.7.4 | Defender’s ThreatMesh Framework (DTF) for infrastructure discovery | K | A / A / B | A / B / B | B / C / C |
| 3.7.4.1 | Apply DTF: select a pivot tactic and pivot from a seed and reject the weak neighbor | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.7.4.2 | Use a selected DTF pivot to guide the next enrichment or lookup | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.7.4.3 | Explain how DTF integrates with or complements ATT&CK, Diamond, and Kill Chain | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4c |

---

## 3.8 Enrichment & Analysis

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.8.1 | Identifying additional adversary infrastructure from seed indicators | K | A / B / B | B / C / C | B / C / C |
| 3.8.1.1 | Pivot from a seed indicator to additional adversary infrastructure | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 3.8.2 | Extracting applicable TTPs from intelligence reports | K | A / B / B | B / C / C | B / C / C |
| 3.8.2.1 | Extract applicable TTPs from an intelligence report | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 3.8.3 | IOC handling and enrichment concepts | K | A / B / B | B / C / C | B / C / C |
| 3.8.3.1 | Enrich and pivot on IOCs using internal and external tools | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 3.8.3.2 | Link analysis and campaign tracking | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.8.4 | Threat relevance and organizational impact | K | A / B / B | B / C / C | B / C / C |
| 3.8.4.1 | Assess threat relevance and potential impact to the organization | T | 1a / 2b / 3c | 2b / 3c / 4c | 3c / 4c / 4d |

---

## 3.9 Platform-Specific Skills

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.9.1 | VirusTotal (Relations and Behavior tabs) | K | A / B / B | B / C / C | B / C / C |
| 3.9.1.1 | Use VirusTotal Relations and Behavior to pivot and extract events | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 3.9.2 | AnyRun | K | A / A / B | A / B / B | B / C / C |
| 3.9.2.1 | Search and review AnyRun submissions for actionable intelligence | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |
| 3.9.3 | Silent Push | K | A / A / B | A / B / B | B / C / C |
| 3.9.3.1 | Enrich an indicator and pivot in Silent Push | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |
| 3.9.4 | URLScan | K | A / A / B | A / B / B | B / C / C |
| 3.9.4.1 | Submit or retrieve a URLScan result and extract actionable intelligence | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |

---

## 3.10 Common STIX Objects

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.10.1 | Core STIX objects | K | A / B / B | B / C / C | B / C / C |
| 3.10.1.1 | Identify and label common STIX objects in a report | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |
| 3.10.2 | How STIX objects are used in intelligence production | K | A / B / B | B / C / C | B / C / C |
| 3.10.2.1 | Create STIX-aligned relationships and explain a threat scenario | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |
| 3.10.2.2 | Create and validate STIX objects | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |
| 3.10.2.3 | Use TAXII for sharing and consumption of intelligence | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |

---

## 3.11 Intelligence Production & Dissemination

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.11.1 | Creating finished intelligence products | K | A / A / B | A / B / B | B / C / C |
| 3.11.1.1 | Draft a finished product and evaluate it against standards | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.11.1.2 | Produce a threat actor profile | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.11.2 | Disseminating intelligence to the correct audiences | K | A / A / B | A / B / B | B / C / C |
| 3.11.2.1 | Select audience and method and apply correct handling markings | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4c |
| 3.11.2.2 | Tailor products to different audiences (technical, leadership, etc.) | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.11.2.3 | Disseminate intelligence products through approved channels | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4c |
| 3.11.3 | Handling RFIs | K | A / A / A | A / A / B | B / C / C |
| 3.11.3.1 | Evaluate, prioritize, and produce a response to an RFI | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4d |

---

## 3.12 Site-Specific CTI Knowledge and Tasks

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.12.1 | Local intelligence requirements and priorities | K | A / A / A | A / A / B | B / C / C |
| 3.12.1.1 | Identify current local priorities and align analytic work to them | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4c |
| 3.12.2 | Local production and approval processes | K | A / A / A | A / A / B | B / C / C |
| 3.12.2.1 | Follow the local process for requesting collection or producing and approving products | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4c |
| 3.12.2.2 | Document and archive intelligence products according to local standards | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4c |
| 3.12.3 | Local dissemination channels and customers | K | A / A / A | A / A / B | B / C / C |
| 3.12.3.1 | Disseminate a product using the correct local channels and customers | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4c |

---

## 4 Detection Engineer (primarily DE)

Taught last. **1.3** is rule syntax / first read-write. Nominations from SOC, hunt, and CTI need not be perfect. Blocks are firewall / IA. Site lists and deploy paths are **4.8** — do not invent them.

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 | DE 3/5/7 |
|---|------|------|-----------|--------------|-----------|----------|
| 4.1 | What DE owns | K | A / B / B | A / B / B | A / B / B | B / C / C |
| 4.1.1 | Sort work to DE, nominator, 1.3, or block | T | 1a / 2b / 2b | 1a / 2b / 2b | 1a / 2b / 2b | 3c / 4c / 4c |
| 4.2 | Making a detection sound and meeting shop requirements | K | A / A / B | A / A / B | A / A / B | B / C / C |
| 4.2.1 | Test a draft or change: what must fire and what must not | T | 1a / 1a / 2b | 1a / 1a / 2b | 1a / 1a / 2b | 3c / 4c / 4d |
| 4.2.2 | Mark which shop requirements are met and which are still missing | T | 1a / 1a / 1a | 1a / 1a / 1a | 1a / 1a / 1a | 3c / 4c / 4c |
| 4.2.3 | Write the close-the-loop note to the nominator | T | 1a / 1a / 2b | 1a / 1a / 2b | 1a / 1a / 2b | 3c / 4c / 4c |
| 4.3 | Nominations from SOC, hunt, and CTI | K | A / B / B | A / B / B | A / B / B | B / C / C |
| 4.3.1 | Review a nomination: accept, send back, or reject, and say who finishes what | T | 1a / 2b / 2b | 1a / 2b / 2b | 1a / 2b / 2b | 3c / 4c / 4d |
| 4.4 | Tune requests from SOC | K | A / B / B | A / A / B | A / A / B | B / C / C |
| 4.4.1 | Pick tune / exception / replace / leave / retire and cite why | T | 1a / 2b / 3c | 1a / 1a / 2b | 1a / 1a / 2b | 3c / 4c / 4d |
| 4.4.2 | Reject a request that is investigation, a block, or IR containment | T | 1a / 2b / 2b | 1a / 1a / 2b | 1a / 1a / 2b | 3c / 4c / 4c |
| 4.5 | Hunt and intel packages | K | A / A / B | A / B / B | A / B / B | B / C / C |
| 4.5.1 | Review a package: one add, one change, or no new rule | T | 1a / 1a / 2b | 1a / 2b / 3c | 1a / 2b / 3c | 3c / 4c / 4d |
| 4.5.2 | Reject turning the package into a block list | T | 1a / 1a / 2b | 1a / 2b / 2b | 1a / 2b / 2b | 3c / 4c / 4c |
| 4.6 | Detection lifecycle | K | A / A / B | A / A / B | A / A / B | B / C / C |
| 4.6.1 | Call modify / retire / leave and cite the reason | T | 1a / 1a / 2b | 1a / 1a / 2b | 1a / 1a / 2b | 3c / 4c / 4d |
| 4.6.2 | Given a block, decide whether the matching rule still earns its keep | T | 1a / 1a / 2b | 1a / 1a / 2b | 1a / 1a / 2b | 3c / 4c / 4d |
| 4.7 | Sensor availability and performance | K | A / A / A | A / A / A | A / A / A | A / B / B |
| 4.7.1 | Given “the rule never fired,” check the rule, the sensor, or both | T | 1a / 1a / 1a | 1a / 1a / 1a | 1a / 1a / 1a | 2b / 3c / 3c |
| 4.7.2 | Reject treating a down sensor as proof the activity did not happen | T | 1a / 1a / 1a | 1a / 1a / 1a | 1a / 1a / 1a | 2b / 3c / 3c |
| 4.8.1 | Local detection requirements | K | A / A / A | A / A / A | A / A / A | B / C / C |
| 4.8.1.1 | Identify whether you have the local list and align only to a list you were shown | T | 1a / 1a / 1a | 1a / 1a / 1a | 1a / 1a / 1a | 3c / 4c / 4c |
| 4.8.2 | Local review, deploy, and retire paths | K | A / A / A | A / A / A | A / A / A | B / C / C |
| 4.8.2.1 | Follow the local path you were shown (or record that you do not have it yet) | T | 1a / 1a / 1a | 1a / 1a / 1a | 1a / 1a / 1a | 3c / 4c / 4c |
| 4.8.2.2 | Reject inventing a change board or ticket name as policy | T | 1a / 1a / 1a | 1a / 1a / 1a | 1a / 1a / 1a | 3c / 4c / 4c |

---

**Notes for Review**
- Primary role ratings are taken from the individual matrices.
- Non-primary roles generally start at awareness level (**A** or **1a**) and only rise where the skill has clear shared value (e.g., frameworks, enrichment tools, ATT&CK, STIX).
- You can adjust any cross-role ratings as needed.
- Section `0` is a shared intro (`0.1`–`0.5` K, `0.5.1` T). Same codes for SOC, Hunter, CTI, and DE. No DE column on `1`–`3` yet.
- Section `4` is Detection Engineer (`4.1`–`4.8`). DE is primary (`docs/matrices/de.md`). Cross-role awareness lives **only** on this combined sheet — not on the SOC, hunter, or CTI sheets. Sensor unit `4.7` is lighter. Site unit `4.8` is obtain-and-follow.
- Hunt `2.x` and CTI `3.x` tasks are children of their knowledge item (`3.2.1` K, `3.2.1.1` T), matching the outline. SOC Zeek units keep the existing `1.2.x.1` K / `1.2.x.2` T pattern. Alert handling is five units (`1.4.1`–`1.4.5`); FP causes are `1.4.3`. Reporting is three units (`1.6.1`–`1.6.3`). Shift change is two units (`1.7.1`–`1.7.2`). Site-specific is five units (`1.8.1`–`1.8.5`); IR process is `1.8.5`. Collection sources are `3.1.8`; relevance/impact is `3.8.4`; actor profile is `3.11.1.2`; local collection request is `3.12.2.1`.
