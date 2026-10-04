# Instructor Guide – Module 2.7.2 – STIX in Intelligence Production

**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Teach learners to connect STIX objects with defensible semantic relationships, validate object-specific requirements, and distinguish STIX containers from TAXII transport structures.

References:
- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
- [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)

## Major Technical Corrections

### 1. Bundle is not “the TAXII payload”

A STIX Bundle is a transient STIX container.

TAXII 2.1 Collection endpoints exchange STIX objects inside a **TAXII Envelope**.

Keep those concepts separate.

### 2. Bundle membership creates no relationship

Two objects in one Bundle are not semantically connected unless Relationship, Sighting, embedded references, or other STIX semantics connect them.

### 3. Validation is object-specific

The old shortcut of checking only:

`type`, `spec_version`, `id`, `created`, `modified`

is incomplete.

For example:
- Indicator also requires `pattern`, `pattern_type`, `valid_from`;
- Relationship requires `relationship_type`, `source_ref`, `target_ref`;
- Sighting requires `sighting_of_ref`.

### 4. Schema-valid does not automatically mean analytically sound

STIX permits an Indicator to `indicates` several target types, including Attack Pattern.

But the analyst still needs to ask:

> Does this detection pattern genuinely detect evidence of that Attack Pattern?

The graph should express the intelligence claim, not merely pass schema validation.

## A12 Example

Preferred simple graph:

- Indicator(hash pattern) **indicates** Malware
- Malware **uses** T1059.001 Attack Pattern
- Indicator **based-on** Observed Data
- Sighting of Indicator with supporting Observed Data

This preserves the distinction among:
- detection pattern;
- malicious object;
- behavior;
- observation;
- sighting.

## TAXII Teaching Model

**STIX objects** = content  
**Relationships/Sightings** = semantic graph  
**Bundle** = optional STIX container  
**Collection** = logical repository exposed by TAXII server  
**Envelope** = TAXII transport wrapper

Classroom `harbor-cti` remains fictional. Learners describe read/write interaction; they do not deploy infrastructure.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| “Bundle = all objects are related.” | Point to the STIX Bundle definition. |
| “TAXII sends a STIX Bundle.” | Teach TAXII Envelope in 2.1. |
| Uses `sighting-of` Relationship. | Use the Sighting SRO. |
| Validates only common fields. | Check required fields by object type. |
| Chooses a schema-valid but weak relationship. | Ask whether the analytic claim is actually supported. |

## Knowledge Check – Answer Key

1. A Bundle has no semantic meaning; relationships must be expressed explicitly.
2. `valid_from` (and also `pattern` and `pattern_type` are required Indicator-specific fields).
3. Bundle = optional STIX container; Collection = logical TAXII repository; Envelope = TAXII wrapper carrying STIX objects through Collection endpoints.

## References

- [OASIS STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
- [OASIS TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html)
- [STIX 2.1 Interoperability Test Document](https://docs.oasis-open.org/cti/stix-2.1-interop/v1.0/stix-2.1-interop-v1.0.html)
