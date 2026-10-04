# Module 2.5.2 – Hashing and Similarity Concepts  
## Slide Deck Content

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Estimated Delivery Time:** 20–25 minutes  
**Total Suggested Slides:** 9

---

### Slide 1 – Title Slide
**Title:** Module 2.5.2 – Hashing and Similarity Concepts  
**Subtitle:** Find candidates for deeper file comparison  
**Footer:** SOC / Hunter / CTI / DE Training Program

**Speaker Notes:**  
Frame the lesson around two questions: exact identity versus useful similarity. The techniques in this lesson help analysts find samples worth comparing; they do not replace deeper analysis.

---

### Slide 2 – Identity and similarity answer different questions
**Title:** Same file, or similar file?

**SHA256:** Are these files byte-for-byte the same?

**Similarity techniques:** Are these files similar enough that I should compare them more closely?

A different SHA256 does not end the investigation.

**Speaker Notes:**  
Connect to the earlier identity-hash lesson without reteaching it. The purpose here is to find candidates after exact identity no longer matches.

---

### Slide 3 – imphash
**Title:** A pivot on PE import structure

**imphash** is derived from the ordered imports of a Windows PE file.

A matching imphash means the files share the import structure represented by the algorithm.

That can suggest:
- similar source/build process;
- a shared builder; or
- a common packer.

It does **not** prove malware family or actor.

**Speaker Notes:**  
Mandiant describes imphash as a useful triage and discovery technique but explicitly cautions against treating it as a single point of attribution. Reference: [Mandiant — Tracking Malware with Import Hashing](https://cloud.google.com/blog/topics/threat-intelligence/tracking-malware-import-hashing).

---

### Slide 4 – ssdeep
**Title:** Higher score = more similar

**ssdeep** compares fuzzy hashes and returns a **0–100 match score**.

Higher = closer under the algorithm.

Classroom exercise: **50 or higher** → select for further comparison.

The score is not a probability, and a match does not prove relationship.

**Speaker Notes:**  
Use the classroom cutoff only as a decision aid for the exercise. Explain that real thresholds depend on the corpus and use case. Reference: [ssdeep — Getting Started](https://ssdeep-project.github.io/ssdeep/usage.html).

---

### Slide 5 – TLSH
**Title:** Lower difference = more similar

**TLSH** compares locality-sensitive hashes using a **difference score**.

Lower = closer.  
0 = extremely close / identical input under the comparison.

Classroom exercise: **30 or lower** → select for further comparison.

Do not read TLSH as a percentage.

**Speaker Notes:**  
Contrast the direction with ssdeep. This is the common learner error: ssdeep high is close; TLSH low is close. Reference: [Trend Micro TLSH](https://github.com/trendmicro/tlsh).

---

### Slide 6 – Similarity is a lead
**Title:** Several signals strengthen the pivot

New file versus `update.exe`:

- different SHA256;
- same imphash;
- ssdeep **68**;
- TLSH **24**.

Reasonable conclusion:

**The new file is a strong candidate for deeper comparison.**

Next compare behavior, strings, configuration, resources, infrastructure, or other independent features.

**Speaker Notes:**  
Do not allow “same family” as the automatic conclusion. Ask what other evidence would support or weaken that relationship.

---

### Slide 7 – Code-signing
**Title:** Signing adds identity and integrity evidence

Inspect:
- signer / subject;
- issuer;
- validity dates;
- signature status.

A valid signature can identify the publisher represented by the certificate and help verify signed-code integrity.

**Signed ≠ benign.**  
**Unsigned ≠ malicious.**

**Speaker Notes:**  
Also distinguish code-signing from a TLS certificate. A stolen, abused, revoked, or expired certificate changes how the evidence should be interpreted. Reference: [Microsoft — Authenticode Digital Signatures](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode).

---

### Slide 8 – Keep the evidence boundary visible
**Title:** Say exactly what the result supports

Same imphash → shared import structure.  
ssdeep 72 → strong fuzzy similarity.  
TLSH 22 → small difference.  
Signed → certificate/signature evidence.  
Unsigned → no usable code-signing signature.

Each is useful. None independently proves actor or malware family.

**Speaker Notes:**  
This slide connects the lesson back to the analytic discipline developed in 2.1 and 2.2.

---

### Slide 9 – Knowledge Check and Summary
**Title:** Use similarity without overclaiming

1. Same imphash, different SHA256: what does that support and what does it not prove?  
2. ssdeep 72 and TLSH 22: how do the score directions differ, and what comes next?  
3. `update.exe` is unsigned: what did you learn, and what would go beyond the evidence?

**Remember:** similarity techniques identify candidates; analysis establishes relationships.


**Speaker Notes:**  
Use the instructor answer key. Listen for correct score direction and explicit evidence boundaries.

**Next:** [2.5.3 – RDAP and WHOIS Concepts](../03-rdap-whois/student-guide.md).
