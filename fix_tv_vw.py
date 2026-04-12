#!/usr/bin/env python3
"""
Replace TV mode implementation in all 16 files.

WHAT CHANGES:
- CSS: #tv-screen now uses exact vw-based coordinates (width:78vw, height:44vw,
  left:11vw, top:12vw, border-radius:18px). No transforms, no JS math.
- CSS: Remove #tv-room-img rule (img element no longer created).
- CSS: background-position: center (vw layout doesn't depend on image anchor math).
- JS: Remove positionScreen(), TV_L/T/R/B variables, resize listener entirely.
- JS: Remove #tv-room-img img element creation from createScene().
- JS: createScene/destroyScene stay. applyTv/toggleTvMode/init stay.

WHAT DOES NOT CHANGE:
- html.tv-mode isolation (all CSS still gated behind it)
- DOM move architecture (content in/out of #tv-screen)
- localStorage key, toggle button color, nav button
- Every other file in the project
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    'index.html', 'door.html', 'login.html', 'signup.html',
    'profile.html', 'id.html', 'orders.html', 'activity.html',
    'checkout.html', 'dispatch.html', 'error.html',
    'sad-gargoyle.html', 'grey-piggy-bank.html',
    'the-pin.html', 'paper-boat.html', 'crocodile.html',
]

OLD_BLOCK = """<!-- TV MODE -->
<style>
html.tv-mode{overflow:hidden!important;height:100vh!important;}
html.tv-mode body{overflow:hidden!important;height:100vh!important;background:transparent!important;}
html.tv-mode #tv-scene{position:fixed;inset:0;z-index:99999;background:#050405 url('tv-room.jpg') top center / cover no-repeat;overflow:hidden;pointer-events:none;}
html.tv-mode #tv-room-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;pointer-events:none;display:block;}
html.tv-mode #tv-screen{position:absolute;overflow:hidden;overflow-y:auto;pointer-events:auto;border-radius:10px 10px 8px 8px;scrollbar-width:none;transform:translateZ(0);}
html.tv-mode #tv-screen::-webkit-scrollbar{display:none;}
</style>
<script>
(function(){
  var TV_KEY='domo-tv-mode';
  /* Fractional coords of TV screen within the living-room reference image
     (calibrated from visual analysis: left=7.5%, top=4.5%, right=92.5%, bottom=61.5%) */
  var TV_L=0.075,TV_T=0.038,TV_R=0.925,TV_B=0.540;

  function positionScreen(){
    var img=document.getElementById('tv-room-img');
    var sc=document.getElementById('tv-screen');
    if(!img||!sc)return;
    var vW=window.innerWidth,vH=window.innerHeight;
    var iW=img.naturalWidth||1280,iH=img.naturalHeight||800;
    /* cover with top-center anchor */
    var scale=Math.max(vW/iW,vH/iH);
    var rW=iW*scale,rH=iH*scale;
    var oX=(vW-rW)/2,oY=0;
    sc.style.left=(oX+TV_L*rW)+'px';
    sc.style.top=(oY+TV_T*rH)+'px';
    sc.style.width=((TV_R-TV_L)*rW)+'px';
    sc.style.height=((TV_B-TV_T)*rH)+'px';
  }

  function createScene(){
    if(document.getElementById('tv-scene'))return;
    var body=document.body;
    var scene=document.createElement('div');scene.id='tv-scene';
    var img=document.createElement('img');img.id='tv-room-img';img.src='tv-room.jpg';img.alt='';
    scene.appendChild(img);
    var sc=document.createElement('div');sc.id='tv-screen';
    scene.appendChild(sc);
    /* snapshot then move all existing body children into tv-screen */
    Array.from(body.children).forEach(function(c){sc.appendChild(c);});
    body.appendChild(scene);
    /* add active class AFTER scene is in DOM so CSS applies immediately */
    document.documentElement.classList.add('tv-mode');
    img.onload=positionScreen;
    positionScreen();
    window.addEventListener('resize',positionScreen);
  }

  function destroyScene(){
    /* remove active class FIRST so no TV CSS applies during teardown */
    document.documentElement.classList.remove('tv-mode');
    var scene=document.getElementById('tv-scene');
    if(!scene)return;
    var sc=document.getElementById('tv-screen');
    var body=document.body;
    if(sc)Array.from(sc.children).forEach(function(c){body.insertBefore(c,scene);});
    scene.remove();
    window.removeEventListener('resize',positionScreen);
  }

  function applyTv(on){
    if(on&&window.innerWidth>=1024){
      createScene();
    } else {
      destroyScene();
    }
    var btn=document.getElementById('tv-nav-btn');
    if(btn)btn.style.color=(on&&window.innerWidth>=1024)?'#ffffff':'#a8a8a2';
  }

  window.toggleTvMode=function(){
    var on=localStorage.getItem(TV_KEY)==='true';
    on=!on;
    localStorage.setItem(TV_KEY,on?'true':'false');
    applyTv(on);
  };

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',function(){
      applyTv(localStorage.getItem(TV_KEY)==='true');
    });
  } else {
    applyTv(localStorage.getItem(TV_KEY)==='true');
  }
})();
</script>"""

NEW_BLOCK = """<!-- TV MODE -->
<style>
html.tv-mode{overflow:hidden!important;height:100vh!important;}
html.tv-mode body{overflow:hidden!important;height:100vh!important;background:transparent!important;}
html.tv-mode #tv-scene{position:fixed;inset:0;z-index:99999;background:#050405 url('tv-room.jpg') center/cover no-repeat;overflow:hidden;pointer-events:none;}
html.tv-mode #tv-screen{position:absolute;width:78vw;height:44vw;left:11vw;top:12vw;overflow:hidden;overflow-y:auto;border-radius:18px;z-index:5;pointer-events:auto;scrollbar-width:none;}
html.tv-mode #tv-screen::-webkit-scrollbar{display:none;}
</style>
<script>
(function(){
  var TV_KEY='domo-tv-mode';

  function createScene(){
    if(document.getElementById('tv-scene'))return;
    var body=document.body;
    var scene=document.createElement('div');scene.id='tv-scene';
    var sc=document.createElement('div');sc.id='tv-screen';
    scene.appendChild(sc);
    Array.from(body.children).forEach(function(c){sc.appendChild(c);});
    body.appendChild(scene);
    document.documentElement.classList.add('tv-mode');
  }

  function destroyScene(){
    document.documentElement.classList.remove('tv-mode');
    var scene=document.getElementById('tv-scene');
    if(!scene)return;
    var sc=document.getElementById('tv-screen');
    var body=document.body;
    if(sc)Array.from(sc.children).forEach(function(c){body.insertBefore(c,scene);});
    scene.remove();
  }

  function applyTv(on){
    if(on&&window.innerWidth>=1024){
      createScene();
    } else {
      destroyScene();
    }
    var btn=document.getElementById('tv-nav-btn');
    if(btn)btn.style.color=(on&&window.innerWidth>=1024)?'#ffffff':'#a8a8a2';
  }

  window.toggleTvMode=function(){
    var on=localStorage.getItem(TV_KEY)==='true';
    on=!on;
    localStorage.setItem(TV_KEY,on?'true':'false');
    applyTv(on);
  };

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',function(){
      applyTv(localStorage.getItem(TV_KEY)==='true');
    });
  } else {
    applyTv(localStorage.getItem(TV_KEY)==='true');
  }
})();
</script>"""

for fname in FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'  SKIP (not found): {fname}')
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if OLD_BLOCK not in content:
        print(f'  WARNING (block not matched): {fname}')
        continue
    content = content.replace(OLD_BLOCK, NEW_BLOCK)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  FIXED: {fname}')

print('Done.')
