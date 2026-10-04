# Module 1.0 – SOC Analyst Fundamentals
## Slide Deck Content

**Total Suggested Slides:** 8

### Slide 1 – Title
**1.0 – SOC Analyst Fundamentals**

How the 1.x block fits together

### Slide 2 – The SOC question
SOC work turns evidence into a defensible answer:

**What happened?**  
**What does the evidence support?**  
**What should happen next?**

### Slide 3 – The 1.x flow
**Observe → Detect → Investigate → Communicate**

- 1.1 Endpoint
- 1.2 Zeek
- 1.3 Detection
- 1.4 Alerts
- 1.5 Reporting

### Slide 4 – Two views of activity
**Endpoint**
- process
- user
- file
- registry
- initiating process

**Network**
- connection
- DNS
- TLS
- HTTP
- transferred artifacts

Different sensors answer different questions.

### Slide 5 – Detection is a lead
A detection tells you:

> **This pattern matched.**

Investigation determines:
- what actually happened;
- what context is missing;
- what the result means.

### Slide 6 – One A12 story, five questions
**1.1:** What happened on `WS-JLEE`?  
**1.2:** What happened on the wire?  
**1.3:** Why did the rule fire?  
**1.4:** How should the alert be assessed?  
**1.5:** How should the result be handed off?

Same activity. Different question.

### Slide 7 – Evidence first
Keep the sequence:

**Observation → interpretation → action**

Describe what the sensor shows before extending the conclusion.

### Slide 8 – Remember the map
**1.1:** Read the host  
**1.2:** Read the wire  
**1.3:** Read the detection  
**1.4:** Investigate the alert  
**1.5:** Communicate the result

**Next:** 1.1.1 – Endpoint Activity
