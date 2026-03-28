<<<<<<< HEAD
from __future__ import annotations

from pathlib import Path


CSS_MARKER_START = "/* DOMO INTERACTION REFRESH (auto) */"
CSS_BLOCK = r"""
/* DOMO INTERACTION REFRESH (auto)
   Scope: interaction sections only (ids ending with "Section"), melt slider section, and Handcuff "Buy Freedom" block.
   Behavior untouched; visuals only. */

/* shared tokens */
[id$="Section"], .melt-section, .freedom-wrap{
  --int-radius: 18px;
  --int-radius-sm: 12px;
  --int-shadow: 0 18px 45px rgba(0,0,0,.12);
  --int-shadow-soft: 0 10px 26px rgba(0,0,0,.10);
  --int-ring: 0 0 0 2px rgba(200,168,74,.22);
}

/* buttons */
[id$="Section"] button,
[id$="Section"] a[role="button"],
.melt-section button,
.freedom-wrap a.btn-freedom{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow-soft) !important;
  transform: translateZ(0);
}
[id$="Section"] button:hover,
.melt-section button:hover,
.freedom-wrap a.btn-freedom:hover{
  filter: saturate(1.05);
}
[id$="Section"] button:focus,
[id$="Section"] textarea:focus,
[id$="Section"] input:focus,
.melt-section input:focus,
.melt-section button:focus,
.freedom-wrap a.btn-freedom:focus{
  outline: none !important;
  box-shadow: var(--int-shadow-soft), var(--int-ring) !important;
}

/* text inputs */
[id$="Section"] textarea,
[id$="Section"] input{
  border-radius: var(--int-radius-sm) !important;
}

/* panels (common ids used across pages: riverPanel, slotPanel, screamPanel, etc.) */
[id$="Section"] [id$="Panel"]{
  border-radius: var(--int-radius-sm) !important;
}

/* coin options (Grey Piggy Bank) */
#coinSection .coin-opt{
  border-radius: 16px !important;
  width: 86px !important;
  height: 86px !important;
  background: linear-gradient(160deg, rgba(255,255,255,.95), rgba(235,235,235,.92) 55%, rgba(210,210,210,.92)) !important;
  border-color: rgba(10,10,10,.18) !important;
}
#coinSection .coin-opt:hover{
  border-color: rgba(10,10,10,.55) !important;
}
#coinSection #slotTarget{
  border-radius: 7px !important;
}

/* paper boat textarea (Paper Boat) */
#riverSection textarea#boatMsg{
  font-size: 13px !important;
}
#riverSection #riverCanvas{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
}

/* scream button (Silence After Scream) */
#screamSection button{
  box-shadow: 0 18px 45px rgba(0,0,0,.35) !important;
}

/* melt slider (Melting Skull) */
.melt-section input[type="range"]{
  accent-color: #c8a84a;
}

/* Buy Freedom (Handcuff) */
.freedom-wrap{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
  overflow: hidden;
}
"""


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


def inject_css(html: str) -> tuple[str, bool]:
    if CSS_MARKER_START in html:
        return html, False
    idx = html.lower().rfind("</style>")
    if idx == -1:
        return html, False
    insert_at = idx
    out = html[:insert_at] + "\n" + CSS_BLOCK.strip() + "\n" + html[insert_at:]
    return out, True


def main() -> None:
    root = Path(__file__).resolve().parent
    changed = 0
    skipped = 0
    for rel in TARGET_FILES:
        p = root / rel
        if not p.exists():
            skipped += 1
            continue
        html = p.read_text(encoding="utf-8", errors="ignore")
        new_html, did = inject_css(html)
        if did:
            p.write_text(new_html, encoding="utf-8", errors="ignore")
            changed += 1
    print(f"updated_files {changed}")
    print(f"missing_files {skipped}")


if __name__ == "__main__":
    main()

=======
from __future__ import annotations

from pathlib import Path


CSS_MARKER_START = "/* DOMO INTERACTION REFRESH (auto) */"
CSS_BLOCK = r"""
/* DOMO INTERACTION REFRESH (auto)
   Scope: interaction sections only (ids ending with "Section"), melt slider section, and Handcuff "Buy Freedom" block.
   Behavior untouched; visuals only. */

/* shared tokens */
[id$="Section"], .melt-section, .freedom-wrap{
  --int-radius: 18px;
  --int-radius-sm: 12px;
  --int-shadow: 0 18px 45px rgba(0,0,0,.12);
  --int-shadow-soft: 0 10px 26px rgba(0,0,0,.10);
  --int-ring: 0 0 0 2px rgba(200,168,74,.22);
}

/* buttons */
[id$="Section"] button,
[id$="Section"] a[role="button"],
.melt-section button,
.freedom-wrap a.btn-freedom{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow-soft) !important;
  transform: translateZ(0);
}
[id$="Section"] button:hover,
.melt-section button:hover,
.freedom-wrap a.btn-freedom:hover{
  filter: saturate(1.05);
}
[id$="Section"] button:focus,
[id$="Section"] textarea:focus,
[id$="Section"] input:focus,
.melt-section input:focus,
.melt-section button:focus,
.freedom-wrap a.btn-freedom:focus{
  outline: none !important;
  box-shadow: var(--int-shadow-soft), var(--int-ring) !important;
}

/* text inputs */
[id$="Section"] textarea,
[id$="Section"] input{
  border-radius: var(--int-radius-sm) !important;
}

/* panels (common ids used across pages: riverPanel, slotPanel, screamPanel, etc.) */
[id$="Section"] [id$="Panel"]{
  border-radius: var(--int-radius-sm) !important;
}

/* coin options (Grey Piggy Bank) */
#coinSection .coin-opt{
  border-radius: 16px !important;
  width: 86px !important;
  height: 86px !important;
  background: linear-gradient(160deg, rgba(255,255,255,.95), rgba(235,235,235,.92) 55%, rgba(210,210,210,.92)) !important;
  border-color: rgba(10,10,10,.18) !important;
}
#coinSection .coin-opt:hover{
  border-color: rgba(10,10,10,.55) !important;
}
#coinSection #slotTarget{
  border-radius: 7px !important;
}

/* paper boat textarea (Paper Boat) */
#riverSection textarea#boatMsg{
  font-size: 13px !important;
}
#riverSection #riverCanvas{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
}

/* scream button (Silence After Scream) */
#screamSection button{
  box-shadow: 0 18px 45px rgba(0,0,0,.35) !important;
}

/* melt slider (Melting Skull) */
.melt-section input[type="range"]{
  accent-color: #c8a84a;
}

/* Buy Freedom (Handcuff) */
.freedom-wrap{
  border-radius: var(--int-radius) !important;
  box-shadow: var(--int-shadow) !important;
  overflow: hidden;
}
"""


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


def inject_css(html: str) -> tuple[str, bool]:
    if CSS_MARKER_START in html:
        return html, False
    idx = html.lower().rfind("</style>")
    if idx == -1:
        return html, False
    insert_at = idx
    out = html[:insert_at] + "\n" + CSS_BLOCK.strip() + "\n" + html[insert_at:]
    return out, True


def main() -> None:
    root = Path(__file__).resolve().parent
    changed = 0
    skipped = 0
    for rel in TARGET_FILES:
        p = root / rel
        if not p.exists():
            skipped += 1
            continue
        html = p.read_text(encoding="utf-8", errors="ignore")
        new_html, did = inject_css(html)
        if did:
            p.write_text(new_html, encoding="utf-8", errors="ignore")
            changed += 1
    print(f"updated_files {changed}")
    print(f"missing_files {skipped}")


if __name__ == "__main__":
    main()

>>>>>>> 95e01d88ba3d7be6026253c45543c09ddb4e0b3f
