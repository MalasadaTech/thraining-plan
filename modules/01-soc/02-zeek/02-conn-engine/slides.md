# Module 1.2.2 – Conn Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 18

---

### Slide 1 – Title Slide
**Title:** Module 1.2.2 – Conn Engine  
**Subtitle:** SOC Analyst & Threat Hunter Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Introduce the module. Emphasize that the `conn` log is the foundation of Zeek network visibility and that almost every network investigation starts here.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Zeek `conn` log
2. Identify and interpret the most important fields
3. Recognize common connection states and what they mean
4. Analyze a `conn` log entry and accurately describe what occurred
5. Create basic SIEM queries for interesting connection activity

**Mapped Items:**  
K: 1.2.2.1 | T: 1.2.2.2 | T: 1.2.2.3

**Speaker Notes:**  
Walk through the objectives. Tell students this module is more practical than the previous conceptual one.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose of the conn log
- Critical fields
- Connection states (`conn_state`)
- Analysis examples
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
Quick roadmap.

---

### Slide 4 – Purpose of the conn Log
**Title:** Purpose of the conn Log

- Records **every** connection Zeek observes
- Protocol-agnostic (TCP, UDP, ICMP)
- Answers the basic questions:
  - Who talked to whom?
  - When and for how long?
  - How much data was transferred?
  - How did the connection end?
- Serves as the index that links other Zeek logs together via `uid`

**Key Point:** If you could only keep one Zeek log, most analysts would choose `conn`.

**Speaker Notes:**  
Ask the class why this log is so foundational. Reinforce that other logs (http, dns, ssl) reference the same `uid`.

---

### Slide 5 – Critical Fields (1 of 2)
**Title:** Critical Fields – Identity & Timing

| Field       | Description                     |
|-------------|---------------------------------|
| `ts`        | Timestamp of connection start   |
| `uid`       | Unique connection ID (pivot key)|
| `id.orig_h` | Originator (source) IP          |
| `id.orig_p` | Originator port                 |
| `id.resp_h` | Responder (destination) IP      |
| `id.resp_p` | Responder port                  |
| `proto`     | Protocol (tcp / udp / icmp)     |
| `service`   | Detected application protocol   |

**Speaker Notes:**  
Emphasize originator = the side that started the connection. Spend time on `uid` — it is how you pivot to http, dns, ssl, files, etc.

---

### Slide 6 – Critical Fields (2 of 2)
**Title:** Critical Fields – Volume & Outcome

| Field         | Description                          |
|---------------|--------------------------------------|
| `duration`    | Length of connection (seconds)       |
| `orig_bytes`  | Bytes sent by originator             |
| `resp_bytes`  | Bytes sent by responder              |
| `conn_state`  | Final state of the connection        |
| `history`     | Detailed connection history flags    |
| `orig_pkts`   | Packets sent by originator           |
| `resp_pkts`   | Packets sent by responder            |
| `missed_bytes`| Bytes missed by Zeek (packet loss)   |

**Most important for daily work:**  
`duration`, `orig_bytes`, `resp_bytes`, `conn_state`, `uid`

**Speaker Notes:**  
Highlight that long duration + low-and-steady bytes is a classic beaconing indicator.

---

### Slide 7 – Connection States Overview
**Title:** Understanding conn_state

The `conn_state` field tells you **how the connection ended**.

Focus on these high-value states first:

| State  | Meaning                              |
|--------|--------------------------------------|
| **SF**   | Normal establishment & termination   |
| **S0**   | Attempt seen, no reply               |
| **REJ**  | Connection attempt rejected          |
| **RSTO** | Originator sent RST                  |
| **RSTR** | Responder sent RST                   |
| **S1**   | Established, not terminated          |
| **OTH**  | No SYN seen (midstream / partial)    |

**Speaker Notes:**  
Tell students they do not need to memorize every possible state today. Master these seven first.

---

### Slide 8 – State Details (SF, S0, REJ)
**Title:** High-Value States – SF, S0, REJ

- **SF** → Clean, successful connection  
  (Normal web browsing, normal application traffic)

- **S0** → SYN sent, no response  
  (Host down, filtered, or part of a scan)

- **REJ** → Connection actively refused  
  (Port closed or service not listening)

**Analyst Tip:**  
Large numbers of `S0` or `REJ` from one internal host → possible scanning.

**Speaker Notes:**  
Give real-world examples for each.

---

### Slide 9 – State Details (Resets & Long-Lived)
**Title:** High-Value States – Resets & Long-Lived

- **RSTO / RSTR** → Connection reset by one side  
  (Can be normal or suspicious depending on context)

- **S1** → Connection established but never cleanly finished  
  (Often seen with long-lived or aborted sessions)

- **OTH** → Midstream traffic, no initial SYN observed  
  (Asymmetric routing or partial capture)

**Speaker Notes:**  
Long-duration `S1` connections deserve extra scrutiny.

---

### Slide 10 – Example 1: Normal HTTPS
**Title:** Example 1 – Normal Web Connection

```
id.orig_h: 10.10.50.23
id.resp_h: 93.184.216.34
id.resp_p: 443
proto: tcp
service: ssl
duration: 4.821
orig_bytes: 892
resp_bytes: 14567
conn_state: SF
```

**Interpretation:**  
Internal host made a normal HTTPS connection. Clean teardown (`SF`). Server sent significantly more data than the client (typical for web browsing).

**Speaker Notes:**  
Ask the class to interpret before revealing the explanation.

---

### Slide 11 – Example 2: Failed Connection
**Title:** Example 2 – Possible Scan / Failed Attempt

```
id.orig_h: 10.10.50.88
id.resp_h: 203.0.113.45
id.resp_p: 445
proto: tcp
conn_state: S0
duration: 0.000
orig_bytes: 0
resp_bytes: 0
```

**Interpretation:**  
Host sent a SYN to port 445 and received no reply. Could be blocked, host down, or part of a scan.

**Speaker Notes:**  
Discuss how volume of similar events changes the interpretation.

---

### Slide 12 – Example 3: Long-Duration Connection
**Title:** Example 3 – Potential Beaconing

```
id.orig_h: 10.10.22.17
id.resp_h: 198.51.100.66
id.resp_p: 443
duration: 86418.5
orig_bytes: 12480
resp_bytes: 9870
conn_state: S1
```

**Interpretation:**  
Connection lasting > 24 hours with relatively low, steady byte counts. Classic hunting lead for possible C2.

**Next Step:** Pivot on the `uid` to ssl / http / files logs.

**Speaker Notes:**  
This is a high-value teaching example. Ask what other logs they would check.

---

### Slide 13 – Using the uid
**Title:** The Power of the uid Field

- Every Zeek protocol log for the same connection shares the same `uid`
- Workflow:
  1. Find interesting `conn` record
  2. Copy the `uid`
  3. Search other logs (`http`, `dns`, `ssl`, `files`, `weird`) for that `uid`
- This is the primary way to build full connection context

**Speaker Notes:**  
Demonstrate the pivot concept even if you only have static examples today.

---

### Slide 14 – Hunting & Detection Ideas
**Title:** Useful conn-Based Detections / Hunts

- Duration > 1 hour (or > 24 hours)
- High number of `S0` / `REJ` from a single host
- Connections to rare external ports
- Large `orig_bytes` to external IPs (possible exfil)
- Long-lived connections with low-and-steady byte counts
- Internal hosts connecting to known-bad infrastructure

**Speaker Notes:**  
These are starting points. Students will refine them as they gain experience.

---

### Slide 15 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. Write a one-sentence summary for each of the three examples.
2. Write a pseudo-query that finds:
   - Connections with duration > 1 hour
   - `S0` or `REJ` connections from internal hosts to ports 445, 3389, or 22
3. Explain why the `uid` field is important.

**Speaker Notes:**  
Let students work. Then review answers as a group using the Instructor Guide.

---

### Slide 16 – Knowledge Check
**Title:** Knowledge Check

1. What is the primary purpose of the Zeek `conn` log?
2. Which field links a connection to other Zeek logs?
3. What does `conn_state = SF` indicate?
4. What does `conn_state = S0` usually indicate?
5. Name three fields useful when hunting for possible C2 beaconing.

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 17 – Summary
**Title:** Key Takeaways

- The `conn` log is the foundation of Zeek network visibility
- Master the core fields: IPs, ports, duration, bytes, `conn_state`, `uid`
- Connection states reveal how a connection ended
- Long duration + steady low volume = classic beaconing lead
- Always pivot with `uid` to build full context

**Speaker Notes:**  
Reinforce the mental model one more time.

---

### Slide 18 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 1.2.3 – DNS Engine
- Module 1.2.5 – HTTP Engine
- Module 1.2.4 – TLS Engine

**Resources:**
- Student Guide for this module
- Zeek conn.log documentation

**Speaker Notes:**  
Open the floor for questions.

---

## Design Notes for Slide Builder

- Keep tables large and readable
- Use monospace or clear formatting for log examples
- Highlight `uid`, `duration`, and `conn_state` visually when possible
- Consistent footer with module number
- Minimal text — let the examples and tables do the teaching
