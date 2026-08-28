# Instructor Guide – Module 3.1 – Purpose of Threat Hunting

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.1.1 B / C / C ; 3.1.1.1 3c / 4c / 4c ; 3.1.1.2 3c / 4c / 4d  
- SOC: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
- CTI: 3.1.1 A / B / B ; 3.1.1.1 1a / 2b / 3c ; 3.1.1.2 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name why hunting exists in the program: find activity the alerts missed, and name detection and visibility gaps.

**Context (plain language):**

- What this lesson is for: SOC works the alerts that already fired. CTI answers requests for more context. Hunters look for malicious or suspicious activity that never appeared in that list, and they name the holes that let it hide. This lesson is why that job exists, next to SOC tickets and detections — not instead of them.
- How it hooks to the lesson before: 2.12.3 closed the CTI track (local channels and customers). The hunter track starts here.
- How it hooks to the lesson after: 3.2.1 is hunt types.
- Why we are doing it this way: name why hunting exists — missed activity and gaps — before anyone picks a hunt type or writes a hunt card.
- What we are *not* doing in this lesson: hunt types (3.2.1), hunt cards (3.2.2), invented hunt tickets (3.7), ATT&CK mapping (3.5.1), persistence how-to (3.6.1), no lab.
- Extra step: none.

Use the same names as the student guide: **missed activity**, **detection gap**, **visibility gap**, **alert queue**, and **package**. **False negative** is the 1.4.2 gloss for missed activity with no fired alert, not a new label. The A12 given uses course-fiction names (`WS-JLEE`, `Updater`, `invoice.vbs`). Do not turn it into a hunt-type or hunt-card exercise.

**Key Teaching Points:**
- Hunting exists to find missed activity and to name detection and visibility gaps.
- A miss is no fired alert, not a disliked item in the queue.
- The hunt product is a package (more hosts, a named gap), not a rewrite of the SOC ticket.

**Common Student Challenges:**
- Treat hunt as a rewrite of the SOC ticket. Why: the same incident is the seed. Example: retelling `wscript` → encoded PowerShell as the hunt product instead of looking for other hosts or `Updater`.
- Call a disliked queue alert missed activity. Why: a false negative has no fired alert. Example: labeling the encoded-PowerShell true positive a miss because they wish the rule had also caught the download.
- Mix a detection gap with a visibility gap. Why: both are holes. Example: saying “we have no detection for `Updater`” when those hosts have no registry logs at all.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 3.1.1 – Purpose of Threat Hunting
- T: 3.1.1.1 – Explain the purpose of threat hunting in the context of the security program
- T: 3.1.1.2 – Identify examples of activity that existing controls might miss

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Why hunt exists next to the queue |
| Key Concepts            | 12 min    | Missed vs gaps; A12 examples |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: SOC works fired alerts; hunters look for what never appeared in that list, and they name the holes.
- Write missed activity, detection gap, and visibility gap. Stop there. Do not pick a hunt type.
- A false negative is no fired alert. Point at 1.4.2 if they treat a noisy true positive as a miss.
- Walk the A12 given from the student guide. The first alert is the process create. The miss is `GET /update.exe` with no alert. The look-for is `Updater` / `update.exe` / more `invoice.vbs` on other hosts. The first alert did not require the Run key.
- If they rewrite the SOC ticket: the product is a package — more hosts and a named gap — not a better story of the same process chain.
- If they invent a hunt ticket name: that is 3.7. Obtain the local path later; do not invent one today.
- If they start mapping ATT&CK: that is 3.5.1. Today is why hunt exists.

---

## Knowledge Check – Answer Key

1. **Threat hunting rewrites the SOC ticket with a better story. True or false?**  
   **Answer:** False. The hunt product is a different package: more hosts and a named gap, not a rewrite of the same ticket.  
   **Explanation:** SOC still owns the incident they already labeled. Hunting looks for what that ticket did not catch.

2. **What two jobs does hunting exist to do in the security program?**  
   **Answer:** Find malicious or suspicious activity that existing controls missed, and identify detection and visibility gaps.  
   **Explanation:** Missed activity is a false negative (no fired alert). A detection gap means logs exist but no rule would have caught it. A visibility gap means the telemetry is not there.

3. **HTTP shows `GET /update.exe` to `203.0.113.88:8080`, and no alert fired. The first process alert did not require the HKCU Run value `Updater`. Name the missed activity, and name one thing a hunt should look for that was not on that first alert.**  
   **Answer:** Missed: the `GET /update.exe` download with no alert. Look-for (any one): HKCU Run **`Updater`**, `%TEMP%\update.exe`, or another `invoice.vbs` on other hosts.  
   **Explanation:** The download is a false negative. The Run key was not required on the first process alert, so hunt looks there and on other hosts.

---

## Additional Instructor Resources

- Next: 3.2.1 Hunt types
