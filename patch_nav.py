import re

filepath = "C:/Users/aayus/Downloads/work/DOMO/domo_final (35)/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

# ── 1. Font import (line 11, index 10) ──
lines[10] = '  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:ital,wght@0,300;0,400;1,300&family=Playfair+Display:wght@400;700;900&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">\n'

# ── 2. Nav CSS block: replace lines 35-89 (index 34-88) ──
new_nav_css = """    /* ─── NAV ─── */
    #mainNav {
      position: fixed;
      top: 0; left: 0; right: 0;
      z-index: 1001;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 34px 52px;
    }
    .brand-text {
      font-family: 'DM Mono', monospace;
      font-size: 12px;
      font-weight: 400;
      letter-spacing: 0.24em;
      color: #d4d4cc;
      text-decoration: none;
      text-transform: uppercase;
    }
    .menu-btn {
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      font-weight: 300;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: #d4d4cc;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
      transition: opacity 0.2s;
    }
    .menu-btn:hover { opacity: 0.5; }

    /* ─── MENU OVERLAY ─── */
    .menu-overlay {
      position: fixed;
      inset: 0;
      z-index: 1000;
      pointer-events: none;
      visibility: hidden;
    }
    .menu-overlay.is-open {
      pointer-events: all;
      visibility: visible;
    }
    .menu-bg {
      position: absolute;
      inset: 0;
      background: #0d0d0b;
      display: flex;
      opacity: 0;
      transition: opacity 0ms 580ms;
    }
    .menu-overlay.is-open .menu-bg {
      opacity: 1;
      transition: opacity 0ms 0ms;
    }
    .tear-panel {
      position: absolute;
      left: 0; right: 0;
      z-index: 2;
      overflow: hidden;
      transition: transform 0.72s cubic-bezier(0.76, 0, 0.24, 1);
    }
    .tear-top {
      top: 0; height: 50vh;
      transform: translateY(0);
    }
    .tear-bottom {
      bottom: 0; height: 50vh;
      transform: translateY(0);
    }
    .menu-overlay.is-open .tear-top  { transform: translateY(-102%); }
    .menu-overlay.is-open .tear-bottom { transform: translateY(102%); }
    .tear-fill {
      width: 100%;
      height: 100%;
      background: #0d0d0b;
    }
    .tear-top .tear-fill  { border-bottom: 0.5px solid rgba(212,212,204,0.08); }
    .tear-bottom .tear-fill { border-top: 0.5px solid rgba(212,212,204,0.08); }

    /* ─── MENU LAYOUT ─── */
    .menu-left {
      flex: 1;
      display: flex;
      align-items: center;
      padding: 80px;
    }
    .menu-main-links {
      display: flex;
      flex-direction: column;
    }
    .menu-main-links a {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(80px, 10vw, 138px);
      line-height: 0.88;
      color: rgba(212,212,204,0.10);
      text-decoration: none;
      letter-spacing: 0.01em;
      transition: color 0.15s ease;
      display: block;
    }
    .menu-main-links a:hover { color: #d4d4cc; }
    .menu-right {
      width: 38%;
      border-left: 0.5px solid rgba(212,212,204,0.12);
      display: flex;
      flex-direction: column;
      height: 100vh;
    }
    .menu-cell {
      flex: 1;
      padding: 52px 48px;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .cell-times { border-bottom: 0.5px solid rgba(212,212,204,0.12); }
    .cell-eyebrow {
      font-family: 'DM Mono', monospace;
      font-size: 9px;
      font-weight: 300;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: rgba(212,212,204,0.35);
      display: block;
      margin-bottom: 16px;
    }
    .cell-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 54px;
      line-height: 1;
      color: #d4d4cc;
      letter-spacing: 0.02em;
    }
    .cell-rule {
      width: 18px;
      height: 1px;
      background: #c1121f;
      margin: 20px 0;
      flex-shrink: 0;
    }
    .cell-articles {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      flex: 1;
    }
    .cell-articles li {
      font-family: 'DM Mono', monospace;
      font-size: 9px;
      font-weight: 300;
      letter-spacing: 0.09em;
      color: rgba(212,212,204,0.38);
      line-height: 1.55;
    }
    .cell-articles li::before { content: '-- '; color: rgba(212,212,204,0.18); }
    .cell-box {
      background: #000;
      cursor: none;
    }
    .cell-terminal {
      display: flex;
      flex-direction: column;
      gap: 8px;
      flex: 1;
    }
    .cell-terminal p {
      font-family: 'DM Mono', monospace;
      font-size: 10px;
      font-weight: 300;
      letter-spacing: 0.12em;
      color: rgba(212,212,204,0.15);
      line-height: 1.6;
    }
    .flashlight {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle 140px at var(--fx,-200px) var(--fy,-200px), transparent 0%, rgba(0,0,0,0.97) 100%);
      pointer-events: none;
    }
    .cell-arrow {
      font-family: 'DM Mono', monospace;
      font-size: 18px;
      color: #d4d4cc;
      text-decoration: none;
      opacity: 0.28;
      transition: opacity 0.15s;
      align-self: flex-end;
      margin-top: 20px;
      position: relative;
      z-index: 2;
    }
    .cell-arrow:hover { opacity: 1; }
    .menu-close {
      position: absolute;
      top: 34px;
      right: 52px;
      font-family: 'DM Mono', monospace;
      font-size: 11px;
      font-weight: 300;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: #d4d4cc;
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
      z-index: 3;
      opacity: 0;
      transition: opacity 0.18s 0.5s;
    }
    .menu-overlay.is-open .menu-close { opacity: 1; }
    .menu-close:hover { opacity: 0.4; }
"""
lines[34:89] = [new_nav_css]

content = "".join(lines)

# ── 3. Replace old brand CSS ──
content = content.replace(
    '.brand{text-decoration:none;display:flex;align-items:center;}\n.brand-logo{height:58px;width:auto;display:block;}',
    '/* brand moved to #mainNav */'
)

# ── 4. Replace nav HTML ──
new_nav_html = """  <!-- NAV -->
  <nav id="mainNav">
    <a href="index.html" class="brand-text">DOMO</a>
    <button class="menu-btn" id="menuBtn" onclick="openMenu()">Menu</button>
  </nav>

  <!-- MENU OVERLAY -->
  <div class="menu-overlay" id="menuOverlay">
    <div class="tear-panel tear-top"><div class="tear-fill"></div></div>
    <div class="tear-panel tear-bottom"><div class="tear-fill"></div></div>
    <div class="menu-bg">
      <div class="menu-left">
        <nav class="menu-main-links">
          <a href="#home" onclick="closeMenu()">Home</a>
          <a href="#objects" onclick="closeMenu()">Objects</a>
          <a href="login.html">Login</a>
          <a href="profile.html">Profile</a>
        </nav>
      </div>
      <div class="menu-right">
        <div class="menu-cell cell-times">
          <span class="cell-eyebrow">Vol. 07 &#8212; Field Dispatch</span>
          <h2 class="cell-title">DOMO<br>Times</h2>
          <div class="cell-rule"></div>
          <ul class="cell-articles">
            <li>Object #12 found dismembered in sector 9</li>
            <li>The catalogue grows: 3 new arrivals this quarter</li>
            <li>Editorial: Nothing happened here and we have proof</li>
          </ul>
          <a href="domo-times.html" class="cell-arrow">&#8594;</a>
        </div>
        <div class="menu-cell cell-box" id="cellBox">
          <div class="cell-terminal">
            <p>access_level / unknown</p>
            <p>contents / [redacted]</p>
            <p>status / awaiting clearance</p>
            <p>last_accessed / &#8212; &#8212; &#8212;</p>
            <p>package_count / 16</p>
          </div>
          <a href="inside-the-box.html" class="cell-arrow">&#8594;</a>
          <div class="flashlight" id="flashlight"></div>
        </div>
      </div>
      <button class="menu-close" onclick="closeMenu()">Close</button>
    </div>
  </div>"""

content = re.sub(
    r'  <!-- NAV -->\n  <nav>.*?</nav>',
    new_nav_html,
    content,
    flags=re.DOTALL
)

# ── 5. Add JS before </body> ──
menu_js = """
<script>
/* MENU TEAR */
function openMenu() {
  document.getElementById('menuOverlay').classList.add('is-open');
  document.body.style.overflow = 'hidden';
}
function closeMenu() {
  document.getElementById('menuOverlay').classList.remove('is-open');
  document.body.style.overflow = '';
}
/* FLASHLIGHT */
(function() {
  var cell = document.getElementById('cellBox');
  var light = document.getElementById('flashlight');
  if (!cell || !light) return;
  cell.addEventListener('mousemove', function(e) {
    var r = cell.getBoundingClientRect();
    var x = ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%';
    var y = ((e.clientY - r.top)  / r.height * 100).toFixed(1) + '%';
    light.style.setProperty('--fx', x);
    light.style.setProperty('--fy', y);
  });
  cell.addEventListener('mouseleave', function() {
    light.style.setProperty('--fx', '-200px');
    light.style.setProperty('--fy', '-200px');
  });
})();
</script>
"""
content = content.replace('</body>', menu_js + '</body>')

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
