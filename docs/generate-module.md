# Generate a module (AI instructions)

Use this file when asked to generate module content for an **existing** teaching-unit ID (Gate 2). Humans follow [contributing.md](contributing.md). You follow this file.

This is a procedure. Clone the sibling module. Do not invent requirements, IDs, or a new voice.

**Caller prompt (either tool):**  
`Follow docs/generate-module.md and generate teaching-unit <ID> (<Title>) for me to review. Do not invent IDs.`

---

## 0. Preconditions

Stop and say what is missing if any of these fail:

- The ID already exists as a combined.md heading **or** a `#` cell (for example `1.2.5`, `2.1`, `3.1.1`).
- You were given that ID, not a vague topic and not an old display number (`section 7`, `section 8`).
- Gate 1 is done. You are not proposing a new matrix row.

**Assign work by ID prefix:** `0.x` = shared intro (`modules/00-intro/`). `1.x` = SOC (`modules/01-soc/`), `2.x` = Hunt (`modules/02-hunter/`), `3.x` = CTI (`modules/03-cti/`). `4.x` = Detection Engineer (`modules/04-de/`).

**`0.x` intro lessons:** five children (`0.1`–`0.5`). Generate only the asked child. Do not write cluster `0` as one module unless the human asks for the whole intro in one folder. Audience is all four roles (SOC, Hunter, CTI, DE). Proficiency Focus must list DE — same `A / B / B` (and `1a / 2b / 2b` on `0.5.1`) as the other roles. `0.1` is what a SOC *is*. Job one-liners are `0.2`. How work moves is `0.3`. Overlap is `0.4`. Course layout and the hand-off task are `0.5` / `0.5.1`. DYA / PRD are course fiction, not site policy. Do not invent tickets, PIR lists, or approval chains.

**How big is one lesson**

| Caller ID | What to generate |
|-----------|------------------|
| A **cluster** heading with several distinct K topics (`3.1` Core Intelligence Concepts) | **Stop.** List the child K items (`3.1.1`, `3.1.2`, `3.1.3`, …) and ask which one. Do **not** write the whole cluster. |
| A **child item** (`3.1.1`, `3.2.2`, `2.6.1`) | That K row plus its child T row(s) only (`3.1.1` + `3.1.1.1`). |
| A **unit** that is already one lesson (`1.1.1` Process Activity, `1.2.5` HTTP, `2.1` Purpose) | That heading’s rows (`1.1.1.1` K, `1.1.1.2` / `1.1.1.3` T). |

**`1.1.x` endpoint lessons:** five activity units (Process, File System, Network, Registry, Image/Driver Load). Use Sysmon Event IDs and MDE table/field names as the examples. Do not teach Sysmon install or config. `1.1.3` is **host-observed** network (initiating process → IP/port/domain). Protocol deep-dive is `1.2` Zeek. Do not merge the two.

**`1.4.x` alert lessons:** five units — investigate (`1.4.1`), classify (`1.4.2`), FP causes (`1.4.3`), categorize (`1.4.4`), SLA clocks (`1.4.5`). Do not collapse FP causes into classification. Do not restate a K item as its task. Detection authoring is `1.3`. Do not open the next `1.4` unit when asked for one child.

**`1.5.x` framework lessons:** three units — ATT&CK (`1.5.1`), Diamond (`1.5.2`), Kill Chain (`1.5.3`). Do not write all three as one module. Do not turn `1.5.1` into hunt planning (`2.5`) or an actor profile (`3.11`). Do not copy `modules/shared/frameworks/` into a role folder.

**`1.6.x` reporting lessons:** three units — report types (`1.6.1`), timelines (`1.6.2`), notification/distribution (`1.6.3`). Do not collapse them. Do not turn this into shift change (`1.7`) or an intel product (`3.11`). Alert start/close clocks are `1.4.5`.

**`1.7.x` shift-change lessons:** two units — changeover process (`1.7.1`), changeover report content (`1.7.2`). Do not collapse them. Do not turn this into reporting types/clocks/routing (`1.6`) or site-specific ops (`1.8`).

**`1.8.x` site-specific lessons:** five units — environment (`1.8.1`), PCAP handling (`1.8.2`), tool access (`1.8.3`), investigation notes (`1.8.4`), IR process (`1.8.5`). Do not collapse IR into notes. Classroom cards are stand-ins, not live org policy. Do not turn `1.8.2` into Zeek (`1.2`) or `1.8.5` into report routing (`1.6.3`).

**`3.1.x` core intel lessons:** eight children (`3.1.1`–`3.1.8`). Generate only the asked child unless the caller asks for the rest of `3.1`. Do not write cluster `3.1` as one module. Collection *source classes* are `3.1.8` (not the lifecycle collection *stage* in `3.1.2`). Audience tailoring is `3.1.6`; finished production is `3.11`. Actor profile is `3.11.1.2`. Local collection *request process* is `3.12.2.1`.

**`3.2.x` tradecraft lessons:** four children — estimative language (`3.2.1`), structured techniques (`3.2.2`), Admiralty Code (`3.2.3`), cognitive bias (`3.2.4`). Generate only the asked child. Do not write cluster `3.2` as one module. Attribution *confidence* (low/medium/high) is `3.1.7`; this lesson is *likelihood terms*. Source letters are `3.2.3`.

**`3.3.x` tool lessons:** two children — internal TIP (`3.3.1`), external tools (`3.3.2`). Generate only the asked child. Do not write cluster `3.3` as one module. Do not turn `3.3.1` into VirusTotal / Silent Push (`3.3.2`, `3.9`) or STIX authoring (`3.10`). Classroom TIP names are stand-ins.

**`3.4` file-similarity lesson:** one teaching unit (`3.4.1`) — imphash, ssdeep, TLSH, and code-signing. Do not turn it into VT Relations (`3.9`) or cryptographic identity-only hashes (`1.2.7` MD5/SHA). Classroom match thresholds are stand-ins.

**`3.5` RDAP/WHOIS lesson:** one teaching unit (`3.5.1`). Do not turn it into SOA / advanced DNS (`3.6`) or Silent Push PDNS (`3.3.2`). Redacted registrant is not “no intel” and is not nation-state attribution (`3.1.7`).

**`3.6` advanced-DNS lesson:** one teaching unit (`3.6.1`) — interpret SOA and use other records for enrichment/pivot. Do not re-teach Zeek `dns` fields or DGA (`1.2.3`). Do not turn it into RDAP (`3.5`) or Silent Push PDNS (`3.3.2`).

**`3.7.x` CTI framework lessons:** four children — ATT&CK (`3.7.1`), Diamond (`3.7.2`), Kill Chain (`3.7.3`), DTF (`3.7.4`). Generate only the asked child. Do not write cluster `3.7` or lumped outline `3.7.5` as one module. Do not re-teach SOC floor (`1.5`) or hunt planning (`2.5`). Do not copy `modules/shared/frameworks/`. DTF is real PTA/P discovery IDs from [defenders-threatmesh-framework](https://github.com/MalasadaTech/defenders-threatmesh-framework). Product is the DTF ID line. No scoring. Do not invent P-codes. Do not teach every P-code. Generic hop sentence is `3.8.1`. Applicable-to-environment TTP extract is `3.8.2`. Actor profile is `3.11`.

**`2.6.x` hunter attacker-technique lessons:** three children — persistence recognition (`2.6.1`), privilege-escalation recognition (`2.6.2`), hunt-for-specific (`2.6.3`). Generate only the asked child. Do not write cluster `2.6` or lumped outline `2.6.3` tasks 1–2 as the `2.6.3` module — those recognition tasks already live in `2.6.1` / `2.6.2`. `2.6.3` is the scoped hunt for **one named** technique. Do not re-teach recognition. Hunt-type execute is `2.2.1`. Hunt card format is `2.2.2`. ATT&CK remapping is `2.5`. Local hunt control is `2.7`.

**`2.7.x` hunter site-specific lessons:** three children — hunt control / leads (`2.7.1`), hunt documentation (`2.7.2`), hunt outputs / hand-off (`2.7.3`). Generate only the asked child unless the caller asks for all of `2.7`. Do **not** invent local hunt tickets, templates, output lists, or hand-off charts. Teach that every site has its own, and a new hunter must obtain them early. Hunt *development* is `2.2.2`. Hunt-for-specific is `2.6.3`. SOC tickets / IR are `1.6` / `1.8.5`. Classroom stand-ins are lesson-only — not live org policy.

**`3.8.x` CTI enrichment lessons:** generate only the asked child (`3.8.1` infra pivot, `3.8.2` applicable TTPs, `3.8.3` IOC handling, `3.8.4` relevance/impact). Do not write cluster `3.8` as one module. `3.8.1` writes the generic hop sentence from a seed; do not re-teach RDAP (`3.5`), SOA (`3.6`), or Silent Push tool choice (`3.3.2`). The DTF ID line is `3.7.4`. `3.8.2` is apply-to-this-environment, not ATT&CK mapping (`3.7.1`) and not organizational impact (`3.8.4`). `3.8.3` handles the IOC as an object (keep / expire / enrich / link) — not the 3.8.1 hop sentence and not 3.9 platform depth. `3.8.4` is the “so what here” line. Use only real ATT&CK IDs. VT Relations depth is `3.9`. Actor profile is `3.11`.

**`3.9.x` CTI platform lessons:** four children — VirusTotal Relations/Behavior (`3.9.1`), AnyRun (`3.9.2`), Silent Push (`3.9.3`), URLScan (`3.9.4`). Generate only the asked child unless the caller asks for all of `3.9`. Do not write cluster `3.9` as one module. Do not re-teach the 3.3.2 survey (purpose / when to pick). Hunt conversion to SIEM/Zeek is `2.3.1`. Conceptual infra hop is `3.8.1`. File-similarity hashes are `3.4`. Applicable TTPs are `3.8.2`. Classroom result cards are lesson-only — do not require a live vendor account.

**`3.10.x` CTI STIX lessons:** two children — core objects (`3.10.1`), production use (`3.10.2` including create/validate and TAXII). Generate only the asked child unless the caller asks for all of `3.10`. Do not write cluster `3.10` or lumped outline `3.10.3` as one module. Hunt-facing STIX *input* is `2.4.3`. Finished narrative products are `3.11`. TIP retrieve is `3.3.1`. Use real STIX 2.1 object and relationship types. Do not invent types. Classroom bundles/collections are lesson-only — do not stand up a TAXII server.

**`3.11.x` CTI production lessons:** three children — finished products (`3.11.1` including actor profile `3.11.1.2`), dissemination (`3.11.2` including tailor and channels), RFIs (`3.11.3`). Generate only the asked child unless the caller asks for all of `3.11`. Do not write cluster `3.11` as one module. Audience *rewrite* floor is `3.1.6`. Attribution *assessment* is `3.1.7`. STIX bundle/TAXII is `3.10`. SOC ticket types/routing are `1.6`. Local approval and customer lists are `3.12`. Classroom markings/channels/RFI queue are lesson-only — not live org policy.

**`3.12.x` CTI site-specific lessons:** three children — local priorities (`3.12.1`), local production/approval/archive (`3.12.2`), local customers/channels (`3.12.3`). Generate only the asked child unless the caller asks for all of `3.12`. Do **not** invent PIRs, approval chains, archive paths, or customer lists. Teach that every org/section has its own, and a new analyst must obtain them early. PIR *concept* is `3.1.4`. Collection *planning* is `3.1.8`. Finished draft is `3.11.1`. Classroom TLP/channels are `3.11.2`. SOC site orientation is `1.8`.

**`4.x` Detection Engineer lessons:** generate only the asked child (`4.1`–`4.7` each with its T row(s); `4.8.1` or `4.8.2` for site). Do **not** write cluster `4` as one module. DE is primary. Copy 3/5/7 from combined.md for **all four roles** (SOC / Hunter / CTI awareness is on combined only — do not add 4.x rows to those role sheets). Folder is `modules/04-de/<nn-short-name>/`. Voice: latest `04-de/` sibling; if none, clone `00-intro` (short, no pad), not an old hour-long SOC lesson.

This section is how detections are **run as a service**. Rule *syntax* and a first read/write are **`1.3`**. Do not teach SIGMA / Suricata / YARA / SIEM authoring here. Nominations from SOC, hunt, and CTI need not be perfect. Extra infrastructure is a **block** (firewall / IA), not a DE deploy. Do **not** invent DYA meta-field lists, change boards, or deploy tickets — those vary by site (`4.8`); obtain the list, do not make one up. DYA / PRD are course fiction, not site policy.

- `4.1` What DE owns — the set (new / change / retire / deploy). Sort work to DE, nominator, `1.3`, or a block. Reject “rough is not DE” and “block request is a deploy.” Sound/test is `4.2`. Nomination review depth is `4.3`. Tunes are `4.4`. Packages are `4.5`. When to modify/retire/leave is `4.6`.
- `4.2` Sound + test + shop requirements + close the loop. The *field list* is `4.8`. Do not invent fields.
- `4.3` Nominations — who can nominate; accept / send back / reject; nominator bar is “clear enough to review.” Clear enough means the **need** plus **context or a reference** (investigation or intel report — number, or title and URL). A drafted rule if they have one — **not** required. Do not invent a DYA form or ticket name.
- `4.4` Tune requests on *live* rules. Same desk, different inbox. Reject investigation, block, or IR containment dressed as a tune. Clear enough means **which live rule** plus **context or a reference** (investigation or intel report — number, or title and URL). “Missing context” in 4.4.a is about the *rule*, not the pointer. Do not invent a DYA form or ticket name.
- `4.5` Hunt and intel packages. Both are inputs. “No new rule” is valid. Treat like a nomination (`4.3`). Reject turning the package into a block list.
- `4.6` Lifecycle — modify / retire / leave, and why. “We blocked it” is not automatically retire.
- `4.7` Sensors — lighter. Sometimes DE. Dead sensor is not “no threat.” Not vendor admin or architecture.
- `4.8.x` Site-specific — generate only the asked child (`4.8.1` local requirements, `4.8.2` review/deploy/retire paths). Obtain-and-follow. Do not invent the list or a ticket name.

**IDs and ratings come from the matrix. Content floor is the outline** for *this* lesson only. Teach every outline `a/b/c` and task that belong to these rows. Expand only to support that syllabus. Do not invent a new matrix obligation. Do not pull in the rest of cluster `3.1` when asked for `3.1.1`.

If the user wants a **new** requirement, stop and point them at [templates/requirement-proposal.md](../templates/requirement-proposal.md).

---

## 1. Read, in this order

1. The [training-outlines.md](outlines/training-outlines.md) block for **this lesson** — e.g. outline `3.1.1` + `3.1.1.1`, not all of outline `3.1`.
2. The matching combined.md **rows** (the K item and its T pair), plus 3/5/7 codes for every role.
3. The matching role matrix (`soc.md` / `hunter.md` / `cti.md`).
4. [proficiency-legend.md](proficiency-legend.md)
5. [contributing.md](contributing.md) Gate 2
6. [templates/student-guide.md](../templates/student-guide.md), [instructor-guide.md](../templates/instructor-guide.md), [slides.md](../templates/slides.md)
7. The **previous sibling module** in the same unit — full `README.md`, `student-guide.md`, `instructor-guide.md`, `slides.md`

Siblings: Zeek → latest `modules/01-soc/02-zeek/`. CTI `3.1.x` → `modules/03-cti/01-core-intel/01-data-info-intel/` (shape + how to stay inside one child item). DE `4.x` → latest `modules/04-de/` (if none, clone `00-intro` voice only). Other first-of-prefix modules may clone TLS for package shape only.

Also open [concept-index.md](concept-index.md) and [tracker.csv](tracker.csv) before you write.

---

## 2. Resolve IDs (do not invent)

| You need | Where it comes from |
|----------|---------------------|
| Lesson ID | What the user typed. Examples: `1.2.5`, `2.1`, `3.1.1`. Not cluster `3.1`. |
| Matrix item IDs | Combined `#` cells for this lesson only. Hunt and CTI nest each task under its knowledge item (`3.2.1` K, `3.2.1.1` T; `2.6.1` K persistence, `2.6.1.1` T). Do not invent a sibling T such as `3.2.2` for the `3.2.1` lesson. SOC Zeek units stay `1.2.x.1` K / `1.2.x.2` T. |
| Outline block | The outline K heading + tasks that map to those rows (example: matrix `3.1.1` / `3.1.1.1` = outline `3.1.1` + `3.1.1.1`). |
| Folder | Usually `modules/<role>/<unit>/<nn-short-name>/`. Cluster children may use `modules/03-cti/01-core-intel/<nn-short-name>/`. |
| Roles | Primary/secondary from the matrix. |
| Proficiency lines | Copy **3 / 5 / 7** codes from the matrix into **both** the student guide and the instructor guide. Same string in both files. Do not collapse levels (wrong: `Hunter A/1a → B/3c`). Do not invent a `4d` if the matrix is `4c`. |

Record the outline ↔ matrix map in the module `README.md`, same table shape as TLS.

If Gate 1 said “add to an existing module,” amend that folder. Do not create a new one.

---

## 3. Clone this shape

Match the sibling’s **voice and fences** (plain words, same names, stay in this lesson). **Do not copy** the sibling’s length, section list, tables, example count, or slide count. An old hour-long lesson is not a mold for a short intro.

**Do not add optional content to fill.** If the template marks a section optional and this lesson does not need it, omit it.

| Artifact | Shape |
|----------|--------|
| Time | As long as the outline needs. A short intro may be 15–20 minutes. A log-reading lesson may be an hour. Never stretch a short topic to fill 60–75 minutes. |
| Audience | Primary + secondary roles from the matrix |
| Proficiency | 3/5/7 codes from the matrix, per role, identical in student + instructor headers |
| Student guide | Objectives → key concepts that cover the outline, including what each **task** looks like when done well. **No labs, demos, or hands-on exercises** until the human asks. **Knowledge check: 1–3 questions per lesson** that has slides. Short summary. |
| Instructor guide | **Intro required** (Context + what this hour is). No demo or lab write-up until the human asks. Timing table lists only sections you actually teach. Answers for the 1–3 lesson questions. |
| Slides | As many as you need. Intro + concepts + **knowledge check (1–3 questions for the lesson)** are required. No demo or exercise slides until the human asks. Face of each slide is short enough to read alone. **Speaker Notes** on every slide: a few plain sentences (why this slide, how it connects). |
| Answers | Only in the instructor guide. No standalone `answer-key.md`. No quiz. |

Outline **tasks stay**. Teach what the task *is* (the product line, what good looks like). **Do not write labs, demos, or hands-on exercises** unless the human asks. Existing labs stay until that section is reviewed.

Examples: use them when they help. Do not invent fail-stories to hit a count.

**“This lesson / other” table** and **“expected vs lead” table:** optional. They fence this hour vs the next, or good call vs bad call. Add one only if it prevents a real mix-up. Do not add both by default. Do not add them to fill.

**Knowledge check:** **1–3 questions per lesson** that has slides. Required. Put them on the slides and/or in the student guide. Not per concept. Do not write a fourth question to fill. Do not ask about the next lesson just to have more items.

Voice: direct, instructional, short paragraphs, tables for fields. Do not lecture about decrypting traffic, writing Zeek scripts, or other later modules.

**Context (required). Challenges (only if real):**

Write **Context (plain language)** as the first block in the instructor overview, before Key Teaching Points. Anyone who was not in the planning chat should still see the connection. Use ordinary words. No outline letters, no matrix codes in this block.

Include:

- What this hour is for (one or two sentences)
- How it hooks to the hour before and the hour after (one line each)
- Why we are doing it this way (the human’s stated reason, not a new rule)
- What we are *not* doing this hour

If you add a step the human did not say, it must appear in Context as “extra, because ___.” If you cannot finish that sentence, do not add the step. Do not jump ahead.

**Common Student Challenges:** omit the whole list when the hour is this simple (facts everyone already has). Do not invent struggles to satisfy a quota. If you *do* list a challenge, each bullet is one short why + one concrete example. Not a label alone (wrong: “They invent a ticket.” Right: “They invent a ticket so the exercise has an answer — e.g. ‘open Jira HUNT-17.’”).

**Slides:** someone who only reads the deck should still get the point. Speaker notes carry the why; they are not “read the bullets again.”

**Words:** use the word the outline and student guide already use. If you want a shop nickname, define it on first use in ordinary words (“bulletin” = this week’s CTI report). If the student guide says **report**, the instructor guide and slide notes say **report** unless you add that one-line gloss. Do not invent a second name and assume the reader knows it.

---

## 4. Teach at least the outline

- Outline knowledge bullets (`a`, `b`, `c`…) become the field/idea sections. None may be skipped.
- Outline tasks are taught as *what good looks like*, not as a lab (until the human asks for labs).
- Combined.md / role-matrix rows are the **sign-off** items and IDs. Put them in the README map.
- Expansion is allowed when it supports the outline (Zeek `uid` / `ts`, extra examples). New obligations need Gate 1.
- If an outline bullet has no home in this teaching-unit, **stop** and say so. Do not drop it.
- Stay out of the *next* lesson (for a `3.1.x` child, that means the next `3.1` topic). Point to it under Related modules.

---

## 5. Write these files

New module:

```
modules/<role>/<unit>/<nn-short-name>/          # or …/01-core-intel/<nn-short-name>/ for 3.1.x
  README.md
  student-guide.md
  instructor-guide.md
  slides.md
  assets/.gitkeep
```

`README.md` must include path, roles, time, mapped proficiency table, **Concepts taught**, artifact links.

Then update:

- [concept-index.md](concept-index.md) — every README concept; **Taught** here; **Used** on this module for terms taught earlier (`uid`, `conn` log, …); aliases people will search; link the folder, not a line number
- [tracker.csv](tracker.csv) — add or update the row; mark only the artifacts you actually wrote
- [tracker.md](tracker.md) — folder map row if this ID is new
- README numbering table in the repo root if this ID is new

Do not set tracker status to `Complete` for the module as a whole if that column exists as a single status — leave content at **Review** for the human. Use the per-artifact columns like the Zeek rows: student/instructor/slides complete, then tell the user it is ready to review.

---

## 6. Do not

- Generate all of cluster `3.1` when asked for `3.1` or `3.1.1`
- Generate all of cluster `4` when asked for `4` or `4.1`
- Skip an outline bullet because the matrix row is shorter
- Invent matrix IDs, outline headings, or proficiency codes
- Collapse or invent 3/5/7 codes (instructor and student headers must match the matrix)
- Treat combined.md `## 7` / `## 8` / `## 9` as real (those headings are gone; use `2.x` / `3.x` / `1.8`)
- Index sample IPs, `example.com`, or passing name-drops
- Put JA3-style depth in a survey module, or HTTP bodies in a TLS module
- Copy shared frameworks into a role folder
- Mark the module human-accepted (`Complete` on the whole package) — stop for review
- Write Gate 1 proposal files unless asked
- Skip **Context (plain language)**
- Invent Common Student Challenges to fill a quota, or leave a listed challenge as a label with no example
- Leave a slide without plain-language speaker notes
- Jump ahead of what the human asked without saying why in Context
- Pad a short lesson, or add optional sections (examples, lab, extra tables, extra slides) only to fill
- Copy a sibling’s table of contents, timing, or example set
- Write more than 3 knowledge-check questions for the lesson, or skip the 1–3 when the lesson has slides
- Write a new lab, demo, or hands-on exercise unless the human asked for one
- Skip the fluff review when you finish
- Use a shop nickname (bulletin, annex, firehose) in the instructor guide or slides without the student-guide word or a one-line gloss

---

## 7. When you finish

List the paths you wrote and the outline ↔ matrix map. Remind the reviewer to confirm: (1) every outline bullet/task is in the student guide, (2) Concepts taught matches the index, (3) Context is in the instructor guide, (4) any challenges have examples (or the list is omitted), (5) every slide has plain speaker notes, (6) **fluff review done** — nothing is there only to fill, (7) 1–3 knowledge-check questions for the lesson, (8) no new lab/demo unless asked, (9) status stays at review until they accept the lesson.

**Fluff review (required, you and the human):** For each extra example, table, slide, lab step, or question, say which outline bullet it serves. If you cannot, delete it.
