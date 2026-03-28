with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Extend restorePrev() to also remove text-shadow and filter ──
old_restore = """  function restorePrev() {
    if (prevEl) {
      prevEl.style.removeProperty('z-index');
      prevEl.style.removeProperty('opacity');
      prevEl.style.removeProperty('color');
      prevEl = null;
    }
  }"""

new_restore = """  function restorePrev() {
    if (prevEl) {
      prevEl.style.removeProperty('z-index');
      prevEl.style.removeProperty('opacity');
      prevEl.style.removeProperty('color');
      prevEl.style.removeProperty('text-shadow');
      prevEl.style.removeProperty('filter');
      prevEl = null;
    }
  }

  function applyGlow (el, s) {
    if (!el) return;
    if (s === 2) {
      // DOMO logo img — use filter drop-shadow
      el.style.filter  = 'drop-shadow(0 0 8px rgba(193,18,31,0.9)) drop-shadow(0 0 20px rgba(193,18,31,0.5)) drop-shadow(0 0 35px rgba(193,18,31,0.3))';
      el.style.opacity = '1';
    } else {
      // LOGIN / OBJECTS text links — use text-shadow
      el.style.textShadow = '0 0 12px rgba(193,18,31,0.9), 0 0 24px rgba(193,18,31,0.5), 0 0 40px rgba(193,18,31,0.3)';
      el.style.color      = '#ffffff';
    }
  }"""

assert old_restore in content, 'restorePrev not found'
content = content.replace(old_restore, new_restore, 1)

# ── 2. Call applyGlow after elevate in renderStep ──
old_render = """  function renderStep (s) {
    var st = steps[s];
    var el = st.getEl();
    elevate(el);
    var r = getRect(el);"""

new_render = """  function renderStep (s) {
    var st = steps[s];
    var el = st.getEl();
    elevate(el);
    applyGlow(el, s);
    var r = getRect(el);"""

assert old_render in content, 'renderStep not found'
content = content.replace(old_render, new_render, 1)

# ── 3. Extend final navEls sweep in endTour to also strip text-shadow and filter ──
old_sweep = """        navEls.forEach(function(n) {
          n.style.removeProperty('z-index');
          n.style.removeProperty('opacity');
          n.style.removeProperty('color');
        });"""

new_sweep = """        navEls.forEach(function(n) {
          n.style.removeProperty('z-index');
          n.style.removeProperty('opacity');
          n.style.removeProperty('color');
          n.style.removeProperty('text-shadow');
          n.style.removeProperty('filter');
        });"""

assert old_sweep in content, 'navEls sweep in endTour not found'
content = content.replace(old_sweep, new_sweep, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
