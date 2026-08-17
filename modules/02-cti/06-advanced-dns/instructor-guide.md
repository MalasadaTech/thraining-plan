# Instructor Guide – Module 3.6.1 – Advanced DNS Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.6.1 A / A / B · 3.6.1.1 1a / 1a / 2b  
- Hunter: 3.6.1 B / C / C · 3.6.1.1 2b / 3c / 4c  
- CTI: 3.6.1 B / C / C · 3.6.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach SOA field meaning and a small set of other records for **enrich/pivot**. Do not re-teach Zeek DNS or RDAP.

**Key Teaching Points:**
- Classroom zone card is a stand-in. Overlay a live `dig SOA` if you can.
- Serial is a zone version, not a file hash.
- A-record-only is **1.2.3**, not this unit.
- Hunter K is **B / C / C** (higher than 3.5). Task **2b / 3c / 4c**. CTI task **3c / 4d**. Do not collapse.
- Same MNAME+NS = cluster, not country.

**Common Student Challenges:**
- Serial = hash / WHOIS created.
- Calling A-record work “advanced DNS.”
- Clustering on generic SPF only.
- Opening Silent Push or RDAP.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional live `dig SOA` / `dig NS` on a *safe* name
- Answer key (this guide)

---

## Learning Objectives

1. Interpret SOA fields.
2. NS / MX / TXT / SRV intel value.
3. Stack them to pivot.

**Mapped Items:** K 3.6.1 · T 3.6.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 1.2.3-as-whole / 3.5 / 3.3.2 |
| SOA + other types + how        | 16 min   | a–c |
| Walkthrough Examples           | 14 min   | Live dig if possible |
| Hands-On Exercise              | 18 min   | Interpret + pivot |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 2 if they hash the serial |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *decode RNAME* and *refuse* serial-as-hash.
- RNAME: first `.` → `@`. `hostmaster.cdn-test.net` → hostmaster@cdn-test.net.

**Question:**  
“Two names share MNAME and NS but RDAP registrars differ. What did DNS give you that WHOIS did not?” (Operator of the *zone*, not the *registrant*.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail serial-as-hash. Fail A-only. Fail SPF-only cluster.

**Summaries:**
- Ex 1: MNAME/RNAME/serial; NS pivot; no country.
- Ex 2: serial ≠ hash.
- Ex 3: A is not this unit.

**SOA interpret (`nightowl-updates.net`):**  
MNAME `ns1.cdn-test.net` | RNAME hostmaster@cdn-test.net | serial 2026080101 = zone rev 1 Aug 2026 | pivot other names on that MNAME/NS | not a hash, not a registrant.

**Pivot:**

| Item | Records | Pivot | Still unknown |
|------|---------|-------|----------------|
| A | SOA MNAME + NS match | Cluster / same operator | Registrant, actor name |
| B | Only generic SPF | **Weak / no cluster** | Almost everything |
| C | A only | **Wrong unit** — send back to SOA/NS/TXT | — |
| D | Unique TXT token | Search that string on other names | Whether it is the same *campaign* |

---

## Knowledge Check – Answer Key

1. **MNAME / RNAME / serial is not?**  
   **Answer:** Primary NS; admin mailbox (dot → @). Serial is zone version, **not** a file hash or WHOIS created date.  
   **Explanation:** Outline a.

2. **Two other types + use?**  
   **Answer:** NS = who serves the zone. MX = mail infra. TXT = tokens/SPF. SRV = service locators. (Any two.)  
   **Explanation:** Outline b.

3. **Same operator vs weak?**  
   **Answer:** Same MNAME+NS (and maybe unique TXT) is a cluster. Shared huge CDN NS or generic `v=spf1 -all` alone is weak.  
   **Explanation:** Outline c / A vs B.

4. **Why not A-only?**  
   **Answer:** A/AAAA are **1.2.3** basics. This unit is SOA + NS/MX/TXT/SRV.  
   **Explanation:** Example 3.

5. **Registration vs historical A?**  
   **Answer:** **3.5** RDAP. **3.3.2** Silent Push.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- Local `dig` / passive-DNS SOP (fetch only)
- Next recommended module: 3.7.1 ATT&CK for intelligence
