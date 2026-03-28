<<<<<<< HEAD
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Ref:
    file: Path
    kind: str  # href|src|action
    target: str


SKIP_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "#",
    "javascript:",
    "data:",
)


def is_skippable(url: str) -> bool:
    u = url.strip()
    # Skip template placeholders / string-concat fragments that are not literal paths.
    if "${" in u or "}" in u:
        return True
    if "+item." in u or "item.img" in u or "w.img" in u or "v.slug" in u or "w.slug" in u:
        return True
    if "LOGO_WHITE_PLACEHOLDER" in u:
        # keep this one (it's a real bug), don't skip
        return False
    return u == "" or u.startswith(SKIP_PREFIXES)


def normalize(url: str) -> str:
    u = url.strip().strip("'").strip('"')
    u = u.split("#", 1)[0].split("?", 1)[0]
    return u


def collect_refs(html_path: Path) -> list[Ref]:
    text = html_path.read_text(encoding="utf-8", errors="ignore")
    refs: list[Ref] = []
    # Very simple attribute parsing is enough for this project.
    for kind in ("href", "src", "action"):
        for m in re.finditer(rf"""\b{kind}\s*=\s*(["'])(.*?)\1""", text, flags=re.I):
            refs.append(Ref(file=html_path, kind=kind, target=m.group(2)))
    return refs


def main() -> None:
    root = Path(__file__).resolve().parent
    html_files = sorted(root.rglob("*.html"))

    missing: list[tuple[Ref, Path]] = []
    for f in html_files:
        for ref in collect_refs(f):
            if is_skippable(ref.target):
                continue
            target = normalize(ref.target)
            # treat root-relative (/x) as workspace-relative
            if target.startswith("/"):
                target_path = root / target.lstrip("/")
            else:
                target_path = (ref.file.parent / target).resolve()
            if not target_path.exists():
                missing.append((ref, target_path))

    print(f"html_files {len(html_files)}")
    print(f"missing_refs {len(missing)}")
    for ref, target_path in missing:
        rel_from_root = ref.file.relative_to(root)
        print(f"MISSING\t{rel_from_root}\t{ref.kind}\t{ref.target}\t->\t{target_path.relative_to(root) if target_path.is_absolute() and str(target_path).startswith(str(root)) else target_path}")


if __name__ == "__main__":
    main()

=======
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Ref:
    file: Path
    kind: str  # href|src|action
    target: str


SKIP_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "#",
    "javascript:",
    "data:",
)


def is_skippable(url: str) -> bool:
    u = url.strip()
    # Skip template placeholders / string-concat fragments that are not literal paths.
    if "${" in u or "}" in u:
        return True
    if "+item." in u or "item.img" in u or "w.img" in u or "v.slug" in u or "w.slug" in u:
        return True
    if "LOGO_WHITE_PLACEHOLDER" in u:
        # keep this one (it's a real bug), don't skip
        return False
    return u == "" or u.startswith(SKIP_PREFIXES)


def normalize(url: str) -> str:
    u = url.strip().strip("'").strip('"')
    u = u.split("#", 1)[0].split("?", 1)[0]
    return u


def collect_refs(html_path: Path) -> list[Ref]:
    text = html_path.read_text(encoding="utf-8", errors="ignore")
    refs: list[Ref] = []
    # Very simple attribute parsing is enough for this project.
    for kind in ("href", "src", "action"):
        for m in re.finditer(rf"""\b{kind}\s*=\s*(["'])(.*?)\1""", text, flags=re.I):
            refs.append(Ref(file=html_path, kind=kind, target=m.group(2)))
    return refs


def main() -> None:
    root = Path(__file__).resolve().parent
    html_files = sorted(root.rglob("*.html"))

    missing: list[tuple[Ref, Path]] = []
    for f in html_files:
        for ref in collect_refs(f):
            if is_skippable(ref.target):
                continue
            target = normalize(ref.target)
            # treat root-relative (/x) as workspace-relative
            if target.startswith("/"):
                target_path = root / target.lstrip("/")
            else:
                target_path = (ref.file.parent / target).resolve()
            if not target_path.exists():
                missing.append((ref, target_path))

    print(f"html_files {len(html_files)}")
    print(f"missing_refs {len(missing)}")
    for ref, target_path in missing:
        rel_from_root = ref.file.relative_to(root)
        print(f"MISSING\t{rel_from_root}\t{ref.kind}\t{ref.target}\t->\t{target_path.relative_to(root) if target_path.is_absolute() and str(target_path).startswith(str(root)) else target_path}")


if __name__ == "__main__":
    main()

>>>>>>> 95e01d88ba3d7be6026253c45543c09ddb4e0b3f
