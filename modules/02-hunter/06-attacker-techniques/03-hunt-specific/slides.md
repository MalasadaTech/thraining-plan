# Module 2.6.3 – Hunt for a Specific Technique  
## Slide Deck Content

**Target Audience:** Threat Hunter (primary), SOC Analyst and CTI Analyst (secondary)  
**Estimated Delivery Time:** 60–75 minutes  
**Total Suggested Slides:** 17

---

### Slide 1 – Title Slide
**Title:** Module 2.6.3 – Hunt One Named Technique  
**Subtitle:** Threat Hunter Training (SOC / CTI secondary)  
**Footer:** SOC / Hunter / CTI Training Program

**Speaker Notes:**  
Recognition is done. This hour hunts one method.

---

### Slide 2 – Learning Objectives
**Title:** Learning Objectives

1. Named technique → scoped hunt
2. Cite a unique pattern
3. Reject tactic sweeps and wrong class

**Mapped Items:**  
T: 2.6.3

**Speaker Notes:**  
Hunter 3c / 4c / 4d. SOC/CTI 1a / 1a / 2b.

---

### Slide 3 – Agenda
**Title:** Agenda

- Hunt line
- Three examples
- Exercise
- Knowledge check

**Speaker Notes:**  
2.7 is next.

---

### Slide 4 – Not This Lesson
**Title:** Not This Hour

Recognize the row (**2.6.1** / **2.6.2**)  
All four hunt types (**2.2.1**)  
Remap ATT&CK (**2.5**)  
Local ticket (**2.7**)

**Key Point:** One named method.

**Speaker Notes:**  
Fence.

---

### Slide 5 – Named, Not a Class
**Title:** Named Technique

HKCU Run `Updater`  
User → SYSTEM token  
Not “persistence”

**Speaker Notes:**  
Class is the column, not the hunt.

---

### Slide 6 – Hunt Line
**Title:** Hunt Line

named | class | unique pattern | scope | query idea | why not the tactic

**Speaker Notes:**  
Write it on the board.

---

### Slide 7 – Unique Pattern (4d)
**Title:** What Makes It Testable

`Updater` + `%TEMP%\update.exe`  
Not “any Run key”

**Speaker Notes:**  
Hunter 4d lives here.

---

### Slide 8 – Scope
**Title:** Where You Will Look

Hosts / time / telemetry  
Then stop

**Speaker Notes:**  
Unbounded host list fails.

---

### Slide 9 – Classroom Seeds
**Title:** Already Recognized

Run `Updater` → persist  
SYSTEM task → persist  
`helpdesk.exe` → SYSTEM → privesc

**Speaker Notes:**  
Do not re-litigate.

---

### Slide 10 – Example 1
**Title:** Expected — Run-Key Hunt

Named Run `Updater`. Scoped. Queryable.

**Key Point:** This is the product shape.

**Speaker Notes:**  
Students write the line first.

---

### Slide 11 – Example 2
**Title:** Lead — Hunt Persistence

Tactic sweep. No pattern.

**Key Point:** Fail.

**Speaker Notes:**  
Ask what they would query.

---

### Slide 12 – Example 3
**Title:** Lead — Wrong Class

SYSTEM task is persist, not privesc.

**Key Point:** Fail the class swap.

**Speaker Notes:**  
Hold the 2.6.1 leftover.

---

### Slide 13 – Common Mistakes
**Title:** Common Mistakes

- Hunt the tactic  
- Hunt the wrong class  
- Rewrite 2.2.2  
- Invent a 2.7 ticket  

**Speaker Notes:**  
Park all four.

---

### Slide 14 – Hands-On Exercise
**Title:** Exercise

Hunt lines A–E. Product is A or C.

**Speaker Notes:**  
Fail B, D, E.

---

### Slide 15 – Knowledge Check
**Title:** Knowledge Check

1. What must be named?  
2. Hunt line besides the name?  
3. Why not “hunt persistence”?  
4. Why not privesc on the task?  
5. Where is the local process?

**Speaker Notes:**  
Answers in the instructor guide.

---

### Slide 16 – Summary
**Title:** Summary

One method. Unique pattern. Right class.

**Coming next:** Module 2.7.1 – Hunt control (local)

**Speaker Notes:**  
Processes vary by site.

---

### Slide 17 – Quick Reference (Optional)
**Title:** Hunt Line

`named | persist/privesc | pattern | scope | query | not the tactic`

**Speaker Notes:**  
Leave up during the exercise.
