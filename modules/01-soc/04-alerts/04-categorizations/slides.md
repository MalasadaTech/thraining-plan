# Module 1.4.4 – Common Alert Categorizations  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.4.4 – Common Alert Categorizations  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Site buckets. Assign + reject neighbor. CTI is A/1a.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Name scan / root / user / unsuccessful / other
2. Assign a category and justify why it is **not** the adjacent one

**Mapped Items:**  
K: 1.4.4.1 | T: 1.4.4.2

**Speaker Notes:**  
Not TP/FP. Not ATT&CK.

---

### Slide 3 – Agenda
**Title:** Agenda

- Four buckets + other
- Adjacent pairs
- Three worked examples
- Four alerts
- Knowledge check

**Speaker Notes:**  
1.4.5 next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

TP / FP (**1.4.2**)  
FP causes (**1.4.3**)  
ATT&CK IDs (**1.5**)  
“Looks like malware so root”

**Key Point:** Bucket + rejected neighbor.

**Speaker Notes:**  
Fence.

---

### Slide 5 – The Buckets
**Title:** Classroom Categories

Scanning / reconnaissance  
Root-level access  
User-level access  
Unsuccessful activity  
**Other** — local list only

**Speaker Notes:**  
Outline a–e.

---

### Slide 6 – Neighbors
**Title:** Adjacent Pairs

Scan ↔ unsuccessful  
User-level ↔ root-level  

Token, not file path.  
Failed login ≠ port sweep.

**Speaker Notes:**  
The whole task.

---

### Slide 7 – Other
**Title:** Other (Local)

Only names your site already uses.  
Still reject a neighbor.  
Do not invent tactics as categories.

**Speaker Notes:**  
Show local list if you have one.

---

### Slide 8 – Example 1: Scan
**Title:** Example 1 – 150 Ports, No Auth

**Scanning.**  
Not unsuccessful — no access attempt.

**Speaker Notes:**  
Students first.

---

### Slide 9 – Example 2: User
**Title:** Example 2 – jlee Medium -enc

**User-level.**  
Not root — token is Medium.

**Speaker Notes:**  
Scary ≠ SYSTEM.

---

### Slide 10 – Example 3: Unsuccessful
**Title:** Example 3 – 40× 401 One Mailbox

**Unsuccessful.**  
Not scanning — one app, failed auth.

**Speaker Notes:**  
HKLM service create = root, not user.

---

### Slide 11 – Root Nearby
**Title:** Nearby Root

Temp `helpdesk.exe` creates HKLM Services key.  

**Root-level** (service/HKLM).  
Not user-level — path is not the token.

**Speaker Notes:**  
One beat.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Encoded = root  
- Failed logon = scan  
- Scanner sweep argued as FP here  
- T1059 as the category  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Sentence Shape
**Title:** Two Sentences

“Category: …”  
“Not … because …”

**Speaker Notes:**  
Leave up.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize Ex 1–3.
2. A–D: category + rejected neighbor + why.
3. No TP/FP. No ATT&CK.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Four buckets + other?
2. Scan vs unsuccessful?
3. User vs root?
4. Why not “assign appropriate” only?
5. Where does ATT&CK belong?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Site buckets. Reject the neighbor.
- Token ≠ path. Failed auth ≠ sweep.
- Next: SLA clocks (**1.4.5**).

**Speaker Notes:**  
Do not open 1.4.5 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Categories — Quick Reference

| Bucket | Reject |
|--------|--------|
| Scan | Unsuccessful |
| Unsuccessful | Scan |
| User-level | Root-level |
| Root-level | User-level |
| Other | Name it; still reject a neighbor |

**Coming next:** Module 1.4.5 – SLA / response time goals

**Footer:** SOC / Hunter / CTI Training Program
