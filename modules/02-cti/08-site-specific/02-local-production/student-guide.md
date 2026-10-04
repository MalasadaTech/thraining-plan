# Module 2.8.2 – Local Production and Approval Processes

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.2 B / C / C ; 2.8.2.1 3c / 4c / 4c ; 2.8.2.2 3c / 4c / 4c  
- Hunter: 2.8.2 A / A / B ; 2.8.2.1 1a / 1a / 2b ; 2.8.2.2 1a / 1a / 2b  
- SOC: 2.8.2 A / A / A ; 2.8.2.1 1a / 1a / 1a ; 2.8.2.2 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Locate and explain the shop's local workflow for collection requests, product review, approval, release, and archival.
2. Follow the known process for a product or collection request and clearly identify any workflow element that has not yet been obtained.

**Mapped Proficiency Items:**
- K: 2.8.2 – Local production and approval processes
- T: 2.8.2.1 – Follow the local process for requesting collection or producing and approving products
- T: 2.8.2.2 – Document and archive intelligence products according to local standards

## 1. Key Concepts

A finished analytic draft is not automatically an official product.

Organizations normally have local steps that determine:
- how additional collection is requested;
- who reviews a product;
- who can approve or release it;
- how changes are resolved;
- where the official version is recorded and retained.

The names of those steps, tools, and roles are local.

This module teaches how to **orient yourself to that process**.

### Build a local workflow map

A useful orientation map answers:

| Workflow question | Local answer |
|---|---|
| How is a collection request submitted? | ______ |
| Who receives / triages it? | ______ |
| Who reviews analytic products? | ______ |
| What review standards/checklist are used? | ______ |
| Who is authorized to approve/release? | ______ |
| Where is the authoritative copy stored? | ______ |
| How are revisions/version history recorded? | ______ |
| What metadata must be preserved? | ______ |

The blanks are completed from the real shop process.

### Collection planning and collection requesting are different

Module 2.1.9 taught collection planning:
- what information is needed;
- which source class may provide it;
- what scope is appropriate.

This module addresses the **local mechanism used to request or coordinate that collection**.

Example:

> **Analytic need:** determine whether `/update.exe` was successfully transferred.  
> **Collection requirement:** obtain response/file-transfer or host-artifact evidence.  
> **Local request path:** use the shop's approved collection-request workflow.

The first two can be reasoned about generically. The last one must be learned locally.

### Review is not the same as approval

A reviewer may:
- check sourcing;
- challenge reasoning;
- check analytic standards;
- verify handling/markings;
- edit for clarity.

An approval authority is the role empowered by local policy to release or make the product official.

Some shops combine those roles; others separate them.

The analyst should learn the actual local arrangement rather than assume one universal model.

### Archive the authoritative version

The official product should be stored according to local standards.

Useful questions include:
- Which repository is authoritative?
- Is the draft also retained?
- How are revisions numbered?
- Are source notes stored with the product or separately?
- What handling/retention rules apply?
- How is superseded content identified?

This matters because future analysts need to know which version was actually released.

### When the local process is not yet known

Use explicit onboarding status:

> **Local production/approval path not yet verified.**

Then identify the missing element:

> Need current review/approval workflow and authoritative archive location from the team lead/process owner.

That is more useful than inventing a Jira queue, ticket name, or folder because the statement tells the team exactly what the analyst still needs to learn.

### A12 walkthrough

Suppose the A12 assessment is drafted.

Before release, the analyst should be able to answer:

1. Who reviews this kind of product?
2. Which standard/checklist applies?
3. Who approves/releases it?
4. Which channel/repository receives the official copy?
5. How is the final version recorded?

If those answers are not known, the product may be analytically complete while the **production workflow is not yet complete**.

## 2. Knowledge Check

1. What is the difference between collection planning and the local collection-request process?
2. Why should review authority and approval authority be learned separately?
3. You have a finished A12 draft but do not know the official archive location. What should you record?

## 3. Summary

Local production is an orientation-and-follow-through skill.

Learn the collection-request path, review process, approval authority, release step, versioning, and authoritative archive.

When part of the workflow has not yet been obtained, identify that gap precisely so it can be closed.


## Reference Model

This module intentionally relies on the organization's **local production, approval, records, and collection-request procedures** as the source of truth.

**Next:** [2.8.3 – Local Dissemination Channels and Customers](../03-local-dissemination/student-guide.md).
