# Module 2.4.3 – STIX as Hunt Input  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.4.3 – STIX as Hunt Input  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Assume 2.4.1 already said hunt-worthy. This lesson is identify objects, then turn them into leads. Not authoring. Not Navigator.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Name the STIX objects a hunter actually uses
2. Tell hunt-relevant vs context vs drop
3. Explain how a bundle seeds a hunt
4. Identify objects, then turn them into hunt leads

**Mapped Items:**  
K: 2.4.3 | T: 2.4.3.1–2.4.3.2

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Identify tops at 4c. Convert can reach 4d.

---

### Slide 3 – Agenda
**Title:** Agenda

- Six objects a hunter uses
- Hunt-relevant vs context
- How a bundle seeds a hunt
- Three worked examples
- Identification practice
- Hands-on seed card
- Knowledge check

**Speaker Notes:**  
2.4.2 was extract from prose. 2.5 is ATT&CK mapping. 3.10 is authoring. Stay here.

---

### Slide 4 – Not a Seed
**Title:** JSON Is Not the Hunt

“All 400 indicators.”  
“Every 2019 hash.”  
“Hunt the intrusion-set.”  
“I’ll add T1547.001 so the bundle is complete.”

**Key Point:** A bundle seeds a hunt only after keep / drop / question.

**Speaker Notes:**  
Leave the slogans up. Kill them in Examples 2 and 3.

---

### Slide 5 – Six Objects
**Title:** Objects a Hunter Uses

| Object | Hunt job |
|--------|----------|
| **indicator** | Named pattern you can query |
| **attack-pattern** | Method (copy printed ATT&CK) |
| **observed-data** | Sample of what was seen |
| **malware** | Sample / hash — not the family slogan |
| **threat-actor / intrusion-set** | Who — scope, not a search |
| **relationship** | Which leftovers belong together |

**Analyst Tip:** Campaign, CoA, identity, sighting — out of scope.

**Speaker Notes:**  
Sort one object from the class table live.

---

### Slide 6 – Hunt-Relevant
**Title:** Hunt-Relevant vs Drop

**Keep looking:** current indicator, specific method, queryable sample  

**Drop:** expired, blocked firehose, slogan TTP, no telemetry  

**Context only:** actor name with no linked artifact  

**Key Point:** Valid STIX ≠ hunt-suitable. Reuse the **2.4.2** drop list.

**Speaker Notes:**  
Force: no registry logs → drop Run-key attack-pattern.

---

### Slide 7 – Seed, Do Not Author
**Title:** How a Bundle Seeds a Hunt

1. Gate already passed (**2.4.1**)  
2. Identify hunt-relevant objects (**2.4.3.1**)  
3. Drop no-telemetry / expired / noise (**2.4.2**)  
4. Turn leftovers into a question (**2.4.3.2**)  

**Do not:** write STIX (**3.10**) · open Navigator (**2.5**) · execute (**2.2.1**)

**Speaker Notes:**  
SOC/CTI convert is 1a / 1a / 2b — recognize a usable seed.

---

### Slide 8 – ATT&CK in This Lesson
**Title:** Copy, Do Not Map

- Object already has an ID → write it next to the lead  
- Object has none → write **none given**  
- Do not invent IDs to complete the bundle  
- Do not author a missing `indicator`

**Analyst Tip:** Recording ≠ coverage analysis (**2.5**).

**Speaker Notes:**  
Invented T1547.001 is the Example 3 trap.

---

### Slide 9 – Example 1: Complete Seed
**Title:** Example 1 – Finance Bundle

- Identified: CDN + hash indicators, HTTPS C2 pattern, `uses`
- Recorded: **T1071.001** as printed
- Dropped: task aside; actor as search; lab (no DNS)
- Question: finance after-hours DNS+TLS to those names

**Interpretation:**  
Seeded. Not authored. Not mapped. Not executed.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: Firehose
**Title:** Example 2 – Indicators vs Leftovers

**A:** 400 IPv4 indicators + 2019 hashes + hunt the intrusion-set.  
**B:** Two current domains + parent/script. Drop expired and noise. Question on process-create.

**Interpretation:**  
A is not a seed. B is identify → drop → lead.

**Speaker Notes:**  
Same firehose family as 2.4.2 Example 2.

---

### Slide 11 – Example 3: Gap + Invented ID
**Title:** Example 3 – Run Keys

**A:** No registry logs. Invent T1547.001. Hunt persistence.  
**B:** Drop Run-key objects (visibility gap). Do not invent the ID. Keep the hostname indicator. DNS/TLS question.

**Interpretation:**  
A hunts a gap. B turns one leftover object into a lead.

**Speaker Notes:**  
Force: unprinted IDs are not recorded. Missing objects are not authored.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Indicator list = hunt
- Actor / intrusion-set as the search
- Slogan attack-pattern kept
- Invented ATT&CK or invented objects
- Extracting a visibility gap
- Re-doing the 2.4.1 gate

**Speaker Notes:**  
Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 14–16 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Write one seed card: objects identified, dropped, leads, question.

**Speaker Notes:**  
Assume hunt-worthy. Park TAXII, authoring, Navigator, SIEM execute. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Three hunter STIX objects — what is each for?
2. When is an indicator hunt-relevant vs drop?
3. Printed T1071.001 — what do you do with the ID here?
4. Run-key attack-pattern, no registry logging — identify, then what?
5. One hunt question two leftover domain indicators could support?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Six objects a hunter uses. Not every STIX type.
- Hunt-relevant after the **2.4.2** drop list.
- Identify, then turn leftovers into a question that can fail.
- Copy printed ATT&CK IDs. Do not map (**2.5**).
- Do not author STIX (**3.10**).
- Next: ATT&CK for hunt planning (**2.5**).

**Speaker Notes:**  
Do not open 2.5 Navigator labs.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.5 – Using MITRE ATT&CK for hunt planning

**Resources:**
- Student Guide for this module
- Module 2.4.2 – Extracting hunt leads
- Module 2.4.1 – Assessing CTI

**Speaker Notes:**  
Park STIX authoring (CTI 3.10) and ATT&CK coverage.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** STIX Input Quick Reference

**Use:** indicator · attack-pattern · observed-data · malware · actor / intrusion-set · relationship  

**Identify:** hunt-relevant / context / drop  

**Seed:** leftovers → one if/then that can fail  

**Test:**  
- whole indicator list → not a seed  
- actor name as search → not a lead  
- slogan attack-pattern → drop  
- invented ID or invented object → wrong lesson  

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the six-object table large enough to read
- Visually reject indicator firehose / actor-as-search / invented IDs
- Consistent footer with module number
- Minimal text — let the three examples teach
