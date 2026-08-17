# Module 3.3.2 – External Tools  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 3.3.2 – External Tools  
**Subtitle:** CTI Analyst Training (Hunter secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Select + one hop. Closes 3.3. Overlay live tools if you have them.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Purpose, strength, weakness of each
2. When in the intel process
3. Select and reject the neighbor
4. One enrichment hop

**Mapped Items:**  
K: 3.3.2 | T: 3.3.2.1

**Speaker Notes:**  
Hunter and CTI 3-level task is 3c / 4d. SOC is 1a / 2b / 3c.

---

### Slide 3 – Agenda
**Title:** Agenda

- Four-tool card
- Three examples
- Select four + pivot three
- Knowledge check — close 3.3

**Speaker Notes:**  
3.4 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Internal TIP (**3.3.1**)  
Hunt → SIEM/Zeek (**2.3.1**)  
VT Relations / Behavior (**3.9**)  
imphash / ssdeep (**3.4**)

**Key Point:** Which external tool. One hop.

**Speaker Notes:**  
Fence.

---

### Slide 5 – VT and AnyRun
**Title:** File / Hash / Behavior

**VT** — reputation + related files. Public. No PDNS.  
**AnyRun** — detonate a **sample**. Needs a file.

**Speaker Notes:**  
Outline a.

---

### Slide 6 – Silent Push and URLScan
**Title:** Infra / Page

**Silent Push** — historical DNS, siblings. Not a sandbox.  
**URLScan** — this page load. Not PDNS.

**Speaker Notes:**  
Outline a.

---

### Slide 7 – When
**Title:** First External Tool

Hash/file look-up → **VT**  
Have a binary → **AnyRun**  
Domain/IP history → **Silent Push**  
Live URL → **URLScan**  
Seen internally? → **TIP**

**Speaker Notes:**  
Outline b.

---

### Slide 8 – One Hop
**Title:** Classroom Advanced

VT → one contacted domain or communicating file  
AnyRun → dropped hash or C2  
Silent Push → historical A or sibling  
URLScan → redirect or contacted host  

Stop. Graphs = **3.9**.

**Speaker Notes:**  
Task 2.

---

### Slide 9 – Example 1: Hash
**Title:** Example 1 – VT

Hash in VT. One hop to `nightowl-updates.net`.  
Then Silent Push is a *new* select.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: History
**Title:** Example 2 – Not URLScan

Year of A records → **Silent Push**.  
URLScan is this load only.

**Speaker Notes:**  
Lead.

---

### Slide 11 – Example 3: No Sample
**Title:** Example 3 – Not AnyRun

SNI only. Nothing to detonate.  
Infra tools first.

**Speaker Notes:**  
Lead.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- URLScan for PDNS  
- AnyRun with no file  
- VT as the TIP  
- 12-hop Relations  
- Zeek query now  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Site Overlay
**Title:** Classroom vs Site

Use licensed tools if posted.  
Keep: select + one hop.

**Speaker Notes:**  
Do not invent org policy.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. A–D: select (C = TIP).
3. A, B, D: one hop.
4. No SIEM query.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Strength and weakness — each tool?
2. Silent Push vs URLScan?
3. VT one hop vs 3.9?
4. Why not external for “have we seen it?”
5. Where is the hunt/SIEM conversion?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Four tools. Select. One hop.
- Cluster **3.3** ends. Next: **3.4**.

**Speaker Notes:**  
Do not open 3.4 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** External Tools — Quick Reference

| Need | Tool | One hop |
|------|------|---------|
| Hash | VT | Contacted domain / file |
| Sample | AnyRun | Dropped hash / C2 |
| History | Silent Push | A record / sibling |
| Live URL | URLScan | Redirect / host |
| Internal | TIP (3.3.1) | — |

**Coming next:** Module 3.4 – File similarity and hashing

**Footer:** SOC / Hunter / CTI Training Program
