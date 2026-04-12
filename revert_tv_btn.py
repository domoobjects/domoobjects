#!/usr/bin/env python3
"""
Remove the TV nav button <li> from the 7 files that still have it.
Uses regex keyed on id="tv-nav-btn" to avoid quote-escaping mismatches.
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    'index.html', 'checkout.html', 'sad-gargoyle.html',
    'grey-piggy-bank.html', 'the-pin.html', 'paper-boat.html', 'crocodile.html',
]

# Matches the entire <li ...><button id="tv-nav-btn" ...>...</button></li>
# Works regardless of quote style or === vs ==
BTN_PATTERN = re.compile(
    r'\n?\s*<li[^>]*>\s*<button\s+id="tv-nav-btn".*?</button>\s*</li>',
    re.DOTALL
)

for fname in FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'SKIP (not found): {fname}')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'tv-nav-btn' not in content:
        print(f'SKIP (no button): {fname}')
        continue

    new_content, count = BTN_PATTERN.subn('', content)
    if count:
        print(f'FIXED ({count} button removed): {fname}')
    else:
        print(f'WARNING (pattern not matched): {fname}')

    # Final check
    remaining = [t for t in ['tv-nav-btn', 'toggleTvMode', 'tv-mode', 'domo-tv-mode'] if t in new_content]
    if remaining:
        print(f'  WARNING traces still found: {remaining}')
    else:
        print(f'  Clean')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Done.')
