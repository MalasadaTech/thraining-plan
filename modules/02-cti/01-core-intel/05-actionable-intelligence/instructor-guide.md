# Instructor Guide – Module 3.1.5 – Ensuring Intelligence Is Actionable

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.1.5 A / A / B · 3.1.5.1 1a / 1a / 1a  
- Hunter: 3.1.5 A / B / B · 3.1.5.1 1a / 2b / 3c  
- CTI: 3.1.5 B / C / C · 3.1.5.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the characteristics and failure modes. Force **evaluate + which check + why**. Do not rewrite for a second audience.

**Key Teaching Points:**
- Five-check card is a stand-in. Overlay a site quality card if you have one.
- “Interesting” is not a pass.
- Late + correct still fails timely.
- Hunter 3-level task is **1a**. CTI is **3c / 4d**. Do not collapse.
- 2.4.1 is “can a hunter start a hunt?” — not this card.

**Common Student Challenges:**
- Defining actionable and never scoring a product.
- Passing a hash dump because it is “technical intel.”
- Opening 3.1.6 on D instead of scoring it.
- Confusing this with 2.4.1.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site quality card
- Answer key (this guide)

---

## Learning Objectives

1. Characteristics.
2. Failure modes.
3. Evaluate + explain.

**Mapped Items:** K 3.1.5 · T 3.1.5.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.1.6 / 2.4.1 / 3.11 |
| Checks + failures              | 16 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~64 min** | Stretch Ex 2 if they pass the slide |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — score a real-looking product, do not recite adjectives.
- Reuse 3.1.1: information shipped as intel is the usual fail-on-so-what.

**Question:**  
“If every check passes except the audience, is that a 3.1.5 fail or only a 3.1.6 fail?” (Both. Here you fail actionable *for that consumer*. 3.1.6 is how you fix it.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail hash-as-intel. Fail “be aware.” Accept A if the requirement was operational.

**Summaries:**
- Ex 1: pass.
- Ex 2: fail 1, 2–3, 5.
- Ex 3: fail timely.

**Cases:**

| Item | Call |
|------|------|
| A | **Actionable** for an *operational* hunt-time PIR: who (hunt/IR), what (10-day series), window, implied confidence. |
| B | **Not.** Fails 1–5. Awareness slogan. |
| C | **Not** for the 7-day PIR. Fails **timely**. Content would have passed last week. |
| D | **Not** for the CEO. Fails who/what *they* can do (and 3.1.6). Do not accept “but SOC could use it.” Score the product *as shipped*. |

---

## Knowledge Check – Answer Key

1. **Five checks?**  
   **Answer:** Answers the requirement; who acts; what they do; timely; confidence/caveat.  
   **Explanation:** Outline a.

2. **One failure mode?**  
   **Answer:** Any of: no requirement, no so-what, no owner/action, too late, wrong consumer, IOC-only.  
   **Explanation:** Outline b.

3. **Why not the hash list?**  
   **Answer:** Does not answer *our* presence, names no actor or action, no confidence.  
   **Explanation:** Example 2.

4. **Correct but fail?**  
   **Answer:** Yes — **timely** (Example 3) or **wrong consumer** (D).  
   **Explanation:** Task.

5. **Vs 2.4.1?**  
   **Answer:** 2.4.1 is whether a hunter can start a hunt from CTI. This card is whether *this product* lets the *named consumer* act on *this PIR*.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Site product quality card
- Next recommended module: 3.1.6 Tailoring output to the audience
