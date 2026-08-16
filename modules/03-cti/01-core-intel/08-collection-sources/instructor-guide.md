# Instructor Guide – Module 3.1.8 – Collection Sources and Methods

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.8 A / A / B · 3.1.8.1 1a / 1a / 1a · 3.1.8.2 1a / 1a / 1a  
- Hunter: 3.1.8 A / B / B · 3.1.8.1 1a / 1a / 2b · 3.1.8.2 1a / 1a / 2b  
- CTI: 3.1.8 B / C / C · 3.1.8.1 3c / 4c / 4c · 3.1.8.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the three classes. Force **class order + plan line**. Close **3.1**. Do not teach VT pivoting or the 3.12 ticket.

**Key Teaching Points:**
- Class ≠ lifecycle stage.
- Internal-presence PIR → internal first.
- Public-story PIR → OSINT first. Do not always start internal.
- Hunter 3-level tasks are **1a**. CTI plan is **3c / 4d**. Do not collapse.
- 3.12.2.1 is how you *request* collection locally. This is *what class* to plan.

**Common Student Challenges:**
- OSINT-only for “are we hit?”
- “Google it” as a plan.
- Planning collection on an unusable PIR.
- Opening 3.3 / 2.3.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional local collection catalog
- Answer key (this guide)

---

## Learning Objectives

1. Three classes.
2. Identify class(es) for a PIR.
3. Plan order + first action + stop.

**Mapped Items:** K 3.1.8 · T 3.1.8.1 · T 3.1.8.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.1.2-as-class / 3.3 / 3.12 |
| Three classes                  | 14 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | Close 3.1 |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they defend blogs |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they pick a first class and a stop, not a tool demo.
- Reuse 3.1.4 Example 3 (blogs vs internal PIR).

**Question:**  
“If internals are dark (1.7.2 Zeek drop), does the class change or does the *plan* add a gap statement?” (Class stays internal; the plan says the sensor was dark — do not silently switch to OSINT and call the PIR answered.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail OSINT-only on A. Fail a plan on C. Fail VT demo.

**Summaries:**
- Ex 1: internal first.
- Ex 2: wrong first class.
- Ex 3: OSINT first for a public-story PIR.

**Cases:**

| Item | Class order | First action | Reject |
|------|-------------|--------------|--------|
| A | Internal → commercial confirm → OSINT context | SIEM/Zeek SNI/JA3 | OSINT-only |
| B | Internal samples/logs + commercial sandbox/TIP | Unique observables from *our* hits / TIP | Board paper |
| C | **No plan** until 3.1.4 refine | Translate the PIR | “Collect all OSINT” |
| D | **Internal** (sensor inventory, Zeek coverage) | Which VLANs have no span | OSINT blogs |

---

## Knowledge Check – Answer Key

1. **Three classes / one use?**  
   **Answer:** OSINT = public context. Commercial = paid enrichment/reporting. Internal = our telemetry and holdings.  
   **Explanation:** Outline a–c.

2. **Why not OSINT first for presence?**  
   **Answer:** Blogs do not say whether *we* are hit.  
   **Explanation:** Example 1–2.

3. **When OSINT first?**  
   **Answer:** When the PIR is the public story / external context (Example 3).  
   **Explanation:** Task 1.

4. **Vs 3.1.2?**  
   **Answer:** 3.1.2 is the *stage* in the loop. This is the *class of source*.  
   **Explanation:** Fence.

5. **Local ticket?**  
   **Answer:** **3.12.2.1**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local collection catalog
- Cluster **3.1** is complete. Next: **3.2.1** Estimative language
