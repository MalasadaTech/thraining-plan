# Module 2.7.2 – STIX in Intelligence Production  
## Slide Deck Content

**Total Suggested Slides:** 10

### Slide 1 – Title
**STIX in Intelligence Production**  
Build the graph, validate the objects, exchange them

### Slide 2 – Relationships carry meaning
Indicator → **indicates** → Malware  
Malware → **uses** → Attack Pattern  
Indicator → **based-on** → Observed Data

Reference: [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Slide 3 – Sighting is its own object
Use:
- `sighting_of_ref`
- optional `observed_data_refs`
- optional `where_sighted_refs`

Not:
`relationship_type: sighting-of`

### Slide 4 – A12 graph
Indicator(hash)  
→ indicates Malware  
→ Malware uses T1059.001

Indicator  
→ based-on Observed Data

Sighting  
→ records that the Indicator was seen

### Slide 5 – Validation is object-specific
Common fields are not enough.

Indicator also needs:
- pattern
- pattern_type
- valid_from

Relationship needs:
- relationship_type
- source_ref
- target_ref

### Slide 6 – Schema-valid ≠ analytically sound
A relationship may be allowed by STIX but still need better evidence.

Model the claim the intelligence actually supports.

### Slide 7 – Bundle
A Bundle is a transient container.

Objects in one Bundle are **not automatically related**.

Reference: [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Slide 8 – TAXII Collection
A Collection is a logical repository exposed by a TAXII server.

Clients can retrieve—and when authorized, add—objects.

Reference: [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)

### Slide 9 – Envelope vs Bundle
**STIX Bundle** → optional STIX container  
**TAXII Envelope** → transport wrapper for TAXII object exchange

Do not treat them as the same object.

### Slide 10 – Knowledge Check
1. Does Bundle membership create a relationship?  
2. Indicator-specific required fields?  
3. Bundle vs Collection vs Envelope?

**Next:** [2.7.3 – Creating Finished Intelligence Products](../03-finished-products/student-guide.md).
