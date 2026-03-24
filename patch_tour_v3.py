with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_tour_js = """(function(){
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
  var prevZ  = '';"""

new_tour_js = """(function(){

  // ── HARD CLEANUP: runs on every load before anything else ──
  // Kills any leftover tour elements instantly regardless of state
  function hardCleanup() {
    var el;
    el = document.getElementById('domoTourOverlay'); if (el) el.remove();
    el = document.getElementById('tCard');           if (el) el.remove();
    el = document.getElementById('tArrowSvg');       if (el) el.remove();
    document.body.style.overflow = '';
    document.body.style.pointerEvents = '';
    // Strip inline tour styles from all nav elements
    var navEls = document.querySelectorAll('#mainNav a, #mainNav button, #mainNav img, #mainNav li, #mainNav .nav-logo');
    navEls.forEach(function(n) {
      n.style.removeProperty('z-index');
      n.style.removeProperty('opacity');
      n.style.removeProperty('color');
    });
  }
  hardCleanup();

  // ── Tour only runs if flag is not set ──
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
  var prevZ  = '';"""

old_elevate = """  function elevate (el) {
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

new_elevate = """  function restorePrev() {
    if (prevEl) {
      prevEl.style.removeProperty('z-index');
      prevEl.style.removeProperty('opacity');
      prevEl.style.removeProperty('color');
      prevEl = null;
    }
  }

  function elevate (el) {
    restorePrev();
    if (el) {
      el.style.position = el.style.position || 'relative';
      el.style.zIndex   = '1001';
      el.style.opacity  = '1';
      el.style.color    = '#ffffff';
    }
    prevEl = el;
  }"""

old_endTour = """  function endTour () {
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

new_endTour = """  function endTour () {
    // Set flag IMMEDIATELY before any animation — survives mid-fade refresh
    localStorage.setItem('domo-toured', 'true');
    // Kill click handler instantly
    document.removeEventListener('click', onClick);
    // Fade out card and arrow
    card.classList.remove('t-show');
    svgEl.classList.remove('t-show');
    // Restore elevated nav element using removeProperty (no residual inline styles)
    restorePrev();
    // Fade overlay, then nuke everything from DOM
    setTimeout(function () {
      overlay.classList.add('t-fade');
      setTimeout(function () {
        overlay.remove();
        card.remove();
        svgEl.remove();
        // Final hard cleanup: body state + any nav inline styles
        document.body.style.overflow = '';
        document.body.style.pointerEvents = '';
        var navEls = document.querySelectorAll('#mainNav a, #mainNav button, #mainNav img, #mainNav li, #mainNav .nav-logo');
        navEls.forEach(function(n) {
          n.style.removeProperty('z-index');
          n.style.removeProperty('opacity');
          n.style.removeProperty('color');
        });
      }, 650);
    }, 180);
  }"""

assert old_tour_js in content,  'tour JS header not found'
assert old_elevate in content,   'elevate() not found'
assert old_endTour in content,   'endTour() not found'

# Also remove the now-unused prevOpacity/prevColor variable declarations
old_prev_vars = """  var prevOpacity = '';
  var prevColor   = '';

  function elevate"""
new_prev_vars = """  function elevate"""

content = content.replace(old_tour_js,   new_tour_js,   1)
content = content.replace(old_elevate,   new_elevate,   1)
content = content.replace(old_endTour,   new_endTour,   1)
content = content.replace(old_prev_vars, new_prev_vars, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
