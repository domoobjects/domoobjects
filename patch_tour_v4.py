with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken hardCleanup-before-check pattern with:
# "if already toured, clean up residual static elements and exit"
old_header = """(function(){

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
  if (localStorage.getItem('domo-toured')) return;"""

new_header = """(function(){

  // ── If already toured: remove residual static elements and exit ──
  if (localStorage.getItem('domo-toured')) {
    var _el;
    _el = document.getElementById('domoTourOverlay'); if (_el) _el.remove();
    _el = document.getElementById('tCard');           if (_el) _el.remove();
    _el = document.getElementById('tArrowSvg');       if (_el) _el.remove();
    document.body.style.overflow = '';
    document.body.style.pointerEvents = '';
    var _navEls = document.querySelectorAll('#mainNav a, #mainNav button, #mainNav img, #mainNav li, #mainNav .nav-logo');
    _navEls.forEach(function(n) {
      n.style.removeProperty('z-index');
      n.style.removeProperty('opacity');
      n.style.removeProperty('color');
    });
    return;
  }"""

assert old_header in content, 'OLD HEADER NOT FOUND'

content = content.replace(old_header, new_header, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
