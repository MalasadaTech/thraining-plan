# Instructor Guide – Module 3.5.1 – RDAP and WHOIS Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.5.1 A / A / B · 3.5.1.1 1a / 1a / 2b  
- Hunter: 3.5.1 A / B / B · 3.5.1.1 2b / 3c / 4c  
- CTI: 3.5.1 B / C / C · 3.5.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  
**Delivery Method:** Instructor-led with hands-on analysis

---

## Module Overview for Instructors

**Purpose of this module:**  
Teach purpose, WHOIS vs RDAP, and force **query + interpret**. Do not teach SOA or Silent Push.

**Key Teaching Points:**
- Classroom cards are stand-ins. Overlay a live RDAP query if you can.
- RDAP first; WHOIS if no RDAP.
- Redacted ≠ skip. Cloud org ≠ actor.
- Hunter 3-level task is **2b** (not 1a). CTI is **3c / 4c**. SOC is **1a / 2b**. Do not collapse.
- Fields *support* a cluster; they do not earn **3.1.7** nation-state.

**Common Student Challenges:**
- Skipping redacted records.
- Country on an IP block as attribution.
- WHOIS-only habit when RDAP exists.
- Pulling PDNS or SOA.

**Required Materials:**
- Student Guide
- Slide Deck
- Optional live `rdap` / browser bootstrap on a *safe* domain
- Answer key (this guide)

---

## Learning Objectives

1. Purpose of WHOIS and RDAP.
2. Differences; RDAP first.
3. Query.
4. Interpret fields; refuse the over-claim.

**Mapped Items:** K 3.5.1 · T 3.5.1.1

---

## Suggested Timing

| Section                        | Time     | Notes |
|--------------------------------|----------|-------|
| Introduction & fence           | 6 min    | Not 3.6 / 3.3.2 / 3.1.7 |
| Purpose, differences, fields   | 16 min   | a–c |
| Walkthrough Examples           | 14 min   | Live query if possible |
| Hands-On Exercise              | 18 min   | Query + interpret |
| Knowledge Check & Discussion   | 8 min    | |
| Summary                        | 4 min    | |
| **Total**                      | **~66 min** | Stretch Ex 3 if they blame the cloud |

---

## Detailed Teaching Notes

**Talking Points:**
- CTI 3: 3c — they should *keep four fields from a redacted record* and *refuse* the country jump.
- If you demo live WHOIS vs RDAP on the same name, show the parse pain.

**Question:**  
“Same NS and create week on two names, both redacted. What *can* you say, and what word do you still not get to use?” (Cluster / related infra. Not nation-state.)

---

## Hands-On Exercise – Instructor Guidance

**How to run:** Fail skip-on-redacted. Fail cloud-as-actor. Fail C as RDAP if the card says none.

**Summaries:**
- Ex 1: RDAP; young + NS; cluster only.
- Ex 2: still have fields.
- Ex 3: hosting, not actor.

**Query:**

| Item | System | Why |
|------|--------|-----|
| A | **RDAP** | Preferred; TLD has RDAP |
| B | **RDAP** | IP objects are RDAP too |
| C | **WHOIS** | Card says no RDAP — say the fallback |

**Interpret:**

| Item | Keep | May claim | Must not |
|------|------|-----------|----------|
| A | created, registrar, NS, status, abuse | Young name; NS pivot | Person / country |
| B | CIDR, Example Cloud, US, 2019 | Hosting type | Actor = the cloud |
| D | (same as A) | — | **Nation-state** from redaction |
| E | shared NS + create week | **Cluster** support | Identity of a registrant |

---

## Knowledge Check – Answer Key

1. **Why WHOIS/RDAP?**  
   **Answer:** Registration / allocation data for a domain or IP — who registered or holds the block.  
   **Explanation:** Outline a.

2. **Two differences / first?**  
   **Answer:** Structured JSON vs free text; HTTPS vs port 43 / random pages; labeled privacy. **RDAP first.**  
   **Explanation:** Outline b.

3. **Four fields when redacted?**  
   **Answer:** Created/updated/expiry, registrar, nameservers, status, abuse (any four).  
   **Explanation:** Outline c / Example 2.

4. **Why not the cloud org as actor?**  
   **Answer:** IP RDAP names the **address holder** (often a VPS). That is hosting, not the operator.  
   **Explanation:** Example 3.

5. **Historical DNS?**  
   **Answer:** **3.3.2** Silent Push — not this lookup.  
   **Explanation:** Fence.

---

## Additional Instructor Resources

- IANA RDAP bootstrap / site WHOIS tool
- Next recommended module: 3.6.1 Advanced DNS
