with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Bump #mainNav z-index from 200 to 1001 so it sits above the overlay
content = content.replace('z-index: 200;\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      padding: 0 28px;', 'z-index: 1001;\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      padding: 0 28px;', 1)

tour_css = """
/* ── DOMO ONBOARDING TOUR ── */
#tourOverlay {
  position: fixed;
  inset: 0;
  background: rgba(180, 10, 10, 0.18);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  z-index: 999;
  pointer-events: none;
  transition: opacity 500ms ease;
}
#tourOverlay.fade-out {
  opacity: 0;
}
.tour-card {
  position: fixed;
  z-index: 1000;
  background: rgba(10, 10, 9, 0.82);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 0.5px solid rgba(193, 18, 31, 0.3);
  padding: 20px 24px;
  width: 300px;
  font-family: 'IBM Plex Mono', monospace;
  pointer-events: none;
  transition: opacity 200ms ease;
}
.tour-card.hidden { opacity: 0; }
.tour-step-ind {
  font-size: 8px;
  color: #c1121f;
  letter-spacing: 2px;
  margin-bottom: 10px;
  font-weight: 700;
}
.tour-msg {
  font-size: 11px;
  color: #d4d4cc;
  line-height: 1.8;
  margin-bottom: 14px;
}
.tour-cta {
  font-size: 8px;
  color: #3a3a38;
  letter-spacing: 1.5px;
}
.tour-arrow {
  position: fixed;
  z-index: 1000;
  pointer-events: none;
  transition: opacity 200ms ease;
}
.tour-arrow.hidden { opacity: 0; }
"""

tour_html_js = """
<!-- DOMO ONBOARDING TOUR -->
<div id="tourOverlay"></div>
<div class="tour-card hidden" id="tourCard">
  <div class="tour-step-ind" id="tourInd"></div>
  <div class="tour-msg" id="tourMsg"></div>
  <div class="tour-cta" id="tourCta"></div>
</div>
<svg class="tour-arrow hidden" id="tourArrow" xmlns="http://www.w3.org/2000/svg" width="120" height="120" style="overflow:visible;"></svg>

<script>
(function(){
  if(localStorage.getItem('domo-toured')) return;

  var overlay = document.getElementById('tourOverlay');
  var card    = document.getElementById('tourCard');
  var ind     = document.getElementById('tourInd');
  var msg     = document.getElementById('tourMsg');
  var cta     = document.getElementById('tourCta');
  var arrow   = document.getElementById('tourArrow');

  var step = 0;
  var transitioning = false;

  var steps = [
    {
      ind: '01 / 03',
      msg: 'This is the department seal. Click it and the world opens — DOMO Times, dispatches from the field, classified objects, things the system forgot to catalogue. Everything lives behind this mark. It is not a logo. It is a door.',
      cta: 'click anywhere to continue',
      target: function(){ return document.getElementById('brand-logo-img') || document.querySelector('.nav-logo') || document.querySelector('#mainNav img'); }
    },
    {
      ind: '02 / 03',
      msg: 'Every object here was found, not made. Click OBJECTS and you enter the collection — things that outlived their owners, things that should not exist, things that the department acquired under circumstances it does not discuss. Each one has a page. Each page has a story. Each story has something the object is trying to say.',
      cta: 'click anywhere to continue',
      target: function(){
        var links = document.querySelectorAll('#mainNav .nav-center a, #mainNav .nav-links a');
        for(var i=0;i<links.length;i++){
          if(links[i].textContent.trim().toUpperCase()==='OBJECTS') return links[i];
        }
        return null;
      }
    },
    {
      ind: '03 / 03',
      msg: 'Access is not given. It is granted. If you have credentials, LOGIN and the department opens its full archive to you. If you do not — the objects can still be seen. But some doors will stay shut. The department does not apologise for this. Neither should you.',
      cta: 'click anywhere to enter',
      target: function(){
        var links = document.querySelectorAll('#mainNav .nav-center a, #mainNav .nav-links a');
        for(var i=0;i<links.length;i++){
          var t=links[i].textContent.trim().toUpperCase();
          if(t==='LOGIN') return links[i];
        }
        return null;
      }
    }
  ];

  function getRect(el){
    if(!el) return {left:0,top:0,right:100,bottom:40,width:100,height:40};
    return el.getBoundingClientRect();
  }

  function drawArrow(x1,y1,x2,y2){
    var dx=x2-x1, dy=y2-y1;
    var len=Math.sqrt(dx*dx+dy*dy);
    if(len<1)len=1;
    var ux=dx/len, uy=dy/len;
    // arrowhead size
    var ah=8;
    var ax=x2-ux*ah-uy*ah*0.5;
    var ay=y2-uy*ah+ux*ah*0.5;
    var bx=x2-ux*ah+uy*ah*0.5;
    var by=y2-uy*ah-ux*ah*0.5;
    arrow.setAttribute('width','1');
    arrow.setAttribute('height','1');
    arrow.style.left='0';
    arrow.style.top='0';
    arrow.style.width='100vw';
    arrow.style.height='100vh';
    arrow.setAttribute('viewBox','0 0 '+window.innerWidth+' '+window.innerHeight);
    arrow.innerHTML=
      '<line x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'" stroke="#c1121f" stroke-width="1" stroke-dasharray="none"/>'
      +'<polygon points="'+x2+','+y2+' '+ax+','+ay+' '+bx+','+by+'" fill="#c1121f"/>';
  }

  function positionStep(s){
    var st = steps[s];
    var el = st.target();
    var r  = getRect(el);
    var vw = window.innerWidth;
    var vh = window.innerHeight;
    var cardW = 300, cardH = 160;

    // Place card below the target, slightly offset
    var cx, cy;
    if(s===0){
      // Step 1: logo - card below and right of logo
      cx = r.left;
      cy = r.bottom + 22;
    } else {
      // Steps 2+3: center under the link
      cx = r.left + r.width/2 - cardW/2;
      cy = r.bottom + 22;
    }
    // clamp to viewport
    cx = Math.max(12, Math.min(vw - cardW - 12, cx));
    cy = Math.max(85, Math.min(vh - cardH - 12, cy));

    card.style.left = cx + 'px';
    card.style.top  = cy + 'px';
    card.style.width = cardW + 'px';

    // Arrow: from card top-center to element center
    var arrowStartX = cx + cardW/2;
    var arrowStartY = cy;
    var arrowEndX   = r.left + r.width/2;
    var arrowEndY   = r.bottom;
    drawArrow(arrowStartX, arrowStartY, arrowEndX, arrowEndY);

    ind.textContent = st.ind;
    msg.textContent = st.msg;
    cta.textContent = st.cta;
  }

  function showStep(s){
    positionStep(s);
    card.classList.remove('hidden');
    arrow.classList.remove('hidden');
  }

  function endTour(){
    overlay.classList.add('fade-out');
    card.classList.add('hidden');
    arrow.classList.add('hidden');
    document.body.style.overflow = '';
    document.removeEventListener('click', onClick);
    setTimeout(function(){
      if(overlay.parentNode) overlay.parentNode.removeChild(overlay);
      if(card.parentNode)    card.parentNode.removeChild(card);
      if(arrow.parentNode)   arrow.parentNode.removeChild(arrow);
    }, 520);
    localStorage.setItem('domo-toured','true');
  }

  function onClick(){
    if(transitioning) return;
    if(step === steps.length - 1){
      endTour();
      return;
    }
    transitioning = true;
    card.classList.add('hidden');
    arrow.classList.add('hidden');
    setTimeout(function(){
      step++;
      positionStep(step);
      card.classList.remove('hidden');
      arrow.classList.remove('hidden');
      transitioning = false;
    }, 210);
  }

  // Start tour
  document.body.style.overflow = 'hidden';
  showStep(0);
  document.addEventListener('click', onClick);
})();
</script>
"""

# 2. Inject tour CSS before the closing </style> at line 572
# Find the first </style> after the nav CSS block (around line 572)
# We look for the sequence "/* brand moved to #mainNav .nav-logo */\n</style>"
target_css_anchor = '/* brand moved to #mainNav .nav-logo */\n</style>'
content = content.replace(target_css_anchor, '/* brand moved to #mainNav .nav-logo */' + tour_css + '</style>', 1)

# 3. Inject tour HTML + JS before </body>
content = content.replace('</body>', tour_html_js + '</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
