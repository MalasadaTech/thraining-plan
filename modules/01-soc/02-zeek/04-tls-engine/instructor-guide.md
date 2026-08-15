# Instructor Guide – Module 1.2.4 – TLS Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:** SOC A/2b → B/3c → C/4c | Hunter B/3c → C/4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach students how to read, interpret, and hunt with the Zeek `ssl` log. Encrypted traffic still leaves handshake metadata that is useful for triage and hunting.

**Key Teaching Points:**
- Zeek’s TLS engine writes the `ssl` log — the name is historical.
- You are not decrypting traffic. You are reading SNI, certs, version, cipher, and (when present) JA3/JA3S.
- Focus on `server_name`, `subject`, `issuer`, `version`, `cipher`, and `uid`.
- JA3 is a lead, never a verdict.
- Always reinforce the `uid` pivot back to `conn` and `dns`.

**Common Student Challenges:**
- Thinking HTTPS is a black box with nothing to analyze.
- Treating every SNI/cert mismatch as phishing (CDNs do this constantly).
- Treating a published “malware JA3” as proof of compromise.
- Forgetting to pivot with `uid`.

**Required Materials:**
- Student Guide
- Sample `ssl` log entries (examples in the guide are sufficient for classroom use)
- Optional: Live SIEM access for query practice

---

## Learning Objectives

1. Explain the purpose of the Zeek `ssl` log.
2. Identify and interpret the most important fields.
3. Use SNI, certificate names, JA3/JA3S, version, and cipher as investigation leads.
4. Analyze an `ssl` log entry and accurately describe what occurred.
5. Create basic SIEM queries for specific TLS activity.

**Mapped Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log
- T: 1.2.4.3 – Create a SIEM query for TLS activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Name the log `ssl` immediately |
| Purpose of the ssl log         | 6 min    | Metadata, not decryption |
| Key Fields                     | 12 min   | SNI, subject, issuer, version, cipher, uid |
| SNI vs certs; JA3; version     | 12 min   | JA3 “not a verdict” |
| Walkthrough Examples           | 12 min   | Interactive |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~72 min** | |

---

## Detailed Teaching Notes

### 1. Purpose of the ssl Log

**Talking Points:**
- Payload is encrypted; handshake metadata is not (or is still logged).
- Useful for:
  - Seeing the hostname the client requested (SNI)
  - Spotting lookalike or self-signed certificates
  - Finding old TLS / weak ciphers
  - Grouping clients by how they speak TLS (JA3)
- Complements `conn` (who talked) and `dns` (what name was resolved).

**Question to ask:**  
“If you cannot read the HTTP body, what can the TLS handshake still tell you about this session?”

### 2. Key Fields

**Teaching approach:**
- Project a sample `ssl` log entry.
- Spend the majority of time on:
  - `server_name` (SNI)
  - `subject` / `issuer`
  - `version` and `cipher`
  - `ja3` / `ja3s` (and “where available”)
  - `id.orig_h`, `id.resp_h`, `id.resp_p`, `uid`

**Important reminder:**  
The `uid` links this handshake to the corresponding `conn` record and to `dns` (and later `http` / `files`).

### 3. SNI vs Certificates, JA3, Version

**Focus list:**
- Match / mismatch / missing SNI / self-signed (`subject` == `issuer`)
- JA3 = client hello fingerprint; JA3S = server hello fingerprint
- TLSv13 / TLSv12 expected; TLSv10 / TLSv11 / SSLv3 are leads

**Teaching tip:**  
Spend a minute on a legitimate CDN mismatch so students do not over-alert. Then show Example 2, where SNI impersonates Microsoft and the cert is self-signed — that combination is the point.

**JA3 caution (say this out loud):**  
A hash is not malware. It is “this client hello looks like these other client hellos.”

### 4. Examples

Work through all three examples interactively. Ask students to interpret before revealing the explanation.

**Extra point for Example 2:**  
The interesting part is the *pair*: trusted-looking SNI + untrusted lookalike/self-signed cert. Either fact alone is weaker.

**Extra point for Example 3:**  
Port 8443 + TLS 1.0 + RC4 is a stack of weak signals. One old-TLS connection to an internal appliance would be a different conversation.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward.

**What good answers look like:**

**Summaries:**
- Example 1: Normal TLS 1.3 HTTPS; SNI and certificate agree.
- Example 2: Client requested a Microsoft hostname; certificate is a self-signed lookalike — suspicious.
- Example 3: Deprecated TLS 1.0 and weak cipher on port 8443 to a generic “update” name.

**Queries (pseudo examples):**
```
ssl
| where isnotempty(server_name) and subject !contains server_name
```
```
ssl
| where version in ("TLSv10", "TLSv11", "SSLv3")
    or ja3 == "<rare-or-watchlisted-hash>"
```

Empty-SNI variant (also acceptable):
```
ssl
| where isempty(server_name) and id.resp_p in (443, 8443)
```

**uid pivot explanation:**  
Copy the `uid` from the `ssl` log entry and search `conn` (and `dns`) for the same `uid` to see duration, bytes, connection state, and the name that was resolved.

---

## Knowledge Check – Answer Key

1. **What is the primary purpose of the Zeek `ssl` log?**  
   **Answer:** To record TLS/SSL handshake metadata (SNI, certificates, version, cipher, fingerprints) so analysts can investigate encrypted sessions without decrypting the payload.

2. **Which field contains the Server Name Indication (SNI)?**  
   **Answer:** `server_name`

3. **What does a JA3 hash represent, and why is it not a malware verdict?**  
   **Answer:** It fingerprints how a client builds its TLS Client Hello. Many legitimate programs share a JA3, and hashes change when software updates. It is a lead, not proof.

4. **Why does an SNI that does not match the certificate subject deserve a closer look?**  
   **Answer:** It can indicate phishing, impersonation, or a self-signed decoy. It can also be a CDN — so it is a reason to investigate, not an automatic true positive.

5. **Why is the `uid` field important when analyzing TLS activity?**  
   **Answer:** It links the handshake to the corresponding `conn` record and to other protocol logs (`dns`, later `http` / `files`) so you can build full context.

---

## Additional Instructor Resources

- Zeek ssl.log documentation
- Internal list of expected JA3 values for standard images (if you have one)
- Internal split of known-good vs watchlisted issuers
- Next recommended module: 1.2.5 HTTP Engine
