with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── FIX 2: Replace elevate() — save/restore z-index + opacity + color ──
old_elevate = """  function elevate (el) {
    if (prevEl) { prevEl.style.zIndex = prevZ; }
    if (el) {
      prevZ = el.style.zIndex;
      el.style.zIndex = '1001';
      el.style.position = el.style.position || 'relative';
    }
    prevEl = el;
  }"""

new_elevate = """  var prevOpacity = '';
  var prevColor   = '';

  function elevate (el) {
    if (prevEl) {
      prevEl.style.zIndex   = prevZ;
      prevEl.style.opacity  = prevOpacity;
      prevEl.style.color    = prevColor;
    }
    if (el) {
      prevZ       = el.style.zIndex;
      prevOpacity = el.style.opacity;
      prevColor   = el.style.color;
      el.style.position = el.style.position || 'relative';
      el.style.zIndex   = '1001';
      el.style.opacity  = '1';
      el.style.color    = '#ffffff';
    }
    prevEl = el;
  }"""

# ── FIX 1: Replace endTour() — use .remove(), restore all state cleanly ──
old_endTour = """  function endTour () {
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
  }"""

new_endTour = """  function endTour () {
    // Fade out card and arrow first
    card.classList.remove('t-show');
    svgEl.classList.remove('t-show');
    // Restore all elevated element styles
    if (prevEl) {
      prevEl.style.zIndex   = prevZ;
      prevEl.style.opacity  = prevOpacity;
      prevEl.style.color    = prevColor;
      prevEl = null;
    }
    // Remove event listener immediately so no further clicks fire
    document.removeEventListener('click', onClick);
    localStorage.setItem('domo-toured', 'true');
    // After card fades (200ms), fade overlay then remove everything from DOM
    setTimeout(function () {
      overlay.classList.add('t-fade');
      setTimeout(function () {
        overlay.remove();
        card.remove();
        svgEl.remove();
        document.body.style.overflow = '';
      }, 650);
    }, 200);
  }"""

assert old_elevate in content, 'elevate() not found'
assert old_endTour in content,  'endTour() not found'

content = content.replace(old_elevate, new_elevate, 1)
content = content.replace(old_endTour, new_endTour, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
