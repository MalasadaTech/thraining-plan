# Module 3.1.8 – Collection Sources and Methods

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.8 A / A / B · 3.1.8.1 1a / 1a / 1a · 3.1.8.2 1a / 1a / 1a  
- Hunter: 3.1.8 A / B / B · 3.1.8.1 1a / 1a / 2b · 3.1.8.2 1a / 1a / 2b  
- CTI: 3.1.8 B / C / C · 3.1.8.1 3c / 4c / 4c · 3.1.8.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the three **source classes**: OSINT, commercial, internal.
2. **Identify** which class(es) fit a given requirement.
3. **Plan** collection against that requirement (order + first action + what you will not collect).

**Mapped Proficiency Items:**
- K: 3.1.8 – Collection sources and methods (OSINT, commercial, internal)
- T: 3.1.8.1 – Identify appropriate collection source classes for a given requirement
- T: 3.1.8.2 – Plan collection against an intelligence requirement

---

## 1. Key Concepts

**3.1.2** named *collection* as a lifecycle **stage**. This hour is **where you collect from**. How to click VirusTotal is **3.3** / **2.3**. How to file the local request ticket is **3.12.2.1**.

**Three classes (outline a–c):**

| Class | What it is | Good for | Not enough when |
|-------|------------|----------|-----------------|
| **OSINT** | Public reporting, public passive DNS, open blogs | Context, first names, “is this discussed outside?” | The PIR is *our* presence or *our* logs |
| **Commercial** | Paid TIP, premium sandboxes, vendor intel | Enriched infra, packaged reporting | You have not checked internals the PIR asked for |
| **Internal** | SIEM, EDR, Zeek, tickets, internal TIP holdings, hunt results | “Are *we* seeing this?” | The PIR is only “what is the public story?” |

Classes stack. Order follows the **requirement** (**3.1.4**), not habit.

**Classroom plan line:**

`requirement | class order | first action | will not collect | rejected wrong class`

| This lesson | Other |
|-------------|-------|
| Which *class* | Lifecycle *stage* — **3.1.2** |
| Plan the collection | File the **ticket** — **3.12.2.1** |
| Not how to pivot VT | **3.3.2** / **2.3** |

The tasks extend the K: **pick the class** and **write the plan**, not “list OSINT.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Internal-presence PIR → internal first | OSINT-only for “are we hit?” |
| Public-story PIR → OSINT then commercial | Planning “google it” with no class or stop |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Internal Presence (Expected)

**Requirement:** Are we seeing Night Owl SNI/JA3 on Harbor hosts **this week**? (Tactical.)

**Classes:** **Internal first** (Zeek/SIEM/EDR). Commercial TIP if you need to confirm the JA3 is still theirs. OSINT last (context only).  
**First action:** Query `nightowl-updates.net` / JA3 `a0e9f5…` in SIEM/Zeek.  
**Will not collect:** A nation-state paper.  
**Reject:** OSINT-only.

### Example 2: OSINT-Only on “Are We Hit?” (Lead)

**Plan shipped:** “Read three blogs and update the TIP.”

**Fail:** The PIR is internal presence. Blogs do not answer it.  
**Correct plan:** Example 1.  
**Lead:** OSINT is a real class. It is the **wrong first class** here.

### Example 3: Public-Story PIR (Lead)

**Requirement:** Leadership — what is the *public* Night Owl story this quarter, to decide whether we brief the board? (Strategic context.)

**Classes:** **OSINT first**, then **commercial** packaged reporting. Internal only if the board question becomes “and are *we* hit?” (that is a second PIR).  
**Reject:** Jumping straight to host isolates as the collection plan.  
**Lead:** Different PIR → different order. Do not always start internal.

---

## 3. Hands-On Exercise

**Objective:** Name the class order and write the plan line.

**Instructions:**

1. One sentence each for Examples 1–3: first class + rejected class.
2. For each item, write the **plan line**.

   - A. Same as Example 1 (internal presence this week).
   - B. Detections: “Give me unique Night Owl observables we can put in SIGMA.” (Technical.)
   - C. “Collect everything OSINT on ransomware” (the bad PIR from 3.1.4 D) — say you must **refine the PIR** before planning.
   - D. Hunt lead needs *internal* coverage gaps for Night Owl (which VLANs have no Zeek).

3. Do not open VirusTotal and pivot (**3.3**). Do not write the 3.12 ticket steps.
4. If C has no usable requirement, the plan is **refine 3.1.4 first**.

**Expected Outcome:**
- Three example summaries
- Four plan lines (C may be “no plan until refined”)
- No VT walkthrough, no local ticket SOP

---

## 4. Knowledge Check

1. Name the three **classes** and one use for each.
2. Why is OSINT the wrong **first** class for an internal-presence PIR?
3. When *should* OSINT go first?
4. How is this different from the **3.1.2** collection *stage*?
5. Where is the **local request ticket** taught?

---

## 5. Summary

- OSINT / commercial / internal. Order follows the PIR.
- Plan: first action + what you will not collect.
- This closes cluster **3.1**. Next cluster: **3.2** Analytic tradecraft.

---

## 6. References & Further Reading

- Related modules:
  - 3.1.7 – Attribution (previous)
  - 3.1.2 – Intelligence lifecycle (collection *stage*)
  - 3.1.4 – Intelligence requirements
  - 3.3 – Tools
  - 3.12.2.1 – Local collection request process
- Local collection catalog (optional — substitutes classroom classes)
