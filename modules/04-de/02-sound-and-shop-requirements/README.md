# Making a Detection Sound and Meeting Shop Requirements

**Path:** `modules/04-de/02-sound-and-shop-requirements`

## Mapped proficiency items

| Matrix ID | Type | Item |
|---|---|---|
| 4.2 | K | Making a detection sound and meeting shop requirements |
| 4.2.1 | T | Test a draft or change |
| 4.2.2 | T | Mark local requirements met/missing |
| 4.2.3 | T | Close the loop with the nominator |

## Concepts taught

- positive detection tests
- negative / benign-control tests
- data-availability tests
- behavioral validation
- local requirements vs external rule formats
- meaningful nominator feedback
- executed detection validation with target, benign-control, and data-path evidence
- deferred local-requirement qualification after verified 4.8 onboarding

## Supporting references

- [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)
- [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)
- [Sigma Filters](https://sigmahq.io/docs/meta/)
- [CTID – Continuous Emulation as Detection Validation](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/)

## Practical artifact

- [detection-validation-practical.md](detection-validation-practical.md) — controlled execution event for `4.2.1`; Part B returns after 4.8 for `4.2.2` using the verified local requirement list.
