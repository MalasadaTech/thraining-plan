# Instructor Guide – Module 1.8.3 – Tool Access and Requests

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.8.3.1 2b / 3c / 4c · 1.8.3.2 2b / 3c / 4c · 1.8.3.3 2b / 3c / 4c  
- Hunter: 1.8.3.1 3c / 4c / 4c · 1.8.3.2 3c / 4c / 4c · 1.8.3.3 3c / 4c / 4c  
- CTI: 1.8.3.1 2b / 3c / 4c · 1.8.3.2 2b / 3c / 4c · 1.8.3.3 2b / 3c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach open-URL vs install ticket vs access ticket. Force an **access line** plus a rejected neighbor.

**Key Teaching Points:**
- Harbor URLs / `SOFT-REQ` / `ACCESS-REQ` are stand-ins. Overlay the site catalog if you have one.
- 403 = access, not install. Missing `.exe` = install, not access.
- `PCAP-REQ` (1.8.2, old file) ≠ `ACCESS-REQ` (login to the UI).
- Hunter 3-level is already **3c**.

**Common Student Challenges:**
- Random Wireshark download.
- SOFT-REQ for a 403.
- Shared password as “access.”
- Filing PCAP-REQ when they cannot log into the UI.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional site tool catalog
- Answer key (this guide)

---

## Learning Objectives

1. Open the named URL.
2. SOFT-REQ vs ACCESS-REQ.
3. Access line + reject neighbor.

**Mapped Items:** T 1.8.3.1 · T 1.8.3.2 · T 1.8.3.3

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & card            | 12 min   | three actions |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~54 min** | Stretch Ex 3 if they file SOFT-REQ |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: 2b — match the blocker to the row.
- Overlay real ticket types (`IAM-REQ`, ServiceNow) if you can.

**Question:**  
“Ticket system itself 403s — how do you file `ACCESS-REQ`?” (Named fallback on the site card — Harbor: call SOC-IT duty; do not use personal email as the system of record.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail unofficial download. Fail shared password. Fail SOFT-REQ on 403.

**Summaries:**
- Ex 1: open SIEM URL.
- Ex 2: SOFT-REQ, not a mirror.
- Ex 3: ACCESS-REQ, not SOFT-REQ, not Pat’s session.

**Cases:**

| Item | Action | URL / ticket | Reject |
|------|--------|--------------|--------|
| A | **Open** | `https://ticket.harbor.internal` | ACCESS-REQ with no evidence of 403 |
| B | **`SOFT-REQ`** | desktop IT | Unofficial installer |
| C | **`ACCESS-REQ`** | PCAP UI login | `PCAP-REQ` (that is 1.8.2 warm file) |
| D | **`ACCESS-REQ`** for *your* SIEM account | SOC-IT | Shared password / teammate session |

---

## Knowledge Check – Answer Key

1. **Open vs ticket?**  
   **Answer:** You already have the account and the link. Just open the URL.  
   **Explanation:** Task 1.

2. **Wireshark ticket / not?**  
   **Answer:** `SOFT-REQ`. Do not download from a random mirror.  
   **Explanation:** Task 2; Example 2.

3. **SIEM 403?**  
   **Answer:** `ACCESS-REQ`. The binary/URL exists; you are not entitled.  
   **Explanation:** Task 3; Example 3.

4. **ACCESS-REQ vs PCAP-REQ?**  
   **Answer:** ACCESS-REQ = login to the UI. PCAP-REQ (**1.8.2**) = retrieve an *old file*.  
   **Explanation:** Fence.

5. **Shared password?**  
   **Answer:** Not an access request. File `ACCESS-REQ` for your own account.  
   **Explanation:** Task 3 / D.

---

## Additional Instructor Resources

- Site tool / IAM catalog
- Next recommended module: 1.8.4 Investigation documentation
