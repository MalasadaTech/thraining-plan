# Instructor Guide – Module 2.10.2 – STIX in Intelligence Production

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.10.2 B / C / C ; 2.10.2.1 3c / 4c / 4d ; 2.10.2.2 3c / 4c / 4d ; 2.10.2.3 3c / 4c / 4c  
- Hunter: 2.10.2 B / C / C ; 2.10.2.1 2b / 3c / 4c ; 2.10.2.2 2b / 3c / 4c ; 2.10.2.3 2b / 3c / 4c  
- SOC: 2.10.2 A / B / B ; 2.10.2.1 1a / 1a / 2b ; 2.10.2.2 1a / 1a / 2b ; 2.10.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Link objects with real relationship types. Validate a classroom object. Consume TAXII — do not stand up a server.

**Context (plain language):**

- What this hour is for: CTI analysts connect objects so the story is reusable.
- How it hooks to the hour before: 2.10.1 named the objects.
- How it hooks to the hour after: 2.11.1 is the narrative product.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b plus create/validate and TAXII consume. No server.
- What we are *not* doing this hour: Invented types. Lumped 2.10.3. Live TAXII. No lab.
- Extra step: none.

**Key Teaching Points:**
- Real relationship types only.
- TAXII = pull a collection.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 2.10.2 ; T 2.10.2.1 ; T 2.10.2.2 ; T 2.10.2.3

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Links, not a server |
| Key Concepts            | 12 min    | A12 relationships; TAXII consume |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write real relationship types. Walk sighting-of / indicates. Fail invented types and “I built TAXII.”

---

## Knowledge Check – Answer Key

1. **Stand up TAXII this hour. True or false?**  
   **Answer:** False. Consume a collection.  
   **Explanation:** Stay-in / task 3.

2. **Two relationship types?**  
   **Answer:** Any two: indicates, based-on, targets, uses, related-to, sighting-of.  
   **Explanation:** Outline b.

3. **Hash to WS-JLEE?**  
   **Answer:** Sighting of the Indicator on Identity WS-JLEE (or indicates + related-to). Real type only.  
   **Explanation:** Task 1.

---

## Additional Instructor Resources

- Next: 2.11.1 Finished intelligence products
