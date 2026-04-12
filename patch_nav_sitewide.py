import re, glob, os

base = 'C:/Users/aayus/Downloads/work/DOMO/domo_final (35)'
index_path = base + '/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    index = f.read()

# ── Extract nav CSS block (from /* ─── PERMANENT NAV BAR ─── */ to end of .cell-overlay rule) ──
css_match = re.search(
    r'(/\* ─── PERMANENT NAV BAR ─── \*/.*?\.cell-overlay \{.*?\})',
    index, re.DOTALL
)
nav_css = css_match.group(1).strip() if css_match else ''
print(f"Nav CSS extracted: {len(nav_css)} chars")

# ── Extract nav HTML block (<!-- NAV --> through end of </div> for navPanel) ──
html_match = re.search(
    r'(  <!-- NAV -->.*?  </div>(?=\s*\n\s*<!-- HERO|\s*\n\s*<section|\s*\n\s*<main|\s*\n\s*<div class="hero|\s*\n\s*<div id="hero))',
    index, re.DOTALL
)
nav_html = html_match.group(1).strip() if html_match else ''
print(f"Nav HTML extracted: {len(nav_html)} chars")

# ── Extract nav JS (togglePanel, closePanel, flashlight block) ──
js_match = re.search(
    r'(/\* PANEL OPEN / CLOSE \*/.*?}\)\(\);)',
    index, re.DOTALL
)
nav_js = js_match.group(1).strip() if js_match else ''
print(f"Nav JS extracted: {len(nav_js)} chars")

# ── Font import line ──
font_import = '<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400&family=Playfair+Display:wght@400;700;900&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">'

# ── Target files (all except index.html, backups, patch scripts) ──
skip = {'index.html', 'index.html.bak', 'index.html.bak2', 'inside-the-box.html'}
all_html = [f for f in glob.glob(base + '/*.html') if '.bak' not in f]
target_files = [f for f in all_html if os.path.basename(f) not in skip]

results = []

for fpath in sorted(target_files):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # 1. Ensure font imports exist
    if 'Bebas+Neue' not in content or 'IBM+Plex+Mono' not in content:
        # Insert after existing <link rel="stylesheet"> or after <meta viewport>
        if font_import not in content:
            content = content.replace(
                '</head>',
                '  ' + font_import + '\n</head>',
                1
            )
            changed = True

    # 2. Remove old nav CSS and inject new
    # Remove any existing style block section for nav
    # Strategy: look for the nav CSS wrapped in a style tag and replace only the nav portion
    # Add new nav CSS into the page's <style> block if present
    if '/* ─── PERMANENT NAV BAR ─── */' not in content:
        # Inject nav CSS at end of first <style> block
        content = content.replace(
            '</style>',
            '\n    /* ─── DOMO NAV (injected) ─── */\n    ' + nav_css.replace('\n', '\n    ') + '\n</style>',
            1
        )
        changed = True
    else:
        # Update existing nav CSS block
        content = re.sub(
            r'/\* ─── PERMANENT NAV BAR ─── \*/.*?\.cell-overlay \{.*?\}',
            nav_css,
            content,
            flags=re.DOTALL
        )
        changed = True

    # 3. Remove old nav HTML and inject new
    # Patterns for old nav bars across various pages
    # Match from <!-- NAV --> or <nav ...> block to </nav>
    old_nav_pattern = re.compile(
        r'(\s*<!-- NAV -->)?\s*<nav\b[^>]*>.*?</nav>(\s*<!-- /NAV -->)?',
        re.DOTALL
    )

    if re.search(old_nav_pattern, content):
        content = old_nav_pattern.sub('\n  ' + nav_html, content, count=1)
        changed = True
    elif '<!-- NAV -->' in content:
        # nav HTML already injected via previous run
        pass

    # 4. Inject nav JS before </body> if not present
    if 'togglePanel' not in content:
        content = content.replace(
            '</body>',
            '<script>\n' + nav_js + '\n</script>\n</body>',
            1
        )
        changed = True
    elif nav_js and nav_js[:30] not in content:
        # Update existing nav JS
        content = re.sub(
            r'/\* PANEL OPEN / CLOSE \*/.*?}\)\(\);',
            nav_js,
            content,
            flags=re.DOTALL
        )
        changed = True

    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        results.append(f"  UPDATED: {fname}")
    else:
        results.append(f"  skipped: {fname}")

print('\n'.join(results))
print(f"\nDone. {len([r for r in results if 'UPDATED' in r])} files updated.")
