# Module 2.9.1 – VirusTotal (Relations and Behavior)  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.9.1 – VirusTotal (Relations and Behavior)  
**Subtitle:** Extra infrastructure and sandbox events from a seed  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is two VirusTotal tabs on a classroom result card. It is not when to pick the tool, and it is not a live login.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

CTI analysts take a **seed** they already have — a hash, a URL, or an IP.

**Relations** names additional infrastructure.  
**Behavior** extracts process, file, registry, and network events.

Write what the result card shows. You do not need a live account.

**Speaker Notes:**  
This slide is the student intro. When to pick VirusTotal is already taught. This lesson is the two tabs. Do not open a live session.

---

### Slide 3 – Relations
**Title:** Relations — extra infrastructure

Linked objects for this seed: contacted domains, IPs, URLs, and dropped files.

The product is additional **infrastructure** that is on the card.  
Not a hop sentence. Not a detection count.

**Speaker Notes:**  
Relations is the graph you can open next. If they start the four-part hop sentence, that is 2.8.1. Stay on the object the tab names.

---

### Slide 4 – Behavior
**Title:** Behavior — four kinds of events

Events from a **sandbox run** of this sample.

**Process**, **file**, **registry**, and **network**.

If the tab is empty, write **not on card**. Do not invent the event.

**Speaker Notes:**  
Empty Behavior usually means no sandbox run was stored. A contacted domain can appear here too; the product is still the event, not the pivot object.

---

### Slide 5 – What good looks like
**Title:** Write what the card shows

Seed: hash of `update.exe`.

**Relations:** contacted IP `203.0.113.88`. Not a sibling hostname.  
**Behavior:** process start, Temp write, `203.0.113.88:8080`. Not Run `Updater`.

No live account. Do not copy the host plot onto VirusTotal.

**Speaker Notes:**  
Walk this card before the knowledge check. “Not on card” is legal. If they write a SIEM query from port 8080, that convert is 3.3.1.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This lesson is “when to pick VirusTotal.” True or false?  
2. What does Relations give you that Behavior does not?  
3. Seed hash of `update.exe`. Name one Relations result you may write from the card, and one thing you must not invent.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Relations names extra infrastructure.  
Behavior extracts process, file, registry, and network events.  
Write what the card shows, or **not on card**.

**Next:** **2.9.2** AnyRun

**Speaker Notes:**  
AnyRun is search and review of a public detonation card. Do not open it unless that lesson is scheduled.
