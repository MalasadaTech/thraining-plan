# Module 3.7.1 – Hunt Control and Lead Management

**Target Audience:** Threat Hunter (primary); SOC Analyst, CTI Analyst (secondary)  
**Proficiency Focus:**  
- Hunter: 3.7.1 B / C / C ; 3.7.1.1 3c / 4c / 4c  
- SOC: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
- CTI: 3.7.1 A / A / B ; 3.7.1.1 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes

## Learning Objectives

1. Locate the site's authoritative process for initiating, controlling, pausing/stopping, and changing the scope of a hunt.
2. Explain how out-of-scope hunt leads are recorded, triaged, and assigned locally.

## Mapped Proficiency Items

- K: 3.7.1 – Hunt control and lead management
- T: 3.7.1.1 – Follow the local process for initiating and controlling a hunt

## 1. Key Concepts

The hunt methodology learned in 3.2 tells you **how to formulate a hunt**.

This module asks:

> How does this organization authorize and govern one?

Those answers are local.

### Build the local governance map

| Question | Local answer |
|---|---|
| Who may initiate a hunt? | ______ |
| What prerequisites/approval are required? | ______ |
| Where is the hunt opened/tracked? | ______ |
| Who can expand or narrow scope? | ______ |
| Who can pause/stop a hunt? | ______ |
| What triggers escalation to incident response? | ______ |
| Where do out-of-scope leads go? | ______ |
| Who owns lead triage/deduplication? | ______ |

The blanks are filled from the real shop process.

### Why hunt control matters

A query can affect:

- analyst time;
- search infrastructure;
- regulated/sensitive data;
- live incident handling;
- other teams' workload.

A scope change from 50 user workstations to the entire enterprise may be operationally significant even when the query itself is harmless.

### Lead management prevents uncontrolled scope growth

A hunt often discovers something interesting that does not answer the current hypothesis.

Instead of silently expanding the hunt forever:

1. record the lead;
2. preserve why it matters and the evidence/source;
3. follow the local triage/ownership process;
4. decide whether it becomes a follow-on hunt, CTI question, detection task, or incident lead.

### Missing local process

Use an explicit onboarding status:

> **Local hunt-governance path not yet verified.**

Then identify the missing owner/source.

That is actionable because it tells the team what still needs to be learned.

## 2. Knowledge Check

1. Why might expanding a hunt's scope require local authorization?
2. What should happen to an interesting finding that is outside the current hunt scope?
3. What should you record if the local hunt-control process has not been provided?

## 3. Summary

Local hunt control defines how hunts become official, how scope changes are governed, and how follow-on leads are managed.

Learn the authoritative process and use it.

**Next:** **3.7.2 – Hunt Documentation Standards**.

## Reference Model

This module intentionally relies on the organization's local hunt-governance process.
