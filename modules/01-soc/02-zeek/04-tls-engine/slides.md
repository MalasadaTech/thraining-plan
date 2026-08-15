# Module 1.2.4 – TLS Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.2.4 – TLS Engine  
**Subtitle:** SOC Analyst & Threat Hunter Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Introduce the module. Say immediately that Zeek records this in the `ssl` log. You are teaching metadata, not decryption.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Zeek `ssl` log
2. Identify and interpret the most important fields
3. Use SNI, certs, JA3/JA3S, version, and cipher as leads
4. Analyze an `ssl` log entry and accurately describe what occurred
5. Create basic SIEM queries for specific TLS activity

**Mapped Items:**  
K: 1.2.4.1 | T: 1.2.4.2 | T: 1.2.4.3

**Speaker Notes:**  
This module builds on Conn (`uid`, ports) and DNS (hostname context).

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose of the ssl log
- Critical fields
- SNI vs certificates
- JA3 / JA3S, version, cipher
- Analysis examples
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
Quick roadmap.

---

### Slide 4 – Purpose of the ssl Log
**Title:** Purpose of the ssl Log

- Written by Zeek’s TLS engine (`ssl` is a historical name)
- Records handshake **metadata**, not the decrypted payload
- High value for seeing:
  - Hostname the client requested (SNI)
  - Certificate subject and issuer
  - TLS version and cipher
  - Client/server fingerprints (JA3 / JA3S)
- Complements `conn` (who talked) and `dns` (what resolved)

**Key Point:** Encrypted traffic is not a black box.

**Speaker Notes:**  
Ask: “If you cannot read the HTTP body, what can the handshake still tell you?”

---

### Slide 5 – Critical Fields
**Title:** Critical Fields

| Field          | Description                     | Priority |
|----------------|---------------------------------|----------|
| `server_name`  | SNI — hostname client requested | Highest  |
| `subject`      | Name on the server certificate  | High     |
| `issuer`       | Who signed the certificate      | High     |
| `version`      | Negotiated TLS version          | High     |
| `cipher`       | Negotiated cipher suite         | High     |
| `ja3` / `ja3s` | Client / server fingerprints    | High*    |
| `uid`          | Links to conn and other logs    | Critical |
| `id.resp_p`    | Server port                     | Medium   |

\*Where available in your Zeek deployment.

**Most important for daily work:**  
`server_name`, `subject`, `issuer`, `version`, `cipher`, `ja3`, `uid`

**Speaker Notes:**  
If JA3 is not logged here, say so and keep going.

---

### Slide 6 – SNI vs Certificate Names
**Title:** SNI vs Certificate Names

| Pattern | Typical reading |
|---------|-----------------|
| SNI and subject match a known site | Normal |
| Trusted SNI + lookalike or self-signed cert | Suspicious |
| SNI + CDN / cloud certificate | Often normal — check context |
| No SNI | Old client, some APIs, or hiding the name |
| `subject` equals `issuer` | Self-signed |

**Analyst Tip:** A mismatch is a lead, not an automatic incident. CDNs mismatch every day.

**Speaker Notes:**  
Show a mental picture: Client Hello says “I want X”; the cert says “I am Y.”

---

### Slide 7 – JA3, Version, Cipher
**Title:** JA3 / JA3S, Version, and Cipher

- **JA3** fingerprints the Client Hello — how the client speaks TLS
- **JA3S** fingerprints the Server Hello
- A hash is **not** malware and is **not** a permanent identity
- Expected versions: **TLSv13**, **TLSv12**
- Leads: **TLSv10**, **TLSv11**, **SSLv3**, RC4 / NULL / export ciphers

**Analyst Tip:** Rare JA3 on a standard workstation image is more interesting than a “malware JA3” hit by itself.

**Speaker Notes:**  
Say the “not a verdict” line out loud. Then move to examples.

---

### Slide 8 – Example 1: Normal HTTPS
**Title:** Example 1 – Normal HTTPS

```
id.orig_h: 10.10.50.23
id.resp_p: 443
version: TLSv13
server_name: www.example.com
subject: CN=www.example.com
issuer: CN=DigiCert Global G2 TLS RSA SHA256 2020 CA1
```

**Interpretation:**  
Current TLS 1.3. SNI and certificate agree. Normal web traffic.

**Speaker Notes:**  
Ask students to interpret first, then confirm.

---

### Slide 9 – Example 2: SNI / Cert Mismatch
**Title:** Example 2 – SNI / Certificate Mismatch

```
id.orig_h: 10.10.50.88
id.resp_p: 443
server_name: login.microsoftonline.com
subject: CN=secure-login-microsoft.com
issuer: CN=secure-login-microsoft.com
```

**Interpretation:**  
Client asked for Microsoft. Certificate is a self-signed lookalike. Suspicious until proven otherwise.

**Speaker Notes:**  
The pair is the point: trusted SNI + untrusted cert. Either fact alone is weaker.

---

### Slide 10 – Example 3: Old TLS, Weak Cipher
**Title:** Example 3 – Old TLS on an Unusual Port

```
id.orig_h: 10.10.22.17
id.resp_p: 8443
version: TLSv10
cipher: TLS_RSA_WITH_RC4_128_SHA
server_name: update.not-a-real-cdn.example
```

**Interpretation:**  
TLS 1.0 + RC4 + port 8443 is not a modern browser talking to a normal site. Hunt it.

**Speaker Notes:**  
Contrast with one old-TLS session to an internal printer — stack of signals vs. one weak signal.

---

### Slide 11 – Pivoting with uid
**Title:** Pivoting with the uid Field

**Standard workflow:**
1. Find an interesting `ssl` record
2. Copy the `uid`
3. Search the `conn` log for the same `uid`
4. Search the `dns` log for the same `uid`
5. Optionally pivot further to `http`, `files`, or `weird`

This gives you duration, bytes, connection state, and the name that was resolved.

**Speaker Notes:**  
This is a critical habit. Demonstrate even with static examples.

---

### Slide 12 – Hunting & Detection Ideas
**Title:** Useful TLS-Based Detections / Hunts

- `server_name` not reflected in `subject`
- Empty SNI on 443 / 8443 to the internet
- Self-signed certificates (`subject` == `issuer`) to external IPs
- TLSv10 / TLSv11 / SSLv3 from user subnets
- Weak ciphers (RC4, NULL, export)
- Rare or watchlisted JA3 on standard workstations
- TLS on unexpected ports combined with odd SNI

**Speaker Notes:**  
Starting points only. Thresholds and allow-lists belong to the local environment.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. Write a one-sentence summary for each of the three examples.
2. Write a pseudo-query that finds:
   - SNI missing from `subject` (or empty SNI)
   - External TLS 1.0 / 1.1, or a rare/watchlisted JA3
3. Explain how you would pivot from a suspicious `ssl` entry to `conn` and `dns`.

**Speaker Notes:**  
Let students work. Then review using the Instructor Guide answer key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. What is the primary purpose of the Zeek `ssl` log?
2. Which field contains the SNI?
3. What does a JA3 hash represent, and why is it not a malware verdict?
4. Why does SNI that does not match `subject` deserve a closer look?
5. Why is the `uid` field important when analyzing TLS activity?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- The TLS engine writes the `ssl` log — metadata, not decrypted content
- Master `server_name`, `subject`, `issuer`, `version`, `cipher`, `ja3`, `uid`
- Mismatches, missing SNI, old TLS, and weak ciphers are leads
- JA3/JA3S describe *how* TLS is spoken, not *who is guilty*
- Always pivot with `uid` to `conn` and `dns`

**Speaker Notes:**  
Reinforce the main points one final time.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 1.2.5 – HTTP Engine

**Resources:**
- Student Guide for this module
- Zeek ssl.log documentation

**Speaker Notes:**  
Open the floor for questions.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** TLS Quick Reference

**Highest-value fields:**  
`server_name` · `subject` · `issuer` · `version` · `cipher` · `ja3` · `uid`

**Key leads:**  
SNI / cert mismatch · self-signed · empty SNI · TLSv10/11 · weak cipher

**Core habit:**  
Interesting `ssl` row → copy `uid` → pivot to `conn` and `dns`

**Speaker Notes:**  
This slide can be left up as a reference or printed as a handout.

---

## Design Notes for Slide Builder

- Keep tables clean and large enough to read
- Use monospace formatting for log examples
- Visually highlight `server_name`, `subject`, and `uid`
- Consistent footer with module number
- Minimal text — let examples and tables teach
