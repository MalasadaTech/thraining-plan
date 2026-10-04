# Module 4.8 – Site-Specific Detection Engineering
## Slide Deck Content

**Total Suggested Slides:** 9

### Slide 1 – Title
**How Detection Engineering Works Here**

### Slide 2 – Find two local sources
1. Detection requirements list  
2. Lifecycle / change path

### Slide 3 – Verify currency
Location  
Owner  
Version/date  
Scope  
Supersession

### Slide 4 – Public format ≠ local policy
Sigma can show common fields.

Your organization decides what is required.

Reference: [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)

### Slide 5 – Map the lifecycle
Intake  
Test  
Review  
Approve  
Deploy  
Monitor  
Change  
Rollback  
Retire

### Slide 6 – Authority matters
Review ≠ approval  
Approval ≠ deployment  
Deployment ≠ rollback authority

### Slide 7 – Know the authoritative copy
Repository?  
Detection-as-code?  
Platform console?

Which one is source of truth?

### Slide 8 – Missing information
Record the exact gap:

**Deployment approval authority not yet verified.**

### Slide 9 – Knowledge Check
1. Sigma vs local standard?  
2. Four lifecycle steps/roles?  
3. Deploy known, approval/rollback unknown: what do you record?

**4.x Detection Engineering complete**
