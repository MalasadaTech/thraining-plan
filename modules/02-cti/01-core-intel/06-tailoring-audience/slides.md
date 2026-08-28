# Module 2.1.6 – Tailoring Output to the Audience  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.1.6 – Tailoring Output to the Audience  
**Subtitle:** Same facts, different reader  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
2.1.5 asked whether the product can be acted on. This lesson is who is reading. It is not a channel list and not how to write an actor profile.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts change **how they say the same facts** so the person who will act can use them.

Leadership needs a short so-what. IR needs host, file, and domain.

The assessment does not change.

**Speaker Notes:**  
This slide is the student intro. Name the reader before anyone rewrites. Do not teach channels or the actor profile today.

---

### Slide 3 – Name who is reading
**Title:** Audience analysis

Name **who is reading** and what they can do before you write.

Leadership owns awareness. They cannot work a hash.

IR / SOC owns the host. They need path and domain.

Wrong reader, wrong shape.

**Speaker Notes:**  
This is why audience analysis matters. If they skip it, they send a hash dump to the lead or a one-liner to IR. Consumers in this lesson are leadership and IR / SOC.

---

### Slide 4 – Content, format, detail
**Title:** Content, format, detail

**Content** — which facts this person needs to act.  
**Format** — one sentence versus a short paragraph.  
**Detail** — hash and path versus no hash.

Facts stay. Detail changes.

**Speaker Notes:**  
Walk the three adjustments. Leadership does not need the hash. Do not invent a style guide. Do not pick a ticket type.

---

### Slide 5 – Same A12, two readers
**Title:** Same A12, two readers

**Given:** `jlee` on **WS-JLEE** ran encoded PowerShell from a script. IR has the host.

**Leadership** — **WS-JLEE** / `jlee` ran encoded PowerShell from a script; IR has the host.  
No hash.

**IR / SOC** — add Temp `invoice.vbs` and the update domain.

**Speaker Notes:**  
Show this given before the knowledge check. Same assessment. Not a different plot. Do not add the Run key or a file hash to the leadership line.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Tailoring means you change the judgment so leadership likes it. True or false?  
2. What three things do you adjust for a named audience?  
3. Same A12 facts: `jlee` on **WS-JLEE** ran encoded PowerShell from Temp `invoice.vbs`; IR has the host; the update domain is in the case. Write the leadership line (no hash) and what you add for IR.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Name who is reading before you write.  
Same facts. Different content, format, and detail.  
Leadership does not need the hash.

**Next:** **2.1.7** Attribution

**Speaker Notes:**  
2.1.7 is who you claim. Stay off that assessment unless that lesson is scheduled.
