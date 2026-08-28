# Module 3.6.3 – Hunt for a Specific Persistence or Privilege-Escalation Technique
## Slide Deck Content

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 3.6.3 – Hunt one named technique  
**Subtitle:** One method, not the whole tactic  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
3.6.1 and 3.6.2 taught recognition. This lesson turns one named method into a bounded hunt. It is not a tactic sweep and not a local ticket.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

Hunters search for activity the alerts **missed**.

After you recognize a method, you turn it into a hunt someone can run.

Name **one method**, a **unique pattern**, and a **bound**.

**Speaker Notes:**  
This slide is the student intro. A class is not a hunt. Do not teach hunt-card format or local tickets today.

---

### Slide 3 – Named technique, not the class
**Title:** Named technique, not the class

**Named** — a method you can point at. HKCU Run **`Updater`**. User parent → SYSTEM child.

**Class** — persistence or privilege escalation. A class is not a hunt by itself.

**Speaker Notes:**  
Named is a value, a parent/child pair, or a specific binary. “Hunt persistence” is the class. Stay on that split before you write the hunt line.

---

### Slide 4 – What you write
**Title:** The hunt line

**Named technique.** The method you can point at.  
**Class.** Persistence or privilege escalation.  
**Unique pattern.** What you search — not the whole tactic.  
**Scope.** Where, how long, which telemetry.  
**Why not the whole tactic.** Why this pattern.

**Speaker Notes:**  
This is the product of the lesson, not a rewrite of the 3.2.2 card. Walk the five pieces, then use the given on the next slide.

---

### Slide 5 – What good looks like
**Title:** One named hunt, two fails

**Hunt** — HKCU Run **`Updater`** → `%TEMP%\update.exe`. Unique pattern is the **value name**, not any Run key. User workstations, last 14 days, registry + file.

**Fail** — “hunt persistence.” No unique pattern.

**Fail** — call a SYSTEM scheduled task privilege escalation when no elevation was shown.

**Speaker Notes:**  
The given is the course-fiction Run value. Do not retell the incident. A SYSTEM task is persistence unless the log shows how a non-privileged actor got SYSTEM.

---

### Slide 6 – Bounded hunt, not the card or the ticket
**Title:** Bounded hunt, not the card or the ticket

This lesson is the **bounded hunt**.

You do not rewrite the hunt card (**3.2.2**).  
You do not pick a hunt type (**3.2.1**).  
You do not remap ATT&CK (**3.5**).  
You do not invent a local ticket (**3.7**).

**Speaker Notes:**  
Keep them on the hunt line. If they want a ticket number, that is 3.7. If they want the four card fields again, that was 3.2.2.

---

### Slide 7 – Knowledge Check
**Title:** Knowledge Check

1. “Hunt persistence” is a valid 3.6.3 hunt. True or false?  
2. What does **named** mean in this lesson?  
3. Write one hunt line for HKCU Run **`Updater`** → `%TEMP%\update.exe` (named technique, class, unique pattern, scope).

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 8 – Summary
**Title:** Summary

One named method. A unique pattern. A bound.  
Wrong class fails.

**Next:** **3.7.1** Hunt control and lead management

**Speaker Notes:**  
3.7.1 is how the shop starts and controls a hunt. Do not invent a ticket in this lesson.
