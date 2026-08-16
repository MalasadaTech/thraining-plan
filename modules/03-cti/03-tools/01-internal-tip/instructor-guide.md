# Instructor Guide – Module 3.3.1 – Internal Threat Intelligence Platform

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.3.1 A / A / B · 3.3.1.1 1a / 1a / 2b  
- Hunter: 3.3.1 A / B / B · 3.3.1.1 1a / 2b / 3c  
- CTI: 3.3.1 B / C / C · 3.3.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach purpose, search/navigate, and force **retrieve + enrich**. Do not teach VT/Silent Push or STIX authoring.

**Key Teaching Points:**
- Harbor TIP is a stand-in. Overlay live screens if you have them.
- Retrieve ≠ enrich. Opening the page is not task 2.
- VT is **3.3.2**. Ticket notes are **1.8.4**.
- SOC 3-level task is **1a / 1a / 2b**. Hunter 3-level is **1a**. CTI is **3c / 4d**. Do not collapse.
- 403 → point at **1.8.3**, do not teach IAM here.

**Common Student Challenges:**
- VT as the TIP.
- Search without opening the object (no retrieve).
- Read-only — never add the new sighting.
- Dumping the whole tenant.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional live TIP (read-only demo) or screenshots
- Answer key (this guide)

---

## Learning Objectives

1. Purpose and functions.
2. Navigate and search.
3. Retrieve.
4. Enrich / analyze with a link or sighting.

**Mapped Items:** K 3.3.1 · T 3.3.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.3.2 / 3.10 / 1.8.4 |
| Purpose, search, three uses    | 16 min   | a–c |
| Walkthrough Examples           | 14 min   | Live search if possible |
| Hands-On Exercise              | 18 min   | Retrieve + enrich |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they defend VT |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *name the query* and *name the link*, not “I would use the TIP.”
- If you have a live tenant, run Example 1 on the projector with a **sanitized** indicator.

**Question:**  
“If the SNI is in the TIP with zero sightings, what does retrieve tell you — and what must enrich add when WS-JLEE hits?”

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail VT. Fail open-and-leave. Accept site object IDs if they overlay.

**Summaries:**
- Ex 1: query SNI, open IND-1882, list fields + sightings.
- Ex 2: VT is the wrong store.
- Ex 3: must add WS-JLEE sighting.

**Retrieve:**

| Item | Query | Open | Retrieved |
|------|-------|------|-----------|
| A | `a0e9f5…` / type Indicator | The JA3 indicator (or “none”) | Fields + linked cluster if any. “None” is a valid retrieve — then create is a site SOP (do not invent a 3.12 process). |
| B | tag `night-owl` | Cluster + member indicators | List object types returned |

**Use:**

| Item | Object | Add / link | Why |
|------|--------|------------|-----|
| C | IND-1882 (+ new hash indicator if needed) | Sighting WS-JLEE / EDR / time; link `6734f374…` | Next shift can see the host hit |
| D | IND-1882 + sightings | Pull prior hosts, tag, TLP, last seen into the SOC note | Analysis uses *our* hits, not a VT score |

---

## Knowledge Check – Answer Key

1. **What problem does the TIP solve?**  
   **Answer:** What *we already hold* and how objects link. SIEM is live telemetry. VT is external.  
   **Explanation:** Outline a.

2. **Three functions?**  
   **Answer:** Store, search, link (and support production).  
   **Explanation:** Outline a.

3. **Retrieve vs enrich?**  
   **Answer:** Retrieve = open and read. Enrich = add a sighting or link so the store changes.  
   **Explanation:** Tasks 1–2 / Example 3.

4. **Why not VT?**  
   **Answer:** Different store. Internal presence is this TIP. VT is **3.3.2**.  
   **Explanation:** Fence / Example 2.

5. **Notes vs TIP?**  
   **Answer:** Working notes = ticket (**1.8.4**). TIP = intel objects. Link the TIP ID in the ticket.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local TIP SOP / demo tenant
- Next recommended module: 3.3.2 External tools
