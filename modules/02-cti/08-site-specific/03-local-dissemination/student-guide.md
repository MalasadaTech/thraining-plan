# Module 2.8.3 – Local Dissemination Channels and Customers

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.8.3 B / C / C ; 2.8.3.1 3c / 4c / 4c  
- Hunter: 2.8.3 A / A / B ; 2.8.3.1 1a / 1a / 2b  
- SOC: 2.8.3 A / A / A ; 2.8.3.1 1a / 1a / 1a  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Locate the authoritative local customer/channel map and identify the primary internal and external consumers the CTI function actually supports.
2. Select the correct local dissemination path for a product, or clearly identify that the required customer/channel mapping has not yet been obtained.

**Mapped Proficiency Items:**
- K: 2.8.3 – Local dissemination channels and customers
- T: 2.8.3.1 – Disseminate a product using the correct local channels and customers

## 1. Key Concepts

Module 2.7.5 taught the general dissemination problem:

- Who needs the product?
- Which approved channel should carry it?
- What sharing/handling restrictions apply?

This module asks for the **local answers**.

Every CTI team has an operating context:
- internal customers;
- possibly external customers or partners;
- approved systems/channels;
- recurring products;
- escalation or urgent-notification paths;
- restrictions on what can be shared with each audience.

A new analyst should learn that map early.

### Customer means an established intelligence consumer

A customer is not simply anyone who might find the information interesting.

The local customer map should tell you which roles, teams, leaders, partner organizations, or other authorized recipients the CTI function is expected to support.

Examples of categories that may exist locally:
- SOC;
- incident response;
- threat hunting;
- detection engineering;
- vulnerability management;
- leadership;
- mission/business units;
- external partners.

These are examples only. The actual list must come from the local organization.

### Map product → customer → channel

A useful orientation table looks like:

| Product / use | Primary customer | Approved channel | Handling notes |
|---|---|---|---|
| Urgent incident intelligence | ______ | ______ | ______ |
| Routine CTI assessment | ______ | ______ | ______ |
| Leadership awareness | ______ | ______ | ______ |
| Hunt-support package | ______ | ______ | ______ |
| External partner share | ______ | ______ | ______ |

The blanks are filled from the site's authoritative customer/channel guidance.

### Channel is more than convenience

A channel may be approved because it provides:
- access control;
- auditability;
- retention;
- classification/handling support;
- ticket linkage;
- version control;
- notification to the right group.

That is why “the right person” does not automatically make an unofficial personal channel acceptable.

### External sharing needs explicit authorization

If the organization supports external customers or partners, learn:
- who they are;
- what products may be shared;
- which channel is approved;
- what marking/handling rules apply;
- whether additional approval is required.

Do not assume an external partner from familiarity or prior collaboration.

### A12 example

Suppose the A12 assessment is approved and ready for dissemination.

Before sending, the analyst should identify from the local map:

1. Which internal customer owns the immediate operational decision?
2. Is there a separate leadership customer?
3. What approved channel is used for each?
4. What handling/sharing instructions apply?
5. Does any external party receive the product?

If the local customer/channel map has not been provided, record:

> **Local dissemination path not yet verified.**

Then identify the missing source/owner rather than selecting a convenient recipient from the classroom scenario.

### Keep 2.7.5 and 2.8.3 connected

**2.7.5** taught the general dissemination method and TLP concepts.

**2.8.3** supplies the organization-specific customer names, channels, and routing rules.

The general model helps you ask the right questions. The local map provides the actual answer.

## 2. Knowledge Check

1. Why is “someone who might like the report” not enough to make them a CTI customer?
2. What four fields belong in a useful local product/customer/channel map?
3. The A12 product is approved, but you have never been shown the customer/channel map. What should you record?

## 3. Summary

Local dissemination requires an authoritative map of **who the CTI function serves and how each product is sent**.

Learn the customer, channel, and handling path for the products you produce.

When the map is missing, record that onboarding gap explicitly instead of substituting a convenient recipient or personal channel.

This completes the **2.x CTI block**.


## Reference Model

This module intentionally relies on the organization's **local customer, dissemination, handling, and partner-sharing guidance** as the source of truth.

**Next:** Continue to [3.x – Threat Hunting](../../../03-hunter/00-intro/student-guide.md).
