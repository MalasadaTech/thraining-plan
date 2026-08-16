# Threat Hunter Proficiency Matrix

**Skill Levels**
- **3** = Apprentice (Note: Threat Hunter 3-level is expected to be roughly equivalent to a mid-to-high SOC Analyst)
- **5** = Journeyman (independent)
- **7** = Craftsman / Senior (can train others)

**Proficiency Codes**
- Knowledge: A (Facts) → B (Principles) → C (Analysis) → D (Evaluation)
- Task Performance: 1 (Extremely Limited) → 2 (Partially Proficient) → 3 (Competent) → 4 (Highly Proficient)
- Task Knowledge: a (Nomenclature) → b (Procedures) → c (Operating Principles) → d (Advanced Theory)

**Baseline for Threat Hunter**
- Knowledge items generally start at **B**
- Task items generally start at **3c**
- Section **0** is the shared intro (same codes as SOC and CTI), not hunter-primary work

---

## 0 How a SOC can operate

Shared intro. Same idea on the SOC and CTI sheets. Not site policy.

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 0.1 | What a SOC is | K | A | B | B | Shared intro. Not hunter-primary; do not start at B/3c. |
| 0.2 | Jobs in one sentence | K | A | B | B | Hunter is one desk among several. |
| 0.3 | How work can move | K | A | B | B | One possible flow. Hunt package is a later beat. |
| 0.4 | Where the jobs lightly overlap | K | A | B | B | Same evidence, different product. |
| 0.5 | How this course is laid out | K | A | B | B | Hunters sit this after SOC and CTI. |
| 0.5.1 | Given a step in the flow, name the next hand-off and whose product it is | T | 1a | 2b | 2b | Name the hand-off. Do not invent a hunt ticket. No 4d. |

---

## 2.1 Purpose of Threat Hunting

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 2.1.1 | Purpose of Threat Hunting | K | B | C | C | Hunter 3 should already understand principles (not just basic facts). 5 and 7 both reach Analysis (C). No need for Evaluation (D) on this concept. |
| 2.1.1.1 | Explain the purpose of threat hunting in the context of the security program | T | 3c | 4c | 4c | Hunter 3 is already competent at explaining it. 5 and 7 are highly proficient. Capped at “c” (Operating Principles). |
| 2.1.1.2 | Identify examples of activity that existing controls might miss | T | 3c | 4c | 4d | Hunter 3 should already be competent. Higher ceiling at 7-level is appropriate for identifying subtle gaps. |

---

## 2.2 Hunt Methodology

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 2.2.1 | Hunt types | K | B | C | C | Hunter 3 should already understand the different hunt types at a principles level. 5/7 reach analysis. |
| 2.2.1.1 | Execute an intel-driven hunt | T | 3c | 4c | 4c | Execution tasks stay at highly proficient for 5 and 7. |
| 2.2.1.2 | Execute a hypothesis-driven hunt | T | 3c | 4c | 4c | Same as above. |
| 2.2.1.3 | Execute a reactive hunt | T | 3c | 4c | 4c | Same as above. |
| 2.2.1.4 | Execute an anomaly-based hunt | T | 3c | 4c | 4c | Same as above. |
| 2.2.2 | Hunt development concepts | K | B | C | C | Same progression – understanding how to develop hunts. |
| 2.2.2.1 | Develop and document a hunt hypothesis | T | 3c | 4c | 4d | Core skill. Hunter 3 should already be competent. 7-level can apply advanced theory and refine methodology. |
| 2.2.2.2 | Scope and prioritize a hunt | T | 3c | 4c | 4d | Important judgment skill that benefits from experience at the 7-level. |
| 2.2.2.3 | Identify unique patterns or behaviors suitable for hunting | T | 3c | 4c | 4d | Key hunting skill. Higher ceiling at 7-level is appropriate. |

---

## 2.3 Online Tools & Enrichment

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 2.3.1 | Tool capabilities for hunting | K | B | C | C | Hunter 3 should already understand the strengths and limitations of the main tools at a principles level. |
| 2.3.1.1 | Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push | T | 3c | 4c | 4d | Core enrichment skill. Hunter 3 should already be competent. 7-level can apply advanced techniques and teach others. |
| 2.3.1.2 | Extract actionable hunting leads from external tool results | T | 3c | 4c | 4d | Critical translation skill from external intel to hunt leads. Higher ceiling at 7-level is appropriate. |
| 2.3.1.3 | Convert external findings into precise internal SIEM or Zeek queries | T | 3c | 4c | 4d | Directly supports hunt execution. Advanced proficiency expected at the senior level. |

---

## 2.4 CTI for Hunters

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 2.4.1 | Assessing CTI for hunting value | K | B | C | C | Hunter 3 should already know hunt-worthy vs awareness-only vs hand-off. |
| 2.4.1.1 | Triage a CTI report: hunt / don’t hunt / hand off, and say why | T | 3c | 4c | 4d | Core consumer skill. 7-level applies finer judgment on weak or mixed reports. |
| 2.4.2 | Extracting hunt leads from CTI | K | B | C | C | TTPs vs IOCs vs behaviors; what to drop; ATT&CK IDs if present. Mapping hunts is 2.5. |
| 2.4.2.1 | Extract hunt-suitable TTPs from a CTI report | T | 3c | 4c | 4d | Direct application of 2.4.2. Overlap with CTI 3.8.2 is hunter-as-consumer. |
| 2.4.2.2 | Extract hunt-suitable artifacts (IOCs, patterns, behaviors) | T | 3c | 4c | 4d | Same as above. |
| 2.4.2.3 | State the hunt question those leads support | T | 3c | 4c | 4d | Bridges 2.4 to methodology (2.2) and queries (2.3). |
| 2.4.3 | STIX as hunt input | K | B | C | C | Objects a hunter uses and how a bundle seeds a hunt. Authoring STIX is CTI 3.10. |
| 2.4.3.1 | Identify hunt-relevant objects in a report or bundle | T | 3c | 4c | 4c | Practical read of a bundle, not production. |
| 2.4.3.2 | Turn those objects into hunt leads | T | 3c | 4c | 4d | Hunter-specific last step. |

---

## 2.5 Framework Application for Hunting

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 2.5.1 | Using MITRE ATT&CK for hunt planning and coverage analysis | K | B | C | C | Hunter 3 should already understand principles of using ATT&CK for hunting. |
| 2.5.1.1 | Map a hunt plan or hunt findings to MITRE ATT&CK | T | 3c | 4c | 4c | Practical mapping skill. |
| 2.5.1.2 | Use ATT&CK to identify detection or visibility gaps | T | 3c | 4c | 4d | Important analytical skill that benefits from senior-level insight. |
| 2.5.1.3 | Use ATT&CK to support hunt prioritization | T | 3c | 4c | 4d | Judgment-heavy task — higher ceiling at 7-level is appropriate. |

---

## 2.6 Attacker Techniques

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 2.6.1 | Persistence techniques | K | B | C | C | Hunter 3 should already understand principles of common persistence methods. 5/7 reach analysis level. |
| 2.6.1.1 | Recognize persistence techniques in logs or telemetry | T | 3c | 4c | 4c | Directly follows the knowledge item. Hunter 3 is already competent at recognition. |
| 2.6.2 | Privilege escalation techniques | K | B | C | C | Same knowledge progression as persistence. |
| 2.6.2.1 | Recognize privilege escalation techniques in logs or telemetry | T | 3c | 4c | 4c | Directly follows the privilege escalation knowledge item. |
| 2.6.3 | Hunt for specific persistence or privilege escalation techniques | T | 3c | 4c | 4d | Core hunting task. 7-level can apply advanced theory and adapt techniques. |

---

## 2.7 Site-Specific Hunt Knowledge and Tasks

| # | Item | Type | Hunter 3 | Hunter 5 | Hunter 7 | Justification |
|---|------|------|----------|----------|----------|---------------|
| 2.7.1 | Hunt control and lead management | K | B | C | C | Hunter 3 should understand local processes at a principles level. |
| 2.7.1.1 | Follow the local process for initiating and controlling a hunt | T | 3c | 4c | 4c | Must be competent at 3-level; highly proficient thereafter. |
| 2.7.2 | Hunt documentation standards | K | B | C | C | Same progression. |
| 2.7.2.1 | Document a hunt according to local standards | T | 3c | 4c | 4c | Same as above. |
| 2.7.3 | Hunt outputs and hand-off | K | B | C | C | Same progression. |
| 2.7.3.1 | Produce required hunt outputs and perform proper hand-off | T | 3c | 4c | 4c | Same as above. |
