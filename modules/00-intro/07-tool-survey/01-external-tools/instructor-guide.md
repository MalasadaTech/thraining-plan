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

**Context (plain language):**

- What this hour is for: Name what each of the four public tools is for, and pick the first one that matches the need.
- How it hooks to the hour before: Kill Chain placed the row in time. Now they pick an outside tool when they have a hash, a file, a domain, or a live URL.
- How it hooks to the hour after: environment / signal flow — where visibility comes from on the site.
- Why we are doing it this way: Everyone needs the same first-tool pick before SOC, hunt, or CTI depth. Survey only. Not a live account.
- What we are *not* doing this hour: TIP navigation. Relations / multi-hop pivot. A lab or a live query.

**Key Teaching Points:**
- Four tools: purpose, one strength, one weakness.
- When to pick each. Reject the neighbor.
- “Have we seen this internally?” is not these four.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:**  
- K: 0.7 – External tools (VirusTotal, AnyRun, Silent Push, URLScan)  
  SOC A / B / B · Hunter B / C / C · CTI B / C / C · DE A / B / B  
- T: 0.7.1 – Select the appropriate external tool for a given enrichment or analysis need  
  SOC 1a / 2b / 3c · Hunter 3c / 4c / 4d · CTI 3c / 4c / 4d · DE 1a / 2b / 3c

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Why pick, not detonate by habit |
| Key Concepts            | 11 min    | Four tools + when + one select |
| Knowledge Check         | 5 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk the four-row table. Do not open a vendor tab. For the select: hash + reputation → VirusTotal; reject AnyRun (no sample) and Silent Push (not history). If they start a Relations hop, park it for 3.9.

---

## Knowledge Check – Answer Key

1. **Purpose and weakness of Silent Push?**  
   **Answer:** Purpose: passive DNS / infra clustering (historical resolutions). Weakness: not a detonation and not a page screenshot.  
   **Explanation:** Outline a.

2. **When URLScan instead of Silent Push?**  
   **Answer:** You need how this URL / page looks *now* (redirects, screenshot, this load). Silent Push is history / cluster, not this page load.  
   **Explanation:** Outline b.

3. **Hash + reputation — which tool, why not AnyRun?**  
   **Answer:** VirusTotal. AnyRun needs a sample to detonate. A hash reputation question is a look-up, not a run.  
   **Explanation:** Outline a–b / task.

---

## Additional Instructor Resources

- Next: 1.8.1 Environment / signal flow
