# Introduction to Computing (Workbench version)

**Site:** https://adci-perth.github.io/intro-to-computing-workbench/

The website version of ADCI's six-week, browser-only beginner course *Introduction to Computing*, built with [The Carpentries Workbench](https://carpentries.github.io/sandpaper-docs/). It is a staging step before the course goes into Canvas.

The course content is maintained in the course folder, `intro-to-computing`. This folder holds the converted lesson. **It contains learner material only:** model answers, quiz pools and the tutor guide stay in the course folder.

## Structure

| Folder | What is in it |
|---|---|
| `episodes/` | One episode per week (`week-1.md` to `week-6.md`). Each holds the week overview, its sections (1.1, 1.2 ...), the Concepts Bridge and the practice task as level-2 headings, which the menu shows as sub-items. |
| `episodes/files/` | Practice-task worksheets and files (`week-N/`) and the Week 4 LMC program (`lmc/`) |
| `episodes/data/` | `course-files.zip`, every learner file in one download |
| `learners/` | Setup and glossary pages |
| `instructors/` | Instructor notes |
| `profiles/` | Learner profiles |
| `scripts/` | `convert_from_course.py` and `wb_meta.py`, which rebuild the episodes from the course folder |

## Updating from the course folder

With both folders side by side:

```bash
python scripts/convert_from_course.py ../intro-to-computing .
```

This rewrites the week episodes and their files. It prints any link it could not map, and warns if a tutor-only file is mentioned. Other pages (home, setup, glossary, instructor notes, profiles, `config.yaml`) are edited by hand. If you add, remove or rename a section or a practice file, update `scripts/wb_meta.py`.

## Building the site locally

You need R, the Workbench packages and pandoc:

```r
install.packages(c("sandpaper", "varnish", "pegboard", "tinkr"),
  repos = c("https://carpentries.r-universe.dev/", getOption("repos")))
sandpaper::build_lesson()        # builds the site into site/docs and opens a preview
sandpaper::validate_lesson()     # checks links, fenced divs and headings
```

## Before publishing

- The site is published from the `gh-pages` branch by the Workbench GitHub Actions in `.github/workflows` (copied from the Intro to Programming Workbench). Every push to `main` rebuilds it.
- Confirm the licence (see `LICENSE.md`).
- Replace the placeholder `contact` in `config.yaml`, and add the code of conduct links in `CODE_OF_CONDUCT.md`.
- The ADCI logo comes from ADCI's fork of the theme, `ADCI-Perth/varnish`, pinned in `config.yaml` (as in the Intro to Programming Workbench).
