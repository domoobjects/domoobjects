#!/usr/bin/env python3
"""
Fix: add background-image to html.tv-mode #tv-scene so the living-room image
is applied via CSS (not just the <img> element). The #050405 stays as fallback.
Only the one CSS rule is changed. Nothing else is touched.
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

OLD = "html.tv-mode #tv-scene{position:fixed;inset:0;z-index:99999;background:#050405;overflow:hidden;pointer-events:none;}"
NEW = "html.tv-mode #tv-scene{position:fixed;inset:0;z-index:99999;background:#050405 url('tv-room.jpg') center/cover no-repeat;overflow:hidden;pointer-events:none;}"

for fname in FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'  SKIP (not found): {fname}')
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if OLD not in content:
        print(f'  SKIP (pattern not found): {fname}')
        continue
    content = content.replace(OLD, NEW)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  FIXED: {fname}')

print('Done.')
