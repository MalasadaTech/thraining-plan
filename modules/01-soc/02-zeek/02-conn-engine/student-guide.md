# Module 1.2.2 – Conn Engine

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.2.1 A / B / C ; 1.2.2.2 2b / 3c / 4c ; 1.2.2.3 2b / 3c / 4c  
- Hunter: 1.2.2.1 B / C / C ; 1.2.2.2 3c / 4c / 4c ; 1.2.2.3 3c / 4c / 4c  
- CTI: 1.2.2.1 A / A / B ; 1.2.2.2 1a / 1a / 2b ; 1.2.2.3 1a / 1a / 2b  
**Estimated Time:** 25–30 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a Zeek `conn` row: who talked to whom, on which ports, and how the connection ended.
2. Describe what a `conn` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`conn`** log to see a connection on the **wire**. **1.2.1** was the map. This hour is the first engine. It does **not** name the initiating process. That was **1.1.4**.

**`conn`** is one row per connection Zeek saw.

| Field | What it is |
|-------|------------|
| **`id.orig_h`** | Originator IP — who started the talk from Zeek’s view |
| **`id.orig_p`** | Originator port |
| **`id.resp_h`** | Responder IP — who was contacted |
| **`id.resp_p`** | Responder port |
| **`conn_state` / `history`** | How it ended, and a short flag string of what was seen (`S` SYN, `H` SYN-ACK, `F` FIN, `R` RST) |

**States you will use:** **`SF`** = established and torn down cleanly. **`S0`** = attempt, no reply. **`REJ`** = attempt refused. If you see another state, say what the field shows. Do not invent a story the flags do not support.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open DNS or TLS fields yet.

**What good looks like:**

- Describe: one sentence — orig IP/port → resp IP/port, state. Do not name a process. Do not call it C2 from port 443 alone.
- Given: `id.orig_h` a workstation, `id.resp_h` `203.0.113.88`, `id.resp_p` `443`, `conn_state` `SF`. **What occurred:** that host completed a TCP connection to `203.0.113.88:443`. Who launched the socket is on the **host** row (**1.1.4**).
- Query: names a **specific** pattern (resp IP or port + state), not “all `conn` rows.”

---

## 2. Knowledge Check

1. `id.orig_h` is the destination IP. True or false?
2. Workstation → `203.0.113.88:443`, `conn_state` `SF`. In one sentence, what occurred?
3. A SIEM query that matches every `conn` row is a good “specific connection activity” query. True or false?

---

## 3. Summary

A `conn` row is who talked to whom, on which ports, and how it ended. State and history are on the wire. The process is not. A query names a specific pattern.

**Next:** **1.2.3** DNS engine.

---

## 4. Related modules

- 1.2.1 – Zeek concepts (previous)
- 1.2.3 – DNS engine
- 1.1.4 – Host-observed network
