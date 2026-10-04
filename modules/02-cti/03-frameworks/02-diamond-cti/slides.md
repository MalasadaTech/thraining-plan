# Module 2.3.2 – Diamond Model Application in CTI  
## Slide Deck Content

**Total Suggested Slides:** 8

### Slide 1 – Title
**Title:** Diamond Model for CTI  
**Subtitle:** Show what the event tells you—and what it does not

### Slide 2 – Four core features
**Adversary**  
**Capability**  
**Infrastructure**  
**Victim**

Reference: [Diamond Model paper](https://threatconnect.com/wp-content/uploads/2023/01/The_Diamond_Model_of_Intrusion_Analysis.pdf)

### Slide 3 – An incomplete Diamond is still useful
Unknown does not mean failure.

A missing vertex can identify the next intelligence question.

### Slide 4 – A12
**Adversary:** unresolved cluster  
**Capability:** encoded PowerShell / `update.exe`  
**Infrastructure:** update domain / `203.0.113.88`  
**Victim:** `WS-JLEE` / `jlee`

### Slide 5 – Preserve attribution provenance
“Vendor X tracks this as PRD APT” preserves the source.

“Adversary = PRD APT” is stronger and needs evidence to justify it.

### Slide 6 – The edges matter
Capability ↔ Infrastructure  
Infrastructure ↔ Victim  
Adversary ↔ Capability  
Adversary ↔ Infrastructure

Relationships create analytic questions and pivots.

### Slide 7 – Knowledge Check
1. Four core features?  
2. Why is Adversary least developed in A12?  
3. How should a vendor tracking name be represented?

### Slide 8 – Summary
Populate what the evidence supports.  
Keep uncertainty visible.  
Use relationships to guide the next question.

**Next:** [2.3.3 – Cyber Kill Chain in Intelligence Analysis](../03-kill-chain-cti/student-guide.md).
