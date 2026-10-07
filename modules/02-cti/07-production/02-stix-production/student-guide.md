# Module 2.7.2 – How STIX Objects Are Used in Intelligence Production

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.7.2 B / C / C ; 2.7.2.1 3c / 4c / 4d ; 2.7.2.2 3c / 4c / 4d ; 2.7.2.3 3c / 4c / 4c  
- Hunter: 2.7.2 B / C / C ; 2.7.2.1 2b / 3c / 4c ; 2.7.2.2 2b / 3c / 4c ; 2.7.2.3 2b / 3c / 4c  
- SOC: 2.7.2 A / B / B ; 2.7.2.1 1a / 1a / 2b ; 2.7.2.2 1a / 1a / 2b ; 2.7.2.3 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Build a small STIX-aligned graph using valid relationship types and Sightings to express a threat scenario.
2. Recognize the key required fields needed for common STIX 2.1 objects used in the classroom example.
3. Explain how TAXII 2.1 Collections exchange STIX objects and distinguish a **STIX Bundle** from a **TAXII Envelope**.

**Mapped Proficiency Items:**
- K: 2.7.2 – How STIX objects are used in intelligence production
- T: 2.7.2.1 – Create STIX-aligned relationships and explain a threat scenario
- T: 2.7.2.2 – Create and validate STIX objects
- T: 2.7.2.3 – Use TAXII for sharing and consumption of intelligence

## 1. Key Concepts

STIX becomes useful when separate facts are structured and connected so people and tools can interpret the same threat model consistently.

Reference: [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

### Relationships give the graph meaning

A STIX **Relationship** object connects a source object to a target object with a `relationship_type`.

Common specification-defined relationships used in this course include:

| Source | Relationship | Target example |
|---|---|---|
| Indicator | **indicates** | Malware or Attack Pattern |
| Indicator | **based-on** | Observed Data |
| Malware | **uses** | Attack Pattern |
| Threat Actor / Intrusion Set / Campaign | **uses** | Malware or Attack Pattern |
| Threat Actor / Intrusion Set / Campaign | **targets** | Identity |
| Course of Action | **mitigates** | Attack Pattern, Indicator, Malware, Tool, Vulnerability |

STIX also permits `related-to` and can permit custom relationships. For this course, use a specification-defined relationship when one clearly fits. A vague or custom verb should not be used to hide uncertainty.

### Sighting is not a Relationship verb

**Sighting** is its own STIX Relationship Object.

It uses:
- `sighting_of_ref` → the STIX Domain Object that was sighted;
- optional `observed_data_refs` → raw observation context;
- optional `where_sighted_refs` → Identity or Location describing who/where saw it.

Reference: [STIX 2.1 – Sighting](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

This means a host sighting should not be modeled as:

`relationship_type: sighting-of`

That is not the STIX 2.1 Sighting model.

### Build the A12 graph with defensible semantics

Assume the classroom scenario has:

- an Indicator pattern for the SHA256 of `invoice.vbs`;
- Malware object for the malicious `invoice.vbs` sample/family if the analysis supports modeling it as Malware;
- Attack Pattern for **T1059.001 PowerShell**;
- Identity for **DYA**;
- optionally an Identity representing **WS-JLEE** as a system;
- Observed Data describing the file/process observation.

A defensible graph might include:

1. **Indicator → indicates → Malware**
2. **Malware → uses → Attack Pattern T1059.001**
3. **Indicator → based-on → Observed Data**
4. **Sighting** of the Indicator, with Observed Data attached and DYA or WS-JLEE represented through `where_sighted_refs` when that modeling decision is appropriate

This is more precise than claiming:

> The invoice hash indicates PowerShell because PowerShell happened somewhere in the same incident.

STIX permits Indicator → indicates → Attack Pattern, but the analyst should still ensure the detection pattern genuinely detects evidence of that Attack Pattern. Relationship validity in the schema does not automatically make the analytic claim sound.

### Required fields depend on object type

Most STIX Domain Objects and STIX Relationship Objects use common required fields such as:

- `type`
- `spec_version`
- `id`
- `created`
- `modified`

But each object can have additional required properties.

Examples:

**Indicator** requires, among other properties:
- `pattern`
- `pattern_type`
- `valid_from`

**Relationship** requires:
- `relationship_type`
- `source_ref`
- `target_ref`

**Sighting** requires:
- `sighting_of_ref`

**Observed Data** requires observation fields such as:
- `first_observed`
- `last_observed`
- `number_observed`
- `object_refs` in the STIX 2.1 model

Validation therefore means more than checking that every object has the five common fields.

Reference: [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)

### A Bundle is a container—not a relationship

A **STIX Bundle** is a transient container holding arbitrary STIX Objects.

The specification explicitly states that objects are **not considered related merely because they appear in the same Bundle**.

Reference: [STIX 2.1 – Bundle Object](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)

A Bundle can be convenient for packaging objects in a file or message, but the semantic links still come from Relationship, Sighting, embedded references, and the objects themselves.

### TAXII is the exchange protocol

**TAXII 2.1** is an application-layer protocol for exchanging cyber threat intelligence over HTTPS.

Reference: [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)

A **Collection** is a logical repository of CTI objects exposed by a TAXII server.

A TAXII client can:
- GET objects from a Collection;
- POST objects to a writable Collection.

### TAXII Envelopes and STIX Bundles Serve Different Purposes

TAXII and STIX define different layers of the exchange, so their container concepts should remain distinct.

TAXII 2.1 uses a **TAXII Envelope** as the transport wrapper when STIX objects are exchanged through Collection endpoints. A **STIX Bundle** is a separate STIX container that can group STIX objects independently of TAXII.

This means a STIX Bundle can be used outside TAXII, while a TAXII exchange does not require every set of objects to be represented as a STIX Bundle.

A useful mental model is:

- **STIX objects** → the intelligence content
- **STIX Relationship/Sighting** → the semantic connections
- **STIX Bundle** → optional transient STIX container
- **TAXII Collection** → logical exchange repository
- **TAXII Envelope** → transport wrapper used by TAXII endpoints

### Classroom TAXII exercise

The classroom collection name `dya-cti` is fictional.

The skill is to explain:

> A TAXII client with read access could retrieve STIX objects from the `dya-cti` Collection.

and, if write permission existed:

> A client could add valid STIX objects to the Collection.

The lesson does not require standing up a server.

## 2. Knowledge Check

1. Why does putting two STIX objects in the same Bundle not establish that they are related?
2. Which required Indicator field is missing from the old shortcut list of `type`, `spec_version`, `id`, `created`, and `modified`?
3. Explain the difference among a STIX Bundle, a TAXII Collection, and a TAXII Envelope.

## 3. Summary

STIX production is graph construction, not merely JSON packaging.

Use precise relationships, model Sightings with the Sighting object, validate the required fields for each object type, and remember that Bundle membership does not create semantic relationships.

TAXII 2.1 provides the exchange mechanism. Collections hold/expose CTI, and TAXII Envelopes wrap STIX objects in Collection exchanges.


## Supporting References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
- [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)
- [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)

**Next:** [2.7.3 – Creating Finished Intelligence Products](../03-finished-products/student-guide.md).
