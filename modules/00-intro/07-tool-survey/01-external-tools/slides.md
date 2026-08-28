# Module 0.7 – External tools  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Estimated Delivery Time:** 20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 0.7 – External tools  
**Subtitle:** VirusTotal, AnyRun, Silent Push, URLScan  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This lesson is the shared survey of four public tools. It names purpose and when to pick. It is not a live account and not how to click the product.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

You will get a **hash**, a **file**, a **domain**, or a **live URL**.

Four public tools each answer a different question.

Pick the first tool that matches the need. Say why the neighbor is the wrong first pick.

**Speaker Notes:**  
This slide is the student intro. They pick so they do not detonate a file when they only needed history, or screenshot a page when they needed a hash reputation. Do not open a vendor tab.

---

### Slide 3 – Purpose, strength, weakness
**Title:** Purpose, strength, weakness

**VirusTotal** — look-up. Fast reputation. Not passive DNS. Not a full sandbox.  
**AnyRun** — detonate a sample. This-run behavior. Needs a file.  
**Silent Push** — history / cluster. Not a detonation. Not a screenshot.  
**URLScan** — this page load. Not passive DNS. Not file behavior.

**Speaker Notes:**  
One strength and one weakness each. **Passive DNS** (also called PDNS) is historical resolutions — Silent Push, not URLScan. Do not memorize vendor menus.

---

### Slide 4 – When to pick
**Title:** When to pick

Hash or file reputation → **VirusTotal**  
Binary and behavior → **AnyRun**  
Domain or IP history → **Silent Push**  
Live URL / page now → **URLScan**  
Seen internally? → **not these** (internal TIP, later)

**Speaker Notes:**  
Match the need. Reject the neighbor. “Have we seen this internally?” is the TIP in a later lesson, not one of these four.

---

### Slide 5 – A finished select
**Title:** A finished select

Need: file hash, vendor reputation.  
Pick **VirusTotal**.  
Not AnyRun — no sample to detonate.  
Not Silent Push — not a history question.

**Speaker Notes:**  
That is the task. Show this given before the knowledge check. No hop. No Relations graph. No live query.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Give one purpose and one weakness of Silent Push.  
2. When do you pick URLScan instead of Silent Push?  
3. You have a hash and need reputation. Which tool, and why not AnyRun?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Four tools. Match the need. Reject the neighbor.  
Do not open the sandbox when the question is history.  
Do not treat a page scan as passive DNS.

**Speaker Notes:**  
Environment / signal flow is next. That lesson is kinds of facts from the shop, not another tool survey.

---

### Slide 8 – Next
**Title:** Next

**0.8** Environment / signal flow

**Speaker Notes:**  
0.8 is where visibility comes from. Do not invent a site card. Do not start TIP navigation or platform depth.
