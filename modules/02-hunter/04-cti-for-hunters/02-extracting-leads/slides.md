# Module 2.4.2 – Extracting Hunt Leads from CTI  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.4.2 – Extracting Hunt Leads from CTI  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Assume 2.4.1 already said hunt-worthy. This lesson is keep / drop / question. Not STIX. Not Navigator.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Tell which TTPs, IOCs, and behaviors can drive a hunt
2. Drop no-telemetry, expired, and noise
3. Record ATT&CK IDs the report already printed
4. Extract leads and state the hunt question they support

**Mapped Items:**  
K: 2.4.2 | T: 2.4.2.1–2.4.2.3

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Push a short extract.

---

### Slide 3 – Agenda
**Title:** Agenda

- TTP vs IOC vs behavior
- What to drop
- Recording ATT&CK IDs
- Three worked examples
- Identification practice
- Hands-on extract card
- Knowledge check

**Speaker Notes:**  
2.4.1 was the gate. 2.4.3 is STIX. Stay here.

---

### Slide 4 – Not Extract
**Title:** The Annex Is Not the Hunt

“All 400 IPs.”  
“Every 2019 hash.”  
“Persistence.”  
“Hunt ransomware.”

**Key Point:** Copying the appendix is not extract.

**Speaker Notes:**  
Leave the slogans up. Kill them in Example 2.

---

### Slide 5 – Three Kinds
**Title:** TTP / IOC / Behavior

| Kind | Hunt when |
|------|-----------|
| **TTP** | Specific method + you can see that method |
| **IOC** | Current named object you can query |
| **Behavior** | Scoped or off-baseline — not daily work |

**Analyst Tip:** Same bar as unique patterns in **2.2.2**.

**Speaker Notes:**  
Sort one object from the class bulletin live.

---

### Slide 6 – Drop
**Title:** What to Drop

1. **No telemetry** — visibility gap, not a lead  
2. **Expired IOC** — old annex, no “still in use”  
3. **Noise** — blocked firehose, slogan TTP, whole CDN ASN  

**Key Point:** If leftovers cannot form a question, re-drop.

**Speaker Notes:**  
Force: no registry logs → drop Run keys.

---

### Slide 7 – ATT&CK in This Lesson
**Title:** Copy, Do Not Map

- Report prints an ID → write it next to the lead  
- Report prints none → write **none given**  
- Do not invent IDs  
- Do not open Navigator (**2.5**)

**Analyst Tip:** Recording ≠ coverage analysis.

**Speaker Notes:**  
Invented T1547.001 is the Example 3 trap.

---

### Slide 8 – Hunt Question
**Title:** What the Leads Support

One if/then the leftovers can test.

**Good:** If finance follows those CDN names after hours, we should see repeated DNS+TLS.  
**Not a question:** Hunt ransomware.

**Key Point:** Full four-field card is **2.2.2**. Here you owe the question.

**Speaker Notes:**  
SOC/CTI 2.4.2.3 is 1a / 1a / 2b — recognize a usable question.

---

### Slide 9 – Example 1: Complete Extract
**Title:** Example 1 – Bulletin Slice

- Kept: CDN C2 procedure, hash, after-hours DNS+TLS  
- Recorded: **T1071.001** as printed  
- Dropped: “scheduled tasks” aside; lab (no DNS)  
- Question: finance after-hours DNS+TLS to those names

**Interpretation:**  
Extracted. Not mapped. Not executed.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: Firehose
**Title:** Example 2 – Annex vs Leftovers

**A:** 400 IPs + 2019 hashes + “persistence.”  
**B:** Two current names + parent/script. Drop expired and noise. Question on process-create.

**Interpretation:**  
A is not extract. B is keep / drop / question.

**Speaker Notes:**  
Same firehose family as 2.4.1 Example 3 write-up A.

---

### Slide 11 – Example 3: Gap + Invented ID
**Title:** Example 3 – Run Keys

**A:** No registry logs. Invent T1547.001. Hunt persistence.  
**B:** Drop Run keys (visibility gap). Do not invent the ID. Keep the hostname. DNS/TLS question.

**Interpretation:**  
A hunts a gap. B extracts what can fail.

**Speaker Notes:**  
Force: unprinted IDs are not recorded.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Annex = extract
- Slogan TTP kept
- Invented ATT&CK
- Extracting a visibility gap
- “Hunt ransomware” as the question
- Re-doing the 2.4.1 gate

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Write one extract card: kept TTPs, kept artifacts, dropped, question.

**Speaker Notes:**  
Assume hunt-worthy. Park STIX, Navigator, SIEM execute. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. When can a TTP vs IOC vs behavior drive a hunt?
2. One reason to drop?
3. Printed T1053.005 — what do you do with the ID here?
4. Run-key TTP, no registry logging — keep or drop?
5. One hunt question two leftover CDN names could support?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Extract the hunt-worthy slice only.
- TTP / IOC / behavior — searchable or drop.
- Drop gaps, expired IOCs, and noise.
- Copy printed ATT&CK IDs. Do not map (**2.5**).
- Leftovers must support a question that can fail.
- Next: STIX as hunt input (**2.4.3**).

**Speaker Notes:**  
Do not open 2.4.3 bundle labs.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.4.3 – STIX as hunt input

**Resources:**
- Student Guide for this module
- Module 2.4.1 – Assessing CTI
- Module 2.2.2 – Hunt development

**Speaker Notes:**  
Park STIX authoring (CTI 3.10) and ATT&CK coverage.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Extract Quick Reference

**Keep:** specific method / current object / off-baseline behavior  

**Drop:** no telemetry · expired · noise  

**ATT&CK:** copy if printed · else none given  

**Question:** one if/then the leftovers can fail  

**Test:**  
- whole annex → not extract  
- slogan TTP → drop  
- invented ID → wrong lesson  
- “hunt ransomware” → not a question  

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the four-row extract card large enough to read
- Visually reject annex / persistence / invented IDs
- Consistent footer with module number
- Minimal text — let the three examples teach
