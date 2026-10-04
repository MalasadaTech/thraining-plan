# Module 1.6 – SOC Analyst Section Summary
## Slide Deck Content

**Total Suggested Slides:** 10

### Slide 1 – Title
**1.6 – SOC Analyst Section Summary**

From evidence to handoff

### Slide 2 – Return to the 1.0 model
**Observe → Detect → Investigate → Communicate**

You have now completed the full loop.

### Slide 3 – 1.x at a glance
**1.1** Read the host  
**1.2** Read the wire  
**1.3** Read the detection  
**1.4** Investigate and assess  
**1.5** Report and route

### Slide 4 – A12: Endpoint + Network
**Endpoint**
- `wscript.exe`
- encoded PowerShell
- host/user/process context

**Network**
- external communication
- `/update.exe` request
- protocol evidence

Different sensors answer different questions.

### Slide 5 – A12: Detection
The analytic fires because:

**the encoded-PowerShell condition matched**

That proves the rule condition matched.

It does not, by itself, prove maliciousness.

### Slide 6 – A12: Investigation
Ask:

- What happened?
- What supports the conclusion?
- What is still missing?
- Does it need escalation?

**Gap:** successful `/update.exe` download/execution not established.

### Slide 7 – Keep the labels separate
**Detection correctness**
TP / FP / TN / FN

**Activity category**
scan / user / root / unsuccessful / local category

**FP cause**
why benign activity matched

Different questions. Different labels.

### Slide 8 – Reporting and handoff
**Incident report**
records the case

**RFI**
asks another team a bounded question

Correct recipient + approved channel

### Slide 9 – SOC readiness
Can you:

- read host evidence?
- read network evidence?
- explain a detection?
- investigate beyond the alert title?
- preserve evidence gaps?
- select the right report/handoff?

### Slide 10 – Bridge to CTI
SOC asks:

> **What happened locally?**

CTI helps answer:

> **What does this activity mean in the wider threat context?**

**Next:** 2.x – Cyber Threat Intelligence
