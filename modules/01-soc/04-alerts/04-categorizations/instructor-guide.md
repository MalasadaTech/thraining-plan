# Instructor Guide – Module 1.4.4 – Common Alert Categorizations

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.4.4.1 A / B / C · 1.4.4.2 2b / 3c / 4c  
- Hunter: 1.4.4.1 B / C / C · 1.4.4.2 2b / 3c / 4c  
- CTI: 1.4.4.1 A / A / A · 1.4.4.2 1a / 1a / 1a  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach site categories and force **assign + reject the adjacent**. CTI is nomenclature only (A / 1a).

**Key Teaching Points:**
- Not TP/FP. Not ATT&CK.
- Neighbors: scan ↔ unsuccessful; user ↔ root.
- User-writable path ≠ user-level if the token is SYSTEM / HKLM service.
- **Other** = local list only.

**Common Student Challenges:**
- Encoded PS → root because “malware.”
- Failed logon → scan.
- Scanner sweep categorized as FP instead of scan (wrong unit).
- Writing T1059.
- Grading CTI as SOC 5.

**Required Materials:**
- Student Guide
- Slide Deck
- Local extra buckets if the site has them
- Answer key (this guide)

---

## Learning Objectives

1. Name the categories including other.
2. Assign + reject the neighbor.

**Mapped Items:** K 1.4.4.1 · T 1.4.4.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 1.4.2 / 1.5 |
| Categories + neighbors         | 14 min   | a–e |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~62 min** | Stretch Ex 2 if they say root |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — pick the bucket and name the neighbor.
- Hunter: B / 2b at 3-level.
- CTI: A / 1a only — they should recognize the words.

**Question:**  
“If I forbade your first choice, which wrong bucket would people pick?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail T1059. Fail TP/FP. Fail “appropriate category” with no neighbor.

**Summaries:**
- Ex 1: **scan**, not unsuccessful.
- Ex 2: **user-level**, not root.
- Ex 3: **unsuccessful**, not scan.

**Cases:**

| Item | Category | Reject | Why |
|------|----------|--------|-----|
| A | **Scanning** | Unsuccessful | Wide unauthenticated 80s, no 401/logon story. |
| B | **Root-level** | User-level | Token is SYSTEM. |
| C | **Unsuccessful** | Scan | One jump box, failed ssh, no wide probe. |
| D | **Scanning** | Unsuccessful (or other) | Activity type is a sweep. Authorized scanner is **1.4.3**, not a different category. |

---

## Knowledge Check – Answer Key

1. **Categories?**  
   **Answer:** Scanning/reconnaissance; root-level access; user-level access; unsuccessful activity; other (local).  
   **Explanation:** Outline a–e.

2. **Scan vs unsuccessful?**  
   **Answer:** Sweep / no auth attempt vs a failed access attempt.  
   **Explanation:** Adjacent pair.

3. **User vs root?**  
   **Answer:** User token vs SYSTEM/admin/service-level control. Path of the binary is not the token.  
   **Explanation:** Adjacent pair.

4. **Why not “assign appropriate”?**  
   **Answer:** That restates the K. Sign-off is reject the neighbor.  
   **Explanation:** Task rewrite.

5. **ATT&CK?**  
   **Answer:** **1.5**, not a category bucket.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local “other” list
- Next recommended module: 1.4.5 SLA / response time goals
