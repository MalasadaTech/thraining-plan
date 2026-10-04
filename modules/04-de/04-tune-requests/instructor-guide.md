# Instructor Guide – Module 4.4 – Tune Requests from SOC

**Estimated Time:** 20–25 minutes

## Purpose

Teach evidence-driven change to live detections without turning every complaint into a filter or every operational request into DE work.

## Key Distinctions

- Tune = live detection.
- Nomination = new/changed defensive need entering engineering review.
- Workflow/ticket separation is local; do not claim a universal “different inbox.”

## Outcomes

Tune  
Exception/filter  
Replace  
Leave  
Retire

## Safety of Exceptions

Teach the learner to:
1. identify the benign condition;
2. make the exclusion as narrow as possible;
3. re-run the positive detection test;
4. review whether the exception creates a meaningful blind spot.

Reference: [Sigma Filters](https://sigmahq.io/docs/meta/)

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| “Noisy = retire.” | Determine whether the rule still catches valuable behavior. |
| Adds broad allowlist. | Narrow the exclusion and re-test positive behavior. |
| Treats investigation as tuning. | Route to SOC/IR investigation. |
| Assumes tune requests always use a separate queue. | Work type is universal; queue design is local. |

## Knowledge Check – Answer Key

1. A tune request changes/reviews a live analytic; a nomination introduces a new defensive need.
2. To ensure the exclusion did not suppress the intended malicious/target behavior.
3. No. The request is investigation work.
