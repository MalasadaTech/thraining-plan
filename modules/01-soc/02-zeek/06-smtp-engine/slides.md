# Module 1.2.6 – SMTP Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.2.6 – SMTP Engine  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Zeek `smtp` log. Envelope metadata, not a mailbox. CTI bar is A / 1a until 7-level.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain mail from, rcpt to, subject, message ID, and source/destination
2. Analyze a Zeek `smtp` log entry and describe what occurred
3. Write a SIEM query for *specific* SMTP activity
4. Pivot with `uid` to `conn`

**Mapped Items:**  
K: 1.2.6.1 | T: 1.2.6.2 | T: 1.2.6.3

**Speaker Notes:**  
SOC A/2b → C/4c. Do not grade CTI as SOC 5.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose of the smtp log
- Fields (outline a–e)
- Three worked examples
- uid pivot
- Two queries
- Knowledge check

**Speaker Notes:**  
Attachments are 1.2.7.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Mailbox / `.eml` forensics  
Attachment SHA256 (**1.2.7**)  
Host process on 587 (**1.1.4**)  
BEC playbook  
Zeek scripts

**Key Point:** Describe *this* `smtp` row.

**Speaker Notes:**  
Park BEC extras.

---

### Slide 5 – Purpose of the smtp Log
**Title:** Purpose of the smtp Log

- Written by Zeek’s SMTP engine
- Envelope + selected headers the sensor saw
- Complements `conn` (who talked) and later `files` (what was attached)

**Key Point:** Not the full message.

**Speaker Notes:**  
Ask: “Who did the envelope name?”

---

### Slide 6 – Envelope
**Title:** Mail From and Rcpt To

**mailfrom** — SMTP MAIL FROM (envelope sender)  
**rcptto** — SMTP RCPT TO (often a list)

These are commands, not proof of the real person.  
Count of `rcptto` matters.

**Speaker Notes:**  
One minute on envelope vs header if they ask. Then stop.

---

### Slide 7 – Subject and Message ID
**Title:** Subject and Message ID

**subject** — useful, easy to spoof, can be empty  
**msg_id** — identifies the *message* when logged

Empty → write “not logged.”  
`msg_id` ≠ `uid`. Different joins.

**Speaker Notes:**  
“Invoice” is not a verdict.

---

### Slide 8 – Source, Dest, uid
**Title:** Who Spoke SMTP

`id.orig_h` — who opened the session  
`id.resp_h` / `id.resp_p` — mail server (25 / 587 / 465)  
`uid` → `conn`

**Expected:** gateway → internal SMTP  
**Lead:** workstation → internet SMTP

**Speaker Notes:**  
Same 5-tuple habit.

---

### Slide 9 – Example 1: Expected
**Title:** Example 1 – Internal Mail

- `jlee@buildingc.internal` → `finance@…`
- Subject: Q3 notes
- orig `10.10.8.40` → `:25`

**Interpretation:**  
Expected.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: External Orig
**Title:** Example 2 – Internet Client, Internal Envelope

- orig `203.0.113.88`
- mailfrom still `jlee@buildingc.internal`
- msg_id `@nightowl-updates.net`

**Interpretation:**  
Lead. Not an automatic BEC.

**Speaker Notes:**  
Orig IP + envelope + msg_id together.

---

### Slide 11 – Example 3: Spray / Empty
**Title:** Example 3 – Null From, Many Rcpt To

- Workstation → internet `:587`
- `mailfrom` `<>`
- Several `rcptto`; subject and msg_id not logged

**Interpretation:**  
Lead. Write the empties.

**Speaker Notes:**  
Park 1.2.7.

---

### Slide 12 – Pivoting with uid
**Title:** Pivoting with the uid Field

1. Interesting `smtp` row  
2. Copy `uid`  
3. Search `conn`  
4. If `fuids` exist → **1.2.7** `files` log  

**Speaker Notes:**  
Demonstrate once.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Envelope from = real sender  
- “Invoice” = phishing  
- Query with no filter  
- Hashing the attachment here  
- Forgetting `uid`

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example.
2. Two queries: internal envelope from + external orig; many rcptto / null from / empty subject.
3. Explain the `uid` pivot.
4. Identify the four items.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Purpose of the `smtp` log?
2. Envelope vs header?
3. Why subject is not a verdict?
4. `msg_id` vs `uid`?
5. Why `uid`?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- `smtp` = mailfrom, rcptto, subject, msg_id, 5-tuple.
- Empty fields → “not logged.”
- Leads: orig vs envelope, null from, recipient spray.
- Pivot `uid` → `conn`. Attachments → **1.2.7**.
- Next: Files engine.

**Speaker Notes:**  
Do not open files lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** SMTP — Quick Reference

| Need | Look at |
|------|---------|
| Envelope | `mailfrom` `rcptto` |
| Label | `subject` |
| Message join | `msg_id` |
| Session join | `uid` → `conn` |

**Coming next:** Module 1.2.7 – Files Engine

**Footer:** SOC / Hunter / CTI Training Program
