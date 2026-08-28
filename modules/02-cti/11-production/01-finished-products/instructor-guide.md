# Instructor Guide – Module 2.11.1 – Creating Finished Intelligence Products

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.11.1 B / C / C ; 2.11.1.1 3c / 4c / 4d ; 2.11.1.2 3c / 4c / 4d  
- Hunter: 2.11.1 A / B / B ; 2.11.1.1 1a / 2b / 3c ; 2.11.1.2 1a / 2b / 3c  
- SOC: 2.11.1 A / A / B ; 2.11.1.1 1a / 1a / 2b ; 2.11.1.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Write a finished product that meets the structure and standards, including a short actor profile that stays on the cluster.

**Context (plain language):**

- What this lesson is for: CTI analysts write a finished product so someone can use the judged answer. Collection and notes do not help until that answer is on the page to a standard. This lesson is how to draft that product, check it, and write a short profile of the cluster you can actually defend.
- How it hooks to the lesson before: 2.10.2 was machine-readable links. This lesson is the narrative product.
- How it hooks to the lesson after: 2.11.2 is who gets it and how.
- Why we are doing it this way: name types, required elements, and quality standards before anyone picks a channel or invents a country.
- What we are *not* doing in this lesson: local approval path, channel list, STIX authoring, audience rewrite, attribution confidence scale, RFI queue. No lab.
- Extra step: none.

Use the same names as the student guide: **finished product**, **assessment**, **profile**, **RFI response**, **TIP**, **question**, **what you know**, **judgment**, **so-what**, **confidence / caveat**, **A12**, and **WS-JLEE**. **TIP** means the shop store of indicators and reports. **RFI** means a request for information. **PRD APT** is a vendor label, not a country.

**Key Teaching Points:**
- A finished product is the judged answer, not a TIP paste or a hash dump.
- Structure is question, what you know, judgment, so-what, and confidence / caveat.
- A profile names the cluster. It does not invent a nation-state.

**Common Student Challenges:**
- Treat a TIP paste or hash list as finished. Why: it looks like a product because it is in a document. Example: pasting SHA256 values with no question, judgment, or so-what.
- Invent a country from a vendor APT name. Why: the PDF already named someone. Example: writing “nation-state PRD APT” on the A12 profile.
- Start picking the channel. Why: shipping feels like sending. Example: “put this on personal SMS so leadership sees it.” That is 2.11.2.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.11.1 – Creating finished intelligence products
- T: 2.11.1.1 – Draft a finished product and evaluate it against standards
- T: 2.11.1.2 – Produce a threat actor profile

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Finished product is the judged answer, not a paste |
| Key Concepts            | 12 min    | Types, structure, standards; draft + profile |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~21 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: someone needs the judged answer on the page. A TIP paste is not that product.
- Name the three types. Pick the one that matches the requirement. An RFI response is a type; the RFI queue is 2.11.3.
- Walk the five elements. Stop there. Do not rewrite for leadership format (2.1.6) and do not pick a channel (2.11.2).
- Walk the A12 draft. Pass: likely the update domain is the payload host; IR has WS-JLEE; medium; Zeek A record plus the host file. Fail: a hash dump.
- Walk the cluster profile: encoded PowerShell, update domain, distinctive nameserver pair, victim WS-JLEE. Vendor APT name stays a label.
- If they write a country: that is 2.1.7 assessment misused as fact. Today the profile stays on the cluster.
- If they pick the channel: that is 2.11.2.
- If they start authoring STIX: that was 2.10. This lesson is the narrative product.

---

## Knowledge Check – Answer Key

1. **A TIP paste is a finished product. True or false?**  
   **Answer:** False.  
   **Explanation:** A TIP paste is a dump of indicators. A finished product answers a question with sourced facts, a judgment, a so-what, and a caveat.

2. **Name three required elements of a finished product.**  
   **Answer:** Any three of: question, what you know, judgment, so-what, confidence / caveat.  
   **Explanation:** Those five are the required structure. A hash dump has none of them.

3. **Write a three-line A12 profile that does not claim a country.**  
   **Answer:** The cluster uses encoded PowerShell, the update domain, and a distinctive nameserver pair. The victim host is WS-JLEE. The vendor APT name is a label only.  
   **Explanation:** That is the activity cluster. “Nation-state PRD APT” invents a government the evidence does not prove.

---

## Additional Instructor Resources

- Next: 2.11.2 Dissemination
