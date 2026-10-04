# Module 2.2.3 – Admiralty Code

**Target Audience:** CTI Analyst (primary); Threat Hunter, SOC Analyst (secondary)  
**Proficiency Focus:**  
- CTI: 2.2.3 B / C / C ; 2.2.3.1 3c / 4c / 4d  
- Hunter: 2.2.3 A / B / B ; 2.2.3.1 1a / 2b / 3c  
- SOC: 2.2.3 A / A / B ; 2.2.3.1 1a / 1a / 2b  
**Estimated Time:** 20–25 minutes

## Learning Objectives

By the end of this module, you will be able to:

1. Evaluate **source reliability** (A–F) separately from **information credibility** (1–6).
2. Combine the two ratings into an Admiralty Code and explain what the pair communicates.

**Mapped Proficiency Items:**
- K: 2.2.3 – Admiralty Code / source reliability and information credibility
- T: 2.2.3.1 – Assign Admiralty Code ratings and evaluate source reliability and credibility

## 1. Key Concepts

When analysts receive reporting, two questions need to stay separate:

1. **How reliable is this source generally?**
2. **How credible is this particular piece of information?**

A source with a strong history can still provide a weak or unconfirmed claim. A source whose reliability is unknown can occasionally provide information that later proves correct. The Admiralty Code keeps those judgments separate by assigning a **letter** to the source and a **number** to the information.

### The two scales

| Source reliability | Information credibility |
|---|---|
| **A** – Completely reliable | **1** – Confirmed by other sources |
| **B** – Usually reliable | **2** – Probably true |
| **C** – Fairly reliable | **3** – Possibly true |
| **D** – Not usually reliable | **4** – Doubtful |
| **E** – Unreliable | **5** – Improbable |
| **F** – Reliability cannot be judged | **6** – Truth cannot be judged |

A complete rating combines the two, such as **B2**.

The letter and number answer different questions. **B2** means the source is usually reliable and this particular information is assessed as probably true. The source's history does not automatically make the information confirmed, and the apparent plausibility of one claim does not automatically make the source highly reliable.

### How to think about source reliability

Source reliability should be based on what is known about the source over time: its access, record of accurate reporting, consistency, and the degree to which its reliability can actually be evaluated.

The source category alone is not enough. “Internal,” “commercial,” or “OSINT” does not automatically map to a particular letter. For example, an internal sensor with a well-understood collection function and a strong history may merit a different rating from a newly deployed sensor whose behavior has not yet been validated.

### How to think about information credibility

Information credibility concerns the specific claim. Relevant considerations include corroboration, consistency with independently observed facts, plausibility, directness of the reporting, and whether contradictory evidence exists.

A **1** requires confirmation by other sources. A single report from a trusted source does not become a 1 merely because the source has a high reliability rating.

### F and 6 mean different things

**F** means the analyst cannot judge the reliability of the source. **6** means the analyst cannot judge the truth of the information. Those conditions often appear together, but they are still separate judgments.

For example, an anonymous public post with no history and a claim that cannot be corroborated might reasonably be rated **F6**. If later independent evidence confirms the claim, the information rating could change even though the original source's reliability remains unknown.

### Worked examples

Suppose a sensor has an established record that supports a **B** source rating. It reports a connection that is independently confirmed by host evidence. The combined rating would be **B1**: usually reliable source, information confirmed by another source.

Now consider an unsigned public post from an unknown author making a claim that cannot be checked against any other evidence. The source reliability may be **F**, and the information credibility may be **6**. The rating communicates uncertainty about both dimensions without pretending they are the same uncertainty.

The number in an Admiralty rating is not an estimative-likelihood term. “Probably true” on the credibility scale and “likely” in an analytic judgment belong to different systems and answer different questions.

## 2. Knowledge Check

1. Why does a highly reliable source not automatically make a particular claim confirmed?
2. A source is usually reliable, and another independent source confirms the specific claim. What Admiralty rating fits that scenario, and what does it mean?
3. An anonymous source has no reliability history, and the claim cannot be corroborated or evaluated. What rating is reasonable, and why?

## 3. Summary

The Admiralty Code separates the reliability of the source from the credibility of the information. The letter describes the source; the number describes the particular claim. Keeping the two ratings independent prevents a trusted source from turning every claim into confirmed information and prevents one plausible claim from becoming a blanket endorsement of the source.


## 4. Related Modules

- 2.2.1 – Estimative language
- 2.2.2 – Structured analytic techniques (previous)
- 2.2.4 – Cognitive biases
- 2.1.8 – Attribution confidence

**Next:** [2.2.4 – Cognitive Biases and Mitigation](../04-cognitive-biases/student-guide.md).
