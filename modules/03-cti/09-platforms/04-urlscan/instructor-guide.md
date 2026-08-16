# Instructor Guide – Module 3.9.4 – URLScan

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.4 A / A / B · 3.9.4.1 1a / 1a / 2b  
- Hunter: 3.9.4 A / B / B · 3.9.4.1 2b / 3c / 4c  
- CTI: 3.9.4 B / C / C · 3.9.4.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
URLScan depth: retrieve (preferred) or submit a **page load**, extract redirect / contacted host / appearance, reject PDNS-use and theft over-claim.

**Key Teaching Points:**
- SOC K is **A / A / B**. Hunter K is **A / B / B**. Task ends at **4c** (not 4d).
- **No live malware submits** from class. The retrieve card *is* the lab.
- Do not re-teach 3.3.2 “when URLScan.”
- This closes **3.9**. Next unit is STIX (**3.10**), not 3.8.3.

**Common Student Challenges:**
- Submitting a known-bad URL “to see.”
- Using URLScan for historical IPs.
- Screenshot = confirmed phish success.
- Opening Silent Push and calling it URLScan.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Capabilities of a page scan.
2. Retrieve vs submit (retrieve here).
3. Extract redirect / host / appearance only.

**Mapped Items:** K 3.9.4 · T 3.9.4.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | No live submit; not 3.9.3 |
| Capabilities + interpret       | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | Closes 3.9 |
| **Total**                      | **~66 min** | Stretch Ex 3 if they write a profile |

---

## Detailed Teaching Notes

**Talking Points:**
- Retrieve existing scan > submit from class. Same extract either way.
- Cert CN `nightowl-updates.net` vs title “Harbor Invoice” is a useful *appearance* contrast — still not attribution.
- Contacted `203.0.113.88` is *this load*. Last year’s A is Silent Push.

**Question:**  
“The screenshot looks like Harbor finance. What would you still need before you claim a user entered a password?”

---

## Hands-On Exercise – Instructor Guidance

**Retrieve/submit:**

| Item | Action | Notes |
|------|--------|-------|
| A | **Retrieve** classroom scan | Why: existing result; no live submit |
| B | **Refuse** | Safety; card already exists |
| C | **Wrong tool** | Historical A = **3.9.3** |

**Extract:** `invoice-harbor.example → nightowl-updates.net/invoice | nightowl-updates.net / 203.0.113.88 | fake Harbor login | not theft / not a profile`  
**D:** reject — appearance ≠ success.  
**E:** keep — contacted IP from *this* load.

---

## Knowledge Check – Answer Key

1. **URLScan for?**  
   **Answer:** Scan or retrieve *this URL / this page load* (redirects, hosts, appearance).  
   **Explanation:** Outline a.

2. **Retrieve vs submit?**  
   **Answer:** Retrieve when a scan already exists (this hour). Do not submit live malware from class.  
   **Explanation:** Task 1.

3. **Two extract fields?**  
   **Answer:** Any two of: redirect chain, contacted host/IP, screenshot/title as appearance, cert CN.  
   **Explanation:** Outline b.

4. **Why not historical A?**  
   **Answer:** One load, not PDNS. That is **3.9.3**.  
   **Explanation:** Example 2.

5. **Why not theft?**  
   **Answer:** Screenshot shows what was *displayed*, not that a password was sent.  
   **Explanation:** Example 3.

---

## Additional Instructor Resources

- Classroom URLScan cards
- Next recommended module: 3.10 Common STIX Objects
