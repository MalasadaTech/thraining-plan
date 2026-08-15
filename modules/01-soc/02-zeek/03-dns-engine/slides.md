# Module 1.2.3 – DNS Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.2.3 – DNS Engine  
**Subtitle:** SOC Analyst & Threat Hunter Training  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Introduce the module. Emphasize that DNS is one of the highest-value data sources for both triage and hunting because nearly every connection starts with a DNS lookup.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain the purpose of the Zeek `dns` log
2. Identify and interpret the most important fields
3. Recognize common query types and response codes
4. Analyze a `dns` log entry and accurately describe what occurred
5. Create basic SIEM queries for suspicious DNS activity

**Mapped Items:**  
K: 1.2.3.1 | T: 1.2.3.2 | T: 1.2.3.3

**Speaker Notes:**  
Walk through the objectives. Note that this module builds directly on the Conn Engine knowledge (especially the use of `uid`).

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose of the dns log
- Critical fields
- Query types & response codes
- Analysis examples
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
Quick roadmap.

---

### Slide 4 – Purpose of the dns Log
**Title:** Purpose of the dns Log

- Records DNS queries and responses
- Provides early visibility into domains being contacted
- High value for detecting:
  - Command-and-control (C2)
  - Domain Generation Algorithms (DGAs)
  - DNS tunneling / data exfiltration
  - Phishing and malicious infrastructure
- Often available even when full packet capture is not

**Key Point:** DNS is frequently the first network indicator of compromise.

**Speaker Notes:**  
Ask the class why DNS might be more valuable than connection logs alone when hunting for C2.

---

### Slide 5 – Critical Fields
**Title:** Critical Fields

| Field         | Description                          | Priority |
|---------------|--------------------------------------|----------|
| `query`       | Domain name being looked up          | Highest  |
| `qtype_name`  | Query type (A, TXT, CNAME…)          | High     |
| `rcode_name`  | Response code (NOERROR, NXDOMAIN…)   | High     |
| `answers`     | List of answers returned             | High     |
| `id.orig_h`   | Client IP that issued the query      | High     |
| `uid`         | Links to conn and other logs         | Critical |
| `id.resp_h`   | DNS server IP                        | Medium   |
| `ttls`        | Time-to-live values                  | Medium   |

**Most important for daily work:**  
`query`, `qtype_name`, `rcode_name`, `answers`, `id.orig_h`, `uid`

**Speaker Notes:**  
Spend extra time on `query` and `uid`. Reinforce that `uid` is the pivot key back to the `conn` log.

---

### Slide 6 – Common Query Types
**Title:** Common Query Types (qtype_name)

| Type    | Meaning                     | Notes |
|---------|-----------------------------|-------|
| **A**     | IPv4 address                | Most common |
| **AAAA**  | IPv6 address                | Increasingly common |
| **CNAME** | Canonical name (alias)      | Domain pointing to another |
| **MX**    | Mail exchange               | Email routing |
| **TXT**   | Text record                 | SPF, verification, **sometimes tunneling** |
| **PTR**   | Reverse lookup              | IP → name |
| **NS**    | Name server                 | Delegation |

**Analyst Tip:** High volumes of TXT (or NULL) queries can indicate DNS tunneling.

**Speaker Notes:**  
Highlight TXT as a dual-use record — legitimate and sometimes abused.

---

### Slide 7 – Common Response Codes
**Title:** Common Response Codes (rcode_name)

| Code         | Meaning                | Typical Interpretation |
|--------------|------------------------|------------------------|
| **NOERROR**    | Success                | Domain exists and answered |
| **NXDOMAIN**   | Non-existent domain    | Domain does not exist (DGA, typo, retired) |
| **SERVFAIL**   | Server failure         | Resolver or authoritative problem |
| **REFUSED**    | Query refused          | Policy or access control |

**Hunting Note:**  
A host generating large numbers of NXDOMAIN responses is a classic DGA or scanning indicator.

**Speaker Notes:**  
Emphasize that volume and patterns matter more than any single NXDOMAIN.

---

### Slide 8 – Example 1: Normal Lookup
**Title:** Example 1 – Normal Successful Lookup

```
id.orig_h: 10.10.50.23
query: www.example.com
qtype_name: A
rcode_name: NOERROR
answers: ["93.184.216.34"]
```

**Interpretation:**  
Internal host successfully resolved a legitimate domain to an IPv4 address. Normal behavior.

**Speaker Notes:**  
Ask students to interpret first, then confirm.

---

### Slide 9 – Example 2: NXDOMAIN
**Title:** Example 2 – Non-Existent Domain

```
id.orig_h: 10.10.50.88
query: kjh3g4f9d2s1a0.example-malware.com
qtype_name: A
rcode_name: NXDOMAIN
answers: []
```

**Interpretation:**  
The domain does not exist. Could be a typo, retired domain, or part of a domain-generation algorithm (DGA) used by malware.

**Speaker Notes:**  
Discuss how DGAs produce high rates of NXDOMAIN and why that is a strong signal.

---

### Slide 10 – Example 3: Suspicious TXT Query
**Title:** Example 3 – Suspicious TXT Activity

```
id.orig_h: 10.10.22.17
query: longstringdatahere.tunnel.example.com
qtype_name: TXT
rcode_name: NOERROR
answers: ["v=encodedpayload..."]
```

**Interpretation:**  
TXT records can be abused for DNS tunneling or covert channels. Frequency, length, and context determine whether this is suspicious.

**Speaker Notes:**  
Remind students that legitimate TXT usage exists (SPF, domain verification). Context is required.

---

### Slide 11 – Pivoting with uid
**Title:** Pivoting with the uid Field

**Standard workflow:**
1. Find an interesting DNS query
2. Copy the `uid`
3. Search the `conn` log for the same `uid`
4. Optionally pivot further to `http`, `ssl`, `files`, or `weird` logs

This gives you the full network context around the DNS activity.

**Speaker Notes:**  
This is a critical habit. Demonstrate the concept even with static examples.

---

### Slide 12 – Hunting & Detection Ideas
**Title:** Useful DNS-Based Detections / Hunts

- High volume of NXDOMAIN responses from a single host
- Unusual volume of TXT (or NULL) queries
- Queries to newly registered or rare domains
- DNS queries to known-bad domains or sinkholes
- Long or high-entropy subdomain strings (possible tunneling/DGA)
- Clients using unexpected DNS servers

**Speaker Notes:**  
These are starting points. Students should refine thresholds based on their environment baselines.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. Write a one-sentence summary for each of the three examples.
2. Write a pseudo-query that finds:
   - Hosts with a high number of NXDOMAIN responses
   - Unusual volumes of TXT queries from a single host
3. Explain how you would pivot from a suspicious DNS query to the related network connection.

**Speaker Notes:**  
Let students work. Then review using the Instructor Guide answer key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. What is the primary purpose of the Zeek `dns` log?
2. Which field contains the domain name that was queried?
3. What does `rcode_name = NXDOMAIN` indicate?
4. Name two query types sometimes abused for tunneling.
5. Why is the `uid` field important when analyzing DNS activity?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- The `dns` log provides early, high-value visibility into domains being contacted
- Master the core fields: `query`, `qtype_name`, `rcode_name`, `answers`, `uid`
- NXDOMAIN spikes and unusual query types are strong hunting leads
- Always pivot with `uid` to the `conn` log for full context
- DNS is one of the best sources for detecting C2, DGAs, and tunneling

**Speaker Notes:**  
Reinforce the main points one final time.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 1.2.5 – HTTP Engine
- Module 1.2.4 – TLS Engine

**Resources:**
- Student Guide for this module
- Zeek dns.log documentation

**Speaker Notes:**  
Open the floor for questions.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** DNS Quick Reference

**Highest-value fields:**  
`query` · `qtype_name` · `rcode_name` · `answers` · `uid` · `id.orig_h`

**Key states/codes:**  
NOERROR · NXDOMAIN · TXT · A / AAAA

**Core habit:**  
Interesting DNS query → copy `uid` → pivot to `conn` (and beyond)

**Speaker Notes:**  
This slide can be left up as a reference or printed as a handout.

---

## Design Notes for Slide Builder

- Keep tables clean and large enough to read
- Use monospace formatting for log examples
- Visually highlight `query`, `rcode_name`, and `uid`
- Consistent footer with module number
- Minimal text — let examples and tables teach
