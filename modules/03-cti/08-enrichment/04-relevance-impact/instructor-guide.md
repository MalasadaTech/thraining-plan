# Instructor Guide – Module 3.8.4 – Threat Relevance and Organizational Impact

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.4 A / B / B · 3.8.4.1 1a / 2b / 3c  
- Hunter: 3.8.4 B / C / C · 3.8.4.1 2b / 3c / 4c  
- CTI: 3.8.4 B / C / C · 3.8.4.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Judge **so what, here**. Fail skipped-path impact, invented PIRs, and attribution letters.

**Key Teaching Points:**
- CTI task **3c / 4c / 4d**. 4d = why user-estate impact is supported and `pay-db-01` is not.
- Hunter task tops at **4c**, not 4d. Do not invent a hunter 4d.
- SOC **1a / 2b / 3c**.
- **3.8.2** is platform apply. This hour is mission/asset impact. Do not let them resubmit the TTP list.
- Overlay a real site card if you have one. Still fail invented PIRs.

**Common Student Challenges:**
- Jumping from WS-JLEE to payroll outage.
- Writing PIR-1 so the finding “matters.”
- Nation-state letter as the impact line.
- “Not relevant” on Night Owl because they want OT/payroll drama.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional: real site card overlay
- Answer key (this guide)

---

## Learning Objectives

1. Relevance to this estate.
2. Impact if true — on the evidence.
3. Reject skipped path, PIR, attribution.

**Mapped Items:** K 3.8.4 · T 3.8.4.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.8.2 redo; not 3.12 PIR |
| Relevance + impact             | 14 min   | a–c |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they sink pay-db-01 |

---

## Detailed Teaching Notes

**Talking Points:**
- “Can it run here?” was **3.8.2**. “Does it matter to *this* estate, and how far?” is now.
- Crown jewels on the 1.8.1 card are bait. A jewel without a path is **not shown**, not “the impact.”
- 4d is the *not because* clause.

**Question:**  
“What extra cite would make `pay-db-01` a legal impact on *this* card?”

---

## Hands-On Exercise – Instructor Guidance

| Item | Result |
|------|--------|
| A | **Product** — relevant to Windows users; impact = that estate; pay-db-01 not shown |
| B | **Not relevant** — no ESXi |
| C | **Fail** — skipped path |
| D | **Fail** — PIR (**3.12.1**) |
| E | **Fail** — attribution (**3.1.7**) |

---

## Knowledge Check – Answer Key

1. **Relevance vs 3.8.2?**  
   **Answer:** 3.8.2 = can the TTP run here. This hour = does the finding matter to this mission/estate.  
   **Explanation:** Outline a / fence.

2. **Impact line?**  
   **Answer:** Finding, relevant (Harbor fact), impact if true, what is not shown.  
   **Explanation:** Product.

3. **Why not pay-db-01?**  
   **Answer:** No path from WS-JLEE to the jewel on this card.  
   **Explanation:** Example 2.

4. **Why not a PIR?**  
   **Answer:** Writing / obtaining requirements is **3.1.4** / **3.12.1**.  
   **Explanation:** Outline c / Example 3.

5. **Real local list?**  
   **Answer:** **3.12.1** — obtain, do not invent.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Harbor stand-in is **1.8.1** (lesson-only)
- Last child of 3.8. Next cluster is **3.9** if scheduled
