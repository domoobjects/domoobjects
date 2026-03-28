import re, glob, os

base = 'C:/Users/aayus/Downloads/work/DOMO/domo_final (35)'
index_path = base + '/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    index = f.read()

# ── Extract nav CSS ──
css_match = re.search(
    r'(/\* ─── PERMANENT NAV BAR ─── \*/.*?\.cell-overlay \{[^}]*\})',
    index, re.DOTALL
)
nav_css = css_match.group(1).strip()

# ── Extract nav HTML (<!-- NAV --> through closing </div> of navPanel) ──
html_match = re.search(
    r'(  <!-- NAV -->.*?  </div>)\s*\n\s*(?:<!-- HERO|<section|<main|<div class="hero|<div id="hero)',
    index, re.DOTALL
)
nav_html = html_match.group(1).strip()

# ── Extract nav JS ──
js_match = re.search(
    r'(/\* PANEL OPEN / CLOSE \*/.*?}\)\(\);)',
    index, re.DOTALL
)
nav_js = js_match.group(1).strip()

# ── Font import ──
font_import = '  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400&family=Playfair+Display:wght@400;700;900&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">'

# ── Object pages only ──
object_pages = [
    'blue-toilet.html', 'bowling-pin.html', 'crocodile.html',
    'grey-piggy-bank.html', 'handcuff.html', 'key.html',
    'melting-skull.html', 'moai.html', 'movable-water-bed.html',
    'octopus.html', 'paper-boat.html', 'raven-skull.html',
    'red-blood-cell.html', 'sad-gargoyle.html', 'silence-after-scream.html',
    'sun.html', 'domo-times.html', 'domo-times-mar11.html',
    'domo-times-vol2.html', 'profile.html', 'checkout.html', 'login.html'
]

for fname in object_pages:
    fpath = base + '/' + fname
    if not os.path.exists(fpath):
        print(f'MISSING: {fname}')
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # ── Step 1: Remove ALL existing <nav>...</nav> blocks ──
    content = re.sub(r'\s*<nav\b[^>]*>.*?</nav>', '', content, flags=re.DOTALL)

    # ── Step 2: Remove existing navPanel div if present ──
    content = re.sub(r'\s*<!-- NAV PANEL -->.*?(?=\s*(?:<!-- HERO|<!-- MAIN|<section|<main|<div class="page|<div class="hero|<div id="hero|<div class="object))',
                     '', content, flags=re.DOTALL)
    # Also remove orphaned navPanel divs
    content = re.sub(r'\s*<div id="navPanel".*?(?=\s*(?:<!-- HERO|<!-- MAIN|<section|<main|<div class="page|<div class="hero|<div id="hero|<div class="object))',
                     '', content, flags=re.DOTALL)

    # ── Step 3: Remove old <!-- NAV --> comments ──
    content = re.sub(r'\s*<!-- NAV -->', '', content)

    # ── Step 4: Remove old nav CSS from style blocks ──
    content = re.sub(r'/\* ─── PERMANENT NAV BAR ─── \*/.*?\.cell-overlay \{[^}]*\}', '', content, flags=re.DOTALL)
    # Also remove old nav CSS patterns
    content = re.sub(r'/\* ─── DOMO NAV \(injected\) ─── \*/.*?(?=/\*|</style>)', '', content, flags=re.DOTALL)

    # ── Step 5: Remove old nav JS ──
    content = re.sub(r'/\* PANEL OPEN / CLOSE \*/.*?}\)\(\);', '', content, flags=re.DOTALL)
    content = re.sub(r'function togglePanel\(\).*?}\s*function closePanel\(\).*?}', '', content, flags=re.DOTALL)

    # ── Step 6: Ensure font import ──
    if 'Bebas+Neue' not in content:
        content = content.replace('</head>', font_import + '\n</head>', 1)

    # ── Step 7: Inject new nav CSS into style block ──
    css_injection = '\n    /* ─── PERMANENT NAV BAR ─── */\n    ' + nav_css.replace('\n', '\n    ') + '\n'
    content = content.replace('</style>', css_injection + '</style>', 1)

    # ── Step 8: Inject nav HTML right after <body> opening ──
    content = re.sub(
        r'(<body[^>]*>)',
        r'\1\n  ' + nav_html.replace('\\', '\\\\'),
        content, count=1
    )

    # ── Step 9: Inject nav JS before </body> ──
    nav_script = '\n<script>\n' + nav_js + '\n</script>\n'
    content = content.replace('</body>', nav_script + '</body>', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'DONE: {fname}')

print('\nAll pages updated.')
