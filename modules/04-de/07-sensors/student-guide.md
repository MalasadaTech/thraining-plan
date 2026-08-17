# Module 4.7 – Sensor availability and performance

**Target Audience:** Detection Engineer (primary); SOC Analyst, Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- DE: 4.7 A / B / B ; 4.7.1 2b / 3c / 3c ; 4.7.2 2b / 3c / 3c  
- SOC: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- Hunter: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
- CTI: 4.7 A / A / A ; 4.7.1 1a / 1a / 1a ; 4.7.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  

---

## Learning Objectives

By the end of this module, you will be able to:

1. Say that DE sometimes checks whether **sensors** are up and seeing the right place — and that this is **not** a vendor-admin course.
2. Given “the rule never fired,” say whether you would check the **rule**, the **sensor**, or **both**, and reject treating a down sensor as proof the activity did not happen.

**Mapped Proficiency Items:**
- K: 4.7 – Sensor availability and performance
- T: 4.7.1 – Given “the rule never fired,” check the rule, the sensor, or both
- T: 4.7.2 – Reject treating a down sensor as proof the activity did not happen

---

## 1. Key Concepts

When a rule never fires, DE sometimes has to ask whether the **sensor** was even up and looking at the right place. This hour is that check.

**4.6** used “sensor gone” as a reason to retire. This hour is the check itself.

**Sometimes** DE watches whether sensors are up and seeing the right place. Examples: **MDE**, **Zeek**, **IDS**. You are not the vendor admin. This is not an architecture course.

A **dead** or **blind** sensor is **not** “no threat.” The activity may still have happened. You just could not see it.

**What good looks like:**

- Given: “the rule never fired,” and the sensor was up and seeing that host. Check the **rule**.
- Given: “the rule never fired,” and the sensor was down or not seeing that place. Check the **sensor**, or **both**.
- Given: the sensor was down all week, so “nothing happened.” **Reject.** A down sensor is not proof the activity did not happen.

Do not log into the vendor box. Do not size a sensor. Do not invent a ticket.

---

## 2. Knowledge Check

1. A down sensor means the activity did not happen. True or false?
2. Someone says “the rule never fired.” What two things might you check?
3. Name three kinds of sensor this hour uses as examples.

---

## 3. Summary

Sometimes DE checks whether sensors are up and seeing the right place. A dead sensor is not “no threat.” Check the rule, the sensor, or both. This is not vendor admin.

**Next:** **4.8** Site-specific DE knowledge.

---

## 4. Related modules

- 4.6 – Detection lifecycle
- 4.8 – Site-specific DE knowledge
- 1.2 – Zeek (how those logs work)
- 1.1 – Endpoint logs (MDE as a source)
