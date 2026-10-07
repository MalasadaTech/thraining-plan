# Module 0.10 – Shared Foundations Section Summary
## Slide Deck Content

**Total Suggested Slides:** 11

### Slide 1 – Title
**0.10 – Shared Foundations Section Summary**

The common language for every role

### Slide 2 – The 0.x map
**Course map → Roles → Handoffs → Frameworks → Tools → Environment → Initial Access**

These foundations stay with you through every later track.

### Slide 3 – Four roles, four primary outcomes
**SOC**
Investigate and coordinate operational cases

**CTI**
Produce assessed intelligence

**Threat Hunting**
Search deliberately for insufficiently surfaced activity

**Detection Engineering**
Maintain durable detection coverage

### Slide 4 – Work moves when the question changes
**Generic workflow example — not A12**

SOC question  
→ CTI question  
→ Hunt question  
→ DE coverage question  
→ future SOC alert

Not every case follows this exact path.

The principle is the handoff.

### Slide 5 – Same evidence, different product
One domain can appear in:

- a SOC case
- a CTI assessment
- a hunt query
- a detection analytic

Same evidence.

Different purpose and product.

### Slide 6 – Three framework views
**ATT&CK**
What behavior?

**Diamond Model**
Which entity relationships?

**Cyber Kill Chain**
Which intrusion stage?

Frameworks organize evidence. They do not invent it.

### Slide 7 – External tools
External platforms can provide:

- relationships
- sandbox observations
- passive DNS
- web observations
- reputation/context

Treat results as evidence or leads—not automatic local truth.

### Slide 8 – Environment path and visibility answer different questions
**Traffic path**
Where activity moves

**Collection point**
Where it can be observed

**Visibility**
What was actually collected and usable

Keep them separate.


### Slide 9 – Initial access: a hypothesis until evidence supports it
**Common paths**
Phishing / malspam · public-facing exploitation · drive-by / watering hole · valid accounts / remote services · trusted relationships / supply chain

Ask: **What does the evidence establish, and what would test the entry-path hypothesis?**

**Speaker notes:** Use A12 only as a spoiler-light boundary example here. The canonical case does not establish how access began, and the detailed process/network/registry evidence is intentionally introduced later in 1.x. Do not preview those observations in the 0.x summary.

### Slide 10 – A12 across the roles
`WS-JLEE`

SOC → investigate  
CTI → add threat context  
Hunt → search elsewhere  
DE → evaluate maintained coverage

The question changes as work moves.

**A12 detail is intentionally deferred:** the specific process/network/registry evidence begins in 1.x, and later hunt/DE outcomes are not yet established.

### Slide 11 – Bridge to 1.x
0.x asked:

> **How does defensive work fit together?**

1.x begins:

> **What does the evidence actually show?**

**Next:** 1.0 – SOC Analyst Fundamentals
