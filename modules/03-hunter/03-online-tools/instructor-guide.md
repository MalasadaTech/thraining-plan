# Instructor Guide – Module 3.3.1 – Tool Capabilities for Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.3.1 B / C / C ; 3.3.1.1–3.3.1.3 3c / 4c / 4d  
- SOC: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 1a / 2b / 3c ; 3.3.1.3 1a / 2b / 3c  
- CTI: 3.3.1 A / B / B ; 3.3.1.1–3.3.1.2 2b / 3c / 4c ; 3.3.1.3 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name each tool’s hunt strength and hunt limit. Convert a classroom-result-card lead into a precise internal SIEM or Zeek query. No `/24`. No live account.

**Context (plain language):**

- What this lesson is for: Hunters take a finding from an external tool and turn it into a search they can run here, in the SIEM or in Zeek. A public detection count, a “malicious” tag, or a screenshot does not tell you whether that activity happened on your network.
- How it hooks to the lesson before: 3.2.2 bounded the hunt (hypothesis, scope, priority, unique pattern). This lesson is how an external finding becomes the internal search.
- How it hooks to the lesson after: 3.4.1 is whether a CTI report is hunt-worthy at all.
- Why we are doing it this way: same four tools as the survey and the platform lessons, but the product here is a hunt lead and a precise internal query — not a first-tool pick, and not a tab extract.
- What we are *not* doing in this lesson: when to pick a tool (0.7). How CTI reads Relations, Behavior, or the other platform tabs (2.9). A live vendor account. A lab.
- Extra step: none.

Use the same names as the student guide: **classroom result card**, **query**, **pivot**, **hunt lead**, and **precise** query. **A** is an IPv4 mapping. **NS** is a nameserver. **/24** is a 256-address block. **Relations / Behavior** are the VirusTotal sections that name linked hosts or files and sandbox events — not a tab class today.

**Key Teaching Points:**
- Four hunt limits: detection count, “malicious” tag, screenshot, whole `/24`.
- A lead is a named artifact you can search here.
- A precise query is IP + port + URI, not every destination.

**Common Student Challenges:**
- Treat a detection count as a hunt query. Why: the survey taught reputation. Example: writing “51/70 on VirusTotal” as the hunt.
- Convert a Silent Push name into a `/24` search. Why: more addresses feel like more coverage. Example: `dest=203.0.113.0/24`.
- Redo when-to-pick or tab reading. Why: these are the same four tools. Example: arguing AnyRun versus URLScan as the first tool, or walking the Relations tab.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.3.1 – Tool capabilities for hunting
- T: 3.3.1.1 – Perform advanced querying and pivoting in VirusTotal, AnyRun, URLScan, and Silent Push
- T: 3.3.1.2 – Extract actionable hunting leads from external tool results
- T: 3.3.1.3 – Convert external findings into precise internal SIEM or Zeek queries

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Convert, not survey |
| Key Concepts            | 12 min    | Four limits; lead; query |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an external finding is only useful if you can search for it here. A count, a tag, or a screenshot is not that search.
- Write the four hunt strengths and four hunt limits. Stop. Do not teach when to pick a tool. Do not walk the platform tabs.
- Define classroom result card, query, pivot, and hunt lead in the student-guide words. The product is what the card shows, not a live login.
- Walk the given: `GET /update.exe` to `203.0.113.88:8080` becomes IP + port + URI. Fail `dest=*` and fail the `/24`.
- If they start the 0.7 pick table: that is when to pick. This lesson is the conversion, not the pick.
- If they open Relations or Behavior as a tab class: that is 2.9.1. Today you only need the host or dropped file the card already named.
- If they query `203.0.113.0/24`: that is noise, not coverage.

---

## Knowledge Check – Answer Key

1. **A VirusTotal detection count is a hunt query. True or false?**  
   **Answer:** False.  
   **Explanation:** A detection count is reputation. It is not a host, URI, or file you can search internally.

2. **Name one hunt limit for Silent Push.**  
   **Answer:** The whole `/24` is noise.  
   **Explanation:** Other names on the same A or NS can be leads. Neighboring addresses on that 256-address block are shared hosting, not a hunt query.

3. **The classroom result card shows `GET /update.exe` to `203.0.113.88:8080`. Write one precise Zeek or SIEM query. Do not use a `/24`.**  
   **Answer:** Zeek `http` `id.resp_h == 203.0.113.88 && id.resp_p == 8080 && uri == "/update.exe"` (or the SIEM equivalent: that dest IP + port 8080 + URI `/update.exe`). Not a `/24`. Not `dest=*`.  
   **Explanation:** Precise means the lead’s IP, port, and URI together. A range or “every destination” is not this task.

---

## Additional Instructor Resources

- Next: 3.4.1 Assessing CTI for hunting value
