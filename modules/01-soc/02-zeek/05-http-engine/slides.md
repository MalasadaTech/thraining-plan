# Module 1.2.5 – HTTP Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.2.5 – HTTP Engine  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Zeek `http` log. Metadata, not body dump. Not 1.1.3 process.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Explain method, host, URI/URL, User-Agent, status, and source/destination
2. Analyze a Zeek `http` log entry and describe what occurred
3. Write a SIEM query for *specific* HTTP activity
4. Pivot with `uid` to `conn`

**Mapped Items:**  
K: 1.2.5.1 | T: 1.2.5.2 | T: 1.2.5.3

**Speaker Notes:**  
Hunter starts at B / 3c. CTI is A / B / B and 1a / 2b / 3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose of the http log
- Fields (outline a–f)
- Three worked examples
- uid pivot
- Identification + two queries
- Knowledge check

**Speaker Notes:**  
1.2.7 files and 1.3 detections are later.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Host process on port 80 (**1.1.3**)  
TLS SNI / JA3 (**1.2.4**)  
File hash / extract (**1.2.7**)  
HTTP *body* content  
Suricata `http.*` rules (**1.3**)

**Key Point:** Describe *this* `http` row.

**Speaker Notes:**  
Park body and Suricata questions.

---

### Slide 5 – Purpose of the http Log
**Title:** Purpose of the http Log

- Written by Zeek’s HTTP engine
- Request / response **metadata** on the wire
- Complements `conn` (who talked) and `dns` (what resolved)
- Does **not** name the process

**Key Point:** Sensor HTTP ≠ endpoint network.

**Speaker Notes:**  
Ask: “What did they ask for, and what status came back?”

---

### Slide 6 – Method, Host, URI
**Title:** Method, Host, URI = the Ask

**method** — GET, POST, PUT, HEAD  
**host** — Host header  
**uri** — path + query  

**URL** = `host` + `uri`  
There is often no single `url` field.

**Speaker Notes:**  
Write a full URL on the board from the two fields.

---

### Slide 7 – User-Agent and Status
**Title:** User-Agent and Status Code

**user_agent** — what the client claimed (can lie or be empty)  
**status_code** — 200 / 301 / 404 / 401 …

Empty UA → “not logged.”  
200 is not benign. 404 is not safe.

**Speaker Notes:**  
PowerShell UA vs Chrome UA — one contrast.

---

### Slide 8 – Source, Dest, uid
**Title:** Who, Where, and the Pivot

`id.orig_h` / `id.orig_p` — client  
`id.resp_h` / `id.resp_p` — server  
`uid` — copy it → search `conn`

**Analyst Tip:** `host` is a name. `id.resp_h` is the IP. Read both.

**Speaker Notes:**  
Same 5-tuple / uid habit as Conn.

---

### Slide 9 – Example 1: Expected GET
**Title:** Example 1 – Intranet PDF

- `GET` `intranet.buildingc.internal` `/docs/q3-notes.pdf`
- Browser UA
- `200` on port 80

**Interpretation:**  
Expected. Not an incident.

**Speaker Notes:**  
Students describe first.

---

### Slide 10 – Example 2: POST + PowerShell UA
**Title:** Example 2 – Beacon-Shaped POST

- `POST` `checkin.nightowl-updates.net` `/api/v1/beacon`
- `WindowsPowerShell/5.1…`
- `200` to `203.0.113.88`

**Interpretation:**  
Lead because of method + host + UA. No body on this row.

**Speaker Notes:**  
Force: 200 ≠ expected.

---

### Slide 11 – Example 3: GET .exe
**Title:** Example 3 – update.exe on 8080

- `GET` `/payload/update.exe`
- UA empty
- Port 8080, status 200

**Interpretation:**  
Lead. Write “UA not logged.” Different uid from a 404 spray.

**Speaker Notes:**  
Point file extract to 1.2.7.

---

### Slide 12 – Pivoting with uid
**Title:** Pivoting with the uid Field

1. Find an interesting `http` record  
2. Copy the `uid`  
3. Search `conn` for the same `uid`  
4. Then `dns` / `ssl` / `files` if those rows exist  

Duration, bytes, state, name, extract.

**Speaker Notes:**  
Demonstrate even with static examples.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- `http` row = process name  
- Query with no filter  
- Inventing the POST body  
- 200 = benign  
- Forgetting `uid`  
- Opening Suricata or files-hash class

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Two queries: scripting/empty UA + POST or executable URI; 401/404 volume by orig.
3. Explain the `uid` pivot.
4. Identify the four items in the student guide.

**Speaker Notes:**  
Review with the Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Purpose of `http` vs 1.1.3?
2. Which fields make the URL?
3. Why User-Agent is not an identity?
4. Why 200 is not a verdict?
5. Why `uid`?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- `http` log = method, host, URI, UA, status, 5-tuple.
- URL = host + URI. Empty field → “not logged.”
- Leads: odd method/UA/URI/port/status — not automatic incidents.
- Always pivot with `uid` to `conn`.
- Next: SMTP engine (**1.2.6**).

**Speaker Notes:**  
Do not open an SMTP lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** HTTP — Quick Reference

| Need | Look at |
|------|---------|
| Ask | `method` `host` `uri` |
| Client claim | `user_agent` |
| Result | `status_code` |
| Who / where | `id.orig_*` / `id.resp_*` |
| Pivot | `uid` → `conn` |

**Coming next:** Module 1.2.6 – SMTP Engine

**Footer:** SOC / Hunter / CTI Training Program
