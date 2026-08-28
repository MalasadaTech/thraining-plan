# Instructor Guide – Module 0.7 – External tools

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
- Hunter: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- CTI: 0.7 B / C / C ; 0.7.1 3c / 4c / 4d  
- DE: 0.7 A / B / B ; 0.7.1 1a / 2b / 3c  
**Estimated Time:** 20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name what each of the four public tools is for, and pick the first one that matches the need.

**Context (plain language):**

- What this lesson is for: You will get a hash, a file, a domain, or a live URL. Four public tools each answer a different question. Pick the first tool that matches the need, and say why the neighbor is the wrong first pick.
- How it hooks to the lesson before: 0.6.3 placed the activity on a Kill Chain stage. This lesson is the first public tool when you have a hash, a file, a domain, or a live URL.
- How it hooks to the lesson after: 0.8 is environment / signal flow — kinds of facts to obtain from your shop.
- Why we are doing it this way: Everyone needs the same first-tool pick before SOC, hunt, or CTI depth. Survey only. Not a live account.
- What we are *not* doing in this lesson: TIP navigation (2.3.1). Platform depth on VirusTotal, AnyRun, Silent Push, or URLScan (2.9). A lab or a live query. The course fiction plot (DYA / PRD).
- Extra step: none.

Use the same names as the student guide: **VirusTotal**, **AnyRun**, **Silent Push**, and **URLScan**. **Passive DNS** (past resolutions, also called **PDNS**) is Silent Push’s history, not a URLScan page load. The **TIP** is the internal threat intelligence platform, not one of these four.

**Key Teaching Points:**
- Four tools: purpose, one strength, one weakness.
- When to pick each. Reject the neighbor.
- “Have we seen this internally?” is not these four.

**Common Student Challenges:**
- Open AnyRun on a hash-only reputation question. Why: AnyRun is the sandbox they have heard of. Example: “I will detonate it” when they only have a hash.
- Pick URLScan for domain history. Why: both tools mention domains. Example: treating a page screenshot as passive DNS.
- Treat “have we seen this internally?” as one of the four. Why: enrichment sounds like a public lookup. Example: opening VirusTotal to answer whether the shop already holds the indicator.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 0.7 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)
- T: 0.7.1 – Select the appropriate external tool for a given enrichment or analysis need

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Pick the first tool. Do not detonate by habit. |
| Key Concepts            | 11 min    | Four tools + when + one select |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a hash, a file, a domain, or a live URL, and a public question about it. Name the first tool. Reject the neighbor.
- Walk the four-tool table. One purpose, one strength, one weakness each. Do not open a vendor tab.
- Walk when to pick. Stop on “have we seen this internally?” That is the TIP later, not these four.
- Walk the given: hash plus vendor reputation is VirusTotal. Reject AnyRun (no sample) and Silent Push (not history).
- If they start a Relations hop or a product walkthrough: that is 2.9. Today is purpose and when to pick.
- If they open the TIP: that is 2.3.1. These four are public tools.
- If they start the DYA / PRD plot: that fiction is from the intro. It is not this lesson.

---

## Knowledge Check – Answer Key

1. **Give one purpose and one weakness of Silent Push.**  
   **Answer:** Purpose: passive DNS / infrastructure clustering (historical resolutions). Weakness: not a detonation and not a page screenshot.  
   **Explanation:** Silent Push is history and cluster. It does not run a file and it does not show this page load.

2. **When do you pick URLScan instead of Silent Push?**  
   **Answer:** You need how this URL or page looks *now* (redirects, screenshot, this load). Silent Push is history / cluster, not this page load.  
   **Explanation:** URLScan is this visit. Silent Push is past resolutions and siblings.

3. **You have a hash and need reputation. Which tool, and why not AnyRun?**  
   **Answer:** VirusTotal. AnyRun needs a sample to detonate. A hash reputation question is a look-up, not a run.  
   **Explanation:** The first tool matches the need. A hash with no file is not an AnyRun detonation.

---

## Additional Instructor Resources

- Next: 0.8 Environment / signal flow
