# Combined Proficiency Matrix  
## SOC Analyst | Threat Hunter | CTI Analyst

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

Headings use **teaching-unit IDs** (`1.1`, `1.2`, `2.1`, `3.1`, …). Those match the `#` column. Do not assign work by old display numbers (there is no “section 7 = all hunting”).

---

## 1.1 Endpoint Logs & Telemetry Analysis (Primarily SOC)

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.1.1.1 | File logging concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.1.2 | Analyze a file event log and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.1.3 | Create a SIEM query to detect specific file operations | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.2.1 | Registry logging concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.2.2 | Analyze a registry event log and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.2.3 | Create a SIEM query to detect specific registry operations | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.3.1 | Process logging concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.3.2 | Analyze a process event log and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.3.3 | Create a SIEM query to detect specific process activity | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.4.1 | Network logging concepts | K | A / B / C | A / B / B | A / A / A |
| 1.1.4.2 | Analyze a network event log and accurately describe what occurred | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.1.4.3 | Create a SIEM query to detect specific network activity | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

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

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.4.1.1 | Alert context and investigation | K | A / B / C | B / C / C | A / A / B |
| 1.4.1.2 | Review an alert and its provided context | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.3 | Trace an alert back to its upstream detection logic | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.1.4 | Collect and examine related endpoint logs for an alert | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.1.5 | Collect and examine PCAP related to an alert | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.2.1 | Alert classification (TP/FP/TN/FN) | K | A / B / C | B / C / C | A / A / B |
| 1.4.2.2 | Common false positive causes | K | A / B / C | B / C / C | A / A / B |
| 1.4.2.3 | Correctly classify an alert as TP, FP, TN, or FN | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.2.4 | Identify likely causes of a false positive | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 2b |
| 1.4.3.1 | Common alert categorizations | K | A / B / C | B / C / C | A / A / A |
| 1.4.3.2 | Assign an appropriate category to an alert | T | 2b / 3c / 4c | 2b / 3c / 4c | 1a / 1a / 1a |
| 1.4.4.1 | Service Level Agreements / Response Time Goals | K | A / B / C | A / B / B | A / A / A |
| 1.4.4.2 | Demonstrate understanding of alert response time requirements | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.4.4.3 | Process an alert within required timeframes | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

---

## 1.5 Frameworks (Shared across all roles)

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

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.6.1.1 | Report types | K | A / B / C | B / C / C | B / C / C |
| 1.6.1.2 | Reporting timeline requirements | K | A / B / C | A / B / B | B / C / C |
| 1.6.1.3 | Notification and distribution | K | A / B / C | A / B / B | B / C / C |
| 1.6.2.1 | Identify the correct report type for a given situation | T | 2b / 3c / 4c | 2b / 3c / 4c | 3c / 4c / 4c |
| 1.6.2.2 | Submit a report within required timelines | T | 2b / 3c / 4c | 2b / 3c / 4c | 3c / 4c / 4c |
| 1.6.2.3 | Route a report to the correct recipients and leadership using approved channels | T | 2b / 3c / 4c | 2b / 3c / 4c | 3c / 4c / 4c |

---

## 1.7 Shift Change (Primarily SOC)

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.7.1.1 | Shift changeover process | K | A / B / C | A / B / B | A / A / A |
| 1.7.1.2 | Required content of the changeover report | K | A / B / C | A / B / B | A / A / A |
| 1.7.2.1 | Conduct or participate in a shift changeover | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |
| 1.7.2.2 | Produce a complete changeover report that includes all required elements | T | 2b / 3c / 4c | 1a / 2b / 3c | 1a / 1a / 1a |

---

## 1.8 Site-Specific Operational Knowledge (Mixed)

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 1.8.1.1 | Environment orientation | K | A / B / C | B / C / C | A / B / B |
| 1.8.2.1 | How to download PCAP | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.8.2.2 | What tool to use to view PCAP | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 1a / 2b |
| 1.8.3.1 | How to access required tools and their URLs | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.3.2 | How to request tools to be installed | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.3.3 | How to request access (e.g., SIEM) | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.4.1 | Where and how to save investigation notes | T | 2b / 3c / 4c | 3c / 4c / 4c | 2b / 3c / 4c |
| 1.8.4.2 | Follow site-specific incident response processes | T | 2b / 3c / 4c | 3c / 4c / 4c | 1a / 2b / 3c |

---

## 2.1 Purpose of Threat Hunting

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.1.1 | Purpose of Threat Hunting | K | A / B / B | B / C / C | A / B / B |
| 2.1.2 | Explain the purpose of threat hunting in the context of the security program | T | 1a / 2b / 3c | 3c / 4c / 4c | 1a / 2b / 3c |
| 2.1.3 | Identify examples of activity that existing controls might miss | T | 1a / 2b / 3c | 3c / 4c / 4d | 1a / 2b / 3c |

---

## 2.2 Attacker Techniques

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.2.1 | Persistence techniques | K | A / B / B | B / C / C | A / B / B |
| 2.2.2 | Recognize persistence techniques in logs or telemetry | T | 1a / 2b / 3c | 3c / 4c / 4c | 1a / 2b / 3c |
| 2.2.3 | Privilege escalation techniques | K | A / B / B | B / C / C | A / B / B |
| 2.2.4 | Recognize privilege escalation techniques in logs or telemetry | T | 1a / 2b / 3c | 3c / 4c / 4c | 1a / 2b / 3c |
| 2.2.5 | Hunt for specific persistence or privilege escalation techniques | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 1a / 2b |

---

## 2.3 Hunt Methodology

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.3.1 | Hunt types | K | A / B / B | B / C / C | A / B / B |
| 2.3.2 | Hunt development concepts | K | A / B / B | B / C / C | A / B / B |
| 2.3.3 | Develop and document a hunt hypothesis | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.3.4 | Scope and prioritize a hunt | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.3.5 | Identify unique patterns or behaviors suitable for hunting | T | 1a / 1a / 2b | 3c / 4c / 4d | 1a / 2b / 3c |
| 2.3.6 | Execute an intel-driven hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.3.7 | Execute a hypothesis-driven hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.3.8 | Execute a reactive hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.3.9 | Execute an anomaly-based hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |

---

## 2.4 Online Tools & Enrichment

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.4.1 | Tool capabilities for hunting | K | A / B / B | B / C / C | A / B / B |
| 2.4.2 | Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push | T | 1a / 2b / 3c | 3c / 4c / 4d | 2b / 3c / 4c |
| 2.4.3 | Extract actionable hunting leads from external tool results | T | 1a / 2b / 3c | 3c / 4c / 4d | 2b / 3c / 4c |
| 2.4.4 | Convert external findings into precise internal SIEM or Zeek queries | T | 1a / 2b / 3c | 3c / 4c / 4d | 1a / 2b / 3c |

---

## 2.5 CTI for Hunters

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.5.1 | Assessing CTI for hunting value | K | A / B / B | B / C / C | B / C / C |
| 2.5.2 | Extract TTPs suitable for hunting from a CTI report | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 2.5.3 | Extract artifacts (IOCs, patterns, behaviors) suitable for hunting | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 2.5.4 | Common STIX objects as they relate to hunting | K | A / B / B | B / C / C | B / C / C |
| 2.5.5 | Identify STIX objects relevant to a hunt | T | 1a / 2b / 3c | 3c / 4c / 4c | 3c / 4c / 4c |
| 2.5.6 | Use STIX-structured information to support hunt planning | T | 1a / 1a / 2b | 3c / 4c / 4d | 3c / 4c / 4d |

---

## 2.6 Framework Application for Hunting

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.6.1 | Using MITRE ATT&CK for hunt planning and coverage analysis | K | A / B / B | B / C / C | B / C / C |
| 2.6.2 | Map a hunt plan or hunt findings to MITRE ATT&CK | T | 1a / 2b / 3c | 3c / 4c / 4c | 3c / 4c / 4c |
| 2.6.3 | Use ATT&CK to identify detection or visibility gaps | T | 1a / 2b / 3c | 3c / 4c / 4d | 2b / 3c / 4c |
| 2.6.4 | Use ATT&CK to support hunt prioritization | T | 1a / 1a / 2b | 3c / 4c / 4d | 2b / 3c / 4c |

---

## 2.7 Site-Specific Hunt Knowledge and Tasks

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 2.7.1 | Hunt control and lead management | K | A / A / B | B / C / C | A / A / B |
| 2.7.2 | Hunt documentation standards | K | A / A / B | B / C / C | A / A / B |
| 2.7.3 | Hunt outputs and hand-off | K | A / A / B | B / C / C | A / A / B |
| 2.7.4 | Follow the local process for initiating and controlling a hunt | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.7.5 | Document a hunt according to local standards | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |
| 2.7.6 | Produce required hunt outputs and perform proper hand-off | T | 1a / 1a / 2b | 3c / 4c / 4c | 1a / 1a / 2b |

---

## 3.1 Intelligence Requirements & Direction

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.1.1 | Priority Intelligence Requirements (PIRs) and intelligence requirements concepts | K | A / A / B | A / B / B | B / C / C |
| 3.1.2 | Develop or refine intelligence requirements | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.1.3 | Translate stakeholder questions into clear intelligence requirements | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |

---

## 3.2 Collection Management

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.2.1 | Collection sources and methods (OSINT, commercial, internal, etc.) | K | A / A / B | A / B / B | B / C / C |
| 3.2.2 | Evaluate source reliability and information credibility | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.2.3 | Plan and request collection against intelligence requirements | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4d |

---

## 3.3 Processing & Exploitation

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.3.1 | IOC handling and enrichment concepts | K | A / B / B | B / C / C | B / C / C |
| 3.3.2 | Enrich and pivot on IOCs using internal and external tools | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 3.3.3 | Extract TTPs and behavioral patterns from raw data or reports | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |

---

## 3.4 Analysis

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.4.1 | Threat actor profiling concepts | K | A / A / B | A / B / B | B / C / C |
| 3.4.2 | Produce a threat actor profile | T | 1a / 1a / 1a | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.4.3 | Link analysis and campaign tracking | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.4.4 | Assess threat relevance and potential impact to the organization | T | 1a / 2b / 3c | 2b / 3c / 4c | 3c / 4c / 4d |

---

## 3.5 Structured Analytic Techniques & Frameworks

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.5.1 | MITRE ATT&CK for CTI analysis and reporting | K | A / B / B | B / C / C | B / C / C |
| 3.5.2 | Map activity or reports to MITRE ATT&CK | T | 2b / 3c / 4c | 3c / 4c / 4c | 3c / 4c / 4c |
| 3.5.3 | Diamond Model application in CTI | K | A / B / B | B / C / C | B / C / C |
| 3.5.4 | Apply the Diamond Model to an intelligence problem | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |
| 3.5.5 | Cyber Kill Chain in intelligence analysis | K | A / B / B | B / C / C | B / C / C |
| 3.5.6 | Use structured analytic techniques (e.g., ACH, key assumptions check) | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |

---

## 3.6 Production & Dissemination

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.6.1 | Intelligence product types and standards | K | A / A / B | A / B / B | B / C / C |
| 3.6.2 | Write clear, concise, and actionable intelligence reports | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.6.3 | Tailor products to different audiences (technical, leadership, etc.) | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4d |
| 3.6.4 | Disseminate intelligence products through approved channels | T | 1a / 1a / 2b | 1a / 2b / 3c | 3c / 4c / 4c |

---

## 3.7 STIX / TAXII & Structured Sharing

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.7.1 | Common STIX objects and relationships | K | A / B / B | B / C / C | B / C / C |
| 3.7.2 | Create and validate STIX objects | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4d |
| 3.7.3 | Use TAXII for sharing and consumption of intelligence | T | 1a / 1a / 2b | 2b / 3c / 4c | 3c / 4c / 4c |

---

## 3.8 Tools & Platforms

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.8.1 | CTI platform and enrichment tool capabilities | K | A / B / B | B / C / C | B / C / C |
| 3.8.2 | Perform advanced research and pivoting in primary CTI tools | T | 1a / 2b / 3c | 3c / 4c / 4d | 3c / 4c / 4d |

---

## 3.9 Site-Specific CTI Knowledge & Processes

| # | Item | Type | SOC 3/5/7 | Hunter 3/5/7 | CTI 3/5/7 |
|---|------|------|-----------|--------------|-----------|
| 3.9.1 | Local intelligence requirements and prioritization process | K | A / A / A | A / A / B | B / C / C |
| 3.9.2 | Local production, review, and dissemination standards | K | A / A / A | A / A / B | B / C / C |
| 3.9.3 | Follow local processes for requesting collection or producing products | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4c |
| 3.9.4 | Document and archive intelligence products according to local standards | T | 1a / 1a / 1a | 1a / 1a / 2b | 3c / 4c / 4c |

---

**Notes for Review**
- Primary role ratings are taken from the individual matrices.
- Non-primary roles generally start at awareness level (**A** or **1a**) and only rise where the skill has clear shared value (e.g., frameworks, enrichment tools, ATT&CK, STIX).
- You can adjust any cross-role ratings as needed.
