# Todo

Do these first (course order and story):

- [x] Put section 0 (How a SOC can operate) in the training outline
- [x] Write the section 0 intro lesson: what a SOC is, how it can run, the jobs, and where they lightly overlap (one-sentence hand-offs; no fake DYA ticket system)
- [x] Write 0.1 What a SOC is (first small review cycle)
- [x] Write 0.2 Jobs in one sentence (first after 0.1; path is now 0.3)
- [x] Write 0.3 How work can move (after 0.2 is reviewed)
- [x] Write 0.4 Where the jobs lightly overlap (after 0.3 is reviewed)
- [x] Write 0.5 How this course is laid out (after 0.4 is reviewed; DYA / PRD highlighted)
- [x] Reorg `00-intro`: `0.1` is layout; shared hours taught before SOC; `00-shared` removed
- [x] Teach in this order (lesson IDs can stay as they are): intro → shared floor → SOC analyst → CTI → hunting → detection engineers
- [x] Revise 1.1.2 Process activity (first 1.x review; 0/4 voice; no lab)
- [x] Add 1.1.1 Endpoint activity map hour (bump process–image to 1.1.2–1.1.6)
- [x] Keep detections before alerts inside the SOC analyst block (current 1.3 then 1.4)
- [x] Add a detection-engineers section after the threat hunters section (outline 4.x; matrix/lessons later)
- [x] Write 4.x stay-in-lesson notes in generate-module.md
- [x] Write 4.1 What DE owns (first DE review cycle)
- [x] Write 4.2 Making a detection sound and meeting shop requirements
- [x] Write 4.3 Nominations from SOC, hunt, and CTI
- [x] Write 4.4 Tune requests from SOC
- [x] Write 4.5 Hunt and intel packages
- [x] Write 4.6 Detection lifecycle
- [x] Write 4.7 Sensor availability and performance
- [x] Write 4.8 Site-specific DE knowledge (4.8.1 + 4.8.2 lumped; obtain-and-follow)
- [x] Put the full incident flow in the companion story: SOC alert → triage → IR + leadership notify → RFI to intel → hunt package, block list to firewall/IA, and a request to write detections. Firewall/IA is a hand-off, not a new course unless we decide we want that track.
- [x] As we review and revise the outline, make the outline follow that same flow, so the companion story is a re-read of the outline as one combined story

Then:

- [x] Explore a fictional back story — an ongoing theme, like the Night Owl story and Harbor company already in the lessons
- [x] Review for chances to re-order things
- [x] Put a “when each fact appears” map in the story bible (alert vs notify vs CTI vs hunt vs DE)
- [x] Keep [docs/story-bible.md](story-bible.md) current as training develops
- [x] Decide leftover Harbor map items that do not fit a law firm (OT, payroll) — OT and payroll are not A12 plot; see story bible
- [ ] Rename Night Owl → Pink River Dolphin (PRD) and Harbor → Dixon, Yamada, & Associates (DYA) in the lessons
- [x] Write the companion story (see [companion-story/](companion-story/))
- [ ] Add common **initial access** material (malspam / phishing, CVE exploits, watering hole, SEO poisoning, drive-by download, and the like). Gate 1 first — do not invent IDs. Then develop it into the [companion story](companion-story/) (bible first, then the story; do not invent a second plot)
- [x] Shared floor in `00-intro`, taught before SOC: frameworks, tool survey, environment. Retired `1.7`, `1.8.2`–`1.8.5`. SOC ends at 1.5.
- [x] Rewrite `0.8` (00.08): why every role must understand infrastructure and signal flow. Do **not** invent a site card / Harbor architecture.
- [ ] Review everything and make sure it makes sense
- [ ] Check the reference links that are already there
- [ ] Look for places to add more reference links

## Companion story

Moved to [companion-story/](companion-story/). The nine-beat spine is in [companion-story/outline.md](companion-story/outline.md). The finished retelling is [companion-story/story.md](companion-story/story.md).

Later: fold common initial access (malspam / phishing, CVE exploits, watering hole, SEO poisoning, drive-by download) into the story after it is on the outline and in the [story bible](story-bible.md).
