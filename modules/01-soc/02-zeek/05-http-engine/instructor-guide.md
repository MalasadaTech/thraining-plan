# Instructor Guide – Module 1.2.5 – HTTP Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.5.1 A / B / C · 1.2.5.2 2b / 3c / 4c · 1.2.5.3 2b / 3c / 4c  
- Hunter: 1.2.5.1 B / C / C · 1.2.5.2 3c / 4c / 4c · 1.2.5.3 3c / 4c / 4c  
- CTI: 1.2.5.1 A / B / B · 1.2.5.2 1a / 2b / 3c · 1.2.5.3 1a / 2b / 3c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read the Zeek `http` log, describe what occurred, write a specific HTTP query, and pivot on `uid`.

**Key Teaching Points:**
- Sensor HTTP metadata, not host process (**1.1.4**), not body dump, not **1.2.7** files.
- Method, host, URI (together = URL), User-Agent, status, 5-tuple, `uid`.
- Empty field → “not logged.” UA is a claim, not an identity. 200 is not benign.
- Always reinforce the `uid` pivot to `conn`.

**Common Student Challenges:**
- Treating `http` as “the process.” It is not.
- Calling every POST or every `.exe` URI an incident.
- Writing `http` with no filter.
- Inventing a request body.
- Forgetting `uid`.
- Opening Suricata HTTP options (**1.3**).

**Required Materials:**
- Student Guide
- Slide Deck
- Sample `http` rows in the guide
- Optional: live SIEM
- Answer key (this guide)

---

## Learning Objectives

1. Explain the `http` log and method, host, URI/URL, User-Agent, status, and source/destination.
2. Analyze a Zeek HTTP log entry and accurately describe what occurred.
3. Write a SIEM query for *specific* HTTP activity.
4. Pivot with `uid` to `conn` (and related logs).

**Mapped Items:**
- K: 1.2.5.1 – HTTP engine
- T: 1.2.5.2 – Analyze a Zeek HTTP log
- T: 1.2.5.3 – Create a SIEM query to detect specific HTTP activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Sensor vs 1.1.4 |
| Purpose of the http log        | 6 min    | Metadata, not body |
| Key Fields                     | 14 min   | a–f; URL = host+uri |
| Walkthrough Examples           | 14 min   | Students first |
| Hands-On Exercise              | 16 min   | Include uid pivot |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Example 2 if they invent a body |

---

## Detailed Teaching Notes

### 1. Purpose of the http Log

**Talking Points:**
- SOC 3 is A / 2b. Push field names and one-sentence “what occurred.”
- SOC 5/7: B/C and 3c/4c — story + a query a teammate can run.
- Hunter: already B / 3c at 3-level. Push the query bar and the pivot.
- CTI: A / B / B and 1a / 2b / 3c on HTTP (higher than SMTP). Nomenclature plus a simple read. Do not grade them as Hunter 5.

**What to emphasize:**
- No process name on this row. That is **1.1.4**.
- Do not teach file extract here.

**Question to ask:**  
“What did the client ask for, from whom, and what status came back?”

### 2. Key Fields

**Talking Points:**
- Walk outline a–f once. URL is host + uri — say it twice.
- Dual-map 5-tuple to **1.2.2**. Dual-map `uid` to the Conn habit.
- UA can lie. Status is context, not a verdict.

**What to emphasize:**
- Empty `user_agent` / `host` = “not logged.”
- `resp_fuids` mention only as a pointer to **1.2.7**.

**Question to ask:**  
“If I only give you `status_code=200`, do you have a story yet?”

### 3. Examples

Work through all three interactively.

**Extra point for Example 1:**  
Baseline. Internal GET + browser UA + 200.

**Extra point for Example 2:**  
POST + PowerShell UA + beacon-looking URI. Still not a body. Pivot uid.

**Extra point for Example 3:**  
Empty UA + `.exe` + 8080 + 200. 404 spray is a *different* uid.

---

## Hands-On Exercise – Instructor Guidance

**How to run:**
- Give 14–16 minutes.
- Allow the Student Guide.
- Grade description + specific queries + uid pivot. No Suricata.
- Review as a group.

**What good answers look like:**

**Summaries:**
- Example 1: GET intranet PDF; browser UA; 200; expected.
- Example 2: POST to nightowl-updates `/api/v1/beacon`; PowerShell UA; 200; lead.
- Example 3: GET `update.exe` on 8080; UA not logged; 200; lead.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| Zeek `http` GET PDF 200 | **HTTP event** | `http` log |
| Zeek `ssl` SNI intranet | **Not this log** | **1.2.4** |
| MDE chrome → :80 | **Not this log** | **1.1.4** |
| Zeek `files` PDF hash | **Not this log** | **1.2.7** |

**Pseudo-queries (equivalent is fine):**

```
http
| where method == "POST"
    or uri endswith ".exe"
    or uri endswith ".ps1"
    or uri endswith ".dll"
| where user_agent has "PowerShell"
    or user_agent has "curl"
    or user_agent has "python"
    or isempty(user_agent)
| where id.resp_h !startswith "10."
```

```
http
| where status_code in (401, 404)
| summarize count() by id.orig_h, host
| where count_ > 10
```

Fail a query with no method/host/UA/status/URI filter, a `DeviceNetworkEvents` query, or a Zeek `ssl`-only query.

**uid pivot:**  
Copy `uid` from the `http` row. Search `conn` for the same `uid` (duration, bytes, state). Optionally `dns` (name), `ssl` (if TLS), `files` (if extracted).

---

## Knowledge Check – Answer Key

1. **Purpose vs 1.1.4?**  
   **Answer:** `http` records HTTP request/response metadata the **sensor** saw (method, host, URI, UA, status). **1.1.4** is host-observed connect/DNS and names the **process**.  
   **Explanation:** Wire vs endpoint.

2. **URL fields?**  
   **Answer:** `host` + `uri`. Describe them together. Zeek often has no single `url` field.  
   **Explanation:** Outline b + c.

3. **User-Agent?**  
   **Answer:** It is what the client **claimed**. Useful to spot scripts vs browsers. It can be spoofed or empty.  
   **Explanation:** Lead, not identity.

4. **Why 200 is not a verdict?**  
   **Answer:** 200 only means the server answered OK. A beacon POST or an `.exe` GET can be 200.  
   **Explanation:** Read status with method + host + URI.

5. **Why uid?**  
   **Answer:** It links this request to `conn` (and `dns` / `ssl` / `files`) so you can build the rest of the session.  
   **Explanation:** Same habit as Conn / DNS / TLS.

---

## Additional Instructor Resources

- Local expected intranet hosts / browser UAs if you have a list
- Escalation: files → 1.2.7; TLS → 1.2.4; host process → 1.1.4; detections → 1.3
- Next recommended module: 1.2.6 SMTP Engine
