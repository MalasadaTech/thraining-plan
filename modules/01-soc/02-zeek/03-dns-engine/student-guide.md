# Module 1.2.3 – DNS Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.3.1 A / B / C ; 1.2.3.2 2b / 3c / 4c ; 1.2.3.3 2b / 3c / 4c  
- Hunter: 1.2.3.1 B / C / C ; 1.2.3.2 3c / 4c / 4c ; 1.2.3.3 3c / 4c / 4c  
- CTI: 1.2.3.1 A / B / B ; 1.2.3.2 1a / 2b / 3c ; 1.2.3.3 1a / 2b / 3c  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `dns` row: question, answer, record type, and who asked whom.
2. Describe what a `dns` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log and accurately describe what occurred
- T: 1.2.3.3 – Create a SIEM query to detect specific DNS activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`dns`** log to see a name lookup on the **wire**. **1.2.2** was the `conn` row. This hour is the DNS extract. It does **not** name the initiating process. That was **1.1.4**.

**`dns`** is one row for a query (and the response Zeek saw).

| Idea | What to read |
|------|----------------|
| **Query (question)** | `query` — the name that was asked |
| **Response (answer)** | `answers` — what came back (an IP, another name, or empty) |
| **Record type** | `qtype_name` — **A**, **AAAA**, **MX**, **CNAME**, **NS**, **TXT**, and the rest when you see them |
| **Source / dest** | `id.orig_h` = who asked. `id.resp_h` = which resolver answered |

A **CNAME** answer is another name, not an address. An empty `answers` list means Zeek did not get a record — say that. Do not invent NXDOMAIN hunting or DGA methodology here.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open TLS or HTTP fields yet.

**What good looks like:**

- Describe: one sentence — who asked, for which name, which type, what answered. Do not name a process. Do not call it C2 from a single A record.
- Given: `id.orig_h` a workstation, `query` a hostname, `qtype_name` `A`, `answers` `["203.0.113.88"]`. **What occurred:** that host asked for that name and got **A** `203.0.113.88`. The `conn` to `:443` is a different row (**1.2.2**). Who launched the lookup is on the **host** (**1.1.4**).
- Query: names a **specific** pattern (`query`, `qtype_name`, or `answers`), not “all `dns` rows.”

---

## 2. Knowledge Check

1. `id.resp_h` on a `dns` row is the IP the name resolved to. True or false?
2. Workstation queries a hostname, type `A`, answers `["203.0.113.88"]`. In one sentence, what occurred?
3. A SIEM query that matches every `dns` row is a good “specific DNS activity” query. True or false?

---

## 3. Summary

A `dns` row is the question, the type, the answer, and who asked which resolver. The process is not on this row. A query names a specific pattern.

**Next:** **1.2.4** TLS engine.

---

## 4. Related modules

- 1.2.2 – Conn engine (previous)
- 1.2.4 – TLS engine
- 1.1.4 – Host-observed network
