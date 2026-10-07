# Module 2.5.2 – Hashing and Similarity Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.2 B / C / C ; 2.5.2.1 3c / 4c / 4d ; 2.5.2.2 3c / 4c / 4c  
- Hunter: 2.5.2 A / B / B ; 2.5.2.1 1a / 2b / 3c ; 2.5.2.2 1a / 2b / 3c  
- SOC: 2.5.2 A / A / B ; 2.5.2.1 1a / 1a / 2b ; 2.5.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Explain what **imphash**, **ssdeep**, and **TLSH** measure and use similarity results to identify samples that merit further comparison.
2. Extract and interpret **code-signing** information from a file without treating the signature as proof of trust or attribution.

**Mapped Proficiency Items:**
- K: 2.5.2 – Hashing and similarity concepts
- T: 2.5.2.1 – Use file similarity hashes to identify related samples
- T: 2.5.2.2 – Extract and interpret certificate / code-signing information from a file

## 1. Key Concepts

A cryptographic hash such as **SHA256** is useful when you need to know whether two files are exactly the same. Change the file and the SHA256 changes.

Threat intelligence often asks a different question: **is this new sample similar enough to another sample that it deserves comparison?**

Similarity techniques help analysts find candidates for that next step. They do not, by themselves, prove that two files belong to the same malware family, came from the same actor, or perform the same behavior.

This lesson uses three similarity techniques plus code-signing information:

| Technique | What it represents | How to interpret it |
|---|---|---|
| **imphash** | A hash derived from the ordered imports of a Windows PE file. | The same value means the files have the same normalized import structure under the algorithm. That can be a useful pivot, but it is not proof of common authorship or family. |
| **ssdeep** | A context-triggered piecewise or “fuzzy” hash based on file content. | Comparison produces a score from 0–100. Higher scores indicate greater similarity, but the score is not a percentage probability and does not prove relationship. |
| **TLSH** | A locality-sensitive hash that summarizes byte-level characteristics of sufficiently complex input. | Comparison produces a difference score. Lower values indicate greater similarity; 0 indicates extremely close or identical input under the comparison. |
| **Code-signing** | Digital-signature and certificate information attached to the file. | Identifies the signing publisher/certificate identity and helps verify file integrity. It does not prove the software is benign or that the named signer authored the malicious activity. |

### imphash: a structural pivot

Windows PE files record imported libraries and functions. **imphash** derives a value from that ordered import information.

If two files have the same imphash, they share the import structure represented by the algorithm. That can be useful for finding samples that may have been built from similar source, a common builder, or a common packing process.

The important word is **may**. Mandiant's original description of imphash explicitly notes that matching values are useful for triage and discovery but should not be treated as a single point of attribution. Simple utilities, common packers, or shared builders can produce the same value across otherwise unrelated activity.

A matching imphash is therefore a **lead for comparison**, not a finished family judgment.

### ssdeep: higher means more similar

**ssdeep** compares fuzzy signatures and returns a match score from 0 to 100. A higher score means the files share more matching structure according to the algorithm.

For classroom exercises, this course may use **50 or higher** as a simple threshold for selecting samples to examine further. That number is a teaching convenience, not a universal operational cutoff. The official ssdeep guidance warns that a match does not itself establish that two files are related; analysts should inspect the matching files and context.

Think of the result as:

> “These samples are similar enough to deserve comparison.”

—not—

> “These samples are definitely the same malware family.”

### TLSH: lower means more similar

**TLSH** works in the opposite direction. Its comparison output is a **difference score**: lower values indicate greater similarity.

For classroom exercises, this course may use **30 or lower** as a simple threshold for selecting close candidates. As with ssdeep, operational thresholds should be calibrated to the corpus and use case rather than treated as universal policy.

Do not read a TLSH value as a percentage. A distance of 30 does not mean “30% similar.”

### Similarity is evidence for a pivot, not the conclusion

Suppose `sync-client.exe` has a different SHA256 from a newly discovered file.

That tells you the files are not byte-identical.

Now suppose:
- they share an imphash;
- ssdeep reports a strong similarity score; or
- TLSH reports a small difference.

Those results justify deeper comparison. Useful next questions include:

- Do the files share imports, strings, configuration structure, or embedded resources?
- Do they communicate with related infrastructure?
- Do they exhibit similar behavior?
- Are the similarities better explained by a common packer or builder?
- Do multiple independent features point to the same relationship?

The strongest analytic statement is usually not “same family because the hash matched.” It is “the similarity result identified a candidate relationship that is supported—or not supported—by additional evidence.”

### Code-signing: inspect the signature, certificate, and status

Code-signing information provides another useful dimension of file analysis.

For a signed Windows file, useful fields include:
- **signer / subject** — the identity represented by the signing certificate;
- **issuer** — the certificate authority or intermediate that issued the certificate;
- **validity period** — the certificate's not-before and not-after dates;
- **signature status** — whether the signature and certificate chain validate in the context of the system performing the check.

Microsoft Authenticode is designed to identify the software publisher and verify that signed code has not been modified since signing. That is valuable evidence, but it does not mean “signed = safe.” Certificates can be stolen, abused, revoked, expired, or used to sign unwanted software.

Likewise, **unsigned** means the file does not contain a usable code-signing signature under the check you performed. It does not mean the file is malicious, and it does not establish attribution.

### Separate worked example — not A12

The files in this exercise are **training-only samples, not A12 evidence**. Canonical A12 does not supply a recovered `update.exe` sample or similarity hashes.

You compare a new PE file with `sync-client.exe`.

- SHA256 differs → the files are not byte-identical.
- imphash matches → they share the import structure represented by imphash.
- ssdeep score is 68 → the classroom exercise treats this as a strong similarity candidate.
- TLSH distance is 24 → the classroom exercise also treats this as a close candidate.
- the new file is signed by a certificate whose subject and issuer are visible → record those facts and verify signature status.

A reasonable conclusion is:

> The new sample is sufficiently similar to `sync-client.exe` to justify deeper comparison. The shared imphash and strong fuzzy-hash similarity support a possible relationship, but additional behavioral or structural evidence is needed before assigning a malware-family or actor relationship.

That statement uses the similarity evidence without asking it to prove more than it can.

### Paired platform application

Return to [VirusTotal](../../04-platforms/03-virustotal/student-guide.md) and [ANY.RUN](../../04-platforms/04-anyrun/student-guide.md). Retrieve a provided seed-file report, compare an exact hash with a similarity lead, and record one observed behavioral or structural feature that supports or weakens the proposed relationship. Preserve the report conditions and source/time. A similarity lead and an observed sandbox event answer different questions.

Keep the result with the enrichment record started in [2.5.1](../01-ioc-handling/student-guide.md).

## 2. Knowledge Check

1. Two PE files have the same imphash but different SHA256 values. What does the imphash match tell you, and what does it *not* establish?
2. ssdeep returns 72 while TLSH returns a difference of 22 for two samples. How do you interpret the direction of each score, and what should you do before calling the files related?
3. `sync-client.exe` is unsigned. What did you learn from that result, and what conclusions would go beyond the evidence?

## 3. Summary

Identity hashes answer **same file**. Similarity techniques help answer **which files deserve comparison**.

imphash describes PE import structure. ssdeep uses a higher-is-closer match score. TLSH uses a lower-is-closer difference score. None of them proves malware family or attribution on its own.

Code-signing information identifies the signing certificate and publisher claim and can support integrity checks. Signed does not automatically mean safe, and unsigned does not automatically mean malicious.


## 4. Related Modules

- 2.4.1 – Internal TIP
- 2.5.3 – RDAP / WHOIS
- 1.2.7 – MD5 / SHA identity hashing
- 2.4 – Platform enrichment / file pivots
- 2.1.8 – Attribution

## Supporting References

- [Mandiant, **Tracking Malware with Import Hashing**](https://cloud.google.com/blog/topics/threat-intelligence/tracking-malware-import-hashing) — explains imphash construction, uses, and limitations as a discovery and triage pivot.
- [ssdeep project documentation](https://ssdeep-project.github.io/ssdeep/usage.html) — explains fuzzy-hash comparison scores and how higher scores represent greater similarity.
- [Trend Micro, **TLSH**](https://github.com/trendmicro/tlsh) — documents TLSH as a fuzzy-matching technique and its lower-is-more-similar difference score.
- [Microsoft, **Authenticode Digital Signatures**](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode) — explains publisher identity and signed-code integrity.

**Next:** [2.5.3 – RDAP and WHOIS Concepts](../03-rdap-whois/student-guide.md).
