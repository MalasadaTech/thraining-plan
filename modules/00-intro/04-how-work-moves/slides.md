# Module 0.4 – How work can move  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 0.4 – How work can move  
**Subtitle:** One possible path after an alert  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson names one possible path of work after an alert. It does not teach how to do each step, and it does not name how a shop files the ticket.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

After an alert, work has to go to the **next desk**.

This lesson names **one possible path**. Not the only way a shop runs.

Name the next **hand-off** and **whose product** it is. Not how your site files the ticket.

**Speaker Notes:**  
This slide is the student intro. Desks already have names from 0.3. Today is the path between them. Do not walk how to triage or write an RFI.

---

### Slide 3 – Alert, then triage
**Title:** Alert, then triage

An analyst gets an alert and **triages** it — sorts what it is and what to do next.

Then: **incident response**, and notify **leadership**.

**Speaker Notes:**  
Start of the path. Triage means sort the alert, not write a novel. IR and leadership are next. Do not tell a plot, and do not invent a ticket name.

---

### Slide 4 – Ask intel
**Title:** RFI

**RFI** = Request for Information.  
Ask intel for more work on *that* alert.

Intel works it, **enriches** it (adds context), and may find more infrastructure.

**Speaker Notes:**  
The RFI is the ask, not intel’s finished work. Enrich means add context. Do not teach how to write the RFI.

---

### Slide 5 – Block vs hunt package
**Title:** Block vs hunt package

Extra infrastructure → whoever **blocks** (firewall / IA).

A **hunt package** → hunters, and that same package to **detection engineers** (MDE, YARA, Suricata, SIGMA, and so on).

**Speaker Notes:**  
These are different outputs. Do not send the extra IPs to the hunt team as if that were the block. Two hats is 0.5.

---

### Slide 6 – Name the next hand-off
**Title:** Name the next hand-off

Someone names a step. You name the **next hand-off** and **whose product** it is.

Not how a site files the ticket.

**Given:** intel found extra infrastructure.  
Next: whoever **blocks** (firewall / IA). Product: the block. Not a hunt.

**Speaker Notes:**  
This is the task. Walk the triage given from the student guide if they need a second. Do not invent a ticket path.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. After triage, what two things can the analyst do with the alert besides asking intel?  
2. Extra infrastructure goes to the hunt team. True or false?  
3. Intel found extra infrastructure. Name the next hand-off and whose product it is.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

Alert → triage → IR and leadership → RFI to intel → enrich.  
Extra infrastructure can be blocked.  
A hunt package can go to hunters and to detection engineers.

One possible path. Name the next hand-off and whose product it is.

**Next:** **0.5** Where the jobs overlap

**Speaker Notes:**  
0.5 is same evidence, different product — and one person may do two jobs. Stay off that overlap until then.
