# Module 3.6.1 – Advanced DNS Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.6.1 A / A / B · 3.6.1.1 1a / 1a / 2b  
- Hunter: 3.6.1 B / C / C · 3.6.1.1 2b / 3c / 4c  
- CTI: 3.6.1 B / C / C · 3.6.1.1 3c / 4c / 4d  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Interpret an SOA** — name the fields that matter for intel.
2. Use **other advanced record types** (NS, MX, TXT, SRV) for enrichment value.
3. **Pivot** from those records to related infrastructure — and say what you still do not know.

**Mapped Proficiency Items:**
- K: 3.6.1 – Advanced DNS concepts (SOA and other records of intel value)
- T: 3.6.1.1 – Interpret an SOA record and use advanced DNS data to enrich or pivot

---

## 1. Key Concepts

**1.2.3** taught that SOA exists as a `qtype`. This hour is **what the SOA *says*** and how NS / MX / TXT / SRV support **infra analysis**. It is not RDAP registration (**3.5**). It is not historical A records (**3.3.2** Silent Push). It is not DGA or DNS tunneling.

**SOA (outline a) — Start of Authority for the *zone*:**

| Field | Meaning | Intel use |
|-------|---------|-----------|
| **MNAME** | Primary nameserver | Same MNAME on many names → same zone operator |
| **RNAME** | Admin mailbox (`hostmaster.cdn-test.net` = hostmaster@cdn-test.net) | Same RNAME → same admin identity (weak if generic) |
| **Serial** | Zone version (often YYYYMMDDnn) | Jumped today → zone just changed; not a file hash |
| **Refresh / retry / expire / minimum** | Slave-timer defaults | Unusual values can cluster cheap/bulletproof DNS; do not over-read |

**Interpret-line:**  
`MNAME | RNAME | serial (what it suggests) | pivot | do not claim`

**Other records of intel value (outline b) — classroom set.** A/AAAA are assumed. Do not make a 20-type catalog.

| Type | Intel value | Trap |
|------|-------------|------|
| **NS** | Delegation — who *serves* the zone | Shared CDN NS is weak alone |
| **MX** | Where mail goes | No MX ≠ “not phishing” |
| **TXT** | SPF/DKIM, verification tokens, odd strings | SPF `-all` is common; a unique token is a pivot |
| **SRV** | Service locators (`_sip._tcp` …) | Absence is normal |

**How they support analysis (outline c):** stack SOA **MNAME/RNAME** + **NS** (+ TXT token). Same stack on a second name is a **cluster** pivot. It is not a registrant (**3.5**) and not a nation-state (**3.1.7**).

**Classroom zone card — `nightowl-updates.net`:**

```
SOA  MNAME ns1.cdn-test.net
     RNAME hostmaster.cdn-test.net
     SERIAL 2026080101
     REFRESH 3600  RETRY 600  EXPIRE 86400  MINIMUM 300
NS   ns1.cdn-test.net, ns2.cdn-test.net
MX   (none)
TXT  "harbor-verify=nightowl"
```

**`login-nightowl.net`:** same SOA MNAME/RNAME and same NS; different TXT (none).

| This lesson | Other |
|-------------|-------|
| SOA fields + NS/MX/TXT/SRV *now* | Zeek `query` / DGA — **1.2.3** |
| Not created/registrar | **3.5** RDAP |
| Not historical A | **3.3.2** Silent Push |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Same MNAME+NS on two names → cluster | Serial treated as SHA256 |
| TXT `harbor-verify=nightowl` as a pivot | A-record-only “advanced DNS” |
| MX none → note it; keep pivoting NS/SOA | No MX ⇒ not malicious / not a domain |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Interpret SOA + Pivot (Expected)

**SOA** on `nightowl-updates.net` as on the card.

**Interpret:** MNAME `ns1.cdn-test.net`. RNAME `hostmaster@cdn-test.net`. Serial `2026080101` = zone dated 1 Aug 2026, first rev — *zone version*, not file identity.  
**Pivot:** other names with that MNAME/NS; search TIP for `cdn-test.net`.  
**Do not claim:** the registrant, a country, or that the serial is a malware hash.

### Example 2: Serial as Hash (Lead)

**Draft:** “Serial 2026080101 matches a Night Owl hash. Same family.”

**Fail.** Serial is a **zone counter**. Format overlap with a date is coincidence to a SHA256.  
**Lead:** Right object (SOA). Wrong meaning.

### Example 3: A Record Only (Lead)

**Draft:** “Advanced DNS: `nightowl-updates.net` A `203.0.113.88`.”

**Fail.** An A record is **1.2.3** basics, not this unit. Advanced here is SOA + NS/MX/TXT/SRV.  
**Fix:** pull the SOA/NS/TXT card, then (if needed) RDAP on the name (**3.5**) and PDNS on the A (**3.3.2**).

---

## 3. Hands-On Exercise

**Objective:** Interpret the SOA and stack records to pivot.

**Use the classroom zone cards.**

**Instructions:**

1. One sentence each for Examples 1–3: SOA meaning vs the fail.
2. **Interpret SOA** (task 1) for `nightowl-updates.net`: write the **interpret-line**.
3. **Enrich / pivot** (task 2): `records used | pivot | what you still do not know`.

   - A. `login-nightowl.net` (same MNAME/NS as the card).  
   - B. A third name with **different** NS and MNAME, only a generic SPF TXT `v=spf1 -all`.  
   - C. Someone uses the A record of `203.0.113.88` as the *only* “advanced DNS” finding.  
   - D. TXT `harbor-verify=nightowl` also appears on an unrelated-looking name.

4. Do not run RDAP. Do not pull historical A. Do not call B a cluster on SPF alone.
5. If A matches MNAME+NS, that is a **cluster** pivot, not attribution.

**Expected Outcome:**
- Three example summaries
- One SOA interpret-line
- Four enrich/pivot lines
- No WHOIS, no PDNS

---

## 4. Knowledge Check

1. What do **MNAME** and **RNAME** tell you, and what is the **serial** *not*?
2. Name two **other** record types in this lesson and one intel use for each.
3. When do two names look like the **same operator**, and when is that weak?
4. Why is “A `203.0.113.88`” not an advanced-DNS product?
5. Where do you look up **registration** vs **historical A**?

---

## 5. Summary

- Interpret SOA. Stack NS / MX / TXT / SRV. Pivot the stack.
- Serial ≠ hash. A record ≠ this unit.
- Next: **3.7** frameworks (advanced application).

---

## 6. References & Further Reading

- Related modules:
  - 3.5.1 – RDAP / WHOIS (previous)
  - 1.2.3 – DNS engine
  - 3.3.2 – Silent Push (PDNS)
  - 3.7.1 – ATT&CK for intelligence (next cluster)
- Local passive/active DNS SOP (optional — how you *fetch* the records)
