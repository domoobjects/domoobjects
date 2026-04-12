#!/usr/bin/env python3
"""
Remove objects-loop.js script from index.html
"""
from pathlib import Path
import re

def remove_script(index_path: Path) -> bool:
    """Remove objects-loop.js script tag from index.html"""
    if not index_path.exists():
        print(f"File not found: {index_path}")
        return False
    
    text = index_path.read_text(encoding="utf-8", errors="ignore")
    
    # Check if script exists
    if 'objects-loop.js' not in text:
        print(f"Script not found in {index_path.name}")
        return False
    
    # Remove the script tag
    pattern = r'<script src="objects-loop\.js"></script>\n*'
    new_text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    
    # Backup
    bak_path = index_path.with_suffix(index_path.suffix + ".bak2")
    if not bak_path.exists():
        bak_path.write_text(text, encoding="utf-8", errors="ignore")
        print(f"Backup created: {bak_path.name}")
    
    index_path.write_text(new_text, encoding="utf-8", errors="ignore")
    print(f"Removed objects-loop.js from {index_path.name}")
    return True

def main():
    root = Path(__file__).resolve().parent
    
    # Fix main index.html
    index_html = root / "index.html"
    remove_script(index_html)
    
    # Fix domo2/index.html if it exists
    domo2_index = root / "domo2" / "index.html"
    if domo2_index.exists():
        remove_script(domo2_index)

if __name__ == "__main__":
    main()
