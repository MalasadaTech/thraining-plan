# Module 1.5.3 – Notification and Distribution

**Target Audience:** SOC Analyst (primary), Threat Hunter and CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.5.3.1 A / B / C · 1.5.3.2 2b / 3c / 4c  
- Hunter: 1.5.3.1 A / B / B · 1.5.3.2 2b / 3c / 4c  
- CTI: 1.5.3.1 B / C / C · 1.5.3.2 3c / 4c / 4c  
**Estimated Time:** 60–75 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Read a **notification chart** (who gets which report).
2. Decide whether **leadership awareness** is required.
3. Name the **approved channel** and reject the wrong one.
4. **Route** a report: recipients + leadership yes/no + channel.

**Mapped Proficiency Items:**
- K: 1.5.3.1 – Notification and distribution
- T: 1.5.3.2 – Route a report: name recipients, leadership awareness, and the approved channel

---

## 1. Key Concepts

You already know the **type** (**1.5.1**) and the **clock** (**1.5.2**). This hour is **who** and **how**. Shift-change recording location is **1.7**.

**Classroom notification chart (this lesson only):**

| Report type | Recipients | Leadership awareness | Approved channel |
|-------------|------------|----------------------|------------------|
| **Incident** | SOC queue + **IR** | **Yes** — duty SOC lead | **Ticket** (case system) |
| **RFI** | The **named team** (CTI, hunt, or IT) | **No**, unless they asked or the chart says so | **Ticket** or **approved RFI form** |
| **Informational** | Named distro (`soc-aware`) | **Yes** — short awareness | **Approved email / distro** |

If your site has a real chart, use it. The obligation is **chart + leadership flag + approved channel**, not these names.

**Approved channels (outline c):** ticket, approved form, approved distro.  
**Not approved (classroom):** personal SMS, private chat to a friend, personal email off-domain.

**Leadership awareness (outline b)** is a yes/no on the chart — not “email the CEO.” Duty SOC lead counts.

| This lesson | Other |
|-------------|-------|
| Who / channel | Type — **1.5.1**; when — **1.5.2** |
| Route the *report* | Escalate a blocked *clock* — **1.5.2** |
| Not where the changeover log lives | **1.7** |

The task is a **route line**:

`type | recipients | leadership yes/no | channel | rejected channel`

| Expected (usually) | Lead (usually) |
|--------------------|----------------|
| Incident → IR + lead, ticket | Incident only in hunter Slack, no lead |
| RFI → CTI via form, no lead | RFI via personal SMS |
| Informational → distro + lead | Informational opened as a ticket to IR |

---

## 2. Detailed Walkthrough / Examples

### Example 1: Incident via Ticket (Expected)

**Type:** Incident (encoded PS + Run key).

**Route:** Recipients **SOC queue + IR**. Leadership **yes** (duty lead). Channel **ticket**.  
**Reject:** Personal email to the IR analyst only — not the approved case system.

### Example 2: RFI via SMS (Lead)

**Type:** RFI to CTI on the nightowl domain. Analyst texts a CTI friend.

**Correct route:** Recipients **CTI**. Leadership **no** (chart). Channel **ticket or RFI form**.  
**Reject:** Personal SMS — not an approved channel.  
**Lead:** Right team, wrong path.

### Example 3: Incident Missing Leadership (Lead)

**Type:** Incident. Analyst posts the write-up only in the hunter channel.

**Correct route:** **SOC queue + IR**, leadership **yes**, **ticket**.  
**Reject:** Hunter chat as the only path; leadership awareness **missing**.

---

## 3. Hands-On Exercise

**Objective:** Write a route line and reject the wrong channel.

**Use the classroom chart** unless the instructor overlays a site chart.

**Instructions:**

1. One sentence each for Examples 1–3: recipients + leadership + channel + rejected path.
2. For each item, write the **route line** (`type | recipients | leadership | channel | rejected`).

   - A. Incident for the 8080 `update.exe` FN; first IR handoff.
   - B. RFI to IT: “Is `10.10.8.90` the scanner?”
   - C. Informational FYI that the TN intranet PDF did not page.
   - D. Someone pastes the incident into a personal WhatsApp group “so leadership sees it faster.”

3. Do not rewrite the report type. Do not score the 30/60 clock. Do not write a 1.7 changeover.
4. If D is “right audience, wrong channel,” say so.

**Expected Outcome:**
- Three example summaries
- Four route lines
- No timeline math, no new type

---

## 4. Knowledge Check

1. What three things does the **notification chart** tell you?
2. When is **leadership awareness** required in the classroom chart?
3. Name one **approved** channel and one **not approved** channel.
4. Why is “I told a hunter in chat” not enough for an incident?
5. Where is the shift-change **record location** taught?

---

## 5. Summary

- Chart: who, leadership yes/no, approved channel.
- Route line + reject the wrong path.
- This closes unit **1.5**. Next unit: **1.7** Shift change.

---

## 6. References & Further Reading

- Related modules:
  - 1.5.1 – Report types
  - 1.5.2 – Reporting timelines (previous)
  - 1.7.1 – Shift changeover process (next)
- Local notification matrix (optional — substitutes the classroom chart)
