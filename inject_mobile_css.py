from __future__ import annotations

from pathlib import Path


LINK_ROOT = '<link rel="stylesheet" href="mobile-overrides.css">'
LINK_DOMO2 = '<link rel="stylesheet" href="../mobile-overrides.css">'


def add_link(html: str, href: str) -> str:
    if "mobile-overrides.css" in html:
        return html
    lower = html.lower()
    i = lower.find("</head>")
    if i == -1:
        return html
    # Keep it near the end of head so it can override page CSS.
    return html[:i] + "\n" + href + "\n" + html[i:]


def main() -> None:
    root = Path(__file__).resolve().parent
    html_files = list(root.rglob("*.html"))
    changed = 0
    for f in html_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        href = LINK_DOMO2 if ("\\domo2\\" in str(f).lower() or "/domo2/" in str(f).lower()) else LINK_ROOT
        new = add_link(text, href)
        if new != text:
            f.write_text(new, encoding="utf-8", errors="ignore")
            changed += 1
    print(f"updated_files {changed}")


if __name__ == "__main__":
    main()

