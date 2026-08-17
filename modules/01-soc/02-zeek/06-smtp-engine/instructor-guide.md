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
Read a Zeek `smtp` row and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this hour is for: SOC analysts read envelope from/to, subject, and message ID when Zeek parsed SMTP.
- How it hooks to the hour before: 1.2.5 was GET /update.exe. This hour is the mail path that can sit next to `invoice.vbs` on the host.
- How it hooks to the hour after: 1.2.7 is the files extract — hashes of what crossed the wire.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–e only. No lab this pass.
- What we are *not* doing this hour: Process name (1.1.4). Phishing playbook. uid-pivot as a unit. Night Owl / Harbor / DYA mail names. No lab.
- Extra step: none.

Keep envelope + subject generic. Do not invent a site MX. Do not tell the PRD plot.

**Key Teaching Points:**
- mailfrom / rcptto are the envelope.
- Subject and msg_id when logged.
- Attachment hash is 1.2.7.
- A query is specific.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 1.2.6.1 ; T 1.2.6.2 ; T 1.2.6.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Envelope, not mailbox |
| Key Concepts            | 16 min    | Fields a–e; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write mailfrom, rcptto, subject, msg_id, orig/resp. Stop on “not a .eml.”

If they name `outlook.exe`: “1.1.4.”  
If they open a hash: “1.2.7.”  
If they write `smtp=*` : “Not specific.”  
If they invent an MX name: “0.8. Do not invent the site.”

---

## Knowledge Check – Answer Key

1. **`mailfrom` is the attachment hash. True or false?**  
   **Answer:** False. It is envelope MAIL FROM. Hashes are 1.2.7.  
   **Explanation:** Outline a.

2. **Outside envelope from, rcptto a user, subject present. What occurred?**  
   **Answer:** That client sent envelope mail from A to B with that subject.  
   **Explanation:** Outline a–e and 1.2.11 task 1.

3. **A query that matches every smtp row is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (mailfrom, rcptto, subject, or dest).  
   **Explanation:** 1.2.11 task 2.

---

## Additional Instructor Resources

- Next: 1.2.7 Files engine
