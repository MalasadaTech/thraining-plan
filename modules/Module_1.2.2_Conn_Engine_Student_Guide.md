# Module 1.2.2 – Conn Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3-level (A/2b) → 5-level (B/3c) → 7-level (C/4c)  
- Hunter: Starts higher (B/3c → C/4c)  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Zeek `conn` log and why it is foundational.
2. Identify and interpret the most important fields in a `conn` log entry.
3. Recognize common connection states and what they indicate.
4. Analyze a `conn` log entry and accurately describe what occurred.
5. Create basic SIEM queries to find interesting connection activity.

**Mapped Proficiency Items:**
- K: 1.2.2.1 – Conn engine
- T: 1.2.2.2 – Analyze a Zeek conn log and accurately describe what occurred
- T: 1.2.2.3 – Create a SIEM query to detect specific connection activity

---

## 1. Key Concepts

### 1.1 Purpose of the conn Log

The `conn` log is the foundation of Zeek network visibility. It records **every** connection Zeek observes, regardless of protocol.

One `conn` entry is created per connection and contains:
- Who talked to whom
- When the connection started and how long it lasted
- How much data was transferred
- How the connection ended (or failed to establish)

Almost every network investigation starts with or references the `conn` log.

### 1.2 Key Fields

Here are the fields you must know well:

| Field            | Description                                      | Why It Matters |
|------------------|--------------------------------------------------|----------------|
| `ts`             | Timestamp of connection start                    | When it happened |
| `uid`            | Unique connection identifier                     | Links to other Zeek logs |
| `id.orig_h`      | Originator (source) IP                           | Who initiated |
| `id.orig_p`      | Originator port                                  | Source port |
| `id.resp_h`      | Responder (destination) IP                       | Who was contacted |
| `id.resp_p`      | Responder port                                   | Destination port |
| `proto`          | Protocol (tcp, udp, icmp)                        | Transport protocol |
| `service`        | Detected application protocol (http, dns, ssl…)  | What Zeek thinks it is |
| `duration`       | Length of the connection in seconds              | Long connections = interesting |
| `orig_bytes`     | Bytes sent by originator                         | Data leaving the source |
| `resp_bytes`     | Bytes sent by responder                          | Data received by source |
| `conn_state`     | Final state of the connection                    | How it ended |
| `history`        | Connection history flags                         | Detailed handshake/behavior |
| `orig_pkts`      | Packets sent by originator                       | Volume indicator |
| `resp_pkts`      | Packets sent by responder                        | Volume indicator |
| `missed_bytes`   | Bytes missed by Zeek (packet loss)               | Data quality indicator |

**Most critical fields for daily work:**  
`id.orig_h`, `id.resp_h`, `id.resp_p`, `proto`, `duration`, `orig_bytes`, `resp_bytes`, `conn_state`, `uid`

### 1.3 Understanding conn_state

The `conn_state` field tells you how the connection ended. Memorize these common values:

| State  | Meaning                                      | Typical Interpretation |
|--------|----------------------------------------------|------------------------|
| **SF**   | Normal establishment and termination         | Clean, successful connection |
| **S0**   | Connection attempt seen, no reply            | Host down, filtered, or stealth scan |
| **S1**   | Connection established, not terminated       | Still open or incomplete teardown |
| **REJ**  | Connection attempt rejected                  | Port closed or actively refused |
| **RSTO** | Originator sent RST                          | Client reset the connection |
| **RSTR** | Responder sent RST                           | Server reset the connection |
| **RSTOS0** | Originator sent RST after SYN-ACK missing  | Possible scan or evasion |
| **RSTRH** | Responder sent RST after partial handshake | Unusual server behavior |
| **SH**   | Originator sent SYN + FIN (no SYN-ACK)       | Unusual / possible scan |
| **SHR**  | Responder sent SYN-ACK + FIN (no SYN)        | Unusual |
| **OTH**  | No SYN seen, midstream traffic               | Partial connection or asymmetric routing |

**Analyst tip:**  
- Large numbers of `S0` or `REJ` from one source can indicate scanning.  
- Long `duration` + steady byte counts can indicate beaconing or C2.

### 1.4 The `history` Field (Advanced Awareness)

The `history` field is a string of flags that records the sequence of observed packets. Common flags include:

- `S` – SYN
- `H` – SYN-ACK
- `A` – ACK
- `D` – Data payload
- `F` – FIN
- `R` – RST
- `I` – Inconsistent packet
- `^` – Direction flip (responder started the activity)

You do not need to master `history` at the 3-level, but 5- and 7-level analysts should become comfortable reading it.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Normal Web Connection (SF)

```
ts: 2026-08-14T18:05:12.123456Z
uid: CAbCdEfGhIjKlMnOp
id.orig_h: 10.10.50.23
id.orig_p: 49152
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
Internal host 10.10.50.23 made a normal HTTPS connection to 93.184.216.34. The connection completed cleanly (`SF`). Client sent a small amount of data; server sent significantly more (typical for web browsing).

### Example 2: Possible Scan or Failed Connection (S0)

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
Host 10.10.50.88 sent a SYN to port 445 on an external IP and received no response. This could be a blocked connection, a down host, or part of a scan.

### Example 3: Long Duration Connection (Potential Beacon)

```
id.orig_h: 10.10.22.17
id.resp_h: 198.51.100.66
id.resp_p: 443
proto: tcp
duration: 86418.5
orig_bytes: 12480
resp_bytes: 9870
conn_state: S1
```

**Interpretation:**  
A connection lasting more than 24 hours with relatively low but steady byte counts. Worth investigating as possible C2 beaconing.

---

## 3. Hands-On Exercise

**Objective:** Practice analyzing `conn` log entries and writing simple detection logic.

**Instructions:**

1. Review the three example connections above.
2. For each example, write a one-sentence summary of what occurred.
3. Write a SIEM-style query (pseudo-query is fine) that would find:
   - Connections with duration > 1 hour
   - Connections in state `S0` or `REJ` from internal hosts to external IPs on ports 445, 3389, or 22
4. Explain why the `uid` field is important.

**Expected Outcome:**
- Accurate short summaries of the three examples
- Two functional pseudo-queries
- Correct explanation of `uid` (it links the conn record to other Zeek logs such as http, dns, ssl, files)

---

## 4. Knowledge Check

1. What is the primary purpose of the Zeek `conn` log?
2. Which field uniquely identifies a connection and links it to other Zeek logs?
3. What does the connection state `SF` indicate?
4. What does the connection state `S0` usually indicate?
5. Name three fields you would examine when looking for possible C2 beaconing.

---

## 5. Summary

- The `conn` log records every connection and is the foundation of Zeek visibility.
- Critical fields: source/destination IPs and ports, protocol, duration, byte counts, conn_state, and uid.
- Connection states (`SF`, `S0`, `REJ`, `RSTO`, etc.) reveal how the connection ended.
- Long duration, unusual states, and asymmetric byte counts are common hunting leads.
- Always use the `uid` to pivot to related http, dns, ssl, or files logs.

---

## 6. References & Further Reading

- Zeek conn.log documentation: https://docs.zeek.org/en/current/scripts/base/protocols/conn/main.zeek.html
- Connection state reference (Zeek docs)
- Related modules:
  - 1.2.1 – Zeek Concepts
  - 1.2.3 – DNS Engine
  - 1.2.5 – HTTP Engine
  - 1.2.4 – TLS Engine
