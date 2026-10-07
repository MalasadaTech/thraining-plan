# Instructor Guide – Module 4.2 – Making a Detection Sound and Meeting Shop Requirements

**Estimated Time:** 20–25 minutes

## Purpose

Teach deployment readiness as an evidence-backed validation problem, not a syntax check.

## Three Test Questions

1. What **must fire**?
2. What realistic **must not fire**?
3. What **data must exist** for the analytic to work?

Use positive, negative/benign-control, and data-availability tests.

## Teaching Notes

- A positive test proves the tested behavior matched under those conditions; it does not prove universal coverage.
- A negative test should use realistic near-neighbor benign activity.
- Verify required fields, population coverage, parsing, and timeliness.
- Keep local deployment fields separate from external rule-format conventions.
- Have the learner write a meaningful close-the-loop note, especially when DE changes the original idea.

References:
- [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)
- [Sigma Logsources](https://sigmahq.io/docs/basics/log-sources.html)
- [CTID detection validation discussion](https://ctid.mitre.org/blog/2025/08/04/lessons-from-sharepoint-vulnerability-cve-2025-53770/)

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| “The query runs, so it is sound.” | Ask for positive, negative, and data-path evidence. |
| Tests only the exact malicious hash. | Test the behavioral claim where practical. |
| Treats Sigma metadata as local policy. | Sigma is a format; the local list is the deployment authority. |
| Writes “done” to nominator. | Explain shipped/changed/sent-back and what changed. |

## Practical Demonstration

Use [detection-validation-practical.md](detection-validation-practical.md) for `4.2.1`. The evaluator should observe the learner actually run the supplied draft against the controlled dataset and interpret positive, benign-control, and data-path results. Discussion of the three test categories is not sufficient sign-off for **test a draft or change**.

`4.2.2` has a later local prerequisite. Teach the checking method here, but complete/sign off the met/missing review only after the learner obtains the verified local shop requirement list in 4.8 (or an authorized local simulation). Do not invent a DYA/BHM field list.

## Knowledge Check – Answer Key

1. Positive/intended, negative/benign-control, and data availability.
2. Required logs/fields may be absent, late, misparsed, or not collected for the relevant population.
3. No. Public format fields are not automatically local requirements.
