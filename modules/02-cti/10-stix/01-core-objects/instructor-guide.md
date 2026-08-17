# Instructor Guide – Module 3.10.1 – Core STIX Objects

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.10.1 A / B / B · 3.10.1.1 1a / 1a / 2b  
- Hunter: 3.10.1 B / C / C · 3.10.1.1 2b / 3c / 4c  
- CTI: 3.10.1 B / C / C · 3.10.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Full STIX 2.1 inventory for CTI: **label** report spans with the correct type. Reject neighbor types and vendor-name Threat Actor.

**Key Teaching Points:**
- Do not re-teach 2.4.3 hunt-relevant slice. One sentence: hunters keep a subset; you label the set.
- Real types only. Invented `ioc` / `apt` fails.
- SOC K is **A / B / B**. Hunter/CTI task **2b / 3c / 4c** and **3c / 4c / 4c** — not 4d (that is 3.10.2 graphs).
- Do not draw relationships or mention TAXII except as “next hour.”
- Cover all eleven types on the card even if the exercise is seven lines.

**Common Student Challenges:**
- Indicator = the log row.
- Vendor APT = threat-actor.
- Attack-pattern = campaign.
- Sighting = a second indicator.
- Writing hunt leads or a 3.11 narrative.

**Required Materials:**
- Student Guide (type card)
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. Eleven real types.
2. Label + reject neighbor.
3. Empty threat-actor is success.

**Mapped Items:** K 3.10.1 · T 3.10.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 2.4.3 / 3.10.2 / 3.11 |
| Eleven types                   | 16 min   | a–k |
| Walkthrough Examples           | 12 min   | |
| Hands-On Exercise              | 18 min   | Label lines |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they keep the APT name |

---

## Detailed Teaching Notes

**Talking Points:**
- Hash *pattern* = indicator. The file on disk = malware. The Zeek row = observed-data. Three objects, one story.
- Intrusion-set as “unattributed Night Owl cluster” is allowed if they say it is *not* a who. Nation-state is **3.1.7**.
- Relationship exists on the card so they know the type; they do not fill `relationship_type` until **3.10.2**.

**Question:**  
“What would have to appear in the Harbor excerpt before **threat-actor** is legal *here*?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail invented types. Fail C as threat-actor. Fail B as indicator.

**Labels:**

| Item | Type | Reject |
|------|------|--------|
| A | **indicator** | observed-data |
| B | **observed-data** | indicator |
| C | **None / empty threat-actor** | vendor name |
| D | **attack-pattern** | campaign |
| E | **sighting** | indicator |
| F | **course-of-action** | sighting |
| G | **identity** | malware |

---

## Knowledge Check – Answer Key

1. **Indicator vs observed-data?**  
   **Answer:** Indicator = reusable *pattern* to look for. Observed-data = a *sample* of what was seen.  
   **Explanation:** Outline a–b.

2. **Empty threat-actor?**  
   **Answer:** When the report does not earn a who. Vendor “APT” is not enough.  
   **Explanation:** Example 2 / outline e.

3. **Why not campaign?**  
   **Answer:** T1059.001 is a *how* (attack-pattern). A campaign is a time-bounded operation the report must name.  
   **Explanation:** Outline d / g.

4. **Sighting points at?**  
   **Answer:** Another STIX object that was *seen* (usually an indicator). It is not the pattern itself.  
   **Explanation:** Outline k.

5. **Where do you link them?**  
   **Answer:** **3.10.2**.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- STIX 2.1 object types (lookup)
- Next recommended module: 3.10.2 STIX in production
