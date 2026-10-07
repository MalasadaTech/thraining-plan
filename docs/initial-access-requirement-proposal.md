# Initial Access — Gate 1 Requirement Proposal

**Proposer:** Curriculum maintenance  
**Date:** 2026-10-04  
**Status:** Approved

## Topic

All four defensive roles should recognize common initial-access paths, distinguish the observed access/delivery evidence from later execution or compromise, and identify what additional evidence would justify a stronger conclusion.

## Justification

The current shared-foundations block teaches defensive roles, handoffs, analytical frameworks, external research tools, and environment/signal flow, but it does not directly teach the common ways an adversary may first gain or attempt to gain access.

That leaves a reasoning gap between the shared framework material and the role-specific evidence lessons. The A12 case begins with suspicious host activity after the possible entry point, so learners can currently follow the investigation without first having a compact mental model for how initial access may have occurred.

Adding a shared initial-access lesson would give learners a common vocabulary before SOC, CTI, Hunting, and Detection Engineering diverge. It would also reinforce the course-wide evidence rule:

> Describe what the evidence shows first. Then decide what it means.

The new material should help prevent common analytical overreach:

- a phishing message or malicious attachment does not by itself establish execution;
- a request to a malicious or compromised website does not by itself establish successful exploitation;
- a vulnerable public-facing application does not by itself establish that a specific exploit succeeded;
- a valid-account login does not by itself establish account compromise;
- a trusted relationship or supply-chain exposure does not by itself establish that the relationship was the entry path.

## Proposed obligation

### Knowledge

Learners should understand:

1. **Initial Access as an adversary objective**
   - ATT&CK Initial Access describes ways adversaries try to gain a foothold.
   - Initial access should not be treated as interchangeable with later execution, persistence, or impact.
   - Cyber Kill Chain Delivery/Exploitation and ATT&CK Initial Access can describe related evidence from different analytical views; one framework label should not be substituted mechanically for another.

2. **Common initial-access families**
   - phishing and malspam, including malicious attachments, links, and messaging/service delivery;
   - exploitation of public-facing applications or exposed services, including vulnerability/CVE-driven intrusion attempts;
   - web-based access such as drive-by compromise, watering-hole activity, malvertising, and search/SEO poisoning that leads a user toward adversary-controlled content;
   - abuse of valid accounts and external remote services;
   - trusted relationships and supply-chain compromise as important third-party paths.

   The lesson should teach these as a practical map, not as an exhaustive ATT&CK catalog.

3. **Evidence progression**
   - exposure or delivery;
   - user/system interaction where relevant;
   - access attempt;
   - evidence of successful access;
   - later execution or follow-on behavior.

   Learners should recognize that evidence at one point in this progression does not automatically prove the later points.

4. **Typical evidence sources**
   - mail/security gateway and message metadata;
   - identity/authentication and remote-access logs;
   - proxy, DNS, HTTP, and other network evidence;
   - public-facing application, WAF, and service logs;
   - endpoint file/process evidence;
   - vulnerability and patch context.

   This is an orientation to evidence sources. Deep field reading remains in the existing SOC and role-specific lessons.

### Task

Given a short incident or intelligence scenario, the learner should:

1. identify the most defensible initial-access path or state that it remains unresolved;
2. cite the evidence supporting that judgment;
3. state what the evidence does **not yet establish**;
4. identify the next evidence source or question that would strengthen or reject the hypothesis.

## Proposed proficiency

These are proposed Gate-1 ratings and should become canonical only when the requirement is approved and assigned an ID.

| Role | 3-level | 5-level | 7-level |
|---|---|---|---|
| SOC | K: A / T: 2b | K: B / T: 3c | K: C / T: 4c |
| Hunter | K: A / T: 2b | K: B / T: 3c | K: C / T: 4c |
| CTI | K: A / T: 2b | K: B / T: 3c | K: C / T: 4c |
| Detection Engineer | K: A / T: 1a | K: B / T: 2b | K: B / T: 3c |

Rationale: SOC, Hunting, and CTI should be able to reason from evidence about a possible entry path. Detection Engineering needs the same conceptual map but is not being assigned primary ownership of reconstructing initial access.

## Placement

- [x] New module
- [ ] Add to an existing module

**Assigned teaching-unit ID:** `0.9` knowledge / `0.9.1` task.

**Suggested outline headings:**
- `[K] Common Initial Access Paths`
- `[T] Initial Access Evidence and Reasoning Tasks`

**Shared vs role-specific:** `modules/00-intro/`

**Approved teaching position:** after `0.8 Environment / signal flow` and before the Shared Foundations Section Summary. The summary moves from `0.9` to `0.10`.

This placement allows the learner to first understand the organization's exposed paths and evidence sources, then learn the common ways adversaries may use those paths, then complete the shared-foundations synthesis before entering SOC.

The approved numbering is `0.9` for Initial Access and `0.10` for the Shared Foundations Section Summary.

## Stay-in-this-lesson boundary

Teach the entry-path mental model and evidence reasoning.

Keep the following depth in their existing homes:

- detailed endpoint-event interpretation → `1.1`;
- Zeek/protocol field interpretation → `1.2`;
- alert investigation and classification → `1.4`;
- CTI analytical frameworks and production → `2.x`;
- hunt development and technique hunting → `3.x`;
- detection design and lifecycle → `4.x`.

The initial-access lesson should help learners recognize *which question to ask next* rather than duplicating those later skills.

## A12 integration after Gate 2

Do not invent a new A12 entry event merely to fill the lesson.

The existing A12 evidence does not establish whether `invoice.vbs` arrived through phishing, a web path, public-facing exploitation, credential abuse, a trusted relationship, or another mechanism.

After the requirement and lesson are approved, update the A12 canonical sources so the story explicitly uses that absence as a reasoning point:

- the SOC can recognize common initial-access hypotheses;
- the current case evidence does not identify which one occurred;
- the analyst should name the evidence that would test those hypotheses;
- the story continues from the existing `wscript` → encoded PowerShell evidence without manufacturing a second plot or a resolved entry path.

This preserves the case's evidence-first model while connecting the new shared concept to the recurring scenario.

## Already signed off

For currently qualified personnel:

- [x] Delta lesson
- [ ] Short brief
- [ ] Wait until next recert
- [ ] Other

The delta should cover only the new shared initial-access requirement. Existing role-specific sign-offs do not need to be repeated.

## Primary technical references

- MITRE ATT&CK — Initial Access: https://attack.mitre.org/tactics/TA0001/
- CISA — #StopRansomware Guide (common initial access vectors, including SEO/search poisoning): https://www.cisa.gov/resources-tools/resources/stopransomware-guide
- MITRE ATT&CK — Phishing (T1566): https://attack.mitre.org/techniques/T1566/
- MITRE ATT&CK — Drive-by Compromise (T1189): https://attack.mitre.org/techniques/T1189/
- MITRE ATT&CK — Exploit Public-Facing Application (T1190): https://attack.mitre.org/techniques/T1190/
- MITRE ATT&CK — Valid Accounts (T1078): https://attack.mitre.org/techniques/T1078/
- MITRE ATT&CK — External Remote Services (T1133): https://attack.mitre.org/techniques/T1133/
- MITRE ATT&CK — Trusted Relationship (T1199): https://attack.mitre.org/techniques/T1199/
- MITRE ATT&CK — Supply Chain Compromise (T1195): https://attack.mitre.org/techniques/T1195/

## Board decision

**Decision:** Approved  
**Date:** 2026-10-04  
**Notes:** Assigned `0.9` / `0.9.1`; placement after `0.8` approved; Shared Foundations Summary renumbered to `0.10`; proposed proficiency ratings approved.
