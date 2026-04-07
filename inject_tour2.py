import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Revert nav z-index from 1001 back to 200 ──
content = content.replace(
    'z-index: 1001;\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      padding: 0 28px;',
    'z-index: 200;\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      padding: 0 28px;',
    1
)

# ── 2. Strip old tour CSS block ──
content = re.sub(
    r'\n/\* [─\-]+ DOMO ONBOARDING TOUR [─\-]+ \*/.*?(?=\n</style>)',
    '',
    content,
    flags=re.DOTALL
)

# ── 3. Strip old tour HTML + JS block ──
content = re.sub(
    r'\n<!-- DOMO ONBOARDING TOUR -->.*?(?=\n</body>)',
    '',
    content,
    flags=re.DOTALL
)

# ── 4. New tour CSS ──
new_css = """
/* ═══ DOMO ONBOARDING TOUR v2 ═══ */
#domoTourOverlay {
  position: fixed; inset: 0;
  background: rgba(10,10,9,0.92);
  z-index: 999;
  pointer-events: none;
  transition: opacity 600ms ease;
}
#domoTourOverlay.t-fade { opacity: 0; }

.t-card {
  position: fixed;
  z-index: 1002;
  width: 300px;
  background: rgba(10,10,9,0.88);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 0.5px solid rgba(193,18,31,0.35);
  padding: 24px 28px;
  font-family: 'IBM Plex Mono', monospace;
  pointer-events: none;
  opacity: 0;
  transition: opacity 180ms ease;
}
.t-card.t-show { opacity: 1; }

.t-ind {
  font-size: 8px;
  color: #c1121f;
  letter-spacing: 3px;
  font-weight: 700;
}
.t-msg {
  font-size: 11px;
  color: #d4d4cc;
  line-height: 1.9;
  margin-top: 10px;
}
.t-divider {
  border: none;
  border-top: 0.5px solid rgba(193,18,31,0.2);
  margin: 16px 0 12px;
}
.t-cta {
  font-size: 8px;
  color: #3a3a38;
  letter-spacing: 2px;
}

.t-arrow-svg {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1002;
  pointer-events: none;
  opacity: 0;
  transition: opacity 180ms ease;
  overflow: visible;
}
.t-arrow-svg.t-show { opacity: 1; }
"""

# ── 5. New tour HTML + JS ──
new_html_js = """
<!-- ═══ DOMO ONBOARDING TOUR v2 ═══ -->
<div id="domoTourOverlay"></div>
<div class="t-card" id="tCard">
  <div class="t-ind" id="tInd"></div>
  <div class="t-msg" id="tMsg"></div>
  <hr class="t-divider">
  <div class="t-cta" id="tCta"></div>
</div>
<svg class="t-arrow-svg" id="tArrowSvg" xmlns="http://www.w3.org/2000/svg"></svg>

<script>
(function(){
  if (localStorage.getItem('domo-toured')) return;

  var overlay = document.getElementById('domoTourOverlay');
  var card    = document.getElementById('tCard');
  var indEl   = document.getElementById('tInd');
  var msgEl   = document.getElementById('tMsg');
  var ctaEl   = document.getElementById('tCta');
  var svgEl   = document.getElementById('tArrowSvg');

  var step = 0;
  var busy = false;
  var prevEl = null;
  var prevZ  = '';

  var steps = [
    {
      ind: '01 / 03',
      msg: 'This is not a login. This is a clearance check. The department does not open its full archive to strangers. If you have been granted access \u2014 your credentials will unlock what most visitors never see. Objects with no public record. Dispatches that were never meant to be found. Enter if you have been expected.',
      cta: 'click anywhere to continue',
      getEl: function () {
        var links = document.querySelectorAll('#mainNav .nav-center a, #mainNav .nav-links a, #mainNav li a');
        for (var i = 0; i < links.length; i++) {
          if (links[i].textContent.trim().toUpperCase() === 'LOGIN') return links[i];
        }
        return document.getElementById('navLoginLink');
      },
      cardPos: function (r) {
        var cx = Math.min(window.innerWidth / 2 + 30, window.innerWidth - 316);
        var cy = r.bottom + 32;
        return { x: cx, y: cy };
      }
    },
    {
      ind: '02 / 03',
      msg: 'The collection. Forty seven objects recovered from estates, demolitions, forgotten inventories, and circumstances the department does not comment on. Each one has a file. Each file has a reckoning. Click OBJECTS and begin. Some of what you find will be uncomfortable. The department considers this a feature not a flaw.',
      cta: 'click anywhere to continue',
      getEl: function () {
        var links = document.querySelectorAll('#mainNav .nav-center a, #mainNav .nav-links a, #mainNav li a');
        for (var i = 0; i < links.length; i++) {
          if (links[i].textContent.trim().toUpperCase() === 'OBJECTS') return links[i];
        }
        return null;
      },
      cardPos: function (r) {
        var cx = Math.max(12, window.innerWidth / 2 - 360);
        var cy = r.bottom + 32;
        return { x: cx, y: cy };
      }
    },
    {
      ind: '03 / 03',
      msg: 'The seal of the department. Click it and the archive expands \u2014 DOMO Times carries field dispatches and object obituaries from operatives in the field. Inside the Box holds what the department has not yet decided to release to the public. This mark is not decoration. It is an entrance. It has always been an entrance.',
      cta: 'click anywhere to enter the department',
      getEl: function () {
        return document.getElementById('brand-logo-img')
          || document.querySelector('#mainNav img')
          || document.querySelector('#mainNav .nav-logo');
      },
      cardPos: function (r) {
        var cx = r.right + 24;
        if (cx + 300 > window.innerWidth) cx = r.left - 24 - 300;
        cx = Math.max(12, cx);
        var cy = r.bottom + 28;
        return { x: cx, y: cy };
      }
    }
  ];

  function getRect (el) {
    if (!el) return { left: 100, top: 20, right: 160, bottom: 50, width: 60, height: 30 };
    return el.getBoundingClientRect();
  }

  function elevate (el) {
    if (prevEl) { prevEl.style.zIndex = prevZ; }
    if (el) {
      prevZ = el.style.zIndex;
      el.style.zIndex = '1001';
      el.style.position = el.style.position || 'relative';
    }
    prevEl = el;
  }

  function drawArrow (x1, y1, x2, y2) {
    var vw = window.innerWidth, vh = window.innerHeight;
    svgEl.setAttribute('viewBox', '0 0 ' + vw + ' ' + vh);
    var dx = x2 - x1, dy = y2 - y1;
    var len = Math.sqrt(dx * dx + dy * dy) || 1;
    var ux = dx / len, uy = dy / len;
    var ah = 7;
    var ax = x2 - ux * ah - uy * ah * 0.5;
    var ay = y2 - uy * ah + ux * ah * 0.5;
    var bx = x2 - ux * ah + uy * ah * 0.5;
    var by = y2 - uy * ah - ux * ah * 0.5;
    svgEl.innerHTML =
      '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="#c1121f" stroke-width="1"/>'
      + '<polygon points="' + x2 + ',' + y2 + ' ' + ax + ',' + ay + ' ' + bx + ',' + by + '" fill="#c1121f"/>';
  }

  function renderStep (s) {
    var st = steps[s];
    var el = st.getEl();
    elevate(el);
    var r = getRect(el);
    var pos = st.cardPos(r);

    // clamp card
    var cw = 300;
    pos.x = Math.max(12, Math.min(window.innerWidth - cw - 12, pos.x));
    pos.y = Math.max(90, Math.min(window.innerHeight - 220, pos.y));

    card.style.left = pos.x + 'px';
    card.style.top  = pos.y + 'px';

    indEl.textContent = st.ind;
    msgEl.textContent = st.msg;
    ctaEl.textContent = st.cta;

    // Arrow: from card top-center toward element center
    var arrowSrcX = pos.x + cw / 2;
    var arrowSrcY = pos.y;
    var arrowDstX = r.left + r.width / 2;
    var arrowDstY = r.bottom;
    drawArrow(arrowSrcX, arrowSrcY, arrowDstX, arrowDstY);

    card.classList.add('t-show');
    svgEl.classList.add('t-show');
  }

  function endTour () {
    card.classList.remove('t-show');
    svgEl.classList.remove('t-show');
    if (prevEl) { prevEl.style.zIndex = prevZ; prevEl = null; }
    setTimeout(function () {
      overlay.classList.add('t-fade');
      setTimeout(function () {
        overlay.parentNode && overlay.parentNode.removeChild(overlay);
        card.parentNode && card.parentNode.removeChild(card);
        svgEl.parentNode && svgEl.parentNode.removeChild(svgEl);
        document.body.style.overflow = '';
        document.removeEventListener('click', onClick);
      }, 620);
    }, 200);
    localStorage.setItem('domo-toured', 'true');
  }

  function onClick () {
    if (busy) return;
    if (step >= steps.length - 1) {
      endTour();
      return;
    }
    busy = true;
    card.classList.remove('t-show');
    svgEl.classList.remove('t-show');
    setTimeout(function () {
      step++;
      renderStep(step);
      busy = false;
    }, 190);
  }

  // Start
  document.body.style.overflow = 'hidden';
  renderStep(0);
  document.addEventListener('click', onClick);
})();
</script>
"""

# Inject CSS before </style> closing the nav block
anchor = '/* brand moved to #mainNav .nav-logo */\n</style>'
content = content.replace(anchor, '/* brand moved to #mainNav .nav-logo */' + new_css + '\n</style>', 1)

# Inject HTML+JS before </body>
content = content.replace('</body>', new_html_js + '\n</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
