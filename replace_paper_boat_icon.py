from __future__ import annotations

import re
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INDEXES = [
    ROOT / "index.html",
    ROOT / "domo2" / "index.html",
]


def make_paper_boat_data_uri() -> str:
    # Clean, centered paper-boat icon (SVG) to match other line icons.
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <path d="M22 118l78-78 78 78" fill="none" stroke="#0b0b0b" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M22 118l78 42 78-42" fill="none" stroke="#0b0b0b" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M100 40v120" fill="none" stroke="#0b0b0b" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" opacity="0.25"/>
</svg>"""
    return "data:image/svg+xml;utf8," + urllib.parse.quote(svg, safe=",:;()[]@!$&'*+?=/#")


def main() -> None:
    uri = make_paper_boat_data_uri()

    # Replace ONLY the paper-boat icon's data URL (the long PNG base64 line).
    # We match within the same line to avoid disturbing layout/formatting.
    pat = re.compile(
        r'(<a\s+href="paper-boat\.html"[^>\n]*>.*?<img\s+[^>\n]*src=")'
        r"(?:data:image/png;base64,[^\"]+|data:image/svg\+xml;utf8,[^\"]+)"
        r'(")',
        re.IGNORECASE,
    )

    updated_any = False
    for idx in INDEXES:
        if not idx.exists():
            continue
        html = idx.read_text(encoding="utf-8", errors="replace")
        new_html, n = pat.subn(rf"\1{uri}\2", html, count=1)
        if n != 1:
            raise SystemExit(f"{idx.name}: expected to replace 1 paper-boat icon, replaced {n}.")
        idx.write_text(new_html, encoding="utf-8")
        print(f"OK: updated paper-boat icon in {idx.as_posix()}")
        updated_any = True

    if not updated_any:
        raise SystemExit("No index files found to update.")


if __name__ == "__main__":
    main()

