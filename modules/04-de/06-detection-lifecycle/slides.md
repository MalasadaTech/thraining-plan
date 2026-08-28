# Module 4.6 – Detection lifecycle  
## Slide Deck Content

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 4.6 – Detection lifecycle  
**Subtitle:** Modify, retire, or leave a live rule  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is a regular review of a detection you already own. It is not a SOC tune request and not how to write a rule.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Detection engineers own **live** rules — detections that are already deployed.

Those rules do not stay useful forever. Review them: **modify**, **retire**, or **leave**, and cite why.

A **block** is not automatic retire.

**Speaker Notes:**  
This slide is the student intro. Regular review of the set you own, not a ticket from SOC. Do not teach how to write a rule.

---

### Slide 3 – Modify, retire, leave
**Title:** Modify, retire, leave

**Modify** — the rule should stay, but not as it is.  
**Retire** — the rule should come out.  
**Leave** — it is still useful. Do not change it because someone is tired of it.

**Speaker Notes:**  
The three calls are the product of this lesson. Tune, exception, and replace are answers to a SOC request in 4.4. Do not teach that inbox here.

---

### Slide 4 – Cite the reason
**Title:** Cite the reason

Still useful. Too noisy. Threat gone.  
Sensor gone. A nomination replaced it.  
Already blocked — so the rule *may* not be needed.

**Speaker Notes:**  
A nomination here means someone asked for a new or different detection that now covers this. Sensor gone is a reason only. How to check a dead sensor is 4.7.

---

### Slide 5 – A block is not automatic retire
**Title:** A block is not automatic retire

Whoever **blocks** (firewall / IA) stopped that infrastructure.

Does this rule still earn its keep?  
Keep it if it still watches something else.  
Retire it if it only existed for what is now blocked.

**Speaker Notes:**  
Walk the student-guide givens if you need them. Too noisy → modify. Threat gone → retire. Still useful and a tired SOC → leave. Blocked IP → decide, do not auto-retire.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Name the three lifecycle calls.  
2. “We blocked this infrastructure” means you must retire the matching rule. True or false?  
3. A live rule still catches the intended activity. SOC wants it gone because it is busy. Modify, retire, or leave?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Modify, retire, or leave — and cite why.  
A block is not automatic retire.

**Speaker Notes:**  
Sensors are next. That lesson is whether the sensor was up, not this review.

---

### Slide 8 – Next
**Title:** Next

**4.7** Sensor availability and performance

**Speaker Notes:**  
4.7 is sometimes DE. A dead sensor is not “no threat.” Not vendor admin.
