# Module 0.7 – External tools  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Estimated Delivery Time:** 20 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 0.7 – External tools  
**Subtitle:** VirusTotal, AnyRun, Silent Push, URLScan  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Survey only. Purpose and when to pick. Not a live account.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Pick the first public tool that matches the need.  
Say why the neighbor is the wrong first tool.

**Speaker Notes:**  
They do this so they do not detonate a file when they only needed history.

---

### Slide 3 – Four tools
**Title:** Purpose, strength, weakness

**VirusTotal** — look-up. Fast reputation. Not PDNS. Not a full sandbox.  
**AnyRun** — detonate a sample. This-run behavior. Needs a file.  
**Silent Push** — history / cluster. Not a detonation. Not a screenshot.  
**URLScan** — this page load. Not PDNS. Not file behavior.

**Speaker Notes:**  
One strength and one weakness each. Do not memorize vendor menus.

---

### Slide 4 – When to pick
**Title:** When to pick

Hash / file reputation → **VirusTotal**  
Binary + behavior → **AnyRun**  
Domain / IP history → **Silent Push**  
Live URL / page now → **URLScan**  
Seen internally? → **not these** (TIP, later)

**Speaker Notes:**  
Match the need. Reject the neighbor.

---

### Slide 5 – A finished select
**Title:** A finished select

Need: file hash, vendor reputation.  
Pick **VirusTotal**.  
Not AnyRun — no sample to detonate.  
Not Silent Push — not a history question.

**Speaker Notes:**  
That is the task. No hop. No Relations graph.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. One purpose and one weakness of Silent Push?  
2. When URLScan instead of Silent Push?  
3. Hash + reputation: which tool, and why not AnyRun?

**Speaker Notes:**  
Answers only in the instructor guide.

---

### Slide 7 – Next
**Title:** Next

**0.8** Environment / signal flow

**Speaker Notes:**  
Where visibility comes from. Not a site-card invention hour.
