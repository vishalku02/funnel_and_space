# Build Handoff — "What is education for?"

A precise plan for building the explorable. Hand this to the implementation chat together with `maya-explorable-script.md` (the content + visual bible). This document is the *how to build*; the script is the *what it is*.

---

## 0. Read first / how to use this

- **Attach two files to the new chat:** `maya-explorable-script.md` (script + visual bible) and `tree-rings-anatomy.svg` (concept-art layout guide). `tree-rings-two-views.svg` is an earlier rough, optional.
- **Do not re-derive the concept.** The thinking is settled and lives in the script. The build job is to realize it, not to reopen it.
- **Build in the order below.** It goes roughest-to-finest on purpose. The first milestone tests the only thing that can sink the project; everything after is craft.

---

## 1. The stack (decided — don't substitute)

- **Plain HTML + CSS** for all nine screens and the spine.
- **HTML `<canvas>`** for the doodle only.
- **Inline SVG** for the diagrams (M1 rings, M8 tree) and the rings→tree transition.
- **No three.js. No 3D assets. No framework needed.** Vanilla JS is enough; a tiny build tool (Vite) is fine if convenient.

**Why no 3D:** the aesthetic is warm paper, hand-drawn, picture-book. A rendered 3D tree would look imported from another universe and kill the intimacy the piece runs on. The rings→tree "rotation" reads better as a 2D morph (dissolve + slight perspective skew, shared center and proportion) than as real 3D. The recognition — "it was a tree all along" — comes from the rings and tree sharing center and size, not from genuine rotation.

---

## 2. Build order (milestones with "done when")

### M0 — The spine gray-box  *(the go/no-go; build this first)*
All nine screens, real on-screen text from the script, plain HTML/CSS, system fonts fine, **no art and no animation** beyond a basic fade. Placeholder boxes labeled "RINGS", "TREE", "BOARD".
- Wire the five text captures, the four support checkboxes, and the consent flag into one in-memory state object (no backend yet).
- Screen 7 ("Your words") renders the three Maya-need answers stacked, labeled by moment.
- **Done when:** you can play start to finish and your three answers appear stacked at the end.
- **Then test it on a few people before building anything pretty.** The whole piece rests on one question: *do the three answers actually drift?* If they move, the piece works and the rest is polish. If they don't, no art will save it — and you found out in a day.

### M1 — The doodle canvas
Small freehand canvas on Screen 2. One graphite stroke weight. No color picker, no tools, no undo-clutter, no "what is this?" labeling. Skip → horse fallback.
- Stored as the player's asset; **never sent to analysis.**
- Reappears **untouched** in a fixed margin slot on every later screen and on the final board.
- **Done when:** draw → it persists in the margin → appears untouched on the board; skip → the horse appears instead.

### M2 — The two palettes + the cold screen (M3)
Apply the warm and cold palettes and the type rules from the script's "Global world" section.
- Build M3 as the cold tutoring dashboard: pure CSS, monospace, the exact table from the script, **hard cut in** (no fade), edge-to-edge cold.
- The line `Off-task events ... 14 flagged` is present and **never explained.**
- **Done when:** the temperature change is felt in the body; M3 reads as competent software, not a strawman, and there is no warm pixel on it.

### M3 — Concept art: rings, tree, and the tip
- Static cold rings on Screen 1 (M1). Static labeled tree on Screen 8 (hand-drawn or recolored SVG; `tree-rings-anatomy.svg` is the layout guide).
- The tip (M8): 2D morph from rings to tree, sharing center and proportion, slow and continuous, with a slight perspective skew. Soil grows in at the base, canopy opens at the top, one fruit falls.
- Only the words **"soil, air, light"** are spoken. All other anatomy labels are faint/optional (hover or low-opacity pencil), never narration.
- **Done when:** the transition reads as the *same object* turning, and a test player says some version of "oh — it was a tree the whole time."

### M4 — Board, margins, sound, final polish
- The bulletin-board ending: concept art + the untouched doodle + the final "What is education for?" field + a smaller credit/consent card in the corner. Feeling first, logistics underneath.
- Place the margin glints (Biesta, Holmes, Edelman) as faint pencil notes; optional, never in the main column.
- Add sound last: pensive and sparse (Zelda/Avatar reference), warm everywhere **except** M3, which thins to near-silence.
- **Done when:** end-to-end feels finished and the close lands on warmth, not housekeeping.

---

## 3. Data capture spec

Capture only with the up-front consent (Screen 0). Anonymous. Five free-text answers per session:

| # | Screen | Prompt | Note |
|---|---|---|---|
| 1 | M1 | What is education for? | opening, most distal |
| 2 | M2 | What does Maya need right now? | proximal |
| 3 | M4 | What does Maya need right now? | proximal |
| 4 | M6 | What does Maya need right now? | proximal |
| 5 | M9 | What is education for? | closing, distal again |

Plus: profession (**store as a coarse category**, not free text, to avoid re-identifying rare titles), the set of support checkboxes ticked (optional, keep out of the way), an anonymous session id, and a timestamp.

- **The doodle is never in the analysis export.** Store it separately as a display asset only.
- **Storage for a class project:** a simple anonymous POST to a Supabase table or a Google Sheet endpoint is plenty. Keep it server-side or in a private sheet; don't put responses in client-visible storage.
- The three proximal points plus the two distal bookends are the trajectory across **levels of distal-ness** — the thing being studied in Stat 292.

---

## 4. Guardrails (easy to break without the backstory — do not violate)

These are the load-bearing design invariants. A fresh agent will be tempted by each; hold the line.

1. **The M4 support menu has no human-contact option.** Every checkbox is a system feature; none is "sit with her" or "be her friend." The menu's incompleteness *is* the argument. Adding a warm option collapses the piece.
2. **M3 is never narrated.** No caption telling the player it's cold. No "the system sees her differently." The color and type carry it. The `14 off-task events flagged` line stays buried and unexplained.
3. **The doodle is untouched and unanalyzed.** Never recolored, animated, classified, or fed to the NLP. It is the one input the system refuses to read — that refusal is the point.
4. **Only "soil, air, light" is spoken aloud.** The piece stays silent and lets the player articulate the rest. The fuller tree labels are studyable art, not narration.
5. **The overlays (ITS / classroom / CoP shapes) are an optional side path,** never on the resting card and never on the spine. Cataloguing the shapes is not the same as feeling what Maya needs.
6. **Voice: window, not stage.** On-screen text is plain, simple, honest. No em dashes. No performed lyricism — the situation, art, and music carry the feeling. Keep "it's unfortunate, because" where it appears; it reads as a person noticing.
7. **The opening rings must not look alive.** No green, no leaves at M1, or the M8 reveal dies.
8. **Don't punish the non-drifter.** A player whose three answers barely move still gets the neutral stacked reveal; drift is never framed as the "correct" outcome.

---

## 5. Asset guidance (the tree)

In order of effort-to-payoff:

1. **Draw it yourself** (recommended). A slightly imperfect hand-drawn tree is *on-thesis* — the unmeasured human mark, same family as the doodle. Procreate, or ink on paper photographed and traced. Use `tree-rings-anatomy.svg` as the layout; make it warm and loose.
2. **Recolor an open SVG.** For a clean vector tree: openclipart.org (public domain), svgrepo.com (filter to CC0/public-domain), undraw.co (free, recolorable, slightly corporate style). Recolor to soil-green / leaf-tan / fruit-red. Verify the license before shipping.
3. **AI-generate the static M8 card only.** Since M8 is a held image, a warm storybook/watercolor tree generated as a *picture* (not a 3D asset) is a fine use. Generate the card, not an interactive object.

Do **not** chase sketch-to-3D tools or photoreal tree models; wrong register, high effort, will fight the aesthetic.

---

## 6. Before public launch (parallel track)

Email the Educ 432 / Stat 292 course staff this week for the **IRB determination** (most likely an exemption) before any version collects a real answer. Sort it alongside M0. To the statistician you'd like as a recommender, having this handled reads as thinking like a researcher.

---

## 7. Ready-to-paste kickoff message for the new chat

> Hi! I'm building an explorable explanation called "What is education for?" with my collaborator. The full script and visual bible is attached (`maya-explorable-script.md`), along with a concept-art guide (`tree-rings-anatomy.svg`) and a build plan (`maya-build-handoff.md`). Please read the build plan first, then the script. The concept is settled — I want to build it, not reopen it.
>
> Start with **Milestone M0: the spine gray-box** from the build plan — all nine screens with the real on-screen text, plain HTML/CSS, no art, placeholder boxes for the visuals, the five text captures and four checkboxes wired into a simple state object, and the Screen 7 "Your words" stack reveal working. I want to play it end to end and test whether the three answers drift, before we build anything pretty.
>
> One hard rule for any on-screen text you write or adjust: plain and simple, no em dashes, no performed poetry — match the voice of these two screens I wrote:
>
> *Meet Maya. She's ten. She's a really hard worker. For three weeks she's been working through the same page in her homework on fractions. She gets the first step right almost every time. But then she stops at the same place each time, just before the end. It's unfortunate, because lately in class she's stopped raising her hand. In the corner of every worksheet, she draws.*
>
> *Maya uses a tutoring app at school. It watches how she does and changes the lessons to fit her. What support would you give her? [checkboxes] Maya sits next to four of her friends in class. It's unfortunate, because lately she hasn't really talked to any of them. What does Maya need right now?*
>
> Build M0, show me the running gray-box, and we'll test it before moving on.

---

*Companion files: `maya-explorable-script.md` (script + visual bible), `tree-rings-anatomy.svg` (labeled concept art), `tree-rings-two-views.svg` (early rough). Voice rule throughout: window, not stage.*
