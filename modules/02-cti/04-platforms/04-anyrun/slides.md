# Module 2.4.4 – ANY.RUN
## Slide Deck Content

**Total Suggested Slides:** 8

**Delivery:** Slides 1–2 support initial orientation. Complete the remaining material and knowledge check with 2.5.2; the combined delivery uses the stated lesson time.

### Slide 1 – Title
**ANY.RUN**  
Search the evidence, then inspect the session

### Slide 2 – What can be searched?
IOCs:
- hash
- IP
- domain
- URL

Events:
- process
- registry
- file
- network
- command line

Reference: [ANY.RUN TI Lookup](https://any.run/threat-intelligence-lookup/)

### Slide 3 – Start from a supplied seed
**Separate classroom scenario — not A12.**

Good:
- `sync-client.exe` SHA256
- `198.51.100.77`
- `sync-gateway.example`

Avoid label-fishing.

### Slide 4 – Review the session
Extract:
- process tree
- contacted infrastructure
- files
- registry
- other sandbox events

### Slide 5 – Attribute labels
“ANY.RUN labels this session as X”

is stronger tradecraft than:

“This is definitely X.”

### Slide 6 – Sandbox limits
One session = one environment/execution path.

Not observed ≠ never occurs.

### Slide 7 – Knowledge Check
1. Tag vs event evidence?  
2. Searchable IOC/event examples?  
3. No POST shown: what can you say?

### Slide 8 – Summary
**Seed → session → concrete event**


Reference: [Query Guide](https://intelligence.any.run/TI_Lookup_Query_Guide_v6.pdf)

**Next:** [2.4.5 – Silent Push](../05-silent-push/student-guide.md).
