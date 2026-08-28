# Instructor Guide – Module 2.9.1 – VirusTotal (Relations and Behavior)

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.1 B / C / C ; 2.9.1.1 3c / 4c / 4d  
- Hunter: 2.9.1 B / C / C ; 2.9.1.1 3c / 4c / 4d  
- SOC: 2.9.1 A / B / B ; 2.9.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read the VirusTotal Relations and Behavior tabs on a classroom result card. Name extra infrastructure and extract events. Do not invent a hit. No live account.

**Context (plain language):**

- What this lesson is for: CTI analysts take a seed they already have and use two VirusTotal tabs — Relations for additional infrastructure, Behavior for process, file, registry, and network events from a sandbox run.
- How it hooks to the lesson before: 2.8.4 was whether a finding applies here and what would change. This lesson is the VirusTotal tabs that feed that kind of enrichment.
- How it hooks to the lesson after: 2.9.2 is AnyRun — search and review a public detonation card.
- Why we are doing it this way: the unit uses classroom result cards so nobody needs a live vendor account. This lesson is the two tabs, not when to pick the tool.
- What we are *not* doing in this lesson: the 0.7 survey (purpose / when to pick). The 2.8.1 hop sentence. File-similarity hashes (2.4). Applicable TTPs (2.8.2). Hunt conversion to SIEM or Zeek (3.3.1). A live VirusTotal login. No lab.
- Extra step: none.

Use the same names as the student guide: **Relations**, **Behavior**, **seed**, **classroom result card**, **contacted IP**, **process / file / registry / network events**, and **not on card**. The given uses course-fiction names (`update.exe`, `203.0.113.88`, Temp, Run `Updater`). Do not turn it into the A12 plot. Do not plant the Run key unless the card shows it.

**Key Teaching Points:**
- Relations is linked objects for pivoting. Behavior is sandbox events. A domain can appear in both; the product still follows the tab.
- Write what the card shows, or **not on card**. Empty Behavior is not a license to invent.
- A detection count is not the product of this lesson.

**Common Student Challenges:**
- Redo “when to pick VirusTotal.” Why: 0.7 was first contact with the tool. Example: writing “use VirusTotal for hash reputation” as the product of this lesson.
- Treat Behavior as Relations. Why: both can name a domain. Example: calling a sandbox DNS line “additional infra” without using Relations, or calling a contacted IP a process event.
- Invent a Run key. Why: they already saw HKCU Run `Updater` on the host. Example: writing that registry line when the card has no registry line.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.9.1 – VirusTotal (Relations and Behavior tabs)
- T: 2.9.1.1 – Use VirusTotal Relations and Behavior to pivot and extract events

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Seed, two tabs, card only |
| Key Concepts            | 12 min    | Relations vs Behavior; walk the card |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: you already have a seed, and you use two VirusTotal tabs to name extra infra and extract events. You do not log in.
- Write Relations vs Behavior. Stop on the overlap: a contacted domain can appear in both; the product still follows the tab.
- Walk the `update.exe` card from the student guide. Relations product: `203.0.113.88`. Behavior product: the process, file, or network line that is on the card.
- If they redo 0.7: when to pick the tool is done. This lesson is the tabs.
- If they write a hop sentence: that is 2.8.1. This lesson is the object on Relations, not the four-part sentence.
- If they invent Run `Updater`: not unless the card shows it. Empty registry is **not on card**.
- If they copy an ATT&CK tag off Behavior: that extract is 2.8.2.
- If they write a SIEM or Zeek query from the port-8080 line: that convert is 3.3.1.

---

## Knowledge Check – Answer Key

1. **This lesson is “when to pick VirusTotal.” True or false?**  
   **Answer:** False. That is 0.7.  
   **Explanation:** This lesson is the Relations and Behavior tabs on a result card, not purpose / when to pick.

2. **What does Relations give you that Behavior does not?**  
   **Answer:** Linked objects you can pivot to — contacted hosts, URLs, and dropped files as additional infrastructure. Behavior is sandbox events (process, file, registry, network), not that object graph.  
   **Explanation:** A domain can show up in both. The Relations product is extra infra. The Behavior product is the event.

3. **Seed hash of `update.exe`. One Relations result you may write from the card, and one thing you must not invent?**  
   **Answer:** You may write contacted IP `203.0.113.88`. You must not invent a sibling hostname or the registry Run key `Updater`.  
   **Explanation:** Write what the card shows. “Not on card” is legal. Do not copy the host plot onto VirusTotal.

---

## Additional Instructor Resources

- Next: 2.9.2 AnyRun
