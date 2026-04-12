#!/usr/bin/env python3
"""
Full revert of TV mode from all 16 files.

REMOVES:
1. The entire <!-- TV MODE --> style+script block from all 16 files.
2. The <li><button id="tv-nav-btn"> HTML element from nav in files that have it.

DOES NOT TOUCH anything else.
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    'index.html', 'door.html', 'login.html', 'signup.html',
    'profile.html', 'id.html', 'orders.html', 'activity.html',
    'checkout.html', 'dispatch.html', 'error.html',
    'sad-gargoyle.html', 'grey-piggy-bank.html',
    'the-pin.html', 'paper-boat.html', 'crocodile.html',
]

# The TV button <li> element — identical string in every file it appears in
TV_BTN_LI = (
    '<li style="display:flex;align-items:center;">'
    '<button id="tv-nav-btn" onclick="toggleTvMode()" title="TV Mode" '
    'style="background:none;border:none;cursor:pointer;padding:4px 6px;'
    'display:flex;align-items:center;color:#a8a8a2;transition:color 0.15s;" '
    'onmouseover="this.style.color=\'#ffffff\'" '
    'onmouseout="this.style.color=localStorage.getItem(\'domo-tv-mode\')==\'true\'?\'#ffffff\':\'#a8a8a2\'">'
    '<svg width="20" height="17" viewBox="0 0 20 17" fill="none" xmlns="http://www.w3.org/2000/svg">'
    '<rect x="0.6" y="3.6" width="18.8" height="11.8" rx="1.2" stroke="currentColor" stroke-width="1.2"/>'
    '<rect x="2.5" y="5.2" width="10.5" height="7.6" stroke="currentColor" stroke-width="0.9"/>'
    '<line x1="14.5" y1="7" x2="17.5" y2="7" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>'
    '<line x1="14.5" y1="9.2" x2="17.5" y2="9.2" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>'
    '<line x1="14.5" y1="11.4" x2="17.5" y2="11.4" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>'
    '<line x1="6.5" y1="3.6" x2="4.5" y2="0.6" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>'
    '<line x1="13.5" y1="3.6" x2="15.5" y2="0.6" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>'
    '</svg></button></li>'
)

def remove_tv_block(content):
    """Remove <!-- TV MODE --> ... </script> block."""
    # Matches from the newline before <!-- TV MODE --> to the closing </script>
    result = re.sub(
        r'\n<!-- TV MODE -->.*?</script>',
        '',
        content,
        flags=re.DOTALL
    )
    if result == content:
        print('    WARNING: TV MODE block not found')
    else:
        print('    Removed TV MODE style+script block')
    return result

def remove_tv_button(content, fname):
    """Remove the TV nav button <li> element if present."""
    if 'tv-nav-btn' not in content or TV_BTN_LI not in content:
        # No HTML button in this file (only JS reference — already gone after block removal)
        return content

    before = content
    # Case 1: indented on its own line (object pages, checkout)
    # Try removing with various indentation levels
    for indent in ['    ', '      ', '  ', '\t']:
        candidate = '\n' + indent + TV_BTN_LI
        if candidate in content:
            content = content.replace(candidate, '')
            print(f'    Removed TV nav button (indented)')
            return content

    # Case 2: inline with no leading newline+indent (index.html)
    content = content.replace(TV_BTN_LI, '')
    if content != before:
        print(f'    Removed TV nav button (inline)')
    else:
        print(f'    WARNING: TV button found but removal pattern unclear in {fname}')
    return content

for fname in FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'SKIP (not found): {fname}')
        continue

    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    if '<!-- TV MODE -->' not in original and 'tv-nav-btn' not in original:
        print(f'SKIP (no TV traces): {fname}')
        continue

    print(f'Processing: {fname}')
    content = original
    content = remove_tv_block(content)
    content = remove_tv_button(content, fname)

    # Sanity check — no TV traces should remain
    remaining = [t for t in ['<!-- TV MODE -->', 'tv-nav-btn', 'toggleTvMode', 'tv-scene', 'tv-screen', 'tv-mode', 'domo-tv-mode'] if t in content]
    if remaining:
        print(f'    WARNING: traces still found: {remaining}')
    else:
        print(f'    Clean — no TV traces remain')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('\nDone.')
