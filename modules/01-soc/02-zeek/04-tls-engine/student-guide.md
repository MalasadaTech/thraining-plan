# Module 1.2.4 – TLS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.4.1 A / B / C ; 1.2.4.2 2b / 3c / 4c ; 1.2.4.3 2b / 3c / 4c  
- Hunter: 1.2.4.1 B / C / C ; 1.2.4.2 3c / 4c / 4c ; 1.2.4.3 3c / 4c / 4c  
- CTI: 1.2.4.1 A / A / B ; 1.2.4.2 1a / 1a / 2b ; 1.2.4.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek TLS (`ssl`) row: SNI, cert names, JA3 where logged, version, cipher, and who talked to whom.
2. Describe what a TLS log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.4.1 – TLS engine
- T: 1.2.4.2 – Analyze a Zeek TLS log and accurately describe what occurred
- T: 1.2.4.3 – Create a SIEM query to detect specific TLS activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`ssl`** log (the TLS engine; the name is historical) to see the **handshake**, not the decrypted bytes. **1.2.3** was the DNS extract. This hour is TLS on the same wire. It does **not** name the initiating process. That was **1.1.4**.

**TLS** is one row for a handshake Zeek saw.

| Idea | What to read |
|------|----------------|
| **SNI** | `server_name` — the hostname in the Client Hello. Empty = not logged / not sent. |
| **Subject / issuer** | `subject` / `issuer` — the name on the cert, and who signed it |
| **JA3 / JA3S** | Client / server TLS fingerprints **where available**. Missing = not logged, not “no TLS.” |
| **Version / cipher** | `version`, `cipher` — what was negotiated |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` |

JA3 is how the client spoke TLS, not a malware name. Do not treat a hash as a verdict. Do not invent a JA3 value.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open HTTP fields yet.

**What good looks like:**

- Describe: one sentence — who talked to whom, SNI if present, subject/issuer, version/cipher, JA3 only if logged. Do not name a process. Do not call it phishing from one mismatch.
- Given: `id.resp_h` `203.0.113.88`, `id.resp_p` `443`, `server_name` empty, `version` / `cipher` present. **What occurred:** that host completed a TLS handshake to `203.0.113.88:443`. SNI not logged. The `conn` is a different row (**1.2.2**). The A record was **1.2.3**.
- Query: names a **specific** pattern (SNI, subject, version, or dest IP/port), not “all `ssl` rows.”

---

## 2. Knowledge Check

1. `server_name` is the name on the server certificate. True or false?
2. Workstation → `203.0.113.88:443`, `server_name` empty, version and cipher present. In one sentence, what occurred?
3. A SIEM query that matches every `ssl` row is a good “specific TLS activity” query. True or false?

---

## 3. Summary

A TLS row is the handshake: SNI, cert, version, cipher, who talked to whom. JA3 only if logged. The process is not on this row. A query names a specific pattern.

**Next:** **1.2.5** HTTP engine.

---

## 4. Related modules

- 1.2.3 – DNS engine (previous)
- 1.2.5 – HTTP engine
- 1.2.2 – Conn engine
- 1.1.4 – Host-observed network
