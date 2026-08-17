# Module 1.2.5 – HTTP Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C ; 1.2.5.2 2b / 3c / 4c ; 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C ; 1.2.5.2 3c / 4c / 4c ; 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B ; 1.2.5.2 1a / 2b / 3c ; 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `http` row: method, host, URI, User-Agent, status, and who talked to whom.
2. Describe what an `http` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log and accurately describe what occurred
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`http`** log to see a request/response on the **wire**. **1.2.4** was the TLS handshake. This hour is HTTP metadata — not the full body, not the process. The process was **1.1.4**.

**`http`** is one row for a request/response pair Zeek parsed.

| Idea | What to read |
|------|----------------|
| **Method** | `method` — GET, POST, PUT, HEAD, … |
| **Host** | `host` — the Host header. Empty = not logged. |
| **URI / URL** | `uri` is the path and query. **Host + URI** is the URL you describe. |
| **User-Agent** | `user_agent` — what the client claimed. Can lie. Empty = not logged. |
| **Status** | `status_code` — 200 is not “benign.” 404 is not “safe.” |
| **Source / dest** | `id.orig_h` / `id.orig_p` → `id.resp_h` / `id.resp_p` |

You usually do **not** get the body. File extract is **1.2.7**. Encrypted HTTPS often has no `http` row — that was the `ssl` extract (**1.2.4**).

**What good looks like:**

- Describe: one sentence — method, host+URI, status, UA if logged, orig → resp. Do not name a process. Do not invent the body.
- Given: `GET`, `uri` `/update.exe`, `id.resp_h` `203.0.113.88`, `id.resp_p` `8080`, `status_code` `200`, `user_agent` empty. **What occurred:** that host **GET** `/update.exe` from `203.0.113.88:8080` and got **200**. UA not logged. The TLS `:443` handshake is a different row.
- Query: names a **specific** pattern (method, host, URI, UA, or dest), not “all `http` rows.”

---

## 2. Knowledge Check

1. `host` is the destination IP. True or false?
2. `GET /update.exe` to `203.0.113.88:8080`, status `200`, UA empty. In one sentence, what occurred?
3. A SIEM query that matches every `http` row is a good “specific HTTP activity” query. True or false?

---

## 3. Summary

An `http` row is method, host+URI, UA, status, and who talked to whom. The process is not on this row. A query names a specific pattern.

**Next:** **1.2.6** SMTP engine.

---

## 4. Related modules

- 1.2.4 – TLS engine (previous)
- 1.2.6 – SMTP engine
- 1.2.7 – Files engine
- 1.1.4 – Host-observed network
