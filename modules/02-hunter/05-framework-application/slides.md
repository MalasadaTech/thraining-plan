# Module 2.5.1 – Using MITRE ATT&CK for Hunt Planning and Coverage Analysis  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.5.1 – ATT&CK for Hunt Planning  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
2.4.2 was copy the printed ID. This lesson is map this hunt, name gaps, support priority. Not persistence how-to.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Map a hunt plan or findings to tactics and techniques
2. Name detection vs visibility gaps from that map
3. Use ATT&CK to support hunt priority
4. Tell a map apart from a copied ID or a heat map

**Mapped Items:**  
K: 2.5.1 | T: 2.5.1.1–2.5.1.3

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Mapping tops at 4c. Gaps and priority can reach 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Copy vs map
- Tactics and techniques for *this* hunt
- Detection vs visibility gaps
- ATT&CK-supported priority
- Three worked examples
- Identification practice
- Hands-on ATT&CK card
- Knowledge check

**Speaker Notes:**  
2.6 is how techniques work. Stay here.

---

### Slide 4 – Not a Map
**Title:** A Heat Map Is Not the Hunt

“Whole intrusion-set layer.”  
“Everything in Persistence is red.”  
“Added T1547.001 so we have coverage.”  
“Hunt TA0003 first because it is reddest.”

**Key Point:** Map the hunt you will run. Not the vendor matrix.

**Speaker Notes:**  
Leave the slogans up. Kill them in Examples 2 and 3.

---

### Slide 5 – Copy vs Map
**Title:** 2.4.2 vs 2.5

| 2.4.2 | 2.5 |
|-------|-----|
| ID already printed | Tactic + technique + *this* method |
| Record or write **none given** | Plan or findings |
| Do not invent | Still do not invent |

**Analyst Tip:** A copied ID is an input to the map, not coverage analysis.

**Speaker Notes:**  
Reuse T1071.001 from the finance leftover if they still have it.

---

### Slide 6 – What to Write
**Title:** Mapping a Hunt

**Plan:** method you will search → TA + T  
**Findings:** method you saw → TA + T  

**Good:** finance CDN C2 → **TA0011** / **T1071.001**  
**Not a map:** “they use persistence”

**Key Point:** Navigator is a view. A table is enough.

**Speaker Notes:**  
Map one leftover live. Two rows only.

---

### Slide 7 – Two Gap Types
**Title:** Coverage After the Map

| Gap | Meaning | Hunt it? |
|-----|---------|----------|
| **Detection** | Logs exist; no analytic | Often yes, if scoped |
| **Visibility** | Cannot see the technique | No — name it |

**Analyst Tip:** Ask per *mapped* technique, not per red cell.

**Speaker Notes:**  
Force: no registry logs → visibility, not a Persistence hunt.

---

### Slide 8 – Priority
**Title:** ATT&CK Supports Priority

ATT&CK + scope + “can this search run.”

**Good:** T1059.005, Building C, process logs, no analytic → first  
**Not a reason:** reddest tactic · “persistence is always first”

**Key Point:** Same technique on two hunts → ATT&CK cannot break the tie (**2.2.2**).

**Speaker Notes:**  
SOC 2.5.1.3 is 1a / 1a / 2b — recognize a usable reason.

---

### Slide 9 – Example 1: Complete Card
**Title:** Example 1 – Finance CDN

- Map: **TA0011** / **T1071.001**
- Detection gap: finance DNS+TLS, no name analytic
- Visibility: lab (no DNS) — do not hunt
- Priority: finance after-hours first

**Interpretation:**  
Mapped. Not a heat map. Not executed. Task aside still dropped.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: Heat Map
**Title:** Example 2 – Layer vs Hunt

**A:** Whole intrusion-set layer. Hunt TA0003 because it is reddest.  
**B:** T1059.005 only. Detection gap on Building C process-create. Finite window.

**Interpretation:**  
A is not a map. B is map / gap / reason.

**Speaker Notes:**  
Same dump family as 2.4.2 Example 2.

---

### Slide 11 – Example 3: Invented Technique
**Title:** Example 3 – Fill Persistence

**A:** Invent T1547.001. No registry logs. Hunt persistence.  
**B:** Do not map T1547.001. Name the visibility gap. Map the hostname/C2 hunt if that is the plan.

**Interpretation:**  
A hunts a gap to fill a tactic. B maps what the hunt is.

**Speaker Notes:**  
Force: unextracted methods are not mapped.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Heat map = map
- Invented technique to fill a tactic
- Red cell = priority
- Hunting a visibility gap
- Stopping after the copied ID
- Teaching persistence how-to (**2.6**)

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Write one ATT&CK card: map, gap, priority.

**Speaker Notes:**  
Assume extract already happened. Park STIX, persistence labs, SIEM execute. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Copy ID vs map a hunt?
2. One mapped hunt (tactic + technique + method)?
3. Detection gap vs visibility gap?
4. Why is a red heat-map tactic not enough?
5. Same technique, two hunts — what breaks the tie?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Map this hunt, not the matrix.
- Copied IDs are inputs (**2.4.2**).
- Detection gap vs visibility gap, per mapped technique.
- ATT&CK supports priority. It does not replace **2.2.2**.
- Do not invent techniques. Do not hunt gaps you cannot see.
- Next: persistence techniques (**2.6**).

**Speaker Notes:**  
Do not open 2.6 registry labs.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.6 – Persistence techniques

**Resources:**
- Student Guide for this module
- Module 2.4.2 – Extracting hunt leads
- Module 2.2.2 – Hunt development

**Speaker Notes:**  
Park technique how-to and local hunt control (2.7).

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** ATT&CK Hunt Quick Reference

**Map:** this plan / these findings → TA + T + method  

**Gap:** detection (see, no alert) · visibility (cannot see)  

**Priority:** mapped technique + scope + can run  

**Test:**  
- whole layer → not a map  
- invented ID → wrong  
- red tactic → not a reason  
- visibility gap → do not hunt  

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the ATT&CK card large enough to read
- Visually reject heat maps / invented Persistence / red-cell priority
- Consistent footer with module number
- Minimal text — let the three examples teach
