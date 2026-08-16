# Instructor Guide – Module 3.11.3 – Handling RFIs

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.11.3 A / A / A · 3.11.3.1 1a / 1a / 1a  
- Hunter: 3.11.3 A / A / B · 3.11.3.1 1a / 1a / 2b  
- CTI: 3.11.3 B / C / C · 3.11.3.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
CTI **receives** RFIs: evaluate, prioritize, answer or decline. Classroom queue only.

**Key Teaching Points:**
- SOC K is **A / A / A** and task **1a / 1a / 1a** — they *recognize* an RFI, they do not run the CTI queue at 3-level. Do not collapse to Hunter/CTI codes.
- CTI **4d** is R2 (answer unattributed without inventing a who) and the decline judgment on R3/R4.
- 1.6.1 is the SOC *ticket type*. This hour is the CTI *inbox*.
- Do not open 3.12 PIR lists except “that is next.”

**Common Student Challenges:**
- Answering R2 as nation-state.
- Writing an exploit for R3.
- A new 6-page product for R4.
- Treating every RFI as a 3.11.1 product.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Purpose + lifecycle.
2. Evaluate and prioritize.
3. Short response or decline.

**Mapped Items:** K 3.11.3 · T 3.11.3.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 1.6.1 / 3.11.1 redo |
| Lifecycle + evaluate           | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Queue |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Closes 3.11 |
| **Total**                      | **~66 min** | Stretch R2 if they fill who |

---

## Detailed Teaching Notes

**Talking Points:**
- Short answer > new product when holdings exist.
- R2 is the 4d item: the question is legitimate; the *honest* answer is empty who.
- R3: decline, do not lecture malware writing.
- If they invent new PDNS holdings, stop — **3.12.2**.

**Question:**  
“Leadership asked ‘is it a nation-state?’ What sentence answers them *and* stays inside 3.11.1.2?”

---

## Hands-On Exercise – Instructor Guidance

| ID | Scope | Priority | Action |
|----|-------|----------|--------|
| R1 | Yes | **High** | CoA sentence (block two names; hunt) |
| R2 | Yes | Medium | **Unattributed** — not nation-state |
| R3 | **No** | — | Decline |
| R4 | Duplicate | **Low** | Point at last activity note |

---

## Knowledge Check – Answer Key

1. **RFI for?**  
   **Answer:** A customer question that needs an intel answer (or a decline).  
   **Explanation:** Outline a.

2. **Lifecycle?**  
   **Answer:** Receive → evaluate → prioritize → respond or decline.  
   **Explanation:** Outline a.

3. **Why R1 > R4?**  
   **Answer:** R1 is an action this window. R4 is already answered.  
   **Explanation:** Outline b.

4. **R2 without who?**  
   **Answer:** Say unattributed / low confidence. The RFI does not create evidence.  
   **Explanation:** Example 2 / 4d.

5. **Need collection?**  
   **Answer:** **3.12.2**. Do not fabricate holdings.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Next recommended module: 3.12.1 Local intelligence requirements and priorities
