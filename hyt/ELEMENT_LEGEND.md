# TRIBAL TRACES — ELEMENT LEGEND & NAMING KEY

## GLOBAL ELEMENTS (All Pages)

### Navigation Bar
- **`#navbar`** — Main navigation container (fixed, top)
- **`.nav-island`** — Floating pill-shaped navbar wrapper
- **`.nav-brand`** — Logo + wordmark link (left)
- **`.nav-logo`** — SVG Warli sun mark
- **`.nav-wordmark`** — "Tribal Traces" text
- **`.nav-links`** — Center navigation list
- **`.nav-title`** — Individual nav link (Begin, Map, Gallery, About)
- **`.nav-sep`** — Ajrakh diamond separator (◇)
- **`.hamburger`** — 3-dot menu button (right, id="hamburger")

### Hamburger Menu (Popover)
- **`#menu-overlay`** — Full-screen overlay container
- **`.menu-scrim`** — Dark background scrim
- **`.menu-pop`** — Floating menu card
- **`.pop-tail`** — Arrow tail pointing up
- **`.pop-head`** — Menu header
- **`.pop-eyebrow`** — "Menu" label
- **`.pop-sep`** — Diamond separator
- **`.pop-sans`** — Sanskrit text (मार्गः)
- **`.pop-rule`** — Horizontal divider
- **`.pop-list`** — Navigation items wrapper
- **`.pop-item`** — Menu item (Begin, Map, Gallery, About)
- **`.pi-num`** — Roman numeral (I, II, III, IV)
- **`.pi-word`** — English text
- **`.pi-sans`** — Sanskrit text
- **`.pi-arrow`** — Arrow glyph (⟶)
- **`.pop-foot`** — Menu footer
- **`.pf-diamonds`** — Diamond pattern (◇ · ◈ · ◇)
- **`.pf-whisper`** — Sanskrit motto

### Back Button (Pages only)
- **`.back-btn`** — Fixed button, top-left
- Contains rotated back arrow image

### Folio / Location Label (top-right)
- **`.folio`** — Fixed label showing page name + year
- **`.top-loc`** — Alternative name for city pages

### Footer
- **`#site-foot`** — Main footer container
- **`.foot-divider`** — Diamond divider row
- **`.foot-inner`** — Main footer content grid
- **`.foot-col`** — Footer column (brand, explore, threads, connect)
- **`.foot-brand`** — Brand/logo column
- **`.foot-mark`** — Logo link inside brand
- **`.foot-logo`** — SVG Warli mark
- **`.foot-wordmark`** — "TRIBAL TRACES" text
- **`.foot-tag`** — Tagline text ("a calm ode...")
- **`.foot-title`** — Column heading (Explore, Threads, Connect)
- **`.foot-list`** — List of links
- **`.foot-whisper`** — Sanskrit motto (सत्यं शिवं सुन्दरम्)
- **`.foot-bottom`** — Bottom credit line
- **`.foot-bullet`** — Diamond separator between credits

---

## HOMEPAGE (index.html)

### Hero Section
- **`.hero-track`** — Scroll track container (provides 300vh scroll distance)
- **`.hero-stage`** — Sticky stage that stays in view during scroll
- **`#particle-canvas`** — Canvas element for animated constellation
- **`#hero-wordmark`** — Main title "TRIBAL TRACES"
- **`.hero-wordmark-text`** — Title text
- **`.hero-wordmark-sub`** — Subtitle ("tribal's visual notes")
- **`.scroll-cue`** — "Scroll" indicator
- **`.scroll-cue-line`** — Line above label
- **`.scroll-cue-label`** — "scroll" text

### Map Section
- **`.map-section`** — Container (id="map-section")
- **`#map-wrapper`** — SVG map wrapper
- **`#india-map`** — Main SVG element
- **`#india-base`** — Faint India silhouette layer
- **`#india-dots`** — All-India dot field
- **`#gujarat-dots`** — Gujarat interactive dots (glow on hover)
- **`#gujarat-detail`** — Gujarat detail map (hidden until second click)

---

## ABOUT PAGE (about.html)

### Section 1: Intro
- **`.section-intro`** — Full-height intro section
- **`.intro-line`** — Main title ("this is not a collection...")
- **`.intro-text`** — Paragraph(s) below title

### Section 2: The Land
- **`.section-land`** — Wide, airy section
- **`.land-mark`** — Label "First" (marigold color)
- **`.land-title`** — Section heading "The Land"
- **`.land-text`** — Paragraph(s)

### Section 3: The Hand
- **`.section-hand`** — Denser, grounded section (with subtle maroon gradient)
- **`.hand-wrap`** — Two-column grid container
- **`.hand-mark`** — Label "Second" (maroon)
- **`.hand-title`** — Section heading "The Hand"
- **`.hand-text`** — Left column paragraphs
- **`.hand-side`** — Right column paragraphs

### Section 4: The Object (Visual Center)
- **`.section-object`** — Strongest visual moment (with borders & subtle radial gradient)
- **`.object-wrap`** — Grid layout (text + visual)
- **`.object-intro`** — Text column
- **`.object-mark`** — Label "Third" (maroon)
- **`.object-title`** — Section heading "The Object"
- **`.object-text`** — Paragraph(s) with emphasis
- **`.object-visual`** — Right column: visual focal point (3/4 aspect ratio box)
- **`.object-marks`** — Grid of decorative marks (◇ and ◈)
- **`.object-label`** — Label at bottom of visual ("Objects · Preserved")

### Section 5: The Memory
- **`.section-memory`** — Softer, reflective section
- **`.memory-mark`** — Label "Fourth" (ochre)
- **`.memory-title`** — Section heading "The Memory"
- **`.memory-text`** — Paragraph(s)

### Section 6: Final Line
- **`.section-final`** — Closing section (full-width, centered)
- **`.final-marks`** — Diamond pattern above (◇ · ◈ · ◇ · ◈ · ◇)
- **`.final-line`** — Main closing line ("the hand still thinks through the screen.")

---

## GALLERY PAGE (gallery.html)

### Header
- **`.gallery-header`** — Top section with title
- **`.gallery-eyebrow`** — Small label text
- **`.gallery-title`** — Main title ("शिल्पालयः" in both scripts)
- **`.gallery-title-sanskrit`** — Sanskrit script version
- **`.gallery-sub`** — Subtitle

### Museum Room (Main Container)
- **`.museum-room`** — Wall container with gradient & texture
- **`.back-btn`** — Back button (top-left, fixed)

### Gallery Shelves
- **`.shelf`** — Individual shelf container (3 total)
- **`.shelf-id`** — Shelf number label
- **`.shelf-label`** — Shelf description

### Artifact Cards
- **`.artifact-card`** — Individual card container
- **`[data-artifact="..."]`** — Artifact identifier (e.g., "terracotta-horse", "charupot", "painted-terracotta-ware", "sankheda", "silver-jewellery")
- **`.artifact-img-wrap`** — Image/thumbnail wrapper
- **`img`** — Thumbnail image
- **`.artifact-3d`** — Hidden 3D canvas (shown on button click)
- **`[data-glb="..."]`** — GLB file reference (e.g., "horse.glb", "pot.glb", "red2.glb", "jhu.glb", "silver.glb")
- **`.artifact-button`** — View 3D button
- **`.artifact-label`** — Name label below thumbnail
- **`.artifact-meta`** — Meta information

### 3D Viewer
- **`.viewer-modal`** — Modal overlay for 3D model
- **`.viewer-canvas`** — Three.js canvas
- **`.viewer-close`** — Close button
- **`.viewer-controls`** — Help text (mouse/touch instructions)

---

## CITY PAGES (bhuj.html, patan.html, ajrakhpur.html)

### Fixed Navigation
- **`.back-btn`** — Back button (top-left)
- **`.side-arrow.left`** — Previous city button
- **`.side-arrow.right`** — Next city button
- **`.progress-rail`** — Top-center progress indicator with city dots
- **`.rail-dot`** — Individual city dot
- **`.rail-dot.active`** — Active city indicator
- **`.top-loc`** — Location label (top-right)

### Page Content
- **`.hero-title`** — City name heading (uses Nomad Kalari font)
- **`.hero-subtitle`** — Sanskrit name (Tiro Devanagari Sanskrit)
- **`.content-section`** — Main content area
- **`.section-text`** — Text blocks
- **`.section-image`** — Image containers
- **`.parallax-image`** — Image with parallax effect

---

## CSS CUSTOM PROPERTIES (Colors)

### Shared Colors
- **`--parchment`** — #f5f1e8 (warm cream, main background)
- **`--parchment-2`** — #efe7d4 (lighter parchment)
- **`--parchment-3`** — #e6dcc3 (deeper parchment)
- **`--ink`** — #1a1a1a (dark text)
- **`--ink-soft`** — rgba(26,26,26,0.72) (medium text)
- **`--ink-whisper`** — rgba(26,26,26,0.40) (light text)
- **`--maroon`** — #7d2027 (deep red accent)
- **`--maroon-deep`** — #5a1318 (darker maroon)
- **`--marigold`** — #e8a34a (gold/orange accent)
- **`--ochre`** — #b45f26 (earth tone)
- **`--lime-white`** — #ede6d1 (off-white)
- **`--line`** — rgba(26,26,26,0.14) (subtle borders)

### Gallery-Specific Colors
- **`--wall-top`** — #efe4cf (ceiling light)
- **`--wall-mid`** — #e5d6b9 (wall mid)
- **`--wall-low`** — #c8ae8a (wall bottom)
- **`--wood-top`** — #8c6a47 (shelf top)
- **`--wood-face`** — #6b4a2e (shelf front)
- **`--wood-dark`** — #3f2a1a (shelf shadow)
- **`--plinth`** — #ece1cb (light stone)
- **`--gold`** — #b78a3c (brass/brass)

---

## ANIMATIONS

- **`fadeInUp`** — Fade in + slide up (0.2s - 0.5s duration, staggered)
- **`fadeInScale`** — Fade in + scale from 0.95 (1.2s, for object visual)
- **`slideIn`** — Horizontal slide animation
- **`pulse`** — Light opacity pulse

---

## LAYOUT PATTERNS

### Spacing Shortcuts
- **Wide/Airy sections** — padding: 180px 12vw (Land section)
- **Normal padding** — padding: 140px-160px 8vw
- **Mobile** — padding: 120px-140px 24px

### Grid Layouts
- **Two-column** — grid-template-columns: 1fr 1fr (Hand section)
- **Text + Visual** — grid-template-columns: 1fr 1.2fr (Object section)
- **Responsive** — switches to 1fr on mobile

### Decorative Elements
- **Ajrakh diamonds** — ◇ ◈ (alternating pattern)
- **Warli sun** — SVG with 8-point star (navigation logo)
- **Pithora dots** — 3 stacked circles (hamburger menu)

---

## RESPONSIVE BREAKPOINTS

- **Mobile** — max-width: 720px (padding 24px, single column, reduced sizes)
- **Tablet** — max-width: 900px-1000px (grid adjustments)
- **Desktop** — 1200px+ (full layouts)

---

## KEY NOTES

- All pages use **DM Sans** (sans-serif) for body text
- All headings use **Cormorant Garamond** (italic serif)
- City pages use **Nomad Kalari** for main city titles
- Sanskrit text uses **Tiro Devanagari Sanskrit**
- Animations use `opacity: 0` → animation finishes (no visible jump)
- Z-index hierarchy: fixed nav (50-100) > content > backgrounds
- All interactive elements have smooth transitions (0.25s-0.3s)
