# Module 1.2.6 – SMTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C ; 1.2.6.2 2b / 3c / 4c ; 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C ; 1.2.6.2 3c / 4c / 4c ; 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B ; 1.2.6.2 1a / 1a / 2b ; 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `smtp` row: mail from, rcpt to, subject, message ID, and who talked to whom.
2. Describe what an `smtp` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`smtp`** log to see a mail transaction on the **wire**. **1.2.5** was HTTP. This hour is envelope and a few headers — not a mailbox, not the attachment bytes. Attachments are **1.2.7**. The process that spoke SMTP is **1.1.4**.

**`smtp`** is one row for a transaction Zeek parsed.

| Idea | What to read |
|------|----------------|
| **Mail from** | `mailfrom` — envelope MAIL FROM. Who the *session* claimed as sender |
| **Rcpt to** | `rcptto` — envelope RCPT TO (can be a list) |
| **Subject** | `subject` — the Subject header. Empty = not logged. Easy to spoof |
| **Message ID** | `msg_id` — Message-ID when logged. Not a file hash |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` (often 25 / 587) |

This is the **extract**. Encrypted submission may have no SMTP fields — that handshake was **1.2.4**. Do not invent a mail-gateway name.

**What good looks like:**

- Describe: one sentence — envelope from, envelope to, subject if logged, orig → resp. Do not name a process. Do not declare phishing.
- Given: `mailfrom` an outside address, `rcptto` a user, `subject` present (invoice), `msg_id` present. **What occurred:** that client sent envelope mail from A to B with that subject. The `.vbs` file create on the host is a different row (**1.1.3**).
- Query: names a **specific** pattern (`mailfrom`, `rcptto`, subject, or dest), not “all `smtp` rows.”

---

## 2. Knowledge Check

1. `mailfrom` is the attachment hash. True or false?
2. Envelope from an outside address, `rcptto` a user, subject present. In one sentence, what occurred?
3. A SIEM query that matches every `smtp` row is a good “specific SMTP activity” query. True or false?

---

## 3. Summary

An `smtp` row is envelope from/to, subject, message ID, and who talked to whom. The process and the attachment hash are not on this row. A query names a specific pattern.

**Next:** **1.2.7** Files engine.

---

## 4. Related modules

- 1.2.5 – HTTP engine (previous)
- 1.2.7 – Files engine
- 1.2.4 – TLS engine
- 1.1.4 – Host-observed network
