# Module 1.2.1 – Zeek Concepts

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3-level (A) → 5-level (B) → 7-level (C)  
- Hunter: Starts at B and moves to C  
**Estimated Time:** 45–60 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain what Zeek is and how it differs from traditional signature-based IDS/IPS.
2. Describe the core components of the Zeek architecture (events, scripts, logs).
3. Identify the primary Zeek log types and the kind of activity each captures.
4. Explain why Zeek logs are highly valuable for both alert triage and threat hunting.

**Mapped Proficiency Items:**
- K: 1.2.1.1 – Zeek concepts (SOC Target: A/B/C | Hunter Target: B/C/C)

---

## 1. Key Concepts

### 1.1 What is Zeek?

Zeek (formerly known as Bro) is an open-source network analysis framework. It is **not** primarily a signature-based intrusion detection system. Instead, Zeek passively monitors network traffic and generates detailed, high-fidelity logs about the protocols and activities it observes.

**Key distinctions from traditional IDS/IPS:**

| Aspect              | Traditional IDS/IPS          | Zeek                          |
|---------------------|------------------------------|-------------------------------|
| Primary method      | Signature / anomaly matching | Protocol analysis + scripting |
| Output              | Alerts                       | Rich, structured logs         |
| Focus               | Detection of known bad       | Deep visibility + detection   |
| Customization       | Limited rule writing         | Full scripting language       |
| Typical use         | Real-time alerting           | Detection + Hunting + IR      |

Zeek sits on the network (usually via a TAP or SPAN port), decodes protocols, and produces logs that are then shipped to a SIEM or data lake.

### 1.2 Core Architecture

Zeek has three major conceptual layers:

1. **Event Engine**  
   - Watches network traffic and generates events when something interesting happens  
   - Examples: `connection_established`, `http_request`, `dns_request`, `ssl_established`

2. **Policy Script Interpreter**  
   - Runs Zeek scripts (written in the Zeek scripting language)  
   - Scripts decide what to do when events fire (log it, raise a notice, extract files, etc.)

3. **Logging Framework**  
   - Outputs structured logs (normally TSV or JSON)  
   - These logs are what analysts actually query in the SIEM

**Simple mental model:**  
Traffic → Events → Scripts decide what to log → Logs land in SIEM → Analysts query them

### 1.3 Primary Zeek Log Types

Here are the most commonly used Zeek logs in a SOC / hunting environment:

| Log Name     | What it records                                      | Typical Use Cases                     |
|--------------|------------------------------------------------------|---------------------------------------|
| **conn**     | Every connection (5-tuple + duration, bytes, state)  | Baseline traffic, beacons, C2         |
| **dns**      | DNS queries and responses                            | Malicious domains, tunneling, C2      |
| **http**     | HTTP requests/responses                              | Web shells, malware download, exfil   |
| **ssl / tls**| SSL/TLS handshake information                        | Certificate analysis, JA3, malicious HTTPS |
| **files**    | Files transferred over the network                   | Malware delivery, data exfil          |
| **smtp**     | SMTP transaction details                             | Phishing, malicious attachments       |
| **weird**    | Unusual or malformed protocol behavior               | Protocol anomalies, evasion attempts  |
| **notice**   | Zeek-generated notices / alerts                      | Built-in detections                   |
| **x509**     | Certificate details                                  | Cert analysis, validity, issuer       |

You do **not** need to memorize every field yet. In later modules we will go deep on the most important logs (especially `conn`, `dns`, `http`, and `ssl`).

### 1.4 Why Zeek Matters for Analysts and Hunters

- **High fidelity**: Zeek sees the actual protocol transactions, not just packet headers.
- **Context-rich**: A single HTTP log entry can contain method, host, URI, user-agent, status code, and more.
- **Hunting friendly**: Because the data is structured and consistent, it is excellent for hypothesis-driven and anomaly-based hunts.
- **Complementary to alerts**: When an IDS/SIEM alert fires, Zeek logs often provide the surrounding context that makes triage much faster.
- **Long-term visibility**: Even if no alert fired, the Zeek logs remain available for retrospective investigation.

---

## 2. Detailed Walkthrough / Examples

### Example 1: Simple Connection Visibility (conn log)

A basic `conn` log entry tells you:
- Who talked to whom (source & destination IP + port)
- When the connection started and how long it lasted
- How many bytes went in each direction
- Connection state (e.g., `SF` = normal teardown, `REJ` = rejected, `S0` = attempt with no reply)

This single log type already supports many hunting use cases (long-duration connections, high byte counts, connections to rare ports, etc.).

### Example 2: HTTP Transaction

A Zeek `http` log entry typically includes:
- Timestamp
- Source & destination
- Method (`GET`, `POST`, etc.)
- Host header
- URI
- User-Agent
- Status code
- Request and response body lengths

This is significantly more useful for triage than a generic “HTTP traffic detected” alert.

---

## 3. Hands-On Exercise

**Objective:** Demonstrate basic understanding of Zeek’s purpose and log types.

**Instructions:**

1. From memory or notes, list the four Zeek logs you believe will be most useful during alert triage.  
2. For each of those four logs, write one sentence describing what kind of malicious or suspicious activity it can help you investigate.  
3. Explain in 2–3 sentences how Zeek differs from a traditional signature-based IDS.

**Expected Outcome:**
- Four relevant logs correctly identified
- Reasonable use-case descriptions
- Clear distinction between Zeek and traditional IDS

---

## 4. Knowledge Check

1. True or False: Zeek is primarily a signature-based intrusion detection system.
2. Which Zeek component is responsible for generating events from network traffic?
3. Name three Zeek log types that are especially valuable for threat hunting.
4. Why are Zeek logs often more useful for investigation than a simple IDS alert?

---

## 5. Summary

- Zeek is a network analysis framework that produces rich, structured logs rather than just alerts.
- Its architecture consists of an event engine, a scripting layer, and a logging framework.
- The most commonly used logs include `conn`, `dns`, `http`, `ssl/tls`, `files`, and `weird`.
- Zeek provides high-fidelity visibility that supports both alert triage and proactive threat hunting.

---

## 6. References & Further Reading

- Official Zeek Documentation: https://docs.zeek.org
- Zeek Log Types Overview: https://docs.zeek.org/en/current/script-reference/log-files.html
- Related upcoming modules:
  - 1.2.2 – Conn Engine
  - 1.2.3 – DNS Engine
  - 1.2.5 – HTTP Engine
  - 1.2.4 – TLS Engine
