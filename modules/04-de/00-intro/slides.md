# Module 4.0 – Detection Engineering
## Slide Deck Content

**Total Suggested Slides:** 9

### Slide 1 – Title
**4.0 – Detection Engineering**

How the 4.x block fits together

### Slide 2 – The DE lifecycle
**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

A detection is more than a rule.

### Slide 3 – The 4.x map
**4.1** What does DE own?  
**4.2** Is the detection sound?  
**4.3** How does new work enter?  
**4.4** How do live detections change?  
**4.5** How do hunt/CTI findings become coverage?  
**4.6** How is coverage maintained?  
**4.7** Can the analytic see the required data?  
**4.8** How does this shop run DE?

### Slide 4 – Start with a defensive need
Example:

**We need durable visibility for A12-style encoded PowerShell.**

Canonical A12 reaches **coverage review**. Any later build/deploy lifecycle steps shown here are hypothetical practice, not A12 outcomes.

A nomination does not need to contain the final rule.

### Slide 5 – Reuse before adding
Possible decisions:

- existing coverage is sufficient
- modify/tune existing analytic
- create new analytic
- detection is not the right control

The goal is useful coverage—not more rules.

### Slide 6 – Validate more than syntax
Ask:

**Positive:** does target behavior match?  
**Benign control:** does normal activity stay out when appropriate?  
**Data:** do the required events/fields exist?

### Slide 7 – A silent rule is ambiguous
Possible causes:

- behavior absent
- logic miss
- collection gap
- ingestion/parsing problem
- population gap
- timing problem

No alert ≠ automatic proof of no activity.

### Slide 8 – Production is a lifecycle
Deploy  
→ monitor  
→ tune/change  
→ revalidate  
→ replace/retire

Maintained coverage needs an owner.

### Slide 9 – Remember the lifecycle
**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

**Next:** 4.1 – What Detection Engineering Owns
