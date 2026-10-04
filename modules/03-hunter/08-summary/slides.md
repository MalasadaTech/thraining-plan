# Module 3.8 – Threat Hunting Section Summary
## Slide Deck Content

**Total Suggested Slides:** 10

### Slide 1 – Title
**3.8 – Threat Hunting Section Summary**

From question to handoff

### Slide 2 – Return to the 3.0 loop
**Question → Hypothesis → Evidence → Refine → Finding → Handoff**

You have now completed the full hunt loop.

### Slide 3 – 3.x at a glance
**3.1** Why hunt?  
**3.2** Define the hunt  
**3.3** Sharpen leads with external tools  
**3.4** Turn CTI into hunt inputs  
**3.5** Organize behavior with ATT&CK  
**3.6** Hunt specific techniques/procedures  
**3.7** Document and hand off locally

### Slide 4 – A12: Question + hypothesis
**Question**

Are additional workstations showing A12-style persistence?

**Hypothesis**

If present, registry telemetry should reveal the same or closely related Run-key behavior.

### Slide 5 – A12: Scope + evidence
**Population:** managed Windows user workstations  
**Window:** 14 days  
**Telemetry:** registry + process/file

CTI/external research can sharpen the pattern.

Local evidence determines whether it occurred here.

### Slide 6 – ATT&CK supports the hunt
Keep separate:

**Technique** → behavior category  
**Procedure** → how activity was carried out  
**Observation** → what local telemetry actually showed

ATT&CK does not replace the hypothesis.

### Slide 7 – A12: Findings
Example:

- 2 exact matches
- 3 related candidates
- 18 hosts fully visible
- 7 hosts missing registry telemetry
- no current analytic covering exact behavior

One hunt. Several outcomes.

### Slide 8 – Keep the gaps separate
**Detection gap**
Telemetry exists; coverage is inadequate.

**Visibility gap**
Required telemetry is missing.

**False negative**
Expected control failed.

Not every unalerted event is a false negative.

### Slide 9 – Bound the conclusion
Do not say:

**The enterprise is clean.**

Say:

**The behavior was not found within the tested population, time window, and available telemetry.**

### Slide 10 – Bridge to DE
Hunt asks:

> **Can we find this behavior?**

Detection Engineering asks:

> **Should and how should we maintain automatic coverage for it?**

**Next:** 4.x – Detection Engineering
