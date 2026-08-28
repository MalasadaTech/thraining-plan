# Instructor Guide – Module 0.8 – Environment / signal flow

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Proficiency Focus:**  
- SOC: 0.8 A / B / C ; 0.8.1 2b / 3c / 4c  
- Hunter: 0.8 B / C / C ; 0.8.1 2b / 3c / 4c  
- CTI: 0.8 A / B / B ; 0.8.1 1a / 2b / 3c  
- DE: 0.8 A / B / B ; 0.8.1 2b / 3c / 4c  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the seven kinds of environment facts every role must obtain from their shop. Tell two kinds apart. Do not invent the site.

**Context (plain language):**

- What this lesson is for: An alert, a hunt, an intel note, and a detection all look at the same host or log. Before you treat a gap as “nothing happened,” you have to know where your site can see and where it cannot. This lesson names the kinds of facts to obtain from your shop. It does not publish the answers.
- How it hooks to the lesson before: 0.7 named outside tools. Those tools do not tell you what this network can see.
- How it hooks to the lesson after: 1.1.1 is endpoint activity. Those host logs sit on a device that lives somewhere on a site they just learned to ask about.
- Why we are doing it this way: these are questions you take to your shop. A filled-in picture of this site’s network (a site card) is not something this course invents.
- What we are *not* doing in this lesson: Inventing a site card, spans, ticket names, or DYA / Harbor architecture. Zeek field reading (1.2). Host-observed network (1.1.4). Sensor health (4.7). No lab.
- Extra step: none.

Use the same names as the student guide: **path to the internet / egress**, **key network segments and data flow**, **email flow**, **edge firewall / choke points**, **trusted third-party / federation**, **crown jewel / critical assets**, **PCAP collection points / sensors**, **kind of fact**, and **your shop**. **Environment / signal flow** means the site’s infrastructure and how traffic and logs move. A **site card** is a filled-in picture of this site’s network (names, spans, sensor locations). If the shop has already shown a real card, they may use *that* card. Do not replace it with one from this lesson.

**Key Teaching Points:**
- Seven kinds of facts. Questions, not answers this course supplies.
- Tell two kinds apart. Reject the neighbor.
- A gap is a fact. “No sensor there” is the sensor kind.

**Common Student Challenges:**
- Invent a site card. Why: they want answers on the slide. Example: naming a firewall, span, or VLAN this course never showed.
- Call an egress question email. Why: both are off the host. Example: a click-to-internet path written as mail flow.
- Treat “could a sensor have seen this” as a Zeek field. Why: both involve network telemetry. Example: asking for conn fields when the question is whether a sensor sits on that path.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 0.8 – Environment / signal flow
- T: 0.8.1 – Identify which kind of fact applies and why it is not the adjacent kind

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | Obtain from your shop. Do not invent. |
| Key Concepts            | 10 min    | Seven kinds; three givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: every desk looks at the same host or log, and a gap is not “nothing happened.”
- Write the seven kinds as questions. Stop. Do not fill in firewall names, spans, VLANs, or ticket names.
- Walk the three “given” lines from the student guide. The product is the kind plus why the neighbor is wrong, not a picture of the site.
- If they start drawing DYA / Harbor gear: stop. Those names are course fiction, not a site card this lesson supplies.
- If they start reading Zeek fields: that is 1.2. Today is whether a sensor sits on the path.
- If they describe the host logging a talk: that is 1.1.4. Today is where a collector sits, not what the endpoint logged.
- If no one has shown them the answer: “I do not have it yet” is a pass. Inventing the network is a fail.

---

## Knowledge Check – Answer Key

1. **Why must every role know where the site can see, and where it cannot?**  
   **Answer:** The same host or log is used by SOC, hunt, intel, and DE. If you do not know visibility (and gaps), you will treat a blind spot as “nothing happened.”  
   **Explanation:** That is why this lesson exists. The answers come from the shop, not from this course.

2. **A user clicked a link and the host talked to the internet. You ask how that traffic left. Which kind, and why is it not email?**  
   **Answer:** **Path to the internet / egress.** Email is how mail enters and leaves (the mail path). Both can be “off the host,” but they are different questions.  
   **Explanation:** Outline a vs c. Sensors would be the kind only if the question was whether anything could have recorded that path.

3. **Could a sensor have recorded that talk — which kind, and why not Zeek?**  
   **Answer:** **PCAP collection points / sensors** — where coverage exists and where it does not. Zeek (**1.2**) is how you read a log you already have, not whether a sensor was there.  
   **Explanation:** Outline g / task. Host-observed network (**1.1.4**) is the host logging the talk, not where a collector sits.

---

## Additional Instructor Resources

- Next: 1.1.1 Endpoint activity (the map)
