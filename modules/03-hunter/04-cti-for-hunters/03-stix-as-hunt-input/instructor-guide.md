# Instructor Guide – Module 3.4.3 – STIX as Hunt Input

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.4.3 B / C / C ; 3.4.3.1 3c / 4c / 4c ; 3.4.3.2 3c / 4c / 4d  
- SOC: 3.4.3 A / A / B ; 3.4.3.1 1a / 1a / 2b ; 3.4.3.2 1a / 1a / 2b  
- CTI: 3.4.3 A / B / B ; 3.4.3.1 1a / 2b / 3c ; 3.4.3.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Identify hunt-relevant STIX objects and seed a lead. Do not author STIX.

**Context (plain language):**

- What this hour is for: Hunters read a bundle as input, not as a writing exercise.
- How it hooks to the hour before: 3.4.2 extracted leftovers from prose.
- How it hooks to the hour after: 3.5.1 maps the hunt onto ATT&CK.
- Why we are doing it this way: Short 0.x / 4.x voice. Outline a–b + two tasks. Spec is STIX 2.1 (not a hunt ID).
- What we are *not* doing this hour: Author, validate, or share STIX (**2.10**). TAXII. Navigator. No lab.
- Extra step: none.

**Key Teaching Points:**
- Actor name is not a search.
- Structured JSON ≠ hunt.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 3.4.3 ; T 3.4.3.1 ; T 3.4.3.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Read, do not author |
| Key Concepts            | 12 min    | Six objects; A12 seed |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write the six objects. Walk A12 indicator + attack-pattern → question.

If they invent a STIX type: “2.10. Real types only.”  
If they dump all IPv4 indicators: “Noise / hand-off.”

---

## Knowledge Check – Answer Key

1. **Hunters author STIX this hour. True or false?**  
   **Answer:** False. Authoring is 2.10.  
   **Explanation:** Outline b / stay-in.

2. **Four objects a hunter uses?**  
   **Answer:** Any four of: indicator, attack-pattern, observed-data, malware, threat-actor / intrusion-set, relationship.  
   **Explanation:** Outline a.

3. **A12 object + lead?**  
   **Answer:** e.g. `indicator` for `/update.exe` :8080 → search that IP + port + URI (or Run **`Updater`** `attack-pattern` → search that value).  
   **Explanation:** Tasks 1–2.

---

## Additional Instructor Resources

- Next: 3.5.1 ATT&CK for hunt planning
