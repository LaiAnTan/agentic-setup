#!/usr/bin/env python3
"""Build one artifact page from a design markdown file.

    python3 build_artifact.py docs/designs/2026-10-22-payout-v2.md [-o out.html]

The markdown is the only source; never edit the output by hand. The page is
written for the Artifact tool, which adds the doctype, head and body and renders
<pre class="mermaid"> blocks itself, so this script emits neither. preview.py
adds both for local viewing.
"""
import argparse
import html
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Needs the markdown package: python3 -m pip install markdown")

MERMAID_FENCE = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.M | re.S)
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+\.)\s")
TABLE_ROW = re.compile(r"^\s*\|")

STYLE = """
/* Layout: sticky contents sidebar beside a single reading column; sidebar stacks on top on phones. */
:root {
  --bg: #fbfbf9; --panel: #f1f2ee; --fg: #1d2321; --muted: #5d6763;
  --rule: #d9ddd7; --accent: #2f6f5e; --code-bg: #eef0eb;
  --body: "IBM Plex Sans", system-ui, sans-serif;
  --display: "IBM Plex Sans Condensed", "IBM Plex Sans", system-ui, sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #141817; --panel: #1b201f; --fg: #e4e8e5; --muted: #9aa5a0;
  --rule: #2c3330; --accent: #7cc4ad; --code-bg: #1f2523; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #141817; --panel: #1b201f; --fg: #e4e8e5; --muted: #9aa5a0;
  --rule: #2c3330; --accent: #7cc4ad; --code-bg: #1f2523; color-scheme: dark }

body { background: var(--bg); color: var(--fg); font: 16px/1.6 var(--body);
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.page { display: grid; grid-template-columns: 15rem minmax(0, 1fr); gap: 3rem;
  max-width: 72rem; margin: 0 auto; padding-block: 2.5rem 4rem; }
nav.toc { position: sticky; top: calc(env(safe-area-inset-top, 0px) + 1.5rem); align-self: start;
  max-height: calc(100vh - 3rem); overflow-y: auto; font-size: 0.875rem; }
nav.toc .label { font: 600 0.75rem var(--body); letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--muted); margin: 0 0 0.75rem; }
nav.toc ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 0.35rem; }
nav.toc ul ul { padding-left: 0.9rem; margin-top: 0.35rem; }
nav.toc a { color: var(--muted); text-decoration: none; }
nav.toc a:hover, nav.toc a:focus-visible { color: var(--accent); }
main { min-width: 0; max-width: 46rem; }
h1, h2, h3 { font-family: var(--display); line-height: 1.2; text-wrap: balance; scroll-margin-top: 1.5rem; }
h1 { font-size: 2.1rem; margin: 0 0 1.5rem; }
h2 { font-size: 1.5rem; margin: 2.75rem 0 0.75rem; padding-top: 1.25rem; border-top: 1px solid var(--rule); }
h3 { font-size: 1.15rem; margin: 1.75rem 0 0.5rem; }
p, li { max-width: 65ch; }
a { color: var(--accent); }
a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
code { font: 0.875em var(--mono); background: var(--code-bg); padding: 0.1em 0.3em; border-radius: 3px; }
pre { background: var(--code-bg); padding: 0.9rem 1rem; border-radius: 4px; overflow-x: auto; }
pre code { background: none; padding: 0; }
pre.mermaid { background: var(--panel); text-align: center; }
.table-wrap { overflow-x: auto; margin: 1rem 0; }
table { border-collapse: collapse; font-size: 0.925rem; font-variant-numeric: tabular-nums; }
th, td { border-bottom: 1px solid var(--rule); padding: 0.5rem 0.75rem; text-align: left; vertical-align: top; }
th { font-weight: 600; color: var(--muted); }
blockquote { margin: 1rem 0; padding-left: 1rem; border-left: 3px solid var(--rule); color: var(--muted); }
input[type=checkbox] { margin-right: 0.4rem; }
@media (max-width: 760px) {
  .page { grid-template-columns: minmax(0, 1fr); gap: 1.5rem; padding-block: 1.5rem 3rem; }
  nav.toc { position: static; max-height: none; padding-bottom: 1rem; border-bottom: 1px solid var(--rule); }
  h1 { font-size: 1.7rem; }
}
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono'
         '&family=IBM+Plex+Sans+Condensed:wght@600&family=IBM+Plex+Sans:wght@400;600&display=swap">')


def stash_mermaid(text):
    """Swap mermaid fences for placeholders so markdown doesn't touch them."""
    blocks = []

    def keep(match):
        blocks.append(match.group(1))
        return f"\n\nMERMAIDBLOCK{len(blocks) - 1}\n\n"

    return MERMAID_FENCE.sub(keep, text), blocks


def separate_lists(text):
    """Python-Markdown only starts a list or table after a blank line; design files often put
    one straight under a label like "**Terms:**". Add the blank line, outside code fences."""
    out, in_fence, prev = [], False, ""
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and prev.strip() and any(
            p.match(line) and not p.match(prev) for p in (LIST_ITEM, TABLE_ROW)
        ):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def toc_html(tokens):
    """Nested list from ## and ### headings (the h1 is the page title)."""
    items = []
    for tok in tokens:
        if tok["level"] == 1:
            items.extend(tok["children"])
        elif tok["level"] == 2:
            items.append(tok)
    out = ["<ul>"]
    for h2 in items:
        out.append(f'<li><a href="#{h2["id"]}">{h2["name"]}</a>')
        subs = [c for c in h2["children"] if c["level"] == 3]
        if subs:
            out.append("<ul>" + "".join(f'<li><a href="#{c["id"]}">{c["name"]}</a></li>' for c in subs) + "</ul>")
        out.append("</li>")
    out.append("</ul>")
    return "".join(out)


def build(source: Path) -> str:
    text, mermaid_blocks = stash_mermaid(separate_lists(source.read_text(encoding="utf-8")))
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "sane_lists", "toc"],
        extension_configs={"toc": {"toc_depth": "1-3"}},
    )
    body = md.convert(text)
    for i, block in enumerate(mermaid_blocks):
        body = body.replace(f"<p>MERMAIDBLOCK{i}</p>", f'<pre class="mermaid">{html.escape(block.strip())}</pre>')
    body = re.sub(r"<table>(.*?)</table>", r'<div class="table-wrap"><table>\1</table></div>', body, flags=re.S)
    body = body.replace("<li>[ ] ", '<li><input type="checkbox" disabled> ')
    body = body.replace("<li>[x] ", '<li><input type="checkbox" checked disabled> ')

    h1 = re.search(r"^# (.+)$", text, re.M)
    title = h1.group(1).strip() if h1 else source.stem
    return (
        f"<title>{html.escape(title)}</title>\n"
        '<meta name="claude:viewport-fit-sides" content="cover">\n'
        f"{FONTS}\n<style>{STYLE}</style>\n"
        '<div class="page">\n'
        f'<nav class="toc" aria-label="Contents"><p class="label">Contents</p>{toc_html(md.toc_tokens)}</nav>\n'
        f"<main>\n{body}\n</main>\n</div>\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", type=Path, help="design markdown file")
    parser.add_argument("-o", "--out", type=Path, help="output file (default: next to the source, .html)")
    args = parser.parse_args()
    out = args.out or args.source.with_suffix(".html")
    out.write_text(build(args.source), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
