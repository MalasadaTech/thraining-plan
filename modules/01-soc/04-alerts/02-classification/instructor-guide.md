# Instructor Guide – Module 1.4.2 – Alert Classification

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.2.1 A / B / C ; 1.4.2.2 2b / 3c / 4c  
- Hunter: 1.4.2.1 B / C / C ; 1.4.2.2 2b / 3c / 4c  
- CTI: 1.4.2.1 A / A / B ; 1.4.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Classify a case as TP, FP, TN, or FN and cite the evidence. Include one miss as FN.

**Context (plain language):**

- What this lesson is for: After you have looked at a case, you classify it so the shop knows whether the detection was right, and you cite the evidence — a short pointer to the field or log that proves the label.
- How it hooks to the lesson before: 1.4.1 gathered context on a fired alert. This lesson is the four labels.
- How it hooks to the lesson after: 1.4.3 is *why* a false positive fired — not the label.
- Why we are doing it this way: name the four labels and require a cite, including a miss as FN, before anyone explains why a false positive fired.
- What we are *not* doing in this lesson: false-positive cause class. Scan / root / user categories. Hunt how-to. Invented alerts so they can classify. No lab.
- Extra step: none.

Use the same names as the student guide: **True Positive**, **False Positive**, **True Negative**, **False Negative**, **alert queue**, and **cite / evidence**. **Alert queue** is the list of fired alerts waiting for an analyst, not the headline word for a true negative or a false negative. The true-positive given is the encoded-PowerShell alert. The false-negative given is `GET /update.exe` with no alert. Do not turn either into the course-fiction plot.

**Key Teaching Points:**
- Four labels. True negatives and false negatives usually have no alert in the queue.
- Cite the field or log. A slogan is not a cite.
- A false negative is a miss, not a disliked alert.

**Common Student Challenges:**
- Treat a false negative as a bad alert in the queue. Why: they have only classified fired alerts. Example: calling the GET a false positive because they dislike that nothing fired.
- Invent an alert so a true negative or false negative can be classified. Why: they think every case must be a queue item. Example: writing a fake browser-malware alert for ordinary browse.
- Explain why the PowerShell rule is broad instead of labeling the `Get-Help` case. Why: the next lesson is causes. Example: “untuned rule” with no FP label and no cite.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.4.2.1 – Alert classification (TP/FP/TN/FN)
- T: 1.4.2.2 – Classify given cases as TP, FP, TN, or FN and cite the evidence

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Label plus cite |
| Key Concepts            | 12 min    | Four labels; four givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: after you have looked at a case, you classify it and cite evidence so the shop knows whether the detection was right.
- Walk the four-label table. Stop on true negative and false negative: they usually have no alert in the queue.
- Walk the four givens. Put the false negative next to the true positive so they do not call a miss a false positive or invent an alert.
- If they start explaining an untuned rule: that is 1.4.3. This lesson is the label only.
- If they invent an alert for the GET: there is no alert. That is the false negative.
- If they say “malicious” with no cite: cite the field.

---

## Knowledge Check – Answer Key

1. **FN is a bad alert sitting in the queue. True or false?**  
   **Answer:** False. A false negative is a miss — no alert on bad activity that should have been detected.  
   **Explanation:** A disliked alert in the queue is still a fired alert. That is a true positive or a false positive, not a false negative.

2. **Alert `Encoded PowerShell from script host`, `wscript` + `-enc` confirmed. Classify and cite.**  
   **Answer:** TP. Cite: parent `wscript` and `-enc` are the activity the rule is for, and that activity happened.  
   **Explanation:** The rule is encoded PowerShell from a script host. The parent and command line prove the hit.

3. **`GET /update.exe` to `203.0.113.88:8080`, no alert. Classify and cite.**  
   **Answer:** FN. Cite: the download occurred; nothing fired.  
   **Explanation:** That is a missed detection. Do not invent an alert so you can classify it.

---

## Additional Instructor Resources

- Next: 1.4.3 Common false positive causes
