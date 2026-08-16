# SOC Analyst Proficiency Matrix

**Skill Levels**
- **3** = Apprentice (supervised, never alone on shift)
- **5** = Journeyman (independent)
- **7** = Craftsman / Senior (can train others)

**Proficiency Codes**
- Knowledge: A (Facts) → B (Principles) → C (Analysis) → D (Evaluation)
- Task Performance: 1 (Extremely Limited) → 2 (Partially Proficient) → 3 (Competent) → 4 (Highly Proficient)
- Task Knowledge: a (Nomenclature) → b (Procedures) → c (Operating Principles) → d (Advanced Theory)

---

## 1.1 Endpoint Logs

Host-observed Sysmon / MDE activity. Not Sysmon deployment. Protocol deep-dive is 1.2.

### 1.1.1 Process activity

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.1.1.1 | Process activity concepts | K | A | B | C | 3-level needs basic facts. 5-level understands principles. 7-level analyzes and draws conclusions. |
| 1.1.1.2 | Analyze a process event (Sysmon or MDE) and accurately describe what occurred | T | 2b | 3c | 4c | 3-level can do most of the task with guidance. 5-level is competent. 7-level can train others. |
| 1.1.1.3 | Create a SIEM query to detect specific process activity | T | 2b | 3c | 4c | Same progression as analysis. |

### 1.1.2 File system activity

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.1.2.1 | File system activity concepts | K | A | B | C | Same knowledge progression as Process activity. |
| 1.1.2.2 | Analyze a file event (Sysmon or MDE) and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression as process analysis. |
| 1.1.2.3 | Create a SIEM query to detect specific file operations | T | 2b | 3c | 4c | Same progression as other query-creation tasks. |

### 1.1.3 Network activity (endpoint)

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.1.3.1 | Network activity (endpoint) concepts | K | A | B | C | Host-observed connect/DNS. Zeek protocol depth is 1.2. |
| 1.1.3.2 | Analyze an endpoint network event (Sysmon or MDE) and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression as previous analysis tasks. |
| 1.1.3.3 | Create a SIEM query to detect specific endpoint network activity | T | 2b | 3c | 4c | Same progression as other query-creation tasks. |

### 1.1.4 Registry activity

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.1.4.1 | Registry activity concepts | K | A | B | C | Same knowledge progression. Persistence locations are examples; hunt techniques are 2.6. |
| 1.1.4.2 | Analyze a registry event (Sysmon or MDE) and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression as previous analysis tasks. |
| 1.1.4.3 | Create a SIEM query to detect specific registry operations | T | 2b | 3c | 4c | Same progression as other query-creation tasks. |

### 1.1.5 Image and driver load activity

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.1.5.1 | Image and driver load activity concepts | K | A | B | C | Same knowledge progression. Sysmon 6/7; MDE DeviceImageLoadEvents. |
| 1.1.5.2 | Analyze an image or driver load event (Sysmon or MDE) and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression as previous analysis tasks. |
| 1.1.5.3 | Create a SIEM query to detect specific image or driver load activity | T | 2b | 3c | 4c | Same progression as other query-creation tasks. |

---

## 1.2 Zeek and Zeek Engines

### 1.2.1 Zeek Concepts

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.1.1 | Zeek concepts | K | A | B | C | 3-level needs basic facts. 5-level should understand principles. 7-level should analyze and apply. |

### 1.2.2 Conn Engine

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.2.1 | Conn engine | K | A | B | C | Same knowledge progression as other Zeek engines. |
| 1.2.2.2 | Analyze a Zeek conn log and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression used for endpoint log analysis. |
| 1.2.2.3 | Create a SIEM query to detect specific connection activity | T | 2b | 3c | 4c | Same progression as other query-creation tasks. |

### 1.2.3 DNS Engine

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.3.1 | DNS engine | K | A | B | C | Same knowledge progression. |
| 1.2.3.2 | Analyze a Zeek DNS log and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression. |
| 1.2.3.3 | Create a SIEM query to detect specific DNS activity | T | 2b | 3c | 4c | Same query-creation progression. |

### 1.2.4 TLS Engine

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.4.1 | TLS engine | K | A | B | C | Same knowledge progression. |
| 1.2.4.2 | Analyze a Zeek TLS log and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression. |
| 1.2.4.3 | Create a SIEM query to detect specific TLS activity | T | 2b | 3c | 4c | Same query-creation progression. |

### 1.2.5 HTTP Engine

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.5.1 | HTTP engine | K | A | B | C | Same knowledge progression. |
| 1.2.5.2 | Analyze a Zeek HTTP log and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression. |
| 1.2.5.3 | Create a SIEM query to detect specific HTTP activity | T | 2b | 3c | 4c | Same query-creation progression. |

### 1.2.6 SMTP Engine

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.6.1 | SMTP engine | K | A | B | C | Same knowledge progression. |
| 1.2.6.2 | Analyze a Zeek SMTP log and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression. |
| 1.2.6.3 | Create a SIEM query to detect specific SMTP activity | T | 2b | 3c | 4c | Same query-creation progression. |

### 1.2.7 Files Engine

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.7.1 | Files engine | K | A | B | C | Same knowledge progression. |
| 1.2.7.2 | Analyze a Zeek files log and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression. |
| 1.2.7.3 | Create a SIEM query to detect specific file transfer activity | T | 2b | 3c | 4c | Same query-creation progression. |

### 1.2.8 Weird Engine

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.2.8.1 | Weird engine | K | A | B | C | Same knowledge progression. |
| 1.2.8.2 | Analyze a Zeek weird log and accurately describe what occurred | T | 2b | 3c | 4c | Same performance progression. |
| 1.2.8.3 | Create a SIEM query to detect specific weird activity | T | 2b | 3c | 4c | Same query-creation progression. |

---

## 1.3 Detection Engineering

### 1.3.1 SIGMA Rules

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.3.1.1 | SIGMA rules | K | A | B | C | 3-level needs basic facts. 5-level understands principles. 7-level can analyze and apply. |
| 1.3.1.2 | Analyze an existing SIGMA rule and describe what it detects | T | 2b | 3c | 4c | Standard analysis progression. |
| 1.3.1.3 | Create or modify a basic SIGMA rule | T | 1a | 2b | 3c | SOC analysts propose rules; Detection Engineering reviews and deploys. 3-level is limited, 5-level partially proficient, 7-level competent. |

### 1.3.2 Suricata Rules

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.3.2.1 | Suricata rules | K | A | B | C | Same knowledge progression. |
| 1.3.2.2 | Analyze an existing Suricata rule and describe what it detects | T | 2b | 3c | 4c | Standard analysis progression. |
| 1.3.2.3 | Create or modify a basic Suricata rule | T | 1a | 2b | 3c | Same rationale as SIGMA – SOC proposes, DE reviews/deploys. |

### 1.3.3 YARA Rules

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.3.3.1 | YARA rules | K | A | B | C | Same knowledge progression. |
| 1.3.3.2 | Analyze an existing YARA rule and describe what it detects | T | 2b | 3c | 4c | Standard analysis progression. |
| 1.3.3.3 | Create or modify a basic YARA rule | T | 1a | 2b | 3c | Same rationale as SIGMA/Suricata. |

### 1.3.4 SIEM Rules

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.3.4.1 | SIEM rules | K | A | B | C | Same knowledge progression. |
| 1.3.4.2 | Analyze an existing SIEM rule and describe what it detects | T | 2b | 3c | 4c | Standard analysis progression. |
| 1.3.4.3 | Create a basic SIEM detection rule from log fields or a SIGMA rule | T | 1a | 2b | 3c | Same rationale – SOC proposes, does not deploy. |

---

## 1.4 Alerts

Detection authoring is 1.3. Tasks apply the knowledge they sit under.

### 1.4.1 Alert context and investigation

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.4.1.1 | Alert context and investigation | K | A | B | C | 3-level needs basic facts. 5-level understands principles. 7-level can analyze and apply. |
| 1.4.1.2 | Review an alert and identify which context is present and which is missing | T | 2b | 3c | 4c | Extends “view context” — must name gaps, not just open the pane. |
| 1.4.1.3 | Review the alert configuration and explain what would fire | T | 2b | 3c | 4c | Knowledge *b* had no task before. |
| 1.4.1.4 | Trace an alert to its upstream detection logic and name each hop | T | 2b | 3c | 4c | Extends upstream knowledge — name the chain, not “look at the rule.” |
| 1.4.1.5 | Collect related endpoint logs and state what they add (or fail to add) | T | 2b | 3c | 4c | Extends collection — say what the logs change about the story. |
| 1.4.1.6 | Collect related PCAP and state what it adds versus the alert fields | T | 2b | 3c | 4c | Extends PCAP — contrast with the alert, not “open a pcap.” |

### 1.4.2 Alert classification

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.4.2.1 | Alert classification (TP/FP/TN/FN) | K | A | B | C | Same knowledge progression. |
| 1.4.2.2 | Classify given cases as TP, FP, TN, or FN and cite the evidence | T | 2b | 3c | 4c | Must include a missed detection (FN). Citing evidence is the extension. |

### 1.4.3 Common false positive causes

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.4.3.1 | Common false positive causes | K | A | B | C | Own unit — not a second K row under classification. |
| 1.4.3.2 | Given a false positive, identify the cause class and what you would change | T | 2b | 3c | 4c | Extends cause knowledge — class plus a change, not just “name a cause.” |

### 1.4.4 Common alert categorizations

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.4.4.1 | Common alert categorizations | K | A | B | C | Same knowledge progression. |
| 1.4.4.2 | Assign a category to an alert and justify why it is not the adjacent category | T | 2b | 3c | 4c | Extends labeling — must rule out the neighbor (scan vs unsuccessful, user vs root). |

### 1.4.5 Service Level Agreements / Response Time Goals

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.4.5.1 | Service Level Agreements / Response Time Goals | K | A | B | C | Two clocks: start investigation vs close/escalate. |
| 1.4.5.2 | Given timestamps, identify whether the start clock or the close/escalate clock is at risk | T | 2b | 3c | 4c | Replaces “demonstrate understanding,” which only restated the K. |
| 1.4.5.3 | Close or escalate an alert and record it against the correct clock | T | 2b | 3c | 4c | Applies both clocks; not “work faster.” |

---

## 1.5 Frameworks

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.5.1.1 | MITRE ATT&CK | K | A | B | C | 3-level needs basic familiarity. 5-level understands principles. 7-level can analyze and apply. |
| 1.5.1.2 | Map an alert or observed activity to MITRE ATT&CK tactics/techniques | T | 2b | 3c | 4c | Practical application skill that grows with experience. |
| 1.5.2.1 | Diamond Model | K | A | B | C | Same knowledge progression. |
| 1.5.2.2 | Apply the Diamond Model to an incident or set of indicators | T | 2b | 3c | 4c | Same performance progression. |
| 1.5.3.1 | Cyber Kill Chain | K | A | B | C | Same knowledge progression. |
| 1.5.3.2 | Identify the Kill Chain stage of observed activity | T | 2b | 3c | 4c | Same performance progression. |

---

## 1.6 Reporting

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.6.1.1 | Report types | K | A | B | C | 3-level needs basic facts. 5-level understands principles. 7-level can analyze and apply. |
| 1.6.1.2 | Reporting timeline requirements | K | A | B | C | Same knowledge progression. |
| 1.6.1.3 | Notification and distribution | K | A | B | C | Same knowledge progression. |
| 1.6.2.1 | Identify the correct report type for a given situation | T | 2b | 3c | 4c | Standard performance progression. |
| 1.6.2.2 | Submit a report within required timelines | T | 2b | 3c | 4c | Core operational task – must be reliable at 5-level. |
| 1.6.2.3 | Route a report to the correct recipients and leadership using approved channels | T | 2b | 3c | 4c | Same performance progression. |

---

## 1.7 Shift Change

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.7.1.1 | Shift changeover process | K | A | B | C | 3-level needs basic facts. 5-level understands principles. 7-level can analyze and improve the process. |
| 1.7.1.2 | Required content of the changeover report | K | A | B | C | Same knowledge progression. |
| 1.7.2.1 | Conduct or participate in a shift changeover | T | 2b | 3c | 4c | 3-level participates with guidance. 5-level can run it independently. 7-level is highly proficient and can train others. |
| 1.7.2.2 | Produce a complete changeover report that includes all required elements | T | 2b | 3c | 4c | Same performance progression. |

---

## 1.8 Site-Specific Knowledge

| # | Item | Type | SOC 3 | SOC 5 | SOC 7 | Justification |
|---|------|------|-------|-------|-------|---------------|
| 1.8.1.1 | Environment orientation | K | A | B | C | 3-level needs basic facts about the environment. 5-level understands how the pieces relate. 7-level can analyze and apply deeper knowledge. |
| 1.8.2.1 | How to download PCAP | T | 2b | 3c | 4c | Standard operational task progression. |
| 1.8.2.2 | What tool to use to view PCAP | T | 2b | 3c | 4c | Same performance progression. |
| 1.8.3.1 | How to access required tools and their URLs | T | 2b | 3c | 4c | Core daily skill. |
| 1.8.3.2 | How to request tools to be installed | T | 2b | 3c | 4c | Same progression. |
| 1.8.3.3 | How to request access (e.g., SIEM) | T | 2b | 3c | 4c | Same progression. |
| 1.8.4.1 | Where and how to save investigation notes | T | 2b | 3c | 4c | Must be consistent and reliable by 5-level. |
| 1.8.4.2 | Follow site-specific incident response processes | T | 2b | 3c | 4c | Critical operational task – standard progression. |
