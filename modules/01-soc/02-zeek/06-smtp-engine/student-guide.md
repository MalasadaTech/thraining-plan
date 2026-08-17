# Module 1.2.6 – SMTP Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.6.1 A / B / C · 1.2.6.2 2b / 3c / 4c · 1.2.6.3 2b / 3c / 4c  
- Hunter: 1.2.6.1 B / C / C · 1.2.6.2 3c / 4c / 4c · 1.2.6.3 3c / 4c / 4c  
- CTI: 1.2.6.1 A / A / B · 1.2.6.2 1a / 1a / 2b · 1.2.6.3 1a / 1a / 2b  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the Zeek `smtp` log and the fields mail from, rcpt to, subject, message ID, and source/destination.
2. Analyze a Zeek SMTP log entry and accurately describe what occurred.
3. Write a SIEM query that finds a *specific* SMTP pattern — not “all SMTP.”
4. Pivot from an `smtp` row to `conn` using `uid`.

**Mapped Proficiency Items:**
- K: 1.2.6.1 – SMTP engine
- T: 1.2.6.2 – Analyze a Zeek SMTP log and accurately describe what occurred
- T: 1.2.6.3 – Create a SIEM query to detect specific SMTP activity

---

## 1. Key Concepts

### 1.1 Purpose of the smtp Log

Zeek’s SMTP engine writes the **`smtp` log**. Each row is an SMTP transaction the sensor saw on the wire: who the envelope says the mail is **from**, who it is **to**, the **subject**, and the **message ID**, plus the 5-tuple.

This is **not** mailbox forensics and **not** a full `.eml`. You get protocol metadata. Attachments, when extracted, land in the **`files` log (1.2.7)**. TLS on port 587/465 is a different row (`ssl`, **1.2.4**) if the session was encrypted before SMTP was visible.

| This lesson | Later / other |
|-------------|---------------|
| Envelope + headers Zeek logged | File hashes of attachments — **1.2.7** |
| Cleartext or still-parsed SMTP | Detection rules — **1.3** |
| Sensor SMTP | Host process that spoke on 25/587 — **1.1.4** |

If subject or message ID is empty, say so. Do not invent it.

### 1.2 Key Fields

| Field | Description | Why it matters |
|-------|-------------|----------------|
| `ts` | Timestamp | When the transaction happened |
| `uid` | Connection identifier | Links to `conn`, `files`, `weird` |
| `id.orig_h` / `id.orig_p` | Client IP / port | Who opened the SMTP session |
| `id.resp_h` / `id.resp_p` | Server IP / port | Mail server (25, 587, 465, …) |
| `mailfrom` | Envelope MAIL FROM | Who the *session* claimed as sender |
| `rcptto` | Envelope RCPT TO (often a list) | Who the *session* claimed as recipient(s) |
| `subject` | Subject header | What the message was labeled |
| `msg_id` | Message-ID header | Identifier for this message (when logged) |

**Envelope vs header (support only):** `mailfrom` / `rcptto` are SMTP commands. Some deployments also log header `from` / `to`. If both exist and disagree, describe both. Do not turn this hour into a full spoofing course.

**Most critical for daily work:** `mailfrom`, `rcptto`, `subject`, `msg_id`, `id.orig_h`, `id.resp_h`, `id.resp_p`, `uid`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Internal `mailfrom` @buildingc.internal to an internal `rcptto`, ordinary subject | External `mailfrom` impersonating a colleague, or `mailfrom` empty / `<>` with an odd subject |
| One or a few `rcptto` | Many `rcptto` on one `uid` (spray) |
| Subject matches a known thread | Subject is invoice/urgent/wire + dest you do not expect |
| `msg_id` present and unique | `msg_id` missing, reused, or clearly malformed |
| Orig is the mail gateway | User workstation speaking SMTP to the internet |

**mailfrom / rcptto:** These are the envelope. Describe them as “envelope from/to.” A display name in a header is extra if you have it.

**subject:** Useful and easy to spoof. Empty → “not logged.” Do not treat “invoice” as malware.

**msg_id:** Helps you join two sightings of the same message. Missing → “not logged.” It is not a hash of the attachment.

Always copy `uid` and search `conn`. If `fuids` are present, that is the door to **1.2.7** — do not analyze the hash here.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Internal Mail

```
ts: 2026-08-15T14:22:10.004Z
uid: CSmtpAb12Cd34Ef56
id.orig_h: 10.10.8.40
id.orig_p: 49811
id.resp_h: 10.10.8.25
id.resp_p: 25
mailfrom: <jlee@buildingc.internal>
rcptto: <finance@buildingc.internal>
subject: Q3 notes for Friday
msg_id: <20260815142210.1A2B@buildingc.internal>
```

**What occurred:** Internal mail host sent envelope from `jlee` to `finance`, ordinary subject, message ID present. Dest is the internal SMTP server on 25. Expected.

**Not done:** Did not hunt attachments. Did not call it phishing.

### Example 2: External Envelope, Invoice Subject (Lead)

```
uid: CSmtpXy98Zt76Uv54
id.orig_h: 203.0.113.88
id.orig_p: 51990
id.resp_h: 10.10.8.25
id.resp_p: 25
mailfrom: <jlee@buildingc.internal>
rcptto: <finance@buildingc.internal>
subject: Urgent invoice copy attached
msg_id: <random-not-from-buildingc@nightowl-updates.net>
```

**What occurred:** An **internet** client (`203.0.113.88`) used envelope from `jlee@buildingc.internal` to finance, invoice subject, message ID **not** from the internal domain.

**Interpretation:** Lead. Describe orig IP + mailfrom + rcptto + subject + msg_id. Do not declare BEC. Pivot `uid` to `conn`. If there is a `fuid`, open **1.2.7** next — not now.

### Example 3: Many Recipients, Empty Subject (Lead)

```
uid: CSmtpQr11Mn22Op33
id.orig_h: 10.10.50.88
id.orig_p: 50220
id.resp_h: 198.51.100.25
id.resp_p: 587
mailfrom: <>
rcptto: <a@vendor.net>, <b@vendor.net>, <c@vendor.net>, <d@vendor.net>
subject: -
msg_id: -
```

**What occurred:** A **workstation** opened SMTP to an internet mail server on 587. Envelope from is null (`<>`). Several `rcptto`. Subject and message ID **not logged**.

**Interpretation:** Lead. Write “subject not logged” and “msg_id not logged.” Name the recipient count and the null envelope from. Pivot `uid` to `conn`. Do not write a 2.6 or phishing-playbook lecture.

---

## 3. Hands-On Exercise

**Objective:** Practice describing SMTP rows and writing queries that find a specific pattern.

**Instructions:**

1. Review the three examples and write a one-sentence summary for each (expected vs lead).
2. Write **two SIEM-style pseudo-queries**:
   - One for **envelope from** that claims `@buildingc.internal` while `id.orig_h` is **not** internal.
   - One for **one connection** with many `rcptto` (or null `mailfrom`, or empty subject — pick one and say why).
3. Explain how you would pivot from a suspicious `smtp` entry to `conn` using `uid`.
4. For each item below, say **SMTP event** or **not this log**. Give one reason.
   - Zeek `smtp` `mailfrom` jlee → finance
   - Zeek `http` POST `/api/v1/beacon`
   - Zeek `files` SHA256 of an attachment
   - MDE `DeviceNetworkEvents` `outlook.exe` → `:587`

**Expected Outcome:**
- Accurate short summaries
- Two specific SMTP queries
- A correct `uid` pivot
- Four identifications with a reason each

---

## 4. Knowledge Check

1. What is the primary purpose of the Zeek `smtp` log?
2. What is the difference between `mailfrom` / `rcptto` and a From/To *header* if both are logged?
3. Why is `subject` useful but not a verdict?
4. What does `msg_id` give you that `uid` does not?
5. Why is the `uid` field important when analyzing SMTP activity?

---

## 5. Summary

- The SMTP engine writes the `smtp` log: envelope and selected headers, not a full mailbox.
- Critical fields: `mailfrom`, `rcptto`, `subject`, `msg_id`, addresses/ports, `uid`.
- Empty subject or message ID → “not logged.”
- External orig + internal envelope from, null mailfrom, recipient spray are leads.
- Always pivot with `uid` to `conn`. Attachments are **1.2.7**.
- Next: Files engine (**1.2.7**).

---

## 6. References & Further Reading

- Zeek smtp.log documentation: https://docs.zeek.org/en/current/scripts/base/protocols/smtp/main.zeek.html
- Related modules:
  - 1.1.4 – Network activity (endpoint)
  - 1.2.2 – Conn engine
  - 1.2.4 – TLS engine
  - 1.2.5 – HTTP engine (previous)
  - 1.2.7 – Files engine (next)
