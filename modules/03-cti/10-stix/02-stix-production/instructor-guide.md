# Instructor Guide – Module 3.10.2 – STIX in Intelligence Production

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.10.2 A / B / B · 3.10.2.1 1a / 1a / 2b · 3.10.2.2 1a / 1a / 2b · 3.10.2.3 1a / 1a / 2b  
- Hunter: 3.10.2 B / C / C · 3.10.2.1 2b / 3c / 4c · 3.10.2.2 2b / 3c / 4c · 3.10.2.3 2b / 3c / 4c  
- CTI: 3.10.2 B / C / C · 3.10.2.1 3c / 4c / 4d · 3.10.2.2 3c / 4c / 4d · 3.10.2.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Produce: **relationships + scenario**, **create/validate**, **TAXII** publish/consume. Classroom collection only.

**Key Teaching Points:**
- Do not re-teach the eleven-type tour. Point at the **3.10.1** card.
- SOC K is **A / B / B**. CTI **4d** on 3.10.2.1–2 (graph completeness + validation judgment). TAXII task is **4c**.
- Real `relationship_type` only. `sighting_of` is a *sighting* property, not a relationship object — if they write `sighting | sighting_of | indicator` as a *line*, accept it and say it is the sighting object, not a `relationship`.
- Do not stand up TAXII. `harbor-cti` is lesson-only.
- Do not write 3.11 prose or 2.4.3 hunt leads.

**Common Student Challenges:**
- Invented `connects-to`.
- `attributed-to` a vendor APT.
- Missing `relationship_type`.
- Email PDF = TAXII.
- Turning the scenario sentence into a full product.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Bundle for share/automation.
2. Real links + one scenario sentence.
3. Validate required fields.
4. TAXII = publish/consume a collection.

**Mapped Items:** K 3.10.2 · T 3.10.2.1 · T 3.10.2.2 · T 3.10.2.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.10.1 redo / 2.4.3 / 3.11 |
| Structure, links, validate, TAXII | 16 min | a–b + three T |
| Walkthrough Examples           | 12 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Closes 3.10 |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep the APT actor |

---

## Detailed Teaching Notes

**Talking Points:**
- 4d: they should *omit* `attributed-to`, not invent a target. That is a better graph than a fake who.
- CoA `mitigates` the attack-pattern *or* the indicator — either is fine if they name the type.
- TAXII collection ≠ TIP search box.

**Question:**  
“What object would have to exist before `attributed-to` is a *valid* link on this card?”

---

## Hands-On Exercise – Instructor Guidance

**Relationships:**

| Item | Line |
|------|------|
| A | indicator `nightowl-updates.net` **indicates** malware `update.exe` |
| B | malware **uses** attack-pattern T1059.001 |
| C | sighting WS-JLEE **sighting_of** indicator (sighting object) |

**Scenario:** one sentence walking A–C (+ optional mitigates/targets). No profile.

**Validate:**

| Item | Result |
|------|--------|
| D | **Valid** — pattern + pattern_type |
| E | **Invalid** — missing relationship_type |
| F | **Invalid** — unearned threat-actor |

**TAXII:**

| Item | Result |
|------|--------|
| G | **Publish** bundle → `harbor-cti` |
| H | **Fail** — PDF email is not TAXII |

---

## Knowledge Check – Answer Key

1. **Bundle for?**  
   **Answer:** Package objects + relationships so they can be shared and automated.  
   **Explanation:** Outline a.

2. **One real relationship_type?**  
   **Answer:** Any of `indicates`, `uses`, `mitigates`, `targets` with the Night Owl ends.  
   **Explanation:** Outline b / 3.10.2.1.

3. **Invalid?**  
   **Answer:** Missing `relationship_type`, invented type, empty pattern, unearned threat-actor.  
   **Explanation:** 3.10.2.2.

4. **TAXII vs bundle?**  
   **Answer:** Bundle = the payload. TAXII = publish/consume that payload on a collection.  
   **Explanation:** 3.10.2.3.

5. **Prose product?**  
   **Answer:** **3.11**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- STIX 2.1 relationships / TAXII 2.1 collections (lookup)
- Next recommended module: 3.11.1 Creating finished intelligence products
