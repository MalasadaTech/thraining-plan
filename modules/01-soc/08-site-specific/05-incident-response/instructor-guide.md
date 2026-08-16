# Instructor Guide – Module 1.8.5 – Incident Response Processes

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.5.1 2b / 3c / 4c  
- Hunter: 1.8.5.1 3c / 4c / 4c  
- CTI: 1.8.5.1 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach follow-the-card. Force a **process line** plus rejected freelance. Close **1.8**.

**Key Teaching Points:**
- Harbor Sev1/2/3 is a stand-in. Overlay the site playbook if you have one.
- Sev1 (jewel / OT / widespread) → IR owns. SOC does not freelance.
- Sev2 isolate only with IR concurrence.
- CTI 3-level is **1a**. Hunter is **3c**. Do not collapse CTI to SOC 2b.
- 1.6.3 is who *hears* about the report. This is who *owns containment*.

**Common Student Challenges:**
- Unplug first, ticket later.
- Treating OT as Sev2 “because one host.”
- Isolating a DC on an informational.
- Rewriting the 1.6.3 chart.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site IR playbook
- Answer key (this guide)

---

## Learning Objectives

1. Follow the IR card.
2. Next step + owner.
3. Reject freelance.

**Mapped Items:** T 1.8.5.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & card            | 14 min   | steps + Sev |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close 1.8 |
| **Total**                      | **~56 min** | Stretch Ex 2 if they defend the cable |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: 2b — read the Sev row and name the next step.
- Overlay real Sev names if you can. Keep “who owns containment.”

**Question:**  
“IR is not answering. Do you isolate `pay-db-01`?” (Escalate the *blocked clock* — **1.6.2** — do not freelance Sev1.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail unplug-the-jewel. Fail isolate-the-DC on informational. Fail OT as Sev2.

**Summaries:**
- Ex 1: Sev2, page, isolate only with concurrence.
- Ex 2: Sev1, IR owns, reject cable.
- Ex 3: OT is Sev1, not “one host.”

**Cases:**

| Item | Sev | Next | Owner | Reject |
|------|-----|------|-------|--------|
| A | Sev2 | IR already on ticket → request **concurrence** then isolate | SOC with IR | Isolate before concurrence |
| B | Sev2 | Ticket + **first** IR page | SOC with IR | SMS-only / no ticket |
| C | **Sev3** (informational, not incident) | Document | SOC — **no isolate** | Taking `dc-01` offline |
| D | **Sev1** (widespread) | Page IR | **IR lead** | SOC mass-isolate without IR |

---

## Knowledge Check – Answer Key

1. **Sev rows / owner?**  
   **Answer:** Sev1 jewel/OT/widespread → IR lead. Sev2 single user host → SOC with IR concurrence. Sev3 no live host → SOC documents.  
   **Explanation:** Card.

2. **Next after confirm incident?**  
   **Answer:** Incident ticket + page IR (ticket + duty lead). Then read Sev.  
   **Explanation:** Steps 1–3.

3. **Why not unplug pay-db-01?**  
   **Answer:** Crown jewel = Sev1. IR owns containment. Freelance unplug is not the process.  
   **Explanation:** Example 2.

4. **Vs 1.6.3?**  
   **Answer:** 1.6.3 is who receives the *report* and by which channel. This is who **owns containment**.  
   **Explanation:** Fence.

5. **Live playbook?**  
   **Answer:** Site IR / severity matrix. Classroom Sev1/2/3 are for this lesson.  
   **Explanation:** Same pattern as other 1.8 cards.

---

## Additional Instructor Resources

- Site IR playbook
- Unit **1.8** is complete. Next outline unit is **2.1** Purpose of Threat Hunting (already generated).
