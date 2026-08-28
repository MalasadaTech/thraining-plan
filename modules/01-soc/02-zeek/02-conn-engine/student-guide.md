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

1. Read a Zeek `conn` event: originator and responder IP and port, and how the connection ended.
2. Describe what a `conn` log shows, and say what a **specific** SIEM query looks like.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

---

## 1. Key Concepts

SOC analysts read the Zeek **`conn`** log to see who talked to whom on the **wire**, and how the connection ended. That is daily alert work: an alert names an IP or a connection, and you have to say which address started the talk, which address was contacted, on which ports, and whether the attempt completed, sat unanswered, or was refused. **1.2.1** taught that Zeek engines extract protocol data from the wire. This lesson is the **`conn`** extract. It does **not** name the initiating process. That is host-network telemetry (**1.1.4**).

The **`conn`** log is one **event** per connection Zeek saw. In a SIEM, that event usually shows up as a **row** in a table. Later lessons may still say “row.” Here it means the same thing as the log.

| Idea | What to read |
|------|----------------|
| **Source IP** | `id.orig_h` — **originator** IP. Who started the talk from Zeek’s view. Not automatically an internal host. |
| **Source port** | `id.orig_p` — originator port |
| **Destination IP** | `id.resp_h` — **responder** IP. Who was contacted. |
| **Destination port** | `id.resp_p` — responder port |
| **Connection state / history** | `conn_state` / `history`. How it ended, and a short flag string of what was seen (`S` SYN, `H` SYN-ACK, `F` FIN, `R` RST) |

**States you will use:** **`SF`** = established and torn down cleanly. **`S0`** = attempt, no reply. **`REJ`** = attempt refused. If you see another state, say what the field shows. Do not invent a story the flags do not support.

`id.orig_h` is the originator, not the destination. Originator is not a synonym for “our network.” Zeek labels the side that started the talk, wherever that address lives.

This is the **extract**. PCAP still verifies or expands (**1.2.1**). Do not open DNS or TLS fields yet.

**What good looks like:**

- Describe: one sentence — originator IP/port → responder IP/port, state. Do not name a process. Do not call it C2 from port 443 alone.
- Given: `id.orig_h` a workstation, `id.resp_h` `203.0.113.88`, `id.resp_p` `443`, `conn_state` `SF`. **What occurred:** that host completed a TCP connection to `203.0.113.88:443`. Who launched the socket is on the **host** (**1.1.4**).
- Query: names a **specific** pattern (responder IP or port + state), not every connection.

DNS fields are the next Zeek lesson (**1.2.3**).

---

## 2. Knowledge Check

1. `id.orig_h` is the destination IP. True or false?
2. Workstation → `203.0.113.88:443`, `conn_state` `SF`. In one sentence, what occurred?
3. A SIEM query that matches every connection is a good “specific connection activity” query. True or false?

---

## 3. Summary

A `conn` event is who talked to whom, on which ports, and how it ended. State and history are on the wire. The process is not. A query names a specific pattern.

**Next:** **1.2.3** DNS engine.

---

## 4. Related modules

- 1.2.1 – Zeek concepts
- 1.2.3 – DNS engine
- 1.1.4 – Host-observed network
