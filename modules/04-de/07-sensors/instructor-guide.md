# Instructor Guide – Module 4.7 – Sensor availability and performance

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.7 A / B / B ; 4.7.1 2b / 3c / 3c ; 4.7.2 2b / 3c / 3c  
- SOC: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- Hunter: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- CTI: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Sometimes DE checks whether sensors are up and seeing the right place. A down sensor is not “no threat.” Not vendor admin.

**Context (plain language):**

- What this hour is for: When a rule never fires, DE sometimes asks whether the sensor was up and looking at the right place. Check the rule, the sensor, or both. A dead sensor is not proof nothing happened.
- How it hooks to the hour before: 4.6 used “sensor gone” as a retire reason. This hour is that check.
- How it hooks to the hour after: 4.8 is local policy — obtain the list and the path. Do not invent either.
- Why we are doing it this way: This unit is lighter on purpose. Sometimes DE. Not a vendor-admin or architecture course.
- What we are *not* doing this hour: Logging into MDE to configure it. Sizing Zeek. Writing a rule (1.3). Lifecycle calls (4.6). No lab. No DYA tickets.
- Extra step: none.

Say **sensor**, **dead**, **blind**, and **never fired** the way the student guide does. **MDE**, **Zeek**, and **IDS** are examples of place, not a tool class.

**Key Teaching Points:**
- Sometimes DE. Not always. Not vendor admin.
- Dead or blind ≠ no threat.
- “Never fired” → rule, sensor, or both.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Items:** K 4.7 ; T 4.7.1 ; T 4.7.2

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After 4.6 sensor-gone |
| Key Concepts            | 10 min    | Up and seeing; never fired |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Write: sometimes DE; MDE / Zeek / IDS as examples; dead ≠ no threat; never fired → rule, sensor, or both.

If they start configuring a sensor: “Not this course.”  
If they say “sensor down, so nothing happened”: “Reject.”  
If they invent a ticket: “Check, not the ticket.”

---

## Knowledge Check – Answer Key

1. **Down sensor means no activity. True or false?**  
   **Answer:** False. A dead or blind sensor is not “no threat.”  
   **Explanation:** Outline b and 4.7.1 task 2.

2. **“The rule never fired.” What two things might you check?**  
   **Answer:** The rule, the sensor, or both.  
   **Explanation:** 4.7.1 task 1.

3. **Three example kinds of sensor?**  
   **Answer:** MDE, Zeek, IDS.  
   **Explanation:** Outline a.

---

## Additional Instructor Resources

- Next: 4.8 Site-specific DE knowledge
