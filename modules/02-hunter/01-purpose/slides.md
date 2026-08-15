# Module 2.1 – Purpose of Threat Hunting  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.1 – Purpose of Threat Hunting  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Ask “what is hunt for?” and write answers on the board. This module is purpose and missed-activity examples. Not technique catalogs. Not hunt types.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

By the end of this module, you will be able to:

1. State hunt’s purpose in the security program
2. Explain how hunt finds activity existing mechanisms missed
3. Distinguish detection gaps from visibility gaps
4. Identify examples of activity controls might miss

**Mapped Items:**  
K: 2.1.1 | T: 2.1.1.1 | T: 2.1.1.2

**Speaker Notes:**  
Hunter 3 is already at principles (B / 3c). Push a program-level explanation, not a slogan.

---

### Slide 3 – Agenda
**Title:** Agenda

- Purpose in the security program
- Missed activity and two kinds of gap
- Three worked examples
- Identification practice
- Hands-on exercise
- Knowledge check

**Speaker Notes:**  
Quick roadmap. Persistence/privesc and hunt types are later.

---

### Slide 4 – Purpose
**Title:** Why Hunt Exists

Find malicious or suspicious activity that **existing security mechanisms did not surface** — and name the **gap**.

**Key Point:** If the only input is the alert queue, you are doing SOC work.

**Speaker Notes:**  
Leave this sentence up. Two clauses: activity + gap.

---

### Slide 5 – Three Seats
**Title:** Hunt in the Security Program

| Seat | Paid to do | Starts from |
|------|------------|-------------|
| SOC | Work what the stack raised | Alert / ticket |
| CTI | Judged answer to a question | Requirement / lead |
| Hunt | What the stack did *not* raise | Hypothesis, intel lead, known blind spot |

**Analyst Tip:** A lead is not an incident. A quiet hunt can still return a gap.

**Speaker Notes:**  
SOC and CTI in the room should be able to say their seat vs hunt’s.

---

### Slide 6 – Two Gaps
**Title:** Detection Gap vs Visibility Gap

| Gap | What is true | Hunt output |
|-----|----------------|-------------|
| **Detection** | Telemetry exists; no useful alert | Show the missed pattern |
| **Visibility** | Telemetry missing or unqueryable | Name the hole; do not claim “clean” |

**Key Point:** “No hits” is not “clean” if you could not see.

**Speaker Notes:**  
Stay here until someone can give both definitions without the table.

---

### Slide 7 – What Controls Miss
**Title:** Activity Existing Mechanisms Might Miss

Examples (classes only — how to hunt them is later):

- Long-running outbound sessions that never match a signature
- Lookalike DNS/TLS with no analytic
- Hosts or VLANs excluded from EDR
- Time windows outside retention you thought you had
- Living-off-the-land activity that looks like admin work

**Analyst Tip:** Prevention + a SOC ticket means the mechanism *worked*. That is not a hunt miss.

**Speaker Notes:**  
Do not open the persistence catalog. Point at 2.2 if they go there.

---

### Slide 8 – Sorting Habit
**Title:** Place the Work

1. Did an existing mechanism already raise this? → **SOC**, not hunt
2. Can you show the events, but nothing alerted? → **Detection gap**
3. Can you not see the host / net / window? → **Visibility gap**
4. Did you only relabel the queue? → **Not hunting**

**Speaker Notes:**  
This replaces the network-log `uid` pivot from the Zeek modules. Same idea: a repeatable habit.

---

### Slide 9 – Example 1: Missed Beacon
**Title:** Example 1 – Green Queue, 14-Day Beacon

- Finance VLAN, names from this week’s report
- DNS + TLS in the SIEM for 14 nights
- No ticket, no EDR block, no detection name

**Interpretation:**  
Hunting. Missed **activity** + **detection gap**. Hand SOC/IR the lead *and* the gap.

**Speaker Notes:**  
Ask students to label it before you reveal the interpretation.

---

### Slide 10 – Example 2: Queue Labeled “Hunt”
**Title:** Example 2 – “Morning Hunt: Re-pull High EDR Alerts”

- Last night’s High queue
- Mark TP/FP, close tickets
- Status: hunt complete

**Interpretation:**  
**SOC triage.** Already raised. No missed activity, no gap. The title is the trap.

**Speaker Notes:**  
Same label-vs-job trap as the CTI “INTEL” paste.

---

### Slide 11 – Example 3: Blind Lab
**Title:** Example 3 – Two Write-ups of Lab

**A:** Zero EDR hits. Lab is clean.  
**B:** Lab excluded from EDR; no DNS. Finding is a **visibility gap**. Building C (visible) had no matching names.

**Interpretation:**  
A claims clean without sight. B fulfills the purpose.

**Speaker Notes:**  
Force the sentence: you cannot claim clean where you cannot see.

---

### Slide 12 – Common Mistakes
**Title:** Common Mistakes

- Hunt = extra triage
- “No hits” on a segment with no sensor
- Finding a host and skipping the gap
- Calling a blocked hash a hunt win
- Teaching yourself persistence methods instead of stating purpose

**Speaker Notes:**  
Ask for a local example. Then move to the exercise.

---

### Slide 13 – Hands-On Exercise
**Title:** Hands-On Exercise

**Time:** 12–15 minutes

1. One-sentence summary of each example.
2. Identify the six items in the student guide (reason each).
3. In four sentences or fewer, explain hunt’s purpose to a SOC lead who thinks hunt is extra triage.

**Speaker Notes:**  
Let students work. Then review using the Instructor Guide answer key.

---

### Slide 14 – Knowledge Check
**Title:** Knowledge Check

1. Purpose of threat hunting in the program?
2. Detection gap vs visibility gap?
3. Why is re-working last night’s queue not hunting?
4. Identify the 14-day SIEM beacon with no alert.
5. Identify “zero EDR hits” on an EDR-excluded VLAN.

**Speaker Notes:**  
Run through answers interactively.

---

### Slide 15 – Summary
**Title:** Key Takeaways

- Hunt finds what existing mechanisms did not surface.
- Name the gap: detection (data, no alert) or visibility (no data).
- SOC works the queue. Hunt works what the queue never saw.
- A lead is not an incident. “No hits” is not “clean.”
- Relabeling triage does not fulfill the purpose.

**Speaker Notes:**  
Reinforce once. Do not open 2.2 techniques.

---

### Slide 16 – Questions & Next Steps
**Title:** Questions & Next Steps

**Questions?**

**Coming Next:**
- Module 2.2 – Attacker techniques

**Resources:**
- Student Guide for this module
- Local hunt charter (when published)

**Speaker Notes:**  
Park persistence, privesc, and hunt-type questions for later units.

---

### Slide 17 – (Optional) Quick Reference Card
**Title:** Purpose of Hunt Quick Reference

**Purpose:** missed activity + the gap that allowed it

**Test:**
- already alerted → SOC
- events exist, no alert → detection gap
- cannot see → visibility gap
- queue with a new title → not hunting

**Core habit:**  
Say what you found **and** what the stack could not do.

**Speaker Notes:**  
Leave this up as a reference or print it.

---

## Design Notes for Slide Builder

- Keep the SOC / Hunt / CTI table large enough to read
- Visually separate detection gap vs visibility gap
- Consistent footer with module number
- Minimal text — let the three examples teach
