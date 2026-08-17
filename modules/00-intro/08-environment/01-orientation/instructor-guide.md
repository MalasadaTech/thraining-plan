# Instructor Guide – Module 0.8 – Environment / signal flow

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Proficiency Focus:**  
- SOC: 0.8 A / B / C ; 0.8.1 2b / 3c / 4c  
- Hunter: 0.8 B / C / C ; 0.8.1 2b / 3c / 4c  
- CTI: 0.8 A / B / B ; 0.8.1 1a / 2b / 3c  
- DE: 0.8 A / B / B ; 0.8.1 2b / 3c / 4c  
**Estimated Time:** 20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Context (plain language):**

- What this hour is for: Remind every role to learn their own site’s infrastructure and signal flow — where visibility comes from, and where it does not.
- How it hooks to the hour before: they picked an outside tool. Now they must know what *their* network can actually see.
- How it hooks to the hour after: SOC starts — endpoint rows. Those rows sit on a host that lives somewhere on the site they just learned to ask about.
- Why we are doing it this way: a reminder, not a fake architecture. The answers come from the shop, not from this course.
- What we are *not* doing this hour: Inventing a site card, spans, ticket names, or DYA / Harbor gear. Zeek fields. Host-observed network. A lab.

**Key Teaching Points:**
- Seven kinds of facts. Questions, not answers we supply.
- Tell two kinds apart. Reject the neighbor.
- A gap is a fact. “No sensor there” is the sensor kind.

**Required Materials:**
- Student Guide
- Slide Deck

If the shop has already shown a real card, they may use *that* card. Do not replace it with one from this lesson.

---

## Learning Objectives

Same as the student guide.

**Mapped Items:**  
- K: 0.8 – Environment / signal flow  
  SOC A / B / C · Hunter B / C / C · CTI A / B / B · DE A / B / B  
- T: 0.8.1 – Identify which kind of fact applies and why it is not the adjacent kind  
  SOC 2b / 3c / 4c · Hunter 2b / 3c / 4c · CTI 1a / 2b / 3c · DE 2b / 3c / 4c

---

## Suggested Timing

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Obtain, do not invent |
| Key Concepts            | 11 min    | Seven kinds + one tell-apart |
| Knowledge Check         | 5 min     | Three questions |
| Summary                 | 1 min     | |
| **Total**               | **~20 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

Walk the seven questions. Stop anyone who starts drawing Harbor / DYA gear. For the select: “host talked to the internet” is egress, not email, not sensors, unless the question is mail path or coverage. Park Zeek fields for 1.2.

---

## Knowledge Check – Answer Key

1. **Why must every role know where the site can see?**  
   **Answer:** The same host or log is used by SOC, hunt, intel, and DE. If you do not know visibility (and gaps), you will treat a blind spot as “nothing happened.”  
   **Explanation:** Intro / why.

2. **Egress vs email?**  
   **Answer:** Egress is how traffic leaves for the internet. Email is how mail enters and leaves (the mail path). Both can be “off box,” but they are different questions.  
   **Explanation:** Outline a vs c.

3. **Could a sensor have seen a host talk — which kind, why not Zeek?**  
   **Answer:** **PCAP / sensors** — where coverage exists and where it does not. Zeek (**1.2**) is how you read a log you already have, not whether a sensor was there.  
   **Explanation:** Outline g / task.

---

## Additional Instructor Resources

- Next: 1.1.1 Endpoint activity (the map)
