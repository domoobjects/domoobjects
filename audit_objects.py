import re
from pathlib import Path


def main() -> None:
    index_path = Path(__file__).with_name("index.html")
    text = index_path.read_text(encoding="utf-8", errors="ignore")

    m = re.search(r'<section\s+id="objects"[\s\S]*?</section>', text, flags=re.I)
    print("objects_section_found", bool(m))
    if not m:
        return

    sec = m.group(0)
    hrefs = re.findall(r'href\s*=\s*"([^"]+)"', sec, flags=re.I)
    local = [
        h.split("#", 1)[0].split("?", 1)[0]
        for h in hrefs
        if not re.match(r"^(https?:|mailto:|tel:|#)", h)
    ]
    unique = sorted(set(local))
    missing = [h for h in unique if not Path(h).exists()]
    present = [h for h in unique if Path(h).exists()]

    print("href_count", len(hrefs))
    print("unique_local", len(unique))
    print("present_unique", len(present))
    print("missing_unique", len(missing))
    for h in present:
        print("PRESENT", h)
    for h in missing:
        print("MISSING", h)


if __name__ == "__main__":
    main()

