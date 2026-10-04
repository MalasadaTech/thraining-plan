# Module 4.4 – Tune Requests from SOC

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.4 B / C / C ; 4.4.1 3c / 4c / 4d ; 4.4.2 3c / 4c / 4c  
- SOC: 4.4 A / B / B ; 4.4.1 1a / 2b / 3c ; 4.4.2 1a / 2b / 2b  
- Hunter: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
- CTI: 4.4 A / A / B ; 4.4.1 1a / 1a / 2b ; 4.4.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Review a SOC request concerning a **live detection** and choose **tune, exception/filter, replace, leave, or retire** with supporting evidence.
2. Distinguish detection-tuning work from investigation, containment, blocking, or other operational requests.

**Mapped Proficiency Items:**
- K: 4.4 – Tune requests from SOC
- T: 4.4.1 – Pick tune / exception / replace / leave / retire and cite why
- T: 4.4.2 – Reject/route a request that is investigation, block, or IR containment

## 1. Key Concepts

A tune request begins with a detection that is **already live**.

SOC has operational evidence that something about the current analytic may need attention:
- excessive benign volume;
- a known blind spot;
- missing context;
- a pattern the current logic handles poorly;
- an old analytic that may no longer provide value.

That makes tuning different from a **new nomination**.

Whether the organization uses a separate queue, ticket type, or shared workflow is local. The important conceptual distinction is the **work type**, not the existence of a separate “inbox.”

### A reviewable tune request

Useful inputs include:

- the live detection/rule ID or name;
- representative alert/case examples;
- the observed problem;
- what SOC believes should behave differently;
- a pointer to the investigation or case where the problem was observed.

If evidence is missing, send the request back with a precise ask.

### Five engineering outcomes

| Outcome | Use when |
|---|---|
| **Tune** | Adjust logic while preserving the detection's purpose. |
| **Exception / filter** | Exclude a narrow, understood benign condition. |
| **Replace** | A different analytic design should supersede the live rule. |
| **Leave** | Evidence shows the rule is behaving as intended and the alert burden is justified. |
| **Retire** | The rule no longer provides enough value to remain active. |

### Exceptions create blind spots if they are too broad

A filter should be as narrow as the benign condition permits.

After adding an exception, rerun the **positive test** from 4.2. A filter that removes the noise but also suppresses the malicious/target behavior is not a successful tune.

Sigma supports filters as a formal mechanism for excluding matching events, but a filter's existence does not make the exclusion safe. See [Sigma Filters](https://sigmahq.io/docs/meta/).

### “Noisy” is evidence to investigate—not an automatic reason to disable

Ask:
- What benign population is producing the volume?
- Is the target behavior still valuable?
- Can the benign pattern be distinguished?
- Does the rule need broader redesign?
- Is the operational cost still justified?

A rule can be noisy and still deserve to remain active while DE works on a safer improvement.

### Requests that are not tuning

**“Investigate why this host ran PowerShell.”**  
→ investigation workflow

**“Isolate this endpoint.”**  
→ IR/containment owner

**“Block this IP.”**  
→ enforcement/control owner

**“Create a new analytic for behavior we do not cover.”**  
→ nomination/new detection work

Route those requests instead of trying to turn them into tune outcomes.

## 2. Knowledge Check

1. What makes a tune request different from a nomination?
2. Why should an exception/filter be followed by a positive re-test?
3. SOC says “this rule is noisy; investigate the host.” Is that a tune request?

## 3. Summary

Tune requests use operational evidence from a **live detection**.

Choose tune, narrow exception, replace, leave, or retire based on what the evidence shows. Re-test after change, especially after adding exclusions.

Investigation, containment, and blocking are separate operational workflows.

**Next:** **4.5 – Hunt and Intel Packages**.

## Supporting Reference

- [Sigma Filters](https://sigmahq.io/docs/meta/)
