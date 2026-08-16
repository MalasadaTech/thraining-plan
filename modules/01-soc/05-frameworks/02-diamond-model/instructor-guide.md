# Instructor Guide – Module 1.5.2 – Diamond Model

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.2.1 A / B / C · 1.5.2.2 2b / 3c / 4c  
- Hunter: 1.5.2.1 B / C / C · 1.5.2.2 3c / 4c / 4d  
- CTI: 1.5.2.1 B / C / C · 1.5.2.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach the four vertices and force a **complete, honest fill** plus **weakest vertex**. Do not produce an actor profile. Hunter/CTI 7-level is **4d** on the apply task — they can challenge a weak Adversary fill, not invent one.

**Key Teaching Points:**
- Purpose = organize know / don’t know.
- Four vertices only. Meta-features are optional name-drops.
- Unknown adversary is correct more often than a blog name.
- Weakest vertex → next SOC-sized collection, not a CTI paper.

**Common Student Challenges:**
- Naming an APT from an IP.
- Skipping empty vertices.
- Filling Capability with “malware” and no method.
- Turning this into ATT&CK IDs or Kill Chain stages.
- Grading SOC 3 as if they must attribute.

**Required Materials:**
- Student Guide
- Slide Deck
- Whiteboard diamond
- Answer key (this guide)

---

## Learning Objectives

1. Purpose.
2. Four vertices.
3. Fill four; name weakest.

**Mapped Items:** K 1.5.2.1 · T 1.5.2.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & purpose         | 8 min    | a |
| Four vertices                  | 12 min   | b |
| Analysis / attribution use     | 8 min    | c; unknown is OK |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 16 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~70 min** | Stretch Ex 2 if they name a gang |

---

## Detailed Teaching Notes

**Talking Points:**
- SOC 3: A / 2b — four boxes + “weakest = empty.”
- Hunter/CTI 3: already B / 3c. 7-level **4d**: they should catch over-attribution.

**Question:**  
“Which box did you invent?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail a named APT. Fail ATT&CK-only cards. Fail “all four complete” with guesses.

**Summaries:**
- Ex 1: weakest Adversary; victim+capability+infra filled.
- Ex 2: do not invent Night Owl; victim may be only an IP.
- Ex 3: infra empty; capability = Run key + drop.

**Cases (accept equivalents):**

| Item | A | C | I | V | Weakest |
|------|---|---|---|---|---------|
| A | Unknown | GET `update.exe` | `198.51.100.80:8080` | `10.10.22.17` | Adversary or Victim (no user) |
| B | Unknown | HKLM service key create | empty | `jlee` / that host | Infrastructure (or Adversary) |
| C | Unknown / spoofed envelope | Invoice lure (capability = social/mail) | `203.0.113.88` | `finance@buildingc.internal` | Adversary (mailfrom is a claim) |

---

## Knowledge Check – Answer Key

1. **Purpose?**  
   **Answer:** Organize an intrusion into four related features so gaps are visible. Supports analysis and later attribution.  
   **Explanation:** Outline a, c.

2. **Four vertices?**  
   **Answer:** Adversary (who directs), Capability (method/tool), Infrastructure (systems they use), Victim (who/what is acted on).  
   **Explanation:** Outline b.

3. **Unknown adversary?**  
   **Answer:** If you have no evidence of *who*, write unknown. An IP is Infrastructure.  
   **Explanation:** Outline c.

4. **Weakest?**  
   **Answer:** The vertex with the least evidence. It drives the next look.  
   **Explanation:** Task.

5. **Why not a profile?**  
   **Answer:** A finished actor profile is **3.11**. This hour only structures the case.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Next recommended module: 1.5.3 Cyber Kill Chain
