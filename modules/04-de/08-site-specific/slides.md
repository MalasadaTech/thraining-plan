# Module 4.8 – Site-Specific Detection Engineering
## Slide Deck Content

**Total Suggested Slides:** 10

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

### Slide 5 – Finish the 4.2.2 local check
Now that the verified list is available:
- return to the 4.2 validation record
- mark requirements met / missing
- cite evidence and list version
- record any unresolved local gap

Do not substitute public Sigma fields for local policy.

### Slide 6 – Map the lifecycle
Intake  
Test  
Review  
Approve  
Deploy  
Monitor  
Change  
Rollback  
Retire

### Slide 7 – Authority matters
Review ≠ approval  
Approval ≠ deployment  
Deployment ≠ rollback authority

### Slide 8 – Know the authoritative copy
Repository?  
Detection-as-code?  
Platform console?

Which one is source of truth?

### Slide 9 – Missing information
Record the exact gap:

**Deployment approval authority not yet verified.**

### Slide 10 – Knowledge Check
1. Sigma vs local standard?  
2. Four lifecycle steps/roles?  
3. Deploy known, approval/rollback unknown: what do you record?

**Next:** 4.9 – Detection Engineering Section Summary
