<<<<<<< HEAD
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "paper-boat.html"
INDEX = ROOT / "index.html"


def main() -> None:
    paper = PAPER.read_text(encoding="utf-8", errors="replace")

    m = re.search(
        r'<img[^>]+id="boatPhoto"[^>]+src="(data:image/png;base64,[^"]+)"',
        paper,
        flags=re.IGNORECASE,
    )
    if not m:
        raise SystemExit("Could not find boatPhoto PNG data URI in paper-boat.html")

    png_uri = m.group(1)

    html = INDEX.read_text(encoding="utf-8", errors="replace")

    pat = re.compile(
        r'(<a\s+href="paper-boat\.html"[^>\n]*>.*?<img\s+[^>\n]*src=")'
        r"(?:data:image/png;base64,[^\"]+|data:image/svg\+xml;utf8,[^\"]+|data:image/svg\+xml;base64,[^\"]+)"
        r'(")',
        re.IGNORECASE,
    )

    new_html, n = pat.subn(rf"\1{png_uri}\2", html, count=1)
    if n != 1:
        raise SystemExit(f"Expected to replace 1 paper-boat icon in index.html, replaced {n}.")

    INDEX.write_text(new_html, encoding="utf-8")
    print("OK: restored paper-boat icon PNG in index.html")


if __name__ == "__main__":
    main()

=======
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "paper-boat.html"
INDEX = ROOT / "index.html"


def main() -> None:
    paper = PAPER.read_text(encoding="utf-8", errors="replace")

    m = re.search(
        r'<img[^>]+id="boatPhoto"[^>]+src="(data:image/png;base64,[^"]+)"',
        paper,
        flags=re.IGNORECASE,
    )
    if not m:
        raise SystemExit("Could not find boatPhoto PNG data URI in paper-boat.html")

    png_uri = m.group(1)

    html = INDEX.read_text(encoding="utf-8", errors="replace")

    pat = re.compile(
        r'(<a\s+href="paper-boat\.html"[^>\n]*>.*?<img\s+[^>\n]*src=")'
        r"(?:data:image/png;base64,[^\"]+|data:image/svg\+xml;utf8,[^\"]+|data:image/svg\+xml;base64,[^\"]+)"
        r'(")',
        re.IGNORECASE,
    )

    new_html, n = pat.subn(rf"\1{png_uri}\2", html, count=1)
    if n != 1:
        raise SystemExit(f"Expected to replace 1 paper-boat icon in index.html, replaced {n}.")

    INDEX.write_text(new_html, encoding="utf-8")
    print("OK: restored paper-boat icon PNG in index.html")


if __name__ == "__main__":
    main()

>>>>>>> 95e01d88ba3d7be6026253c45543c09ddb4e0b3f
