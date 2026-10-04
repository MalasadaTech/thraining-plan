# Course Summary – Bringing the Defensive Workflow Together
## Slide Deck Content

**Total Suggested Slides:** 12

### Slide 1 – Title
**Course Summary**

Bringing the defensive workflow together

### Slide 2 – The course-wide loop
**Observe → Understand → Search → Improve Coverage → Observe Again**

**SOC → CTI → Hunt → DE → SOC**

### Slide 3 – Five sections, five questions
**0.x** How does defensive work fit together?  
**1.x** What happened?  
**2.x** What does the evidence mean and why does it matter?  
**3.x** Does related activity exist elsewhere?  
**4.x** Should this become maintained coverage?

### Slide 4 – A12: SOC
Observe:

- encoded PowerShell
- network activity
- `/update.exe`
- persistence evidence

Separate observation from conclusion.

### Slide 5 – A12: CTI requirement
RFI:

> What is known about the update domain, and does evidence support payload delivery?

The requirement drives collection.

### Slide 6 – A12: reorganized CTI workflow
**Requirement → Collect → Evaluate → Enrich → Correlate → Assess → Produce → Disseminate**

Platforms answer lookups.

Analysis answers the requirement.

### Slide 7 – CTI claim strength
**Candidate pivot**  
→ **supported relationship**  
→ **activity-set/campaign assessment**  
→ **attribution**

Do not skip evidence levels.

### Slide 8 – CTI significance
**Applicability** – can it happen here?  
**Visibility** – can we see it?  
**Relevance** – does it matter here?  
**Impact** – what could follow?

### Slide 9 – A12: Hunt
Turn CTI into:

- bounded question
- hypothesis
- population
- time window
- telemetry
- findings/limitations

“Not found” stays bounded.

### Slide 10 – A12: Detection Engineering
**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

A detection is a maintained capability.

### Slide 11 – Cross-course rules
**Evidence before conclusion**  
**Question before tool**  
**Provenance before confidence**  
**Scope before negative claim**  
**Handoff before silo**

### Slide 12 – Final model
**SOC → CTI → Threat Hunting → Detection Engineering → SOC**

> Follow the evidence.  
> Answer the question.  
> Preserve uncertainty.  
> Give the next defender something usable.
