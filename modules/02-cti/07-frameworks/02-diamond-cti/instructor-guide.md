# Instructor Guide – Module 3.7.2 – Diamond Model Application in CTI

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.7.2 A / B / B · 3.7.2.1 1a / 2b / 3c  
- Hunter: 3.7.2 B / C / C · 3.7.2.1 3c / 4c / 4d  
- CTI: 3.7.2 B / C / C · 3.7.2.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Advanced Diamond for CTI: fill vertices from a **report/activity set**, name the weakest, let that vertex **constrain the intel product**, reject vendor-name Adversary and uncited Capability.

**Key Teaching Points:**
- Do not re-teach the 0.6.2 vertex tour. One recap sentence, then the excerpt.
- Adversary unknown is a *success*, not a failed card.
- Hunter/CTI task goes to **4d** — the 7-level move is the *product constraint*, not a prettier table.
- SOC K is **A / B / B** (not A/B/C). Task **1a / 2b / 3c**. Do not collapse.
- Do not copy `modules/00-intro/06-frameworks/` into this folder.

**Common Student Challenges:**
- Pasting the vendor cluster name into Adversary.
- Stuffing T1486 / “ransomware” into Capability.
- Expanding Victim from one host to “Harbor” or “finance.”
- Writing a **3.11** profile or a **3.1.7** confidence letter.
- Putting ATT&CK IDs in the vertices instead of facts.

**Required Materials:**
- Student Guide
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Diamond on an intelligence problem (report / activity set).
2. Fill → weakest → product constraint.
3. Reject vendor-name Adversary and uncited Capability.

**Mapped Items:** K 3.7.2 · T 3.7.2.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 0.6.2 redo / 3.1.7 / 3.11 |
| Advanced fill + product use    | 14 min   | a |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | Diamond lines |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep the APT name |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they already filled incident cards in 0.6.2. Push **product constraint**.
- 4d: “Adversary is weakest” is not enough. They must say **what claim drops out of the product**.
- Meta-features: name them once, then leave them. They are not vertices and not a profile.

**Question:**  
“The vendor named Night Owl APT. What would have to appear in the Harbor excerpt before Adversary is legal *here*?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail vendor-name Adversary. Fail uncited T1486 Capability. Fail Victim = “all of Harbor.” Fail E as a 3.11 write-up.

**Summaries:**
- Ex 1: C / I / V filled; Adversary unknown; product cannot name a group.
- Ex 2: vendor label ≠ Adversary.
- Ex 3: uncited T1486 ≠ Capability.

**Diamond lines:**

| Item | A | C | I | V | Weakest | Notes |
|------|---|---|---|---|---------|-------|
| A | Unknown | PS-enc; Run `Updater`; HTTP GET `update.exe` | `nightowl-updates.net` / `203.0.113.88:8080` | `jlee` / `WS-JLEE` | **Adversary** | Product: C/I/V only |
| B | **None / reject** | — | — | — | — | Label, not a who |
| C | — | **None / reject** T1486 | — | — | — | Reported, not observed |
| D | — | — | — | **Reject** “all of Harbor” | — | One host is not the sector |
| E | **Refuse** | — | — | — | — | **3.11**, not this card |

**Product sentence (A):** “Encoded PowerShell, Run-key persistence, and HTTP GET of `update.exe` from `nightowl-updates.net` (`203.0.113.88`) against `jlee` / `WS-JLEE`. Adversary unattributed.”

---

## Knowledge Check – Answer Key

1. **Advanced vs 0.6.2?**  
   **Answer:** Report or activity set; weakest vertex *constrains the intel product*; reject vendor-name Adversary. 0.6.2 fills an incident / indicator card.  
   **Explanation:** Outline a.

2. **Diamond line besides the four fills?**  
   **Answer:** Weakest vertex, and what the product cannot claim.  
   **Explanation:** Task.

3. **Why not vendor “APT” in Adversary?**  
   **Answer:** A cluster / marketing name is not evidence of *who* on this problem. Adversary stays empty.  
   **Explanation:** Example 2.

4. **Why not vendor T1486 as Capability?**  
   **Answer:** Not in *this* evidence. Uncited capability stays off this card.  
   **Explanation:** Example 3.

5. **Finished actor profile?**  
   **Answer:** **3.11**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Diamond Model of Intrusion Analysis (lookup)
- Next recommended module: 3.7.3 Cyber Kill Chain in CTI
