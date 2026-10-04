# Module 4.9 – Detection Engineering Section Summary
## Slide Deck Content

**Total Suggested Slides:** 10

### Slide 1 – Title
**4.9 – Detection Engineering Section Summary**

From defensive need to maintained coverage

### Slide 2 – Return to the 4.0 lifecycle
**Need → Coverage Decision → Build/Change → Validate → Deploy → Monitor → Improve/Retire**

You have now completed the full lifecycle.

### Slide 3 – 4.x at a glance
**4.1** Define DE ownership  
**4.2** Validate soundness  
**4.3** Accept nominations  
**4.4** Tune live coverage  
**4.5** Convert hunt/CTI findings  
**4.6** Maintain the lifecycle  
**4.7** Verify sensors/data  
**4.8** Follow local production governance

### Slide 4 – A12: Need + coverage decision
**Need**

Durable coverage for A12-style encoded PowerShell.

First ask:

- already covered?
- modify existing?
- new analytic?
- another control?

Coverage first. Rule count second.

### Slide 5 – A12: Validate
**Positive**
Does target behavior match?

**Benign control**
Does representative normal activity stay out?

**Data**
Do required events and fields actually arrive?

Valid syntax is only one requirement.

### Slide 6 – A12: Deploy + monitor
**Review → Approve → Deploy → Validate production**

Then monitor:

- alert quality
- data health
- population coverage
- operational burden

### Slide 7 – Tuning is engineering
A safe tune:

- addresses the real benign condition
- stays narrow
- preserves target behavior
- is revalidated

Exception ≠ success by itself.

### Slide 8 – Silent detection?
Check:

1. source event
2. ingestion
3. parsing
4. population
5. timeliness
6. logic

No alert ≠ automatic proof of no activity.

### Slide 9 – Keep the boundaries clear
**Nomination ≠ finished rule**  
**Syntax ≠ soundness**  
**Tune ≠ new nomination**  
**Detection gap ≠ data gap**  
**Detection ≠ enforcement**  
**Deployment ≠ completion**

### Slide 10 – Close the defensive loop
**SOC → CTI → Hunt → Detection Engineering → SOC**

Final principle:

**A detection is a maintained capability, not a finished query.**
