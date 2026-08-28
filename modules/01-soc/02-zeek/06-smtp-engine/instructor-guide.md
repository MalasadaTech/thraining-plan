# Instructor Guide – Module 1.2.6 – SMTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C ; 1.2.6.2 2b / 3c / 4c ; 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C ; 1.2.6.2 3c / 4c / 4c ; 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B ; 1.2.6.2 1a / 1a / 2b ; 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek `smtp` log and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read the Zeek `smtp` log to see a mail transaction on the wire. An alert names a session, and you have to say who the session claimed mail was from and to, what subject was logged, and which hosts talked.
- How it hooks to the lesson before: 1.2.5 was the HTTP extract on the same wire. This lesson is mail.
- How it hooks to the lesson after: 1.2.7 is the files extract — hashes of what crossed the wire.
- Why we are doing it this way: after other protocol extracts, read this engine so you can describe the envelope before you open a file hash or a phishing playbook.
- What we are *not* doing in this lesson: process name (1.1.4). Attachment hash (1.2.7). Phishing playbook. uid-pivot as a unit. Site mail-gateway names. No lab.
- Extra step: none.

Use the same names as the student guide: **mail from**, **rcpt to**, **subject**, **message ID**, and **source / dest**. **Row** is the SIEM-table gloss from the student intro, not the headline word. `mailfrom` is envelope MAIL FROM, not the From header.

**Key Teaching Points:**
- `mailfrom` / `rcptto` are the envelope.
- Subject and `msg_id` when logged. Empty means not logged.
- Attachment hash is 1.2.7. The process is 1.1.4.
- A query is specific, not every `smtp` event.

**Common Student Challenges:**
- Treat `mailfrom` as the attachment hash. Why: the next engine is files. Example: writing a SHA256 from the `smtp` event.
- Name the process that sent the mail. Why: Zeek does not carry the process. Example: “`outlook.exe` sent this” from `smtp` fields alone.
- Write `smtp=*` as a “specific” query. Why: the task is a named pattern. Example: matching every `smtp` event with no `mailfrom`, `rcptto`, subject, or dest filter.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Envelope on the wire, not a mailbox |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a mail session, and you have to say who the session claimed mail was from and to.
- Walk `mailfrom` and `rcptto` as the envelope. Stop: `mailfrom` is not the From header, and it is not a file hash. `rcptto` can be more than one address.
- Walk `subject` and `msg_id`. Empty means not logged, not “no mail.” Encrypted submission may have no SMTP fields; that handshake is 1.2.4.
- Walk orig → resp. Ports are often 25 or 587. Do not invent a site mail-gateway name.
- Walk the given: outside `mailfrom`, `rcptto` a user, subject present. One sentence. Do not name a process. Do not call it phishing.
- If they name `outlook.exe`: that is 1.1.4.
- If they open a hash: that is 1.2.7.
- If they write `smtp=*`: that is not a specific query.

---

## Knowledge Check – Answer Key

1. **`mailfrom` is the attachment hash. True or false?**  
   **Answer:** False. It is envelope MAIL FROM. Hashes are 1.2.7.  
   **Explanation:** `mailfrom` is who the session claimed as sender. A file hash is the files engine, not this log.

2. **Envelope from an outside address, `rcptto` a user, subject present. What occurred?**  
   **Answer:** That client sent envelope mail from A to B with that subject.  
   **Explanation:** One sentence from the envelope and the subject. Do not name a process. Do not declare phishing.

3. **A query that matches every `smtp` event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (`mailfrom`, `rcptto`, subject, or dest).  
   **Explanation:** “All SMTP events” is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.2.7 Files engine
