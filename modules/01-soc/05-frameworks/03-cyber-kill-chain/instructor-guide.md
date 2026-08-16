# Instructor Guide – Module 1.5.3 – Cyber Kill Chain

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C · 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 B / C / C · 1.5.3.2 3c / 4c / 4c  
- CTI: 1.5.3.1 B / C / C · 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the seven stages and force **stage + not previous + not next**. Close **1.5**. Do not teach ATT&CK tactics as stages.

**Key Teaching Points:**
- Sequence, not a matrix.
- Weaponization is usually **not observed**.
- One row, one primary stage.
- Hunter/CTI start at B / 3c — push the neighbor reject.

**Common Student Challenges:**
- Everything is Actions on Objectives.
- C2 on a process-create.
- Delivery vs Installation (file in flight vs persist).
- Writing T-IDs instead of stages.
- Treating 1.4.4 “scan” as a different system without mapping it to Reconnaissance.

**Required Materials:**
- Student Guide
- Slide Deck
- Seven-stage strip on the board
- Answer key (this guide)

---

## Learning Objectives

1. Purpose.
2. Seven stages in order.
3. Identify stage; reject previous or next.

**Mapped Items:** K 1.5.3.1 · T 1.5.3.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & purpose         | 6 min    | a |
| Seven stages                   | 16 min   | b; weaponization empty |
| Progression / mapping          | 8 min    | c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Close 1.5 |
| **Total**                      | **~72 min** | Stretch Ex 2 if they say C2 |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — name the stage and one neighbor.
- Recite order once as a group.
- Installation = foothold/persist. Delivery = getting it there.

**Question:**  
“If this is stage N, what would stage N+1 look like in *logs*?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail ATT&CK-only answers. Fail Actions on Objectives without objective evidence.

**Summaries:**
- Ex 1: Delivery (GET exe); not Exploitation/Installation without persist.
- Ex 2: Installation (Run key); not C2.
- Ex 3: Reconnaissance (sweep); not Actions.

**Cases:**

| Item | Stage | Not previous | Not next |
|------|-------|--------------|----------|
| A | **Exploitation** or **Installation** (code running / foothold). Prefer Installation if they cite persist; Exploitation if they cite first exec only. | Delivery (file already used) | C2 (no network row) |
| B | **Delivery** (mail as the vehicle) | Weaponization (not seen) | Exploitation (no open/click/exec yet) |
| C | **Command and Control** | Installation (this row is the channel) | Actions (no steal/encrypt shown) |
| D | **Reconnaissance** or **Unsuccessful**-adjacent: failed auth is still **Reconnaissance** / access *attempt*. Prefer **Reconnaissance** if they treat it as probing; if they argue it is a failed action, accept **not Actions** (objectives not achieved) and **not Delivery**. Classroom key: **Reconnaissance** (credential probing), not Actions. | Weaponization N/A | Exploitation (no session) |

D is the soft one — accept Reconnaissance with “not Actions because nothing succeeded.”

---

## Knowledge Check – Answer Key

1. **Purpose?**  
   **Answer:** Place activity on an intrusion **sequence** so you can describe progression.  
   **Explanation:** Outline a, c.

2. **Seven stages?**  
   **Answer:** Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objectives.  
   **Explanation:** Outline b.

3. **Weaponization empty?**  
   **Answer:** Pairing exploit and payload usually happens off-network. SOC rarely logs it. Write not observed.  
   **Explanation:** Visibility.

4. **Why reject neighbors?**  
   **Answer:** Stops “everything is C2/Actions.” Sign-off is the boundary, not the label alone.  
   **Explanation:** Task.

5. **Stage vs ATT&CK tactic?**  
   **Answer:** Stage = place in a **sequence**. Tactic = **why** in a behavior matrix. Same activity can have both; they are different systems.  
   **Explanation:** Fence with 1.5.1.

---

## Additional Instructor Resources

- Next recommended module: 1.6.1 Report types
