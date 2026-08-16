# Module 3.5.1 – RDAP and WHOIS Concepts

**Target Audience:** CTI Analyst (primary), Threat Hunter (secondary)  
**Proficiency Focus:**  
- SOC: 3.5.1 A / A / B · 3.5.1.1 1a / 1a / 2b  
- Hunter: 3.5.1 A / B / B · 3.5.1.1 2b / 3c / 4c  
- CTI: 3.5.1 B / C / C · 3.5.1.1 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain **why** WHOIS and RDAP exist.
2. State the **key differences** between them.
3. **Query** RDAP (preferred) or WHOIS for a domain or IP.
4. **Extract and interpret** fields for enrichment or attribution — including what redaction does *not* mean.

**Mapped Proficiency Items:**
- K: 3.5.1 – RDAP and WHOIS concepts
- T: 3.5.1.1 – Query RDAP/WHOIS and interpret fields for enrichment or attribution

---

## 1. Key Concepts

Registration data answers “who *registered* this domain or *holds* this IP block?” It is not passive DNS history (**3.3.2** Silent Push) and not an SOA record (**3.6**). It does not, by itself, name a nation-state (**3.1.7**).

**Purpose (outline a):**

| System | Purpose |
|--------|---------|
| **WHOIS** | Legacy registration lookup (often free text on port 43 or a web form) |
| **RDAP** | Modern, structured registration lookup (HTTPS + JSON, standard objects) |

You query so you can **enrich** (age, registrar, nameservers, IP org) and **support** attribution (same registrant/NS/abuse box across domains) — not to declare the actor.

**Key differences (outline b):**

| | WHOIS | RDAP |
|--|-------|------|
| Format | Unstructured text; every registrar looks different | Structured objects (JSON) |
| Access | Port 43 / random web WHOIS | HTTPS, standard bootstrap |
| Privacy | Inconsistent redaction | Privacy/redaction is normal and labeled |
| Status | Still everywhere; parse at your peril | Preferred when it answers |

**Classroom query order:** RDAP first (`https://rdap.harbor.internal` stand-in, or the public bootstrap). If RDAP is empty or the TLD has no RDAP, fall back to WHOIS and say so. Overlay the site tool if posted.

**Key fields (outline c):**

| Field | Enrichment use | Attribution use | Trap |
|-------|----------------|-----------------|------|
| **Created / updated / expiry** | Young domain; churn | Same create-day cluster | Expiry ≠ “they’re gone” |
| **Registrar** | Where it was bought | Same registrar *plus* other lines | Popular registrar ≠ actor |
| **Registrant / org** | Rarely present now | Strong *if* real and repeating | **Redacted** ≠ no intel; ≠ country |
| **Nameservers** | Infra pivot | Shared NS across a cluster | Shared CDN NS is weak |
| **Status** | lock / hold / pending delete | — | Not a verdict |
| **Abuse contact** | Who to notify | Same abuse box on many names | Often the registrar’s |
| **IP: CIDR / org / country** | Hosting type (cloud vs ISP) | Same org *and* unusual pattern | Cloud org ≠ the adversary |

**Query line:** `object | RDAP or WHOIS | why that one`  
**Interpret line:** `fields kept | enrichment | attribution support | what you must not claim`

| This lesson | Other |
|-------------|-------|
| Registration data | Historical A / siblings — **3.3.2** Silent Push |
| Not SOA / MX / TXT meaning | **3.6** / **1.2.3** |
| Fields *support* attribution | Cluster vs country — **3.1.7** |

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| RDAP first; keep created + NS + registrar | “WHOIS is redacted so skip it” |
| Cloud IP org = hosting, not the actor | Redacted registrant → “it’s China” |
| Young domain + shared NS = enrichment | Treating WHOIS text as RDAP structure |

---

## 2. Detailed Walkthrough / Examples

**Classroom RDAP cards (this lesson only):**

**Domain `nightowl-updates.net`**  
Created: 14 days ago. Registrar: Harbor Registrar. Registrant: **redacted**. NS: `ns1.cdn-test.net`, `ns2.cdn-test.net`. Status: `clientTransferProhibited`. Abuse: `abuse@harbor-registrar.example`.

**IP `203.0.113.88`**  
CIDR: `203.0.113.0/24`. Org: Example Cloud LLC. Country: US. Allocated: 2019. No domain-style registrant.

### Example 1: Domain RDAP (Expected)

**Query:** RDAP for `nightowl-updates.net` (preferred).  
**Keep:** created 14 days, Harbor Registrar, `cdn-test.net` NS, transfer lock.  
**Enrichment:** young name + those NS — check other Night Owl names for the same NS.  
**Attribution:** supports a **cluster** of recently registered names on that NS. Does **not** name a person or a country (registrant redacted).

### Example 2: Redacted = Skip (Lead)

**Draft:** “WHOIS is privacy-protected. No intel.”

**Fail.** Redaction is expected. You still have created, registrar, NS, status, abuse.  
**Lead:** Privacy is a *field outcome*, not an empty query.

### Example 3: Cloud Org as Actor (Lead)

**Draft:** “203.0.113.88 is Example Cloud LLC in the US — the actor is that company.”

**Fail.** IP RDAP names the **holder of the block** (a VPS provider). That is hosting enrichment. Attribution to the *cloud company as Night Owl* is wrong.  
**Query was fine** (RDAP on the IP). **Interpret** failed.

---

## 3. Hands-On Exercise

**Objective:** Query, then interpret — including redaction and cloud IP.

**Use the classroom cards.** Overlay a live RDAP query if the instructor runs one.

**Instructions:**

1. One sentence each for Examples 1–3: query + what you may / may not claim.
2. **Query** (task 1): `object | RDAP or WHOIS | why`.

   - A. `nightowl-updates.net`  
   - B. `203.0.113.88`  
   - C. A TLD the classroom card says has **no RDAP** (use `old-whois-only.example`).

3. **Interpret** (task 2): write the **interpret line** for A, B, and:

   - D. Same domain card, but someone concludes “redacted ⇒ nation-state.”  
   - E. A second name `login-nightowl.net` with the **same NS and create week** (no registrant).

4. Do not pull historical A records (Silent Push). Do not read an SOA. Do not assign Admiralty (**3.2.3**) unless you *label* that you left this unit.
5. If two names share only a huge registrar (GoDaddy-scale) and nothing else, say **weak**.

**Expected Outcome:**
- Three example summaries
- Three query lines
- Three interpret lines (A, B, D/E — D is a fail claim; E is cluster support)
- No PDNS, no SOA

---

## 4. Knowledge Check

1. What problem do WHOIS and RDAP exist to solve?
2. Give **two differences** between WHOIS and RDAP. Which do you try first?
3. Name four **fields** you still have when the registrant is redacted.
4. Why is the **cloud org** on an IP RDAP not the adversary?
5. Where is **historical DNS** taught, versus registration data?

---

## 5. Summary

- RDAP first. Structured fields. Redacted ≠ empty.
- Enrichment vs what you must not claim.
- Next: **3.6** advanced DNS.

---

## 6. References & Further Reading

- Related modules:
  - 3.4.1 – File similarity (previous)
  - 3.6.1 – Advanced DNS (next)
  - 3.3.2 – Silent Push (PDNS)
  - 3.1.7 – Attribution
- Local RDAP/WHOIS tool / bootstrap (optional — substitutes Harbor URL)
