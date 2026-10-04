# Instructor Guide – Module 2.5.3 – RDAP and WHOIS Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.3 B / C / C ; 2.5.3.1 3c / 4c / 4c  
- Hunter: 2.5.3 A / B / B ; 2.5.3.1 2b / 3c / 4c  
- SOC: 2.5.3 A / A / B ; 2.5.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners retrieve and interpret domain or IP registration data while keeping registration roles separate from threat-actor attribution.

**Context:** Module 2.5.2 focused on file similarity. This lesson moves to infrastructure enrichment. Learners should understand what registration systems can tell them about a domain or address block and where that evidence stops.

**Current standards note:** RDAP is the modern IETF-standard registration-data protocol. For gTLD registration data, ICANN sunset the contractual WHOIS requirement effective January 28, 2025. WHOIS can still appear in other registries, RIRs, tools, and historical workflows, so the lesson retains it as a legacy concept rather than teaching it as the default first query.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain what RDAP and legacy WHOIS registration data are used for and how the two access methods differ.
2. Query a domain or IP registration record, extract useful fields, and interpret those fields without turning registration data into unsupported attribution.

**Mapped Proficiency Items:**
- K: 2.5.3 – RDAP and WHOIS concepts
- T: 2.5.3.1 – Query RDAP/WHOIS and interpret fields for enrichment or attribution

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Explain what registration data answers. |
| RDAP vs WHOIS | 5 minutes | Establish modern and legacy access models. |
| Domain fields | 5 minutes | Interpret registrar, events, nameservers, and redaction. |
| IP-network fields | 4 minutes | Separate network holder from activity operator. |
| A12 examples | 4 minutes | Apply the evidence boundaries. |
| Knowledge check | 3 minutes | Test interpretation, not memorization. |
| **Total** | **24 minutes** | Adjust demonstration time as needed. |

## Detailed Teaching Notes

### 1. Start with the question registration data can answer

Ask: **If a domain appears in an incident, what can a registration lookup tell us?**

Guide learners toward registrar, registration events, nameservers, public entities, and network-holder information.

Then ask what it cannot establish by itself: the malicious operator, campaign owner, malware family, or nation-state sponsor.

### 2. Teach RDAP as the modern standard

Explain that RDAP provides structured JSON over HTTP/HTTPS. Its object model makes fields and links more consistent than legacy WHOIS text.

For gTLDs, use the ICANN 2025 transition as the concrete operational fact: RDAP is now the definitive registration-data source. WHOIS remains useful to recognize because some environments and non-gTLD registries still expose it.

Reference: [ICANN — Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en).

### 3. Distinguish the roles

Put **registry**, **registrar**, **registrant/entity**, and **network holder** on the board.

A common learner mistake is to see a company name anywhere in the record and treat it as the actor. Ask what role that company actually occupies.

### 4. Teach redaction as a property of the record

If the registrant is not public, learners should still inspect:
- registrar;
- nameservers;
- dates/events;
- status;
- notices;
- remaining entities.

The absence of a public registrant is itself a limitation of the available record, not a reason to discard every other field.

### 5. Teach nameservers as pivots whose value depends on distinctiveness

A shared NS pair can justify further investigation. It becomes more useful when combined with other independent similarities.

Ask learners to compare:
- two domains on a huge managed-DNS provider;
- two domains on the same unusual NS pair, registered near the same time, resolving to the same uncommon address.

The second case is a stronger pivot, but still requires corroboration.

### 6. Teach IP registration carefully

Use `203.0.113.88`.

If the RDAP network object lists Example Cloud, the registration claim is about the **network holder**.

Ask: **Could an unrelated customer also use an address in that provider's space?** Yes. That makes the attribution boundary intuitive.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| WHOIS is always the primary/default lookup. | Explain the RDAP transition and environment-specific legacy WHOIS availability. |
| Redacted registrant means the lookup has no value. | Point to registrar, events, nameservers, status, and notices. |
| Registrar equals registrant. | Separate the service provider from the registration holder. |
| IP-network organization equals threat actor. | Reframe it as the network holder or provider. |
| Shared nameserver proves shared operator. | Ask how common the provider is and what additional evidence corroborates the relationship. |

## Knowledge Check – Answer Key

### 1. Why prefer RDAP?

**Expected answer:** RDAP is the modern standardized protocol using structured JSON over HTTP/HTTPS, with more consistent object semantics than legacy free-text WHOIS. For gTLDs, it is now the definitive registration-data source.

### 2. Redacted registrant but other fields remain

**Expected answer:** The analyst can still use registrar, nameservers, registration/updated events, status, notices, and other public entities. The correct statement is that registrant data is not publicly disclosed, not that there is no intelligence.

### 3. IP in a cloud-provider network

**Expected answer:** State that the address falls within a network registered to the provider. Do not attribute the activity to the provider or infer that the threat actor controls the entire block.

## Summary and Transition

Close with: **registration data identifies recorded registration relationships; analysis determines what those relationships mean.**

The next lesson examines the DNS records published for the name itself.

## Instructor References

- [ICANN — Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en)
- [RFC 9082 — RDAP Query Format](https://www.rfc-editor.org/rfc/rfc9082.html)
- [RFC 9083 — RDAP JSON Responses](https://www.rfc-editor.org/rfc/rfc9083.html)
- [RFC 3912 — WHOIS Protocol Specification](https://www.rfc-editor.org/rfc/rfc3912.html)

## Paired application

Complete the application portion of 2.4.2 with this lesson. Use an approved registration service or the supplied registration record. Identify the entity role, relevant dates, and redacted or unavailable fields. Record one useful lead and one conclusion the registration data cannot support. Use the existing platform-guide answer key for its knowledge check. Account for the remaining platform time separately from this method lesson; do not repeat the orientation.
