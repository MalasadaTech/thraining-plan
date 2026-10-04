# Instructor Guide – Module 2.2.3 – Admiralty Code

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.3 B / C / C ; 2.2.3.1 3c / 4c / 4d  
- Hunter: 2.2.3 A / B / B ; 2.2.3.1 1a / 2b / 3c  
- SOC: 2.2.3 A / A / B ; 2.2.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes  
**Delivery Method:** Instructor-led explanation and discussion

## Module Overview for Instructors

**Purpose:** Teach learners to evaluate the source and the specific information as two independent judgments, then communicate both with an Admiralty Code rating.

**Context:** The previous lesson examined how analysts test reasoning. This lesson examines the reporting that feeds that reasoning. Its central discipline is separation: source reliability is not the same thing as information credibility.

Avoid teaching fixed mappings such as “internal = B” or “anonymous blog = E5.” The code is applied from the evidence available about the source and the claim. Use conditional scenarios so learners practice the reasoning rather than memorizing source categories.

**Required materials:** The aligned student guide and slide deck.

## Learning Objectives

By the end of this module, learners will be able to:

1. Evaluate source reliability (A–F) separately from information credibility (1–6).
2. Combine the two ratings into an Admiralty Code and explain what the pair communicates.

**Mapped Proficiency Items:**
- K: 2.2.3 – Admiralty Code / source reliability and information credibility
- T: 2.2.3.1 – Assign Admiralty Code ratings and evaluate source reliability and credibility

## Suggested Timing

| Part | Time | Teaching purpose |
|---|---:|---|
| Introduction | 3 minutes | Establish the two independent questions. |
| Source reliability | 5 minutes | Explain what the letter evaluates. |
| Information credibility | 5 minutes | Explain what the number evaluates. |
| Combined examples | 6 minutes | Apply the pair without collapsing the scales. |
| Knowledge check | 4 minutes | Assign and explain ratings. |
| Summary and transition | 1 minute | Connect source evaluation to cognitive bias. |
| **Total** | **24 minutes** | Adjust discussion time as needed. |

## Detailed Teaching Notes

### 1. Start with two questions

Write the two questions separately: “How reliable is the source generally?” and “How credible is this particular information?” Ask learners why those questions can produce different answers.

A familiar example is a normally reliable source reporting something outside its usual access or an unknown source whose claim later receives independent confirmation.

### 2. Teach source reliability as a record, not a category

Walk A through F. Emphasize that the letter should be informed by what is known about the source's history, access, and reporting record. Being internal, commercial, or public does not by itself decide the letter.

Use **F** deliberately: it means reliability cannot be judged. It is not a synonym for “bad source.”

### 3. Teach information credibility as claim-specific

Walk 1 through 6. Emphasize corroboration and the evidence surrounding the specific claim. A rating of **1** requires confirmation by other sources; a high-reliability source does not supply that confirmation by itself.

Use **6** deliberately: it means the truth of the claim cannot be judged. It is not the same as saying the source is unknown.

### 4. Combine without blending

Use the scenario: a source with a demonstrated record supporting **B** reports a fact independently confirmed elsewhere. The result is **B1**. Ask learners to read the pair aloud in words.

Then use an unsigned source with no track record and a claim that cannot be evaluated: **F6** is reasonable. Ask what new evidence could change the number while leaving the letter unchanged.

### 5. Keep Admiralty separate from likelihood and confidence

Learners may try to translate **2** directly into *likely*. Explain that the credibility scale and the estimative-language scale are different tools. Likewise, low/medium/high analytic confidence is a separate judgment from the Admiralty pair.

## Common Student Challenges

| Misunderstanding | Teaching response |
|---|---|
| A trusted source makes every claim confirmed. | Ask what independent source confirms this particular claim. |
| Internal sources deserve a fixed letter. | Ask what is known about that source's actual reporting record and access. |
| F means unreliable. | Clarify that F means reliability cannot be judged. E is the unreliable category. |
| 6 means false. | Clarify that 6 means truth cannot be judged; it is not the same as 5 improbable. |
| Admiralty 2 means the same thing as “likely.” | Explain that the two scales serve different analytic functions. |

## Knowledge Check – Answer Key

### 1. Why does a highly reliable source not automatically make a claim confirmed?

**Expected answer:** Because the letter rates the source generally, while confirmation is a judgment about this specific information and requires corroboration from other sources.

### 2. Usually reliable source + independent confirmation

**Expected answer:** **B1**. The source is usually reliable and the specific information is confirmed by another source.

### 3. Anonymous source with no history + unevaluable claim

**Expected answer:** **F6** is reasonable. The source reliability cannot be judged and the truth of the information cannot be judged.

## Summary and Transition

Close by having learners read a pair in words: letter = source, number = information. The next lesson examines how cognitive shortcuts can still distort judgment even when analysts have source-rating and analytic techniques available.
