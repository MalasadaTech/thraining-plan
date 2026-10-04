# Instructor Guide – Module 4.1 – What Detection Engineering Owns

**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Purpose

Establish Detection Engineering as lifecycle ownership of detection capability rather than “the team that writes queries.”

## Teaching Model

DE owns:
- new detection work;
- validation;
- deployment;
- tuning/change;
- maintenance;
- retirement/replacement.

Adjacent work:
- SOC/hunt/CTI nominate needs;
- 1.3 teaches rule syntax/mechanics;
- enforcement follows the local control-owner model.

## Important Boundary

Avoid teaching “DE never blocks” as a universal industry fact.

In this course, firewall/EDR-prevention/containment requests route to the authorized enforcement owner. A real organization may assign some of those controls to DE.

## A12 Examples

- rough hunt package asking for durable encoded-PowerShell coverage → nomination / DE review;
- “write Sigma syntax for this condition” → 1.3;
- noisy live analytic → DE tune/change;
- firewall block request → local enforcement owner.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Treats a rough nomination as incomplete DE work. | DE owns turning the defensive need into a production-capable analytic. |
| Treats syntactic validity as deployment readiness. | Ask how it was validated, deployed, monitored, and maintained. |
| Assumes every defensive control belongs to DE. | Use the local operating model to separate detection from enforcement authority. |

## Knowledge Check – Answer Key

1. DE owns the lifecycle after authoring: validation, deployment, maintenance, tuning, and retirement.
2. Yes, if the need and evidence/context are clear enough to review.
3. Blocking is an enforcement action whose ownership varies by organization; the local control model decides who may perform it.
