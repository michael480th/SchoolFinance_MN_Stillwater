# Stillwater Schools Finance Project

Independent, nonpartisan research on the finances of **Stillwater Area Public
Schools — Independent School District No. 834** (Washington County, Minnesota).

This repository is both the archive and the website. It stores the primary
source documents and analysis, and it publishes a static "think tank" homepage
and a series of thought pieces via **GitHub Pages**.

> **Live site:** the homepage is `index.html`, deployed to GitHub Pages.
> It is _generated_ — do not edit `index.html` by hand.

---

## How the site is built

The homepage is produced by [`build.py`](build.py), a small, dependency-free
Python 3 script. It scans this repository and regenerates `index.html`:

- **Publications** — every `*.html` file in [`publications/`](publications/)
  (thought pieces) becomes a card, newest first.
- **Collections** — the folders listed in [`site.json`](site.json)
  (source documents, analysis, reference notes) become browsable document lists.
- **Headline stats** and site text come from `site.json`.

To rebuild after adding material:

```bash
python3 build.py
```

That's it — no build tools, no `npm install`, standard library only. The
[GitHub Pages workflow](.github/workflows/pages.yml) also runs `build.py`
automatically on every push, so the live site rebuilds itself.

Check whether the committed `index.html` is up to date (used in CI):

```bash
python3 build.py --check
```

---

## Adding a new thought piece

1. Copy the template:

   ```bash
   cp publications/_template.html publications/2026-08-15-my-slug.html
   ```

2. Fill in the metadata block at the top (this drives the homepage card):

   ```html
   <meta name="pub:title"        content="Your headline">
   <meta name="pub:date"         content="2026-08-15">
   <meta name="pub:category"     content="Fiscal Analysis">
   <meta name="pub:summary"      content="One or two sentence blurb.">
   <meta name="pub:reading_time" content="6 min read">
   <!-- optional: <meta name="pub:featured" content="true"> -->
   ```

3. Write the article inside `<div class="a-body"> … </div>`.
4. Rebuild: `python3 build.py`.
5. Commit and push. The new piece appears on the homepage automatically.

Files whose names start with `_` (like `_template.html`) are ignored by the
builder.

## Adding source documents

Drop files into the relevant folder and rebuild:

- `01_Source_Documents/` — audited reports and official budget publications
  (grouped by sub-folder, e.g. `ACFRs/`, `Budget_FY2026-27/`).
- `02_Summaries_and_Analysis/` — the project's own consolidated summaries.
- `03_Reference_Notes/` — methodology and data-source notes (Markdown).

PDFs, spreadsheets, and HTML are linked directly (served by Pages); Markdown
notes link to their rendered view on GitHub. To add a whole new collection or
change section blurbs, edit the `collections` list in `site.json`.

## Updating the headline numbers and trend chart

- **Hero stat tiles** live in the `stats` array in `site.json`. Set
  `"tone": "alert"` on a stat to render it in caution red.
- **The "Data & Trends" chart** (the per-pupil line chart on the homepage) is
  driven by the `trends` block in `site.json`: edit `x` (the year labels),
  each series' `values`, the `highlights` bullets, and the `source` line. The
  builder redraws the SVG and the data table from those numbers — no chart code
  to touch. Add a third series by appending another `{name, color, values}`
  object (use a validated, colorblind-safe hue).

Update these when a new audit, budget, or Report Card release lands, then rebuild.

> Editor/OS backup artifacts (`* - Copy.md`, `~$*`, `.DS_Store`, `Thumbs.db`)
> are automatically skipped, so they never show up in the document lists.

---

## Repository layout

```
index.html                     ← generated homepage (do not edit by hand)
build.py                       ← site generator (python3 build.py)
site.json                      ← site config: name, stats, collections, repo
assets/site.css                ← shared stylesheet (homepage + publications)
publications/
  _template.html               ← starter for new thought pieces
  2026-07-01-...html           ← published pieces
01_Source_Documents/           ← primary audited & budget documents
02_Summaries_and_Analysis/     ← consolidated project summaries
03_Reference_Notes/            ← methodology & data-source notes
.github/workflows/pages.yml    ← builds & deploys to GitHub Pages on push
.nojekyll                      ← serve files as-is (no Jekyll processing)
```

## Enabling GitHub Pages

In the repository's **Settings → Pages**, set **Source** to
**GitHub Actions**. The included workflow builds `index.html` and deploys the
whole repository as the site on each push to the configured branch.

---

*Independent research for informational purposes only. Not affiliated with,
endorsed by, or speaking for Stillwater Area Public Schools or its Board of
Education. Figures are drawn from audited statements and official budget
publications.*
