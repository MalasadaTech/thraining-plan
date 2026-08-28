# Instructor Guide – Module 1.2.4 – TLS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read a Zeek TLS (`ssl`) event and describe it. Say what a specific SIEM query looks like.

**Context (plain language):**

- What this lesson is for: SOC analysts read the handshake when the payload is encrypted — who talked to whom, SNI, certificate, version, and cipher.
- How it hooks to the lesson before: 1.2.3 is the DNS extract on the same wire. This lesson is TLS.
- How it hooks to the lesson after: 1.2.5 is HTTP — cleartext fields, not this handshake.
- Why we are doing it this way: encrypted traffic still has a handshake you can describe before anyone opens HTTP or names a process.
- What we are *not* doing in this lesson: process name (1.1.4). Phishing catalog. uid-pivot as a unit. Invented JA3. HTTP fields. PCAP analysis. No lab.
- Extra step: none.

Use the same names as the student guide: **`ssl` log**, **SNI** (`server_name`), **subject**, **issuer**, **JA3 / JA3S**, **version**, and **cipher**. **Row** is the SIEM-table gloss from the student intro, not the headline word. The given uses `203.0.113.88:443` with empty SNI. Empty SNI means the Client Hello did not carry `server_name`, or Zeek did not log it — not “the certificate has no name,” and not a host-log URL field. Do not tell the intro plot.

**Key Teaching Points:**
- TLS event, not decrypted HTTP, not the process.
- SNI is Client Hello, not the certificate subject.
- JA3 only where logged — not a verdict. Missing is not “no TLS.”
- A query is specific, not every `ssl` event.

**Common Student Challenges:**
- Treat `server_name` as the certificate subject. Why: both look like hostnames. Example: writing “the cert is for `example.com`” from SNI alone.
- Treat a missing JA3 as “no TLS,” or a JA3 value as malware. Why: JA3 is optional metadata, not the handshake itself. Example: “this is not TLS because `ja3` is empty.”
- Write `ssl=*` as a “specific” query. Why: the task is a named pattern. Example: every `ssl` event with no SNI, subject, version, or dest filter.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Handshake, not payload |
| Key Concepts            | 16 min    | Fields; two products |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~25 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: encrypted traffic still needs a description of the handshake.
- Walk SNI versus subject first. Empty `server_name` means not sent or not logged, not “the certificate has no name.”
- JA3 only where the shop logs it. Missing is not “no TLS.” Do not treat JA3 as a malware name.
- Walk version, cipher, and orig/resp. Originator started the talk from Zeek’s view; responder was contacted.
- Walk the given: handshake to `203.0.113.88:443`, SNI not logged. One sentence. Do not name a process.
- If they name `powershell.exe`: that is 1.1.4. Stay on this TLS event.
- If they write `ssl=*`: that is not a specific query.
- If they open HTTP fields: that is 1.2.5.

---

## Knowledge Check – Answer Key

1. **`server_name` is the name on the server certificate. True or false?**  
   **Answer:** False. It is SNI from the Client Hello. The certificate name is `subject`.  
   **Explanation:** SNI is what the client asked for. Subject is what the certificate presents. They can differ.

2. **Workstation → 203.0.113.88:443, SNI empty, version/cipher present. What occurred?**  
   **Answer:** That host completed a TLS handshake to 203.0.113.88 on 443. SNI was not logged.  
   **Explanation:** Version and cipher show negotiation happened. Empty `server_name` is a gap, not a process name and not a phishing verdict.

3. **A query that matches every ssl event is specific. True or false?**  
   **Answer:** False. A good query names a specific pattern (SNI, subject, version, or dest).  
   **Explanation:** Every `ssl` event is a table dump, not a detection for this task.

---

## Additional Instructor Resources

- Next: 1.2.5 HTTP engine
