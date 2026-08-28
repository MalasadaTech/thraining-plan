# Instructor Guide – Module 1.2.3 – DNS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek `dns` log and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read Zeek dns logs to see a name lookup on the wire — who asked, for which name, which type, and what came back.
- How it hooks to the lesson before: 1.2.2 was who talked to 203.0.113.88:443. This lesson is the lookup that can sit next to that flow.
- How it hooks to the lesson after: 1.2.4 is TLS — SNI and certificate on the same wire, not DNS.
- Why we are doing it this way: after the connection extract, read the DNS extract so you can describe the name lookup before you open TLS or HTTP.
- What we are *not* doing in this lesson: the initiating process (1.1.4). DGA or tunneling methodology. TLS or HTTP fields. uid-pivot as a unit. No lab.
- Extra step: none.

Use the same names as the student guide: **query**, **answers**, **qtype_name**, **id.orig_h**, and **id.resp_h**. **Row** is the SIEM-table gloss from the student intro, not the headline word. Continue `203.0.113.88` as the A answer. Do not invent Night Owl / Harbor resolver names. Do not tell the PRD plot.

**Key Teaching Points:**
- Question versus answer: `query` is the name that was asked; `answers` is what came back.
- Record types: A, AAAA, MX, CNAME, NS, TXT. CNAME is another name, not an address.
- `id.orig_h` asked; `id.resp_h` is the DNS server that was asked, not the A record.
- A query names a specific pattern, not every dns event.

**Common Student Challenges:**
- Treat `id.resp_h` as the resolved IP. Why: resp is the DNS server; `answers` holds the A. Example: writing “resolved to 8.8.8.8” because `id.resp_h` is `8.8.8.8`.
- Name the process from a dns log. Why: the process is on the host (1.1.4). Example: writing “powershell looked up that name” from this log alone.
- Write `dns=*` as a “specific” query. Why: the task is a named pattern. Example: matching every dns event with no `query`, type, or `answers` filter.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Name lookup, not conn |
| Key Concepts            | 16 min    | Question, answer, type, who asked whom; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a domain or a lookup, and you have to say who asked, for which name, which type, and what came back.
- Walk `query` and `answers` first. Empty `answers` means this log does not show a returned record. Do not start an NXDOMAIN hunt.
- Walk the type table. Stop on CNAME: it is another name, not an address.
- Stop on `id.resp_h`: it is the DNS server that was asked, often a resolver. It is not the A record. The A, when present, is in `answers`.
- Walk the given: workstation, type `A`, answers `["203.0.113.88"]`. One sentence. Who asked, which name, which type, what answered.
- If they name `powershell.exe`: that is 1.1.4. The process is not on this log.
- If they start DGA or tunneling: that is not this lesson. Describe the event.
- If they write `dns=*`: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **`id.resp_h` on a `dns` log is the IP the name resolved to. True or false?**  
   **Answer:** False. It is the DNS server that was asked. The A record is in `answers`.  
   **Explanation:** `id.resp_h` is the destination of the DNS packet, often a resolver. The address the name resolved to, when present, is in `answers`.

2. **Workstation queries a hostname, type `A`, answers `["203.0.113.88"]`. In one sentence, what occurred?**  
   **Answer:** That host asked for that name and got A 203.0.113.88.  
   **Explanation:** Who asked, which name, which type, what answered. Do not name a process. Do not call it C2 from this one A record.

3. **A SIEM query that matches every `dns` log is a good “specific DNS activity” query. True or false?**  
   **Answer:** False. A good query names a specific pattern (`query`, type, or `answers`).  
   **Explanation:** “Every dns log” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.2.4 TLS engine
