content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Access Terminal - DOMO</title>
  <link rel="icon" type="image/png" href="favicon.png">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { width: 100%; height: 100%; background: #0d0d0b; overflow: hidden; }
    body { display: flex; align-items: center; justify-content: center; font-family: 'IBM Plex Mono', monospace; }
    #crtCanvas { position: fixed; inset: 0; width: 100vw; height: 100vh; z-index: 0; opacity: 0.18; }
    #scanlines { position: fixed; inset: 0; z-index: 1; background: repeating-linear-gradient(to bottom, transparent 0px, transparent 2px, rgba(0,0,0,0.08) 2px, rgba(0,0,0,0.08) 4px); pointer-events: none; }
    #vignette { position: fixed; inset: 0; z-index: 2; background: radial-gradient(ellipse at center, transparent 40%, rgba(0,0,0,0.55) 100%); pointer-events: none; }
    #redTint { position: fixed; inset: 0; z-index: 3; background: rgba(193,18,31,0.12); opacity: 0; pointer-events: none; }
    #glitchLine { position: fixed; left: 0; width: 100vw; height: 1px; background: rgba(255,255,255,0.15); z-index: 4; opacity: 0; pointer-events: none; transform: scaleX(0); transform-origin: left center; }
    #blackCover { position: fixed; inset: 0; background: #0d0d0b; z-index: 20; opacity: 0; pointer-events: none; }
    #loginCard { position: relative; z-index: 10; width: 380px; padding: 52px 48px; background: rgba(10,10,9,0.72); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 0.5px solid rgba(255,255,255,0.07); }
    .card-logo { display: block; height: 32px; width: auto; opacity: 0.5; margin: 0 auto 32px; }
    .card-heading { font-family: 'Bebas Neue', sans-serif; font-size: 28px; letter-spacing: 6px; color: #d4d4cc; text-align: center; display: block; margin-bottom: 6px; }
    .card-sub { font-size: 9px; letter-spacing: 2px; color: #3a3a38; text-align: center; display: block; margin-bottom: 40px; }
    .field { width: 100%; background: rgba(255,255,255,0.03); border: 0.5px solid #1e1e1c; color: #d4d4cc; font-family: 'IBM Plex Mono', monospace; font-size: 11px; padding: 14px 16px; outline: none; border-radius: 0; display: block; }
    .field::placeholder { color: #2a2a28; }
    .field:focus { border-color: #3a3a38; }
    .field + .field { margin-top: 12px; }
    .field-row { display: flex; align-items: center; justify-content: space-between; margin-top: 16px; }
    .remember-label { display: flex; align-items: center; gap: 6px; font-size: 8px; letter-spacing: 1px; color: #3a3a38; cursor: pointer; }
    .remember-label input[type=checkbox] { accent-color: #3a3a38; width: 10px; height: 10px; cursor: pointer; }
    .lost-access { font-size: 8px; letter-spacing: 1px; color: #3a3a38; text-decoration: none; transition: color 0.15s; cursor: pointer; }
    .lost-access:hover { color: #d4d4cc; }
    #submitBtn { display: block; width: 100%; margin-top: 32px; background: #d4d4cc; color: #0d0d0b; font-family: 'Bebas Neue', sans-serif; font-size: 16px; letter-spacing: 4px; padding: 14px; border: none; border-radius: 0; cursor: pointer; transition: background 0.15s, transform 0.1s; }
    #submitBtn:hover { background: #ffffff; }
    #submitBtn:active { transform: scale(0.98); }
    .card-footer { font-size: 8px; letter-spacing: 1px; color: #2a2a28; text-align: center; margin-top: 20px; display: block; }
    .card-footer .req { color: #2a2a28; cursor: pointer; transition: color 0.15s; }
    .card-footer .req:hover { color: #3a3a38; }
    #errorMsg { font-size: 9px; letter-spacing: 1px; color: #c1121f; margin-top: 10px; display: none; font-family: 'IBM Plex Mono', monospace; }
  </style>
</head>
<body>
<canvas id="crtCanvas"></canvas>
<div id="scanlines"></div>
<div id="vignette"></div>
<div id="redTint"></div>
<div id="glitchLine"></div>
<div id="blackCover"></div>
<div id="loginCard">
  <img src="favicon.png" class="card-logo" alt="DOMO"/>
  <span class="card-heading">Access Terminal</span>
  <span class="card-sub">Enter credentials to continue</span>
  <form id="loginForm" onsubmit="return handleSubmit(event)">
    <input id="emailField" class="field" type="text" placeholder="identifier" autocomplete="off"/>
    <input id="passwordField" class="field" type="password" placeholder="password" autocomplete="off"/>
    <div id="errorMsg">Signal rejected &mdash; try again</div>
    <div class="field-row">
      <label class="remember-label"><input type="checkbox"/> Remember signal</label>
      <span class="lost-access">Lost access?</span>
    </div>
    <button id="submitBtn" type="submit">Enter</button>
  </form>
  <span class="card-footer">No account? <span class="req">Request access</span></span>
</div>
<script>
var canvas = document.getElementById('crtCanvas');
var ctx = canvas.getContext('2d');
var redTint = document.getElementById('redTint');
var W, H, imgData;
var state = 'CALM';
var noiseMax = 80, targetMax = 80;
var canvasOpacity = 0.18, targetOpacity = 0.18;

function resize() {
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
  imgData = ctx.createImageData(W, H);
}
resize();
window.addEventListener('resize', resize);

function drawNoise() {
  var data = imgData.data;
  var max = noiseMax | 0;
  for (var i = 0; i < data.length; i += 4) {
    var v = (Math.random() * max) | 0;
    data[i] = data[i+1] = data[i+2] = v;
    data[i+3] = 255;
  }
  ctx.putImageData(imgData, 0, 0);
}

function loop() {
  requestAnimationFrame(loop);
  if (Math.abs(noiseMax - targetMax) > 0.3) noiseMax += (targetMax - noiseMax) * 0.04;
  else noiseMax = targetMax;
  if (Math.abs(canvasOpacity - targetOpacity) > 0.002) {
    canvasOpacity += (targetOpacity - canvasOpacity) * 0.06;
    canvas.style.opacity = canvasOpacity.toFixed(3);
  }
  drawNoise();
}
requestAnimationFrame(loop);

function setChaos() {
  if (state === 'CLEARING') return;
  state = 'CHAOS';
  targetMax = 255; targetOpacity = 0.65;
  canvas.style.filter = 'contrast(1.4)';
  redTint.style.transition = 'none';
  redTint.style.opacity = '1';
  setTimeout(function() { redTint.style.transition = 'opacity 400ms ease'; redTint.style.opacity = '0'; }, 800);
  setTimeout(function() { state = 'CALM'; targetMax = typingMax(); targetOpacity = 0.18; canvas.style.filter = ''; }, 1200);
}

function setClearing() {
  state = 'CLEARING';
  targetOpacity = 0; targetMax = 0;
  canvas.style.filter = '';
  var sl = document.getElementById('scanlines');
  var vg = document.getElementById('vignette');
  sl.style.transition = vg.style.transition = 'opacity 1200ms ease';
  sl.style.opacity = vg.style.opacity = '0';
  var card = document.getElementById('loginCard');
  setTimeout(function() { card.style.transition = 'opacity 400ms ease'; card.style.opacity = '0'; }, 1200);
  var cover = document.getElementById('blackCover');
  cover.style.pointerEvents = 'all';
  setTimeout(function() { cover.style.transition = 'opacity 300ms ease'; cover.style.opacity = '1'; }, 1600);
  setTimeout(function() { window.location.href = 'index.html'; }, 2000);
}

var charCount = 0, typingTimer = null, driftTimer = null;
function typingMax() { return Math.max(40, 80 - charCount * 1.5); }

function onType() {
  charCount++;
  if (state === 'CALM') targetMax = typingMax();
  document.getElementById('errorMsg').style.display = 'none';
  clearTimeout(typingTimer); clearInterval(driftTimer);
  typingTimer = setTimeout(function() {
    var start = noiseMax, end = 80, steps = 60, step = 0;
    driftTimer = setInterval(function() {
      step++;
      targetMax = start + (end - start) * (step / steps);
      if (step >= steps) { clearInterval(driftTimer); charCount = 0; }
    }, 2000 / steps);
  }, 3000);
}
document.getElementById('emailField').addEventListener('input', onType);
document.getElementById('passwordField').addEventListener('input', onType);

function handleSubmit(e) {
  e.preventDefault();
  var pw = document.getElementById('passwordField').value;
  if (pw === 'domo2024') { setClearing(); }
  else { setChaos(); document.getElementById('errorMsg').style.display = 'block'; }
  return false;
}

function scheduleFlicker() {
  setTimeout(function() {
    document.body.style.transition = 'opacity 40ms ease';
    document.body.style.opacity = '0.92';
    setTimeout(function() {
      document.body.style.opacity = '1';
      setTimeout(function() { document.body.style.transition = ''; scheduleFlicker(); }, 80);
    }, 40);
  }, 4000 + Math.random() * 4000);
}
scheduleFlicker();

var gl = document.getElementById('glitchLine');
function scheduleGlitch() {
  setTimeout(function() {
    gl.style.top = (Math.random() * window.innerHeight) + 'px';
    gl.style.transition = 'none';
    gl.style.opacity = '1';
    gl.style.transform = 'scaleX(0)';
    requestAnimationFrame(function() { requestAnimationFrame(function() {
      gl.style.transition = 'transform 200ms linear';
      gl.style.transform = 'scaleX(1)';
      setTimeout(function() {
        gl.style.transition = 'opacity 200ms ease';
        gl.style.opacity = '0';
        setTimeout(scheduleGlitch, 300);
      }, 200);
    }); });
  }, 6000 + Math.random() * 6000);
}
scheduleGlitch();
</script>
</body>
</html>"""

with open('C:/Users/aayus/Downloads/work/DOMO/domo_final (35)/login.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done.', len(content), 'chars')
