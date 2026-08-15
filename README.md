# Training Plan

Curriculum for SOC Analysts, Threat Hunters, and CTI Analysts. Content is organized so each teaching module is one folder, grouped by role and unit.

## Layout

```
docs/
  outlines/training-outlines.md   # source list of knowledge and task items
  proficiency-legend.md           # CFETP-style 3/5/7 levels and codes
  matrices/                       # combined + per-role proficiency matrices
  tracker.csv                     # module status (edit this)
  tracker.md                      # status legend and folder mapping
templates/                        # copy these when starting a new module
modules/
  01-soc/<unit>/<module>/
  02-hunter/<unit>/<module>/
  03-cti/<unit>/<module>/
  shared/frameworks/              # write once (MITRE, Diamond, Kill Chain)
labs/                             # reusable sample logs and PCAP
```

Do not put more than three path levels under `modules/` (`role / unit / module`).

## Numbering

Two ID systems exist. Do not mix them in filenames.

| System | Example | Use for |
|--------|---------|---------|
| **Matrix item** (canonical) | `1.2.2.1`, `1.2.2.2` | Proficiency tracking, mapped items in guides |
| **Outline heading** | `1.2.2` Conn knowledge, `1.2.3` Conn tasks | Curriculum design only |

A **module** is a teaching unit. It may cover one outline knowledge item plus its matching tasks. Folder names are not dotted IDs:

| Folder | Matrix items | Outline headings |
|--------|----------------|------------------|
| `modules/01-soc/02-zeek/01-concepts` | `1.2.1.1` | `1.2.1` |
| `modules/01-soc/02-zeek/02-conn-engine` | `1.2.2.1`–`1.2.2.3` | `1.2.2` + `1.2.3` |
| `modules/01-soc/02-zeek/03-dns-engine` | `1.2.3.1`–`1.2.3.3` | `1.2.4` + `1.2.5` |

Record the mapping in each module `README.md`.

## Adding a module

1. Create `modules/<role>/<unit>/<nn-short-name>/`.
2. Copy files from `templates/` and rename them to `instructor-guide.md`, `student-guide.md`, `slides.md`, and `answer-key.md` as needed.
3. Put lesson-specific screenshots in that module's `assets/` folder.
4. Put reusable logs or PCAP in `labs/`.
5. Add a row to [docs/tracker.csv](docs/tracker.csv).

Shared topics (frameworks, cross-role primers) go under `modules/shared/`, not copied into each role.
