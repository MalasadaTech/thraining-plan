# Module 2.1.2 – Intelligence lifecycle  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.1.2 – Intelligence lifecycle  
**Subtitle:** How a question becomes a usable answer  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Connect this lesson to 2.1.1. The previous lesson examined what an item contains. This lesson examines the work that moves a question toward an answer and then uses feedback to continue the process.

---

### Slide 2 – What the lifecycle helps you see
**Title:** What kind of work is happening now?

The intelligence lifecycle organizes the work required to move from a **question** to a **usable answer**.

It helps an analyst recognize:
- what the current activity is trying to accomplish;
- what work should happen next; and
- when new evidence or feedback requires a return to an earlier stage.

**Speaker Notes:**  
Frame the lifecycle as a practical way to understand purpose. One analyst, one team, or one platform may perform work from several stages, so the stage is not determined by an organizational label.

---

### Slide 3 – Six stages
**Title:** Six stages, six purposes

| Stage | Purpose |
|---|---|
| **Planning and Direction** | Define the question and what is needed to answer it. |
| **Collection** | Gather material relevant to the question. |
| **Processing and Exploitation** | Prepare collected material for analytical use. |
| **Analysis and Production** | Evaluate the information and develop the answer. |
| **Dissemination** | Deliver the intelligence to the people who need it. |
| **Evaluation and Feedback** | Determine whether the need was met and what comes next. |

**Speaker Notes:**  
Give one plain-language example for each stage. Explain that exploitation here means making collected material usable—for example, extracting, normalizing, translating, or organizing it—not exploiting a computer system.

---

### Slide 4 – Connect it to data, information, and intelligence
**Title:** The lifecycle organizes the work around the analysis

**Collection** often provides recorded observations.  
**Processing and Exploitation** makes those observations easier to understand and compare.  
**Analysis and Production** evaluates the available information against the question and develops an intelligence assessment.

**Planning**, **Dissemination**, and **Evaluation** organize the work before and after that analytical development.

**Speaker Notes:**  
Use this slide to connect 2.1.1 and 2.1.2 without turning the relationship into a rigid equation. Real work can overlap stages, and a newly processed record can immediately reveal another collection need.

---

### Slide 5 – Start with the A12 question
**Title:** Planning gives the work a purpose

SOC asks CTI:

**What role did the update domain play in the activity on WS-JLEE?**

**Planning and Direction** clarifies the question and identifies what evidence could help answer it.

**Collection** obtains the relevant material, such as HTTP, DNS, and incident records from the A12 time frame.

**Speaker Notes:**  
Ask learners what evidence they would want before showing examples. The goal is to make the transition from a question to a collection need visible.

---

### Slide 6 – Prepare, then interpret
**Title:** Processing prepares the evidence; analysis explains what it means

**Processing and Exploitation**  
Extract and organize the domain, IP address, timestamps, request path, source host, and other relevant fields so the activity can be compared.

**Analysis and Production**  
Evaluate those observations against the question. In A12, the request for `/update.exe` during suspicious activity supports a likely attempted-delivery role, while successful download and execution remain unresolved.

**Speaker Notes:**  
This is the key distinction for many learners. Preparing evidence for use is different from interpreting its significance. Reuse the uncertainty taught in 2.1.1 so the lifecycle feels connected to the previous lesson.

---

### Slide 7 – Delivery creates feedback
**Title:** Dissemination is not the end of the process

**Dissemination** delivers the assessment and its limits to SOC in a usable form and channel.

SOC may then ask:

**Did the requested file actually execute on WS-JLEE?**

That is **Evaluation and Feedback** creating a new or refined intelligence need.

The lifecycle begins another pass as needed.

**Speaker Notes:**  
Explain that feedback is operationally useful information about whether the answer was sufficient. It may close the question, refine it, or open the next one.

---

### Slide 8 – Why the lifecycle loops
**Title:** Analysis can send you back for more evidence

Suppose analysis shows an HTTP request for `/update.exe`, but the available records cannot establish whether the transfer completed.

The analyst now knows **what is missing**.

That gap can lead back to **Planning and Direction** and **Collection** to identify and obtain evidence that could answer it.

Returning to an earlier stage is normal analytical work.

**Speaker Notes:**  
Emphasize that iteration is not failure. Analysis often makes collection more focused because it reveals which missing evidence actually matters to the question.

---

### Slide 9 – Knowledge Check and Summary
**Title:** Recognize the purpose of the work

1. You are extracting fields from collected A12 HTTP and DNS records into a consistent format. Which stage, and why?  
2. Analysis reveals that successful download cannot be established. What should happen next?  
3. SOC receives the assessment and asks whether the file executed. Which stage produced that new need?

**Remember:** classify the stage by **what the activity is trying to accomplish**, not by the tool or folder where it happens.


**Speaker Notes:**  
Use the answer key in the instructor guide. Listen for the reasoning behind each classification. Close by tracing the A12 question from planning through feedback and reinforcing that the lifecycle is iterative.

**Next:** [2.1.3 – Intelligence Types](../03-intelligence-types/student-guide.md).
