# Module 0.8 – Environment / signal flow  
## Slide Deck Content

**Target Audience:** SOC Analyst, Threat Hunter, CTI Analyst, Detection Engineer (shared intro)  
**Estimated Delivery Time:** 15–20 minutes  
**Total Suggested Slides:** 8

---

### Slide 1 – Title Slide
**Title:** Module 0.8 – Environment / signal flow  
**Subtitle:** Obtain from your shop. Do not invent.  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
This is the last shared intro lesson before SOC. It names the kinds of site facts to obtain. It does not publish a classroom network.

---

### Slide 2 – Why this lesson exists
**Title:** Why this lesson exists

An alert, a hunt, an intel note, and a detection all look at the same host or log.

Before you treat a gap as “nothing happened,” know **where your site can see** and where it cannot.

This course does not give you those answers. You get them from **your shop**.

**Speaker Notes:**  
This slide is the student intro. Name the kinds of questions before anyone draws a network. Do not fill in firewall names or spans today.

---

### Slide 3 – Seven kinds of facts
**Title:** Seven kinds of facts

**Path to the internet / egress** — how traffic leaves.  
**Key network segments and data flow** — main pieces, how data moves.  
**Email flow** — how mail enters and leaves.  
**Edge firewall / choke points** — where the shop can block or see at the edge.  
**Trusted third-party / federation** — who else is trusted onto the network.  
**Crown jewels** — which assets are critical. Do not guess them.  
**PCAP / sensors** — where a sensor sits, and where it does not.

**Speaker Notes:**  
These are questions. The shop supplies the answers. A gap is still a fact. Stop if they start naming gear this course never showed.

---

### Slide 4 – Tell two kinds apart
**Title:** Tell two kinds apart

Host talked to the internet — how did it leave? → **egress**  
How a message arrived → **email**  
Could anything have recorded it? → **PCAP / sensors**

Name the kind. Reject the neighbor. Do not name a firewall you were not shown.

**Speaker Notes:**  
That is the task. Walk the three givens in the student guide if you need them. “I do not have it yet” is a pass. Inventing the network is a fail.

---

### Slide 5 – Obtain. Do not invent.
**Title:** Obtain. Do not invent.

Not Zeek fields (**1.2**).  
Not host-observed network (**1.1.4**).  
Not a network this course made up.

**Speaker Notes:**  
PCAP / sensors is where a collector sits. Zeek is how you read a log you already have. Host-observed network is the host logging a talk. If they start drawing DYA or Harbor gear, stop them.

---

### Slide 6 – Knowledge Check
**Title:** Knowledge Check

1. Why must every role know where the site can see, and where it cannot?  
2. A user clicked a link and the host talked to the internet. You ask how that traffic left. Which kind, and why is it not email?  
3. “Could a sensor have recorded this?” — which kind, and why not Zeek?

**Speaker Notes:**  
Answers are only in the instructor guide. Three questions for the whole lesson. Do not add a fourth.

---

### Slide 7 – Summary
**Title:** Summary

Seven kinds of questions.  
Obtain the answers from your shop.  
Name the kind. Reject the neighbor.  
A gap is a fact. Do not invent the network.

**Speaker Notes:**  
Same three teaching points. Endpoint activity is next. Stay off host logs until then.

---

### Slide 8 – Next
**Title:** Next

**1.1.1** Endpoint activity (the map)

**Speaker Notes:**  
1.1.1 names the five kinds of host activity. Those logs sit on a device that lives somewhere on a site they just learned to ask about.
