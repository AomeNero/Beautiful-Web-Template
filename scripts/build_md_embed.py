#!/usr/bin/env python3
"""Build script: inline all template .md files into index.html as a JS object.

Uses base64 encoding to embed markdown content. Base64 output contains only
[A-Za-z0-9+/=] characters — no quotes, no backslashes, no newlines, no
special chars that could break JS syntax. 100% safe.

At runtime, MD_DATA values are decoded with atob() before being parsed by marked.

Usage:
    python scripts/build_md_embed.py
"""
import base64
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
TEMPLATES_DIR = BASE_DIR / "templates"
INDEX_HTML = BASE_DIR / "index.html"

START_MARKER = "/* --- EMBEDDED_MD_START (auto-generated) --- */"
END_MARKER   = "/* --- EMBEDDED_MD_END   (auto-generated) --- */"


def collect_md_data():
    """Read every templates/*/Name.md and return {name: content}."""
    data = {}
    for d in sorted(TEMPLATES_DIR.iterdir()):
        if not d.is_dir():
            continue
        md_file = d / f"{d.name}.md"
        if md_file.exists():
            data[d.name] = md_file.read_text(encoding="utf-8")
    return data


def build_embed_block(data):
    """Return a JS const declaration with base64-encoded markdown values."""
    lines = ["var MD_DATA = {"]
    for name in sorted(data):
        content = data[name]
        b64 = base64.b64encode(content.encode("utf-8")).decode("ascii")
        lines.append(f"  '{name}': '{b64}',")
    lines.append("};")
    return "\n".join(lines)


def update_index_html(embed_block):
    """Replace or insert the embedded MD_DATA block in index.html."""
    html = INDEX_HTML.read_text(encoding="utf-8")

    if START_MARKER in html and END_MARKER in html:
        pattern = re.compile(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER),
            flags=re.DOTALL,
        )
        new_block = f"{START_MARKER}\n{embed_block}\n{END_MARKER}"
        html = pattern.sub(new_block, html)
    else:
        idx = html.rfind("</script>")
        if idx == -1:
            raise RuntimeError("Cannot find </script> in index.html")
        new_block = f"\n{START_MARKER}\n{embed_block}\n{END_MARKER}\n"
        html = html[:idx] + new_block + html[idx:]

    INDEX_HTML.write_text(html, encoding="utf-8")
    print(f"Embedded {len(data)} markdown files into index.html (base64)")


if __name__ == "__main__":
    data = collect_md_data()
    embed = build_embed_block(data)
    update_index_html(embed)
