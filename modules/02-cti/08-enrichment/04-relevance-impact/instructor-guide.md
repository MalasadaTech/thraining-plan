# Instructor Guide – Module 2.8.4 – Threat Relevance and Organizational Impact

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.4 B / C / C ; 2.8.4.1 3c / 4c / 4d  
- Hunter: 2.8.4 B / C / C ; 2.8.4.1 2b / 3c / 4c  
- SOC: 2.8.4 A / B / B ; 2.8.4.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Write two sentences: whether a finding applies here, and what would change if it is true. No PIR. No country.

**Context (plain language):**

- What this lesson is for: CTI analysts say whether a finding matters here, not only whether it is technically interesting. After enrichment leaves a finding, someone still has to write the so-what for this shop.
- How it hooks to the lesson before: 2.8.3 handled the IOC as an object (keep, expire, enrich, or link).
- How it hooks to the lesson after: 2.9.1 is VirusTotal Relations and Behavior — a tool tab, not impact.
- Why we are doing it this way: write the so-what as two sentences so enrichment does not stop at “interesting.”
- What we are *not* doing in this lesson: writing or inventing a PIR list. Extracting TTPs. Attribution. Inventing a shop list of impact categories. No lab.
- Extra step: none.

Use the same names as the student guide: **relevance**, **impact**, **mission**, **assets**, and **platform**. A **PIR** is a priority intelligence requirement — a ranked question, not this product. The classroom company is a law firm with Windows workstations. **A12** on **WS-JLEE** is the given they already know. Do not turn it into the intro plot. Do not invent OT as architecture. Do not invent a DYA impact catalog.

**Key Teaching Points:**
- Relevance is mission, assets, and platform — does this finding apply here.
- Impact is the change that follows from this finding, not “crisis” and not a catalog.
- That pair is not TTP applicability, not a PIR, and not attribution.

**Common Student Challenges:**
- Treat relevance as writing a PIR. Why: both sound like “what matters.” Example: “PIR-01: nation-state targeting law firms” as the product of this lesson.
- Write a country as impact. Why: impact feels like “how bad.” Example: “nation-state crisis” instead of IR has the host.
- Extract a TTP ID as the product. Why: 2.8.2 already kept encoded PowerShell. Example: writing T1059.001 as the impact line.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.8.4 – Threat relevance and organizational impact
- T: 2.8.4.1 – Assess threat relevance and potential impact to the organization

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | So-what for this shop |
| Key Concepts            | 12 min    | Two sentences; A12 given |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: a finding can be technically interesting and still not matter here. This lesson writes whether it applies, and what would change if it is true.
- Write relevance as mission, assets, and platform. Stop. Do not turn those three words into a shop catalog.
- Write impact as the change that follows from this finding. Concrete: IR has the host; the payload path is live. Not “crisis.”
- Walk the A12 given from the student guide. The product is two sentences, not the incident story.
- Walk the OT-wipe reject: not this platform, so not relevant, so impact is none here. Do not invent OT as something this shop runs.
- If they write a country or a vendor “APT” name: that is 2.1.7. This lesson is not attribution.
- If they extract T1059.001: that is 2.8.2. This lesson is not the TTP keep/reject.
- If they write PIR-01 or invent a shop PIR list: that is 2.1.4 / 2.12.1. This lesson is not the question list.
- If they start a list of DYA impact categories (mail, clients, payroll, OT): write the change that follows from this finding. Do not publish a catalog.

---

## Knowledge Check – Answer Key

1. **Relevance is the same as writing a PIR. True or false?**  
   **Answer:** False.  
   **Explanation:** Relevance is whether this finding applies to this mission, assets, and platform. A PIR is a ranked question the shop wants answered. That list is 2.1.4 / 2.12.1, not this product.

2. **What two sentences do you write?**  
   **Answer:** Relevance (does this finding apply here?) and impact (if it is true, what would change here?).  
   **Explanation:** That pair is the so-what. It is not a TTP list, a PIR, or a country.

3. **Given encoded PowerShell and an update-domain fetch on WS-JLEE (A12). One relevance sentence and one impact sentence.**  
   **Answer:** Relevant: Windows workstation shop; we already saw it on that host. Impact: IR has the host; the payload path is live on a user workstation. No country. No PIR.  
   **Explanation:** The task is the two sentences for this organization. OT wipe would be not relevant, with no impact here — that is the reject, not this given.

---

## Additional Instructor Resources

- Next: 2.9.1 VirusTotal Relations and Behavior
