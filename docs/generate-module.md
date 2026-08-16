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

**Assign work by ID prefix:** `1.x` = SOC (`modules/01-soc/`), `2.x` = Hunt (`modules/02-hunter/`), `3.x` = CTI (`modules/03-cti/`).

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

**`3.7.x` CTI framework lessons:** four children — ATT&CK (`3.7.1`), Diamond (`3.7.2`), Kill Chain (`3.7.3`), DTF (`3.7.4`). Generate only the asked child. Do not write cluster `3.7` or lumped outline `3.7.5` as one module. Do not re-teach SOC floor (`1.5`) or hunt planning (`2.5`). Do not copy `modules/shared/frameworks/`. Applicable-to-environment TTP extract is `3.8.2`. Actor profile is `3.11`.

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

Siblings: Zeek → latest `modules/01-soc/02-zeek/`. CTI `3.1.x` → `modules/03-cti/01-core-intel/01-data-info-intel/` (shape + how to stay inside one child item). Other first-of-prefix modules may clone TLS for package shape only.

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

Match the sibling. Typical engine module:

| Artifact | Shape |
|----------|--------|
| Time | 60–75 minutes (~72 in the timing table) |
| Audience | Primary + secondary roles from the matrix |
| Proficiency | 3/5/7 codes from the matrix, per role, identical in student + instructor headers |
| Student guide | Objectives → key concepts (fields + 1–2 idea sections) → 3 walkthrough examples → hands-on exercise → 5 knowledge-check questions → summary → references |
| Instructor guide | Purpose, teaching points, pitfalls, timing, notes per section, exercise key (pseudo-queries), knowledge-check answers |
| Slides | ~17 slides: title, objectives, agenda, concepts, 3 examples, `uid` pivot if network logs, hunts, exercise, check, summary, next steps, optional quick-reference |
| Answers | Only in the instructor guide. No standalone `answer-key.md`. No quiz. |

Exercise pattern (engine modules): one-sentence summary of each example; two SIEM-style **pseudo-queries**; explain the `uid` pivot when the log has a `uid`.

Examples: one normal, two leads. Leads are not automatic incidents.

Voice: direct, instructional, short paragraphs, tables for fields. Do not lecture about decrypting traffic, writing Zeek scripts, or other later modules.

---

## 4. Teach at least the outline

- Outline knowledge bullets (`a`, `b`, `c`…) become the field/idea sections. None may be skipped.
- Outline tasks become the analysis exercise and the two pseudo-queries (or equivalent practice).
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
- [tracker.csv](tracker.csv) — add or update the row; guides/slides `Complete`; exercise/quiz as in the sibling (usually exercise `Not Started`, answer key `Complete` if answers are in the instructor guide)
- [tracker.md](tracker.md) — folder map row if this ID is new
- README numbering table in the repo root if this ID is new

Do not set tracker status to `Complete` for the module as a whole if that column exists as a single status — leave content at **Review** for the human. Use the per-artifact columns like the Zeek rows: student/instructor/slides complete, then tell the user it is ready to review.

---

## 6. Do not

- Generate all of cluster `3.1` when asked for `3.1` or `3.1.1`
- Skip an outline bullet because the matrix row is shorter
- Invent matrix IDs, outline headings, or proficiency codes
- Collapse or invent 3/5/7 codes (instructor and student headers must match the matrix)
- Treat combined.md `## 7` / `## 8` / `## 9` as real (those headings are gone; use `2.x` / `3.x` / `1.8`)
- Index sample IPs, `example.com`, or passing name-drops
- Put JA3-style depth in a survey module, or HTTP bodies in a TLS module
- Copy shared frameworks into a role folder
- Mark the module human-accepted (`Complete` on the whole package) — stop for review
- Write Gate 1 proposal files unless asked

---

## 7. When you finish

List the paths you wrote and the outline ↔ matrix map. Remind the reviewer to confirm: (1) every outline bullet/task is in the student guide, (2) Concepts taught matches the index, (3) status stays at review until they accept the lesson.
