# Module 3.0 – Threat Hunting
## Slide Deck Content

**Total Suggested Slides:** 9

### Slide 1 – Title
**3.0 – Threat Hunting**

How the 3.x block fits together

### Slide 2 – The hunt loop
**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

A hunt is more than a query.

### Slide 3 – The 3.x map
**3.1** Why hunt?  
**3.2** What are we testing?  
**3.3** What external evidence sharpens the lead?  
**3.4** What CTI becomes huntable?  
**3.5** How does ATT&CK organize the behavior?  
**3.6** How do we hunt a technique?  
**3.7** How does this shop control and route the hunt?

### Slide 4 – Start with a question
Weak:

**Hunt persistence**

Stronger:

**Are there additional workstations with A12-style persistence?**

### Slide 5 – Evidence can come from several places
**Internal telemetry**
- process
- file
- registry
- network

**CTI / external research**
- procedures
- indicators
- infrastructure
- sandbox / passive-DNS leads

External evidence gives you a reason to look locally.

### Slide 6 – Refine the search
Broad candidate set  
→ add discriminating context  
→ investigate manageable candidates

Do not tune away the behavior you are trying to find.

### Slide 7 – Hypothetical practice result — not canonical A12
Illustrative result only:

No matches on 18 visible hosts.

7 hosts lack required registry telemetry.

Conclusion:

**Not found within tested scope and available visibility.**

### Slide 8 – Findings create handoffs
Compromise → SOC / IR  
Detection gap → Detection Engineering  
Visibility gap → telemetry owner  
New intelligence lead → CTI  
Follow-on pattern → next hunt

### Slide 9 – Remember the loop
**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

**Next:** 3.1 – Purpose of Threat Hunting
