#!/usr/bin/env python3
"""
Fix TV mode CSS isolation across all 16 DOMO files.
Scopes all TV-mode element CSS under html.tv-mode prefix.
Adds fallback image dimensions. Moves classList toggle inside create/destroyScene.
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    'index.html', 'door.html', 'login.html', 'signup.html',
    'profile.html', 'id.html', 'orders.html', 'activity.html',
    'checkout.html', 'dispatch.html', 'error.html',
    'sad-gargoyle.html', 'grey-piggy-bank.html',
    'the-pin.html', 'paper-boat.html', 'crocodile.html',
]

OLD_CSS = """<!-- TV MODE -->
<style>
html.tv-mode{overflow:hidden!important;height:100vh!important;}
html.tv-mode body{overflow:hidden!important;height:100vh!important;background:transparent!important;}
#tv-scene{position:fixed;inset:0;z-index:99999;background:#050405;overflow:hidden;pointer-events:none;}
#tv-room-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;pointer-events:none;display:block;}
#tv-screen{position:absolute;overflow:hidden;overflow-y:auto;pointer-events:auto;border-radius:10px 10px 8px 8px;scrollbar-width:none;transform:translateZ(0);}
#tv-screen::-webkit-scrollbar{display:none;}
</style>"""

NEW_CSS = """<!-- TV MODE -->
<style>
html.tv-mode{overflow:hidden!important;height:100vh!important;}
html.tv-mode body{overflow:hidden!important;height:100vh!important;background:transparent!important;}
html.tv-mode #tv-scene{position:fixed;inset:0;z-index:99999;background:#050405;overflow:hidden;pointer-events:none;}
html.tv-mode #tv-room-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top center;pointer-events:none;display:block;}
html.tv-mode #tv-screen{position:absolute;overflow:hidden;overflow-y:auto;pointer-events:auto;border-radius:10px 10px 8px 8px;scrollbar-width:none;transform:translateZ(0);}
html.tv-mode #tv-screen::-webkit-scrollbar{display:none;}
</style>"""

OLD_JS_POSITIONSCREEN = """  function positionScreen(){
    var img=document.getElementById('tv-room-img');
    var sc=document.getElementById('tv-screen');
    if(!img||!sc)return;
    if(!img.complete||!img.naturalWidth){img.onload=positionScreen;return;}
    var vW=window.innerWidth,vH=window.innerHeight;
    var iW=img.naturalWidth,iH=img.naturalHeight;
    /* cover with top-center anchor */
    var scale=Math.max(vW/iW,vH/iH);
    var rW=iW*scale,rH=iH*scale;
    var oX=(vW-rW)/2,oY=0;
    sc.style.left=(oX+TV_L*rW)+'px';
    sc.style.top=(oY+TV_T*rH)+'px';
    sc.style.width=((TV_R-TV_L)*rW)+'px';
    sc.style.height=((TV_B-TV_T)*rH)+'px';
  }"""

NEW_JS_POSITIONSCREEN = """  function positionScreen(){
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
  }"""

OLD_JS_CREATESCENE = """  function createScene(){
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
    img.onload=positionScreen;
    if(img.complete&&img.naturalWidth)positionScreen();
    window.addEventListener('resize',positionScreen);
  }"""

NEW_JS_CREATESCENE = """  function createScene(){
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
  }"""

OLD_JS_DESTROYSCENE = """  function destroyScene(){
    var scene=document.getElementById('tv-scene');
    if(!scene)return;
    var sc=document.getElementById('tv-screen');
    var body=document.body;
    if(sc)Array.from(sc.children).forEach(function(c){body.insertBefore(c,scene);});
    scene.remove();
    window.removeEventListener('resize',positionScreen);
  }"""

NEW_JS_DESTROYSCENE = """  function destroyScene(){
    /* remove active class FIRST so no TV CSS applies during teardown */
    document.documentElement.classList.remove('tv-mode');
    var scene=document.getElementById('tv-scene');
    if(!scene)return;
    var sc=document.getElementById('tv-screen');
    var body=document.body;
    if(sc)Array.from(sc.children).forEach(function(c){body.insertBefore(c,scene);});
    scene.remove();
    window.removeEventListener('resize',positionScreen);
  }"""

OLD_JS_APPLYTV = """  function applyTv(on){
    if(on&&window.innerWidth>=1024){
      document.documentElement.classList.add('tv-mode');
      createScene();
    } else {
      document.documentElement.classList.remove('tv-mode');
      destroyScene();
    }
    var btn=document.getElementById('tv-nav-btn');
    if(btn)btn.style.color=on?'#ffffff':'#a8a8a2';
  }"""

NEW_JS_APPLYTV = """  function applyTv(on){
    if(on&&window.innerWidth>=1024){
      createScene();
    } else {
      destroyScene();
    }
    var btn=document.getElementById('tv-nav-btn');
    if(btn)btn.style.color=(on&&window.innerWidth>=1024)?'#ffffff':'#a8a8a2';
  }"""

REPLACEMENTS = [
    (OLD_CSS, NEW_CSS),
    (OLD_JS_POSITIONSCREEN, NEW_JS_POSITIONSCREEN),
    (OLD_JS_CREATESCENE, NEW_JS_CREATESCENE),
    (OLD_JS_DESTROYSCENE, NEW_JS_DESTROYSCENE),
    (OLD_JS_APPLYTV, NEW_JS_APPLYTV),
]

def fix_file(fname):
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        print(f'  SKIP (not found): {fname}')
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- TV MODE -->' not in content:
        print(f'  SKIP (no TV MODE block): {fname}')
        return

    changed = 0
    for old, new in REPLACEMENTS:
        if old in content:
            content = content.replace(old, new)
            changed += 1
        else:
            print(f'  WARNING: pattern not found in {fname}:')
            print(f'    {repr(old[:60])}...')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  FIXED ({changed} replacements): {fname}')

print('Applying TV mode isolation fix...')
for fname in FILES:
    fix_file(fname)
print('Done.')
