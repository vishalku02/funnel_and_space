# funnel_and_space

Two explorable explanations on learning, made for Educ 432 (Explorable Explanations) and Stat 292 (Statistical Models of Language and Text) at Stanford, by Vishal and Yoyo.

## The pieces

- **`index.html` — *What is education for?*** (the Maya piece). A picture-book explorable: you sit with one ten-year-old as the same question is asked from far away and up close, and watch your own answer drift. Ends on a tree that was a set of cold rings all along.
- **`lenses.html` — *Four Lenses on Learning*.** An interactive piece on the four perspectives in learning science (Behaviorist, Cognitive, Situated/Distributed, Socio-cultural) as different lenses on the same situation. Cursor-as-lens scene, a pattern map, a positionality beat, and a design-bench.

Both are single self-contained HTML files. Open either directly in a browser, or serve the folder:

```sh
python3 -m http.server 4321
# then open http://localhost:4321/index.html  or  /lenses.html
```

## Companion documents

- `maya-explorable-script.md` — the Maya piece's content + visual bible (reconciled with the build).
- `maya-build-handoff.md` — the Maya piece's build plan and as-built status.
- `lenses-explorable-outline.md` — the Four Lenses design outline and as-built status.
- `tree-rings-anatomy.svg`, `tree-rings-two-views.svg` — concept art for the rings↔tree model.

## Status

Both explorables are built and playable. Responses are captured in-memory only (no backend yet); an anonymous save and the IRB determination are required before any public release that collects real answers. Voice rule throughout: *window, not stage.*
