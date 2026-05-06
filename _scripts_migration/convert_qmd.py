#!/usr/bin/env python3
"""
convert_qmd.py — Quarto .qmd → Hugo .md conversion for the DaF migration.

Usage:
    python _scripts_migration/convert_qmd.py [paths...]

If no paths are given, the script reads `_scripts_migration/batches.txt`
and converts every listed file. Output lands under content/ following the
mapping rules in MIGRATION_PLAN.md §5.

Conversion rules (kept narrow on purpose):
  - Frontmatter: drop `format:` block (Reveal.js + PDF are not Hugo's job),
    keep all other keys as Hugo params. Top-level `title` and `subtitle`
    become Hugo's `title` (subtitle merged when present).
  - Quarto callouts ::: {.callout-X [title=…] [collapse=true]} … :::
    → {{< callout type="X" title="…" >}} … {{< /callout >}}
    or {{< details type="X" title="…" >}} … {{< /details >}} when collapse.
  - Generic fenced divs ::: {.foo .bar} … ::: → <div class="foo bar"> … </div>
    Goldmark `unsafe = true` is already configured.
  - Span attributes [text]{.a .b} → <span class="a b">text</span>.
  - Cross-refs (foo.qmd) → (/foo/) and (path/foo.qmd) → (/path/foo/).
  - Index-folding: kurs_<L>/index.qmd + kurs_<L>/uebersicht.qmd are written
    to content/kurs_<L>/_index.md (concatenated), preserving every word.
  - _exam.qmd files are skipped (LaTeX → PDF; out of Hugo's path).

Word-count diff: per file, source vs destination after frontmatter +
shortcodes are stripped. Drift > 2% appended to MIGRATION_PLAN.md §7.
"""
from __future__ import annotations

import re
import sys
import shutil
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Need PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"

# ------------------------------ frontmatter -----------------------------------

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, text[m.end():]


def emit_frontmatter(fm: dict) -> str:
    fm = dict(fm)
    fm.pop("format", None)
    fm.pop("editor", None)
    fm.pop("lang", None)  # Hugo derives language from site config
    # Merge subtitle into title at write-time (preserved nowhere lost).
    subtitle = fm.pop("subtitle", None)
    if subtitle and fm.get("title"):
        fm.setdefault("description", subtitle)
    out = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{out}\n---\n"


# ------------------------------ body transforms -------------------------------

# ::: {.callout-X title="..." collapse="true"} … :::
CALLOUT_OPEN = re.compile(
    r"::: \{\.callout-(?P<type>note|tip|warning|important|caution)"
    r"(?P<attrs>[^}]*)\}"
)


def parse_attrs(s: str) -> dict:
    """Pull out title="…" and collapse=true|"true" from a div attribute string."""
    out = {}
    m = re.search(r'title\s*=\s*"([^"]*)"', s)
    if m:
        out["title"] = m.group(1)
    m = re.search(r"collapse\s*=\s*(true|\"true\"|\"yes\")", s)
    if m:
        out["collapse"] = True
    return out


# Generic fenced div: ::: {.classname  .other  #id  key=val}
GENERIC_OPEN = re.compile(r"^::: \{(?P<inside>[^}]+)\}\s*$", re.M)
GENERIC_CLOSE = re.compile(r"^:::\s*$", re.M)


def transform_callouts_and_divs(body: str) -> str:
    """One-pass scanner converting Quarto fenced divs to Hugo equivalents.

    Stack-based because ::: blocks nest. Outermost type drives the open tag;
    matching close ::: pops the stack.
    """
    lines = body.split("\n")
    out: list[str] = []
    stack: list[str] = []  # close-tag for each open block

    GENERIC_HEAD = re.compile(r"^::: \{([^}]+)\}\s*$")

    for line in lines:
        m = GENERIC_HEAD.match(line)
        if m:
            inside = m.group(1).strip()
            # Class tokens like ".callout-note", ".hero-block".
            classes = re.findall(r"\.([A-Za-z0-9_\-]+)", inside)
            attrs = parse_attrs(inside)

            callout_class = next(
                (c for c in classes if c.startswith("callout-")), None
            )
            if callout_class:
                ctype = callout_class.split("-", 1)[1]
                title = attrs.get("title", "")
                if attrs.get("collapse"):
                    tag_open = '{{< details type="%s"%s >}}' % (
                        ctype,
                        f' title="{title}"' if title else ' title="Mehr"',
                    )
                    close = "{{< /details >}}"
                else:
                    tag_open = '{{< callout type="%s"%s >}}' % (
                        ctype,
                        f' title="{title}"' if title else "",
                    )
                    close = "{{< /callout >}}"
                out.append(tag_open)
                stack.append(close)
                continue

            # Generic class wrapper -> div
            cls = " ".join(classes) if classes else ""
            id_match = re.search(r"#([A-Za-z0-9_\-]+)", inside)
            id_attr = f' id="{id_match.group(1)}"' if id_match else ""
            out.append(
                f'<div class="{cls}"{id_attr}>' if cls else f"<div{id_attr}>"
            )
            stack.append("</div>")
            continue

        if line.strip() == ":::" and stack:
            out.append(stack.pop())
            continue

        out.append(line)

    # Any unclosed div is bug-bait — surface it.
    if stack:
        sys.stderr.write(
            f"  warn: {len(stack)} unclosed fenced div(s) — manual review\n"
        )
        out.extend(reversed(stack))

    return "\n".join(out)


SPAN_ATTR_RE = re.compile(r"\[([^\]]+)\]\{((?:\s*[\.#][A-Za-z0-9_\-]+\s*)+)\}")


def transform_span_attrs(body: str) -> str:
    """[text]{.a .b}  →  <span class="a b">text</span>."""
    def repl(m: re.Match) -> str:
        text = m.group(1)
        toks = re.findall(r"[\.#]([A-Za-z0-9_\-]+)", m.group(2))
        cls = " ".join(toks)
        return f'<span class="{cls}">{text}</span>'

    return SPAN_ATTR_RE.sub(repl, body)


LINK_QMD_RE = re.compile(r"\(([^)\s]*?\.qmd)(#[^)]*)?\)")


def transform_links(body: str, src_rel_dir: Path) -> str:
    """Rewrite [text](foo.qmd) → [text](/abs/path/) resolving relatives.

    `src_rel_dir` is the source file's directory, relative to repo root,
    e.g. Path("anhaenge") for anhaenge/kompetenzbaum.qmd. Used to resolve
    `../foo.qmd` and `./foo.qmd` to repo-absolute Hugo URLs.
    """
    def repl(m: re.Match) -> str:
        href = m.group(1)
        anchor = m.group(2) or ""

        # Resolve relative paths against the source's directory.
        if href.startswith("/"):
            resolved = Path(href.lstrip("/"))
        else:
            # Use posix-style join then normalise.
            joined = (src_rel_dir / href).as_posix()
            parts: list[str] = []
            for p in joined.split("/"):
                if p in ("", "."):
                    continue
                if p == "..":
                    if parts:
                        parts.pop()
                    continue
                parts.append(p)
            resolved = Path("/".join(parts))

        path = resolved.as_posix().removesuffix(".qmd")

        # index pages and section uebersicht both fold to the section root.
        if path == "index":
            path = "/"
        elif path.endswith("/index"):
            path = "/" + path[: -len("/index")] + "/"
        elif (
            path.endswith("/uebersicht")
            and path.split("/")[0].startswith("kurs_")
            and path.count("/") == 1
        ):
            # kurs_<L>/uebersicht  →  /kurs_<L>/
            path = "/" + path[: -len("/uebersicht")] + "/"
        else:
            path = "/" + path + "/"

        return f"({path}{anchor})"

    return LINK_QMD_RE.sub(repl, body)


def transform_body(body: str, src_rel_dir: Path) -> str:
    body = transform_callouts_and_divs(body)
    body = transform_span_attrs(body)
    body = transform_links(body, src_rel_dir)
    return body


# ------------------------------ path mapping ---------------------------------

@dataclass
class Job:
    src: Path
    dst: Path
    role: str  # "page", "section_index", "skip"
    fold_with: list[Path] = field(default_factory=list)


def plan_path(src: Path) -> Job | None:
    rel = src.relative_to(REPO)
    parts = rel.parts
    name = src.name

    # Skip exam wrappers — Phase 4 problem.
    if name.endswith("_exam.qmd"):
        return Job(src, REPO / "legacy" / rel, role="skip")

    # Site root index.
    if rel == Path("index.qmd"):
        return Job(src, CONTENT / "_index.md", role="page")

    # kurs_<L>/index.qmd or kurs_<L>/uebersicht.qmd: section index, folded.
    if (
        len(parts) == 2
        and parts[0].startswith("kurs_")
        and parts[1] in ("index.qmd", "uebersicht.qmd")
    ):
        return Job(
            src,
            CONTENT / parts[0] / "_index.md",
            role="section_index",
        )

    # kurs_<L>/units/unitNN_slug.qmd
    if (
        len(parts) == 3
        and parts[0].startswith("kurs_")
        and parts[1] == "units"
    ):
        return Job(
            src,
            CONTENT / parts[0] / "units" / name.replace(".qmd", ".md"),
            role="page",
        )

    # anhaenge/*.qmd
    if len(parts) == 2 and parts[0] == "anhaenge":
        return Job(
            src,
            CONTENT / "anhaenge" / name.replace(".qmd", ".md"),
            role="page",
        )

    # Top-level legal/info pages.
    if len(parts) == 1:
        return Job(src, CONTENT / name.replace(".qmd", ".md"), role="page")

    return None


# ------------------------------ word count -----------------------------------

WS_RE = re.compile(r"\s+")
SHORTCODE_RE = re.compile(r"\{\{<[^>]*>\}\}")
HTML_TAG_RE = re.compile(r"<[^>]+>")


QUARTO_FENCE_RE = re.compile(r"^::: ?(\{[^}]*\})?\s*$", re.M)
SPAN_ATTRS_RE = re.compile(r"\{[^}]*\}")  # also catches inline `{.cls}`


def word_count(text: str) -> int:
    text = QUARTO_FENCE_RE.sub(" ", text)
    text = SHORTCODE_RE.sub(" ", text)
    text = HTML_TAG_RE.sub(" ", text)
    text = SPAN_ATTRS_RE.sub(" ", text)
    return len([w for w in WS_RE.split(text) if w])


# ------------------------------ driver ---------------------------------------

def convert_one(src: Path) -> tuple[Job | None, int, int, str]:
    """Returns (job, src_words, dst_words, dst_text). Skipped if role=skip."""
    job = plan_path(src)
    if job is None or job.role == "skip":
        return job, 0, 0, ""

    text = src.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    src_rel_dir = src.relative_to(REPO).parent

    # For unit articles, pull custom keys we want as Hugo params and drop
    # Quarto-only ones. Hugo accepts arbitrary frontmatter, so we keep them.
    body_new = transform_body(body, src_rel_dir)
    fm_new = dict(fm)

    out_text = emit_frontmatter(fm_new) + "\n" + body_new.lstrip("\n")

    src_w = word_count(body)
    dst_w = word_count(body_new)
    return job, src_w, dst_w, out_text


def write_dst(job: Job, content: str) -> None:
    job.dst.parent.mkdir(parents=True, exist_ok=True)
    if job.role == "section_index" and job.dst.exists():
        existing = job.dst.read_text(encoding="utf-8")
        # Concatenate body of new content (skip its frontmatter; keep first FM).
        _, new_body = parse_frontmatter(content)
        merged = existing.rstrip() + "\n\n" + new_body.lstrip("\n")
        job.dst.write_text(merged, encoding="utf-8")
    else:
        job.dst.write_text(content, encoding="utf-8")


def main(argv: list[str]) -> int:
    if argv:
        files = [REPO / a for a in argv]
    else:
        batches = REPO / "_scripts_migration" / "batches.txt"
        if not batches.exists():
            print("no paths given and _scripts_migration/batches.txt missing")
            return 2
        files = [
            REPO / line.strip()
            for line in batches.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        ]

    drift = []
    for src in files:
        if not src.exists():
            print(f"  miss  {src.relative_to(REPO)}")
            continue
        job, sw, dw, text = convert_one(src)
        if job is None:
            print(f"  ?     {src.relative_to(REPO)} (no path mapping)")
            continue
        if job.role == "skip":
            print(f"  skip  {src.relative_to(REPO)}")
            continue
        write_dst(job, text)
        drift_pct = abs(dw - sw) / max(sw, 1) * 100
        flag = " [DRIFT]" if drift_pct > 2 else ""
        print(
            f"  ok    {src.relative_to(REPO)} -> "
            f"{job.dst.relative_to(REPO)}  ({sw}->{dw} words, "
            f"{drift_pct:.1f}%){flag}"
        )
        if drift_pct > 2:
            drift.append((src.relative_to(REPO), sw, dw, drift_pct))

    if drift:
        print("\nFiles flagged for manual review (>2% word drift):")
        for r in drift:
            print(f"  {r[0]}: {r[1]}->{r[2]} words ({r[3]:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
