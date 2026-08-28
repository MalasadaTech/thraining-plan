# Module 4.7 – Sensor availability and performance  
## Slide Deck Content

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 4.7 – Sensor availability and performance  
**Subtitle:** Detection Engineer (SOC / Hunter / CTI sit this too)  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the sensor check: was the collector up and seeing the right place. It is not vendor admin and not how to size a collector. Readers who skip 4.6 can still take it.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Detections only fire on what a **sensor** actually saw.

When a rule never fires, DE sometimes asks: was the sensor **up** and looking at the **right place**?

Check the **rule**, the **sensor**, or **both**.  
A dead sensor is not “no threat.”

**Speaker Notes:**  
This slide is the student intro. A silent rule is not always a broken rule. Stay on that check. Do not teach vendor consoles or a site diagram.

---

### Slide 3 – Up and seeing the right place
**Title:** Up and seeing the right place

**Sometimes** DE watches sensors.  
Examples: **MDE**, **Zeek**, **IDS**.

“Up and seeing the right place” means the collector is working and looking at the host or path the rule needs.

Not a vendor-admin course. Not architecture.

**Speaker Notes:**  
Name the three as places, not a lab. Do not log into the box. Do not invent where those sensors sit at a site.

---

### Slide 4 – Dead or blind is not no threat
**Title:** Dead or blind is not “no threat”

**Dead** — the sensor is down or not sending.  
**Blind** — it is up, but it is not looking at that host or path.

The activity may still have happened.  
You just could not see it.

**Speaker Notes:**  
Silence is a gap, not a close. Do not let them treat a down sensor as proof nothing happened.

---

### Slide 5 – The rule never fired
**Title:** Rule, sensor, or both

Sensor up and seeing that host — check the **rule**.  
Sensor down or not seeing that place — check the **sensor**, or **both**.

A down sensor is not proof the activity did not happen.

**Speaker Notes:**  
Walk the three student-guide givens if you need them. Down all week so “nothing happened” is a reject. The product is the check, not a ticket.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. A down sensor means the activity did not happen. True or false?  
2. Someone says “the rule never fired.” What two things might you check?  
3. Name three kinds of sensor this lesson uses as examples.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Sometimes DE checks sensors.  
Dead is not “no threat.”  
Rule, sensor, or both.  
Not vendor admin.

**Speaker Notes:**  
Site lists are next. Obtain them. Do not invent fields or a change path.

---

### Slide 8 – Next
**Title:** Next

**4.8** Site-specific DE knowledge

**Speaker Notes:**  
That lesson is local policy: obtain the list and the path. Do not invent either.
