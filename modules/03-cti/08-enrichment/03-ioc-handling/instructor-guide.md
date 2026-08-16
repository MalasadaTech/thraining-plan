# Instructor Guide – Module 3.8.3 – IOC Handling and Enrichment Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.8.3 A / B / B · 3.8.3.1 1a / 2b / 3c · 3.8.3.2 1a / 1a / 2b  
- Hunter: 3.8.3 B / C / C · 3.8.3.1 3c / 4c / 4d · 3.8.3.2 1a / 2b / 3c  
- CTI: 3.8.3 B / C / C · 3.8.3.1 3c / 4c / 4d · 3.8.3.2 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Handle IOCs as objects: keep / expire / reject, **name** the next enrichment, and **link** a set. Fail hop-sentence redo, tool labs, and APT-name glue.

**Key Teaching Points:**
- CTI **3.8.3.1** and **3.8.3.2** both top at **4d**. 4d = why this object stays in (or out of) the set.
- Hunter **3.8.3.2** is **1a / 2b / 3c** — they should see the set, not author campaign tracking at 4d.
- SOC K is **A / B / B**. Do not collapse.
- **3.8.1** hop is a sibling sentence, not this product. If they write only the hop, fail the handle/enrich/link.

**Common Student Challenges:**
- Rewriting the 3.8.1 hop and calling it handling.
- Keeping the /24 or the 2019 IP.
- “Night Owl APT” as the link.
- Opening VT because “that’s enrichment.”

**Required Materials:**
- Student Guide (tray)
- Slide Deck
- Answer key (this guide)

---

## Learning Objectives

1. IOC ≠ TTP.
2. Keep / expire / reject.
3. Enrich line names a known tool/field.
4. Link objects, not names.

**Mapped Items:** K 3.8.3 · T 3.8.3.1 · T 3.8.3.2

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 8 min    | Not 3.8.1 / 3.9 redo |
| Handle + enrich + link         | 14 min   | a–d |
| Walkthrough Examples           | 14 min   | |
| Hands-On Exercise              | 18 min   | |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 3 if they glue with APT |

---

## Detailed Teaching Notes

**Talking Points:**
- Hold the 3.8.1 hop sentence. “That named a sibling. This hour *files* the objects.”
- Expire vs reject: expire = was an IOC, no longer useful; reject = never earned a slot.
- 4d on the link: same host + same A is a cite. The label is not.

**Question:**  
“What would put `evil-c2.net` on the keep list?”

---

## Hands-On Exercise – Instructor Guidance

**Handle:**

| Item | Call |
|------|------|
| A | **Keep** — cited domain |
| B | **Keep** — cited hash |
| C | **Expire** — 2019, no Harbor cite |
| D | **Reject** — shared /24 |
| E | **Reject** — not an IOC |

**Enrich:** A → RDAP/SOA/PDNS NS or A. B → VT Relations contacted hosts (named only). Fail a hop sentence.

**Link:** A+B+Run = same set (same host / payload path). E is not glue.

---

## Knowledge Check – Answer Key

1. **IOC vs TTP?**  
   **Answer:** Observable you handle (domain, hash, key). A TTP is behavior (**3.8.2**).  
   **Explanation:** Outline a.

2. **Expire vs reject?**  
   **Answer:** Expire = cited once, now stale. Reject = uncited, shared, or not an IOC.  
   **Explanation:** Outline b.

3. **Enrich line?**  
   **Answer:** IOC, known tool, field, what you hope to learn. Not the 3.8.1 hop. Not a live query.  
   **Explanation:** Outline c / 3.8.3.1.

4. **Same activity set?**  
   **Answer:** Shared cite on *this* card (same host, same A, same payload).  
   **Explanation:** Outline d / 3.8.3.2.

5. **Why not the APT name?**  
   **Answer:** A label is not a shared object.  
   **Explanation:** Example 3.

---

## Additional Instructor Resources

- Classroom tray (student guide)
- Next recommended module: 3.8.4 Threat relevance and organizational impact
