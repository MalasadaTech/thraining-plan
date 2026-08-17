# Instructor Guide – Module 3.11.2 – Disseminating Intelligence to the Correct Audiences

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.11.2 A / A / B · 3.11.2.1 1a / 1a / 2b · 3.11.2.2 1a / 1a / 2b · 3.11.2.3 1a / 1a / 2b  
- Hunter: 3.11.2 A / B / B · 3.11.2.1 1a / 2b / 3c · 3.11.2.2 1a / 2b / 3c · 3.11.2.3 1a / 2b / 3c  
- CTI: 3.11.2 B / C / C · 3.11.2.1 3c / 4c / 4c · 3.11.2.2 3c / 4c / 4d · 3.11.2.3 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Send the **3.11.1** product: audience, classroom TLP, approved channel, two tailored versions.

**Key Teaching Points:**
- SOC K is **A / A / B**. CTI tailor task is **4d**; markings/send are **4c**. Do not collapse.
- Say “lesson-only TLP/channel card” out loud. Swap if the site has a real card.
- One recap of 3.1.6, then attach marking + channel.
- Do not teach 3.12.3 customer names.

**Common Student Challenges:**
- TLP:CLEAR on a live host note.
- Slack / personal mail.
- One undifferentiated blob to everyone.
- Calling TAXII the leadership brief.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Audience + method + marking.
2. Two tailored versions.
3. Send on an approved channel.

**Mapped Items:** K 3.11.2 · T 3.11.2.1 · T 3.11.2.2 · T 3.11.2.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.11.1 redo / 1.6.3 / 3.12.3 |
| Audience, TLP, channels, tailor | 16 min | a–c + three T |
| Walkthrough Examples           | 12 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they CLEAR the host |

---

## Detailed Teaching Notes

**Talking Points:**
- 4d: leadership version must *cut* hashes and *name a decision*. Same facts.
- AMBER is the default for this Night Owl note because of host + live infra. GREEN/CLEAR would require stripping those — and then it may no longer be useful to SOC.
- Ticket + TIP for SOC is one *send* with two approved channels; that is fine.

**Question:**  
“What would you have to strip before this note could be TLP:CLEAR — and would SOC still be able to act?”

---

## Hands-On Exercise – Instructor Guidance

| Item | Audience | Marking | Channel | Tailor |
|------|----------|---------|---------|--------|
| A | SOC/IR | **AMBER** | Ticket + TIP | Keep host/domain/action; cut actor essay |
| B | Leadership | **AMBER** | Brief slot | Keep implication/decision; cut hashes |
| C | **Reject** | CLEAR + public | Not on the card | — |

---

## Knowledge Check – Answer Key

1. **Three things before send?**  
   **Answer:** Audience, marking, approved channel (and a method that fits).  
   **Explanation:** Outline a–c / 3.11.2.1.

2. **Why not CLEAR?**  
   **Answer:** Live host and live infra. Need-to-know.  
   **Explanation:** Marking card.

3. **Approved vs rejected channel?**  
   **Answer:** Approved: TIP, intel DL, SOC ticket, leadership brief. Rejected: Slack, personal mail, public post.  
   **Explanation:** Outline b.

4. **Add to 3.1.6?**  
   **Answer:** 3.1.6 rewrites. This hour also **marks** and **sends**.  
   **Explanation:** Fence / 3.11.2.2–3.

5. **Local customer list?**  
   **Answer:** **3.12.3**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Next recommended module: 3.11.3 Handling RFIs
