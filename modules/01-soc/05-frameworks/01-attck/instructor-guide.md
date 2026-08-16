# Instructor Guide – Module 1.5.1 – MITRE ATT&CK

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.1.1 A / B / C · 1.5.1.2 2b / 3c / 4c  
- Hunter: 1.5.1.1 B / C / C · 1.5.1.2 3c / 4c / 4c  
- CTI: 1.5.1.1 B / C / C · 1.5.1.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach ATT&CK structure and force a **tactic + technique + cite + rejected neighbor** on activity they already know. Do not run **2.5** hunt planning.

**Key Teaching Points:**
- Columns = tactics (why). Cells = techniques / sub-techniques (how).
- Map the **row you have**.
- Hunter/CTI already start at **B / 3c** — push the neighbor reject, not the alphabet.
- SOC 3 is A / 2b — tactic + ID + one cite is a pass.

**Common Student Challenges:**
- C2 on a process-create with no network row.
- Five IDs on one event.
- Navigator / coverage talk.
- Using 1.4.4 categories as tactics.
- Opening Diamond or Kill Chain.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional: one printed Enterprise tactic strip (not a full memorize sheet)
- Answer key (this guide)

---

## Learning Objectives

1. Purpose and matrix structure.
2. Tactic vs technique vs sub-technique.
3. Map activity with cite and rejected neighbor.

**Mapped Items:** K 1.5.1.1 · T 1.5.1.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 2.5 / 1.5.2 |
| Purpose and structure          | 14 min   | a–c |
| Mapping method                 | 10 min   | d |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~72 min** | Stretch Ex 2 if they insist C2 |

---

## Detailed Teaching Notes

**Talking Points:**
- Do not require all 14 tactic names from memory. Require *what a tactic is* and the ones in the examples.
- Sub-technique when the how is specific (PowerShell vs “scripting”).
- IDs can be looked up in class. The skill is the map, not reciting numbers.

**Question:**  
“What field on *this* row forces that ID?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail Navigator. Fail category-only. Fail C2 without a network cite.

**Summaries:**
- Ex 1: Execution T1059.001; cite `-enc`; reject C2.
- Ex 2: Same row is still Execution; C2 only if POST beacon row is cited.
- Ex 3: T1105; cite GET `.exe`; reject Impact.

**Cases (accept equivalent IDs if cited):**

| Item | Tactic | Technique | Cite | Reject |
|------|--------|-----------|------|--------|
| A | Execution or Defense Evasion staging | **T1105** or file-drop as staging; **T1059.005** if they emphasize vbs write | Temp `update.exe` from wscript | Persistence (no autorun yet) |
| B | Persistence | **T1547.001** Registry Run Keys | HKCU Run = Temp exe | Execution (the *set* is the persist) |
| C | Privilege Escalation (and Execution) | **T1059.001** + note SYSTEM token; **T1543** if they cite the service | `-enc` as SYSTEM | User-level category talk without an ID |
| D | Command and Control | **T1071.001** | POST `/api/v1/beacon` + PS UA | Execution (that is a different row) |

A: if they only say T1059.001 because wscript ran, accept if they cite the *create process* not the file. If they map the **file create**, T1105 is the better primary.

---

## Knowledge Check – Answer Key

1. **Purpose / matrix?**  
   **Answer:** Shared language for adversary **behavior**. Matrix = tactics (columns) × techniques (cells).  
   **Explanation:** Outline a.

2. **Tactic vs technique vs sub?**  
   **Answer:** Tactic = why/goal. Technique = named how (`T1059`). Sub-technique = more specific how (`T1059.001`).  
   **Explanation:** Outline b–c.

3. **Four parts of a map?**  
   **Answer:** Tactic, technique/sub (ID + name), evidence cite, rejected neighbor.  
   **Explanation:** Task.

4. **Why not 2.5?**  
   **Answer:** Coverage, Navigator, hunt priority are hunt-planning. This hour maps **one activity**.  
   **Explanation:** Fence.

5. **Why not “looks like C2”?**  
   **Answer:** C2 needs network evidence on *that* story. A process create is Execution until you cite a connect/URI.  
   **Explanation:** Example 2.

---

## Additional Instructor Resources

- attack.mitre.org (Enterprise)
- Next recommended module: 1.5.2 Diamond Model
