# Module 1.4.2 – Alert Classification  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.4.2 – Alert Classification  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Four labels + evidence. FN is a miss. Causes are 1.4.3.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Define TP, FP, TN, FN
2. Classify *cases* and cite evidence
3. Treat FN as a missed detection

**Mapped Items:**  
K: 1.4.2.1 | T: 1.4.2.2

**Speaker Notes:**  
CTI is 1a / 1a / 2b on the task.

---

### Slide 3 – Agenda
**Title:** Agenda

- The 2×2
- Evidence
- Three worked examples (plus a TN)
- Five cases
- Knowledge check

**Speaker Notes:**  
Park 1.4.3.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Why this FP fired (**1.4.3**)  
Scan / root / user category (**1.4.4**)  
Rewriting the rule (**1.3**)  
“FN = I don’t like this alert”

**Key Point:** Label the **case**. Cite.

**Speaker Notes:**  
Draw the fence.

---

### Slide 5 – The 2×2
**Title:** Detection × Reality

|  | Reality bad | Reality benign |
|--|-------------|----------------|
| Fired | **TP** | **FP** |
| Quiet | **FN** | **TN** |

TN and FN usually have **no** queue row.

**Speaker Notes:**  
Outline a–d.

---

### Slide 6 – False Negative
**Title:** FN Is a Miss

Something bad happened.  
No alert fired.  

You meet it in logs, PCAP, or a hunt — not by relabeling a ticket.

**Speaker Notes:**  
Say this twice.

---

### Slide 7 – Evidence
**Title:** Cite, Don’t Slogan

Good: `wscript` + `-enc`; URI `/payload/update.exe`; “no sid on 8080”  
Bad: “malicious”; “looks like C2”

**Speaker Notes:**  
Task wording.

---

### Slide 8 – Example 1: TP
**Title:** Example 1 – Encoded PS

- Alert fired
- wscript + Temp vbs + `-enc`

**Interpretation:**  
**TP.** Cite the chain.

**Speaker Notes:**  
Students first.

---

### Slide 9 – Example 2: FP
**Title:** Example 2 – Get-Help

- Any-PowerShell fired
- explorer + `Get-Help`

**Interpretation:**  
**FP.** Cite the cmdline. Cause class is **1.4.3**.

**Speaker Notes:**  
Stop them if they start “over-broad.”

---

### Slide 10 – Example 3: FN
**Title:** Example 3 – update.exe, No Alert

- PCAP/Zeek: GET on **8080**
- Queue empty

**Interpretation:**  
**FN.** Miss. Not an FP.

**Speaker Notes:**  
Intranet PDF with no alert = **TN**.

---

### Slide 11 – True Negative
**Title:** Nearby TN

Chrome GET intranet PDF.  
No alert.  

**TN** — correctly quiet. Never a ticket.

**Speaker Notes:**  
One beat only.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Miss labeled FP  
- Phantom alert on a TN  
- No cite  
- Writing the FP cause  
- Categories in this hour  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Case Setup
**Title:** Five Cases (Exercise)

A Office → unexpected cmd (alert)  
B Documented export script (no alert)  
C update.exe on another host (no alert)  
D Lab PCAP replay (alert)  
E Intranet PDF (no alert)  

**Speaker Notes:**  
Leave up.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 16–18 minutes

1. Summarize Ex 1–3.
2. Classify A–E with one cite each.
3. At least one FN.
4. No cause class. No category.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Define the four labels.
2. Why is FN not a queue row?
3. What counts as evidence?
4. A TN that is never a ticket?
5. Where does this lesson stop on an FP?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- 2×2. Cite evidence.
- FN = miss. TN = correctly quiet.
- Next: FP **causes** (**1.4.3**).

**Speaker Notes:**  
Do not open 1.4.3 unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Classification — Quick Reference

| Label | Fired? | Bad? |
|-------|--------|------|
| TP | Yes | Yes |
| FP | Yes | No |
| TN | No | No |
| FN | No | Yes |

**Coming next:** Module 1.4.3 – Common false positive causes

**Footer:** SOC / Hunter / CTI Training Program
