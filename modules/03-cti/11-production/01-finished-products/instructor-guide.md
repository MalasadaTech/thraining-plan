# Instructor Guide – Module 3.11.1 – Creating Finished Intelligence Products

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.11.1 A / A / B · 3.11.1.1 1a / 1a / 2b · 3.11.1.2 1a / 1a / 1a  
- Hunter: 3.11.1 A / B / B · 3.11.1.1 1a / 2b / 3c · 3.11.1.2 1a / 2b / 3c  
- CTI: 3.11.1 B / C / C · 3.11.1.1 3c / 4c / 4d · 3.11.1.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Draft and evaluate a finished *prose* product, then produce an **honest Night Owl profile**. Empty who is success.

**Key Teaching Points:**
- SOC K is **A / A / B**. SOC 3.11.1.2 is **1a / 1a / 1a** — they *recognize* a profile, they do not author one at 3-level. Do not collapse.
- CTI **4d** is the quality judgment and the unattributed profile, not a longer essay.
- Do not re-teach 3.1.6 rewrite or 3.1.7 confidence scale. Use them.
- Classroom types only. If the site has other names, swap the *labels*, keep structure + quality.
- Do not open 3.11.2 markings.

**Common Student Challenges:**
- Shipping the vendor PDF.
- Nation-state in the profile.
- Assessment with no gaps.
- Writing a STIX bundle or a SOC incident ticket.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Types + structure + quality.
2. Draft and evaluate.
3. Honest actor profile.

**Mapped Items:** K 3.11.1 · T 3.11.1.1 · T 3.11.1.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.1.6 / 3.10 / 3.11.2 |
| Types, structure, quality, profile | 16 min | a–c + 3.11.1.2 |
| Walkthrough Examples           | 12 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep T1486 |

---

## Detailed Teaching Notes

**Talking Points:**
- Activity note vs profile: one window vs durable picture. Both can have empty who.
- 4d: they should *remove* T1486 and the APT name, not add a confidence adjective on top.
- SOC 3-level: they can say “this draft fails who/T1486/certainty.” They need not write the profile.

**Question:**  
“What would have to appear before the profile’s **who** section is allowed to name a group?”

---

## Hands-On Exercise – Instructor Guidance

**Draft:** Activity note or assessment. BLUF = Harbor events + unattributed. Action = block/hunt. No T1486.

**Eval (Ex 2):**

| Standard | Result |
|----------|--------|
| Who | **Fail** — nation-state unearned |
| T1486 | **Fail** — not observed |
| Certainty | **Fail** — “will” |

**Profile:** TTPs = four supported IDs. Infra = two names + IP. Who = empty/low. Gaps = no encrypt, no identity.

---

## Knowledge Check – Answer Key

1. **Two types + a not?**  
   **Answer:** Any two of activity note / assessment / actor profile / defensive note. Profile is not for a single unattributed window if you only need a note; activity note is not a who-essay.  
   **Explanation:** Outline a.

2. **Draft line besides BLUF?**  
   **Answer:** Type, one gap, one action.  
   **Explanation:** Structure / task.

3. **One Ex 2 fail?**  
   **Answer:** Unearned who, uncited T1486, or banned certainty.  
   **Explanation:** Quality / Example 2.

4. **Who section?**  
   **Answer:** Unattributed / empty / low. Not “Night Owl APT nation-state.”  
   **Explanation:** 3.11.1.2.

5. **Channel and marking?**  
   **Answer:** **3.11.2**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Next recommended module: 3.11.2 Dissemination
