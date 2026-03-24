import re

filepath = "C:/Users/aayus/Downloads/work/DOMO/domo_final (35)/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

# ── 1. Font import line 11 (index 10) ──
lines[10] = '  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400&family=Playfair+Display:wght@400;700;900&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">\n'

# ── 2. Replace nav CSS block lines 35-89 (index 34-88) ──
new_nav_css = """    /* ─── PERMANENT NAV BAR ─── */
    #mainNav {
      position: fixed;
      top: 0; left: 0; right: 0;
      height: 52px;
      background: #0d0d0b;
      border-bottom: 0.5px solid #1e1e1c;
      z-index: 200;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
    }
    .nav-logo {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 18px;
      letter-spacing: 6px;
      color: #d4d4cc;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
      line-height: 1;
    }
    .nav-center {
      display: flex;
      align-items: center;
      gap: 32px;
      list-style: none;
    }
    .nav-center a,
    .nav-center .nav-link {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 9px;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: #4a4a46;
      text-decoration: none;
      transition: color 0.15s;
      cursor: pointer;
      background: none;
      border: none;
    }
    .nav-center a:hover,
    .nav-center .nav-link:hover { color: #d4d4cc; }
    .nav-cart {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 9px;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: #4a4a46;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
      transition: color 0.15s;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .nav-cart:hover { color: #d4d4cc; }

    /* ─── NAV PANEL ─── */
    #navPanel {
      position: fixed;
      top: 52px;
      left: 0; right: 0;
      height: calc(100vh - 52px);
      background: #0d0d0b;
      z-index: 100;
      clip-path: circle(0% at 36px 26px);
      transition: clip-path 650ms cubic-bezier(0.87, 0, 0.13, 1);
      display: grid;
      grid-template-columns: 55% 45%;
    }
    #navPanel.is-open {
      clip-path: circle(150% at 36px 26px);
    }

    /* close button */
    .panel-close {
      position: absolute;
      top: 28px;
      right: 28px;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 9px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #3a3a38;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
      transition: color 0.15s;
      z-index: 2;
    }
    .panel-close:hover { color: #d4d4cc; }

    /* Left column */
    .panel-left {
      padding: 60px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-right: 0.5px solid #1e1e1c;
    }
    .panel-links {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .panel-link {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 78px;
      letter-spacing: 3px;
      color: #1e1e1c;
      text-decoration: none;
      display: flex;
      align-items: baseline;
      gap: 18px;
      line-height: 1;
      transition: color 0.2s;
    }
    .panel-link:hover { color: #d4d4cc; }
    .panel-link:hover .panel-idx { color: #3a3a38; }
    .panel-idx {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 9px;
      letter-spacing: 1px;
      color: #2a2a28;
      transition: color 0.2s;
      flex-shrink: 0;
      margin-bottom: 4px;
    }
    .panel-footer-text {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 9px;
      letter-spacing: 1.5px;
      color: #2a2a28;
      margin-top: auto;
      padding-top: 60px;
    }

    /* Right column */
    .panel-right {
      display: flex;
      flex-direction: column;
    }
    .panel-cell {
      flex: 1;
      padding: 40px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .panel-cell + .panel-cell {
      border-top: 0.5px solid #1e1e1c;
    }
    .cell-eyebrow {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 8px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #3a3a38;
      display: block;
      margin-bottom: 0;
    }
    .cell-redline {
      width: 18px;
      height: 0.5px;
      background: #c1121f;
      margin: 16px 0;
      flex-shrink: 0;
    }
    .cell-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 48px;
      color: #d4d4cc;
      line-height: 0.9;
      letter-spacing: 2px;
      margin-bottom: 18px;
    }
    .cell-article {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 9px;
      letter-spacing: 0.5px;
      color: #2a2a28;
      line-height: 1.9;
    }
    .cell-arrow {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 11px;
      color: #2a2a28;
      text-decoration: none;
      display: inline-block;
      margin-top: auto;
      padding-top: 20px;
      transition: color 0.15s, transform 0.15s;
    }
    .cell-arrow:hover {
      color: #888;
      transform: translateX(4px);
    }
    /* Inside the Box cell */
    .cell-box { cursor: none; }
    .cell-content {
      position: absolute;
      inset: 0;
      padding: 40px;
      display: flex;
      flex-direction: column;
    }
    .cell-overlay {
      position: absolute;
      inset: 0;
      background: #0d0d0b;
      pointer-events: none;
    }
"""
lines[34:89] = [new_nav_css]

content = "".join(lines)

# ── 3. Replace old nav-cart-btn and brand CSS ──
# Replace nav-cart-btn lines with a comment (we have new .nav-cart class)
content = re.sub(
    r'\.nav-cart-btn\{[^\n]+\}\n\.nav-cart-btn:hover\{[^\n]+\}',
    '/* nav-cart-btn replaced by .nav-cart */',
    content
)
content = content.replace(
    '.brand{text-decoration:none;display:flex;align-items:center;}\n.brand-logo{height:58px;width:auto;display:block;}',
    '/* brand moved to #mainNav .nav-logo */'
)

# ── 4. Replace nav HTML (<!-- NAV --> to </nav>) ──
new_nav_html = """  <!-- NAV -->
  <nav id="mainNav">
    <button class="nav-logo" onclick="togglePanel()">DOMO</button>
    <ul class="nav-center">
      <li><a href="#objects">Objects</a></li>
      <li id="navLoginLink"><a href="login.html">Login</a></li><li id="navAvatar" style="display:none;position:relative;" onmouseenter="clearTimeout(window._ddT);this.querySelector('.nav-dropdown').style.display='flex'" onmouseleave="window._ddT=setTimeout(()=>this.querySelector('.nav-dropdown').style.display='none',320)" ondblclick="window.location.href='profile.html'"><div class="nav-avatar-btn"><div class="nav-avatar-circle"><span class="nav-avatar-initial">?</span></div></div><div class="nav-dropdown"><div class="nav-dropdown-top"><div class="nav-avatar-name">Name</div><div class="nav-avatar-email">email</div></div><a href="profile.html" class="nav-dd-link">&#9654; My Profile</a><button class="nav-dd-signout" onclick="doSignOut()">Sign Out</button></div></li>
    </ul>
    <button class="nav-cart" onclick="openCart()">Cart <span class="cart-badge hidden" id="cartBadge">0</span></button>
  </nav>

  <!-- NAV PANEL -->
  <div id="navPanel">
    <button class="panel-close" onclick="closePanel()">Close</button>

    <!-- Left column -->
    <div class="panel-left">
      <nav class="panel-links">
        <a href="domo-times.html" class="panel-link">
          <span class="panel-idx">01</span>DOMO Times
        </a>
        <a href="inside-the-box.html" class="panel-link">
          <span class="panel-idx">02</span>Inside The Box
        </a>
      </nav>
      <p class="panel-footer-text">Dept. of Misc. Objects</p>
    </div>

    <!-- Right column -->
    <div class="panel-right">
      <!-- Top cell: DOMO Times -->
      <div class="panel-cell cell-times">
        <span class="cell-eyebrow">Vol. 07 &#8212; Field Dispatch</span>
        <div class="cell-redline"></div>
        <h2 class="cell-title">DOMO<br>Times</h2>
        <p class="cell-article">Object #447 found in estate sale</p>
        <p class="cell-article">The last known cursed mirror</p>
        <p class="cell-article">Inventory drop &#8212; March 2026</p>
        <a href="domo-times.html" class="cell-arrow">&#8594;</a>
      </div>
      <!-- Bottom cell: Inside the Box -->
      <div class="panel-cell cell-box" id="cellBox">
        <div class="cell-content">
          <span class="cell-eyebrow">Classified Archive</span>
          <div class="cell-redline" style="background:#1e1e1c;"></div>
          <h2 class="cell-title">Inside<br>The Box</h2>
          <p class="cell-article">access_level / unknown</p>
          <p class="cell-article">contents / [redacted]</p>
          <p class="cell-article">authorised / pending</p>
          <a href="inside-the-box.html" class="cell-arrow">&#8594;</a>
        </div>
        <div class="cell-overlay" id="cellOverlay"></div>
      </div>
    </div>
  </div>"""

content = re.sub(
    r'  <!-- NAV -->\n  <nav>.*?</nav>',
    new_nav_html,
    content,
    flags=re.DOTALL
)

# ── 5. Add JS before </body> ──
panel_js = """
<script>
/* PANEL OPEN / CLOSE */
function togglePanel() {
  document.getElementById('navPanel').classList.toggle('is-open');
  document.body.style.overflow = document.getElementById('navPanel').classList.contains('is-open') ? 'hidden' : '';
}
function closePanel() {
  document.getElementById('navPanel').classList.remove('is-open');
  document.body.style.overflow = '';
}

/* FLASHLIGHT — Inside The Box cell */
(function() {
  var cell = document.getElementById('cellBox');
  var overlay = document.getElementById('cellOverlay');
  if (!cell || !overlay) return;
  cell.addEventListener('mousemove', function(e) {
    var r = cell.getBoundingClientRect();
    var x = (e.clientX - r.left).toFixed(1);
    var y = (e.clientY - r.top).toFixed(1);
    overlay.style.maskImage = 'radial-gradient(circle 80px at ' + x + 'px ' + y + 'px, transparent 0%, transparent 40%, #0d0d0b 100%)';
    overlay.style.webkitMaskImage = 'radial-gradient(circle 80px at ' + x + 'px ' + y + 'px, transparent 0%, transparent 40%, #0d0d0b 100%)';
  });
  cell.addEventListener('mouseleave', function() {
    overlay.style.maskImage = '';
    overlay.style.webkitMaskImage = '';
  });
})();
</script>
"""
content = content.replace('</body>', panel_js + '</body>')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
