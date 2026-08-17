# Instructor Guide – Module 1.2.8 – Weird Engine

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.2.8.1 A / B / C · 1.2.8.2 2b / 3c / 4c · 1.2.8.3 2b / 3c / 4c  
- Hunter: 1.2.8.1 B / C / C · 1.2.8.2 3c / 4c / 4c · 1.2.8.3 3c / 4c / 4c  
- CTI: 1.2.8.1 A / A / A · 1.2.8.2 1a / 1a / 1a · 1.2.8.3 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach analysts to read the Zeek `weird` log, describe the type and endpoints, write a *specific* weird query, and pivot on `uid`. Close unit **1.2**.

**Key Teaching Points:**
- Lead generator, not a verdict. Many names are noise.
- `name` is the type. `notice` on this row is a flag, not `notice.log`.
- 5-tuple + `uid`. Empty uid happens — say so.
- Do not teach Zeek script authoring or the full notice framework.
- CTI is A / 1a only — nomenclature.

**Common Student Challenges:**
- Ticketing a single `dns_unmatched_reply`.
- Writing `weird` with no `name` filter.
- Calling `weird.notice` the notice log.
- Forgetting `uid`.
- Asking for a catalog of every Zeek weird name.
- Grading CTI as SOC 5.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional: local top-10 weird names
- Answer key (this guide)

---

## Learning Objectives

1. Explain `name`, `notice` flag, source/destination, and `uid` linking.
2. Analyze a Zeek weird log entry and describe what occurred.
3. Write a SIEM query for *specific* weird activity.
4. Pivot with `uid` to `conn`.

**Mapped Items:**
- K: 1.2.8.1 – Weird engine
- T: 1.2.8.2 – Analyze a Zeek weird log
- T: 1.2.8.3 – Create a SIEM query to detect specific weird activity

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & Objectives      | 4 min    | Last 1.2 unit |
| Purpose of the weird log       | 8 min    | Noise vs lead |
| Key Fields                     | 14 min   | a–c; name vs notice log |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close 1.2 → 1.3 |
| **Total**                      | **~68 min** | Stretch Example 1 if they ticket noise |

---

## Detailed Teaching Notes

### 1. Purpose of the weird Log

**Talking Points:**
- SOC 3: `name` + addresses + one sentence.
- Hunter: volume and stacking with `conn` / `http`.
- CTI: A / 1a. They should recognize the word `weird` and `name`. Stop.

**Question to ask:**  
“What did Zeek think was off, and who was talking?”

### 2. Key Fields

**Talking Points:**
- Walk outline a–c. `name` is a. 5-tuple is b. `uid` is c.
- `notice` flag vs `notice` log — draw two boxes.
- Do not inventory 200 weird names. Use the three in the examples plus any local list.

**Question to ask:**  
“If I only tell you ‘there was a weird,’ do you have a story yet?”

### 3. Examples

**Example 1:** Noise baseline. Resolver unmatched reply.  
**Example 2:** `data_before_established` on the HTTP beacon 5-tuple. Stack; don’t convict.  
**Example 3:** Rare HTTP line-ending + `notice=true` on the update.exe dest.

---

## Hands-On Exercise – Instructor Guidance

**How to run:** 14–16 minutes. Fail `weird` with no filter. Fail treating notice.log as this row.

**Summaries:**
- Example 1: `dns_unmatched_reply` on resolver path; likely noise.
- Example 2: `data_before_established` workstation → 203.0.113.88:80; lead; pivot.
- Example 3: `line_terminated_with_single_CR` on :8080, `notice=true`; lead.

**Identifications:**

| Item | Answer | Why |
|------|--------|-----|
| weird data_before_established | **weird event** | `weird` log |
| http POST beacon | **Not this log** | **1.2.5** — stack via uid |
| notice log policy row | **Not this log** | Different log |
| MDE DeviceNetworkEvents | **Not this log** | **1.1.4** |

**Pseudo-queries:**

```
weird
| where name == "data_before_established"
| where id.orig_h startswith "10.10.50."
    or id.orig_h startswith "10.10.22."
```

```
weird
| where name == "dns_unmatched_reply"
| summarize count() by id.orig_h
| where count_ > 50
```

`notice == true` plus a rare-name list is also acceptable for query 2.

**uid pivot:** Copy `uid` → `conn`, then protocol logs. If uid empty: write “no connection uid”; use `id.*` + `ts` + `name`.

---

## Knowledge Check – Answer Key

1. **Purpose? Why not an incident?**  
   **Answer:** Record protocol/traffic behavior Zeek considers unusual. Many types are common noise; one row is a **lead**.  
   **Explanation:** Weird ≠ malicious.

2. **Type field? notice field?**  
   **Answer:** Type is `name`. `notice` on the weird row is a **boolean flag** (this type also raised a notice), not the notice log itself.  
   **Explanation:** Outline a.

3. **weird vs notice log?**  
   **Answer:** `weird` is the anomaly hook. `notice.log` is policy notices. This lesson signs off on `weird`.  
   **Explanation:** Do not swap the logs.

4. **Source / dest?**  
   **Answer:** `id.orig_h` / `id.orig_p` and `id.resp_h` / `id.resp_p` — same 5-tuple as Conn.  
   **Explanation:** Outline b.

5. **uid? Missing uid?**  
   **Answer:** `uid` joins to `conn` and protocol logs. If missing, write “no connection uid” and use addresses, ports, time, and `name`.  
   **Explanation:** Outline c.

---

## Additional Instructor Resources

- Local top weird names / allow-list if you have one
- Next recommended module: 1.3.1 SIGMA rules
