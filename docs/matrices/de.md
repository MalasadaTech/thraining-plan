# Detection Engineer Proficiency Matrix

**Skill Levels**
- **3** = Apprentice (supervised, never alone on shift)
- **5** = Journeyman (independent)
- **7** = Craftsman / Senior (can train others)

**Proficiency Codes**
- Knowledge: A (Facts) → B (Principles) → C (Analysis) → D (Evaluation)
- Task Performance: 1 (Extremely Limited) → 2 (Partially Proficient) → 3 (Competent) → 4 (Highly Proficient)
- Task Knowledge: a (Nomenclature) → b (Procedures) → c (Operating Principles) → d (Advanced Theory)

**Baseline for Detection Engineer**
- Knowledge items generally start at **B**
- Task items generally start at **3c**
- Section **0** is the shared intro (same codes as SOC, Hunter, and CTI), not DE-primary work. Do not start 0.x at B/3c.
- Shared floor after **0** (`0.6`, `3.3.2`, `1.8.1`) is also not DE-primary. Do not start those at B/3c.
- Sensor work (**4.7**) is lighter
- Site-specific (**4.8**) is obtain-and-follow, not invented DYA process
- Rule syntax / first read-write is **1.3**, not this sheet

---

## 0 Front door

Everyone. Taught before SOC. Same idea on the SOC, hunter, and CTI sheets. Not site policy.

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 0.1 | How this course is laid out | K | A | B | B | Course map. Not DE-primary. |
| 0.2 | What a SOC is | K | A | B | B | Shared intro. Not DE-primary; do not start at B/3c. |
| 0.3 | Jobs in one sentence | K | A | B | B | DE is one desk among several. |
| 0.4 | How work can move | K | A | B | B | Hunt package to DE is a later beat. |
| 0.4.1 | Given a step in the flow, name the next hand-off and whose product it is | T | 1a | 2b | 2b | Name the hand-off. Do not invent a ticket path. No 4d. |
| 0.5 | Where the jobs lightly overlap | K | A | B | B | Same evidence, different product. |

---

## Shared floor (IDs unchanged)

Taught after **0**, before SOC **1.1**. Same IDs as the SOC/CTI sheets. Not DE-primary.

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 0.6.1.1 | MITRE ATT&CK | K | A | B | B | Shared floor. Hunt planning is 2.5. DTF is 3.7.4. |
| 0.6.1.2 | Map observed activity to an ATT&CK tactic and technique (or sub-technique) and cite the evidence | T | 1a | 2b | 2b | Awareness map. Do not start at 3c. |
| 0.6.2.1 | Diamond Model | K | A | B | B | Shared floor. |
| 0.6.2.2 | Apply the Diamond Model to an incident or set of indicators | T | 1a | 2b | 2b | Awareness apply. |
| 0.6.3.1 | Cyber Kill Chain | K | A | B | B | Shared floor. |
| 0.6.3.2 | Identify the Kill Chain stage of observed activity | T | 1a | 2b | 2b | Awareness apply. |
| 3.3.2 | External tools (VirusTotal, AnyRun, Silent Push, URLScan) | K | A | B | B | Purpose and when to pick. Platform depth is 3.9. |
| 3.3.2.1 | Select the appropriate external tool for a given enrichment or analysis need | T | 1a | 2b | 3c | Select. Not a 3.9 pivot. Matches SOC awareness. |
| 1.8.1.1 | Environment orientation | K | A | B | B | Seven facts including PCAP sensors. Sensor *health* is 4.7. |
| 1.8.1.2 | Identify which orientation fact applies and why it is not the adjacent fact | T | 2b | 3c | 4c | Same apply-task as SOC. Needed for 4.7. |

---

## 4.1 What DE owns

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.1 | What DE owns | K | B | C | C | Own new / change / retire / deploy. Nominations can be rough. Not 1.3. Not a block. |
| 4.1.1 | Sort work to DE, nominator, 1.3, or block | T | 3c | 4c | 4c | First-day sort. Reject “rough draft is not DE” and “block request is a deploy.” |

---

## 4.2 Making a detection sound and meeting shop requirements

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.2 | Making a detection sound and meeting shop requirements | K | B | C | C | Sound + test + required fields + close the loop. Field *list* is 4.8. |
| 4.2.1 | Test a draft or change: what must fire and what must not | T | 3c | 4c | 4d | Core craft. 7-level adapts tests when the activity is messy. |
| 4.2.2 | Mark which shop requirements are met and which are still missing | T | 3c | 4c | 4c | Fill the list you were shown. Do not invent fields. |
| 4.2.3 | Write the close-the-loop note to the nominator | T | 3c | 4c | 4c | Shipped / changed / sent back / retired. |

---

## 4.3 Nominations from SOC, hunt, and CTI

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.3 | Nominations from SOC, hunt, and CTI | K | B | C | C | Draft need not be perfect. Bar is need + pointer, not a finished rule. |
| 4.3.1 | Review a nomination: accept, send back, or reject, and say who finishes what | T | 3c | 4c | 4d | Distinctive vs weak nomination. 7-level judges what DE should finish. |

---

## 4.4 Tune requests from SOC

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.4 | Tune requests from SOC | K | B | C | C | Live rules. Different inbox. Which rule + pointer. |
| 4.4.1 | Pick tune / exception / replace / leave / retire and cite why | T | 3c | 4c | 4d | Judgment on a live rule. |
| 4.4.2 | Reject a request that is investigation, a block, or IR containment | T | 3c | 4c | 4c | Stay on the DE product. |

---

## 4.5 Hunt and intel packages

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.5 | Hunt and intel packages | K | B | C | C | Both CTI and hunters. Treat like a nomination. “No new rule” is valid. |
| 4.5.1 | Review a package: one add, one change, or no new rule | T | 3c | 4c | 4d | Core package review. |
| 4.5.2 | Reject turning the package into a block list | T | 3c | 4c | 4c | Blocks are firewall / IA. |

---

## 4.6 Detection lifecycle

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.6 | Detection lifecycle | K | B | C | C | Modify / retire / leave, and why. |
| 4.6.1 | Call modify / retire / leave and cite the reason | T | 3c | 4c | 4d | 7-level when reasons compete. |
| 4.6.2 | Given a block, decide whether the matching rule still earns its keep | T | 3c | 4c | 4d | Block is not automatically retire. |

---

## 4.7 Sensor availability and performance

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.7 | Sensor availability and performance | K | A | B | B | Lighter. Sometimes DE. Not vendor admin. |
| 4.7.1 | Given “the rule never fired,” check the rule, the sensor, or both | T | 2b | 3c | 3c | Not a 4d sensor-engineering task. |
| 4.7.2 | Reject treating a down sensor as proof the activity did not happen | T | 2b | 3c | 3c | Same ceiling as 4.7.1. |

---

## 4.8 Site-specific DE knowledge

| # | Item | Type | DE 3 | DE 5 | DE 7 | Justification |
|---|------|------|------|------|------|---------------|
| 4.8.1 | Local detection requirements | K | B | C | C | Obtain the list. Do not invent meta fields. |
| 4.8.1.1 | Identify whether you have the local list and align only to a list you were shown | T | 3c | 4c | 4c | Same pattern as other site units. |
| 4.8.2 | Local review, deploy, and retire paths | K | B | C | C | How this shop ships and retires. |
| 4.8.2.1 | Follow the local path you were shown (or record that you do not have it yet) | T | 3c | 4c | 4c | Do not invent a ticket name. |
| 4.8.2.2 | Reject inventing a change board or ticket name as policy | T | 3c | 4c | 4c | Same fail as other site units. |
