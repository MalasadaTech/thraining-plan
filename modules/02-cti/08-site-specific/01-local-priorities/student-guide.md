# Module 2.8.1 – Local Intelligence Requirements and Priorities

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.1 B / C / C ; 2.8.1.1 3c / 4c / 4c  
- Hunter: 2.8.1 A / A / B ; 2.8.1.1 1a / 1a / 2b  
- SOC: 2.8.1 A / A / A ; 2.8.1.1 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Locate and verify the shop's **current intelligence requirements and priorities** using the authoritative local source.
2. Align analytic work to a stated local requirement and clearly identify when the current priority list has not yet been obtained.

**Mapped Proficiency Items:**
- K: 2.8.1 – Local intelligence requirements and priorities
- T: 2.8.1.1 – Identify current local priorities and align analytic work to them

## 1. Key Concepts

Earlier modules taught how intelligence requirements work. This module asks a different question:

> **What priorities are actually in force in this organization today?**

That answer cannot come from a generic textbook or this classroom scenario. It must come from the shop's own authoritative source.

A new analyst should learn three things early:

1. **Where the current priority list lives**
2. **Who owns or maintains it**
3. **How to tell that the copy is current**

The source might be a formal requirements document, a team workspace, a program plan, a briefing deck, or another locally approved system. The specific source is site-dependent.

### Current means current

Requirements and priorities change.

A copy from last quarter may still be useful background, but it should not automatically be treated as the list governing today's work.

Before aligning analysis to a requirement, verify:
- the effective date or version;
- whether the list has been superseded;
- the owning role or authority;
- whether the requirement is active, standing, deferred, or retired, if the local process uses those states.

### PIRs are one kind of local priority structure

Some organizations use **Priority Intelligence Requirements (PIRs)**. Others may use:
- intelligence requirements;
- standing requirements;
- leadership priorities;
- mission priorities;
- collection or analytic priorities.

The important point is not the label. The analyst needs the **authoritative list that governs local work**.

Module 2.1.4 taught what a PIR and intelligence requirement are. This module teaches how to orient yourself to the local implementation.

### Align work only when the connection is explicit

Suppose A12 is an active incident involving a Windows workstation.

That makes A12 operationally important, but it does not automatically make A12 a PIR.

To say that A12 analysis supports a local requirement, you should be able to point to the actual requirement.

Example:

> **Local requirement:** Assess malicious use of scripting interpreters on enterprise Windows endpoints.  
> **A12 alignment:** The incident includes encoded PowerShell on `WS-JLEE`, so the analysis directly supports this requirement.

Without the local requirement list, the correct status is:

> **Current priority alignment not yet verified.**

That statement is more useful than assigning an invented PIR number because it tells the team exactly what onboarding information is still missing.

### Record the source of the priority

When practical, preserve:
- requirement or priority title/ID;
- authoritative source;
- version/effective date;
- owner;
- how the current analytic task supports it.

This makes later review easier when priorities change.

### A practical onboarding note

A new analyst could maintain a small orientation entry:

| Item | Local answer |
|---|---|
| Authoritative priority source | ______ |
| Owner / maintainer | ______ |
| Current version / effective date | ______ |
| Review cadence | ______ |
| How work is mapped to a requirement | ______ |

The blanks are intentional. They are filled from the real shop, not from classroom fiction.

## 2. Knowledge Check

1. Why is an old priority list not automatically sufficient for current alignment?
2. A12 is an active incident, but you have not seen the current requirement list. What should you record about priority alignment?
3. What information should you capture about the authoritative local priority source?

## 3. Summary

Site-specific priority work begins by locating the authoritative local source and confirming that it is current.

Then map analytic work to the stated requirement it actually supports.

When that source has not yet been obtained, record the gap clearly instead of filling it with a classroom assumption.


## Related Modules

- [2.1.5 – RFI Intake and Prioritization](../../01-core-intel/05-rfi-intake/student-guide.md)
- [2.7.4 – RFI Responses and Closure](../../07-production/04-rfi-response/student-guide.md)
- 2.1.4 – Intelligence requirements
- 2.1.9 – Collection planning
- 2.8.2 – Local production and approval

**Next:** [2.8.2 – Local Production and Approval Processes](../02-local-production/student-guide.md).
