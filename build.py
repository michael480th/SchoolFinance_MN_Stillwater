#!/usr/bin/env python3
"""
build.py — regenerate the Stillwater Schools Finance Project homepage.

The homepage (index.html) is a static "think tank" index over everything in
this repository:

  * Publications  — thought pieces authored as standalone HTML files in
                    publications/ (each carries <meta name="pub:*"> tags).
  * Collections   — the source-document and reference folders listed in
                    site.json (PDFs, notes, summaries).

Nothing here is magic: run `python3 build.py` after adding material and the
index rebuilds itself. No third-party dependencies — Python 3 standard
library only. The GitHub Pages workflow runs this automatically on push.

Usage:
    python3 build.py            # writes ./index.html
    python3 build.py --check    # rebuild and fail if index.html is stale
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "site.json"
OUT_PATH = ROOT / "index.html"
PUBLICATIONS_DIR = ROOT / "publications"

# Extensions served directly by GitHub Pages (linked relatively).
WEB_SERVED = {".pdf", ".html", ".htm", ".csv", ".xlsx", ".xls", ".png",
              ".jpg", ".jpeg", ".svg", ".json", ".txt"}
# Extensions we'd rather link to GitHub's rendered view.
GITHUB_RENDERED = {".md", ".markdown"}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def esc(value: str) -> str:
    return html.escape(value or "", quote=True)


def load_config() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def human_size(num_bytes: int) -> str:
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            if unit == "B":
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"


def humanize_filename(name: str) -> str:
    stem = os.path.splitext(name)[0]
    stem = stem.replace("Stillwater_ISD834_", "")
    stem = stem.replace("_", " ").replace("  ", " ").strip()
    return stem


def humanize_dirname(name: str, labels: dict) -> str:
    if name in labels:
        return labels[name]
    return name.replace("_", " ").strip()


def github_blob_url(repo: dict, rel_path: str) -> str:
    owner = repo.get("owner", "")
    name = repo.get("name", "")
    branch = repo.get("branch", "main")
    rel = rel_path.replace(os.sep, "/")
    return f"https://github.com/{owner}/{name}/blob/{branch}/{rel}"


def rel_url(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


# --------------------------------------------------------------------------- #
# Publications
# --------------------------------------------------------------------------- #
META_RE = re.compile(
    r'<meta\s+name=["\']pub:([\w-]+)["\']\s+content=["\'](.*?)["\']\s*/?>',
    re.IGNORECASE | re.DOTALL,
)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def discover_publications() -> list[dict]:
    if not PUBLICATIONS_DIR.is_dir():
        return []
    pubs = []
    for path in sorted(PUBLICATIONS_DIR.glob("*.html")):
        if path.name.startswith("_") or path.name == "index.html":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        meta = {k.lower(): html.unescape(v.strip())
                for k, v in META_RE.findall(text)}
        title = meta.get("title")
        if not title:
            m = TITLE_RE.search(text)
            title = m.group(1).strip() if m else humanize_filename(path.name)
        pubs.append({
            "title": title,
            "date": meta.get("date", ""),
            "summary": meta.get("summary", ""),
            "category": meta.get("category", "Analysis"),
            "author": meta.get("author", ""),
            "reading_time": meta.get("reading_time", ""),
            "featured": meta.get("featured", "").lower() in ("1", "true", "yes"),
            "url": rel_url(path),
        })
    # Newest first; undated items sort last.
    pubs.sort(key=lambda p: (p["date"] or "0000-00-00"), reverse=True)
    return pubs


def format_date(iso: str) -> str:
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", iso or "")
    if not m:
        return iso or ""
    months = ["", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return f"{months[mo]} {d}, {y}"


def render_publications(pubs: list[dict]) -> str:
    if not pubs:
        return (
            '<p class="empty-note">No thought pieces have been published yet. '
            'New pieces added to the <code>publications/</code> folder will '
            'appear here automatically the next time the site is built.</p>'
        )
    cards = []
    for i, p in enumerate(pubs):
        featured = p["featured"] or (i == 0 and len(pubs) > 1)
        classes = "card featured" if featured else "card"
        foot_bits = []
        if p["date"]:
            foot_bits.append(esc(format_date(p["date"])))
        if p["reading_time"]:
            foot_bits.append(esc(p["reading_time"]))
        foot_left = " · ".join(foot_bits) or "&nbsp;"
        cards.append(f"""        <article class="{classes}">
          <span class="tag">{esc(p['category'])}</span>
          <h3><a href="{esc(p['url'])}">{esc(p['title'])}</a></h3>
          <p class="dek">{esc(p['summary'])}</p>
          <div class="card-foot">
            <span>{foot_left}</span>
            <a class="read" href="{esc(p['url'])}">Read &rarr;</a>
          </div>
        </article>""")
    return '      <div class="cards">\n' + "\n".join(cards) + "\n      </div>"


# --------------------------------------------------------------------------- #
# Document collections
# --------------------------------------------------------------------------- #
def collect_files(coll_path: Path) -> dict[str, list[Path]]:
    """Return {group_label_dir: [files]} for one collection directory."""
    groups: dict[str, list[Path]] = {}
    if not coll_path.is_dir():
        return groups
    for dirpath, dirnames, filenames in os.walk(coll_path):
        dirnames.sort()
        rel_dir = os.path.relpath(dirpath, coll_path)
        key = "" if rel_dir == "." else rel_dir.split(os.sep)[0]
        for fn in sorted(filenames):
            if fn.startswith(".") or fn == ".nojekyll":
                continue
            groups.setdefault(key, []).append(Path(dirpath) / fn)
    return groups


def render_collection(coll: dict, config: dict) -> str:
    coll_path = ROOT / coll["path"]
    groups = collect_files(coll_path)
    labels = config.get("labels", {})
    repo = config.get("repo", {})

    if not groups:
        body = ('<p class="empty-note">No documents in this collection yet.</p>')
    else:
        blocks = []
        # Root-level files first, then named sub-groups alphabetically.
        ordered_keys = ([""] if "" in groups else []) + sorted(
            k for k in groups if k)
        for key in ordered_keys:
            files = groups[key]
            heading = (humanize_dirname(key, labels) if key
                       else "Documents")
            items = []
            for f in files:
                ext = f.suffix.lower()
                badge = ext.lstrip(".") or "file"
                badge_class = badge if badge in (
                    "pdf", "md", "html", "csv", "xlsx") else ""
                if ext in GITHUB_RENDERED:
                    href = github_blob_url(repo, rel_url(f))
                    target = ' target="_blank" rel="noopener"'
                else:
                    href = esc(rel_url(f))
                    target = ""
                size = human_size(f.stat().st_size)
                items.append(
                    f"""          <li class="doc-item">
            <span class="badge {badge_class}">{esc(badge.upper())}</span>
            <span class="doc-name"><a href="{href}"{target}>"""
                    f"""{esc(humanize_filename(f.name))}</a></span>
            <span class="doc-size">{esc(size)}</span>
          </li>""")
            blocks.append(
                f"""        <div class="doc-group">
          <h4>{esc(heading)}</h4>
          <ul class="doc-list">
{chr(10).join(items)}
          </ul>
        </div>""")
        body = "\n".join(blocks)

    return f"""    <section class="block" id="{esc(section_id(coll['title']))}">
      <div class="wrap split">
        <div class="aside">
          <p class="kicker">Collection</p>
          <div class="section-head" style="margin-bottom:0">
            <h2>{esc(coll['title'])}</h2>
          </div>
          <p>{esc(coll.get('blurb',''))}</p>
        </div>
        <div>
{body}
        </div>
      </div>
    </section>"""


def section_id(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


# --------------------------------------------------------------------------- #
# Page assembly
# --------------------------------------------------------------------------- #
def render_stats(stats: list[dict]) -> str:
    tiles = []
    for s in stats:
        cls = "stat alert" if s.get("tone") == "alert" else "stat"
        note = f'<div class="note">{esc(s["note"])}</div>' if s.get("note") else ""
        tiles.append(f"""        <div class="{cls}">
          <div class="num">{esc(s['num'])}</div>
          <div class="lab">{esc(s['lab'])}</div>
          {note}
        </div>""")
    return '      <div class="stats">\n' + "\n".join(tiles) + "\n      </div>"


def render_page(config: dict) -> str:
    site = config["site"]
    pubs = discover_publications()
    stats_html = render_stats(config.get("stats", []))
    pubs_html = render_publications(pubs)
    collections_html = "\n".join(
        render_collection(c, config) for c in config.get("collections", []))
    year = "2026"

    nav_links = [
        ("Publications", "#publications"),
        ("Analysis", "#analysis-summaries"),
        ("Source Library", "#source-document-library"),
        ("Reference", "#reference-methodology"),
        ("About", "#about"),
    ]
    nav_html = "\n".join(
        f'        <a href="{href}">{esc(label)}</a>'
        for label, href in nav_links)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(site['name'])} &middot; {esc(site['sub'])}</title>
  <meta name="description" content="{esc(site['tagline'])}">
  <meta property="og:title" content="{esc(site['name'])}">
  <meta property="og:description" content="{esc(site['tagline'])}">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="assets/site.css">
  <!-- Generated by build.py — do not edit index.html by hand. Run: python3 build.py -->
</head>
<body>
  <a class="skip-link" href="#publications">Skip to content</a>

  <header class="masthead">
    <div class="wrap">
      <a class="brand" href="./index.html">
        <span class="seal">{esc(site.get('seal','834'))}</span>
        <span class="brand-text">
          <span class="brand-name">{esc(site['name'])}</span><br>
          <span class="brand-sub">{esc(site['sub'])}</span>
        </span>
      </a>
      <nav class="nav" aria-label="Primary">
{nav_html}
      </nav>
    </div>
  </header>

  <div class="hero">
    <div class="wrap">
      <p class="kicker">Stillwater Area Public Schools &middot; ISD 834 &middot; Washington County, MN</p>
      <h1>{esc(site['hero_title'])}</h1>
      <p class="lede">{esc(site['hero_lede'])}</p>
      <p class="meta-line">{esc(site['as_of'])}</p>
{stats_html}
    </div>
  </div>

  <main>
    <section class="block" id="publications">
      <div class="wrap">
        <div class="section-head">
          <p class="kicker">Thought pieces</p>
          <h2>Publications</h2>
          <p>Short, sourced analyses of the district's finances. Each piece is a
             standalone briefing you can read, print, or share.</p>
        </div>
{pubs_html}
      </div>
    </section>

{collections_html}

    <section class="block" id="about">
      <div class="wrap">
        <div class="mission">
          <p class="kicker">About this project</p>
          <h2>What we do &mdash; and what we are not</h2>
          <p>The Stillwater Schools Finance Project is an independent, nonpartisan
             effort to make the finances of Independent School District No. 834
             legible to the people who fund and depend on them. We work only from
             public records: audited financial reports, the district's official
             budget publications, board packets, and state and federal finance
             data.</p>
          <p>Every figure we publish is traceable to a primary source, and the
             underlying documents live in this repository so anyone can check our
             work. As new audits, budgets, and levy filings are released, we add
             them here and update the analysis.</p>
          <p><strong style="color:#fff">This is not an official publication of
             Stillwater Area Public Schools.</strong> We are not affiliated with,
             endorsed by, or speaking for the district or its Board of Education.</p>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-foot" id="colophon">
    <div class="wrap">
      <div class="foot-top">
        <div>
          <strong>{esc(site['name'])}</strong><br>
          {esc(site['tagline'])}
        </div>
        <div>
          <a href="https://github.com/{esc(config['repo'].get('owner',''))}/{esc(config['repo'].get('name',''))}">Repository &amp; source data &rarr;</a>
        </div>
      </div>
      <p class="disclaimer">Independent research for informational purposes only;
        not an official district document and not financial, investment, or legal
        advice. Figures are drawn from audited statements and official budget
        publications and may differ from other tabulations due to the treatment of
        interfund transfers and reporting timing. &copy; {year} {esc(site['name'])}.
        This page is generated automatically from the contents of the repository.</p>
    </div>
  </footer>
</body>
</html>
"""


# --------------------------------------------------------------------------- #
# Entry point
# --------------------------------------------------------------------------- #
def main(argv: list[str]) -> int:
    config = load_config()
    page = render_page(config)

    if "--check" in argv:
        current = OUT_PATH.read_text(encoding="utf-8") if OUT_PATH.exists() else ""
        if current != page:
            print("index.html is stale — run: python3 build.py", file=sys.stderr)
            return 1
        print("index.html is up to date.")
        return 0

    OUT_PATH.write_text(page, encoding="utf-8")
    pubs = discover_publications()
    print(f"Wrote {OUT_PATH.relative_to(ROOT)} "
          f"({len(pubs)} publication(s), "
          f"{len(config.get('collections', []))} collection(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
