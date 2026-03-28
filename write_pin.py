import os

with open('_nav_block.txt', 'r', encoding='utf-8') as f:
    nav_html = f.read()

head = '''<!DOCTYPE html>
<html lang="en">
<head>
<link rel="icon" type="image/png" href="favicon.png">
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>The Pin &ndash; D.O.M.O-039 &ndash; DOMO</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@300;400;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#ffffff;
  --bg2:#f8f8f6;
  --bg3:#f2f0ee;
  --panel:#f8f8f6;
  --ink:#0d0d0b;
  --ink2:#2a2a28;
  --ink3:#6a6a68;
  --red:#c1121f;
  --red2:#e01428;
  --border:#0d0d0b;
  --border2:rgba(13,13,11,0.15);
  --nav-bg:rgba(8,6,0,.92);
  --nav-border:#2a2008;
  --nav-ink:#f0e8c8;
  --nav-ink3:#6a5a28;
  --gold:#c8a830;
  --gold3:#a88820;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  background:var(--bg);color:var(--ink);
  font-family:'IBM Plex Mono',monospace;
  min-height:100vh;overflow-x:hidden;
}

/* NAV - dark glass, verbatim from key.html */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:20px 52px;
  background:var(--nav-bg);
  border-bottom:1px solid var(--nav-border);
  backdrop-filter:blur(20px);
}
.brand{font-family:'Bebas Neue',sans-serif;font-size:24px;letter-spacing:.12em;color:var(--nav-ink);text-decoration:none;display:flex;align-items:center;}
.brand sub{font-family:'Space Mono',monospace;font-size:8px;display:block;letter-spacing:.28em;color:var(--nav-ink3);text-transform:uppercase;}
.brand-logo{height:58px;width:auto;display:block;}
.nav-links{display:flex;gap:28px;list-style:none;align-items:center;}
.nav-links a{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:var(--nav-ink3);text-decoration:none;font-weight:700;transition:color .2s;}
.nav-links a:hover{color:var(--gold);}
.nav-links a[href="domo-times.html"]{border:1px solid var(--nav-border);padding:3px 9px;}
.cart-btn{background:none;border:1px solid var(--nav-border);padding:8px 14px;cursor:pointer;font-family:'Space Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--nav-ink3);display:flex;align-items:center;gap:8px;transition:all .2s;position:relative;}
.cart-btn:hover{background:var(--gold3);color:#0d0d0b;border-color:var(--gold3);}
.cart-badge{background:var(--gold);color:#080600;border-radius:50%;width:17px;height:17px;display:flex;align-items:center;justify-content:center;font-size:8px;font-weight:700;position:absolute;top:-7px;right:-7px;}
.cart-badge.hidden{display:none;}

/* NAV AVATAR */
.nav-avatar-btn{cursor:pointer;display:flex;align-items:center;}
.nav-avatar-circle{width:30px;height:30px;border-radius:50%;background:#c1121f;display:flex;align-items:center;justify-content:center;font-family:"Space Mono",monospace;font-size:11px;font-weight:700;color:#fff;border:1.5px solid rgba(255,255,255,.2);transition:box-shadow .2s;}
.nav-avatar-circle:hover{box-shadow:0 0 0 3px rgba(255,255,255,.15);}
.nav-dropdown{display:none;flex-direction:column;position:absolute;top:calc(100% + 10px);right:0;min-width:200px;background:#0a0a0a;border:1px solid rgba(255,255,255,.1);z-index:500;padding:0;}
.nav-dropdown-top{padding:14px 16px 10px;border-bottom:1px solid rgba(255,255,255,.07);}
.nav-avatar-name{font-family:"Space Mono",monospace;font-size:11px;color:#fff;text-transform:uppercase;letter-spacing:.03em;}
.nav-avatar-email{font-family:"Space Mono",monospace;font-size:8px;color:rgba(255,255,255,.35);letter-spacing:.05em;margin-top:2px;word-break:break-all;}
.nav-dd-link{display:block;padding:11px 16px;font-family:"Space Mono",monospace;font-size:9px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.6);text-decoration:none;transition:background .15s,color .15s;border-bottom:1px solid rgba(255,255,255,.05);}
.nav-dd-link:hover{background:rgba(255,255,255,.06);color:#fff;}
.nav-dd-signout{display:block;width:100%;padding:11px 16px;font-family:"Space Mono",monospace;font-size:9px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,80,60,.7);background:none;border:none;cursor:pointer;text-align:left;transition:background .15s,color .15s;}
.nav-dd-signout:hover{background:rgba(255,60,40,.08);color:#ff4030;}

/* NAV ARROWS */
.obj-nav{position:fixed;top:50%;transform:translateY(-50%);z-index:200;text-decoration:none;opacity:.08;transition:opacity .3s;}
.obj-nav:hover{opacity:1;}
.obj-nav.prev{left:12px;}.obj-nav.next{right:12px;}
.obj-nav-arrow{width:42px;height:42px;border:0.5px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:18px;background:#fff;color:var(--ink);transition:all .2s;}
.obj-nav:hover .obj-nav-arrow{background:var(--red);color:#fff;border-color:var(--red);}

/* BREADCRUMB */
.breadcrumb{padding:88px 52px 0;font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink3);font-weight:700;position:relative;z-index:2;}
.breadcrumb a{color:var(--ink3);text-decoration:none;}.breadcrumb a:hover{color:var(--red);}

/* PRODUCT WRAP */
.product-wrap{position:relative;z-index:2;padding-top:22px;}

/* TOP GRID */
.product-top{
  display:grid;grid-template-columns:1fr 1fr;
  border-top:0.5px solid var(--border);
  border-bottom:0.5px solid var(--border);
  min-height:calc(100vh - 160px);
}

/* LEFT */
.col-left{
  padding:48px 52px;
  border-right:0.5px solid var(--border);
  display:flex;flex-direction:column;
  background:var(--bg);
}
.cat-tag{font-family:'IBM Plex Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:var(--red);margin-bottom:14px;}
.obj-title{
  font-family:'Bebas Neue',sans-serif;
  font-size:clamp(72px,10vw,148px);line-height:.88;
  letter-spacing:.02em;color:var(--ink);
}
.obj-model{font-family:'IBM Plex Mono',monospace;font-size:10px;font-weight:700;letter-spacing:.25em;color:var(--ink3);text-transform:uppercase;margin-top:14px;margin-bottom:28px;}
.red-rule{width:72px;height:0.5px;background:var(--red);margin-bottom:26px;}
.obj-desc{font-family:'IBM Plex Mono',monospace;font-size:13px;font-weight:300;line-height:1.9;color:var(--ink2);max-width:440px;margin-bottom:10px;}
.obj-desc-body{font-family:'IBM Plex Mono',monospace;font-size:10px;line-height:2.1;color:var(--ink3);max-width:440px;margin-bottom:32px;letter-spacing:.02em;}
.specs-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;border-top:0.5px solid var(--border);margin-top:auto;}
.spec{padding:13px 0;border-bottom:0.5px solid var(--border2);}
.spec:nth-child(odd){border-right:0.5px solid var(--border2);padding-right:14px;}
.spec:nth-child(even){padding-left:14px;}
.spec-k{font-family:'IBM Plex Mono',monospace;font-size:7.5px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--ink3);margin-bottom:2px;}
.spec-v{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--red);line-height:1.6;}

/* RIGHT */
.col-right{
  position:relative;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  padding:52px 40px;background:var(--bg2);overflow:hidden;
}
.col-right::before{
  content:'';position:absolute;inset:0;
  background:repeating-linear-gradient(0deg,transparent,transparent 39px,rgba(13,13,11,0.04) 39px,rgba(13,13,11,0.04) 40px);
  pointer-events:none;
}

/* TICKER */
.ticker{position:absolute;top:0;left:0;right:0;overflow:hidden;white-space:nowrap;font-family:'IBM Plex Mono',monospace;font-size:8px;font-weight:700;letter-spacing:.12em;color:rgba(193,18,31,0.2);border-bottom:0.5px solid var(--border);padding:7px 0;z-index:3;}
.ticker-inner{display:inline-block;animation:tick 28s linear infinite;}
.ticker-btm{position:absolute;bottom:0;left:0;right:0;overflow:hidden;white-space:nowrap;font-family:'IBM Plex Mono',monospace;font-size:8px;font-weight:700;letter-spacing:.12em;color:rgba(193,18,31,0.12);border-top:0.5px solid var(--border);padding:7px 0;z-index:3;}
.ticker-btm .ticker-inner{animation-duration:36s;animation-direction:reverse;}
@keyframes tick{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* PIN STAGE */
.pin-stage{position:relative;width:100%;max-width:240px;aspect-ratio:1/1.8;display:flex;align-items:center;justify-content:center;z-index:2;}

/* STATS */
.stats-strip{position:absolute;bottom:44px;left:20px;right:20px;display:grid;grid-template-columns:repeat(4,1fr);border:0.5px solid var(--border);z-index:3;background:rgba(255,255,255,.95);}
.stat{padding:9px 10px;border-right:0.5px solid var(--border);text-align:center;}
.stat:last-child{border-right:none;}
.stat-k{font-family:'IBM Plex Mono',monospace;font-size:6.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink3);margin-bottom:2px;}
.stat-v{font-family:'IBM Plex Mono',monospace;font-size:16px;color:var(--red);font-weight:700;}

/* PRICE STRIP */
.price-strip{display:grid;grid-template-columns:1fr 1fr;border-bottom:0.5px solid var(--border);}
.price-left{padding:40px 52px;border-right:0.5px solid var(--border);display:flex;flex-direction:column;justify-content:center;background:var(--bg);}
.price-label{font-family:'IBM Plex Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:var(--ink3);margin-bottom:4px;}
.price-num{font-family:'Bebas Neue',sans-serif;font-size:clamp(64px,9vw,118px);line-height:.88;color:var(--ink);letter-spacing:.02em;}
.price-num sup{font-size:.36em;vertical-align:super;}
.price-sub{font-family:'IBM Plex Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ink3);margin-top:8px;}
.price-right{padding:40px 52px;display:flex;flex-direction:column;justify-content:center;gap:12px;background:var(--bg2);}
.stock-line{font-family:'IBM Plex Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--ink3);display:flex;align-items:center;gap:8px;}
.stock-dot{width:7px;height:7px;border-radius:50%;background:var(--red);flex-shrink:0;animation:stockPulse 2s ease-in-out infinite;}
@keyframes stockPulse{0%,100%{box-shadow:0 0 0 0 rgba(193,18,31,.3);}50%{box-shadow:0 0 8px 3px rgba(193,18,31,.1);}}
.btn-cart-main{background:var(--red);color:#fff;border:none;padding:20px 40px;font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;cursor:pointer;transition:all .2s;width:100%;}
.btn-cart-main:hover{background:var(--ink);}
.btn-save{background:transparent;border:0.5px solid var(--border);padding:13px;font-family:'IBM Plex Mono',monospace;font-size:10px;cursor:pointer;color:var(--ink3);transition:all .2s;width:100%;letter-spacing:.08em;text-transform:uppercase;font-weight:700;}
.btn-save:hover{border-color:var(--red);color:var(--red);}

/* DATA STRIP */
.data-strip{background:var(--ink);overflow:hidden;white-space:nowrap;height:52px;display:flex;align-items:center;border-bottom:0.5px solid var(--border);}
.data-strip-inner{display:inline-flex;align-items:center;animation:tick 20s linear infinite;}
.ds-item{display:inline-flex;align-items:center;gap:10px;padding:0 32px;border-right:1px solid rgba(255,255,255,.06);height:52px;}
.ds-k{font-family:'IBM Plex Mono',monospace;font-size:7.5px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.25);}
.ds-v{font-family:'IBM Plex Mono',monospace;font-size:14px;color:var(--red);font-weight:700;}
.ds-v.dim{color:rgba(193,18,31,.4);}

/* WARNING STRIP */
.warning-strip{background:var(--bg3);padding:16px 52px;display:flex;align-items:flex-start;gap:18px;border-bottom:0.5px solid var(--border);border-left:3px solid var(--red);}
.w-label{font-family:'IBM Plex Mono',monospace;font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--red);flex-shrink:0;padding-top:1px;}
.w-text{font-family:'IBM Plex Mono',monospace;font-size:9.5px;letter-spacing:.03em;color:var(--ink3);line-height:1.9;}

/* INTERACTION BOOTH */
.booth-section{background:var(--bg);padding:56px 52px;border-bottom:0.5px solid var(--border);position:relative;}
.booth-label{font-family:'IBM Plex Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:var(--ink3);margin-bottom:8px;}
.booth-rule{width:100%;height:0.5px;background:var(--border);margin-bottom:40px;}
.booth-title{font-family:'Bebas Neue',sans-serif;font-size:48px;color:var(--ink);letter-spacing:.04em;margin-bottom:6px;}
.booth-sub{font-family:'IBM Plex Mono',monospace;font-size:10px;color:var(--ink3);line-height:1.8;max-width:560px;margin-bottom:48px;}
.booth-arena{position:relative;width:100%;min-height:320px;border:0.5px solid var(--border);background:var(--bg2);overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:48px 0;}
.pin-row{display:flex;align-items:flex-end;gap:20px;position:relative;z-index:2;}
.booth-hint{font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:.1em;color:var(--red);margin-top:24px;z-index:2;position:relative;}

/* STORY */
.story{display:grid;grid-template-columns:220px 1fr;border-bottom:0.5px solid var(--border);}
.story-tag{padding:52px 32px 52px 52px;border-right:0.5px solid var(--border);display:flex;align-items:flex-start;background:var(--bg);}
.story-tag span{font-family:'Bebas Neue',sans-serif;font-size:36px;line-height:.9;color:var(--red);writing-mode:vertical-rl;transform:rotate(180deg);}
.story-body{padding:52px;background:var(--bg2);}
.story-body h3{font-family:'Bebas Neue',sans-serif;font-size:32px;color:var(--ink);letter-spacing:.04em;margin-bottom:18px;line-height:1.1;}
.story-body p{font-family:'IBM Plex Mono',monospace;font-size:10.5px;line-height:2.1;color:var(--ink3);max-width:660px;}
.story-body p+p{margin-top:18px;}
.pull-quote{font-family:'Bebas Neue',sans-serif;font-size:26px;color:var(--red);line-height:1.15;margin:28px 0;padding-left:18px;border-left:3px solid var(--red);max-width:600px;letter-spacing:.04em;}

/* FOOTER */
footer{display:flex;align-items:center;justify-content:space-between;padding:26px 52px;background:var(--bg);border-top:0.5px solid var(--border);}
.footer-brand{font-family:'Bebas Neue',sans-serif;font-size:22px;letter-spacing:.1em;color:var(--ink);}
.footer-brand small{font-family:'IBM Plex Mono',monospace;font-size:8px;letter-spacing:.2em;color:var(--ink3);display:block;text-transform:uppercase;}
.footer-back a{font-family:'IBM Plex Mono',monospace;font-size:9px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--ink3);text-decoration:none;transition:color .15s;}
.footer-back a:hover{color:var(--red);}

/* CART */
.cart-overlay{position:fixed;inset:0;background:rgba(0,0,0,.8);z-index:900;opacity:0;pointer-events:none;transition:opacity .3s;}
.cart-overlay.open{opacity:1;pointer-events:all;}
.cart-drawer{position:fixed;top:0;right:0;bottom:0;width:400px;max-width:95vw;background:#fff;z-index:901;transform:translateX(100%);transition:transform .35s cubic-bezier(.4,0,.2,1);display:flex;flex-direction:column;border-left:0.5px solid var(--border);}
.cart-drawer.open{transform:translateX(0);}
.cart-header{display:flex;align-items:center;justify-content:space-between;padding:22px 26px;border-bottom:0.5px solid var(--border);flex-shrink:0;}
.cart-header-title{font-family:'IBM Plex Mono',monospace;font-size:14px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--ink);}
.cart-close{background:none;border:0.5px solid var(--border);width:34px;height:34px;cursor:pointer;font-size:16px;color:var(--ink3);display:flex;align-items:center;justify-content:center;transition:all .15s;}
.cart-close:hover{background:var(--red);color:#fff;border-color:var(--red);}
.cart-body{flex:1;overflow-y:auto;padding:0 26px;}
.cart-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;gap:10px;}
.cart-empty .empty-big{font-family:'IBM Plex Mono',monospace;font-size:28px;font-weight:700;color:rgba(13,13,11,.1);text-transform:uppercase;letter-spacing:.1em;}
.cart-empty .empty-sm{font-family:'IBM Plex Mono',monospace;font-size:8px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink3);}
.drawer-item{display:flex;gap:12px;padding:16px 0;border-bottom:0.5px solid var(--border2);align-items:center;}
.drawer-item-info{flex:1;min-width:0;}
.drawer-item-name{font-family:'IBM Plex Mono',monospace;font-size:12px;font-weight:700;color:var(--ink);}
.drawer-item-meta{font-family:'IBM Plex Mono',monospace;font-size:7.5px;color:var(--ink3);letter-spacing:.1em;text-transform:uppercase;margin-top:2px;}
.drawer-item-price{font-family:'IBM Plex Mono',monospace;font-size:13px;color:var(--red);font-weight:700;margin-top:3px;}
.drawer-item-remove{background:none;border:none;cursor:pointer;font-size:13px;color:var(--ink3);transition:color .15s;flex-shrink:0;}
.drawer-item-remove:hover{color:var(--red);}
.cart-footer{padding:18px 26px;border-top:0.5px solid var(--border);flex-shrink:0;}
.cart-subtotal{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;}
.cart-subtotal .lbl{font-family:'IBM Plex Mono',monospace;font-size:8.5px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--ink3);}
.cart-subtotal .val{font-family:'IBM Plex Mono',monospace;font-size:20px;font-weight:700;color:var(--ink);}
.btn-checkout-link{display:block;background:var(--red);color:#fff;padding:17px;font-family:'IBM Plex Mono',monospace;font-weight:700;font-size:12px;letter-spacing:.15em;text-transform:uppercase;cursor:pointer;width:100%;transition:opacity .15s;text-align:center;text-decoration:none;}
.btn-checkout-link:hover{opacity:.85;}

@media(max-width:860px){
  .product-top,.price-strip,.story{grid-template-columns:1fr;}
  .col-left,.col-right,.price-left,.price-right,.story-tag,.story-body{border-right:none!important;border-bottom:0.5px solid var(--border);}
  .story-tag span{writing-mode:horizontal-tb;transform:none;font-size:28px;}
  nav{padding:14px 20px;}
  .col-left,.price-left,.story-body,footer,.booth-section,.warning-strip{padding-left:20px;padding-right:20px;}
  .col-right,.price-right{padding:28px 20px;}
  .stats-strip{display:none;}
  .obj-nav.prev{left:4px;}.obj-nav.next{right:4px;}
}
</style>
</head>
<body>

<a href="octopus.html" class="obj-nav prev"><div class="obj-nav-arrow">&#8592;</div></a>
<a href="moai.html" class="obj-nav next"><div class="obj-nav-arrow">&#8594;</div></a>

'''

body = '''
<div class="breadcrumb"><a href="index.html">Home</a> / <a href="index.html#objects">Objects</a> / The Pin</div>

<div class="product-wrap">
  <div class="product-top">

    <!-- LEFT -->
    <div class="col-left">
      <div class="cat-tag">Manufactured Object &mdash; D.O.M.O-039 &mdash; In Stock</div>
      <h1 class="obj-title">The<br>Pin</h1>
      <p class="obj-model">Model No. D.O.M.O-039 &nbsp;/&nbsp; Standard Issue</p>
      <div class="red-rule"></div>
      <div class="obj-desc">Every system needs something to keep everything in line. You are looking at it.</div>
      <div class="obj-desc-body">The pin does not decide. It does not refuse. It holds the formation together because the formation requires it to. It was made to be identical to all the others. It was made to stay exactly where it was put. It was made to be replaced without ceremony if it is ever found to be different. The pin does not know this. That is the point.</div>
      <div class="specs-grid">
        <div class="spec"><div class="spec-k">Era</div><div class="spec-v">The moment the first school bell rang and someone realised the bell was cheaper than the teacher.</div></div>
        <div class="spec"><div class="spec-k">Material</div><div class="spec-v">Lacquered hardwood. Precision-weighted. Produced to tolerances that leave no room for variation.</div></div>
        <div class="spec"><div class="spec-k">Condition</div><div class="spec-v">Mint. Identical to all others in the set. This is not a coincidence. It is the specification.</div></div>
        <div class="spec"><div class="spec-k">Reckoning</div><div class="spec-v">The system does not break you. It makes you impossible to distinguish from the person beside you. That is worse.</div></div>
        <div class="spec"><div class="spec-k">Finish</div><div class="spec-v">White. Always white. The colour of a form that has already been filled in on your behalf.</div></div>
        <div class="spec"><div class="spec-k">Quantity</div><div class="spec-v">Ten. Always ten. Anything other than ten is a malfunction to be corrected.</div></div>
        <div class="spec"><div class="spec-k">Weight</div><div class="spec-v">1.53 kg. Standardised. Certified. Compliant.</div></div>
        <div class="spec"><div class="spec-k">Function</div><div class="spec-v">To stand. To be knocked down. To be reset. To stand again. Indefinitely.</div></div>
      </div>
    </div>

    <!-- RIGHT -->
    <div class="col-right">
      <div class="ticker">
        <span class="ticker-inner">STANDARD ISSUE &nbsp;&#9632;&nbsp; D.O.M.O-039 &nbsp;&#9632;&nbsp; LACQUERED WHITE &nbsp;&#9632;&nbsp; MASS PRODUCED &nbsp;&#9632;&nbsp; CERTIFIED COMPLIANT &nbsp;&#9632;&nbsp; STANDARD ISSUE &nbsp;&#9632;&nbsp; D.O.M.O-039 &nbsp;&#9632;&nbsp; LACQUERED WHITE &nbsp;&#9632;&nbsp; MASS PRODUCED &nbsp;&#9632;&nbsp; CERTIFIED COMPLIANT &nbsp;&#9632;&nbsp;</span>
      </div>
      <div class="ticker-btm">
        <span class="ticker-inner">THE SYSTEM DOES NOT NEED YOU TO AGREE &mdash; IT ONLY NEEDS YOU TO BE INDISTINGUISHABLE FROM THE OTHERS &mdash; THE SYSTEM DOES NOT NEED YOU TO AGREE &mdash; IT ONLY NEEDS YOU TO BE INDISTINGUISHABLE FROM THE OTHERS &mdash;</span>
      </div>

      <div class="pin-stage">
        <svg viewBox="0 0 120 260" xmlns="http://www.w3.org/2000/svg" width="120" height="260">
          <ellipse cx="60" cy="252" rx="32" ry="6" fill="rgba(13,13,11,0.07)"/>
          <path d="M60 18 C88 18 92 58 92 92 C92 126 84 140 74 150 L74 220 C74 230 68 238 60 238 C52 238 46 230 46 220 L46 150 C36 140 28 126 28 92 C28 58 32 18 60 18Z" fill="#ffffff" stroke="#0d0d0b" stroke-width="1.5"/>
          <rect x="46" y="148" width="28" height="12" fill="#c1121f"/>
          <ellipse cx="50" cy="36" rx="9" ry="6" fill="rgba(255,255,255,0.45)" transform="rotate(-15 50 36)"/>
        </svg>
      </div>

      <div class="stats-strip">
        <div class="stat"><div class="stat-k">Produced</div><div class="stat-v">Millions</div></div>
        <div class="stat"><div class="stat-k">Unique</div><div class="stat-v">None</div></div>
        <div class="stat"><div class="stat-k">Replaced</div><div class="stat-v">Always</div></div>
        <div class="stat"><div class="stat-k">Remembered</div><div class="stat-v">Never</div></div>
      </div>
    </div>
  </div>

  <!-- PRICE -->
  <div class="price-strip">
    <div class="price-left">
      <div class="price-label">Listed Price</div>
      <div class="price-num">&#8377;039</div>
      <div class="price-sub">Lacquered Wood &middot; Standard Regulation &middot; Fully Interchangeable</div>
    </div>
    <div class="price-right">
      <div class="stock-line"><span class="stock-dot"></span>&nbsp;In Stock &mdash; Will Always Be In Stock &mdash; There Is No Shortage of Pins</div>
      <button class="btn-cart-main" id="addCartBtn" onclick="addToCart()">Acquire The Pin</button>
      <button class="btn-save" id="wishBtn" onclick="toggleWishlist()">Hold for Later &#9661;</button>
    </div>
  </div>

  <!-- DATA STRIP -->
  <div class="data-strip">
    <div class="data-strip-inner">
      <div class="ds-item"><div class="ds-k">Units in Existence</div><div class="ds-v">Uncountable</div></div>
      <div class="ds-item"><div class="ds-k">Deviations Permitted</div><div class="ds-v dim">Zero</div></div>
      <div class="ds-item"><div class="ds-k">Individuality Index</div><div class="ds-v">0.00</div></div>
      <div class="ds-item"><div class="ds-k">Replacement Time</div><div class="ds-v dim">Immediate</div></div>
      <div class="ds-item"><div class="ds-k">Units in Existence</div><div class="ds-v">Uncountable</div></div>
      <div class="ds-item"><div class="ds-k">Deviations Permitted</div><div class="ds-v dim">Zero</div></div>
      <div class="ds-item"><div class="ds-k">Individuality Index</div><div class="ds-v">0.00</div></div>
      <div class="ds-item"><div class="ds-k">Replacement Time</div><div class="ds-v dim">Immediate</div></div>
    </div>
  </div>

  <!-- WARNING -->
  <div class="warning-strip">
    <div class="w-label">Compliance Note</div>
    <div class="w-text">This object meets all regulatory standards for uniformity. Any unit found to deviate from specification has been identified, removed, and replaced. The set you are viewing contains no deviations. It never has. The system is working correctly.</div>
  </div>

  <!-- INTERACTION BOOTH -->
  <div class="booth-section">
    <div class="booth-label">Interaction Booth &mdash; Object D.O.M.O-039</div>
    <div class="booth-rule"></div>
    <div class="booth-title">Replication Protocol</div>
    <div class="booth-sub">The system does not need to force conformity. It only needs to make conformity feel like the default state. Hover over any pin below. Watch what happens. Move away when you have seen enough.</div>
    <div class="booth-arena" id="boothArena">
      <div class="pin-row" id="pinRow"></div>
      <div class="booth-hint">hover to replicate &mdash; move away to forget</div>
    </div>
  </div>

  <!-- STORY -->
  <div class="story">
    <div class="story-tag"><span>The Story</span></div>
    <div class="story-body">
      <h3>The System Does Not Break You. It Makes You Indistinguishable.</h3>
      <p>The pin was not designed to hurt you. It was designed to be comfortable to stand in. Upright, steady, perfectly balanced, taking up exactly the right amount of space and no more. The people who built the systems that shaped you were not cruel. They were efficient. There is a difference, and the difference is what makes it so hard to be angry.</p>
      <div class="pull-quote">The classroom was not a prison. It just had bells that told you when you were allowed to think.</div>
      <p>The corporation was not a cage. It just had performance reviews that measured how well you had stopped being yourself. The education system was not a factory. It just happened to produce outputs that were graded, sorted, and assigned to slots in a larger machine that had already decided what it needed before you were born.</p>
      <p>The pin does not resist. It stands where it is placed. It falls when it is hit. It is reset by a mechanism it cannot see. It does this for as long as it is useful. When it is no longer useful &mdash; when it is chipped, or different, or simply worn in a way that makes it slightly unequal to the others &mdash; it is removed. Not punished. Removed. The distinction matters enormously to the system. The system does not punish. It corrects.</p>
      <p style="margin-top:22px;border-top:0.5px solid rgba(13,13,11,0.15);padding-top:18px;color:var(--ink3);">Object D.O.M.O-039 is made from lacquered hardwood. Weight: 1.53 kg. Height: 38.1 cm. Identical to all others in the set. Priced at &#8377;039. The price is not a coincidence.</p>
    </div>
  </div>

  <footer>
    <div class="footer-brand">DOMO<small>Department of Miscellaneous Objects &copy; 2024</small></div>
    <div class="footer-back"><a href="index.html">&#8592; Back to Objects</a></div>
  </footer>
</div>

<div class="cart-overlay" id="cartOverlay" onclick="closeCart()"></div>
<div class="cart-drawer" id="cartDrawer">
  <div class="cart-header"><div class="cart-header-title">Cart</div><button class="cart-close" onclick="closeCart()">&#x2715;</button></div>
  <div class="cart-body" id="cartBody">
    <div class="cart-empty" id="cartEmpty"><div class="empty-big">Empty</div><div class="empty-sm">Nothing yet</div></div>
  </div>
  <div class="cart-footer" id="cartFooter" style="display:none">
    <div class="cart-subtotal"><span class="lbl">Subtotal</span><span class="val" id="cartSubtotal">&#8377;0</span></div>
    <a href="checkout.html" class="btn-checkout-link">Checkout &#8594;</a>
  </div>
</div>

<script>
// CART
var PRODUCT={name:"The Pin",model:"D.O.M.O-039",price:39,slug:"the-pin"};
var cartItems=JSON.parse(localStorage.getItem('domo_cart')||'[]');
function updateCartUI(){
  var badge=document.getElementById('cartBadge');
  var body=document.getElementById('cartBody');
  var empty=document.getElementById('cartEmpty');
  var footer=document.getElementById('cartFooter');
  var sub=document.getElementById('cartSubtotal');
  if(badge){badge.textContent=cartItems.length;badge.classList.toggle('hidden',cartItems.length===0);}
  if(!body)return;
  if(cartItems.length===0){empty.style.display='flex';footer.style.display='none';return;}
  empty.style.display='none';footer.style.display='';
  body.innerHTML='';
  cartItems.forEach(function(item,idx){
    var d=document.createElement('div');d.className='drawer-item';
    d.innerHTML='<div class="drawer-item-info"><div class="drawer-item-name">'+item.name+'</div><div class="drawer-item-meta">'+item.model+'</div><div class="drawer-item-price">&#8377;'+item.price+'</div></div><button class="drawer-item-remove" onclick="removeItem('+idx+')">&#x2715;</button>';
    body.appendChild(d);
  });
  var total=cartItems.reduce(function(a,b){return a+b.price;},0);
  sub.textContent='&#8377;'+total;
}
window.addToCart=function(){cartItems.push(Object.assign({},PRODUCT));localStorage.setItem('domo_cart',JSON.stringify(cartItems));updateCartUI();openCart();};
window.removeItem=function(i){cartItems.splice(i,1);localStorage.setItem('domo_cart',JSON.stringify(cartItems));updateCartUI();};
window.openCart=function(){document.getElementById('cartOverlay').classList.add('open');document.getElementById('cartDrawer').classList.add('open');document.body.style.overflow='hidden';};
window.closeCart=function(){document.getElementById('cartOverlay').classList.remove('open');document.getElementById('cartDrawer').classList.remove('open');document.body.style.overflow='';};
updateCartUI();

// PIN INTERACTION BOOTH
(function(){
  var arena=document.getElementById('boothArena');
  var row=document.getElementById('pinRow');
  var ghostsByPin={};
  var hoverTimers={};
  var PIN_W=44, PIN_H=96, GAP=20;

  function makePinHTML(opacity,scale){
    scale=scale||1;
    var w=Math.round(PIN_W*scale), h=Math.round(PIN_H*scale);
    return '<svg viewBox="0 0 44 96" xmlns="http://www.w3.org/2000/svg" width="'+w+'" height="'+h+'" style="display:block;">'
      +'<ellipse cx="22" cy="92" rx="12" ry="3" fill="rgba(13,13,11,0.06)"/>'
      +'<path d="M22 6 C34 6 36 22 36 36 C36 50 31 56 27 60 L27 80 C27 85 25 88 22 88 C19 88 17 85 17 80 L17 60 C13 56 8 50 8 36 C8 22 10 6 22 6Z" fill="#ffffff" stroke="#0d0d0b" stroke-width="1"/>'
      +'<rect x="17" y="59" width="10" height="5" fill="#c1121f"/>'
      +'<ellipse cx="18" cy="14" rx="4" ry="2.5" fill="rgba(255,255,255,0.5)" transform="rotate(-15 18 14)"/>'
      +'</svg>';
  }

  // Build 10 base pins
  for(var i=0;i<10;i++){
    (function(idx){
      var wrap=document.createElement('div');
      wrap.style.cssText='position:relative;display:flex;align-items:flex-end;justify-content:center;cursor:default;';
      wrap.innerHTML=makePinHTML(1,1);
      ghostsByPin[idx]=[];
      row.appendChild(wrap);

      wrap.addEventListener('mouseenter',function(){startCloning(idx);});
      wrap.addEventListener('mouseleave',function(){stopCloning(idx);});
    })(i);
  }

  function startCloning(idx){
    stopCloning(idx);
    // Immediate first clone
    spawnRowGhost(idx,0);
    var count=0;
    hoverTimers[idx]=setInterval(function(){
      count++;
      spawnRowGhost(idx,count);
      // After ~8s (count>=6) start overflow
      if(count>=6){spawnOverflow(idx);}
    },1200);
  }

  function stopCloning(idx){
    clearInterval(hoverTimers[idx]);
    fadeAll(idx);
  }

  function spawnRowGhost(idx,count){
    var op=Math.max(0.05,0.5-count*0.08);
    var ghost=document.createElement('div');
    ghost.style.cssText='position:absolute;bottom:0;pointer-events:none;transition:opacity 0.6s ease;opacity:'+op+';';
    // Alternate left/right from center
    var side=(count%2===0)?1:-1;
    var dist=(Math.floor(count/2)+1)*(PIN_W+GAP);
    ghost.style.left='calc(50% + '+(side*dist)+'px - '+(PIN_W/2)+'px)';
    ghost.innerHTML=makePinHTML(op,1);
    arena.appendChild(ghost);
    ghostsByPin[idx].push(ghost);
  }

  function spawnOverflow(idx){
    var op=0.04+Math.random()*0.1;
    var ghost=document.createElement('div');
    var x=(Math.random()-0.5)*(arena.offsetWidth*0.85);
    var y=(Math.random()-0.5)*(arena.offsetHeight*0.7);
    ghost.style.cssText='position:absolute;pointer-events:none;transition:opacity 0.6s ease;opacity:'+op+';'
      +'left:calc(50% + '+x+'px - '+(PIN_W*0.75/2)+'px);top:calc(50% + '+y+'px - '+(PIN_H*0.75/2)+'px);';
    ghost.innerHTML=makePinHTML(op,0.75);
    arena.appendChild(ghost);
    ghostsByPin[idx].push(ghost);
  }

  function fadeAll(idx){
    var ghosts=ghostsByPin[idx].slice();
    ghosts.forEach(function(g){g.style.opacity='0';});
    setTimeout(function(){
      ghosts.forEach(function(g){if(g.parentNode)g.parentNode.removeChild(g);});
      ghostsByPin[idx]=[];
    },650);
  }
})();
</script>

<script type="module">
import{initializeApp,getApps}from"https://www.gstatic.com/firebasejs/11.0.0/firebase-app.js";
import{getAuth,onAuthStateChanged,signOut}from"https://www.gstatic.com/firebasejs/11.0.0/firebase-auth.js";
import{getFirestore,doc,setDoc,deleteDoc,getDoc,addDoc,collection,serverTimestamp}from"https://www.gstatic.com/firebasejs/11.0.0/firebase-firestore.js";
const _cfg={"apiKey":"AIzaSyA6_5oWBRKZLnZhTsjtfepm2NleAEEsrPA","authDomain":"domo-8cfe1.firebaseapp.com","projectId":"domo-8cfe1","storageBucket":"domo-8cfe1.appspot.com","messagingSenderId":"123456789","appId":"1:123456789:web:abcdef"};
const _app=getApps().length?getApps()[0]:initializeApp(_cfg);
const _auth=getAuth(_app);
const _db=getFirestore(_app);
let _currentUser=null;
function initNav(u){
  const loginLi=document.getElementById('navLoginLink');
  const avatarLi=document.getElementById('navAvatar');
  if(!loginLi||!avatarLi)return;
  if(u){
    loginLi.style.display='none';avatarLi.style.display='flex';
    const init=(u.displayName||u.email||'?')[0].toUpperCase();
    const el=avatarLi.querySelector('.nav-avatar-initial');
    const nm=avatarLi.querySelector('.nav-avatar-name');
    const em=avatarLi.querySelector('.nav-avatar-email');
    if(el)el.textContent=init;if(nm)nm.textContent=u.displayName||u.email.split('@')[0];if(em)em.textContent=u.email;
  }else{loginLi.style.display='';avatarLi.style.display='none';}
}
onAuthStateChanged(_auth,async u=>{
  _currentUser=u||null;initNav(u);if(!u)return;
  try{await addDoc(collection(_db,'users',u.uid,'pageViews'),{page:"The Pin",slug:"the-pin",timestamp:serverTimestamp()});}catch(e){}
  try{const ws=await getDoc(doc(_db,'users',u.uid,'wishlist','the-pin'));const btn=document.getElementById('wishBtn');if(btn&&ws.exists()){btn.textContent='Held \u2665';btn.style.opacity='0.6';}}catch(e){}
});
window.doSignOut=async()=>{await signOut(_auth);window.location.href='login.html';};
window.toggleWishlist=async()=>{
  const u=_auth.currentUser;const btn=document.getElementById('wishBtn');
  if(!u){window.location.href='login.html';return;}
  try{
    const ref=doc(_db,'users',u.uid,'wishlist','the-pin');const snap=await getDoc(ref);
    if(snap.exists()){await deleteDoc(ref);if(btn){btn.textContent='Hold for Later \u2661';btn.style.opacity='';}}
    else{const p=Object.assign({},PRODUCT);p.savedAt=serverTimestamp();await setDoc(ref,p);if(btn){btn.textContent='Held \u2665';btn.style.opacity='0.6';}}
  }catch(e){}
};
</script>
</body>
</html>'''

content = head + nav_html + body
with open('the-pin.html', 'w', encoding='utf-8') as f:
    f.write(content)

os.remove('_nav_block.txt')
print('Done. the-pin.html:', len(content), 'chars')
