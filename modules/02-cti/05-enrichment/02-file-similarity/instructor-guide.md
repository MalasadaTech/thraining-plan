# Instructor Guide – Module 2.5.2 – Hashing and Similarity Concepts

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.5.2 B / C / C ; 2.5.2.1 3c / 4c / 4d ; 2.5.2.2 3c / 4c / 4c  
- Hunter: 2.5.2 A / B / B ; 2.5.2.1 1a / 2b / 3c ; 2.5.2.2 1a / 2b / 3c  
- SOC: 2.5.2 A / A / B ; 2.5.2.1 1a / 1a / 2b ; 2.5.2.2 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Help learners use imphash, ssdeep, and TLSH as similarity pivots that identify samples worth comparing, then interpret code-signing information without overstating what the signature proves.

**Context:** Module 2.4.1 taught learners to recover context the organization already holds. This lesson focuses on a file-analysis problem: a new file may have a different cryptographic hash from a known sample but still share structural or content similarity.

The central teaching discipline is **similarity is a lead, not a verdict**. Learners should be able to interpret the technique correctly, select a candidate for further comparison, and state the limits of the evidence.

**Classroom thresholds:** The student guide retains ssdeep ≥50 and TLSH ≤30 for exercises because they provide a simple classroom decision point. Present them as local teaching thresholds only. Real thresholds should be calibrated to the corpus and use case.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Explain what imphash, ssdeep, and TLSH measure and use similarity results to identify samples that merit further comparison.
2. Extract and interpret code-signing information from a file without treating the signature as proof of trust or attribution.

**Mapped Proficiency Items:**
- K: 2.5.2 – Hashing and similarity concepts
- T: 2.5.2.1 – Use file similarity hashes to identify related samples
- T: 2.5.2.2 – Extract and interpret certificate / code-signing information from a file

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Contrast exact identity with similarity. |
| imphash | 5 minutes | Explain the PE-import pivot and its limitations. |
| ssdeep and TLSH | 6 minutes | Interpret direction, score, and classroom thresholds. |
| Code-signing | 5 minutes | Interpret signer, issuer, validity, and signature status. |
| Worked example | 3 minutes | Combine multiple similarity signals without overclaiming. |
| Knowledge check | 3 minutes | Test interpretation and evidence boundaries. |
| **Total** | **25 minutes** | Compress discussion slightly if needed. |

## Detailed Teaching Notes

### 1. Begin with two different questions

Write these on the board:

- **Are these files exactly the same?**
- **Are these files similar enough to compare?**

SHA256 answers the first question. The techniques in this lesson help with the second.

This prevents learners from treating similarity values as weaker versions of cryptographic identity.

### 2. Teach imphash as an import-structure pivot

Explain that imphash is derived from the ordered imported DLLs/functions of a PE file.

A matching imphash can be useful because similar source, build process, shared builder, or common packer may preserve the import structure. It is not family proof.

Use Mandiant's own limitation as the teaching principle: imphash is valuable for triage and discovery, but simple tools, shared builders, or packers can create matches across otherwise unrelated activity.

Ask learners: **What additional evidence would you want before calling two samples the same family?**

Good answers include behavior, configuration format, strings, code overlap, infrastructure, or additional file characteristics.

### 3. Teach ssdeep without turning the score into a probability

ssdeep returns a 0–100 comparison score. Higher means more similar.

The official documentation cautions that a match is not itself proof the files are related. Reinforce that the score is a prioritization signal.

For classroom exercises, ≥50 means “select this sample for further comparison.” Avoid teaching “50 means 50% related.”

### 4. Teach TLSH as a difference

TLSH uses a difference score. Lower is more similar.

Use the contrast explicitly:
- ssdeep: **higher = closer**
- TLSH: **lower = closer**

For classroom exercises, ≤30 means “select this sample for further comparison.” The number is not a percentage.

### 5. Show why multiple features are stronger than one

Use the `update.exe` worked example:
- different SHA256;
- matching imphash;
- ssdeep 68;
- TLSH 24.

Ask learners what they can say.

A strong answer is that several independent similarity signals justify deeper comparison. They still should not jump directly to actor attribution or guaranteed malware-family identity.

### 6. Teach code-signing as identity and integrity evidence

Have learners separate:
- signer / subject;
- issuer;
- validity period;
- signature verification status.

Authenticode can help verify the publisher identity represented by the certificate and whether the signed code has changed since signing. It does not guarantee the software is benign.

Point out several reasons:
- certificates can be stolen or abused;
- certificates can be expired or revoked;
- unwanted or malicious software can be signed;
- unsigned software is common and is not automatically malicious.

### 7. Keep the evidence boundary visible

The lesson should repeatedly return to this pattern:

**Observation → what it supports → what it does not establish.**

Examples:
- same imphash → shared import structure → not same actor.
- ssdeep 72 → strong similarity signal → not 72% probability of common origin.
- TLSH 22 → small difference → not proof of family.
- signed → certificate identity/integrity evidence → not safe.
- unsigned → no usable signature → not malicious.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| Same imphash means same malware family. | Ask what shared builder or packer could explain the same imports. |
| ssdeep score is a probability or percent relationship. | Describe it as a match score used to prioritize comparison. |
| TLSH 80 means “80% similar.” | Reinforce that TLSH is a difference score: lower is closer. |
| One threshold works for every corpus. | Explain that exercise thresholds are teaching aids; operational cutoffs require calibration. |
| Signed means trusted or benign. | Separate certificate identity/integrity from behavior or reputation. |
| Unsigned means malicious or unattributed nation-state malware. | State only the observable: no usable signature was present. |

## Knowledge Check – Answer Key

### 1. Same imphash, different SHA256

**Expected answer:** The files share the import structure represented by imphash and are useful candidates for further comparison. The match does not establish byte identity, malware family, actor, or common origin by itself.

### 2. ssdeep 72 and TLSH 22

**Expected answer:** Both values indicate relatively strong similarity under their respective methods: higher is closer for ssdeep and lower is closer for TLSH. The analyst should compare additional structural, behavioral, or contextual evidence before asserting a relationship.

### 3. `update.exe` is unsigned

**Expected answer:** The file has no usable code-signing signature under the check performed. That does not establish maliciousness, actor attribution, or malware family.

## Summary and Transition

Close with the wording: **similarity techniques help find candidates; analysis establishes relationships.**

The next module moves from file pivots to registration data for domains and IP space.

## Instructor References

- [Mandiant, *Tracking Malware with Import Hashing*](https://cloud.google.com/blog/topics/threat-intelligence/tracking-malware-import-hashing).
- [ssdeep project documentation](https://ssdeep-project.github.io/ssdeep/usage.html).
- [Trend Micro TLSH project documentation](https://github.com/trendmicro/tlsh).
- [Microsoft Authenticode Digital Signatures documentation](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode).

## Paired application

Complete the application portion of 2.4.3 and 2.4.4 with this lesson. Retrieve a provided seed-file report, compare an exact hash with a similarity lead, and record one observed behavioral or structural feature that supports or weakens the proposed relationship. Preserve the report conditions and source/time. A similarity lead and an observed sandbox event answer different questions. Use the existing platform-guide answer key for its knowledge check. Account for the remaining platform time separately from this method lesson; do not repeat the orientation.
