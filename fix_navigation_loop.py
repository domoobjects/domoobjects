#!/usr/bin/env python3
"""
Fix navigation loop between object pages.
Creates a circular prev/next navigation through all object pages.
"""
import re
from pathlib import Path

# List of object pages in desired order (matches index.html order)
OBJECT_PAGES = [
    "grey-piggy-bank.html",
    "paper-boat.html",
    "silence-after-scream.html",
    "handcuff.html",
    "red-blood-cell.html",
    "bowling-pin.html",
    "moai.html",
    "sun.html",
    "blue-toilet.html",
    "movable-water-bed.html",
    "crocodile.html",
    "melting-skull.html",
    "octopus.html",
    "raven-skull.html",
    "sad-gargoyle.html",
    "key.html",
]

def fix_navigation_in_file(filepath: Path, page_list: list[str]) -> bool:
    """Fix prev/next navigation in a single HTML file."""
    if not filepath.exists():
        return False
    
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    filename = filepath.name
    
    if filename not in page_list:
        return False
    
    idx = page_list.index(filename)
    prev_page = page_list[idx - 1] if idx > 0 else page_list[-1]  # Loop to last
    next_page = page_list[idx + 1] if idx < len(page_list) - 1 else page_list[0]  # Loop to first
    
    # Pattern to match obj-nav links
    prev_pattern = r'<a\s+href="[^"]*"\s+class="obj-nav\s+prev"[^>]*>.*?</a>'
    next_pattern = r'<a\s+href="[^"]*"\s+class="obj-nav\s+next"[^>]*>.*?</a>'
    
    # New navigation links
    new_prev = f'<a href="{prev_page}" class="obj-nav prev"><div class="obj-nav-arrow">â†</div></a>'
    new_next = f'<a href="{next_page}" class="obj-nav next"><div class="obj-nav-arrow">â†’</div></a>'
    
    modified = False
    
    # Replace prev link
    if re.search(prev_pattern, content, re.IGNORECASE | re.DOTALL):
        content = re.sub(prev_pattern, new_prev, content, flags=re.IGNORECASE | re.DOTALL)
        modified = True
    else:
        # If no prev link exists, add it before the nav element
        content = new_prev + "\n" + content
        modified = True
    
    # Replace next link
    if re.search(next_pattern, content, re.IGNORECASE | re.DOTALL):
        content = re.sub(next_pattern, new_next, content, flags=re.IGNORECASE | re.DOTALL)
        modified = True
    else:
        # If no next link exists, add it after the prev link
        content = content.replace(new_prev, new_prev + "\n" + new_next, 1)
        modified = True
    
    if modified:
        filepath.write_text(content, encoding="utf-8", errors="ignore")
    
    return modified

def main():
    root = Path(__file__).resolve().parent
    
    fixed_count = 0
    missing_pages = []
    
    for page in OBJECT_PAGES:
        filepath = root / page
        if filepath.exists():
            if fix_navigation_in_file(filepath, OBJECT_PAGES):
                fixed_count += 1
                print(f"Fixed navigation: {page}")
            else:
                print(f"No changes needed: {page}")
        else:
            missing_pages.append(page)
            print(f"MISSING: {page}")
    
    # Also fix domo2 folder if it exists
    domo2 = root / "domo2"
    if domo2.exists():
        for page in OBJECT_PAGES:
            filepath = domo2 / page
            if filepath.exists():
                if fix_navigation_in_file(filepath, OBJECT_PAGES):
                    print(f"Fixed navigation (domo2): {page}")
    
    print(f"\nFixed {fixed_count} files")
    if missing_pages:
        print(f"Missing {len(missing_pages)} pages: {missing_pages}")

if __name__ == "__main__":
    main()
