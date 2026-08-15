# Instructor Guide – Module 1.2.3 – DNS Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:** SOC A/2b → B/3c → C/4c | Hunter B/3c → C/4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach students how to read, interpret, and hunt with the Zeek `dns` log. DNS is one of the highest-value data sources for both triage and proactive detection.

**Key Teaching Points:**
- DNS is often the first network activity associated with malware and C2.
- Focus on `query`, `qtype_name`, `rcode_name`, and `answers`.
- NXDOMAIN spikes and unusual query types are classic leads.
- Always reinforce the `uid` pivot back to the `conn` log.

**Common Student Challenges:**
- Treating every NXDOMAIN as malicious (context and volume matter).
- Not knowing which query types are commonly abused (TXT, NULL, etc.).
- Forgetting to pivot with `uid` to see the full connection.

**Required Materials:**
- Student Guide
- Sample DNS log entries (examples in the guide are sufficient for classroom use)
- Optional: Live SIEM access for query practice

---

## Learning Objectives

1. Explain the purpose of the Zeek `dns` log.
2. Identify and interpret the most important fields.
3. Recognize common query types and response codes.
4. Analyze a `dns` log entry and accurately describe what occurred.
5. Create basic SIEM queries for suspicious DNS activity.

**Mapped Items:**
- K: 1.2.3.1 – DNS engine
- T: 1.2.3.2 – Analyze a Zeek DNS log
- T: 1.2.3.3 – Create a SIEM query for DNS activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | |
| Purpose of the dns log         | 6 min    | |
| Key Fields                     | 12 min   | Focus on query, qtype, rcode, answers |
| Query Types & Response Codes   | 12 min   | |
| Walkthrough Examples           | 12 min   | Interactive |
| Hands-On Exercise              | 15 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 3 min    | |
| **Total**                      | **~72 min** | |

---

## Detailed Teaching Notes

### 1. Purpose of the dns Log

**Talking Points:**
- Nearly every connection starts with a DNS query.
- Excellent source for detecting:
  - Malicious domains / C2
  - DGAs
  - DNS tunneling
  - Phishing infrastructure
- Often available even when full packet capture is not.

**Question to ask:**  
“Why might DNS be more valuable than the connection log alone when hunting for C2?”

### 2. Key Fields

**Teaching approach:**
- Project a sample DNS log entry.
- Spend the majority of time on:
  - `query` (the domain)
  - `qtype_name`
  - `rcode_name`
  - `answers`
  - `id.orig_h` and `uid`

**Important reminder:**  
The `uid` links this DNS activity to the corresponding `conn` record (and any related http/ssl/files logs).

### 3. Query Types & Response Codes

**Focus list:**
- Query types: A, AAAA, CNAME, TXT, MX, PTR
- Response codes: NOERROR, NXDOMAIN, SERVFAIL

**Teaching tip:**  
Emphasize that a single NXDOMAIN is rarely interesting. Patterns and volume are what matter.

### 4. Examples

Work through all three examples interactively. Ask students to interpret before revealing the explanation.

**Extra point for Example 2 (NXDOMAIN):**  
Discuss how DGAs produce high rates of NXDOMAIN responses and why that is a strong hunting signal.

**Extra point for Example 3 (TXT):**  
Note that legitimate use of TXT records exists (SPF, domain verification), so context and frequency are required before calling something suspicious.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 12–15 minutes.
- Allow use of the Student Guide.
- Review answers as a group afterward.

**What good answers look like:**

**Summaries:**
- Example 1: Normal successful A record lookup.
- Example 2: Query for a non-existent domain (possible DGA or typo).
- Example 3: TXT query that could be associated with tunneling or covert channel activity.

**Queries (pseudo examples):**
```
rcode_name = "NXDOMAIN" | stats count by id.orig_h | where count > threshold
```
```
qtype_name = "TXT" | stats count by id.orig_h | sort by count desc
```

**uid pivot explanation:**  
Copy the `uid` from the DNS log entry and search the `conn` log (and other protocol logs) for the same `uid` to see the full network connection context.

---

## Knowledge Check – Answer Key

1. **What is the primary purpose of the Zeek `dns` log?**  
   **Answer:** To record DNS queries and responses, providing visibility into domains being contacted and enabling detection of malicious infrastructure, DGAs, and tunneling.

2. **Which field contains the domain name that was queried?**  
   **Answer:** `query`

3. **What does the response code `NXDOMAIN` indicate?**  
   **Answer:** The queried domain does not exist.

4. **Name two query types that are sometimes abused for data tunneling.**  
   **Answer:** TXT and NULL (also occasionally CNAME or others). TXT is the most commonly discussed.

5. **Why is the `uid` field important when analyzing DNS activity?**  
   **Answer:** It links the DNS query to the corresponding connection in the `conn` log and to other related protocol logs, allowing full context to be built.

---

## Additional Instructor Resources

- Zeek dns.log documentation
- Internal lists of known-good DNS servers and high-volume legitimate TXT usage (if available)
- Next recommended modules: 1.2.5 HTTP Engine or 1.2.4 TLS Engine
