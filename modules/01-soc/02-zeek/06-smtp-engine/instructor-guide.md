# Instructor Guide – Module 1.2.6 – SMTP Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C · 1.2.6.2 2b / 3c / 4c · 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C · 1.2.6.2 3c / 4c / 4c · 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B · 1.2.6.2 1a / 1a / 2b · 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read the Zeek `smtp` log, describe the transaction, write a specific SMTP query, and pivot on `uid`.

**Key Teaching Points:**
- Sensor SMTP metadata, not mailbox forensics, not **1.2.7** hashes.
- Envelope `mailfrom` / `rcptto`, `subject`, `msg_id`, 5-tuple, `uid`.
- Empty fields → “not logged.” Subject is not a verdict.
- Stay out of BEC playbooks and Zeek scripts.

**Common Student Challenges:**
- Treating envelope from as proof of the real sender.
- Calling every “invoice” subject phishing.
- Writing `smtp` with no filter.
- Analyzing an attachment hash in this hour.
- Forgetting `uid`.
- Grading CTI as SOC 5 (CTI is A / A / B and 1a / 1a / 2b).

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Explain `smtp` fields: mail from, rcpt to, subject, message ID, source/destination.
2. Analyze a Zeek SMTP log entry and describe what occurred.
3. Write a SIEM query for *specific* SMTP activity.
4. Pivot with `uid` to `conn`.

**Mapped Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Not mailbox forensics |
| Purpose of the smtp log        | 6 min    | Envelope vs full message |
| Key Fields                     | 14 min   | a–e; mailfrom ≠ identity |
| Walkthrough Examples           | 14 min   | Students first |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Example 2 if they say “BEC” |

---

## Detailed Teaching Notes

### 1. Purpose of the smtp Log

**Talking Points:**
- SOC 3 is A / 2b. Field names + one sentence.
- Hunter already B / 3c. Push query + pivot.
- CTI: nomenclature at 3/5 (A / 1a); 7-level A→B and 1a→2b. Do not run them through the SOC query bar.

**Question to ask:**  
“Who did the *envelope* say this was from and to?”

### 2. Key Fields

**Talking Points:**
- Walk outline a–e. Envelope vs header is one minute, then stop.
- `rcptto` is often a list. Count matters.
- `msg_id` joins messages; `uid` joins Zeek logs. Different jobs.

**Question to ask:**  
“If I only give you the subject `Urgent invoice`, do you have a story yet?”

### 3. Examples

**Example 1:** Baseline internal.
**Example 2:** Internet orig + internal envelope from + foreign msg_id. Lead. Not a BEC lecture.
**Example 3:** Workstation → internet:587, null mailfrom, many rcptto, empty subject/msg_id.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Group review. Park files and 1.3.

**Summaries:**
- Example 1: Internal jlee → finance; expected.
- Example 2: External IP, envelope from jlee, invoice subject, foreign msg_id; lead.
- Example 3: Workstation to internet 587, `<>` from, several rcptto, subject/msg_id not logged; lead.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Zeek smtp jlee → finance | **SMTP event** | `smtp` log |
| Zeek http POST beacon | **Not this log** | **1.2.5** |
| Zeek files SHA256 | **Not this log** | **1.2.7** |
| MDE outlook → :587 | **Not this log** | **1.1.4** |

**Pseudo-queries:**

```
smtp
| where mailfrom has "@buildingc.internal"
| where id.orig_h !startswith "10."
```

```
smtp
| where array_length(rcptto) > 5
    or mailfrom == "<>"
    or isempty(subject)
```

Fail a no-filter query, a files-hash query, or a host-network query.

**uid pivot:** Copy `uid` → `conn`. `fuids` → **1.2.7** next module.

---

## Knowledge Check – Answer Key

1. **Purpose?**  
   **Answer:** Record SMTP transaction metadata (envelope from/to, subject, message ID, 5-tuple) the sensor saw. Not a full mailbox.  
   **Explanation:** Protocol log.

2. **Envelope vs header?**  
   **Answer:** `mailfrom` / `rcptto` are SMTP commands. Header From/To (if logged) are inside the message and can disagree. Describe both when present.  
   **Explanation:** Support only — not a spoofing course.

3. **Why subject is not a verdict?**  
   **Answer:** It is attacker-controlled text. Useful context. “Invoice” is common on real mail too.  
   **Explanation:** Lead.

4. **msg_id vs uid?**  
   **Answer:** `msg_id` identifies the *message* (when logged). `uid` identifies the *Zeek connection* so you can open `conn` / `files`.  
   **Explanation:** Two different joins.

5. **Why uid?**  
   **Answer:** Links this SMTP transaction to `conn` (and later `files` / `weird`).  
   **Explanation:** Same habit as other engines.

---

## Additional Instructor Resources

- Local internal mail-gateway IPs if you have a list
- Next recommended module: 1.2.7 Files Engine
