<<<<<<< HEAD
from __future__ import annotations

import re
from pathlib import Path


MARKER = "DOMO INTERACTION REFRESH (auto)"

NEW_BLOCK = r"""
/* DOMO INTERACTION REFRESH (auto) v2
   Scope: interaction sections only (ids ending with "Section"), melt slider section, and Handcuff "Buy Freedom" block.
   Behavior untouched; visuals only. */

/* shared tokens */
[id$="Section"], .melt-section, .freedom-wrap{
  --int-ink: #0a0a0a;
  --int-paper: #fbfaf7;
  --int-paper-2: #f4f1e8;
  --int-accent: #c8a84a;
  --int-accent-2: #7b6cff;
  --int-radius: 18px;
  --int-radius-sm: 12px;
  --int-shadow: 0 22px 60px rgba(0,0,0,.16);
  --int-shadow-soft: 0 10px 26px rgba(0,0,0,.12);
  --int-ring: 0 0 0 2px rgba(200,168,74,.28), 0 0 0 6px rgba(200,168,74,.10);
}

/* make the interaction itself look like a “module” */
[id$="Section"], .melt-section{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
  overflow: hidden;
}

/* subtle texture so it’s visibly different */
[id$="Section"]::before,
.melt-section::before{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    radial-gradient(900px 260px at 18% 18%, rgba(200,168,74,.18), transparent 60%),
    radial-gradient(700px 240px at 85% 22%, rgba(123,108,255,.10), transparent 55%),
    linear-gradient(180deg, rgba(255,255,255,.10), transparent 40%);
  mix-blend-mode:multiply;
  opacity:.85;
}

/* keep content above the overlay */
[id$="Section"] > * ,
.melt-section > *{
  position:relative;
  z-index:1;
}

/* panels: “glass card” */
[id$="Section"] [id$="Panel"],
[id$="Section"] [style*="border:3px solid"],
[id$="Section"] [style*="border: 3px solid"]{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow-soft) !important;
}

/* buttons: more graphical + obvious */
[id$="Section"] button,
.melt-section button,
.freedom-wrap a.btn-freedom{
  border-radius: 999px !important;
  box-shadow: 0 18px 45px rgba(0,0,0,.18) !important;
  transform: translateZ(0);
  position:relative;
  overflow:hidden;
}
[id$="Section"] button::after,
.melt-section button::after,
.freedom-wrap a.btn-freedom::after{
  content:"";
  position:absolute;
  inset:-2px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.22), transparent);
  transform: translateX(-120%);
  transition: transform .55s ease;
  pointer-events:none;
}
[id$="Section"] button:hover::after,
.melt-section button:hover::after,
.freedom-wrap a.btn-freedom:hover::after{
  transform: translateX(120%);
}
[id$="Section"] button:focus,
[id$="Section"] textarea:focus,
[id$="Section"] input:focus,
.melt-section input:focus,
.melt-section button:focus,
.freedom-wrap a.btn-freedom:focus{
  outline: none !important;
  box-shadow: 0 18px 45px rgba(0,0,0,.18), var(--int-ring) !important;
}

/* text inputs */
[id$="Section"] textarea,
[id$="Section"] input{
  border-radius: var(--int-radius-sm) !important;
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.06) !important;
}

/* Grey Piggy Bank: make coins look like “cards” not circles */
#coinSection .coin-opt{
  width: 108px !important;
  height: 78px !important;
  border-radius: 16px !important;
  background:
    radial-gradient(90px 55px at 20% 20%, rgba(255,255,255,.92), rgba(255,255,255,0) 60%),
    linear-gradient(160deg, rgba(255,255,255,.92), rgba(235,235,235,.90) 50%, rgba(210,210,210,.92)) !important;
  border: 1px solid rgba(10,10,10,.18) !important;
}
#coinSection .coin-opt:hover{
  transform: translateY(-6px) scale(1.03) !important;
  border-color: rgba(10,10,10,.55) !important;
}
#coinSection #slotTarget{
  border-radius: 9px !important;
  box-shadow: 0 10px 26px rgba(0,0,0,.22) !important;
}

/* Paper Boat: river should feel “premium” */
#riverSection #riverCanvas{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
}

/* Scream: stronger presence */
#screamSection button{
  box-shadow: 0 22px 60px rgba(0,0,0,.40) !important;
}

/* Melt slider */
.melt-section input[type="range"]{
  accent-color: var(--int-accent);
}

/* Handcuff: Buy Freedom block becomes an obvious interaction module */
.freedom-wrap{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
}
""".strip()


TARGET_FILES = [
    "another-brick-in-the-wall.html",
    "blue-toilet.html",
    "bowling-pin.html",
    "crocodile.html",
    "division-bell.html",
    "grey-piggy-bank.html",
    "handcuff.html",
    "key.html",
    "melting-skull.html",
    "moai.html",
    "octopus.html",
    "paper-boat.html",
    "raven-skull.html",
    "red-blood-cell.html",
    "silence-after-scream.html",
    "sun.html",
]


def upgrade_one(path: Path) -> bool:
    html = path.read_text(encoding="utf-8", errors="ignore")
    i = html.find(MARKER)
    if i == -1:
        return False
    style_close = html.lower().find("</style>", i)
    if style_close == -1:
        return False
    # Replace everything from the start of the comment to </style>
    # Find the start of the comment block containing the marker.
    comment_start = html.rfind("/*", 0, i)
    if comment_start == -1:
        comment_start = i
    new_html = html[:comment_start] + NEW_BLOCK + "\n</style>" + html[style_close + len("</style>") :]
    if new_html != html:
        path.write_text(new_html, encoding="utf-8", errors="ignore")
        return True
    return False


def main() -> None:
    root = Path(__file__).resolve().parent
    updated = 0
    for rel in TARGET_FILES:
        if upgrade_one(root / rel):
            updated += 1
    # also update domo2 copies if present
    domo2 = root / "domo2"
    if domo2.exists():
        for rel in TARGET_FILES:
            p = domo2 / rel
            if p.exists() and upgrade_one(p):
                updated += 1
    print(f"updated_files {updated}")


if __name__ == "__main__":
    main()

=======
from __future__ import annotations

import re
from pathlib import Path


MARKER = "DOMO INTERACTION REFRESH (auto)"

NEW_BLOCK = r"""
/* DOMO INTERACTION REFRESH (auto) v2
   Scope: interaction sections only (ids ending with "Section"), melt slider section, and Handcuff "Buy Freedom" block.
   Behavior untouched; visuals only. */

/* shared tokens */
[id$="Section"], .melt-section, .freedom-wrap{
  --int-ink: #0a0a0a;
  --int-paper: #fbfaf7;
  --int-paper-2: #f4f1e8;
  --int-accent: #c8a84a;
  --int-accent-2: #7b6cff;
  --int-radius: 18px;
  --int-radius-sm: 12px;
  --int-shadow: 0 22px 60px rgba(0,0,0,.16);
  --int-shadow-soft: 0 10px 26px rgba(0,0,0,.12);
  --int-ring: 0 0 0 2px rgba(200,168,74,.28), 0 0 0 6px rgba(200,168,74,.10);
}

/* make the interaction itself look like a “module” */
[id$="Section"], .melt-section{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
  overflow: hidden;
}

/* subtle texture so it’s visibly different */
[id$="Section"]::before,
.melt-section::before{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    radial-gradient(900px 260px at 18% 18%, rgba(200,168,74,.18), transparent 60%),
    radial-gradient(700px 240px at 85% 22%, rgba(123,108,255,.10), transparent 55%),
    linear-gradient(180deg, rgba(255,255,255,.10), transparent 40%);
  mix-blend-mode:multiply;
  opacity:.85;
}

/* keep content above the overlay */
[id$="Section"] > * ,
.melt-section > *{
  position:relative;
  z-index:1;
}

/* panels: “glass card” */
[id$="Section"] [id$="Panel"],
[id$="Section"] [style*="border:3px solid"],
[id$="Section"] [style*="border: 3px solid"]{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow-soft) !important;
}

/* buttons: more graphical + obvious */
[id$="Section"] button,
.melt-section button,
.freedom-wrap a.btn-freedom{
  border-radius: 999px !important;
  box-shadow: 0 18px 45px rgba(0,0,0,.18) !important;
  transform: translateZ(0);
  position:relative;
  overflow:hidden;
}
[id$="Section"] button::after,
.melt-section button::after,
.freedom-wrap a.btn-freedom::after{
  content:"";
  position:absolute;
  inset:-2px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.22), transparent);
  transform: translateX(-120%);
  transition: transform .55s ease;
  pointer-events:none;
}
[id$="Section"] button:hover::after,
.melt-section button:hover::after,
.freedom-wrap a.btn-freedom:hover::after{
  transform: translateX(120%);
}
[id$="Section"] button:focus,
[id$="Section"] textarea:focus,
[id$="Section"] input:focus,
.melt-section input:focus,
.melt-section button:focus,
.freedom-wrap a.btn-freedom:focus{
  outline: none !important;
  box-shadow: 0 18px 45px rgba(0,0,0,.18), var(--int-ring) !important;
}

/* text inputs */
[id$="Section"] textarea,
[id$="Section"] input{
  border-radius: var(--int-radius-sm) !important;
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.06) !important;
}

/* Grey Piggy Bank: make coins look like “cards” not circles */
#coinSection .coin-opt{
  width: 108px !important;
  height: 78px !important;
  border-radius: 16px !important;
  background:
    radial-gradient(90px 55px at 20% 20%, rgba(255,255,255,.92), rgba(255,255,255,0) 60%),
    linear-gradient(160deg, rgba(255,255,255,.92), rgba(235,235,235,.90) 50%, rgba(210,210,210,.92)) !important;
  border: 1px solid rgba(10,10,10,.18) !important;
}
#coinSection .coin-opt:hover{
  transform: translateY(-6px) scale(1.03) !important;
  border-color: rgba(10,10,10,.55) !important;
}
#coinSection #slotTarget{
  border-radius: 9px !important;
  box-shadow: 0 10px 26px rgba(0,0,0,.22) !important;
}

/* Paper Boat: river should feel “premium” */
#riverSection #riverCanvas{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
}

/* Scream: stronger presence */
#screamSection button{
  box-shadow: 0 22px 60px rgba(0,0,0,.40) !important;
}

/* Melt slider */
.melt-section input[type="range"]{
  accent-color: var(--int-accent);
}

/* Handcuff: Buy Freedom block becomes an obvious interaction module */
.freedom-wrap{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
}
""".strip()


TARGET_FILES = [
    "another-brick-in-the-wall.html",
    "blue-toilet.html",
    "bowling-pin.html",
    "crocodile.html",
    "division-bell.html",
    "grey-piggy-bank.html",
    "handcuff.html",
    "key.html",
    "melting-skull.html",
    "moai.html",
    "octopus.html",
    "paper-boat.html",
    "raven-skull.html",
    "red-blood-cell.html",
    "silence-after-scream.html",
    "sun.html",
]


def upgrade_one(path: Path) -> bool:
    html = path.read_text(encoding="utf-8", errors="ignore")
    i = html.find(MARKER)
    if i == -1:
        return False
    style_close = html.lower().find("</style>", i)
    if style_close == -1:
        return False
    # Replace everything from the start of the comment to </style>
    # Find the start of the comment block containing the marker.
    comment_start = html.rfind("/*", 0, i)
    if comment_start == -1:
        comment_start = i
    new_html = html[:comment_start] + NEW_BLOCK + "\n</style>" + html[style_close + len("</style>") :]
    if new_html != html:
        path.write_text(new_html, encoding="utf-8", errors="ignore")
        return True
    return False


def main() -> None:
    root = Path(__file__).resolve().parent
    updated = 0
    for rel in TARGET_FILES:
        if upgrade_one(root / rel):
            updated += 1
    # also update domo2 copies if present
    domo2 = root / "domo2"
    if domo2.exists():
        for rel in TARGET_FILES:
            p = domo2 / rel
            if p.exists() and upgrade_one(p):
                updated += 1
    print(f"updated_files {updated}")


if __name__ == "__main__":
    main()

>>>>>>> 95e01d88ba3d7be6026253c45543c09ddb4e0b3f
