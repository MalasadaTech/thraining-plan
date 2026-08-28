# Module 2.8.1 – Identifying additional adversary infrastructure from seed indicators  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 2.8.1 – Identifying additional adversary infrastructure  
**Subtitle:** Hop from a seed to more infrastructure  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
2.7.4 recorded the DTF ID line. This lesson is the hop sentence without those IDs. It does not re-teach RDAP, SOA, Silent Push, or VirusTotal.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

You already have a **seed** — a domain, an IP, or another indicator.

One seed is rarely the whole picture. Hop to other **adversary infrastructure**: what you share, what you found, and why it is not coincidence.

Select and record enrichment. Do not re-teach the tool.

**Speaker Notes:**  
This slide is the student intro. The job is the sentence, not a tool demo and not a DTF P-ID. Sources already taught stay named, not re-taught.

---

### Slide 3 – Hop sentence
**Title:** Seed, shared characteristic, candidate

A **seed** is the indicator you already have. To **pivot** (hop) is to use a **shared characteristic** to find more infrastructure.

**Hop sentence:** `seed | shared characteristic | candidate | why not coincidence`

The shared thing has to be distinctive. A public nameserver or a shared cloud range is coincidence.

**Speaker Notes:**  
Write the four parts and stop. If they add a PTA/P code, that is 2.7.4. If they chain hops into a campaign, that is 2.8.3.

---

### Slide 4 – Common source classes
**Title:** Name the source. Do not operate it.

**Registration** — nameservers, registrar, created date.  
**DNS** — who runs the zone; same NS or A.  
**Same A** — other names that resolved to this IP.  
**TLS certificate** — other names on the same cert.  
**HTTP title** — same page title or resources.

You name the class. You do not re-teach **0.7** or **2.9**.

**Speaker Notes:**  
Name each class in ordinary words. This is not a lookup walkthrough. Registration was 2.5. SOA was 2.6. Silent Push and VirusTotal Relations wait. If they open a tool, name the class and come back to the sentence.

---

### Slide 5 – Take vs reject
**Title:** Take vs reject

**Take** — update domain / `203.0.113.88`. Distinctive NS pair `ns1.cdn-test.net` / `ns2.cdn-test.net` → `login-prd.net`. Not a public resolver.

**Reject** — whole `203.0.113.0/24`. Shared hosting.

**Speaker Notes:**  
Show this given before the knowledge check. Same A on that named sibling can support the hop. The `/24` still is not theirs. Four parts, not a P-ID.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. This lesson requires a DTF P-ID on the hop. True or false?  
2. What four parts does a hop sentence have?  
3. You have the update domain / `203.0.113.88`. Shared nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net` point at `login-prd.net`. Write the hop, or say why you would reject the whole `203.0.113.0/24`.

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Seed → shared characteristic → candidate → why not coincidence.  
Shared `/24` is not a hop.  
Name the source class. Do not re-teach the tool.

**Next:** **2.8.2** Applicable TTPs

**Speaker Notes:**  
2.8.2 is TTPs that apply here. Stay off the hop sentence when you get there.
