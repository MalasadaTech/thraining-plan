# Module 4.2 – Sound Detections
## Slide Deck Content

**Total Suggested Slides:** 10

### Slide 1 – Title
**Sound Detection Engineering**  
Test behavior, non-target behavior, and data

### Slide 2 – Parsing is not validation
A rule can be syntactically valid and operationally useless.

### Slide 3 – Positive test
What **must fire**?

Use known or safely emulated intended behavior.

### Slide 4 – Negative test
What **must not fire**?

Use realistic benign / near-neighbor activity.

### Slide 5 – Data test
Do the required:
- logs
- fields
- population
- parsing
- timing
exist?

Reference: [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)

### Slide 6 – Test behavior
Exact IOC replay can help.

Behavioral validation is more durable.

Reference: [CTID detection validation](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/)

### Slide 7 – Local requirements
Public formats ≠ local deployment policy.

Learn the check here; complete `4.2.2` only after 4.8 provides the verified local list.

### Slide 8 – Close the loop
Shipped  
Changed  
Sent back  
Retired / superseded

Explain meaningful changes.

### Slide 9 – Run the validation practical
`4.2.1` requires an executed test:
- target behavior
- benign near-neighbor
- data path
- PASS / CHANGE / FAIL-HOLD decision

### Slide 10 – Knowledge Check
1. Three test categories?  
2. Why can logic be right but detection fail?  
3. Does Sigma define local policy?

**Next:** 4.3 – Nominations
