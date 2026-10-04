# Module 2.5.4 – Advanced DNS Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.5.4 – Advanced DNS  
**Subtitle:** Read the zone, then build defensible pivots  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is authoritative DNS: records published for the zone. It is separate from RDAP registration, Zeek DNS logs, and passive DNS history.

---

### Slide 2 – Three different DNS-adjacent data sources
**Title:** Know which data you are reading

**Registration:** RDAP / WHOIS  
**Authoritative DNS:** records the zone publishes  
**Observed/history:** telemetry and passive DNS

This lesson focuses on **authoritative DNS**.

**Speaker Notes:**  
Establish the boundary early so learners do not mix the previous lesson or Zeek fields into the SOA exercise.

---

### Slide 3 – SOA
**Title:** MNAME, RNAME, SERIAL

**MNAME** — name server designated as the original / primary source of zone data.  
**RNAME** — DNS-encoded mailbox of the person responsible for the zone.  
**SERIAL** — unsigned 32-bit version number of the zone.

Reference: [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html)

**Speaker Notes:**  
Use the standard definitions rather than simplifying them into ownership claims.

---

### Slide 4 – Read RNAME and SERIAL carefully
**Title:** Mailbox and version—not actor and timestamp

`hostmaster.cdn-test.net.` → simple rendering: `hostmaster@cdn-test.net`

A changed **SERIAL** means the zone version changed.

A date-looking serial may follow an operator convention, but DNS does not require it to be a timestamp.

**Speaker Notes:**  
Mention escaped-dot edge cases only briefly. The learner needs the basic mailbox concept and the evidence boundary.

---

### Slide 5 – Records of intelligence value
**Title:** Infrastructure you can pivot on

**NS** — authoritative name servers  
**A / AAAA** — addresses  
**CNAME** — aliases  
**MX** — mail exchangers  
**TXT** — published text / tokens  
**SRV** — service targets and ports

References: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html), [RFC 1035](https://www.rfc-editor.org/rfc/rfc1035.html), [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782.html)

**Speaker Notes:**  
Focus on what each record can expose as infrastructure rather than teaching full DNS administration.

---

### Slide 6 – Shared infrastructure has different evidentiary weight
**Title:** Ask: how distinctive is the match?

Same large managed-DNS provider → weak signal.

Same rare NS pair + same uncommon A + similar timing → stronger candidate relationship.

Same shared-cloud IP alone → often weak.

**Speaker Notes:**  
The relationship strengthens as multiple independent and distinctive features converge.

---

### Slide 7 – A12 pivot
**Title:** Candidate sibling, not automatic sibling

Update domain and `login-prd.net` share:

- `ns1.cdn-test.net`;
- `ns2.cdn-test.net`;
- `203.0.113.88`.

Defensible first statement:

**Candidate related domain based on shared DNS infrastructure; corroboration required.**

**Speaker Notes:**  
This replaces the old “same control” conclusion, which was too strong for the evidence provided.

---

### Slide 8 – Do not expand one address into a subnet
**Title:** One shared A record is not ownership of the /24

Observed:

Both domains resolve to `203.0.113.88`.

Not established:

The actor controls `203.0.113.0/24`.

Combine DNS with RDAP, telemetry, passive DNS, and other evidence before making broader infrastructure claims.

**Speaker Notes:**  
Connect directly to 2.5.3's network-holder distinction.

---

### Slide 9 – Knowledge Check and Summary
**Title:** DNS creates pivots; evidence establishes relationships

1. What do MNAME, RNAME, and SERIAL mean?  
2. SERIAL changes—what can you infer safely?  
3. Same NS pair + same A—what is the first defensible conclusion, and what determines how strong it is?


**Speaker Notes:**  
Use the instructor key. Listen for candidate/pivot language rather than ownership or attribution.

**Next:** [2.5.5 – Identifying Additional Adversary Infrastructure from Seed Indicators](../05-infra-pivot/student-guide.md).
