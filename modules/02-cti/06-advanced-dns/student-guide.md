# Module 2.6.1 – Advanced DNS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.6.1 B / C / C ; 2.6.1.1 3c / 4c / 4d  
- Hunter: 2.6.1 B / C / C ; 2.6.1.1 2b / 3c / 4c  
- SOC: 2.6.1 A / A / B ; 2.6.1.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Interpret an **SOA** record.
2. Use advanced DNS (SOA, NS, related records) to enrich or pivot — not Zeek `dns` fields.

**Mapped Proficiency Items:**
- K: 2.6.1 – Advanced DNS concepts
- T: 2.6.1.1 – Interpret an SOA record and use advanced DNS data to enrich or pivot

---

## 1. Key Concepts

CTI analysts read **authoritative DNS** so they can see who runs the zone and whether two names share that control. Zeek `dns` fields and DGA are **1.2.3**. RDAP is **2.5**. Silent Push PDNS is **0.7**.

| Record | What you take from it |
|--------|------------------------|
| **SOA** | Primary NS (MNAME), responsible mailbox (RNAME), serial |
| **NS** | Who answers the zone (already seen on RDAP) |
| **Other** | MX / TXT when the card has them — intel value is “who else is tied to this zone,” not a full MX class |

**What good looks like:**

- **Interpret SOA** on the update domain: MNAME / RNAME `hostmaster.cdn-test.net`, a serial. That is who runs the zone, not a country.
- **Pivot:** sibling `login-prd.net` with the **same NS pair** and same A `203.0.113.88` is a related name. Shared Example Cloud `/24` is **not** “theirs.”

---

## 2. Knowledge Check

1. This hour is Zeek `dns` field reading. True or false?
2. What two SOA fields do you read first (MNAME / RNAME)?
3. Same NS + same A on `login-prd.net` — what can you say, and what must you **not** say about `203.0.113.0/24`?

---

## 3. Summary

SOA says who runs the zone. Same NS / same A can be a sibling. A shared /24 is not theirs.

**Next:** **2.7.1** ATT&CK for CTI.

---

## 4. Related modules

- 2.5.1 – RDAP / WHOIS (previous)
- 2.7.1 – ATT&CK for CTI
- 1.2.3 – Zeek DNS / DGA
- 0.7 – Silent Push
