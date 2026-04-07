import re, os

base = 'C:/Users/aayus/Downloads/work/DOMO/domo_final (35)'
fpath = base + '/index.html'

with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the objects-grid boundaries
grid_start = content.index('<div class="objects-grid">')
grid_end   = content.index('</div>', grid_start) # first closing div after grid open

# We need to find the MATCHING closing div for objects-grid
# Count nested divs
depth = 0
i = grid_start
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
        i += 4
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            grid_end = i + 6
            break
        i += 6
    else:
        i += 1

grid_inner_start = content.index('>', grid_start) + 1
grid_content = content[grid_inner_start:grid_end - 6]  # content inside objects-grid

# Split grid into individual items
# Each item is an <a href="...">...</a> block OR a standalone element
# Find all top-level items by matching <a ...>...</a> blocks
items = re.findall(r'<a\s+href="([^"]*)"[^>]*>.*?</a>', grid_content, re.DOTALL)

# Parse each item as a full block with its href
item_blocks = re.findall(r'(<a\s+href="[^"]*"[^>]*>.*?</a>)', grid_content, re.DOTALL)

# Also find items NOT wrapped in <a> (no href - standalone divs/buttons)
# These are object-card divs not preceded by <a href
no_link_blocks = re.findall(
    r'(?<!href=")[^\S\n]*<div class="object-card"[^>]*>.*?</div>',
    grid_content, re.DOTALL
)

print(f"Items with href: {len(item_blocks)}")
print(f"Items without href (approximate): {len(no_link_blocks)}")

# Process linked items: keep only those with existing files, first occurrence only
seen_hrefs = set()
kept_items = []
removed = []

for block in item_blocks:
    href_match = re.search(r'href="([^"]*)"', block)
    if not href_match:
        removed.append(('no-href', block[:60]))
        continue
    href = href_match.group(1)
    # Check file exists
    if not os.path.exists(base + '/' + href):
        removed.append(('missing-file: ' + href, block[:60]))
        continue
    # Check duplicate
    if href in seen_hrefs:
        removed.append(('duplicate: ' + href, block[:60]))
        continue
    seen_hrefs.add(href)
    kept_items.append(block)

print(f"\nKept: {len(kept_items)}")
print(f"Removed: {len(removed)}")
for r in removed:
    print(f"  - {r[0]}")

# Rebuild grid content with only kept items
new_grid_content = '\n        '.join(kept_items)
new_grid = '<div class="objects-grid">\n        ' + new_grid_content + '\n    </div>'

# Replace old grid in content
old_grid = content[grid_start:grid_end]
content = content.replace(old_grid, new_grid, 1)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone. index.html updated.")
