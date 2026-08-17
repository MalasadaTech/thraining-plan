# Module 0.8 – Environment / signal flow  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer  
**Estimated Delivery Time:** 20 minutes  
**Total Suggested Slides:** 7

---

### Slide 1 – Title Slide
**Title:** Module 0.8 – Environment / signal flow  
**Subtitle:** Obtain from your shop. Do not invent.  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Reminder hour. Questions you take to the site. No classroom network.

---

### Slide 2 – What this hour is
**Title:** What this hour is

Know where **your** site can see — and where it cannot.  
This course does not give you the answers.

**Speaker Notes:**  
Every desk uses the same host or log. A gap is not “nothing happened.”

---

### Slide 3 – Seven kinds
**Title:** Seven kinds of facts

Egress · Segments · Email  
Choke points · Third-party / federation  
Crown jewels · PCAP / sensors

**Speaker Notes:**  
These are questions. The shop supplies the answers. Do not invent names.

---

### Slide 4 – Tell two apart
**Title:** Tell two apart

Host talked to the internet → **egress**  
How a message arrived → **email**  
Could anything have recorded it? → **sensors**

**Speaker Notes:**  
Name the kind. Reject the neighbor. Do not name a firewall you were not shown.

---

### Slide 5 – Not this hour
**Title:** Not this hour

Not Zeek fields (**1.2**).  
Not host-observed network (**1.1.4**).  
Not a site card we made up.

**Speaker Notes:**  
If they start drawing Harbor or DYA gear, stop them.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Why must every role know where the site can see?  
2. Egress question vs email question?  
3. “Could a sensor have seen this?” — which kind, and why not Zeek?

**Speaker Notes:**  
Answers only in the instructor guide.

---

### Slide 7 – Next
**Title:** Next

**1.1.1** Endpoint activity (the map)

**Speaker Notes:**  
SOC starts. Those rows sit on a host that lives somewhere on the site they just learned to ask about.
