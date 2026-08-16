# Module 2.4.1 – Assessing CTI for Hunting Value  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.4.1 – Assessing CTI for Hunting Value  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Ask what they would *search* from the last PDF they starred. This lesson is the gate, not the extract. Not STIX. Not ATT&CK coverage.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. Sort a report: hunt-worthy / awareness-only / hand off
2. Rapid-triage without extracting every TTP
3. Name question, telemetry, and scope
4. Triage: hunt / don’t hunt / hand off, and say why

**Mapped Items:**  
K: 2.4.1 | T: 2.4.1.1

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Push a teammate-ready label.

---

### Slide 3 – Agenda
**Title:** Agenda

- Three dispositions
- What “actionable for a hunt” means
- Rapid triage passes
- Three worked examples
- Identification practice
- Hands-on triage card
- Knowledge check

**Speaker Notes:**  
2.4.2 is extract. 2.4.3 is STIX. Stay here.

---

### Slide 4 – Not a Hunt
**Title:** Interesting Is Not a Hunt

“APT is active worldwide.”  
“Hunt ransomware.”  
“High priority CTI.”

**Key Point:** A report is not hunt-worthy until a question can fail in *your* data.

**Speaker Notes:**  
Leave the slogans up. Kill them in Example 2.

---

### Slide 5 – Three Dispositions
**Title:** Hunt / Awareness / Hand Off

| Label | Job |
|-------|-----|
| **Hunt-worthy** | Question + telemetry + scope; not already owned |
| **Awareness-only** | Context. No hunt this week |
| **Hand off** | Detections or IR own it |

**Analyst Tip:** Mixed reports **split**. Hunt this section. Hand off that pack.

**Speaker Notes:**  
One student gives a hunt-worthy reason; another gives a hand-off reason.

---

### Slide 6 – Actionable for a Hunt
**Title:** Question / Telemetry / Scope

1. **Hunt question** — what we would test  
2. **Telemetry** — which sensors could answer it  
3. **Scope** — who / where / how long  

**Key Point:** Missing one → not hunt-worthy *as written*. No DNS on that VLAN → visibility gap, not clean.

**Speaker Notes:**  
Full if/then card format is 2.2.2. Here they only owe the three names.

---

### Slide 7 – Rapid Triage
**Title:** Five Passes, Then a Why

1. Fresh and in theater?
2. Named thing or rare behavior?
3. Can we see it?
4. Already owned (SOC / IR)?
5. Hunt / don’t hunt / hand off + **one sentence why**

**Analyst Tip:** A TTP table means you left this lesson (**2.4.2**).

**Speaker Notes:**  
“High” fails pass 5.

---

### Slide 8 – Consumer, Not Producer
**Title:** Stay in This Lane

- Enrichment tools → **2.3**
- Extract TTPs / IOCs → **2.4.2**
- STIX objects → **2.4.3**
- ATT&CK coverage → **2.5**
- First search → **2.2.1**

**Key Point:** Today you only owe the gate.

**Speaker Notes:**  
Park every detour.

---

### Slide 9 – Example 1: Hunt-worthy
**Title:** Example 1 – Finance CDN Bulletin

- Question: after-hours DNS+TLS to bulletin names from finance
- Telemetry: DNS + TLS (lab has none)
- Scope: finance; 7 days; **not lab**
- **Hunt-worthy** — named hosts, data exists, no analytic, no IR

**Interpretation:**  
Assessed. Not extracted. Not executed.

**Speaker Notes:**  
Students score the card before you reveal the interpretation.

---

### Slide 10 – Example 2: Awareness
**Title:** Example 2 – Actor Slogan

**A:** APT still active worldwide. Hunt it. High.  
**B:** Awareness-only. No object, no question that can fail, no telemetry hook.

**Interpretation:**  
A is not a triage. B is the gate.

**Speaker Notes:**  
Re-triage if objects appear later. Still this skill.

---

### Slide 11 – Example 3: Split
**Title:** Example 3 – IR vs Leftover Hunt

**A:** IR has the hash. Hunt the enterprise. Dump 400 IOCs.  
**B:** Hand off Building C to IR. Hand off the blocklist to detections. Hunt-worthy only leftover finance CDN names with no analytic.

**Interpretation:**  
A re-owns an incident. B splits the report.

**Speaker Notes:**  
Force: do not hunt the open case.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Hunting every APT PDF
- “High” as the reason
- Hunting open IR
- IOC appendix = hunt
- Starting the 2.4.2 extract first

**Speaker Notes:**  
Ask for a local rejected intake. Then the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. Write one triage card: question, telemetry, scope, disposition + why.

**Speaker Notes:**  
Park TTP tables and SIEM execute blocks. Review with the Instructor Guide key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Three names before a report is actionable?
2. One reason for awareness-only?
3. One reason to hand off?
4. Named host, no DNS/TLS on that VLAN — what do you do?
5. IR owns Building C hash; finance CDN names have no analytic — what do you do?

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Gate first: hunt-worthy / awareness / hand off + why.
- Actionable = question + telemetry + scope.
- Rapid triage is a label, not an extract.
- Open IR and blocklist firehoses are not hunts.
- Extract → **2.4.2**. STIX → **2.4.3**. ATT&CK → **2.5**.

**Speaker Notes:**  
Do not open 2.4.2 extract labs.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.4.2 – Extracting hunt leads from CTI

**Resources:**
- Student Guide for this module
- Module 2.2.2 – Hunt development
- Module 2.3.1 – Online tools

**Speaker Notes:**  
Park STIX, ATT&CK, persistence.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** CTI Hunt Gate

**Hunt-worthy:** question + telemetry + scope; not owned  

**Awareness:** no testable question / no object  

**Hand off:** IR or detections already own it  

**Test:**  
- slogan only → awareness  
- “high” only → not ready  
- open incident → hand off  
- TTP table first → wrong lesson  

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the four-field triage card large enough to read
- Visually reject worldwide / high / dump-all-IOCs
- Consistent footer with module number
- Minimal text — let the three examples teach
