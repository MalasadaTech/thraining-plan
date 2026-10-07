# Module 2.4.3 – VirusTotal Relations and Behavior
## Slide Deck Content

**Total Suggested Slides:** 8

**Delivery:** Slides 1–2 support initial orientation. Complete the remaining material and knowledge check with 2.5.2; the combined delivery uses the stated lesson time.

### Slide 1 – Title
**VirusTotal Relations and Behavior**  
Linked objects vs sandbox observations

### Slide 2 – Two different evidence types
**Relations:** connected objects  
**Behavior:** sandbox-observed activity

References: [Relationships](https://docs.virustotal.com/reference/relationships) | [File Behaviours](https://docs.virustotal.com/reference/file-object-behaviours)

### Slide 3 – Relations
A file may relate to:
- domains
- IPs
- URLs
- other files

A relationship creates a **candidate pivot**, not automatic ownership.

### Slide 4 – Behavior
Sandbox reports may record:
- process
- file
- registry
- network events

Observed in sandbox ≠ universal behavior.

### Slide 5 – Absence is narrow
Not shown on one behavior report:

→ **not observed here**

Not:

→ **never happens**

### Slide 6 – Separate classroom card
**Not A12:** A12 has no recovered sample/hash/VT behavior.
Relations → `198.51.100.77`

Behavior → `sync-client.exe` start + Temp write + connection to `198.51.100.77:8080`

No Run-key event shown.

### Slide 7 – Knowledge Check
1. What does a relationship prove?  
2. What does an absent sandbox event mean?  
3. One valid Relations and Behavior finding?

### Slide 8 – Summary
**Linked object ≠ ownership**  
**Sandbox event ≠ universal behavior**

**Next:** [2.4.4 – ANY.RUN](../04-anyrun/student-guide.md).
