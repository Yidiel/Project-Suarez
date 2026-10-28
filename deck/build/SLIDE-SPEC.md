# Slide content spec

Write slides as a JSON array in a file. Each slide is one object:

{
  "n": 6,                        // slide number from OUTLINE.md
  "layout": "...",               // one of the layouts below
  "title": "...",                // the headline, a plain sentence or short phrase. No label above it.
  "body": "...",                 // 1 to 3 short sentences. Optional.
  "points": ["...", "..."],      // optional, 2 to 5 items, each one sentence, can start with a **bold** lead
  "images": [{"src": "moodboards/web/<lane>/<file>.jpg", "caption": "..."}],  // optional; only files that exist under deck/moodboards/web/
  "table": {"head": ["..",".."], "rows": [["..",".."]]},   // optional
  "quote": {"text": "...", "who": "..."},                  // optional
  "big": "...",                  // optional, a single number or short line set huge
  "sources": ["Short source name, year"],                  // optional, small footnote list
  "notes": "..."                 // speaker notes, 2 to 5 sentences: the thought process behind the slide
}

Layouts:
- "section": part opener. title + body only.
- "statement": one big line (title), optional body.
- "text-image": title, body or points on one side, 1 image on the other.
- "grid": title, short body, 3 to 6 images with captions.
- "table": title, short body, a table.
- "quote": a quote with attribution, title optional.
- "points": title plus 3 to 6 points, no image.
- "big": title, a huge number or line in "big", body explains it.

Writing rules: plain casual sentences, no em dashes, no eyebrows, no hype words. Every claim must come from the research files; mark anything unverified with "(verify)". Prices and numbers from research only. Do not name Park City. Do not use Olympic marks; Salt Lake 2002 history is fine as history.
