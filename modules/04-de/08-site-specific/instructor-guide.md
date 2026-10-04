# Instructor Guide – Module 4.8 – Site-Specific Detection Engineering Knowledge

**Estimated Time:** 20–25 minutes

## Purpose

Turn the old “do not invent local policy” lesson into a practical Detection Engineering onboarding exercise.

## Two Local Artifacts to Locate

1. **Current detection requirements/standards**
2. **Current lifecycle path** from intake through review, approval, deployment, monitoring, change, rollback, and retirement

## Requirements Orientation

Have learners identify:
- authoritative location;
- owner;
- version/effective date;
- applicable platform/scope.

Public formats such as Sigma can illustrate common metadata but do not define local policy.

Reference: [Sigma Rules Specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html)

## Lifecycle Map

Require the learner to fill local answers for:
- intake;
- engineer;
- test/stage;
- review;
- approval;
- deploy;
- post-deploy monitoring;
- rollback;
- change/tune;
- retire/replace;
- authoritative source repository.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Copies public Sigma fields as local requirements. | Ask where local policy adopts those fields. |
| Knows deployment button but not approval authority. | Deployment mechanics and authority are different. |
| Assumes production console is authoritative source. | Verify source control / system of record. |
| Guesses missing process. | Record the precise onboarding gap and obtain it from the owner. |

## Knowledge Check – Answer Key

1. Sigma defines a portable rule format; the organization defines its deployment/governance requirements.
2. Any four of review, approval, deploy, monitoring, rollback, tune/change, retire, repository/source control.
3. Record that approval and rollback authority have not yet been verified and identify the process owner/source needed.
