from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    html_files = list(root.rglob("*.html"))
    changed = 0
    for f in html_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        if "rel=\"icon\"" not in text and "rel='icon'" not in text:
            continue

        new = text
        # Replace common broken favicon.png reference with favicon.svg.
        new = new.replace('rel="icon" type="image/png" href="favicon.png"', 'rel="icon" type="image/svg+xml" href="favicon.svg"')
        new = new.replace("rel='icon' type='image/png' href='favicon.png'", "rel='icon' type='image/svg+xml' href='favicon.svg'")
        new = new.replace('rel="icon" href="favicon.png"', 'rel="icon" type="image/svg+xml" href="favicon.svg"')

        if new != text:
            f.write_text(new, encoding="utf-8", errors="ignore")
            changed += 1

    print(f"updated_files {changed}")


if __name__ == "__main__":
    main()

