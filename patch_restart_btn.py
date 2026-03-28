with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Insert button HTML into panel-left, after footer text ──
old_panel_footer = """      <p class="panel-footer-text">Dept. of Misc. Objects</p>
    </div>

    <!-- Right column -->"""

new_panel_footer = """      <p class="panel-footer-text">Dept. of Misc. Objects</p>
      <button class="restart-tour-btn" onclick="restartTour()">restart orientation</button>
    </div>

    <!-- Right column -->"""

assert old_panel_footer in content, 'panel footer anchor not found'
content = content.replace(old_panel_footer, new_panel_footer, 1)

# ── 2. Add button CSS in a new <style> block before </head> ──
btn_css = """<style>
/* ── RESTART TOUR BUTTON ── */
.restart-tour-btn {
  background: none;
  border: 0.5px solid #2a2a28;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 9px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #2a2a28;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 0;
  display: block;
  margin-top: 24px;
  transition: border-color 180ms ease, color 180ms ease;
}
.restart-tour-btn:hover {
  border-color: #3a3a38;
  color: #3a3a38;
}
</style>
</head>"""

assert '</head>' in content, '</head> not found'
content = content.replace('</head>', btn_css, 1)

# ── 3. Add restartTour() function in a new <script> block before </body> ──
restart_script = """<script>
/* RESTART TOUR */
function restartTour() {
  // Step 1: close the panel
  closePanel();
  // Step 2: after panel animation (650ms), remove flag and re-run tour
  setTimeout(function () {
    localStorage.removeItem('domo-toured');
    // Re-inject tour elements if they were removed after a previous tour run
    if (!document.getElementById('domoTourOverlay')) {
      var ov = document.createElement('div');
      ov.id = 'domoTourOverlay';
      document.body.appendChild(ov);
    }
    if (!document.getElementById('tCard')) {
      var cd = document.createElement('div');
      cd.className = 't-card';
      cd.id = 'tCard';
      cd.innerHTML = '<div class="t-ind" id="tInd"></div><div class="t-msg" id="tMsg"></div><hr class="t-divider"><div class="t-cta" id="tCta"></div>';
      document.body.appendChild(cd);
    }
    if (!document.getElementById('tArrowSvg')) {
      var sv = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      sv.setAttribute('class', 't-arrow-svg');
      sv.id = 'tArrowSvg';
      sv.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      document.body.appendChild(sv);
    }
    // Clone and re-execute the tour script (the IIFE will see no flag and run)
    document.querySelectorAll('script').forEach(function (sc) {
      if (sc.textContent.indexOf('domoTourOverlay') > -1 && sc.textContent.indexOf('restorePrev') > -1) {
        var newSc = document.createElement('script');
        newSc.textContent = sc.textContent;
        document.body.appendChild(newSc);
      }
    });
  }, 650);
}
</script>
</body>"""

assert '</body>' in content, '</body> not found'
content = content.replace('</body>', restart_script, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
