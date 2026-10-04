# Module 2.5.3 – RDAP and WHOIS Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.5.3 – RDAP and WHOIS  
**Subtitle:** Read registration data without turning it into attribution  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is about what registration systems record for domains and IP networks. The goal is accurate enrichment and clear evidence boundaries.

---

### Slide 2 – What registration data can answer
**Title:** Who registered or holds the resource?

Registration data can expose:

- registrar or registry context;
- registration events;
- nameservers;
- public entities / contacts; and
- the registered holder of an IP network.

It does **not** automatically identify the malicious operator.

**Speaker Notes:**  
Make the distinction before introducing protocols. The record describes registration relationships.

---

### Slide 3 – RDAP and legacy WHOIS
**Title:** Modern structured access vs legacy text

**RDAP** — HTTP/HTTPS + structured JSON.  
**WHOIS** — legacy TCP/43 + free-text responses.

For gTLD registration data, RDAP became the definitive source on **January 28, 2025**.

Reference: [ICANN — Launching RDAP; Sunsetting WHOIS](https://www.icann.org/en/announcements/details/icann-update-launching-rdap-sunsetting-whois-27-01-2025-en)

**Speaker Notes:**  
WHOIS may still exist in some registries, RIRs, tools, and historical workflows. Do not teach it as the universal primary lookup.

---

### Slide 4 – Registration roles
**Title:** Registrar, registrant, and network holder are different

**Registrar** — manages the domain registration.  
**Registrant / entity** — associated registration holder when public.  
**Network holder** — organization registered for an IP block.

None of those labels automatically equals the threat actor.

**Speaker Notes:**  
Ask learners to describe each role before interpreting a company name from a record.

---

### Slide 5 – Domain fields
**Title:** Extract what the record actually provides

Useful fields include:

- registrar;
- status;
- creation / registration event;
- updated / changed event;
- expiration event, when available;
- nameservers;
- public entities / contacts;
- notices and remarks.

**Redacted** means not publicly disclosed—not “no intel.”

**Speaker Notes:**  
Reference for RDAP object structure: [RFC 9083](https://www.rfc-editor.org/rfc/rfc9083.html).

---

### Slide 6 – IP-network fields
**Title:** The network holder is not the operator

`203.0.113.88` → RDAP network object → `203.0.113.0/24`, **Example Cloud**

Defensible:

**The address is in a network registered to Example Cloud.**

Unsupported:

**Example Cloud conducted the activity.**

**Speaker Notes:**  
This is especially important for shared hosting and cloud infrastructure.

---

### Slide 7 – Nameservers are pivots, not proof
**Title:** Ask how distinctive the shared infrastructure is

Same common managed-DNS provider → weak relationship signal.

Same rare NS pair + similar registration timing + same uncommon address → stronger candidate pivot.

The shared NS still needs corroboration.

**Speaker Notes:**  
The skill is weighting the evidence, not declaring every shared nameserver a cluster.

---

### Slide 8 – A12 registration example
**Title:** Write the enrichment line

RDAP for the update domain:

- Example Registrar;
- `ns1.cdn-test.net`;
- `ns2.cdn-test.net`;
- recent registration event;
- registrant not publicly disclosed.

Write those facts. Then decide what additional evidence is needed.

**Speaker Notes:**  
Do not turn redaction or the nameserver pair into nation-state attribution.

---

### Slide 9 – Knowledge Check and Summary
**Title:** Registration data is one layer of evidence

1. Why is RDAP generally preferable to legacy WHOIS?  
2. Registrant is redacted; what useful fields can remain?  
3. An IP is registered to a cloud provider. What can you say—and what can you not attribute?


**Speaker Notes:**  
Use the instructor key. Reinforce role separation and evidence boundaries.

**Next:** [2.5.4 – Advanced DNS Concepts](../04-advanced-dns/student-guide.md).
