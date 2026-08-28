# Instructor Guide – Module 2.9.4 – URLScan

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.4 B / C / C ; 2.9.4.1 3c / 4c / 4c  
- Hunter: 2.9.4 A / B / B ; 2.9.4.1 2b / 3c / 4c  
- SOC: 2.9.4 A / A / B ; 2.9.4.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a URLScan result. Extract the title, requested hosts or IPs, and redirects that are on it, or write that the result is missing. No live submit.

**Context (plain language):**

- What this lesson is for: CTI analysts retrieve a URLScan result to see what a URL served on this page load, then extract what is on that result so they do not invent a page.
- How it hooks to the lesson before: 2.9.3 was Silent Push — passive DNS and infra context on a classroom card.
- How it hooks to the lesson after: 2.10.1 is core STIX objects. 2.9 ends here.
- Why we are doing it this way: 0.7 already named when to pick URLScan. This lesson is retrieve and read. Classroom result card only.
- What we are *not* doing in this lesson: the 0.7 survey (purpose / when to pick). A live URLScan submit. The hop sentence (2.8.1). Hunt conversion to SIEM or Zeek (3.3.1). File-similarity hashes (2.4). Applicable TTPs (2.8.2). No lab.
- Extra step: none.

Use the same names as the student guide: **URLScan**, **this page load**, **retrieve**, **submit**, **classroom result card**, **page title / final URL**, **requested hosts / IPs**, **redirect chain**, and **not on card**. **Card** means the provided scan result, not a live account. The given uses the **update domain** URL already in the course. Do not turn it into the intro plot. Do not treat `login-prd.net` as a URLScan page unless the card shows it.

**Key Teaching Points:**
- URLScan records this page load. When to pick it is 0.7.
- Retrieve is enough. Submit is named, not performed live.
- Extract title, requested hosts or IPs, and redirects that are on the card. A screenshot is information.
- No result means write **not on card**. Do not invent a login page.

**Common Student Challenges:**
- Treat this as the 0.7 pick lesson. Why: 0.7 already named URLScan. Example: spending the block on “URLScan versus Silent Push” instead of reading a result.
- Invent a page when the card is empty. Why: they remember `login-prd.net` from 2.9.3. Example: writing “login page for `login-prd.net`” when there is no result.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.9.4 – URLScan
- T: 2.9.4.1 – Submit or retrieve a URLScan result and extract actionable intelligence

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | What a URL served on this page load |
| Key Concepts            | 12 min    | Retrieve; extract or miss |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: you have a live URL, often the update domain, and you have to see what that URL served.
- Name the capability once: URLScan visits the URL and records this page load. Do not re-teach when to pick it. That is 0.7.
- Walk retrieve versus submit. Retrieve is reading an existing result. Submit is sending the URL so URLScan visits it. This lesson uses a classroom result card. No live account.
- Walk the extract table: title / final URL, requested hosts / IPs, redirect chain. Stop. A screenshot is information, not a judgment.
- Walk the two givens. A card with a title and a requested host: extract those two. No card: write **not on card**. Fail an invented login page.
- If they start the hop sentence: that is 2.8.1. Extract the host or IP. Do not write the hop.
- If they open a SIEM or Zeek hunt: that is 3.3.1.
- If they start STIX objects: that is 2.10.1. 2.9 ends here.

---

## Knowledge Check – Answer Key

1. **This lesson is “when to pick URLScan.” True or false?**  
   **Answer:** False. When to pick is 0.7. This lesson is retrieve and read.  
   **Explanation:** The survey already named purpose and first-tool choice. Stay on the result.

2. **Name two fields you extract from a URLScan result.**  
   **Answer:** Any two of: page title, final URL, requested hosts or IPs, redirect chain.  
   **Explanation:** Those are what the scan recorded on this page load. A screenshot is information, not a substitute for those fields.

3. **You have no card for the update URL. What do you write?**  
   **Answer:** **Not on card** / no result. Do not invent a page.  
   **Explanation:** Missing is a legal product. Filling in a login page for `login-prd.net` is inventing a result.

---

## Additional Instructor Resources

- Next: 2.10.1 Core STIX objects
