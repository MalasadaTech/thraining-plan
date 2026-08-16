# Instructor Guide – Module 3.1.6 – Tailoring Output to the Audience

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.6 A / A / B · 3.1.6.1 1a / 1a / 2b  
- Hunter: 3.1.6 A / B / B · 3.1.6.1 1a / 2b / 3c  
- CTI: 3.1.6 B / C / C · 3.1.6.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach audience analysis and force an actual **rewrite**. Do not teach 3.11 channels or markings.

**Key Teaching Points:**
- Same facts, different product.
- Keep / cut / format is the skill.
- SOC 3-level task is **1a / 1a / 2b**. CTI is **3c / 4d**. Do not collapse.
- 3.11.2.2 is the production-depth version of this skill.

**Common Student Challenges:**
- Saying “it depends” without writing the sentence.
- Sending JA3 to leadership.
- One blob for all audiences.
- Opening 3.11 dissemination.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional local audience catalog
- Answer key (this guide)

---

## Learning Objectives

1. Audience analysis.
2. Adjust content, format, detail.
3. Rewrite for a named audience.

**Mapped Items:** K 3.1.6 · T 3.1.6.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.11 / 3.1.5 rescore |
| Analysis + adjust              | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | They write four sentences |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they defend the JA3 |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they produce two usable sentences from one fact set.
- Accept paraphrase of Example 1 if keep/cut is right.

**Question:**  
“If leadership asks ‘so what do I *click*?,’ what did you fail to cut or add?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail JA3-in-the-exec-body. Fail one-blob. Accept D as technical fields.

**Summaries:**
- Ex 1: two products, same facts.
- Ex 2: facts OK, audience fail.
- Ex 3: split the memo.

**Cases:**

| Item | Keep | Cut | Format | Sentence (accept paraphrase) |
|------|------|-----|--------|------------------------------|
| A | Host, isolate + hunt, medium | Budget | Ticket line | Isolate WS-JLEE with IR concurrence; hunt SNI/JA3 this shift. |
| B | Cluster, 10-day lab→finance, IR owns victims | Exec spend para | Operational note | Run ten days on Night Owl (lab then finance); IR takes confirmed victims. |
| C | Implication + fund/defer + residual risk | JA3, hash | Short para | Fund extra TLS this quarter or accept more missed beacons like WS-JLEE. |
| D | SNI, JA3, hash, port | Isolate/budget | Technical note | `nightowl-updates.net` / JA3 `a0e9f5…` / hash `6734f374…` — detect/pivot fields. |

---

## Knowledge Check – Answer Key

1. **Four analysis questions?**  
   **Answer:** Decision they own; time they have; vocabulary they can use; what they must not have to ask next.  
   **Explanation:** Outline a.

2. **Three adjusts?**  
   **Answer:** Content, format, detail.  
   **Explanation:** Outline b.

3. **Why not JA3 to leadership?**  
   **Answer:** They cannot execute a fingerprint. They need implication + a decision.  
   **Explanation:** Example 2.

4. **Why not one memo?**  
   **Answer:** Each audience owns a different decision. One blob forces someone to mine their line.  
   **Explanation:** Example 3.

5. **Channel / marking?**  
   **Answer:** **3.11.2**, not this lesson.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local audience catalog
- Next recommended module: 3.1.7 Attribution
