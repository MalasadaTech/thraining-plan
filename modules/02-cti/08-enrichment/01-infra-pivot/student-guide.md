# Module 2.8.1 – Identifying additional adversary infrastructure from seed indicators

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- Hunter: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4d  
- SOC: 2.8.1 A / B / B ; 2.8.1.1 1a / 2b / 3c  
**Estimated Time:** 20–25 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Write a **hop sentence** from a seed: what you share, what you found, and why it is not coincidence.
2. Name a common source class for that hop — without re-teaching RDAP, SOA, Silent Push, or VirusTotal.

**Mapped Proficiency Items:**
- K: 2.8.1 – Identifying additional adversary infrastructure from seed indicators
- T: 2.8.1.1 – Pivot from a seed indicator to additional adversary infrastructure

---

## 1. Key Concepts

CTI analysts start from a **seed** they already have — a domain, an IP, or another indicator from an RFI, a report, or an incident. One seed is rarely the whole picture. The job in this lesson is to hop from that seed to other **adversary infrastructure**: write what you share, what you found, and why it is not coincidence. You **select and record** enrichment from sources already taught. You do not re-teach the tools (**0.7** / **2.9**). You do not write a DTF ID (**2.7.4**).

A **seed** is the indicator you already have. To **pivot** (also: hop) is to use a **shared characteristic** of that seed to find more infrastructure. The extra name or IP you find is a **candidate**. The product is a **hop sentence** — the four-part line you record — not a tool demo and not a DTF P-ID (the PTA/P code from **2.7.4**).

**Hop sentence:** `seed | shared characteristic | candidate | why not coincidence`

The shared characteristic has to be distinctive enough that two names sharing it is not luck. A public nameserver, a shared cloud range, or an uncited vendor label is coincidence. Stop after one cited hop. Do not turn this lesson into campaign tracking (**2.8.3**) or a TTP extract (**2.8.2**).

**Common source classes.** Name the class and what you hope to learn. You do not operate these tools here.

| Source class | What you hope to learn |
|--------------|------------------------|
| **Registration** | Nameservers, registrar, created date |
| **DNS** | Who runs the zone; other names with the same NS or A |
| **Same A** | Other names that resolved to this IP |
| **TLS certificate** | Other names on the same cert (SAN / issuer) |
| **HTTP title** | Same page title or resources on another host |

Registration was **2.5**. SOA and zone DNS were **2.6**. Silent Push and the other external tools were **0.7**; platform depth (VirusTotal Relations, Silent Push pivots) is **2.9**. This lesson names the class. It does not re-teach the lookup.

**What good looks like:** someone gives you a seed. You write the hop, or you reject the weak neighbor. You do not open a tool class.

- **Take.** Seed = update domain / `203.0.113.88`. Shared nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net` → candidate `login-prd.net`. Why not coincidence: distinctive NS pair, not a public resolver. Same A on that named sibling can support the hop. You still write the four parts, not a P-ID.
- **Reject.** Whole `203.0.113.0/24` — shared hosting. The seed IP sitting in that range does not make the range theirs.

---

## 2. Knowledge Check

1. This lesson requires a DTF P-ID on the hop. True or false?
2. What four parts does a hop sentence have?
3. You have the update domain / `203.0.113.88`. Shared nameservers `ns1.cdn-test.net` / `ns2.cdn-test.net` point at `login-prd.net`. Write the hop, or say why you would reject the whole `203.0.113.0/24`.

---

## 3. Summary

Seed → shared characteristic → candidate → why not coincidence. Shared `/24` is not a hop. Name the source class. Do not re-teach the tool. No P-ID required.

**Next:** **2.8.2** Applicable TTPs.

---

## 4. Related modules

- 2.7.4 – DTF ID line (previous)
- 2.8.2 – Applicable TTPs
- 2.5 / 2.6 / 0.7 / 2.9 – Tools you name, not re-teach
