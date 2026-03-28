#!/usr/bin/env python3
"""
Comprehensive audit of all object pages
- Check navigation loop integrity
- Verify all links point to existing files
- Report any broken or missing references
"""
import re
from pathlib import Path

# List of all object pages in the loop order
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

def audit_file(filepath: Path, page_list: list[str]) -> dict:
    """Audit a single HTML file for navigation integrity."""
    result = {
        "exists": filepath.exists(),
        "prev_link": None,
        "next_link": None,
        "prev_valid": False,
        "next_valid": False,
        "in_loop": filepath.name in page_list,
    }
    
    if not result["exists"]:
        return result
    
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    
    # Extract prev/next links
    prev_match = re.search(r'<a\s+href="([^"]+)"\s+class="obj-nav\s+prev"', content, re.IGNORECASE)
    next_match = re.search(r'<a\s+href="([^"]+)"\s+class="obj-nav\s+next"', content, re.IGNORECASE)
    
    if prev_match:
        result["prev_link"] = prev_match.group(1)
        result["prev_valid"] = (filepath.parent / result["prev_link"]).exists()
    
    if next_match:
        result["next_link"] = next_match.group(1)
        result["next_valid"] = (filepath.parent / result["next_link"]).exists()
    
    return result

def main():
    root = Path(__file__).resolve().parent
    
    print("=" * 60)
    print("OBJECT PAGES AUDIT REPORT")
    print("=" * 60)
    
    issues = []
    fixed_nav = 0
    
    # Audit main folder
    print("\n[MAIN FOLDER]")
    for page in OBJECT_PAGES:
        filepath = root / page
        result = audit_file(filepath, OBJECT_PAGES)
        
        if not result["exists"]:
            issues.append(f"MISSING: {page}")
            print(f"  FAIL {page} - FILE DOES NOT EXIST")
            continue
        
        status = "OK" if result["prev_valid"] and result["next_valid"] else "FAIL"
        print(f"  {status} {page}")
        print(f"      prev: {result['prev_link']} {'OK' if result['prev_valid'] else 'FAIL'}")
        print(f"      next: {result['next_link']} {'OK' if result['next_valid'] else 'FAIL'}")
        
        if not result["prev_valid"]:
            issues.append(f"BROKEN PREV: {page} -> {result['prev_link']}")
        if not result["next_valid"]:
            issues.append(f"BROKEN NEXT: {page} -> {result['next_link']}")
        if result["prev_valid"] and result["next_valid"]:
            fixed_nav += 1
    
    # Audit domo2 folder
    domo2 = root / "domo2"
    if domo2.exists():
        print("\n[DOMO2 FOLDER]")
        for page in OBJECT_PAGES:
            filepath = domo2 / page
            result = audit_file(filepath, OBJECT_PAGES)
            
            if not result["exists"]:
                if page in ["sad-gargoyle.html", "key.html"]:
                    print(f"  ! {page} - Optional file not in domo2")
                else:
                    print(f"  ✗ {page} - FILE DOES NOT EXIST")
                continue
            
            status = "OK" if result["prev_valid"] and result["next_valid"] else "FAIL"
            print(f"  {status} {page}")
            
            if not result["prev_valid"]:
                issues.append(f"DOMO2 BROKEN PREV: {page} -> {result['prev_link']}")
            if not result["next_valid"]:
                issues.append(f"DOMO2 BROKEN NEXT: {page} -> {result['next_link']}")
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Object pages in loop: {len(OBJECT_PAGES)}")
    print(f"Navigation fixed: {fixed_nav}/{len(OBJECT_PAGES)}")
    
    if issues:
        print(f"\nIssues found: {len(issues)}")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✓ No issues found! All navigation links are valid.")
    
    # Verify loop integrity
    print("\n" + "=" * 60)
    print("LOOP INTEGRITY CHECK")
    print("=" * 60)
    
    loop_ok = True
    for i, page in enumerate(OBJECT_PAGES):
        filepath = root / page
        if not filepath.exists():
            continue
        
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        prev_match = re.search(r'<a\s+href="([^"]+)"\s+class="obj-nav\s+prev"', content, re.IGNORECASE)
        next_match = re.search(r'<a\s+href="([^"]+)"\s+class="obj-nav\s+next"', content, re.IGNORECASE)
        
        if prev_match and next_match:
            prev_page = prev_match.group(1)
            next_page = next_match.group(1)
            
            expected_prev = OBJECT_PAGES[i - 1] if i > 0 else OBJECT_PAGES[-1]
            expected_next = OBJECT_PAGES[i + 1] if i < len(OBJECT_PAGES) - 1 else OBJECT_PAGES[0]
            
            if prev_page == expected_prev and next_page == expected_next:
                print(f"  ✓ {page} -> prev={prev_page}, next={next_page}")
            else:
                print(f"  ✗ {page} -> prev={prev_page} (expected {expected_prev}), next={next_page} (expected {expected_next})")
                loop_ok = False
    
    if loop_ok:
        print("\n✓ Navigation loop is correctly configured!")
    else:
        print("\n✗ Navigation loop has issues!")

if __name__ == "__main__":
    main()
