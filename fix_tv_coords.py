#!/usr/bin/env python3
"""
Two targeted fixes to TV mode across all 16 files:

1. CSS background-position: change 'center/cover' → 'top center / cover'
   The JS uses oY=0 (top-center anchor). CSS must match or the website
   appears ~30-50px too low — floating over the table, not the TV screen.

2. TV coordinates: TV_B=0.615 is wrong for 1536×1024 image.
   TV screen bottom is at ~y=550px → fraction ≈ 0.537.
   At 0.615 the site extends into the wooden TV housing below the screen.
   Also pull TV_T slightly up: 0.045 → 0.038 (tighter to screen top).

No other changes. Zero other files touched.
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    'index.html', 'door.html', 'login.html', 'signup.html',
    'profile.html', 'id.html', 'orders.html', 'activity.html',
    'checkout.html', 'dispatch.html', 'error.html',
    'sad-gargoyle.html', 'grey-piggy-bank.html',
    'the-pin.html', 'paper-boat.html', 'crocodile.html',
]

REPLACEMENTS = [
    # Fix 1: background-position mismatch (center → top center)
    (
        "background:#050405 url('tv-room.jpg') center/cover no-repeat",
        "background:#050405 url('tv-room.jpg') top center / cover no-repeat"
    ),
    # Fix 2: TV screen coordinates — correct T and B fractions
    (
        "var TV_L=0.075,TV_T=0.045,TV_R=0.925,TV_B=0.615;",
        "var TV_L=0.075,TV_T=0.038,TV_R=0.925,TV_B=0.540;"
    ),
]

for fname in FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'  SKIP (not found): {fname}')
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<!-- TV MODE -->' not in content:
        print(f'  SKIP (no TV block): {fname}')
        continue
    changed = 0
    for old, new in REPLACEMENTS:
        if old in content:
            content = content.replace(old, new)
            changed += 1
        else:
            print(f'  WARNING: pattern not found in {fname}: {repr(old[:50])}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  FIXED ({changed}/2): {fname}')

print('Done.')
