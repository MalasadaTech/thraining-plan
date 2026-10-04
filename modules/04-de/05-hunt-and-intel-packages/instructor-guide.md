# Instructor Guide – Module 4.5 – Hunt and Intel Packages

**Estimated Time:** 20–25 minutes

## Purpose

Teach DE to translate hunt/intel evidence into durable coverage decisions without turning every IOC or infrastructure pivot into a production analytic.

## Review Sequence

1. What defensive need does the package identify?
2. Do we already cover it?
3. Does existing coverage need change?
4. Is a new analytic justified?
5. If not, is “no new rule” the correct result?

## Durability Discussion

Exact indicators may support short-lived search, monitoring, or enforcement.

Behavior often provides better durability when:
- it is distinctive enough;
- telemetry exists;
- the behavior is expected to recur across infrastructure changes.

Do not teach “IOC bad / behavior good” as an absolute. The engineering question is expected utility and lifetime.

## Common Student Challenges

| Challenge | Coaching response |
|---|---|
| Creates new rule before checking existing coverage. | Reuse first. |
| Treats every IOC as durable. | Ask how easily it rotates and how long it remains useful. |
| Converts candidate infrastructure to block list. | Route enforcement decisions to the proper control owner. |
| Thinks “no new rule” means package had no value. | It may confirm existing coverage or provide investigative context. |

## Knowledge Check – Answer Key

1. To avoid redundant analytics and unnecessary operational burden.
2. No; utility, durability, context, and existing coverage matter.
3. No. Shared infrastructure requires analysis, and blocking follows the control-owner process.
