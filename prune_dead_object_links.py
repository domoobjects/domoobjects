import re
import sys
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    rel = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    index_path = (root / rel).resolve()
    if not index_path.exists():
        raise SystemExit(f"File not found: {rel}")
    text = index_path.read_text(encoding="utf-8", errors="ignore")

    # Find the Objects section.
    m = re.search(r'(<section\s+id="objects"[\s\S]*?>)([\s\S]*?)(</section>)', text, flags=re.I)
    if not m:
        raise SystemExit("Could not find <section id=\"objects\"> in index.html")

    open_tag, body, close_tag = m.group(1), m.group(2), m.group(3)

    # Collect hrefs inside the section, and mark those that point to missing local files.
    hrefs = re.findall(r'href\s*=\s*"([^"]+)"', body, flags=re.I)
    local = [
        h.split("#", 1)[0].split("?", 1)[0]
        for h in hrefs
        if not re.match(r"^(https?:|mailto:|tel:|#)", h)
    ]
    unique = sorted(set(local))
    missing = [h for h in unique if not (root / h).exists()]

    if not missing:
        print("No dead object links found; nothing to prune.")
        return

    # Remove full <a ...>...</a> blocks for missing href targets.
    pruned_body = body
    removed = 0
    for href in missing:
        # Non-greedy match; spans across newlines if needed.
        pattern = re.compile(
            r'<a\s+[^>]*href\s*=\s*"'
            + re.escape(href)
            + r'"[^>]*>[\s\S]*?</a>',
            flags=re.I,
        )
        pruned_body, n = pattern.subn("", pruned_body)
        removed += n

    # Clean up: collapse runs of blank lines created by removals.
    pruned_body = re.sub(r"\n[ \t]*\n[ \t]*\n+", "\n\n", pruned_body)

    new_text = text[: m.start()] + open_tag + pruned_body + close_tag + text[m.end() :]

    # Backup then write.
    bak_path = index_path.with_suffix(index_path.suffix + ".bak")
    if not bak_path.exists():
        bak_path.write_text(text, encoding="utf-8", errors="ignore")
        print(f"Backup created: {bak_path.name}")

    index_path.write_text(new_text, encoding="utf-8", errors="ignore")

    print(f"Missing href targets: {len(missing)}")
    print(f"Removed <a> blocks: {removed}")


if __name__ == "__main__":
    main()

