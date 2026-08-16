# Module 3.1.5 – Ensuring Intelligence Is Actionable

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.5 A / A / B · 3.1.5.1 1a / 1a / 1a  
- Hunter: 3.1.5 A / B / B · 3.1.5.1 1a / 2b / 3c  
- CTI: 3.1.5 B / C / C · 3.1.5.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Name the **characteristics** of actionable intelligence.
2. Name **common reasons** a product fails that test.
3. **Evaluate** a piece and **explain why** it is or is not actionable.

**Mapped Proficiency Items:**
- K: 3.1.5 – Ensuring intelligence is actionable
- T: 3.1.5.1 – Evaluate whether a piece of intelligence is actionable and explain why

---

## 1. Key Concepts

You already have a **requirement** (**3.1.4**). This hour is whether the *product* lets someone **act** on that requirement. Hunt “actionable for a hunt” is **2.4.1** — a different test. Audience rewrite is **3.1.6**.

**Classroom actionable test (this lesson only):**

| Check | Pass looks like |
|-------|-----------------|
| **1. Answers the named requirement** | The question from 3.1.4 is actually answered |
| **2. Who acts** | A role or team is named |
| **3. What they do** | A specific next action, not “be aware” |
| **4. Timely** | Still inside the decision window |
| **5. Confidence / caveat** | How sure you are, and what would change the call |

Fail any check → **not actionable** (or say *which* check failed). “Interesting” is not a pass.

**Common failures (outline b):**

| Failure | Looks like |
|---------|------------|
| No requirement | Product exists; nobody asked a decision question |
| No “so what” | Facts only (3.1.1 information shipped as intel) |
| No owner / no action | “Leadership should consider improving security” |
| Too late | After the window in the PIR |
| Wrong consumer | CEO gets a JA3 (also **3.1.6** — here you still fail *actionable for that audience*) |
| IOC list only | Hashes with no judged action |

| This lesson | Other |
|-------------|-------|
| Evaluate the product | Write the PIR — **3.1.4** |
| Not rewrite for a second audience | **3.1.6** |
| Not hunt-lead extract | **2.4.1** / **2.4.2** |
| Not finished-product format | **3.11** |

The task is **pass/fail + which check + why**, not “define actionable.”

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Isolate WS-JLEE with IR concurrence, medium confidence | Hash dump titled INTEL |
| Names SOC + action + window | “We should do better” |
| Flags a late product as fail-on-timely | Calling a blog headline intelligence |

---

## 2. Detailed Walkthrough / Examples

**Requirement in play:** SOC lead | Night Owl on Harbor hosts **this week**? | if yes → Sev2 path (**1.8.5**)

### Example 1: Actionable Tactical Note (Expected)

> We assess **WS-JLEE** is likely Night Owl (medium). **SOC / IR:** isolate with IR concurrence tonight; hunt `nightowl-updates.net` / JA3 `a0e9f5…` this shift.

**Evaluate:** Passes 1–5. Requirement answered, who, what, now, confidence.  
**Actionable.**

### Example 2: INTEL Slide of Hashes (Lead)

> INTEL: `203.0.113.88`, `nightowl-updates.net`, `6734f374…`. Source: blog today.

**Evaluate:** Fails 1 (does not say *we* are hit), 2–3 (no who/what), 5 (no confidence).  
**Not actionable.** Still **information / data** (**3.1.1**).  
**Lead:** Adding the word INTEL does not pass the test.

### Example 3: Late Strategic Line (Lead)

> We assess extra TLS sensors would have reduced Night Owl risk. (PIR window was “this quarter”; the budget lock was last Friday.)

**Evaluate:** Might pass 1–3 and 5. **Fails 4 (timely).**  
**Not actionable** for *that* decision. A new PIR could restart the clock.  
**Lead:** Correct judgment, dead window.

---

## 3. Hands-On Exercise

**Objective:** Score the five checks and explain the fail.

**Use the classroom test.** Requirement = Night Owl presence **this week** unless stated.

**Instructions:**

1. One sentence each for Examples 1–3: pass/fail + which check.
2. For each item, write **actionable? / failed checks / why**.

   - A. “Hunt lead: spend the next ten days on Night Owl in lab then finance; IR owns victims.” (Requirement was *operational* hunt-time.)
   - B. “Nation-state APT — be aware.” No hosts, no window.
   - C. Example 1 text, but it is now **day 12** and the PIR was seven days.
   - D. Same facts as Example 1, sent only as a JA3 to the **CEO**.

3. Do not rewrite D for leadership (**3.1.6**). You may *say* it fails actionable *for that consumer*.
4. Do not draft a 3.11 product.

**Expected Outcome:**
- Three example summaries
- Four evaluate lines
- No audience rewrite, no PIR rewrite unless a check requires naming the missing requirement

---

## 4. Knowledge Check

1. Name the five classroom **checks**.
2. Give one **failure mode** from outline b and what it looks like.
3. Why is a hash list titled INTEL not actionable?
4. Can a correct judgment still fail? How?
5. How is this test different from **2.4.1** (hunt-actionable CTI)?

---

## 5. Summary

- Five checks. Fail any → explain which.
- Next: tailor the *same* intelligence to a specified audience (**3.1.6**).

---

## 6. References & Further Reading

- Related modules:
  - 3.1.4 – Intelligence requirements (previous)
  - 3.1.6 – Tailoring output to the audience (next)
  - 2.4.1 – Assessing CTI for hunting value
  - 3.11.1 – Finished intelligence products
- Local product quality card (optional — substitutes the five checks)
