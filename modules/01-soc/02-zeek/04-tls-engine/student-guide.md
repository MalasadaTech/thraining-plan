# Module 1.2.4 – TLS Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3-level (A/2b) → 5-level (B/3c) → 7-level (C/4c)  
- Hunter: Starts higher (B/3c → C/4c)  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Zeek `ssl` log and why TLS metadata matters when the payload is encrypted.
2. Identify and interpret the most important fields in an `ssl` log entry.
3. Use SNI, certificate names, JA3/JA3S, TLS version, and cipher as investigation leads.
4. Analyze an `ssl` log entry and accurately describe what occurred.
5. Create basic SIEM queries to detect specific TLS activity.

**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

---

## 1. Key Concepts

### 1.1 Purpose of the ssl Log

Zeek’s TLS engine writes the **`ssl` log**. The name is historical (SSL). Almost everything you see today is TLS.

You usually cannot read the bytes inside an HTTPS session. You still get useful metadata from the handshake:

- What hostname the client asked for (SNI)
- What name is on the server certificate
- Who issued that certificate
- Which TLS version and cipher were negotiated
- A fingerprint of how the client (and sometimes the server) speaks TLS (JA3 / JA3S)

That is often enough for triage and hunting: phishing domains, unusual encryption, odd destinations on 443/8443, and clients that do not look like a normal browser.

### 1.2 Key Fields

Here are the fields you must know well:

| Field            | Description                                      | Why It Matters |
|------------------|--------------------------------------------------|----------------|
| `ts`             | Timestamp of the TLS handshake                   | When it happened |
| `uid`            | Unique connection identifier                     | Links to `conn`, `dns`, and other logs |
| `id.orig_h`      | Client (source) IP                               | Who initiated |
| `id.orig_p`      | Client port                                      | Ephemeral in normal browsing |
| `id.resp_h`      | Server (destination) IP                          | Who was contacted |
| `id.resp_p`      | Server port                                      | Usually 443; odd ports deserve a look |
| `server_name`    | Server Name Indication (SNI)                     | Hostname the client requested |
| `subject`        | Certificate subject                              | Name on the presented cert |
| `issuer`         | Certificate issuer                               | Who signed the cert |
| `ja3`            | Client TLS fingerprint (where available)         | How the client hello is built |
| `ja3s`           | Server TLS fingerprint (where available)         | How the server hello is built |
| `version`        | Negotiated TLS version                           | Old versions are a lead |
| `cipher`         | Negotiated cipher suite                          | Weak ciphers are a lead |

**Most critical fields for daily work:**  
`server_name`, `subject`, `issuer`, `ja3`, `ja3s`, `version`, `cipher`, `id.orig_h`, `id.resp_h`, `id.resp_p`, `uid`

JA3/JA3S are not in every Zeek deployment. If the fields are empty, work with SNI, certs, version, and cipher.

### 1.3 SNI vs Certificate Names

**SNI (`server_name`)** is the hostname in the Client Hello. It is sent in the clear on older TLS and is still commonly logged even with TLS 1.3 (encrypted SNI is rare in most enterprise traffic).

**Subject (`subject`)** is the name on the server certificate (CN and, in richer logs, SAN).

They should usually tell a consistent story:

| Pattern | Typical meaning |
|---------|-----------------|
| SNI and subject match a known site | Normal HTTPS |
| SNI is a well-known brand; subject is a lookalike or self-signed | Phishing, malware, or intercept |
| SNI present; subject is a CDN or cloud name | Often normal (fronting / shared hosting) — check context |
| No SNI | Old client, some APIs, or an attempt to hide the hostname |
| Subject equals issuer | Self-signed certificate |

A single mismatch is not automatically malicious. CDNs and load balancers produce mismatches every day. Combine SNI, subject, issuer, destination IP, and the `uid` pivot before you decide.

### 1.4 JA3 and JA3S

**JA3** hashes selected fields from the TLS Client Hello (version, ciphers, extensions, and so on). Clients that speak TLS the same way produce the same hash.

**JA3S** is the same idea for the Server Hello.

Use them as a **lead**, not a verdict:

- A rare JA3 on a workstation that normally looks like Chrome is interesting.
- A JA3 that is widely published as “malware” is also used by plenty of legitimate tools.
- JA3 changes when a browser or library updates. Do not treat a hash as a permanent identity.

If `ja3` / `ja3s` are missing in your environment, say so in your notes and move on. The rest of this module still applies.

### 1.5 Version and Cipher

| Version | Notes |
|---------|--------|
| **TLSv13** | Current default for modern browsers |
| **TLSv12** | Still common and usually acceptable |
| **TLSv11 / TLSv10** | Deprecated; unexpected on user browsers |
| **SSLv3 / SSLv2** | Should not appear on a healthy network |

Weak or obsolete ciphers (RC4, export suites, NULL, anonymous DH) are a hunting and compliance lead. A single old-TLS connection to an internal printer is different from a fleet of workstations doing TLS 1.0 to the internet.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal HTTPS

```
ts: 2026-08-14T19:40:11.210Z
uid: CTlsAbCdEfGhIjKl
id.orig_h: 10.10.50.23
id.orig_p: 51244
id.resp_h: 93.184.216.34
id.resp_p: 443
version: TLSv13
cipher: TLS_AES_128_GCM_SHA256
server_name: www.example.com
subject: CN=www.example.com
issuer: CN=DigiCert Global G2 TLS RSA SHA256 2020 CA1
ja3: 579ccef312d18482fc42e2b822ca2430
ja3s: 15af977ce25de452b96affa2addb1036
```

**Interpretation:**  
Internal host opened a current TLS 1.3 session to port 443. SNI and certificate subject match. This is normal web traffic. Next step if you still care: pivot on `uid` to `conn` and `dns` to confirm the rest of the session.

### Example 2: SNI / Certificate Mismatch (Self-Signed)

```
id.orig_h: 10.10.50.88
id.resp_h: 198.51.100.80
id.resp_p: 443
version: TLSv12
cipher: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
server_name: login.microsoftonline.com
subject: CN=secure-login-microsoft.com
issuer: CN=secure-login-microsoft.com
ja3: 3b5074b1b5d032e5620f69f9f700ff0e
```

**Interpretation:**  
The client asked for Microsoft’s login hostname (SNI), but the certificate is a lookalike name and is self-signed (`subject` equals `issuer`). Treat this as suspicious until proven otherwise. Pivot with `uid` to `conn` (bytes, duration, state) and `dns` (what name actually resolved).

### Example 3: Old TLS and Weak Cipher on an Unusual Port

```
id.orig_h: 10.10.22.17
id.resp_h: 203.0.113.90
id.resp_p: 8443
version: TLSv10
cipher: TLS_RSA_WITH_RC4_128_SHA
server_name: update.not-a-real-cdn.example
subject: CN=update.not-a-real-cdn.example
issuer: CN=Some Cheap CA
ja3: 6734f37431670b3ab4292b8f60f29984
```

**Interpretation:**  
TLS 1.0 and RC4 on port 8443 are not how a current browser talks to a normal site. The hostname is generic “update” branding. Worth a hunt: who is 10.10.22.17, how often does this JA3 appear, and what does the matching `conn` record look like?

---

## 3. Hands-On Exercise

**Objective:** Practice interpreting TLS logs and writing simple detection logic.

**Instructions:**

1. Review the three examples above and write a one-sentence summary for each.
2. Write a SIEM-style pseudo-query that would find:
   - Sessions where `server_name` does not appear in `subject` (or SNI is empty)
   - External sessions using TLS 1.0 / 1.1, or a JA3 you have marked as rare in your environment
3. Explain how you would pivot from a suspicious `ssl` entry to the related connection and DNS activity using the `uid`.

**Expected Outcome:**
- Accurate short summaries
- Two useful pseudo-queries
- Correct understanding of the `uid` pivot to the `conn` log and `dns` log

---

## 4. Knowledge Check

1. What is the primary purpose of the Zeek `ssl` log?
2. Which field contains the Server Name Indication (SNI)?
3. What does a JA3 hash represent, and why is it not a malware verdict?
4. Why does an SNI that does not match the certificate subject deserve a closer look?
5. Why is the `uid` field important when analyzing TLS activity?

---

## 5. Summary

- The TLS engine writes the `ssl` log: handshake metadata, not decrypted content.
- Critical fields: `server_name`, `subject`, `issuer`, `ja3` / `ja3s`, `version`, `cipher`, addresses/ports, and `uid`.
- SNI vs certificate mismatches, missing SNI, self-signed certs, old TLS, and weak ciphers are leads — not automatic incidents.
- JA3/JA3S (when present) describe *how* a client or server speaks TLS. They are not an identity or a conviction.
- Always pivot with `uid` to `conn` and `dns` (and later `http` / `files`) for full context.

---

## 6. References & Further Reading

- Zeek ssl.log documentation: https://docs.zeek.org/en/current/scripts/base/protocols/ssl/main.zeek.html
- Related modules:
  - 1.2.1 – Zeek Concepts
  - 1.2.2 – Conn Engine
  - 1.2.3 – DNS Engine
  - 1.2.5 – HTTP Engine
