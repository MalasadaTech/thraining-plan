# Module 1.2.1 – Zeek Concepts  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 45–60 minutes  
**Total Suggested Slides:** 16

---

### Slide 1 – Title Slide
**Title:** Module 1.2.1 – Zeek Concepts  
**Subtitle:** SOC Analyst & Threat Hunter Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Welcome students. Introduce yourself and the module. Mention that this is a foundational module before we go deep on individual Zeek logs.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain what Zeek is and how it differs from traditional IDS/IPS
2. Describe the core components of the Zeek architecture
3. Identify the primary Zeek log types and what each captures
4. Explain why Zeek logs are valuable for triage and threat hunting

**Mapped Item:** K: 1.2.1.1 – Zeek concepts

**Speaker Notes:**  
Read through the objectives. Emphasize that we are staying at the conceptual level today — field-level analysis comes in later modules.

---

### Slide 3 – Agenda
**Title:** Agenda

- What is Zeek?
- Zeek vs Traditional IDS/IPS
- Core Architecture
- Primary Log Types
- Why Zeek Matters
- Exercise & Knowledge Check

**Speaker Notes:**  
Quick roadmap so students know where the session is going.

---

### Slide 4 – What is Zeek?
**Title:** What is Zeek?

- Open-source network analysis framework
- Formerly known as Bro
- Passively monitors network traffic
- Generates detailed, structured logs
- Focuses on protocol analysis, not just signatures

**Key Point:** Zeek is primarily a visibility and analysis platform, not just an alerting tool.

**Speaker Notes:**  
Stress the name change (Bro → Zeek) only briefly. Focus on the core identity: high-fidelity network visibility through logs.

---

### Slide 5 – Zeek vs Traditional IDS/IPS
**Title:** Zeek vs Traditional IDS/IPS

| Aspect         | Traditional IDS/IPS       | Zeek                          |
|----------------|---------------------------|-------------------------------|
| Primary Method | Signature / Anomaly       | Protocol Analysis + Scripts   |
| Main Output    | Alerts                    | Rich, structured logs         |
| Focus          | Detect known bad          | Deep visibility + detection   |
| Customization  | Rule writing              | Full scripting language       |
| Best Used For  | Real-time alerting        | Detection + Hunting + IR      |

**Speaker Notes:**  
Walk through the table row by row. Ask the class: “If you already have Suricata or a commercial IDS, why add Zeek?” Let them discuss briefly.

---

### Slide 6 – Core Architecture
**Title:** Zeek Architecture – Simple Mental Model

**Traffic → Event Engine → Scripts → Logs → SIEM**

1. **Event Engine** – Watches traffic and generates events
2. **Policy Scripts** – Decide what to do when events fire
3. **Logging Framework** – Writes structured logs (TSV/JSON)

**Speaker Notes:**  
Draw or animate this flow if possible. Students only need this high-level model. Do not go into the Zeek scripting language.

---

### Slide 7 – Event Engine
**Title:** Event Engine

- Observes network traffic in real time
- Generates events when notable activity occurs
- Examples of events:
  - `connection_established`
  - `http_request`
  - `dns_request`
  - `ssl_established`
  - `file_transferred`

**Speaker Notes:**  
Events are the raw observations. Scripts decide whether (and how) to log them.

---

### Slide 8 – Primary Zeek Log Types (1 of 2)
**Title:** Primary Zeek Log Types

| Log      | What It Records                          |
|----------|------------------------------------------|
| **conn** | Every connection (5-tuple, bytes, state) |
| **dns**  | DNS queries and responses                |
| **http** | HTTP requests and responses              |
| **ssl**  | SSL/TLS handshake information            |

**Speaker Notes:**  
These four are the most frequently used in most SOCs. We will go deep on each in upcoming modules.

---

### Slide 9 – Primary Zeek Log Types (2 of 2)
**Title:** Primary Zeek Log Types (Continued)

| Log       | What It Records                              |
|-----------|----------------------------------------------|
| **files** | Files transferred over the network           |
| **smtp**  | SMTP transaction details                     |
| **weird** | Unusual or malformed protocol behavior       |
| **notice**| Zeek-generated notices / alerts              |
| **x509**  | Certificate details                          |

**Speaker Notes:**  
Highlight that `weird` is often under-used but very valuable for detecting anomalies and evasion.

---

### Slide 10 – Why Zeek Matters
**Title:** Why Zeek Matters for Analysts & Hunters

- **High fidelity** – Sees actual protocol transactions
- **Context-rich** – Method, host, URI, user-agent, certs, etc.
- **Hunting friendly** – Structured and consistent data
- **Complements alerts** – Provides surrounding context for triage
- **Retrospective power** – Data remains available even when no alert fired

**Speaker Notes:**  
Connect each point to real work. Example: “When a Suricata alert fires, the first place many analysts look is the corresponding Zeek http or conn log.”

---

### Slide 11 – Example: conn Log Value
**Title:** Example – Value of the conn Log

A single conn log entry can tell you:

- Who talked to whom (source & destination)
- When the connection started and how long it lasted
- How many bytes went in each direction
- Connection state (normal, rejected, attempt with no reply, etc.)

**Use Cases:** Beaconing, long-lived C2, data staging, unusual port usage

**Speaker Notes:**  
This is just a preview. Full conn log analysis comes in the next module.

---

### Slide 12 – Example: http Log Value
**Title:** Example – Value of the http Log

Typical fields available:

- Method (GET, POST, etc.)
- Host header
- URI
- User-Agent
- Status code
- Request / response body lengths

**Much more useful than a generic “HTTP traffic detected” alert.**

**Speaker Notes:**  
Again, this is a preview. Students will dig into these fields in the HTTP Engine module.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 8–10 minutes

1. List the four Zeek logs you believe are most useful during alert triage.
2. For each log, write one sentence describing a type of suspicious activity it can help investigate.
3. In 2–3 sentences, explain how Zeek differs from a traditional signature-based IDS.

**Speaker Notes:**  
Let students work individually or in pairs. After time is up, ask 2–3 people to share.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. True or False: Zeek is primarily a signature-based IDS.
2. Which component generates events from network traffic?
3. Name three Zeek log types especially useful for threat hunting.
4. Why are Zeek logs often more useful than a simple IDS alert?

**Speaker Notes:**  
Run through answers as a group. Use the Instructor Guide answer key.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Zeek is a network analysis framework that produces rich, structured logs
- Architecture: Event Engine → Scripts → Logs → SIEM
- Most important logs for daily work: conn, dns, http, ssl, files, weird
- Zeek provides high-fidelity visibility that supports both triage and hunting

**Speaker Notes:**  
Reinforce the mental model one final time.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 1.2.2 – Conn Engine
- Module 1.2.3 – DNS Engine
- Module 1.2.5 – HTTP Engine

**Resources:**
- Zeek Documentation: https://docs.zeek.org
- Student Guide for this module

**Speaker Notes:**  
Open the floor. After questions, point students to the Student Guide for review.

---

## Design Notes for Slide Builder

- Keep text minimal — prefer tables and short bullets
- Use a consistent color scheme (recommend dark blue headers)
- Include the module number in the footer of every slide
- For comparison and log tables, make them large and readable
- Consider adding simple icons (network, log file, magnifying glass) if the visual style supports it
- Screenshot placeholders can be added later when showing real log examples in future modules
