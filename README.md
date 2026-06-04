# On Building Fish Eyes for Learning

An interactive explorable about the four learning-theory camps (behaviorist,
cognitive, situated, sociocultural) and the fish-eye lens idea: holding all four
views at once, one in focus while the rest stay visible at the edges.

## Files
- `index.html` — the whole explorable (HTML + CSS + JS in one file)
- `images/` — all artwork referenced by the page (relative paths, e.g. `images/cold-open.jpg`)

## Run it locally
The page uses relative image paths, so it must be served over HTTP (opening the
file directly with `file://` will load the page but may not behave identically).

Easiest options:

**Python (already installed on most machines)**
```bash
cd maya-explorable
python3 -m http.server 8000
# then open http://localhost:8000 in your browser
```

**Node (if you prefer)**
```bash
cd maya-explorable
npx serve .
```

**VS Code / Cursor**
Install the "Live Server" extension, right-click `index.html`, and choose
"Open with Live Server."

**Claude Code**
Just ask it to "serve this folder locally and open it" — it can start a static
server (e.g. `python3 -m http.server`) and hand you the localhost URL.

## Notes for editing
- Everything is in `index.html`. Copy is plain HTML; the fish-eye mechanic and the
  product-sort are vanilla JS near the bottom in a single `<script>` block.
- Reader responses (opening + closing reflections, the checklist picks, and the
  product sort) are collected client-side in `window.fisheyeSession` for later
  data collection — open the browser console and type `fisheyeSession` to inspect.
- To swap art, drop a replacement into `images/` using the same filename; no HTML
  change needed.
