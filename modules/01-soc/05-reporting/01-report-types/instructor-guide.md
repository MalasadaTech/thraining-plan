# Instructor Guide – Module 1.6.1 – Report Types

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.6.1.1 A / B / C · 1.6.1.2 2b / 3c / 4c  
- Hunter: 1.6.1.1 B / C / C · 1.6.1.2 2b / 3c / 4c  
- CTI: 1.6.1.1 B / C / C · 1.6.1.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach incident vs RFI vs other, and force **type + rejected neighbor**. Do not teach clocks or routing.

**Key Teaching Points:**
- Incident = case record. RFI = question. Other = named local (classroom: informational).
- RFI can sit beside an incident.
- Shift change is **1.7**. Intel product is **3.11**.
- Hunter/CTI start at B; CTI task is **3c** at 3-level.

**Common Student Challenges:**
- Every question becomes a new incident.
- Shift changeover as “other.”
- Writing the report body.
- Opening 1.6.2/1.6.3.

**Required Materials:**
- Student Guide
- Slide Deck
- Local extra types if the site has them
- Answer key (this guide)

---

## Learning Objectives

1. Name the types.
2. Identify type + reject neighbor.

**Mapped Items:** K 1.6.1.1 · T 1.6.1.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 1.7 / 3.11 |
| Three types                    | 14 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~62 min** | Stretch Ex 2 if they open a second incident |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — pick the bucket and name the neighbor.
- CTI 3: already 3c on the task.

**Question:**  
“Are you recording a case or asking a question?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail a 1.7 answer as a 1.6 type. Fail a full report draft.

**Summaries:**
- Ex 1: Incident, not RFI.
- Ex 2: RFI to CTI, not a second incident.
- Ex 3: Informational, not incident.

**Cases:**

| Item | Type | Reject | Why |
|------|------|--------|-----|
| A | **Incident** | RFI | First case record for a real miss/download. |
| B | **RFI** (IT) | Incident | Question about scanner identity. |
| C | **Not 1.6** — **1.7** changeover | Incident / other | Shift handoff is its own unit. |
| D | **RFI** or **Informational** | Incident | No internal case. If they ask CTI “have we seen this?”, RFI. If lead wants FYI only, Informational. Accept either with a clean neighbor reject. |

---

## Knowledge Check – Answer Key

1. **Incident vs RFI?**  
   **Answer:** Incident records a case. RFI asks another party for information.  
   **Explanation:** Outline a–b.

2. **Other / not parked there?**  
   **Answer:** Named local types (classroom: informational). Do not park shift change (**1.7**) or intel products (**3.11**).  
   **Explanation:** Outline c.

3. **RFI beside incident?**  
   **Answer:** The incident is the case. The RFI is a question that supports it. Different type.  
   **Explanation:** Example 2.

4. **Why not “appropriate”?**  
   **Answer:** That restates the K. Sign-off is reject the neighbor.  
   **Explanation:** Task.

5. **Shift-change write-up?**  
   **Answer:** **1.7**, not a 1.6 report type.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Next recommended module: 1.6.2 Reporting timelines
