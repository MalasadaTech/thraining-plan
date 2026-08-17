# Module 4.2 – Making a detection sound and meeting shop requirements

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.2 B / C / C ; 4.2.1 3c / 4c / 4d ; 4.2.2 3c / 4c / 4c ; 4.2.3 3c / 4c / 4c  
- SOC: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- Hunter: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
- CTI: 4.2 A / A / B ; 4.2.1 1a / 1a / 2b ; 4.2.2 1a / 1a / 1a ; 4.2.3 1a / 1a / 2b  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say what **sound** means, and what you state before a rule goes live.
2. Mark shop requirements against a list you were **shown** — or say you do not have the list.
3. Name the four **close-the-loop** notes to the nominator.

**Mapped Proficiency Items:**
- K: 4.2 – Making a detection sound and meeting shop requirements
- T: 4.2.1 – Test a draft or change: what must fire and what must not
- T: 4.2.2 – Mark which shop requirements are met and which are still missing
- T: 4.2.3 – Write the close-the-loop note to the nominator

---

## 1. Key Concepts

**4.1** said DE owns new, change, retire, and deploy. This hour is what “good enough to ship” looks like. Not how to write the rule (**1.3**).

**Sound** means two things: it **fires** on the intended activity, and it does **not** fire on what it must not.

**Test before it goes live.** State what **must fire** and what **must not**. If you cannot name both, you are not ready to ship.

**Shop requirements** DE owns: required meta fields, naming, IDs, tags, logging. The *list* is local (**4.8**). You check the list you were **shown**. Mark met vs missing. If nobody showed you a list, say that. Do not invent fields.

**Close the loop** with the nominator (and SOC). The note is one of: **shipped**, **changed**, **sent back**, or **retired**.

**What good looks like:**

- Test: one line for must-fire, one line for must-not-fire.
- Shop list: met / missing against a list you were shown — or “I do not have the list yet.”
- Note to the nominator: shipped / changed / sent back / retired. Not a ticket name you made up.

---

## 2. Knowledge Check

1. A detection is sound when it does what two things?
2. You were not shown a shop list. Do you invent the fields?
3. Name the four close-the-loop notes.

---

## 3. Summary

Sound = fires on the intended activity and not on what it must not. Test those two before live. Check the list you were shown. Close the loop: shipped, changed, sent back, or retired.

**Next:** **4.3** Nominations from SOC, hunt, and CTI.

---

## 4. Related modules

- 4.1 – What DE owns
- 1.3 – Detection authoring (how a rule works)
- 4.3 – Nominations from SOC, hunt, and CTI
- 4.8 – Site-specific DE knowledge (the list)
