<<<<<<< HEAD
from __future__ import annotations

import re
from pathlib import Path


HREF_RE = re.compile(r'<a\s+href="([^"]+)"', re.IGNORECASE)


def dedupe_objects_grid_lines(html: str) -> tuple[str, int]:
    """
    Dedupe repeated object-card <a href="..."> lines inside the #objects section,
    keeping the first occurrence of each href.
    """
    lines = html.splitlines(True)  # keep EOLs
    out: list[str] = []

    in_objects = False
    seen: set[str] = set()
    removed = 0

    for line in lines:
        if '<section id="objects"' in line:
            in_objects = True
            out.append(line)
            continue

        if in_objects and "</section>" in line:
            in_objects = False
            out.append(line)
            continue

        if in_objects and "object-card" in line and "<a " in line and "</a>" in line:
            m = HREF_RE.search(line)
            href = (m.group(1).strip() if m else "")
            if href and href in seen:
                removed += 1
                continue
            if href:
                seen.add(href)
            out.append(line)
            continue

        out.append(line)

    return ("".join(out), removed)


def process_file(path: Path) -> int:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    updated, removed = dedupe_objects_grid_lines(raw)
    if updated != raw:
        path.write_text(updated, encoding="utf-8", errors="ignore")
    return removed


def main() -> None:
    root = Path(__file__).resolve().parent
    targets = [
        root / "index.html",
        root / "domo2" / "index.html",
    ]

    total_removed = 0
    for p in targets:
        if not p.exists():
            continue
        total_removed += process_file(p)

    print(f"removed_duplicates {total_removed}")


if __name__ == "__main__":
    main()

=======
from __future__ import annotations

import re
from pathlib import Path


HREF_RE = re.compile(r'<a\s+href="([^"]+)"', re.IGNORECASE)


def dedupe_objects_grid_lines(html: str) -> tuple[str, int]:
    """
    Dedupe repeated object-card <a href="..."> lines inside the #objects section,
    keeping the first occurrence of each href.
    """
    lines = html.splitlines(True)  # keep EOLs
    out: list[str] = []

    in_objects = False
    seen: set[str] = set()
    removed = 0

    for line in lines:
        if '<section id="objects"' in line:
            in_objects = True
            out.append(line)
            continue

        if in_objects and "</section>" in line:
            in_objects = False
            out.append(line)
            continue

        if in_objects and "object-card" in line and "<a " in line and "</a>" in line:
            m = HREF_RE.search(line)
            href = (m.group(1).strip() if m else "")
            if href and href in seen:
                removed += 1
                continue
            if href:
                seen.add(href)
            out.append(line)
            continue

        out.append(line)

    return ("".join(out), removed)


def process_file(path: Path) -> int:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    updated, removed = dedupe_objects_grid_lines(raw)
    if updated != raw:
        path.write_text(updated, encoding="utf-8", errors="ignore")
    return removed


def main() -> None:
    root = Path(__file__).resolve().parent
    targets = [
        root / "index.html",
        root / "domo2" / "index.html",
    ]

    total_removed = 0
    for p in targets:
        if not p.exists():
            continue
        total_removed += process_file(p)

    print(f"removed_duplicates {total_removed}")


if __name__ == "__main__":
    main()

>>>>>>> 95e01d88ba3d7be6026253c45543c09ddb4e0b3f
