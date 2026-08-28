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

- What this lesson is for: Detections only fire on what a sensor actually saw. When a rule never fires, DE sometimes asks whether the sensor was up and looking at the right place. Check the rule, the sensor, or both. A dead sensor is not proof nothing happened.
- How it hooks to the lesson before: 4.6 used “sensor gone” as a retire reason. This lesson is the check itself.
- How it hooks to the lesson after: 4.8 is local policy — obtain the list and the path. Do not invent either.
- Why we are doing it this way: This unit is lighter on purpose. Sometimes DE. Not a vendor-admin or architecture course.
- What we are *not* doing in this lesson: Logging into MDE to configure it. Sizing Zeek. Writing a rule (1.3). Lifecycle calls (4.6). No lab. No DYA tickets. No invented site architecture.
- Extra step: none.

Use the same names as the student guide: **sensor**, **dead**, **blind**, and **never fired**. **MDE**, **Zeek**, and **IDS** are examples of place, not a tool class. **Dead** means down or not sending. **Blind** means up but not looking at that host or path.

**Key Teaching Points:**
- Sometimes DE. Not always. Not vendor admin.
- Dead or blind is not “no threat.”
- “Never fired” means check the rule, the sensor, or both.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 4.7 – Sensor availability and performance
- T: 4.7.1 – Given “the rule never fired,” check the rule, the sensor, or both
- T: 4.7.2 – Reject treating a down sensor as proof the activity did not happen

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Sensor check, not vendor admin |
| Key Concepts            | 10 min    | Up and seeing; never fired |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: detections only fire on what a sensor saw. When a rule never fires, DE sometimes has to ask whether that collector was up and seeing the right place.
- Name MDE, Zeek, and IDS as examples of place. Stop there. Do not log into the box or draw a site diagram.
- A dead sensor is down or not sending. A blind sensor is up but not looking at that host or path. Neither one means “no threat.”
- Walk the three givens from the student guide. Sensor up and seeing that host: check the rule. Sensor down or not seeing that place: check the sensor, or both. Down all week so “nothing happened”: reject.
- If they start configuring a sensor: that is not this lesson.
- If they say the sensor was down, so nothing happened: reject. Silence is not proof.
- If they invent a ticket or a network layout: the product is the check, not a ticket name or an architecture.

---

## Knowledge Check – Answer Key

1. **A down sensor means the activity did not happen. True or false?**  
   **Answer:** False. A dead or blind sensor is not “no threat.”  
   **Explanation:** The activity may still have happened. You just could not see it. A down sensor is not proof.

2. **Someone says “the rule never fired.” What two things might you check?**  
   **Answer:** The rule, the sensor, or both.  
   **Explanation:** A silent rule is not always a broken rule. If the sensor was up and seeing that host, check the rule. If it was down or not seeing that place, check the sensor, or both.

3. **Name three kinds of sensor this lesson uses as examples.**  
   **Answer:** MDE, Zeek, IDS.  
   **Explanation:** Those are examples of collectors DE might watch for up-and-seeing. They are not a vendor-admin lab.

---

## Additional Instructor Resources

- Next: 4.8 Site-specific DE knowledge
