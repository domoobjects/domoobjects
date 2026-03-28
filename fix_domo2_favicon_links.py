<<<<<<< HEAD
from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    domo2 = root / "domo2"
    if not domo2.exists():
        print("domo2 folder not found; nothing to do.")
        return

    changed = 0
    for f in domo2.rglob("*.html"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        new = text.replace('href="favicon.svg"', 'href="../favicon.svg"')
        new = new.replace("href='favicon.svg'", "href='../favicon.svg'")
        if new != text:
            f.write_text(new, encoding="utf-8", errors="ignore")
            changed += 1

    print(f"updated_files {changed}")


if __name__ == "__main__":
    main()

=======
from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    domo2 = root / "domo2"
    if not domo2.exists():
        print("domo2 folder not found; nothing to do.")
        return

    changed = 0
    for f in domo2.rglob("*.html"):
        text = f.read_text(encoding="utf-8", errors="ignore")
        new = text.replace('href="favicon.svg"', 'href="../favicon.svg"')
        new = new.replace("href='favicon.svg'", "href='../favicon.svg'")
        if new != text:
            f.write_text(new, encoding="utf-8", errors="ignore")
            changed += 1

    print(f"updated_files {changed}")


if __name__ == "__main__":
    main()

>>>>>>> 95e01d88ba3d7be6026253c45543c09ddb4e0b3f
