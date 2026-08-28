# Module 1.4.3 – Common False Positive Causes  
## Slide Deck Content

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 1.4.3 – Common False Positive Causes  
**Subtitle:** Why a false positive fired, and what you would change  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson sits after classification. The case is already a false positive. The work here is the cause class and one named change. Analysts do not deploy that change.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

A **false positive** already used queue time.

Say **why** it matched, and **one change** that would stop the same fire.

You do not re-decide true positive versus false positive.  
You do not deploy the change.

**Speaker Notes:**  
This slide is the student intro. A false positive still used queue time. The job is the cause class and one change so the same benign fire does not keep repeating. Do not re-open classification.

---

### Slide 3 – Two cause classes
**Title:** Analyst or tool versus overly broad

**Analyst or tool activity** — someone tested or downloaded a live rule; replayed a capture; ran a shop-owned scanner.  
Change: exclude that identity or window. Do not delete a good signature.

**Untuned or overly broad detection logic** — any PowerShell; GET on any TCP; MZ-only YARA wired to an alert.  
Change: add a selector. Hand it to detection engineering.

**Speaker Notes:**  
Those two classes are the whole set. If neither fits, say other and still name a change. Do not invent a third official class.

---

### Slide 4 – Class plus one sentence
**Title:** Class plus one sentence

**Overly broad** — `Get-Help` on any-PowerShell.  
Change: require `-enc` and parent `wscript`.

**Analyst or tool** — replay of `GET /update.exe` into production.  
Change: exclude the replay. Do not delete the signature.

**Speaker Notes:**  
Show these two givens before the knowledge check. “Tune it” is not a change. Do not tell the PRD plot.

---

### Slide 5 – Name the change. You do not deploy it.
**Title:** Name the change. You do not deploy it.

Do not reclassify true positive versus false positive.  
Do not deploy the change.  
Do not pick scan, root, or user (**1.4.4**).

**Speaker Notes:**  
Stay on cause and change. Category is the next lesson. Detection engineering deploys.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This lesson is for deciding true positive versus false positive. True or false?  
2. What are the two cause classes?  
3. False positive: any-PowerShell on `Get-Help`. Name the class and one change sentence.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

After a false positive: class plus change.  
Analyst or tool activity versus overly broad logic.  
Name the change. You do not deploy it.

**Next:** **1.4.4** Common alert categorizations

**Speaker Notes:**  
1.4.4 is the site category, not the false-positive cause. Stay off cause class when you get there.
