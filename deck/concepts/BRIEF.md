# Concept round 1 brief (shared by all five lane designers)

Client: Visit Salt Lake (VSL). Creative director: Yid. Read first: brand/vsl/BRAND-DIGEST.md, research/merch/04-destination-merch-and-slc-symbol-bank.md, deck/moodboards/<lane>/captions.md, deck/moodboards/MARKS.md (design ONLY from the IN items of your lane; treat OUT items as banned directions).

Hard rules
- No Olympic rings, no "Olympic," no "2034," no Ski Utah, no "Greatest Snow on Earth," no Utah state flag, no VSL logo in the artwork (a small salt-crystal line icon may appear as a label mark).
- "Utah" and "Salt Lake" are fine. The DMO says "Salt Lake," not "Salt Lake City."
- No invented taglines. Phrases must come from the scene, the place, or the community, or be plain statements.
- If you could buy it at the airport, it's wrong. Nothing basic. No logo-on-a-blank.
- Brand palette by hex from BRAND-DIGEST.md; you may add black, white, and one off-palette hit per piece if the lane demands it (xerox pink, lift green, arena orange).

Deliverable per piece (three pieces per lane)
1. An SVG artwork file at deck/concepts/<lane>/<NN>-<slug>.svg, 1200 x 1500 viewBox, showing the garment or object as a clean flat technical illustration (front and back where relevant, or the object) WITH the graphic applied, all text as real vector text (use web-safe or Google fonts by name in font-family with fallbacks; text must be legible). Draw the garment simply: silhouette outline, fabric fill in the garment color, seams as thin lines. The graphic is the point. Include a small spec strip at the bottom: blank, fabric weight, decoration technique, colorway, placement sizes in inches.
2. A matching entry in deck/concepts/<lane>/NOTES.md: name, the IN references it draws from (file names), the idea in two sentences, why this garment and fabric, technique and why, what a local would say about it, and one risk.

Make real design decisions: type choices, scale, placement, color. Hand-lettering can be approximated with a display font plus notes that a letterer would redraw it. Keep the SVGs self-contained (no external images). Validate each SVG parses (python3 -c "import xml.dom.minidom,sys;xml.dom.minidom.parse(sys.argv[1])" file).
