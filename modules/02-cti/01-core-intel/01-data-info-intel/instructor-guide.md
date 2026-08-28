# Instructor Guide – Module 2.1.1 – Difference between data, information, and intelligence

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.1.1 B / C / C ; 2.1.1.1 3c / 4c / 4c  
- Hunter: 2.1.1 A / B / B ; 2.1.1.1 1a / 2b / 3c  
- SOC: 2.1.1 A / A / A ; 2.1.1.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name an item as data, information, or intelligence so the next desk gets a judged answer, not a raw field with a new title.

**Context (plain language):**

- What this lesson is for: A CTI analyst is asked to brief or hand off what landed on the desk. Before treating it as something someone should act on, they have to know what layer they have. This lesson names those layers.
- How it hooks to the lesson before: SOC reporting (`1.5`) closed the SOC track. An RFI is the door into CTI. This is the start of the CTI analyst track.
- How it hooks to the lesson after: 2.1.2 is the intelligence lifecycle — which job you are in. This lesson is only the three words and the sort.
- Why we are doing it this way: name data, information, and intelligence before anyone walks a lifecycle, writes a requirement, or drafts a finished product.
- What we are *not* doing in this lesson: lifecycle stages, PIR format, finished product, attribution, platform depth, hunt. No lab.
- Extra step: none.

Use the same names as the student guide: **data**, **information**, and **intelligence**. The givens use course-fiction names (`203.0.113.88`, Temp `invoice.vbs`, **WS-JLEE** / `jlee`, incident **A12**). Do not turn them into the intro plot. Do not dump the Run key.

**Key Teaching Points:**
- Data is a recorded fact. Information is a story. Intelligence is a judged answer to a question.
- The path is add context, then add judgment. Not a rename.
- If they are unsure, it is not intelligence yet.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.1.1 – Difference between data, information, and intelligence
- T: 2.1.1.1 – Correctly categorize examples as data, information, or intelligence

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Sort the layer |
| Key Concepts            | 12 min    | Three terms; three givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: something landed on the desk, and you have to know the layer before you brief it as a decision.
- Write the three terms. Stop there. Information describes. Intelligence judges.
- Walk the three “given” lines from the student guide. The product is the layer, not a story of the incident.
- If they call a VirusTotal detection count intelligence: that is context. It is still information.
- If they want PIR format: that is 2.1.4. Today the question can be informal.
- If they start the lifecycle: that is 2.1.2.
- If they write a finished paper: that is 2.11.
- If they start the DYA / PRD plot: that fiction is from the intro. It is not this lesson.

---

## Knowledge Check – Answer Key

1. **A hash with no other text is intelligence. True or false?**  
   **Answer:** False. That is data.  
   **Explanation:** A hash with no other text is a recorded fact. It has no story and no judgment.

2. **What must you add before information becomes intelligence?**  
   **Answer:** A judgment against a question, and a so-what (what someone should do).  
   **Explanation:** Context makes a story. Intelligence is that story judged against a question, with an action someone can take.

3. **“We assess that domain is the payload host for incident A12; treat it as such.” Data, information, or intelligence?**  
   **Answer:** Intelligence.  
   **Explanation:** It answers a question and names a so-what. It is not a raw field and not only a who / what / where story.

---

## Additional Instructor Resources

- Next: 2.1.2 Intelligence lifecycle
