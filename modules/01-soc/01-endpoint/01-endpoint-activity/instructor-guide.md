# Instructor Guide – Module 1.1.1 – Endpoint activity (the map)

**Target Audience:** SOC Analyst (primary); Threat Hunter, CTI Analyst (secondary)  
**Proficiency Focus:**  
- SOC: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 2b / 2b  
- Hunter: 1.1.1.1 A / B / B ; 1.1.1.2 1a / 1a / 2b  
- CTI: 1.1.1.1 A / A / A ; 1.1.1.2 1a / 1a / 1a  
**Estimated Time:** 15–20 minutes  
**Delivery Method:** Instructor-led

---

## Module Overview for Instructors

**Purpose of this module:**  
Name the five kinds of host activity so the next lessons can stay on one kind each.

**Context (plain language):**

- What this lesson is for: An alert usually names a host. That host generated a log. Before you describe what happened, you have to know what kind of activity the log is about. This lesson names those kinds.
- How it hooks to the lesson before: the shared intro block (course layout, what a SOC is, jobs, frameworks, tools, environment). This is the start of the SOC analyst track.
- How it hooks to the lesson after: 1.1.2 is process activity — who ran what.
- Why we are doing it this way: name process, file, registry, host-network, and image/driver load before anyone reads a single event.
- What we are *not* doing in this lesson: process fields, Sysmon install, Zeek, the course fiction plot (DYA / PRD), no lab.
- Extra step: none.

Use the same names as the student guide: **log**, **event**, **process**, **file**, **registry**, **host-network**, and **image/driver load**. **Row** is the SIEM-table gloss from the student intro, not the headline word. **Host-network** means the endpoint logged a talk, not a Zeek protocol lesson.

**Key Teaching Points:**
- Five kinds of host activity. This lesson is the overview.
- Sysmon and MDE record the same activities with different field names.
- Name the kind. Do not describe the event yet.

**Required Materials:**
- Student Guide
- Slide Deck

---

## Learning Objectives

Same as the student guide.

**Mapped Proficiency Items:**
- K: 1.1.1.1 – Endpoint activity (the map)
- T: 1.1.1.2 – Given a one-line description, name the activity type

---

## Suggested Timing

Keep the **intro** (Context + what this lesson is). Drop any row you are not teaching.

| Section                 | Time      | Notes |
|-------------------------|-----------|-------|
| Introduction (required) | 3 min     | After the shared intro block |
| Key Concepts            | 10 min    | Five kinds; three givens |
| Knowledge Check         | 4 min     | Three questions |
| Summary                 | 2 min     | |
| **Total**               | **~19 min** | |

---

## Detailed Teaching Notes

### 1. Key Concepts

**Talking Points:**
- Open with the job: an alert names a host, that host generated a log, and you have to know the kind of activity before you describe it.
- Write the five kinds. Stop there. Do not add fields or Event IDs.
- Walk the three “given” lines from the student guide. The product is the kind, not a story of the incident.
- If they start listing Event IDs: that is 1.1.2. Today is only the kind of activity.
- If they say host-network is Zeek: the host logged the talk. Zeek is 1.2.
- If they start the DYA / PRD plot: that fiction is from the intro. It is not this lesson.

---

## Knowledge Check – Answer Key

1. **Sysmon and MDE are two different stories. True or false?**  
   **Answer:** False. Two tools, same five kinds of activity, different field names.  
   **Explanation:** The course uses both as examples of the same host activity, not as two separate facts.

2. **“A program started on the host.” Which type?**  
   **Answer:** Process.  
   **Explanation:** A program ran. That is process activity, not file or network.

3. **“This host connected to an IP and port.” Process or host-network?**  
   **Answer:** Host-network.  
   **Explanation:** A process started the connection, but the log that recorded the talk is host-network. Process would be “a program started,” not “this host connected.”

---

## Additional Instructor Resources

- Next: 1.1.2 Process activity
