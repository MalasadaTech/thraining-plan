# Module 4.4 – Tune Requests
## Slide Deck Content

**Total Suggested Slides:** 9

### Slide 1 – Title
**Tuning Live Detections**

### Slide 2 – Tune vs nomination
**Tune:** live analytic  
**Nomination:** new defensive need

Ticket/queue design is local.

### Slide 3 – Evidence to review
Rule ID  
Representative alerts  
Observed problem  
Case/investigation pointer  
Desired behavior

### Slide 4 – Five outcomes
Tune  
Exception/filter  
Replace  
Leave  
Retire

### Slide 5 – Narrow exceptions
Exclude the understood benign case—not an entire broad population.

Reference: [Sigma Filters](https://sigmahq.io/docs/meta/)

### Slide 6 – Re-test
After tuning:
- intended behavior still fires?
- benign case suppressed?
- new blind spot?

### Slide 7 – Noise is not automatic retirement
Operational cost matters, but so does detection value.

### Slide 8 – Not tuning
Investigate host → investigation  
Isolate host → IR  
Block IP → control owner

### Slide 9 – Knowledge Check
1. Tune vs nomination?  
2. Why re-test exclusions?  
3. “Investigate the host”: tune?

**Next:** 4.5 – Packages
