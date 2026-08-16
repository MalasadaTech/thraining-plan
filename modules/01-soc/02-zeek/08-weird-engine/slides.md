# Module 1.2.8 – Weird Engine  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.2.8 – Weird Engine  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Last 1.2 unit. Lead generator, not a verdict. CTI is A / 1a only.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Explain `name`, the `notice` flag, source/destination, and `uid` linking
2. Analyze a Zeek `weird` log entry and describe what occurred
3. Write a SIEM query for *specific* weird activity
4. Pivot with `uid` to `conn`

**Mapped Items:**  
K: 1.2.8.1 | T: 1.2.8.2 | T: 1.2.8.3

**Speaker Notes:**  
Do not grade CTI as SOC 5.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose of the weird log
- Fields (outline a–c)
- Noise vs lead
- Three worked examples
- Two queries
- Knowledge check — close 1.2

**Speaker Notes:**  
1.3 is next unit.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

The `notice` log (policy notices)  
Writing Zeek scripts  
Memorizing every weird `name`  
Host process rows (**1.1**)  
“Weird = incident”

**Key Point:** Describe *this* `weird` row.

**Speaker Notes:**  
Park notice-framework questions.

---

### Slide 5 – Purpose of the weird Log
**Title:** Purpose of the weird Log

- Zeek saw something **off-spec or uncommon**
- A **lead**, often noise
- Complements `conn` (what the session did)

**Key Point:** The word “weird” is not a verdict.

**Speaker Notes:**  
Ask: “What was off, and who was talking?”

---

### Slide 6 – The Type
**Title:** Weird Activity Type = name

**name** — the type string you query  
**addl** — extra detail when present  

Describe the string you have.  
Do not inventory the whole catalog this hour.

**Speaker Notes:**  
Outline a.

---

### Slide 7 – notice Flag vs notice Log
**Title:** Two Different Things

**`weird.notice`** — boolean on this row  
**`notice.log`** — a different log (policy notices)

This lesson signs off on **`weird`**.  
`notice=true` means “this type was also raised,” not “read the notice course.”

**Speaker Notes:**  
Two boxes on the board.

---

### Slide 8 – Addresses and uid
**Title:** Source, Dest, Pivot

`id.orig_*` / `id.resp_*` — same 5-tuple as Conn  
`uid` → `conn`, then `http` / `dns` / `ssl` / `files`

No `uid` → write “no connection uid.” Use IP/port/time/`name`.

**Speaker Notes:**  
Outline b and c.

---

### Slide 9 – Example 1: Noise
**Title:** Example 1 – dns_unmatched_reply

- Resolver `10.10.8.53` ↔ workstation
- `notice: false`

**Interpretation:**  
Often noise. Do not ticket a single row.

**Speaker Notes:**  
Students first. Volume would change the story.

---

### Slide 10 – Example 2: Timing Weird
**Title:** Example 2 – data_before_established

- `10.10.50.88` → `203.0.113.88:80`
- Same pair as the HTTP POST beacon *if uid matches*

**Interpretation:**  
Lead. Stack with `conn` / `http`. Not C2 by itself.

**Speaker Notes:**  
Force the pivot.

---

### Slide 11 – Example 3: notice true
**Title:** Example 3 – HTTP Line Ending

- `line_terminated_with_single_CR`
- Dest `:8080` (update.exe session)
- `notice: true`

**Interpretation:**  
Lead. Name the type and the flag. Pivot.

**Speaker Notes:**  
Do not teach notice policy.

---

### Slide 12 – Pivoting with uid
**Title:** Pivoting with the uid Field

1. Interesting `weird` row  
2. Copy `uid`  
3. Search `conn` (`history`, `conn_state`, bytes)  
4. Then the protocol log that matches the dest port  

**Speaker Notes:**  
Same habit as every 1.2 engine.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- All weird = incident  
- Query with no `name`  
- `weird.notice` = notice log  
- Forgetting `uid`  
- Asking for every Zeek `name`  

**Speaker Notes:**  
Then the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example (noise vs lead).
2. Two queries: specific `name` from user subnets; volume (or `notice==true`).
3. Explain the `uid` pivot (and empty uid).
4. Identify the four items.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Purpose of `weird`? Why not an incident?
2. Type field? `notice` field?
3. `weird` vs `notice` log?
4. Source / dest fields?
5. `uid` — and if it is missing?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- `weird` = Zeek thought something was off. Lead, not verdict.
- Query `name` (and volume). Read 5-tuple + `uid`.
- `notice` on this row is a flag.
- Unit **1.2** ends here. Next unit: **1.3** Detection Engineering.

**Speaker Notes:**  
Do not open a SIGMA lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Weird — Quick Reference

| Need | Look at |
|------|---------|
| Type | `name` (+ `addl`) |
| Who | `id.orig_*` / `id.resp_*` |
| Raised? | `notice` flag |
| Session | `uid` → `conn` |

**Coming next:** Module 1.3.1 – SIGMA rules

**Footer:** SOC / Hunter / CTI Training Program
