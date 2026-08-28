# Module 2.8.2 – Extracting Applicable TTPs from Intelligence Reports  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 2.8.2 – Extracting applicable TTPs  
**Subtitle:** Keep what a defender here can use  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is extract and apply. It is not how to map a new ATT&CK ID, and it is not the impact paragraph.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A vendor report often names many techniques.

CTI analysts pull the behaviors a defender **here** can detect or hunt.

They do not copy the whole ATT&CK table.

**Speaker Notes:**  
This slide is the student intro. A long vendor table wastes hunt and detection time if those techniques cannot happen on this network. Stay on extract and apply. Mapping and impact wait.

---

### Slide 3 – Find TTPs in a report
**Title:** Find TTPs in a report

A **TTP** is a **behavior** — how the adversary works. Not an IOC.

**Keep as a candidate** when the report gives a **how**: tool, command, procedure, or ATT&CK ID tied to that how.

**Skip** hashes, IPs, slogans (“they use persistence”), and an ID with no how.

Use **real** ATT&CK IDs only.

**Speaker Notes:**  
This is how you identify a relevant TTP. Do not start the keep-for-DYA test until they can tell a how from a slogan. Do not teach IOC handling.

---

### Slide 4 – Applicable to this environment
**Title:** Applicable to this environment

**Platform** — we have that OS / stack.  
**Path** — the behavior can happen here.  
**Use** — a defender here can detect or hunt it.

Classroom shop: **DYA**, a law firm with Windows workstations.

**Reject** OT / ICS, macOS-only, or no path here.

**Speaker Notes:**  
Name the three criteria. If they have no visibility and no way to get it, it is not applicable unless they name that gap — and they still do not list it as usable. Site facts at a real shop come from that shop.

---

### Slide 5 – Keep or reject
**Title:** Keep or reject

**Keep** — **T1059.001** PowerShell (encoded). **WS-JLEE** already showed it. Applies.

**Reject** — wipe OT historians. Not this shop. Write **not applicable here**.

Not an ATT&CK mapping class. Not an impact paragraph.

**Speaker Notes:**  
Walk both lines before the knowledge check. The product is keep / reject for this environment. If they write a crisis sentence, that is the next impact lesson, not this one.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Every ATT&CK ID in a vendor report is applicable here. True or false?  
2. What three things make a TTP applicable to this environment?  
3. Encoded PowerShell (**T1059.001**) vs an OT-wipe TTP — keep or reject each, and why?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Find TTPs that have a how.  
Keep what this shop can see or hunt.  
Reject the rest.

**Speaker Notes:**  
IOC handling is next. Stay off keep / expire / enrich / link unless that lesson is scheduled.

---

### Slide 8 – Next
**Title:** Next

**2.8.3** IOC handling

**Speaker Notes:**  
2.8.3 treats the indicator as an object. This lesson was the TTP extract for this environment.
