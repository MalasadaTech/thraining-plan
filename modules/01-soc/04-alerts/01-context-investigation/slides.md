# Module 1.4.1 – Alert Context and Investigation  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 1.4.1 – Alert Context and Investigation  
**Subtitle:** SOC Analyst Training (Hunter / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Work the alert object. Do not classify. Do not author rules.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Present vs missing context
2. What the configuration would fire
3. Name each upstream hop
4. What endpoint logs add or fail to add
5. What PCAP adds versus the alert (or N/A)

**Mapped Items:**  
K: 1.4.1.1 | T: 1.4.1.2–1.4.1.6

**Speaker Notes:**  
CTI is 1a on logs/PCAP.

---

### Slide 3 – Agenda
**Title:** Agenda

- Context and configuration
- Hops, logs, PCAP
- Three worked examples
- Five-line cards
- Knowledge check

**Speaker Notes:**  
1.4.2 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Writing SIGMA / Suricata / SIEM (**1.3**)  
TP / FP / TN / FN (**1.4.2**)  
FP *causes* (**1.4.3**)  
Inventing a missing command line  
PCAP on a process-only alert

**Key Point:** Five sentences. Not “I opened the alert.”

**Speaker Notes:**  
Park classify.

---

### Slide 5 – Context
**Title:** Present vs Missing

**Context** = what arrived with the alert  
Two columns: present | missing  

Missing ≠ benign. Do not invent the field.

**Speaker Notes:**  
Outline a. Task 1.

---

### Slide 6 – Configuration
**Title:** What Would Fire

Read the SIEM rule / sid / translated SIGMA.  
One sentence: what would fire.  

You are not proposing a new rule.

**Speaker Notes:**  
Outline b. Task 2.

---

### Slide 7 – Upstream Hops
**Title:** Name Each Hop

Classroom chain:  
`Suricata sid` → `SIEM correlation` → `SIEM alert`

SIEM-only is one hop. Say so. Do not invent Suricata.

**Speaker Notes:**  
Outline c. Task 3.

---

### Slide 8 – Logs and PCAP
**Title:** What They Add

**Endpoint logs** — what they add or **fail to add**  
**PCAP** — contrast with alert fields, or **N/A**

“I queried” is not the task.

**Speaker Notes:**  
Outline d–e. Tasks 4–5.

---

### Slide 9 – Example 1: Complete
**Title:** Example 1 – Encoded PS Alert

- Context has parent + `-enc`
- Config matches 1.3.1 Example 1
- SIEM-only hop
- Logs add Temp `invoice.vbs`
- PCAP N/A

**Interpretation:**  
Complete investigation card. Not a verdict.

**Speaker Notes:**  
Students first.

---

### Slide 10 – Example 2: Thin
**Title:** Example 2 – Any PowerShell

- Missing cmdline, parent, user
- Config: any powershell create
- Logs **add** explorer + Get-Help

**Interpretation:**  
Lead as an investigation. Park FP / rewrite.

**Speaker Notes:**  
Force “what logs add.”

---

### Slide 11 – Example 3: Network
**Title:** Example 3 – GET update.exe

- Hops: sid 1000001 → SIEM → alert
- Logs **fail** to add a process
- PCAP **adds** the URI

**Interpretation:**  
Lead. Three hops. Contrast PCAP vs IP:port.

**Speaker Notes:**  
URI was missing on the pane.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Inventing missing fields  
- “That’s an FP” in this hour  
- Rewriting SIGMA  
- Fake Suricata hop  
- PCAP on a process alert  

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Card Template
**Title:** Five-Line Card

1. Present / missing  
2. Config would fire …  
3. Hops: …  
4. Logs add / fail to add …  
5. PCAP adds … / N/A  

**Speaker Notes:**  
Leave this up for the exercise.

---

### Slide 14 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. Summarize each example.
2. Five-line cards for Ex 2 and Ex 3.
3. Five-line card for Office → cmd.
4. No TP/FP. No new rule.

**Speaker Notes:**  
Instructor Guide key.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. Context vs configuration?
2. What does “missing” mean?
3. Three-hop vs one-hop chain?
4. What must the logs sentence contain?
5. When is PCAP N/A?

**Speaker Notes:**  
Interactive.

---

### Slide 16 – Summary
**Title:** Key Takeaways

- Present vs missing. What would fire. Named hops.
- Logs/PCAP must add or fail to add.
- Next: classification (**1.4.2**).

**Speaker Notes:**  
Do not open a classify lab unless scheduled.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Investigation — Quick Reference

| Need | Write |
|------|--------|
| Context | present / missing |
| Config | what would fire |
| Chain | each hop |
| Host | logs add / fail |
| Wire | PCAP vs alert / N/A |

**Coming next:** Module 1.4.2 – Alert classification

**Footer:** SOC / Hunter / CTI Training Program
