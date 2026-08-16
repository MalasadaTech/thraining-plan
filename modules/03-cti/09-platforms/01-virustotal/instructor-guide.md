# Instructor Guide – Module 3.9.1 – VirusTotal Relations and Behavior

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.9.1 A / B / B · 3.9.1.1 1a / 2b / 3c  
- Hunter: 3.9.1 B / C / C · 3.9.1.1 3c / 4c / 4d  
- CTI: 3.9.1 B / C / C · 3.9.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
VT depth: **Relations** for cited infra hops, **Behavior** for process/file/registry/network events. Classroom cards only.

**Key Teaching Points:**
- One recap of 3.3.2 (when to open VT), then the tabs. Do not re-teach the four-tool survey.
- Cards are **lesson-only**. If they have a live VT account, same edges — do not require login.
- SOC K is **A / B / B**. Hunter/CTI task **3c / 4c / 4d**. 4d is *edge type* (contacted domain vs communicating file vs community “related”).
- Do not convert hops to Zeek (**2.3.1**). Do not run AnyRun (**3.9.2**).

**Common Student Challenges:**
- Pasting the whole Relations graph.
- Calling every related *file* infrastructure.
- Using Detection ATT&CK labels as Behavior.
- Opening Silent Push because “that’s pivoting.”

**Required Materials:**
- Student Guide (classroom cards)
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Relations: seed → cited additional infra.
2. Behavior: four event classes.
3. Reject unlabeled nodes and Detection dumps.

**Mapped Items:** K 3.9.1 · T 3.9.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.3.2 redo / 2.3.1 / 3.9.2 |
| Relations + Behavior           | 14 min   | a–b |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Lines |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep helpdesk.exe as infra |

---

## Detailed Teaching Notes

**Talking Points:**
- Contacted domain/IP = infra hop (same *idea* as **3.8.1**, different *UI*).
- Communicating file = next *sample*, maybe **3.4** or a second Relations walk — not a domain.
- Behavior network row matching Relations contacted domain is a *consistency check*, not two products.

**Question:**  
“What edge would `random-cdn.example` need before it is legal additional infra?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail D. Fail C as infra (accept “file — not infra”). Fail Detection-tab Behavior lines.

**Relations:**

| Item | Additional infra | Edge | Notes |
|------|------------------|------|-------|
| A | `nightowl-updates.net` | Contacted domain | Yes |
| B | `login-nightowl.net` | Contacted domain | Yes |
| C | **None (file)** | Communicating file | `88aa9911…` |
| D | **Reject** | Community / none | No edge |

**Behavior line:** `wscript→powershell -enc | %TEMP%\update.exe | HKCU Run Updater | GET update.exe :8080 nightowl-updates.net`

---

## Knowledge Check – Answer Key

1. **Relations vs Behavior?**  
   **Answer:** Relations = how objects are *linked* (infra hop). Behavior = sandbox *events* (process/file/reg/net).  
   **Explanation:** Outline a–b.

2. **Relations line besides the name?**  
   **Answer:** Seed, edge type, why not a coincidence.  
   **Explanation:** Task 1.

3. **Why not the communicating file as infra?**  
   **Answer:** It is another sample, not a domain/IP.  
   **Explanation:** Example 2.

4. **Why not Detection T-IDs?**  
   **Answer:** Wrong tab. Labels without a Behavior row are not this extract.  
   **Explanation:** Example 3.

5. **Zeek/SIEM query?**  
   **Answer:** **2.3.1**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Classroom VT cards
- Next recommended module: 3.9.2 AnyRun
