#!/usr/bin/env python3
"""
Inject objects-loop.js into index.html before closing </body> tag
"""
from pathlib import Path
import re

def inject_script(index_path: Path) -> bool:
    """Add objects-loop.js script tag to index.html"""
    if not index_path.exists():
        print(f"File not found: {index_path}")
        return False
    
    text = index_path.read_text(encoding="utf-8", errors="ignore")
    
    # Check if already injected
    if 'objects-loop.js' in text:
        print("Script already injected")
        return False
    
    # Find </body> tag and inject before it
    pattern = r'(</body>)'
    replacement = r'<script src="objects-loop.js"></script>\n\1'
    
    new_text, count = re.subn(pattern, replacement, text, flags=re.IGNORECASE)
    
    if count == 0:
        print("Could not find </body> tag")
        return False
    
    # Backup
    bak_path = index_path.with_suffix(index_path.suffix + ".bak")
    if not bak_path.exists():
        bak_path.write_text(text, encoding="utf-8", errors="ignore")
        print(f"Backup created: {bak_path.name}")
    
    index_path.write_text(new_text, encoding="utf-8", errors="ignore")
    print(f"Injected objects-loop.js into {index_path.name}")
    return True

def main():
    root = Path(__file__).resolve().parent
    
    # Fix main index.html
    index_html = root / "index.html"
    inject_script(index_html)
    
    # Fix domo2/index.html if it exists
    domo2_index = root / "domo2" / "index.html"
    if domo2_index.exists():
        inject_script(domo2_index)

if __name__ == "__main__":
    main()
