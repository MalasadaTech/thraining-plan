# Instructor Guide – Module 2.8.2 – Extracting Applicable TTPs from Intelligence Reports

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- Hunter: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4d  
- SOC: 2.8.2 A / B / B ; 2.8.2.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Find TTPs in a report, then keep only those that apply to this environment. Real ATT&CK IDs only.

**Context (plain language):**

- What this lesson is for: CTI analysts pull behaviors a defender here can detect or hunt. They do not copy every ATT&CK ID out of a vendor report.
- How it hooks to the lesson before: 2.8.1 was the generic hop from a seed to extra infrastructure. This lesson keeps only TTPs that apply to this environment. It is not another hop.
- How it hooks to the lesson after: 2.8.3 treats the IOC as an object (keep / expire / enrich / link), not a TTP.
- Why we are doing it this way: find a TTP that has a how, then test platform, path, and whether a defender here can use it. Mapping IDs is already a lesson. Impact is later.
- What we are *not* doing in this lesson: ATT&CK mapping (tactic / technique / evidence / neighbor). Organizational impact. Hunt-lead extract. Actor profile. Invented ATT&CK IDs. No lab.
- Extra step: none.

Use the same names as the student guide: **TTP**, **how**, **applicable**, **this environment**, **keep**, **reject**. **This environment** is DYA, a law firm with Windows workstations. **WS-JLEE** is the user workstation already in the course. **OT** means operational technology / plant systems — not this shop. **T1059.001** is PowerShell. Do not say “T-ID” unless you also say ATT&CK ID.

**Key Teaching Points:**
- A relevant TTP in a report has a how. Slogans and IOC lists are not TTPs.
- Applicable means platform + path possible here + a defender can detect or hunt it (or you name the gap and still do not call it usable).
- Keep T1059.001 encoded PowerShell. Reject an OT-historian wipe for this law firm.

**Common Student Challenges:**
- Copy every ATT&CK ID from the vendor table. Why: the appendix looks complete. Example: pasting an ICS technique into the DYA extract.
- Write an impact sentence. Why: “so what” feels like the next line. Example: “nation-state crisis if historians are wiped” instead of “not applicable here.”
- Treat a slogan as a TTP. Why: the report said “they use persistence.” Example: keeping “persistence” with no tool, command, or ID.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.8.2 – Extracting applicable TTPs from intelligence reports
- T: 2.8.2.1 – Extract applicable TTPs from an intelligence report

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Pull what a defender here can use |
| Key Concepts            | 12 min    | Find a how; three criteria; two givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a vendor report names many techniques, and you have to keep only the ones a defender here can use.
- Walk find-the-TTP first. A relevant TTP has a how. Skip hashes, slogans, and an ATT&CK ID with no how.
- Walk the three criteria: platform, path, use. DYA is a law firm with Windows workstations. OT and macOS-only fail platform.
- Walk the two givens. Keep T1059.001 encoded PowerShell — WS-JLEE already showed it. Reject wipe OT historians — not this shop. The product is keep / reject, not a crisis paragraph.
- If they start mapping tactic / technique / evidence or rejecting a neighbor ID: that is 2.7.1. This lesson is which extracted TTPs apply here.
- If they write an impact sentence: that is 2.8.4.
- If they invent an ATT&CK ID: real IDs only.
- If they copy the hunt-lead extract (keep artifacts, state a hunt question): that is 3.4.2.

---

## Knowledge Check – Answer Key

1. **Every ATT&CK ID in a vendor report is applicable here. True or false?**  
   **Answer:** False.  
   **Explanation:** Applicability is platform, path, and whether a defender here can use it. A printed ID is only a candidate.

2. **What three things make a TTP applicable to this environment?**  
   **Answer:** We have that platform, the path is possible here, and a defender here can detect or hunt it.  
   **Explanation:** No visibility and no way to get it is not applicable unless you name that gap — and you still do not list it as usable here.

3. **Encoded PowerShell (T1059.001) vs an OT-wipe TTP — keep or reject each, and why?**  
   **Answer:** Keep T1059.001 — Windows workstation shop; already seen on WS-JLEE. Reject the OT wipe — DYA is a law firm and does not run OT historians.  
   **Explanation:** The product is keep / reject for this environment, not an impact paragraph.

---

## Additional Instructor Resources

- Next: 2.8.3 IOC handling
