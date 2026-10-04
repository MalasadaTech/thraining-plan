# Module 2.3.3 – Cyber Kill Chain in Intelligence Analysis

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.3.3 B / C / C ; 2.3.3.1 3c / 4c / 4c  
- Hunter: 2.3.3 B / C / C ; 2.3.3.1 3c / 4c / 4c  
- SOC: 2.3.3 A / B / B ; 2.3.3.1 2b / 3c / 4c  
**Estimated Time:** 20–25 minutes

## Learning Objectives

1. Use the seven Cyber Kill Chain stages to describe attack progression in an intelligence product.
2. Assign a stage only when the observed or reported activity supports that stage and explain when the evidence is insufficient to distinguish between stages.

**Mapped Proficiency Items:**
- K: 2.3.3 – Cyber Kill Chain in intelligence analysis
- T: 2.3.3.1 – Identify the Kill Chain stage of observed or reported activity

## 1. Key Concepts

Lockheed Martin's Cyber Kill Chain describes seven stages adversaries progress through in a successful intrusion:

1. **Reconnaissance**
2. **Weaponization**
3. **Delivery**
4. **Exploitation**
5. **Installation**
6. **Command and Control**
7. **Actions on Objectives**

References:
- [Lockheed Martin – Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [Lockheed Martin overview PDF](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)

The value of the framework in CTI is to describe **progression that the evidence supports**. It is not a requirement to fill all seven stages.

### What each stage means

| Stage | Evidence that can support it |
|---|---|
| **Reconnaissance** | Target research, scanning, or other preparation focused on understanding the victim. |
| **Weaponization** | Building or pairing exploit and payload before delivery. Often described in external reporting rather than victim telemetry. |
| **Delivery** | Transmitting the weapon or payload to the target environment. |
| **Exploitation** | Triggering exploitation or executing the delivered mechanism to gain code execution/access. |
| **Installation** | Installing or establishing malware, an implant, persistence, or other foothold on the victim. |
| **Command and Control** | Establishing or using a channel that allows adversary control/communication. |
| **Actions on Objectives** | Performing the intended mission effect, such as collection, theft, disruption, or destruction. |

### Do not force a stage from an ambiguous event

A process event such as:

`wscript.exe` → `powershell.exe -enc ...`

shows execution. By itself, it does **not** necessarily tell you whether the Cyber Kill Chain role is Exploitation, Installation, or part of a later stage.

The surrounding context matters.

Examples:

- malicious script arrives by email → **Delivery**
- user/script execution triggers malicious code → may support **Exploitation**
- a payload is written and persistence is established → **Installation**
- the implant begins periodic callbacks → **Command and Control**

The framework is describing the role of the activity in the intrusion, not simply the name of the process.

### A download is not automatically Installation

Suppose A12 shows a successful download of `/update.exe`.

That can support **Delivery** of a follow-on payload into the victim environment.

It supports **Installation** only when there is evidence that the payload was installed, established, or otherwise placed as the intrusion's foothold.

If the download occurs over an established control channel, it may also occur during Command and Control, but the file-transfer event itself does not prove the control relationship.

### Gaps are valuable

If the product supports Delivery and Command and Control but contains no evidence of Reconnaissance or Weaponization, leave those stages unfilled.

That tells the reader something important about the evidence base.

The Kill Chain should help answer:

> Which parts of the progression do we actually know?

—not—

> Which stages probably happened because every attack has a beginning?

### Worked progression example

Suppose reporting contains:

- phishing email with `invoice.vbs` → **Delivery**
- user launches the script and malicious code executes → **Exploitation**
- malware writes a persistent implant → **Installation**
- implant checks in to the update domain every 60 seconds → **Command and Control**

A CTI product can list those supported stages and leave Reconnaissance, Weaponization, and Actions on Objectives unresolved if they are not in the evidence.

## 2. Knowledge Check

1. Why should an intelligence product not list all seven Kill Chain stages by default?
2. A host successfully downloads `/update.exe`, but there is no evidence it executes or persists. Which stage is best supported, and which stage would require more evidence?
3. `wscript.exe` launches encoded PowerShell. Why is the process event alone not enough to declare “Installation”?

## 3. Summary

The Cyber Kill Chain describes attack progression, but stage assignment depends on context.

List only the stages the evidence supports. A delivery event does not automatically establish installation; code execution does not automatically establish persistence; network traffic does not automatically establish command and control.

Unobserved stages are useful gaps, not blanks that need to be filled.


## Supporting References

- [Lockheed Martin – Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)
- [Cyber Kill Chain overview PDF](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/Gaining_the_Advantage_Cyber_Kill_Chain.pdf)

**Next:** [2.4.1 – Internal Threat Intelligence Platform](../../04-platforms/01-internal-tip/student-guide.md).
