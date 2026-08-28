# Instructor Guide – Module 2.9.3 – Silent Push

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.9.3 B / C / C ; 2.9.3.1 3c / 4c / 4d  
- Hunter: 2.9.3 A / B / B ; 2.9.3.1 2b / 3c / 4c  
- SOC: 2.9.3 A / A / B ; 2.9.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Read Silent Push for passive DNS and infrastructure context on a classroom card. Enrich a seed. Pivot only to names the card shows. Reject the whole `/24`.

**Context (plain language):**

- What this lesson is for: CTI analysts already have a seed — a domain or IP from the case. They open Silent Push to see the passive DNS history around that seed and any related infrastructure the product actually lists. This lesson is enrich the seed from the classroom card, then pivot only to extra names the card shows.
- How it hooks to the lesson before: 2.9.2 was AnyRun — a sandbox submission card.
- How it hooks to the lesson after: 2.9.4 is URLScan — a page-scan card.
- Why we are doing it this way: 0.7 already taught when to pick Silent Push. This lesson is the platform: what you read on the card, and what a good enrich and pivot look like. Classroom card only, so no live vendor account.
- What we are *not* doing in this lesson: the 0.7 survey (purpose / when to pick). RDAP (2.5). SOA (2.6). The hop sentence as the product (2.8.1). Hunt conversion to SIEM or Zeek (3.3.1). No live account. No lab.
- Extra step: none.

Use the same names as the student guide: **seed**, **passive DNS** (PDNS), **A** record, **NS** (nameserver), **enrich**, **pivot**, and **classroom result card**. **PDNS** is the gloss for historical DNS resolutions, not the headline word. The given uses course-fiction names (`203.0.113.88`, the update domain, `login-prd.net`). Do not turn it into the intro plot.

**Key Teaching Points:**
- Silent Push is passive DNS and infrastructure context, not a sandbox and not a page scan.
- Enrich the seed. Pivot only to names the card shows.
- Names on `203.0.113.88` are a take if they are on the card. The whole `/24` is a reject.

**Common Student Challenges:**
- Treat the whole `/24` as extra adversary infrastructure. Why: neighboring IPs look related. Example: writing `203.0.113.0/24` as theirs after enriching `.88`.
- Invent a sibling that is not on the card. Why: they remember the hop from 2.8.1. Example: adding `login-prd.net` when this card does not list it.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 2.9.3 – Silent Push
- T: 2.9.3.1 – Enrich an indicator and pivot in Silent Push

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Seed, passive DNS, classroom card |
| Key Concepts            | 12 min    | Capabilities; enrich / pivot; take vs reject |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: they already have a seed, and they open Silent Push for passive DNS history and related infrastructure.
- Write the three capabilities. Stop. Do not re-teach when to pick Silent Push versus URLScan.
- Walk enrich versus pivot. Enrich is what the card says about this seed. Pivot is extra names that share an A or an NS pair **on the card**.
- Walk the given: enrich `203.0.113.88`. Take the update domain and `login-prd.net` if they are on the card. Reject the whole `/24`.
- If they start the 0.7 survey: that lesson already happened. Today is what you read in Silent Push.
- If they write an SOA or RDAP field as the product: that is 2.6 or 2.5. Stay on the Silent Push card.
- If they write the four-part hop sentence as the product: that is 2.8.1. Here the product is the enrich line and the on-card pivot.
- If they ask for a live login: there is no live account in this lesson.

---

## Knowledge Check – Answer Key

1. **This lesson is “when to pick Silent Push.” True or false?**  
   **Answer:** False. When to pick it is 0.7.  
   **Explanation:** This lesson is what you read in Silent Push: enrich the seed and pivot only to names the card shows.

2. **What two jobs do you do in Silent Push?**  
   **Answer:** Enrich the seed. Pivot to other names or IPs the card shows.  
   **Explanation:** Enrich is history on the indicator you already have. Pivot is extra infrastructure that shares an A or an NS pair on this card.

3. **Enrich `203.0.113.88`. One legal pivot, and one thing you must reject.**  
   **Answer:** Legal: names on that A that the card lists (the update domain, maybe `login-prd.net`). Reject: the whole `/24`.  
   **Explanation:** Neighboring IPs on shared hosting are not extra adversary infrastructure. If a name is not on the card, write “not on the card.”

---

## Additional Instructor Resources

- Next: 2.9.4 URLScan
