#!/usr/bin/env python3
"""
Convert Godot docs RST files to Markdown. Lives in .docs/; all input and output stay in .docs/.

- Each run: clones a fresh copy of godot-docs from GitHub, then converts RST → MD.
- Output: .docs/godot-docs-md/ (same folder structure as the cloned repo).
- Proper markdown tables, internal :ref:/:doc: → .md links, external links removed.
- Images and assets copied so links work.

Usage (from repo root or .docs):
  python .docs/rst_to_md.py
"""
from pathlib import Path
import re
import os
import subprocess
import shutil

BASE_DIR = Path(__file__).resolve().parent
GODOT_DOCS_REPO = "https://github.com/godotengine/godot-docs.git"
CLONE_DIR = BASE_DIR / "godot-docs"
OUT_DIR = BASE_DIR / "godot-docs-md"
SKIP_DIRS = {"_build", ".git", "__pycache__"}

REPLACEMENTS = {
    "|virtual|": "*virtual*",
    "|const|": "*const*",
    "|vararg|": "*vararg*",
    "|constructor|": "*constructor*",
    "|static|": "*static*",
    "|operator|": "*operator*",
    "|bitfield|": "*BitField*",
    "|void|": "void",
}


def clone_fresh_repo() -> Path:
    if CLONE_DIR.exists():
        print(f"Removing existing clone: {CLONE_DIR}")
        shutil.rmtree(CLONE_DIR, ignore_errors=True)
    CLONE_DIR.parent.mkdir(parents=True, exist_ok=True)
    print(f"Cloning {GODOT_DOCS_REPO} into {CLONE_DIR} ...")
    subprocess.run(["git", "clone", "--depth", "1", GODOT_DOCS_REPO, str(CLONE_DIR)], check=True)
    print("Clone done.")
    return CLONE_DIR


def normalize_ref_label(label: str) -> str:
    return label.lower()


def collect_anchors_and_files(src: Path) -> tuple[dict[str, str], list[Path]]:
    anchor_to_rel: dict[str, str] = {}
    rst_files: list[Path] = []
    for rst in src.rglob("*.rst"):
        if any(s in rst.parts for s in SKIP_DIRS):
            continue
        try:
            rel = rst.relative_to(src)
        except ValueError:
            continue
        rel_str = str(rel).replace("\\", "/")
        rst_files.append(rst)
        content = rst.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"^\.\.\s+_([a-zA-Z0-9_]+)\s*:\s*$", content, re.MULTILINE):
            anchor_to_rel[m.group(1)] = rel_str
            anchor_to_rel[normalize_ref_label(m.group(1))] = rel_str
    return anchor_to_rel, rst_files


def rel_path(from_path: str, to_path: str) -> str:
    from_dir = os.path.dirname(from_path)
    to_md = to_path.replace(".rst", ".md")
    try:
        r = os.path.relpath(to_md, from_dir or ".")
    except ValueError:
        return to_md
    return r.replace("\\", "/")


def resolve_ref(anchor: str, anchor_to_rel: dict[str, str], current_rel: str) -> str | None:
    rel_rst = anchor_to_rel.get(anchor) or anchor_to_rel.get(normalize_ref_label(anchor))
    if not rel_rst:
        return None
    return rel_path(current_rel, rel_rst).replace(".rst", ".md")


def convert_refs(line: str, anchor_to_rel: dict[str, str], current_rel: str) -> str:
    def repl(m: re.Match) -> str:
        inner = m.group(1)
        if "<" in inner and ">" in inner:
            text, label = re.match(r"(.*?)<([^>]+)>", inner, re.DOTALL).groups()
            text, label = text.strip(), label.strip()
        else:
            label = inner.strip()
            text = label
        path = resolve_ref(label, anchor_to_rel, current_rel)
        if path is None:
            return text
        return f"[{text}]({path}#{label})"
    return re.sub(r":ref:`([^`]+)`", repl, line)


def convert_doc_links(line: str, current_rel: str) -> str:
    def repl(m: re.Match) -> str:
        text, path = m.group(1).strip(), m.group(2).strip()
        from_dir = os.path.dirname(current_rel)
        full = os.path.normpath(os.path.join(from_dir, path)) if from_dir else os.path.normpath(path)
        full = full.replace("\\", "/")
        if not full.endswith(".md") and not full.endswith(".rst"):
            full = full + ".md"
        full = full.replace(".rst", ".md")
        try:
            rel_to = os.path.relpath(full, from_dir or ".")
        except ValueError:
            rel_to = full
        return f"[{text}]({rel_to.replace(chr(92), '/')})"
    return re.sub(r":doc:`([^<]+)<([^>]+)>`", repl, line)


def strip_external_links(line: str) -> str:
    return re.sub(r"`([^`]*?)\s*<https?://[^>]+>`_?_?", r"\1", line)


def apply_replacements(line: str) -> str:
    for k, v in REPLACEMENTS.items():
        line = line.replace(k, v)
    return line


def parse_rst_table(lines: list[str], start: int) -> tuple[list[list[str]], int]:
    rows, i = [], start
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*\+[-+]+\+", line):
            i += 1
            continue
        if re.match(r"^\s*\|", line):
            cells = [c.strip() for c in re.split(r"\s*\|\s*", line.strip()) if c.strip()]
            if cells:
                rows.append(cells)
            i += 1
        else:
            break
    return rows, i


def table_to_markdown(rows: list[list[str]], ref_fn) -> str:
    if not rows:
        return ""
    qualifiers = {"const", "void", "static", "virtual", "vararg", "constructor", "operator", "bitfield"}

    def norm_row(row: list[str]) -> list[str]:
        row = [ref_fn(c) for c in row]
        row = [apply_replacements(c) for c in row]
        row = [re.sub(r"``([^`]+)``", r"`\1`", c) for c in row]
        row = [c.replace("\\ ", " ").replace("\\(", "(").replace("\\)", ")").replace("\\:", ":") for c in row]
        if len(row) == 3 and row[2].lower().strip() in qualifiers:
            row = [row[0], row[1] + " " + row[2].strip()]
        return row

    out = []
    for i, row in enumerate(rows):
        row = norm_row(row)
        out.append("| " + " | ".join(row) + " |")
        if i == 0:
            out.append("| " + " | ".join("---" for _ in row) + " |")
    return "\n".join(out)


def convert_inline_code(line: str) -> str:
    return re.sub(r"``([^`]+)``", r"`\1`", line)


def convert_image(line: str, current_dir: str) -> str:
    m = re.match(r"^\s*\.\.\s+image::\s+(.+)$", line)
    return f"![]({m.group(1).strip()})" if m else ""


def convert_heading_underline(line: str, next_line: str) -> tuple[str, str, bool]:
    if not next_line:
        return line, next_line, False
    s = next_line.strip()
    if re.match(r"^=+\s*$", s):
        lv = 1
    elif re.match(r"^\-+\s*$", s):
        lv = 2
    elif re.match(r"^\^+\s*$", s):
        lv = 3
    else:
        return line, next_line, False
    return "#" * (lv + 1) + " " + line.strip(), "", True


def is_directive_to_skip(line: str) -> bool:
    if not line.strip():
        return False
    s = line.strip()
    if s.startswith(".. "):
        if any(s.startswith(".. " + d) for d in (
            "DO NOT EDIT", "Generated", "Generator:", "XML source:", "github_url", "allow_comments",
            "rst-class::", "only::", "centered::", "replace::", "abbr::")):
            return True
        if re.match(r"\.\.\s+(image|figure)::", s):
            return False
        if re.match(r"\.\.\s+(table|toctree|tabs|code-tab|warning|note)::", s):
            return False
        if re.match(r"\.\.\s+_[a-zA-Z0-9_]+\s*:", s):
            return False
    return False


def convert_rst_to_md(rst_path: Path, anchor_to_rel: dict[str, str], out_root: Path, src_dir: Path) -> None:
    rel = rst_path.relative_to(src_dir)
    current_rel = str(rel).replace("\\", "/")

    def ref_fn(text: str) -> str:
        return convert_refs(apply_replacements(text), anchor_to_rel, current_rel)

    lines = rst_path.read_text(encoding="utf-8", errors="replace").splitlines()
    out_lines, i = [], 0

    while i < len(lines):
        line = lines[i]

        if re.search(r"https?://", line) and re.match(r"^\s*\.\.\s+|^\s*`[^`]*<https?://", line):
            if ".. " in line and "image::" not in line and "figure::" not in line:
                i += 1
                continue
        if is_directive_to_skip(line):
            i += 1
            continue
        if re.match(r"^:(github_url|allow_comments):", line.strip()):
            i += 1
            continue
        if re.match(r"^\s*\.\.\s+\|[^|]+\|\s+replace::", line):
            i += 1
            continue

        anchor_m = re.match(r"^\s*\.\.\s+_([a-zA-Z0-9_]+)\s*:\s*$", line)
        if anchor_m:
            out_lines.append(f'<span id="{anchor_m.group(1)}"></span>')
            i += 1
            continue

        if re.match(r"^\s*\.\.\s+image::", line):
            out_lines.append(convert_image(line, ""))
            i += 1
            continue

        # .. raw:: html — profile grid → Markdown list; else emit HTML
        if re.match(r"^\s*\.\.\s+raw::\s+html\s*$", line):
            i += 1
            block = []
            while i < len(lines) and (not lines[i].strip() or lines[i].startswith(" ") or lines[i].startswith("\t")):
                block.append(lines[i])
                i += 1
            indented = [b for b in block if b.strip()]
            min_indent = min(len(b) - len(b.lstrip()) for b in indented) if indented else 0
            stripped_block = [b[min_indent:] if b.strip() else b for b in block]
            block_text = "\n".join(stripped_block)
            if "grid-container" in block_text and "grid-item" in block_text:
                out_lines.extend(["", "- **[I've never made a game before — I want to make a game.](about/introduction.md)**",
                    "- **[I know how to make a game — I want to know how to use Godot.](getting_started/step_by_step/index.md)**",
                    "- **[I know how to use Godot — I want to learn more advanced topics.](tutorials/index.md)**",
                    "- **I know Godot and want to contribute** (external: contributing.godotengine.org)", ""])
            else:
                for raw_line in stripped_block:
                    if raw_line.strip():
                        raw_line = re.sub(r'href="([^"]+)\.html"', r'href="\1.md"', raw_line)
                        raw_line = re.sub(r'href="https?://[^"]*"', r'href="#"', raw_line)
                    out_lines.append(raw_line)
            continue

        if re.match(r"^\s*\.\.\s+table::", line):
            i += 1
            while i < len(lines) and (not lines[i].strip() or lines[i].strip().startswith(":")):
                i += 1
            if i < len(lines) and re.match(r"^\s*\+", lines[i]):
                rows, i = parse_rst_table(lines, i)
                md = table_to_markdown(rows, ref_fn)
                if md:
                    out_lines.extend(["", md, ""])
            continue

        if re.match(r"^----+\s*$", line.strip()):
            out_lines.append("---")
            i += 1
            continue

        if i + 1 < len(lines) and line.strip():
            conv, _, ok = convert_heading_underline(line, lines[i + 1])
            if ok:
                out_lines.append(conv)
                i += 2
                continue

        # toctree: consume all entries (skip blank lines and ".. " comment lines; stop only at new directive)
        if re.match(r"^\s*\.\.\s+toctree::", line):
            i += 1
            while i < len(lines) and (lines[i].strip().startswith(":") or not lines[i].strip()):
                i += 1
            while i < len(lines):
                cur = lines[i]
                stripped = cur.strip()
                if not stripped:
                    i += 1
                    continue
                if re.match(r"^\s*\.\.\s+\w+\s*::", cur):
                    break
                if stripped.startswith(".. ") and "toctree" not in stripped:
                    i += 1
                    while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")) and "/" not in lines[i].strip():
                        i += 1
                    continue
                entry = stripped
                i += 1
                if entry.startswith("class_"):
                    target_rel = anchor_to_rel.get(normalize_ref_label(entry))
                    if target_rel:
                        link = rel_path(current_rel, target_rel)
                        title = entry.replace("class_", "").replace("_", " ").title()
                        out_lines.append(f"- [{title}]({link})")
                else:
                    link = f"{entry}.md"
                    title = entry.replace("_", " ").replace("-", " ").title()
                    out_lines.append(f"- [{title}]({link})")
            continue

        if re.match(r"^\s*\.\.\s+(code-tab|code-block)::", line):
            m = re.match(r"\.\.\s+(?:code-tab|code-block)::\s*(\w+)?", line)
            lang = m.group(1) if m and m.group(1) else ""
            i += 1
            out_lines.append(f"```{lang}")
            while i < len(lines) and (lines[i].startswith("    ") or lines[i].startswith("\t")):
                out_lines.append(lines[i].strip())
                i += 1
            out_lines.append("```")
            continue

        if re.match(r"^\s*\.\.\s+(warning|note)::", line):
            kind = "warning" if "warning" in line else "note"
            i += 1
            block = []
            while i < len(lines) and (lines[i].startswith("    ") or lines[i].startswith("\t") or not lines[i].strip()):
                if lines[i].strip():
                    block.append(lines[i].strip())
                i += 1
            out_lines.append(f"> **{kind.capitalize()}:** " + " ".join(block))
            continue

        line = convert_refs(line, anchor_to_rel, current_rel)
        line = convert_doc_links(line, current_rel)
        line = strip_external_links(line)
        line = apply_replacements(line)
        line = convert_inline_code(line)
        line = line.replace("\\ ", " ").replace("\\(", "(").replace("\\)", ")").replace("\\:", ":")
        line = line.rstrip().rstrip("\\")
        if line.strip() or (out_lines and out_lines[-1].strip()):
            out_lines.append(line)
        i += 1

    while out_lines and re.search(r"\.\.\s+\|.+\|\s+replace::", out_lines[-1]):
        out_lines.pop()

    out_path = out_root / rel.with_suffix(".md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(out_lines).strip() + "\n", encoding="utf-8")


def copy_assets(src: Path, out: Path) -> None:
    for path in src.rglob("*"):
        if path.is_file() and path.suffix.lower() != ".rst":
            if any(s in path.parts for s in SKIP_DIRS):
                continue
            try:
                rel = path.relative_to(src)
            except ValueError:
                continue
            dest = out / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, dest)
    print("Copied assets (images, etc.) to output.")


def main():
    clone_fresh_repo()
    src_dir = CLONE_DIR
    print("Scanning RST files and collecting anchors...")
    anchor_to_rel, rst_files = collect_anchors_and_files(src_dir)
    print(f"Found {len(anchor_to_rel)} anchors, {len(rst_files)} RST files.")
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for rst in rst_files:
        try:
            convert_rst_to_md(rst, anchor_to_rel, OUT_DIR, src_dir)
        except Exception as e:
            print(f"Error converting {rst}: {e}")
            raise
    copy_assets(src_dir, OUT_DIR)
    print("Removing cloned repo to save space...")

if __name__ == "__main__":
    main()
